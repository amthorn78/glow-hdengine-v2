# PF07 redlines, revision r2 — gtwpe-20261101-pf10-v14-0-5 — T-18

## Package identity

| Field | Value |
| :---- | :---- |
| Redlines file | `PF07-Canon-Glow-Infrastructure-v2.3.4.redlines.gtwpe-20261101-pf10-v14-0-5.r2.md` |
| Proof log | `PF07-Canon-Glow-Infrastructure-v2.3.4.redlines.gtwpe-20261101-pf10-v14-0-5.r2.proof-log.md`, in the same directory |
| Run identity | `gtwpe-20261101-pf10-v14-0-5/T-18/drain-r2` |
| Supersedes | Package `drain-r1`, `PF07-Canon-Glow-Infrastructure-v2.3.4.redlines.gtwpe-20261101-pf10-v14-0-5.md` at commit `19a92a9`. Its RL-01 to RL-04 are carried here byte-identical; RL-05 to RL-43 are new. |
| Preparer | TW-DRAIN-10 100926.1 (Notion page `3f44590a05eb8172a314fe6b958bb9ff`, fetched live again at the start of this revision), run in the Claude Code document session Nathan started for T-18 on 2026-11-02 |
| Authorization for RL-05 to RL-43 | Nathan, 2026-11-02, in this session, after the drain-r1 and apply-r1 report: "you can fix the defects and discrepancies you noticed". The defects are observations O-1 to O-9 in the drain-r1 proof log §8. |
| Preparation outcome | `READY`; save state recorded in the proof log |
| Ledger | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/LEDGER.md` at `a3632c0`; task T-18 (§8); rows C-02, C-03, C-17, C-18, C-26, and C-01 added by Nathan's direction for O-1 |
| Target (original) | `docs/pfcanon/PF07-Canon-Glow-Infrastructure-v2.3.4.md`, title `PF07-Canon-Glow-Infrastructure`, v2.3.4, git blob `60fd3f0b3feff007491dc7add29a9c4491cbdf95`, SHA-256 `9e00712a3af2c1b498b5dddf5ada35c72b44952293d3b73ec3915cbba586d790`, 99,393 bytes, 1,443 LF characters (1,444 lines; the last line has no final LF), unchanged from `e2b7427ff418ca8f08f05587c4a541308a76da56` to `origin/main` `84d6d1cad95c67788336d174dc4b8922d9bb0cb2` |
| Source | `docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md`, v14.0.5, git blob `9df074d90b59fe783c32f7cb3db25872d5dfe9d2`, SHA-256 `cea605d0475889bd9120a51947e23176ce7d2308eb5ab4503b040fd68ddf669d`; addendum 2.1 D-1 (l.225–276, added for O-1), D-2 (l.277–344), D-3 (l.345–396) and context (l.205–224, l.491–516); 2.8 (l.1048–1145); 2.15 (l.1650–1868) |
| Simulated one-pass result | SHA-256 `642c5c1aff0a4c671120f58b82c3a68a400a311851d250ab6d5dbe35b7ea098a`, 101,233 bytes, 1,446 LF characters (scratch only; Apply produces the final file) |

## Literal and operation conventions

- Every operation is `REPLACE` against the unchanged original target. No operation reads another operation's output.
- Each OLD and NEW literal is the exact text between its opening and closing four-backtick fence lines. The newline that ends the last literal line, just before the closing fence, is not part of the literal. Every other newline and every space inside the fence is part of it, including leading spaces and trailing double spaces.
- Each OLD literal is one or more complete original lines, without the newline that ends its last line. That newline stays in place after the replacement. Its expected occurrence count is over the whole original target.
- Section paths quote the original heading lines exactly, including two-space indents where the original has them and the U+2011 non-breaking hyphen in the §2.5 heading; RL-02 to RL-04 also quote the bold label that opens their block. For a redline whose OLD is itself a heading line, the path ends at that heading's parent. Paths locate the edit; the OLD literal's unique occurrence is the binding locator.
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

## RL-05

- Ledger rows: C-17 (CRD root form); Nathan-authorized fix
- Observation fixed: O-6 (drain-r1 proof log §8)
- Source basis: PF03 §3 "Structure and language" (no ellipsis); PF10 2.8 decision 3, l.1068; Nathan's direction, 2026-11-02, in this session: "you can fix the defects and discrepancies you noticed"
- Change type: DOC_HYGIENE
- Operation: REPLACE
- Target document: PF07-Canon-Glow-Infrastructure
- Section path: "# **0\. Front Matter**"
- Original line(s): 23 (informative)
- Expected OLD occurrences in the whole original: 1
- Rationale: Replaces the ellipsis in the §0 example with the root forms, and adds the CRD root that RL-03 and RL-04 record.

OLD:

````
* Canonical root paths for governed evidence and QA trees (for example, `audit/qa/<epic-id>/...`).
````

NEW:

````
* Canonical root paths for governed evidence and QA trees (for example, `audit/qa/<epic-id>/` and `audit/qa/<crd-id>/`).
````

## RL-06

- Ledger rows: None; Nathan-authorized fix
- Observation fixed: O-9 (drain-r1 proof log §8)
- Source basis: PF06 in-document title `PF06-Canon-Change-Process-Guide`; PF03 §3 "Canonical ownership" (route by exact in-document title); Nathan's direction, 2026-11-02, in this session: "you can fix the defects and discrepancies you noticed"
- Change type: CONSISTENCY
- Operation: REPLACE
- Target document: PF07-Canon-Glow-Infrastructure
- Section path: "# **0\. Front Matter**"
- Original line(s): 42 (informative)
- Expected OLD occurrences in the whole original: 1
- Rationale: PF06's title is Change-Process-Guide; Epic-Process-Guide names no current document.

OLD:

````
* **Process & PR workflow** (PR-first; human index \+ machine mirror updated in the same PR) → **Epic-Process-Guide** (titles-only).
````

NEW:

````
* **Process & PR workflow** (PR-first; human index \+ machine mirror updated in the same PR) → **Change-Process-Guide** (titles-only).
````

## RL-07

- Ledger rows: None; Nathan-authorized fix
- Observation fixed: O-9 (drain-r1 proof log §8)
- Source basis: As RL-06
- Change type: CONSISTENCY
- Operation: REPLACE
- Target document: PF07-Canon-Glow-Infrastructure
- Section path: "# **0\. Front Matter**"
- Original line(s): 87 (informative)
- Expected OLD occurrences in the whole original: 1
- Rationale: As RL-06.

OLD:

````
* **PF06 — Epic-Process-Guide**  
````

NEW:

````
* **PF06 — Change-Process-Guide**  
````

## RL-08

- Ledger rows: C-17 (CRD root form); Nathan-authorized fix
- Observation fixed: O-6 (drain-r1 proof log §8)
- Source basis: As RL-05
- Change type: DOC_HYGIENE
- Operation: REPLACE
- Target document: PF07-Canon-Glow-Infrastructure
- Section path: "# **1\) Purpose & boundaries**"
- Original line(s): 108 (informative)
- Expected OLD occurrences in the whole original: 1
- Rationale: As RL-05, in §1.

OLD:

````
* Canonical key names and high-level locations for infra configuration (for example, `DEV_SAMPLER_URL`, `DATABASE_URL`, canonical QA roots such as `audit/qa/<epic-id>/...`).
````

NEW:

````
* Canonical key names and high-level locations for infra configuration (for example, `DEV_SAMPLER_URL`, `DATABASE_URL`, canonical QA roots such as `audit/qa/<epic-id>/` and `audit/qa/<crd-id>/`).
````

## RL-09

- Ledger rows: None; Nathan-authorized fix
- Observation fixed: O-9 (drain-r1 proof log §8)
- Source basis: As RL-06
- Change type: CONSISTENCY
- Operation: REPLACE
- Target document: PF07-Canon-Glow-Infrastructure
- Section path: "# **1\) Purpose & boundaries**"
- Original line(s): 135 (informative)
- Expected OLD occurrences in the whole original: 1
- Rationale: As RL-06.

OLD:

````
* **PF06 — Epic-Process-Guide** (process and change control)
````

NEW:

````
* **PF06 — Change-Process-Guide** (process and change control)
````

## RL-10

- Ledger rows: None; Nathan-authorized fix
- Observation fixed: O-3 (drain-r1 proof log §8)
- Source basis: PF07 §10.5 (l.1438: evidence families and artifact paths are owned by HDE-Schemas & Artifacts); Nathan's direction, 2026-11-02, in this session: "you can fix the defects and discrepancies you noticed"
- Change type: CONSISTENCY
- Operation: REPLACE
- Target document: PF07-Canon-Glow-Infrastructure
- Section path: "# 2\) Environments overview" > "## **2.3 Routing (titles-only)**" > "### **2.3.3 Ops-only identity**"
- Original line(s): 215 (informative)
- Expected OLD occurrences in the whole original: 1
- Rationale: §10.5 records no /internal/version evidence bundle; it routes evidence families and paths to HDE-Schemas & Artifacts. The pointer now says so.

OLD:

````
`/internal/version` is **operator-only** and **not A7-eligible**. Its transport posture (cache behavior, validator/HEAD handling, and conditional semantics) is defined by title in the owning governance/contract documents. PF07 records only the infra fact that this surface is ops-only and where its governed evidence bundle lives (see §10.5).
````

NEW:

````
`/internal/version` is **operator-only** and **not A7-eligible**. Its transport posture (cache behavior, validator/HEAD handling, and conditional semantics) is defined by title in the owning governance/contract documents. PF07 records only the infra fact that this surface is ops-only. Its governed evidence families and paths are owned by **HDE-Schemas & Artifacts** (§10.5).
````

## RL-11

- Ledger rows: None; Nathan-authorized fix
- Observation fixed: O-6 (drain-r1 proof log §8)
- Source basis: PF03 §3 (no ellipsis) and §13 (obvious placeholders for secrets); PF07's own `{redacted}` form (l.1269-1271); Nathan's direction, 2026-11-02, in this session: "you can fix the defects and discrepancies you noticed"
- Change type: DOC_HYGIENE
- Operation: REPLACE
- Target document: PF07-Canon-Glow-Infrastructure
- Section path: "# 2\) Environments overview" > "## **2.3 Routing (titles-only)**" > "### **2.3.3 Ops-only identity**"
- Original line(s): 220 (informative)
- Expected OLD occurrences in the whole original: 1
- Rationale: Replaces the U+2026 ellipsis with PF07's own redaction form.

OLD:

````
If a run uses an auth header (for example, `Authorization: Bearer …`), it is **optional until canonized** and MUST be treated as **Observed Evidence** only. Runbooks/plans that include an auth header MUST state the header’s source as a concrete input (presence-only; never the value) or they risk creating a false “ops gap” blocker.
````

NEW:

````
If a run uses an auth header (for example, `Authorization: Bearer {redacted}`), it is **optional until canonized** and MUST be treated as **Observed Evidence** only. Runbooks/plans that include an auth header MUST state the header’s source as a concrete input (presence-only; never the value) or they risk creating a false “ops gap” blocker.
````

## RL-12

- Ledger rows: None; Nathan-authorized fix
- Observation fixed: O-3 (drain-r1 proof log §8)
- Source basis: As RL-10; PF07 §5.1 directory naming (l.729)
- Change type: CONSISTENCY
- Operation: REPLACE
- Target document: PF07-Canon-Glow-Infrastructure
- Section path: "# 2\) Environments overview" > "## **2.3 Routing (titles-only)**" > "### **2.3.3 Ops-only identity**"
- Original line(s): 228 (informative)
- Expected OLD occurrences in the whole original: 1
- Rationale: §10.5 lists no Ops or QA audit roots. The pointer now names where PF07 records the QA roots and where other roots are owned.

OLD:

````
Store the captured evidence in-repo under a lowercase audit path (see the Ops/QA audit roots in §10.5).
````

NEW:

````
Store the captured evidence in-repo under a lowercase `audit/` path. PF07 records the QA evidence root patterns (§2.8, §8.1); other governed evidence roots and paths are owned by **HDE-Schemas & Artifacts** (§10.5).
````

## RL-13

- Ledger rows: None; Nathan-authorized fix
- Observation fixed: O-5 (drain-r1 proof log §8)
- Source basis: PF03 §7 "Revision and retention rules" (formatting repair of indentation and malformed Markdown) and §8 (preserve heading hierarchy); Nathan's direction, 2026-11-02, in this session: "you can fix the defects and discrepancies you noticed"
- Change type: DOC_HYGIENE
- Operation: REPLACE
- Target document: PF07-Canon-Glow-Infrastructure
- Section path: "# 2\) Environments overview" > "## **2.4 Env Deployment Inventory \[Required-Now\]**"
- Original line(s): 294 (informative)
- Expected OLD occurrences in the whole original: 1
- Rationale: The two-space indent after a list item makes this heading part of the list item instead of a heading of §2.4. Removing it restores the heading.

OLD:

````
  ### **Development — OpenAI Codex**
````

NEW:

````
### **Development — OpenAI Codex**
````

## RL-14

- Ledger rows: None; Nathan-authorized fix
- Observation fixed: O-5 (drain-r1 proof log §8)
- Source basis: As RL-13
- Change type: DOC_HYGIENE
- Operation: REPLACE
- Target document: PF07-Canon-Glow-Infrastructure
- Section path: "# 2\) Environments overview" > "## **2.4 Env Deployment Inventory \[Required-Now\]**"
- Original line(s): 320 (informative)
- Expected OLD occurrences in the whole original: 1
- Rationale: As RL-13.

OLD:

````
  ### **QA — GitHub Codespaces**
````

NEW:

````
### **QA — GitHub Codespaces**
````

## RL-15

- Ledger rows: None; Nathan-authorized fix
- Observation fixed: O-4 (drain-r1 proof log §8)
- Source basis: PF07 §7.0 (l.930) and §8.1 (l.1144-1150): retired bridge keys have no active mapping and their values are never recorded; Nathan's direction, 2026-11-02, in this session: "you can fix the defects and discrepancies you noticed"
- Change type: CONSISTENCY
- Operation: REPLACE
- Target document: PF07-Canon-Glow-Infrastructure
- Section path: "# 2\) Environments overview" > "## **2.4 Env Deployment Inventory \[Required-Now\]**" > "  ### **QA — GitHub Codespaces**"
- Original line(s): 328 (informative)
- Expected OLD occurrences in the whole original: 1
- Rationale: §2.4 recorded a value for a retired key that §7.0 and §8.1 say has no active mapping and whose value is never reported. The line now records the key's retired posture, in the form l.336 uses for `HDAPI_BASE_URL`.

OLD:

````
* `DB_BRIDGE_URL=https://illustrious-freedom-production.up.railway.app`  
````

