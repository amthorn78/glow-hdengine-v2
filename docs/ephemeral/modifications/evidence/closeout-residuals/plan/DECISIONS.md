# PLAN repair decisions (plan author, 2026-09-23)

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

## Body rules and texts

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

## Skills

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

## Registry

- **P-27** Rule codes TOP-001 / CTR-001 / CTR-002 are accepted.
- **P-28** G-K40 and G-K39 leave RS-40. G-K35 per row. G-K36 new text. G-K47 new pattern. G-K08
  amended. G-K19 PR-10 fragment. PART-17 suffix. BRANCH-RECV text in G-K22's rows and the PR-40
  input. MGMT-10's G-K40 uses the P-04 variant. QA-10's G-K35 per P-03. A CL-30 guard slot per P-18.

## Repository and Notion texts

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

## Added after the rule-level dry run (all 51 bodies)

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

## Settled from the texts and Notion workers' open issues

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

## Settled from the PLAN review, round 2 (wf_045af16b-3ed: completeness, executability, consistency)

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
- **P-59 land.py hardening.** `--no-ops` prints counts only (the rehearsal). The token test refuses only a `{{` the
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
- **P-71 Tokens and their fills.** Every token in the Notion and repository edits, and what fills it. A new text that
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
- **P-58 (revised again) No rollback journal.** *[Its stop procedure is made exact by P-85, and its forward repair by
  P-88.]* `D22` prohibits backups without exception, and a file of a body's
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
- **P-78 Sessions.** *[Made true by P-87: evidence is committed as it is produced.]* Any step can run in a new session. Each needs only the repository, the installed skills and fresh
  Notion reads, or rebuilds the rest from them: `$PKG` by `execute.1.then`, the packages by `execute.4b`, whose
  extracted freeze digests reproduce X4.3's. The D24 verdicts bind to those freeze digests, not to the archives' own
  sha256, which vary with timestamps. A landing resumed in a new session runs `check` on a page that reports
  `ALREADY_LANDED`.
- **P-79 The whole skills root is measured, not held to a constant.** It also covers skills this Modification does not
  change, which may sync at any time. X0.3 and X1.1 record it, and `run_gate.py` checks that each run leaves it as it
  found it. Only the seven package digests are held to expected values.
- **P-80 `{{MIGRATION_DATE}}`** is the UTC date of the X5.1 page creation. The page's callout, revision bullet and
  M2-R1, and the pointers' "held the list until" and "moved" clauses carry it, so every record dates the move alike even
  if X5.3 falls on a later day. `{{EXECUTE_DATE}}` stays the date of the write for a "Corrected" note.
- **P-81 Commit 1 carries the status change.** X2.1 sets `status: EXECUTING` and commit 1 holds it with the
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

- **P-84 A stop before X5.0, and how EXECUTE starts again.** A failing gate before X5.0, a D24 rejection included,
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
- **P-85 The stop after X5.0, exactly.** A failure that `plan` on a fresh fetch cannot repair (P-88) stops the unit.
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
- **P-87 Evidence is committed as it is produced, so any step can run in a new session.** X0.2 starts `EX/run.json`
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
- **P-88 Forward repair, in the engine.** `land.py` states each edit on the fetched page: `NOT_LANDED` (its anchor
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
- **P-90 A control-page edit is applied once.** Before each control-page edit, EXECUTE re-fetches the page. If the
  edit's filled new text (its `new_str` less its `old_str`) is already there, the edit has landed: it goes straight to
  the readback. Otherwise its `old_str` must occur exactly once. This covers every insertion that keeps its own anchor
  (`TRACK-*`, `PART-11-TRACK-01`, `PART-12-HUB-01`, `PART-18-AF009-01`, the `PART-06-ITEM*-02` entries).
- **P-91 No code inside bold.** Notion reads a bold run that holds a code span back split around the code, so the
  literal `new_str` would not be found. `PART-18-AF009-01` now closes its bold before the code. A scan of the 20
  control-page edits and `M2.json` finds no other bold run with code in it. Each control-page readback compares the
  re-fetched page with the `new_str` as filled.
- **P-92 Guarded removals and a failing X4.3 gate.** Every `rm -rf` in the manifest takes the form `"${VAR:?}"`, which
  cannot expand to `/` and which the session's safety check allows (the unguarded form needs a person's approval).
  `execute.4b` writes the seven extracted freeze lines to a file and compares it by `diff` with
  `EV/skills/expected_after_patch.txt`, so X4.3's gate fails mechanically on a mismatch. The §9-order proof was run
  again and keeps each step's full output (`gate_proof_x.json`, built by `build_gate_proof.py`).
- **P-93 What the D24 verdicts bind to.** The brief's §1 lists, for each package, the archive name, file count, bytes
  and sha256, marked informative because a re-cut changes it, and the extracted freeze digest (`<files> <digest>`) as
  the identity the verdict binds to. Its §10 binds each verdict to those freeze digests and makes it void for any other
  file content. The brief is `docs/ephemeral/modifications/evidence/closeout-residuals/REVIEWER-BRIEF-cr1.md`; the
  verdicts are `SECTION-10-REVIEW-cr1-SFR-CR1-1.md` and `-2.md` beside it, each committed unedited as it returns.
- **P-94 X7.4 runs on `main`, and its failure is recorded.** X7.4 begins by restarting the branch from `main`
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
