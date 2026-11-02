# Redlines: PF27-Canon-Plan-Templates v2.0.6, run gtwpe-20261101-pf10-v14-0-5 (task T-07)

## Package identity

| Field | Value |
| :---- | :---- |
| Run identity | `gtwpe-20261101-pf10-v14-0-5/T-07/prep-r1` |
| Preparation outcome | `READY` |
| Preparer | TW-DRAIN-10 — Prepare PF Document Redlines — 100926.1 (Notion page `3f44590a05eb8172a314fe6b958bb9ff`, fetched live at the start of this step; page last edited 2026-10-09T11:05:22Z), run in the Claude Code cloud session https://claude.ai/code/session_01Q789tyeqMDbVqbUtqxA64b, which Nathan started for document task T-07 on 2026-11-02 |
| Target (original) | `docs/pfcanon/PF27-Canon-Plan-Templates-v2.0.6.md`; in-document title `PF27-Canon-Plan-Templates`; version v2.0.6; git blob `c21096d78b9865bf5aa0c531eee701e462d71a50`; SHA-256 `850dc1a3c8294a0e0521f02cb7300fb05233beccb1ecadf611b41e8ea9adfb00`; 323,765 bytes; 3,938 lines; LF line endings |
| Target baseline commit | `origin/main` `e2b7427ff418ca8f08f05587c4a541308a76da56`. The target blob is unchanged at `origin/main` `84d6d1cf` (checked 2026-11-02). |
| Source | `docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md`; HDE Build Notes v14.0.5; git blob `9df074d90b59fe783c32f7cb3db25872d5dfe9d2`; SHA-256 `cea605d0475889bd9120a51947e23176ce7d2308eb5ab4503b040fd68ddf669d`; 1,976 lines; read at `e2b7427f` |
| Selected source units | 2.1 D-2, lines 277–344 (C-02), with 2.1 context lines 205–224 and 491–516 (C-06); 2.2 status and R-2, lines 517–546 (C-08); 2.2 R-3, lines 547–551 (C-09); 2.15 status and R-1 to R-6, lines 1650–1804 (C-26: R-1, R-3, R-4) |
| Ledger | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/LEDGER.md` at `142feb35144d8795f927e0c78b665ace52279064`; task T-07; rows C-02, C-08, C-09, C-26; supporting C-06 |
| Proof log | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF27/PF27-Canon-Plan-Templates-v2.0.6.redlines.gtwpe-20261101-pf10-v14-0-5.proof-log.md` |

## Payload conventions

* Every redline is a `REPLACE`. Each OLD block is one complete line of the original, without its terminating LF, and occurs exactly once in the whole original. The text between the fence lines is the literal block: its lines are joined with LF (U+000A), and the block has no LF after its last line. The LF that ends the original line stays in place after the NEW block.
* Fences are four backticks with the info string `text`. The fence lines and the info string are not part of any literal. No payload contains a fence.
* Some lines end with exactly two U+0020 SPACE characters, the Markdown line break this target uses inside lists and front matter. Each redline lists those lines by their 1-based line number within the block. No other payload line has trailing whitespace.
* The SHA-256 and UTF-8 byte length of every OLD and NEW block are given for mechanical verification.
* All OLD locations are resolved against the unchanged original. The stated line numbers are informative; the literal OLD block is the locator.

## Redline RL-01

