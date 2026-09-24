---
artifact_type: GCFPE_RECOVERY_ANALYSIS
artifact_version: "1.0"
created_date: 2026-09-24
session: PE36
status: ISSUED_DECISIONS_PENDING
authority: Product Owner request, 2026-09-24 — "review", with the Prompt Ecosystem Recovery Brief
repository_state: origin/main c2fbf3c
input_rca: docs/ephemeral/modifications/evidence/closeout-residuals/RCA-20260924-closeout-residuals.md
evidence: docs/ephemeral/pe36.mgmt-redesign/recovery-20260924/
---

# Recovery analysis — the prompt ecosystem after the eight review rounds

**Recoverable forward, with nothing to roll back.** The eight rounds changed nothing live. They built a
plan for the follow-up Modification that was never approved or run. The live ecosystem was changed a day
earlier, on 2026-09-23, by the Alpha Feedback Modification. After refute-by-default checking, none of its 48
known defects is material, and none is shown to make behaviour worse than it was before 09-23. The plan's
content converged by round 5 and is intact on `main`. What went wrong in the rounds is the failure-handling
machinery they kept adding, and that machinery never ran.

**Of the brief's five possibilities, this is 5, mixed.** The content converged legitimately (1). The
machinery was review-induced regression (3), kept going by a review design with no likelihood test and a
self-set exit rule (4). Another round or two would not have converged (§5).

## Corrections to what I told you

Two claims from my redesign (PE36, 2026-09-22/23) were wrong, and both fed this.

- **"Scope freezes at approval, which is what bounds the review loops."** It bounds the item list, and no
  item was added after 21:05. It bounds nothing else. My redesign's own audit named the real problem,
  review loops with no convergence rule (its RC6), and I answered that problem with the freeze. The claim
  is in `D20`, template rule 3, the proposed MGMT-10 body and the tracking page.
- **The pilot was skipped.** The redesign said to pilot PLAN and EXECUTE on one small change first (stage
  4). My 09-23 handoff sent six items into their first run instead, and that run edited all 55 live bodies.
  The pilot that did run, AF-005, reached ANALYZE only.

## 1. Answers to the brief's questions

| The brief asks | Answer | § |
|---|---|---|
| What actually failed? | The follow-up Modification's PLAN never converged: 8 review rounds in 11 h 24 m, and no plan reached you. Before that, the Alpha Feedback Modification's completion check tested only its new wording. It passed while old, contradicting text remained in about 50 live bodies. | 3, 5 |
| What did the rounds improve? | The Alpha Feedback run put all six feedback entries into the live ecosystem. The eight rounds turned the follow-up's plan from one that would have failed into a rehearsed content payload for its 40 items: 51 body edits, 7 skill diffs, a registry diff and 11 repository texts. Each still applies to `main` today. | 3, 4.3 |
| What regressions were introduced? | In live behaviour, none. Seven defects are the Alpha run's own text, and only one has a credible consequence: C-LAT's three steps in PR-40. In the plan, 45 of the 51 required defects in rounds 3–8 sat in machinery that a repair had added. | 4.2, 5 |
| Can they be repaired forward? | Yes. Every live defect has a text-level fix, and you have already ruled on the PR-40 one (Q2 (a)). No live work needs a selective revert. | 4.2 |
| What is the smallest selective revert? | It is in the plan only: withdraw the machinery, 27 of its 119 decisions. Three of round 8's four open defects go with it. | 4.3 |
| Was the process converging? | The content was, by round 5. The machinery was not: serious machinery defects ran 1, 3, 3, 5, 5, 5, 3 over rounds 2–8, a new set each round. You did not stop early. | 5 |
| Which findings actually matter? | None is material. Five are credible risks. Two of those are on the path of the next development work, PR-40's reject routing and change-flow's stale Alpha state, and each has a one-line workaround. | 4.2 |
| What can be retained? | All of the live change, the plan's content and its normal-path tools, and the RCA. The process rules stay, with patches. | 4 |
| What should be deferred? | The 43 findings that are low-impact or affect records only, the plan's content (kept as a ready package), and every rule patch except the stopping rule. | 4, 8 |
| Was the model configuration appropriate? | Not as the default. The finds that mattered came from simulation and breadth sweeps, not depth. Depth mostly widened the review surface and removed the budget signal. It was not the cause: ANALYZE converged under the same mode. | 6 |
| What should trigger escalation? | Five named triggers, each answered with one bounded pass. | 6 |
| What is the stopping rule? | Dry-run the normal path first. Then allow at most two full reviews and one check of the repair's diff. Then the plan comes to you with every open finding listed. Stop earlier if defects stop halving or the budget doubles. | 7 |

