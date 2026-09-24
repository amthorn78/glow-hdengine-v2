---
artifact_type: PE_WORK_RECORD
created_date: 2026-09-24
session: PE37 (`session_018teDumz2XyKdoXF9p3BKFM`)
authority: Product Owner instruction, 2026-09-24 — "The first step should be to analyze `TW-MGTMT-10` using the PE Metaprompt … Proceed with that analysis first." (read as TW-MGMT-10, the page the invocation named exactly)
method: PE Metaprompt 091426.1, mode Analyze, permission 0 — Inspect
target: TW-MGMT-10 — Manage the Glow TW Ecosystem — 090826.2, Notion 3d54590a05eb81a8b55afabc42298df9, last edited 2026-09-08T07:07:26.670Z
companions: TW-BASELINE-20260924.md (the current-state baseline); PE-METAPROMPT-TEST-20260924.md (the PE Metaprompt's test)
status: RECORD — analysis only. No prompt, Notion page, skill, registry row, graph part or canon file was changed. Merging preserves the record and approves nothing (D21-C)
---

# TW-MGMT-10, analyzed with the PE Metaprompt

**TW-MGMT-10 cannot be revised into the GTWPE's manager.** It and the seven prompts it manages
share four dependencies that current rules retire:
- PF canon read from Drive;
- artifacts kept in ChatGPT Library or Drive;
- ChatGPT Work sessions;
- a model-advice stage.

The GTWPE (read here as *Glow Technical Writing Prompt Ecosystem*) is therefore an ecosystem
redesign. The PE Metaprompt runs that as **Ecosystem Design / Draft**: a versioned design package
that Nathan approves before any prompt body is written.

**The single-session approach fits the Claude environment and current Anthropic guidance, under conditions:**
- the managing session is the only writer;
- one subagent handles each target PF's judgement work;
- code handles the mechanics;
- a fresh verifier checks the result without seeing the expected answer;
- Nathan's approvals are pauses inside the one session;
- reviews are capped (`D26`).

It has not yet run in Claude, so one trial run should confirm it.

**Canon writes work only as exact edits in a pull request Nathan merges.** Complete-file
regeneration is not viable: six PFs are larger than Opus 5.5's maximum output. Three current
controls forbid the write today; that is decision 1 in §7.

## 1. How it was run

**The run was a fresh-context subagent**, given only what Nathan would paste. That makes it a test
of the PE Metaprompt as well as an analysis (`PE-METAPROMPT-TEST-20260924.md`). PE37 then checked
every load-bearing claim against source. §2 marks which findings PE37 checked, and §8 lists what
nobody checked.

```text
Use PE Metaprompt 091426.1 — https://app.notion.com/p/3db4590a05eb8174be35d9e35acb3f77 — read it completely and follow it.

PROMPT_ID: https://app.notion.com/p/3d54590a05eb81a8b55afabc42298df9

PO_NOTE (Nathan, 2026-09-24, verbatim):
"We should create a new parent page for the next version of the GTWPE so the rewriting process has a clean organizational structure. From there, we can create the necessary sibling artifacts and run the required tests.

The first step should be to analyze `TW-MGTMT-10` using the PE Metaprompt. This is the correct starting point for the rewrite, and it also gives us an opportunity to validate the PE Metaprompt itself, which has not been tested since its most recent refactor.

Proceed with that analysis first.

As part of the analysis, verify that both the resulting approach and any proposed revisions are compatible with the Claude environment and aligned with the latest metaprompting best practices. Once that analysis is complete, we can use the findings to structure the new GTWPE parent page, define the sibling artifacts that need to be created, and establish the testing sequence."

Context from earlier the same day (Nathan, verbatim). It is a hypothesis to evaluate, not a decision:
"My current hypothesis is that the entire TW workflow can be executed within a single managing session using subagents. The workflow appears highly deterministic, and I believe it can be adapted to the skills, patterns, and operating processes we have already developed.
I would also be comfortable allowing that managing session to write approved changes directly and correctly into the relevant PFcanon Markdown files. I have had good results with complete-file updates in my recent ChatGPT runs. That experience was in ChatGPT rather than Claude, so treat it as evidence that the approach can work, not as proof that the same behavior has already been validated here."
```

**What the run read**, all completely:
- the PE Metaprompt;
- all eight selected TW prompts;
- the TW catalog, *Alpha 1 — Implementation and Validation*, and the HDE TW page;
- the GCFPE hub;
- `AGENTS.md`;
- the eight governing documents in `docs/prompt_ecosystem_management/`.

It read the release register and the Ops Hub in part, and PF03, PF04, PF06 and PF10 by keyword only.
It read nothing in Drive. It took the repository at `main` @ `25b2c87`.

**Result: `PARTIAL`.** The findings are complete. The durable run record that the PE requires for
multi-prompt work is this file, written by PE37 because the test run was read-only.

## 2. Findings on TW-MGMT-10

| # | Finding | Evidence: the TW text, then the current rule | What breaks in a real run | PE37 check |
|---|---|---|---|---|
| F1 | **The canon source is inverted** | TW-MGMT-10 does its compatibility reading "from `Glow / Core Docs / PFCanon`", and holds that "mirrors cannot replace current Drive PF authority". TW-DRAIN-10 says "All PF authority still comes from current Drive Markdown". Against that, `D7` and the PE: "PF resources are in the repository at `docs/pfcanon/`, read-only" | A run that obeys the prompts reads reference copies that carry no authority, and refuses the authoritative files. TW's records cite PF10 v13.1; the repository holds v13.3 | Checked in TW-MGMT-10 and TW-DRAIN-10 |
| F2 | **Output has no lawful destination** | Reports go to Drive `Glow / Ops / Assessments & Decisions`, "using Library for actual generated/attached deliverables". The PE: "Do not route important artifacts through ChatGPT Library" | Redline packages, reports and checkpoints have nowhere admissible to land. Claude has no Library | Checked |
| F3 | **The model-advice stage is outside what the PE may author** | An `<operator_model_guidance>` block ("ChatGPT Work — GPT-6 Astra — Extra High", "Approximate workload: 9–10/10"); TW-ASSESS-10 is mandatory; TW-DRAIN-10 will "stop before creating or applying redlines" without the assessment. The PE: "Do not create, request, evaluate, recommend, or route work through runtime-selection … or workload-rating fields" | The PE cannot revise any member without deleting this. Deleting TW-ASSESS-10 removes a member and every worker's entry gate, which is an Ecosystem Design change | Checked in TW-MGMT-10 and TW-DRAIN-10 |
| F4 | **It assumes a ChatGPT-only platform** | ChatGPT Work sessions named `TW-PFxx-x`, Library downloads, the `openai-docs` skill, the PF04 "Astra Max" hang | The session, delivery and research steps cannot run in Claude Code. `openai-docs` is not installed | Checked |
| F5 | **Three required procedures cannot be resolved** | TW-MGMT-10 requires three documents in Drive `Glow / Ops`. None is in the repository, and the v5.0.0 operating procedure names none. The PE: "Do not infer a `Glow / Ops` procedure route". The Ops Hub: "Where procedure lives — the repository, not ephemeral — canonical — 2026-09-21" | A maintenance run has no admissible source for three controls it must read | Checked |
| F6 | **It points at a removed PE feature, and asks for prompt fingerprints** | "Use PE's five-dimension descriptive complexity profile": the current PE has none. Its source register wants "useful fingerprints"; `prompt-corpus-policy.md` and `D22` forbid hashing a prompt body | An author looks for a feature that is gone, and hashes prompt bodies | Checked |
| F7 | **Rules are restated across prompts, and incidents became rules** | TW-MGMT-10 restates worker duties ("Cover RL-045's forbidden single-occurrence FIND_AND_REPLACE", "PF04 remains unresolved…"). The five workers repeat the same authority, preflight and save-recovery sections. Anthropic's prompt-audit guide names "Patch accretion" and "History narratives: past tense, incident IDs …" | A rule change takes five to eight edits, and the copies drift | TW-MGMT-10 checked; the repetition across workers rests on the run's reading |
| F8 | **The test baseline lives only in Drive** | "retain the established 18-case alpha suite". The suite and its 29 checks are cited only as Drive reports. TW has 0 rows in the contract registry and 0 graph parts | The GTWPE's testing sequence has no in-repository baseline to start from. The suite's content is Unknown | Checked |
| F9 | **`tw-flowmaster` is stale and does not implement the hypothesis** | Revision 1.2.0 runs one session per PF, pins prompts with hashes (defect TW-01, deferred), keeps the "GPT-5.6 Sol … Max … Ultra" rules, and names both Drive and `docs/pfcanon` as the PF source. `flowmaster-validate` line 184 requires "pre-creation and pre-Apply assessments" | It cannot run a single-session design, and it breaks `D22` and the model-advice ban. Changing it, or its validator, needs skill-change authority (`D24`) | Line 184 and the revision checked |
| F10 | **A name and a neighbour overlap** | UTIL-10 sits on the GCFPE hub titled "HDE TW — GCFPE-20260914.1 — 091426.1" and overlaps TW-APPLY-10. "Drain" means two different things in TW and in GCFPE | A GCFPE clean-up that searches for "TW" or "drain" can hit the GTWPE. UTIL-10 stays GCFPE-owned (the PE: "duplicate and customize the prompt for each ecosystem") | UTIL-10's parent checked; the "drain" overlap rests on the run's reading |

**Keep these in the rewrite.** They agree with PF03 §8 and PF06, and they are fragile operations
where exact wording belongs:
- the exact-redline contract: `REPLACE`, `DELETE` and `INSERT`; `FIND_AND_REPLACE` only for a count of 2 or more; no overlaps; every edit bound to the original;
- whole-batch rejection when any edit is invalid;
- the exact `no redlines` exit;
- PF09's six-dimension accounting;
- section-only PF20 and PF30 records;
- no invented IDs or statuses;
- drainage is not closure.

## 3. The two hypotheses

**A. One managing session with subagents: supported, with conditions. Not yet run in Claude.**
- It is the model the workspace already uses for maintenance. `D21`: "one session can carry the
  whole process". `execution-and-delegation-model.md` §1 uses in-session subagents because "A sibling
  cloud session receives a message but cannot message back". `D23-D`'s no-subagent rule binds GCFPE
  prompts only.
- "Highly deterministic" is true of the mechanics: literal counts, overlap checks, applying edits, the
  version, date and Last Update Gate update, and the preservation diff. It is not true of the drain
  judgement: which PF10 change goes into which PF, whether text is already equivalent, PF09 accounting,
  and record content. Put the mechanics in code, and give each target PF its own judging subagent.
- The conditions are the ones stated at the top of this record. The first two come from
  `execution-and-delegation-model.md`: in §5 a subagent "writes nothing", and in §7 a verifier must
  not see the answer it is checked against.
- In this environment subagent nesting is off (`CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH=1`), so only the
  managing session delegates, which is the shape the design wants.

**B. The session writes approved changes into `docs/pfcanon/`: forbidden today; workable only as exact edits in a pull request.**
- **Three controls forbid it now:**
  - `glow-write-boundary`, "read-only to you";
  - the PE, "read-only";
  - the release register, "forbidden to open a pull request or directly edit any PF document unless the Product Owner explicitly instructs that exact action".

  `AGENTS.md` alone has an exception, for a Product Owner instruction naming the files.
- **Complete-file regeneration is the wrong mechanism.** At about 4 bytes a token, six PFs are
  ≈ 140k–238k tokens (PF04, PF11, PF12, PF14, PF19, PF20), and Opus 5.5's maximum output is 128,000
  tokens. Anthropic's migration guidance: "try to surgically edit a file rather than rewrite the
  entire thing". Claude Code's edit tool already enforces the `REPLACE` contract: the old text must
  match exactly and uniquely, or the edit fails. `git diff` then proves nothing else changed, and
  Nathan's merge becomes the act that adopts the change.
- **Risk: nothing automated reviews these edits.** `docs/pfcanon/` is exempt from CI and from
  automated review (`AGENTS.md`), so reviewing the diff is the only check. The design has to supply
  its own mechanical check: the diff must equal the approved redlines.

## 4. Compatibility with the Claude environment

The environment is Claude Code on the web: a cloud session on Claude Opus 5.5, with the Notion,
Google Drive and GitHub connectors, the synced skills, and this repository.

### 4.1 TW-MGMT-10's assumptions

| TW-MGMT-10 says | In this environment | Result |
|---|---|---|
| An `operator_model_guidance` block: "ChatGPT Work — GPT-6 Astra — Extra High" | Nathan chooses model and effort for the session, turn by turn; a prompt body sets neither. Opus 5.5 offers `low`, `medium` (default), `high`, `xhigh` and `max`. Anthropic: "Start at `medium` … test several levels against your own evals" [P2]. A skill's or a custom subagent's **definition** can set `effort` [S1, S2] | **Incompatible as written.** The function has a Claude-native home, fixed per role in a definition and calibrated by test. The PE's exclusion rule currently forbids that (PE test, D7) |
| "The analyzer uses openai-docs" | No `openai-docs` skill is installed | **Incompatible** |
| "using Library for actual generated/attached deliverables" | No Library equivalent. Durable artifacts are repository files under `docs/ephemeral/`, landed by pull request | **Incompatible** |
| Procedures and PFs from Drive; "mirrors cannot replace current Drive PF authority" | Drive is connected but "not a storage authority at all" (`D7`) | **Conflicts with the workspace's rules** |
| Notion reads, successor publication, TW navigation edits | The Notion connector works; each write needs task-level authorization (`notion-write-boundary.md`) | **Compatible** |
| "do not … spawn agents without explicit applicable authorization" | Subagents are native. Each gets a fresh context with `AGENTS.md` loaded and its own tools, MCP connectors included. It cannot ask the user anything, and it can be isolated in a worktree [S2] | **Compatible.** The design must authorize them |
| "No PF mutation, repository change, PR, merge … follows from maintenance" | The PE sends Glow working artifacts to `docs/ephemeral/` by pull request | **Conflicts with the PE** |
| "retain the established 18-case alpha suite" | Drive reports only | **Cannot be re-run here as it stands** |
| Identity lines `<name> <version>` and `Prompt Version:` | Still required by the PE's general rule | **Compatible** |

### 4.2 The approach

| Element | What the environment and the rules say | Holds? |
|---|---|---|
| One managing session carries the flow | The coordinator model exists (`execution-and-delegation-model.md` §0). Opus 5.5 "sustains long-running autonomous work better than Claude Opus 5 … with parallel subagents" [P2] | **Yes** |
| A subagent drafts each PF's redlines | "Use subagents when tasks can run in parallel, require isolated context, or involve independent workstreams that don't need to share state" [P1] | **Yes**, and for isolated verification too |
| Applying the edits to one PF | "For simple tasks, sequential operations, single-file edits … work directly rather than delegating" [P1] | **In the managing session, mechanically** |
| Complete-file updates | Six PFs are larger than one response (§3 B) | **Only as a mechanical product:** apply the approved edits exactly, emit the complete file, and verify that the diff equals the approved redlines |
| Writing to `docs/pfcanon/` | Forbidden by three controls today (§3 B) | **Ruling needed:** decision 1 |
| Setting effort per role | Skills and subagent definitions can set `effort` [S1, S2]. The agent call takes a model but no effort. An agent definition would live in `.claude/agents/`, which is outside the paths a session may write | **For the design package** (§7) |
| Nathan's approval | A subagent cannot ask the user [S2] | **The gate stays in the managing session**, between drafting and applying |
| Session creation | None needed. `create_session` exists here but is lineage-limited, and `D23-D` bars automated session creation for GCFPE | **One session removes the issue** |

## 5. Current prompting practice

Sources, fetched 2026-09-24:
- **[P1]** *Prompting best practices*: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- **[P2]** *Prompting Claude Opus 5.5*: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5
- **[C1]** *Best practices for Claude Code*: https://code.claude.com/docs/en/best-practices.md
- **[S1]** *Skills*: https://code.claude.com/docs/en/skills.md
- **[S2]** *Subagents*: https://code.claude.com/docs/en/sub-agents.md
- **[A1]** Anthropic's prompt-audit guide, bundled with Claude Code 2.1.282: `claude-api/shared/prompt-audit.md`

| Practice | TW-MGMT-10 |
|---|---|
| "Show your prompt to a colleague with minimal context … If they'd be confused, Claude will be too." [P1] | Long compressed lists, for example "Keep worker essentials self-contained: current Drive PF authority and PF03, complete target/whole or selected-source reading, precise every-turn preflight, …" |
| "Providing context or motivation behind your instructions … can help Claude better understand your goals" [P1] | Rules are mostly stated without reasons |
| "Tell Claude what to do instead of what not to do" [P1]; "If you emphasize many lines, none of them stands out" [C1] | Heavy prohibition, for example "Do not overwrite, rename, suffix, move, archive, delete, trash or clear …" |
| Effort is "the main control"; "Lowering effort reduces thinking … more reliably than prompt instructions do" [P2] | Carries model advice in the body |
| "Give Claude something that produces a pass or fail, and the loop closes on its own" [C1] | Validation is prose, and its suite is in Drive |
| "Use git for state tracking" [P1] | Checkpoints go to a Notion control page and a Drive report |
| "Patch accretion" and "History narratives" are fossils to remove; "An LLM executor for a deterministic plan" is a pattern to remove [A1] | RL-045, the PF04 hang and dated model appraisals are written in as rules; deterministic checks are left to the model |

**The direction for the rewrite.** Each item uses only capabilities §4 shows are available:
1. Remove all model, effort and workload content from prompt bodies.
2. State the goal, inputs, outputs, authority and how to verify. Keep exact scripts only where one
   sequence is safe: redline literals, the canon write, and publication readback. [A1]: "Fragile
   operations keep exact scripts."
3. Replace incident histories with the rule each one produced.
4. State each shared contract once, in the manager or in a skill.
5. Put the deterministic checks in code.
6. Verify with an isolated subagent. Self-review is not validation (the PE; [C1] "Add an adversarial
   review step").
7. Let prompt bodies carry behaviour only (`prompt-body-content-policy.md`).

## 6. Inputs to the design step, not the design

**The next step is PE Ecosystem Design / Draft.** Its package, as the PE defines it:
- current and proposed membership, with dispositions;
- a Mermaid diagram;
- each prompt's purpose, owner, inputs, outputs, permitted writes, approval effects and completion;
- each producer-consumer contract;
- the single maintenance prompt's scope;
- a change plan with validation;
- the exact decisions needing approval.

That covers Nathan's three next items:

| Nathan's item | Where it sits in the design package |
|---|---|
| The parent page | The home the proposed membership publishes under (decision 3) |
| The sibling artifacts | The proposed membership and contracts |
| The testing sequence | The change plan's validation |

**Inputs the design must take:**
1. **A disposition for each of the eight members and for `tw-flowmaster`**, including
   `flowmaster-validate`'s TW assertions.
2. **One maintenance prompt, derived from the proposed `GCFPE-MGMT-10` body.** The PE: "When a
   common workflow component is needed in different ecosystems, duplicate and customize the prompt
   for each ecosystem as requested, record lineage, and approve updates separately". The GTWPE then
   inherits the Modification lifecycle and `D26`'s bounded reviews, the lessons of the larger workflow.
   Maintenance and the TW run stay separate prompts; TW-MGMT-10 already says "Maintenance is separate
   from ordinary execution".
3. **TW-ALPHA-20260908.1 stays intact.** It is marked superseded when the GTWPE is selected, and
   nothing is rewritten in place.
4. **Storage.**
   - Design, test specification and run records go under `docs/ephemeral/gtwpe.rewrite/`.
   - Any lasting procedure goes under `docs/prompt_ecosystem_management/`.
   - The Drive-only TW evidence is either migrated as repository fixtures where the design needs it,
     or retired.
5. **Code for the mechanics.** The exact-redline validator and applier is shared by TW-DRAIN-10,
   TW-DRAIN-20 and TW-APPLY-10, so it passes the PE's two-prompt skill test. Building it as a skill
   needs skill-change authority (`D24`).
6. **PF03, PF06 and PF10 read completely** before any new prompt is created. The PE mandates this
   for new Glow prompts.
7. **The PE Metaprompt's defects D1, D2 and D6 would hit the design step**
   (`PE-METAPROMPT-TEST-20260924.md`). Until they are repaired, the design invocation carries three
   workarounds:
   - procedure comes from `docs/prompt_ecosystem_management/`;
   - `D22` applies;
   - subagents are authorized as workers only.

**The testing sequence should include:**
- fixtures that store no prompt body;
- a static contract review;
- a first trial on one small PF with a small PF10 selection;
- one PF09 phase;
- one PF of 300 KB or more, to prove the path that never regenerates a whole file;
- isolated verification;
- `D26` review caps;
- if a skill is built, the skills guide's test: run each prompt "in a fresh session with the skill
  available and again with it disabled, and compare" [S1].

## 7. Decisions

| # | Question | Impact | Recommendation |
|---|---|---|---|
| 1 | May the GTWPE's managing session write approved PF changes into `docs/pfcanon/`? | Changes three controls; a canon write is hard to reverse | Yes: exact edits, in a pull request Nathan merges. The first trial runs under `AGENTS.md`'s per-change exception |
| 2 | Is one managing session with subagents the GTWPE's execution model? | Replaces the eight-prompt manual flow and `tw-flowmaster`'s one-session-per-PF model | Yes, confirmed by one trial run |
| 3 | Where does the GTWPE parent page go, what is it called, and what does GTWPE stand for? | Blocks publication; the PE forbids inventing a parent | Under `AI Prompts / HDE TW`, titled so it cannot be confused with the GCFPE hub "HDE TW — GCFPE-20260914.1 — 091426.1" |

**For the design package, not needed now.** Each has PE37's default recommendation:
- **Versioning.** Adopt C-VERSION and short handoffs for the GTWPE (AF-012 is still open for TW).
- **Effort.** No model or effort in any prompt body; Nathan sets effort per turn, measured in the
  first trial. Definition-level effort needs a PE ruling (PE test, D7).

## 8. Not verified, and not done

- No TW behaviour has been observed in Claude. The approach is untested.
- The Drive-only TW records (the requirements brief, the implementation and verification reports, the
  18-case suite) were not read.
- The three `Glow / Ops` procedures: content Unknown.
- The PF token sizes are estimates at about 4 bytes a token.
- Two findings rest on the test run's reading alone: the repetition across workers (F7) and the
  "drain" overlap (F10).
- Whether dynamic workflows are enabled in Nathan's managing session: Unverified.
- Nothing changed in Notion, Drive, the skills, the registry, the graph or canon.
