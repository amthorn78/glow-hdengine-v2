3 distinct confirmed REQUIRED findings.

# REVIEW-PLAN-1-A — PLAN of MODIFICATION-20261011-gcfpe-mb008-to-promotion, full review 1

**Answer.** Most of the plan holds up, and the dry run reproduces wherever I could rerun it.
- **The body operations and their checks hold.** I re-read 10 candidate pages fresh, across the CF, CL, ESC, MGR, PR, QA and RS lanes and PE. On all 10, every operation resolves once and applies, every batch is safe, and every guard passes after the edits.
- **The tools hold.** The insertion logic in `body_check.py` is correct. The F06 tools rebuild the plan's exact values. All 46 package redlines land.
- **One gap in the guards.** No live sentence on my pages gives model advice that the guards miss. The sentences that could still suppress the reading or the surface advice end in a loud `TypeSafe: not read`, or need a PE repair to do harm. All of them are listed below.

**The three required defects are all in PART-05, and they follow from DN-C option A.** That part makes the D20 three-mode body GCFPE-MGMT-10's successor. The dry run did not exercise it.
- **R-A1.** Candidate texts still name or describe the 091426.1 MGMT-10. One is PR-35's "selected" maintenance binding; another is PE's MGMT-10 contract. No operation or guard covers them, and X20's sweep would either miss them or edit a selected member body after validation.
- **R-A2.** X11's MGMT-10 registry row is specified by three fields only. The proposal row it is assembled from describes the 091426.1 page. Two of that row's three required assertions fail on the successor body (I checked with the shipped audit engine).
- **R-A3.** M-HEAD and M-TS, applied to the testing body's actual text, silently produce wrong text: a duplicated `Prompt ID` line, and an orphaned "Never without his approval."

No finding sits in text a repair added: this is round 1, and the plan has had no repair.

**The record reviewed.**
- **Commit:** `1b742bb84e42b5fdceb63eebcc2ba3b7cce0b15d`: the record's frontmatter and §P, `PLAN-20261011.md`, and `plan/`. The branch head `0c0c510` adds only the two briefs.
- **Canon:** `main` `9312add2`. The branch changes nothing under `docs/pfcanon/`.
- **Brief:** `BRIEF-PLAN-1-A.md` at `0c0c510`.

## REQUIRED

### R-A1 — DN-C option A's successor is not reconciled with candidate texts that name or describe the 091426.1 MGMT-10

- **Rubric class:** R1, a defect on the normal path. Its X20 branch is R4, a plausible path with a silent outcome.
- **Path:** normal, every promotion. **Likelihood:** certain for PR-35 and PE, which I read fresh. Other pages are unmeasured.
- **Consequence:** the selected 100926.1 release ships these two texts in contradiction with the selected MGMT-10.
  - PR-35 sends prompt defects to a manager page that X19 archives, and calls that page "the selected" one.
  - PE's validation contract describes a MGMT-10 that no longer exists.
- **In text the last repair added:** no.

**The exact text.**
- PR-35 100926.1, *Prompt navigation and maintenance*, fresh read at revision `2026-10-09T20:12:39.512Z`: "Report a defect in this prompt/version to the selected `GCFPE-MGMT-10 — Manage an Ecosystem Change — 091426.1`; do not repair prompt policy during a PR run."
- PE Metaprompt 100926.1, GCFPE overlay, *Validation and completion*, revision `2026-10-11T16:10:06.322Z`. This paragraph is not scoped "for this repair":
  - "`GCFPE-MGMT-10` remains a reusable ecosystem manager with the actual case-bound `GCFPE_ECOSYSTEM_CHANGE_REPORT`."
  - It goes on to describe `ECOSYSTEM_CHANGE_COMPLETE` with a conditional `ORIGINAL_NATIVE_STAGE` continuation.
  - It also describes `READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION`, with a PR-10 invocation.
- The plan covers neither. `edits.json` touches PR-35 only with `TS-PR-35` and `T1-PR-35`, and PE only with `TS-PE`, `PE-EXCL`, `PE-SCAN`, `PE-AF013` and `PE-STD`. No guard in `guards.json` matches either text.