## 2. The freeze point

Nothing needs freezing: no prompt body, skill, registry or graph has changed since the Alpha run's
close-out.

| Surface | Last changed | Identity now |
|---|---|---|
| The 55 live prompt bodies | E6 step 4, 2026-09-23 13:18–13:39Z. The PE Metaprompt, which is not a member, at 17:17Z | Notion. There is no body copy, by policy |
| Six installed skills | installed before E6 step 4 | Freeze digests re-measured today equal E6 step 2: flowmaster-validate 31 `a79401de…`, change-flow 22 `ee546df5…`, glow-hde-pr-development 4 `68077fa6…`, session-relay-flowmaster 5 `15aef989…`, amthor-workspace-governance-audit 15 `819915e4…`, tw-flowmaster 2 `fd6c344b…` |
| Graph parts | `d848942` | 55 nodes, 229 edges, 575,074 B, `ae2bd159…`, rebuilt today |
| Registry | `77d98dd` | sha256 `8b4e46ed…` |
| Direct-handoff contract | E2 | `6902924a…`, 4.1.0. Regenerated today from the kept pre-E2 contract, and byte-equal to both installed copies |
| Governing documents | `c2fbf3c` (#478) | four changes: notion-write-boundary (the Backlog becomes a maintenance destination), authoritative-surfaces, the decision record's D18 and D23 successors, and template rule 3's Backlog sentence |

No body, skill, registry or graph change has landed since 17:36Z on 09-23. The only Notion writes in the
PLAN window were the Modification Backlog, a link to it on the Alpha Feedback page and one Backlog update.

**The E6 change freeze was never lifted.** E6's step 8, "Nathan lifts the freeze", still reads `pending`,
and no record anywhere lifts it. PR05 waits on it (decision 1).

**The reference for what worked before.**
- Release `GCFPE-20260914.1` / `091426.1`, promoted 2026-09-21 (`PROMOTION-RECORD-20260921.md`). The
  baseline just before the change is `a63bf80` for the graph, the registry and the documents, and spec v2
  §2 for skill digests.
- The only end-to-end run on the pre-change bodies is HDE-EPIC040-PR04, 2026-09-22, accepted by its PR-40
  review (#469).
- **Two things did not survive in the repository.**
  - The pre-change body text. Notion page history is the only source, and it is not verified.
  - The six pre-change skill packages. They sat at a scratch path in the executing session. If you kept
    the copies delivered before E6, those are the only ones.

  The recommended path reverts nothing, so it needs neither.

## 3. What changed live, and whether it works

The Alpha Feedback Modification (#474, #476, #477) delivered AF-004, AF-006, AF-008, AF-009 (with AF-010),
AF-011 and AF-012.

| Unit | What it changed | Checked by | Not checked |
|---|---|---|---|
| D23-A: results live in the artifact | C-ART in 53 bodies; the PR skill; the Hub | placed once; 1,484 registry assertions, 0 findings | older text still naming the handoff as a home (ITEM-27) |
| D23-B: short handoffs, block last | C-HANDOFF in 53 bodies; C-PLACE in 48, plus a variant in 5; the graph's handoff contract; contract 4.1.0; 3 skills | the same, plus G06 | older "carry lineage, evidence, decisions" text outside the replaced paragraph: 123 findings in 46 bodies (ITEM-26) |
| D23-C: implementor latitude | C-LAT in 10 bodies, C-DEC in 3; 2 skills | placement; guards | whether C-LAT fits the 8 of those bodies that implement nothing (ITEM-37) |
| D23-D: PR-35 in its own session | C-SESSION in 19 bodies; 79 rewrites in 27 bodies; the graph; the R1 successor | same-session anchors | the governance audit's prose fixture (ITEM-07) |
| D23-E: MERGE_OBSERVED | PR-35, RS-40 and PR-40's entry; 2 graph edges | guards on those three | 21 bodies still describe entry by your assertion alone (ITEM-29); closed result lists (ITEM-30) |
| D23-F: a PR-40 reject re-plans | PR-40, PR-20, PR-30, PR-35; one graph edge; the R1 successor | G26, G27 | PR-40's older sentence that keeps the defect with the PR owner (ITEM-31) |
| D23-G: no release header lines | all 55 bodies (154 lines); the catalog; the register | G12–G14 | labels after the first 8 non-blank lines (ITEM-36) |
| C-TOP: no prompt runs as a subagent | 54 bodies; 3 skills | G18–G21 | — |
| D22, D24, AF-004, AF-006 | policy text; skill text; 8 bodies (AF-006) | — | D22 is applied but unguarded (ITEM-16) |

**Does it work?** Statically, yes: every gate passed at E6, and nothing has changed since. Functionally, it
is untested: no GCFPE lifecycle session has run on the edited bodies. The first will be PR05 (decision 1).

**What went wrong in it.** Its completion check tested that the new wording was present. It did not test
that contradicting old wording was gone. The follow-up's body sweep then found 184 real findings; 123 of
them are old handoff-content text in 46 bodies. Where a body now carries both an old and a new
instruction, the old one is the behaviour that worked before 09-23 (§4.2).

## 4. The recovery map

### 4.1 Live changes: keep all of them

Every unit in §3 is **KEEP**. None needs a revert: the new texts are correct, and the defects are old text
left beside them, plus one misplacement. Two units are **KEEP + PATCH**, and both patches are already
ruled or planned:
- **D23-F and D23-C in PR-40.** Remove the sentence "An ordinary in-scope defect remains with the existing
  PR owner" (ITEM-31), and remove C-LAT's three steps (ITEM-37; your Q2 (a)).
- **The close-out's retirement of the Alpha-state block.** The installed change-flow (`SKILL.md:335`),
  flowmaster-validate (`:174`) and governance audit still say Alpha is stopped at PR04 (ITEM-39).

### 4.2 Known open defects: none material

There are 48 known open defects. They come from the follow-up's 40 items, the close-out, the E6 residuals,
the Modification Backlog and the round-a5 findings. After the refute-by-default check:

| Significance | Rows |
|---|---|
| material | 0 |
| credible risk | 5 |
| low impact | 31 |
| no runtime effect | 12 |

**By origin:**
- 21 were there before 09-23;
- 17 are old text that the Alpha run left beside its new text;
- 7 are the Alpha run's own text;
- 3 affect records only.

**Against the behaviour before 09-23**, none is worse. Three are less consistent (ITEM-31, ITEM-37 and
ITEM-26b), and two are better.

The five credible risks, in four rows:

| Items | What | Consequence | Origin | Recommendation |
|---|---|---|---|---|
| ITEM-31, ITEM-37 (PR-40) | PR-40 gives three answers to an in-scope defect: re-plan through PR-20 (the graph and C-REPLAN), keep it with the PR owner (the old sentence), and decide, implement and test it (C-LAT) | Only on a REJECT: a PR-40 session could route the old way. The worst case is the route from before 09-23 | old text left beside new; C-LAT misplaced | **Now:** the workaround in decision 1. **Fix:** the two removals you ruled, which are in the parked plan |
| ITEM-39 | change-flow, flowmaster-validate and the audit say Alpha is stopped, PR04 is next, and "must not execute PR-10 … or resume Alpha" | A change-flow session at PR05's kickoff may stop or ask instead of planning. The failure is safe | there before 09-23; made stale by the close-out's D18 successor | **Now:** one line at PR05's kickoff (decision 1). **Fix:** the prepared skill diffs |
| ITEM-08 | The Flowmaster core pins stage prompts by their complete content and keeps content hashes | Resuming a ledger pinned before E6 stops the run; fresh runs are unaffected. Hashing bodies breaches D22 | there before 09-23 | Defer to the next skill cycle |
| TW-01 | The same pin in tw-flowmaster | TW only | there before 09-23 | Defer: TW is out of scope |

**The other 43 go to the backlog.** They include:
- the 123 handoff-content leftovers: handoffs longer than D23-B intends, but no wrong route;
- the 21 bodies that describe PR-40 entry by your assertion: that is the fallback, and it still works;
- read-only self-descriptions beside commits: sessions commit anyway, as PR04's PR-40 did;
- QA-110's and QA-80's contradictions: both there since 09-17, and both fail-safe, because every route ends
  at ESC-10 or with you;
- the registry's parent IDs, which only the audit reads.

The full list is `recovery-20260924/read_defects.json`, with the checker's corrections in
`verify_defects.json`.

**One ordering constraint, whenever they land.** The receivers' input lists (ITEM-26b) must change with or
before the senders' lists (ITEM-26a): today the unfixed sender lists are what satisfy the receivers.

### 4.3 The eight rounds' plan: keep the content, withdraw the machinery

| Part of the plan | Size | Class | Evidence |
|---|---|---|---|
| **Content**: 51 body edits (spec §3 and the engine), 7 skill diffs, the registry diff and guards, the graph reindex, 11 repository texts, 19 Notion edits | about 147 KB of the spec (35%); 62 of the 119 decisions | **KEEP** | §3 is byte-identical since repair round 6 (`8a905f3`; re-checked). The edit text has changed by one regex line since the first plan. Dry runs 4–7 passed 51/51 on plan and landed-check, with 0 refusals; that readback is simulated, not read from Notion. Re-applied to `main` today: the registry goes `8b4e46ed` → `97bda1a0`, the skill diffs reproduce their expected digests, the text anchors are unique, and the reindex is byte-equal |
| **Normal-path tools**: land.py (plan, check, state), run_gate.py, apply_texts.py, m2.py, the first-round D24 brief | 30 decisions | **KEEP**; R8-02 needs its one-line fix | suite gate: pre 12/12, pkg 34/34, post 28/28 |
| **Machinery**: automated stop and reversal; the stop record, restoration check, lift and end routes; resuming in a new session at any step; leases, the sent list, post-merge routing, D24 re-roll variants | 27 decisions (P-88's landing-state core stays with the normal path); about 209 KB of the spec's 234 KB growth | **SELECTIVE REVERT** (withdraw) | 45 of the 51 required defects in rounds 3–8 were here. R8-01, R8-03 and R8-04 go with it |

**What survives of the machinery's purpose.** Within one session, keep the idempotence: values recorded
once, apply-once tests and operations safe to send twice, because compaction during a long EXECUTE is
near-certain. A failure after the first Notion write does what E6 did:
1. commit a failure record where it survives, which is a record PR to `main`;
2. sweep read-only;
3. keep the freeze;
4. return to you.

Restoring bodies is then your call, from Notion page history.

**Before any landing:**
- The manifest commands changed in rounds 6–7 were tested only piecemeal, so the manifest needs one fresh
  run, in order.
- A failure record left only on an unmerged branch can be lost, which is R5-03's class of defect, so the
  record goes in a record PR.

### 4.4 The process rules

The rules that drove the loop. Most of them are mine.

| Rule | Where | Author | What it did | Class | Smallest patch |
|---|---|---|---|---|---|
| The scope freeze "bounds the review loops" | template rule 3; `D20`; MGMT-10 proposed body | PE36 | gave false assurance: the growth was in machinery, which the freeze does not reach | KEEP + PATCH | "It bounds scope, not review rounds"; the stopping rule (§7) bounds those |
| A part lands whole or not at all | template rule 6; `D21-B`; the validator | PE36 | With `D22`, rolling back a live body has nothing to roll back to. The plan built machinery instead of asking you | KEEP + PATCH | Where a rollback needs a body copy that D22 forbids, the rollback is your restoration from Notion page history, and the plan automates nothing further |
| A plan runs "mechanically with no interpretation" | template §P | PE36 | Applied to every failure path, it has no fixed point: §9's preamble grew from 56 to 3,019 words | KEEP + PATCH | "…on its normal path. A failure path ends with a record, a stop and a return to Nathan" |
| An upstream finding "records a finding and returns" | template rule 1 | PE36 | read as "don't edit upstream", not "return to Nathan": PLAN recorded 7 findings against §A and kept going | KEEP + PATCH | "…returns to the Product Owner with a DECISION NEEDED" |
| `interaction_cost` | template | PE36 | counts only skill review cycles, so the eight rounds cost nothing on paper | KEEP + PATCH | count ANALYZE and PLAN review rounds; state a time and token estimate |
| D24 condition 5: every SKILL_REPAIR_REQUIRED is repaired and re-reviewed | decision record | the Modification session, from your ruling | nothing caps it (the Alpha run went a1 to a5) | KEEP + PATCH | after two consecutive REPAIR rounds, you decide before a third |
| DISP-001 and "No open findings" | `ecosystem-change-management.md` | PE31 era | can read as "repair everything": 132 dispositions, none declined | KEEP + PATCH | a finding is also resolved when it is declined with reasoning, or listed as an accepted risk that you approve |
| "Clean review" as PLAN's exit | the session's own statements, 00:32–07:46 | the Modification session | the primary driver (RCA RC1) | SELECTIVE REVERT | replaced by the stopping rule |

**Kept without a patch:**
- Rule 4, that every step has a verification that can fail. It is what made the Alpha preflight catch an
  approved plan that would have failed.
- Rule 2, that approval is a recorded field.
- `D21`, one run in parts, delegated by workload. It was not followed (87 subagents), but it is not
  defective.
- `D22` and `D24` themselves.

## 5. Was it converging?

The PLAN review rounds: confirmed required defects by kind, recomputed from
`rca-20260924/defects-by-round.csv`.

| Round | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| substance of the 40 items | 16 | 2 | 0 | 2 | 0 | 0 | 0 | 0 |
| normal-path execution | 1 | 5 | 3 | 2 | 1 | 1 | 0 | 1 |
| machinery | 0 | 1 | 6 | 4 | 6 | 9 | 7 | 3 |
| of these, introduced by the previous repair | — | 0 | 7 of 9 | 6 of 8 | 6 of 7 | 9 of 10 | 7 of 7 | 4 of 4 |

- **The content converged, early.** Substance defects reached zero at round 5 and stayed there, and the
  edit payload has barely changed since the first plan. That is legitimate convergence.
- **The machinery did not.** Its defects never halved and were new each round. Most came from the repair
  just before. Round 8's two plausible-path defects came from repairing findings the reviews had not
  required. That is review-induced regression. The review design kept it going: "required" had no
  likelihood test, every finding was repaired, and the only exit was zero.
- **You did not stop shortly before a stable state.** Another round would have fixed round 8's four
  defects and, on the pattern of rounds 3–8, added three to nine new ones. Under the stopping rule in §7,
  the plan would have reached you at about 02:00, with its open findings listed *(inferred)*.

**The day's other loops show the same pattern.**

| Loop | Rounds | What mattered | Continued after clean? | Value |
|---|---|---|---|---|
| Alpha run: EXECUTE preflight | 2 | the approved plan would have failed: 48 of 172 fixtures, 18 error codes | no; it went back to you as Amendment 1 | high |
| Alpha run: skill review a1–a5 | 5 | a1–a3: guard gaps on your rulings, and a false claim in a brief | yes. a3 was FIT/FIT; folding in its optional findings (your choice) cost a4 and a5, and a4 found a regression that the hardening had made | a1–a3 justified; a4–a5 low |
| Alpha run: completion check | 1 | nothing: it tested only the new wording | it stopped at a false clean | too shallow |
| Follow-up ANALYZE | 3 | class errors, missing gates, ordering | no; you were present and its verifiers refuted by default | justified |
| Follow-up body sweep | 1 | 184 real findings that the completion check missed | no | high |
| Follow-up PLAN | 8 | rounds 1–4: real content defects; 5–6: two tools; 7–8: only the repairs' own defects | it never reached clean | rounds 1–4 justified; 7–8 negative |

Breadth and simulation paid. Depth spent on the author's own newest text did not. The one check that was
too shallow, the completion check, is what caused the widened follow-up.

## 6. Model configuration

- **The finds that mattered came from simulation and breadth, not depth.**
  - The Alpha preflight simulated the plan and found 48 of 172 fixtures failing.
  - The follow-up's body sweep read all 55 bodies with refute-by-default verifiers.
  - R3-01 and R4-06, the two certain failures that full PLAN reviews found late, fall to a dry run of the
    normal-path readbacks, which pass 4 did once someone ran it *(inferred)*.
- **Depth mainly widened the surface.** Each round used 3 lenses and 3 verifiers: 87 subagents in all.
  Every round re-read up to 425 KB, and 25–33% of reports were duplicates. The subtle silent-outcome
  defects that deep review did find (R5-03, R6-02 and R6-08) all sat in machinery the loop itself had
  added.
- **It removed the budget signal.** The mode's guidance says token cost is not a constraint. The approved
  estimate of 1–2M tokens was passed during drafting and never re-priced.
- **It was not the cause.** ANALYZE converged in three rounds under the same mode, with you present and
  refute-by-default verifiers. The causes were the review design and the self-set exit.
- **Limit:** the evidence cannot separate the effort level from the multi-agent mode.

**Recommendation, for your setting:** use Max without ultracode for routine maintenance. Turn the
multi-agent mode on for one bounded pass, then off, only when one of these triggers fires:
1. a completion claim is refuted, or a check is shown to test only the new wording. Response: one breadth
   sweep with refute-by-default verifiers;
2. a dry run or preflight fails on the normal path. Response: a deeper check of executability, then back
   to you;
3. a path could silently breach one of your rulings, or silently mis-edit a live page. Response: a deep
   review of that path only;
4. a new oracle, validator or guard whose failure would be silent;
5. a change across more than about 10 live bodies or more than one skill package *(threshold inferred)*.

**Not a trigger:** a review finding more defects in machinery the last repair added. That is the
non-convergence signal, and the response is to come back to you, not to look harder.

**This analysis ran in the multi-agent mode,** because the brief contains the word "UltraCode". It was one
pass with seven agents (four readers and three refute-by-default checkers): 1.36M subagent tokens, 32
minutes, no loop.

## 7. The stopping rule

One rule for every maintenance review loop: a PLAN review, an ANALYZE review or a D24 skill review.

1. **Dry run first.** Before any full review, run every normal-path gate and readback on the landed text,
   read-only against the live pages. Check that every step's verification names a committed command.
2. **At most two full reviews, then at most one check of the repair's diff.** The two are the first review
   and one after its repair. After that the plan goes to Nathan with every open finding listed by path,
   likelihood and consequence, however many there are. Skill packages follow the same cap: after two
   consecutive SKILL_REPAIR_REQUIRED rounds, Nathan decides before a third.
3. **What counts as required:** a defect on the normal path; a silent wrong edit to a body, governed
   document or control page; a silent breach of a ruling; a plausible path with a silent or destructive
   outcome. A failure that ends in a loud stop and a return to Nathan is listed, not required. Verifiers
   refute by default.
4. **Non-blocking findings are listed, not repaired.** They appear as accepted risks in the approval
   request. Repairing one is Nathan's opt-in, priced as another round.
5. **Stop early and ask** when:
   - the count of distinct confirmed required defects does not at least halve from one round to the next;
   - most of a round's findings sit in text the last repair added;
   - time or tokens pass twice the estimate Nathan approved.
6. **A session never tightens an exit rule that Nathan approved.** Every stopping rule it states names who
   set it and when. A compaction summary quotes the session's commitment and Nathan's reply word for word.

**Against this day** *(inferred from the round data)*:
- PLAN reaches you around 02:00 with its findings listed, instead of never;
- the skill review stops at a3 (FIT/FIT), before a4's regression;
- ANALYZE stops at round 3, as it did;
- the budget clause fires before PLAN's second round.

**The risk:** a defect in unchanged text that the dry run does not exercise can ship, listed or not.
R3-07 and R4-07 were of that kind.

**The brief's own stopping rule, applied now:**

| Condition | Now |
|---|---|
| no material defect is open | met |
| credible risks are fixed or have workarounds | met for the two on PR05's path (decision 1) |
| the improvements are preserved | met: the live change is kept, and the plan's content is on `main` |
| the remaining findings are low-impact | met: 43 of 48 |
| the next real run shows the flow works | outstanding: PR05 |

## 8. Decisions

| # | Question | If nothing changes | Recommendation |
|---|---|---|---|
| 1 | Is the ecosystem recovered? | PR05 cannot start: the E6 freeze is still in force on the record | **Yes.** Lift the freeze and run PR05 as the functional test, with two workarounds |
| 2 | What happens to the stopped Modification? | It sits at PLANNED, with a plan nobody should approve as written | **Park it.** Withdraw the machinery and keep the content as a ready package |
| 3 | Adopt the stopping rule? | The next PLAN review or skill review has no cap, just like this one | **Yes, as `D26`,** binding now. `D25` is already drafted in the parked plan |

### Decision 1 — is the ecosystem recovered?

- **(a) Recovered.** Lift the freeze and run PR05 as the functional test. It costs nothing beyond the run.
- **(b) One bounded pass first.** Land the PR-40 text fix and the ITEM-39 skill fix, then run PR05. That
  costs a skill package cycle (review and install) and a body edit through MGMT-10: about half a day.

**Recommendation: (a).** The two workarounds:
- **At PR05's kickoff,** one line: *"Alpha state is recorded in the repository (D18 successor,
  2026-09-23): HDE-EPIC040-PR04 was accepted by its PR-40 review,
  `docs/ephemeral/HDE-EPIC040-PR04-pr-work-unit-lineage-review-v1.0.md`. change-flow `SKILL.md:335` is
  stale."*
- **If a PR-40 returns REJECT,** the work re-plans through PR-20 (`D23-F`), whatever PR-40's older
  sentence says.

**Watch points in PR05.** These are the new behaviours that have never run:
- PR-35 in its own session;
- the subscription and MERGE_OBSERVED, with your merge assertion still the fallback;
- handoffs, some of which will still be long where old text remains;
- no prompt run as a subagent.

A material failure in any of them gets its own fix, and no new review round.

### Decision 2 — the stopped Modification

- **(a) Park it.** Record that PLAN stopped, withdraw the machinery, and keep the content as a ready
  package. Land it only when one of these happens:
  - PR05 shows that one of its items matters;
  - another change needs a skill cycle anyway, so the 7 packages ride along;
  - the MGMT-10 body is promoted.

  It costs one record edit now.
- **(b) Land it now in one bounded pass.**
  1. Withdraw the machinery, fix R8-02 and run the manifest once.
  2. Bring you the plan.
  3. Execute it the way E6 did: one session, forward only, and back to you on any failure.

  It costs about half a day of session work, a D24 review of 7 packages, an install and two merges. It
  edits 51 live bodies, mostly for consistency.
- **(c) End it.** Mark it ABANDONED and keep the content as evidence.

**Recommendation: (a).**
- 43 of its 48 known defects are low-impact. The brief's test, operational benefit against the risk of
  changing working prompts, does not justify editing 51 of them now.
- Nothing is lost: the content is on `main` and re-applies today.
- The RCA recommended applying the four round-8 fixes and bringing the plan for approval. Three of those
  four fixes are to machinery that should go instead.

### Decision 3 — the stopping rule

- **(a) Adopt §7 now, as `D26`.** It binds every maintenance session through the decision record. The
  template, validator and MGMT-10 body patches in §4.4 wait for stage 5 or the next MGMT-10 run.
- **(b) Adopt it together with those patches.**
- **(c) Not now.**

**Recommendation: (a).** It is the one change that prevents a repeat, and it costs one entry. The §4.4
patches are real, but none is needed before the next MGMT-10 run.

## 9. Method, cost and limits

**Scope.** This covers the brief's phases 1–3 and 7, worked from the RCA and the recorded evidence. There
was no new review of prompts or skills, and no agent fetched a prompt body.

**The one body I read.** I read the proposed MGMT-10 body myself, the one I wrote, to check whether it
required the PLAN loop. It does not: its PLAN mode returns the plan for approval and prescribes no review.
It does carry the false "bounds review loops" line. The read was inline, and no file was made.

**Evidence.** `recovery-20260924/` holds four readers (live changes; known defects; the plan's salvage and
convergence; process and model configuration), three refute-by-default checkers, and the prompts they were
given (`workflow-script.js`). The checkers' corrections are applied above. The largest: the defect reader
rated 2 rows material and 10 credible risks, and the checker brought that to 0 and 5.

**Re-checked myself:**
- the PR-40 sentence;
- change-flow `:335`;
- E6 step 8;
- your Q2 (a) ruling;
- §3's hash at five commits.

**Cost:** 7 agents, 1.36M subagent tokens and 32 minutes, in one pass.

**Where this differs from the RCA:**
- **Its option 1.** Apply the four fixes, run one check, bring the plan for approval. This analysis parks
  the plan instead (decision 2).
- **Its RC7.** It says the pilot-stage process ran at full size in the follow-up. It was already full size
  in the Alpha run, whose PLAN was approved although it was not executable; its preflight caught that.
- **Its RC1.** It could not say whether the proposed MGMT-10 body required the loop. It does not.

**Limits:**
- The post-09-23 ecosystem's behaviour is untested. "No material defect" means none has been demonstrated.
- The significance ratings are judgement from recorded evidence. The checker moved 9 of the reader's 12
  upper rows down.
- Notion page history, as a source of the pre-change body text, is not verified to exist.
- The six pre-change skill packages are not in the repository.
- The consequence classes for plan rounds 1–3 are inferred.
- The evidence cannot separate the effort level from the multi-agent mode.
- Candidate-era (09-15) full body text is committed under `docs/ephemeral/`, for example in the post-flight
  evidence manifests. It is stale, it is not a restore source, and it bears on the corpus policy. It is
  noted here, not acted on.
