---
artifact_type: PE_WORK_RECORD
created_date: 2026-09-24
session: PE37 (`session_018teDumz2XyKdoXF9p3BKFM`)
authority: Product Owner instruction, 2026-09-24 — "it also gives us an opportunity to validate the PE Metaprompt itself, which has not been tested since its most recent refactor"
subject: PE Metaprompt 091426.1, Notion 3db4590a05eb8174be35d9e35acb3f77, last edited 2026-09-23T17:17:22.217Z
status: RECORD — test findings for the next PE Metaprompt maintenance; nothing was changed
---

# PE Metaprompt 091426.1 — first test since the 2026-09-23 refactor

**It works for Analyze.** In a fresh context, following only its own text, it:
- chose the right mode in one step;
- read every source completely or declared the bound;
- stayed inside Analyze's limits;
- returned an honest result.

Every claim PE37 checked held (the checks are listed below).

**It should not carry design or authoring outside GCFPE unrepaired.** It has eleven defects. The worst,
D1, caused a breach of `D22` during this test.

The run it was tested on is TW-MGMT-10's analysis, recorded in `TW-MGMT-10-ANALYSIS-20260924.md`
beside this file.

## How it was tested

Anthropic's "golden rule" is the method: *"Show your prompt to a colleague with minimal context on
the task and ask them to follow it. If they'd be confused, Claude will be too."* (Prompting best
practices, platform.claude.com, fetched 2026-09-24.)

- **Who ran it.** A fresh-context subagent (general-purpose, Opus 5.5, in the PE37 session). It
  received only the invocation Nathan would paste and four test limits. The invocation is in
  `TW-MGMT-10-ANALYSIS-20260924.md` §1.
- **The four limits.**
  - It could not ask Nathan anything; it had to record each question and the assumption it used.
  - It was read-only.
  - It could keep no prompt body on disk.
  - It could start no session or subagent and run no live prompt.
- **How PE37 judged it.** PE37 scored the run against the PE Metaprompt's own Analyze contract and
  checked the run's load-bearing claims against source.

## Scorecard against the PE Metaprompt's own contract

| Check | The PE Metaprompt's requirement | What the run did | Result |
|---|---|---|---|
| Mode | "Analysis requests, including ecosystem analysis, use Analyze / Inspect." | Analyze / 0 — Inspect, by that rule | Pass |
| Target | resolve the name "from an exact override or operative body identity" | Resolved "TW-MGTMT-10" through the exact `PROMPT_ID`, and recorded the assumption | Pass |
| Complete reads | "Read each source prompt and creation brief completely", with a source record | 15 Notion pages recorded with ID, parent, last-edited time and completeness. The tool-saved PE body read by slices to the end | Pass |
| Bounded claims | "Never infer document-wide or ecosystem-wide findings from a bounded extract." | PF03, PF04, PF06 and PF10 read by keyword only, declared, with no whole-document claim | Pass |
| Glow sources | "PF resources are in the repository at `docs/pfcanon/`, read-only"; "Do not infer a `Glow / Ops` procedure route" | Read nothing in Drive. Reported the TW prompts' Drive canon as a finding | Pass |
| Product Owner note | "Read a supplied PO Note completely and apply each directive within its exact scope." | Gave each directive a disposition | Pass |
| Model-advice exclusion | "Do not create, request, evaluate, recommend, or route work through runtime-selection … or workload-rating fields." | Identified the content without appraising it | Pass, with the tension in D7 |
| Tool availability | "Distinguish available, documented-only, unverified, and unavailable." | A capability table in those four classes | Pass |
| Analyze limits | "Do not author executable replacement prompt bodies"; "Proposed architecture diagrams require Draft authority." | Returned design inputs only: no design and no bodies | Pass |
| Result | "Use a precise result" | `PARTIAL`: the durable run record could not be saved in a read-only test | Pass |
| Handoff | "only when a handoff is actually needed" | None, with the reason | Pass, with the conflict in D5 |
| Unknowns | "Mark inaccessible facts Unknown" | Stated, with reasons | Pass |
| The prompt-corpus rule (`D22`) | Stated only in the GCFPE overlay: "never hashed, byte-compared or kept as a standing copy" | Hashed its transient PE-body file once, before it had read `D22`. The value was unused, disclosed, and the file deleted | **Fail**, caused by D1 |

