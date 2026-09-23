---
artifact_type: GCFPE_MODIFICATION_EXECUTION_SPECIFICATION
modification_id: MODIFICATION-20260923-closeout-residuals
version: v1
written: 2026-09-23
status: FOR PLAN APPROVAL
compiled_by: the plan's author, from the PLAN workflow wf_73fca782-464, the repair round wf_22dee43c-01f and two dry-run passes over every live body
---

# Execution specification — MODIFICATION-20260923-closeout-residuals

This file holds everything behind §P of the Modification record: every edit, literal, guard, package, command and
check, and the disposition of every finding. §P's steps cite its sections.

## §0 How to read it

- **Precedence.** 1: the Product Owner's rulings in §A. 2: the PLAN decisions in §1. 3: the other sections. If a
  section seems to contradict a ruling, the ruling governs, and EXECUTE stops and takes it to Nathan.
- **Nothing is left open.** A choice not stated here is void.
- **Mechanical by construction.** The body edits are data run by one engine
  (`evidence/closeout-residuals/plan/engine/`), the same code for the dry runs (§8) and for landing (§9 X4.4). The
  registry change is one diff with a known base and result. Each skill package is one diff with known freeze
  digests before and after. The repository texts are exact anchors with exact new text.
- **Corpus policy (`D22`).** No prompt body is copied, hashed or stored here or in the evidence. Body clauses appear
  only as anchors and kept-sentence clauses, each at most 15 words. The engine reads a body only from a fetch made
  for the check in hand, and opens only harness files written in the last 30 minutes (P-39).
- **Evidence** (`docs/ephemeral/modifications/evidence/closeout-residuals/plan/`, `EV` below):

| path | what |
|---|---|
| `EV/DECISIONS.md` | the PLAN decisions, P-01 to P-54 (§1) |
| `EV/engine/` | `canon.py`, `closeout_rules.py`, `locals.json`, `dryrun.py`, `land.py`, `pages.json` |
| `EV/registry/` | `registry.diff`, `row_assertions.json`, `GUARDS.md`, `report.json`, `guard_tests.json`, `nam002_live.py` |
| `EV/skills/` | `manifest.json`, `diffs/<skill>.diff` (7), `contract-template-README.md`, `results/` (suites, regressions, reindex) |
| `EV/texts/` | `edits.json` and one Markdown file per repository text |
| `EV/notion/` | `edits.json` (14 control-page edits), `M2.json` (the list migration), `NOTES.md` |
| `EV/dryrun/` | pass 2's per-body results (56 files) and both passes' batch reports; no body text |

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
- **P-15 G-K47** becomes the forbidden `code/Ops remediation\. Do not fix it here\.`, which the
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
  the URL filled after the page exists (commit 2).
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
  P30-VERSION and P32.
- **P-44** The AF-009 disposition on *GCFPE Alpha Feedback — Deferred Items* ("C-LAT, in the ten bodies ...") gets the
  drafted dated amendment (PART-18). The Alpha feedback list is an established maintenance destination.
- **P-45** The Glow Operations Checklist property *Authoritative Drive register* on the four item rows stays as history;
  each row gets the drafted dated movement entry. No data-source change.
- **P-46** The 10 pointer edits (Hub ×3, item rows ×8 — two per row) are PART-06 steps, run only after the new page's
  readback passes.
- **P-47** Migration method M2: the eight Drive self-references outside the fence are rewritten to name the Notion page,
  and one dated bullet is appended to *Scope-repair revision record*. Exact old/new pairs are in the spec.
- **P-48** No Notion or repository write may land a `{{...}}` token: the landing step refuses any new text containing
  `{{`.
- **P-49** Before every Notion edit, EXECUTE re-fetches the page and confirms each `old_str` still occurs exactly once.
- **P-50** The tracking page's stale status lines (yaml status, "at INTAKE with ANALYZE in progress", the Records row) are
  updated at the close-out, from the state at that time.
- **P-51** The tracking-page entry is dated by its write date ({{EXECUTE_DATE}}) and names the census of 2026-09-23.
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

## §2 Every PLAN review finding and drafter issue, with its disposition

The first PLAN workflow (`wf_73fca782-464`) ended with two reviews: completeness (21 findings, 14 required) and
executability (18 findings, 12 required). Each finding below is answered by a decision in §1 and by the section
of this specification that carries it. None is left open.

### 2.1 Completeness review

| # | severity | finding | disposition | carried in |
|---|---|---|---|---|
| C-R1 | required | The decision-record texts were not drafted, and nothing ordered them first | Drafted: D25 (D25-A, D25-B), the D23-C, D23-G and D18 successors and the D14 note, all in commit 1, before any other edit. The D22 status goes in the close commit | P-29, P-43; §6; §9 X1 |
| C-R2 | required | PART-06 lacked the destination rule, the page creation and migration, and Nathan's Drive banner | Destination-rule row drafted for `notion-write-boundary.md`. The page creation, M2 migration, readback F1–F10 and the 10 pointer edits are ordered steps. The Drive banner is a Product Owner action | P-30, P-46, P-47; §6; §7.4; §9 X4.1–X4.3 |
| C-R3 | required | No execution sequence | §9 gives the ordered sequence, with actor, gate and readback for each step | §9 |
| C-R4 | required | The PART-11 entry on the D20 tracking page was not planned | Drafted entry `PART-11-TRACK-01`, dated by its write date | P-51; §7.3 |
| C-R5 | required | PART-12's Hub and `session-working-rules.md` edits were missing | Drafted, with P-32's sentence verbatim in all three homes | P-32; §6; §7.1 |
| C-R6 | required | PART-17's policy edit was not drafted | Drafted (`P31-POLICY`). It lands in the close commit, once the whole-body check is installed | P-31, P-43; §6 |
| C-R7 | required | PART-18's PE Metaprompt overlay was not checked | Read in full: it states no C-LAT placement; it places canonical texts where the registry row requires them, which stays true. One control page does state the placement (AF-009 on the Alpha feedback list) and gets a dated amendment | P-44; §7.2 |
| C-R8 | required | PART-04's correction note on the repair-a4 record was not drafted | Drafted (`P33-A5NOTE`), appended to `REVIEWER-PROMPT-a5.md`, which states C8 and §2; it names the residual limit | P-33, P-43; §6 |
| C-R9 | required | PART-08 had no entry | PART-08 is `NOT_APPLICABLE` (§A: mention bans correctly scoped). §P records it and §E disposes of ITEM-20 | §P step 30 |
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
| X-R11 | required | The R-ITEM18 placeholder and the destination rule | The URL is filled from the created page; the landing tool refuses `{{` | P-30, P-48; §9 X4 |
| X-R12 | required | The policy line and the decision-record entries | As C-R1 and C-R6 | P-29, P-31 |
| X-N1 | non-blocking | G-K47 | As C-N7 | P-15 |
| X-N2 | non-blocking | Install timing | The execution PR merges first, then the install, then the close-out PR | §9 X6; §11 |
| X-N3 | non-blocking | Authored wording in FRAME slots | Allowed with C-HANDOFF and C-ART vocabulary; every authored phrase is listed for acceptance | P-20; §3.6 |
| X-N4 | non-blocking | Decorated release labels | The `{0,2}` suffix in the registry and R-ITEM23; flowmaster-validate already strips them (56/56 synthetic cases) | P-16 |
| X-N5 | non-blocking | Scratch scripts that re-read harness files | Not committed and not re-run | P-36 |
| X-N6 | non-blocking | MGMT-10's storage sentence; QA-10's literal ITEM-17 | MGMT-10 variant names its control files; QA-10's role sentence drops "read-only" | P-03, P-04 |

