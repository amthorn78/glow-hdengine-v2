---
artifact_type: PE_IMPLEMENTATION_PLAN
plan_id: GTWPE-IMPL-PLAN
version: "1.1"
created_date: 2026-09-25
revised_date: 2026-09-28 — P0 findings applied (§15)
supersedes: GTWPE-IMPLEMENTATION-PLAN-v1.0.md (kept as issued)
facilitator: PE37 (`session_018teDumz2XyKdoXF9p3BKFM`)
executor: one worker session, W1, which Nathan starts with the kickoff in §14
status: G0 — v1.0 was acted on when Nathan started W1 with the §14 kickoff on 2026-09-25; his confirmation of G0 for this version is recorded in §15 when given
inputs: TW-BASELINE-20260924.md, TW-MGMT-10-ANALYSIS-20260924.md, PE-METAPROMPT-TEST-20260924.md (same directory)
---

# GTWPE implementation plan

**It builds the GTWPE: one repeatable production flow that starts from either of two inputs and
ends with validated, finished PF documents in `docs/pfcanon/`.** One worker session (W1) executes.
PE37 facilitates: it manages the relay, scores each step with TypeSafe, keeps the error log, runs
validation and gives final acceptance. Nathan approves at six gates (§6) and merges every pull
request.

## 1. Authority

**Nathan's rulings of 2026-09-25, on the decisions in `TW-MGMT-10-ANALYSIS-20260924.md` §7:**

| # | Ruling | Nathan's words |
|---|---|---|
| 1 | The GTWPE managing session may write approved PF changes into `docs/pfcanon/`, as exact edits in a pull request he merges. The first live change runs under `AGENTS.md`'s per-change exception | "Yes." |
| 2 | The execution model is one managing session with subagents | "Yes, that is the intended goal." |
| 3 | The parent page goes under `AI Prompts / HDE TW`, titled "GTWPE — Glow Technical Writing Prompt Ecosystem" | "Approved." |

**The same message also instructed:**
- W1 executes, with PE37 as facilitator (relay and TypeSafe);
- this plan comes first;
- the flow has two starting paths;
- PF27 and PF30 are updated only when a specification exists.

**What the rulings do not yet change.** Three controls still forbid canon writes:
- `glow-write-boundary`;
- the PE Metaprompt's "read-only" line;
- the release register's PF rule.

Ruling 1 is carried out through them in P5 (§5). Until then, every canon write goes through
`AGENTS.md`'s exception: Nathan's approval names the exact file. `D22`, `D24` and `D26` apply
throughout.

## 2. The flow W1 will build

### 2.1 Two starting paths

| Path | Inputs | What it produces |
|---|---|---|
| **A — Document** | One source document of a supported type (§2.3) | The finished PF documents the document requires |
| **B — Specification + PF10** | A specification, plus the applicable PF10 file set | The finished PF documents the PF10 set requires, plus the PF27 and PF30.1 updates the specification requires |

### 2.2 How the flow decides which documents change

Only the inputs that actually exist decide it. The flow never adds a target just to be complete.

