---
artifact_type: GCFPE_MODIFICATION_EXECUTION_SPECIFICATION
modification_id: MODIFICATION-20260923-closeout-residuals
version: v2
written: 2026-09-23; revised 2026-09-24 (repair rounds 2, 3, 4, 5 and 6)
status: FOR PLAN APPROVAL
compiled_by: the plan's author, from the PLAN workflow wf_73fca782-464, the repair rounds wf_22dee43c-01f and wf_9c136682-f25, repair rounds 3, 4, 5 and 6, and six dry-run passes over every live body
---

# Execution specification — MODIFICATION-20260923-closeout-residuals

This file holds everything behind §P of the Modification record: every edit, literal, guard, package, command and
check, and the disposition of every finding. §P's steps cite its sections.

## §0 How to read it

- **Precedence.** 1: the Product Owner's rulings in §A. 2: the PLAN decisions in §1. 3: the other sections. If a
  section seems to contradict a ruling, the ruling governs, and EXECUTE stops and takes it to Nathan.
- **Nothing is left open.** A choice not stated here is void.
- **Mechanical by construction.** The body edits are data run by one engine
  (`evidence/closeout-residuals/plan/engine/`), the same code for the dry runs (§8) and for landing (§9 X5.4). The
  registry change is one diff with a known base and result. Each skill package is one diff with known freeze
  digests before and after. The repository texts are exact anchors with exact new text.
- **Corpus policy (`D22`).** No prompt body is copied, hashed or stored here or in the evidence. Body clauses appear
  only as anchors and kept-sentence clauses, each at most 15 words. The engine reads a body only from a fetch made
  for the check in hand, and opens only harness files written in the last 30 minutes (P-39).
- **Evidence** (`docs/ephemeral/modifications/evidence/closeout-residuals/plan/`, `EV` below):

| path | what |
|---|---|
| `EV/DECISIONS.md` | the PLAN decisions, P-01 to P-102 (§1) |
| `EV/engine/` | `canon.py`, `closeout_rules.py`, `locals.json`, `dryrun.py`, `land.py`, `graph_check.py`, `pages.json`; the read-only helpers `ctrl.py` (control pages and hub child lists, P-96, P-98) and `drive_check.py` (the Drive file, P-102) |
| `EV/registry/` | used at EXECUTE: `registry.diff`, `row_assertions.json`, `nam002_live.py`; records: `GUARDS.md`, `report.json`, `guard_tests.json`, `nam002_proof/`, `nam002_live_plan/` (the four runs on live hubs, P-101); PLAN-time generators (P-74): `guards.py`, `apply_registry.py`, `guard_tests.py`, `summarize.py`, `build_guards_md.py` |
| `EV/skills/` | `manifest.json` (its `execute` block holds every EXECUTE command), `run_gate.py` (the suite gate, P-60), `diffs/<skill>.diff` (7), `contract-template-README.md`, `expected_after_patch.txt` (X4.3's comparison), `packages_json.py` (X4.3), `REVIEWER-PROMPT-cr.draft.md` and `fill_brief.py` (X4.4, P-100), `results/` (suites, regressions, reindex, the §9-order proof and its builder, `brief_fill_proof.json`) |
| `EV/texts/` | `edits.json`, one Markdown file per repository text, and `apply_texts.py` (the applier, P-102) with `apply_texts_proof.json` |
| `EV/notion/` | `edits.json` (24 control-page edits, five of them only after a stop), `M2.json` (the list migration), `NOTES.md`; `ctrl_proof.py` with `ctrl_proof.out.json` and its stand-in `ctrl_proof.run.json` (P-96, P-98, P-99); `anchor_check_plan.json` and `drive_check_plan.json` (X4.6's checks on today's pages, P-102) |
| `EV/dryrun/` | pass 1's batch reports; pass 2's per-body results (56 body files, plus `qa110_item34.json`); pass 3's to pass 6's rehearsal results (56 bodies and the graph check each) and their `report.json`; `synthetic/` (the partial-landing test on synthetic text, P-88); no body text |

## §1 PLAN decisions

The repair round's decision file, as the workers applied it. Each settles a review finding, a drafter issue or a dry-run result (§2 maps them).

These settle every finding of the PLAN reviews (completeness and executability) and every open issue
of the PLAN drafters. They are the source of truth for the repair round. Where a drafter's earlier
text differs, this file governs. A worker who finds that one of these cannot be applied as written
reports it with evidence and does not improvise.

Inputs: `scratchpad/plan_result.json` (canon.rules, bodies, reg, skills, review), the Modification
record `docs/ephemeral/modifications/MODIFICATION-20260923-closeout-residuals.md` (§A is frozen and
approved; PLAN never edits it), and its evidence under
`docs/ephemeral/modifications/evidence/closeout-residuals/`.

Standing rules for every worker:
- D22: prompt bodies are read from Notion only, transiently, for the check in hand. Never copy,
  save, hash or byte-compare a body. Never re-read a harness-saved body file from an earlier task.
  Quote at most 15 words of any body clause in anything you write. Report every harness-saved file.
- Write only in the scratchpad. No repository write, no Notion write, no write under
  /root/.claude/skills.
- `PYTHONDONTWRITEBYTECODE=1` and `TMPDIR=<scratchpad>/plan/tmp` for every python run.

### Body rules and texts

- **P-01 BRANCH-RECV text (G06-silent).** R-26-BRANCH-RECV's sentence becomes, everywhere:
  `The branch, head and commits are verified at entry from the recorded vehicle and repository state; the handoff does not carry them.`
  The rule is LOCAL-only, like R-26-FRAME: it holds the text and the guards; the per-site LOCAL
  edits (PR-20 L20-3, PR-35, PR-40 L40-5, RS-20, RS-40) are authoritative and each uses this text.
  G-K22's required pattern is unchanged and still matches. Each site must be G06-silent on the whole
  post-edit body. The registry's PR-40 input text follows the PR-40 body.
- **P-02 R-OWN text.** `Every statement in this prompt that it is read-only or does not change the repository excludes its own output artifacts, which it writes, commits and pushes, and any pull request that carries them.`
  This covers CL-40's "does not create ... PR" and GCFPE-MGMT-10's "PR/CI activity" claims (both
  prompts open a PR for their own artifacts). G-K36 follows the new text. G-K35 is split per row:
  each row carries only the alternative that matches its own placement anchor.
- **P-03 QA-10 role sentence (ITEM-17, literal).** After R-OWN is applied, a LOCAL edit replaces
  `This is a read-only audit and readiness role.` with `This is an audit and readiness role.`
  QA-10's G-K35 alternative becomes the plain forbidden `read-only audit and readiness role`.
- **P-04 GCFPE-MGMT-10 storage sentence (R-A5 LOCAL variant).** MGMT-10's new text is
  `This prompt's artifacts are written only under `docs/ephemeral/` and `docs/graph/`, the controls it maintains only under `docs/prompt_ecosystem_management/``
  so the kept tail reads `..., and `docs/pfcanon/` is read-only.` PR-35 keeps the base R-A5 text.
  RS-40: R-A5 is NOT_APPLICABLE (the sentence is absent); G-K39 and G-K40 are removed from RS-40's row
  and RS-40 leaves R-A5.applies_to.
- **P-05** PR-10 moves from R-A1a to R-A1b (expected 1). G-K02 already covers PR-10.
- **P-06** R-26-FRAME on PR-10: expected 1 by the rule; the RS-10 package site is the drafter's LOCAL
  L4. G-K19's PR-10 second alternative becomes
  `dependency and evidence history; read-only substantiation of the mismatch; completed work`.
- **P-07 R-A2g.** IA-30 gets the site-scoped anchor `(?<=dependency state, )conflict register, `
  (IA-30's own MATERIAL_PLAN_DELTA_REVIEW intake item is never edited). Expected counts are the
  measured ones: IA-10 1, IA-20 1, IA-30 1, OPS-10 4, OPS-20 4, OPS-30 5, PR-20 4, QA-10 6, and PR-10
  and PR-40 as measured in the dry run. The OPS-10 and OPS-20 `Complete return to ESC-30` register
  items and PR-20's RS-30 package item (L20-8) are owned by LOCAL edits.
- **P-08 R-A7-LOCAL.** The DOC-20 alternative is widened to
  `needed after Nathan's assertion: continue to `?PR-40`; DOC-20 expects 2. Every LOCAL edit at a REAL
  site carries a guard that fires on the pre-edit text and is silent after (GUARD-001), or the site
  is listed as unguarded with its reason.
- **P-09 R-ITEM40** runs as its own pattern, without the release-line alternative, and R-ITEM23's
  pattern runs as the second gate pattern. Expected: R-ITEM40 0 hits before and after; R-ITEM23 2
  before, 0 after. Both compile on the installed Python 3.11.
- **P-10 Order inside a body.** Shared rules apply first, in rule-table order; then the body's LOCAL
  edits in their listed order. Every expected count assumes this order.
- **P-11 R-ITEM30d** is split into R-ITEM30d1 (insert at the lookbehind) and R-ITEM30d2 (replace), each
  with its own anchor, action and literal new_text.
- **P-12 Regression injections** are each at most 15 words, and each must fire its guard (forbidden
  present, or required absent) on a synthetic document built from the canonical and authored texts,
  and again on the landed body at EXECUTE.
- **P-13 R-26-P4** applies to every carrier (ITEM-26's statement is absolute). G-K14 stays on its 10
  rows; 0 hits in OPS-10 and OPS-20 is expected (sentence absent) and is recorded, not an error.
- **P-14 R-ITEM35** new text is the pointer only: `, routed as *Required result and routing* states`.
  QA-80's Required result and routing already states both graph branches (drafter, by reading).
  G-K49 and G-K50 are unchanged.
- **P-15 G-K47** *[Placement superseded by P-15 (revised).]* becomes the forbidden `code/Ops remediation\. Do not fix it here\.`, which the
  insertion breaks.
- **P-16 Release-line label suffix.** `(?:\*\*|__|`){0,2}[ \t]*:` in the three registry PART-17 patterns
  and in R-ITEM23. flowmaster-validate's PROMPT_BODY_RELEASE_HEADER must catch `**`Prompt version`**: x`
  and `3. **`Set`**: x` and stay silent on `- Settings: x` and `Set up the run:`; if it does not, its
  pattern is adjusted in the same package.
- **P-17 G-K08** adopts the PR drafter's amended pattern (adds `Complete ` to the native-inputs
  prefix and `Complete RS-\d+ package` to the list-heading alternative), plus, on OPS-10 and OPS-20,
  `(?m)^(?:Complete return to ESC-30|RS-30 native revision):[^\n]*CANON_CONFLICT_REGISTER`.
  Proven in the dry run on all 10 A2g rows: fires before, silent after.
- **P-18 CL-30** gets a LOCAL edit for its second A2 carrier (the outgoing ADR package's input list:
  drop the conflict-history item, as R-A2g does elsewhere) and a CL-30 row guard for that fragment.
  Drafted in the dry run from the full read.
- **P-19 QA-10 twin of OPS-30's deletion.** If QA-10's Task-only next-step transport section carries
  the sentence that OPS-30's LOCAL edit deletes, QA-10 gets the same LOCAL deletion; otherwise the
  dry run records it absent.
- **P-20 R-26-FRAME slots** may use C-HANDOFF and C-ART vocabulary ("names ... by repository path",
  "the artifacts hold the rest", "which records ..."). The spec lists every authored phrase per site
  so the plan review accepts each explicitly.

### Skills

- **P-21 contract_recipe** bounds the once-per-merge section at the next `\n### ` or `\n## ` and asserts
  exactly two `> ` lines are read. No decision-record entry this Modification adds contains a line
  starting `> `. The regeneration runs on the post-decision-record tree and must still give EQUAL x2
  (6902924a… from the kept pre-E2 contract) and dbae180b… for 4.1.1.
- **P-22** validator_revision moves 3.3.0 → 3.3.1 at its four sites (unspent-identity rule).
- **P-23** The seven governance-audit and relay edits beyond the census sites are kept: each is inside
  its item's statement (ITEM-39, ITEM-05, ITEM-02, ITEM-14).
- **P-24** ITEM-06's change-flow `:295` site belongs to the change-flow package.
- **P-25** change-flow's own validator gets must-fail regressions for its new forbidden entries (keep
  the new required marker, inject each forbidden phrase). One `contract_recipe --check` negative
  control is run and recorded (one-byte drift → DIFFERENT, exit 1).
- **P-26** The simulated relay and PR-skill edits are replaced by the real drafts in one final trial
  tree; every suite runs there.

### Registry

- **P-27** Rule codes TOP-001 / CTR-001 / CTR-002 are accepted.
- **P-28** G-K40 and G-K39 leave RS-40. G-K35 per row. G-K36 new text. G-K47 new pattern. G-K08
  amended. G-K19 PR-10 fragment. PART-17 suffix. BRANCH-RECV text in G-K22's rows and the PR-40
  input. MGMT-10's G-K40 uses the P-04 variant. QA-10's G-K35 per P-03. A CL-30 guard slot per P-18.

### Repository and Notion texts

- **P-29 Decision record, EXECUTE's first commit** (none has a line starting `> `):
  - **D25-A** (ruling 1, Q1 (A)): the Candidate CRD Items List lives in Notion; GCFPE-MGMT-10 creates
    the page under the Glow Operations Hub at EXECUTE and migrates the Drive list; a destination rule
    in `notion-write-boundary.md` names the page; CL-40's registry `mutations` allow the write; CL-40's
    A4c sentence goes; the Drive file becomes Nathan's reference copy, which he banners.
  - **D25-B** (ruling 2): every prompt commits its output files; a read-only or no-repository-change
    claim excludes the prompt's own committed outputs and the pull request that carries them.
  - **D23-C successor** (ruling 4, Q2 (a)): C-LAT's three-step block is removed from the eight
    non-implementing bodies; the Material definition and each body's routing stay; PR-30 and PR-35 keep
    the whole C-LAT.
  - **D18 successor** (Q3 (A)): `alpha_resumption_contract` in the graph and the contracts is the
    promotion-time record; the two validator checks are renamed to promotion-record checks; the graph
    does not change.
  - **D14 note** (ITEM-16): the D22 guards pin exact phrases; prose paraphrase is not mechanically
    detectable (the prototype missed 30 of 30 paraphrases).
  - **D23-G successor** (ITEM-36): the release-line check covers the whole body; the spec v2 §3
    literal "in the header window" in `prompt-body-content-policy.md` is superseded.
- **P-30 Destination rule** (PART-06): a row in `notion-write-boundary.md` naming the one page, with
  the URL filled after the page exists (committed at X5.2; P-73).
- **P-31** `prompt-body-content-policy.md`'s Enforcement line: the label line is rejected anywhere in
  the body, line-anchored.
- **P-32** ITEM-24 wording, shared by glow-po-reporting, the Hub *Worker communication rules* §2 and
  `session-working-rules.md`: `When a `NEXT_PROMPT_HANDOFF` block ends the message, as it does for a maintenance, repair, validation or review session, the block comes last and the named state is the line immediately before it. Nothing follows the block.`
- **P-33** A dated correction note is appended to the repair-a4 record for C8 and §2, stating the
  ITEM-15 residual limit (`<div hidden>`, `<details>` and other type-6 HTML blocks are not matched).
- **P-34** Upstream findings (census RS-40 A5; the census summary's A1–A4 claim for the proposed
  MGMT-10 body) are recorded in §P, not edited in the ANALYZE evidence (template rule 1).
- **P-35** Out of frozen scope, for a follow-up Modification spawned from this one: PR-20's PR-40
  DOWNSTREAM "REJECT returns precise in-scope findings to the PR owner" (contradicts C-REPLAN);
  governance audit `references/epic-reengineering-interoperability.md:55-56` (retired Analyzer
  advice); DOC-20's route to PR-40 against once-per-merge.

### Added after the rule-level dry run (all 51 bodies)

- **P-15 (revised)** R-ITEM34's sentence goes after `Do not fix it here.`, so "it" keeps its referent (dry run F).
  G-K47 becomes `Do not fix it here\.(?! This applies only before the whole approved run is complete)`.
- **P-36** Scratch scripts that read harness-saved body files (`plan/drafter_pr_rs_test.py`, `qa_drafter_test.py`,
  `qa_drafter_read.py`, `drafter_ops30_test.py`, `shared_rules_test.py`'s `main()`) are not committed and not re-run
  (D22 condition 2). Only the engine, which reads a fetch made for the check in hand, is committed.
- **P-37 Intake lists.** A prompt's own intake list may name `CANON_CONFLICT_REGISTER` as an input: the register is a
  record inside the named artifacts, and ITEM-27 governs what outgoing handoffs carry. So IA-10's optional LIA-10-1 is
  dropped, and the intakes of IA-20, DOC-10, DOC-20, OPS-30 and PR-40 (and the registry inputs that mirror them) stay.
- **P-38 PR-40's RS-20 package** (ANALYZE-body-evidence row for PR-40 *MATERIAL → RS-20 package*: "carries decision
  history and complete RESCOPE_PROPOSAL", REAL): besides R-A2g's register clause, `RESCOPE_PROPOSAL_ID and complete
  RESCOPE_PROPOSAL` becomes `RESCOPE_PROPOSAL_ID, naming the RESCOPE_PROPOSAL by repository path` (rule R-26-RSP, with a
  guard on PR-40). PR-10 and PR-20 are scanned for the same phrase.
- **P-39** The engine's body lookup opens only harness files written in the last 30 minutes, so an earlier task's
  file is never read (D22 condition 2).
- **P-40** The anchor table had PR-20 and PR-50 swapped for R-OWN (dry runs A and E1): PR-20's placement is
  `Do not mutate the repository in this authoring operation.` and PR-50's is `otherwise mutating the workspace, ...`.
  G-K35's per-row split follows.
- **P-41** GCFPE-MGMT-10's open-PR outcome ("an open pull request is a complete outcome"; its outputs are committed
  and pushed) makes P-02's "and any pull request that carries them" true for it; no further edit.
- **P-42 New guards from the dry run:** DOC-10/DOC-20 sites (alternatives appended to G-K26); `A saved attachment, link
  or scattered fields do not replace the handoff\.` on OPS-30 and QA-10; the CL-30 P-18 guard; R-26-RSP's guard on
  PR-40.

### Settled from the texts and Notion workers' open issues

- **P-43** P31 (policy Enforcement line) and P33 (the repair-a4 correction note) describe checks that exist only after the
  install, so they move to the close commit (the close-out PR, after the post-install gate). Commit 2 keeps P30-DEST,
  P30-VERSION and P32. *[Commit placement superseded by P-73: `P32` lands in the X3.5 commit, `P30-DEST` and
  `P30-VERSION` in the X5.2 commit.]*
- **P-44** The AF-009 disposition on *GCFPE Alpha Feedback — Deferred Items* ("C-LAT, in the ten bodies ...") gets the
  drafted dated amendment (PART-18). The Alpha feedback list is an established maintenance destination.
- **P-45** The Glow Operations Checklist property *Authoritative Drive register* on the four item rows stays as history;
  each row gets the drafted dated movement entry. No data-source change.
- **P-46** The eleven pointer edits (Hub ×3, item rows ×8 — two per row) are PART-06 steps, run only after the new
  page's readback passes.
- **P-47** Migration method M2: the eight Drive self-references outside the fence are rewritten to name the Notion page,
  and one dated bullet is appended to *Scope-repair revision record*. Exact old/new pairs are in the spec.
- **P-48** No Notion or repository write may land a `{{...}}` token: the landing step refuses any new text containing
  `{{`.
- **P-49** *[Narrowed by P-90 and P-96: a control-page edit whose new text is present has landed.]* Before every Notion edit, EXECUTE re-fetches the page and confirms each `old_str` still occurs exactly once.
- **P-50** The tracking page's stale status lines (yaml status, "at INTAKE with ANALYZE in progress", the Records row) are
  updated at the close-out, from the state at that time.
- **P-51** *[Its date is the unit's start date, recorded at X5.0 (P-96).]* The tracking-page entry is dated by its write date ({{EXECUTE_DATE}}) and names the census of 2026-09-23.
- **P-52** `notion-write-boundary.md`'s artifact_version moves 1.2 → 1.3 with the destination row (P30-VERSION kept).
- **P-53** Decision-record entries are dated 2026-09-23, the date of the rulings they record (house style).
- **P-54** The parent record's §E line (`MODIFICATION-20260923-alpha-feedback-open-entries.md:1112`) repeats the C8
  overstatement. It is a completed record and is not edited; the correction note is the record of the correction.
- **P-39 (revised, dry run pass 2, batch P3)** A live session transcript keeps a fresh modification time while holding
  fetches from earlier tasks. So the engine also filters each transcript entry by its own timestamp (the last 30
  minutes), reports the file it read the body from, and keeps the file-level test for tool-results files. Proved on
  all 12 P3 bodies (identical results, now from the task's own fetches) and by a negative control (a 1-minute window
  refuses with `NO_FETCH_FOUND`). The limit, stated: the scan still parses older entries of a live transcript in memory
  to skip them; it never selects or uses them.

### Settled from the PLAN review, round 2 (wf_045af16b-3ed: completeness, executability, consistency)

- **P-55** G-K55 (forbidden `outside the approved Plan, return the metadata\b` on PR-30) guards LPR-30-2 (dry run pass 2
  registry repair); it closes the last unguarded LOCAL edit at a REAL site.
- **P-56 Order.** The seven packages are patched into the scratchpad (and the full skills root and the candidate root
  built) before any repository change that needs them: the reindex needs the new builder, the registry gate needs the
  new deriver. The contract regeneration runs after commit 1, the reindex and the contract-template move.
- **P-57 One landing unit.** *[Superseded in repair round 4 by P-57 and P-58 (revised again).]* Every part that edits a prompt body or the registry (PART-05, 06, 07, 10, 11, 13, 14, 15,
  16, 17, 18) lands as one unit, because one page carries several parts' edits and one registry diff carries their
  guards. Before the first Notion write to a body, `land.py plan --no-ops` rehearses every page and must print no
  refusal. PART-06's page must exist first (PART-15 is after PART-06). If a page then fails `check` and cannot be
  repaired forward in the same sitting, every landed page is reversed from the rollback journal (P-58), the registry
  commit is reverted, and the unit is BLOCKED as a whole (template rule 6). The skill parts (PART-01 to 04, 12) are
  a separate unit held by the D24 review.
- **P-58 Rollback journal.** *[Superseded in repair round 4 by P-57 and P-58 (revised again).]* `land.py plan --journal DIR` writes each page's operations to `DIR/<PID>.ops.json` in the
  session scratchpad, so a reversal is mechanical. Under D22 this is part of the landing transaction in hand: outside
  the repository, never hashed or compared, read only to reverse the landing it records, deleted when the unit passes
  its gate or has been reversed, and reported in §E. No other use.
- **P-59 land.py hardening.** *[Its refusals and exit codes are superseded by P-88 and P-96.]* `--no-ops` prints counts only (the rehearsal). The token test refuses only a `{{` the
  edit introduces. A body where every rule and edit reads 0 and every CHECK passes is reported NOTHING_TO_LAND (run
  check), which covers deletion-only bodies. `check` reports STALE_READBACK, not a failure, when a page that should
  carry new text does not yet show it; the executor re-fetches, and only a non-stale failure is acted on (repaired forward: P-58 (revised again)).
- **P-60 The suite gate is a script.** `EV/skills/run_gate.py --set pre|pkg|post` runs each set with its expected
  results embedded and exits non-zero on any difference: `pre` (before the reindex: today's parts fail the new
  builder with exactly 7 bookkeeping errors), `pkg` (the patched tree and the reindexed working tree), `post` (the
  installed tree; no pre-reindex row and no 1.12.0-audit row).
- **P-61 W-4 is required on every A7 row.** G-K24 (`PR-40 is entered on the observed merge event for the identified
  PR`) goes on all 21 ITEM-29 rows (PR-40 keeps its existing G25B, which the same text satisfies), so ITEM-29's
  "uses the A1-5 wording verbatim" has a guard that fails on removal in every body (§A PART-14 gate).
- **P-62** G-K39 (forbidden, the retired storage sentence) goes back on RS-40's row; G-K40 stays off. RS-40's part of
  ITEM-32 keeps a guard that fires if the sentence comes back.
- **P-63 ITEM-22 titles and lane parents.** `nam002_live.py` also checks each lane `notion_parent_id` and every
  parent title against the live child lists, with an injected wrong title as its must-fail case.
- **P-64 PART-16 against the graph.** `EV/engine/graph_check.py` reads QA-110's and QA-80's branches from
  `docs/graph/parts` and asserts the landed bodies state them (the gate for §A PART-16's "text matches the graph").
- **P-65 Tracking-page records.** The PART-11 entry is dated `{{EXECUTE_DATE}}` and inserted before the paragraph that
  introduces "the three decisions below". The freeze start and lift, and the close-out status lines, are drafted as
  exact edits with tokens. They are the run's own record-keeping on a maintenance surface, not items.
- **P-66 Freeze window.** *[Superseded by P-66 (revised), repair round 3.]* The freeze runs from the first Notion write to the close-out merge, not only to the corpus
  gate as §A order 4 says: the landed bodies must not be used before the matching skills are installed. Recorded as an
  upstream finding (spec §10.1).
- **P-67** PART-06-HUB-03 is reduced to a pointer-only rewrite. The eleven PART-06 pointer edits and the AF-009 amendment
  are consequences of ITEM-18 and ITEM-37 that §A's target lists omitted (spec §10.1).
- **P-68** D25 cites the execution specification (not §P) for its wording and guards, and attributes the pull-request
  clause to the approved plan (P-02). The D18 successor names both renamed checks. `{{INSTALL_DATE}}` is the X7.3 date
  and `{{FREEZE_DIGESTS}}` the seven `<skill> <files> <digest>` lines of the post-install comparison.
- **P-69** ITEM-13's regeneration reads one input from a skill, not the repository: the R1 oracle bundled in
  flowmaster-validate, pinned by its digest. Recorded in ITEM-13's disposition, not widened.
- **P-70** The v5.0.0 procedure's pointer to `E3-E4-report.md` for per-body placement goes stale for W-4, ONCE and C-LAT.
  Recorded on the Modification Backlog (MB-004, S3), not edited here.

### Repair round 3 (2026-09-24): the close order and the tokens

- **P-66 (revised) Freeze window.** Nathan confirms the freeze at X5.0, before the run's first Notion write, and lifts
  it at X7.5, once X7.4's post-install verification passes: the seven installed digests equal the packaged ones, the
  `post` gate exits 0 and the corpus gate passes 55/55 with the installed skills. From then on the landed bodies and
  the installed skills agree, so flow sessions may run; the close-out PR that follows carries only records. The lift
  line on the tracking page states only the install, the verification and the lift. This replaces "to the close-out
  merge" (P-66); §A order 4's "after full readback and the corpus gate" stays an upstream finding (spec §10.1),
  because the bodies land before the skills are installed.
- **P-58 (revised) Journal retention.** *[Superseded in repair round 4 by P-57 and P-58 (revised again).]* The rollback journal is kept until X7.4 passes, the last gate that can call
  for a reversal of the body unit, and deleted at X7.5 (or at once after a reversal). It stays in the session
  scratchpad throughout and is reported in §E.
- **P-71 Tokens and their fills.** *[Its fill times are superseded by P-96, which also adds `{{STOP_DATE}}`.]* Every token in the Notion and repository edits, and what fills it. A new text that
  still carries `{{` is refused when it lands (P-48), by `land.py` for bodies and by the readback for the rest.

  | token | filled with | where |
  |---|---|---|
  | `{{CANDIDATE_CRD_LIST_URL}}` | the page URL from X5.1, normalized to `https://app.notion.com/p/<32 hex>` | body rules (R-ITEM18), `P30-DEST`, ten of the eleven PART-06 pointer edits, M2-R4, R5 and R9 (the page's self-links) |
  | `{{EXECUTE_DATE}}` | the UTC date (YYYY-MM-DD) of the Notion write that carries it | `TRACK-FREEZE-START`, `PART-11-TRACK-01`, `PART-18-AF009-01`, `PART-06-HUB-01`'s "Corrected" note, and `TRACK-UNIT-STOPPED` on the stop path (P-85) |
  | `{{MIGRATION_DATE}}` | the UTC date of the X5.1 page creation (P-80, repair round 4) | M2-R1, the M2 callout and revision bullet, `PART-06-HUB-01`'s "held the list until" and the four `PART-06-ITEM*-02` edits |
  | `{{INSTALL_DATE}}` | the UTC date of Nathan's install sitting (X7.3), as X7.4 records it | `CLOSE-D22` |
  | `{{FREEZE_DIGESTS}}` | seven Markdown bullet lines, one per package in manifest order, ``- `<skill>` `<files> <digest>` ``, from X7.4's comparison (P-68) | `CLOSE-D22` |
  | `{{LIFT_DATE}}` | the UTC date Nathan lifts the freeze (X7.5) | `TRACK-FREEZE-LIFT` |
  | `{{CLOSE_DATE}}` | the UTC date of the close commit that sets `COMPLETE` (X7.6) | `TRACK-STATUS-01` to `03` |
- **P-72 Close order.** X7.4 verifies the install. X7.5: Nathan lifts the freeze; `TRACK-FREEZE-LIFT` lands. X7.6: the close commit (`CLOSE-D22`, `P31-POLICY`, `P33-A5NOTE`, §E's install record and the
  X7.5 readback, the dispositions, the actual cost, `COMPLETE`) on the designated branch restarted from `main`, and the
  close-out PR opened. X7.7: `TRACK-STATUS-01` to `03` land, dated by that commit, and their readback is added to §E in
  a second commit on the same PR. X7.8: Nathan merges the close-out PR (the Drive banner is read back at X7.6, P-83). No tracking line
  claims a state before the record holds it.
- **P-73 Commit labels and the registry commit.** `EV/texts/edits.json` labels each text by the step that commits it:
  `X2.2` (the decision record), `X3.5` (`P32-SWR`), `X5.2` (`P30-DEST`, `P30-VERSION`) and `close` (X7.6). The former
  label `2` covered two different commits. The registry diff is committed alone at X3.1, so reverting the body unit
  (P-57) reverts exactly that commit and leaves the reindex and the contract-template move. *[The revert is superseded
  in repair round 4 by P-58 (revised again): a stopped unit leaves the branch unmerged, so nothing is reverted; the
  registry commit stays alone so that §E can name it.]*
- **P-74 The PLAN-time generators.** `EV/registry/apply_registry.py`, `guard_tests.py`, `summarize.py` and
  `build_guards_md.py` ran in the PLAN scratchpad beside a copy of the governance audit's scripts and record how the
  diff, the guard file and `GUARDS.md` were made. EXECUTE runs none of them: it uses `registry.diff`,
  `row_assertions.json` and `nam002_live.py` (with `--audit-root`).

### Repair round 4 (2026-09-24): review round 3 (`wf_b886670d-753`)

- **P-57 (revised again) One landing unit, from the first Notion write.** *[Its resume point is superseded by P-84, and
  its last sentence narrowed by P-94.]* Before X5.0 nothing leaves the branch: no
  Notion write, no merge, no install. A failure before X5.0, a D24 rejection included, stops EXECUTE with the branch
  unmerged, and the fix is a change to the approved plan: EXECUTE returns to PLAN and Nathan approves the change.
  Shipping without a rejected part is such a change (template rule 7). From X5.0 all 17 parts land as one unit: the
  page, the destination rule, the pointers, the 51 bodies and the control-page edits. The packages are installed only
  after the unit has passed (X6) and the execution PR has merged (X7.1), so no part straddles two units. Supersedes
  P-57 and its revision.
- **P-58 (revised again) No rollback journal.** *[Its stop procedure is made exact by P-85, then by P-97 to P-99; its
  forward repair by P-88; its "or he rules a forward fix" is withdrawn by P-99.]* `D22` prohibits backups without exception, and a file of a body's
  replaced text, kept to restore it later, is one. So nothing keeps a copy of a body. The rehearsal (X4.5) proves,
  before any write, that each page's operations reproduce the edit and that the readback will pass on the text they
  produce (P-76). A readback that fails after a landing is repaired forward: the engine re-reads the page and lands
  what is missing. A failure that cannot be repaired forward in the sitting stops the unit: EXECUTE sets the record
  `BLOCKED`, lists in §E every write already made (page, time, edit), reverses the control-page edits (§7 holds each
  `old_str`; control pages are not bodies), moves the new page to trash, keeps the freeze, leaves the branch unmerged
  and returns to Nathan. Restoring a landed body is his action, from Notion's page history, or he rules a forward fix.
  `land.py` loses `--journal` and `reverse`. Supersedes P-58 and P-58 (revised).
- **P-75 The readback fills the page URL.** `land.py check`, like `plan`, fills `{{CANDIDATE_CRD_LIST_URL}}` before it
  compares, and refuses to run on a body whose rules carry the token (CL-40) without `--candidate-url`. Without the
  fill, a correctly landed CL-40 read as not landed, for ever.
- **P-76 The rehearsal runs the readback.** `land.py plan` computes, on the text its operations produce, both the
  precheck and `check` itself, the STALE test included, and refuses unless both pass (`PRECHECK_FAILED`,
  `LANDED_CHECK_FAILED`). So the rehearsal proves the readback each landing will run. Pass 4 (spec §8) ran it on all
  51 bodies.
- **P-77 No Notion write before the checks that need none.** NAM-002 (PART-10) reads only the registry and the hubs'
  child lists, so it runs at X3.6, after the registry commit. The rehearsal runs at X4.5, after the D24 review. Both
  come before X5.0.
- **P-78 Sessions.** *[Made true by P-87: evidence is committed as it is produced. Its rebuild of the packages is superseded by P-100, and its rebuild of `$PKG` limited to steps before X7.3 by P-101.]* Any step can run in a new session. Each needs only the repository, the installed skills and fresh
  Notion reads, or rebuilds the rest from them: `$PKG` by `execute.1.then`, the packages by `execute.4b`, whose
  extracted freeze digests reproduce X4.3's. The D24 verdicts bind to those freeze digests, not to the archives' own
  sha256, which vary with timestamps. A landing resumed in a new session runs `check` on a page that reports
  `ALREADY_LANDED`.
- **P-79 The whole skills root is measured, not held to a constant.** It also covers skills this Modification does not
  change, which may sync at any time. X0.3 and X1.1 record it, and `run_gate.py` checks that each run leaves it as it
  found it. Only the seven package digests are held to expected values.
- **P-80 `{{MIGRATION_DATE}}`** *[Recorded before the create call, not after it, and `{{EXECUTE_DATE}}` is the unit's start date, not the date of each write (P-96).]* is the UTC date of the X5.1 page creation. The page's callout, revision bullet and
  M2-R1, and the pointers' "held the list until" and "moved" clauses carry it, so every record dates the move alike even
  if X5.3 falls on a later day. `{{EXECUTE_DATE}}` stays the date of the write for a "Corrected" note.
- **P-81 Commit 1 carries the status change.** *[Its last sentence is replaced by P-86.]* X2.1 sets `status: EXECUTING` and commit 1 holds it with the
  decision-record entries, so D25's "in its first execution commit" and §A order 2 both hold. D25's closing sentence
  no longer waits on a later update: it points to this record's §E for the date the guards landed.
- **P-82 The post-install failure path is forward only.** *[Its record step is P-94.]* At X7.4 the bodies and the registry are on `main`. An
  installed digest that differs from X4.3's is fixed by reinstalling the delivered file (X7.3 again). Any other failure
  stops EXECUTE with the freeze held and returns to Nathan with the failing rows. Nothing is reversed automatically.
- **P-83 Mechanics.** *[Its evidence list is extended by P-87 and its async rule by P-89.]* EXECUTE's evidence goes to `docs/ephemeral/modifications/evidence/closeout-residuals/execute/`:
  the NAM-002 files (X3.6), the gate summaries (X1.3, X4.2, X7.4), the rehearsal, landing and corpus results (X4.5,
  X5.4, X6.1) and nothing else; no body text (`D22`). Every `notion-update-page` call uses `allow_async: false`. The
  first push after X0.2 and after X7.6 uses `git push --force-with-lease`, because the squash merge leaves the remote
  branch's old history in place. X4.3's packaging and extraction commands are exact (`execute.4b`). The page's three
  self-link spots and their step-7 operations are exact (`M2.json` `self_links`). The Drive banner is read back by
  MGMT-10 before the close commit (X7.6).

### Repair round 5 (2026-09-24): review round 4 (`wf_05b74ccf-d84`)

- **P-84 A stop before X5.0, and how EXECUTE starts again.** *[Superseded by P-84 (revised), repair round 6.]* A failing gate before X5.0, a D24 rejection included,
  stops EXECUTE with nothing outside the branch. EXECUTE writes §E on the branch: a row for each step done, the
  failing step `BLOCKED` with its evidence, and the finding. The status stays `EXECUTING`, because the Modification
  has not ended (template rule 1: a mode that finds its upstream section wrong records a finding and returns). It runs
  `modification_validate.py`, commits and pushes the branch with its `EX/` files, leaves it unmerged, and returns to
  Nathan. The fix is a plan change. A PLAN session copies the stopped attempt's §E rows and `EX/` files into
  `docs/ephemeral/modifications/evidence/closeout-residuals/attempt-<n>/`, revises §P and the spec, sets `PLANNING`
  and, once Nathan approves the change, `PLANNED` with the new `plan_approved_date`; that record reaches `main` by its
  own pull request. EXECUTE then starts again at X0.1. X0.2 restarts the branch from that `main`
  (`--force-with-lease`), which drops the stopped attempt's commits, so every step from X0.1 runs again and nothing is
  resumed in place. Shipping without a rejected part is such a change (template rule 7). Supersedes P-57 (revised
  again)'s "resumes at X1.1".
- **P-85 The stop after X5.0, exactly.** *[Superseded by P-97, P-98 and P-99, repair round 6.]* A failure that `plan` on a fresh fetch cannot repair (P-88) stops the unit.
  EXECUTE, in this order:
  1. lists in §E every write already made: the page, the UTC time, and the edit ids or the body's PID, taken from
     `EX/landing/`, `EX/run.json` and this sitting's tool results;
  2. reverses the control-page edits already applied, in reverse order of application, except `TRACK-FREEZE-START`,
     which stays because the freeze is kept. Each reversal re-fetches the page, takes as `old_str` the text as it now
     stands there (the edit's `new_str` with its tokens filled, as re-fetched), restores the §7 `old_str`, and reads
     back. The PART-06 pointers (X5.3) are reversed the same way;
  3. moves the new page to trash: it re-fetches the Hub and runs `update_content` on it with `old_str` set to the
     page's exact child line as fetched (`<page url="…">Candidate CRD Items List</page>`), `new_str` empty and
     `allow_deleting_content: true`, then re-fetches the Hub to confirm the child is gone. Notion keeps the page in
     its trash, where Nathan can restore it;
  4. applies `TRACK-UNIT-STOPPED` (§7.3), so the tracking page states the stop beside the freeze line;
  5. adds the reversals, the trash call and the tracking line to §E's list; sets every item's disposition to
     `BLOCKED` and each part's outcome in §E *Parts* to blocked, with the landed writes it leaves and their owner.
     A part whose items are all `BLOCKED` is not half applied, so `modification_validate.py` passes. Sets the status
     to `BLOCKED`;
  6. commits and pushes the branch, which stays unmerged, keeps the freeze and returns to Nathan. Restoring a landed
     body is his action, from Notion's page history, or he rules a forward fix.
  Supersedes the stop steps of P-58 (revised again).
- **P-86 The day `D25` applies.** `D25` names its event: the merge that puts its guards on `main` (X7.1), after they
  have fired on the landed bodies (X6.1, `D14`). X7.6 writes into §E the line
  `D25 applies from: <merge commit sha>, <YYYY-MM-DD>` with the X7.1 merge commit and its UTC date, and its gate
  finds that line exactly once. Replaces P-81's "the date the guards landed".
- **P-87 Evidence is committed as it is produced, so any step can run in a new session.** *[`EX/run.json` also holds the token values (P-96); the list is extended by P-102 (i).]* X0.2 starts `EX/run.json`
  (`$BASE` and the X0.3(e) root digest); X1.1 adds its root digest. Commit 1 (X2.2) carries `EX/run.json` and
  `EX/gate_pre.json` with the decision record and the record. X3.6 commits `EX/nam002/`; X4.2 and X4.3 commit
  `EX/gate_pkg.json` and `EX/packages.json` (the seven freeze lines and archive sha256s); X4.4 commits the brief before
  the review and each verdict, unedited, as it returns; X4.5 commits `EX/rehearsal/`; X5.1 adds the page id, `<URL>`
  and `{{MIGRATION_DATE}}` to `EX/run.json`, committed at X5.2; X5.4 commits `EX/landing/` after each batch; X6.4
  commits `EX/corpus/`; X7.4's `EX/gate_post.json` and `EX/corpus-post/` go into the close commit. A new session
  fetches the pushed branch, reads `EX/run.json`, rebuilds `$PKG` (`execute.1.then`) and the packages
  (`execute.4b`), and re-fetches Notion. The session starts at the repository root, so its harness files are where
  `land.py` looks (`--harness-root` otherwise). A landing summary that is lost can be rebuilt: `check` on a landed page
  reproduces it. Replaces X1.3's "committed at X6.4".
- **P-88 Forward repair, in the engine.** *[Its pass-5 counts are rows, 476 of them distinct, and pass 6 ran `plan` on the landed text (P-96, P-102 (k)); a refused partial stops the unit by P-98's procedure.]* `land.py` states each edit on the fetched page: `NOT_LANDED` (its anchor
  matches its expected count and its new text is not already in place), `LANDED` (its new text stands where the
  anchor matches, or a replacement's anchor is gone and its new text is present, or a deletion's anchor is gone) or
  `MIXED`. `plan` plans only the `NOT_LANDED` edits and lists the `LANDED` ones as `repair`; it refuses a `MIXED` edit
  (`COUNT_MISMATCH`) and a page where every edit reads landed (`ALREADY_LANDED`). `check` reports
  `STALE_READBACK_OR_NOT_LANDED` unless every edit reads landed, fails on an insertion that occurs twice in a row
  (`doubled_insertions`), prints the harness file it read (`source_file`), and exits 1 when it fails. `repair` must be
  `[]` on the rehearsal (X4.5) and on each page's first `plan` at X5.4; it may be non-empty only on a re-plan after a
  landing call on that page. `dryrun.latest_body` takes the newest capture first (a tool-results file's capture time
  is its mtime), because a page's "as of" need not advance when it is edited. Two cases the first draft got wrong,
  both found by running it: a replacement whose new text is part of the text it replaces (CL-30's `LCL-30-2` and
  PR-10's `R-ITEM38` leave `;`) read `LANDED` on the unlanded page, so a replacement now reads landed only where the
  match lies inside an occurrence of its new text; and QA-10's `R-OWN` is anchored after the sentence that
  `LQA-10-P03` rewrites, so on the landed page its anchor was gone and it read `MIXED`, so QA-10's `R-OWN` anchor
  matches that sentence before or after `LQA-10-P03`. Proved on synthetic text (every subset of one body's
  operations) and by pass 5 on every live body (§8.4): 51 of 51 plan with `repair` `[]`; on each landed page every edit
  reads `LANDED`; of 516 partial landings, 450 are repaired to exactly the landed page, 66 are refused and none is
  repaired to anything else. A refused partial stops the unit (P-85).
- **P-89 Asynchronous writes.** After every `notion-update-page` or `notion-create-pages` call whose response is an
  `async_task`, EXECUTE polls `notion-get-async-task` until the task reads `succeeded` or `failed`, waiting as the
  response suggests. A failed task is an uncertain write: re-fetch and inspect the page before anything else. Only
  then does EXECUTE re-fetch and check, so a pending task never counts as a stale readback.
- **P-90 A control-page edit is applied once.** *[Made exact by P-96: `ctrl.py edits` with the values recorded in `EX/run.json`.]* Before each control-page edit, EXECUTE re-fetches the page. If the
  edit's filled new text (its `new_str` less its `old_str`) is already there, the edit has landed: it goes straight to
  the readback. Otherwise its `old_str` must occur exactly once. This covers every insertion that keeps its own anchor
  (`TRACK-*`, `PART-11-TRACK-01`, `PART-12-HUB-01`, `PART-18-AF009-01`, the `PART-06-ITEM*-02` entries).
- **P-91 No code inside bold.** Notion reads a bold run that holds a code span back split around the code, so the
  literal `new_str` would not be found. `PART-18-AF009-01` now closes its bold before the code. A scan of the 20
  control-page edits and `M2.json` finds no other bold run with code in it. Each control-page readback compares the
  re-fetched page with the `new_str` as filled.
- **P-92 Guarded removals and a failing X4.3 gate.** *[The proof keeps up to 400 lines per step (P-102 (k)).]* Every `rm -rf` in the manifest takes the form `"${VAR:?}"`, which
  cannot expand to `/` and which the session's safety check allows (the unguarded form needs a person's approval).
  `execute.4b` writes the seven extracted freeze lines to a file and compares it by `diff` with
  `EV/skills/expected_after_patch.txt`, so X4.3's gate fails mechanically on a mismatch. The §9-order proof was run
  again and keeps each step's full output (`gate_proof_x.json`, built by `build_gate_proof.py`).
- **P-93 What the D24 verdicts bind to.** *[Superseded by P-100, repair round 6.]* The brief's §1 lists, for each package, the archive name, file count, bytes
  and sha256, marked informative because a re-cut changes it, and the extracted freeze digest (`<files> <digest>`) as
  the identity the verdict binds to. Its §10 binds each verdict to those freeze digests and makes it void for any other
  file content. The brief is `docs/ephemeral/modifications/evidence/closeout-residuals/REVIEWER-BRIEF-cr1.md`; the
  verdicts are `SECTION-10-REVIEW-cr1-SFR-CR1-1.md` and `-2.md` beside it, each committed unedited as it returns.
- **P-94 X7.4 runs on `main`, and its failure is recorded.** *[Its reset waits on P-97's guard, its push follows `git fetch --prune origin`, and its record commit also writes the D25 line (P-102 (g)).]* X7.4 begins by restarting the branch from `main`
  (`git fetch origin main && git checkout -B claude/epic-tesla-17406z origin/main`), so both gates read `main`'s
  registry and parts. X7.6 continues on that branch. If X7.4 fails and a reinstall does not fix it (P-82), EXECUTE
  writes §E's X7.4 row (the failing rows, the installed digests, the freeze held), keeps the status `EXECUTING`,
  commits and pushes (`--force-with-lease`), opens a record pull request, and returns to Nathan. This narrows P-57
  (revised again)'s "no part straddles two units": a part with a skill half lands its repository and Notion halves in
  the unit, and its package at X7.3, after the unit has passed and merged; the package is verified at X7.4 and fixed
  forward only.
- **P-95 Smaller corrections.** X3.1 and X6.3 give their exact commands. X4.5 runs `plan` on the 51 bodies with edits
  and `check` on the five without (CF-PO-10, MGR-10, IA-40, IA-50, IA-60); X5.4 lands those 51 less
  `GCFPE-MGMT-10-PROPOSED`, whose landing is X5.5. A new read-only step X4.6 downloads the Drive file and checks its
  bytes, the nine M2 old strings and the Hub collision before X5.0, so a changed file stops EXECUTE before any Notion
  write; X5.1 downloads it again and repeats the checks. X5.1 resumes a create that was already made: a Hub child
  titled *Candidate CRD Items List* whose callout names this Modification is this run's page, read back against F1 to
  F10 and continued at step 7; any other child of that title is a collision. F6 counts 8 pairs at step 6 and 11 after
  step 7. When `plan`'s operations exceed the tool's output limit, EXECUTE reads them from the harness's saved output
  file, under the same transient rule (`D22`). §P's not-in-scope line points to step 19, and §11 counts a D24
  rejection at a plan approval, a review round and a record merge.

### Repair round 6 (2026-09-24): review round 5 (`wf_ad66aa45-00a`)

- **P-96 A resumed step recognizes what already landed.** Every token value a Notion write carries is fixed once,
  written to `EX/run.json`, committed and pushed before the first write that carries it. Every later fill, readback,
  apply-once test and reversal uses the recorded value, on whatever day and in whatever session it runs. Round 5's
  plan filled `{{EXECUTE_DATE}}` with the date of each write and recorded it nowhere, so a session resuming on a later
  UTC day could not recognize a landed control-page edit: it would apply an insertion a second time, or stop the unit
  on a correctly landed replacement (completeness#0, executability#0, consistency#2). The values, and when each is
  recorded:

  | token | `EX/run.json` key | recorded | where it is used |
  |---|---|---|---|
  | `{{CANDIDATE_CRD_LIST_URL}}` | `url` (and `page_id`) | at X5.1 as soon as the create returns, committed and pushed before step 7's write | body rules (R-ITEM18), `P30-DEST`, ten PART-06 pointers, M2-R4, R5 and R9 |
  | `{{MIGRATION_DATE}}` | `migration_date` | at X5.1, the UTC date, committed and pushed before the create call | M2-R1, the M2 callout and revision bullet, `PART-06-HUB-01`, the four `PART-06-ITEM*-02` edits |
  | `{{EXECUTE_DATE}}` | `execute_date` | at X5.0, the UTC date, committed and pushed before `TRACK-FREEZE-START`: the date the unit started | `TRACK-FREEZE-START`, `PART-11-TRACK-01`, `PART-18-AF009-01`, `PART-06-HUB-01`'s "Corrected" note |
  | `{{STOP_DATE}}` | `stop_date` | at a stop after X5.0, the UTC date, first (P-98 step 1) | `TRACK-UNIT-STOPPED`, `TRACK-STATUS-STOP-01` to `03`, `TRACK-FREEZE-LIFT-STOP` |
  | `{{INSTALL_DATE}}` | `install_date` | at X7.4, first: the UTC date Nathan gives for his install sitting, or of his install confirmation when he gives none | `CLOSE-D22` |
  | `{{LIFT_DATE}}` | `lift_date` | when Nathan lifts the freeze, before `TRACK-FREEZE-LIFT` (X7.5) or `TRACK-FREEZE-LIFT-STOP` (P-99) | those two lines |
  | `{{CLOSE_DATE}}` | `close_date` | at X7.6, the UTC date, in the close commit itself | `TRACK-STATUS-01` to `03` (X7.7) |
  | `{{FREEZE_DIGESTS}}` | — | at X7.4: `EX/installed_freeze.txt`, execute.5's seven lines | `CLOSE-D22` (`EV/texts/apply_texts.py`) |

  The apply-once test (P-90) is `python3 EV/engine/ctrl.py edits <PAGE> <EDIT_ID>... --run EX/run.json` on a fresh
  fetch. `LANDED`: the edit has landed and goes to its readback. `NOT_LANDED`: apply it. `TOKEN_NOT_RECORDED`: a value
  it carries was not recorded, so it was never written; record the value, push, and test again. `MIXED`: it cannot be
  repaired forward (P-98). `EV/notion/ctrl_proof.py` replays the success and stop sequences on the seven live control
  pages with a stand-in `run.json`: every step's test reads right, and a resume with the same `run.json` reads every
  landed edit `LANDED`; with the execute date moved one day, as round 5 would have filled it, four landed edits are
  missed (the finding, reproduced). `land.py` gets the same property for bodies. `plan` refuses `ALREADY_LANDED`
  whenever every live edit reads `LANDED`, before it tests `NOTHING_TO_LAND`, so a landed deletion-only or
  replacement-only body (IA-10, IA-20, UTIL-10 and others) resumes by `check` like any other (executability#1).
  `check` reports `STALE_READBACK_OR_NOT_LANDED` whenever an edit does not read `LANDED`, with no exception for a page
  where no anchor matches (executability#5). Pass 6 (spec §8.5) ran the refusal chain itself, through `land.py`'s
  `main()` on each fetch, on all 51 bodies with edits. `state` reads `UNTOUCHED` on every fetch and `LANDED` on every
  landed text. `plan` on every landed text exits 3 with `ALREADY_LANDED`. Of 476 distinct partial landings, every one
  reads `PARTIAL`: 410 are repaired to exactly the landed text, 66 are refused (`COUNT_MISMATCH`, on QA-10, PR-10,
  PR-20, PR-40, OPS-10, OPS-20 and OPS-30), and none is repaired to anything else. On an X5.1 resume the migration
  date is already recorded, and the step-7 operations go through the same test, so F6 counts 11 after step 7 either
  way. Supersedes P-71's fill times and P-80's "the UTC date of the X5.1 page creation" (now recorded before the create),
  and makes P-90 exact.
- **P-97 A stop's record reaches `main`.** Round 5 left a stopped attempt's record, its §E list of Notion writes and
  `EX/` only on the unmerged branch, while `main` kept a record that still passed X0.1, and the next X0.2 would have
  reset that branch (completeness#2, #4, #5). Every stop now ends with a record pull request, in this order:
  1. `mkdir -p "$SCRATCH/attempt"`; `git log --format='%H %s' origin/main..HEAD > "$SCRATCH/attempt/commits.txt"`;
     copy `EX/` and this attempt's briefs and verdicts (`REVIEWER-PROMPT-cr*.md`, `SECTION-10-REVIEW-cr*-*.md` in
     `docs/ephemeral/modifications/evidence/closeout-residuals/`) and the record's §E text into `$SCRATCH/attempt/`;
  2. `git fetch --prune origin && git checkout -B claude/epic-tesla-17406z origin/main`;
  3. `n` = 1 + the number of `attempt-*/` directories in the closeout-residuals evidence directory on `main`. Copy
     `$SCRATCH/attempt/` (less the §E text) to `docs/ephemeral/modifications/evidence/closeout-residuals/attempt-<n>/`,
     with `EX/` as `attempt-<n>/execute/`. From here on, the stopped attempt's `run.json` is
     `attempt-<n>/execute/run.json`: every later `--run`, and every value recorded after the stop (`lift_date`), uses
     that file;
  4. in `main`'s record, set `status: EXECUTING` (its `plan_approved_by` is set) and add to §E a subsection
     *Attempt <n>* holding the stopped attempt's rows. The rows are each step done, the failing step `BLOCKED` with
     its evidence, the finding, and, after X5.0, the sweep's list (P-98). They also say that archives delivered at
     X4.4, if any, must not be installed;
  5. run `modification_validate.py`, commit (*closeout-residuals attempt <n> stopped: record*), push
     (`git push --force-with-lease origin claude/epic-tesla-17406z`), open the record pull request against `main`, and
     return to Nathan.
  The attempt's execution commits leave the branch; their list is in `attempt-<n>/commits.txt`, and the next attempt
  rebuilds each from `EV`. **The reset guard.** Every other reset of the branch to `origin/main` first runs
  `git fetch --prune origin`. These resets are X0.2, X7.4, a plan change's PLAN session (P-84) and the restoration
  check (P-99). Then, when `origin/claude/epic-tesla-17406z` exists,
  `git diff --quiet origin/main origin/claude/epic-tesla-17406z -- docs/ephemeral/modifications/MODIFICATION-20260923-closeout-residuals.md docs/ephemeral/modifications/evidence/closeout-residuals`
  must exit 0: the remote branch holds no record or evidence that `main` lacks. Otherwise the reset is refused and
  EXECUTE returns to Nathan, because that branch's pull request must merge first. The guard makes X7.4 wait for a
  P-94 record PR (completeness#13). X0.1 requires `main`'s record at `PLANNED`, so an attempt cannot start over an
  unresolved stop. Every `--force-with-lease` push follows a `git fetch --prune origin`, so a branch deleted on merge
  leaves no stale lease (executability#2).
- **P-98 The stop sweep, after X5.0.** A failure that cannot be repaired forward (P-88: a refusal on a page's first
  `plan`, a second failing `check`, a failed async task that the fresh fetch cannot explain, or an apply-once test that
  reads `MIXED`) stops the unit. EXECUTE, in this order:
  1. records `stop_date` in `EX/run.json`, commits and pushes;
  2. **sweeps Notion**, read-only. For each of the 51 bodies with edits: fetch;
     `python3 EV/engine/land.py state <PID> <PAGE>` (CL-40: `--candidate-url <URL>` when `url` is recorded), output to
     `EX/stop/bodies/<PID>.json`. Then fetch the seven control pages and run
     `python3 EV/engine/ctrl.py all --run EX/run.json > EX/stop/control.json`. Then fetch the Hub and run
     `python3 EV/engine/ctrl.py children <HUB> > EX/stop/hub.json`. The list of writes is every body whose verdict is not
     `UNTOUCHED`, with its edit states; every control edit that reads `LANDED` or `MIXED`; and the page, if the Hub
     lists a *Candidate CRD Items List* child. The list comes from Notion, so it includes writes made by an earlier
     sitting; times come from `EX/landing/` where recorded (completeness#1);
  3. reverses each control edit the sweep reads `LANDED`, except `TRACK-FREEZE-START`, in reverse §9 order: re-fetch;
     `old_str` is the edit's `new_str` filled from `EX/run.json`, as the page shows it; `new_str` is its §7 `old_str`;
     read back with `ctrl.py edits`, which must read `NOT_LANDED` with `old_count` 1. A control edit that reads `MIXED`
     is not touched; it stays on the list for Nathan;
  4. if the Hub lists the page, trashes it: `update_content` on the Hub with `old_str` the page's exact child line
     as fetched, `new_str` empty, `allow_deleting_content: true`; then re-fetches the Hub. If the page does not exist,
     it skips this step;
  5. re-runs `ctrl.py all` and `ctrl.py children` into `EX/stop/` to confirm that no control edit but
     `TRACK-FREEZE-START` reads `LANDED` and that no such child remains;
  6. writes §E's stop rows (the list, each body pending Nathan's restoration, the reversals, the trash call, each
     step done, the failing step `BLOCKED` with its evidence, the finding) and runs the stop record (P-97). The status
     stays `EXECUTING`;
  7. after the record PR is pushed, applies `TRACK-UNIT-STOPPED` and `TRACK-STATUS-STOP-01` to `03` (§7.3; P-90's
     test with `--run attempt-<n>/execute/run.json`), reads them back, and records the readback in §E in a second commit on the record PR, pushed with
     `--force-with-lease` after `git fetch --prune origin`. So no tracking line claims a record before it exists
     (consistency#0).
  The freeze and `TRACK-FREEZE-START` stay. Supersedes P-85's steps.
- **P-99 After a stop past X5.0: restore, verify, then end or change the plan.** Round 5 set every item and the status
  to `BLOCKED` while landed bodies were still live. That is terminal, against template rule 6 ("Roll back what was
  applied, or unblock the rest"), and it left "a forward fix" with no vehicle (completeness#3, consistency#1). Now the
  status stays `EXECUTING`. Nathan restores each body on the list from Notion's page history. Then, at his direction,
  a `GCFPE-MGMT-10` session runs the **restoration check** on the branch reset from `main` (P-97's guard). The check
  runs the sweep again: every one of the 51 bodies reads `UNTOUCHED`;
  `ctrl.py all --run attempt-<n>/execute/run.json --expect restored` exits 0, so only the freeze line and the four stop
  lines read `LANDED`; and the Hub lists no *Candidate CRD Items List* child. The session writes `attempt-<n>/restore/`
  and a §E row. A body that does not read
  `UNTOUCHED` goes back to Nathan by name, and EXECUTE restores nothing. Then Nathan chooses:
  - **end**: every item's disposition and each part's outcome is `BLOCKED` with its applied steps rolled back, which
    is now true and checked; the status is `BLOCKED`; `modification_validate.py`; commit; record PR;
  - **a plan change** (P-84 revised): the plan change also revises §7's control-page edits for the pages as they then
    stand, because the stop lines replaced the anchors of `TRACK-STATUS-01` to `03`.
  When Nathan lifts the freeze, which he may do once the restoration check has passed, MGMT-10 records `lift_date` in
  `attempt-<n>/execute/run.json`,
  applies `TRACK-FREEZE-LIFT-STOP`, reads it back, and records the readback in §E. It goes in the restoration
  record's pull request if that is open, or in a record PR of its own. "A forward fix" is withdrawn: after a stop,
  nothing more lands except through a plan change after the restoration. Supersedes P-85's end state and P-58
  (revised again)'s "or he rules a forward fix".
- **P-84 (revised) A stop before X5.0, and how EXECUTE starts again.** A failing gate before X5.0, a D24 rejection
  included, stops EXECUTE with nothing outside the branch. EXECUTE writes the stop rows and runs the stop record
  (P-97), so `main`'s record goes to `EXECUTING` with them. Nothing was applied outside the branch, so nothing is
  restored. Nathan then chooses one of two routes. The first is to end: items and status `BLOCKED` through a record
  PR, and nothing was applied. The second is a plan change. Once the stop record has merged, a PLAN session resets the
  designated branch from `origin/main` (P-97's guard). It revises §P, the specification and `EV`, and writes
  `EV/skills/REVIEWER-PROMPT-prior.md` for the next review round (P-100). It sets `PLANNING`, and on Nathan's approval
  `PLANNED` with the new `plan_approved_by` and `plan_approved_date`, then opens the plan-change PR. §E keeps each
  attempt's subsection as written, because PLAN does not edit §E (template rule 1). Once the plan-change PR has
  merged, EXECUTE starts again at X0.1, and every step runs again; nothing is resumed in place. Shipping without a
  rejected part is such a change (template rule 7). Supersedes P-84. The phrase it withdrew, "resumes at X1.1", came
  from round 4's §9 landing-unit rule, not from P-57 (consistency#12).
- **P-100 The review binds to the archives it read, and those are the archives delivered.** `D24` requires the
  canonical template, filled, and its §10 binds the verdict to every digest in §1. The packaging convention binds a
  confirmation to the `.skill` digests and voids it for any other bytes. Round 5's plan re-cut the archives in a new
  session and bound the verdicts to freeze digests only, which changed §10 (consistency#3). Re-packaging a rebuilt
  tree gives another sha256 with the same freeze digest (measured: `EV/skills/results/brief_fill_proof.json`). So:
  - the brief is drafted at PLAN (executability#3, completeness#14). `EV/skills/REVIEWER-PROMPT-cr.draft.md` is the
    template with §2 to §9 filled. `EV/skills/packages_json.py` writes `EX/packages.json` at X4.3: each archive's
    name, file entries, bytes and sha256, and its extracted freeze line. `EV/skills/fill_brief.py` fills the draft's
    six tokens at X4.4, mechanically: the round number, the archives, their directory, `HEAD`, and §2's and §10's
    prior-round text by variant;
  - the brief is `docs/ephemeral/modifications/evidence/closeout-residuals/REVIEWER-PROMPT-cr<k>.md` (the naming of
    rounds a1 to a5; consistency#11), and the verdicts are `SECTION-10-REVIEW-cr<k>-SFR-CR<k>-1.md` and `-2.md`
    beside it. `k` = 1 + the number of earlier `REVIEWER-PROMPT-cr*.md` there and under `attempt-*/`. A round after a
    plan change cites the prior round's paths, verdicts and digests in §2, and asks for the disposition of each prior
    finding in §10;
  - §1 lists both digests for each package, and §10 is the canonical text, unchanged;
  - when both verdicts return `SKILL_FIT_CONFIRMED`, X4.4 ends by delivering the seven X4.3 archives with
    `SendUserFile`. Each caption leads with the archive's sha256, then its freeze digest. The brief and both verdict
    files go with them, with the instruction to install at X7.3 and not before. Nothing is re-cut after delivery.
    X7.2 is Nathan's install cue, and X7.4 checks each installed freeze digest against `EX/packages.json`;
  - if the session holding the archives ends between X4.3 and the delivery, X4.3 runs again in the new session and
    X4.4 runs a new round with the re-cut variant. The earlier brief, and any verdicts, stay committed unedited;
  - a `SKILL_REPAIR_REQUIRED` verdict stops EXECUTE before X5.0 (P-84 revised).
  Supersedes P-93, and P-78's rebuild of the packages in a new session.
- **P-101 Sessions.** A new session at a step before X7.3 fetches the pushed branch, reads `EX/run.json`, rebuilds
  `$PKG` (`execute.1.then`) and re-fetches Notion; the archives are re-cut only as P-100 says. From X7.3 on, `$INST`
  holds the patched packages, and a new session rebuilds neither `$PKG` nor the archives: `execute.1.then` would
  patch a tree that is already patched and fail (executability#4). The engine reads only the running session's harness
  files: `dryrun.SESSION` is `$CLAUDE_CODE_SESSION_ID`, and `--session` sets it otherwise. So another session's fetch
  of the same page is never taken for the one just made (executability#9). X5.4, X6.1 and X7.4 also check that each
  printed `source_file` lies under this session's directory and that `fetched` is the "as of" time of the fetch just
  made. `ctrl.py` (`edits`, `all`, `children`) and `drive_check.py` are the committed read-only helpers for X3.6, X4.6,
  X5.1 and the sweeps, so no step copies a hash, count or id by hand (executability#11). Pass 6 ran before the session
  filter was added, and every harness file it read belongs to this session, the only one under the project directory,
  so its selections are unchanged.
- **P-102 Smaller corrections (round 5's non-blocking findings).** (a) X4.6 also runs
  `ctrl.py all --run EX/run.json --expect unlanded`: every control edit's `old_str` occurs exactly once and none is
  landed, before X5.0 (completeness#11). It passes on today's pages (`EV/notion/anchor_check_plan.json`).
  `drive_check.py --hub` does X4.6's Drive and collision checks (`EV/notion/drive_check_plan.json`). (b) X6.3's command
  is in the manifest's execute block (`execute.6`), unescaped (executability#6). (c) X7.6's token gate is
  `git show --format= HEAD | grep '^+[^+]' | grep -c '{{'` printing `0`: it reads only the lines the close commit adds
  (executability#7). (d) X0.3(c) reads "prints embedded JSON 575074 bytes sha256 `ae2bd159…`; `g0.md` itself hashes
  to `a70a9326…`" (executability#8). (e) The Drive banner window opens when X6.4 passes and closes at X7.6. After
  X6.4 the page is permanent, because a failure after it is forward only, so the banner never points at a trashed page
  (completeness#12, consistency#9). (f) X0.1 reads "merges the record PR (#478, or the plan-change PR after a stop)"
  (consistency#12). (g) P-94's record commit also writes `D25 applies from: <X7.1 merge sha>, <date>`, and X7.6
  writes that line only when it is absent, so its gate still counts 1 (completeness#8, consistency#10).
  (h) `{{INSTALL_DATE}}` comes from Nathan's install confirmation (P-96, completeness#9). The Product Owner action for
  an X7.4 stop is: merge the record PR, then rule a reinstall or a plan change for new packages; bodies are not
  restored (completeness#6). (i) P-87's list adds `EX/drive_check.json` and `EX/anchor_check.json` (X4.6),
  `EX/graph_check.json` (X6.2, committed at X6.4), `EX/installed_freeze.txt` (X7.4), `EX/stop/`, and after a stop `attempt-<n>/restore/`
  (consistency#13). The manifest's `BASE` is read from
  `EX/run.json` (completeness#15c). (j) §4.4 step 5 and `GUARDS.md` PART-10 step 5 say "committed and pushed at X3.6
  (P-87)" and cite P-84 (revised) for a stop (consistency#6, completeness#15b). (k) Claims are worded as run. Pass 5
  tried 2n subsets per body: 516 rows, 476 of them distinct. Pass 6 counts distinct partials only. The §9-order proof
  covered the manifest commands, not X0.3(a), (c) or (d), X3.1's validator and deriver, X3.6, X4.4 to X4.6, X5 or X6,
  and it keeps up to 400 lines per step (the first and last 200) (executability#10, consistency#4, #5).
  `EV/texts/apply_texts.py`, which the proof ran as a scratch copy, is committed with its fills and token refusal, and
  it is X2.1's, X3.4's, X5.2's and X7.6's applier. Its X2.2 output equals the proof's (`EV/texts/apply_texts_proof.json`).
  (l) The `NOTES.md` banner is current (consistency#8). (m) Supersession marks are added to P-49, P-51, P-59, P-71,
  P-78, P-80, P-81, P-84, P-85 and P-93 (consistency#7).

## §2 Every PLAN review finding and drafter issue, with its disposition

The first PLAN workflow (`wf_73fca782-464`) ended with two reviews: completeness (21 findings, 14 required) and
executability (18 findings, 12 required). Each finding below is answered by a decision in §1 and by the section
of this specification that carries it. None is left open.

### 2.1 Completeness review

| # | severity | finding | disposition | carried in |
|---|---|---|---|---|
| C-R1 | required | The decision-record texts were not drafted, and nothing ordered them first | Drafted: D25 (D25-A, D25-B), the D23-C, D23-G and D18 successors and the D14 note, all in commit 1, before any other edit. The D22 status goes in the close commit | P-29, P-43; §6; §9 X2 |
| C-R2 | required | PART-06 lacked the destination rule, the page creation and migration, and Nathan's Drive banner | Destination-rule row drafted for `notion-write-boundary.md`. The page creation, M2 migration, readback F1–F10 and the eleven pointer edits are ordered steps. The Drive banner is a Product Owner action | P-30, P-46, P-47; §6; §7.4; §9 X5.1–X5.3 |
| C-R3 | required | No execution sequence | §9 gives the ordered sequence, with actor, gate and readback for each step | §9 |
| C-R4 | required | The PART-11 entry on the D20 tracking page was not planned | Drafted entry `PART-11-TRACK-01`, dated by its write date | P-51; §7.3 |
| C-R5 | required | PART-12's Hub and `session-working-rules.md` edits were missing | Drafted, with P-32's sentence verbatim in all three homes | P-32; §6; §7.1 |
| C-R6 | required | PART-17's policy edit was not drafted | Drafted (`P31-POLICY`). It lands in the close commit, once the whole-body check is installed | P-31, P-43; §6 |
| C-R7 | required | PART-18's PE Metaprompt overlay was not checked | Read in full: it states no C-LAT placement; it places canonical texts where the registry row requires them, which stays true. One control page does state the placement (AF-009 on the Alpha feedback list) and gets a dated amendment | P-44; §7.2 |
| C-R8 | required | PART-04's correction note on the repair-a4 record was not drafted | Drafted (`P33-A5NOTE`), appended to `REVIEWER-PROMPT-a5.md`, which states C8 and §2; it names the residual limit | P-33, P-43; §6 |
| C-R9 | required | PART-08 had no entry | PART-08 is `NOT_APPLICABLE` (§A: mention bans correctly scoped). §P records it and §E disposes of ITEM-20 | §P step 22 |
| C-R10 | required | CL-30's second A2 carrier was unedited and unguarded | `LCL-30-2` drops the conflict-history item from the outgoing ADR package, and G-K52 guards it | P-18; §3.4; §4 |
| C-R11 | required | R-OWN did not reach CL-40's and GCFPE-MGMT-10's pull-request claims | R-OWN's sentence now ends "and any pull request that carries them"; both prompts open a PR for their outputs | P-02, P-41; §3.2 |
| C-R12 | required | The rule table disagreed with the bodies | Corrected: PR-10 to R-A1b; the R-26-FRAME counts; R-A2g's IA-30 anchor and counts; DOC-20's A7 form; R-A5 `NOT_APPLICABLE` on RS-40. The census points are recorded as upstream findings | P-04–P-08, P-34; §3; §10 |
| C-R13 | required | G-K08, G-K19 and G-K40 would miss or false-fire | G-K08 amended, with the OPS extension; G-K19's PR-10 fragment corrected; G-K39 and G-K40 leave RS-40 | P-06, P-17, P-28; §4 |
| C-R14 | required | The BRANCH-RECV sentence tripped G06 | The G06-silent sentence is used at every site; G06 reads 0 on all five bodies in the dry run | P-01; §3; §8 |
| C-N1 | non-blocking | R-26-P4's scope | Applies to every carrier; 0 in OPS-10 and OPS-20 is expected | P-13 |
| C-N2 | non-blocking | Kept sentences judged NOT_REAL | Listed with reasons | §10.3 |
| C-N3 | non-blocking | PR-10's CANDIDATE_AUTHORING_LEFTOVER finding | Census A3d NOT_REAL overrides the lane verdict; no edit | §10.3 |
| C-N4 | non-blocking | change-flow's forbidden entries had no own regression, and no `--check` negative control had run | 11/11 must-fail cases on change-flow's own validator; the negative control reports DIFFERENT, exit 1 | P-25; §5 |
| C-N5 | non-blocking | R-ITEM35 restated the rule | Pointer only | P-14 |
| C-N6 | non-blocking | QA-10's twin of OPS-30's deletion | QA-10 carries the sentence; `LQA-10-P19` deletes it, and G-K54 guards both | P-19, P-42 |
| C-N7 | non-blocking | G-K35 on every row; G-K47's anchor | G-K35 per row. G-K47 is tied to its own site | P-02, P-15 |

### 2.2 Executability review

| # | severity | finding | disposition | carried in |
|---|---|---|---|---|
| X-R1 | required | R-ITEM40 did not compile | Its own pattern, without the release alternative. R-ITEM23's pattern is the second gate; both compile on 3.11 | P-09 |
| X-R2 | required | R-A2g was not minimal | IA-30's scoped anchor, the measured counts, and the LOCAL owners of the missed sites | P-07 |
| X-R3 | required | PR-10 was in R-A1a | Moved to R-A1b | P-05 |
| X-R4 | required | R-A7-LOCAL missed DOC-20's backtick form | Widened; the DOC sites are guarded through G-K26 | P-08, P-42 |
| X-R5 | required | G-K40 on RS-40 | Removed | P-04 |
| X-R6 | required | G-K19 and G-K08 left REAL sites unguarded | Corrected, and proved on all ten A2g rows | P-06, P-17; §8 |
| X-R7 | required | BRANCH-RECV against G06 | As C-R14 | P-01 |
| X-R8 | required | contract_recipe's once-per-merge slice would read later successors | The slice ends at the next heading and asserts two lines; tested on synthetic records | P-21; §5 |
| X-R9 | required | Regression strings above 15 words | Every regression is 12 words or fewer, its shortest firing fragment | P-12; §4 |
| X-R10 | required | BRANCH-RECV and R-ITEM30d not executable; order unstated | BRANCH-RECV is LOCAL-only; R-ITEM30d split in two; shared rules apply before LOCAL edits | P-01, P-10, P-11 |
| X-R11 | required | The R-ITEM18 placeholder and the destination rule | The URL is filled from the created page; the landing tool refuses `{{` | P-30, P-48; §9 X5 |
| X-R12 | required | The policy line and the decision-record entries | As C-R1 and C-R6 | P-29, P-31 |
| X-N1 | non-blocking | G-K47 | As C-N7 | P-15 |
| X-N2 | non-blocking | Install timing | The execution PR merges first, then the install, then the close-out PR | §9 X7; §11 |
| X-N3 | non-blocking | Authored wording in FRAME slots | Allowed with C-HANDOFF and C-ART vocabulary; every authored phrase is listed for acceptance | P-20; §3.6 |
| X-N4 | non-blocking | Decorated release labels | The `{0,2}` suffix in the registry and R-ITEM23; flowmaster-validate already strips them (56/56 synthetic cases) | P-16 |
| X-N5 | non-blocking | Scratch scripts that re-read harness files | Not committed and not re-run | P-36 |
| X-N6 | non-blocking | MGMT-10's storage sentence; QA-10's literal ITEM-17 | MGMT-10 variant names its control files; QA-10's role sentence drops "read-only" | P-03, P-04 |

### 2.3 Drafter open issues and unplaceable notes

| source | issue | disposition |
|---|---|---|
| canon | calibration limits: 6 bodies read, 2 in python | Superseded: all 51 bodies ran through the engine twice (§8) |
| canon | harness-saved files | Disclosed in §8.6; none is committed or re-read (P-36, P-39) |
| canon | R-26-P4 scope | P-13 |
| canon | kept NOT_REAL sentences | §10.3 |
| canon | R-OWN design vs a literal ITEM-17 | P-03 |
| canon | A3b stays where it is a separate sentence | Confirmed in PR-40, QA-10, CL-20, OPS-30 by the dry runs |
| canon | W-4 appears three times in PR-40 | Accepted: each site replaced its own entry claim with canonical wording; paraphrase is not allowed |
| canon | PR-35's A7 sentences ride R-ITEM30d | Confirmed: they bar `MERGE_OBSERVED`, which is ITEM-30's statement |
| canon | DOC-20's route to PR-40 | Outside the frozen scope; follow-up (§10.2) |
| canon | unread bodies | Superseded: all read (§8) |
| canon | ITEM-40 census inconsistency | Upstream finding (§10.1); the gate reads 0 on the full body |
| canon | registry edits outside the bodies | In `registry.diff` (§4.3) |
| canon | the ITEM-18 placeholder | P-48; §9 X5.1 |
| registry | G06 masking | P-01 |
| registry | release label shape | P-16 |
| registry | required guards on unread bodies | All proved on the live bodies (§8) |
| registry | NAM-002 prototype circular | A live snapshot at EXECUTE (§4.4) |
| registry | rule codes | P-27 |
| registry | deduplications, FRAME fragments, A7-LOCAL coverage, ALL55 guards | Kept as built; each guard proved (§4, §8) |
| registry | MGMT-10 and R-A5 | P-04 |
| registry | PR-40 registry input follows the body | Two input changes mirror LPR-40-4 and LPR-40-5 (§4.3) |
| registry | not drafted outside the registry | P-29–P-33 |
| skills | ITEM-06 at change-flow `:295` | P-24 |
| skills | ITEM-08 override wording | One literal in change-flow and the relay, required twice by CONTRACT_REQUIRED; D24 reviews it |
| skills | validator_revision moves | P-22 |
| skills | ITEM-11 cases run only with the alias contract | The alias run is an explicit gate step (§5) |
| skills | reindex append rule | Unchanged; documented |
| skills | ITEM-15 residual limit | In `P33-A5NOTE` |
| skills | SELF_FORBIDDEN split literal | For D24 review; G18 proves it fires |
| skills | `/tmp` disclosure; D22 disclosure | No prompt body involved |
| skills | registry_deriver against 1.13.0 | Re-run against the final audit copy: drift [] (§4) |
| skills | seven edits beyond the census sites | P-23 |
| skills | governance audit `epic-reengineering-interoperability.md:55-56` | Follow-up (§10.2) |
| skills | ITEM-07 and ITEM-39 prose unguarded | As §A records |
| skills | relay/TW parity breaks | By design: TW is out of scope |
| skills | the ITEM-24 wording | P-32 |
| skills | governance-audit description in the sync manifest | Updated by the install |
| bodies | CL-40's PR claim | P-02 |
| bodies | CL-C-10's CLOSE route names the addenda as links | Kept: it names artifacts (§10.3) |
| bodies | DOC-10's RS-10 return-phase carry | Kept: `PR_RETURN_PHASE` is a routing value, the minimum context C-HANDOFF allows (§10.3) |
| bodies | DOC-20's R-A7-LOCAL regex | P-08 |
| bodies | PR-10, PR-20, PR-40 kept package bullets | §10.3 |
| bodies | PR-20's PR-40 DOWNSTREAM REJECT sentence | Follow-up (§10.2) |
| bodies | RS-20's "verified at entry" wording | Accepted: the sentence is fixed text naming the resuming phase's entry check |
| bodies | RS-40's `MERGE_OBSERVED` bullet names no link | Accepted: C-DISPATCH in the same body supplies the handoff |
| bodies | QA-* kept routing phrases | §10.3 |
| bodies | PR-10 CANDIDATE_AUTHORING_LEFTOVER (the one uncovered finding) | C-N3 |
| dry run | the PR-20 and PR-50 R-OWN anchors were swapped | P-40 |
| dry run | CF-x-20 serial comma | Adopted |
| dry run | QA-110's inserted sentence displaced "it" | P-15 (revised) |
| dry run | IA-10's optional intake edit; IA-20 and PR-40 intakes | P-37 |
| dry run | PR-40's RS-20 package carries the complete proposal | P-38 |
| dry run | LPR-30-2 unguarded | G-K55 |
| texts | P31 and P33 true only after the install | P-43 |
| texts | the parent record's §E repeats the C8 overstatement | P-54 |
| Notion | the AF-009 amendment | P-44 |
| Notion | the Checklist property *Authoritative Drive register* | P-45 |
| Notion | the tracking page's stale status lines | P-50 |

### 2.4 The second PLAN review (`wf_045af16b-3ed`)

Three reviewers (completeness, executability, consistency) returned NEEDS_REPAIR: 7 distinct required findings and 21
non-blocking ones. Each is repaired.

| finding | lens | disposition |
|---|---|---|
| The reindex and the registry gate need the patched glow-graph-contract, which existed only after X3.1 | all three (required) | Order changed: the skills are patched first (X1), then commit 1, then the repository changes (P-56; §9) |
| No full skills root or candidate root is built, and §5.3 used PLAN paths | executability (required) | X1.1 builds `$PKG` (freeze `323 047ca742…`); `EV/skills/run_gate.py` builds and checks the candidate root at `$GATE/cand` and runs every suite with EXECUTE paths (P-60) |
| §5.3 rows cannot reproduce after the reindex or the install | executability, consistency (required) | Three sets, `pre`, `pkg` and `post`, each with its own expected results (P-60) |
| execute.3's `git mv` and README source fail | executability (required) | `mkdir -p` first; the README comes from `EV/skills/contract-template-README.md` (X3.3) |
| The tracking-page entry is hard-dated | all three (required) | Opens `{{EXECUTE_DATE}}`, and is inserted before the paragraph that introduces the three decisions (P-65) |
| No part-level landing or rollback | completeness (required) | Two landing units; a rehearsal before any body write; a rollback journal and a `reverse` mode (P-57, P-58, P-59). *Superseded in round 4: one unit from X5.0, no journal, no `reverse` (P-57, P-58 revised again)* |
| W-4 required on only 6 of 21 A7 rows | completeness (required) | G-K24 on all 21 ITEM-29 rows (P-61) |
| The reindex-diff comparison fails on git headers | completeness (required), executability | The headers are stripped before `cmp` (X3.2) |
| §4.1 printed the base hash as `None` | executability, consistency | Fixed |
| `land.py` was never exercised; `{{` and deletion-only bodies | executability | `--no-ops` rehearsal run on every body at PLAN (§8); the token test counts only introduced tokens; NOTHING_TO_LAND (P-59) |
| The NAM-002 control run's expectation | executability | Stated: NAM-002 55, exit 1; the old registry comes from `git show` (§4.4) |
| A stale readback could trigger a wrong reversal | executability | `check` reports STALE_READBACK_OR_NOT_LANDED, which is never reversed (P-59) |
| X0.3(c) output argument; the page-ID source; no EXECUTING status | executability | X0.3(c) and X5.4 fixed; X0.4 added. *Superseded in round 4: the status change is in commit 1, X2.1 (P-81)* |
| G-K55 cited P-55, which did not exist; C-R9's step | executability, consistency | P-55 added; C-R9 now cites §P step 22 |
| The freeze window departs from §A order 4 | completeness, consistency | Recorded as an upstream finding (P-66; §10.1) |
| The tracking-page freeze and status writes were not drafted | completeness, consistency | Drafted as exact edits with tokens (P-65; §7.3) |
| "ten" pointer edits (there are eleven) | completeness, consistency | Corrected (P-46) |
| ITEM-22's lane parent IDs and titles have no live check | completeness | `nam002_live.py` checks them, with an injected wrong title (P-63) |
| ITEM-13 reads the R1 oracle from a skill | completeness | Recorded in ITEM-13's disposition (P-69) |
| PART-16 has no check against the graph | completeness | `EV/engine/graph_check.py` (P-64; X6.2) |
| No record that no skill states C-LAT's placement; the v5.0.0 pointer | completeness | §7.2 records the grep; MB-004 on the backlog (P-70) |
| Notion edits beyond §A's targets; HUB-03 said more than a pointer | completeness | Recorded in §10.1; HUB-03 reduced to a pointer (P-67) |
| G-K39 was removed from RS-40 | completeness | Restored (P-62) |
| Three `why` notes quoted more than 15 words | completeness | Trimmed |
| D25 pointed at §P, called authored text canonical, and credited P-02 to ruling 2 | consistency | Corrected (P-68) |
| `{{FREEZE_DIGESTS}}` had no fill rule | consistency | Defined (P-68) |
| The D18 successor under-named the renamed checks | consistency | Both named (P-68) |
| §P step 2 called PART-05 class A | consistency | Corrected in §P |

### 2.5 Found while integrating repair round 2 (repair round 3)

The integration of round 2's results was itself checked end to end: the manifest proof re-run in EXECUTE order, pass
3 on every body, and a re-read of §9 against the Notion and repository edits. It found these, and each is repaired.

| finding | how it was found | disposition |
|---|---|---|
| The freeze lift was tied to the close-out merge, and `TRACK-FREEZE-LIFT` claimed that merge although it lands before the close-out PR exists | re-reading X7 against the tracking edits | The freeze lifts after X7.4's post-install verification; the lift line states only the install, the verification and the lift (P-66 revised; X7.5) |
| `TRACK-STATUS-*` claimed `COMPLETE` before the record said so | the same | They land after the close commit, dated by it, with their readback in a second commit on the close-out PR (P-72; X7.6, X7.7) |
| `{{LIFT_DATE}}` and `{{CLOSE_DATE}}` had no fill rule, and `PART-18-AF009-01` dated itself by the D23-C commit rather than its write | a token census over every edit | One table of every token and its fill (P-71) |
| The registry was committed with the reindex, so reverting the body unit would also revert the reindex | re-reading P-57's rollback against X3 | The registry diff is committed alone at X3.1 (P-73) |
| The text label `commit: 2` covered two different commits (X3.5 and X5.2) | the same | Each text is labelled by the step that commits it (P-73) |
| The manifest's `when` fields and `GUARDS.md`'s NAM-002 section used the pre-round-2 step numbers, and the `pre` gate sat inside `execute.2` | a step-reference scan | Aligned to §9 X0–X7; `pre` runs once at X1.3 (manifest `suite_gate.pre`) |
| The rollback journal was deleted at the corpus gate, before the last gate that could call for a reversal | re-reading X7.4's failure path | Kept until X7.4 passes (P-58 revised). *Superseded in round 4: no journal (P-58 revised again)* |
| `P-68` dated `{{INSTALL_DATE}}` by X6.3, a step that no longer exists | the step-reference scan | X7.3 |
| The registry generators in `EV/registry/` depend on files in the PLAN scratchpad | a rebuild of `GUARDS.md` from `EV` | Recorded as PLAN-time generators; EXECUTE runs none of them (P-74) |
| The first manifest proof after round 2 read a stale manifest and proved nothing | reading its log | Re-run on the committed manifest, then again in exact §9 order (§8) |

### 2.6 The third PLAN review (`wf_b886670d-753`)

Three reviewers (completeness, executability, consistency) returned `NEEDS_REPAIR`: 16 required findings, several
shared between lenses, and 18 non-blocking ones. Each is repaired below. Step numbers in §2.1 to §2.6 are the numbers
of their time; §9 and §P hold the current ones, and §2.7 corrects four of these dispositions.

| finding | lens | disposition |
|---|---|---|
| `land.py check` never filled the page URL, so a correctly landed CL-40 read as not landed, for ever (X5.4, X6.1, X7.4 could never pass) | completeness, executability (required) | `check` fills the URL and refuses CL-40 without `--candidate-url` (P-75); `plan` now runs the readback itself on the text its operations produce (P-76), and pass 4 ran it on all 51 bodies (§8) |
| `land.py reverse` could not reverse a pure deletion | executability (required) | There is no reverse mode: no body copy is kept (P-58 revised again) |
| The rollback journal is a stored copy of body text read later to restore it, which `D22` forbids ("backups … without exception"; "never a source for later work") | all three (required) | No journal. The rehearsal proves every page's operations and readback before any write; a failed readback is repaired forward; a failure that cannot be stops the unit and returns to Nathan, who restores landed bodies from Notion's page history (P-58 revised again). This also supersedes §2.5's "kept until X7.4" row |
| The two landing units split parts (PART-17's validator edit in the skill unit, its guards in the body unit; PART-12's surfaces; PART-06's page, rule and pointers outside the reversal) | completeness, consistency (required) | Nothing leaves the branch before X5.0; a D24 rejection is a plan change; from X5.0 all 17 parts land as one unit, with every control-page edit and the page in the stop procedure (P-57 revised again; §9) |
| The body unit's failure paths left parts half-landed; the rehearsal and NAM-002 ran after Notion writes; §P step 21's rollback had no means | completeness, consistency (required) | NAM-002 runs at X3.6 and the rehearsal at X4.5, before any Notion write (P-77); the stop procedure lists every reversal (§9); §P rollbacks follow the unit rule |
| X7.4's failure path needed an unplanned revert PR and disagreed with §P | all three (required) | Forward only: reinstall the delivered file, or return to Nathan with the freeze held (P-82); §P step 25 matches |
| Session continuity: the journal, the `.skill` files and the gate directory lived in one session's scratchpad | completeness (required) | Any step can run in a new session; every input is rebuilt or re-read (P-78); the verdicts bind to freeze digests, which a re-cut reproduces |
| The gates held the whole skills root to a PLAN-time digest, so an unrelated skill sync or a D24 repair broke them | consistency (required), executability | The root digest is measured and compared within each run; only the seven package digests are asserted (P-79); a D24 repair is a plan change (P-57) |
| X0.4 committed the status before commit 1, so D25's "in its first execution commit" was false | consistency (required), completeness | The status change is in commit 1 (P-81); D25's closing sentence points to §E |
| Stale fill rules and step references in `why` fields, the manifest note, `land.py`'s docstring, `NOTES.md` and §P step 3 | consistency | Corrected, or marked superseded with the current rule named |
| §7.3 miscounted its insertions; §3.1 printed `{` for `{{`; §0 miscounted pass 2's files; §P step 2 named `$CAND` | completeness, consistency | Corrected |
| The pointers dated the move by their own write date | consistency | `{{MIGRATION_DATE}}` (P-80) |
| TRACK-STATUS claimed `COMPLETE` while `main` still shows `EXECUTING` | consistency | The lines name the close-out pull request |
| The Drive banner had two places and no record | completeness | Nathan banners it any time after X5.1; MGMT-10 reads it back before the close commit (X7.6) |
| D22 condition 5 was not carried into the close; no evidence directory was named; X7.2 was missing from §P | completeness | X7.6 discloses X7.4's harness files; `EX/` holds EXECUTE's evidence (P-83); §P step 25 includes delivery |
| X4.3 gave no command | executability | `execute.4b`, run and verified on `$PKG` (§8) |
| `notion-update-page` defaults to async | executability | `allow_async: false` everywhere (P-83) |
| `plan --journal` printed operations even when its precheck failed | executability | `plan` refuses `PRECHECK_FAILED` and `LANDED_CHECK_FAILED` (P-76) |
| The page's self-link spots had no exact text | executability | `M2.json` `self_links`: exact create-time text and step-7 operations, checked to reproduce M2-R4, R5 and R9 |
| The first push after a squash merge would be rejected | executability | `--force-with-lease` (P-83) |
| NAM-002's control run named `<record merge base>` | executability | `$BASE`, recorded at X0.2 |
| D25 stayed "ruled but not applied" for ever | completeness | Its closing sentence now points to the record's §E |

### 2.7 The fourth PLAN review (`wf_05b74ccf-d84`)

Three reviewers (completeness, executability, consistency), each followed by a verifier that tried to refute its
required findings, returned `NEEDS_REPAIR`: 11 distinct required findings (14 reports, 3 of them downgraded by the
verifiers and repaired anyway) and 20 non-blocking ones. Each is repaired below. Where a row here corrects a §2.6
disposition, this row governs.

| finding | lens | disposition |
|---|---|---|
| After a stop before X5.0 (a D24 rejection above all), "resumes at X1.1" could not run: the pre gate, a second D25 and the registry patch would all fail on the pushed branch | completeness, consistency (required) | §E records the stop on the branch, the status stays `EXECUTING`, the fix is a plan change merged to `main`, and EXECUTE starts again at X0.1, whose X0.2 drops the stopped commits (P-84) |
| The stop after X5.0 reversed `TRACK-FREEZE-START` while keeping the freeze, gave no reversal order, no trash operation and no item dispositions | all three (required) | The freeze line stays and `TRACK-UNIT-STOPPED` states the stop; reversals run in reverse order on the text as re-fetched; the trash call is exact; every item is `BLOCKED` (P-85) |
| `land.py` could not repair forward: a partly landed page gave `COUNT_MISMATCH` for ever or had an insertion added twice, which every gate passed | executability (required) | Each edit is stated `NOT_LANDED`, `LANDED` or `MIXED`; `plan` lands only what is missing; `check` fails a doubled insertion. Proved on synthetic text and by pass 5 on every body (P-88, §8.4) |
| D25's closing sentence named no event and no step wrote its date | all three (required) | D25 applies from the X7.1 merge; X7.6 writes `D25 applies from: <sha>, <date>` into §E, with a gate (P-86). Corrects §2.6's last row |
| Evidence stayed uncommitted until X6.4, the D24 verdicts had no path, and X5.1 could not resume after its create, so P-78 did not hold | completeness, consistency (required) | Each step commits its evidence; `EX/run.json` carries the values later steps need; the verdicts have paths and are committed as they return; X5.1 recognizes its own page (P-87, P-93, P-95). Corrects §2.6's session row |
| `PART-18-AF009-01` put code inside bold, which Notion reads back split, so its readback and reversal could not match | executability (required) | The bold closes before the code; a scan finds no other case (P-91) |
| `allow_async: false` can still return an `async_task`, never polled | executability (required) | Every write's task is polled to its end before the readback (P-89). Corrects §2.6's async row |
| The manifest's `rm -rf $PKG` forms need a person's approval in this environment | consistency (required) | `"${VAR:?}"` forms, which the check allows; the proof was run again (P-92) |
| An X7.4 failure could not reach the record | completeness (downgraded, repaired) | §E's X7.4 row, a record PR, status `EXECUTING` (P-94). Corrects §2.6's X7.4 row |
| Spec §1 lacked two supersession marks that `DECISIONS.md` carried | consistency (downgraded, repaired) | The spec is built after the copy, and the build asserts the two are equal; P-15 and P-66 are marked too |
| The Drive checks ran after the first Notion write | consistency (downgraded, repaired) | A read-only X4.6 runs them before X5.0 (P-95) |
| Control-page insertions keep their anchor, so a resumed step would insert twice | executability | Each edit is applied once: present new text means landed (P-90) |
| X4.5 named 51 pages from a 56-entry list; X5.4's 50 were implicit | executability, consistency | The five untouched bodies run `check`; X5.4 is the 51 less the proposed body (P-95) |
| X3.1 and X6.3 gave no command lines; `plan`'s output may exceed the tool limit; `check` always exited 0 | executability | Exact commands, both run at PLAN; the saved output file under `D22`; `check` exits 1 on failure (P-88, P-95) |
| X7.4's gates read the local branch, not `main` | consistency | X7.4 restarts the branch from `main` first (P-94) |
| The D24 brief's §1 bound the verdict to archive sha256s that a re-cut changes | executability | §1 names the freeze digests as the identity (P-93) |
| X4.3's comparison could not fail; the proof kept 6 lines per step | consistency | `diff` against `expected_after_patch.txt`; the full output is kept (P-92) |
| `check` and `graph_check.py` did not print the harness file; `dryrun` could prefer an older inline fetch; its root was fixed to one project directory | consistency, executability | Both print `source_file`; the newest capture wins; `--harness-root` (P-87, P-88) |
| F6 could not pass at step 6 | consistency | 8 pairs at step 6, 11 after step 7 (P-95) |
| Stale `why` fields and help strings (P29-D25, P29-D23C, the four `ITEM*-02`, M2-R1, `dryrun --skills`, §2.3's section number, §P's header) | consistency | Corrected |
| §P's not-in-scope line cited step 18; §11 counted a rejection at 1; P-83 omitted `EX/corpus-post/` | completeness, consistency | Step 19; 3 per rejection; listed (P-87, P-95) |

Running the repair found two cases its first draft stated wrongly; no reviewer raised them. A replacement whose new
text is part of the text it replaces (CL-30's `LCL-30-2`, PR-10's `R-ITEM38`) read `LANDED` on the unlanded page;
a static scan of every replacement found only these two, and the fix came before pass 5. QA-10's `R-OWN` read `MIXED`
on its landed page, because `LQA-10-P03` rewrites the sentence it is anchored after; pass 5 found it, and QA-10 was run
again on the fixed engine. Both fixes are in P-88.

### 2.8 The fifth PLAN review (`wf_ad66aa45-00a`)

Three reviewers (completeness, executability, consistency), each followed by a verifier that tried to refute its
required findings, returned `NEEDS_REPAIR`: 15 required reports (12 confirmed, 3 downgraded by the verifiers and
repaired anyway), which come to 10 distinct defects, and 27 non-blocking reports. Each is repaired below. Where a row
here corrects a §2.7 disposition, this row governs.

| finding | lens | disposition |
|---|---|---|
| `{{EXECUTE_DATE}}` was the date of each write and recorded nowhere, so a session resuming on a later day missed landed control-page edits: an insertion applied twice, or a correctly landed replacement stopped the unit. The same held for `{{MIGRATION_DATE}}` on an X5.1 resume and `{{INSTALL_DATE}}` at X7.4 | completeness#0, executability#0, consistency#2 (required); completeness#9, #10 | Every token value is recorded in `EX/run.json`, committed and pushed before the write that carries it; the apply-once test is `ctrl.py edits` with those values. `ctrl_proof.py` replays both sequences on the live pages and reproduces the round-5 miss (P-96, §8.7). Corrects §2.7's apply-once row |
| The stop's list of Notion writes came from `EX/` and the sitting's tool results, so a write made by an earlier session could be missing: Nathan's only basis for restoring bodies | completeness#1 (required) | The stop sweeps Notion itself: `land.py state` on the 51 bodies, `ctrl.py all` on the control pages, `ctrl.py children` on the Hub (P-98) |
| After a stop past X5.0 the record and its list stayed on an unmerged branch, `main` still passed X0.1, and the next X0.2 would reset the branch; the brief and verdicts were not preserved and the next round reused `cr1`; the PLAN session's branch was unnamed | completeness#2, #4, #5 (required); consistency#11, #12 | Every stop ends with a record PR from a branch reset to `main`, carrying `attempt-<n>/` (EX, briefs, verdicts, commit list) and §E's stop rows at `EXECUTING`; a reset guard refuses to reset over record work `main` lacks; X0.1 requires `PLANNED`; rounds are `cr<k>` by count and the brief is `REVIEWER-PROMPT-cr<k>.md` (P-84 revised, P-97, P-100) |
| The stop set every item and the status `BLOCKED` while landed bodies were still live, against template rule 6, and offered "a forward fix" with no vehicle | completeness#3, consistency#1 (required) | The status stays `EXECUTING`; Nathan restores; a restoration check verifies every body `UNTOUCHED`; then he ends the Modification (`BLOCKED`, now true) or rules a plan change; the stop's own lift line claims no install; "a forward fix" is withdrawn (P-99) |
| On an already landed deletion-only or replacement-only body, `plan` refused `NOTHING_TO_LAND` before `ALREADY_LANDED`, so a resumed landing would stop the unit | executability#1 (required) | `plan` refuses `ALREADY_LANDED` first whenever every live edit reads landed; pass 6 ran `plan` itself on all 51 landed texts: 51 `ALREADY_LANDED` (P-96, §8.5). Corrects §2.7's and §8.4's "a second plan refuses `ALREADY_LANDED`", which pass 5 computed rather than ran |
| A `--force-with-lease` push after the remote branch was deleted on merge is rejected as stale | executability#2 (downgraded, repaired) | Every lease push follows `git fetch --prune origin` (P-97) |
| X4.4 had to author the brief's §2 to §9, the gate commands in §8b above all | executability#3 (required), completeness#14 | The brief is drafted at PLAN; `packages_json.py` and `fill_brief.py` fill its six tokens mechanically; tested for all three round variants (P-100, §8.7) |
| A new session after the install would re-patch `$INST`'s already patched packages and report a false failure | executability#4 (required) | The rebuild applies only before X7.3 (P-101) |
| `TRACK-UNIT-STOPPED` claimed a `BLOCKED` record and a pushed §E before either existed | consistency#0 (downgraded, repaired) | It is applied after the record PR is pushed, and says only what is then true (P-98 step 7) |
| The verdicts were bound to freeze digests by reinterpreting the canonical §10, and X7.2 delivered re-cut archives no reviewer saw | consistency#3 (downgraded, repaired) | §10 is canonical; §1 lists both digests; the archives reviewed are delivered at X4.4 and never re-cut; a re-cut before the delivery gets its own round. Re-packaging a rebuilt tree changes the sha256 (measured; P-100) |
| No next action for an X7.4 stop; no tracking lines for a stop; D25's date unwritten on the X7.4 failure path; a re-run of X7.4 before its record PR merges erases it | completeness#6, #7, #8, #13, consistency#10 | The PO action is stated; the stop lines and the stop's lift line exist; P-94's record writes the D25 line; the reset guard makes X7.4 wait for the PR (P-97, P-99, P-102 (g), (h)) |
| A control-anchor drift would first be found after X5.0 | completeness#11 | X4.6 runs `ctrl.py all --expect unlanded` (P-102 (a)) |
| The Drive banner window overlapped the stop path | completeness#12, consistency#9 | The window opens when X6.4 passes (P-102 (e)) |
| Stale or incomplete statements: status wording, §4.4 vs X3.6, the manifest's `BASE`, "if the page exists", the X7.6 token gate's scope | completeness#15, consistency#6, executability#7 | Each corrected; the gate reads only the lines the close commit adds (P-98, P-102 (c), (i), (j)) |
| `check` skipped STALE on a page where no anchor matched | executability#5 | STALE is reported whenever an edit does not read landed (P-96) |
| X6.3's command lived only in a table cell with escaped pipes | executability#6 | `execute.6` in the manifest (P-102 (b)) |
| X0.3(c) named the wrong sha256 | executability#8 | Both values stated (P-102 (d)) |
| The engine could read another session's fetch | executability#9 | Only the running session's harness files; X5.4, X6.1 and X7.4 check `source_file` and `fetched` (P-101) |
| Evidence claims wider than what ran; the applier was not committed | executability#10, consistency#4, #5 | Worded as run (476 distinct partials; the proof's coverage and its 400-line cap); `apply_texts.py` committed and tested (P-102 (k), §8.4, §8.6) |
| Hashing, counting and child-list steps had no committed helper | executability#11 | `drive_check.py`, `ctrl.py all` and `ctrl.py children`, each run on today's pages (P-101, §8.7) |
| Three decisions lacked supersession marks; `NOTES.md`'s banner was stale; P-83/P-87 omitted `EX/graph_check.json` | consistency#7, #8, #13 | Marked; banner current; listed (P-102 (i), (l), (m)) |

## §3 Body edits

### 3.1 How they run

`closeout_rules.apply(pid, text)` applies, in this order: the shared RULES in table order, then the body's LOCAL
edits in their listed order (P-10). Every rule and edit asserts its expected count, and a mismatch is reported, never
forced. After the edits, each LOCAL-only CHECK must read 0 on its rows. `land.py plan` states each edit on the fetched
page, in the same order: `NOT_LANDED`, `LANDED` or `MIXED` (P-88). It plans only the `NOT_LANDED` edits, turns them
into `update_content` operations, and lists the `LANDED` ones as `repair` (`[]` on an unlanded page). It refuses, in
this order: a `MIXED` edit or a failing CHECK (`COUNT_MISMATCH`); a page where every edit reads landed
(`ALREADY_LANDED`, a landed deletion-only body included, P-96); a body with nothing to land (`NOTHING_TO_LAND`); a
`{{` token the edit introduces (P-48, P-59); and operations that do not reproduce the edit. On the text the operations
produce it runs the precheck and the readback itself (`check`, the STALE test included), and refuses unless both pass
(`PRECHECK_FAILED`, `LANDED_CHECK_FAILED`; P-76). `check` reports `STALE_READBACK_OR_NOT_LANDED` whenever an edit does
not read landed (P-96), fails on an insertion that occurs twice in a row (`doubled_insertions`), prints the harness
file it read (`source_file`) and exits 1 when it fails. `state` is read-only: it prints each edit's state and the
page's verdict (`UNTOUCHED`, `LANDED`, `PARTIAL`, or `NO_EDITS`) for the stop sweep and the restoration check (P-98,
P-99). Every mode reads only the running session's harness files (P-101). `--no-ops` prints
counts and both checks, never the operations (the rehearsal). For CL-40, whose rules carry the page-URL token, both
`plan` and `check` require `--candidate-url` and fill it first (P-75). There is no rollback journal and no reverse mode:
no copy of a body is kept (P-58 revised again, `D22`).

Bodies touched: 51 (50 live bodies and the proposed MGMT-10 body). Rules: 46. LOCAL edits: 66, in 26 bodies.
CHECKs: 7.

### 3.2 Texts

**Canonical texts** are read by `canon.py` from their repository homes: spec v2 §3 (`EXECUTION-SPEC-20260923-alpha-feedback-open-entries-v2.md`) and the D23 successor *PR-40 is entered once per merge*. They are never re-authored. Used here: W-4 (the PR-40 entry wording), ONCE, C-DISPATCH's predicate, Step 16's clause, C-LAT's *Decide it during work* block (deleted, compared to canonical before deletion), C-REPLAN's heading, and the two `merge_observed` conditions.

**Texts this Modification authors**, each written once in `closeout_rules.py`:

- `OWN`

```text
Every statement in this prompt that it is read-only or does not change the repository excludes its own output artifacts, which it writes, commits and pushes, and any pull request that carries them.
```
- `RECV`

```text
The branch, head and commits are verified at entry from the recorded vehicle and repository state; the handoff does not carry them.
```
- `A5_NEW`

```text
This prompt's artifacts are written only under `docs/ephemeral/` and `docs/graph/`
```
- `A5_MGMT`

```text
This prompt's artifacts are written only under `docs/ephemeral/` and `docs/graph/`, the controls it maintains only under `docs/prompt_ecosystem_management/`
```
- `A10_NEW`

```text
Reviewers remain read-only toward the work they review
```
- `P1_NEW`

```text
Then give the other fields the handoff rule above names; sections the artifact already holds are named, not repeated.
```
- `P4_NEW`

```text
Catalogs carry the verified direct Notion links, repository paths and exact selected prompt versions required by this release; a runtime handoff names its destination and input artifacts by those links, versions and paths, and the artifacts hold their lineage.
```
- `TASK_NEW`

```text
Populate the exact immediate destination or actual owner, the receiving role and session, and each input artifact by repository path; the artifacts hold the rest.
```
- `CLOSE_NEW`

```text
Name the positive closure decision and every post-closure result artifact by repository path; those artifacts hold the unresolved observations and manual-action dispositions.
```
- `A2E_NEW`

```text
Keep exact register lineage, publication evidence and unresolved facts in the output artifact, which each next or recovery handoff names
```
- `ITEM21_NEW`

```text
PR-40's entry, on `MERGE_OBSERVED` or, only where no `MERGE_OBSERVED` result was returned for this merge, on Nathan's merge assertion, is defined in *Product Owner merge action, PR phase ownership, and abort boundary*; that entry creates no runtime approval
```
- `ITEM31_NEW`

```text
A precise in-scope defect in landed work returns `REJECT` and re-plans through `PR-20`, as **PRECISE IN-SCOPE DEFECT → re-plan** states.
```
- `ITEM18_NEW`

```text
The Candidate CRD Items List is the Notion page `Candidate CRD Items List` (`{{CANDIDATE_CRD_LIST_URL}}`), which a destination rule names; it is the list's only store, and this prompt writes to it only as this section directs. 
```
- `ITEM19_NEW`

```text
 Name the board by the board reference the change context supplies; when none is supplied, record the board update as pending, owned under PF04 §9.1.1 by the authorized manual operator and the actual receiving owners.
```
- `ITEM34_NEW`

```text
 This applies only before the whole approved run is complete: a completed failing run is `ACCEPT` and continues to QA-120.
```
- `ITEM35_NEW`

```text
, routed as *Required result and routing* states
```
- `ITEM30D1_NEW`

```text
 and only where no `MERGE_OBSERVED` result was returned for this merge; for `MERGE_OBSERVED`, it is the same selected PR-40
```
- `ITEM30D2_NEW`

```text
The conditional `PR-40` block states only its manual prerequisite: it is usable only after Nathan manually merges the identified PR and only where no `MERGE_OBSERVED` result was returned for this merge; `PR-40`'s own body holds the verification rules.
```

### 3.3 Shared rules

For each rule: its item and part, action, anchor, new text, and the bodies with their expected hit counts. Per-body anchors or texts are shown as `pid:`.

#### R-A1a — ITEM-27 (A1), PART-13

- action: `replace`
- bodies: CL-20 1, CL-30 1, CL-E-20 1, CL-E-30 1, CL-E-40 1, DOC-10 1, DOC-20 1, ESC-10 1, ESC-25 1, ESC-30 1, ESC-40 1, OPS-10 1, OPS-20 1, PR-30 1, PR-40 1, QA-100 1, QA-110 1, QA-120 1, QA-20 1, QA-50 1, QA-60 1, QA-70 1, QA-80 1, QA-90 1, RS-10 1, RS-20 1, RS-30 1
- anchor:

```regex
\bin permitted metadata or (?:the )?handoff\b
```
- new text:

```text
in the output artifact's permitted metadata
```

#### R-A1b — ITEM-27 (A1), PART-13

- action: `replace`
- bodies: CL-C-10 1, CL-E-10 1, OPS-30 1, PR-10 1, PR-20 1, QA-10 1
- anchor:

```regex
\bin (?:the )?existing permitted metadata or (?:the )?handoff\b
```
- new text:

```text
in the output artifact's existing permitted metadata
```

#### R-A1c — ITEM-27 (A1), PART-13

- action: `delete`
- bodies: CL-C-10 1, CL-E-10 1, CL-E-20 1, CL-E-30 1, CL-E-40 1, DOC-10 1, DOC-20 1, ESC-10 1, ESC-25 1, ESC-30 1, ESC-40 1, OPS-10 1, OPS-20 1, OPS-30 1, PR-10 1, PR-20 1, PR-30 1, PR-40 1, QA-10 1, QA-100 1, QA-110 1, QA-120 1, QA-20 1, QA-50 1, QA-60 1, QA-70 1, QA-80 1, QA-90 1, RS-10 1, RS-20 1, RS-30 1
- anchor:

```regex
(?:(?<=lineage metadata)|(?<=artifact lineage)) or (?:the )?(?:returned )?handoff(?=[:.,;])
```

#### R-A1d — ITEM-27 (A1) / ITEM-26, PART-13

- action: `replace`
- bodies: CL-C-10 1, CL-E-10 1, OPS-10 1, OPS-30 1, PR-10 1, PR-20 1, QA-10 1
- anchor:

```regex
(?<=exist, )in (?:the )?returned handoff\b
```
- new text:

```text
in the output artifact's lineage metadata
```

#### R-A1e — ITEM-27 (A1), PART-13

- action: `delete`
- bodies: CL-20 1, CL-30 1, CL-C-10 1, CL-E-10 1, OPS-30 1, PR-10 1, PR-20 1, PR-30 1, PR-40 1, QA-10 1
- anchor:

```regex
(?<=artifact metadata) or handoff(?=\.)
```

#### R-A1f — ITEM-27 (A1), PART-13

- action: `replace`
- bodies: PR-35 1
- anchor:

```regex
permitted artifact/handoff metadata
```
- new text:

```text
permitted artifact metadata
```

#### R-A2a — ITEM-27 (A2), PART-13

- action: `replace`
- bodies: DOC-10 1, DOC-20 1, ESC-10 1, ESC-25 1, ESC-30 1, ESC-40 1, QA-100 1, QA-110 1, QA-120 1, QA-20 1, QA-50 1, QA-60 1, QA-70 1, QA-80 1, QA-90 1, RS-10 1, RS-20 1, RS-30 1
- anchor:

```regex
(?<=in the existing substantive artifact) and handoff\b
```
- new text:

```text
, which the handoff names
```

#### R-A2b — ITEM-27 (A2), PART-13

- action: `replace`
- bodies: CL-C-10 1, CL-E-10 1, OPS-30 1, PR-10 1, PR-20 1, PR-30 1, PR-40 1, QA-10 1
- anchor:

```regex
(?<=substantive artifact metadata/content) and handoffs\b
```
- new text:

```text
, which the handoff names
```

#### R-A2c — ITEM-27 (A2), PART-13

- action: `replace`
- bodies: OPS-10 1
- anchor:

```regex
task, receipt, review and handoff metadata
```
- new text:

```text
task, receipt and review metadata, which the handoff names
```

#### R-A2d — ITEM-27 (A2), PART-13

- action: `replace`
- bodies: OPS-20 1
- anchor:

```regex
task, execution result, receipt and handoff when applicable
```
- new text:

```text
task, execution result and receipt, which the handoff names, when applicable
```

#### R-A2e — ITEM-27 (A2) / ITEM-26, PART-13

- action: `replace`
- bodies: CL-C-10 1, CL-E-10 1, OPS-10 1, OPS-30 1, PR-10 1, PR-20 1, PR-30 1, PR-40 1, QA-10 1
- anchor:

```regex
Carry exact register lineage, publication evidence and unresolved facts through (?:all next/recovery packages|every next and recovery package)
```
- new text:

```text
Keep exact register lineage, publication evidence and unresolved facts in the output artifact, which each next or recovery handoff names
```

#### R-A2f1 — ITEM-27 (A2), PART-13

- action: `replace`
- bodies: PR-40 1
- anchor:

```regex
review result and every native return without deciding Canon
```
- new text:

```text
review result without deciding Canon; every native return names those artifacts
```

#### R-A2f2 — ITEM-27 (A2), PART-13

- action: `replace`
- bodies: QA-10 1
- anchor:

```regex
, `QA_READINESS` and every return package
```
- new text:

```text
 and `QA_READINESS`; every return package names those artifacts
```

#### R-A2g — ITEM-27 (A2), PART-13

- action: `delete`
- bodies: IA-10 1, IA-20 1, IA-30 1, OPS-10 4, OPS-20 4, OPS-30 5, PR-10 4, PR-20 4, PR-40 6, QA-10 6
- anchor (every body):

```regex
; `?CANON_CONFLICT_REGISTER`?(?=;)|`?CANON_CONFLICT_REGISTER`? and approved/rejected (?:history|dispositions); |, `?CANON_CONFLICT_REGISTER`?(?= and )|; (?:and )?`?CANON_CONFLICT_REGISTER`?(?=\.)|(?<=, )conflict register, 
```
- anchor (IA-30):

```regex
(?<=dependency state, )conflict register, 
```

#### R-26-P1 — ITEM-26, PART-13

- action: `replace`
- bodies: OPS-10 1, OPS-20 1, OPS-30 1, PR-10 1, PR-20 1, PR-30 1, PR-40 1, QA-10 1
- anchor:

```regex
Then identify the required receiving role/session[^\n]*?expected output/state\.(?: Carry complete native inputs[^\n]*?filename\.)?
```
- new text:

```text
Then give the other fields the handoff rule above names; sections the artifact already holds are named, not repeated.
```

#### R-26-P1b — ITEM-26, PART-13

- action: `delete`
- bodies: IA-30 1, UTIL-10 1
- anchor:

```regex
,? naming [^.\n]*\bunresolved items/owners, next action, and expected (?:output|review state)(?=\.)
```

#### R-26-P3 — ITEM-26, PART-13

- action: `replace`
- bodies: CL-20 1, CL-30 1, CL-40 1, CL-C-10 1, CL-E-10 1
- anchor:

```regex
(?<=PF10/addendum lineage )into its result and handoff\b
```
- new text:

```text
into its result artifact, which the handoff names
```

#### R-26-P4 — ITEM-26, PART-13

- action: `replace`
- bodies: CL-C-10 1, CL-E-10 1, PR-40 1, QA-10 1, PR-10 1, PR-20 1, PR-30 1, OPS-30 1, OPS-10 0, OPS-20 0
- anchor:

```regex
Catalogs and runtime handoffs carry the verified direct Notion links[^.\n]*\.
```
- new text:

```text
Catalogs carry the verified direct Notion links, repository paths and exact selected prompt versions required by this release; a runtime handoff names its destination and input artifacts by those links, versions and paths, and the artifacts hold their lineage.
```

#### R-26-TASK — ITEM-26, PART-13

- action: `replace`
- bodies: OPS-30 1, QA-10 1
- anchor:

```regex
Populate the exact immediate destination or actual owner, actor/session continuity, native inputs,[^.\n]*required action\.
```
- new text:

```text
Populate the exact immediate destination or actual owner, the receiving role and session, and each input artifact by repository path; the artifacts hold the rest.
```

#### R-26-CLOSE — ITEM-26, PART-13

- action: `replace`
- bodies: CL-20 1, CL-30 1
- anchor:

```regex
Carry the positive closure decision, complete post-closure results, unresolved observations[^.\n]*\.
```
- new text:

```text
Name the positive closure decision and every post-closure result artifact by repository path; those artifacts hold the unresolved observations and manual-action dispositions.
```

#### R-A7-S1a — ITEM-29, PART-14

- action: `replace`
- bodies: OPS-30 1, PR-10 1, PR-20 1, PR-30 1, PR-40 1, QA-10 1
- anchor:

```regex
(?<=usable only after Nathan later manually merges the identified PR)(?=\.)
```
- new text:

```text
 and only where no `MERGE_OBSERVED` result was returned for this merge
```

#### R-A7-S1b — ITEM-29, PART-14

- action: `replace`
- bodies: OPS-30 1, PR-10 1, PR-20 1, PR-30 1, PR-40 1, QA-10 1
- anchor:

```regex
; Nathan's later invocation asserts a merge occurred; (?=PR-40 independently verifies)
```
- new text:

```text
. PR-40 is entered on the observed merge event for the identified PR, delivered to the subscribed PR-35 session as MERGE_OBSERVED, or, only where no MERGE_OBSERVED result was returned for this merge, on Nathan's assertion that he manually merged it. PR-40 is entered once per merge: paste the `MERGE_OBSERVED` handoff when one arrives, otherwise the fallback block. Once either has been pasted, the other is void. 
```

#### R-A7-S2 — ITEM-29, PART-14

- action: `replace`
- bodies: OPS-30 1, PR-10 1, PR-20 1, PR-30 1, PR-40 1, QA-10 1
- anchor:

```regex
Nathan's (?:later PR-40 invocation asserts that a manual merge occurred; |PR-40 invocation asserts the manual-merge event, while )(?=PR-40 independently verifies)
```
- new text:

```text
PR-40 is entered on the observed merge event for the identified PR, delivered to the subscribed PR-35 session as MERGE_OBSERVED, or, only where no MERGE_OBSERVED result was returned for this merge, on Nathan's assertion that he manually merged it. 
```

#### R-A7-CL — ITEM-29, PART-14

- action: `replace`
- bodies: CL-20 1, CL-30 1, CL-40 1, CL-C-10 1, CL-E-10 1
- anchor:

```regex
Nathan's later manual PR-40 invocation asserts only that he manually merged the identified PR; 
```
- new text:

```text
PR-40 is entered on the observed merge event for the identified PR, delivered to the subscribed PR-35 session as MERGE_OBSERVED, or, only where no MERGE_OBSERVED result was returned for this merge, on Nathan's assertion that he manually merged it. PR-40 is entered once per merge: paste the `MERGE_OBSERVED` handoff when one arrives, otherwise the fallback block. Once either has been pasted, the other is void. 
```

#### R-A7-S3 — ITEM-29, PART-14

- action: `replace`
- bodies: CL-E-20 1, CL-E-30 1, CL-E-40 1, DOC-10 1, DOC-20 1, ESC-10 1, ESC-25 1, ESC-30 1, ESC-40 1, QA-20 1
- anchor:

```regex
PR-40 independently verifies the later asserted merge and landed lineage\.
```
- new text:

```text
PR-40 is entered on the observed merge event for the identified PR, delivered to the subscribed PR-35 session as MERGE_OBSERVED, or, only where no MERGE_OBSERVED result was returned for this merge, on Nathan's assertion that he manually merged it. PR-40 is entered once per merge: paste the `MERGE_OBSERVED` handoff when one arrives, otherwise the fallback block. Once either has been pasted, the other is void. PR-40 independently verifies the merged state and landed lineage.
```

#### R-ITEM21 — ITEM-21, PART-14

- action: `replace`
- bodies: CL-20 1, CL-30 1, CL-C-10 1, CL-E-10 1
- anchor:

```regex
(?:The (?:specific )?)?Product Owner PR-40 merge-approval effect is defined above
```
- new text:

```text
PR-40's entry, on `MERGE_OBSERVED` or, only where no `MERGE_OBSERVED` result was returned for this merge, on Nathan's merge assertion, is defined in *Product Owner merge action, PR phase ownership, and abort boundary*; that entry creates no runtime approval
```

#### R-ITEM30a — ITEM-30, PART-14

- action: `insert_after`
- bodies: PR-35 1
- anchor:

```regex
(?m)^- `MERGE_PENDING`: every readiness predicate above passes\.$
```
- new text:

```text

- `MERGE_OBSERVED`: the subscribed PR-35 session observes the merge of the identified PR, performed by Nathan.
```

#### R-ITEM30b — ITEM-30, PART-14

- action: `insert_after`
- bodies: RS-40 1
- anchor:

```regex
(?m)^- `MERGE_PENDING`[^\n]*$
```
- new text:

```text

- `MERGE_OBSERVED`: resumed PR-35 phase; the subscribed PR-35 session observes the merge of the identified PR, performed by Nathan.
```

#### R-ITEM30c — ITEM-30, PART-14

- action: `replace`
- bodies: PR-35 1
- anchor:

```regex
\bsixth top-level PR-35 result\b
```
- new text:

```text
seventh top-level PR-35 result
```

#### R-ITEM30d1 — ITEM-30, PART-14

- action: `replace`
- bodies: PR-35 1
- anchor:

```regex
(?<=conditionally usable only after Nathan's manual merge)(?=\.)
```
- new text:

```text
 and only where no `MERGE_OBSERVED` result was returned for this merge; for `MERGE_OBSERVED`, it is the same selected PR-40
```

#### R-ITEM30d2 — ITEM-30, PART-14

- action: `replace`
- bodies: PR-35 1
- anchor:

```regex
The PR-40 handoff must say: [^\n]*?agent merge\.
```
- new text:

```text
The conditional `PR-40` block states only its manual prerequisite: it is usable only after Nathan manually merges the identified PR and only where no `MERGE_OBSERVED` result was returned for this merge; `PR-40`'s own body holds the verification rules.
```

#### R-26-RSP — ITEM-26 (P-38), PART-13

- action: `replace`
- bodies: PR-40 1
- anchor:

```regex
RESCOPE_PROPOSAL_ID and complete RESCOPE_PROPOSAL\b
```
- new text:

```text
RESCOPE_PROPOSAL_ID, naming the RESCOPE_PROPOSAL by repository path
```

#### R-ITEM31 — ITEM-31, PART-14

- action: `replace`
- bodies: PR-40 1
- anchor:

```regex
An ordinary in-scope defect remains with the existing PR owner\.
```
- new text:

```text
A precise in-scope defect in landed work returns `REJECT` and re-plans through `PR-20`, as **PRECISE IN-SCOPE DEFECT → re-plan** states.
```

#### R-OWN — ITEM-32 (A6) / ITEM-17, PART-05

- action: `insert_after`
- bodies: PR-40 1, CL-E-20 1, DOC-20 1, QA-10 1, PR-50 1, ESC-25 1, PR-20 1, GCFPE-MGMT-10 1, CL-20 1, CL-30 1, CL-40 1
- anchor (PR-40):

```regex
(?<=operating read-only\.)
```
- anchor (CL-E-20):

```regex
(?<=revalidation session, read-only\.)
```
- anchor (DOC-20):

```regex
(?<=do not edit documentation, Canon, PF10, or repository state\.)
```
- anchor (QA-10):

```regex
(?:(?<=This is a read-only audit and readiness role\.)|(?<=This is an audit and readiness role\.))
```
- anchor (PR-50):

```regex
otherwise mutating the workspace, worktree, branch, open PR, commits or evidence[^.\n]*\.
```
- anchor (ESC-25):

```regex
read-only repository reviewer[^.\n]*\.
```
- anchor (PR-20):

```regex
(?<=Do not mutate the repository in this authoring operation\.)
```
- anchor (GCFPE-MGMT-10):

```regex
does not execute product Change Flow, implementation, repository work[^.\n]*\.
```
- anchor (CL-20):

```regex
Use only the read-only tools, stores, repository access[^.\n]*\.
```
- anchor (CL-30):

```regex
Use only the read-only tools, stores, repository access[^.\n]*\.
```
- anchor (CL-40):

```regex
It does not edit Canonical PF09, PF10, Canon, a board, registry, repository[^.\n]*\.
```
- new text:

```text
 Every statement in this prompt that it is read-only or does not change the repository excludes its own output artifacts, which it writes, commits and pushes, and any pull request that carries them.
```

#### R-A10 — ITEM-32 (A10), PART-05

- action: `replace`
- bodies: OPS-10 1, OPS-30 1, PR-40 1, QA-10 1
- anchor:

```regex
Reviewers remain read-only(?! toward the work they review)
```
- new text:

```text
Reviewers remain read-only toward the work they review
```

#### R-A5 — ITEM-32 (A5), PART-05

- action: `replace`
- bodies: GCFPE-MGMT-10 1, PR-35 1
- anchor:

```regex
Repository paths outside `docs/ephemeral/` and `docs/graph/` are not written
```
- new text (every body):

```text
This prompt's artifacts are written only under `docs/ephemeral/` and `docs/graph/`
```
- new text (GCFPE-MGMT-10):

```text
This prompt's artifacts are written only under `docs/ephemeral/` and `docs/graph/`, the controls it maintains only under `docs/prompt_ecosystem_management/`
```

#### R-A3a — ITEM-33 (A3a), PART-15

- action: `delete`
- bodies: CL-20 1, CL-30 1, CL-C-10 1, CL-E-10 1, OPS-30 1, PR-10 1, PR-20 1, PR-30 1, PR-40 1, QA-10 1
- anchor:

```regex
Embed only applicable workflow contracts: [^.\n]*\. ?
```

#### R-A4a — ITEM-33 (A4a), PART-15

- action: `delete`
- bodies: CL-20 1, CL-30 1, CL-40 1, CL-C-10 1, CL-E-10 1
- anchor:

```regex
 These candidate URL tokens must be replaced by observed direct Notion URLs[^.\n]*\.
```

#### R-A4c — ITEM-33 (A4c) / ITEM-18, PART-15

- action: `delete`
- bodies: CL-40 1
- anchor:

```regex
 This authoring candidate does not perform that update\.
```

#### R-CLAT — ITEM-37, PART-18

- action: `delete`
- bodies: PR-10 1, PR-20 1, PR-40 1, RS-10 1, RS-20 1, DOC-10 1, DOC-20 1, IA-30 1
- anchor:

```regex
(?m)^\*\*Decide it during work:\*\*\n1\. [^\n]*\n2\. [^\n]*\n3\. [^\n]*\n?
```

#### R-ITEM18 — ITEM-18, PART-06

- action: `replace`
- bodies: CL-40 1
- anchor:

```regex
(?=The existing noncanonical Candidate CRD Items List may be updated in place)
```
- new text:

```text
The Candidate CRD Items List is the Notion page `Candidate CRD Items List` (`{{CANDIDATE_CRD_LIST_URL}}`), which a destination rule names; it is the list's only store, and this prompt writes to it only as this section directs. 
```

#### R-ITEM19 — ITEM-19, PART-07

- action: `insert_after`
- bodies: CL-20 1
- anchor:

```regex
(?m)^4\. Include Master Scrum's precise board-update instruction[^.\n]*\.
```
- new text:

```text
 Name the board by the board reference the change context supplies; when none is supplied, record the board update as pending, owned under PF04 §9.1.1 by the authorized manual operator and the actual receiving owners.
```

#### R-ITEM34 — ITEM-34, PART-16

- action: `replace`
- bodies: QA-110 1
- anchor:

```regex
(?<=code/Ops remediation\. Do not fix it here\.)
```
- new text:

```text
 This applies only before the whole approved run is complete: a completed failing run is `ACCEPT` and continues to QA-120.
```

#### R-ITEM35 — ITEM-35, PART-16

- action: `replace`
- bodies: QA-80 1
- anchor:

```regex
(?<=`WRONG_ROUTE_APPROVED_BASE`) terminally\b
```
- new text:

```text
, routed as *Required result and routing* states
```

#### R-ITEM38 — ITEM-38, PART-15

- action: `replace`
- bodies: PR-10 1
- anchor:

```regex
material change \(D23-C\) change\b
```
- new text:

```text
material change (D23-C)
```

#### R-ITEM23 — ITEM-23, PART-11

- action: `delete`
- bodies: GCFPE-MGMT-10-PROPOSED 2
- anchor:

```regex
(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?(?:Prompt [Vv]ersion|Ecosystem release|Set)(?:\*\*|__|`){0,2}[ \t]*:[^\n]*\n?
```

### 3.4 LOCAL edits

Each LOCAL anchor is a literal of at most 15 words. The span is `anchor` (the literal only), `eol` (to the end of its line), `eos` (to the end of its sentence) or `through` (to the named closing words, on the same line). Every new text is authored and is accepted with the plan as written (P-20).

#### CF-C-10

- **LCF-C-10-1** — ITEM-26 (R-26-FRAME, self-recovery package); section *Required result and routing*; action `replace`; span `anchor`

```text
carries the original CLASS_SELECTION_REF, source references, exact omission, preserved analysis, and correction required
```

  becomes

```text
names CLASS_SELECTION_REF, SOURCE_REF and the BLOCKED kickoff artifact by repository path; the artifacts hold the rest
```

- **LCF-C-10-2** — ITEM-26 (R-26-FRAME, CF-PO-10 unresolved-class package); section *Required result and routing*; action `replace`; span `anchor`

```text
with the preserved source/change facts; CF-PO-10 requests
```

  becomes

```text
naming SOURCE_REF and the BLOCKED kickoff artifact by repository path; the artifacts hold the rest. CF-PO-10 requests
```

#### CF-C-20

- **LCF-C-20-1** — ITEM-26 (R-26-FRAME, direct package to CF-C-30), 1 of 2; section *Required result and routing*; action `replace`; span `anchor`

```text
The direct package contains the exact pending Specification, class/change lineage, relevant kickoff decision/evidence,
```

  becomes

```text
The direct package names, by repository path, the exact pending Specification, the kickoff,
```

- **LCF-C-20-2** — ITEM-26 (R-26-FRAME, direct package to CF-C-30), 2 of 2; section *Required result and routing*; action `insert_after`; span `anchor`

```text
current sources only when they actually exist and the review requires them
```

  becomes

```text
; the artifacts hold the rest
```

- **LCF-C-20-3** — ITEM-26 (R-26-FRAME, recovery to CF-C-10); section *Required result and routing*; action `replace`; span `anchor`

```text
carries the original kickoff link, exact defect, class/change lineage, and all recoverable source/selection evidence
```

  becomes

```text
names the original kickoff and all recoverable source/selection evidence by repository path, with the exact defect as minimum context only where no named artifact records it; the artifacts hold the rest
```

#### CF-C-30

- **LCF-C-30-1** — ITEM-26/27 (R-26-FRAME, package to IA-10), 1 of 3; section *Required result and routing*; action `replace`; span `anchor`

```text
The complete package carries the exact approved Specification
```

  becomes

```text
The complete package names the exact approved Specification
```

- **LCF-C-30-2** — ITEM-26/27 (R-26-FRAME, package to IA-10), 2 of 3; section *Required result and routing*; action `replace`; span `anchor`

```text
path, class/change and approval lineage, the carried conflict register, actual existing source/repository/access facts, and the
```

  becomes

```text
path, and the
```

- **LCF-C-30-3** — ITEM-26/27 (R-26-FRAME, package to IA-10), 3 of 3; section *Required result and routing*; action `insert_after`; span `anchor`

```text
required IA/session binding or its truthful unassigned state
```

  becomes

```text
; the artifacts hold the rest
```

#### CF-C-40

- **LCF-C-40-1** — ITEM-26 (R-26-FRAME, direct package to CF-C-30), 1 of 3; section *Required result and routing*; action `replace`; span `anchor`

```text
The direct package contains the exact produced artifact and application record
```

  becomes

```text
The direct package states the actual mode and names, by repository path, the exact produced artifact and application record
```

- **LCF-C-40-2** — ITEM-26 (R-26-FRAME, direct package to CF-C-30), 2 of 3; section *Required result and routing*; action `replace`; span `anchor`

```text
actual mode, class/change/base lineage, and current
```

  becomes

```text
and current
```

- **LCF-C-40-3** — ITEM-26 (R-26-FRAME, direct package to CF-C-30), 3 of 3; section *Required result and routing*; action `insert_after`; span `anchor`

```text
PF10/overlay links only when the branch requires them
```

  becomes

```text
; the artifacts hold the rest
```

#### CF-E-10

- **LCF-E-10-1** — ITEM-26 (R-26-FRAME, self-recovery package); section *Required result and routing*; action `replace`; span `anchor`

```text
carries the original CLASS_SELECTION_REF, source references, exact omission, preserved analysis, and correction required
```

  becomes

```text
names CLASS_SELECTION_REF, SOURCE_REF and the BLOCKED kickoff artifact by repository path; the artifacts hold the rest
```

- **LCF-E-10-2** — ITEM-26 (R-26-FRAME, CF-PO-10 unresolved-class package); section *Required result and routing*; action `replace`; span `anchor`

```text
with the preserved source/change facts; CF-PO-10 requests
```

  becomes

```text
naming SOURCE_REF and the BLOCKED kickoff artifact by repository path; the artifacts hold the rest. CF-PO-10 requests
```

#### CF-E-20

- **LCF-E-20-1** — ITEM-26 (R-26-FRAME, direct package to CF-E-30), 1 of 2; section *Required result and routing*; action `replace`; span `anchor`

```text
The direct package contains the exact pending Specification, class/change lineage, relevant kickoff decision/evidence,
```

  becomes

```text
The direct package names, by repository path, the exact pending Specification, the kickoff,
```

- **LCF-E-20-2** — ITEM-26 (R-26-FRAME, direct package to CF-E-30), 2 of 2; section *Required result and routing*; action `insert_after`; span `anchor`

```text
current sources only when they actually exist and the review requires them
```

  becomes

```text
; the artifacts hold the rest
```

- **LCF-E-20-3** — ITEM-26 (R-26-FRAME, recovery to CF-E-10); section *Required result and routing*; action `replace`; span `anchor`

```text
carries the original kickoff link, exact defect, class/change lineage, and all recoverable source/selection evidence
```

  becomes

```text
names the original kickoff and all recoverable source/selection evidence by repository path, with the exact defect as minimum context only where no named artifact records it; the artifacts hold the rest
```

#### CF-E-30

- **LCF-E-30-1** — ITEM-26/27 (R-26-FRAME, package to IA-10), 1 of 3; section *Required result and routing*; action `replace`; span `anchor`

```text
The complete package carries the exact approved Specification
```

  becomes

```text
The complete package names the exact approved Specification
```

- **LCF-E-30-2** — ITEM-26/27 (R-26-FRAME, package to IA-10), 2 of 3; section *Required result and routing*; action `replace`; span `anchor`

```text
path, class/change and approval lineage, the carried conflict register, actual existing source/repository/access facts, and the
```

  becomes

```text
path, and the
```

- **LCF-E-30-3** — ITEM-26/27 (R-26-FRAME, package to IA-10), 3 of 3; section *Required result and routing*; action `insert_after`; span `anchor`

```text
required IA/session binding or its truthful unassigned state
```

  becomes

```text
; the artifacts hold the rest
```

#### CF-E-40

- **LCF-E-40-1** — ITEM-26 (R-26-FRAME, direct package to CF-E-30), 1 of 3; section *Required result and routing*; action `replace`; span `anchor`

```text
The direct package contains the exact produced artifact and application record
```

  becomes

```text
The direct package states the actual mode and names, by repository path, the exact produced artifact and application record
```

- **LCF-E-40-2** — ITEM-26 (R-26-FRAME, direct package to CF-E-30), 2 of 3; section *Required result and routing*; action `replace`; span `anchor`

```text
actual mode, class/change/base lineage, and current
```

  becomes

```text
and current
```

- **LCF-E-40-3** — ITEM-26 (R-26-FRAME, direct package to CF-E-30), 3 of 3; section *Required result and routing*; action `insert_after`; span `anchor`

```text
PF10/overlay links only when the branch requires them
```

  becomes

```text
; the artifacts hold the rest
```

#### CL-20

- **LCL-20-1** — ITEM-26 (R-26-FRAME site: CL-30 route); section *Next step and recovery*; action `replace`; span `eos`

```text
carrying the exact qualified condition, lineage, evidence, owner, gates
```

  becomes

```text
naming the positive closure decision and the `POST_CLOSURE_RECORD`, which records the exact qualified condition, by repository path; the artifacts hold the rest.
```

#### CL-30

- **LCL-30-1** — ITEM-26 (R-26-FRAME site; also the census A2 borderline 'existing ADR/conflict history' carriage); section *Next step and recovery*; action `replace`; span `eos`

```text
Carry the complete candidate, positive closure and architecture-decision lineage
```

  becomes

```text
Name the complete `ADR_CANDIDATE` and the positive closure decision by repository path; the artifacts hold the rest.
```

- **LCL-30-2** — ITEM-27 (A2, DECISIONS P-18: second census A2 carrier); section *Direct native branch packages / Complete ADR candidate*; action `replace`; span `anchor`

```text
; existing ADR/conflict history;
```

  becomes

```text
;
```

#### CL-C-10

- **LCL-C-10-1** — ITEM-26 (R-26-FRAME site: CL-20 route); section *Next step and recovery*; action `replace`; span `eos`

```text
Carry exact CRD Specification, Implementation Plan/review, final accepted PR/Ops/documentation
```

  becomes

```text
Name the `CHANGE_CLOSURE_DECISION` and each already-produced addendum by repository path; the artifacts hold the rest.
```

- **LCL-C-10-2** — ITEM-26 (R-26-FRAME site: package rule); section *Next step and recovery*; action `replace`; span `eos`

```text
Each runnable direct-native package states its prompt/directory, actor and retained session
```

  becomes

```text
Each runnable direct-native package names its destination, receiving role and session, and input artifacts by repository path; the artifacts hold the rest.
```

#### CL-E-10

- **LCL-E-10-1** — ITEM-26 (R-26-FRAME site: CL-20 route); section *Next step and recovery*; action `replace`; span `eos`

```text
Carry exact Epic Specification, Strategy Card, Plan/review, PR/Ops/documentation
```

  becomes

```text
Name the `CHANGE_CLOSURE_DECISION` and each already-produced addendum by repository path; the artifacts hold the rest.
```

- **LCL-E-10-2** — ITEM-26 (R-26-FRAME site: package rule); section *Next step and recovery*; action `replace`; span `eos`

```text
Each runnable package states prompt/directory, actor/session, inputs/lineage, state
```

  becomes

```text
Each runnable package names its destination, receiving role and session, and input artifacts by repository path; the artifacts hold the rest.
```

#### DOC-10

- **LDOC-10-1** — ITEM-29 (R-A7-LOCAL site); section *Execute (step 5)*; action `replace`; span `anchor`

```text
Nathan manual merge, PR-40 read-only landed-lineage review
```

  becomes

```text
Nathan manual merge, PR-40 read-only landed-lineage review entered on `MERGE_OBSERVED` or, only where no `MERGE_OBSERVED` result was returned for this merge, on Nathan's merge assertion
```

#### DOC-20

- **LDOC-20-1** — ITEM-29 (R-A7-LOCAL site 1); section *Required inputs*; action `replace`; span `anchor`

```text
separately from Nathan's later merge assertion and PR-40's independent landed-lineage evidence
```

  becomes

```text
separately from the `MERGE_OBSERVED` merge event or, only where no `MERGE_OBSERVED` result was returned for this merge, Nathan's merge assertion, and from PR-40's independent landed-lineage evidence
```

- **LDOC-20-2** — ITEM-29 (R-A7-LOCAL site 2); section *Result routing*; action `replace`; span `anchor`

```text
landed-lineage review needed after Nathan's assertion:
```

  becomes

```text
landed-lineage review needed after Nathan's merge assertion, only where no `MERGE_OBSERVED` result was returned for this merge:
```

#### GCFPE-MGMT-10-PROPOSED

- **LGCFPE-MGMT-10-PROPOSED-1** — ITEM-23 (R-ITEM23 companion: stale preamble sentence); section *(page preamble, above the first ---)*; action `replace`; span `anchor`

```text
are left unstamped on purpose — those are set when the register promotes it
```

  becomes

```text
are not lines of this body, because bodies carry no release-bound header line (`D23-G`); the register records its version at promotion
```

#### OPS-10

- **LOPS-10-1** — ITEM-26 (PART-13), R-26-FRAME site; section *Complete OPS_TASK in READY state → OPS-20*; action `replace`; span `anchor`

```text
must preserve in its execution result and return handoff
```

  becomes

```text
must preserve in its execution result, which its return handoff names
```

- **LOPS-10-2** — ITEM-27 (A2, PART-13), census package carrier missed by R-A2g; section *Remediation discovery task → ESC-25 and ESC-30*; action `replace`; span `anchor`

```text
redlines when applicable, CANON_CONFLICT_REGISTER, all actual evidence, attempts and access limitations
```

  becomes

```text
redlines when applicable, all actual evidence, attempts and access limitations
```

#### OPS-20

- **LOPS-20-1** — ITEM-27 (A2, PART-13), census package carrier missed by R-A2g; section *Remediation discovery task → ESC-25 then ESC-30*; action `replace`; span `anchor`

```text
redlines when applicable, CANON_CONFLICT_REGISTER, all evidence, attempts and access limitations
```

  becomes

```text
redlines when applicable, all evidence, attempts and access limitations
```

#### OPS-30

- **LOPS-30-1** — ITEM-26 (PART-13), REAL finding 'Task-only next-step transport'; section *Task-only next-step transport*; action `delete`; span `anchor+space`

```text
A saved attachment, link or scattered fields do not replace the handoff.
```

  becomes

(deleted)

#### PR-10

- **LPR-10-1** — ITEM-26 (R-26-FRAME); section *INSTRUCTION_READY → PR-20*; action `replace`; span `eol`

```text
Complete native input package: carry PR_INSTRUCTION_ID and its complete content
```

  becomes

```text
Complete native input package naming PR_INSTRUCTION_ID by repository path; the artifacts hold the rest.
```

- **LPR-10-2** — ITEM-26 / ITEM-28 (R-26-BRANCH-SEND); section *INSTRUCTION_READY → PR-20 (Direct continuation after PR-20)*; action `replace`; span through `which runs in its own dedicated session.`

```text
PR-30 then hands the workspace/worktree, branch, open PR, instruction, Plan, original Proceed,
```

  becomes

```text
PR-30 then hands off directly to PR-35 — Resolve PR Reviews and Reach Merge Readiness, which runs in its own dedicated session, naming `PR_IMPLEMENTATION_RESULT` by repository path and the pull request reference; the artifacts hold the rest.
```

- **LPR-10-3** — ITEM-29 (R-A7-LOCAL); section *INSTRUCTION_READY → PR-20 (Direct continuation after PR-20)*; action `replace`; span `anchor`

```text
only after Nathan asserts it occurred may PR-40
```

  becomes

```text
only after the merge is observed as `MERGE_OBSERVED` or, only where no `MERGE_OBSERVED` result was returned for this merge, asserted by Nathan, may PR-40
```

- **LPR-10-4** — ITEM-26 (R-26-FRAME); section *MATERIAL SCOPE, ARCHITECTURE, REQUIREMENT OR DESIGN CHANGE → RS-10 and RS-20*; action `replace`; span `eol`

```text
RS-10 complete native inputs: GCF-17.RESCOPE coverage; exact PR_INSTRUCTION_ID or FINDING_REF;
```

  becomes

```text
RS-10 complete native inputs: GCF-17.RESCOPE coverage, naming PR_INSTRUCTION_ID or FINDING_REF, the Specification, Implementation Audit, Implementation Plan and PLAN_REVIEW, and any existing RESCOPE_PROPOSAL_ID or RESCOPE_REVIEW_ID by repository path; the artifacts hold the rest.
```

#### PR-20

- **LPR-20-1** — ITEM-26 / ITEM-28 (R-26-BRANCH-SEND); section *COMPLETE APPROVED-SCOPE PLAN → PR-30 (Complete native input package, 4th bullet)*; action `replace`; span `eol`

```text
Exact CHANGE_CLASS, CHANGE_ID, branch and repository/reference baseline; planned files/components; exclusions;
```

  becomes

```text
`PR_IMPLEMENTATION_PLAN` and `PR_INSTRUCTION` are each named by repository path; the artifacts hold the baseline, scope, acceptance and the rest.
```

- **LPR-20-2** — ITEM-26 / ITEM-28 (R-26-BRANCH-SEND); section *COMPLETE APPROVED-SCOPE PLAN → PR-30 (Native PR-30 operation and result)*; action `replace`; span through `and unresolved lineage.`

```text
carrying the one workspace/worktree, branch, open PR, instruction, Plan, original Proceed, commits,
```

  becomes

```text
naming `PR_IMPLEMENTATION_RESULT` by repository path and the pull request reference; the artifacts hold the rest.
```

- **LPR-20-3** — ITEM-26 / ITEM-28 (R-26-BRANCH-SEND); section *PR-35 REVIEW AND READINESS PHASE IN ITS OWN DEDICATED SESSION*; action `replace`; span `eol`

```text
Complete native input package: the exact PR-30 result; PR-35's own dedicated session, entered
```

  becomes

```text
Complete native input package: PR-35's own dedicated session, entered from PR-30's handoff, naming the PR-30 result (`PR_IMPLEMENTATION_RESULT`), the PR instruction and the detailed Plan by repository path and the pull request reference; the artifacts hold the rest. The branch, head and commits are verified at entry from the recorded vehicle and repository state; the handoff does not carry them.
```

- **LPR-20-4** — ITEM-29 (R-A7-LOCAL); section *PR-40 DOWNSTREAM LINEAGE REVIEW (Destination prompt and directory)*; action `replace`; span `anchor`

```text
and Nathan invokes PR-40 asserting that manual merge occurred
```

  becomes

```text
and the merge is observed as `MERGE_OBSERVED` or, only where no `MERGE_OBSERVED` result was returned for this merge, asserted by Nathan
```

- **LPR-20-5** — ITEM-29 (R-A7-LOCAL); section *PR-40 DOWNSTREAM LINEAGE REVIEW (Complete native input package, 3rd bullet)*; action `replace`; span `eol`

```text
Nathan's PR-40 invocation asserts that the identified PR was manually merged;
```

  becomes

```text
The complete PR-35 result: MERGE_OBSERVED with the observed merge event, or, only where no MERGE_OBSERVED result was returned for this merge, the earlier MERGE_PENDING, which is historical pre-merge evidence, with Nathan's assertion that he manually merged the identified PR. Neither substitutes for PR-40's independent verification of actual merged state and landed lineage.
```

- **LPR-20-6** — ITEM-26 (R-26-FRAME); section *PR-40 DOWNSTREAM LINEAGE REVIEW (Complete native input package, 2nd bullet)*; action `replace`; span `eol`

```text
Exact CHANGE_CLASS, CHANGE_ID, WORK_UNIT_ID, Specification/Implementation Audit/Plan/review lineage, continuing reviewer/session identity
```

  becomes

```text
Exact CHANGE_CLASS, CHANGE_ID and WORK_UNIT_ID and the continuing reviewer/session identity; the artifacts hold the rest, and PR-40 resolves merge, commit, order and check evidence from repository evidence.
```

- **LPR-20-7** — ITEM-26 (R-26-FRAME); section *MATERIAL ... → RS-10, RS-20, RS-30 (Complete RS-10 package, 1st bullet)*; action `replace`; span `eol`

```text
GCF-17.RESCOPE; exact PR_INSTRUCTION_ID, CHANGE_CLASS, CHANGE_ID, WORK_UNIT_ID, approved SPECIFICATION_ID
```

  becomes

```text
GCF-17.RESCOPE, naming PR_INSTRUCTION_ID, the current PR plan, SPECIFICATION_ID, IMPLEMENTATION_AUDIT_ID, IMPLEMENTATION_PLAN_ID and PLAN_REVIEW_ID by repository path; the artifacts hold the rest.
```

- **LPR-20-8** — ITEM-26 (R-26-FRAME); section *MATERIAL ... → RS-10, RS-20, RS-30 (Complete RS-30 package, 1st bullet, 3rd sentence)*; action `replace`; span `eol`

```text
Also carry the originating stage, CHANGE_CLASS, CHANGE_ID, WORK_UNIT_ID, approved Specification/Plan/review,
```

  becomes

```text
Also name the approved Specification/Plan/review by repository path, with the Product Owner/manual prerequisites as minimum context; the artifacts hold the rest.
```

#### PR-30

- **LPR-30-1** — ITEM-26 / ITEM-28 (R-26-BRANCH-SEND); section *Execute (step 6)*; action `replace`; span through `and recovery lineage.`

```text
Carry the exact dedicated session, open PR, instruction, detailed Plan, original Proceed, immutable base,
```

  becomes

```text
The handoff names `PR_IMPLEMENTATION_RESULT`, the instruction and the detailed Plan by repository path, and the pull request reference; the artifacts hold the rest.
```

- **LPR-30-2** — ITEM-27 (A1 variant; R-A1e note); section *GCFPE identity, maintenance and prompt-use evidence*; action `replace`; span `anchor`

```text
If that path is outside the approved Plan, return the metadata
```

  becomes

```text
If that path is outside the approved Plan, record the metadata in the output artifact
```

#### PR-35

- **LPR-35-1** — ITEM-26 / ITEM-28 (R-26-FRAME + R-26-BRANCH-RECV); section *Required inputs and continuity identity (package list, 8th bullet)*; action `replace`; span `eol`

```text
exact repository, authorized local root, open PR, tests, publication state, reviews/checks already observed,
```

  becomes

```text
exact repository, authorized local root, open PR and artifact links; and
```

- **LPR-35-2** — ITEM-26 / ITEM-28 (R-26-BRANCH-RECV); section *Required inputs and continuity identity (after the package list)*; action `insert_after`; span `anchor`

```text
exact `PR_RETURN_PHASE` and rescope lineage when entering from an eligible RS-40 continuation.
```

  becomes

```text

The branch, head and commits are verified at entry from the recorded vehicle and repository state; the handoff does not carry them.
```

#### PR-40

- **LPR-40-1** — ITEM-26 (R-26-FRAME); section *ACCEPT → same whole-change IA owner (Complete native input package, 2nd bullet)*; action `replace`; span `eol`

```text
Complete Specification, Implementation Audit, Plan, Plan review, PR instruction and implementation result; actual merged-state
```

  becomes

```text
Specification, Implementation Audit, Plan, Plan review, PR instruction and implementation result, each named by repository path, and the same whole-change IA identity; the artifacts hold the rest.
```

- **LPR-40-2** — ITEM-26 (R-26-FRAME); section *MATERIAL ... → RS-10, RS-20, RS-30 (RS-10 package, 1st bullet)*; action `replace`; span `eol`

```text
GCF-17.RESCOPE; the complete PR_WORK_UNIT_LINEAGE_REVIEW finding; PR_INSTRUCTION_ID; PR_IMPLEMENTATION_PLAN_ID
```

  becomes

```text
GCF-17.RESCOPE, naming the PR_WORK_UNIT_LINEAGE_REVIEW finding, PR_INSTRUCTION_ID, PR_IMPLEMENTATION_PLAN_ID, the PR-30 and PR-35 results, SPECIFICATION_ID, IMPLEMENTATION_AUDIT_ID and PLAN_REVIEW_ID by repository path, with the exact PR refs; the artifacts hold the rest.
```

- **LPR-40-3** — ITEM-26 / ITEM-29 (R-26-FRAME; A7 package item); section *PENDING MERGE OR UNAVAILABLE EVIDENCE*; action `replace`; span `eol`

```text
Complete native input package: PR_WORK_UNIT_LINEAGE_REVIEW with PENDING; exact missing PR or repository fact
```

  becomes

```text
Complete native input package: PR_WORK_UNIT_LINEAGE_REVIEW with PENDING, PR_INSTRUCTION_ID, PR_IMPLEMENTATION_PLAN_ID and the PR-30 and PR-35 results, each by repository path; the exact missing PR or repository fact, its evidence owner and the exact manual prerequisite as minimum context; the artifacts hold the rest.
```

- **LPR-40-4** — ITEM-26 / ITEM-28 (R-26-BRANCH-RECV); section *Inputs (4th bullet)*; action `replace`; span `anchor`

```text
, with each actual PR reference, commit identity, order, review/check state and merge evidence
```

  becomes

```text
; PR-40 resolves each PR's commits, order, review/check state and merge evidence from repository evidence
```

- **LPR-40-5** — ITEM-26 / ITEM-28 (R-26-BRANCH-RECV); section *Inputs (after the package list, before the W-4 paragraph)*; action `insert_after`; span `anchor`

```text
NOT PRODUCED and NOT EXECUTED values, and all actual access limitations.
```

  becomes

```text

The branch, head and commits are verified at entry from the recorded vehicle and repository state; the handoff does not carry them.
```

- **LPR-40-6** — ITEM-29 (R-A7-LOCAL); section *Read-only review boundary*; action `replace`; span `anchor`

```text
Nathan's invocation supplies only the later manual-merge assertion and review authorization
```

  becomes

```text
The pasted handoff supplies the observed merge event or, only where no `MERGE_OBSERVED` result was returned for this merge, Nathan's manual-merge assertion, and review authorization
```

- **LPR-40-7** — ITEM-29 (R-A7-LOCAL); section *Execute (step 1)*; action `replace`; span `anchor`

```text
historical PR-35 `MERGE_PENDING` result, Nathan's later manual-merge assertion,
```

  becomes

```text
PR-35 `MERGE_OBSERVED` result or, only where no `MERGE_OBSERVED` result was returned for this merge, the historical PR-35 `MERGE_PENDING` result and Nathan's manual-merge assertion,
```

#### QA-10

- **LQA-10-P03** — ITEM-17 (P-03); section *role*; action `replace`; span `anchor`

```text
This is a read-only audit and readiness role.
```

  becomes

```text
This is an audit and readiness role.
```

- **LQA-10-P19** — ITEM-26 (PART-13), P-19: QA-10 twin of LOPS-30-1; section *Task-only next-step transport*; action `delete`; span `anchor+space`

```text
A saved attachment, link or scattered fields do not replace the handoff.
```

  becomes

(deleted)

#### RS-20

- **LRS-20-1** — ITEM-26 / ITEM-28 (R-26-BRANCH-RECV); section *Required inputs*; action `replace`; span through `and unresolved work.`

```text
Carry original Proceed, dedicated PR session, workspace/worktree, branch, open PR/head only when one exists,
```

  becomes

```text
The request or proposal records the original Proceed, the recorded phase's own dedicated session, the open PR reference only when one exists, and the instruction and Plan by repository path; `RESCOPE_REVIEW` records the vehicle state it relies on. The branch, head and commits are verified at entry from the recorded vehicle and repository state; the handoff does not carry them.
```

#### RS-40

- **LRS-40-1** — ITEM-26 / ITEM-28 (R-26-BRANCH-RECV); section *Required inputs*; action `replace`; span through `and return condition.`

```text
the recorded phase's own dedicated session, workspace/worktree, branch, pull request, and current head;
```

  becomes

```text
the recorded phase's own dedicated session, pull request reference and artifacts by repository path; and the return condition. The branch, head and commits are verified at entry from the recorded vehicle and repository state; the handoff does not carry them.
```

- **LRS-40-2** — ITEM-29 / ITEM-30 (R-A7-LOCAL); section *Public result and routing (MERGE_PENDING bullet)*; action `replace`; span `anchor`

```text
Return one conditional block for use only after Nathan manually merges the identified PR;
```

  becomes

```text
Return one conditional block for use only after Nathan manually merges the identified PR and only where no `MERGE_OBSERVED` result was returned for this merge;
```

- **LRS-40-3** — ITEM-29 (R-A7-LOCAL); section *Public result and routing (MERGE_PENDING bullet)*; action `delete`; span `anchor`

```text
states that Nathan's later invocation asserts the manual merge, 
```

  becomes

(deleted)

### 3.5 CHECKs (the LOCAL-only rules' anchors)

Each must read 0 on its rows after the edits, and each read above 0 on the unedited bodies where its class occurred (§8).

- **R-26-FRAME** on CF-C-10, CF-E-10, CF-C-20, CF-E-20, CF-C-30, CF-E-30, CF-C-40, CF-E-40, CL-20, CL-30, CL-C-10, CL-E-10, OPS-10, PR-10, PR-20, PR-35, PR-40

```regex
recovery package carries the original CLASS_SELECTION_REF|UNRESOLVED_CLASSIFICATION_CASE with the preserved source/change facts|direct package contains the exact pending Specification, class/change lineage|recovery carries the original kickoff link, exact defect, class/change lineage|and approval lineage, the carried conflict register|actual mode, class/change/base lineage|carrying the exact qualified condition, lineage, evidence|Carry the complete candidate, positive closure and architecture-decision lineage|Carry exact (?:CRD|Epic) Specification|Each runnable (?:direct-native )?package states|must preserve in its execution result and return handoff|carry PR_INSTRUCTION_ID and its complete content|dependency and evidence history; read-only substantiation of the mismatch; completed work|dependency/evidence history, completed work and unaffected obligations|all actual merge/commit/order/check evidence|PR instruction and implementation result; actual merged-state evidence|dependency, acceptance and evidence history
```

- **R-26-BRANCH-SEND** on PR-10, PR-20, PR-30

```regex
(?i)\b(?:hands?|carry|carrying|carries)\s+(?:the\s+)?(?:one\s+|exact\s+|same\s+)?(?:original Proceed, dedicated PR session, )?workspace/worktree, branch\b|Carry the exact dedicated session, open PR|commit and remote-head references; completed work|branch and repository/reference baseline
```

- **R-26-BRANCH-RECV** on PR-35, PR-40, RS-20, RS-40

```regex
Carry original Proceed, dedicated PR session, workspace/worktree, branch|current head; completed work, commits/local changes|reviews/checks already observed, unresolved items|with each actual PR reference, commit identity, order|dedicated session, workspace/worktree, branch, pull request, and current head
```

- **R-A7-LOCAL** on PR-10, PR-20, PR-40, DOC-10, DOC-20, RS-40

```regex
only after Nathan asserts it occurred may PR-40|Nathan invokes PR-40 asserting that manual merge occurred|Nathan's PR-40 invocation asserts that the identified PR was manually merged|Nathan's invocation supplies only the later manual-merge assertion|historical PR-35 `MERGE_PENDING` result, Nathan's later manual-merge assertion|Nathan manual merge, PR-40 read-only landed-lineage review(?! entered on `MERGE_OBSERVED`)|Nathan's later merge assertion and PR-40's independent|needed after Nathan's assertion: continue to `?PR-40|states that Nathan's later invocation asserts the manual merge|Return one conditional block for use only after Nathan manually merges the identified PR;
```

- **R-ITEM40** on GCFPE-MGMT-10-PROPOSED

```regex
(?:metadata|lineage) or (?:the |returned |the returned )?handoff\b|artifact/handoff metadata|, in (?:the )?returned handoff\b|substantive artifact(?: metadata/content)? and handoffs?\b|through (?:all next/recovery packages|every next and recovery package)\b|Embed only applicable workflow contracts|These candidate URL tokens must be replaced|Repository paths outside `?docs/ephemeral/`? and `?docs/graph/`? are not written
```

- **R-ITEM23-gate** on GCFPE-MGMT-10-PROPOSED

```regex
(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?(?:Prompt [Vv]ersion|Ecosystem release|Set)(?:\*\*|__|`){0,2}[ \t]*:
```

- **R-26-RSP-scan** on PR-10, PR-20, PR-40

```regex
RESCOPE_PROPOSAL_ID and complete RESCOPE_PROPOSAL\b
```

### 3.6 Authored wording accepted with the plan (P-20)

Every LOCAL new text in §3.4 is authored. It names artifacts by repository path, says "the artifacts hold the rest"
(C-HANDOFF, C-PLACE), and uses C-ART's "which records …" and "which the handoff names". Where a slot needed words the
original sentence lacked, the words come from the body's own Inputs or Required result. The CF twins' texts are word
for word the same in each C/E pair (dry run A). Approving the plan accepts these texts as written.

## §4 Registry

### 4.1 The change

`EV/registry/registry.diff` applies to `project-prompt-contract-registry.md` at sha256
`8b4e46ed2dc24442e3dadc416dfe4c810a048788bf03c799808927a54c2677d4` (322556 B) and gives sha256 `97bda1a06b0c917fa66bdfb098e9d9c0b5d394f16d62a3bfa953f16253219015` (7700 lines). The diff's
own sha256 is `fcfd549e2850423a169adb6ad6166e580625e0e8e1e87adbdde03941d122bc8b`. Assertions: [1484, 2024]. Both the installed and the final
validator report `valid: true`. `registry_deriver` reports drift `[]` against the current parts and the reindexed
parts, with both audit copies. The synthetic suite (`guard_tests.py`) is `ALL_OK`: every forbidden guard fires on
its regression and is silent on the 75 canonical and 188 authored texts, except the intended G-K51 (C-LAT) and G-K44
(the unfilled token). Every required guard fails on removal and on the retired wording put back.

### 4.2 Guards

Rule codes: TOP-001 for handoff content, CTR-001 for other forbidden guards, CTR-002 for required guards; the release
guards keep SRC-001 and INV-003 (P-27). Every regression is at most 12 words.

- **G-K01 R-A1a, R-A1b, R-A1c, R-A1d, R-A1e, R-A1f** — `forbidden_regex`, `TOP-001`, rows: ALL55 (every row)

```regex
(?:metadata|lineage) or (?:the |returned |the returned )?handoff\b|artifact/handoff metadata|, in (?:the )?returned handoff\b
```

  regression: ```text
inject into CL-20: metadata or handoff
```

- **G-K02 R-A1a, R-A1b** — `required_regex`, `CTR-002`, rows: CL-20, CL-30, CL-E-20, CL-E-30, CL-E-40, DOC-10, DOC-20, ESC-10, ESC-25, ESC-30, ESC-40, OPS-10, OPS-20, PR-30, PR-40, QA-100, QA-110, QA-120, QA-20, QA-50, QA-60, QA-70, QA-80, QA-90, RS-10, RS-20, RS-30, CL-C-10, CL-E-10, OPS-30, PR-10, PR-20, QA-10

```regex
in the output artifact's (?:existing )?permitted metadata
```

  regression: ```text
in CL-20, put the retired wording back in place of the new text: in permitted metadata or handoff
```

- **G-K03 R-A2a, R-A2b, R-A2c, R-A2d, R-A2e, R-A2f1, R-A2f2** — `forbidden_regex`, `TOP-001`, rows: ALL55 (every row)

```regex
substantive artifact(?: metadata/content)? and handoffs?\b|through (?:all next/recovery packages|every next and recovery package)\b|review result and every native return\b|and every return package\b|receipt, review and handoff metadata|receipt and handoff when applicable
```

  regression: ```text
inject into CL-20: substantive artifact and handoff
```

- **G-K04 R-A2a, R-A2b, R-A2c, R-A2d** — `required_regex`, `CTR-002`, rows: DOC-10, DOC-20, ESC-10, ESC-25, ESC-30, ESC-40, QA-100, QA-110, QA-120, QA-20, QA-50, QA-60, QA-70, QA-80, QA-90, RS-10, RS-20, RS-30, CL-C-10, CL-E-10, OPS-30, PR-10, PR-20, PR-30, PR-40, QA-10, OPS-10, OPS-20

```regex
(?:substantive artifact(?: metadata/content)?|review metadata|and receipt), which the handoff names
```

  regression: ```text
in DOC-10, put the retired wording back in place of the new text: in the existing substantive artifact and handoff
```

- **G-K05 R-A2e** — `required_regex`, `CTR-002`, rows: CL-C-10, CL-E-10, OPS-10, OPS-30, PR-10, PR-20, PR-30, PR-40, QA-10

```regex
unresolved facts in the output artifact, which each next or recovery handoff names
```

  regression: ```text
in CL-C-10, put the retired wording back in place of the new text: unresolved facts through all next/recovery packages
```

- **G-K06 R-A2f1** — `required_regex`, `CTR-002`, rows: PR-40

```regex
every native return names those artifacts
```

  regression: ```text
in PR-40, put the retired wording back in place of the new text: review result and every native return without deciding Canon
```

- **G-K07 R-A2f2** — `required_regex`, `CTR-002`, rows: QA-10

```regex
every return package names those artifacts
```

  regression: ```text
in QA-10, put the retired wording back in place of the new text: `QA_READINESS` and every return package
```

- **G-K08 R-A2g** — `forbidden_regex`, `TOP-001`, rows: IA-10, IA-20, IA-30, OPS-30, PR-10, PR-20, PR-40, QA-10

```regex
(?m)(?:^(?:Complete native input package|(?:Exact |Required |Complete )?[Nn]ative inputs(?: and artifact lineage)?|RS-\d+ complete native inputs|Complete RS-\d+ package|Sole substantive input)\b[^\n]*`?CANON_CONFLICT_REGISTER|^(?:Complete native input package|Required native inputs|Complete RS-\d+ package):\n(?:- [^\n]*\n)*?- [^\n]*`?CANON_CONFLICT_REGISTER|(?:\bsend\b|\bcarrying\b)[^.\n]*\bconflict register\b)
```

  regression: ```text
inject into IA-10: Complete native input package: PR_WORK_UNIT_LINEAGE_REVIEW with PENDING; CANON_CONFLICT_REGISTER
```

- **G-K08 R-A2g** — `forbidden_regex`, `TOP-001`, rows: OPS-10, OPS-20

```regex
(?m)(?:^(?:Complete native input package|(?:Exact |Required |Complete )?[Nn]ative inputs(?: and artifact lineage)?|RS-\d+ complete native inputs|Complete RS-\d+ package|Sole substantive input)\b[^\n]*`?CANON_CONFLICT_REGISTER|^(?:Complete native input package|Required native inputs|Complete RS-\d+ package):\n(?:- [^\n]*\n)*?- [^\n]*`?CANON_CONFLICT_REGISTER|(?:\bsend\b|\bcarrying\b)[^.\n]*\bconflict register\b|^(?:Complete return to ESC-30|RS-30 native revision):[^\n]*CANON_CONFLICT_REGISTER)
```

  regression: ```text
inject into OPS-10: Complete return to ESC-30: ORIGINATING_FINDING_REF, CANON_CONFLICT_REGISTER
```

- **G-K09 R-26-P1** — `forbidden_regex`, `TOP-001`, rows: ALL55 (every row)

```regex
current status and lineage; decisions already made|Carry complete native inputs rather than referring to
```

  regression: ```text
inject into CL-20: current status and lineage; decisions already made
```

- **G-K10 R-26-P1** — `required_regex`, `CTR-002`, rows: OPS-10, OPS-20, OPS-30, PR-10, PR-20, PR-30, PR-40, QA-10

```regex
Then give the other fields the handoff rule above names; sections the artifact already holds are named, not repeated\.
```

  regression: ```text
in OPS-10, put the retired wording back in place of the new text: current status and lineage; decisions already made
```

- **G-K11 R-26-P1b** — `forbidden_regex`, `TOP-001`, rows: IA-30, UTIL-10

```regex
unresolved items/owners, next action, and expected (?:output|review state)
```

  regression: ```text
inject into IA-30: unresolved items/owners, next action, and expected output
```

- **G-K12 R-26-P3** — `forbidden_regex`, `TOP-001`, rows: CL-20, CL-30, CL-40, CL-C-10, CL-E-10

```regex
lineage into its result and handoff\b
```

  regression: ```text
inject into CL-20: lineage into its result and handoff
```

- **G-K13 R-26-P3** — `required_regex`, `CTR-002`, rows: CL-20, CL-30, CL-40, CL-C-10, CL-E-10

```regex
PF10/addendum lineage into its result artifact, which the handoff names
```

  regression: ```text
in CL-20, put the retired wording back in place of the new text: PF10/addendum lineage into its result and handoff
```

- **G-K14 R-26-P4** — `forbidden_regex`, `TOP-001`, rows: CL-C-10, CL-E-10, PR-40, QA-10, PR-10, PR-20, PR-30, OPS-10, OPS-20, OPS-30

```regex
Catalogs and runtime handoffs carry\b
```

  regression: ```text
inject into CL-C-10: Catalogs and runtime handoffs carry
```

- **G-K15 R-26-TASK** — `forbidden_regex`, `TOP-001`, rows: OPS-30, QA-10

```regex
native inputs, lineage, current state, gates, risks and required action
```

  regression: ```text
inject into OPS-30: native inputs, lineage, current state, gates, risks and required action
```

- **G-K16 R-26-TASK** — `required_regex`, `CTR-002`, rows: OPS-30, QA-10

```regex
each input artifact by repository path; the artifacts hold the rest
```

  regression: ```text
in OPS-30, put the retired wording back in place of the new text: native inputs, lineage, current state, gates, risks and required action
```

- **G-K17 R-26-CLOSE** — `forbidden_regex`, `TOP-001`, rows: CL-20, CL-30

```regex
Carry the positive closure decision, complete post-closure results
```

  regression: ```text
inject into CL-20: Carry the positive closure decision, complete post-closure results
```

- **G-K18 R-26-CLOSE** — `required_regex`, `CTR-002`, rows: CL-20, CL-30

```regex
Name the positive closure decision and every post-closure result artifact by repository path
```

  regression: ```text
in CL-20, put the retired wording back in place of the new text: Carry the positive closure decision, complete post-closure results
```

- **G-K19 R-26-FRAME** — `forbidden_regex`, `TOP-001`, rows: CF-C-10, CF-E-10

```regex
recovery package carries the original CLASS_SELECTION_REF|UNRESOLVED_CLASSIFICATION_CASE with the preserved source/change facts
```

  regression: ```text
inject into CF-C-10: recovery package carries the original CLASS_SELECTION_REF
```

- **G-K19 R-26-FRAME** — `forbidden_regex`, `TOP-001`, rows: CF-C-20, CF-E-20

```regex
direct package contains the exact pending Specification, class/change lineage|recovery carries the original kickoff link, exact defect, class/change lineage
```

  regression: ```text
inject into CF-C-20: direct package contains the exact pending Specification, class/change lineage
```

- **G-K19 R-26-FRAME** — `forbidden_regex`, `TOP-001`, rows: CF-C-30, CF-E-30

```regex
and approval lineage, the carried conflict register
```

  regression: ```text
inject into CF-C-30: and approval lineage, the carried conflict register
```

- **G-K19 R-26-FRAME** — `forbidden_regex`, `TOP-001`, rows: CF-C-40, CF-E-40

```regex
actual mode, class/change/base lineage
```

  regression: ```text
inject into CF-C-40: actual mode, class/change/base lineage
```

- **G-K19 R-26-FRAME** — `forbidden_regex`, `TOP-001`, rows: CL-20

```regex
carrying the exact qualified condition, lineage, evidence
```

  regression: ```text
inject into CL-20: carrying the exact qualified condition, lineage, evidence
```

- **G-K19 R-26-FRAME** — `forbidden_regex`, `TOP-001`, rows: CL-30

```regex
Carry the complete candidate, positive closure and architecture-decision lineage
```

  regression: ```text
inject into CL-30: Carry the complete candidate, positive closure and architecture-decision lineage
```

- **G-K19 R-26-FRAME** — `forbidden_regex`, `TOP-001`, rows: CL-C-10, CL-E-10

```regex
Carry exact (?:CRD|Epic) Specification|Each runnable (?:direct-native )?package states
```

  regression: ```text
inject into CL-C-10: Carry exact Epic Specification
```

- **G-K19 R-26-FRAME** — `forbidden_regex`, `TOP-001`, rows: OPS-10

```regex
must preserve in its execution result and return handoff
```

  regression: ```text
inject into OPS-10: must preserve in its execution result and return handoff
```

- **G-K19 R-26-FRAME** — `forbidden_regex`, `TOP-001`, rows: PR-10

```regex
carry PR_INSTRUCTION_ID and its complete content|dependency and evidence history; read-only substantiation of the mismatch; completed work
```

  regression: ```text
inject into PR-10: dependency and evidence history; read-only substantiation of the mismatch; completed work
```

- **G-K19 R-26-FRAME** — `forbidden_regex`, `TOP-001`, rows: PR-20

```regex
dependency/evidence history, completed work and unaffected obligations|all actual merge/commit/order/check evidence|current stage and suspended boundary, completed work, dependencies, evidence
```

  regression: ```text
inject into PR-20: dependency/evidence history, completed work and unaffected obligations
```

- **G-K19 R-26-FRAME** — `forbidden_regex`, `TOP-001`, rows: PR-40

```regex
PR instruction and implementation result; actual merged-state evidence|dependency, acceptance and evidence history; completed work|all completed review work; attempts; limitations
```

  regression: ```text
inject into PR-40: PR instruction and implementation result; actual merged-state evidence
```

- **G-K20 R-26-BRANCH-SEND** — `forbidden_regex`, `TOP-001`, rows: PR-10, PR-20, PR-30

```regex
(?i)\b(?:hands?|carry|carrying|carries)\s+(?:the\s+)?(?:one\s+|exact\s+|same\s+)?(?:original Proceed, dedicated PR session, )?workspace/worktree, branch\b|Carry the exact dedicated session, open PR|commit and remote-head references; completed work|branch and repository/reference baseline
```

  regression: ```text
inject into PR-10: hands the workspace/worktree, branch
```

- **G-K21 R-26-BRANCH-RECV, R-26-FRAME** — `forbidden_regex`, `TOP-001`, rows: PR-35, PR-40, RS-20, RS-40

```regex
Carry original Proceed, dedicated PR session, workspace/worktree, branch|current head; completed work, commits/local changes|reviews/checks already observed, unresolved items|with each actual PR reference, commit identity, order
```

  regression: ```text
inject into PR-35: reviews/checks already observed, unresolved items
```

- **G-K22 R-26-BRANCH-RECV** — `required_regex`, `CTR-002`, rows: PR-35, PR-40, RS-20, RS-40

```regex
verified at entry from the recorded vehicle and repository state; the handoff does not carry them
```

  regression: ```text
in PR-35, put the retired wording back in place of the new text: open PR, tests, reviews/checks already observed, unresolved items
```

- **G-K23 R-A7-S1a, R-A7-S1b, R-A7-S2, R-A7-CL, R-A7-S3, R-ITEM21, R-A7-LOCAL** — `forbidden_regex`, `CTR-001`, rows: ALL55 (every row)

```regex
Nathan's (?:later )?(?:manual )?(?:PR-40 )?invocation asserts\b|PR-40 independently verifies the later asserted merge\b|usable only after Nathan later manually merges the identified PR\.|merge-approval effect is defined above
```

  regression: ```text
inject into CL-20: Nathan's later invocation asserts
```

- **G-K24 R-A7-S1b, R-A7-S2, R-A7-CL, R-A7-S3** — `required_regex`, `CTR-002`, rows: OPS-30, PR-10, PR-20, PR-30, QA-10, CL-20, CL-30, CL-40, CL-C-10, CL-E-10, CL-E-20, CL-E-30, CL-E-40, DOC-10, DOC-20, ESC-10, ESC-25, ESC-30, ESC-40, QA-20

```regex
PR-40 is entered on the observed merge event for the identified PR
```

  regression: ```text
in OPS-30, put the retired wording back in place of the new text: Nathan's later PR-40 invocation asserts that a manual merge occurred;
```

- **G-K25 R-A7-S1b, R-A7-CL, R-A7-S3** — `required_regex`, `CTR-002`, rows: OPS-30, PR-10, PR-20, PR-30, PR-40, QA-10, CL-20, CL-30, CL-40, CL-C-10, CL-E-10, CL-E-20, CL-E-30, CL-E-40, DOC-10, DOC-20, ESC-10, ESC-25, ESC-30, ESC-40, QA-20

```regex
PR-40 is entered once per merge: paste the `?MERGE_OBSERVED`? handoff when one arrives
```

  regression: ```text
in OPS-30, put the retired wording back in place of the new text: PR-40 independently verifies the later asserted merge and landed lineage.
```

- **G-K26 R-A7-LOCAL** — `forbidden_regex`, `CTR-001`, rows: PR-10, PR-20, PR-40, DOC-10, DOC-20, RS-40

```regex
only after Nathan asserts it occurred may PR-40|Nathan invokes PR-40 asserting that manual merge occurred|Nathan's invocation supplies only the later manual-merge assertion|historical PR-35 `MERGE_PENDING` result, Nathan's later manual-merge assertion|Nathan manual merge, PR-40 read-only landed-lineage review(?! entered on `MERGE_OBSERVED`)|Nathan's later merge assertion and PR-40's independent|needed after Nathan's assertion: continue to `?PR-40
```

  regression: ```text
inject into PR-10: only after Nathan asserts it occurred may PR-40
```

- **G-K27 R-ITEM21** — `required_regex`, `CTR-002`, rows: CL-20, CL-30, CL-C-10, CL-E-10

```regex
that entry creates no runtime approval
```

  regression: ```text
in CL-20, put the retired wording back in place of the new text: The specific Product Owner PR-40 merge-approval effect is defined above
```

- **G-K28 R-ITEM30a, R-ITEM30b** — `required_regex`, `CTR-002`, rows: PR-35, RS-40

```regex
`MERGE_OBSERVED`: [^\n]*?the subscribed PR-35 session observes the merge of the identified PR, performed by Nathan
```

  regression: ```text
in PR-35, put the retired wording back in place of the new text: - `MERGE_PENDING`: every readiness predicate above passes.
```

- **G-K29 R-ITEM30a, R-ITEM30c** — `forbidden_regex`, `CTR-001`, rows: PR-35

```regex
sixth top-level PR-35 result
```

  regression: ```text
inject into PR-35: sixth top-level PR-35 result
```

- **G-K30 R-ITEM30c** — `required_regex`, `CTR-002`, rows: PR-35

```regex
seventh top-level PR-35 result
```

  regression: ```text
in PR-35, put the retired wording back in place of the new text: sixth top-level PR-35 result
```

- **G-K31 R-ITEM30d** — `forbidden_regex`, `CTR-001`, rows: PR-35

```regex
The PR-40 handoff must say:|Nathan's later paste asserts
```

  regression: ```text
inject into PR-35: The PR-40 handoff must say:
```

- **G-K32 R-ITEM30d** — `required_regex`, `CTR-002`, rows: PR-35

```regex
for `MERGE_OBSERVED`, it is the same selected PR-40
```

  regression: ```text
in PR-35, put the retired wording back in place of the new text: conditionally usable only after Nathan's manual merge.
```

- **G-K33 R-ITEM31** — `forbidden_regex`, `CTR-001`, rows: PR-40

```regex
ordinary in-scope defect remains with the existing PR owner
```

  regression: ```text
inject into PR-40: ordinary in-scope defect remains with the existing PR owner
```

- **G-K34 R-ITEM31** — `required_regex`, `CTR-002`, rows: PR-40

```regex
re-plans through `?PR-20`?, as \*\*PRECISE IN-SCOPE DEFECT → re-plan\*\* states
```

  regression: ```text
in PR-40, put the retired wording back in place of the new text: An ordinary in-scope defect remains with the existing PR owner.
```

- **G-K35 R-OWN** — `forbidden_regex`, `CTR-001`, rows: CL-20, CL-30

```regex
Use only the read-only tools, stores, repository access[^.\n]*\.(?! Every statement in this prompt that it is read-only or does not change the repository excludes its own output artifacts)
```

  regression: ```text
inject into CL-20: Use only the read-only tools, stores, repository access.
```

- **G-K35 R-OWN** — `forbidden_regex`, `CTR-001`, rows: CL-40

```regex
It does not edit Canonical PF09, PF10, Canon, a board, registry, repository[^.\n]*\.(?! Every statement in this prompt that it is read-only or does not change the repository excludes its own output artifacts)
```

  regression: ```text
inject into CL-40: It does not edit Canonical PF09, PF10, Canon, a board, registry, repository.
```

- **G-K35 R-OWN** — `forbidden_regex`, `CTR-001`, rows: CL-E-20

```regex
revalidation session, read-only\.(?! Every statement in this prompt that it is read-only or does not change the repository excludes its own output artifacts)
```

  regression: ```text
inject into CL-E-20: revalidation session, read-only.
```

- **G-K35 R-OWN** — `forbidden_regex`, `CTR-001`, rows: DOC-20

```regex
do not edit documentation, Canon, PF10, or repository state\.(?! Every statement in this prompt that it is read-only or does not change the repository excludes its own output artifacts)
```

  regression: ```text
inject into DOC-20: do not edit documentation, Canon, PF10, or repository state.
```

- **G-K35 R-OWN** — `forbidden_regex`, `CTR-001`, rows: ESC-25

```regex
read-only repository reviewer[^.\n]*\.(?! Every statement in this prompt that it is read-only or does not change the repository excludes its own output artifacts)
```

  regression: ```text
inject into ESC-25: read-only repository reviewer.
```

- **G-K35 R-OWN** — `forbidden_regex`, `CTR-001`, rows: GCFPE-MGMT-10

```regex
does not execute product Change Flow, implementation, repository work[^.\n]*\.(?! Every statement in this prompt that it is read-only or does not change the repository excludes its own output artifacts)
```

  regression: ```text
inject into GCFPE-MGMT-10: does not execute product Change Flow, implementation, repository work.
```

- **G-K35 R-OWN** — `forbidden_regex`, `CTR-001`, rows: PR-20

```regex
Do not mutate the repository in this authoring operation\.(?! Every statement in this prompt that it is read-only or does not change the repository excludes its own output artifacts)
```

  regression: ```text
inject into PR-20: Do not mutate the repository in this authoring operation.
```

- **G-K35 R-OWN** — `forbidden_regex`, `CTR-001`, rows: PR-40

```regex
operating read-only\.(?! Every statement in this prompt that it is read-only or does not change the repository excludes its own output artifacts)
```

  regression: ```text
inject into PR-40: operating read-only.
```

- **G-K35 R-OWN** — `forbidden_regex`, `CTR-001`, rows: PR-50

```regex
otherwise mutating the workspace, worktree, branch, open PR, commits or evidence[^.\n]*\.(?! Every statement in this prompt that it is read-only or does not change the repository excludes its own output artifacts)
```

  regression: ```text
inject into PR-50: otherwise mutating the workspace, worktree, branch, open PR, commits or evidence.
```

- **G-K35 R-OWN** — `forbidden_regex`, `CTR-001`, rows: QA-10

```regex
read-only audit and readiness role
```

  regression: ```text
inject into QA-10: read-only audit and readiness role
```

- **G-K36 R-OWN** — `required_regex`, `CTR-002`, rows: CL-20, CL-30, CL-40, CL-E-20, DOC-20, ESC-25, GCFPE-MGMT-10, PR-20, PR-40, PR-50, QA-10

```regex
Every statement in this prompt that it is read-only or does not change the repository excludes its own output artifacts, which it writes, commits and pushes, and any pull request that carries them\.
```

  regression: ```text
in CL-20, put the retired wording back in place of the new text: excludes its own output artifacts, which it writes, commits and pushes.
```

- **G-K37 R-A10** — `forbidden_regex`, `CTR-001`, rows: ALL55 (every row)

```regex
Reviewers remain read-only(?! toward the work they review)
```

  regression: ```text
inject into CL-20: Reviewers remain read-only
```

- **G-K38 R-A10** — `required_regex`, `CTR-002`, rows: OPS-10, OPS-30, PR-40, QA-10

```regex
Reviewers remain read-only toward the work they review
```

  regression: ```text
in OPS-10, put the retired wording back in place of the new text: Reviewers remain read-only and acceptance requires substantive evidence.
```

- **G-K39 R-A5** — `forbidden_regex`, `CTR-001`, rows: GCFPE-MGMT-10, PR-35, RS-40

```regex
Repository paths outside `?docs/ephemeral/`? and `?docs/graph/`? are not written
```

  regression: ```text
inject into GCFPE-MGMT-10: Repository paths outside `docs/ephemeral/` and `docs/graph/` are not written
```

- **G-K40 R-A5** — `required_regex`, `CTR-002`, rows: GCFPE-MGMT-10

```regex
This prompt's artifacts are written only under `docs/ephemeral/` and `docs/graph/`, the controls it maintains only under `docs/prompt_ecosystem_management/`
```

  regression: ```text
in GCFPE-MGMT-10, put the retired wording back in place of the new text: Repository paths outside `docs/ephemeral/` and `docs/graph/` are not written
```

- **G-K40 R-A5** — `required_regex`, `CTR-002`, rows: PR-35

```regex
This prompt's artifacts are written only under `docs/ephemeral/` and `docs/graph/`
```

  regression: ```text
in PR-35, put the retired wording back in place of the new text: Repository paths outside `docs/ephemeral/` and `docs/graph/` are not written
```

- **G-K41 R-A3a** — `forbidden_regex`, `CTR-001`, rows: CL-20, CL-30, CL-C-10, CL-E-10, OPS-30, PR-10, PR-20, PR-30, PR-40, QA-10

```regex
Embed only applicable workflow contracts
```

  regression: ```text
inject into CL-20: Embed only applicable workflow contracts
```

- **G-K42 R-A4a** — `forbidden_regex`, `CTR-001`, rows: CL-20, CL-30, CL-40, CL-C-10, CL-E-10

```regex
These candidate URL tokens must be replaced
```

  regression: ```text
inject into CL-20: These candidate URL tokens must be replaced
```

- **G-K43 R-A4c, R-ITEM18** — `forbidden_regex`, `CTR-001`, rows: CL-40

```regex
This authoring candidate does not perform that update
```

  regression: ```text
inject into CL-40: This authoring candidate does not perform that update
```

- **G-K44 R-ITEM18** — `forbidden_regex`, `CTR-001`, rows: CL-40

```regex
\{\{CANDIDATE_CRD_LIST_URL\}\}
```

  regression: ```text
inject into CL-40: (`{{CANDIDATE_CRD_LIST_URL}}`)
```

- **G-K45 R-ITEM18** — `required_regex`, `CTR-002`, rows: CL-40

```regex
Notion page `?Candidate CRD Items List`? \(`?https://app\.notion\.com/p/[0-9a-f]{32}(?:\?pvs=\d+)?`?\)
```

  regression: ```text
in CL-40, put the retired wording back in place of the new text: Notion page `Candidate CRD Items List` (`{{CANDIDATE_CRD_LIST_URL}}`)
```

- **G-K46 R-ITEM19** — `required_regex`, `CTR-002`, rows: CL-20

```regex
when none is supplied, record the board update as pending, owned under PF04 §9\.1\.1
```

  regression: ```text
in CL-20, put the retired wording back in place of the new text: 4. Include Master Scrum's precise board-update instruction for the board.
```

- **G-K47 R-ITEM34** — `forbidden_regex`, `CTR-001`, rows: QA-110

```regex
code/Ops remediation\. Do not fix it here\.(?! This applies only before the whole approved run is complete)
```

  regression: ```text
inject into QA-110: code/Ops remediation. Do not fix it here.
```

- **G-K48 R-ITEM34** — `required_regex`, `CTR-002`, rows: QA-110

```regex
a completed failing run is `ACCEPT` and continues to QA-120
```

  regression: ```text
in QA-110, put the retired wording back in place of the new text: code/Ops remediation. Do not fix it here.
```

- **G-K49 R-ITEM35** — `forbidden_regex`, `CTR-001`, rows: QA-80

```regex
`WRONG_ROUTE_APPROVED_BASE` terminally
```

  regression: ```text
inject into QA-80: `WRONG_ROUTE_APPROVED_BASE` terminally
```

- **G-K50 R-ITEM35** — `required_regex`, `CTR-002`, rows: QA-80

```regex
routed as \*Required result and routing\* states
```

  regression: ```text
in QA-80, put the retired wording back in place of the new text: return `WRONG_ROUTE_APPROVED_BASE` terminally
```

- **G-K51 R-CLAT** — `forbidden_regex`, `CTR-001`, rows: PR-10, PR-20, PR-40, RS-10, RS-20, DOC-10, DOC-20, IA-30

```regex
Decide it during work
```

  regression: ```text
inject into PR-10: **Decide it during work:**
```

- **G-K52 R-A2-CL30 (LCL-30-2, P-18)** — `forbidden_regex`, `TOP-001`, rows: CL-30

```regex
decision lineage; existing ADR/conflict history
```

  regression: ```text
inject into CL-30: decision lineage; existing ADR/conflict history
```

- **G-K53 R-26-RSP (P-38)** — `forbidden_regex`, `TOP-001`, rows: PR-40

```regex
RESCOPE_PROPOSAL_ID and complete RESCOPE_PROPOSAL\b
```

  regression: ```text
inject into PR-40: RESCOPE_PROPOSAL_ID and complete RESCOPE_PROPOSAL
```

- **G-K54 LOPS-30-1, LQA-10-P19 (P-19, P-42)** — `forbidden_regex`, `TOP-001`, rows: OPS-30, QA-10

```regex
A saved attachment, link or scattered fields do not replace the handoff\.
```

  regression: ```text
inject into OPS-30: A saved attachment, link or scattered fields do not replace the handoff.
```

- **G-K55 LPR-30-2 (P-55)** — `forbidden_regex`, `TOP-001`, rows: PR-30

```regex
outside the approved Plan, return the metadata\b
```

  regression: ```text
inject into PR-30: If that path is outside the approved Plan, return the metadata
```

- **PART-17 ITEM-36 (replaces the \A{0,7} window guard in place, same list position)** — `forbidden_regex`, `SRC-001`, rows: ALL55 (every row)

```regex
(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Prompt [Vv]ersion(?:\*\*|__|`){0,2}[ \t]*:
```

  regression: ```text
inject into CL-20: **`Prompt version`**: 3.3.1
```

- **PART-17 ITEM-36 (replaces the \A{0,7} window guard in place, same list position)** — `forbidden_regex`, `INV-003`, rows: ALL55 (every row)

```regex
(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Ecosystem release(?:\*\*|__|`){0,2}[ \t]*:
```

  regression: ```text
inject into CL-20: **Ecosystem release:** GCFPE-20260914.1
```

- **PART-17 ITEM-36 (replaces the \A{0,7} window guard in place, same list position)** — `forbidden_regex`, `SRC-001`, rows: ALL55 (every row)

```regex
(?m)^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?Set(?:\*\*|__|`){0,2}[ \t]*:
```

  regression: ```text
inject into CL-20: 3. **`Set`**: 091426.1
```

- **R-CLAT (PART-18, ITEM-37): required removed** — other: none needed: the forbidden twin G-K51 carries the regression; the Material required regex stays on all 10 rows and PR-30/PR-35 keep the required decide pattern

- **PR-40 inputs (P-01)** — other: not an assertion: the PR_REFS input follows LPR-40-4, and P-01's sentence becomes its own input entry before W-4 (LPR-40-5)

- **CL-40 mutations.allowed (PART-06)** — other: not an assertion: one allowed entry names the Candidate CRD Items List page write

- **ITEM-07 (PART-03)** — other: none: a governance-audit behavioral-fixture prose line, not a registry row; §A lists ITEM-07 as unguarded (D24 review holds it)

- **R-ITEM38 (PART-15)** — other: not placed: §A lists ITEM-38 as unguarded (a typo with no behaviour); the regex is the drafter's readback check only

- **R-ITEM23, R-ITEM40 (PART-11)** — other: not placed: the proposed body has no registry row; the PART-11 gate runs R-ITEM40's pattern and then R-ITEM23's (this one) directly

### 4.3 Other registry changes

- **PART-10 (ITEM-22):** 16 lane `notion_parent_id` and 55 row `expected_parent_id` values, and 70 titles, name each prompt's actual 091426.1 parent page. No old ID remains.
- **PR-40 inputs:** the `PR_REFS` entry takes LPR-40-4's text, and P-01's sentence is a new entry before the W-4 entry, as LPR-40-5 places it in the body.
- **CL-40 `mutations`:** the *Candidate CRD Items List* page write is allowed (D25-A).
- **PART-18:** the required *Decide it during work* leaves the eight rows; G-K51 forbids it there.

### 4.4 NAM-002 on a live snapshot

PART-10 (ITEM-22): NAM-002, lane parents and parent titles on a live snapshot, EXECUTE procedure

When: X3.6 (spec §9), after the registry commit (X3.1) and before any Notion write (P-77). A failure here stops
EXECUTE with nothing outside the branch (P-84 revised). Nothing is written to Notion and no prompt body is read: a hub page is a control page, and its child list
gives page IDs and titles only. `nam002_live.py` runs three checks from one `childlist.json` (its docstring states them):

- NAM-002 (the governance audit's own rule): each row's page is listed under the hub its `expected_parent_id` names.
- Lane parents (P-63): each of the 16 lanes' `notion_parent_id` is the one hub that holds that lane's rows.
- Parent titles (P-63): each of the 70 parent titles (16 lane `notion_parent_title`, 54 row `expected_parent_title`;
  PR-35 has none) equals the fetched title of the hub it refers to. Findings are one per hub, so one wrong hub title is
  exactly one finding.

1. Fetch the six 091426.1 hub pages with `notion-fetch`, each by ID. From each fetch record the page title, the as-of
   timestamp, and the direct child pages it lists (child page ID, 32 hex undashed, and child title):

   | hub id | expected title | lanes | rows expected under it |
   |---|---|---|---|
   | `3db4590a05eb81d59059eb6b95ed5fcf` | HDE Change Flow — GCFPE-20260914.1 — 091426.1 | CF-PO, CF-C, CF-E, CL-C, CL-E, CL, MGR | 18: CF-C-10, CF-C-20, CF-C-30, CF-C-40, CF-E-10, CF-E-20, CF-E-30, CF-E-40, CF-PO-10, CL-20, CL-30, CL-40, CL-C-10, CL-E-10, CL-E-20, CL-E-30, CL-E-40, MGR-10 |
   | `3db4590a05eb8195a2ccf7c0959a8b6e` | HDE IA — GCFPE-20260914.1 — 091426.1 | DOC, IA, OPS, PR, RS | 21: DOC-10, DOC-20, IA-10, IA-20, IA-30, IA-40, IA-50, IA-60, OPS-10, OPS-20, OPS-30, PR-10, PR-20, PR-30, PR-35, PR-40, PR-50, RS-10, RS-20, RS-30, RS-40 |
   | `3db4590a05eb814d96d3dcfa8835f96d` | HDE QA — GCFPE-20260914.1 — 091426.1 | QA | 10: QA-10, QA-100, QA-110, QA-120, QA-20, QA-50, QA-60, QA-70, QA-80, QA-90 |
   | `3db4590a05eb81cd938de84cfffead9c` | Escalation — GCFPE-20260914.1 — 091426.1 | ESC | 4: ESC-10, ESC-25, ESC-30, ESC-40 |
   | `3db4590a05eb811b9c14f2ae89c28df7` | HDE TW — GCFPE-20260914.1 — 091426.1 | UTIL | 1: UTIL-10 |
   | `3db4590a05eb81de9736ea69bac61016` | Glow HDE Prompt Flow Index — GCFPE-20260914.1 — 091426.1 | GCFPE-MGMT | 1: GCFPE-MGMT-10 |

2. Right after the six fetches, build `$SCRATCH/nam002/childlist.json` with the committed helper (P-101), which reads
   each hub's newest fetch in this session and copies nothing by hand:
   `python3 $EV/engine/ctrl.py children 3db4590a05eb81d59059eb6b95ed5fcf 3db4590a05eb8195a2ccf7c0959a8b6e 3db4590a05eb814d96d3dcfa8835f96d 3db4590a05eb81cd938de84cfffead9c 3db4590a05eb811b9c14f2ae89c28df7 3db4590a05eb81de9736ea69bac61016 > $SCRATCH/nam002/childlist.json`
   It writes the shape the script documents; every hub carries its fetched `title` (a hub without one is unusable
   input, exit 2). It keeps every child; a child that is not a registry row does not enter the snapshot:
   `{"captured_at": "<UTC>", "hubs": [{"id": "<hub id>", "title": "<fetched page title>", "fetched": "<as-of>", "children": [{"id": "<page id>", "title": "<child title>"}]}]}`
3. Obtain the pre-change registry for the control run from `$BASE`, the `main` commit X0.2 restarted the branch from
   and recorded (it carries the merged record PR; X0.3(a) checked its registry). Stop if the hash differs:

   ```sh
   git show $BASE:docs/prompt_ecosystem_management/project-prompt-contract-registry.md > $SCRATCH/reg-old.md
   sha256sum $SCRATCH/reg-old.md   # 8b4e46ed2dc24442e3dadc416dfe4c810a048788bf03c799808927a54c2677d4, 322556 bytes
   ```

4. Run the four checks. Each run's JSON goes to a file by redirection, not a pipe, so `$?` is the script's own status.
   `--audit-root` is required at EXECUTE: `EV/registry/` carries no copy of the audit scripts.

   ```sh
   export PYTHONDONTWRITEBYTECODE=1 TMPDIR=$SCRATCH/tmp
   EV=docs/ephemeral/modifications/evidence/closeout-residuals/plan
   AUD=$INST/amthor-workspace-governance-audit
   REG=docs/prompt_ecosystem_management/project-prompt-contract-registry.md   # the working tree after X3.1: sha256 97bda1a0…
   CL=$SCRATCH/nam002/childlist.json
   python3 $EV/registry/nam002_live.py $REG $CL --audit-root $AUD --snapshot-out $SCRATCH/nam002/snapshot.json > $SCRATCH/nam002/run1-committed.json; echo "exit $?"
   python3 $EV/registry/nam002_live.py $REG $CL --audit-root $AUD --inject ESC-10=3db4590a05eb81d59059eb6b95ed5fcf > $SCRATCH/nam002/run2-inject-parent.json; echo "exit $?"
   python3 $EV/registry/nam002_live.py $REG $CL --audit-root $AUD --inject-title 3db4590a05eb81cd938de84cfffead9c=Escalation > $SCRATCH/nam002/run3-inject-title.json; echo "exit $?"
   python3 $EV/registry/nam002_live.py $SCRATCH/reg-old.md $CL --audit-root $AUD > $SCRATCH/nam002/run4-control-old.json; echo "exit $?"
   ```

   Expected (each from the run's `summary` and `expectation_met`; any other result stops PART-10):

   | run | expected summary | `expectation_met` | exit |
   |---|---|---|---|
   | 1, the committed registry | NAM-002 0 over 55 sources; no unplaced row; `other_errors` 0; `lane_parent_findings` 0; `title_findings` 0; `title_references` {compared 70, mismatched 0} | true | 0 |
   | 2, `--inject ESC-10=<Change Flow hub>` (a real hub, the wrong one for ITEM-22's source row) | exactly one NAM-002, on ESC-10 | true | 0 |
   | 3, `--inject-title <Escalation hub>=Escalation` (the hub's pre-091426.1 title) | exactly one title finding, on hub `3db4590a05eb81cd938de84cfffead9c`; `title_references.mismatched` 5 (its lane and 4 rows) | true | 0 |
   | 4, control: the old registry `8b4e46ed…` | NAM-002 55; `lane_parent_findings` 16; `title_findings` 6 (every hub); `title_references` {compared 70, mismatched 70} | false | 1 |

   NAM-001 (a WARNING on a prompt-title difference) is recorded and does not fail the gate: prompt titles are outside
   PART-10. Runs 2 and 3 are must-fail cases: each checks only its own injected finding, and each passes only when
   that one finding is produced; run 1 must pass first. Runs 2 and 3 cannot be combined (argparse exits 2).
5. Copy `childlist.json`, the snapshot and the four results to `docs/ephemeral/modifications/evidence/closeout-residuals/execute/nam002/`
   (hub and child IDs and titles only; P-83), with each run's exit status; they are committed and pushed at X3.6 (P-87).
   A result other than the table above stops EXECUTE before any Notion write (P-84 revised).

How the script reads the snapshot: `build_snapshot()` makes one source per registry row, `{"source_id": <row
notion_page_id>, "kind": "notion_page", "complete": true, "in_scope": true, "title": <child title>, "parent": <hub id>}`.
No source has a `path`, so `_read_snapshot_text` returns None: no text is read, no assertion and no SRC-003 runs.
`audit_governance()` compares `parent` with `expected_parent_id` as a plain string (installed
`audit_workspace_governance.py:604-605`; r1 final copy `:620-621`). A registry page found under no hub is left out
(the audit then raises INV-001, and the run reports it as unplaced); a page listed under two hubs stops the run. The
lane-parent and title checks read the same child lists and the registry fields only.

PLAN prototype (`guard_tests.py` T7, and the CLI runs in `nam002_proof/`): the child list is built in memory from the new
registry's own parent IDs and titles (`nam002_proof/make_childlist.py`; equal to the ANALYZE parent map), so it is
circular by construction. Results, as NAM-002 / lane-parent / title findings / mismatched title references:
- old registry: 55 / 16 / 6 / 70 of 70
- new registry: 0 / 0 / 0 / 0 of 70
- new registry, ESC-10 parent injected wrong: 1 / 0 / 0 / 0 of 70; NAM-002 rows ['ESC-10']
- new registry, Escalation hub title injected wrong: 0 / 0 / 1 / 5 of 70; title hubs ['3db4590a05eb81cd938de84cfffead9c']
- `expectation_met`: {"new": true, "inject ESC-10": true, "inject-title Escalation hub": true, "old (control, expected false)": false}; T7 = True.
- Command line (`nam002_proof/run_cli.py` -> `cli_matrix.json`, ALL_OK = True): the four runs with each of three
  audit roots (the byte-identical `wga_scripts` copy, the installed audit, the r1 final copy) give, as exit / NAM-002 /
  lane-parent / title findings: 1 committed (new) 0/0/0/0; 2 inject parent ESC-10 0/1/0/0; 3 inject title Escalation hub 0/0/0/1; 4 control (old) 1/55/16/6. Unusable input exits 2: inject-title on a non-hub id (2), inject-title equal to the fetched title (2), --inject with --inject-title (2), a hub without its title (2), missing child-list file (2).
PLAN live run (repair round 6, P-101; `nam002_live_plan/`): the six hubs were fetched live and the child list built by
`ctrl.py children` (2026-09-24T04:10:57Z; HDE Change Flow 19, HDE IA 21, HDE QA 10, Escalation 4, HDE TW 2, Glow HDE Prompt Flow Index 4 children). Steps 3 and 4 then ran on it with the PLAN copy of the new registry (runs 1 to 3) and the pre-change
registry `8b4e46ed…` (run 4). As NAM-002 / lane-parent / title findings / mismatched title references, expectation_met: run1 0 / 0 / 0 / 0 of 70, True; run2 1 / 0 / 0 / 0 of 70, True; run3 0 / 0 / 1 / 5 of 70, True; run4 55 / 16 / 6 / 70 of 70, False: the table above, on live hubs.
Non-prompt findings from the minimal run manifest and workspace registry (COL-002, SRC-001) are not prompt findings and do not enter the gate.



## §5 Skill packages

### 5.1 Packages

One install event for all seven (§A order 3). Each diff was proved by a round trip: `patch -p1` on a copy of the installed package gives the final package exactly.

| package | revision | installed freeze | final freeze | files changed / added |
|---|---|---|---|---|
| flowmaster-validate | 3.3.0 → 3.3.1 | `31 a79401deaabe35ce…` | `31 0ca2a74d50a57803…` | 8 / 0 |
| change-flow | 3.3.0 → 3.3.1 | `22 ee546df57f3d5f0f…` | `22 9a551af36e042e56…` | 3 / 0 |
| glow-graph-contract | none advertised (D19: freeze digest) | `6 4e671ddc935b629f…` | `9 e241bb9a67c44708…` | 2 / 3 |
| session-relay-flowmaster | 3.1.0 → 3.2.0 | `5 15aef9890ebfa286…` | `5 c8a5b22432a44f57…` | 3 / 0 |
| glow-hde-pr-development | 1.3.0 → 1.3.1 | `4 68077fa662099299…` | `4 265f9170d8459fc4…` | 2 / 0 |
| amthor-workspace-governance-audit | 1.12.0 → 1.13.0 | `15 819915e4a57184fd…` | `15 c214e8741e9c54d3…` | 8 / 0 |
| glow-po-reporting | none advertised (D19: freeze digest) | `1 3221ae8de6f6500d…` | `1 7e04368a63e40c99…` | 1 / 0 |

The contract `gcfpe-20260914.1-091426.1-direct-handoff-contract.json` goes 4.1.0 → 4.1.1 (`6902924a…` → `dbae180b…`) in both bundled copies. The two structural differences are `.contract_revision` and `.pr_development_contract.primary_skill_revision` (1.3.0 → 1.3.1). `SKILL_TREE_SHA256` is re-declared last (`ed52208f…`). `validator_revision` is 3.3.1 at all four sites (P-22).

### 5.2 Edits by package and item

| package | item | edits |
|---|---|---|
| amthor-workspace-governance-audit | ITEM-05 | 12 |
| amthor-workspace-governance-audit | ITEM-07 | 1 |
| amthor-workspace-governance-audit | ITEM-16 | 2 |
| amthor-workspace-governance-audit | ITEM-39 | 3 |
| amthor-workspace-governance-audit | REVISION | 2 |
| change-flow | ITEM-06, ITEM-16 | 1 |
| change-flow | ITEM-08 | 1 |
| change-flow | ITEM-09 | 1 |
| change-flow | ITEM-10 | 1 |
| change-flow | ITEM-39 | 2 |
| change-flow | ITEM-39, ITEM-16 | 1 |
| change-flow | PART-01 | 1 |
| change-flow | REVISION | 2 |
| change-flow | RULING-5-Q3-A (:1017-1018) | 1 |
| flowmaster-validate | ITEM-03, ITEM-36 | 1 |
| flowmaster-validate | ITEM-04 | 8 |
| flowmaster-validate | ITEM-11 | 3 |
| flowmaster-validate | ITEM-15 | 5 |
| flowmaster-validate | ITEM-16 | 3 |
| flowmaster-validate | ITEM-16, ITEM-02, ITEM-06, ITEM-14 | 1 |
| flowmaster-validate | ITEM-16, ITEM-06 | 1 |
| flowmaster-validate | ITEM-16, REVISION | 2 |
| flowmaster-validate | ITEM-36 | 2 |
| flowmaster-validate | ITEM-36, P-16 | 1 |
| flowmaster-validate | ITEM-39 | 2 |
| flowmaster-validate | PART-01 | 6 |
| flowmaster-validate | REVISION | 7 |
| flowmaster-validate | RULING-5-Q3-A (:1900-1909 ALPH | 1 |
| flowmaster-validate | RULING-5-Q3-A (:1909 code) | 1 |
| flowmaster-validate | RULING-5-Q3-A (:1916 code) | 1 |
| flowmaster-validate | RULING-5-Q3-A (:492 fixture ex | 1 |
| flowmaster-validate | RULING-5-Q3-A (SKILL.md:384) | 1 |
| glow-graph-contract | ITEM-09 | 3 |
| glow-graph-contract | ITEM-09, ITEM-12 | 2 |
| glow-graph-contract | ITEM-09, ITEM-13 | 1 |
| glow-graph-contract | ITEM-12 | 5 |
| glow-graph-contract | ITEM-12, ITEM-13 | 1 |
| glow-graph-contract | ITEM-13 | 1 |
| glow-graph-contract | ITEM-25 | 1 |
| glow-hde-pr-development | ITEM-01 | 2 |
| glow-hde-pr-development | REVISION | 2 |
| glow-po-reporting | ITEM-24 | 1 |
| session-relay-flowmaster | ITEM-02 | 3 |
| session-relay-flowmaster | ITEM-06 | 2 |
| session-relay-flowmaster | ITEM-08 | 1 |
| session-relay-flowmaster | ITEM-14 | 9 |
| session-relay-flowmaster | REVISION | 1 |

The old and new text of every edit is in `EV/skills/diffs/`.

### 5.3 The suite gate (`EV/skills/run_gate.py`, P-60)

Each set embeds its expected results and exits 0 only when every row equals them. The rows re-express `EV/skills/results/suites_final.json` on EXECUTE paths. The manifest's commands were run in §9 order on a fresh copy of the repository (`EV/skills/results/gate_proof_x.json`, §8.6).

| set | when | rows | proof run |
|---|---|---|---|
| `pre` | X1.3, once, on the unchanged working tree before commit 1 and the reindex | 12 | exit 0; 12/12 ok |
| `pkg` | X4.2, after commit 1 (X2), the registry, the reindex, the contract-template move, P32-SWR (X3) and the contract regeneration (X4.1) | 34 | exit 0; 34/34 ok |
| `post` | X7.4, after the install sitting, on main with the execution PR merged | 28 | exit 0; 28/28 ok |

**`pre` rows:** `freeze_recipe.sha256`, `freeze.skills_root`, `freeze.flowmaster-validate`, `freeze.change-flow`, `freeze.glow-graph-contract`, `freeze.session-relay-flowmaster`, `freeze.glow-hde-pr-development`, `freeze.amthor-workspace-governance-audit`, `freeze.glow-po-reporting`, `parts.freeze`, `graph_parts.build.pre_reindex_working_tree`, `freeze.skills_root.after`

**`pkg` rows:** `freeze_recipe.sha256`, `freeze.skills_root`, `freeze.flowmaster-validate`, `freeze.change-flow`, `freeze.glow-graph-contract`, `freeze.session-relay-flowmaster`, `freeze.glow-hde-pr-development`, `freeze.amthor-workspace-governance-audit`, `freeze.glow-po-reporting`, `candidate_root`, `validate_flowmaster.default`, `validate_flowmaster.candidate`, `run_change_flow_fixtures`, `run_gcfpe_current_fixtures.default`, `run_gcfpe_current_fixtures.historical_alias`, `run_gcfpe_20260914_fixtures`, `validate_gcfpe_20260914.candidate_root`, `validate_gcfpe_20260914.no_root`, `validate_gcfpe_current`, `change_flow_own_validator`, `relay_self_test`, `pr_skill_validator`, `governance_audit_run_fixture_suite`, `parts.freeze`, `graph_parts.build.repo_parts`, `graph_parts.reindex.copy_idempotent`, `registry_deriver.patched_audit.repo_parts`, `parts_pre_reindex.git_archive`, `parts_pre_reindex.freeze`, `graph_parts.build.pre_reindex_parts`, `registry_deriver.patched_audit.pre_reindex_parts`, `registry_deriver.installed_audit_1.12.0.repo_parts`, `registry_deriver.installed_audit_1.12.0.pre_reindex_parts`, `freeze.skills_root.after`

**`post` rows:** `freeze_recipe.sha256`, `freeze.skills_root`, `freeze.flowmaster-validate`, `freeze.change-flow`, `freeze.glow-graph-contract`, `freeze.session-relay-flowmaster`, `freeze.glow-hde-pr-development`, `freeze.amthor-workspace-governance-audit`, `freeze.glow-po-reporting`, `candidate_root`, `validate_flowmaster.default`, `validate_flowmaster.candidate`, `run_change_flow_fixtures`, `run_gcfpe_current_fixtures.default`, `run_gcfpe_current_fixtures.historical_alias`, `run_gcfpe_20260914_fixtures`, `validate_gcfpe_20260914.candidate_root`, `validate_gcfpe_20260914.no_root`, `validate_gcfpe_current`, `change_flow_own_validator`, `relay_self_test`, `pr_skill_validator`, `governance_audit_run_fixture_suite`, `parts.freeze`, `graph_parts.build.repo_parts`, `graph_parts.reindex.copy_idempotent`, `registry_deriver.patched_audit.repo_parts`, `freeze.skills_root.after`

The build of today's parts with the new builder fails on purpose (7 bookkeeping errors) until X3.2's reindex; the `pre` set asserts exactly that. Every must-fail regression also fires (`EV/skills/results/regress_final_*.json`): regress_plan 36/36, function-level 20/20, the four-package set 33/33, change-flow's own 11/11 (P-25).

### 5.4 The EXECUTE commands

````json
{
 "variables": {
  "cwd": "the repository root; every relative path below is relative to it",
  "ENV": "export PYTHONDONTWRITEBYTECODE=1 TMPDIR=$SCRATCH/tmp (mkdir -p $SCRATCH/tmp first)",
  "EV": "docs/ephemeral/modifications/evidence/closeout-residuals/plan",
  "EX": "docs/ephemeral/modifications/evidence/closeout-residuals/execute: EXECUTE's evidence (P-83, P-87); EX/run.json holds $BASE, the root digests, the page id and the token values (P-96)",
  "INST": "/root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502",
  "SCRATCH": "the executing session's scratchpad directory; never the repository or a skill",
  "PKG": "$SCRATCH/pkg-root: a full copy of $INST with the seven packages replaced by their patched copies (execute.1.then); freeze.py $PKG is recorded (it is 323 047ca74293082dd1d824c1e74f2aef17945bea1f609f365afcc31106b4de00ae when no skill outside the seven has changed since PLAN; P-79)",
  "GGC, FV, CF, RELAY, PR, AUDIT, REPORT": "$PKG/glow-graph-contract, $PKG/flowmaster-validate, $PKG/change-flow, $PKG/session-relay-flowmaster, $PKG/glow-hde-pr-development, $PKG/amthor-workspace-governance-audit, $PKG/glow-po-reporting",
  "GATE": "$SCRATCH/gate: run_gate.py's --out; it builds the candidate root at $GATE/cand (graph/GCFPE-20260914.1-Candidate-Graph-Contract.json = $CF/references/gcfpe-20260914.1-091426.1-candidate-graph-contract.json, byte-equal to the graph bundled in $FV)",
  "FVI, CFI": "$INST/flowmaster-validate, $INST/change-flow (installed, before the install sitting)",
  "BASE": "the main commit X0.2 restarts the branch from: BASE=$(git rev-parse HEAD) right after the checkout, written to EX/run.json as \"base\" at X0.2 and read from there by every later step and session (P-87, P-102 (i)); GUARDS.md NAM-002 step 3 reads the pre-change registry from it"
 },
 "1_base_unchanged_before_applying": {
  "commands": [
   "python3 docs/prompt_ecosystem_management/freeze.py $INST/flowmaster-validate",
   "python3 docs/prompt_ecosystem_management/freeze.py $INST/change-flow",
   "python3 docs/prompt_ecosystem_management/freeze.py $INST/glow-graph-contract",
   "python3 docs/prompt_ecosystem_management/freeze.py $INST/session-relay-flowmaster",
   "python3 docs/prompt_ecosystem_management/freeze.py $INST/glow-hde-pr-development",
   "python3 docs/prompt_ecosystem_management/freeze.py $INST/amthor-workspace-governance-audit",
   "python3 docs/prompt_ecosystem_management/freeze.py $INST/glow-po-reporting"
  ],
  "expected_stdout": {
   "flowmaster-validate": "31 a79401deaabe35ce1393d91e8d333e86c26a71500b3c5abd89ff5fdbaa7f8f48",
   "change-flow": "22 ee546df57f3d5f0f0dc29c514376e64ca0fa830fe03e64ff7acd8645648bcb73",
   "glow-graph-contract": "6 4e671ddc935b629f7285baeb42b93c9848b19fdeb1be39ebfcaa35c2d171f1b8",
   "session-relay-flowmaster": "5 15aef9890ebfa286bf56272e64cc9880d6dc57701d4e8b45e15fa6f45c3f2121",
   "glow-hde-pr-development": "4 68077fa6620992997c8bb3949b1135ba47b1c5bd275610eb49c3b7d8d04ecf22",
   "amthor-workspace-governance-audit": "15 819915e4a57184fd3af0c783f13e102892eb7182d0c951727869655d11ae078d",
   "glow-po-reporting": "1 3221ae8de6f6500d27154ed0e77c0241e1679999ce42a953a9f6fad4515a0464"
  },
  "whole_root": {
   "command": "python3 docs/prompt_ecosystem_management/freeze.py $INST",
   "expected_stdout_at_plan_time": "320 420705ec2881bdd82cc46d32880fa02abb463460f081dfa728c3c4aca928f24a",
   "note": "the whole root also covers the 19 skills outside the seven packages; any sync of them changes it",
   "when": "X0.3(e): recorded, not a stop. A value other than expected_stdout_at_plan_time means a skill outside the seven synced since PLAN; \u00a7E records it (P-79)"
  },
  "then": {
   "when": "X1.1 (spec \u00a79), before any repository change (P-56): the reindex needs $GGC, the registry gate needs its deriver. A new session rebuilds $PKG with it only at a step before X7.3: from X7.3 on $INST already holds the patched packages and the patches would not apply (P-101)",
   "commands": [
    "mkdir -p \"${SCRATCH:?}/tmp\" && rm -rf \"${PKG:?}\" && cp -r \"${INST:?}\" \"$PKG\"",
    "(for s in flowmaster-validate change-flow glow-graph-contract session-relay-flowmaster glow-hde-pr-development amthor-workspace-governance-audit glow-po-reporting; do rm -rf \"${PKG:?}/${s:?}\" && cp -r $INST/$s $PKG/$s && patch -p1 -s -d $PKG/$s < $EV/skills/diffs/$s.diff || { echo \"PATCH FAILED: $s\"; exit 1; }; done)",
    "python3 docs/prompt_ecosystem_management/freeze.py $PKG/flowmaster-validate",
    "python3 docs/prompt_ecosystem_management/freeze.py $PKG/change-flow",
    "python3 docs/prompt_ecosystem_management/freeze.py $PKG/glow-graph-contract",
    "python3 docs/prompt_ecosystem_management/freeze.py $PKG/session-relay-flowmaster",
    "python3 docs/prompt_ecosystem_management/freeze.py $PKG/glow-hde-pr-development",
    "python3 docs/prompt_ecosystem_management/freeze.py $PKG/amthor-workspace-governance-audit",
    "python3 docs/prompt_ecosystem_management/freeze.py $PKG/glow-po-reporting",
    "python3 docs/prompt_ecosystem_management/freeze.py $PKG"
   ],
   "expected": [
    "exit 0",
    "exit 0: every patch exits 0 (the subshell exits 1 and names the package at the first failure)",
    "31 0ca2a74d50a57803e2c4b8426a84f43877f68f6d1c93731d54368f413e5c5626",
    "22 9a551af36e042e56a48045297ac316b4102a4eb21f31622853c8be700e223f47",
    "9 e241bb9a67c4470895fc666a25d0f97d8df7e8e2df06539de5deaf12bc46467c",
    "5 c8a5b22432a44f57fb12bc508169f85aa3d0ca3298b793590c364eb9a2afc8e4",
    "4 265f9170d8459fc477287c320f0bbdd8eaaf0e6ba1dd4ee513275a76a22f8f7a",
    "15 c214e8741e9c54d395cfbd1379cbc7947e6c07beee5bd03aca433dc5dda937ab",
    "1 7e04368a63e40c99e31ede3eda9ba88cfbbb9915a48b46cdc39027da7cef68e1",
    "recorded (P-79): 323 047ca74293082dd1d824c1e74f2aef17945bea1f609f365afcc31106b4de00ae (final_root_freeze) when no skill outside the seven has changed since PLAN; any other value is recorded in \u00a7E and is not a stop, because only the seven package digests above are this Modification's"
   ]
  },
  "expected_after_patch": {
   "flowmaster-validate": "31 0ca2a74d50a57803e2c4b8426a84f43877f68f6d1c93731d54368f413e5c5626",
   "change-flow": "22 9a551af36e042e56a48045297ac316b4102a4eb21f31622853c8be700e223f47",
   "glow-graph-contract": "9 e241bb9a67c4470895fc666a25d0f97d8df7e8e2df06539de5deaf12bc46467c",
   "session-relay-flowmaster": "5 c8a5b22432a44f57fb12bc508169f85aa3d0ca3298b793590c364eb9a2afc8e4",
   "glow-hde-pr-development": "4 265f9170d8459fc477287c320f0bbdd8eaaf0e6ba1dd4ee513275a76a22f8f7a",
   "amthor-workspace-governance-audit": "15 c214e8741e9c54d395cfbd1379cbc7947e6c07beee5bd03aca433dc5dda937ab",
   "glow-po-reporting": "1 7e04368a63e40c99e31ede3eda9ba88cfbbb9915a48b46cdc39027da7cef68e1"
  },
  "when": "X0.3 (spec \u00a79), before any repository change"
 },
 "2_graph_reindex_ITEM-12_repository_in_execution_PR_before_install": {
  "commands": [
   "python3 docs/prompt_ecosystem_management/freeze.py docs/graph/parts",
   "python3 $GGC/scripts/graph_parts.py reindex docs/graph/parts",
   "git diff --stat docs/graph/parts",
   "git diff --no-color docs/graph/parts | grep -v -e '^diff --git' -e '^index ' | cmp - $EV/skills/results/parts_reindex.repo.diff",
   "python3 docs/prompt_ecosystem_management/freeze.py docs/graph/parts",
   "python3 $GGC/scripts/graph_parts.py build docs/graph/parts $SCRATCH/graph.md",
   "python3 $GGC/scripts/graph_parts.py reindex docs/graph/parts"
  ],
  "expected": [
   "56 980af73e656e20740663ae1dbfa8780eff61b41e2f754c5719c743e4647cae50 (today's parts, HEAD 705568e)",
   "exit 0; 'reindex: 229 edges; 27 file(s) rewritten' and the 27 names (global.json + 26 prompt parts)",
   "27 files changed, 107 insertions(+), 113 deletions(-); only edge_indices / _other_edge_indices change (results/parts_reindex.json holds the from/to table)",
   "exit 0 (cmp prints nothing): the reindex diff, less its 27 'diff --git' and 27 'index' header lines, is byte-identical to the stored diff (sha256 b37fc1d7b79e0f4f88f9a1ae000e6e30123ea57782885171dd739b19e98ddb7b, 6296 B). Run it before staging docs/graph/parts",
   "56 84dbb1fe5e7566b871ddc436bcbc875a772dcc695be221d2b4d45a18a470027f (the reindexed parts)",
   "exit 0; 'build: 55 nodes, 229 edges, 55 state_routes'; 'embedded JSON 575074 bytes  sha256 ae2bd159f0ba947c2e470f96579fadfbf060f74423aa974ae1194ac16bb2484d'; graph.md 575672 B sha256 a70a93263f2943be45450a210f62a82a2a27abfd49a259d04f838e469ba0cc24",
   "exit 0; 'reindex: 229 edges; 0 file(s) rewritten' (idempotent)"
  ],
  "read_only_cross_check": "git apply --check $EV/skills/results/parts_reindex.repo.diff exits 0 before the reindex; git apply --check -R $EV/skills/results/parts_reindex.repo.diff exits 0 after it",
  "note": "$GGC is the patched package in $PKG (execute.1.then, run first); the installed builder has no reindex and passes today's parts. The cmp check reads the unstaged working tree, so it runs before `git add`",
  "when": "X3.2 (spec \u00a79): after commit 1 (X2.2) and the registry commit (X3.1); the pre gate ran at X1.3 on the unchanged tree"
 },
 "3_contract_template_move_ITEM-13_repository_in_execution_PR": {
  "commands": [
   "sha256sum docs/ephemeral/modifications/evidence/pre-e2-contract/gcfpe-20260914.1-091426.1-direct-handoff-contract-4.0.6.json",
   "mkdir -p docs/graph/contract-template",
   "git mv docs/ephemeral/modifications/evidence/pre-e2-contract/gcfpe-20260914.1-091426.1-direct-handoff-contract-4.0.6.json docs/graph/contract-template/gcfpe-20260914.1-091426.1-direct-handoff-contract-4.0.6.json",
   "git rm docs/ephemeral/modifications/evidence/pre-e2-contract/README.md",
   "cp $EV/skills/contract-template-README.md docs/graph/contract-template/README.md",
   "git add docs/graph/contract-template/README.md",
   "sha256sum docs/graph/contract-template/gcfpe-20260914.1-091426.1-direct-handoff-contract-4.0.6.json docs/graph/contract-template/README.md"
  ],
  "expected": [
   "2b78f877e7a31efb2da8488d7f129794e60bcbdbf9f43e9851a319f83f06b53b, 606657 B",
   "exit 0 (docs/graph/contract-template/ exists; without it git mv exits 128)",
   "exit 0; rename, bytes unchanged",
   "exit 0; the old README (839 B, sha256 995399d40b11f94b03058283059e78885bf2d5613769aa96c826f512850c7e2f) is removed and docs/ephemeral/modifications/evidence/pre-e2-contract/ no longer exists",
   "exit 0; new README 1158 B",
   "exit 0; the README is staged",
   "2b78f877e7a31efb2da8488d7f129794e60bcbdbf9f43e9851a319f83f06b53b; 469e2265640439b0b126379c358aa7e862638c77240b2f0c6b52de8c5ba60fde"
  ],
  "note": "evidence/regenerate_contract.py and evidence/repair-a4/contract_recipe.py stay as dated records (drafter's recommendation, AUTH-001); the maintained copies are the glow-graph-contract scripts",
  "when": "X3.3 (spec \u00a79)"
 },
 "4_contract_regeneration_PART-01_after_steps_2_3_and_the_decision_record_commit": {
  "commands": [
   "python3 $GGC/scripts/graph_parts.py build docs/graph/parts $SCRATCH/graph.md",
   "python3 $GGC/scripts/contract_recipe.py $SCRATCH/graph.md docs/graph/contract-template/gcfpe-20260914.1-091426.1-direct-handoff-contract-4.0.6.json $FV/references/glow-hde-canonical-change-flow-r1-20260923.json docs/prompt_ecosystem_management/gcfpe.decision-record.md $SCRATCH/contract-4.1.0.json --contract-revision 4.1.0 --primary-skill-revision 1.3.0 --check $CFI/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json $FVI/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json",
   "python3 $GGC/scripts/contract_recipe.py $SCRATCH/graph.md docs/graph/contract-template/gcfpe-20260914.1-091426.1-direct-handoff-contract-4.0.6.json $FV/references/glow-hde-canonical-change-flow-r1-20260923.json docs/prompt_ecosystem_management/gcfpe.decision-record.md $SCRATCH/contract-4.1.1.json --contract-revision 4.1.1 --primary-skill-revision 1.3.1 --check $CF/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json $FV/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json",
   "diff $SCRATCH/contract-4.1.0.json $SCRATCH/contract-4.1.1.json",
   "python3 -c \"import sys,pathlib; sys.path.insert(0,'$FV/scripts'); import validate_gcfpe_20260914 as v; print(v.skill_tree_digest(pathlib.Path('$FV')))\""
  ],
  "expected": [
   "exit 0; embedded JSON 575074 B sha256 ae2bd159\u2026; graph.md 575672 B sha256 a70a93263f2943be45450a210f62a82a2a27abfd49a259d04f838e469ba0cc24",
   "E2 7a7fd0285730622217cc2e2d117552a002f57f9e391eac1c3d94b553fabbb675 613162; recipe 6902924a2de7f3d348e75951fd5562632bcb690e3c4687c473695261b70f3718 613326; EQUAL x2; exit 0",
   "E2 5ad52062133068fa5947eb512a52ddc72bd4791f65faa27444af3357495c03b2 613162; recipe dbae180bb5c2f73e3f27a46601bfb5cbe7321e5431dbaba8763b1a576cd9343c 613326; EQUAL x2 (the packages already carry the regenerated bytes and every pin); exit 0",
   "exit 1 with exactly two changed lines (the contracts are canonical JSON, indent 2, sorted keys): \"contract_revision\": \"4.1.0\" -> \"4.1.1\" and \"primary_skill_revision\": \"1.3.0\" -> \"1.3.1\" (.pr_development_contract)",
   "ed52208f48479124f39119a54f29774096381ab85f54109a73bc3a7f3cc572af (= SKILL_TREE_SHA256 on $FV/SKILL.md:9)"
  ],
  "note": "the oracle is byte-identical in $FV and $FVI (not a changed file). The recipe reads the two '> ' lines of the D23-E once-per-merge section only, bounded at the next '### ' or '## ' heading, and asserts there are exactly two (P-21), so entries added under D23 or later decisions do not change the output. $CFI and $FVI are the installed packages before the install sitting; $CF and $FV are in $PKG",
  "when": "X4.1 (spec \u00a79), after X2 and X3"
 },
 "4b_package_X4.3_after_the_pkg_gate": {
  "when": "X4.3 (spec \u00a79), after the pkg gate (X4.2). Run again only when the session holding the archives ends before X4.4 delivers them, and then followed by a new review round (P-100); never after the delivery",
  "commands": [
   "mkdir -p $SCRATCH/skills-out $SCRATCH/skills-ext",
   "(for s in flowmaster-validate change-flow glow-graph-contract session-relay-flowmaster glow-hde-pr-development amthor-workspace-governance-audit glow-po-reporting; do (cd $PKG/skill-creator && python3 -m scripts.package_skill $PKG/$s $SCRATCH/skills-out) || { echo \"PACKAGE FAILED: $s\"; exit 1; }; done)",
   "(for s in flowmaster-validate change-flow glow-graph-contract session-relay-flowmaster glow-hde-pr-development amthor-workspace-governance-audit glow-po-reporting; do rm -rf \"${SCRATCH:?}/skills-ext/${s:?}\" && mkdir -p $SCRATCH/skills-ext/$s && (cd $SCRATCH/skills-ext/$s && unzip -q $SCRATCH/skills-out/$s.skill) || exit 1; done)",
   "(for s in flowmaster-validate change-flow glow-graph-contract session-relay-flowmaster glow-hde-pr-development amthor-workspace-governance-audit glow-po-reporting; do printf '%s ' $s; python3 docs/prompt_ecosystem_management/freeze.py $SCRATCH/skills-ext/$s/$s; done) > $SCRATCH/skills-ext/freeze.txt && cat $SCRATCH/skills-ext/freeze.txt && diff $SCRATCH/skills-ext/freeze.txt $EV/skills/expected_after_patch.txt",
   "python3 $EV/skills/packages_json.py $SCRATCH/skills-out $SCRATCH/skills-ext/freeze.txt $EX/packages.json",
   "python3 docs/prompt_ecosystem_management/freeze.py $PKG"
  ],
  "expected": [
   "exit 0",
   "exit 0; 'Skill is valid!' once per package (seven); seven files <skill>.skill in $SCRATCH/skills-out",
   "exit 0; each archive extracts to $SCRATCH/skills-ext/<skill>/<skill>/",
   "seven lines '<skill> <files> <digest>' printed, then `diff` exits 0: each equals execute.1.expected_after_patch for that skill ($EV/skills/expected_after_patch.txt). A mismatch makes diff exit 1, and the step fails",
   "exit 0; seven lines '<skill>.skill <entries> <bytes> <sha256> <files> <digest>', and EX/packages.json written with them and out_dir; committed and pushed with EX/gate_pkg.json. The archive sha256s vary with the tree's file mtimes (EV/skills/results/brief_fill_proof.json), so the archives reviewed at X4.4 are the ones delivered there (P-100)",
   "the value X1.1 recorded: packaging wrote nothing into $PKG"
  ],
  "note": "skill-creator runs from $PKG's copy (a full copy of $INST), never from $INST, and with PYTHONDONTWRITEBYTECODE=1, so nothing is written into a skill tree. The seven archives stay in $SCRATCH/skills-out until X4.4 delivers them"
 },
 "6_closure_X6.3": {
  "when": "X6.3 (spec \u00a79), after X6.2 (P-102 (b): the command lives here, unescaped, not only in \u00a79's table)",
  "commands": [
   "for id in $(grep -o '^[A-Z][A-Z0-9-]*  -- closure' docs/ephemeral/modifications/evidence/closeout-residuals/ANALYZE-closure.md | cut -d' ' -f1); do python3 docs/prompt_ecosystem_management/closure.py $id; done > $SCRATCH/closure.now.txt",
   "awk '/^```$/{f=!f; next} f' docs/ephemeral/modifications/evidence/closeout-residuals/ANALYZE-closure.md | diff - $SCRATCH/closure.now.txt"
  ],
  "expected": [
   "exit 0; one closure block per live prompt ANALYZE listed",
   "exit 0 (diff prints nothing): closure over the 50 live prompts is unchanged against ANALYZE-closure.md (proved on the reindexed tree at PLAN)"
  ]
 },
 "5_after_the_install_sitting": {
  "commands": [
   "mkdir -p $EX && (for s in flowmaster-validate change-flow glow-graph-contract session-relay-flowmaster glow-hde-pr-development amthor-workspace-governance-audit glow-po-reporting; do printf '%s ' $s; python3 docs/prompt_ecosystem_management/freeze.py $INST/$s; done) > $EX/installed_freeze.txt && cat $EX/installed_freeze.txt && diff $EX/installed_freeze.txt $EV/skills/expected_after_patch.txt"
  ],
  "expected_stdout": {
   "flowmaster-validate": "31 0ca2a74d50a57803e2c4b8426a84f43877f68f6d1c93731d54368f413e5c5626",
   "change-flow": "22 9a551af36e042e56a48045297ac316b4102a4eb21f31622853c8be700e223f47",
   "glow-graph-contract": "9 e241bb9a67c4470895fc666a25d0f97d8df7e8e2df06539de5deaf12bc46467c",
   "session-relay-flowmaster": "5 c8a5b22432a44f57fb12bc508169f85aa3d0ca3298b793590c364eb9a2afc8e4",
   "glow-hde-pr-development": "4 265f9170d8459fc477287c320f0bbdd8eaaf0e6ba1dd4ee513275a76a22f8f7a",
   "amthor-workspace-governance-audit": "15 c214e8741e9c54d395cfbd1379cbc7947e6c07beee5bd03aca433dc5dda937ab",
   "glow-po-reporting": "1 7e04368a63e40c99e31ede3eda9ba88cfbbb9915a48b46cdc39027da7cef68e1"
  },
  "then": "python3 $EV/skills/run_gate.py --set post --inst $INST --out $GATE (suite_gate.post); exit 0, 28 rows ok",
  "one_install_event": "flowmaster-validate 3.3.1 passes only with change-flow 3.3.1, relay 3.2.0, PR skill 1.3.1 and the dbae180b contract in both bundled copies; install the seven together",
  "when": "X7.4 (spec \u00a79), after Nathan's install sitting (X7.3)",
  "expected": [
   "seven lines '<skill> <files> <digest>' printed, then diff exits 0: each equals expected_stdout below and the freeze line recorded for its archive in EX/packages.json. EX/installed_freeze.txt fills {{FREEZE_DIGESTS}} (apply_texts.py --installed-freeze, P-96)"
  ]
 },
 "suite_gate": {
  "script": "$EV/skills/run_gate.py (expected results embedded; exit 0 only when every row is ok; writes only under --out and --cand, refuses either inside the repository or a skill tree)",
  "pre": {
   "when": "X1.3, once, on the unchanged working tree before commit 1 and the reindex",
   "command": "python3 $EV/skills/run_gate.py --set pre --pkg-root $PKG --out $GATE",
   "expected": "exit 0; gate_pre.json: 12 rows, all ok"
  },
  "pkg": {
   "when": "X4.2, after commit 1 (X2), the registry, the reindex, the contract-template move, P32-SWR (X3) and the contract regeneration (X4.1)",
   "command": "python3 $EV/skills/run_gate.py --set pkg --pkg-root $PKG --out $GATE",
   "expected": "exit 0; gate_pkg.json: 34 rows, all ok"
  },
  "post": {
   "when": "X7.4, after the install sitting, on main with the execution PR merged",
   "command": "python3 $EV/skills/run_gate.py --set post --inst $INST --out $GATE",
   "expected": "exit 0; gate_post.json: 28 rows, all ok"
  }
 },
 "_changes_from_committed_manifest": [
  "variables: TMPDIR is $SCRATCH/tmp (spec \u00a79); PKG, EV, GATE and cwd defined; GGC..REPORT are $PKG's packages",
  "1.then: builds the full skills root $PKG (a copy of $INST with the seven patched packages) and gates it on the whole-root freeze; runs at X1.1, before any repository change (P-56)",
  "2: the new builder's expected refusal of today's parts runs as run_gate.py --set pre; the reindex-diff check is the mechanical cmp; the 'alternative' git apply became a read-only cross-check",
  "3: mkdir -p before git mv; README source is $EV/skills/contract-template-README.md; README staged",
  "4: the structural diff is a plain diff of the two canonical contracts; no PLAN scratch path",
  "suite_gate (new): the three run_gate.py calls; 5.then points at suite_gate.post",
  "repair round 3: 'when' fields follow spec \u00a79 X0-X7; the pre gate runs at X1.3 (suite_gate.pre), no longer inside execute.2",
  "repair round 4: 4b (packaging, X4.3) added with exact commands; the whole-root digest is recorded, not asserted (P-79); BASE defined (P-83)",
  "repair round 5: every `rm -rf` takes the guarded form \"${VAR:?}\" (P-92), which the session's safety check allows and which cannot expand to /; execute.4b compares the extracted freeze digests with expected_after_patch.txt by diff, so X4.3's gate fails mechanically on a mismatch; the archive sha256s go to EX/packages.json",
  "repair round 6: BASE is read from EX/run.json; execute.1.then only before X7.3 (P-101); execute.4b writes EX/packages.json with packages_json.py and is never re-run after X4.4's delivery (P-100); execute.5 writes EX/installed_freeze.txt and compares it by diff; execute.6 carries X6.3's closure commands unescaped (P-102)"
 ]
}
````

## §6 Repository texts

Applied in this order; each anchor occurs exactly once at its turn. Each text is labelled by the step that commits it (P-73): `X2.2` is the decision record (commit 1), `X3.5` is `P32-SWR`, `X5.2` is `P30-DEST` and `P30-VERSION` (after the page exists), and `close` is the close commit (X7.6). `EV/texts/apply_texts.py <repo> EV/texts/edits.json <label>` applies them, filling each token from `EX/run.json` and `EX/installed_freeze.txt` (P-96) and refusing any text that still carries one (P-48, P-102).

### P29-D25 — `docs/prompt_ecosystem_management/gcfpe.decision-record.md`, label `X2.2`, `insert_after`

anchor:

```text
this entry says so rather than implying a guard exists.

```

new text:

```markdown

## D25 — The Candidate CRD Items List lives in Notion, and every prompt commits its output files

**Product Owner, 2026-09-23**, during the analysis of `MODIFICATION-20260923-closeout-residuals`:
*"candidate CRD can live in notion, I don't think it is a huge doc"*. Then: *"all output files are
committed, that is the only way they are ever seen"*. And, approving the analysis's recommendation
that `CL-40` write the list itself under a destination rule: *"ok approved"*.

### What was wrong

- **`CL-40` had no store for the list it updates** (ITEM-18). It adds each finished change's new
  CRD candidates to the Candidate CRD Items List, but it named no store, and an authoring leftover
  in its body read as forbidding the update its step 7 authorizes. No Notion page held the list.
  The only copy was the Drive file `Candidate-CRD-Items-List.md`
  (`1JPN7WcqCddC2J7UKkHdO4gnIPYRJPGJO`, last modified 2026-09-08), and Drive is not a storage
  authority (`D7`). A flow prompt writes to Notion only under a destination rule
  (`notion-write-boundary.md`), and no rule named a page. With no writer, the list goes stale,
  which is the failure that retired the `D18` block.
- **Bodies that commit their own output artifacts called themselves read-only** (ITEM-17, ITEM-32).
  The analysis's census found the claim in 13 live bodies, among them `QA-10`, which called itself
  read-only while it saves three artifacts. It found an unscoped "Reviewers remain read-only" in
  four (`docs/ephemeral/modifications/evidence/closeout-residuals/ANALYZE-anchor-census.md`, A6
  and A10). The behaviour was right and the wording wrong: each of those bodies writes, commits
  and pushes its own artifacts.

### The rulings

**D25-A — The Candidate CRD Items List lives in Notion, and `CL-40` writes it (ruling 1; ruling 5,
Open question 1, answer (A)).**

- The list's one store is the Notion page *Candidate CRD Items List*, under the Glow Operations
  Hub.
- `GCFPE-MGMT-10` creates the page at EXECUTE of `MODIFICATION-20260923-closeout-residuals`, under
  that run's task-level authorization. It migrates the Drive list into the page and reads the page
  back against the Drive source.
- A destination rule in `notion-write-boundary.md` names that page. Under it, `CL-40` updates the
  page in place with each change's new CRD candidates, and writes no other Notion page.
- `CL-40`'s registry `mutations` allow that write, and the authoring leftover goes (A4c).
- The Drive file becomes Nathan's reference copy. He banners it as superseded, pointing to the
  Notion page. The file is his, and nothing reads it as a store.

**D25-B — Every prompt commits its output files (ruling 2).**

- A prompt's output artifacts are written, committed and pushed. That is the only way they are
  seen, so the commit stays.
- Every statement in a body that the prompt is read-only, or does not change the repository,
  excludes the prompt's own committed output artifacts (C-ART) and, by the approved plan (its decision
  P-02), any pull request that carries them. The claim is scoped, and the behaviour does not change.
- A reviewer stays read-only toward the work it reviews, and commits its own review artifacts.
- Nothing else is excluded. Every other limit a body states on what it may change still holds.

### Consequences

- **Both are recorded before any EXECUTE edit** of `MODIFICATION-20260923-closeout-residuals`, in
  its first execution commit. `D25-A` changes what `CL-40` writes and where (class A, PART-06).
  `D25-B` aligns wording with what the bodies already do (class B, PART-05).
- **The exact wording each ruling is applied with is in that Modification's execution specification**
  (`docs/ephemeral/modifications/specs/EXECUTION-SPEC-20260923-closeout-residuals.md` §3.2), which its §P cites. It is
  cited there, not restated here, so the two cannot drift (`DERIV-001`).
- **`CL-40`'s rule is a flow prompt's own destination rule.** It names one page, and authorizes
  `CL-40` alone. The line `notion-write-boundary.md` draws between executing the flow and
  maintaining the ecosystem stands, and no other flow prompt gains a Notion write.
- **The Drive list's only repository mention**
  (`docs/ephemeral/HDE-EPIC040-PR40-workspace-register.md:206`) sits inside a dated 2026-09-09
  snapshot of a Notion page, and stays as written (`AUTH-001`).
- **`D25-B` gives no prompt a new write.** It corrects what bodies say about the writes they
  already make.

### The tested guard (`D14`)

Registry assertions in `project-prompt-contract-registry.md`, listed in that Modification's execution
specification (§4.2). Each
is fired by an injected must-fail regression, on synthetic text at PLAN and again on the landed
body at EXECUTE (`GUARD-001`):

- **`D25-A`:** G-K43 forbids `CL-40`'s authoring leftover. G-K44 forbids the page-URL placeholder
  in `CL-40`, so the corpus gate fails while the URL is unfilled. G-K45 requires `CL-40` to name
  the page *Candidate CRD Items List* by its direct Notion URL.
- **`D25-B`:** G-K35 forbids each carrying row's unscoped read-only claim. G-K36 requires the
  scoping sentence on those rows. G-K37 forbids an unscoped "Reviewers remain read-only" on all 55
  rows. G-K38 requires the scoped form on the four rows that carry it.

The destination rule, `CL-40`'s `mutations` entry and the migrated list have no check that fires.
Readback holds them, the list against its Drive source, and this entry records that rather than
implying a guard. **`D25` applies from the merge that puts those guards on `main`, after they have fired on the landed bodies.
That Modification's record (§E) states the merge commit and its date.**

```

### P29-D23C — `docs/prompt_ecosystem_management/gcfpe.decision-record.md`, label `X2.2`, `insert_before`

anchor:

```text
## D24 — The independent skill review is run by reviewer subagents; Nathan installs approved packages

```

new text:

```markdown
### Successor, 2026-09-23 — C-LAT's three steps leave the eight bodies that implement nothing (D23-C)

**Product Owner, 2026-09-23**, on ITEM-37 of `MODIFICATION-20260923-closeout-residuals`. Offered a
step 2 that hands the decision to the implementing PR owner, he replied *"yes those words don't
seem to mean anything do they"*. Review then found that receiver wrong for `PR-40`, `IA-30` and
`PR-10`, so the question was asked again, and he approved answer (a) with *"ok approved"*.

C-LAT's placement by step 22 of `MODIFICATION-20260923-alpha-feedback-open-entries` (spec v2 §3)
is superseded for eight bodies. `D23-C` above is left as written (`AUTH-001`).

- **C-LAT's three-step *Decide it during work* block is removed from `PR-10`, `PR-20`, `PR-40`,
  `RS-10`, `RS-20`, `DOC-10`, `DOC-20` and `IA-30`.** None of them implements anything, yet step 2
  told each to decide, implement and test. `PR-40` sends an in-scope defect to a re-plan instead
  (`D23-F`).
- **The Material definition stays in all ten bodies, and so does each body's own routing.** A
  material change still goes to rescope, and the rest is handled by the body's role.
- **`PR-30` and `PR-35` keep the whole C-LAT.** They implement, and `D23-C`'s latitude is theirs.
- **C-LAT's text is unchanged.** Only its placement changes.

**Guard (`D14`).** In the registry, *Decide it during work* stops being required on those eight
rows and becomes forbidden there (G-K51). The Material requirement stays on all ten rows, and
`PR-30` and `PR-35` keep both. The forbidden pattern is fired by an injected regression.


```

### P29-D23G — `docs/prompt_ecosystem_management/gcfpe.decision-record.md`, label `X2.2`, `insert_before`

anchor:

```text
## D24 — The independent skill review is run by reviewer subagents; Nathan installs approved packages

```

new text:

```markdown
### Successor, 2026-09-23 — the release-line check covers the whole body (D23-G)

Recorded by `MODIFICATION-20260923-closeout-residuals` (ITEM-36), whose analysis Nathan approved on
2026-09-23 (*"yes"*). It applies `D23-G` as ruled, and rules nothing new.

- **`D23-G` bars a release-bound label line anywhere in a body.** `prompt-body-content-policy.md`
  forbids any field whose value changes because of a release event, with no header limit.
- **Both checks saw only a header window**, the first eight non-blank lines: the registry's guards
  on all 55 rows, and `flowmaster-validate`'s `PROMPT_BODY_RELEASE_HEADER`. A label line after the
  window passed. The window was an implementation limit, not the rule.
- **Both are widened to the whole body, line-anchored.** A `Prompt version:`, `Set:` or
  `Ecosystem release:` label line fails wherever it stands, plain or decorated (bold, backticked,
  numbered). A mention of a label inside a sentence does not.
- **This supersedes one literal**, *"in the header window"*, which step 41 of
  `MODIFICATION-20260923-alpha-feedback-open-entries` (spec v2 §3.5) placed in the Enforcement line
  of `prompt-body-content-policy.md`. That line changes to "anywhere in the body, line-anchored" in
  the same Modification. The spec is left as written (`AUTH-001`).

**Guard (`D14`).** The registry's three window patterns are replaced in place by whole-body
patterns, and `flowmaster-validate` gains fixtures for its check. Each fails on a label line
injected past the eighth non-blank line, which the window let through.


```

### P29-D18 — `docs/prompt_ecosystem_management/gcfpe.decision-record.md`, label `X2.2`, `insert_before`

anchor:

```text
## D19 — A prose skill carries no advertised identity; its freeze digest is its identity

```

new text:

```markdown
### Successor, 2026-09-23 — `alpha_resumption_contract` is the promotion-time record

**Product Owner, 2026-09-23:** *"ok approved"*, approving the recommendation on Open question 3 of
`MODIFICATION-20260923-closeout-residuals`, answer (A).

The successor above left Alpha state to the Epic's own artifacts. Machine records still carry the
resumption contract as promotion recorded it: the graph's `global.json` and both `091426.1`
contracts hold an `alpha_resumption_contract` with
`state: ALPHA_STOPPED_PENDING_CHANGE_FLOW_REFACTOR` and `next_intended_unit: HDE-EPIC040-PR04`,
and two validator checks require those values.

- **They are the promotion-time record, not current Alpha state.** Current Alpha state is what the
  Epic's own artifacts record (the successor above). No prompt reads the block for routing.
- **The values stay, and the graph does not change.** Its digest stays `ae2bd159…`, and the
  regenerated contract carries the same block.
- **The validator checks are renamed** from Alpha-state checks to promotion-record checks, with
  their values unchanged: `flowmaster-validate`'s `ALPHA_STATE` and `ALPHA_TRIGGER` at
  `validate_gcfpe_20260914.py:1901-1916` become `ALPHA_PROMOTION_RECORD` and
  `ALPHA_PROMOTION_RECORD_TRIGGER` (with the fixture mutation renamed to match), and `change-flow`'s
  two requires at `:1017-1018` are reworded (3.3.0 line numbers). The skills' prose says the same.
- **Retiring the block was not chosen.** It would move the graph digest, and every proof token and
  pin with it.


```

### P29-D14 — `docs/prompt_ecosystem_management/gcfpe.decision-record.md`, label `X2.2`, `insert_before`

anchor:

```text
## D15 — Ten qualifying-approval branches were still marked terminal after drainage removal

```

new text:

```markdown
### Note, 2026-09-23 — a phrase guard cannot see a paraphrase

Recorded by `MODIFICATION-20260923-closeout-residuals` (ITEM-16), whose guards for `D22` pin exact
phrases. The ruling above is left as written (`AUTH-001`); this records a limit of its second part.

- **The guards pin phrases, not meaning.** `CONTRACT_REQUIRED` holds one exact override sentence in
  `change-flow` and `session-relay-flowmaster`. `CONTRACT_FORBIDDEN`, or the owning skill's own
  suite, forbids each exact retired body-copying or body-hashing phrase. A governance-audit fixture
  proves that a prompt-kind source carries no digest.
- **A paraphrase passes them.** The prose guard first prototyped for `D22` missed 30 of 30
  paraphrased violations and flagged the edits' own prohibitions
  (`docs/ephemeral/modifications/evidence/closeout-residuals/ANALYZE-skill-evidence.md`, ITEM-16).
  The guards were narrowed to exact phrases for that reason.
- **The residual limit is prose paraphrase.** A retired rule reintroduced in new words is not
  mechanically detectable. Review holds it: the first part of this ruling, which asks what the text
  makes an agent *do*, and the `D24` review of every skill change.
- **An exact-phrase guard still meets the second part** once an injected regression has fired it.


```

### P30-DEST — `docs/prompt_ecosystem_management/notion-write-boundary.md`, label `X5.2`, `insert_after`

anchor:

```text
| operational status, navigation, plan state | Notion — where a destination rule already says so |

```

new text:

```markdown
| the Candidate CRD Items List | the Notion page *Candidate CRD Items List* (`{{CANDIDATE_CRD_LIST_URL}}`), under the Glow Operations Hub, and nowhere else. An established destination rule (`D25-A`): `CL-40` updates that page in place with each change's new CRD candidates, and writes no other Notion page. It is a flow prompt's own rule, so it authorizes `CL-40` alone and lends nothing to any other flow prompt. The Drive file it replaced is Nathan's reference copy, not a store. |

```

### P30-VERSION — `docs/prompt_ecosystem_management/notion-write-boundary.md`, label `X5.2`, `replace`

anchor:

```text
artifact_version: "1.2"

```

new text:

```markdown
artifact_version: "1.3"

```

### P31-POLICY — `docs/prompt_ecosystem_management/prompt-body-content-policy.md`, label `close`, `replace`

anchor:

```text
  matches the registry binding; rejects `Prompt version:`, `Set:` and `Ecosystem release:` in the
  header window as `PROMPT_BODY_RELEASE_HEADER` (D23-G);

```

new text:

```markdown
  matches the registry binding; rejects a `Prompt version:`, `Set:` or `Ecosystem release:` label
  line anywhere in the body, line-anchored, as `PROMPT_BODY_RELEASE_HEADER` (D23-G; the whole-body
  check replaces the header window, per the `D23-G` successor of 2026-09-23 in
  `gcfpe.decision-record.md`);

```

### P32-SWR — `docs/prompt_ecosystem_management/session-working-rules.md`, label `X3.5`, `insert_after`

anchor:

```text
- **IN FLIGHT** — something is running; the Product Owner waits

```

new text:

```markdown

When a `NEXT_PROMPT_HANDOFF` block ends the message, as it does for a maintenance, repair, validation or review session, the block comes last and the named state is the line immediately before it. Nothing follows the block.


```

### P33-A5NOTE — `docs/ephemeral/modifications/evidence/REVIEWER-PROMPT-a5.md`, label `close`, `insert_after`

anchor:

````text
Put your answer first and close with DECISION NEEDED, NOTHING NEEDED, or IN FLIGHT.
```

````

new text:

```markdown

## Correction, 2026-09-23 — C8 and §2 overstated the comment rule

Recorded by `MODIFICATION-20260923-closeout-residuals` (ITEM-15). The brief above is left as written
(`AUTH-001`). SFR-A5-1 N1 and SFR-A5-2 F3 are one finding in two halves: a code half, which ITEM-15
repairs in `flowmaster-validate`, and a claim half, which this note corrects. Both round-a5 verdicts
were `SKILL_FIT_CONFIRMED`, and neither depends on the statements corrected here.

- **C8 was too broad** (the claim half of N1). It says that adding "any HTML comment other than a
  whole-line FLOWMASTER marker" fails the suites. The round-a4 rule (R1) looked only for `<!--`,
  `-->` and `--!>`. A bogus comment (`<!x …>`), a processing instruction (`<?…?>`) and a CDATA
  section (`<![CDATA[`), which an HTML parser also turns into comment nodes, passed every gate
  (SFR-A5-1 probes D1, D2 and D4; SFR-A5-2 probe Q2). C8 held for `<!--`-delimited comments only.
  SFR-A5-2 read C8 as holding as worded; this note takes N1's reading.
- **§2's known limits were incomplete** (the claim half of F3, and N1's limit entry). They did not
  list text hidden in a rendered file by markup other than a comment: an unclosed `<script>` or
  `<style>`, a `<template>` element, a `<div hidden>` element, or a `[//]: #` reference line. Each
  passed every gate (SFR-A5-1 probes D3, D5, D7 and D8; SFR-A5-2 probes Q1, Q2b and Q4).

**What ITEM-15 changes.** `flowmaster-validate` 3.3.1 replaces R1's token test with
`DISPATCH_HIDING_RE`. After the six whole-line section markers are removed, it rejects any `<!` or
`<?` in a carrying file (every comment, bogus comment, declaration, CDATA section and processing
instruction), any `--!>`, any opening `<script`, `<style`, `<template` or `<textarea` tag, and any
`[label]: #` reference line. The markers it admits are exactly `FLOWMASTER_CORE_`,
`FLOWMASTER_SPECIALIZATION_` and `FLOWMASTER_PROHIBITIONS_`, each with `BEGIN` or `END` (SFR-A5-2
F2), and a bare `-->` arrow is no longer rejected (SFR-A5-1 N4, SFR-A5-2 F4). From 3.3.1, C8's
comment clause holds for every construct that opens with `<!` or `<?`.

**The limit that remains.** `<div hidden>`, `<details>` and other type-6 HTML blocks are not matched
by `DISPATCH_HIDING_RE`, and neither is any other element that hides text through an attribute such
as `hidden`. They hide text only in some renderers, and they share their HTML block type with
ordinary markup. The whole passage moved intact into such an element stays a known limit, as §2
lists for `<details>`. A model reads the raw file, and the pinned passage is counted on the raw
file, so the risk is to a human reading the rendered file.

```

### CLOSE-D22 — `docs/prompt_ecosystem_management/gcfpe.decision-record.md`, label `close`, `insert_before`

anchor:

```text
## D23 — The Alpha Feedback rule changes: artifacts hold results, handoffs are short, implementors have latitude, PR-35 has its own session, releases stop copying unchanged prompts

```

new text:

```markdown
### Status, {{INSTALL_DATE}} — guarded

`MODIFICATION-20260923-closeout-residuals` (ITEM-16) carried the guard the status above owed. It
was installed on {{INSTALL_DATE}}, with these freeze digests (`freeze.py`, files hashed and digest):

{{FREEZE_DIGESTS}}

The status above is left as written (`AUTH-001`).

- **`CONTRACT_REQUIRED`** in `flowmaster-validate` holds ITEM-08's override sentence in
  `change-flow` and `session-relay-flowmaster`: a GCFPE prompt is pinned by stable ID, version and
  direct Notion URL, and no copy, hash or snapshot of its body is kept.
- **`CONTRACT_FORBIDDEN`**, or the owning skill's own suite, forbids every retired body-copying or
  body-hashing phrase that Modification removed from `change-flow`, `session-relay-flowmaster`,
  `flowmaster-validate` and `amthor-workspace-governance-audit`.
- **A governance-audit fixture** proves that a prompt-kind source carries no digest.
- **Each fired on an injected regression**, and each is silent on the installed text.
- **What they cannot see** is prose paraphrase, recorded under `D14` (its note of 2026-09-23). As
  before, no repository check sees a harness session directory, so condition 5, the report, still
  makes every transient file visible.
- `tw-flowmaster` was outside that Modification's scope, and carries no `D22` guard.


```

## §7 Notion

Every edit: re-fetch the page and run `python3 EV/engine/ctrl.py edits <PAGE> <EDIT_ID> --run EX/run.json` (P-90, P-96). `LANDED`: it has landed, so go to the readback. `NOT_LANDED`: fill its tokens from `EX/run.json`, apply with `notion-update-page` `update_content` (`allow_async: false`, P-83; poll an `async_task` to its end, P-89). `TOKEN_NOT_RECORDED`: record the value first. `MIXED`: stop (P-98). Read back: the same command reads `LANDED` and the filled `new_str` is on the re-fetched page. No bold run holds a code span (P-91). No new text may carry `{{` when it lands (P-48). Each edit's *when* names its §9 step and §P step. The tokens, their `EX/run.json` keys and when each is recorded (P-96):

| token | `EX/run.json` key | recorded | where it is used |
|---|---|---|---|
| `{{CANDIDATE_CRD_LIST_URL}}` | `url` (and `page_id`) | at X5.1 as soon as the create returns, committed and pushed before step 7's write | body rules (R-ITEM18), `P30-DEST`, ten PART-06 pointers, M2-R4, R5 and R9 |
| `{{MIGRATION_DATE}}` | `migration_date` | at X5.1, the UTC date, committed and pushed before the create call | M2-R1, the M2 callout and revision bullet, `PART-06-HUB-01`, the four `PART-06-ITEM*-02` edits |
| `{{EXECUTE_DATE}}` | `execute_date` | at X5.0, the UTC date, committed and pushed before `TRACK-FREEZE-START`: the date the unit started | `TRACK-FREEZE-START`, `PART-11-TRACK-01`, `PART-18-AF009-01`, `PART-06-HUB-01`'s "Corrected" note |
| `{{STOP_DATE}}` | `stop_date` | at a stop after X5.0, the UTC date, first (P-98 step 1) | `TRACK-UNIT-STOPPED`, `TRACK-STATUS-STOP-01` to `03`, `TRACK-FREEZE-LIFT-STOP` |
| `{{INSTALL_DATE}}` | `install_date` | at X7.4, first: the UTC date Nathan gives for his install sitting, or of his install confirmation when he gives none | `CLOSE-D22` |
| `{{LIFT_DATE}}` | `lift_date` | when Nathan lifts the freeze, before `TRACK-FREEZE-LIFT` (X7.5) or `TRACK-FREEZE-LIFT-STOP` (P-99) | those two lines |
| `{{CLOSE_DATE}}` | `close_date` | at X7.6, the UTC date, in the close commit itself | `TRACK-STATUS-01` to `03` (X7.7) |
| `{{FREEZE_DIGESTS}}` | — | at X7.4: `EX/installed_freeze.txt`, execute.5's seven lines | `CLOSE-D22` (`EV/texts/apply_texts.py`) |

### 7.1 PART-12 — the Hub's *Worker communication rules* §2 (ITEM-24)

#### PART-12-HUB-01 — Glow Operations Hub (`3ce4590a05eb814f8892f88ff8539308`)

Inserts P-32's sentence after the definition of the three named states. *When:* X5.6; §P step 20.

old_str:

```text
- **IN FLIGHT** — something is running; the Product Owner waits
```

new_str:

```markdown
- **IN FLIGHT** — something is running; the Product Owner waits
When a `NEXT_PROMPT_HANDOFF` block ends the message, as it does for a maintenance, repair, validation or review session, the block comes last and the named state is the line immediately before it. Nothing follows the block.
```

### 7.2 PART-18 — C-LAT's placement on control pages and skills

The PE Metaprompt (`3db4590a05eb8174be35d9e35acb3f77`) was read in full: its GCFPE overlay states no placement. It places each canonical text where the registry row requires it, which stays true (the Material pattern stays on all ten rows). No edit.

**The skills.** A grep of the installed skills root and of `$PKG` (the TW skill excluded) for `C-LAT` or `Decide it during work`, 2026-09-24, finds two files in each, and nothing else: `glow-hde-pr-development/SKILL.md:133` and `glow-hde-pr-development/scripts/validate_glow_hde_pr_development.py:87`. Both are the implementing PR skill's own *Decide it during work*, which stays: PR-30 and PR-35 keep the whole C-LAT (D23-C successor). No skill states the eight bodies' placement, so no skill edit follows from PART-18.

The Alpha feedback list's AF-009 disposition does state the placement, so it gets a dated amendment (P-44).

#### PART-18-AF009-01 — GCFPE Alpha Feedback — Deferred Items — 091426.1 (`3df4590a05eb8111a6a5f67cb82f96f6`)

Appends a dated amendment after AF-009's disposition; the disposition is not rewritten. *When:* X5.6; §P step 21.

old_str:

```text
Scope is the PR lane; the ESC remediation lane keeps its own threshold.
```

new_str:

```markdown
Scope is the PR lane; the ESC remediation lane keeps its own threshold. **Amended {{EXECUTE_DATE}}** (`D23-C` successor; `MODIFICATION-20260923-closeout-residuals` PART-18): C-LAT's three-step *Decide it during work* block now sits whole only in PR-30 and PR-35, which implement; PR-10, PR-20, PR-40, RS-10, RS-20, DOC-10, DOC-20 and IA-30 keep its Material definition and their own routing. The parenthesis above is left as written (`AUTH-001`).
```

### 7.3 The D20 redesign tracking page: PART-11, the freeze and the close-out status (Decision 11; P-65, P-66, P-72, P-98, P-99)

Three dated insertions and three status replacements on one page. After a stop past X5.0 only, a dated stop line and three stop variants of the status replacements (P-98 step 7), and a lift line after the restoration check (P-99). The insertions share one anchor, the opening of the paragraph that introduces *the three decisions below*, so each lands after the one before it, in date order. `ctrl_proof.py` replays both sequences on the live page (§8.7).

#### TRACK-FREEZE-START — GCFPE MGMT Change-Process Redesign — Tracking (`3e34590a05eb81e7927efe0541258916`)

The run's first Notion write, after Nathan confirms the freeze. *When:* X5.0; §P step 13 — after Nathan confirms the freeze, as the run's first Notion write.

old_str:

```text
**The three decisions below are recorded as
```

new_str:

```markdown
**{{EXECUTE_DATE}}: the freeze started.** Nathan confirmed it before `MODIFICATION-20260923-closeout-residuals` made its first Notion write: no flow session runs until the seven skills it changes are installed and verified and Nathan lifts the freeze, so no landed prompt body is used before the matching skills are installed.
**The three decisions below are recorded as
```

#### PART-11-TRACK-01 — GCFPE MGMT Change-Process Redesign — Tracking (`3e34590a05eb81e7927efe0541258916`)

One entry, dated by the unit's start date (P-51, P-96), listing the proposed MGMT-10 body's design-level contradictions for stage 5. *When:* X5.6; §P step 19.

old_str:

```text
**The three decisions below are recorded as
```

new_str:

```markdown
**{{EXECUTE_DATE}}: input for stage 5 — the proposed body's design-level contradictions.** `MODIFICATION-20260923-closeout-residuals` records them in `docs/ephemeral/modifications/evidence/closeout-residuals/ANALYZE-anchor-census.md`, section *The proposed MGMT-10 body*, from a complete read of the proposed body (the child page below) on 2026-09-23. **They are not resolved by that Modification** (its §A, Decision 11): each needs a design choice the `D20` track owns, so they wait for stage 5. That Modification changes the proposed body only to remove the classes it removes from the live bodies (ITEM-23, ITEM-40).
- **Read-only lines:** ANALYZE's "Must not: change anything, propose a plan, decide a policy question" and PLAN's "Must not: apply anything, add scope not in the analysis", yet each mode writes, commits and pushes its own section of the Modification.
- **Exactly one Modification:** "Every invocation reads and writes exactly one Modification" conflicts with ANALYZE's read-only line, and with EXECUTE turning genuinely new scope into a new Modification, whose writer is not stated.
- **Result codes:** one result per invocation, with three codes only; the pending-approval return of ANALYZE and PLAN has no code, and one session may span several modes.
- **Approval fields:** "Each mode writes only its own section" does not say which mode or session writes `analyze_approved_by` and `plan_approved_by` when modes chain in one session.
- **Artifact locations:** every artifact is Markdown under `docs/ephemeral/`, but graph parts live in `docs/graph/` and rule changes in `docs/prompt_ecosystem_management/`.
- **Entry contract:** a raw-request ANALYZE has no id, yet the body finds the Modification by its id; creating the file and the branch is not specified.
- **Open-PR outcome:** "An open pull request is a complete outcome" against `ECOSYSTEM_CHANGE_COMPLETE`'s "applied and verified" and "a part lands whole"; the result code for an unmerged PR or a pending install is unclear.
- **Install verification:** PLAN's chain of package, independent review, Nathan's install and post-install digest comparison cannot finish inside EXECUTE, which stops at install.
- **Release-selection boundary:** the body says it does not execute release selection or promotion, yet PLAN's prompt step moves registry rows of selected release members.
- **YAML governance state:** the page preamble carries `status: APPROVED_FOR_TESTING` and `approved_by`, while the body says a prompt body carries behaviour, never governance state.
**The three decisions below are recorded as
```

#### TRACK-FREEZE-LIFT — GCFPE MGMT Change-Process Redesign — Tracking (`3e34590a05eb81e7927efe0541258916`)

After X7.4 passes and Nathan lifts the freeze. It states only what is then true. *When:* X7.5; §P step 26 — after X7.4's post-install verification passes and Nathan lifts the freeze.

old_str:

```text
**The three decisions below are recorded as
```

new_str:

```markdown
**{{LIFT_DATE}}: the freeze lifted.** The seven skills `MODIFICATION-20260923-closeout-residuals` changes were installed and verified after install, and Nathan lifted the freeze: flow sessions may run again.
**The three decisions below are recorded as
```

#### TRACK-STATUS-01 — GCFPE MGMT Change-Process Redesign — Tracking (`3e34590a05eb81e7927efe0541258916`)

After the close commit that sets `COMPLETE` is pushed, dated by the `close_date` it records. *When:* X7.7; §P step 28 — after the close commit (X7.6) is pushed.

old_str:

```text
FOLLOW_UP_MODIFICATION_AT_INTAKE
```

new_str:

```markdown
FOLLOW_UP_MODIFICATION_COMPLETE ({{CLOSE_DATE}}, close-out PR, docs/ephemeral/modifications/MODIFICATION-20260923-closeout-residuals.md)
```

#### TRACK-STATUS-02 — GCFPE MGMT Change-Process Redesign — Tracking (`3e34590a05eb81e7927efe0541258916`)

After the close commit that sets `COMPLETE` is pushed, dated by the `close_date` it records. *When:* X7.7; §P step 28 — after the close commit (X7.6) is pushed.

old_str:

```text
which is at `INTAKE` with `ANALYZE` in progress
```

new_str:

```markdown
which reached `COMPLETE` on {{CLOSE_DATE}} in its close-out pull request (record: `docs/ephemeral/modifications/MODIFICATION-20260923-closeout-residuals.md`)
```

#### TRACK-STATUS-03 — GCFPE MGMT Change-Process Redesign — Tracking (`3e34590a05eb81e7927efe0541258916`)

After the close commit that sets `COMPLETE` is pushed, dated by the `close_date` it records. *When:* X7.7; §P step 28 — after the close commit (X7.6) is pushed.

old_str:

```text
`INTAKE`, branch
```

new_str:

```markdown
`COMPLETE` on {{CLOSE_DATE}}, branch
```

**Only after a stop past X5.0** (P-98, P-99):

#### TRACK-UNIT-STOPPED — GCFPE MGMT Change-Process Redesign — Tracking (`3e34590a05eb81e7927efe0541258916`)

After the stop record PR is pushed (P-98 step 7). The freeze line stays; this states why. *When:* Only on the stop path after X5.0 (spec §9, 'The landing unit', stop step 7; P-98), after the stop record's pull request is pushed and opened (P-97); never on a run whose unit passes.

old_str:

```text
**The three decisions below are recorded as
```

new_str:

```markdown
**{{STOP_DATE}}: the closeout-residuals Modification stopped.** `MODIFICATION-20260923-closeout-residuals` stopped during `EXECUTE`: its landing unit did not pass, so the freeze holds until Nathan lifts it. Its record's §E, in the stop's record pull request, lists every Notion write found on the pages; Nathan restores those bodies from page history, then ends the Modification or rules a plan change.
**The three decisions below are recorded as
```

#### TRACK-STATUS-STOP-01 — GCFPE MGMT Change-Process Redesign — Tracking (`3e34590a05eb81e7927efe0541258916`)

With `TRACK-UNIT-STOPPED`, in place of the close status line it replaces. *When:* Only on the stop path after X5.0, with TRACK-UNIT-STOPPED (stop step 7; P-98).

old_str:

```text
FOLLOW_UP_MODIFICATION_AT_INTAKE
```

new_str:

```markdown
FOLLOW_UP_MODIFICATION_STOPPED ({{STOP_DATE}}, stop record PR, docs/ephemeral/modifications/MODIFICATION-20260923-closeout-residuals.md)
```

#### TRACK-STATUS-STOP-02 — GCFPE MGMT Change-Process Redesign — Tracking (`3e34590a05eb81e7927efe0541258916`)

With `TRACK-UNIT-STOPPED`, in place of the close status line it replaces. *When:* Only on the stop path after X5.0, with TRACK-UNIT-STOPPED (stop step 7; P-98).

old_str:

```text
which is at `INTAKE` with `ANALYZE` in progress
```

new_str:

```markdown
which stopped during `EXECUTE` on {{STOP_DATE}}; its record's §E (`docs/ephemeral/modifications/MODIFICATION-20260923-closeout-residuals.md`) lists what landed
```

#### TRACK-STATUS-STOP-03 — GCFPE MGMT Change-Process Redesign — Tracking (`3e34590a05eb81e7927efe0541258916`)

With `TRACK-UNIT-STOPPED`, in place of the close status line it replaces. *When:* Only on the stop path after X5.0, with TRACK-UNIT-STOPPED (stop step 7; P-98).

old_str:

```text
`INTAKE`, branch
```

new_str:

```markdown
stopped during `EXECUTE` on {{STOP_DATE}}, branch
```

#### TRACK-FREEZE-LIFT-STOP — GCFPE MGMT Change-Process Redesign — Tracking (`3e34590a05eb81e7927efe0541258916`)

After the restoration check passes and Nathan lifts the freeze (P-99). It claims no install. *When:* Only after a stop past X5.0, once the restoration sweep passes (P-99) and Nathan lifts the freeze.

old_str:

```text
**The three decisions below are recorded as
```

new_str:

```markdown
**{{LIFT_DATE}}: the freeze lifted.** `MODIFICATION-20260923-closeout-residuals` stopped on {{STOP_DATE}}; every body it landed was restored and checked unlanded (its record's §E), and Nathan lifted the freeze: flow sessions may run again.
**The three decisions below are recorded as
```

### 7.4 PART-06 — the *Candidate CRD Items List* page

#### 7.4.1 Source

The Drive file `Candidate-CRD-Items-List.md` (`1JPN7WcqCddC2J7UKkHdO4gnIPYRJPGJO`): 31923 B, sha256
`2d7ff0936191e079641f4719c5d39769fc47a6e3dd1e1b84539c5ec7f235b3d3`, modified 2026-09-08T07:25:47.904Z. UTF-8, LF only (0 CR), 296 LF, ends with ".\n\n" (one trailing blank line). one fenced block, lines 119 (```markdown) to 286 (```); inner content 18,624 B, sha256 7108e84a46658c4dfa3a7fc34607bc06d87572967da110ee87bc2c9f2c701c5f (for the F7 byte check).
EXECUTE recomputes both hashes from its own download and stops if either differs.

#### 7.4.2 Method (M2, P-47)

1. **Preconditions:** commit 1 has landed, and X4.6 has passed. `migration_date` is recorded in `EX/run.json`,
   committed and pushed, before anything else (P-96; on a resumed step it is already there). Fetch the Hub: it may
   list no child titled *Candidate CRD Items List*, with one exception (P-95): a child of that title whose callout
   names `MODIFICATION-20260923-closeout-residuals` is this run's page, from a create whose session ended. Then do not
   create again: record its id and URL in `EX/run.json`, read it back against F1 to F10 (step 6), and continue at
   step 7, whose operations are applied only where their new text is not already on the page.
2. **Read** the raw bytes with `download_file_content`, then run `python3 EV/engine/drive_check.py --hub
   3ce4590a05eb814f8892f88ff8539308` (without `--hub` on a resumed step): it decodes the newest download of this
   session in memory and checks the length, both sha256 values and each M2 `old` once outside the fence (X4.6 ran
   the same checks before X5.0; this is the copy the page is made from). Nothing is transcribed by hand.
3. **Rewrite** M2-R1 to R9 below, in memory. Each `old` occurs exactly once outside the fence. R3's text also occurs
   inside the fence, which never changes. The fence content stays byte-identical.
4. **Convert:** the body H1 becomes the title. Add the callout at the top and append the revision bullet to
   *Scope-repair revision record*. The metadata lines become paragraphs; headings and lists are unchanged; the
   blockquote is one `> ` line. Both pipe tables outside the fence become `<table header-row="true">`. The fence
   becomes one `markdown` code block, content unchanged. Nothing is escaped.
5. **Create** with `notion-create-pages` under the Hub (`3ce4590a05eb814f8892f88ff8539308`), with the three
   self-link spots (R4, R5, R9) as the plain text in 7.4.4 (`M2.json` `self_links.create_time_text`). If the call
   rejects the size, create through *Moved-items history* and append the rest with `notion-update-page`, reading back
   after each write. Record `page_id` and the normalized `url` in `EX/run.json`, commit and push, as soon as the
   create returns.
6. **Read back** against F1 to F10 below (F6 counts the 8 pairs here, 11 after step 7). On a failure, fix only the
   failing block and read back again. Never repeat a create.
7. Apply the three step-7 operations in 7.4.4 with `url` from `EX/run.json`, in one `update_content` call
   (`allow_async: false`): each whose new text is not yet on the page, with its `old_str` found exactly once first;
   read back and confirm no `{{` remains.
8. Nathan banners the Drive file as superseded, pointing to the page, once X6.4 has passed and before X7.6, which
   reads the banner back (§P, Product Owner actions; P-102 (e)). After X6.4 the page is permanent.

#### 7.4.3 Readback criteria

- **F1.** The title is *Candidate CRD Items List*, and the parent is the Hub.
- **F2.** The ordered (level, text) headings outside the code block equal the Drive file's 12 H2 and 1 H3.
- **F3.** The active list holds 0 entries in both, and its "Empty" statement is present. The moved-items table holds
  4 data rows in both.
- **F4.** For each moved-items row, all 6 cells are equal after whitespace normalization. Notion links are compared
  by their 32-hex page id.
- **F5.** The review-status table's 6 rows × 2 cells are equal.
- **F6.** Links outside code: the Drive file's 8 (link text, target) pairs are all present: 8 at step 6, and 11 after
  step 7 with the 3 self-links. Notion targets are compared by page id; other targets exactly.
- **F7.** Exactly one code block, language `markdown`, whose content equals the Drive fence's byte for byte after
  LF normalization (18 624 B, sha256 in 7.4.1). Only trailing spaces on a line are tolerated, and are recorded.
- **F8.** List counts: Inclusion 5, Routing 7, Classification 5, Candidate item format 13 (labels equal), and
  Scope-repair record 2 original bullets plus the M2 bullet.
- **F9.** The normalized plain text of every block outside code equals the Drive file's, except the callout, the
  M2 rewrites and the M2 bullet.
- **F10.** The identifiers {1, 2, 3, 4} and the four titles appear in F4 and in the code block's H2s.

#### 7.4.4 The rewrites, callout and revision bullet

- **M2-R1** — Header metadata, line 3 (Updated); before the fence

```text
Updated: 2026-09-08
```

  becomes

```text
Updated: {{MIGRATION_DATE}} (migrated to Notion)
```

- **M2-R2** — Header metadata, line 4 (Document status); before the fence

```text
Document status: Noncanonical development-candidate register; authoritative candidate record in Google Drive
```

  becomes

```text
Document status: Noncanonical development-candidate register; authoritative candidate record in Notion
```

- **M2-R3** — Header metadata, line 5 (Home); before the fence. The same text occurs once more inside the fence (line 123), which must not change.

```text
Home: Google Drive / Glow / Ops / Assessments & Decisions
```

  becomes

```text
Home: Notion / Glow Operations Hub
```

- **M2-R4** — Header metadata, line 7 (Persistent filename); before the fence

```text
Persistent filename: `Candidate-CRD-Items-List.md`
```

  becomes

```text
Persistent page: [Candidate CRD Items List]({{CANDIDATE_CRD_LIST_URL}})
```

- **M2-R5** — Document purpose, paragraph 2, sentence 1 (line 13); before the fence

```text
Keep this exact Drive file in place as the authoritative development-candidate register.
```

  becomes

```text
Keep this exact Notion page, [Candidate CRD Items List]({{CANDIDATE_CRD_LIST_URL}}), in place as the authoritative development-candidate register.
```

- **M2-R6** — Classification test, closing paragraph, sentence 3 (line 49); before the fence

```text
If a decisive answer is missing or disputed, use `Ambiguous — PO Decision Required` in Notion and keep the item out of the active Drive list.
```

  becomes

```text
If a decisive answer is missing or disputed, use `Ambiguous — PO Decision Required` in Notion and keep the item out of the active Candidate CRD Items List.
```

- **M2-R7** — Routing instructions, item 3 (line 86, the whole item); before the fence

```text
3. For a misplaced active Drive entry, mark `Moved to Operational Tracking`, link its one operational item identity, and retain its complete original facts and dated decisions in this file's moved history.
```

  becomes

```text
3. For a misplaced active Candidate CRD Items List entry, mark `Moved to Operational Tracking`, link its one operational item identity, and retain its complete original facts and dated decisions in this page's moved history.
```

- **M2-R8** — Routing instructions, item 4, sentence 2 (line 87); before the fence

```text
Do not add them to the active Drive list while classification remains unresolved.
```

  becomes

```text
Do not add them to the active Candidate CRD Items List while classification remains unresolved.
```

- **M2-R9** — Maintenance rule, sentence 3 (line 290); after the fence

```text
Re-read this exact Drive file immediately before updating it and reconcile newer valid evidence; verify the saved content after each change.
```

  becomes

```text
Re-read this exact Notion page, [Candidate CRD Items List]({{CANDIDATE_CRD_LIST_URL}}), immediately before updating it in place and reconcile newer valid evidence; verify the saved content after each change.
```

Callout (first block of the page; it carries the source's hash for provenance):

```text
Migrated {{MIGRATION_DATE}} from the Google Drive file `Candidate-CRD-Items-List.md` (id `1JPN7WcqCddC2J7UKkHdO4gnIPYRJPGJO`, 31,923 B, sha256 `2d7ff0936191e079641f4719c5d39769fc47a6e3dd1e1b84539c5ec7f235b3d3`, modified 2026-09-08T07:25:47.904Z) under `GCFPE-MGMT-10` and `MODIFICATION-20260923-closeout-residuals` PART-06 (`D25-A`). This page is the list's only store: read and update it here. The Drive file is the Product Owner's reference copy and is not updated. References that named Drive as the store were rewritten; see the Scope-repair revision record.
```

Revision bullet (the third bullet of *Scope-repair revision record*):

```text
- {{MIGRATION_DATE}}: Moved this list from the Google Drive file `Candidate-CRD-Items-List.md` (id `1JPN7WcqCddC2J7UKkHdO4gnIPYRJPGJO`) to this Notion page, Candidate CRD Items List, under MODIFICATION-20260923-closeout-residuals PART-06 (D25-A). This page is now the list's only store. Rewrote the references that named Drive or the file as the list's store: the `Updated`, `Document status`, `Home` and `Persistent filename` (now `Persistent page`) metadata lines, Document purpose paragraph 2 sentence 1, the Classification test closing paragraph, Routing instructions items 3 and 4, and Maintenance rule sentence 3. The pre-repair source in the code block, the 2026-09-08 entry above and all other text are unchanged. The Drive file is the Product Owner's reference copy and is no longer updated.
```

Self-link spots (P-83). At creation (step 5) each is the plain text below; step 7 turns each into the link. Each operation's result equals its M2 rewrite's new text.

- **M2-R4** at creation:

```text
Persistent page: Candidate CRD Items List
```

  step 7 `old_str`:

```text
Persistent page: Candidate CRD Items List
```

  `new_str`:

```text
Persistent page: [Candidate CRD Items List]({{CANDIDATE_CRD_LIST_URL}})
```

- **M2-R5** at creation:

```text
Keep this exact Notion page, Candidate CRD Items List, in place as the authoritative development-candidate register.
```

  step 7 `old_str`:

```text
Keep this exact Notion page, Candidate CRD Items List, in place
```

  `new_str`:

```text
Keep this exact Notion page, [Candidate CRD Items List]({{CANDIDATE_CRD_LIST_URL}}), in place
```

- **M2-R9** at creation:

```text
Re-read this exact Notion page, Candidate CRD Items List, immediately before updating it in place and reconcile newer valid evidence; verify the saved content after each change.
```

  step 7 `old_str`:

```text
Re-read this exact Notion page, Candidate CRD Items List, immediately
```

  `new_str`:

```text
Re-read this exact Notion page, [Candidate CRD Items List]({{CANDIDATE_CRD_LIST_URL}}), immediately
```

#### 7.4.5 Pointer edits (P-46), after the readback passes

The Checklist property *Authoritative Drive register* stays as history (P-45).

#### PART-06-HUB-01 — Glow Operations Hub (`3ce4590a05eb814f8892f88ff8539308`)

 *When:* X5.3; §P step 16 — after the new page's readback passes (X5.1).

old_str:

```text
[Open the authoritative Candidate CRD Items List](https://drive.google.com/file/d/1JPN7WcqCddC2J7UKkHdO4gnIPYRJPGJO/view?usp=drivesdk), maintained in place at Glow / Ops / Assessments & Decisions as `Candidate-CRD-Items-List.md`.
```

new_str:

```markdown
[Open the Candidate CRD Items List]({{CANDIDATE_CRD_LIST_URL}}), a Notion page under this Hub and the list's only store (`D25-A`); `CL-40` updates it in place under the destination rule in `docs/prompt_ecosystem_management/notion-write-boundary.md`. The Drive file `Candidate-CRD-Items-List.md` (`1JPN7WcqCddC2J7UKkHdO4gnIPYRJPGJO`), which held the list until {{MIGRATION_DATE}}, is Nathan's reference copy and is not updated. (Corrected {{EXECUTE_DATE}}: this line named the Drive file as the authoritative list.)
```

#### PART-06-HUB-02 — Glow Operations Hub (`3ce4590a05eb814f8892f88ff8539308`)

 *When:* X5.3; §P step 16 — after the new page's readback passes (X5.1).

old_str:

```text
Their original identities and complete source history are preserved in the Drive moved-items history.
```

new_str:

```markdown
Their original identities and complete source history are preserved in the list's moved-items history, which moved with it from Drive.
```

#### PART-06-HUB-03 — Glow Operations Hub (`3ce4590a05eb814f8892f88ff8539308`)

 *When:* X5.3; §P step 16 — after the new page's readback passes (X5.1).

old_str:

```text
Keep ambiguous items in Notion and out of the active Drive list.
```

new_str:

```markdown
Keep ambiguous items in Notion and out of the active [Candidate CRD Items List]({{CANDIDATE_CRD_LIST_URL}}).
```

#### PART-06-ITEM1-01 — Repository prompt-use provenance helper (`3d54590a05eb8142a187d32ad4435950`)

 *When:* X5.3; §P step 16 — after the new page's readback passes (X5.1).

old_str:

```text
- [Authoritative Drive register and complete moved-item history](https://drive.google.com/file/d/1JPN7WcqCddC2J7UKkHdO4gnIPYRJPGJO/view)
```

new_str:

```markdown
- [Candidate CRD Items List — the list and its complete moved-item history]({{CANDIDATE_CRD_LIST_URL}})
- [Drive reference copy of the list, not updated after the move to Notion](https://drive.google.com/file/d/1JPN7WcqCddC2J7UKkHdO4gnIPYRJPGJO/view)
```

#### PART-06-ITEM1-02 — Repository prompt-use provenance helper (`3d54590a05eb8142a187d32ad4435950`)

 *When:* X5.3; §P step 16 — after the new page's readback passes (X5.1).

old_str:

```text
Preserve the original local number and all dated facts in the same Drive file. This row is the current item-level tracking identity; other references are evidence or historical pointers.
```

new_str:

```markdown
Preserve the original local number and all dated facts in the same Drive file. This row is the current item-level tracking identity; other references are evidence or historical pointers.
{{MIGRATION_DATE}}: the Candidate CRD Items List moved from the Drive file to the Notion page [Candidate CRD Items List]({{CANDIDATE_CRD_LIST_URL}}) (`D25-A`; `MODIFICATION-20260923-closeout-residuals` PART-06). This item's original local number and dated facts are preserved there, in its moved-items history; the Drive file is Nathan's reference copy and is not updated.
```

#### PART-06-ITEM2-01 — QA-10 substantive, paste-ready PF10 findings summary (`3d54590a05eb8119affafcfb024ba990`)

 *When:* X5.3; §P step 16 — after the new page's readback passes (X5.1).

old_str:

```text
- [Authoritative Drive register and complete moved-item history](https://drive.google.com/file/d/1JPN7WcqCddC2J7UKkHdO4gnIPYRJPGJO/view)
```

new_str:

```markdown
- [Candidate CRD Items List — the list and its complete moved-item history]({{CANDIDATE_CRD_LIST_URL}})
- [Drive reference copy of the list, not updated after the move to Notion](https://drive.google.com/file/d/1JPN7WcqCddC2J7UKkHdO4gnIPYRJPGJO/view)
```

#### PART-06-ITEM2-02 — QA-10 substantive, paste-ready PF10 findings summary (`3d54590a05eb8119affafcfb024ba990`)

 *When:* X5.3; §P step 16 — after the new page's readback passes (X5.1).

old_str:

```text
Preserve the original local number and all dated facts in the same Drive file. This row is the current item-level tracking identity; other references are evidence or historical pointers.
```

new_str:

```markdown
Preserve the original local number and all dated facts in the same Drive file. This row is the current item-level tracking identity; other references are evidence or historical pointers.
{{MIGRATION_DATE}}: the Candidate CRD Items List moved from the Drive file to the Notion page [Candidate CRD Items List]({{CANDIDATE_CRD_LIST_URL}}) (`D25-A`; `MODIFICATION-20260923-closeout-residuals` PART-06). This item's original local number and dated facts are preserved there, in its moved-items history; the Drive file is Nathan's reference copy and is not updated.
```

#### PART-06-ITEM3-01 — QA-90 explicit Product Owner task selection (`3d54590a05eb8159a73cf6af261c1c2b`)

 *When:* X5.3; §P step 16 — after the new page's readback passes (X5.1).

old_str:

```text
- [Authoritative Drive register and complete moved-item history](https://drive.google.com/file/d/1JPN7WcqCddC2J7UKkHdO4gnIPYRJPGJO/view)
```

new_str:

```markdown
- [Candidate CRD Items List — the list and its complete moved-item history]({{CANDIDATE_CRD_LIST_URL}})
- [Drive reference copy of the list, not updated after the move to Notion](https://drive.google.com/file/d/1JPN7WcqCddC2J7UKkHdO4gnIPYRJPGJO/view)
```

#### PART-06-ITEM3-02 — QA-90 explicit Product Owner task selection (`3d54590a05eb8159a73cf6af261c1c2b`)

 *When:* X5.3; §P step 16 — after the new page's readback passes (X5.1).

old_str:

```text
Preserve the original local number and all dated facts in the same Drive file. This row is the current item-level tracking identity; other references are evidence or historical pointers.
```

new_str:

```markdown
Preserve the original local number and all dated facts in the same Drive file. This row is the current item-level tracking identity; other references are evidence or historical pointers.
{{MIGRATION_DATE}}: the Candidate CRD Items List moved from the Drive file to the Notion page [Candidate CRD Items List]({{CANDIDATE_CRD_LIST_URL}}) (`D25-A`; `MODIFICATION-20260923-closeout-residuals` PART-06). This item's original local number and dated facts are preserved there, in its moved-items history; the Drive file is Nathan's reference copy and is not updated.
```

#### PART-06-ITEM4-01 — Combined audit-and-plan invocations for IA and QA preparation (`3d54590a05eb8118b229e0ca25bdfd42`)

 *When:* X5.3; §P step 16 — after the new page's readback passes (X5.1).

old_str:

```text
- [Authoritative Drive register and complete moved-item history](https://drive.google.com/file/d/1JPN7WcqCddC2J7UKkHdO4gnIPYRJPGJO/view)
```

new_str:

```markdown
- [Candidate CRD Items List — the list and its complete moved-item history]({{CANDIDATE_CRD_LIST_URL}})
- [Drive reference copy of the list, not updated after the move to Notion](https://drive.google.com/file/d/1JPN7WcqCddC2J7UKkHdO4gnIPYRJPGJO/view)
```

#### PART-06-ITEM4-02 — Combined audit-and-plan invocations for IA and QA preparation (`3d54590a05eb8118b229e0ca25bdfd42`)

 *When:* X5.3; §P step 16 — after the new page's readback passes (X5.1).

old_str:

```text
Preserve the original local number and all dated facts in the same Drive file. This row is the current item-level tracking identity; other references are evidence or historical pointers.
```

new_str:

```markdown
Preserve the original local number and all dated facts in the same Drive file. This row is the current item-level tracking identity; other references are evidence or historical pointers.
{{MIGRATION_DATE}}: the Candidate CRD Items List moved from the Drive file to the Notion page [Candidate CRD Items List]({{CANDIDATE_CRD_LIST_URL}}) (`D25-A`; `MODIFICATION-20260923-closeout-residuals` PART-06). This item's original local number and dated facts are preserved there, in its moved-items history; the Drive file is Nathan's reference copy and is not updated.
```

## §8 Dry-run evidence

**Pass 1** (7 batches, rule level): all 51 bodies passed after the data fixes now in the engine (P-40, the CF-x-20
comma, P-15 revised, P-18, P-19, P-37, P-38). **Pass 2** (6 batches, the complete check): the merged engine, the
repaired registry and guard file, and the final skill tree's validator. It covered the 50 live bodies, the proposed
MGMT-10 body and the five untouched live bodies (CF-PO-10, MGR-10, IA-40, IA-50, IA-60), which show that the new
all-rows guards are silent where nothing changes. **Pass 3** (§8.2) ran `land.py` itself; **pass 4** (§8.3) ran it
again after repair round 4, with the readback each landing will run (P-76); **pass 5** (§8.4) ran it after repair
round 5, with the landing-state proof (P-88); **pass 6** (§8.5) ran it after repair round 6, through `land.py`'s own
refusal chain (P-96). §8.7 records the round-6 helpers run on today's pages.

### 8.1 Pass 2

| body | pass | failures |
|---|---|---|
| CF-C-10 | True | 0 |
| CF-C-20 | True | 0 |
| CF-C-30 | True | 0 |
| CF-C-40 | True | 0 |
| CF-E-10 | True | 0 |
| CF-E-20 | True | 0 |
| CF-E-30 | True | 0 |
| CF-E-40 | True | 0 |
| CF-PO-10 | True | 0 |
| CL-20 | True | 0 |
| CL-30 | True | 0 |
| CL-40 | True | 0 |
| CL-C-10 | True | 0 |
| CL-E-10 | True | 0 |
| CL-E-20 | True | 0 |
| CL-E-30 | True | 0 |
| CL-E-40 | True | 0 |
| DOC-10 | True | 0 |
| DOC-20 | True | 0 |
| ESC-10 | True | 0 |
| ESC-25 | True | 0 |
| ESC-30 | True | 0 |
| ESC-40 | True | 0 |
| GCFPE-MGMT-10 | True | 0 |
| GCFPE-MGMT-10-PROPOSED | True | 0 |
| IA-10 | True | 0 |
| IA-20 | True | 0 |
| IA-30 | True | 0 |
| IA-40 | True | 0 |
| IA-50 | True | 0 |
| IA-60 | True | 0 |
| MGR-10 | True | 0 |
| OPS-10 | True | 0 |
| OPS-20 | True | 0 |
| OPS-30 | True | 0 |
| PR-10 | True | 0 |
| PR-20 | True | 0 |
| PR-30 | True | 0 |
| PR-35 | True | 0 |
| PR-40 | True | 0 |
| PR-50 | True | 0 |
| QA-10 | True | 0 |
| QA-100 | True | 0 |
| QA-110 | True | 0 |
| QA-120 | True | 0 |
| QA-20 | True | 0 |
| QA-50 | True | 0 |
| QA-60 | True | 0 |
| QA-70 | True | 0 |
| QA-80 | True | 0 |
| QA-90 | True | 0 |
| RS-10 | True | 0 |
| RS-20 | True | 0 |
| RS-30 | True | 0 |
| RS-40 | True | 0 |
| UTIL-10 | True | 0 |

Passed: 56 of 56.

### 8.2 Pass 3 — the landing rehearsal

What ran: land.py plan --no-ops (51 bodies with edits) and land.py check (5 untouched) on fresh fetches, with the new registry (sha256 97bda1a0...) and the full patched skills root ($PKG, freeze 323 047ca742...); graph_check.py --simulate for QA-110 and QA-80. Run: 2026-09-24; batches P2, P4, P5 by workflow agents (wf_a465047b-110); P1, P3, P6 and the graph check in the main session after the permission classifier stopped the script inside those three agents. Each body was fetched fresh and the engine ran on that fetch at once;
the candidate URL is a placeholder of the right form (https://app.notion.com/p/00000000000000000000000000000000 (placeholder of the right form)), so R-ITEM18 is exercised with a filled
token.

Result: 51 of 51 bodies plan with no refusal and a passing precheck; 5 of 5 untouched
bodies pass `check`; the graph check passes; refusals 0. Each
result is in `EV/dryrun/pass3/<batch>/<PID>.json` (counts, rule hits, the precheck; no body text).

| body | mode | exit | refused | pass | operations |
|---|---|---|---|---|---|
| CF-C-10 | plan | 0 | — | True | 2 |
| CF-C-20 | plan | 0 | — | True | 2 |
| CF-C-30 | plan | 0 | — | True | 1 |
| CF-C-40 | plan | 0 | — | True | 1 |
| CF-E-10 | plan | 0 | — | True | 2 |
| CF-E-20 | plan | 0 | — | True | 2 |
| CF-E-30 | plan | 0 | — | True | 1 |
| CF-E-40 | plan | 0 | — | True | 1 |
| CF-PO-10 | check | 0 | — | True | — |
| CL-20 | plan | 0 | — | True | 10 |
| CL-30 | plan | 0 | — | True | 10 |
| CL-40 | plan | 0 | — | True | 5 |
| CL-C-10 | plan | 0 | — | True | 11 |
| CL-E-10 | plan | 0 | — | True | 11 |
| CL-E-20 | plan | 0 | — | True | 3 |
| CL-E-30 | plan | 0 | — | True | 2 |
| CL-E-40 | plan | 0 | — | True | 2 |
| DOC-10 | plan | 0 | — | True | 5 |
| DOC-20 | plan | 0 | — | True | 7 |
| ESC-10 | plan | 0 | — | True | 3 |
| ESC-25 | plan | 0 | — | True | 4 |
| ESC-30 | plan | 0 | — | True | 3 |
| ESC-40 | plan | 0 | — | True | 3 |
| GCFPE-MGMT-10 | plan | 0 | — | True | 2 |
| GCFPE-MGMT-10-PROPOSED | plan | 0 | — | True | 2 |
| IA-10 | plan | 0 | — | True | 1 |
| IA-20 | plan | 0 | — | True | 1 |
| IA-30 | plan | 0 | — | True | 3 |
| IA-40 | check | 0 | — | True | — |
| IA-50 | check | 0 | — | True | — |
| IA-60 | check | 0 | — | True | — |
| MGR-10 | check | 0 | — | True | — |
| OPS-10 | plan | 0 | — | True | 10 |
| OPS-20 | plan | 0 | — | True | 9 |
| OPS-30 | plan | 0 | — | True | 15 |
| PR-10 | plan | 0 | — | True | 15 |
| PR-20 | plan | 0 | — | True | 19 |
| PR-30 | plan | 0 | — | True | 11 |
| PR-35 | plan | 0 | — | True | 8 |
| PR-40 | plan | 0 | — | True | 23 |
| PR-50 | plan | 0 | — | True | 1 |
| QA-10 | plan | 0 | — | True | 18 |
| QA-100 | plan | 0 | — | True | 2 |
| QA-110 | plan | 0 | — | True | 3 |
| QA-120 | plan | 0 | — | True | 2 |
| QA-20 | plan | 0 | — | True | 3 |
| QA-50 | plan | 0 | — | True | 2 |
| QA-60 | plan | 0 | — | True | 2 |
| QA-70 | plan | 0 | — | True | 2 |
| QA-80 | plan | 0 | — | True | 3 |
| QA-90 | plan | 0 | — | True | 2 |
| RS-10 | plan | 0 | — | True | 3 |
| RS-20 | plan | 0 | — | True | 4 |
| RS-30 | plan | 0 | — | True | 2 |
| RS-40 | plan | 0 | — | True | 2 |
| UTIL-10 | plan | 0 | — | True | 1 |
| graph_check | graph | 0 | — | True | — |

### 8.3 Pass 4 — the rehearsal with the readback (P-76)

What ran: land.py plan --no-ops on the 51 bodies with edits (precheck and landed check, CL-40 with the page-URL placeholder filled) and land.py check on the 5 untouched, on fresh fetches, with the new registry (97bda1a0...) and the full patched skills root ($PKG, freeze 323 047ca742...); graph_check.py --simulate for QA-110 and QA-80. Run: 2026-09-24; batches P2, P4 and parts of P1/P5 by workflow agents (wf_ce55a240-5a1); the rest in the main session after the permission classifier stopped the script in those agents.

Result: 51 of 51 bodies plan with no refusal, a passing precheck and a passing landed check (the
readback `check` runs after the landing, STALE test included, on the text the operations produce); 5
of 5 untouched bodies pass `check`; the graph check passes; refusals
0. Each result is in `EV/dryrun/pass4/<batch>/<PID>.json` (counts, rule hits, both checks; no body text).

| body | mode | exit | refused | precheck | landed check | operations |
|---|---|---|---|---|---|---|
| CF-C-10 | plan | 0 | — | True | True | 2 |
| CF-C-20 | plan | 0 | — | True | True | 2 |
| CF-C-30 | plan | 0 | — | True | True | 1 |
| CF-C-40 | plan | 0 | — | True | True | 1 |
| CF-E-10 | plan | 0 | — | True | True | 2 |
| CF-E-20 | plan | 0 | — | True | True | 2 |
| CF-E-30 | plan | 0 | — | True | True | 1 |
| CF-E-40 | plan | 0 | — | True | True | 1 |
| CF-PO-10 | check | 0 | — | — | True | — |
| CL-20 | plan | 0 | — | True | True | 10 |
| CL-30 | plan | 0 | — | True | True | 10 |
| CL-40 | plan | 0 | — | True | True | 5 |
| CL-C-10 | plan | 0 | — | True | True | 11 |
| CL-E-10 | plan | 0 | — | True | True | 11 |
| CL-E-20 | plan | 0 | — | True | True | 3 |
| CL-E-30 | plan | 0 | — | True | True | 2 |
| CL-E-40 | plan | 0 | — | True | True | 2 |
| DOC-10 | plan | 0 | — | True | True | 5 |
| DOC-20 | plan | 0 | — | True | True | 7 |
| ESC-10 | plan | 0 | — | True | True | 3 |
| ESC-25 | plan | 0 | — | True | True | 4 |
| ESC-30 | plan | 0 | — | True | True | 3 |
| ESC-40 | plan | 0 | — | True | True | 3 |
| GCFPE-MGMT-10 | plan | 0 | — | True | True | 2 |
| GCFPE-MGMT-10-PROPOSED | plan | 0 | — | True | True | 2 |
| IA-10 | plan | 0 | — | True | True | 1 |
| IA-20 | plan | 0 | — | True | True | 1 |
| IA-30 | plan | 0 | — | True | True | 3 |
| IA-40 | check | 0 | — | — | True | — |
| IA-50 | check | 0 | — | — | True | — |
| IA-60 | check | 0 | — | — | True | — |
| MGR-10 | check | 0 | — | — | True | — |
| OPS-10 | plan | 0 | — | True | True | 10 |
| OPS-20 | plan | 0 | — | True | True | 9 |
| OPS-30 | plan | 0 | — | True | True | 15 |
| PR-10 | plan | 0 | — | True | True | 15 |
| PR-20 | plan | 0 | — | True | True | 19 |
| PR-30 | plan | 0 | — | True | True | 11 |
| PR-35 | plan | 0 | — | True | True | 8 |
| PR-40 | plan | 0 | — | True | True | 23 |
| PR-50 | plan | 0 | — | True | True | 1 |
| QA-10 | plan | 0 | — | True | True | 18 |
| QA-100 | plan | 0 | — | True | True | 2 |
| QA-110 | plan | 0 | — | True | True | 3 |
| QA-120 | plan | 0 | — | True | True | 2 |
| QA-20 | plan | 0 | — | True | True | 3 |
| QA-50 | plan | 0 | — | True | True | 2 |
| QA-60 | plan | 0 | — | True | True | 2 |
| QA-70 | plan | 0 | — | True | True | 2 |
| QA-80 | plan | 0 | — | True | True | 3 |
| QA-90 | plan | 0 | — | True | True | 2 |
| RS-10 | plan | 0 | — | True | True | 3 |
| RS-20 | plan | 0 | — | True | True | 4 |
| RS-30 | plan | 0 | — | True | True | 2 |
| RS-40 | plan | 0 | — | True | True | 2 |
| UTIL-10 | plan | 0 | — | True | True | 1 |
| graph_check | graph | 0 | — | — | True | — |

### 8.4 Pass 5 — forward repair and re-planning (P-88)

What ran: land.py plan --no-ops on the 51 bodies with edits and land.py check on the 5 untouched, on fresh fetches, with the new registry (97bda1a0...) and the full patched skills root ($PKG, freeze 323 047ca742...), plus, per plan body and in memory on the same fetch, the landing-state proof (P-88); graph_check.py --simulate for QA-110 and QA-80. Run: 2026-09-24, main session.

Result: 51 of 51 bodies plan with no refusal, `repair` `[]`, a passing precheck and landed check, and a
passing state proof; 5 of 5 untouched bodies pass `check`; the graph check
passes; refusals 0. The state proof, per body, on the same
fetch: every edit reads `NOT_LANDED` before the landing (51 of 51); on the landed text every
edit reads `LANDED` (51 of 51; pass 5 computed this from `edit_states`, and pass 6 ran `plan`
itself on the landed text, §8.5); no insertion is doubled (51 of 51). It tried 2n subsets per body
(each operation left out alone, and each applied alone): 516 rows, of which 476 are distinct partial
landings; the rest repeat a subset (a body with two operations gives the same two subsets both ways) or are not
partial (a body with one operation). Of the rows, 450 are repaired to exactly the landed
text, 66 are refused, and 0 are repaired to anything else. Each
result is in `EV/dryrun/pass5/<batch>/<PID>.json` (counts, edit ids, booleans; no body text).

During the pass: QA-10's first run: state proof FAILED: on the landed text R-OWN read MIXED (relanded_not_LANDED ['R-OWN']), because LQA-10-P03 rewrites the sentence R-OWN is anchored after; 36 partials, 12 repaired exact, 24 refused, 0 wrong. Fix: closeout_rules.OWN_AT['QA-10'] matches that sentence before or after LQA-10-P03 (P-88); read only for QA-10, so the 50 other rows, run before the fix, are unaffected.
QA-10's re-run: state proof passes; 24 repaired exact, 12 refused, 0 wrong (the row below).

On synthetic text (`EV/dryrun/synthetic/`), every one of the 8 subsets of CL-E-20's 3
operations was landed and then planned: all behave as above, and an insertion
added twice fails `check` (`doubled_insertions` ['R-OWN']).

| body | mode | exit | refused | precheck | landed check | operations | partials repaired / refused / wrong |
|---|---|---|---|---|---|---|---|
| CF-C-10 | plan | 0 | — | True | True | 2 | 4 / 0 / 0 |
| CF-C-20 | plan | 0 | — | True | True | 2 | 4 / 0 / 0 |
| CF-C-30 | plan | 0 | — | True | True | 1 | 1 / 0 / 0 |
| CF-C-40 | plan | 0 | — | True | True | 1 | 1 / 0 / 0 |
| CF-E-10 | plan | 0 | — | True | True | 2 | 4 / 0 / 0 |
| CF-E-20 | plan | 0 | — | True | True | 2 | 4 / 0 / 0 |
| CF-E-30 | plan | 0 | — | True | True | 1 | 1 / 0 / 0 |
| CF-E-40 | plan | 0 | — | True | True | 1 | 1 / 0 / 0 |
| CF-PO-10 | check | 0 | — | — | True | — | — |
| CL-20 | plan | 0 | — | True | True | 10 | 20 / 0 / 0 |
| CL-30 | plan | 0 | — | True | True | 10 | 20 / 0 / 0 |
| CL-40 | plan | 0 | — | True | True | 5 | 10 / 0 / 0 |
| CL-C-10 | plan | 0 | — | True | True | 11 | 22 / 0 / 0 |
| CL-E-10 | plan | 0 | — | True | True | 11 | 22 / 0 / 0 |
| CL-E-20 | plan | 0 | — | True | True | 3 | 6 / 0 / 0 |
| CL-E-30 | plan | 0 | — | True | True | 2 | 4 / 0 / 0 |
| CL-E-40 | plan | 0 | — | True | True | 2 | 4 / 0 / 0 |
| DOC-10 | plan | 0 | — | True | True | 5 | 10 / 0 / 0 |
| DOC-20 | plan | 0 | — | True | True | 7 | 14 / 0 / 0 |
| ESC-10 | plan | 0 | — | True | True | 3 | 6 / 0 / 0 |
| ESC-25 | plan | 0 | — | True | True | 4 | 8 / 0 / 0 |
| ESC-30 | plan | 0 | — | True | True | 3 | 6 / 0 / 0 |
| ESC-40 | plan | 0 | — | True | True | 3 | 6 / 0 / 0 |
| GCFPE-MGMT-10 | plan | 0 | — | True | True | 2 | 4 / 0 / 0 |
| GCFPE-MGMT-10-PROPOSED | plan | 0 | — | True | True | 2 | 4 / 0 / 0 |
| IA-10 | plan | 0 | — | True | True | 1 | 1 / 0 / 0 |
| IA-20 | plan | 0 | — | True | True | 1 | 1 / 0 / 0 |
| IA-30 | plan | 0 | — | True | True | 3 | 6 / 0 / 0 |
| IA-40 | check | 0 | — | — | True | — | — |
| IA-50 | check | 0 | — | — | True | — | — |
| IA-60 | check | 0 | — | — | True | — | — |
| MGR-10 | check | 0 | — | — | True | — | — |
| OPS-10 | plan | 0 | — | True | True | 10 | 12 / 8 / 0 |
| OPS-20 | plan | 0 | — | True | True | 9 | 10 / 8 / 0 |
| OPS-30 | plan | 0 | — | True | True | 15 | 20 / 10 / 0 |
| PR-10 | plan | 0 | — | True | True | 15 | 22 / 8 / 0 |
| PR-20 | plan | 0 | — | True | True | 19 | 30 / 8 / 0 |
| PR-30 | plan | 0 | — | True | True | 11 | 22 / 0 / 0 |
| PR-35 | plan | 0 | — | True | True | 8 | 16 / 0 / 0 |
| PR-40 | plan | 0 | — | True | True | 23 | 34 / 12 / 0 |
| PR-50 | plan | 0 | — | True | True | 1 | 1 / 0 / 0 |
| QA-10 | plan | 0 | — | True | True | 18 | 24 / 12 / 0 |
| QA-100 | plan | 0 | — | True | True | 2 | 4 / 0 / 0 |
| QA-110 | plan | 0 | — | True | True | 3 | 6 / 0 / 0 |
| QA-120 | plan | 0 | — | True | True | 2 | 4 / 0 / 0 |
| QA-20 | plan | 0 | — | True | True | 3 | 6 / 0 / 0 |
| QA-50 | plan | 0 | — | True | True | 2 | 4 / 0 / 0 |
| QA-60 | plan | 0 | — | True | True | 2 | 4 / 0 / 0 |
| QA-70 | plan | 0 | — | True | True | 2 | 4 / 0 / 0 |
| QA-80 | plan | 0 | — | True | True | 3 | 6 / 0 / 0 |
| QA-90 | plan | 0 | — | True | True | 2 | 4 / 0 / 0 |
| RS-10 | plan | 0 | — | True | True | 3 | 6 / 0 / 0 |
| RS-20 | plan | 0 | — | True | True | 4 | 8 / 0 / 0 |
| RS-30 | plan | 0 | — | True | True | 2 | 4 / 0 / 0 |
| RS-40 | plan | 0 | — | True | True | 2 | 4 / 0 / 0 |
| UTIL-10 | plan | 0 | — | True | True | 1 | 1 / 0 / 0 |
| graph_check | graph | 0 | — | — | True | — | — |

### 8.5 Pass 6 — the refusal chain itself (P-96)

What ran: land.py plan --no-ops on the 51 bodies with edits and land.py check on the 5 untouched, on fresh fetches, with the new registry (97bda1a0...) and the full patched skills root ($PKG, freeze 323 047ca742...), on the round-6 engine (land.py check STALE unconditional, plan refusal order, state mode; P-96, P-98); plus, per plan body and in memory on the same fetch, through land.py's own main(): state UNTOUCHED on the fetch and LANDED on the landed text, plan on the landed text refused ALREADY_LANDED, every distinct partial landing (each operation left out alone and each applied alone) read PARTIAL and either repaired to exactly the landed text or refused; graph_check.py --simulate for QA-110 and QA-80. Run: 2026-09-24, main session.

Result: 51 of 51 bodies plan with no refusal, `repair` `[]`, a passing precheck and landed check, and a
passing proof; 5 of 5 untouched bodies pass `check`; the graph check
passes; refusals 0. The proof, per body, through `land.py`'s
`main()` on the same fetch: `state` reads `UNTOUCHED` on the fetch (51 of 51) and `LANDED`
on the landed text (51 of 51); `plan` on the landed text exits 3 with `ALREADY_LANDED`
(51 of 51, the deletion-only and replacement-only bodies included); no insertion is
doubled (51 of 51). Of 476 distinct partial landings, 476
read `PARTIAL`; `plan` repairs 410 to exactly the landed text and refuses
66 (COUNT_MISMATCH, on OPS-10, OPS-20, OPS-30, PR-10, PR-20, PR-40, QA-10);
0 are repaired to anything else. A refused partial stops the unit (P-98). Each result is
in `EV/dryrun/pass6/<batch>/<PID>.json` (counts, edit ids, booleans; no body text). Pass 6 ran before the engine read
only the running session's harness files (P-101); every file it read belongs to this session, the only one in the
project directory, so its selections stand.

| body | mode | exit | refused | precheck | landed check | operations | partials repaired / refused / wrong |
|---|---|---|---|---|---|---|---|
| CF-C-10 | plan | 0 | — | True | True | 2 | 2 / 0 / 0 |
| CF-C-20 | plan | 0 | — | True | True | 2 | 2 / 0 / 0 |
| CF-C-30 | plan | 0 | — | True | True | 1 | 0 / 0 / 0 |
| CF-C-40 | plan | 0 | — | True | True | 1 | 0 / 0 / 0 |
| CF-E-10 | plan | 0 | — | True | True | 2 | 2 / 0 / 0 |
| CF-E-20 | plan | 0 | — | True | True | 2 | 2 / 0 / 0 |
| CF-E-30 | plan | 0 | — | True | True | 1 | 0 / 0 / 0 |
| CF-E-40 | plan | 0 | — | True | True | 1 | 0 / 0 / 0 |
| CF-PO-10 | check | 0 | — | — | True | — | — |
| CL-20 | plan | 0 | — | True | True | 10 | 20 / 0 / 0 |
| CL-30 | plan | 0 | — | True | True | 10 | 20 / 0 / 0 |
| CL-40 | plan | 0 | — | True | True | 5 | 10 / 0 / 0 |
| CL-C-10 | plan | 0 | — | True | True | 11 | 22 / 0 / 0 |
| CL-E-10 | plan | 0 | — | True | True | 11 | 22 / 0 / 0 |
| CL-E-20 | plan | 0 | — | True | True | 3 | 6 / 0 / 0 |
| CL-E-30 | plan | 0 | — | True | True | 2 | 2 / 0 / 0 |
| CL-E-40 | plan | 0 | — | True | True | 2 | 2 / 0 / 0 |
| DOC-10 | plan | 0 | — | True | True | 5 | 10 / 0 / 0 |
| DOC-20 | plan | 0 | — | True | True | 7 | 14 / 0 / 0 |
| ESC-10 | plan | 0 | — | True | True | 3 | 6 / 0 / 0 |
| ESC-25 | plan | 0 | — | True | True | 4 | 8 / 0 / 0 |
| ESC-30 | plan | 0 | — | True | True | 3 | 6 / 0 / 0 |
| ESC-40 | plan | 0 | — | True | True | 3 | 6 / 0 / 0 |
| GCFPE-MGMT-10 | plan | 0 | — | True | True | 2 | 2 / 0 / 0 |
| GCFPE-MGMT-10-PROPOSED | plan | 0 | — | True | True | 2 | 2 / 0 / 0 |
| IA-10 | plan | 0 | — | True | True | 1 | 0 / 0 / 0 |
| IA-20 | plan | 0 | — | True | True | 1 | 0 / 0 / 0 |
| IA-30 | plan | 0 | — | True | True | 3 | 6 / 0 / 0 |
| IA-40 | check | 0 | — | — | True | — | — |
| IA-50 | check | 0 | — | — | True | — | — |
| IA-60 | check | 0 | — | — | True | — | — |
| MGR-10 | check | 0 | — | — | True | — | — |
| OPS-10 | plan | 0 | — | True | True | 10 | 12 / 8 / 0 |
| OPS-20 | plan | 0 | — | True | True | 9 | 10 / 8 / 0 |
| OPS-30 | plan | 0 | — | True | True | 15 | 20 / 10 / 0 |
| PR-10 | plan | 0 | — | True | True | 15 | 22 / 8 / 0 |
| PR-20 | plan | 0 | — | True | True | 19 | 30 / 8 / 0 |
| PR-30 | plan | 0 | — | True | True | 11 | 22 / 0 / 0 |
| PR-35 | plan | 0 | — | True | True | 8 | 16 / 0 / 0 |
| PR-40 | plan | 0 | — | True | True | 23 | 34 / 12 / 0 |
| PR-50 | plan | 0 | — | True | True | 1 | 0 / 0 / 0 |
| QA-10 | plan | 0 | — | True | True | 18 | 24 / 12 / 0 |
| QA-100 | plan | 0 | — | True | True | 2 | 2 / 0 / 0 |
| QA-110 | plan | 0 | — | True | True | 3 | 6 / 0 / 0 |
| QA-120 | plan | 0 | — | True | True | 2 | 2 / 0 / 0 |
| QA-20 | plan | 0 | — | True | True | 3 | 6 / 0 / 0 |
| QA-50 | plan | 0 | — | True | True | 2 | 2 / 0 / 0 |
| QA-60 | plan | 0 | — | True | True | 2 | 2 / 0 / 0 |
| QA-70 | plan | 0 | — | True | True | 2 | 2 / 0 / 0 |
| QA-80 | plan | 0 | — | True | True | 3 | 6 / 0 / 0 |
| QA-90 | plan | 0 | — | True | True | 2 | 2 / 0 / 0 |
| RS-10 | plan | 0 | — | True | True | 3 | 6 / 0 / 0 |
| RS-20 | plan | 0 | — | True | True | 4 | 8 / 0 / 0 |
| RS-30 | plan | 0 | — | True | True | 2 | 2 / 0 / 0 |
| RS-40 | plan | 0 | — | True | True | 2 | 2 / 0 / 0 |
| UTIL-10 | plan | 0 | — | True | True | 1 | 0 / 0 / 0 |
| graph_check | graph | 0 | — | — | True | — | — |

### 8.6 The EXECUTE sequence, in §9 order

`EV/skills/results/gate_proof_x.json`: the committed manifest's execute commands, run literally in spec §9 order on a fresh copy of the repository (scratch), 2026-09-24, after repair round 5 (the guarded rm forms, P-92; X4.3's digest comparison by diff). Order: X0.3(b), X1.1, X1.2, X1.3 pre, X2.1 (texts X2.2), X3.1 registry.diff, X3.2 execute.2, X3.3 execute.3, X3.4 (texts X3.5), X4.1 execute.4, X4.2 pkg, X4.3 execute.4b (package, extract, compare), X7.4 post with $PKG standing in for the installed root. Every command exited as the manifest
expects (True); X4.1's plain diff of the 4.1.0 and 4.1.1 contracts exits 1 by design (two changed lines, manifest execute.4 expected). The whole skills root is measured and compared within each run (P-79). Each step keeps its full output (at most 400 lines: the first and last 200); paths are shown as $SCRATCH and $REPO. `pre` 12/12,
`pkg` 34/34, `post` 28/28.
The registry after X3.1 is `97bda1a06b0c917fa66bdfb098e9d9c0b5d394f16d62a3bfa953f16253219015`; the reindex diff is byte-equal to the stored one; the second
reindex rewrites 0 files; the contract regenerates to `6902924a…` (4.1.0) and `dbae180b…` (4.1.1), EQUAL to both
bundled copies each time.

Packaging (X4.3, `execute.4b`) ran in the same sequence: 7 `Skill is valid!`, and
the comparison of the seven extracted freeze lines with `expected_after_patch.txt` exited
0 (P-92). The file keeps up to 400 lines of each step's output (the first and
last 200). What it covers is round 5's manifest commands: it did not run X0.3 (a), (c) or (d), X3.1's validator and
deriver, X3.6, X4.4 to X4.6, X5 or X6, which pass 6 and §8.7 cover. Repair round 6 changed three manifest entries:
`execute.4b`'s `packages_json.py`, `execute.5`'s `EX/installed_freeze.txt` and the new `execute.6`. Each was run at
PLAN (`EV/skills/results/manifest_r6_proof.json`: `execute.5` with the patched root standing in for `$INST`, diff exit
0; `execute.6` on the working tree, diff exit 0). It applied the X2.2 and X3.5 texts with the PLAN
copy of the applier; `EV/texts/apply_texts.py`, committed in repair round 6, gives the same X2.2 result
(`EV/texts/apply_texts_proof.json`: `gcfpe.decision-record.md` sha256 `6742d593…`, 101 936 B).

### 8.7 The round-6 helpers, on today's pages (P-96 to P-102)

- **Control pages** (`EV/notion/ctrl_proof.py` → `ctrl_proof.out.json`, stand-in values in `ctrl_proof.run.json`):
  24 edits on 7 live pages, applied in memory in §9 order. The success sequence
  (19 steps) and the stop sequence (34 steps: the reversals, the
  stop lines and the lift line) each pass every step's test: all_ok True. A resume with the same `run.json`
  reads every landed edit `LANDED`; with the execute date moved one day, as round 5 would have filled it, the test
  misses PART-06-HUB-01, PART-11-TRACK-01, PART-18-AF009-01, TRACK-FREEZE-START (the round-5 finding, reproduced). The
  restoration check (`--expect restored`) passes after the stop sequence, and the anchor check (`--expect unlanded`)
  on the pages as fetched.
- **The anchor check on the live pages** (`EV/notion/anchor_check_plan.json`, `ctrl.py all --expect unlanded`): all
  24 edits' `old_str` occur exactly once on the seven pages and none reads `LANDED`: pass True.
- **The Drive file** (`EV/notion/drive_check_plan.json`, `drive_check.py --hub`): 31923 B, size
  True, sha256 True, fence lines [119, 286] (18624 B) sha256
  True, each M2 `old` once outside the fence, no Hub collision: pass True.
- **NAM-002 on live hubs** (`EV/registry/nam002_live_plan/`, §4.4): the child list built by `ctrl.py children`, and
  the four runs give exactly §4.4's expected table.
- **The D24 brief** (`EV/skills/results/brief_fill_proof.json`): `packages_json.py` and `fill_brief.py` on archives
  cut from the patched tree give a brief with no token left for the first round, the re-cut round and the plan-change
  round (which refuses without its prior-round file). Re-packaging a rebuilt tree changes the archive sha256 and keeps
  the freeze digest, which is why the archives reviewed are the archives delivered (P-100).

### 8.8 Harness files (D22 condition 5)

Each dry-run pass recorded the harness files its fetches created (passes 3 to 6: the `source_file` of each result;
from repair round 5 `check` and `graph_check.py` print it too, and from repair round 6 `ctrl.py` and `drive_check.py`).
Inline fetches sit in a transcript; large ones in the session's `tool-results/` folder. None is committed, copied,
hashed or read again, and the harness's teardown removes them.

## §9 Execution order and cut-over

`EV` is `docs/ephemeral/modifications/evidence/closeout-residuals/plan/`. `EX` is
`docs/ephemeral/modifications/evidence/closeout-residuals/execute/`, where EXECUTE's evidence goes (P-83, P-87).
`$SCRATCH` is the executing session's scratchpad, and `$INST` the installed skills root
(`/root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502`). `$PKG` is
the full patched skills root built at X1.1 (`$SCRATCH/pkg-root`). `$GATE` is the suite gate's work directory
(`$SCRATCH/gate`); `run_gate.py` builds and checks the candidate root at `$GATE/cand`. `$BASE` is the `main` commit
X0.2 restarts from. `<URL>` is the page URL from X5.1, normalized to `https://app.notion.com/p/<32 hex>`.
`EX/run.json` holds the values later steps need: `base`, the root digests, `page_id`, `url` and every token value,
each recorded, committed and pushed before the first write that carries it (P-96: `migration_date`, `execute_date`,
`stop_date`, `install_date`, `lift_date`, `close_date`). Every python run uses
`PYTHONDONTWRITEBYTECODE=1 TMPDIR=$SCRATCH/tmp`. The actor is `GCFPE-MGMT-10` unless the step names Nathan. A step
whose gate fails stops EXECUTE, and §E records it: before X5.0 by P-84 (revised), from X5.0 to X6.4 by P-98 once
forward repair (P-88) has failed, at X7.4 by P-94. A failure from X7.5 on is repaired forward or returned to Nathan
with the freeze held; nothing is reversed.

**Notion writes.** Every `notion-update-page` call uses `allow_async: false` (P-83). If a response is still an
`async_task`, EXECUTE polls `notion-get-async-task` until it reads `succeeded` or `failed`, and only then re-fetches
the page; a `failed` task is an uncertain write, inspected on a fresh fetch before anything else (P-89). Before each
control-page edit EXECUTE re-fetches the page and runs
`python3 EV/engine/ctrl.py edits <PAGE> <EDIT_ID>... --run EX/run.json` (P-90, P-96): `LANDED` goes straight to the
readback; `NOT_LANDED` is applied, with `old_str` and `new_str` filled from `EX/run.json`; `TOKEN_NOT_RECORDED`
means a value was not recorded first: record it, push, and test again; `MIXED` cannot be repaired forward. The
readback re-fetches the page and runs the same command, which must read `LANDED`, and finds the filled `new_str` there.

**Sessions (P-78, P-87, P-101).** Any step can run in a new session. EXECUTE commits each step's evidence when the
step produces it, and records in `EX/run.json` the values later steps need. A new session at a step before X7.3
fetches the pushed branch, reads `EX/run.json`, rebuilds `$PKG` (`execute.1.then`) and re-fetches Notion; from X7.3
on it rebuilds neither `$PKG` nor the archives. The archives are cut only at X4.3 and re-cut only as X4.4 says
(P-100). The session starts at the repository root. `land.py`, `ctrl.py`, `graph_check.py` and `drive_check.py` read
only the running session's harness files (`$CLAUDE_CODE_SESSION_ID`; `--session` and `--harness-root` point them
elsewhere). A landing resumed in a new session runs `check` on a page that `plan` reports `ALREADY_LANDED`.

**The landing unit (P-57, P-84 revised, P-88, P-97 to P-99).**
- **Before X5.0 nothing leaves the branch.** There is no Notion write, no merge and no install. A failure before
  X5.0, a D24 rejection included, stops EXECUTE (P-84 revised): EXECUTE writes the stop rows and runs the stop record
  below, so `main`'s record carries them at `EXECUTING`. Nathan ends the Modification, or rules a plan change;
  EXECUTE then starts again at X0.1 once the plan-change PR has merged. Shipping without a rejected part is such a
  change (template rule 7).
- **From X5.0 all 17 parts land as one unit.** The unit is the page, the destination rule, the pointers, the 51
  bodies and the control-page edits. Each package is installed only after the unit has passed (X6) and the execution
  PR has merged (X7.1), and is verified at X7.4 (P-94).
- **A readback that fails is repaired forward (P-88).** After the write's task has succeeded (P-89), EXECUTE
  re-fetches the page and runs `check` again. If it still reports `STALE_READBACK_OR_NOT_LANDED`, EXECUTE runs
  `land.py plan` on that fresh fetch. `ALREADY_LANDED`: run `check` again. Operations whose `repair` lists the edits
  already landed: apply them once, as at X5.4, and run `check`. Any refusal, or a second failing `check`, cannot be
  repaired forward. A control-page edit that reads `MIXED` cannot be repaired forward either.
- **A failure that cannot be repaired forward stops the unit (P-98).** EXECUTE, in this order:
  1. records `stop_date` in `EX/run.json`, commits and pushes;
  2. sweeps Notion, read-only: for each of the 51 bodies with edits, fetch and
     `python3 EV/engine/land.py state <PID> <PAGE>` (CL-40: `--candidate-url <URL>` when `url` is recorded) into
     `EX/stop/bodies/<PID>.json`; fetch the seven control pages and
     `python3 EV/engine/ctrl.py all --run EX/run.json > EX/stop/control.json`; fetch the Hub and
     `python3 EV/engine/ctrl.py children 3ce4590a05eb814f8892f88ff8539308 > EX/stop/hub.json`. The list of writes is
     every body not `UNTOUCHED`, every control edit `LANDED` or `MIXED`, and the page if the Hub lists a
     *Candidate CRD Items List* child; times from `EX/landing/` where recorded;
  3. reverses each control edit the sweep reads `LANDED`, except `TRACK-FREEZE-START`, in reverse §9 order
     (`PART-18-AF009-01`, `PART-12-HUB-01`, `PART-11-TRACK-01`, then the PART-06 pointers in reverse): re-fetch;
     `old_str` is its `new_str` filled from `EX/run.json`, as the page shows it; `new_str` is its §7 `old_str`; then
     `ctrl.py edits` must read `NOT_LANDED` with `old_count` 1. A `MIXED` edit is left for Nathan. `P30-DEST` and
     `P30-VERSION` are on the branch only;
  4. if the Hub lists the page, trashes it: `update_content` on the Hub with `old_str` the page's exact child line as
     fetched (`<page url="…">Candidate CRD Items List</page>`), `new_str` empty and `allow_deleting_content: true`;
     re-fetches the Hub. If there is no such page, skips this step;
  5. re-runs `ctrl.py all` and `ctrl.py children` into `EX/stop/`: no control edit but `TRACK-FREEZE-START` reads
     `LANDED`, and no such child remains;
  6. writes the stop rows: the list (each body pending Nathan's restoration), the reversals, the trash call, each step
     done, the failing step `BLOCKED` with its evidence, and the finding. Then the stop record (below); the status
     stays `EXECUTING`;
  7. after the record PR is pushed, applies `TRACK-UNIT-STOPPED` and `TRACK-STATUS-STOP-01` to `03` (§7.3) with
     `{{STOP_DATE}}` from the stopped attempt's `run.json` (`ctrl.py edits … --run attempt-<n>/execute/run.json`),
     reads them back, and records the readback in §E in a second commit on the
     record PR.

  The freeze stays. Nothing keeps a copy of a body (`D22`).
- **After a stop past X5.0 (P-99).** Nathan restores each listed body from Notion's page history. At his direction a
  `GCFPE-MGMT-10` session runs the restoration check on the branch reset from `main` (the reset guard below): the
  sweep of step 2 again, where every body must read `UNTOUCHED`,
  `ctrl.py all --run attempt-<n>/execute/run.json --expect restored` must exit 0 and the Hub must list no such child.
  It writes `attempt-<n>/restore/` and a §E row. A body that does not read
  `UNTOUCHED` goes back to Nathan by name. Nathan then ends the Modification (every item and part `BLOCKED` with its
  applied steps rolled back, status `BLOCKED`, a record PR) or rules a plan change (P-84 revised), which also revises
  §7's control-page edits for the pages as they then stand. When he lifts the freeze, MGMT-10 records `lift_date` in
  `attempt-<n>/execute/run.json`,
  applies `TRACK-FREEZE-LIFT-STOP`, reads it back and records the readback in §E, in an open restoration record PR or
  in a record PR of its own.

**The stop record (P-97).** Every stop ends with a record pull request:
1. `mkdir -p "$SCRATCH/attempt"`; `git log --format='%H %s' origin/main..HEAD > "$SCRATCH/attempt/commits.txt"`; copy
   `EX/` and this attempt's `REVIEWER-PROMPT-cr*.md` and `SECTION-10-REVIEW-cr*-*.md` (in
   `docs/ephemeral/modifications/evidence/closeout-residuals/`) and the record's stop rows into `$SCRATCH/attempt/`;
2. `git fetch --prune origin && git checkout -B claude/epic-tesla-17406z origin/main`;
3. `n` = 1 + the number of `attempt-*/` directories in the closeout-residuals evidence directory; copy
   `$SCRATCH/attempt/` (less the stop rows) to `docs/ephemeral/modifications/evidence/closeout-residuals/attempt-<n>/`,
   with `EX/` as `attempt-<n>/execute/`. From here on the stopped attempt's `run.json` is
   `attempt-<n>/execute/run.json`, and every later `--run` and recorded value uses it;
4. in the record, set `status: EXECUTING` and add to §E a subsection *Attempt <n>* with the stop rows, saying that
   archives delivered at X4.4, if any, must not be installed;
5. `python3 docs/prompt_ecosystem_management/modification_validate.py docs/ephemeral/modifications/MODIFICATION-20260923-closeout-residuals.md`;
   commit (*closeout-residuals attempt <n> stopped: record*); `git push --force-with-lease origin claude/epic-tesla-17406z`;
   open the record PR against `main`; return to Nathan.

**The reset guard (P-97).** Every other reset of the branch to `origin/main` (X0.2, X7.4, a plan change's PLAN
session, the restoration check) first runs `git fetch --prune origin` and then, when `origin/claude/epic-tesla-17406z`
exists,
`git diff --quiet origin/main origin/claude/epic-tesla-17406z -- docs/ephemeral/modifications/MODIFICATION-20260923-closeout-residuals.md docs/ephemeral/modifications/evidence/closeout-residuals`,
which must exit 0. Otherwise the remote branch holds record or evidence that `main` lacks: EXECUTE does not reset
and returns to Nathan, because that branch's pull request must merge first. Every `--force-with-lease` push follows a
`git fetch --prune origin`.

### X0 Preconditions

| step | actor | action | gate |
|---|---|---|---|
| X0.1 | Nathan | Approves the PLAN, recorded as `plan_approved_by`. Merges the record PR (#478, or the plan-change PR after a stop) | The record on `main` has `status: PLANNED` and carries `plan_approved_by`; `modification_validate.py` passes on it |
| X0.2 | MGMT-10 | The reset guard; `git checkout -B claude/epic-tesla-17406z origin/main`; `BASE=$(git rev-parse HEAD)`; writes `EX/run.json` with `base`. The first push after this is `git fetch --prune origin && git push --force-with-lease origin claude/epic-tesla-17406z` | The guard's `git diff --quiet` exits 0, or the remote branch is absent. `HEAD` equals `origin/main` |
| X0.3 | MGMT-10 | Checks that the base has not moved | (a) The registry's sha256 is `8b4e46ed2dc24442e3dadc416dfe4c810a048788bf03c799808927a54c2677d4`. (b) `freeze.py $INST/<skill>` equals `EV/skills/manifest.json` `execute.1.expected_stdout` for each of the 7 packages. (c) `python3 $INST/glow-graph-contract/scripts/graph_parts.py build docs/graph/parts $SCRATCH/g0.md` exits 0 and prints embedded JSON 575074 bytes sha256 `ae2bd159…`; `g0.md` itself hashes to `a70a9326…`. (d) `python3 EV/engine/closeout_rules.py` prints `checks_matching_authored_or_canonical: []`. (e) `freeze.py $INST` is written to `EX/run.json`; `320 420705ec…` unless a skill outside the seven has synced (P-79; not a stop). Any mismatch in (a)–(d): stop (P-84 revised) |

### X1 The skills, in the scratchpad (P-56: before any repository step that needs them)

| step | actor | action | gate |
|---|---|---|---|
| X1.1 | MGMT-10 | `execute.1.then`: builds `$PKG` (a copy of `$INST`, then each of the 7 packages replaced by a fresh copy of `$INST/<skill>` with `EV/skills/diffs/<skill>.diff` applied by `patch -p1`) | Each patch exits 0. Each `freeze.py $PKG/<skill>` equals `execute.1.expected_after_patch`. `freeze.py $PKG` is written to `EX/run.json` (P-79) |
| X1.2 | MGMT-10 | `mkdir -p $SCRATCH/tmp $GATE` | Both exist, and neither is inside the repository or a skill tree (`run_gate.py` refuses an `--out` that is) |
| X1.3 | MGMT-10 | `python3 EV/skills/run_gate.py --set pre --pkg-root $PKG --out $GATE` on the unchanged working tree, before commit 1 and the reindex | Exit 0: 12 rows ok; the new builder rejects today's parts with exactly the 7 recorded bookkeeping errors. The summary goes to `EX/gate_pre.json`, committed in commit 1 (P-87) |

### X2 Commit 1 — the decision record and the status (class A gate)

| step | actor | action | gate |
|---|---|---|---|
| X2.1 | MGMT-10 | Sets the record's `status` to `EXECUTING` (P-81). `python3 EV/texts/apply_texts.py . EV/texts/edits.json X2.2` applies D25, D23-C, D23-G, D18 and D14 in order (P-102) | The applier exits 0: each anchor occurs exactly once when applied. `grep -c '^## D25'` = 1. No added line starts `> `. `EV/engine/canon.py` imports (ONCE = 2 quoted lines). `modification_validate.py` passes on the record |
| X2.2 | MGMT-10 | Commits and pushes (`git fetch --prune origin` first; `--force-with-lease`, X0.2): *closeout-residuals commit 1, decision record* | The commit touches only `gcfpe.decision-record.md`, the record, `EX/run.json` and `EX/gate_pre.json` |

### X3 Repository changes, and the registry's live check

| step | actor | action | gate |
|---|---|---|---|
| X3.1 | MGMT-10 | `git apply EV/registry/registry.diff`; commits it alone and pushes: *closeout-residuals registry* (P-73). Then runs `python3 $PKG/amthor-workspace-governance-audit/scripts/validate_project_prompt_registry.py docs/prompt_ecosystem_management/project-prompt-contract-registry.md` and `python3 $PKG/glow-graph-contract/scripts/registry_deriver.py $PKG/amthor-workspace-governance-audit docs/prompt_ecosystem_management/project-prompt-contract-registry.md docs/graph/parts --derive` | sha256 equals §4.1's result. The commit touches only the registry. The validator prints `"valid": true` and `"problems": []`. The deriver prints `"rows": 55`, `"parts": 55`, `"drift": []` |
| X3.2 | MGMT-10 | `execute.2`: `python3 $PKG/glow-graph-contract/scripts/graph_parts.py reindex docs/graph/parts` (ITEM-12) | `git diff --no-color docs/graph/parts \| grep -v -e '^diff --git' -e '^index ' \| cmp - EV/skills/results/parts_reindex.repo.diff` exits 0 (the manifest's `execute.2` carries it unescaped). `graph_parts.py build docs/graph/parts $SCRATCH/graph.md` gives 55 nodes, 229 edges, 575 074 B, `ae2bd159…`. A second reindex rewrites 0 files |
| X3.3 | MGMT-10 | `execute.3`: `mkdir -p docs/graph/contract-template`; `git mv` the pre-E2 contract into it; `git rm` the old README; `cp EV/skills/contract-template-README.md docs/graph/contract-template/README.md` (ITEM-13) | The contract at its new path: sha256 `2b78f877…`, 606 657 B. README: sha256 `469e2265…`, 1 158 B |
| X3.4 | MGMT-10 | `python3 EV/texts/apply_texts.py . EV/texts/edits.json X3.5` applies `P32-SWR` to `session-working-rules.md` | The applier exits 0 (anchor found once); the sentence byte-equals P-32 |
| X3.5 | MGMT-10 | Commits and pushes X3.2–X3.4 | The commit touches only `docs/graph/`, `session-working-rules.md` and the old contract path under `docs/ephemeral/` |
| X3.6 | MGMT-10 | NAM-002 and the ITEM-22 title and lane checks on a live snapshot of the six hubs (§4.4; PART-10; P-77). Fetches the six hubs; builds the child list with `ctrl.py children` (§4.4 step 2); reads no prompt body. Copies the snapshot and results to `EX/nam002/`, commits and pushes them | 0 findings against the working-tree registry. Exactly one on ESC-10 with the injected wrong parent, and exactly one title finding with the injected wrong title. The control run on `$BASE`'s registry: NAM-002 55, exit 1 (the PLAN live run gave exactly this: §4.4) |

### X4 The contract, the suite gate, the packages, the review, the rehearsal and the read-only Notion checks

| step | actor | action | gate |
|---|---|---|---|
| X4.1 | MGMT-10 | PART-01 contract regeneration, `execute.4`, on the working tree after X2 and X3 | The acceptance gives `6902924a…` EQUAL x2 from the kept template. The 4.1.1 regeneration gives `dbae180b…`, equal to both bundled copies in `$PKG`. The plain `diff` of the two contracts exits 1 with exactly the two expected lines |
| X4.2 | MGMT-10 | `python3 EV/skills/run_gate.py --set pkg --pkg-root $PKG --out $GATE` | Exit 0: all 34 rows equal their expected results (§5.3), among them `candidate_root` (built at `$GATE/cand`, byte-equal to the graph bundled in flowmaster-validate). The summary goes to `EX/gate_pkg.json` |
| X4.3 | MGMT-10 | `execute.4b`: packages the seven with skill-creator from `$PKG`'s copy into `$SCRATCH/skills-out`, extracts each archive into `$SCRATCH/skills-ext/<skill>`, takes each extracted package's freeze digest and compares the seven lines with `EV/skills/expected_after_patch.txt`, and writes `EX/packages.json` with `EV/skills/packages_json.py` (each archive's name, entries, bytes, sha256 and freeze line). Commits and pushes `EX/packages.json` with `EX/gate_pkg.json`. The archives stay in `$SCRATCH/skills-out` for X4.4 | `Skill is valid!` seven times. The `diff` exits 0 (P-92). `packages_json.py` exits 0. `freeze.py $PKG` is unchanged |
| X4.4 | MGMT-10 | **The D24 review and the delivery (P-100).** `python3 EV/skills/fill_brief.py EX/packages.json --write` (after a plan change add `--prior-file EV/skills/REVIEWER-PROMPT-prior.md`) writes `docs/ephemeral/modifications/evidence/closeout-residuals/REVIEWER-PROMPT-cr<k>.md` and prints `k`, the brief's path and the two reviewers' ids and record paths; commits and pushes the brief. Then spawns two fresh reviewer subagents (`D24`; no forked or context-inheriting agent), each given the filled brief as its only brief, with its own `<REVIEWER_ID>` and record path as printed (`SFR-CR<k>-1` and `-2`; `SECTION-10-REVIEW-cr<k>-SFR-CR<k>-1.md` and `-2.md` beside the brief). Commits and pushes each verdict unedited as it returns. When both confirm, delivers the seven archives from `$SCRATCH/skills-out` with `SendUserFile`, each caption leading with its sha256 and then its freeze digest, together with the brief and both verdict files, and says to install them at X7.3 and not before | `fill_brief.py` exits 0 and the brief carries no `{{`. The brief is committed before either reviewer starts. Both verdicts return `SKILL_FIT_CONFIRMED`, bound to the §1 digests. Each delivered file's sha256 equals its line in `EX/packages.json`. On `SKILL_REPAIR_REQUIRED`: stop (P-84 revised). If the session holding the archives ends before the delivery, X4.3 runs again in the new session and X4.4 runs a new round (P-100) |
| X4.5 | MGMT-10 | **Rehearsal (P-76, P-77).** For each of the 51 bodies with edits (`EV/engine/pages.json` less CF-PO-10, MGR-10, IA-40, IA-50 and IA-60): fetch; `python3 EV/engine/land.py plan <PID> <PAGE> --no-ops --skills $PKG`, and for CL-40 add `--candidate-url https://app.notion.com/p/00000000000000000000000000000000`. For the five: fetch; `land.py check <PID> <PAGE> --skills $PKG`. Writes a summary per page to `EX/rehearsal/` (counts, no body text); commits and pushes them | Every `plan` prints no refusal, its `repair` is `[]`, and its `precheck` and `landed_check` both pass. Every `check` exits 0. One failure stops EXECUTE before any Notion write (P-84 revised) |
| X4.6 | MGMT-10 | **Read-only Notion checks (P-95, P-102).** Downloads the Drive file (`download_file_content`, file `1JPN7WcqCddC2J7UKkHdO4gnIPYRJPGJO`) and fetches the Hub; runs `python3 EV/engine/drive_check.py --hub 3ce4590a05eb814f8892f88ff8539308 > EX/drive_check.json`. Fetches the seven control pages (§7) and runs `python3 EV/engine/ctrl.py all --run EX/run.json --expect unlanded > EX/anchor_check.json`. Commits and pushes both | `drive_check.py` exits 0: the bytes are sha256 `2d7ff093…`, 31 923 B; the fence content's sha256 is `7108e84a…`; each M2 `old` occurs once outside the fence; no Hub child is titled *Candidate CRD Items List*. `ctrl.py` exits 0: every control edit's `old_str` occurs once and none reads `LANDED`. Any failure stops EXECUTE before any Notion write (P-84 revised) |

### X5 Notion, under the freeze (one landing unit from X5.0)

| step | actor | action | gate |
|---|---|---|---|
| X5.0 | Nathan, then MGMT-10 | Nathan confirms the freeze: no flow session runs until he lifts it at X7.5, after the post-install verification (P-66 revised). MGMT-10 writes `execute_date` (today, UTC) to `EX/run.json`, commits and pushes it, then applies `TRACK-FREEZE-START` (§7.3) | `ctrl.py edits` reads `LANDED` on the re-fetched page |
| X5.1 | MGMT-10 | Creates the *Candidate CRD Items List* page (§7.4.2). Writes `migration_date` (today, UTC) to `EX/run.json`, commits and pushes it, unless it is already recorded (a resumed step). Downloads the Drive file again and fetches the Hub; `drive_check.py --hub <Hub>`, and on a resume, where the Hub already lists a child of that title, §7.4.2 step 1's rule: a child whose callout names this Modification is this run's page, continued at step 7, and any other is a collision. Applies M2-R1 to R9 with the self-link spots as plain text (`M2.json` `self_links`); creates the page under the Hub; writes `page_id` and `url` (normalized) to `EX/run.json` as soon as the create returns, commits and pushes; reads the page back; applies the three `self_links.step7_ops` with `<URL>`, each only if its new text is not already on the page; reads it back | `drive_check.py` passes: 31 923 B, sha256 `2d7ff093…`, each M2 `old` once outside the fence, and no collision. Each step-7 operation is applied once or found already applied. F1–F10 pass (F6: 8 pairs at step 6, 11 after step 7). No `{{` on the page |
| X5.2 | MGMT-10 | `python3 EV/texts/apply_texts.py . EV/texts/edits.json X5.2 --run EX/run.json` applies `P30-DEST` with `<URL>` and `P30-VERSION`. Commits them with `EX/run.json` and pushes | The applier exits 0: anchors found once, no token left. `grep -rn '{{' docs/prompt_ecosystem_management` shows no new token |
| X5.3 | MGMT-10 | Applies the eleven PART-06 pointer edits (§7.4.5), with `url`, `migration_date` and `execute_date` from `EX/run.json` (P-96) | Each edit applied once (P-90); `ctrl.py edits` reads `LANDED` on each re-fetched page, and no `{{` |
| X5.4 | MGMT-10 | Lands the 50 live bodies with edits (X4.5's 51 less `GCFPE-MGMT-10-PROPOSED`), one page at a time. Fetch; run `python3 EV/engine/land.py plan <PID> <PAGE> --skills $PKG` (CL-40: `--candidate-url <URL>`), reading its JSON from the harness's saved output file when the tool truncates it (`D22`, transient); apply the printed `ops` in one `notion-update-page` `update_content` call (P-89); re-fetch; run `python3 EV/engine/land.py check <PID> <PAGE> --skills $PKG` (CL-40: `--candidate-url <URL>`). Writes each check summary to `EX/landing/`; commits and pushes them after every ten pages and after the last | The first `plan` on each page prints no refusal and its `repair` is `[]` (a refusal stops the unit before that page's write; on a page an earlier sitting landed, `plan` reports `ALREADY_LANDED` and `check` follows). `check` exits 0. Each printed `source_file` lies under this session's directory, and `fetched` is the "as of" time of the fetch just made (P-101). A failing `check` is repaired forward or stops the unit (the landing-unit rule above) |
| X5.5 | MGMT-10 | Lands PART-11 on `GCFPE-MGMT-10-PROPOSED` the same way | `check` exits 0: the R-ITEM40 and R-ITEM23 gates read 0 |
| X5.6 | MGMT-10 | Applies `PART-11-TRACK-01`, `PART-12-HUB-01` and `PART-18-AF009-01` (`execute_date` from `EX/run.json`) | Each edit applied once (P-90); `ctrl.py edits` reads `LANDED` on each re-fetched page |

### X6 The Tier 1 gate

| step | actor | action | gate |
|---|---|---|---|
| X6.1 | MGMT-10 | Corpus gate on all 55 live bodies, the five untouched ones included. For each: fetch; run `land.py check <PID> <PAGE> --skills $PKG` (CL-40: `--candidate-url <URL>`). Writes the summaries to `EX/corpus/` | 55/55 exit 0. Each new guard fires on its injected regression, and each required guard fails when removed, on the landed text. Each `source_file` and `fetched` belongs to the fetch just made (P-101) |
| X6.2 | MGMT-10 | `python3 EV/engine/graph_check.py --qa110 <QA-110 page> --qa80 <QA-80 page>` after fetching both; output to `EX/graph_check.json` | Exit 0 (§A PART-16: the text matches the graph) |
| X6.3 | MGMT-10 | `execute.6` (the manifest): the closure of each live prompt `ANALYZE-closure.md` lists, compared by `diff` with that file | The `diff` exits 0: closure over the 50 live prompts is unchanged against `ANALYZE-closure.md` (proved on the reindexed tree at PLAN) |
| X6.4 | MGMT-10 | Writes §E: a disposition for every step and item, and the harness files (`D22` condition 5), citing `EX/run.json` for `$BASE`, the root digests, the page, `<URL>` and the token values, and `EX/packages.json` for the archives. Commits `EX/corpus/`, `EX/graph_check.json` and the record, pushes, and opens the execution PR | `modification_validate.py` passes. The PR changes only `docs/prompt_ecosystem_management/`, `docs/graph/` and `docs/ephemeral/`. From here on Nathan may banner the Drive file (P-102 (e)) |

### X7 Merge, install and close

| step | actor | action | gate |
|---|---|---|---|
| X7.1 | Nathan | Merges the execution PR. The reindex reaches `main` before the stricter builder is installed | The merge commit is on `main` |
| X7.2 | MGMT-10 | Asks Nathan to install the seven archives delivered at X4.4 (P-100), naming each by the sha256 its caption leads with, and to give the date of his install sitting. Nothing is re-cut | — |
| X7.3 | Nathan | Installs all seven in one sitting, and gives the date | — |
| X7.4 | MGMT-10 | The reset guard; `git checkout -B claude/epic-tesla-17406z origin/main` (P-94). Writes `install_date` (P-96) to `EX/run.json`. Then the post-install verification: <br>• `execute.5`: the seven `freeze.py $INST/<skill>` lines to `EX/installed_freeze.txt`, compared by `diff` with `EV/skills/expected_after_patch.txt`; <br>• `python3 EV/skills/run_gate.py --set post --inst $INST --out $GATE`; <br>• X6.1's corpus gate with `--skills $INST`. <br>Commits `EX/run.json` and `EX/installed_freeze.txt` and pushes (`git fetch --prune origin`; `--force-with-lease`). The summaries (`EX/gate_post.json`, `EX/corpus-post/`) go into the close commit; a new session re-runs this step | Each installed digest equals X4.3's (`EX/packages.json`): the `diff` exits 0. `run_gate` exits 0 (28 rows). 55/55 exit 0, with each `source_file` and `fetched` from the fetch just made. On a failure the freeze stays. A differing digest is fixed by reinstalling the delivered file (X7.3 again). Any other failure: §E's X7.4 row (the failing rows, the installed digests, the freeze held) and the line `D25 applies from: <X7.1 merge commit sha>, <its UTC date>`, status stays `EXECUTING`, commit, push, a record PR, and return to Nathan (P-82, P-94, P-102 (g)). X7.4 runs again only after that PR has merged (the reset guard) |
| X7.5 | Nathan, then MGMT-10 | After X7.4 passes, Nathan lifts the freeze. MGMT-10 writes `lift_date` to `EX/run.json`, commits and pushes it, and applies `TRACK-FREEZE-LIFT` (§7.3) | `ctrl.py edits` reads `LANDED` on the re-fetched page |
| X7.6 | MGMT-10 | Reads the Drive file's first lines to confirm Nathan's banner. On the branch X7.4 restarted, makes the close commit (P-72): <br>• `close_date` (today, UTC) in `EX/run.json`; <br>• `python3 EV/texts/apply_texts.py . EV/texts/edits.json close --run EX/run.json --installed-freeze EX/installed_freeze.txt` (`CLOSE-D22`, `P31-POLICY`, `P33-A5NOTE`); <br>• §E's install record, the X7.5 readback, X7.4's harness files (`D22` condition 5) and the actual interaction cost; <br>• the line `D25 applies from: <X7.1 merge commit sha>, <its UTC date>` (P-86), unless a P-94 record already wrote it; <br>• the item dispositions (ITEM-13's names the oracle input, P-69); <br>• `EX/gate_post.json` and `EX/corpus-post/`; <br>• `status: COMPLETE`. <br>Commits, pushes (`git fetch --prune origin`; `--force-with-lease`), and opens the close-out PR | The banner is present. If it is not, MGMT-10 asks Nathan and waits. `grep -cE '^D25 applies from: [0-9a-f]{40}, [0-9]{4}-[0-9]{2}-[0-9]{2}$'` on the record is 1. `modification_validate.py` passes on `COMPLETE`. `git show --format= HEAD \| grep '^+[^+]' \| grep -c '{{'` prints `0` (P-102 (c)). The PR changes only the three open paths |
| X7.7 | MGMT-10 | Applies `TRACK-STATUS-01` to `03`, with `close_date` from `EX/run.json` (§7.3). Records their readback in §E in a second commit on the close-out PR; this is step 28's disposition | Each edit applied once (P-90); `ctrl.py edits` reads `LANDED`; `modification_validate.py` passes |
| X7.8 | Nathan | Merges the close-out PR | The merge commit is on `main` |

## §10 Upstream findings, follow-ups and kept sentences

### 10.1 Findings on upstream sections, recorded rather than edited (template rule 1)

| upstream | finding | effect on this plan |
|---|---|---|
| `ANALYZE-anchor-census.md`, A5 row | It lists RS-40 as an A5 carrier. RS-40 does not carry the sentence; its runtime-artifact sentence already scopes to "explicitly authorized paths" | R-A5 is `NOT_APPLICABLE` on RS-40 (P-04). ITEM-32's "PR-35, RS-40 and GCFPE-MGMT-10 … scope the storage sentence" is met by PR-35 and GCFPE-MGMT-10, and by RS-40's existing wording |
| `ANALYZE-anchor-census.md`, the proposed MGMT-10 body | Its summary says the body "Carries A1, A2, A3, A4, A5 and A8". The per-body rows and both full reads find only A8 (2 lines) among the classes this Modification removes; its A5 is "writable set" wording that the pattern does not match | ITEM-40's gate reads 0 before and after, and R-ITEM23 removes the two A8 lines |
| §A opening sentence | "five prompt bodies" | It is 50 live bodies plus the proposed MGMT-10 body (already recorded in §A) |
| §A *Decisions*, item 1 | `validator_revision` is not listed | It moves 3.3.0 → 3.3.1 under the same rule (P-22) |
| §A *Readiness and interaction cost* | 2 merges predicted | 3: the close-out PR carries the post-install record (§11) |
| `MODIFICATION-20260923-alpha-feedback-open-entries.md:1112` | It repeats the C8 overstatement | A completed record; the correction note is the record (P-54) |
| §A *Order, cut-over and freeze*, item 4 | The freeze "lifts after full readback and the corpus gate" | It lifts at X7.5, once X7.4's post-install verification passes: the bodies land at X5, before the matching skills are installed at X7.3, so they must not be used until then (P-66 revised) |
| §A per-part targets, PART-06 and PART-18 | They omit the Notion pointers to the Drive list and the AF-009 placement statement | Both are included as consequences of ITEM-18 and ITEM-37 (P-67) |
| ITEM-13 | "regenerates byte for byte from repository sources" | One input, digest-pinned, is the R1 oracle bundled in flowmaster-validate; recorded in ITEM-13's disposition, not widened (P-69) |

### 10.2 Follow-ups outside the frozen scope

Recorded on the **GCFPE Modification Backlog** (Notion `3e54590a05eb81eb818fd0f42045167a`, created 2026-09-24 at the
Product Owner's instruction), each with a severity. A later Modification takes each as an item. None is edited here.

| backlog | severity | what |
|---|---|---|
| MB-001 | S2 | DOC-20 routes to PR-40 after Nathan's merge assertion, which may be a second PR-40 entry for one merge (against once-per-merge). This plan adds only the fallback predicate (R-A7-LOCAL) |
| MB-002 | S3 | PR-20's PR-40 DOWNSTREAM says "REJECT returns precise in-scope findings to the PR owner", against C-REPLAN and D23-F. ITEM-31 covers PR-40's own body only |
| MB-003 | S3 | The governance audit's `references/epic-reengineering-interoperability.md:55-56` still describes an Analyzer, `MODEL_HANDOFF` and model advice, against the same skill's retired-assessment rule |
| MB-004 | S3 | The v5.0.0 procedure (`docs/ephemeral/GCFPE-Direct-Handoff-and-Runtime-Artifact-Operating-Procedure-v5.0.0-20260923.md:37`) points to `E3-E4-report.md` for which body carries which canonical text; after this Modification that record no longer describes C-LAT, W-4 or ONCE (P-70) |

Seen and not defects, so not on the backlog:
- **RS-30** keeps "Repository paths outside `docs/ephemeral/` and `docs/graph/` are not written", which is correct for
  RS-30 (the census verdict "correct elsewhere").
- **GCFPE-MGMT-10's live page** fetches "as of 2026-09-21T22:56Z" although Notion records a 2026-09-23 edit. The dry
  run used the content as fetched; at X5.4 the landing re-fetches, and `update_content` refuses an `old_str` that no
  longer matches, so a stale read cannot land.

### 10.3 Kept sentences (NOT_REAL), so that ITEM-26 is verified against the measured scope

ITEM-26's statement is absolute ("no body's … sentence"), and its scope is §A's measured set: the REAL findings and
the census carriers. These sentences were judged NOT_REAL, by the lane re-check or the census, and stay. The guards
are silent on them. Each clause is at most 15 words.

| body | kept sentence (clause) | why it stays |
|---|---|---|
| PR-10, PR-20, PR-30, PR-40 | "Each handoff carries the complete native input package, exact artifact and version lineage" (Managed entry) | NOT_REAL in the lane re-check: it describes the package the receiver requires, which the receiver resolves from named artifacts |
| PR-10, PR-20, PR-40 | RS-20 and RS-30 package bullets; SAME-OWNER and TERMINAL input lines | NOT_REAL; R-A2g removes only the register item |
| PR-10 | "Do not copy historical example constants into this reusable contract." | Census A3d NOT_REAL overrides the lane (the one uncovered finding) |
| QA-10 | Execution posture: "direct native owner/stage handoffs with complete native input packages" | NOT_REAL, the same class as the Managed-entry sentence |
| QA-10 | ASSESSMENT_INCOMPLETE: "Carry the missing source/unit, … partial artifacts, current state and precise resume point" | NOT_REAL: minimum context for a condition no artifact records |
| QA-100, QA-110 | "carry exact lineage and unresolved obligations to the actual reader" | NOT_REAL in the lane re-check |
| QA-110 | "with complete failure evidence" (ESC-10); "with the already-authored task and exact rerun decision" (QA-100) | NOT_REAL: they name what the routed artifact holds |
| QA-120 | PASS routing "all rescope/remediation/unresolved-finding lineage"; the existing Strategy Card | Outside the census and the worklist; no shared guard fires |
| QA-20 | BLOCKED routing "with the exact affected objective, evidence, lineage, missing predicate, owner" | Outside the worklist |
| QA-50 | recovery routing to QA-90 "with the exact approved Plan, review, Audit, upstream lineage" | Outside the worklist |
| QA-80 | PLAN_PENDING_REVISED "with exact predecessor/redline/PF10/addendum lineage" | Outside the worklist |
| CL-20, CL-30 | the "Inputs and lineage:" receiver lists | NOT_REAL: intake lists (P-37) |
| CL-C-10, CL-E-10 | CLOSE route: "return the complete closure decision and … addendum direct links" | It names artifacts; the sweep did not flag it |
| DOC-10 | RS-10 bullet: "Carry `PR_RETURN_PHASE: PR-30_PREPUBLICATION` only when …" | A routing value, the minimum context C-HANDOFF allows |
| CF-C-30, CF-E-30 | CF-C-40/CF-E-40 route lines "INITIAL_DENY carries …", "CORRECTION_REDLINE carries …", "DELTA_DENY carries …" | SCOPED_CORRECTLY in the lane re-check |
| CF-C-10, CF-E-10 | "carry it as EVIDENCED_SELECTION_RECORDING_OR_RECOVERY"; Execute step 4 "Produce a self-contained sanitized handoff" | ARTIFACT_NOT_HANDOFF (`ANALYZE-body-evidence.md:226`, `:230`) |
| IA-20, DOC-10, DOC-20, OPS-30, PR-40 | Intake lists naming `CANON_CONFLICT_REGISTER` | An intake names an input; the register is a record in the named artifacts (P-37) |
| PR-10, QA-10, PR-40, CL-20, OPS-30 | A3b "Stable source names/directories and instructions to read and apply them are permitted." | A separate sentence whose "them" means the subject-matter items (census condition) |

## §11 Interaction cost, as planned

    interaction_cost = open rulings 3 + 2 + review cycles 1 + installs 1 + merges 3 + freeze 1 + Drive banner 1 = 12

§A predicted 11 with 2 merges. The install must follow the execution PR's merge (§A order 3: the reindex reaches
`main` first), so the post-install verification and the close texts need a third merge, the close-out PR. A D24
rejection stops EXECUTE before X5.0 and makes the fix a plan change (P-84 revised), so each one adds 4: the stop
record's merge, the plan approval, the further review round and the plan-change merge. A stop after X5.0 adds
Nathan's restoration of the listed bodies and the restoration check's record merge before either route (P-99).