**Claims PE37 checked, all of which held:**
- **Environment and bundled guidance:**
  - `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH=1`, and Claude Code is 2.1.282.
  - The bundled `claude-api/shared/prompt-audit.md` (39,013 bytes) carries the quoted "Fossils", "Patch accretion", "History narratives", "An LLM executor for a deterministic plan" and "Fragile operations keep exact scripts".
  - `model-migration.md` says "surgically edit a file rather than rewrite the entire thing".
- **Repository:**
  - `flowmaster-validate` line 184 requires "pre-creation and pre-Apply assessments".
  - `prompt-corpus-policy.md` and `D22` condition 3 prohibit hashing a body.
  - The v5.0.0 operating procedure names neither missing document (0 matches).
- **Notion:**
  - The register says agents are "forbidden to open a pull request or directly edit any PF document unless the Product Owner explicitly instructs that exact action".
  - The Ops Hub says "Where procedure lives — the repository, not ephemeral — canonical — 2026-09-21".
  - TW-DRAIN-10 reads "PF Markdown through Google Drive", holds that "All PF authority still comes from current Drive Markdown", and says it will "stop before creating or applying redlines" without its assessment.

## Defects, ranked by consequence

| # | Defect | Evidence | What it does in a real run | Fix |
|---|---|---|---|---|
| D1 | **`D22` is stated only for GCFPE.** The general source rule asks for a source record with "complete retrieved representations"; "never hashed, byte-compared or kept as a standing copy" appears only in the GCFPE overlay | The test run hashed the PE body's transient file | A run on any non-GCFPE ecosystem gets no warning, and breaches `D22` condition 3 | Move the prompt-corpus rule, and `D22`'s five conditions for transient read files, into the general *Source acquisition* section |
| D2 | **Its procedure route points at documents that are not there.** "…in `docs/ephemeral`, including `NON-CANONICAL — General Prompt Flow and Creation Guidelines` and `Prompt Selection and Session Delegation Protocol`" | Neither file exists in the repository. They are Drive files (the Guidelines at v1.11.0, `docs/ephemeral/HDE-EPIC040-PR40-workspace-register.md:230`). The Ops Hub puts procedure in `docs/prompt_ecosystem_management/` | Every Glow run has an unresolvable required source | Point the rule at `docs/prompt_ecosystem_management/` (its README) and drop the two names |
| D3 | **Stale repair text is still operative.** "For this repair" appears 3 times; the Alpha baseline block reads `ALPHA_STOPPED_PENDING_CHANGE_FLOW_REFACTOR`, next unit `HDE-EPIC040-PR04`, stage PR-10; "read all 54 predecessor bodies and all 55 candidate bodies" | PR05's implementation plan merged on 2026-09-24 (#491) | A run reads a false current state, and must work out for itself that it is history | Delete it; the history is in the decision record |
| D4 | **GCFPE-only text sits outside the GCFPE overlay.** "PR work runs in Claude Code…" is under the general *Skills, tools, and integrations*; "Artifact availability at the native stage" (QA-10 through Isis) is under the general *Run state* | Found by the test run | A non-GCFPE run must classify every section by its content | Move both into the overlay |
| D5 | **Two handoff rules.** "For every continuation, require exactly one … `NEXT_PROMPT_HANDOFF` block" against "Provide a concise populated next invocation only when a handoff is actually needed" | Found by the test run | Runs may differ on whether an analysis emits a handoff | Keep one rule |
| D6 | **Silent outside GCFPE.** Nothing says which PE version governs a non-GCFPE ecosystem (its `selection_rule` ties its status to the GCFPE register). There is no platform statement, and no subagent rule except GCFPE's C-TOP | Found by the test run | A non-GCFPE run has no rule for delegation or the platform | Add a short general section on execution platform and delegation |
| D7 | **The model-advice ban also forbids *evaluating* model and effort.** Effort is the platform's "main control" for reasoning (*Prompting Claude Opus 5.5*), and Claude Code skills and subagent definitions can each set `effort` | Found by the test run, and by PE37 | A PE analysis cannot assess a large part of current Claude guidance, even when the Product Owner asks for it | A ruling. Keep model and effort out of prompt bodies, since a body cannot set them anyway, but let an analysis evaluate definition-level settings when the Product Owner asks |
| D8 | **A PE refactor does not reach non-GCFPE consumers.** TW-MGMT-10 still tells authors to "Use PE's five-dimension descriptive complexity profile"; the current PE has none | Found by the test run | A consumer follows a rule that no longer exists | After a PE change, run the old-text search (`D26-E`) over non-GCFPE consumers too |
| D9 | **Its claims about the environment are out of date.** "Use `gh` … if it is not, ask the operator to install/authenticate it or provide a token"; "there is no connector abstraction to fall back on"; "Use `flowmaster-propagate` …"; "not programmable ChatGPT variables" | In cloud sessions `gh` is absent and GitHub goes through the GitHub MCP server, with credentials the proxy injects. `flowmaster-propagate` is not installed | A PR session could ask Nathan for a token it does not need | Update these to the cloud-session facts. It is GCFPE PR-lane text |
| D10 | **Its Drive rule contradicts `D7`.** Rule 8 says "Resolve Drive references through connected Google Drive and the current selection controls"; `D7` says Drive "is not a storage authority at all" | Found by the test run | Runs can differ on whether Drive is a source | Limit rule 8 to a file Nathan directs |
| D11 | **Size and emphasis.** 75,530 characters and 10,113 words; 37% of the body (27,607 characters) is the GCFPE overlay; 114 negative directives ("Do not", "never", "must not") in about 581 sentences | Measured by PE37 from its transient read. Current guidance: "If your CLAUDE.md is too long, Claude ignores half of it because important rules get lost in the noise"; "If you emphasize many lines, none of them stands out" (*Best practices for Claude Code*); "Tell Claude what to do instead of what not to do" (*Prompting best practices*) | Slower runs, and rules that get lost; the test run reported the overlay slowed it on a non-GCFPE target | Load the GCFPE overlay only for GCFPE work, and restate the key rules positively with their reasons. This is a design-level change to the PE |

