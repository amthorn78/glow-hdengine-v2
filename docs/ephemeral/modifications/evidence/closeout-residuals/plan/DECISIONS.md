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
  P30-VERSION and P32.
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
- **P-57 One landing unit.** Every part that edits a prompt body or the registry (PART-05, 06, 07, 10, 11, 13, 14, 15,
  16, 17, 18) lands as one unit, because one page carries several parts' edits and one registry diff carries their
  guards. Before the first Notion write to a body, `land.py plan --no-ops` rehearses every page and must print no
  refusal. PART-06's page must exist first (PART-15 is after PART-06). If a page then fails `check` and cannot be
  repaired forward in the same sitting, every landed page is reversed from the rollback journal (P-58), the registry
  commit is reverted, and the unit is BLOCKED as a whole (template rule 6). The skill parts (PART-01 to 04, 12) are
  a separate unit held by the D24 review.
- **P-58 Rollback journal.** `land.py plan --journal DIR` writes each page's operations to `DIR/<PID>.ops.json` in the
  session scratchpad, so a reversal is mechanical. Under D22 this is part of the landing transaction in hand: outside
  the repository, never hashed or compared, read only to reverse the landing it records, deleted when the unit passes
  its gate or has been reversed, and reported in §E. No other use.
- **P-59 land.py hardening.** `--no-ops` prints counts only (the rehearsal). The token test refuses only a `{{` the
  edit introduces. A body where every rule and edit reads 0 and every CHECK passes is reported NOTHING_TO_LAND (run
  check), which covers deletion-only bodies. `check` reports STALE_READBACK, not a failure, when a page that should
  carry new text does not yet show it; the executor re-fetches, and only a non-stale failure is reversed.
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
- **P-66 Freeze window.** The freeze runs from the first Notion write to the close-out merge, not only to the corpus
  gate as §A order 4 says: the landed bodies must not be used before the matching skills are installed. Recorded as an
  upstream finding (spec §10.1).
- **P-67** PART-06-HUB-03 is reduced to a pointer-only rewrite. The eleven PART-06 pointer edits and the AF-009 amendment
  are consequences of ITEM-18 and ITEM-37 that §A's target lists omitted (spec §10.1).
- **P-68** D25 cites the execution specification (not §P) for its wording and guards, and attributes the pull-request
  clause to the approved plan (P-02). The D18 successor names both renamed checks. `{{INSTALL_DATE}}` is the X6.3 date
  and `{{FREEZE_DIGESTS}}` the seven `<skill> <files> <digest>` lines of the post-install comparison.
- **P-69** ITEM-13's regeneration reads one input from a skill, not the repository: the R1 oracle bundled in
  flowmaster-validate, pinned by its digest. Recorded in ITEM-13's disposition, not widened.
- **P-70** The v5.0.0 procedure's pointer to `E3-E4-report.md` for per-body placement goes stale for W-4, ONCE and C-LAT.
  Recorded on the Modification Backlog (MB-004, S3), not edited here.