NEW:

````
* `DB_BRIDGE_URL` — retired HDE database-transport key with no active PF07 mapping (§7.0, §8.1). If it is present, it is configuration drift: report the key name only, never its value.  
````

## RL-16

- Ledger rows: None; Nathan-authorized fix
- Observation fixed: O-5 (drain-r1 proof log §8)
- Source basis: As RL-13
- Change type: DOC_HYGIENE
- Operation: REPLACE
- Target document: PF07-Canon-Glow-Infrastructure
- Section path: "# 2\) Environments overview" > "## **2.4 Env Deployment Inventory \[Required-Now\]**"
- Original line(s): 348 (informative)
- Expected OLD occurrences in the whole original: 1
- Rationale: As RL-13. RL-01 (l.352) does not touch this line.

OLD:

````
  ### **Key-spelling and downgrade rules**
````

NEW:

````
### **Key-spelling and downgrade rules**
````

## RL-17

- Ledger rows: C-17 (CRD root form); Nathan-authorized fix
- Observation fixed: O-6 (drain-r1 proof log §8)
- Source basis: As RL-05
- Change type: DOC_HYGIENE
- Operation: REPLACE
- Target document: PF07-Canon-Glow-Infrastructure
- Section path: "# 2\) Environments overview" > "## **2.6 Prod on Railway, QA via Codespaces (names-only)**"
- Original line(s): 459 (informative)
- Expected OLD occurrences in the whole original: 1
- Rationale: As RL-05, in §2.6.