| Inputs present | Targets | PF27 and PF30.1 |
|---|---|---|
| A document only | The PFs the document's content bears on, found by reading the document against each PF's declared purpose and scope | **Not touched.** A missing specification never blocks Path A |
| A specification and PF10 | The PFs the PF10 addenda address (today's triage), plus PF27 and PF30.1 | **Evaluated.** PF30.1 gets the change's record. PF27 changes only if the specification changes a template it owns. Each gets a finding of either `CHANGE` or `NO_CHANGE: <reason>` |
| A specification, a document, and PF10 | The union of both rows | Evaluated, as in Path B |
| A specification without PF10 | The specification's own targets, plus PF27 and PF30.1 | Evaluated. PF10 is treated as absent, not as an error |
| PF10 only | The PFs its addenda address | Not touched |
| Nothing usable | None | Stops with `BLOCKED: INPUT_MISSING` and a list of the accepted inputs |

A target the flow is unsure of is **named with its reason and put to Nathan at gate G3**. It is
never silently dropped and never silently added.

### 2.3 Supported inputs

Each input is normalized into a Markdown source record under
`docs/ephemeral/gtwpe.runs/<run-id>/source/`, recording its origin, type and how it was read:

| Type | How it is read |
|---|---|
| Markdown or text, as a repository path, an upload, or pasted text | As is |
| `.docx` | The `docx` skill |
| `.pdf` | The `pdf` skill |
| HTML | Converted to Markdown |
| A Notion page | Fetched live. A prompt body stays out of the record (`D22`) |
| A spreadsheet (`.xlsx`, `.csv`) | The `xlsx` skill, only when its tables are the content |

The readers' dependencies are not preinstalled here (W1 P0 §4.5: pandoc, pypdf, openpyxl and HTML converters are absent; PyPI is reachable). P1's design names how S1 provisions a pinned reader for each type, and P2 builds and tests it; a reader that cannot be provisioned stops with `BLOCKED: UNSUPPORTED_INPUT <type>`, never a guessed conversion.

Any other type stops with `BLOCKED: UNSUPPORTED_INPUT <type>`. The flow never guesses at an
input's content.

### 2.4 Stages of one run

Everything runs in one managing session. Subagents are workers only: they write nothing, and they
cannot ask Nathan anything.

| Stage | Who | What it does | Check that can fail |
|---|---|---|---|
| S0 Intake | Manager | Determine the path (§2.2), give the run an ID, write `RUN.md` | Every input is resolved, or the run is `BLOCKED` with its reason |
| S1 Normalize | Manager | Write the source records (§2.3) | Each record has its origin and read method, and its reads are complete |
| S2 Targets | Manager, with one subagent per candidate PF when there are many | Decide the target list and its reasons | Every target cites the source passage that requires it. PF27 and PF30.1 are evaluated if and only if a specification exists |
| S3 Draft | One subagent per target PF | Write the redlines in PF03 §8 format (`INSERT`, `REPLACE`, `DELETE`), with a report. Output is `READY`, `NO_CHANGE` (exactly `no redlines`) or `BLOCKED` | The validator in S4 |
| S4 Validate | Script `gtwpe_redline.py validate` | Checks each anchor is literal and occurs exactly once, the edits don't overlap, the batch applies in one pass, and the version, date and Last Update Gate fields are right | Exit 0, or the whole batch is rejected and goes back to S3 once (§8) |
| **S5 Approval: G3** | **Nathan** | Approves a package that names each file, edit and new version. This approval is `AGENTS.md`'s "direct and specific" instruction | The approval is recorded verbatim in `RUN.md` |
| S6 Apply | Script `gtwpe_redline.py apply` | Applies the edits exactly, writes the complete file under its new versioned filename, and removes the old one | The script's diff check: the change equals the approved edits and nothing else. The whole file is never regenerated |
| S7 Verify | A fresh subagent that is not shown the expected result | Reads the approved package and the applied file independently, and reports any difference | Zero differences, or the run stops (§8) |
| S8 Publish: G4 | Manager opens the canon PR; Nathan merges | One canon PR per run, on its own branch, touching only the target files. It is the one PR whose merge matters: the merge adopts the change (ruling 1). No other work waits on it; only S9 does | The PR's diff equals S6's diff |
| S9 Close | Manager | After the merge, reads the files back from `main`, finishes `RUN.md`, writes the run report | The files on `main` equal S6's output |

### 2.5 Proposed membership, confirmed at G1

| Current | Proposed |
|---|---|
| TW-TRIAGE-10 | Folded into S2 |
| TW-DRAIN-10 and TW-DRAIN-20 | Subagent briefs inside the run prompt. The PF09 six-dimension rules are kept |
| TW-APPLY-10 | Replaced by `gtwpe_redline.py`, plus S6 and S7 |
| TW-ASSESS-10 | Retired. Nathan sets effort per turn, and PE37 recommends it |
| TW-RECORD-20 | Becomes the PF30.1 record step in Path B |
| TW-RECORD-10 | Open question Q1 (§13) |
| TW-MGMT-10 | Replaced by **GTWPE-MGMT-10**, derived from the proposed `GCFPE-MGMT-10` body with its lineage recorded. It keeps the Modification lifecycle and `D26` |
| `tw-flowmaster` | Retired through a `D24` skill package that Nathan installs (P5) |
| New: **GTWPE-RUN-10** | The run prompt for §2.4 |

TW-ALPHA-20260908.1 stays intact. Its pages get a superseded banner at G5, and none is rewritten.

## 3. Roles

| Role | Holds | Never does |
|---|---|---|
| **Nathan** | G0 to G5, every merge, every skill install, starting W1 | Routine analysis or artifact work |
| **PE37**, the facilitator | The relay; one TypeSafe-scored effort level per step; the error log (§7); validation at each checkpoint; the checkpoint decision; final acceptance | Doing W1's work; merging |
| **W1**, the worker | Executing P0 to P5; opening PRs; the run records | Merging; creating sessions; approving its own work; running subagents as prompts rather than as workers |
| **W1's subagents** | Drafting, classifying and verifying, each with exact scope and a fixed return format | Writing anything |

## 4. Where things live

| What | Where |
|---|---|
| This plan, the design package, the error log, checkpoints and relay notes | `docs/ephemeral/gtwpe.rewrite/` |
| Each production run's records | `docs/ephemeral/gtwpe.runs/<run-id>/` |
| `gtwpe_redline.py` and its selftest, which outlive any run | `docs/prompt_ecosystem_management/gtwpe/` |
| Prompt bodies | Notion only, under the GTWPE parent page |
| Finished documents | `docs/pfcanon/`, by PR only |
| Fixtures | Synthetic Markdown only. No prompt body is ever stored (`D22`) |

## 5. Phases

Every phase ends at a **checkpoint**. W1 commits and pushes its records, updates `CHECKPOINT.md`,
and relays a report ending in `DECISION NEEDED`, `NOTHING NEEDED` or `IN FLIGHT`. PE37 validates
the report before the next phase starts.

| Phase | W1 does | Output | Validation checkpoint (PE37) | Gate |
|---|---|---|---|---|
| **P0 Preflight** | Read this plan, `AGENTS.md`, the three input records and the PE Metaprompt (with the workarounds in §14). Probe the environment: the connectors, the skills, `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH` | `CHECKPOINT.md` at P0 | V0: every source read completely, every probe recorded | — |
| **P1 Design** | PE Ecosystem Design / Draft: membership (§2.5), a Mermaid diagram, per-prompt contracts, producer-consumer contracts, GTWPE-MGMT-10's scope, the change plan, the test specification (P4). One dry run, then at most one diff check (`D26-A`) | `design/GTWPE-DESIGN-v1.0.md` | V1: every requirement in §2 has a home; the reviews ledger is within the caps | **G1** |
| **P2 Tools** | Write `gtwpe_redline.py` (normalize, validate, apply, diff check) and a selftest of at least 30 positive and negative cases | The script, its selftest, and a guard proof like `guard_proof.py` | V2: selftest 100%; every check proven to fail when disabled | — |
| **P3 Publish** | Create the parent page, then GTWPE-RUN-10 and GTWPE-MGMT-10 under it, and the GTWPE catalog entry. Read every write back | Page IDs and readback evidence in `CHECKPOINT.md` | V3: title, parent and complete body verified; no page outside the approved list | **G2**, before any write |
| **P4 Trials** | Run the test specification (§11). T1 to T5 run on scratch copies; T6 is live | Run records for each trial | V4: every expected result matched, and every mismatch is in the error log with a disposition | — |
| **P5 Adoption** | In this order: (1) the skill package through `D24` — an exception in `glow-write-boundary` for GTWPE canon PRs, `tw-flowmaster` retired, `flowmaster-validate` updated — installed by Nathan and read back; (2) only then T6, the live pilot through S5 to S9; (3) the superseded banners and a decision-record entry | A merged pilot PR; the skill package; the banners | V5: the pilot's files on `main` equal the approved edits; the skills are installed and read back | **G3 and G4** in the pilot; **G5** for acceptance |

## 6. Nathan's gates

| Gate | He approves | Before |
|---|---|---|
| G0 | This plan, v1.0 | W1 starts |
| G1 | The design package, pinned by its version | Any page, tool or prompt is written |
| G2 | The list of Notion writes | The first Notion write |
| G3 | Each change package: its files, edits and versions | Any change is applied to a canon file |
| G4 | Each canon PR, by merging it | The change is in canon |
| G5 | Final acceptance and GTWPE selection | TW-ALPHA is marked superseded |

A skill package also needs his install, under `D24`.

## 7. Error tracking

**One ledger:** `docs/ephemeral/gtwpe.rewrite/ERRORS.md`. W1 reports each error in its relay
message; PE37 enters it and keeps the ledger. Each row records:

| Field | Values |
|---|---|
| `id` | `E-001`, and up |
| `phase / step` | For example `P2 / selftest` |
| `class` | `SOURCE` · `TOOL_ACCESS` · `AUTHORITY` · `VALIDATION` · `PLAN_DEFECT` · `PROMPT_DEFECT` · `EXTERNAL_PENDING` |
| `severity` | `REQUIRED` (R1 to R4 of the review rubric) or `LISTED` |
| `found by` | W1, a W1 subagent, PE37, a reviewer, or Nathan |
| `evidence` | A path, a command and its output, or a page and its time |
| `disposition` | `FIXED <commit>` · `DECLINED <reason>` · `ACCEPTED_RISK` (only when Nathan approves it, per `DISP-001`) · `OPEN` |

**A phase does not close with a `REQUIRED` error open.** A `LISTED` error open at G1 or G5 goes to
Nathan as an accepted risk.

## 8. Failure handling and recovery

**The rule (`D26-B`).** Before the first external write, a failure is repaired in place, with at most
two materially different attempts. After an external write (a Notion page, a canon PR, a skill),
W1 stops. It writes a failure record, sweeps read-only for what landed, keeps everything else
frozen, and returns to PE37, who brings it to Nathan. Nothing retries a write it cannot see.

| Failure | Detection | Recovery |
|---|---|---|
| An input is missing or unreadable | S0 or S1 | `BLOCKED: INPUT_MISSING`, or `UNSUPPORTED_INPUT`, naming the input. Nothing downstream runs |
| A target is ambiguous | S2 | Named with its reason at G3; never guessed |
| An anchor is not unique, or edits overlap | S4 validator | The batch is rejected whole and goes back to its drafting subagent once, with the diagnostic. A second failure is logged `REQUIRED` and taken to Nathan |
| The drafting subagent returns `BLOCKED` | S3 | The exact missing authority or source is logged and taken to Nathan. There is no silent no-change |
| The apply diff differs from the approval | S6 diff check | Stop. No file is kept. Logged `REQUIRED`; the defect is in the script or the package |
| The verifier disagrees | S7 | Stop. PE37 compares the two centrally, never inside the worker (delegation model §7) |
| The PF changed on `main` after drafting | Before S6, and again at S8 | Re-read, re-validate, and re-approve at G3 if any anchor moved. An approval of the old text never carries over |
| CI is red, or the PR conflicts | S8 | Diagnose. Fix only within the approved edits; anything else goes back to G3 |
| A Notion write times out or is ambiguous | P3 | Inspect the exact target first, and never write twice blind |
| W1's context fills, or W1 compacts | Any phase | Resume from `CHECKPOINT.md` and the committed records only (`D26-C`) |
| W1's session is lost | Any phase | Nathan starts a new W1 with the resume kickoff (§14), pointing at `CHECKPOINT.md` |
| A PE Metaprompt defect bites | P1 or P3 | Apply the §14 workaround, log it as `PROMPT_DEFECT`, continue |
| A rule conflict or missing authority | Any | Stop the affected work, `DECISION NEEDED` to Nathan through PE37, and continue any independent work |
| A review loop runs over its cap | P1 or P5 | `D26-A`: two full reviews and one diff check at most; stop early at twice the estimate |

## 9. Checkpoints and resume

`CHECKPOINT.md` holds:
- the last completed step;
- the head commit of each branch;
- every external write, with its identity;
- the open errors;
- the next action.

W1 updates it at each phase end and before every external write. A resume starts only from a
checkpoint, reads the file, re-verifies the recorded external writes, and never repeats one.

## 10. Relay and TypeSafe protocol

1. W1 ends each checkpoint with a report. Nathan pastes it to PE37 prefixed `relay:`.
2. PE37 checks the report against the repository, Notion and the plan, and updates `ERRORS.md`.
3. PE37 gives Nathan the exact reply text, plus **one** effort level for W1's next turn. The level is
   scored with the frozen TypeSafe v4 method: `jev-1.13.0`, the level from the effort score, and
   ultracode only when P(single_session) < 0.5.
4. PE37 logs each recommendation in the TypeSafe usage log in Notion. Nathan reports the level he
   used.
5. A question W1 asks mid-turn inherits that turn's level.

## 11. Test specification, finalized in P1

| Trial | Input | What it proves |
|---|---|---|
| T1 | Path A: a short Markdown document bearing on one small PF | The document route with no specification: PF27 and PF30.1 untouched |
| T2 | Path B: a synthetic CRD specification plus PF10 | PF30.1's record and PF27's evaluation; the PF10 targets |
| T3 | A PF09 phase target | The six-dimension accounting |
| T4 | A target of 300 KB or more (PF04, PF12, PF14 or PF19) | The exact-edit path; nothing regenerated |
| T5 | Negative cases: a non-unique anchor, overlapping edits, an unsupported type, a missing input, a PF changed mid-run | Each fails loudly, with the expected blocker |
| T6 | One real, approved change, run live through the PR and Nathan's merge | The whole flow end to end |

T1 to T5 write only to scratch copies and to `docs/ephemeral/`. T6 is the only live canon write.

## 12. Estimate (`D26-D`)

| Phase | Time | Tokens |
|---|---|---|
| P0 and P1 | about 3 h | about 2M |
| P2 | about 2 h | about 1M |
| P3 | about 1 h | about 0.5M |
| P4 | about 3 h | about 2M |
| P5 | about 2 h, plus Nathan's installs | about 1M |

At twice any phase's estimate, W1 stops and PE37 re-prices it with Nathan.

## 13. Open questions, answered at G0 or taken as the defaults

| # | Question | Default |
|---|---|---|
| Q1 | Does an Epic specification update PF20, as TW-RECORD-10 did? `AGENTS.md` calls PF20 historical and reference-only | No. Only PF27 and PF30.1, as instructed |
| Q2 | What is "the applicable PF10 file set"? | The current `docs/pfcanon/PF10-*.md`, plus any `PF10_BUILD_NOTES_ADDENDUM` files the specification names under `docs/ephemeral/` |
| Q3 | Is §2.3 the complete list of supported types? | Yes. Anything else is `UNSUPPORTED_INPUT` until added through GTWPE-MGMT-10 |

## 14. W1 kickoff

Nathan starts W1 as a new Claude Code session on this repository, after G0 and after PR #493 merges,
and pastes:

```text
You are W1, the GTWPE worker session. PE37 (another session) facilitates you. Nathan relays your
reports to PE37 and brings back its replies.

Read first, completely: AGENTS.md;
docs/ephemeral/gtwpe.rewrite/GTWPE-IMPLEMENTATION-PLAN-v1.0.md (your governing plan, approved at G0);
TW-BASELINE-20260924.md, TW-MGMT-10-ANALYSIS-20260924.md and PE-METAPROMPT-TEST-20260924.md
in the same directory.

Execute phase P0, then stop at its checkpoint and report as the plan's §5 and §10 describe. Do not
start P1 until the relay tells you to.

Use PE Metaprompt 091426.1 (https://app.notion.com/p/3db4590a05eb8174be35d9e35acb3f77) for prompt
engineering, with these workarounds for the defects its test found:
- procedure lives in docs/prompt_ecosystem_management/, not in docs/ephemeral or Drive (D2);
- D22 applies to every prompt body: never hash, byte-compare or keep one; delete transient read
  files when the read is done, and report them (D1);
- subagents are workers inside your task only, and write nothing (D6);
- ignore its GCFPE-only text: the overlay, the PR-lane text and the Alpha baseline (D3, D4).

Nathan alone merges and installs. You create no sessions. Pull requests store records and gate
nothing (Nathan, 2026-09-28). Work on one branch,
docs/20260925-gtwpe-w1, with one PR, pushed at every checkpoint so PE37 can read it. End every
report with DECISION NEEDED, NOTHING NEEDED or IN FLIGHT.
```

**The resume kickoff** is the same text, with "Execute phase P0" replaced by "Resume from
docs/ephemeral/gtwpe.rewrite/CHECKPOINT.md".

## 15. Revisions

**v1.1, 2026-09-28**, from W1's P0 checkpoint (`CHECKPOINT.md` §6, §8) and PE37's V0 check:

| Change | Why | Ledger |
|---|---|---|
| `status` no longer reads `AWAITING_APPROVAL` | W1 acted on the plan from Nathan's kickoff of 2026-09-25 | E-001 |
| P5 orders the skill package's install before T6 | `glow-write-boundary` forbids the canon write until its exception is installed; `AGENTS.md`'s exception does not clear the skill | E-002 |
| S8: the canon PR is separate from W1's records branch, and is the only PR whose merge matters | Nathan, 2026-09-28: "We can't use PRs to manage work in this stream. There is too much parallel work. We can use them, but they cannot gate." Ruling 1 keeps canon adoption on his merge | E-003 |
| §2.3: readers are provisioned by a pinned step that P1 designs and P2 tests | Their dependencies are absent in the container | E-004 |
| §14: pull requests store and gate nothing | The same ruling | E-003 |

Nothing else changed from v1.0.