### 2.3 Drafter open issues and unplaceable notes

| source | issue | disposition |
|---|---|---|
| canon | calibration limits: 6 bodies read, 2 in python | Superseded: all 51 bodies ran through the engine twice (§8) |
| canon | harness-saved files | Disclosed in §8.3; none is committed or re-read (P-36, P-39) |
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
| canon | the ITEM-18 placeholder | P-48; §9 X4.1 |
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

## §3 Body edits

### 3.1 How they run

`closeout_rules.apply(pid, text)` applies, in this order: the shared RULES in table order, then the body's LOCAL
edits in their listed order (P-10). Every rule and edit asserts its expected count, and a mismatch is reported, never
forced. After the edits, each LOCAL-only CHECK must read 0 on its rows. `land.py plan` turns the result into
`update_content` operations and refuses a landed body, a count mismatch, an unfilled `{` token (P-48) and operations
that do not reproduce the edit.

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
(?<=This is a read-only audit and readiness role\.)
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
`None` and gives sha256 `4643741b154969406fe74d135dd2d97a3321c4bef8c73a4451fc2dac4df8144a` (7668 lines). The diff's
own sha256 is `f74abc3803cfa96f9d5a3bc4f6b6edca207c0a6d197dbd249109808b63a3e0bd`. Assertions: [1484, 2008]. Both the installed and the final
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

- **G-K24 R-A7-S1b, R-A7-S2** — `required_regex`, `CTR-002`, rows: OPS-30, PR-10, PR-20, PR-30, QA-10

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

- **G-K39 R-A5** — `forbidden_regex`, `CTR-001`, rows: GCFPE-MGMT-10, PR-35

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

PART-10 (ITEM-22): NAM-002 on a live snapshot, EXECUTE procedure

When: after the registry commit on the execution branch, in the same sitting as the corpus gate. Nothing is written to
Notion; no prompt body is read (a hub page is a control page; its child list gives IDs and titles only).

1. Fetch the six 091426.1 hub pages with `notion-fetch`, each by ID, and record each fetch's as-of timestamp:

   | hub id | title | lanes | rows expected under it |
   |---|---|---|---|
   | `3db4590a05eb81d59059eb6b95ed5fcf` | HDE Change Flow — GCFPE-20260914.1 — 091426.1 | CF-PO, CF-C, CF-E, CL-C, CL-E, CL, MGR | 18: CF-C-10, CF-C-20, CF-C-30, CF-C-40, CF-E-10, CF-E-20, CF-E-30, CF-E-40, CF-PO-10, CL-20, CL-30, CL-40, CL-C-10, CL-E-10, CL-E-20, CL-E-30, CL-E-40, MGR-10 |
   | `3db4590a05eb8195a2ccf7c0959a8b6e` | HDE IA — GCFPE-20260914.1 — 091426.1 | DOC, IA, OPS, PR, RS | 21: DOC-10, DOC-20, IA-10, IA-20, IA-30, IA-40, IA-50, IA-60, OPS-10, OPS-20, OPS-30, PR-10, PR-20, PR-30, PR-35, PR-40, PR-50, RS-10, RS-20, RS-30, RS-40 |
   | `3db4590a05eb814d96d3dcfa8835f96d` | HDE QA — GCFPE-20260914.1 — 091426.1 | QA | 10: QA-10, QA-100, QA-110, QA-120, QA-20, QA-50, QA-60, QA-70, QA-80, QA-90 |
   | `3db4590a05eb81cd938de84cfffead9c` | Escalation — GCFPE-20260914.1 — 091426.1 | ESC | 4: ESC-10, ESC-25, ESC-30, ESC-40 |
   | `3db4590a05eb811b9c14f2ae89c28df7` | HDE TW — GCFPE-20260914.1 — 091426.1 | UTIL | 1: UTIL-10 |
   | `3db4590a05eb81de9736ea69bac61016` | Glow HDE Prompt Flow Index — GCFPE-20260914.1 — 091426.1 | GCFPE-MGMT | 1: GCFPE-MGMT-10 |

2. From each fetch take only the direct child pages the page lists: the child page ID (32 hex, undashed) and its title.
   Write them to `childlist.json` in the shape `nam002_live.py` documents:
   `{"captured_at": "<UTC>", "hubs": [{"id": "<hub id>", "title": "...", "fetched": "<as-of>", "children": [{"id": "<page id>", "title": "..."}]}]}`.
   Keep every child; children that are not registry rows do not enter the snapshot.
3. `nam002_live.build_snapshot()` makes the governance audit's snapshot, one source per registry row:
   `{"source_id": <row notion_page_id>, "kind": "notion_page", "complete": true, "in_scope": true, "title": <child title>, "parent": <hub id>}`.
   No source has a `path`, so `_read_snapshot_text` returns None: no text is read, no assertion and no SRC-003 runs.
   `audit_governance()` compares `parent` with `expected_parent_id` as a plain string (installed
   `audit_workspace_governance.py:604-605`; r1 final copy `:620-621`) and `title` with `expected_title` (NAM-001, a WARNING).
   A registry page found under no hub is left out (the audit then raises INV-001, and the run reports it as unplaced);
   a page listed under two hubs stops the run.