OLD:

````
* “Codespaces” is treated as a **console and artifact sink**: a place to store and inspect QA evidence under `audit/qa/<epic-id>/...` and to run offline checks against those artifacts.
````

NEW:

````
* “Codespaces” is treated as a **console and artifact sink**: a place to store and inspect QA evidence under the change's QA evidence root (`audit/qa/<epic-id>/` or `audit/qa/<crd-id>/`) and to run offline checks against those artifacts.
````

## RL-18

- Ledger rows: None; Nathan-authorized fix
- Observation fixed: O-9 (drain-r1 proof log §8)
- Source basis: As RL-06
- Change type: CONSISTENCY
- Operation: REPLACE
- Target document: PF07-Canon-Glow-Infrastructure
- Section path: "# 2\) Environments overview" > "## **2.6 Prod on Railway, QA via Codespaces (names-only)**"
- Original line(s): 461 (informative)
- Expected OLD occurrences in the whole original: 1
- Rationale: As RL-06.

OLD:

````
PF07 does **not** decide where behavior tests that satisfy D-goals are executed; those decisions (for example, which admin terminal or GUI exercises compat, narratives, vendor, or admin bundle behavior) are specified in **Epic-Process-Guide** and **Glow QA Guide** by title. PF07 names only the providers, projects, services, repositories, and canonical QA evidence roots that those documents rely on.
````