**The evidence.**
1. The successor part (`graph_assemble.py` `node_values`, `edge()`) carries:
   - output `GCFPE_MODIFICATION_RECORD`;
   - four results, `PRODUCT_OWNER_ACTION_PENDING` among them;
   - no `ORIGINAL_NATIVE_STAGE` or `PR-10` edge.
   Its self-test row `rejects_kept_pr10_edge` enforces that. The PE paragraph contradicts all three.
2. X16 makes MGMT-10 100926.1 the selected manager, and X19 archives MGMT-10 091426.1. After that, PR-35's sentence names an archived page as "the selected" manager.
   - Other members name the manager without a version, which stays true. Examples: ESC-25, QA-50 and RS-20 say "the selected GCFPE-MGMT-10 maintenance owner"; OPS-10 and PR-30 say "GCFPE-MGMT-10 — Manage an Ecosystem Change in Notion directory …".
3. **X20** searches for the literal `091426.1`, and "each page that asserts the predecessor as current is corrected or bannered".
   - PLAN §8 authorizes "X20's corrections and banners on pages the sweep finds asserting the predecessor as current". Prompt bodies are not excluded.
   - If the sweep finds PR-35, it edits a selected, qualified member body. That edit runs after X18's production validation and outside X5's guarded operations.
   - D17 records why that is wrong: "A promotion that silently edited 55 validated bodies would have voided the post-flight verdict that authorised it." If the sweep misses PR-35, the stale binding ships.
   - P-L4 lists pages *outside the survey* that may be missed. It does not cover a selected member body, or a sweep edit to one.
4. **PF04 §9.1.6** (read on `main`) requires the affected counterparts to be reconciled "in one coherent successor selection", and says "an edited subgroup is not ready while an affected counterpart remains incompatible". PE is a control that X15(b) binds into the release.

**Smallest correction.** Inside ITEM-06 (carry MGMT-10 into the release):
1. In PART-05, measure the 55 candidate pages and PE by broad match on `MGMT-10`. The permitted exception is a versionless reference to the selected maintenance owner.
2. Add one operation per surviving instance. At least:
   - drop the version from PR-35's binding;
   - restate PE's *Validation and completion* MGMT-10 sentences for the successor: four results, `GCFPE_MODIFICATION_RECORD`, no handoff.
3. Add a forbidden guard on every row and on PE: `GCFPE-MGMT-10[^.\n]{0,60}091426\.1|GCFPE_ECOSYSTEM_CHANGE_REPORT|READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION`. The predecessor-history sentence PE scopes "for this repair" is a named exception.
4. State in X20 that the sweep never edits a selected member body. If the sweep finds one, that is a stop.

### R-A2 — X11's GCFPE-MGMT-10 registry row is underspecified, and the proposal row it is assembled from fails on the successor body

- **Rubric class:** R1, a defect on the normal path. One branch is R4, silent.
- **Path:** normal, X11. **Likelihood:** certain that X11 cannot be executed mechanically as written.
- **Consequence:** the row as specified gives one of three results:
  - X11's "every row's `audit_assertions` pass" fails, which is a loud stop on the normal path;
  - the executor writes the row's assertions and identity during EXECUTE, without a plan or review;
  - if the audit reads MGMT-10 by the row's page id, the assertions pass on the 091426.1 body. X21 then commits a selected registry whose MGMT-10 row points at a page X19 archives. That outcome is silent.
- **In text the last repair added:** no.

**The exact text.**
- PLAN §3, PART-05 (line 97): "Registry row: inputs `MODE` and the subject; consumers and interfaces none; states derived from the part".
- PLAN §3, PART-07 table (line 111): "assembled from the grandparent's non-derived 100926.1 proposal, the MGMT-10 row above, fields derived from the final parts, and every guard … every row's `audit_assertions` pass on fresh reads of all 55 bodies".
- Record §P, X11 (line 302).

