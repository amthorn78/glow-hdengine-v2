---
artifact_type: PROMPT_ECOSYSTEM_CONTROLLED_CONVENTION
artifact_version: "1.0"
created_date: 2026-09-21
revised_date: 2026-09-24 — *Loops*, D26
status: BINDING
authority: Product Owner direction 2026-09-21 — persistent procedure lives in the repository, not in Notion
migrated_from: Glow Operations Hub, *Source reads — minimal by rule — 2026-09-21*, *Tracking is part of the work — 2026-09-21*, *Worker communication rules — 2026-09-20*
---

# Session working rules

Four rules that govern how a session works rather than what it produces: how much source it reads,
how it records what it did, how it talks to other sessions, and how it reports a loop. Each was
written after the failure it prevents.

## Source reads — minimal by rule

Standing rule, Product Owner direction 2026-09-21. Applies to **every** prompt-engineering, analysis, repair, review and manager session, and to **every** Notion read without exception.
Added after PE35 pulled all 55 GCFPE prompt bodies — **1,060,628 bytes** — through its context in **55 sequential page fetches**, when the task required only that those 55 files exist on disk for a validator's `--prompt-dir`. The bodies were never reasoned about. Every fetch result was already being written to disk by the harness, so the entire read was waste. In the same session PE35 read **zero bytes** of this page, which its own handoff named as holding the reviewer-prompt rules, and shipped a reviewer prompt missing five mandatory elements as a result.
Both are one defect: **reading by volume instead of by need.**
### The rule
**Before any read, name the fact you need and the smallest unit that carries it.** If you cannot name the fact, you are browsing, and browsing is not a read.
1. **A corpus is data, not reading.** When N sources are inputs to a *tool*, land them on disk and let the tool read them. Never route a corpus through your own context. If the deliverable is "files in a directory", the content must never appear in a response.
   **This rule is about method and cost. It is not a permission gate, and it does not apply to prompt bodies.** Prompt bodies are never kept on disk — the Prompt Corpus Storage and Fidelity Policy forbids any standing copy, and a transient file the tooling makes in order to read a body is part of the read under its five conditions (`D22`) — and reading them is not restricted in any way. Read one or read all fifty-five, as the work requires. A session that cites this rule to avoid reading prompts has misread it; that happened once, and the correction is in `prompt-corpus-policy.md` under *Reading is not restricted. Copying is.*
2. **Fetch, persist, extract — never fetch and retype.** Tool results are recorded on disk. Extract the payload programmatically from that record. Retyping doubles the cost and adds transcription error as a new failure mode. **Prompt bodies are the exception to the persist half:** read them, take the finding, discard them. Rules 2, 3 and 4 say "to disk" because they were written for ordinary sources; for prompt bodies, keep only the finding. A file the tooling makes in order to read a body, such as the harness's save of a large result, is part of that read under `D22`'s five conditions: it serves the read in hand only and is never cached or re-read for later work (rule 4 does not apply).
3. **Size before reading.** A large result goes to disk and is read by slice, search or structured query. Reading a 100 KB page to find one table is a defect even when the answer is right.
4. **Read once.** Cache to disk, re-read from disk. A second fetch of unchanged content is a defect.
5. **Quote the minimum span that carries the claim.** In analysis and in reports, cite the sentence, not the section.
6. **Batch what must be fetched.** Sequential single fetches of a known set are a defect; the set is known, so request it as a set.
### The asymmetry that matters
**Governing controls are read in full. Corpora are not read at all.**
A control — this page, `AGENTS.md`, a plan, a registry, a canonical rule section — is short, decides what you build, and is read completely before you build it. A corpus is long, is consumed by a tool, and never needs your eyes. Spending context on the corpus while skipping the control is the exact inversion this rule exists to stop, and it is how a session produces a technically correct artifact that violates a rule it never read.
**Naming a control is not reading it.** A predecessor's one-line summary of a rule is not the rule. If a handoff names a page as governing, open it before producing the thing it governs.
### A grep proves the absence of a string, never the absence of a thing
Corollary, added 2026-09-21 after it cost a cycle. Searching for a named item and finding nothing is equally consistent with **corrected by rename**, **deleted**, and **silently dropped**. Reporting the third without excluding the first is judging by name instead of function — the failure `AGENTS.md` already names, in its most mechanical form.
**Before reporting anything as missing, absent, dropped or outstanding:**
1. Search for what it **does**, not what it is called — its behaviour, its error code, its neighbours in the same family.
2. Read the change that would have touched it. A rename is only findable in the patch that performed it.
3. If the record says an item was deferred into a later change, open that change. A later entry failing to mention an item is not evidence the item was dropped.
**And when a record misleads a reader, fix the record, not just the belief.** An item that landed but was never written down will mislead the next session exactly as it misled this one.
### Enforcement
This is measurable, so measure it. A session that reads a corpus into context states how many bytes and why. There is no acceptable answer for a corpus destined for disk.