NEW:

````
PF07 does **not** decide where behavior tests that satisfy D-goals are executed; those decisions (for example, which admin terminal or GUI exercises compat, narratives, vendor, or admin bundle behavior) are specified in **Change-Process-Guide** and **Glow QA Guide** by title. PF07 names only the providers, projects, services, repositories, and canonical QA evidence roots that those documents rely on.
````

## RL-19

- Ledger rows: None; Nathan-authorized fix
- Observation fixed: O-9 (drain-r1 proof log §8)
- Source basis: As RL-06
- Change type: CONSISTENCY
- Operation: REPLACE
- Target document: PF07-Canon-Glow-Infrastructure
- Section path: "# 2\) Environments overview" > "## **2.7 Terminal CLI access as admin surface (names-only, pre-Glow)**"
- Original line(s): 507 (informative)
- Expected OLD occurrences in the whole original: 1
- Rationale: The informal home list names PF06 by its current title.

OLD:

````
* Current PF07 posture remains names-only: PF07 records the target names, key names, roots, and evidence locations. Command behavior, route bytes, adapter semantics, provider behavior, QA predicates, OPS execution rules, token semantics, and PF09 status remain owned by the HDE CLI/API, Mechanics, Governance, QA, Schemas and Artifacts, Epic Process, and Build Checklist homes by title.  
````

NEW:

````
* Current PF07 posture remains names-only: PF07 records the target names, key names, roots, and evidence locations. Command behavior, route bytes, adapter semantics, provider behavior, QA predicates, OPS execution rules, token semantics, and PF09 status remain owned by the HDE CLI/API, Mechanics, Governance, QA, Schemas and Artifacts, Change Process, and Build Checklist homes by title.  
````

## RL-20

- Ledger rows: None; Nathan-authorized fix
- Observation fixed: O-5 (drain-r1 proof log §8)
- Source basis: As RL-13
- Change type: DOC_HYGIENE
- Operation: REPLACE
- Target document: PF07-Canon-Glow-Infrastructure
- Section path: "# 3\) Provider inventory (names-only)" > "## **3.1 Railway**"
- Original line(s): 597-599 (informative)
- Expected OLD occurrences in the whole original: 1
- Rationale: l.597 is a sentence marked as a heading inside a bullet; it becomes a plain bullet. The indent on l.599 makes "3.2 Vercel" part of that list item; removing it restores the §3.2 heading. l.598 is unchanged.

OLD:

````
* ## PF07 does **not** define how connectivity tests are run or which D-goals or QA tokens they satisfy; it records only the provider, project, service, base-URL, and instance names that those tests and tokens depend on.

  ## **3.2 Vercel**
````

NEW:

````
* PF07 does **not** define how connectivity tests are run or which D-goals or QA tokens they satisfy; it records only the provider, project, service, base-URL, and instance names that those tests and tokens depend on.

## **3.2 Vercel**
````

## RL-21

- Ledger rows: C-26 (2.15 R-1 deployed check); Nathan-authorized fix
- Observation fixed: O-2 (drain-r1 proof log §8)
- Source basis: PF10 2.15 R-1, l.1719 (the production Reader, for each Reader version); supporting: HDE-CLI-API-Vendor-Ref (PF05 l.2202, l.2420), adapter/http_reader.py l.380, docs/ENDPOINTS_CATALOG.json; Nathan's direction, 2026-11-02, in this session: "you can fix the defects and discrepancies you noticed"
- Change type: CONSISTENCY
- Operation: REPLACE
- Target document: PF07-Canon-Glow-Infrastructure
- Section path: "# **4\) Component maps**" > "## **4.1 HD Engine**"
- Original line(s): 648 (informative)
- Expected OLD occurrences in the whole original: 1
- Rationale: R-1's deployed-service check scores the production Reader for each Reader version. PF07 recorded only Reader v1. The production blueprint serves both, and the route contract stays with HDE-CLI-API-Vendor-Ref; the rest of the line is unchanged.

OLD:

````
  * **Reader v1 route posture (names-only):** The canonical production target is `POST /api/reader?v=1`. The checked-in `GET /reader?v=1` file-path surface remains development-only and non-authoritative; when the Reader blueprint is mounted under `/api`, `/api/reader` is the mounted form rather than a separate contract. There is no `/api/reader-proof/v1` route and it MUST NOT be referenced. The Endpoint Catalog remains internal-only and env-gated, and catalog-driven proofs use the cataloged success route for the configured mount. Route bytes, request/response shapes, projection, A7 policy, and invariants live in **HDE-CLI-API-Vendor-Ref** and **HDE-Governance**.  
````

NEW:

````
  * **Reader route posture (names-only):** The canonical production targets are `POST /api/reader?v=1` (Reader v1) and `POST /api/reader?v=2` (Reader v2). The checked-in `GET /reader?v=1` file-path surface remains development-only and non-authoritative; when the Reader blueprint is mounted under `/api`, `/api/reader` is the mounted form rather than a separate contract. There is no `/api/reader-proof/v1` route and it MUST NOT be referenced. The Endpoint Catalog remains internal-only and env-gated, and catalog-driven proofs use the cataloged success route for the configured mount. Route bytes, request/response shapes, projection, A7 policy, and invariants live in **HDE-CLI-API-Vendor-Ref** and **HDE-Governance**.  