**The evidence.** The proposal row `GCFPE-MGMT-10` in `20261009-gcfpe-latest-alpha-analysis/execute/candidate-registry-nonderived.json` describes the reused 091426.1 page in fields the plan does not name:
- `notion_page_id` `3db4590a05eb81d1bb64ebcb3ca8eb54` and its `notion_url`;
- `expected_title` "GCFPE-MGMT-10 — Manage an Ecosystem Change — 091426.1";
- `outputs[].artifact` "GCFPE_SUCCESSOR_RELEASE / CHANGE_RECORD", where §9A's stage 3 specification and the successor part both have `GCFPE_MODIFICATION_RECORD`;
- `evidence_contract` "Reused selected member at 091426.1; no body change";
- `source_snapshot` `REUSED_UNCHANGED_NOTION_MEMBER`;
- `controlling_sources`, `function`, `inputs`;
- three `required_regex` assertions.

I ran the shipped audit engine (`audit_workspace_governance._evaluate_assertions`) on two inputs:
- **The MGMT-10 row, on the testing body as it would land.** This is a fresh read at the X0 pin `2026-09-24T11:00:24.691Z`, with the M-HEAD header and the M-TS insertion applied in memory. Two `CTR-002` ERRORs:
  - "Every statement in this prompt that it is read-only or does not change the repository excludes its own output artifacts, …" is absent;
  - "This prompt's artifacts are written only under `docs/ephemeral/` and `docs/graph/`, the controls it maintains only under `docs/prompt_ecosystem_management/`" is absent.
- **The proposal's rows, on my 9 fresh reads of runtime members.** All 9 rows pass, before and after the planned edits. So do the rows for the two further reads found in the shared harness records, OPS-10 and PR-50. The failure is confined to MGMT-10.

The plan names no tool that assembles the registry, and gives MGMT-10's row no TypeSafe assertion: G-TS-1 and G-TS-2 list 53 members and PE, not GCFPE-MGMT-10. D26-A rule 1 asks the dry run to rehearse every normal-path gate "on the text as it would land". The testing body is live, and the proposal row is committed, so this could have been rehearsed.

**Smallest correction.** Specify the complete MGMT-10 row in the plan:
- **Identity:** the successor's page id, URL and title, filled after X1.
- **Output and evidence:** output `GCFPE_MODIFICATION_RECORD`; `evidence_contract` and `source_snapshot` describing the successor.
- **Assertions:** drop the two 091426.1 `required_regex` and assert the successor body's own text instead. Add the TypeSafe rule and the procedure line as required assertions, and put GCFPE-MGMT-10 on G-TS-1 and G-TS-2 with M-TS's wording, or give it its own guard.
- **Rehearsal:** run the row through the audit engine on the testing body with M-HEAD and M-TS in memory, as a dry-run gate.

### R-A3 — M-HEAD and M-TS produce unintended text on the testing body's actual text

- **Rubric class:** R2, a silent wrong edit to a prompt body.
- **Path:** normal, X2. **Likelihood:** certain if the operations are applied as written.
- **Consequence:** low in behaviour, but both changes are invisible to every planned check.
  - M-HEAD leaves the successor body with two identical `Prompt ID` lines.
  - M-TS separates "Never without his approval." from the invocation sentence it qualifies. It then reads as a rider to the pick-recording rule. The approval rule survives only because the same paragraph also says "only after Nathan approves".
- **In text the last repair added:** no.

**The exact text.** PLAN §3, PART-05:
- **M-HEAD (line 94):** "Replace everything above `# Manage an Ecosystem Change`, and that heading, with the identity header: `GCFPE-MGMT-10 — Manage an Ecosystem Change — 100926.1`, `` Prompt ID: `GCFPE-MGMT-10` ``, and `Notion URL:` …".
- **M-TS (line 95):** "After 'In a fresh session, he invokes this prompt with that `MODE` and the Modification id.', insert: …".

