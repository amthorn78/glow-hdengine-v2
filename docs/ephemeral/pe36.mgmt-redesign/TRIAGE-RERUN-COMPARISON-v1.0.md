---
artifact_type: GCFPE_MGMT_REDESIGN_TRIAGE_COMPARISON
artifact_version: "1.0"
created_date: 2026-09-23
session: PE36
stage: 4 — first real use, intake step
status: TEST_COMPLETE_RUN_D_ADOPTED
authority: Product Owner ruling, 2026-09-23 — "if the triage prompt is invalid, the results are invalid"; rerun after the fixes
prompt_under_test: "Modification Intake and Triage — PROPOSED (D20 redesign)", Notion 3e34590a05eb81bfbf1ed0651e6b6ddf, as revised 2026-09-23
repository_state: PR #471 head 6a3ee19, whose docs match main cacd5a1 exactly; one git worktree per run
predecessor_record: TRIAGE-COMPARISON-v1.0.md (the first comparison, whose results were voided)
---

# Triage rerun — two independent runs on the corrected prompt

**The disagreement is gone.** On the corrected prompt, the two runs agree on every disposition
and group the list identically: six Modifications, the same couplings, the same outcomes in each.
The one place they differ is how finely they split off the parts that are already true, and
neither run contradicts the other there. Run D's result is adopted.

The rerun also found one gap in the validator, fixed in the pull request that carries this record.

## 1. Setup

Identical to the first comparison, except for the corrected prompt.

| | |
|---|---|
| Input, identical for both | "Run the open Alpha Feedback items through triage: AF-004, AF-006, AF-008, AF-009 (it now includes AF-010's merged scope), AF-011, AF-012." |
| Isolation | One git worktree each, at `6a3ee19`, the head of #471 before it merged |
| Deviation from real use | Both stopped before commit and push; the adopted run then pushed from `main` (§8) |
| Run C | 76 tool uses, about 22 minutes |
| Run D | 84 tool uses, about 26 minutes |

## 2. Dispositions — they agree everywhere

Every outcome that both runs stated received the same disposition. Run C found 18 items and run D
found 22; the four extra items in run D are finer splits, listed in §3.

| AF | already true, both runs | new, both runs |
|---|---|---|
| AF-004 | — | the scan of the 40 unscanned bodies |
| AF-006 | the Notion read-only default in the skills and policy; the operational guidance stating it | the workflow explanations and handoffs stating it |
| AF-008 | each handoff is one labelled, paste-ready block | minimal content; artifacts hold every fact; the block is not buried; no branch or commit |
| AF-009 | — | the latitude rule, the rescope criteria, the decision tree, recording decisions in the report |
| AF-011 | PR-20 and PR-30 share a session; PR-30 builds and PR-35 handles reviews and CI; PR-35 stays on the one PR | PR-35 in its own session; that session subscribes to the PR; automatic PR-40 dispatch after merge |
| AF-012 | — | version bump instead of a new page for unchanged prompts |

**AF-011 is settled.** The first comparison split on it. Now both runs mark the same three parts
already true and cite the same evidence: the connection map's PR continuity contract and PR-30's
session role, plus the `change-flow` skill. The fix for gap G1 worked.

Evidence checked for this record, beyond the first comparison's AF-011 checks:

- AF-006: `session-working-rules.md` line 53 makes a session running the workflow read-only toward
  Notion, and `docs/prompt_ecosystem_management/README.md` line 110 states the read-only default.
- AF-008: `handoff_contract` in `docs/graph/parts/global.json` already requires exactly one fenced
  block per non-terminal result, first line `NEXT_PROMPT_HANDOFF`, complete and paste-ready.
- AF-009: `glow-hde-pr-development` lines 65 and 135 already keep an ordinary in-scope defect out of
  rescoping. That is run D's extra already-true item.

## 3. The only difference — how finely the already-true parts were split off

| where | run C | run D |
|---|---|---|
| AF-008 "no branch or commit" | inside the minimal-content item | its own item |
| AF-009 latitude and rescope criteria | one item | two items |
| AF-009 "a defect found while implementing is fixed without a rescope" | not split off | split off as already true |
| AF-011 "PR-35 already produces a conditional PR-40 handoff" | noted in the evidence | split off as already true |

Neither run contradicts the other: each extra split in run D restates part of an item run C kept
whole. The prompt sets no granularity, and both runs flagged that.

## 4. Grouping — identical