````

## RL-22

- Ledger rows: C-17 (CRD root form); Nathan-authorized fix
- Observation fixed: O-6 (drain-r1 proof log §8)
- Source basis: As RL-05
- Change type: DOC_HYGIENE
- Operation: REPLACE
- Target document: PF07-Canon-Glow-Infrastructure
- Section path: "# **5\) Repositories**" > "## **5.1 HD Engine repo**"
- Original line(s): 723 (informative)
- Expected OLD occurrences in the whole original: 1
- Rationale: As RL-05, in §5.1.

OLD:

````
* `audit/` — QA and audit logs, including trees rooted at `audit/qa/<epic-id>/...` referenced by title in QA guides.
````

NEW:

````
* `audit/` — QA and audit logs, including QA trees rooted at `audit/qa/<epic-id>/` and `audit/qa/<crd-id>/` referenced by title in QA guides.
````

## RL-23

- Ledger rows: None; Nathan-authorized fix
- Observation fixed: O-9 (drain-r1 proof log §8)
- Source basis: PF05 in-document title `PF05-Canon-HDE-CLI-API-Vendor-Ref`; PF03 §3 (one term consistently); Nathan's direction, 2026-11-02, in this session: "you can fix the defects and discrepancies you noticed"
- Change type: CONSISTENCY
- Operation: REPLACE
- Target document: PF07-Canon-Glow-Infrastructure
- Section path: "# **5\) Repositories**" > "## **5.1 HD Engine repo**"
- Original line(s): 725 (informative)
- Expected OLD occurrences in the whole original: 1
- Rationale: The only variant spelling of PF05's title in PF07; every other mention uses HDE-CLI-API-Vendor-Ref.

OLD:

````
PF07 records this repo structure as an infra inventory only. Transport behavior, governance, QA policy, schemas, and evidence acceptance are routed by title to their owning PF documents (for example, **HDE-Governance**, **HDE-CLI API Vendor Ref**, **HDE-Schemas & Artifacts**, **Glow QA Guide**, **HDE-Mechanics Guide**).
````

NEW:

````
PF07 records this repo structure as an infra inventory only. Transport behavior, governance, QA policy, schemas, and evidence acceptance are routed by title to their owning PF documents (for example, **HDE-Governance**, **HDE-CLI-API-Vendor-Ref**, **HDE-Schemas & Artifacts**, **Glow QA Guide**, **HDE-Mechanics Guide**).
````

## RL-24

- Ledger rows: C-17 (CRD root form); Nathan-authorized fix
- Observation fixed: O-6 (drain-r1 proof log §8)
- Source basis: As RL-05
- Change type: DOC_HYGIENE
- Operation: REPLACE
- Target document: PF07-Canon-Glow-Infrastructure
- Section path: "# **5\) Repositories**" > "## **5.1 HD Engine repo**"
- Original line(s): 731 (informative)
- Expected OLD occurrences in the whole original: 1
- Rationale: As RL-05, in §5.1 directory naming.

OLD:

````
This applies to all governed roots listed above (for example, `docs/`, `artifacts/`, `audit/`, `catalog/`, `schemas/`, and per-epic QA trees under `audit/qa/<epic-id>/...`).
````

NEW:

````
This applies to all governed roots listed above (for example, `docs/`, `artifacts/`, `audit/`, `catalog/`, `schemas/`, and per-change QA trees under `audit/qa/<epic-id>/` and `audit/qa/<crd-id>/`).
````

## RL-25

- Ledger rows: None; Nathan-authorized fix
- Observation fixed: O-5 (drain-r1 proof log §8)
- Source basis: As RL-13
- Change type: DOC_HYGIENE
- Operation: REPLACE
- Target document: PF07-Canon-Glow-Infrastructure
- Section path: "# **5\) Repositories**" > "## **5.1 HD Engine repo**"
- Original line(s): 785 (informative)
- Expected OLD occurrences in the whole original: 1
- Rationale: As RL-13.

OLD:

````
  ### **5.1.5 EPIC-019 D6 vendor Live QA harness (names-only)**
````

NEW:

````
### **5.1.5 EPIC-019 D6 vendor Live QA harness (names-only)**
````

## RL-26

- Ledger rows: None; Nathan-authorized fix
- Observation fixed: O-5 (drain-r1 proof log §8)
- Source basis: As RL-13
- Change type: DOC_HYGIENE
- Operation: REPLACE
- Target document: PF07-Canon-Glow-Infrastructure
- Section path: "# **5\) Repositories**" > "## **5.1 HD Engine repo**"
- Original line(s): 808 (informative)
- Expected OLD occurrences in the whole original: 1
- Rationale: As RL-13.

OLD:

````
  ### **5.1.6 EPIC-019 D3 sampler QA harnesses & remedial docs (names-only)**
````

NEW:

````
### **5.1.6 EPIC-019 D3 sampler QA harnesses & remedial docs (names-only)**
````

## RL-27

- Ledger rows: C-26 (2.15 R-3)
- Observation fixed: O-7 (drain-r1 proof log §8)
- Source basis: PF10 2.15 R-3, l.1755-1759 (Live QA is reserved for QA that ran the live test; other QA is closed-rails QA); Nathan's direction, 2026-11-02, in this session: "you can fix the defects and discrepancies you noticed"
- Change type: CONSISTENCY
- Operation: REPLACE
- Target document: PF07-Canon-Glow-Infrastructure
- Section path: "# **5\) Repositories**" > "## **5.1 HD Engine repo**" > "  ### **5.1.6 EPIC-019 D3 sampler QA harnesses & remedial docs (names-only)**"
- Original line(s): 816 (informative)
- Expected OLD occurrences in the whole original: 1
- Rationale: The text called a harness that runs under closed rails a Live QA harness. The file path is a real name and stays.

