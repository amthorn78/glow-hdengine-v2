---
artifact_type: GCFPE_MGMT_REDESIGN_TRIAGE_COMPARISON
artifact_version: "1.0"
created_date: 2026-09-22
session: PE36
stage: 4 — first real use, intake step
status: TEST_COMPLETE_FINDINGS_RECORDED
authority: Product Owner instruction, 2026-09-22 — "why not run two subagents and compare"
prompt_under_test: "Modification Intake and Triage — PROPOSED (D20 redesign)", Notion 3e34590a05eb81bfbf1ed0651e6b6ddf, as it stood before the 2026-09-22 handoff edit recorded in §7
repository_state: main @ db36a8c, one git worktree per run
---

# Triage comparison test — two independent runs on the same input

**The two runs grouped the list identically and disagreed on one thing: whether three parts of
AF-011 are already true. Run B was right, verified against the connection map and the installed
skills.** Both runs independently found the same two tooling defects, both fixed in the pull
request that carries this record. My own prediction, made before the runs, was wrong in one place,
and the runs were right.

## 1. Setup

| | |
|---|---|
| Input, identical for both | "Run the open Alpha Feedback items through triage: AF-004, AF-006, AF-008, AF-009 (it now includes AF-010's merged scope), AF-011, AF-012." |
| Prompt | Read from Notion by each run and followed as written |
| Isolation | One git worktree each, at `main` @ `db36a8c`. Neither run could see the other or the prediction |
| Deviation from real use | Both stopped before commit and push. Two runs pushing competing intake branches would leave two branches this environment cannot delete |
| Run A | 43 tool uses, about 20.5 minutes |
| Run B | 48 tool uses, about 21.6 minutes |

## 2. Items and dispositions

Run B split the six entries into 17 items and run A into 14. The difference is entirely in AF-011.

| AF | run A | run B | agree? |
|---|---|---|---|
| AF-004 | 1 item, NEW | 1 item, NEW | yes |
| AF-006 | 1 item, NEW | 1 item, NEW, noting the rule is already in the skills | yes |
| AF-008 | 4 items, all NEW | 4 items, all NEW | yes, same four outcomes |
| AF-009 | 4 items, all NEW | 4 items, all NEW | yes, same four outcomes |
| AF-011 | 3 items, all NEW | 6 items: 3 NEW, 3 NOT_A_CHANGE | **no** |
| AF-012 | 1 item, NEW | 1 item, NEW | yes |

### The disagreement, and which run was right

Run B found three parts of AF-011 already true. Each was checked for this record:

| AF-011 part | run B | evidence, read 2026-09-22 |
|---|---|---|
| PR-20 and PR-30 run in one session | already true | `change-flow` SKILL.md line 365: "One dedicated session per planned PR work unit; the same session performs both". PR-30's receiving role in `docs/graph/parts/prompts/PR-30.json` is "the same dedicated PR engineering session" |
| PR-35 continues the same PR, never a new one | already true | `pr_continuity_contract.shared_exactly_one` in `docs/graph/parts/global.json` lists exactly one `branch` and one `pull request` for PR-30 and PR-35 |
| PR-30 builds; PR-35 handles review findings and CI | already true | PR-35's function in `PR-35.json`; the phase split in `glow-hde-pr-development` |

**Run B was right.** Run A disposed "PR-20 and PR-30 may share a session" as NEW. The cause is in
the prompt, not the run: step 3 names four places to dedupe against, and none of them describes
current behaviour. Run B went further on its own judgement and read the graph parts and skills.

The genuinely new parts of AF-011 agree across both runs: PR-35 in its own session, that session
subscribing to its PR, and automatic PR-40 dispatch after merge. The last conflicts with a
deliberate contract, `post_merge_three_event_contract` in `global.json`, which sets
`direct_PR35_to_PR40_automatic_edge: false` and makes Nathan's manual merge assertion the event
PR-40 waits on. No decision-record entry rules on it, so NEW is correct. ANALYZE has to decide
what replaces that contract.

## 3. Grouping — identical

| Modification | items | coupling | run A slug | run B slug |
|---|---|---|---|---|
| AF-004 governance-line sweep | 1 | ATOMIC | `af004-governance-line-sweep` | same |
| AF-006 Notion read-only | 1 | ATOMIC | `af006-notion-read-only-default` | `af006-notion-read-only-guidance` |
| AF-008 short handoffs | 4 | ATOMIC | `af008-short-handoffs` | same |
| AF-009 implementation latitude | 4 | ATOMIC | `af009-implementation-latitude` | same |
| AF-011 PR session boundaries | 3 | INDEPENDENT | `af011-pr-session-boundaries` | `af011-pr35-session-and-pr40-dispatch` |
| AF-012 version bump without sibling | 1 | ATOMIC | `af012-version-bump-without-sibling` | same |

Six Modifications, the same members, the same couplings. **Grouping is consistent across runs.**

Links between groups that both runs raised for ANALYZE:

- AF-008, AF-009 and AF-011 all touch `glow-hde-pr-development` and `change-flow`. As three
  Modifications that is three package, review and install cycles. Neither run merged them, because
  AF-008 and AF-009 are multi-item ATOMIC rules and a group has one coupling.
- AF-012 changes how every other change is released, so its order relative to them matters.
- Run A only: AF-006 asks handoffs to *communicate* the Notion default, while AF-008 forbids a
  handoff from restating workflow rules.