* Redline number: RL-01
* Ledger rows: C-08
* Source items: HDE Build Notes v14.0.5, addendum 2.2, R-2 (lines 540-546); drainage target named at line 581 ("Plan Templates 'Canon precedence for template use' (R-2 citations)")
* Change type: CANON_UPDATE (R-2 citation rule) with CONSISTENCY (provenance sentence reconciled with R-2's no-pin rule)
* Operation: `REPLACE`
* Target document: `PF27-Canon-Plan-Templates`
* Section path: "# **0\) Document Control**" > "## **Purpose & scope \[Required−Now\]**" > "### **Canon precedence for template use**"
* Original location (informative): line 287
* Action: `REPLACE ONCE` the OLD block with the NEW block
* Expected occurrence of OLD in the whole original: 1
* First boundary and last boundary: the single original line 287, which is the whole OLD block
* Rationale: R-2 makes PF-Canon resolvable by stable identity, never by version: citations name the PF document by title (and section where needed), HDE Build Notes by title alone because its addendum numbers restart with each base version, and nothing that must remain valid pins a PF file name, version or digest. The target already carried the title-only rule for HDE Build Notes; this adds the version premise, the reason, the never-by-file-name-or-version rule for other PF references, the ADR scope and the no-pin consequence for the retained provenance sentence.
* OLD: 334 bytes, SHA-256 `e75b9906b6f546533009bd19e61beb1400a5cf68c750e9bca65c66a54862e553`; lines ending with two spaces: none

````text
Cite HDE Build Notes by title alone in current PF prose and derived references, without an internal addendum number, heading, section or file-version locator. Other PF references use their current title and applicable section. Preserve actual file identities and historical citations in source-use inventories and evidence provenance.
````

* NEW: 780 bytes, SHA-256 `7bac5f3464cda96c1941f33cb7ac69d8116e8eb8dc369dc1be6c7e4510eeec17`; lines ending with two spaces: none

````text
PF-Canon document versions, and therefore file names, may change at any time. Cite HDE Build Notes by title alone in current PF prose and derived references, without an internal addendum number, heading, section or file-version locator, because its addendum numbers restart with each base version. Other PF references use their current title, and their section where needed, and never a file name or version. These citation rules also apply to an ADR that a derived artifact carries.

Preserve actual file identities and historical citations in source-use inventories and evidence provenance as a record of what was read. A derived artifact that must remain valid does not pin a PF document's file name, version or content digest, and does not require its bytes to stay unchanged.
````

## Redline RL-02

* Redline number: RL-02
* Ledger rows: C-26
* Source items: HDE Build Notes v14.0.5, addendum 2.15, R-4 'The live-test line' (lines 1763-1771); drainage target named at line 1849
* Change type: NEW_CANON (template field)
* Operation: `REPLACE`
* Target document: `PF27-Canon-Plan-Templates`
* Section path: "# **A) Glow Plan and Runbook Templates**" > "## **1\) Live QA Plan**" > "### **Front matter**"
* Original location (informative): line 326
* Action: `REPLACE ONCE` the OLD block with the NEW block
* Expected occurrence of OLD in the whole original: 1
* First boundary and last boundary: the single original line 326, which is the whole OLD block
* Rationale: R-4 requires the QA plan to carry a line 'Live test:' with RAN (and its evidence references), WAIVED (and the Product Owner's quoted words and date) or MISSING. The front matter is where this template carries plan-level fields, so the line is added there as a template field with allowed placeholder markers. The existing front-matter placeholders are kept unchanged.
* OLD: 79 bytes, SHA-256 `9df012c479baa3d1b0f603a46563f624c822c39e10cabe95ad35d0814bd3e408`; lines ending with two spaces: none

````text
Operators (names-only): PO, IA, (optional) QA agent, (optional) executing agent
````

* NEW: 183 bytes, SHA-256 `4fe82a1703e0919d28769452f978c2caa162dcc05d05fb042f45a5647b3c58d8`; lines ending with two spaces: line 1

````text
Operators (names-only): PO, IA, (optional) QA agent, (optional) executing agent  
Live test: RAN (`<EVIDENCE_REFERENCES>`) | WAIVED (`<PRODUCT_OWNER_QUOTED_WORDS_AND_DATE>`) | MISSING
````

## Redline RL-03

* Redline number: RL-03
* Ledger rows: C-26
* Source items: HDE Build Notes v14.0.5, addendum 2.15: 'Relation to other canon' (lines 1666-1681), R-1 (lines 1704-1739), R-3 (lines 1755-1759), R-4 (lines 1761-1784, the QA plan and plan review rows and 'Who may override'); scope and CRD exclusion (lines 1825, 1835, supporting reading); drainage target at line 1849
* Change type: NEW_CANON (R-1 universal live compat test, R-3 naming, R-4 plan and review enforcement)
* Operation: `REPLACE`
* Target document: `PF27-Canon-Plan-Templates`
* Section path: "# **A) Glow Plan and Runbook Templates**" > "## **1\) Live QA Plan**" > "### **Open-Rails Live QA Requirement for production-affecting epics**"
* Original location (informative): line 389
* Action: `REPLACE ONCE` the OLD block with the NEW block
* Expected occurrence of OLD in the whole original: 1
* First boundary and last boundary: the single original line 389, which is the whole OLD block
* Rationale: R-1 makes the live compat test part of every Epic's QA plan and run, independent of any touches-production finding (2.15 supersedes that dependency for the scopes R-1 to R-4 address). R-3 reserves the name Live QA. R-4 requires the plan and its review to carry the live-test line and blocks approval on MISSING. The existing Open-Rails subsection is kept: it still governs the Epic's own production or vendor surfaces, which R-1 says HDE Governance §3.4 keeps governing. The new subsection is a new H3 placed after the Open-Rails subsection's last line, so no existing heading, title or order changes.
* OLD: 81 bytes, SHA-256 `b4a2075fc35b643aaf6046f2f7835694f5dc7e8fb434c5fb29aa3ef96607c617`; lines ending with two spaces: none

````text
* HDE Build Notes → what it changes for this runbook → impacted PF references
````

* NEW: 3993 bytes, SHA-256 `84733cf5fa7fd5e2a92dd51fda16c0d42bf221ae5b245d8783fc2a99381b7417`; lines ending with two spaces: lines 11, 16

````text
* HDE Build Notes → what it changes for this runbook → impacted PF references

### Live compat test for every Epic (required)

Every Epic's Live QA Plan includes, and its QA run executes, the live compat test below. This holds whatever the Epic changed, and whether or not the Epic's own surfaces are on a production path; the requirement does not depend on a finding that the Epic touches or can affect a production surface. Compat is the product, so a QA verdict that has not seen compat work live says nothing about the product.

These rules apply to Epics. Reusing this template for a CRD does not by itself apply them to the CRD; whether a CRD that changes runtime code also runs the live compat test is the Product Owner's decision.

The plan includes these checks in its **Runbook Check Matrix** and **Check Blocks**:

* **Live vendor compat:** `hdctl showcompat --source vendor` under `SAFE_MODE=0` and `ALLOW_NETWORK=1`, step-local, on synthetic birth data only, at the Epic's QA execution source. Run at least two distinct pairs, each as AB and as BA, and run one pair twice. PASS requires that each output has the canonical result shape and the release identity of the source, that AB and BA are byte-identical, that the two runs are byte-identical, that the Reader bytes stay `{id, band}` only, and that the two pairs produce different results.  
* **Deployed-service check:** a check of the production HD Engine. It compares the `/internal/version` release identity with the release on `main`, and has the production Reader, for each Reader version, score the two synthetic stored people SYN-A and SYN-B in both orders. PASS requires that each answer is eligible and bands-only, and that AB and BA are byte-identical. A mismatch between the deployed release and `main`, and a difference between the deployed bands and the CLI bands for the same birth data, are reported as findings with the QA result.

SYN-A and SYN-B are kept in the production database as permanent QA fixtures under fixed UUIDs, because the deployed Reader scores only people whose charts are stored there:

* SYN-A: `9cff60ae-6eb6-5618-aec5-8acaa4f290d2` (`uuid5(NAMESPACE_URL, "hde-live-qa-synthetic-a")`), born 1990-01-01 at 12:00 in Amsterdam, Netherlands.  
* SYN-B: `57f0c055-ff09-5fdb-aedb-def880437e6f` (`uuid5(NAMESPACE_URL, "hde-live-qa-synthetic-b")`), born 1985-07-15 at 08:30 in London, United Kingdom.

They are stored through the engine's own write path under the Product Owner's write authorization. If either is missing when a QA run starts, the deployed-service check is `TOOLING_BLOCKED` until it is stored again.

When the Epic's own surfaces are on a production or vendor path, the plan also adds at least one open-rails step that exercises those surfaces live, as **Open-Rails Live QA Requirement for production-affecting epics** above and `PF04-Canon-HDE-Governance` §3.4 require. `PF04-Canon-HDE-Governance` §3.4 governs how the live test is executed and its controls.

Closed-rails tests, fixture replay, mocks, static analysis, governed evidence artifacts, review approval and an unrun procedure do not satisfy this requirement.

**Live-test line (required).** The plan and its review each carry a line `Live test:` with one of `RAN` (and its evidence references), `WAIVED` (and the Product Owner's quoted words and date), or `MISSING`. A plan whose line reads `MISSING` is not approval-ready, and its review cannot approve it. No agent may override this block; only the Product Owner may waive this requirement, or any part of it.

**Use of the name "Live QA" (required).** A guide, plan, task set, evidence branch, report or verdict may use the name "Live QA" only if it covers or records the live test this section requires, or a recorded Product Owner waiver of it. Any other QA is called "closed-rails QA" in its title, branch name and verdict line. A QA report without the live test says so in its first line, "No live test ran.", and names the waiver or the missing test.
````

## Redline RL-04

* Redline number: RL-04
* Ledger rows: C-26
* Source items: HDE Build Notes v14.0.5, addendum 2.15, R-4 (line 1769 'the final QA report and RCA'; table row 'Final QA report | No PASS verdict', line 1780)
* Change type: NEW_CANON (template content requirement)
* Operation: `REPLACE`
* Target document: `PF27-Canon-Plan-Templates`
* Section path: "# **A) Glow Plan and Runbook Templates**" > "## **1\) Live QA Plan**" > "### **Close-out deliverables**" > "#### **What “QA RCA & Doc Delta summary” means (explicit; non-drifting)**"
* Original location (informative): line 973
* Action: `REPLACE ONCE` the OLD block with the NEW block
* Expected occurrence of OLD in the whole original: 1
* First boundary and last boundary: the single original line 973, which is the whole OLD block
* Rationale: R-4 requires the final QA report and RCA to carry the live-test line and to give no PASS verdict when the line reads MISSING. In this template the QA RCA & Doc Delta summary is the closure-oriented summary that states what Live QA found and gives the readiness / closeout recommendation, so its content list gains the line and the effect.
* OLD: 225 bytes, SHA-256 `c4a655e687a7fe88eb5dd3f83010de223e278b549754fe268eddd44329bd1a17`; lines ending with two spaces: line 1

````text
* includes an explicit readiness / closeout recommendation that is justified with evidence pointers to the QA event stream and named artifacts; missing required tokens/evidence MUST be labeled as **Unknown** (no inference).  
````

* NEW: 415 bytes, SHA-256 `b03448d1a167dd0ef0cb6727e01d47beffcde3c260cf1af685a2f207633ddf1b`; lines ending with two spaces: lines 1, 2

````text
* includes an explicit readiness / closeout recommendation that is justified with evidence pointers to the QA event stream and named artifacts; missing required tokens/evidence MUST be labeled as **Unknown** (no inference).  
* carries the line `Live test:` with `RAN` (and its evidence references), `WAIVED` (and the Product Owner's quoted words and date), or `MISSING`; with `MISSING`, it gives no PASS verdict.  
````

## Redline RL-05

* Redline number: RL-05
* Ledger rows: C-09
* Source items: HDE Build Notes v14.0.5, addendum 2.2, R-3 (lines 547-551), drained as written; drainage target named at line 581
* Change type: NEW_CANON
* Operation: `REPLACE`
* Target document: `PF27-Canon-Plan-Templates`
* Section path: "# **A) Glow Plan and Runbook Templates**" > "## **Review guardrails**" > "### **CI lane classification and automated budget-control discipline**"
* Original location (informative): line 1312
* Action: `REPLACE ONCE` the OLD block with the NEW block
* Expected occurrence of OLD in the whole original: 1
* First boundary and last boundary: the single original line 1312, which is the whole OLD block
* Rationale: R-3 states when the close-pack writer runs and that its test is a close-stage test selected only by changes to the writer, a close-candidate source schema, the closeout validation workflow or the test, outside full validation and any other ordinary required PR CI. R-3 cites this section as its lane basis. The rule is drained as written, after the paragraph that keeps administrative closeout work out of ordinary required PR CI. R-3's parenthetical citation of this same section is dropped because the text now sits in it. The HDE-EPIC041 bounded CCR-5 ruling (addendum 2.9) is not drained.
* OLD: 563 bytes, SHA-256 `390ff365727da2c2320494429eea032c600e8f2da7ba1288e305baacf068c454`; lines ending with two spaces: none

````text
Administrative closeout work MUST NOT become ordinary required PR CI solely to create, refresh, normalize, package, index, mirror, hash, sign, transfer, or validate an epic close report, token matrix, Doc Delta package, close pack, historical receipt, closeout ledger, acceptance package, or other administrative proof. Separately authorized closeout automation MAY remain isolated and non-gating. A control that protects a genuine release, security, compliance, QA, audit, product, build, deployment, or operational boundary remains in the smallest correct lane.
````

* NEW: 974 bytes, SHA-256 `093479d82dec0023faae3243e72802afc543e0394ccc9921deb1f49ded211d51`; lines ending with two spaces: none

````text
Administrative closeout work MUST NOT become ordinary required PR CI solely to create, refresh, normalize, package, index, mirror, hash, sign, transfer, or validate an epic close report, token matrix, Doc Delta package, close pack, historical receipt, closeout ledger, acceptance package, or other administrative proof. Separately authorized closeout automation MAY remain isolated and non-gating. A control that protects a genuine release, security, compliance, QA, audit, product, build, deployment, or operational boundary remains in the smallest correct lane.

The close-pack writer writes a close pack only at the close stage, at the end of a full work-unit cycle, after the authorized QA verdict and the closure decision exist. The writer's test is a close-stage test. CI selects it when the writer, a close-candidate source schema, the closeout validation workflow or the test itself changes. It is not part of full validation or of any other ordinary required PR CI.
````

## Redline RL-06

* Redline number: RL-06
* Ledger rows: C-02
* Source items: HDE Build Notes v14.0.5, addendum 2.1, D-2 (lines 277-344): 'Canon superseded or added to', line 316; drainage target, line 323
* Change type: CLARIFY (CANON_UPDATE of a category's meaning)
* Operation: `REPLACE`
* Target document: `PF27-Canon-Plan-Templates`
* Section path: "# **A) Glow Plan and Runbook Templates**" > "## **2\) HDE-EPIC-Specification**" > "### **Epic Record Template (Normative)**" > "#### **Contract and Compatibility Posture (MUST)**"
* Original location (informative): line 1459
* Action: `REPLACE ONCE` the OLD block with the NEW block
* Expected occurrence of OLD in the whole original: 1
* First boundary and last boundary: the single original line 1459, which is the whole OLD block
* Rationale: D-2 records that the PF27 category 'explicit legacy fallback' reads as the terminal-v1 legacy selection: a terminal v1 base keeps the retained legacy route, the v1 path is retained legacy selection and not fallback, and HDE CLI/API/Vendor Ref §7.1.10 governs route selection and the configured-base boundary. The category keeps its name, as D-2 keeps the matching evidence label unchanged; the bullet gains the reading and the routing to the owner.
* OLD: 384 bytes, SHA-256 `1fbee1319705ea7319e5445440aaa0bf82767b0220dfb49e34e5ebfde22a33f1`; lines ending with two spaces: line 1

````text
* **`bg:resolve --source vendor` route-policy posture:** If an epic, implementation plan, QA plan, remediation guide, or review artifact involves `bg:resolve --source vendor`, vendor-backed BodyGraph resolution, or future BodyGraph-detail runtime compatibility, it MUST state whether the path is v2 chart-backed, explicit legacy fallback, dual-route policy, or unsupported nonclaim.  
````

* NEW: 707 bytes, SHA-256 `5874fe269b537ed2edc8f0ad39b9df9d35f1e57b30ec5d064835d93dd3f13845`; lines ending with two spaces: line 1

````text
* **`bg:resolve --source vendor` route-policy posture:** If an epic, implementation plan, QA plan, remediation guide, or review artifact involves `bg:resolve --source vendor`, vendor-backed BodyGraph resolution, or future BodyGraph-detail runtime compatibility, it MUST state whether the path is v2 chart-backed, explicit legacy fallback, dual-route policy, or unsupported nonclaim. The category explicit legacy fallback reads as the terminal-v1 legacy selection: the retained legacy route that a configured base ending in a terminal `v1` segment selects. It is not a fallback and makes no fallback claim. `PF05-Canon-HDE-CLI-API-Vendor-Ref` §7.1.10 owns route selection and the configured-base boundary.  
````

## Batch check

| Redline | Original line | OLD count (expected / observed) | Span start–end (character offsets in the original) |
| :---- | :---- | :---- | :---- |
| RL-01 | 287 | 1 / 1 | 27086–27420 |
| RL-02 | 326 | 1 / 1 | 30064–30143 |
| RL-03 | 389 | 1 / 1 | 35357–35434 |
| RL-04 | 973 | 1 / 1 | 88968–89193 |
| RL-05 | 1312 | 1 / 1 | 161547–162110 |
| RL-06 | 1459 | 1 / 1 | 180321–180705 |

No two spans intersect or share a boundary, no redline anchors on text another redline produces, and the six redlines apply in one pass against the unchanged original. The proof log records the validation and the one-pass simulation.

END OF REDLINES