## What worked, in the test run's words

- The routing table gave one mode in one step.
- The model-advice ban turned TW's largest problem into a mechanical test.
- The completeness rules fitted how the tooling saves large results.
- The availability classes shaped the environment check.
- The duplicate-and-customize rule and the skill-candidate test settled UTIL-10's ownership and two skill candidates without judgement calls.

## Incidents, disclosed under `D22` condition 5

1. **The test run hashed a prompt body.** At about 23:24Z it hashed its transient PE-body file with `sha256sum`, before it had read `D22` condition 3. The value was never used or reported. It deleted that file, and a command-output file holding three short PE excerpts, after use. Cause: D1.
2. **PE37's own transient read.** PE37 read the PE body from its own transient file by character slices, and counted words, sections and directives from it. It never hashed the file, and deleted it on 2026-09-24 after use.
3. **A lapse from earlier today.** A PE37 Notion-reading subagent left a transient PE-body file (created 18:45:22Z) in the session's tool-results directory after its task ended, contrary to `D22` condition 4. PE37 found it and deleted it during this task.
4. **A commit during the test run.** PE37 committed `2fdd7a2` into the shared working tree mid-run. The test run did not read it, though one search printed two of its lines.

## Cost

| Run | Time | Tool uses | Tokens |
|---|---|---|---|
| The test run | 25 min 14 s | 102 | 620,128 |
| The documentation research subagent | 3 min 4 s | 17 | 87,640 |

## Where the fixes go

The PE Metaprompt is a GCFPE control: the register binds it. Under the `D23` successor of
2026-09-23 it follows C-VERSION, so a changed body gets a successor page, which the register then binds.
Its repair is therefore a `GCFPE-MGMT-10` Modification. The queued MGMT-10 promotion Modification
can carry it.