- Run B only: AF-011's separate PR-35 session must be told which PR to continue, while AF-008
  removes branch and commit from handoffs.

## 4. Against the prediction made before the runs

The prediction had four groups: AF-012; AF-008; AF-009 with AF-011 as INDEPENDENT; AF-006 with
AF-004 as INDEPENDENT.

- **AF-009 with AF-011 was wrong.** AF-009's four items are one rule, so it is ATOMIC. Putting it
  in an INDEPENDENT group would let its parts land separately, and the prompt's own rule, "a group
  has one coupling", forbids it. Both runs applied the rule; the prediction broke it.
- **AF-004 with AF-006 is a judgement call.** They share a verification method, reading every
  body, but they are different rules. Both runs kept them apart.
- **The prediction's ordering notes were confirmed by both runs**: AF-012 first, and a shared
  skill cycle for the PR-lane changes.

## 5. Defects found — fixed in this pull request

Both runs found both of these, independently.

1. **The template's empty `override` block failed validation after INTAKE.** The template ships
   `override:` with every field empty and says to keep the keys. The validator treated any present
   block as an override, so every Modification made from the template failed as soon as it left
   INTAKE ("override present but has no 'by'"). Reproduced for this record on a copy of run A's
   AF-012 draft: 1/1 at INTAKE, 0/1 at ANALYZING.
   - **Fix:** an all-empty block is the template, not an override. A block with any field set must
     be complete, and must now also name at least one gate.
   - **Why the selftest missed it:** every fixture was hand-written, and none matched the shipped
     template. That is `PAIR-001`. The selftest now also validates the template itself, as shipped
     at INTAKE and minimally filled at ANALYZING.
   - **Proof the guard fires (`GUARD-001`):** with the old condition reinjected into a copy of the
     script, the selftest fails 2 of 22. With the fix it passes 22 of 22.
2. **The template defaulted `coupling` to `INDEPENDENT`.** A draft nobody had decided looked
   decided. Both runs removed it by hand. The template now ships it empty. The validator already
   requires it beyond INTAKE, so an undecided coupling cannot pass ANALYZE.

## 6. Gaps in the triage prompt — not yet fixed, awaiting the Product Owner

| # | gap | how it showed | proposed fix |
|---|---|---|---|
| G1 | "Already true" names no place to check current behaviour | Run A missed three already-true parts of AF-011 | Name them: the graph parts, the registry and the installed skills. Cite the evidence line |
| G2 | The grouping and couplings exist only in the chat report | Both runs left `coupling` empty and wrote their reasons only to chat | Write the proposed coupling into each draft and the reason into its body. ANALYZE confirms or revises |
| G3 | Items that are not NEW leave no record | Run B's three NOT_A_CHANGE items exist only in chat | One intake record per run, beside the drafts, holding tables A and B |
| G4 | An input item that is itself an Alpha Feedback entry is literally a duplicate of its own entry | Both runs made the same sensible call without guidance | Say so: an entry you were given is the item's source, not a duplicate |
| G5 | "request, verbatim" is undefined when the input is only ids | Run A copied up to 5,484 characters of entry text; run B kept the 208-character pasted line | Keep the pasted input verbatim and name the source entry. Do not copy entry text, which drifts |
| G6 | The handoff names `GCFPE-MGMT-10`, which resolves to the live body without modes | Run A flagged it | Until promotion, name the proposed body by its exact title, and add "revert at promotion" to the stage 3 checklist |

Minor, recorded rather than fixed: with one item, both coupling values behave the same (`P3`
again); a one-way dependency inside an INDEPENDENT group has no field and belongs in PLAN; `gh` is
unavailable, so "open branch" means "exists on the remote".

## 7. Changes made after both runs finished

The Product Owner approved the handoff change on 2026-09-22 while the runs were in progress. It was
applied only after both finished, so both tested the same version:

- the triage handoff block no longer carries a branch or a commit; the receiving session finds the
  Modification by its id;
- the proposed MGMT-10 body's entry contract finds a Modification by its id: on `main`, then on
  every open `docs/*-modification-*` branch. Where more than one copy exists, it uses the one
  furthest along, and `main` when they are level.

Both Notion edits were read back.

## 8. State of the drafts, and side effects

| | run A | run B |
|---|---|---|
| draft files | 6, uncommitted in `scratchpad/triage-a` | 6, uncommitted in `scratchpad/triage-b` |
| `request` field | pasted line plus entry text, 990–5,484 chars | pasted line only, 208 chars |
| empty `override` block | kept | omitted |
| validator, shipped version | 7/7 at INTAKE | 7/7 at INTAKE |
| validator, fixed version | 7/7 | 7/7 |

Neither run wrote outside its worktree's `docs/ephemeral/modifications/`, apart from scratch files
outside the repository that run A deleted afterwards. Run B ran `git fetch --prune`, which removed
three remote-tracking references in the shared clone for branches already deleted on GitHub. No
working file changed and nothing was written to Notion.

The drafts live in session scratch space and are lost when the session ends. The findings above
do not depend on them, and a rerun from the corrected prompt can regenerate them.

The stray remote branch `docs/20260922-pe36-stage1-modification-format` matches the intake-branch
pattern, so every triage run will find it and read it. It holds no Modification files. Only the
Product Owner can delete it.