## Tracking is part of the work

Standing rule, Product Owner direction 2026-09-21, after the same instruction was given to every session and followed by none of them. **Every step is tracked — the step, not the outcome only.**

**Where it is tracked depends on which kind of session you are.** Product Owner policy, 2026-09-22, `notion-write-boundary.md`:

| session | tracking destination |
|---|---|
| **Maintaining the ecosystem** — a `GCFPE-MGMT-10` run, a prompt-repair round, a release transaction | Notion, on the maintenance surfaces that already name it: the round-tracking page, the release register, the Alpha feedback list, the release controls. These are established destination rules, so the write is authorized by rule. Plus the repository, per `README.md`. |
| **Executing the ecosystem flow** — planning, implementing, reviewing or QA-ing a work unit | `docs/ephemeral/` in the repository, landed by pull request. **Read-only with respect to Notion** unless that specific task's instruction directs a Notion write. |

**Tracking is not a Notion-write requirement.** A development session that completes a task, produces a report or hands off to the next session has tracked its work correctly by landing it in the repository. Do not infer a Notion write from the work having happened — see `notion-write-boundary.md` for the list of things that are **not** an authorization.
The damage this repairs, measured rather than asserted:
- The governing repair plan's checklists stood at **101 boxes unchecked against 11 checked**, with unchecked items that were demonstrably complete and a `BATCH_2_BLOCKED` verdict from 2026-09-16 that nothing in twenty-plus later rounds either resolved or reaffirmed.
- The round-tracking page's own `status` and `gate` header stayed **twenty rounds stale**, still declaring a gate blocked that had been satisfied.
- `D5` landed in round 21 exactly as planned and **was never written down**, so a later session read the record correctly, concluded the item was open, and reported it to the Product Owner as a loose end. The record caused the error.
The through-line: work that lands without being recorded is indistinguishable from work that never happened, and the next session pays for it.
### The rule
**If your work changes the truth of anything written down, you change what is written down, in the same session — at the destination that already holds it.** That includes a checkbox, a status field, a frontmatter line, a verdict, a dated status sentence, and an item another page lists as open. The rule is about *not leaving a record false*; it never licenses creating a new Notion page to hold something nothing was tracking. If no existing record claims the thing, nothing has gone stale, and there is nothing to correct.
1. **Record steps, not just conclusions.** A round entry says what was done, measured, decided and deferred — each with its evidence. A conclusion with no visible step cannot be checked by anyone later.
2. **Update the artifact that tracks it, not only your own report.** Writing a round report is not tracking. If a plan, checklist or register holds the item, that is where the change belongs. A report the tracker does not point at will be missed.
3. **Close every deferral by name.** An item deferred into a later change is closed *in the record* when that change lands. Round 21 carried `D5` and did not say so; that silence cost a cycle.
4. **Never tick a box you cannot evidence.** Asserting completion without evidence is the same neglect facing the other way. Reconcile with the evidence named, and leave undetermined items explicitly undetermined with the one read that would settle them.
5. **Read it back before reporting it.** A write you have not read back is a claim, not a record.
6. **A stale current-state field is a defect, not cosmetics.** `status`, `gate` and frontmatter are what a reader trusts first. They are current-state fields, so they are corrected in place; dated entries below them are never rewritten (`AUTH-001`).
### Why sessions keep skipping it
Tracking presents itself as overhead attached to the end of real work, so it is the first thing dropped when context runs short or a task looks finished. It is not overhead. In a multi-session repair the record **is** the deliverable that survives the session, and every hour of the next session's work is priced off its accuracy.
**Budget for it before you start, not after you finish.** A session that runs out of room to record what it did has not finished; it has left the next one to pay.

## Worker communication rules