**The evidence.** Fresh read of the testing body at the pin. Counts only, under D22:
- "Prompt ID: `GCFPE-MGMT-10`" occurs once, on the line directly after the heading: one newline separates them. It is below the replaced span, so M-HEAD's header adds a second copy. The result reads title, `Prompt ID`, `Notion URL`, `Prompt ID`, then *Native purpose*.
- The 100926.1 identity check (`prompt_identity_header_valid`) needs only one `Prompt ID` line within the first eight lines, so it passes. M-HEAD's absence checks also pass.
- The M-TS anchor occurs once, and the next characters are "Never without his approval." Only M-TS's "inserted text occurs once" check runs on it.

**Smallest correction.**
- **M-HEAD:** either end the replaced span after the existing `Prompt ID` line, or keep that line and replace only the material above it with the title line, inserting `Notion URL:` after it. Check that exactly one `Prompt ID` line remains.
- **M-TS:** anchor the insertion after "Never without his approval." Check that "Never without his approval." directly follows the invocation sentence.

## LISTED

Each line gives the path, likelihood, consequence and why the finding is listed rather than required. None sits in repaired text.

- **L-A1.** C-TYPESAFE asks the lines before the block to "name the TypeSafe reading". §A.7's option 1, which option 2 inherits, said those lines name "the cell, the flags and the artifact path". Normal path; possible; Nathan must open the artifact to see the cell. Nathan's chosen wording, "names it", is met.
- **L-A2.** In C-TYPESAFE, "record that pick … with a reference to the reading" has an ambiguous antecedent. It could mean the reading this session wrote for its receiver, rather than the upstream reading for this session. Normal; low to medium; a pick recorded against the wrong reading.
- **L-A3.** `TS-PE` puts "(C-TYPESAFE)" after the inserted text's last period. The tag then reads as attached to "For GCFPE, this contract replaces the general handoff content list above." PE's other tags sit before the period. Cosmetic; certain.
- **L-A4.** In PE, C-TYPESAFE's imperatives and "this session" can be read as addressing the PE session itself. Low; one extra script run.
- **L-A5.** Same-session handoffs still get a reading for a session that is already running. Examples: PR-30 `RECOVERY_PENDING`; PR-35 `REMOTE_EVIDENCE_PENDING`; ESC-25 to ESC-30 "in that same continuing Thoth session"; QA-50 to QA-60; RS-20 to PR-30 "in the same PR session". Certain; cost only.
- **L-A6.** CL-40's "Use only available authorized read-only source, repository, and record tools needed for this bounded scan", and ESC-25's read-only reviewer role, can lead a session to skip the script. Failure path; loud, as `TypeSafe: not read` with the reason (rule 4).
- **L-A7.** PE's "Keep session setup outside the authored prompt" and its operator note "Session setup remains outside the prompt contract" get no GCFPE carve-out, unlike PE-EXCL and PE-SCAN. G-TS-3 passes both. A PE-run repair could strip C-TYPESAFE. Low.
- **L-A8.** DN-B replaces skill step 4, and with it the record of the action text ("Action sent (v6)"). The artifact does not take it over, so the skill's "one text, one reading" cannot be audited. Certain; low.
- **L-A9.** With `--markdown`, the skill prints "Notion row (paste verbatim as the page properties)". Copying the reading "as the skill prints it" carries that instruction into artifacts. C-TYPESAFE forbids the row. Low.
- **L-A10.** typesafe-scoring's installed steps 3 to 5 (paste into the prompt header, create the Notion row, set the pick) contradict C-TYPESAFE for any session that loads the skill. The body text is explicit. Low; A-7 was accepted at ANALYZE.
- **L-A11.** C4 and A5, the R1 Kronos token mapping.
  - `maintenance_metadata` (`validate_flowmaster.py:1328–1336`) is limited by its own comment to "two historical package/lifecycle metadata anchors", and the comment says "every runtime row, actor, approval and edge is still compared".
  - Mapping `KRONOS_NEVER_EXECUTES_OPS_OR_QA` widens it to an actor rule. R1 GCF-23 ("Authorized environment/DevOps operator executes a bounded QA Task") and the prohibited pattern `KRONOS_EXECUTES_QA` stay as they are.
  - D23 Amendment 1 used a successor oracle for behavioural R1 changes. The mapping is disclosed in §P, so it is not silent.
  - Consequence: change-flow's pinned GCF-23 contradicts its own QA-execution row. V1 should at least update the comment and say that the overlay governs.