OLD:

````
  Dev-only sampler Live QA harness for EPIC-019 D3. Exercises `DEV_SAMPLER_URL` and related APP\_ENV permutations under closed rails, writing governed logs under the EPIC019 sampler QA evidence root. Classification semantics and token bindings (for example, ENV rails tokens) are owned by **Glow QA Guide**, **HDE-Governance**, and **HDE-Phased Epics**.  
````

NEW:

````
  Dev-only closed-rails sampler QA harness for EPIC-019 D3. Its file name keeps the historical "live" label, but its runs are closed-rails QA, not Live QA. It exercises `DEV_SAMPLER_URL` and related APP\_ENV permutations under closed rails, writing governed logs under the EPIC019 sampler QA evidence root. Classification semantics and token bindings (for example, ENV rails tokens) are owned by **Glow QA Guide**, **HDE-Governance**, and **HDE-Phased Epics**.  
````

## RL-28

- Ledger rows: C-26 (2.15 R-3)
- Observation fixed: O-7 (drain-r1 proof log §8)
- Source basis: As RL-27
- Change type: CONSISTENCY
- Operation: REPLACE
- Target document: PF07-Canon-Glow-Infrastructure
- Section path: "# **5\) Repositories**" > "## **5.1 HD Engine repo**" > "  ### **5.1.6 EPIC-019 D3 sampler QA harnesses & remedial docs (names-only)**"
- Original line(s): 819 (informative)
- Expected OLD occurrences in the whole original: 1
- Rationale: As RL-27; the same line already says the logs were produced under closed rails.

OLD:

````
  QA evidence root for EPIC-019 sampler QA (healthcheck and Live QA). Contains governed logs produced by the sampler QA harnesses for D3 under closed rails. Artifact schemas, indexing rules, and Machine Mirror records live in **HDE-Schemas & Artifacts**; QA usage and sample runs live in **Glow QA Guide**.  
````

NEW:

````
  QA evidence root for EPIC-019 sampler QA (healthcheck and closed-rails sampler QA). Contains governed logs produced by the sampler QA harnesses for D3 under closed rails. Artifact schemas, indexing rules, and Machine Mirror records live in **HDE-Schemas & Artifacts**; QA usage and sample runs live in **Glow QA Guide**.  
````

## RL-29

- Ledger rows: None; Nathan-authorized fix
- Observation fixed: O-5 (drain-r1 proof log §8)
- Source basis: As RL-13
- Change type: DOC_HYGIENE
- Operation: REPLACE
- Target document: PF07-Canon-Glow-Infrastructure
- Section path: "# **5\) Repositories**" > "## **5.2 Glow Backend repo**"
- Original line(s): 846 (informative)
- Expected OLD occurrences in the whole original: 1
- Rationale: A list item marked as a heading; it becomes a plain nested bullet like the Railway project line above it.

OLD:

````
  * ## **Railway service:** `glow-backend-v4`
````

NEW:

````
  * **Railway service:** `glow-backend-v4`
````

## RL-30

- Ledger rows: None; Nathan-authorized fix
- Observation fixed: O-5 (drain-r1 proof log §8)
- Source basis: As RL-13
- Change type: DOC_HYGIENE
- Operation: REPLACE
- Target document: PF07-Canon-Glow-Infrastructure
- Section path: "# 6\) Domains & DNS (names-only)"
- Original line(s): 905 (informative)
- Expected OLD occurrences in the whole original: 1
- Rationale: As RL-13.

OLD:

````
  ## **6.5 Routing (titles-only)**
````

NEW:

````
## **6.5 Routing (titles-only)**
````

## RL-31

- Ledger rows: None; Nathan-authorized fix
- Observation fixed: O-5 (drain-r1 proof log §8)
- Source basis: As RL-13
- Change type: DOC_HYGIENE
- Operation: REPLACE
- Target document: PF07-Canon-Glow-Infrastructure
- Section path: "# **7\) Databases & Schemas \[Required-Now\]**"
- Original line(s): 986 (informative)
- Expected OLD occurrences in the whole original: 1
- Rationale: As RL-13.

OLD:

````
  ## **7.2 Application schema map (per application)**
````

NEW:

````
## **7.2 Application schema map (per application)**
````

## RL-32

- Ledger rows: None; Nathan-authorized fix
- Observation fixed: O-5 (drain-r1 proof log §8)
- Source basis: As RL-13
- Change type: DOC_HYGIENE
- Operation: REPLACE
- Target document: PF07-Canon-Glow-Infrastructure
- Section path: "# **7\) Databases & Schemas \[Required-Now\]**" > "  ## **7.2 Application schema map (per application)**"
- Original line(s): 1009 (informative)
- Expected OLD occurrences in the whole original: 1
- Rationale: As RL-13.

OLD:

````
  ### **7.2.2 Backend schema — TBD \[Speculative\]**
````

NEW:

````
### **7.2.2 Backend schema — TBD \[Speculative\]**
````

## RL-33

- Ledger rows: None; Nathan-authorized fix
- Observation fixed: O-5 (drain-r1 proof log §8)
- Source basis: As RL-13
- Change type: DOC_HYGIENE
- Operation: REPLACE
- Target document: PF07-Canon-Glow-Infrastructure
- Section path: "# **8\) Config keys & references (names \+ current values)**" > "## **8.1 Shared keys**"
- Original line(s): 1179 (informative)
- Expected OLD occurrences in the whole original: 1
- Rationale: A list item marked as a heading; it becomes a plain bullet like the Connection binding note above it.