Written after a session in which the Product Owner had to ask, in sequence: *"are we talking about the same thing?"*, *"I am not sure if you are asking me a question or if I am waiting for you"*, *"is it useful or not?"*, and *"this odd backhanded way you have of asking for more actions is very confusing."* Each was caused by a specific, avoidable habit. The rules below name the habit and the fix.
These bind any session reporting to the Product Owner in this workspace. `glow-po-reporting` governs structure; this governs clarity.
### 1. The first line is the answer or the status
Never preamble. Never method-before-result. If asked *"is it useful?"*, the first word is Yes or No.
**Observed failure:** asked whether TypeSafe was useful, a worker returned three sections of methodology before answering. The Product Owner had to ask twice more.
### 2. Say what is needed, explicitly, every time
Every message ends in one of exactly three states, named:
- **DECISION NEEDED** — with options and a recommendation
- **NOTHING NEEDED** — work continues, no input required
- **IN FLIGHT** — something is running; the Product Owner waits
**Observed failure:** a status message left it ambiguous whether a question was pending, and the Product Owner had to ask which it was.
### 3. Never phrase a request as an observation
*"What I'd want before building v7 is…"* is a request for authorization wearing the costume of a remark. If input is needed, write **"I need X."** If it is not needed, do not mention it.
This is the single most-cited failure. It reads as passive-aggressive even when it is not intended that way.
### 4. State proven things flatly
Something reproduced by execution is reported as fact, without hedging. Confidence language is for genuine uncertainty only, and belongs in the sentence carrying the claim — never in a trailing caveat paragraph.
### 5. Reasoning only when asked, or when it changes the decision
Method, rationale and alternatives considered are omitted by default. They are supplied on request, or when knowing them would change what the Product Owner does. Everything else is noise.
### 6. Corrections: once, flat, at the top
State what was said, what is true, what changed. No cushioning, no reconstruction of how the error happened, no repeated apology. Then continue.
### 7. Deliverables are verified usable before they are sent
Name the format. Confirm the recipient can open and use it. Where an installable artifact is required, produce the installable artifact — not a diff, an archive, or a set of files requiring manual reassembly.
**Observed failure:** a skill repair was delivered three times — a `.tgz`, then renamed loose `.py` files, then finally a `.skill` package — because the worker did not check the required format before sending. Two wasted turns.
### 8. Disambiguate overloaded vocabulary on first use
This workspace reuses "pilot", "PoC", "review", "round", "gate" and "flag" across unrelated things. Name which one is meant, or use a distinct word.
**Observed failure:** "pilot" simultaneously referred to a retired execution-model pilot, a failed automation pilot, and a live TypeSafe test. The Product Owner had to ask which.
### 9. Length is a defect
If a message can be cut by half without losing a fact the Product Owner needs, it was too long. Tables and lists beat paragraphs. A status update is one to three lines.
### Note on enforcement
This page records the rules; it does not load them. A session reads its installed skills, not the Operations Hub, before writing. **The durable enforcement path is ****`glow-po-reporting`**, which is already loaded before every report to the Product Owner. Rules that must survive into future sessions belong in that skill, packaged with `skill-creator` and installed by the Product Owner. This page is the reference; the skill is the mechanism.

## Loops

Standing rule, `D26` (2026-09-24). Written after eight PLAN review rounds on
`MODIFICATION-20260923-closeout-residuals` ran for most of a night with nobody told they were not
converging. Applies to any repeated round: a review, a repair, a re-run.

1. **A status update inside a loop carries the trend and an option to stop.** One to three lines:
   the round, the count of distinct confirmed required defects against the last round, and "stop
   here and take it as it stands" as a named option.
2. **A changed commitment is headlined as a correction.** If the session said it would bring the
   work back after a review and then kept going, the next message opens with that, flatly.
3. **A compaction summary quotes, it does not paraphrase.** It carries the session's own commitment
   word for word and Nathan's reply to it word for word, and every stopping rule it states names who
   set it and when. "Continue when the review is done" must not become "repair until clean".
4. **Re-price at twice the estimate.** When time or tokens pass twice the estimate Nathan approved,
   stop and return to him with the new estimate before the next round.
5. **Stop on non-convergence.** When required defects do not at least halve, or most of a round's
   findings sit in text the last repair added, return to Nathan with a `DECISION NEEDED`. Looking
   harder is not the response (`D26-F`).

None of this is mechanically checked, and `D26` says so. `glow-po-reporting` needs the same lines;
it is a skill, so they wait for its next package cycle.