- **L-A12.** A body-side F02 survivor: "Apply the accepted R1 workflow: … authorized environment operators execute Ops/QA". It is on OPS-10, PR-10 and PR-30 in my fresh reads, and probably on other pages. It is outside MB-008's package scope; a backlog candidate.
- **L-A13.** C5 understates `make_profile_20261009.py`: S12 also adds a predecessor-contract pin and `RETIRED_091426_STAGING_SOURCE`, and S13 adds the F09 receivers. PLAN §3 discloses both. No defect.
- **L-A14.** PLAN §3 F06 says "five named prompt references", but the patch derives six. The sixth is `alpha_resumption_contract.successor_trigger.prompt`, rewritten to the PR-10 100926.1 page, while CF-F06-4 calls that object "the record made at the 091426.1 promotion". Low.
- **L-A15.** SR-F07-1 reads "a relay that composes a GCFPE handoff itself, … run the installed …"; it should say "runs". Cosmetic; a V6 phrase check may fail loudly at X9.
- **L-A16.** `validate_flowmaster.py:364`'s forbidden phrase "surface/model/reasoning recommendation" is not addressed in V1–V7. ANALYZE said it partly conflicts with surface advice. No planned text uses it; latent.
- **L-A17.** The MGMT-10 part marks `PRODUCT_OWNER_ACTION_PENDING` as `terminal_for_invocation`, while the body says "Not terminal." This is consistent with graph semantics, since there is no handoff; wording only.
- **L-A18.** X1's rollback, "move the duplicate to the archive", is a Notion write that §8 does not list.
- **L-A19.** G-F05-D matches only "allocat… number". The scope measurement used `numbering`, and `number` with PF10 or addendum. A regression worded "Nathan numbers it" would pass. Low.
- **L-A20.** PE-STD keeps "does not authorize live PF10 inspection, numbering" ahead of the GCFPE exception, although resolving the number means reading current PF10. Low.
- **L-A21.** M-TS's "in the few lines of the return" names a rule the MGMT-10 body never states; it comes from the Hub standard, a D23 successor. Low.
- **L-A22.** V1–V7, the 100926.1 fixtures, the fixture runner and change-flow's derived validator are described but not committed. D26-A rule 1 asks that every step's verification name a committed command. D24 reviews them; this is a question.

## Claims, in brief

- **C1 holds**, subject to L-A1 to L-A4. C-PLACE, C-ART and D23-B are kept: the reading and the advice go in the artifact, the lines before the block name them, and nothing goes in the block. Skill steps 1 and 2 are kept, and DN-B replaces steps 3 to 5.
- **C2 holds.** The insertion rules are correct for an untouched page, a landed page, a doubled insertion and a second send, and batch safety holds. All 17 resolver self-test cases pass. On my 10 reads, 0 operations conflict.
- **C3 holds** on the pages I read. ESC-25's "Never … allocate PF10 numbering" and PR-35's "does not edit, number, or claim canonical adoption" are nonproducers speaking of themselves. No other universal numbering sentence survives.
- **C4 holds**, subject to L-A11.
- **C5 holds**, subject to L-A13 and L-A14.
- **C6 holds.**
- **C7 fails**, on R-A2, R-A3 and part of R-A1.
- **C8 fails on X20's reach** (R-A1).
- **C9 holds where the dry run exercised it.** X11 is not mechanical (R-A2).
- **C10 is incomplete** by R-A1 to R-A3.

## What I checked, and how

The repository was read at `1b742bb8` and canon at `main` `9312add2`. The installed skills were copied to scratch by `dry_run.py` and run with `PYTHONDONTWRITEBYTECODE=1`.