OLD:

````
* ## **Historical evidence:** `artifacts/runtime/env_connectivity.snapshot.json` is retained as a governed bridge-era record only. It is not a current fallback requirement or evidence target.
````

NEW:

````
* **Historical evidence:** `artifacts/runtime/env_connectivity.snapshot.json` is retained as a governed bridge-era record only. It is not a current fallback requirement or evidence target.
````

## RL-34

- Ledger rows: None; Nathan-authorized fix
- Observation fixed: O-5 (drain-r1 proof log §8)
- Source basis: As RL-13
- Change type: DOC_HYGIENE
- Operation: REPLACE
- Target document: PF07-Canon-Glow-Infrastructure
- Section path: "# **8\) Config keys & references (names \+ current values)**"
- Original line(s): 1198-1200 (informative)
- Expected OLD occurrences in the whole original: 1
- Rationale: As RL-13, for the §8.2 and §8.2.1 headings; l.1199 is unchanged.

OLD:

````
  ## **8.2 Component-specific keys**

  ### **8.2.1 HD Engine**
````

NEW:

````
## **8.2 Component-specific keys**

### **8.2.1 HD Engine**
````

## RL-35

- Ledger rows: None; Nathan-authorized fix
- Observation fixed: O-6 (drain-r1 proof log §8)
- Source basis: PF03 §3 (no ellipsis; `<PLACEHOLDER_NAME>` is the explicit form); Nathan's direction, 2026-11-02, in this session: "you can fix the defects and discrepancies you noticed"
- Change type: DOC_HYGIENE
- Operation: REPLACE
- Target document: PF07-Canon-Glow-Infrastructure
- Section path: "# **8\) Config keys & references (names \+ current values)**" > "  ## **8.2 Component-specific keys**" > "  ### **8.2.1 HD Engine**"
- Original line(s): 1239 (informative)
- Expected OLD occurrences in the whole original: 1
- Rationale: Replaces the ellipsis in the example command with an explicit placeholder, as PF07 already does with `<base_url>` (l.1227).

OLD:

````
* Shell-level `export DEV_SAMPLER_URL=...` MAY be used for one-off debugging, but the devcontainer environment is the **authoritative infra binding** for this environment.
````

NEW:

````
* Shell-level `export DEV_SAMPLER_URL=<url>` MAY be used for one-off debugging, but the devcontainer environment is the **authoritative infra binding** for this environment.
````

## RL-36

- Ledger rows: C-26 (2.15 R-3)
- Observation fixed: O-7 (drain-r1 proof log §8)
- Source basis: As RL-27
- Change type: CONSISTENCY
- Operation: REPLACE
- Target document: PF07-Canon-Glow-Infrastructure
- Section path: "# **8\) Config keys & references (names \+ current values)**" > "  ## **8.2 Component-specific keys**" > "  ### **8.2.1 HD Engine**"
- Original line(s): 1243 (informative)
- Expected OLD occurrences in the whole original: 1
- Rationale: As RL-27.

OLD:

````
* Dev sampler HTTP QA tools in this repo (for example, healthcheck and D3 Live QA harnesses) are expected to **read DEV\_SAMPLER\_URL from the environment** and treat it as a required input; they MUST NOT hardcode host/port or recompute `<base_url>` internally.  
````

NEW:

````
* Dev sampler HTTP QA tools in this repo (for example, the healthcheck and D3 closed-rails sampler QA harnesses) are expected to **read DEV\_SAMPLER\_URL from the environment** and treat it as a required input; they MUST NOT hardcode host/port or recompute `<base_url>` internally.  
````

## RL-37

- Ledger rows: C-01 (2.1 D-1), added to T-18 by Nathan's direction
- Observation fixed: O-1 (drain-r1 proof log §8)
- Source basis: PF10 2.1 D-1, l.229-241 (the override covers bg:resolve, showcompat and vendor-selecting conjunction; audit command values); l.506 (item 9 open); code at main: engine/bodygraph/vendor_audit.py l.140 and engine/cli/main.py l.53; Nathan's direction, 2026-11-02, in this session: "you can fix the defects and discrepancies you noticed"
- Change type: CONSISTENCY
- Operation: REPLACE
- Target document: PF07-Canon-Glow-Infrastructure
- Section path: "# **8\) Config keys & references (names \+ current values)**" > "  ## **8.2 Component-specific keys**" > "  ### **8.2.1 HD Engine**"
- Original line(s): 1278 (informative)
- Expected OLD occurrences in the whole original: 1
- Rationale: D-1 extends the override, and its audit events, to showcompat and conjunction, but the implementing change is open. The key now names the sink by the override, routes command coverage to its owner, and states the checked-in code's single writer as a code fact, so it stays true when item 9 delivers.

OLD:

````
* **Key.** Names the local file to which `hdctl bg:resolve --source vendor` appends its production vendor-override audit events. The value is a filesystem path, not a secret. Per-environment bindings are **OPEN/TBD**.  
````

NEW:

````
* **Key.** Names the local file to which the production vendor override appends its audit events. **HDE-CLI-API-Vendor-Ref** owns which commands the override covers; in the checked-in code, only `hdctl bg:resolve --source vendor` writes these events. The value is a filesystem path, not a secret. Per-environment bindings are **OPEN/TBD**.  
````

## RL-38

