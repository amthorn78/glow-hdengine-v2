# PF04-Canon-HDE-Governance v2.8.8 — redlines — gtwpe-20261101-pf10-v14-0-5 (T-01)

## 1. Package identity

| Field | Value |
| :---- | :---- |
| Redlines file | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF04/PF04-Canon-HDE-Governance-v2.8.8.redlines.gtwpe-20261101-pf10-v14-0-5.md` |
| Proof log | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF04/PF04-Canon-HDE-Governance-v2.8.8.redlines.gtwpe-20261101-pf10-v14-0-5.proof-log.md` |
| Preparation outcome | `READY`. Save completeness is recorded in the proof log's save-verification receipt. |
| Run identity | `gtwpe-20261101-pf10-v14-0-5/T-01/drain-1`, prepared 2026-11-02 |
| Prompt | TW-DRAIN-10 — Prepare PF Document Redlines — 100926.1 (Notion page `3f44590a05eb8172a314fe6b958bb9ff`, page last edited 2026-10-09T11:05:22.094Z), fetched live when this step began |
| Originating preparer | The executing document agent in the Claude Code session Nathan started for T-01 (session `session_01Q789tyrM8bruo2RGNCMLM8`). No subagent, reviewer or other session took part. |
| Original target | `docs/pfcanon/PF04-Canon-HDE-Governance-v2.8.8.md` read at `origin/main` `e2b7427ff418ca8f08f05587c4a541308a76da56`. In-document title `PF04-Canon-HDE-Governance`; version v2.8.8; git blob `0c3ce100f9429435bce8e021f36e405120159e4a`; SHA-256 `7a50dbe3d4eb67a1d01bab89e55d6ed0c0570258b5f7b9c4251626277c76ee72`; 580,196 bytes; 4,748 LF-terminated lines; no CR byte. The same blob is on `origin/main` `84d6d1cad95c67788336d174dc4b8922d9bb0cb2`. |
| Source | `docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md`, HDE Build Notes v14.0.5; git blob `9df074d90b59fe783c32f7cb3db25872d5dfe9d2`; SHA-256 `cea605d0475889bd9120a51947e23176ce7d2308eb5ab4503b040fd68ddf669d`; 385,734 bytes; read at `origin/main` `e2b7427`, unchanged at `84d6d1c` |
| Selected source units | 2.1 D-3 (lines 345–396), D-4 (397–450), D-5 (451–490) and context (205–224, 491–516); 2.2 status, R-1 and R-2 (517–546); 2.8 decisions and stated limits (1063–1106), drainage table and note (1111–1127), and the 2026-11-01 amendment (1060); 2.15 status and R-1 to R-6 (1650–1804); 2.16 status, R-1 and R-2 (1869–1939) |
| Supporting reading (not drain scope) | 2.8 lines 1048–1062, 1107–1110 and 1128–1145; 2.9 lines 1146–1229; 2.15 lines 1805–1868; 2.16 lines 1940–1976; PF03 Technical Writing Best Practices v1.8.8 (editorial standard) |
| Ledger | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/LEDGER.md` at commit `142feb35144d8795f927e0c78b665ace52279064`; task T-01; rows C-03, C-04, C-05, C-07, C-08, C-17, C-18, C-26, C-29; supporting C-06, C-20, C-30 |
| Branch and PR | `claude/gtwpe-triage-authoring-j94ewf`; draft PR amthorn78/glow-hdengine-v2#826 (open) |
| Expected final output | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF04/PF04-Canon-HDE-Governance-v2.8.9.md`, with its `.proof-log.md` beside it; TW-APPLY-10 derives the name |
| Apply diagnostic path | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF04/PF04-apply-diagnostic.gtwpe-20261101-pf10-v14-0-5.md` |

## 2. Application contract

* Every operation resolves independently against the unchanged original target in §1. Apply all fourteen in one pass by their original-bound positions; no operation's output is another's locator, and nothing is rematched on mutated text.
* Operations used: `REPLACE` (nine) and `INSERT` (five). No `DELETE`, `FIND AND REPLACE` or `FIND_AND_REPLACE` operation is used.
* `REPLACE`: the old block occurs exactly once in the whole original and is replaced by the replacement block. Nothing outside the old block is consumed.
* `INSERT`: the BEFORE anchor and the AFTER anchor each occur exactly once in the whole original, and they are contiguous: the AFTER anchor begins at the byte where the BEFORE anchor ends. That boundary is the gap. Neither anchor changes. The inserted text supplies every newline at the gap.
* Payload literals. Each literal sits in a fenced block that opens with a line of exactly four backticks followed by `text` and closes with a line of exactly four backticks. The literal is the bytes strictly between the line feed that ends the opening fence line and the line feed that immediately precedes the closing fence line; that last line feed is a delimiter, not part of the literal. An empty first line inside a fence is therefore a leading line feed, and an empty last line is a trailing line feed. No literal contains a run of four backticks. Trailing spaces are significant: the target ends each non-final list item with two spaces, and the literals keep that convention.
* Every literal states its UTF-8 byte length and SHA-256. A mismatch is an authoring defect for the preparer, not for the applier to normalize.
* Non-overlap. The fourteen original spans are disjoint, and no insertion gap touches a replaced span. The proof log records each span's original byte offsets and the one-pass simulation.
* Document-control fields are reserved for TW-APPLY-10. No redline edits original lines 5–10 (`**Title:**`, `**Version:**`, `**Status:**`, `**Effective date:**`, `**Last Update Gate:**`, `**Invocation tag:**`). Baseline values: `PF04-Canon-HDE-Governance`, `v2.8.8`, `Canon`, `2026-10-26`, `BN 13.8.8`, `` `INV-f2ac55d77ce9aacc` ``. Native schema: one `**Field:** value` line each, with two trailing spaces on every line but the last. The source that justifies this update, in source order, is `PF10-HDE-Build-Notes-v14.0.5.md`, HDE Build Notes v14.0.5; it is the only source. The original states its own version and date nowhere else except as history in the §9.3.1 log, which no redline changes.
* Change history. RL-10 adds the PF04 §9.3.1 entry that PF04 §9.3 requires for every normative change. It names version v2.8.9, the baseline v2.8.8 bumped once by the log's own patch scheme (v2.8.7 to v2.8.8), and 2026-11-02, the preparation date, in its `Date / Author` field. If TW-APPLY-10 derives a different version, the package returns to its preparer.
* Hygiene. The original carries no `Draft` status language, TODO, unresolved drafting note or editorial comment outside canon-required template or history text, so no hygiene redline is included (proof log §6).

## 3. Redlines

### RL-01 — REPLACE

- Operation: `REPLACE`
- Ledger rows: C-05 (with C-06 context)
- Change type (report classification): CANON_UPDATE
- Location (original-baseline heading path): "# **2\. Acceptance Policy — A3–A4–A7 \[Required-Now\]**" > "## **2.0 Acceptance Tokens (single-home roster) \[Required-Now\]**" > "### **2.0.10 Env / rails / infra**", list item beginning "* **LOGS\_KEYS\_ONLY\_OK** —" under "*Observability & privacy tokens.*"
- Original-baseline lines (informative only, not a locator): 584
- Scope: whole PF; expected occurrences: old block 1; observed: 1
- Controlling source: HDE Build Notes v14.0.5, 2.1 D-5 (lines 451-490), "Decision" and "Canon superseded or added to" (HDE Governance §2.0.10 LOGS_KEYS_ONLY_OK added to); context 2.1 status and nonclaims (lines 205-224, 491-516)
- Effect: Names governed gate check rows as governed logs and adds the D-5 row-content rule as a nested item.

- Old block (207 bytes, SHA-256 `a2c3ae2607340fd3230a58870d3261d74f52f49cc2fce168560e841306c9d005`):

````text
* **LOGS\_KEYS\_ONLY\_OK** — Governed logs (including A7 proofs, BodyGraph diagnostics, and ops probes) are keys-only: no payload values, no PII. Payload bytes and PII must never appear in governed logs.  
````

- Replacement block (932 bytes, SHA-256 `08e118726d876248efc329f6eefa00b35880d37d7404922d18d0a1a56f04fd98`):

````text
* **LOGS\_KEYS\_ONLY\_OK** — Governed logs (including A7 proofs, BodyGraph diagnostics, ops probes, and governed gate check rows) are keys-only: no payload values, no PII. Payload bytes and PII must never appear in governed logs.  
  * **Governed gate check rows.** Each row of `audit/gates/json_gate/canonical/json_gate_check_log.ndjson` and `audit/gates/json_gate/canonical/json_gate_compare_log.ndjson`, and of any other gate family that **HDE-Schemas & Artifacts** governs, is a governed log under this token and §7.1. Each issue entry is a closed token; an exception contributes its type name at most, as `validation_error:<ExceptionType>`. No row carries exception message text, library message text or a stack trace. Every path a row records is repository-relative (§2.0.6); no row carries an absolute or machine-local path. Detail for diagnosing a failing run goes to the tool's stderr, which is not governed evidence.  
````

### RL-02 — REPLACE

- Operation: `REPLACE`
- Ledger rows: C-18 (amendment B-1; with C-17, C-20 support)
- Change type (report classification): CANON_UPDATE
- Location (original-baseline heading path): "# **2\. Acceptance Policy — A3–A4–A7 \[Required-Now\]**" > "## **2.0 Acceptance Tokens (single-home roster) \[Required-Now\]**" > "### **2.0.19 QA bootstrap & harness (EPIC021+)**" > list item beginning "* **Close report minimal content (normative).**" > nested item "**Tracked-issue items under the generic v2 writer.**"
- Original-baseline lines (informative only, not a locator): 914
- Scope: whole PF; expected occurrences: old block 1; observed: 1
- Controlling source: HDE Build Notes v14.0.5, 2.8 (lines 1048-1145): 2026-11-01 amendment B-1 (line 1060), stated limit on tracked issues (line 1099), and the unapportioned drainage note (line 1127); supporting 2.9 B-1 (lines 1146-1229)
- Effect: Adds the accepted tracked-issue ID forms after the form (b) citation; the rest of the item is unchanged.

- Old block (472 bytes, SHA-256 `8fd8a95a204b3c94b5a5662c2b76f1b665b46d7c8ca0afb944a99a745f4b67ca`):

````text
  * **Tracked-issue items under the generic v2 writer.** The v2 writer renders each tracked-issue item only as an ADR-status item, in the literal `ADR status line:` field, and the item's ID occurs in the drain-targets ledger (**Change Process Guide** §3.5.2.1, form (b)). It cannot express a TI item closed as satisfied through PF09 or PF30 pointers (form (a), with the `PF09 pointers:` and `TI-<id> pointers:` fields); such a close needs a later source-schema version.  
````

- Replacement block (613 bytes, SHA-256 `0df16da596e2fb65425112a91137ff118c70516e0d7b75a5675dd0c9078ba0da`):

````text
  * **Tracked-issue items under the generic v2 writer.** The v2 writer renders each tracked-issue item only as an ADR-status item, in the literal `ADR status line:` field, and the item's ID occurs in the drain-targets ledger (**Change Process Guide** §3.5.2.1, form (b)). A tracked-issue ID is `TI-NNN` or, for an Epic, that Epic's own `ISSUE-EPIC<NNN>-TI-<nn>`; the writer refuses an ID that names another Epic. It cannot express a TI item closed as satisfied through PF09 or PF30 pointers (form (a), with the `PF09 pointers:` and `TI-<id> pointers:` fields); such a close needs a later source-schema version.  
````

### RL-03 — INSERT

- Operation: `INSERT`
- Ledger rows: C-18 (Epic close-run family; amendment B-2, B-4) with C-17 decision 7
- Change type (report classification): CANON_UPDATE
- Location (original-baseline heading path): "# **2\. Acceptance Policy — A3–A4–A7 \[Required-Now\]**" > "## **2.0 Acceptance Tokens (single-home roster) \[Required-Now\]**" > "### **2.0.19 QA bootstrap & harness (EPIC021+)**" > list item beginning "* **Close report minimal content (normative).**" > "  * Same-run evidence pointer rule.  "
- Original-baseline lines (informative only, not a locator): gap between 978 and 979
- Scope: whole PF; expected occurrences: gap 1 (BEFORE and AFTER each 1, and contiguous 1); observed: 1
- Controlling source: HDE Build Notes v14.0.5, 2.8: decision 7 (line 1082), stated limit on pointers (line 1100), 2026-11-01 amendment B-2 and B-4 (line 1060) and the unapportioned drainage note (line 1127); drainage-table row for HDE Governance (line 1121)
- Effect: Adds one nested item after the existing same-run evidence pointer rule and before the key_outputs shape item.

- BEFORE anchor (332 bytes, SHA-256 `2e78f0a12e19efb8eda14805ebfd7236a0adbb7dadf73affc9ed8f3085e799b2`):

````text
    * When the close slice touches the Evidence Index, hash sentinel, machine mirror, or their required proof companions, the close report MUST point directly, or via the manifest \`key\_outputs\` or token/evidence matrix, to the same-run gate or QA log evidence that proves the write/check workflow actually executed and passed.  

````

- AFTER anchor (56 bytes, SHA-256 `5a187480f52134ba33d39f88bc18be095746a089882887790dff1ab6d2a0f71a`):

````text
* Close-pack manifest `key_outputs` shape (normative):  
````

- Inserted text (679 bytes, SHA-256 `eac463b1474b33025d4c79a02dc9681adaed878842fd5bf3dec20d0d40b26a08`):

````text
    * For a v2 close pack, the same-run evidence of the close run is the change's post-verdict close-run family under `audit/qa/<change-dir>/close/`, which the canonical updater publishes after the close pack is written. The close report's pointer to that directory meets this rule, and it may name the directory before the close run writes it: a CRD's close report MUST name it, and an Epic's close report MAY. Only an admitted CRD, and an Epic whose close run the Product Owner has explicitly admitted, has a close-run family. **HDE-Schemas & Artifacts** records the family's path and post-verdict status, and **Change Process Guide** names it as the same-run evidence home.  

````

### RL-04 — REPLACE

- Operation: `REPLACE`
- Ledger rows: C-26 (2.15 R-1, R-2, R-5; R-6 represented), C-30 support
- Change type (report classification): CANON_UPDATE
- Location (original-baseline heading path): "# **3\) Rails & Environments (Vendor posture) \[Required-Now\]**" > "## **3.4 Open rails (controlled) \[Required-Now\]**", from "**Production-functional epic live-proof requirement.**" through the "**Other production-affecting scope.**" paragraph
- Original-baseline lines (informative only, not a locator): 1192–1200
- Scope: whole PF; expected occurrences: old block 1; observed: 1
- Controlling source: HDE Build Notes v14.0.5, 2.15 status and R-1 to R-6 (lines 1650-1804), with its "Relation to other canon" (lines 1666-1682) and dependencies (line 1846: HDE Governance §3.4, R-1, R-2 and R-5); supporting 2.16 R-3 (lines 1940-1947)
- Effect: Places the live compat test, the Product Owner-only waiver and the blocked-test rule before the existing live-proof rules and aligns those rules with them.

- Old block (3393 bytes, SHA-256 `b79013f6b085dc4e946fb3094a43428760f0489ef98c4275d6d88f8ecfc3c33f`):

````text
**Production-functional epic live-proof requirement.** Every QA plan for an epic touching any surface used to produce a production feature that PF canon describes as functional MUST include an open-rails test. The test MUST make a live vendor call under `SAFE_MODE=0` and `ALLOW_NETWORK=1`, using synthetic data only, with no real person, user or production data. Identification of the affected surfaces remains with the epic's Specification and plans. A plan without this test is not approval-ready.

Closed-rails tests, fixture replay, mocks or fake services, static analysis, generated or governed evidence artifacts, path-proof validation, Index or Mirror refresh, repository inspection, review approval, an unrun smoke procedure, and OPS discovery without a live vendor call do not satisfy this requirement. A non-vendor deployed-service check or database read does not satisfy it by itself. An exemption or closed-rails-only approval does not replace the required test within this scope. Any question about retaining an exemption ground remains for Product Owner determination; it is not permission to omit the test.

The live vendor step retains task-specific Product Owner authorization where secrets or external services are involved, a defined request limit, explicit step-local rails, synthetic inputs, redaction, secret scanning and quarantine, trustworthy evidence, stop checks and failure classification before any product-failure conclusion. It authorizes no load, stress or volume testing and raises no request limit. Open-rails Ops evidence remains Ops evidence; including or referencing it does not convert it into QA evidence.

A passing test proves only the behavior it exercises. It does not establish full vendor conformance, whole-change QA PASS, acceptance, PF09 movement, deployment, release activation, epic closure, public Reader behavior changes, new routes or flags, or PF-canon drainage.

**Other production-affecting scope.** Outside the mandatory production-functional scope above, the standing broader requirement remains: an epic that can affect production surfaces, public or app-facing behavior, runtime compute, vendor ingest, HumanDesignAPI calls, external API integrations, database persistence or retrieval, DB bridge behavior, deployed service behavior, environment-variable or secret binding, request shaping, response mapping, authentication or authorization, production-used CLI/API behavior, queues, workers, jobs, schedulers, runtime services or another path that must work outside isolated fixtures requires at least one bounded open-rails live QA step before acceptance unless an explicit approved exemption is recorded. The step proves a real production-relevant behavior the epic can affect, retains the existing authorization and evidence controls, and is clear about its limits. Closed-rails-only QA is not approval-ready for that broader scope without the explicit exemption. A valid exemption states why no open-rails behavior can be safely or meaningfully exercised, the authorizing owner, accepted risk, substitute proof and why it is sufficient, the production claim withheld and any future live-proof obligation. Silence, reviewer preference, convenience or closed-rails success is not an exemption. This retained broader rule supplies no exemption from the mandatory synthetic-data live vendor test for production-functional surfaces.
````

- Replacement block (7497 bytes, SHA-256 `2df2572abaf8bd204e554b3b23ce658dd3998f7de4cf2f7193230ae0934d5118`):

````text
**Every Epic's Live QA runs the live compat test.** Every Epic's QA plan includes, and its QA run executes, the live compat test below, whatever the Epic changed and whether or not its own surfaces are on a production path. Compat is the product: a QA verdict that has not seen compat work live says nothing about the product. This rule covers Epics; whether a CRD that changes runtime code also runs the test is undecided and remains the Product Owner's decision.

* **Live vendor compat.** `hdctl showcompat --source vendor` runs under `SAFE_MODE=0` and `ALLOW_NETWORK=1`, step-local, on synthetic birth data only, at the Epic's QA execution source. It runs at least two distinct pairs, each as AB and as BA, and runs one pair twice. It passes only when each output has the canonical result shape and the release identity of the source, AB and BA are byte-identical, the two runs are byte-identical, the Reader bytes stay `{id, band}` only, and the two pairs produce different results.  
* **Deployed-service check.** The check compares the production HD Engine's `/internal/version` release identity with the release on `main`, and has the production Reader score the two synthetic stored people, SYN-A and SYN-B, in both orders for each Reader version. It passes only when each answer is eligible and bands-only and AB and BA are byte-identical. A mismatch between the deployed release and `main`, and a difference between the deployed bands and the CLI bands for the same birth data, are reported as findings with the QA result.  
* **The two synthetic stored people.** The production Reader scores only people whose charts are stored in the production database, so two synthetic people are kept there as permanent QA fixtures under fixed UUIDs: SYN-A, `9cff60ae-6eb6-5618-aec5-8acaa4f290d2` (`uuid5(NAMESPACE_URL, "hde-live-qa-synthetic-a")`), born 1990-01-01 at 12:00 in Amsterdam, Netherlands; and SYN-B, `57f0c055-ff09-5fdb-aedb-def880437e6f` (`uuid5(NAMESPACE_URL, "hde-live-qa-synthetic-b")`), born 1985-07-15 at 08:30 in London, United Kingdom. They are stored through the engine's own write path under the Product Owner's write authorization. If either is missing when a QA run starts, the deployed-service check is `TOOLING_BLOCKED` until it is stored again.  
* **The Epic's own live surfaces.** An Epic whose own surfaces are on a production or vendor path also runs at least one open-rails step that exercises those surfaces live, under the production-functional and production-affecting rules below.  
* **Ops evidence and stage records.** The live compat test and the deployed-service check are Ops evidence under this section, and the execution controls below apply to them in full. **Change Process Guide**, **Glow QA Guide** and **Plan Templates** govern how each QA and closure stage plans, records and enforces the live test.

**Only the Product Owner can waive any part of the live test.** Only the Product Owner may decide that the live test of this section, or any part of it, does not apply to an Epic.

* **Recorded waiver.** A waiver is written and specific to the change. It quotes the Product Owner's words with their date and states the reason, the accepted risk, the substitute proof and why it suffices, the claim withheld and any later live-proof obligation.  
* **An agent's finding is a question.** An agent may find that an Epic's surfaces are not on a live path, or that the live test cannot be run meaningfully. Either finding is put to the Product Owner as a named decision no later than QA-10 readiness, and the QA plan is not approval-ready until the Product Owner answers.  
* **Not a waiver.** Silence, reviewer agreement or preference, convenience, closed-rails success or a finding of non-applicability is not a waiver. Without a recorded waiver, the live test applies in full.

**A live test that cannot run blocks; it does not pass.** A live test that cannot run is `TOOLING_BLOCKED`, including for missing credentials, missing target facts, an unavailable vendor or a missing authorization. The Epic waits: a blocked live test is never converted into a PASS, a waiver or a closure, and the Product Owner decides how to proceed.

**Production-functional epic live-proof requirement.** Every QA plan for an epic touching any surface used to produce a production feature that PF canon describes as functional MUST include an open-rails test. The test MUST make a live vendor call under `SAFE_MODE=0` and `ALLOW_NETWORK=1`, using synthetic data only, with no real person, user or production data. The epic's Specification and plans identify the affected surfaces; a finding that the epic touches no such surface is a question for the Product Owner under the waiver rule above. A plan without this test is not approval-ready.

Closed-rails tests, fixture replay, mocks or fake services, static analysis, generated or governed evidence artifacts, path-proof validation, Index or Mirror refresh, repository inspection, review approval, an unrun procedure, and OPS discovery without a live vendor call do not satisfy the live compat test or this requirement. A non-vendor deployed-service check or database read does not satisfy either by itself. Only a recorded Product Owner waiver under the rule above removes any part of a required test; another exemption or a closed-rails-only approval does not replace it.

Each live step, including the live compat test and the deployed-service check, retains task-specific Product Owner authorization where secrets or external services are involved, a defined request limit, explicit step-local rails, synthetic inputs, redaction, secret scanning and quarantine, trustworthy evidence, stop checks and failure classification before any product-failure conclusion. It authorizes no load, stress or volume testing and raises no request limit. Open-rails Ops evidence remains Ops evidence; including or referencing it does not convert it into QA evidence.

A passing test proves only the behavior it exercises. It does not establish full vendor conformance, whole-change QA PASS, acceptance, PF09 movement, deployment, release activation, epic closure, public Reader behavior changes, new routes or flags, or PF-canon drainage.

**Other production-affecting scope.** Outside the mandatory production-functional scope above, the standing broader requirement remains: an epic that can affect production surfaces, public or app-facing behavior, runtime compute, vendor ingest, HumanDesignAPI calls, external API integrations, database persistence or retrieval, DB bridge behavior, deployed service behavior, environment-variable or secret binding, request shaping, response mapping, authentication or authorization, production-used CLI/API behavior, queues, workers, jobs, schedulers, runtime services or another path that must work outside isolated fixtures requires at least one bounded open-rails live QA step before acceptance unless the Product Owner has waived it under the waiver rule above. The step proves a real production-relevant behavior the epic can affect, retains the existing authorization and evidence controls, and is clear about its limits. Closed-rails-only QA is not approval-ready for that broader scope without a recorded waiver. A valid waiver of this step also states why no open-rails behavior can be safely or meaningfully exercised. This retained broader rule supplies no waiver of the live compat test or of the mandatory synthetic-data live vendor test for production-functional surfaces.
````

### RL-05 — INSERT

- Operation: `INSERT`
- Ledger rows: C-03 (2.1 D-3, with C-06 context)
- Change type (report classification): CANON_UPDATE
- Location (original-baseline heading path): "# **4\) Evidence & Artifacts \[Required-Now\]**" > "## **4.1 Classes of evidence \[Required-Now\]**" > "### **4.1.4 Rails posture — closed refusal; open conformance**", block "**Dev/admin APP\_ENV gating (dev/test/local only) NEW CANON.**"
- Original-baseline lines (informative only, not a locator): gap between 1313 and 1314
- Scope: whole PF; expected occurrences: gap 1 (BEFORE and AFTER each 1, and contiguous 1); observed: 1
- Controlling source: HDE Build Notes v14.0.5, 2.1 D-3 (lines 345-396), "Decision" and "Canon superseded or added to" (HDE Governance §4.1.4 added to; §8.3 unchanged); context lines 205-224 and 491-516
- Effect: Adds the compat-namespace block after the dev/admin gating rule and before the determinism env pins harness block.

- BEFORE anchor (214 bytes, SHA-256 `8028d24d2a61cdf51bac8d53fa43ff397abd8df8d4965e4e45fef2e9118b6555`):

````text
This `APP_ENV` gating is a precondition for treating any dev/admin-only surface as “on-rails”; it couples to `ENV_RAILS_POLICY_OK` in §2.0.10 and applies regardless of whether vendor rails are open or closed.

````

- AFTER anchor (46 bytes, SHA-256 `6b4887726f96e9fee6f7f2b9fa50e511732451bbf8bf8da037a540500780752e`):

````text

**Determinism env pins harness (EPIC018 D2)**
````

- Inserted text (1646 bytes, SHA-256 `802d3bbbdaf290a8da15b70030c6e3f71af55ece2e42e3873bf5161b3abc898e`):

````text

**Compat namespace (dev/admin surface).** The compat namespace, `/api/compat/v1` and its descendants, is a dev/admin-only surface under this rule.

* **Gate order.** On every method, the gate runs before any compat computation, database read or vendor call. A production-like posture, as **HDE-CLI-API-Vendor-Ref** resolves it, keeps that route's not-found response. Any other request is served only when `APP_ENV` is exactly `dev`, `test` or `local`, with no trimming, no case-folding and no default; a missing, empty or other value receives the writer-style refusal envelope that the dev/admin HTTP surfaces use. `ENGINE_ENV` never admits the surface.  
* **No credential while gated.** No credential is required while the surface is admitted only under those `APP_ENV` values, as for every other dev/admin surface under this rule. The admin-bundle scope of §8.3 is unchanged.  
* **Wider exposure.** Before the compat route is served in any other environment, a later decision MUST require the admin credential of §8.3.2, or an equivalent credential pinned in **HDE-CLI-API-Vendor-Ref**, and MUST add the logging rules of §8.3.4.  
* **Accepted residual risk.** A dev, test or local process connected to the shared production database serves stored-user compat results to whoever reaches its port. Where the process listens, under the loopback access that **Glow Infrastructure** documents, controls that exposure; this route does not. It is the same posture as every other dev/admin surface.  
* **Exact bytes.** The compat route's status codes, error codes, headers, method rules and probe rules are owned by **HDE-CLI-API-Vendor-Ref**.

````

### RL-06 — INSERT

- Operation: `INSERT`
- Ledger rows: C-04 (2.1 D-4, sanity-pipeline part, with C-06 context)
- Change type (report classification): CANON_UPDATE
- Location (original-baseline heading path): "# **4\) Evidence & Artifacts \[Required-Now\]**" > "## **4.1 Classes of evidence \[Required-Now\]**" > "### **4.1.8 Sanity pipeline & evidence skeleton (EPIC018+)**" > block "**Sanity log artifact (records-only; governed).**"
- Original-baseline lines (informative only, not a locator): gap between 1394 and 1395
- Scope: whole PF; expected occurrences: gap 1 (BEFORE and AFTER each 1, and contiguous 1); observed: 1
- Controlling source: HDE Build Notes v14.0.5, 2.1 D-4 (lines 397-450), "Decision for the sanity pipeline" and "Canon superseded or added to" (HDE Governance §4.1.8 "Sanity log artifact" added to); context lines 205-224 and 491-516
- Effect: Adds the --log-path bound as the last list item of the sanity-log block.

- BEFORE anchor (147 bytes, SHA-256 `c3ebc6e5b021dcf5f6674dfa5dbe065baa31c49aab02e81f4c672ca8c0a0fc24`):

````text
* The log **MUST NOT** include timestamps, wall-clock data, or env-dependent noise that would break determinism. It is LF-terminated and BOM-free.

````

- AFTER anchor (39 bytes, SHA-256 `b2808947a0c7a98894086a3efbdf4b87c44521f21dca8e26177cf3fad29329dd`):

````text

**Coupling to the evidence skeleton.**
````

- Inserted text (460 bytes, SHA-256 `f2a729edca58ede5f60fd2ac81dc818acd6c5777df2a35a00ed1a38e3bf81b9a`):

````text
* **`--log-path` bound.** A `--log-path` target inside the repository is accepted only when it is the canonical log `audit/gates/sanity_pipeline/sanity_pipeline.log`. A target outside the repository is accepted only when it is not a symlink, no component of its path is a symlink, its parent directory exists, and it names a regular file or no existing file. A refused target fails with a typed, numeric-free error before any step runs or any byte is written.

````

### RL-07 — INSERT

- Operation: `INSERT`
- Ledger rows: C-08 (2.2 R-2)
- Change type (report classification): NEW_CANON
- Location (original-baseline heading path): "# **9\) Change Management — Doc-Delta Hooks & Merge Gates \[Required-Now\]**" > "## **9.1 Single-home doctrine (routing by title)**" > "### **9.1.2 Canon precedence and persistent sources \[Required-Now\]**"
- Original-baseline lines (informative only, not a locator): gap between 2439 and 2440
- Scope: whole PF; expected occurrences: gap 1 (BEFORE and AFTER each 1, and contiguous 1); observed: 1
- Controlling source: HDE Build Notes v14.0.5, 2.2 status and relation to other canon (lines 524-525) and R-2 (lines 540-546)
- Effect: Adds the stable-identity rule after the persistent-authority paragraph.

- BEFORE anchor (676 bytes, SHA-256 `94770e17f7da77c8a6440d9d0ae4d72eea5b54a2b690d03a8c0654453875ee16`):

````text
The persistent PF authority is `docs/pfcanon/` on `main`. Each document keeps the standing it declares; the current version is the version there, and repository history retains superseded versions after they leave that directory. Native Google Docs, Markdown exports, Drive folders, Notion pages and PF-named files elsewhere in the repository confer no PF authority. Adoption does not prove content approval, implementation, QA acceptance or closure. Resolving repository canon grants no tool, credential, network, rails, mutation or privileged-action permission; agents may edit PF canon only under the Product Owner's exact authority for the identified document and action.

````

- AFTER anchor (61 bytes, SHA-256 `986c8a00d95492ab5d228cd310ca4f72e6a6f1997a31cc9afa2034b733db460f`):

````text

At the start of each task and whenever its subject changes, 
````

- Inserted text (881 bytes, SHA-256 `a0b995b37e9a436ac7e48883a77856c980791de70619fd43be8c682fd0e50e71`):

````text

**PF-Canon is resolved by stable identity, never by version.** PF-Canon document versions, and therefore file names, may change at any time. No code, test, tool, CI step, schema, governed artifact or committed record that must remain valid pins a PF document's file name, version or content digest, or requires its bytes to stay unchanged. A tool that needs current canon resolves the document when it runs, by PF identity and versionless title, to the one current file under `docs/pfcanon/`, and refuses when that resolution is not unique. Validation of an already committed artifact does not re-read canon. A citation of canon in code, a test, a tool, an ADR or a governed artifact names the PF document by title, and its section where needed; **HDE Build Notes** is cited by title alone, without an addendum number, because its addendum numbers restart with each base version.

````

### RL-08 — INSERT

- Operation: `INSERT`
- Ledger rows: C-07 (2.2 status and R-1)
- Change type (report classification): NEW_CANON
- Location (original-baseline heading path): "# **9\) Change Management — Doc-Delta Hooks & Merge Gates \[Required-Now\]**" > "## **9.1 Single-home doctrine (routing by title)**" > "### **9.1.2 Canon precedence and persistent sources \[Required-Now\]**"
- Original-baseline lines (informative only, not a locator): gap between 2443 and 2444
- Scope: whole PF; expected occurrences: gap 1 (BEFORE and AFTER each 1, and contiguous 1); observed: 1
- Controlling source: HDE Build Notes v14.0.5, 2.2 status and relation to other canon (lines 524-525) and R-1 (lines 533-539)
- Effect: Adds the planning-only rule after the in-flight documents paragraph.

- BEFORE anchor (430 bytes, SHA-256 `69fa9d7500c7f9c8b6f79ff7f32794753640b6329f128188753f09038a8bcdd3`):

````text
In-flight documents in `docs/ephemeral/` are canon for their change: the approved Specification is its permanent intended-scope authority; approved Plans are working execution direction; actual reviews and Product Owner dispositions govern within their scope. Use current versions, preserve superseded history and apply the **Plan Templates** canon-precedence rule for conflicts. No Specification write is implied by PF drainage.

````

- AFTER anchor (61 bytes, SHA-256 `c24642fd7803b496168213c1329bd4fa74899429ffdc73514f7af9314028343c`):

````text

The Notion development board remains operational metadata. B
````

- Inserted text (1039 bytes, SHA-256 `443dad2296000c2c86ff83bca97f1faac98a816147dcef9b7367ae6c34f59d89`):

````text

**Planning documents serve planning only.** A planning document is any change-process work product stored under `docs/ephemeral/`: Specifications, Plans, instructions, reviews, reports, RCAs, readiness records, dispositions, handoffs and result records. No code, test, tool, CI step, workflow, schema, governed evidence artifact, close pack, manifest, Index or Mirror row or path proof reads, binds, hashes, resolves or requires a path under `docs/ephemeral/`; a test builds any document it needs as its own fixture. A fact a later stage needs from a planning document is recorded where that stage reads it, when it is recorded: for a close pack, in the close-candidate source, as a record text naming the document's identity and SHA-256, and as the structured facts the writer checks (requirement IDs, QA plan checks and their mapped criteria, and the QA verdict). A prose citation of a planning document in a permanent record is a reference only; archiving or deleting the cited document invalidates nothing that depends on the record.

````

### RL-09 — REPLACE

- Operation: `REPLACE`
- Ledger rows: C-07 (2.2 R-1)
- Change type (report classification): CONSISTENCY
- Location (original-baseline heading path): "# **9\) Change Management — Doc-Delta Hooks & Merge Gates \[Required-Now\]**" > "## **9.1 Single-home doctrine (routing by title)**" > "### **9.1.3 Artifact storage and execution-surface selection \[Required-Now\]**", table row beginning "| `REPOSITORY_CONTROLLED` |"
- Original-baseline lines (informative only, not a locator): 2452
- Scope: whole PF; expected occurrences: old block 1; observed: 1
- Controlling source: HDE Build Notes v14.0.5, 2.2 R-1 (lines 533-539); consistency pointer in the storage section
- Effect: Appends one routing sentence to the REPOSITORY_CONTROLLED row; the rest of the row is unchanged.

- Old block (497 bytes, SHA-256 `63b9f4328895004a43654e90c7997a158c0f08cc4fc2e8713b36c0e607c26337`):

````text
| `REPOSITORY_CONTROLLED` | Intake, kickoff, Specifications, Plans, audits, triage, readiness records, Guides, instructions, tasks, reviews, reports, RCAs, remediation, handoffs, redlines, dispositions, drainage, closure and retrospective work products belong under `docs/ephemeral/`. Persistent prompt-ecosystem management records belong under `docs/prompt_ecosystem_management/`. Code, tests, configuration and governed evidence retain their established paths, writers and integrity contracts. |
````

- Replacement block (590 bytes, SHA-256 `9334e3f0c40370e4c3b70006c4a6109ba38cdbad6203ae68be6eaa74f88162bb`):

````text
| `REPOSITORY_CONTROLLED` | Intake, kickoff, Specifications, Plans, audits, triage, readiness records, Guides, instructions, tasks, reviews, reports, RCAs, remediation, handoffs, redlines, dispositions, drainage, closure and retrospective work products belong under `docs/ephemeral/`. Persistent prompt-ecosystem management records belong under `docs/prompt_ecosystem_management/`. Code, tests, configuration and governed evidence retain their established paths, writers and integrity contracts. Storage under `docs/ephemeral/` serves planning only; §9.1.2 governs what may depend on it. |
````

### RL-10 — INSERT

- Operation: `INSERT`
- Ledger rows: PF04 §9.3 and §9.3.1 change-history rule (for C-03 to C-08, C-17, C-18, C-26, C-29)
- Change type (report classification): DOC_HYGIENE (required change-history entry)
- Location (original-baseline heading path): "# **9\) Change Management — Doc-Delta Hooks & Merge Gates \[Required-Now\]**" > "> ## **9.3 Doc-Delta entries (what to record for any normative change)**" > "> ### **9.3.1 PF04 Governance Change Log \[Required-Now\]**"
- Original-baseline lines (informative only, not a locator): gap between 2665 and 2666
- Scope: whole PF; expected occurrences: gap 1 (BEFORE and AFTER each 1, and contiguous 1); observed: 1
- Controlling source: PF04 §9.3 and §9.3.1 (every normative PF04 change adds a Doc-Delta entry; NON_EPIC record class; GOV-YYYYMMDD-<shortslug> identity); TW-DRAIN-10 change-history rule
- Effect: Adds the v2.8.9 entry after the v2.8.8 entry, in the log's own format.

- BEFORE anchor (395 bytes, SHA-256 `6e57d70362d3ae380ee00af3cc664432ac29433f88ad260443978ef14f42d70d`):

````text
> Change Log entry (one line): v2.8.8 | GOV-20261026-gtwpe-pf04 | NON_EPIC | Scope: GCFPE TypeSafe model guidance; business case per requirement and work unit; CRD close packs and the generic v2 close-pack writer | Targets: §2.0.19, §9.1.3, §9.1.6, §9.7.7, §11.2, Appendix D.0 | Acceptance: None | Evidence: None | Freeze-pack: No | Canonical record: PF04 §9.3.1 / GOV-20261026-gtwpe-pf04

````

- AFTER anchor (57 bytes, SHA-256 `66c397ea614cb823ef0c1a7d7b7d6c495c250953ed3b8f37b56f4db9b11fa094`):

````text


> ---

> ## **9.4 Doc-Delta template \[Required-Now\]**
````

- Inserted text (4524 bytes, SHA-256 `bdc3f25a53edef6cfef3f2f179d5aeb7d2f5c0615c743ca4de236a35a4dff299`):

````text

v2.8.9 | GOV-20261102-gtwpe-pf04 | NON_EPIC | Scope: Live compat test for every Epic and Product Owner-only waiver; GATE:CORE-DET evidence and retired entries; compat namespace as a dev/admin surface; sanity-pipeline log-path bound; governed gate check rows; planning-document and PF-version independence; v2 close-run evidence and tracked-issue IDs | Targets: §2.0.10, §2.0.19, §3.4, §4.1.4, §4.1.8, §9.1.2, §9.1.3, §12.2, Appendices B.2/D.1/D.3 | Acceptance: LOGS_KEYS_ONLY_OK | Evidence: None | Freeze-pack: No | Canonical record: PF04 §9.3.1 / GOV-20261102-gtwpe-pf04

> DOC-DELTA-ID: GOV-20261102-gtwpe-pf04
>
> Date / Author: 2026-11-02 / executing document agent in Nathan's T-01 document session
>
> PF04 version: v2.8.9
>
> Record class: NON_EPIC
>
> Epic ID: NOT APPLICABLE - NON_EPIC
>
> Draft / binding surface: NOT APPLICABLE - NON_EPIC
>
> Stable record surface: PF04 §9.3.1 / GOV-20261102-gtwpe-pf04
>
> Scope: Acceptance/Evidence; Rails Enablement; Security/Logging; Governance/Documentation
>
> Targets (section anchors): §2.0.10, §2.0.19, §3.4, §4.1.4, §4.1.8, §9.1.2, §9.1.3, §12.2, Appendices B.2/D.1/D.3
>
> Summary (≤ 5 bullets):
>
> 1) Every Epic's QA runs the live compat test and the deployed-service check on SYN-A and SYN-B; only the Product Owner waives any part of it, and a live test that cannot run is `TOOLING_BLOCKED` while the Epic waits.
> 2) GATE:CORE-DET evidence is the compat-path owner tests and each live compat test run; the compat-determinism generator, the A3 identity marker, three CI jobs and four composite fixture and log entries are retired from §12.2 and Appendices B.2, D.1 and D.3.
> 3) Name the compat namespace a dev/admin surface, bound the sanity pipeline's `--log-path` target, and make governed gate check rows keys-only governed logs.
> 4) State that planning documents serve planning only and that PF-Canon is resolved by stable identity, never by version.
> 5) Name the v2 close-run family as the close report's same-run evidence, and the accepted tracked-issue ID forms.
>
> Acceptance impact (binary gates to update or verify): Every Epic's QA plan and run include the live compat test unless the Product Owner's recorded waiver removes a part of it; GATE:CORE-DET evidence binds to the compat-path owner tests and the live compat test runs, and its pass conditions are unchanged; `LOGS_KEYS_ONLY_OK` names governed gate check rows within its existing keys-only meaning; the compat namespace follows the dev/admin `APP_ENV` gate. The A3, A4 and A7 gates are unchanged. No new or satisfied token, QA verdict, OPS result or acceptance decision is claimed.
>
> Evidence updates (titles and paths only): No governed evidence artifact, golden, script, header snapshot, CI job, Human Evidence Index, hash sentinel, Machine Mirror or path proof is created or regenerated by this document revision. §12.2 and Appendices B.2, D.1 and D.3 drop the retired GATE:CORE-DET entries and name the compat-path owner tests; the retired files that remain in the repository stay as history.
>
> Freeze-pack impact: No; this document revision cuts, recomputes, activates and promotes no release and changes no release member.
>
> Routing (titles only confirmations): HDE CLI/API Vendor Ref owns the compat route's exact refusal bytes. HDE Schemas and Artifacts owns gate-family row schemas and the close-run family's path. Change Process Guide, Glow QA Guide and Plan Templates own stage enforcement of the live test and the Live QA name. HDE Build Notes supplies the scoped overrides.
>
> Rollout plan: Nathan's authorized publication of the complete revised PF is a separate manual action. No runtime staging, canary, deployment or pointer flip is performed by this revision. A document backout uses the retained v2.8.8 source through ordinary authorized publication. Runtime monitoring and rollback retain their existing owners and controls.
>
> Change Log entry (one line): v2.8.9 | GOV-20261102-gtwpe-pf04 | NON_EPIC | Scope: Live compat test for every Epic and Product Owner-only waiver; GATE:CORE-DET evidence and retired entries; compat namespace as a dev/admin surface; sanity-pipeline log-path bound; governed gate check rows; planning-document and PF-version independence; v2 close-run evidence and tracked-issue IDs | Targets: §2.0.10, §2.0.19, §3.4, §4.1.4, §4.1.8, §9.1.2, §9.1.3, §12.2, Appendices B.2/D.1/D.3 | Acceptance: LOGS_KEYS_ONLY_OK | Evidence: None | Freeze-pack: No | Canonical record: PF04 §9.3.1 / GOV-20261102-gtwpe-pf04

````

### RL-11 — REPLACE

- Operation: `REPLACE`
- Ledger rows: C-29 (2.16 R-1, R-2), C-30 support
- Change type (report classification): CANON_UPDATE
- Location (original-baseline heading path): "# **12\. Gate Suites (Governance Gates) \[Required-Now\]**" > "## **12.2 Evidence links (titles-only) \[Required-Now\]**" > "### **GATE:CORE-DET — Determinism and identity**"
- Original-baseline lines (informative only, not a locator): 4206–4208
- Scope: whole PF; expected occurrences: old block 1; observed: 1
- Controlling source: HDE Build Notes v14.0.5, 2.16 status and relation to other canon (lines 1876-1890), R-1 (lines 1919-1926) and R-2 (lines 1928-1938); supporting R-3 (lines 1940-1947)
- Effect: Replaces the three GATE:CORE-DET evidence items.

- Old block (340 bytes, SHA-256 `7bbe77599ede6b0136ed19035d087dd5063aa18a881d32d5635f132f258c441d`):

````text
* Goldens (AB↔BA, two-run): `goldens/reader/v1/g02_ab_ba_parity_A.jsonl`, `goldens/reader/v1/g02_ab_ba_parity_B.jsonl`  
* Idempotence recompute and parity scripts: `scripts/make_reader_v1_goldens.py`, `scripts/make_compat_determinism_artifacts.py`  
* Identity marker (preimage → sha256 → final): `artifacts/cards/A3/IDENTITY_OK.txt`
````

- Replacement block (1598 bytes, SHA-256 `06e24d5b48bf6392dd9b36f72b19fadda9bbc7a61f9f19fcde567eddf433e473`):

````text
GATE:CORE-DET evidence is the real compat path, in two parts; the gate's pass conditions in §12.1 are unchanged.

* Compat-path owner tests (closed rails; run as CI selects them): `tests/core/test_engine_core_abba.py`, `tests/core/test_engine_core_determinism.py`, `tests/compat/test_evaluate_pair_eligibility.py`, `tests/compat/test_compat_public_ab_ba_identity.py`, `tests/cli/test_showcompat_parity_and_identity.py`. A change that removes or weakens one of them needs its owner's review, like any other gate test.  
* Live compat test (open rails): each run of the §3.4 live compat test, which is Ops evidence under §3.4.  
* Reader goldens (emitter canonical bytes and preimage hashing; not evidence of compat AB↔BA): `goldens/reader/v1/g02_ab_ba_parity_A.jsonl`, `goldens/reader/v1/g02_ab_ba_parity_B.jsonl`  
* Reader golden and preimage recompute script: `scripts/make_reader_v1_goldens.py`  
* Retired entries: `scripts/make_compat_determinism_artifacts.py`, `artifacts/cards/A3/IDENTITY_OK.txt`, `ci/jobs/preimage_recompute_and_compare.yml`, `ci/jobs/ab_ba_parity_bytecompare.yml`, `ci/jobs/two_run_identity_bytecompare.yml`, `fixtures/composite/abba/*.json`, `audit/gates/determinism/abba_compare.log`, `fixtures/composite/integration_abba/*.json` and `audit/gates/determinism/abba_compare_integration.log` are not GATE:CORE-DET evidence, and no record may cite them as current proof. The generator, its test that pins exit 2, its captures under `artifacts/compat/` and the lower-case marker `artifacts/cards/a3/IDENTITY_OK.txt` stay as history; no code changes with this retirement.
````

### RL-12 — REPLACE

- Operation: `REPLACE`
- Ledger rows: C-29 (2.16 R-1, R-2)
- Change type (report classification): CANON_UPDATE
- Location (original-baseline heading path): "# **Appendix B — Acceptance Gate Details \[Required-Now\]**" > "## **B.2 GATE:CORE-DET — Determinism and identity**"
- Original-baseline lines (informative only, not a locator): 4450–4453
- Scope: whole PF; expected occurrences: old block 1; observed: 1
- Controlling source: HDE Build Notes v14.0.5, 2.16 R-1 and R-2 (B.2: the three retired CI jobs, line 1934)
- Effect: Replaces the retired CI job list; the checklist item is unchanged.

- Old block (173 bytes, SHA-256 `31404e6214060246e345757a49e57f95c362c7f08669ac0c1959e68f12d36f63`):

````text
* **CI jobs (titles-only):**  
  * `ci/jobs/preimage_recompute_and_compare.yml`  
  * `ci/jobs/ab_ba_parity_bytecompare.yml`  
  * `ci/jobs/two_run_identity_bytecompare.yml`
````

- Replacement block (362 bytes, SHA-256 `3d9f4c5d5a7f3613e5633b801723bd230e1b0b11c44edb4d1fdd21729028a6f4`):

````text
* **CI enforcement (closed rails):** the compat-path owner tests named in §12.2, run as CI selects them. The former CI job entries `ci/jobs/preimage_recompute_and_compare.yml`, `ci/jobs/ab_ba_parity_bytecompare.yml` and `ci/jobs/two_run_identity_bytecompare.yml` are retired (§12.2).  
* **Open rails:** each run of the §3.4 live compat test, as Ops evidence.
````

### RL-13 — REPLACE

- Operation: `REPLACE`
- Ledger rows: C-29 (2.16 R-1, R-2)
- Change type (report classification): CANON_UPDATE
- Location (original-baseline heading path): "# **Appendix D — Evidence Index (titles/paths only) \[Required-Now\]**" > "## **D.1 Parity (Reader↔CLI, AB↔BA, two-run)**"
- Original-baseline lines (informative only, not a locator): 4602–4604
- Scope: whole PF; expected occurrences: old block 1; observed: 1
- Controlling source: HDE Build Notes v14.0.5, 2.16 R-1 and R-2 (D.1: generator line 1932; composite and integration entries line 1935); D.1 sub-entry mapping lines 1888 and 1932-1935
- Effect: Replaces the byte-compare scripts, composite fingerprint and integration set items.

- Old block (333 bytes, SHA-256 `13064dd837180f00c45f3c06c6c05ac9b87ff9ec25bd128dd23791ac4d8da0d2`):

````text
* Byte-compare scripts: `scripts/make_reader_v1_goldens.py`, `scripts/make_compat_determinism_artifacts.py`  
* Composite fingerprint: `fixtures/composite/abba/*.json`, `audit/gates/determinism/abba_compare.log`  
* Integration set: `fixtures/composite/integration_abba/*.json`, `audit/gates/determinism/abba_compare_integration.log`
````

- Replacement block (460 bytes, SHA-256 `e8086cf34232c757f0095aed9312a5e69eb75956de08538ac67c16d49aff58f9`):

````text
* Byte-compare scripts: `scripts/make_reader_v1_goldens.py`  
* Compat-path owner tests (GATE:CORE-DET; closed rails): `tests/core/test_engine_core_abba.py`, `tests/core/test_engine_core_determinism.py`, `tests/compat/test_evaluate_pair_eligibility.py`, `tests/compat/test_compat_public_ab_ba_identity.py`, `tests/cli/test_showcompat_parity_and_identity.py`  
* Live compat test (GATE:CORE-DET; open rails; Ops evidence): each run of the §3.4 live compat test
````

### RL-14 — REPLACE

- Operation: `REPLACE`
- Ledger rows: C-29 (2.16 R-1, R-2)
- Change type (report classification): CANON_UPDATE
- Location (original-baseline heading path): "# **Appendix D — Evidence Index (titles/paths only) \[Required-Now\]**" > "## **D.3 Idempotence coupling (preimage → sha256 → final)**"
- Original-baseline lines (informative only, not a locator): 4617–4618
- Scope: whole PF; expected occurrences: old block 1; observed: 1
- Controlling source: HDE Build Notes v14.0.5, 2.16 R-1 and R-2 (D.3: generator line 1932 and the A3 marker line 1933); the owner-test preimage recompute fact (line 1913)
- Effect: Replaces the identity marker and recompute scripts items; the schemas item is unchanged.

- Old block (169 bytes, SHA-256 `bbd2e66102b44c55c5e5a7faaf938011a8e7c0ccfbc37dd79cb47ebd8c4083f4`):

````text
* Identity marker/logs: `artifacts/cards/A3/IDENTITY_OK.txt`  
* Recompute scripts: `scripts/make_reader_v1_goldens.py`, `scripts/make_compat_determinism_artifacts.py`  
````

- Replacement block (209 bytes, SHA-256 `579e8b4a0dd9f755db6848a953ce4bc3486b022903fca19f189f29a062818a3e`):

````text
* Recompute scripts: `scripts/make_reader_v1_goldens.py`  
* Compat-path preimage recompute (owner tests): `tests/compat/test_evaluate_pair_eligibility.py`, `tests/cli/test_showcompat_parity_and_identity.py`  
````

END OF REDLINES