| Check | Result |
|---|---|
| `dry_run.py` rerun in scratch (fetch cutoff `2026-10-11T23:30Z`) | N0: 7 of 7 digests. N1: 14 guards, 37 fixture rows, 17 resolver cases. N4: 12 of 12 self-test cases; parent 237 edges `ff296b1e…`, candidate 235 `df3b57a5…`, production 235 `8391ad84…`, all validation PASS. N5: patch applies; shipped 091426.1 contract EQUAL; unfilled marker refused; candidate 634,454 B, production 631,092 B. N6: 25 substitutions, only the two pending errors. N8: 46 of 46 land, second apply refused, audit fixture suite passes. N2, N3 and N7 ran only on the pages I fetched |
| `body_check.py plan` on my 10 fresh reads (CF-E-30, CL-40, ESC-25, MGR-10, PE, PR-10, PR-30, PR-35, QA-50, RS-20) | Revisions equal their pins; every operation applies once; batches are safe; every guard passes after; landing would pass |
| Shipped audit engine: the proposal's rows on those pages, and the MGMT-10 row on the testing body | Runtime rows: 0 findings before and after. MGMT-10: 2 ERRORs (R-A2) |
| Testing body anchors | M-HEAD and M-TS anchors once each; `Prompt ID` follows the heading directly (R-A3) |
| Proposal assertions, `validate_flowmaster.py`, the R1 oracle, `score.py`, regenerator | Read as cited above |

**Notion reads, one fresh fetch per page:** the 10 pages above and the MGMT-10 testing body.
- The harness saved two of the results, PE and PR-10, to its own tool-results files; the rest returned inline. Every scan was a transient read that printed counts or matched sentences to this session only.
- No body was copied, hashed or compared, and no body text is in this record beyond the cited sentences.
- **This session's harness records were shared with another agent.** One of my scans also picked up that agent's fetches of OPS-10 and PR-50. I rest no claim on them except that L-A12 names OPS-10.
- **The scratch directory is shared too.** It holds other agents' files. My `dry_run.py` rerun used `scratchpad/dryrun`, which the script deletes and recreates. If another run had used that name, its scratch output was replaced; no repository file or committed receipt was affected. My scratch files held repository copies, skill copies and count-only outputs, no prompt body, and I deleted them at the end.
- I did not open the other reviewer's record.

**Canon relied on:**
- `AGENTS.md`, the canon-first rule.
- PF10-HDE-Build-Notes v13.5.2, complete: precedence §§1–9 and addendum 2.1.
- PF04-Canon-HDE-Governance v2.8.7, §9.1.2, §9.1.3 and §9.1.6.
- PF06-Canon-Change-Process-Guide v2.5.4, §0.1A.
- PF27-Canon-Plan-Templates v2.0.5, *Canon precedence for template use*.
- In-flight: the record under review (§A, §P) and its PLAN evidence; the parent's `findings.md`; `MODIFICATION-20260923-alpha-feedback-open-entries` §P for the canonical C-ART, C-HANDOFF and C-PLACE; `GCFPE-MGMT-REDESIGN-ANALYSIS-v1.0.md` §9A; the grandparent's non-derived registry proposal.
- Controls: `gcfpe.decision-record.md` D17, D23 with its successors, D26 and D27; `notion-write-boundary.md`; `authoritative-surfaces.md` (*Stale-state sweep*, *Restating is allowed; asserting is not*).
- I did not read in full, and claim nothing from: D20–D22, D24 and D25; `modification-template.md`; `ecosystem-change-management.md`; `skill-packaging-and-delivery.md`; `postflight-procedure.md`; `prompt-corpus-policy.md`; `PROMOTION-RECORD-20260921.md`.
- Applied with PF27's precedence rule: "Applicable, active, non-superseded PF10 addenda supersede conflicting PF-Canon only for the exact scope they address; otherwise follow PF-Canon. A formally approved bounded Product Owner rescope may supersede conflicting PF-Canon only for the exact decision it adjudicates."

R-A1 to R-A3 go to the author's repair and the second full review under D26-A. The LISTED findings ride in the approval request as accepted risks unless Nathan opts in.

NOTHING NEEDED