- Ledger rows: None; Nathan-authorized fix
- Observation fixed: O-6 (drain-r1 proof log §8)
- Source basis: PF03 §3 (no ellipsis); Nathan's direction, 2026-11-02, in this session: "you can fix the defects and discrepancies you noticed"
- Change type: DOC_HYGIENE
- Operation: REPLACE
- Target document: PF07-Canon-Glow-Infrastructure
- Section path: "# **9\) Resource catalog (IDs & links)**" > "## **9.2 Services**" > "### **9.2.1 Object storage (narratives pack store)**"
- Original line(s): 1336 (informative)
- Expected OLD occurrences in the whole original: 1
- Rationale: Replaces the ellipsis with the prefix form; the pattern is unchanged.

OLD:

````
• **Bucket / prefix:** TBD (immutable path pattern `/narratives/<pack_sha>/...`)  
````

NEW:

````
• **Bucket / prefix:** TBD (immutable path prefix `/narratives/<pack_sha>/`)  
````

## RL-39

- Ledger rows: None; Nathan-authorized fix
- Observation fixed: O-5 (drain-r1 proof log §8)
- Source basis: As RL-13
- Change type: DOC_HYGIENE
- Operation: REPLACE
- Target document: PF07-Canon-Glow-Infrastructure
- Section path: "# **9\) Resource catalog (IDs & links)**"
- Original line(s): 1356 (informative)
- Expected OLD occurrences in the whole original: 1
- Rationale: Unlike the other indented headings, this one follows a paragraph, so Markdown already reads it as a heading. The indent is removed so that it matches every other section heading and a heading match anchored at the line start finds it.

OLD:

````
  ## **9.4 Domains**
````

NEW:

````
## **9.4 Domains**
````

## RL-40

- Ledger rows: None; Nathan-authorized fix
- Observation fixed: O-5 (drain-r1 proof log §8)
- Source basis: As RL-13
- Change type: DOC_HYGIENE
- Operation: REPLACE
- Target document: PF07-Canon-Glow-Infrastructure
- Section path: "# **10\) Service start declarations**"
- Original line(s): 1415 (informative)
- Expected OLD occurrences in the whole original: 1
- Rationale: As RL-13.

OLD:

````
  ## **10.3 Environment prerequisites (names-only)**
````

NEW:

````
## **10.3 Environment prerequisites (names-only)**
````

## RL-41

- Ledger rows: None; Nathan-authorized fix
- Observation fixed: O-5 (drain-r1 proof log §8)
- Source basis: As RL-13
- Change type: DOC_HYGIENE
- Operation: REPLACE
- Target document: PF07-Canon-Glow-Infrastructure
- Section path: "# **10\) Service start declarations**"
- Original line(s): 1423 (informative)
- Expected OLD occurrences in the whole original: 1
- Rationale: As RL-13.

OLD:

````
  ## **10.4 Change control (minimal)**
````

NEW:

````
## **10.4 Change control (minimal)**
````

## RL-42

- Ledger rows: None; Nathan-authorized fix
- Observation fixed: O-9 (drain-r1 proof log §8)
- Source basis: As RL-06
- Change type: CONSISTENCY
- Operation: REPLACE
- Target document: PF07-Canon-Glow-Infrastructure
- Section path: "# **10\) Service start declarations**" > "  ## **10.4 Change control (minimal)**"
- Original line(s): 1429 (informative)
- Expected OLD occurrences in the whole original: 1
- Rationale: As RL-06; this mention uses the PF-numbered title form, so it takes PF06's full in-document title.

OLD:

````
- Governed evidence synchronization is owned by `PF12-Canon-HDE-Schemas-and-Artifacts`. PR workflow is owned by `PF06-Canon-Epic-Process-Guide`. PF07 does not restate either contract.
````

NEW:

````
- Governed evidence synchronization is owned by `PF12-Canon-HDE-Schemas-and-Artifacts`. PR workflow is owned by `PF06-Canon-Change-Process-Guide`. PF07 does not restate either contract.
````

## RL-43

- Ledger rows: C-17 (QA roots); Nathan-authorized fix
- Observation fixed: O-8 (drain-r1 proof log §8)
- Source basis: PF07 §0 "Intent & scope" (l.23: PF07 owns canonical root paths for QA trees); Nathan's direction, 2026-11-02, in this session: "you can fix the defects and discrepancies you noticed"
- Change type: CONSISTENCY
- Operation: REPLACE
- Target document: PF07-Canon-Glow-Infrastructure
- Section path: "# **10\) Service start declarations**" > "## **10.5 Evidence index locations and ownership**"
- Original line(s): 1438 (informative)
- Expected OLD occurrences in the whole original: 1
- Rationale: §0 gives PF07 the canonical QA root paths, which §2.8 and §8.1 record, while §10.5 said PF07 owns no additional evidence root. §10.5 now names those patterns as the exception; layout, families and paths stay with their owners.

OLD:

````
PF07 owns no additional evidence root, index, schema, record shape, artifact-path catalog, QA layout, run-history policy, or snapshot policy. Governed evidence families, record shapes, artifact paths, companion proofs, checksums, root classification, and index/mirror contracts are owned by `PF12-Canon-HDE-Schemas-and-Artifacts`. Live QA layout, current-state evidence posture, historical-run treatment, and the optional Codespaces snapshot posture are owned by `PF19-Canon-Glow-QA-Guide`.
````

NEW:

````
Beyond these two locations and the canonical QA evidence root patterns in §2.8 and §8.1, PF07 owns no evidence root, index, schema, record shape, artifact-path catalog, QA layout, run-history policy, or snapshot policy. Governed evidence families, record shapes, artifact paths, companion proofs, checksums, root classification, and index/mirror contracts are owned by `PF12-Canon-HDE-Schemas-and-Artifacts`. Live QA layout, current-state evidence posture, historical-run treatment, and the optional Codespaces snapshot posture are owned by `PF19-Canon-Glow-QA-Guide`.
````

END OF REDLINES
