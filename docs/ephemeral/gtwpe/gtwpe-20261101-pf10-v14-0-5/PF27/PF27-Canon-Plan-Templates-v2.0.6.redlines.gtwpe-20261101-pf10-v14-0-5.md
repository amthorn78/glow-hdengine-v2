# Redlines: PF27-Canon-Plan-Templates v2.0.6, run gtwpe-20261101-pf10-v14-0-5 (task T-07)

## Package identity

| Field | Value |
| :---- | :---- |
| Run identity | `gtwpe-20261101-pf10-v14-0-5/T-07/prep-r2` |
| Preparation outcome | `READY` |
| Revision | `prep-r2` supersedes `prep-r1`, which is the parent commit on the branch ("docs(ephemeral): add T-07 PF27 redlines and proof log (gtwpe-20261101-pf10-v14-0-5)") and was never given to TW-APPLY-10. The proof log records why. |
| Preparer | TW-DRAIN-10 — Prepare PF Document Redlines — 100926.1 (Notion page `3f44590a05eb8172a314fe6b958bb9ff`, fetched live at the start of this step; page last edited 2026-10-09T11:05:22Z), run in the Claude Code cloud session https://claude.ai/code/session_01Q789tyeqMDbVqbUtqxA64b, which Nathan started for document task T-07 on 2026-11-02 |
| Target (original) | `docs/pfcanon/PF27-Canon-Plan-Templates-v2.0.6.md`; in-document title `PF27-Canon-Plan-Templates`; version v2.0.6; git blob `c21096d78b9865bf5aa0c531eee701e462d71a50`; SHA-256 `850dc1a3c8294a0e0521f02cb7300fb05233beccb1ecadf611b41e8ea9adfb00`; 323,765 bytes; 3,938 lines; LF line endings |
| Target baseline commit | `origin/main` `e2b7427ff418ca8f08f05587c4a541308a76da56`. The target blob is unchanged at `origin/main` `84d6d1cf` (checked 2026-11-02). |
| Source | `docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md`; HDE Build Notes v14.0.5; git blob `9df074d90b59fe783c32f7cb3db25872d5dfe9d2`; SHA-256 `cea605d0475889bd9120a51947e23176ce7d2308eb5ab4503b040fd68ddf669d`; 1,976 lines; read at `e2b7427f` |
| Selected source units | 2.1 D-2, lines 277–344 (C-02), with 2.1 context lines 205–224 and 491–516 (C-06); 2.2 status and R-2, lines 517–546 (C-08); 2.2 R-3, lines 547–551 (C-09); 2.15 status and R-1 to R-6, lines 1650–1804 (C-26: R-1, R-3, R-4) |
| Ledger | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/LEDGER.md` at `142feb35144d8795f927e0c78b665ace52279064`; task T-07; rows C-02, C-08, C-09, C-26; supporting C-06 |
| Proof log | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF27/PF27-Canon-Plan-Templates-v2.0.6.redlines.gtwpe-20261101-pf10-v14-0-5.proof-log.md` |

## Payload conventions

* Every redline is a `REPLACE`. Each OLD block is one or more complete contiguous lines of the original, without the LF that ends its last line, and occurs exactly once in the whole original. The text between the fence lines is the literal block: its lines are joined with LF (U+000A), and the block has no LF after its last line. The LF that ends the original line stays in place after the NEW block.
* Fences are four backticks with the info string `text`. The fence lines and the info string are not part of any literal. No payload contains a fence.
* Some lines end with exactly two U+0020 SPACE characters, the Markdown line break this target uses inside lists and front matter. Each redline lists those lines by their 1-based line number within the block. No other payload line has trailing whitespace.
* The SHA-256 and UTF-8 byte length of every OLD and NEW block are given for mechanical verification.
* All OLD locations are resolved against the unchanged original. The stated line numbers are informative; the literal OLD block is the locator.

## Redline RL-01

* Redline number: RL-01
* Ledger rows: C-02
* Source items: HDE Build Notes v14.0.5, addendum 2.1, D-2: 'The two canon rules fit together' (lines 290-297), with 'Canon superseded or added to' (line 313)
* Change type: CONSISTENCY (context drainage)
* Operation: `REPLACE`
* Target document: `PF27-Canon-Plan-Templates`
* Section path: "# **0\) Document Control**" > "## **Purpose & scope \[Required−Now\]**" > "### **Exact technical facts and secret safety**"
* Original location (informative): line 112
* Action: `REPLACE ONCE` the OLD block with the NEW block
* Expected occurrence of OLD in the whole original: 1
* First boundary and last boundary: the single original line 112, which is the whole OLD block
* Rationale: D-2 makes the configured base's terminal v1 or v2 segment the single permitted reading of a version: one exact comparison made once, before any route is built, and owned by HDE CLI/API/Vendor Ref §7.1.10; every other prohibition stays. This row lists the only classifications under which a plan may show a version literal, and without this addition it would forbid a plan from stating the route-selection rule D-2 makes canon, including the v2 chart-backed and terminal-v1 categories of the route-policy posture. The route-construction prohibition is unchanged.
* OLD: 275 bytes, SHA-256 `13534b3e6e3255208d61a9bdeb5f9673a7d224f81a9d8dfd0bdea6c5d7b9ea8c`; lines ending with two spaces: none