| Modification (run D's name) | coupling | run C's name |
|---|---|---|
| `af004-governance-line-scan` | ATOMIC | `governance-line-sweep` |
| `af006-notion-read-only-consistency` | ATOMIC | `notion-read-only-messaging` |
| `af008-short-handoffs` | ATOMIC | `short-handoffs` |
| `af009-implementation-latitude` | ATOMIC | `implementation-latitude` |
| `af011-pr35-session-and-pr40-dispatch` | INDEPENDENT | `pr35-session-and-pr40-dispatch` |
| `af012-version-bump-without-sibling` | ATOMIC | `version-bump-without-siblings` |

Both runs raised the same links between groups, each now written in the drafts' `## Intake`
sections rather than only in chat:

- **Shared skills (rule 6):** `glow-hde-pr-development`, `change-flow` and the bundled contracts in
  `flowmaster-validate` are touched by the AF-008, AF-009 and AF-011 groups.
- **Order:** AF-008 before or with AF-011, because AF-011 creates two new handoffs.
- **Tension:** AF-006 asks handoffs to communicate the Notion default; AF-008 forbids a handoff
  from restating workflow rules.
- **Keep true:** the one-PR rule must survive PR-35 moving to its own session.
- **Replaces a Product Owner step:** automatic PR-40 dispatch replaces the merge assertion that
  triggers PR-40 today. The merge itself stays Nathan's.
- **Policy conflict for AF-012:** `prompt-body-content-policy.md` bars a body field whose value
  changes on a release event, which is what a bumped version line would be.

## 5. Defect found — fixed in this pull request

**An unfilled template section passed as filled.** The template's own headings and guidance under
§A, §P and §E run past the validator's 40-character emptiness threshold. A Modification could
claim `ANALYZED` with §A still holding only the template's text, and pass. Run D found it; it was
reproduced for this record before the fix.

- **Fix:** a section counts as filled only by what it says beyond the template's own headings and
  guidance for that section. Keeping the guidance and writing beneath it is fine.
- **Tests:** a must-fail case, the template's §A copied in unfilled, and a must-pass case, the
  guidance kept with real analysis beneath it. 30/30 pass.
- **Proof the guard fires (`GUARD-001`):** with the check disabled in a copy of the script, the
  must-fail case is not caught, 29/30.

## 6. What both runs still had to decide for themselves

Both runs made the same call on each of the points below, so none of them changed a result. They
are candidates to write into the prompt at its next revision.

- **Draft contents:** keep every template frontmatter key, and leave out the §A, §P and §E
  scaffolding.
- **Item ids:** number items once across the run, and reuse those ids in the drafts.
- **One-item groups:** ATOMIC.
- **Evidence:** cite it for every disposition, not only the three the template requires.
- **Intake record:** add a note of what was deduplicated against, including when nothing matched.
- **"Already true" sources:** step 4's list is not closed. Also read any surface the item itself
  names, such as the Operations Hub.
- **Grouping:** one request with separable outcomes that share a cycle forms one INDEPENDENT group.
  Separate rules stay separate groups, flagged under rule 6.

The one point where they diverged is §3's granularity.

## 7. Observations

- **Independence was not perfect.** Each run's search for AF ids surfaced one or two lines of the
  redesign analysis mentioning the first comparison's AF-011 disagreement. Both runs say they read
  no further, and every AF-011 disposition rests on cited evidence rather than on that line.
- **A large Notion fetch is written to disk by the harness.** The Operations Hub, at 172,000
  characters, was saved to a local tool-results file automatically. For a prompt body, that would
  breach the corpus policy's rule against copying bodies to disk without anyone choosing to. No
  prompt body was fetched in this test. This belongs with `prompt-corpus-policy.md`, not triage.
- **A residual wording in the registry:** PR-30's allowed mutation still reads "Implement, test,
  commit, publish, and review-correct", while review correction belongs to PR-35. It is noted,
  not an item; nobody asked for it.

## 8. Adopted result

**Run D**, because it split the already-true parts more finely and named each Modification after
its source entry. Run C's drafts are discarded unused; this record keeps the comparison.

Run D committed its intake record and six drafts from `main` and pushed them. The branch and
commit are in §9.

## 9. Pushed

Branch `docs/20260923-modification-intake-alpha-feedback-open-items`, commit `95fa9af`, one commit
on top of `main` @ `cacd5a1`. It holds the intake record and the six drafts, 7 files, and nothing
else. Run D did this step itself, so the prompt's own commit-and-push instruction was also tested.

Read back from GitHub for this record, not from the run's copy: the validator passes 7/7 on the
pushed files, with the version on `main` and with this pull request's fix.