4. Run `PYTHONDONTWRITEBYTECODE=1 python3 nam002_live.py <registry> childlist.json --audit-root <installed
   amthor-workspace-governance-audit dir> --snapshot-out <file>` three times:
   - the committed registry: expected NAM-002 = 0 over 55 sources, no unplaced row, no other prompt error; exit 0.
     Any NAM-001 is recorded (a prompt-title difference is outside PART-10) and does not fail this gate.
   - the committed registry with `--inject ESC-10=3db4590a05eb81d59059eb6b95ed5fcf` (the Change Flow hub: a real hub, the
     wrong one for ITEM-22's source row): expected exactly one NAM-002, on ESC-10; exit 0.
   - control, the pre-commit registry (the HEAD blob `8b4e46ed…`): expected NAM-002 on all 55 rows.
5. Keep `childlist.json`, the snapshot and the three results as EXECUTE evidence (hub child IDs and titles only).

PLAN prototype (T7, synthetic child lists built from the ANALYZE mapping, so circular by construction): {"old registry": 55, "new registry": 0, "new registry, ESC-10 parent injected wrong": 1} NAM-002 findings; the injected run names only ESC-10.
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

### 5.3 Suites on the final tree (the gate for X3.3, X5.2 and X6.4)

Each must give the same exit code and result on the patched tree at X3.3, and on the installed tree at X6.4. The full record, with commands, is `EV/skills/results/suites_final.json`.

| suite | exit | result |
|---|---|---|
| validate_flowmaster.default | 0 | verdict FLOWMASTER_SUITE_PASS; findings 0 |
| validate_flowmaster.candidate | 0 | verdict FLOWMASTER_SUITE_PASS; findings 0 |
| run_change_flow_fixtures | 0 | cases_passed 32/32 |
| run_gcfpe_current_fixtures.default | 0 | cases_passed 236/236 |
| run_gcfpe_current_fixtures.historical_alias | 0 | cases_passed 84/84 |
| run_gcfpe_20260914_fixtures | 0 | cases_passed 236/236 |
| validate_gcfpe_20260914.candidate_root | 0 | ok True; contract_sha256 dbae180bb5c2f73e3f27a46601bfb5cbe7321e54 |
| validate_gcfpe_20260914.no_root | 0 | ok True; contract_sha256 dbae180bb5c2f73e3f27a46601bfb5cbe7321e54 |
| validate_gcfpe_current | 0 | ok True; contract_sha256 dbae180bb5c2f73e3f27a46601bfb5cbe7321e54 |
| change_flow_own_validator | 0 | PASS: change-flow GCFPE-20260914.1 contract and Markdown-only source policy |
| relay_self_test | 0 | status PASS; cases 232 |
| pr_skill_validator | 0 | PASS: Glow HDE PR development skill structural contract |
| governance_audit_run_fixture_suite | 0 | OK |
| graph_parts.build.today_parts | 1 | VALIDATION FAILED: / global.json: 13 _other_edge_indices for 3 _other_edges |
| graph_parts.build.reindexed_parts | 0 | build: 55 nodes, 229 edges, 55 state_routes / embedded JSON 575074 bytes  sha256 ae2bd159f0ba947c2e470f96579fadfbf06 |
| registry_deriver.final_audit_1.13.0.repo_parts | 0 | drift [] |
| registry_deriver.final_audit_1.13.0.reindexed_parts | 0 | drift [] |
| registry_deriver.installed_audit_1.12.0.repo_parts | 0 | drift [] |
| registry_deriver.installed_audit_1.12.0.reindexed_parts | 0 | drift [] |

The build of today's parts with the new builder fails on purpose (7 bookkeeping errors) until X2.2's reindex. Every must-fail regression also fires (`EV/skills/results/regress_final_*.json`): regress_plan 36/36, function-level 20/20, the four-package set 33/33, change-flow's own 11/11 (P-25).

### 5.4 The EXECUTE commands

```json
{
 "variables": {
  "ENV": "export PYTHONDONTWRITEBYTECODE=1 TMPDIR=$SCRATCH",
  "INST": "/root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502",
  "SCRATCH": "a scratchpad directory; never the repository or a skill",
  "GGC, FV, CF, RELAY, PR, AUDIT, REPORT": "the new package directories (the patched copies or the extracted packages)",
  "FVI, CFI": "$INST/flowmaster-validate, $INST/change-flow (installed, before the install sitting)"
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
   "note": "the whole root also covers the 19 skills outside the seven packages; any sync of them changes it"
  },
  "then": "cp -r $INST/<skill> $SCRATCH/pkg/<skill>; patch -p1 -d $SCRATCH/pkg/<skill> < diffs/<skill>.diff (exit 0), then freeze.py $SCRATCH/pkg/<skill> must print final_freeze below",
  "expected_after_patch": {
   "flowmaster-validate": "31 0ca2a74d50a57803e2c4b8426a84f43877f68f6d1c93731d54368f413e5c5626",
   "change-flow": "22 9a551af36e042e56a48045297ac316b4102a4eb21f31622853c8be700e223f47",
   "glow-graph-contract": "9 e241bb9a67c4470895fc666a25d0f97d8df7e8e2df06539de5deaf12bc46467c",
   "session-relay-flowmaster": "5 c8a5b22432a44f57fb12bc508169f85aa3d0ca3298b793590c364eb9a2afc8e4",
   "glow-hde-pr-development": "4 265f9170d8459fc477287c320f0bbdd8eaaf0e6ba1dd4ee513275a76a22f8f7a",
   "amthor-workspace-governance-audit": "15 c214e8741e9c54d395cfbd1379cbc7947e6c07beee5bd03aca433dc5dda937ab",
   "glow-po-reporting": "1 7e04368a63e40c99e31ede3eda9ba88cfbbb9915a48b46cdc39027da7cef68e1"
  }
 },
 "2_graph_reindex_ITEM-12_repository_in_execution_PR_before_install": {
  "commands": [
   "python3 docs/prompt_ecosystem_management/freeze.py docs/graph/parts",
   "python3 $GGC/scripts/graph_parts.py build docs/graph/parts $SCRATCH/g-before.md",
   "python3 $GGC/scripts/graph_parts.py reindex docs/graph/parts",
   "git diff --stat docs/graph/parts",
   "python3 docs/prompt_ecosystem_management/freeze.py docs/graph/parts",
   "python3 $GGC/scripts/graph_parts.py build docs/graph/parts $SCRATCH/graph.md",
   "python3 $GGC/scripts/graph_parts.py reindex docs/graph/parts"
  ],
  "expected": [
   "56 980af73e656e20740663ae1dbfa8780eff61b41e2f754c5719c743e4647cae50 (today's parts, HEAD 705568e)",
   "exit 1; VALIDATION FAILED with exactly 7 bookkeeping errors: global.json 13 _other_edge_indices for 3 _other_edges; CF-C-10 4 for 5; ESC-40 3 for 5; PR-35 4 for 5; QA-70 5 for 4; RS-40 5 for 6; 'edge indices are not exactly 0..228, each once (235 indices for 229 edges)'; then the reindex hint line",
   "exit 0; 'reindex: 229 edges; 27 file(s) rewritten' and the 27 names (global.json + 26 prompt parts)",
   "27 files changed, 107 insertions(+), 113 deletions(-); only edge_indices / _other_edge_indices change (results/parts_reindex.json holds the from/to table)",
   "56 84dbb1fe5e7566b871ddc436bcbc875a772dcc695be221d2b4d45a18a470027f (the reindexed parts)",
   "exit 0; 'build: 55 nodes, 229 edges, 55 state_routes'; 'embedded JSON 575074 bytes  sha256 ae2bd159f0ba947c2e470f96579fadfbf060f74423aa974ae1194ac16bb2484d'; graph.md 575672 B sha256 a70a93263f2943be45450a210f62a82a2a27abfd49a259d04f838e469ba0cc24",
   "exit 0; 'reindex: 229 edges; 0 file(s) rewritten' (idempotent)"
  ],
  "alternative": "git apply results/parts_reindex.repo.diff (git apply --check exits 0 on HEAD 705568e)",
  "note": "the installed builder has no reindex and passes today's parts; $GGC must be the new package"
 },
 "3_contract_template_move_ITEM-13_repository_in_execution_PR": {
  "commands": [
   "sha256sum docs/ephemeral/modifications/evidence/pre-e2-contract/gcfpe-20260914.1-091426.1-direct-handoff-contract-4.0.6.json",
   "git mv docs/ephemeral/modifications/evidence/pre-e2-contract/gcfpe-20260914.1-091426.1-direct-handoff-contract-4.0.6.json docs/graph/contract-template/gcfpe-20260914.1-091426.1-direct-handoff-contract-4.0.6.json",
   "git rm docs/ephemeral/modifications/evidence/pre-e2-contract/README.md",
   "cp <plan>/new/repo/docs/graph/contract-template/README.md docs/graph/contract-template/README.md",
   "sha256sum docs/graph/contract-template/gcfpe-20260914.1-091426.1-direct-handoff-contract-4.0.6.json docs/graph/contract-template/README.md"
  ],
  "expected": [
   "2b78f877e7a31efb2da8488d7f129794e60bcbdbf9f43e9851a319f83f06b53b, 606657 B",
   "rename, bytes unchanged",
   "the old README (839 B, sha256 995399d40b11f94b03058283059e78885bf2d5613769aa96c826f512850c7e2f) is replaced",
   "new README 1158 B",
   "2b78f877e7a31efb2da8488d7f129794e60bcbdbf9f43e9851a319f83f06b53b; 469e2265640439b0b126379c358aa7e862638c77240b2f0c6b52de8c5ba60fde"
  ],
  "note": "evidence/regenerate_contract.py and evidence/repair-a4/contract_recipe.py stay as dated records (drafter's recommendation, AUTH-001); the maintained copies are the glow-graph-contract scripts"
 },
 "4_contract_regeneration_PART-01_after_steps_2_3_and_the_decision_record_commit": {
  "commands": [
   "python3 $GGC/scripts/graph_parts.py build docs/graph/parts $SCRATCH/graph.md",
   "python3 $GGC/scripts/contract_recipe.py $SCRATCH/graph.md docs/graph/contract-template/gcfpe-20260914.1-091426.1-direct-handoff-contract-4.0.6.json $FV/references/glow-hde-canonical-change-flow-r1-20260923.json docs/prompt_ecosystem_management/gcfpe.decision-record.md $SCRATCH/contract-4.1.0.json --contract-revision 4.1.0 --primary-skill-revision 1.3.0 --check $CFI/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json $FVI/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json",
   "python3 $GGC/scripts/contract_recipe.py $SCRATCH/graph.md docs/graph/contract-template/gcfpe-20260914.1-091426.1-direct-handoff-contract-4.0.6.json $FV/references/glow-hde-canonical-change-flow-r1-20260923.json docs/prompt_ecosystem_management/gcfpe.decision-record.md $SCRATCH/contract-4.1.1.json --contract-revision 4.1.1 --primary-skill-revision 1.3.1 --check $CF/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json $FV/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json",
   "structural diff of contract-4.1.0.json against contract-4.1.1.json",
   "python3 -c \"import sys,pathlib; sys.path.insert(0,'$FV/scripts'); import validate_gcfpe_20260914 as v; print(v.skill_tree_digest(pathlib.Path('$FV')))\""
  ],
  "expected": [
   "embedded JSON 575074 B sha256 ae2bd159\u2026",
   "E2 7a7fd0285730622217cc2e2d117552a002f57f9e391eac1c3d94b553fabbb675 613162; recipe 6902924a2de7f3d348e75951fd5562632bcb690e3c4687c473695261b70f3718 613326; EQUAL x2; exit 0",
   "E2 5ad52062133068fa5947eb512a52ddc72bd4791f65faa27444af3357495c03b2 613162; recipe dbae180bb5c2f73e3f27a46601bfb5cbe7321e5431dbaba8763b1a576cd9343c 613326; EQUAL x2 (the packages already carry the regenerated bytes and every pin); exit 0",
   "exactly .contract_revision 4.1.0 -> 4.1.1 and .pr_development_contract.primary_skill_revision 1.3.0 -> 1.3.1",
   "ed52208f48479124f39119a54f29774096381ab85f54109a73bc3a7f3cc572af (= SKILL_TREE_SHA256 on $FV/SKILL.md:9)"
  ],
  "note": "the oracle is byte-identical in $FV and $FVI (not a changed file). The recipe reads the two '> ' lines of the D23-E once-per-merge section only, bounded at the next '### ' or '## ' heading, and asserts there are exactly two (P-21), so entries added under D23 or later decisions do not change the output"
 },
 "5_after_the_install_sitting": {
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
   "flowmaster-validate": "31 0ca2a74d50a57803e2c4b8426a84f43877f68f6d1c93731d54368f413e5c5626",
   "change-flow": "22 9a551af36e042e56a48045297ac316b4102a4eb21f31622853c8be700e223f47",
   "glow-graph-contract": "9 e241bb9a67c4470895fc666a25d0f97d8df7e8e2df06539de5deaf12bc46467c",
   "session-relay-flowmaster": "5 c8a5b22432a44f57fb12bc508169f85aa3d0ca3298b793590c364eb9a2afc8e4",
   "glow-hde-pr-development": "4 265f9170d8459fc477287c320f0bbdd8eaaf0e6ba1dd4ee513275a76a22f8f7a",
   "amthor-workspace-governance-audit": "15 c214e8741e9c54d395cfbd1379cbc7947e6c07beee5bd03aca433dc5dda937ab",
   "glow-po-reporting": "1 7e04368a63e40c99e31ede3eda9ba88cfbbb9915a48b46cdc39027da7cef68e1"
  },
  "then": "rerun every suite of results/suites_final.json against $INST; expected exits and counts as recorded there",
  "one_install_event": "flowmaster-validate 3.3.1 passes only with change-flow 3.3.1, relay 3.2.0, PR skill 1.3.1 and the dbae180b contract in both bundled copies; install the seven together"
 }
}
```

## §6 Repository texts

Applied in this order; each anchor occurs exactly once at its turn. Commit 1 is the decision record (X1). Commit 2 texts land in X2.4 and X4.2. The close texts land in the close-out PR (X6.5).

### P29-D25 — `docs/prompt_ecosystem_management/gcfpe.decision-record.md`, commit 1, `insert_after`

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
  excludes the prompt's own committed output artifacts and the pull request that carries them
  (C-ART). The claim is scoped, and the behaviour does not change.
- A reviewer stays read-only toward the work it reviews, and commits its own review artifacts.
- Nothing else is excluded. Every other limit a body states on what it may change still holds.

### Consequences

- **Both are recorded before any EXECUTE edit** of `MODIFICATION-20260923-closeout-residuals`, in
  its first execution commit. `D25-A` changes what `CL-40` writes and where (class A, PART-06).
  `D25-B` aligns wording with what the bodies already do (class B, PART-05).
- **The exact wording each ruling is applied with is the canonical wording in that Modification's
  §P.** It is cited there, not restated here, so the two cannot drift (`DERIV-001`).
- **`CL-40`'s rule is a flow prompt's own destination rule.** It names one page, and authorizes
  `CL-40` alone. The line `notion-write-boundary.md` draws between executing the flow and
  maintaining the ecosystem stands, and no other flow prompt gains a Notion write.
- **The Drive list's only repository mention**
  (`docs/ephemeral/HDE-EPIC040-PR40-workspace-register.md:206`) sits inside a dated 2026-09-09
  snapshot of a Notion page, and stays as written (`AUTH-001`).
- **`D25-B` gives no prompt a new write.** It corrects what bodies say about the writes they
  already make.

### The tested guard (`D14`)

Registry assertions in `project-prompt-contract-registry.md`, listed in that Modification's §P. Each
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
implying a guard. **Until the guards land, `D25` is ruled but not applied.**

```

### P29-D23C — `docs/prompt_ecosystem_management/gcfpe.decision-record.md`, commit 1, `insert_before`

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

### P29-D23G — `docs/prompt_ecosystem_management/gcfpe.decision-record.md`, commit 1, `insert_before`

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

### P29-D18 — `docs/prompt_ecosystem_management/gcfpe.decision-record.md`, commit 1, `insert_before`

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
- **The two validator checks are renamed** from Alpha-state checks to promotion-record checks, with
  their values unchanged: `flowmaster-validate`'s at `validate_gcfpe_20260914.py:1901-1908`, and
  `change-flow`'s at `:1017-1018` (3.3.0 line numbers). The skills' prose says the same.
- **Retiring the block was not chosen.** It would move the graph digest, and every proof token and
  pin with it.


```

### P29-D14 — `docs/prompt_ecosystem_management/gcfpe.decision-record.md`, commit 1, `insert_before`

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

### P30-DEST — `docs/prompt_ecosystem_management/notion-write-boundary.md`, commit 2, `insert_after`

anchor:

```text
| operational status, navigation, plan state | Notion — where a destination rule already says so |

```

new text:

```markdown
| the Candidate CRD Items List | the Notion page *Candidate CRD Items List* (`{{CANDIDATE_CRD_LIST_URL}}`), under the Glow Operations Hub, and nowhere else. An established destination rule (`D25-A`): `CL-40` updates that page in place with each change's new CRD candidates, and writes no other Notion page. It is a flow prompt's own rule, so it authorizes `CL-40` alone and lends nothing to any other flow prompt. The Drive file it replaced is Nathan's reference copy, not a store. |

```

### P30-VERSION — `docs/prompt_ecosystem_management/notion-write-boundary.md`, commit 2, `replace`

anchor:

```text
artifact_version: "1.2"

```

new text:

```markdown
artifact_version: "1.3"

```

### P31-POLICY — `docs/prompt_ecosystem_management/prompt-body-content-policy.md`, commit close, `replace`

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

### P32-SWR — `docs/prompt_ecosystem_management/session-working-rules.md`, commit 2, `insert_after`

anchor:

```text
- **IN FLIGHT** — something is running; the Product Owner waits

```

new text:

```markdown

When a `NEXT_PROMPT_HANDOFF` block ends the message, as it does for a maintenance, repair, validation or review session, the block comes last and the named state is the line immediately before it. Nothing follows the block.


```

### P33-A5NOTE — `docs/ephemeral/modifications/evidence/REVIEWER-PROMPT-a5.md`, commit close, `insert_after`

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

### CLOSE-D22 — `docs/prompt_ecosystem_management/gcfpe.decision-record.md`, commit close, `insert_before`

anchor:

```text
## D23 — The Alpha Feedback rule changes: artifacts hold results, handoffs are short, implementors have latitude, PR-35 has its own session, releases stop copying unchanged prompts

```

new text:

```markdown
### Status, {{INSTALL_DATE}} — guarded

`MODIFICATION-20260923-closeout-residuals` (ITEM-16) carried the guard the status above owed. It
was installed on {{INSTALL_DATE}}: {{FREEZE_DIGESTS}}. The status above is left as written
(`AUTH-001`).

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

Every edit: re-fetch the page, confirm each `old_str` occurs exactly once (P-49), apply with `notion-update-page` `update_content`, and read back. No new text may carry `{{` when it lands (P-48). `{{EXECUTE_DATE}}` is the write date; `{{CANDIDATE_CRD_LIST_URL}}` is the normalized URL from X4.1.

### 7.1 PART-12 — the Hub's *Worker communication rules* §2 (ITEM-24)

#### PART-12-HUB-01 — Glow Operations Hub (`3ce4590a05eb814f8892f88ff8539308`)

Inserts P-32's sentence after the definition of the three named states.

old_str:

```text
- **IN FLIGHT** — something is running; the Product Owner waits
```

new_str:

```markdown
- **IN FLIGHT** — something is running; the Product Owner waits
When a `NEXT_PROMPT_HANDOFF` block ends the message, as it does for a maintenance, repair, validation or review session, the block comes last and the named state is the line immediately before it. Nothing follows the block.
```

### 7.2 PART-18 — C-LAT's placement on control pages

The PE Metaprompt (`3db4590a05eb8174be35d9e35acb3f77`) was read in full: its GCFPE overlay states no placement. It places each canonical text where the registry row requires it, which stays true (the Material pattern stays on all ten rows). No edit. The Alpha feedback list's AF-009 disposition does state it, so it gets a dated amendment (P-44).

#### PART-18-AF009-01 — GCFPE Alpha Feedback — Deferred Items — 091426.1 (`3df4590a05eb8111a6a5f67cb82f96f6`)

Appends a dated amendment after AF-009's disposition; the disposition is not rewritten.

old_str:

```text
Scope is the PR lane; the ESC remediation lane keeps its own threshold.
```

new_str:

```markdown
Scope is the PR lane; the ESC remediation lane keeps its own threshold. **Amended {{EXECUTE_DATE}} (`D23-C` successor; `MODIFICATION-20260923-closeout-residuals` PART-18):** C-LAT's three-step *Decide it during work* block now sits whole only in PR-30 and PR-35, which implement; PR-10, PR-20, PR-40, RS-10, RS-20, DOC-10, DOC-20 and IA-30 keep its Material definition and their own routing. The parenthesis above is left as written (`AUTH-001`).
```

### 7.3 PART-11 — the D20 redesign tracking page (Decision 11)

#### PART-11-TRACK-01 — GCFPE MGMT Change-Process Redesign — Tracking (`3e34590a05eb81e7927efe0541258916`)

One entry, dated by its write date (P-51), listing the proposed MGMT-10 body's design-level contradictions for stage 5.

old_str:

```text
## The three decisions — answered 2026-09-22
```

new_str:

```markdown
**2026-09-23: input for stage 5 — the proposed body's design-level contradictions.** `MODIFICATION-20260923-closeout-residuals` records them in `docs/ephemeral/modifications/evidence/closeout-residuals/ANALYZE-anchor-census.md`, section *The proposed MGMT-10 body*, from a complete read of the proposed body (the child page below) on 2026-09-23. **They are not resolved by that Modification** (its §A, Decision 11): each needs a design choice the `D20` track owns, so they wait for stage 5. That Modification changes the proposed body only to remove the classes it removes from the live bodies (ITEM-23, ITEM-40).
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
## The three decisions — answered 2026-09-22
```

### 7.4 PART-06 — the *Candidate CRD Items List* page

#### 7.4.1 Source

The Drive file `Candidate-CRD-Items-List.md` (`1JPN7WcqCddC2J7UKkHdO4gnIPYRJPGJO`): 31923 B, sha256
`2d7ff0936191e079641f4719c5d39769fc47a6e3dd1e1b84539c5ec7f235b3d3`, modified 2026-09-08T07:25:47.904Z. UTF-8, LF only (0 CR), 296 LF, ends with ".\n\n" (one trailing blank line). one fenced block, lines 119 (```markdown) to 286 (```); inner content 18,624 B, sha256 7108e84a46658c4dfa3a7fc34607bc06d87572967da110ee87bc2c9f2c701c5f (for the F7 byte check).
EXECUTE recomputes both hashes from its own download and stops if either differs.

#### 7.4.2 Method (M2, P-47)

1. **Preconditions:** commit 1 has landed. Search the Hub for a child titled *Candidate CRD Items List*: none may
   exist.
2. **Read** the raw bytes with `download_file_content`, decode as UTF-8, and check the length and sha256 above.
3. **Rewrite** M2-R1 to R9 below, in memory. Each `old` occurs exactly once outside the fence. R3's text also occurs
   inside the fence, which never changes. The fence content stays byte-identical.
4. **Convert:** the body H1 becomes the title. Add the callout at the top and append the revision bullet to
   *Scope-repair revision record*. The metadata lines become paragraphs; headings and lists are unchanged; the
   blockquote is one `> ` line. Both pipe tables outside the fence become `<table header-row="true">`. The fence
   becomes one `markdown` code block, content unchanged. Nothing is escaped.
5. **Create** with `notion-create-pages` under the Hub (`3ce4590a05eb814f8892f88ff8539308`), with the three
   self-link spots (R4, R5, R9) as plain text. If the call rejects the size, create through *Moved-items history*
   and append the rest with `notion-update-page`, reading back after each write.
6. **Read back** against F1 to F10 below. On a failure, fix only the failing block and read back again. Never
   repeat a create.
7. **Normalize** the URL to `https://app.notion.com/p/<32 hex>`. Add the three self-links in one update, then read
   back and confirm no `{{` remains.
8. Nathan banners the Drive file as superseded, pointing to the page (§P, Product Owner actions).

#### 7.4.3 Readback criteria

- **F1.** The title is *Candidate CRD Items List*, and the parent is the Hub.
- **F2.** The ordered (level, text) headings outside the code block equal the Drive file's 12 H2 and 1 H3.
- **F3.** The active list holds 0 entries in both, and its "Empty" statement is present. The moved-items table holds
  4 data rows in both.
- **F4.** For each moved-items row, all 6 cells are equal after whitespace normalization. Notion links are compared
  by their 32-hex page id.
- **F5.** The review-status table's 6 rows × 2 cells are equal.
- **F6.** Links outside code: the Drive file's 8 (link text, target) pairs are all present, plus the 3 self-links
  after step 7, 11 in all. Notion targets are compared by page id; other targets exactly.
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
Updated: {{EXECUTE_DATE}} (migrated to Notion)
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
Migrated {{EXECUTE_DATE}} from the Google Drive file `Candidate-CRD-Items-List.md` (id `1JPN7WcqCddC2J7UKkHdO4gnIPYRJPGJO`, 31,923 B, sha256 `2d7ff0936191e079641f4719c5d39769fc47a6e3dd1e1b84539c5ec7f235b3d3`, modified 2026-09-08T07:25:47.904Z) under `GCFPE-MGMT-10` and `MODIFICATION-20260923-closeout-residuals` PART-06 (`D25-A`). This page is the list's only store: read and update it here. The Drive file is the Product Owner's reference copy and is not updated. References that named Drive as the store were rewritten; see the Scope-repair revision record.
```

Revision bullet (the third bullet of *Scope-repair revision record*):

```text
- {{EXECUTE_DATE}}: Moved this list from the Google Drive file `Candidate-CRD-Items-List.md` (id `1JPN7WcqCddC2J7UKkHdO4gnIPYRJPGJO`) to this Notion page, Candidate CRD Items List, under MODIFICATION-20260923-closeout-residuals PART-06 (D25-A). This page is now the list's only store. Rewrote the references that named Drive or the file as the list's store: the `Updated`, `Document status`, `Home` and `Persistent filename` (now `Persistent page`) metadata lines, Document purpose paragraph 2 sentence 1, the Classification test closing paragraph, Routing instructions items 3 and 4, and Maintenance rule sentence 3. The pre-repair source in the code block, the 2026-09-08 entry above and all other text are unchanged. The Drive file is the Product Owner's reference copy and is no longer updated.
```

#### 7.4.5 Pointer edits (P-46), after the readback passes

The Checklist property *Authoritative Drive register* stays as history (P-45).

#### PART-06-HUB-01 — Glow Operations Hub (`3ce4590a05eb814f8892f88ff8539308`)



old_str:

```text
[Open the authoritative Candidate CRD Items List](https://drive.google.com/file/d/1JPN7WcqCddC2J7UKkHdO4gnIPYRJPGJO/view?usp=drivesdk), maintained in place at Glow / Ops / Assessments & Decisions as `Candidate-CRD-Items-List.md`.
```

new_str:

```markdown
[Open the Candidate CRD Items List]({{CANDIDATE_CRD_LIST_URL}}), a Notion page under this Hub and the list's only store (`D25-A`); `CL-40` updates it in place under the destination rule in `docs/prompt_ecosystem_management/notion-write-boundary.md`. The Drive file `Candidate-CRD-Items-List.md` (`1JPN7WcqCddC2J7UKkHdO4gnIPYRJPGJO`), which held the list until {{EXECUTE_DATE}}, is Nathan's reference copy and is not updated. (Corrected {{EXECUTE_DATE}}: this line named the Drive file as the authoritative list.)
```

#### PART-06-HUB-02 — Glow Operations Hub (`3ce4590a05eb814f8892f88ff8539308`)



old_str:

```text
Their original identities and complete source history are preserved in the Drive moved-items history.
```

new_str:

```markdown
Their original identities and complete source history are preserved in the list's moved-items history, which moved with it from Drive.
```

#### PART-06-HUB-03 — Glow Operations Hub (`3ce4590a05eb814f8892f88ff8539308`)



old_str:

```text
Keep ambiguous items in Notion and out of the active Drive list.
```

new_str:

```markdown
Keep ambiguous items in the Checklist's *Ambiguous — PO Decision Required* view and out of the active Candidate CRD Items List.
```

#### PART-06-ITEM1-01 — Repository prompt-use provenance helper (`3d54590a05eb8142a187d32ad4435950`)



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



old_str:

```text
Preserve the original local number and all dated facts in the same Drive file. This row is the current item-level tracking identity; other references are evidence or historical pointers.
```

new_str:

```markdown
Preserve the original local number and all dated facts in the same Drive file. This row is the current item-level tracking identity; other references are evidence or historical pointers.
{{EXECUTE_DATE}}: the Candidate CRD Items List moved from the Drive file to the Notion page [Candidate CRD Items List]({{CANDIDATE_CRD_LIST_URL}}) (`D25-A`; `MODIFICATION-20260923-closeout-residuals` PART-06). This item's original local number and dated facts are preserved there, in its moved-items history; the Drive file is Nathan's reference copy and is not updated.
```

#### PART-06-ITEM2-01 — QA-10 substantive, paste-ready PF10 findings summary (`3d54590a05eb8119affafcfb024ba990`)



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



old_str:

```text
Preserve the original local number and all dated facts in the same Drive file. This row is the current item-level tracking identity; other references are evidence or historical pointers.
```

new_str:

```markdown
Preserve the original local number and all dated facts in the same Drive file. This row is the current item-level tracking identity; other references are evidence or historical pointers.
{{EXECUTE_DATE}}: the Candidate CRD Items List moved from the Drive file to the Notion page [Candidate CRD Items List]({{CANDIDATE_CRD_LIST_URL}}) (`D25-A`; `MODIFICATION-20260923-closeout-residuals` PART-06). This item's original local number and dated facts are preserved there, in its moved-items history; the Drive file is Nathan's reference copy and is not updated.
```

#### PART-06-ITEM3-01 — QA-90 explicit Product Owner task selection (`3d54590a05eb8159a73cf6af261c1c2b`)



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



old_str:

```text
Preserve the original local number and all dated facts in the same Drive file. This row is the current item-level tracking identity; other references are evidence or historical pointers.
```

new_str:

```markdown
Preserve the original local number and all dated facts in the same Drive file. This row is the current item-level tracking identity; other references are evidence or historical pointers.
{{EXECUTE_DATE}}: the Candidate CRD Items List moved from the Drive file to the Notion page [Candidate CRD Items List]({{CANDIDATE_CRD_LIST_URL}}) (`D25-A`; `MODIFICATION-20260923-closeout-residuals` PART-06). This item's original local number and dated facts are preserved there, in its moved-items history; the Drive file is Nathan's reference copy and is not updated.
```

#### PART-06-ITEM4-01 — Combined audit-and-plan invocations for IA and QA preparation (`3d54590a05eb8118b229e0ca25bdfd42`)



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



old_str:

```text
Preserve the original local number and all dated facts in the same Drive file. This row is the current item-level tracking identity; other references are evidence or historical pointers.
```

new_str:

```markdown
Preserve the original local number and all dated facts in the same Drive file. This row is the current item-level tracking identity; other references are evidence or historical pointers.
{{EXECUTE_DATE}}: the Candidate CRD Items List moved from the Drive file to the Notion page [Candidate CRD Items List]({{CANDIDATE_CRD_LIST_URL}}) (`D25-A`; `MODIFICATION-20260923-closeout-residuals` PART-06). This item's original local number and dated facts are preserved there, in its moved-items history; the Drive file is Nathan's reference copy and is not updated.
```

## §8 Dry-run evidence

**Pass 1** (7 batches, rule level): all 51 bodies passed after the data fixes now in the engine (P-40, the CF-x-20
comma, P-15 revised, P-18, P-19, P-37, P-38). **Pass 2** (6 batches, the complete check): the merged engine, the
repaired registry and guard file, and the final skill tree's validator. It covered the 50 live bodies, the proposed
MGMT-10 body and the five untouched live bodies (CF-PO-10, MGR-10, IA-40, IA-50, IA-60), which show that the new
all-rows guards are silent where nothing changes.

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

### 8.3 Harness files (D22 condition 5)

Each dry-run agent reported the harness files its fetches created. Inline fetches sit in the agent's own transcript; large ones in the session's `tool-results/` folder. None is committed, copied, hashed or read again, and the harness's teardown removes them.

## §9 Execution order and cut-over

`EV` is `docs/ephemeral/modifications/evidence/closeout-residuals/plan/`. `SCRATCH` is the executing session's
scratchpad. Every python run uses `PYTHONDONTWRITEBYTECODE=1 TMPDIR=$SCRATCH/tmp`. The actor is `GCFPE-MGMT-10`
unless the step names Nathan. A step whose gate fails stops its part. EXECUTE records the step in §E and does not
move on to the next step of that part.

### X0 Preconditions

| step | actor | action | gate |
|---|---|---|---|
| X0.1 | Nathan | Approves the PLAN, recorded as `plan_approved_by`. Merges the record PR (#478) | The record on `main` carries `plan_approved_by`; `modification_validate.py` passes on it |
| X0.2 | MGMT-10 | Restarts the designated branch from `main` (`git fetch origin main && git checkout -B claude/epic-tesla-17406z origin/main`) | `HEAD` equals `origin/main` |
| X0.3 | MGMT-10 | Checks that the base has not moved | (a) the registry's sha256 is `8b4e46ed…` (`registry.diff`'s base). (b) Each installed package's freeze digest equals `EV/skills/manifest.json` `execute.1` (7 digests). (c) `graph_parts.py build docs/graph/parts` with the installed builder gives `ae2bd159…`. (d) `EV/engine/closeout_rules.py` self-test prints `checks_matching_authored_or_canonical: []`. Any mismatch: stop and report to Nathan |

### X1 Commit 1 — the decision record (class A gate)

| step | actor | action | gate |
|---|---|---|---|
| X1.1 | MGMT-10 | Applies `EV/texts/edits.json` entries with `commit: 1` in order (D25, D23-C, D23-G, D18, D14), each at its anchor | Each anchor occurs exactly once when applied. `grep -c '^## D25'` = 1. No added line starts `> `. `EV/engine/canon.py` imports (ONCE = 2 quoted lines) |
| X1.2 | MGMT-10 | Commits and pushes: *docs(prompt-ecosystem): closeout-residuals commit 1, decision record* | Push accepted; the commit touches only `gcfpe.decision-record.md` |

### X2 Repository changes

| step | actor | action | gate |
|---|---|---|---|
| X2.1 | MGMT-10 | `git apply EV/registry/registry.diff` | The registry's sha256 equals `4643741b…`. The governance audit's loader and `validate_project_prompt_registry.py` report `valid: true`. `registry_deriver` drift `[]` |
| X2.2 | MGMT-10 | Reindexes the graph parts with the final `glow-graph-contract` builder (`EV/skills/manifest.json` `execute.2`) | 27 files change, and `git diff` equals `EV/skills/results/parts_reindex.repo.diff`. The build gives 55 nodes, 229 edges, embedded JSON 575 074 B and `ae2bd159…`, byte-identical to the build before the reindex. A second reindex rewrites 0 files |
| X2.3 | MGMT-10 | Moves the pre-E2 contract to `docs/graph/contract-template/` with its new README (`execute.3`) | sha256 `2b78f877…`, 606 657 B, at the new path; README sha256 `469e2265…` |
| X2.4 | MGMT-10 | Applies `P32-SWR` to `session-working-rules.md` | Anchor count 1; the sentence is byte-identical to P-32 |
| X2.5 | MGMT-10 | Commits and pushes X2.1–X2.4 | Push accepted |

### X3 Skills, in the scratchpad

| step | actor | action | gate |
|---|---|---|---|
| X3.1 | MGMT-10 | Copies the seven installed packages to `SCRATCH/pkg/` and applies `EV/skills/diffs/<skill>.diff` with `patch -p1` | Each patch exits 0. Each package's freeze digest equals `execute.1.expected_after_patch` |
| X3.2 | MGMT-10 | PART-01 contract regeneration on the working tree, now after commit 1 and X2 (`execute.4`) | The acceptance gives `6902924a…` EQUAL x2 from the kept template. The 4.1.1 regeneration gives `dbae180b…`, equal to both bundled copies |
| X3.3 | MGMT-10 | Runs every suite on the patched tree (§5.3) | Every count and exit code equals §5.3 |
| X3.4 | MGMT-10 | Packages each of the seven with `skill-creator`. Extracts each `.skill` into a clean directory and reruns its gates from the extracted contents | `Skill is valid!` seven times. Each extracted freeze digest equals X3.1's. Each `.skill`'s sha256 is recorded |
| X3.5 | MGMT-10 | Fills `reviewer-prompt-template.md` for the seven packages and commits it as `evidence/closeout-residuals/REVIEWER-BRIEF-cr1.md`. Then spawns two fresh reviewer subagents (`D24`) | The brief is committed before either reviewer starts. Both verdict files (`SECTION-10-REVIEW-cr1-SFR-CR1-1.md`, `-2.md`) return `SKILL_FIT_CONFIRMED`, bound to the X3.4 digests. On `SKILL_REPAIR_REQUIRED`, EXECUTE repairs, re-cuts the packages and runs a fresh round (`cr2`), which counts as +1 review cycle |

### X4 Notion, under the freeze

| step | actor | action | gate |
|---|---|---|---|
| X4.0 | Nathan | Confirms the freeze: no flow session runs until X6.5 | Recorded in §E and on the D20 tracking page |
| X4.1 | MGMT-10 | Creates the *Candidate CRD Items List* page (§7.4). Collision check; downloads the Drive file and checks its bytes; applies M2-R1…R9; creates the page under the Hub; reads it back; normalizes the URL; adds the page's self-links; reads it back again | The Drive bytes are sha256 `2d7ff093…`, 31 923 B (stop if not). Every M2 `old` occurs exactly once outside the fence. F1–F10 pass. No `{{` is left on the page |
| X4.2 | MGMT-10 | Applies `P30-DEST` with the URL filled, and `P30-VERSION`. Commits and pushes | Anchor counts are 1. `grep -r '{{' docs/prompt_ecosystem_management` finds no new token |
| X4.3 | MGMT-10 | Applies the ten PART-06 pointer edits (§7.4.5), with `{{CANDIDATE_CRD_LIST_URL}}` and `{{EXECUTE_DATE}}` filled | Each page is re-fetched and each `old_str` occurs once (P-49). A readback shows the new text and no `{{` |
| X4.4 | MGMT-10 | Lands the body edits in the 50 live bodies (CL-40 after X4.1), one page at a time: fetch; `EV/engine/land.py plan <PID> <PAGE> --candidate-url <URL> --registry <working-tree registry> --skills SCRATCH/pkg-root`; apply the printed operations with one `notion-update-page` `update_content` call; re-fetch; `land.py check` | `plan` prints no refusal, and its precheck passes. `check` passes: 0 registry findings, no guard failure, validator ok, no `{{`. On a failure, the same session reverses that page's operations (each `new_str` back to its `old_str`), records it and stops the part |
| X4.5 | MGMT-10 | Lands PART-11 on the proposed MGMT-10 body (`GCFPE-MGMT-10-PROPOSED`) the same way | `check`: the R-ITEM40 and R-ITEM23 gates read 0 |
| X4.6 | MGMT-10 | Applies the control-page edits `PART-12-HUB-01`, `PART-18-AF009-01` and `PART-11-TRACK-01` (dated by the write date) | Re-fetched; each `old_str` occurs once; the readback shows the new text |
| X4.7 | MGMT-10 | Runs NAM-002 on a live snapshot (§4.4) | 0 findings against the working-tree registry. Exactly ESC-10 with the injected wrong parent. 55 against the pre-change registry |

### X5 The Tier 1 gate

| step | actor | action | gate |
|---|---|---|---|
| X5.1 | MGMT-10 | Runs the corpus gate on all 55 live bodies, the five untouched ones included: fetch, then `land.py check` | 55/55 pass. Each new guard fires on its injected regression, and each required guard fails on removal, on the landed text |
| X5.2 | MGMT-10 | Runs the flowmaster-validate suite on the patched tree in default and candidate modes. Runs `closure.py` over every prompt | PASS with 0 findings. The graph proof token is unchanged (`ae2bd159…`), so closure is unchanged against `ANALYZE-closure.md` |
| X5.3 | MGMT-10 | Writes §E (a disposition for every step and item) and commits the evidence | `modification_validate.py` passes |
| X5.4 | MGMT-10 | Opens the execution PR (commits X1–X5) | The PR carries only `docs/prompt_ecosystem_management/`, `docs/graph/` and `docs/ephemeral/` paths |

### X6 Merge, install and close

| step | actor | action | gate |
|---|---|---|---|
| X6.1 | Nathan | Merges the execution PR. The reindex reaches `main` before the stricter builder is installed | The merge commit is on `main` |
| X6.2 | MGMT-10 | Delivers the seven `.skill` files with `SendUserFile`, each captioned with its digest, together with the brief and both verdicts | Delivery complete (`D24`) |
| X6.3 | Nathan | Installs all seven in one sitting | — |
| X6.4 | MGMT-10 | Post-install verification | Each installed freeze digest equals its X3.4 digest. Every §5.3 suite passes on the installed tree. The corpus gate (X5.1) passes against `main`'s registry with the installed skills |
| X6.5 | MGMT-10, then Nathan | The close commit on a close-out PR: `CLOSE-D22` (date and digests filled), `P31-POLICY`, `P33-A5NOTE`, §E's install record and actual interaction cost, item dispositions, and status `COMPLETE`. The tracking page's stale status lines are updated (P-50). Nathan banners the Drive file, lifts the freeze and merges the close-out PR | `modification_validate.py` passes on `COMPLETE`. The readbacks show the new text. The Drive banner is visible on the file |

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

### 10.2 Follow-ups outside the frozen scope

These go to a new Modification with `spawned_from: MODIFICATION-20260923-closeout-residuals`, opened after this one
completes. None is edited here.

1. **PR-20's PR-40 DOWNSTREAM** says "REJECT returns precise in-scope findings to the PR owner", which contradicts
   C-REPLAN and D23-F. ITEM-31 covers PR-40's own body only.
2. **DOC-20 routes to PR-40** after Nathan's merge assertion. That may conflict with "PR-40 is entered once per
   merge". This plan adds only the fallback predicate (R-A7-LOCAL).
3. **The governance audit's `references/epic-reengineering-interoperability.md:55-56`** still describes an Analyzer,
   `MODEL_HANDOFF` and model advice, against the retired-assessment rule in the same skill.
4. **RS-30** keeps "Repository paths outside `docs/ephemeral/` and `docs/graph/` are not written". That is correct for
   RS-30, which writes only there (the census verdict "correct elsewhere"), so it is listed only to show it was seen.
5. **GCFPE-MGMT-10's live page** fetches "as of 2026-09-21T22:56Z" although Notion records a 2026-09-23 edit. The
   dry run used the content as fetched. At X4.4 the landing re-fetches, and `update_content` refuses an `old_str` that
   no longer matches, so a stale read cannot land.

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
`main` first), so the post-install verification and the close texts need a third merge, the close-out PR. Each
further D24 review round adds 1.