````text
| Version literals | Do not use `/v1` or `/v2` as active route-construction inputs. A version literal MAY appear only when classified as historical evidence, an artifact-family name, non-runtime provenance, a configurable-version test input, or a legacy route-family label. |
````

* NEW: 422 bytes, SHA-256 `796b8177137075ddd03b39d5d5e0bed2dbf63c2e324f8b194febaa91787b500d`; lines ending with two spaces: none

````text
| Version literals | Do not use `/v1` or `/v2` as active route-construction inputs. A version literal MAY appear only when classified as historical evidence, an artifact-family name, non-runtime provenance, a configurable-version test input, a legacy route-family label, or the single permitted classification of the configured base's terminal `v1` or `v2` segment that `PF05-Canon-HDE-CLI-API-Vendor-Ref` §7.1.10 owns. |
````

## Redline RL-02

* Redline number: RL-02
* Ledger rows: C-08
* Source items: HDE Build Notes v14.0.5, addendum 2.2, R-2 (lines 540-546), bullets 1, 2 and 4; drainage target named at line 581
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

## Redline RL-03

* Redline number: RL-03
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
* Rationale: R-4 requires the QA plan to carry a line 'Live test:' with RAN (and its evidence references), WAIVED (and the Product Owner's quoted words and date) or MISSING. The front matter carries this template's plan-level fields, so the line is added there with allowed placeholder markers. The existing front-matter placeholders are kept unchanged.
* OLD: 79 bytes, SHA-256 `9df012c479baa3d1b0f603a46563f624c822c39e10cabe95ad35d0814bd3e408`; lines ending with two spaces: none

````text
Operators (names-only): PO, IA, (optional) QA agent, (optional) executing agent
````

* NEW: 183 bytes, SHA-256 `4fe82a1703e0919d28769452f978c2caa162dcc05d05fb042f45a5647b3c58d8`; lines ending with two spaces: line 1

````text
Operators (names-only): PO, IA, (optional) QA agent, (optional) executing agent  
Live test: RAN (`<EVIDENCE_REFERENCES>`) | WAIVED (`<PRODUCT_OWNER_QUOTED_WORDS_AND_DATE>`) | MISSING
````

## Redline RL-04

* Redline number: RL-04
* Ledger rows: C-26
* Source items: HDE Build Notes v14.0.5, addendum 2.15: 'Relation to other canon' (lines 1666-1681), R-1 (1704-1739), R-2 (1741-1753), R-3 (1755-1759), R-4 (1761-1784: the plan and plan-review rows and 'Who may override'), R-5 (1787-1790), R-6 (1792-1803); supporting: scope and CRD exclusion (1825, 1835); drainage target (1849)
* Change type: NEW_CANON (R-1 universal live compat test; R-2 waiver; R-3 naming; R-4 plan and review enforcement; R-5 blocked live test; R-6 routing)
* Operation: `REPLACE`
* Target document: `PF27-Canon-Plan-Templates`
* Section path: "# **A) Glow Plan and Runbook Templates**" > "## **1\) Live QA Plan**" > "### **Open-Rails Live QA Requirement for production-affecting epics**"
* Original location (informative): line 389
* Action: `REPLACE ONCE` the OLD block with the NEW block
* Expected occurrence of OLD in the whole original: 1
* First boundary and last boundary: the single original line 389, which is the whole OLD block
* Rationale: R-1 makes the live compat test part of every Epic's QA plan and run, independent of any touches-production finding (2.15 supersedes that dependency for the scopes R-1 to R-4 address). R-2 reserves the waiver to the Product Owner and makes an agent's non-applicability finding a question. R-3 reserves the name Live QA. R-4 requires the plan and its review to carry the live-test line and blocks approval on MISSING. R-5 keeps a live test that cannot run TOOLING_BLOCKED. R-6 keeps the execution controls and the Ops-evidence posture with HDE Governance §3.4, which this text routes to. The existing Open-Rails subsection is kept: it still governs the Epic's own production or vendor surfaces, which R-1 says HDE Governance §3.4 keeps governing. The new subsection is a new H3 after the Open-Rails subsection's last line, so no existing heading, title or order changes.
* OLD: 81 bytes, SHA-256 `b4a2075fc35b643aaf6046f2f7835694f5dc7e8fb434c5fb29aa3ef96607c617`; lines ending with two spaces: none

````text
* HDE Build Notes → what it changes for this runbook → impacted PF references
````

* NEW: 5156 bytes, SHA-256 `444ff55821ea7f22c168981fa54db4d6d39358beb9a99ac42bcb244fa862f7b5`; lines ending with two spaces: lines 11, 16

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

When the Epic's own surfaces are on a production or vendor path, the plan also adds at least one open-rails step that exercises those surfaces live, as **Open-Rails Live QA Requirement for production-affecting epics** above and `PF04-Canon-HDE-Governance` §3.4 require. `PF04-Canon-HDE-Governance` §3.4 governs how the live test is executed and its controls, and the live test's result is Ops evidence under that section.

Closed-rails tests, fixture replay, mocks, static analysis, governed evidence artifacts, review approval and an unrun procedure do not satisfy this requirement.

A live test that cannot run, because of missing credentials, missing target facts, an unavailable vendor or a missing authorization, is `TOOLING_BLOCKED`. It is never converted into a PASS, a waiver or a closure: the Epic waits, and the Product Owner decides how to proceed.

**Waiver (Product Owner only).** Only the Product Owner may decide that this requirement, or any part of it, does not apply to an Epic. A waiver is written and specific to the change. It quotes the Product Owner's words with their date and carries the content `PF04-Canon-HDE-Governance` §3.4 requires of an exemption: the reason, the accepted risk, the substitute proof and why it suffices, the claim withheld, and any later live-proof obligation. An agent's finding that the Epic's surfaces are not on a live path, or that the live test cannot run meaningfully, is a question for the Product Owner, put as a named decision no later than QA readiness; the plan is not approval-ready until the Product Owner answers. Silence, reviewer agreement, convenience, closed-rails success or a finding of non-applicability is not a waiver; without a recorded waiver, this requirement applies in full.

**Live-test line (required).** The plan and its review each carry a line `Live test:` with one of `RAN` (and its evidence references), `WAIVED` (and the Product Owner's quoted words and date), or `MISSING`. A plan whose line reads `MISSING` is not approval-ready, and its review cannot approve it. No agent may override this block.

**Use of the name "Live QA" (required).** A guide, plan, task set, evidence branch, report or verdict may use the name "Live QA" only if it covers or records the live test this section requires, or a recorded Product Owner waiver of it. Any other QA is called "closed-rails QA" in its title, branch name and verdict line. A QA report without the live test says so in its first line, "No live test ran.", and names the waiver or the missing test.
````

## Redline RL-05

* Redline number: RL-05
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

## Redline RL-06

* Redline number: RL-06
* Ledger rows: C-26
* Source items: HDE Build Notes v14.0.5, addendum 2.15, R-4 (table rows 'QA plan | Not approval-ready' and 'Plan review | Not approvable', lines 1777-1778; 'Who may override', line 1784)
* Change type: CONSISTENCY (context drainage)
* Operation: `REPLACE`
* Target document: `PF27-Canon-Plan-Templates`
* Section path: "# **A) Glow Plan and Runbook Templates**" > "## **Review guardrails**" > "### **Hard blockers for plan approval/execution**"
* Original location (informative): line 1168
* Action: `REPLACE ONCE` the OLD block with the NEW block
* Expected occurrence of OLD in the whole original: 1
* First boundary and last boundary: the single original line 1168, which is the whole OLD block
* Rationale: This bullet is the closed list of valid Live QA Plan approval blockers; reviewers may not block on anything outside it. R-4 makes a plan whose live-test line reads MISSING not approvable, and no agent may override that block, so the block is added to the list.
* OLD: 855 bytes, SHA-256 `17e33eb0dd18a7df7051b5cb6746fca764644ef89337c20f71b5327a01081fda`; lines ending with two spaces: line 1

````text
* Valid Live QA Plan approval blockers are operational: missing required QA step coverage, missing required deliverables or explicit PASS/FAIL criteria, unsafe rails, secret exposure, live-provider or external-action boundary violation, public/private surface boundary violation, token overclaim, non-token proof label treated as an acceptance token, PF23 used as an execution artifact, PF20 used as current authority, PF14 used as governance or acceptance authority, PF-canon drainage required as a gate, unproven required existing locus with no source-grounded proof, no discovery posture, and no QA-created fallback, wrong target execution, prohibited mutation, no governed evidence family, no decisive receipt, contradiction of active PF10, or contradiction of permanent PF-Canon where PF10 is silent and the contradiction affects operational truth.  
````

* NEW: 964 bytes, SHA-256 `5f3719e48432345f7c85ab30cd73da98204079b2a6f9e360f2d109f82a7b89d1`; lines ending with two spaces: line 1

````text
* Valid Live QA Plan approval blockers are operational: missing required QA step coverage, a missing live compat test with no recorded Product Owner waiver (a `Live test:` line that reads `MISSING`), missing required deliverables or explicit PASS/FAIL criteria, unsafe rails, secret exposure, live-provider or external-action boundary violation, public/private surface boundary violation, token overclaim, non-token proof label treated as an acceptance token, PF23 used as an execution artifact, PF20 used as current authority, PF14 used as governance or acceptance authority, PF-canon drainage required as a gate, unproven required existing locus with no source-grounded proof, no discovery posture, and no QA-created fallback, wrong target execution, prohibited mutation, no governed evidence family, no decisive receipt, contradiction of active PF10, or contradiction of permanent PF-Canon where PF10 is silent and the contradiction affects operational truth.  
````

## Redline RL-07

* Redline number: RL-07
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
* Rationale: R-3 states when the close-pack writer runs and that its test is a close-stage test, selected only by changes to the writer, a close-candidate source schema, the closeout validation workflow or the test, and outside full validation and every other ordinary required PR CI. R-3 cites this section as its lane basis. The rule is drained as written, after the paragraph that keeps administrative closeout work out of ordinary required PR CI; R-3's parenthetical citation of this same section is dropped because the text now sits in it. The HDE-EPIC041 bounded CCR-5 ruling (addendum 2.9) is not drained.
* OLD: 563 bytes, SHA-256 `390ff365727da2c2320494429eea032c600e8f2da7ba1288e305baacf068c454`; lines ending with two spaces: none

````text
Administrative closeout work MUST NOT become ordinary required PR CI solely to create, refresh, normalize, package, index, mirror, hash, sign, transfer, or validate an epic close report, token matrix, Doc Delta package, close pack, historical receipt, closeout ledger, acceptance package, or other administrative proof. Separately authorized closeout automation MAY remain isolated and non-gating. A control that protects a genuine release, security, compliance, QA, audit, product, build, deployment, or operational boundary remains in the smallest correct lane.
````

* NEW: 974 bytes, SHA-256 `093479d82dec0023faae3243e72802afc543e0394ccc9921deb1f49ded211d51`; lines ending with two spaces: none

````text
Administrative closeout work MUST NOT become ordinary required PR CI solely to create, refresh, normalize, package, index, mirror, hash, sign, transfer, or validate an epic close report, token matrix, Doc Delta package, close pack, historical receipt, closeout ledger, acceptance package, or other administrative proof. Separately authorized closeout automation MAY remain isolated and non-gating. A control that protects a genuine release, security, compliance, QA, audit, product, build, deployment, or operational boundary remains in the smallest correct lane.

The close-pack writer writes a close pack only at the close stage, at the end of a full work-unit cycle, after the authorized QA verdict and the closure decision exist. The writer's test is a close-stage test. CI selects it when the writer, a close-candidate source schema, the closeout validation workflow or the test itself changes. It is not part of full validation or of any other ordinary required PR CI.
````

## Redline RL-08

* Redline number: RL-08
* Ledger rows: C-26
* Source items: HDE Build Notes v14.0.5, addendum 2.15: 'Relation to other canon' (1666-1681), R-1 scope (1706), R-2 'The rule' (1743), R-4 QA plan row (1777)
* Change type: CANON_UPDATE (context drainage)
* Operation: `REPLACE`
* Target document: `PF27-Canon-Plan-Templates`
* Section path: "# **A) Glow Plan and Runbook Templates**" > "## **2\) HDE-EPIC-Specification**" > "### **Epic Record Template (Normative)**" > "#### **Contract and Compatibility Posture (MUST)**"
* Original location (informative): lines 1450–1453
* Action: `REPLACE ONCE` the OLD block with the NEW block
* Expected occurrence of OLD in the whole original: 1
* First boundary: the complete original line 1450; last boundary: the complete original line 1453; the OLD block is that inclusive range
* Rationale: These Epic Specification bullets make the Epic's open-rails QA obligation depend on whether the epic touches a production-functional surface, the dependency 2.15 supersedes for the minimum live test. The declaration, preservation and review bullets therefore also carry the live compat test every Epic's QA runs, waivable only by the Product Owner; the production-functional live vendor test and the broader open-rails rules stay as written. 'Open-rails triggering surfaces' (line 1451) is unchanged and is reproduced only because this REPLACE covers the contiguous region 1450-1453.
* OLD: 1950 bytes, SHA-256 `7ac20f11c30e7e8669cc367a2391aa0238c80619d9ac2fafbc3beee9763d8bb8`; lines ending with two spaces: lines 1, 2, 3, 4

````text
* **Open-rails QA declaration:** Identify whether the epic touches a surface used to produce a production feature stated as functional in PF-Canon. For that scope, declare the mandatory bounded live vendor test with synthetic data only and `SAFE_MODE=0`, `ALLOW_NETWORK=1`; no exemption or non-vendor substitute is established. Outside that scope, retain the applicable broader production-affecting open-rails requirement and any already authorized exemption. Keep the declaration planning-level; do not embed Live QA commands in the Epic Specification.  
* **Open-rails triggering surfaces:** User or production-surface triggers include public app behavior, user-facing behavior, production runtime behavior, CLI behavior, operator-facing CLI surfaces, vendor ingestion, vendor request shaping, vendor response handling, vendor route policy, external API transport, environment or secret binding behavior, database persistence or retrieval behavior, runtime compute behavior, deployed service behavior, and admin or ops-facing behavior that can affect production truth.  
* **Implementation preservation:** Any Implementation Plan, remediation guide or downstream QA-prep artifact derived from the Epic Specification MUST preserve the mandatory live vendor test for production-functional scope. Closed-rails proof, static validation, repository inspection, generated evidence, a database or deployed-service probe, OPS observation or exemption language does not erase it. Preserve any separately applicable broader open-rails obligation outside that scope.  
* **Review posture:** A QA Plan within production-functional scope is not approval-ready without the bounded synthetic live vendor test. Identify the affected feature and surface; do not approve a closed-rails-only plan on an exemption or a non-vendor live-step substitute. Outside that scope, apply the existing broader production-affecting requirement and its controlling authorization.  
````

* NEW: 2481 bytes, SHA-256 `e37c15b8362dab4601e7c962fd4cf087de7b86b3e5c83cf42dce1e77e6b25ff3`; lines ending with two spaces: lines 1, 2, 3, 4

````text
* **Open-rails QA declaration:** Declare that the epic's QA plan includes, and its QA run executes, the live compat test that the Live QA Plan template's **Live compat test for every Epic (required)** defines, whatever the epic changes. That declaration does not depend on whether the epic touches a production surface, and only the Product Owner may waive the test or any part of it. Also identify whether the epic touches a surface used to produce a production feature stated as functional in PF-Canon. For that scope, declare the mandatory bounded live vendor test with synthetic data only and `SAFE_MODE=0`, `ALLOW_NETWORK=1`; no exemption or non-vendor substitute is established. Outside that scope, retain the applicable broader production-affecting open-rails requirement and any already authorized exemption. Keep the declaration planning-level; do not embed Live QA commands in the Epic Specification.  
* **Open-rails triggering surfaces:** User or production-surface triggers include public app behavior, user-facing behavior, production runtime behavior, CLI behavior, operator-facing CLI surfaces, vendor ingestion, vendor request shaping, vendor response handling, vendor route policy, external API transport, environment or secret binding behavior, database persistence or retrieval behavior, runtime compute behavior, deployed service behavior, and admin or ops-facing behavior that can affect production truth.  
* **Implementation preservation:** Any Implementation Plan, remediation guide or downstream QA-prep artifact derived from the Epic Specification MUST preserve the live compat test every Epic's QA runs and the mandatory live vendor test for production-functional scope. Closed-rails proof, static validation, repository inspection, generated evidence, a database or deployed-service probe, OPS observation or exemption language does not erase either. Preserve any separately applicable broader open-rails obligation outside that scope.  
* **Review posture:** An Epic's QA Plan is not approval-ready without the live compat test, unless the Product Owner has recorded a waiver of it. A QA Plan within production-functional scope is not approval-ready without the bounded synthetic live vendor test. Identify the affected feature and surface; do not approve a closed-rails-only plan on an exemption or a non-vendor live-step substitute. Outside that scope, apply the existing broader production-affecting requirement and its controlling authorization.  
````

## Redline RL-09

* Redline number: RL-09
* Ledger rows: C-02
* Source items: HDE Build Notes v14.0.5, addendum 2.1, D-2 (lines 277-344): 'Canon superseded or added to', line 316; drainage target, line 323; 'The v1 path is retained legacy selection, not fallback', line 288
* Change type: CLARIFY (CANON_UPDATE of a category's meaning)
* Operation: `REPLACE`
* Target document: `PF27-Canon-Plan-Templates`
* Section path: "# **A) Glow Plan and Runbook Templates**" > "## **2\) HDE-EPIC-Specification**" > "### **Epic Record Template (Normative)**" > "#### **Contract and Compatibility Posture (MUST)**"
* Original location (informative): line 1459
* Action: `REPLACE ONCE` the OLD block with the NEW block
* Expected occurrence of OLD in the whole original: 1
* First boundary and last boundary: the single original line 1459, which is the whole OLD block
* Rationale: D-2 records that the Plan Templates category 'explicit legacy fallback' reads as the terminal-v1 legacy selection: a terminal v1 base keeps the retained legacy route, the v1 path is retained legacy selection and not fallback, and HDE CLI/API/Vendor Ref §7.1.10 governs route selection and the configured-base boundary. The category keeps its name, as D-2 keeps the matching evidence label unchanged; the bullet gains the reading and the routing to the owner.
* OLD: 384 bytes, SHA-256 `1fbee1319705ea7319e5445440aaa0bf82767b0220dfb49e34e5ebfde22a33f1`; lines ending with two spaces: line 1

````text
* **`bg:resolve --source vendor` route-policy posture:** If an epic, implementation plan, QA plan, remediation guide, or review artifact involves `bg:resolve --source vendor`, vendor-backed BodyGraph resolution, or future BodyGraph-detail runtime compatibility, it MUST state whether the path is v2 chart-backed, explicit legacy fallback, dual-route policy, or unsupported nonclaim.  
````

* NEW: 707 bytes, SHA-256 `5874fe269b537ed2edc8f0ad39b9df9d35f1e57b30ec5d064835d93dd3f13845`; lines ending with two spaces: line 1

````text
* **`bg:resolve --source vendor` route-policy posture:** If an epic, implementation plan, QA plan, remediation guide, or review artifact involves `bg:resolve --source vendor`, vendor-backed BodyGraph resolution, or future BodyGraph-detail runtime compatibility, it MUST state whether the path is v2 chart-backed, explicit legacy fallback, dual-route policy, or unsupported nonclaim. The category explicit legacy fallback reads as the terminal-v1 legacy selection: the retained legacy route that a configured base ending in a terminal `v1` segment selects. It is not a fallback and makes no fallback claim. `PF05-Canon-HDE-CLI-API-Vendor-Ref` §7.1.10 owns route selection and the configured-base boundary.  
````

## Redline RL-10

* Redline number: RL-10
* Ledger rows: C-26
* Source items: HDE Build Notes v14.0.5, addendum 2.15, R-4 (line 1770 'the close mutation set result'; table row 'Close mutation set | Not close-PR-ready', line 1781)
* Change type: NEW_CANON (template field; context drainage)
* Operation: `REPLACE`
* Target document: `PF27-Canon-Plan-Templates`
* Section path: "# **A) Glow Plan and Runbook Templates**" > "## 3B) Close Mutation Set Task Record (Template)" > "### Record fields (required)"
* Original location (informative): line 2261
* Action: `REPLACE ONCE` the OLD block with the NEW block
* Expected occurrence of OLD in the whole original: 1
* First boundary and last boundary: the single original line 2261, which is the whole OLD block
* Rationale: R-4 requires the close mutation set result to carry the live-test line and makes it not close-PR-ready on MISSING. This template's record fields define that record, so the field is added after Exit. The held Entries and exit subsection (H-06) is not touched.
* OLD: 58 bytes, SHA-256 `978134d7eaac48d11fe1a5b8ce3593e1c4c4553aa4d94a75d08d2190da14176f`; lines ending with two spaces: line 1

````text
* **Exit:** the closure decision that judges the result.  
````

* NEW: 248 bytes, SHA-256 `71c0daf1ffc3b683905787ce052351b3ba2111ac19d0bc07937ccbec4c918125`; lines ending with two spaces: lines 1, 2

````text
* **Exit:** the closure decision that judges the result.  
* **Live test:** `RAN` (and its evidence references), `WAIVED` (and the Product Owner's quoted words and date), or `MISSING`. With `MISSING`, the close mutation set is not close-PR-ready.  
````

## Redline RL-11

* Redline number: RL-11
* Ledger rows: C-26
* Source items: HDE Build Notes v14.0.5, addendum 2.15, R-4 (line 1768 'the QA evidence review'; table row 'Evidence review | Not acceptable', line 1779)
* Change type: NEW_CANON (conditional template field; context drainage)
* Operation: `REPLACE`
* Target document: `PF27-Canon-Plan-Templates`
* Section path: "# **A) Glow Plan and Runbook Templates**" > "## **8\) QA Pass Review Record (Template; REVIEW mode only)**" > "### **Required structure (paste-ready)**"
* Original location (informative): line 3120
* Action: `REPLACE ONCE` the OLD block with the NEW block
* Expected occurrence of OLD in the whole original: 1
* First boundary and last boundary: the single original line 3120, which is the whole OLD block
* Rationale: R-4 requires the QA evidence review to carry the live-test line and makes the evidence not acceptable on MISSING. This template reviews a Live QA check or check cluster; when it is used as the run's QA evidence review, it must carry the line, so the field is added conditionally to the Review Summary. A review of a single check is unaffected.
* OLD: 83 bytes, SHA-256 `08fe3ab6197290ab56f5398efa10b0c487d51add7b414d4d6d7090b4742ed232`; lines ending with two spaces: none

````text
* State `None` when no PF-Canon inconsistencies or new doc requirements were found.
````

* NEW: 331 bytes, SHA-256 `9ffac894d4f687d22ebf901b77905530fe43840dcc05116343243704d7395b81`; lines ending with two spaces: line 1

````text
* State `None` when no PF-Canon inconsistencies or new doc requirements were found.  
* Live test, when this record is the QA evidence review for the run as a whole: `RAN` (and its evidence references), `WAIVED` (and the Product Owner's quoted words and date), or `MISSING`. With `MISSING`, the reviewed evidence is not acceptable.
````

## Redline RL-12

* Redline number: RL-12
* Ledger rows: C-26
* Source items: HDE Build Notes v14.0.5, addendum 2.15, R-3 'The report's first line' (line 1759)
* Change type: NEW_CANON (template rule; context drainage)
* Operation: `REPLACE`
* Target document: `PF27-Canon-Plan-Templates`
* Section path: "# **A) Glow Plan and Runbook Templates**" > "## **9\) Final QA Closeout Review \+ QA RCA (Template; REVIEW mode only)**" > "### **Scope**"
* Original location (informative): line 3218
* Action: `REPLACE ONCE` the OLD block with the NEW block
* Expected occurrence of OLD in the whole original: 1
* First boundary and last boundary: the single original line 3218, which is the whole OLD block
* Rationale: R-3 requires a QA report without the live test to say so in its first line and name the waiver or the missing test. This template produces the epic's final QA closeout report and RCA, so its scope states the first-line rule.
* OLD: 346 bytes, SHA-256 `ef0b4f2643eb9f8f50fb137cba4e2551e309e599fb9f30be6703c8a74fc98a32`; lines ending with two spaces: none

````text
**Use this template when the completed Live QA stream for an epic must be synthesized into a closeout recommendation, canonical RCA basis, coverage-vs-plan accounting, and PF-only doc-delta proposals. It is review-only: it summarizes executed QA and closeout posture, and it does not create new runbooks, new commands, or new acceptance tokens.**
````

* NEW: 494 bytes, SHA-256 `27c5288cde2f5635424dda7f9e9fc7e29f718742283abeb608eaf8e285b67fd0`; lines ending with two spaces: none

````text
**Use this template when the completed Live QA stream for an epic must be synthesized into a closeout recommendation, canonical RCA basis, coverage-vs-plan accounting, and PF-only doc-delta proposals. It is review-only: it summarizes executed QA and closeout posture, and it does not create new runbooks, new commands, or new acceptance tokens.**

When no live test ran, the report's first line is `No live test ran.`, and the report names the recorded Product Owner waiver or the missing test.
````

## Redline RL-13

* Redline number: RL-13
* Ledger rows: C-26
* Source items: HDE Build Notes v14.0.5, addendum 2.15, R-4 (line 1769 'the final QA report and RCA')
* Change type: NEW_CANON (template field; context drainage)
* Operation: `REPLACE`
* Target document: `PF27-Canon-Plan-Templates`
* Section path: "# **A) Glow Plan and Runbook Templates**" > "## **9\) Final QA Closeout Review \+ QA RCA (Template; REVIEW mode only)**" > "### **Required structure (paste-ready)**"
* Original location (informative): line 3232
* Action: `REPLACE ONCE` the OLD block with the NEW block
* Expected occurrence of OLD in the whole original: 1
* First boundary and last boundary: the single original line 3232, which is the whole OLD block
* Rationale: R-4 requires the final QA report and RCA to carry the live-test line; the field is added to the QA Closeout Summary after the Epic reviewed field.
* OLD: 22 bytes, SHA-256 `71873dafc9395a410d3c649da9c87521e2e9b380be53c8f47d110c7045ac0802`; lines ending with two spaces: line 1

````text
* **Epic reviewed:**  
````

* NEW: 149 bytes, SHA-256 `8dd7b3a081d171aede14216b153a2fc3661b32d842ad27cf8324d05cd83af66a`; lines ending with two spaces: lines 1, 2

````text
* **Epic reviewed:**  
* **Live test:** `RAN` (and its evidence references), `WAIVED` (and the Product Owner's quoted words and date), or `MISSING`  
````

## Redline RL-14

* Redline number: RL-14
* Ledger rows: C-26
* Source items: HDE Build Notes v14.0.5, addendum 2.15, R-4 (table row 'Final QA report | No PASS verdict', line 1780)
* Change type: NEW_CANON (template rule; context drainage)
* Operation: `REPLACE`
* Target document: `PF27-Canon-Plan-Templates`
* Section path: "# **A) Glow Plan and Runbook Templates**" > "## **9\) Final QA Closeout Review \+ QA RCA (Template; REVIEW mode only)**" > "### **Required structure (paste-ready)**"
* Original location (informative): line 3447
* Action: `REPLACE ONCE` the OLD block with the NEW block
* Expected occurrence of OLD in the whole original: 1
* First boundary and last boundary: the single original line 3447, which is the whole OLD block
* Rationale: R-4 gives the final QA report no PASS verdict when the live-test line reads MISSING. The verdict field keeps its four values and gains that rule.
* OLD: 64 bytes, SHA-256 `075c97caf8257a26c958468f1eebe8003eb0d5619cc9ea4622b29646d0ed3050`; lines ending with two spaces: line 1

````text
* **Verdict:** PASS | READY WITH CAVEATS | NOT READY | BLOCKED  
````

* NEW: 115 bytes, SHA-256 `ad27eadba3cacbe04a33f03b707f95f91cced730e9f01a04462326bc433bb662`; lines ending with two spaces: line 1

````text
* **Verdict:** PASS | READY WITH CAVEATS | NOT READY | BLOCKED (not PASS when the live-test line reads `MISSING`)  
````

## Redline RL-15

* Redline number: RL-15
* Ledger rows: C-26
* Source items: HDE Build Notes v14.0.5, addendum 2.15, R-4 (line 1771 'the closure decision'; table row 'Closure decision | Not CLOSE', line 1782)
* Change type: NEW_CANON (template field; context drainage)
* Operation: `REPLACE`
* Target document: `PF27-Canon-Plan-Templates`
* Section path: "# **A) Glow Plan and Runbook Templates**" > "## **10\) Epic Closure Review \+ Retrospective (Template; REVIEW mode only)**" > "### **Required structure (paste-ready)**"
* Original location (informative): line 3560
* Action: `REPLACE ONCE` the OLD block with the NEW block
* Expected occurrence of OLD in the whole original: 1
* First boundary and last boundary: the single original line 3560, which is the whole OLD block
* Rationale: R-4 requires the closure decision to carry the live-test line and makes it not CLOSE on MISSING. This template records the epic closure decision, so the field is added after it.
* OLD: 30 bytes, SHA-256 `6b6dbd0a66a3010eba79a1d6e9604a72e199b38e2d7324582da22ec441471512`; lines ending with two spaces: line 1

````text
* **Epic closure decision:**  
````

* NEW: 209 bytes, SHA-256 `3510afc2d3720ec4beb9e2321a7a0a4a9c42331b928098287fc2fc134a569be2`; lines ending with two spaces: lines 1, 2

````text
* **Epic closure decision:**  
* **Live test:** `RAN` (and its evidence references), `WAIVED` (and the Product Owner's quoted words and date), or `MISSING`. With `MISSING`, the closure decision is not CLOSE.  
````

## Batch check

| Redline | Original lines | OLD count (expected / observed) | Span start–end (character offsets in the original) |
| :---- | :---- | :---- | :---- |
| RL-01 | 112 | 1 / 1 | 8497–8772 |
| RL-02 | 287 | 1 / 1 | 27086–27420 |
| RL-03 | 326 | 1 / 1 | 30064–30143 |
| RL-04 | 389 | 1 / 1 | 35357–35434 |
| RL-05 | 973 | 1 / 1 | 88968–89193 |
| RL-06 | 1168 | 1 / 1 | 134106–134961 |
| RL-07 | 1312 | 1 / 1 | 161547–162110 |
| RL-08 | 1450–1453 | 1 / 1 | 176395–178345 |
| RL-09 | 1459 | 1 / 1 | 180321–180705 |
| RL-10 | 2261 | 1 / 1 | 245520–245578 |
| RL-11 | 3120 | 1 / 1 | 278628–278711 |
| RL-12 | 3218 | 1 / 1 | 284474–284820 |
| RL-13 | 3232 | 1 / 1 | 284997–285019 |
| RL-14 | 3447 | 1 / 1 | 295485–295549 |
| RL-15 | 3560 | 1 / 1 | 300089–300119 |

No two spans intersect or share a boundary, no redline anchors on text another redline produces, and the 15 redlines apply in one pass against the unchanged original. The proof log records the validation and the one-pass simulation.

END OF REDLINES
