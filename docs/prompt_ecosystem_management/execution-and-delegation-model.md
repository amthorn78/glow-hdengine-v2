---
artifact_type: PROMPT_ECOSYSTEM_EXECUTION_AND_DELEGATION_MODEL
artifact_version: "3.0"
created_date: 2026-09-17
status: BINDING
authority: Product Owner decision, 2026-09-17
governing_plan: GCFPE Expanded Prompt Repair Plan and Six-Batch Checklist — 20260915.1, §6B
mechanism: IN_SESSION_SUBAGENTS
model: opus
pilot_phase: 2
pilot_outcome: PASSED — adopted as the standing execution model
last_revised: 2026-09-18 (v3.0 — batch sequence retired; see §0A)
baseline: main @ 3c0b1fa (PR #415)
---

# Execution and delegation model

How work is divided in this prompt ecosystem. Piloted at Phase 2, then run at scale
for the cross-cutting drainage removal across all 55 prompts. **Adopted as the
standing model.**

## 0A. The batch sequence is retired — consolidated pass and one gate

Product Owner ruling, 2026-09-18. Batches 1 and 2 are complete. **Batches 3–6 are replaced
by one consolidated pass over the 37 remaining prompts plus one release-wide gate.**

### Why

The six-batch model assumed defects are per-prompt and lane-shaped. Two completed batches
show they are per-rule and corpus-shaped:

- **Batch 1's own report**: *"Root cause found at the control, not the prompts."*
- **Batch 2**: 22 of 22 contract findings closed on the prompt side. **Zero required a prompt
  edit.** Its summary: *"blocker is control-side and tooling-side, not prompt-side."*
- The two repairs that actually changed prompt bodies — drainage removal (333 passages, 44
  prompts) and the Drive → repository storage pass (333 passages, 44 prompts) — were single
  rulings applied corpus-wide, and both were executed **outside** the batch sequence.

This document already records the reason: splitting one shared rule across several
authorizations *"creates six chances to apply it six different ways."* That argument applies
to everything that remains.

### The model

**One sweep.** The four remaining lanes run **concurrently**, not sequentially, using the
instrument that worked for Batch 2: precomputed hit lists, settled rules handed to each
worker, structured returns, every evidence quote verified verbatim centrally. Each worker
answers only — does this prompt fulfil its registry contract, do its interfaces close, does it
violate a settled ruling.

Findings return to the coordinator. **Anything cross-cutting is decided once and applied
uniformly, never per lane.**

**One gate.** A single release-wide verification replaces per-batch rechecking: graph rebuild
and closure, registry validator, interface closure across all 55, isolated readback of
everything changed.

Per-batch checking re-verifies the same concerns with different eyes four more times, which is
where inconsistent application comes from. **A single corpus-wide gate cannot produce four
different answers.**

### What the Product Owner still gates

Two decisions, both where they decide something: authorizing the consolidated pass, and
approving promotion at the gate. The batch-by-batch authorization checkpoints are removed
because they bounded the wrong thing.

## 0B. Lessons carried from Batches 1 and 2

Binding on how the consolidated pass is run.

**Discovery by pattern systematically undercounts.** Measured three times: 93 passage families
→ 142 (+53%); 39 PFCanon prompts → 42; 236 occurrence lines → 333 (+41%). Enumerating known
phrasings finds only known phrasings. **Match the broad term, then subtract the permitted
exceptions** — never assemble a list of phrasings seen so far.

**Validate behaviour, not wording.** See D11. Exact-substring assertions produced 70 failures
against correct behaviour and zero true positives; the largest had never been present in any
of the 55 bodies and never flagged the 44 prompts that genuinely named Drive as Canon
authority. A check that fails on every member of a set carries no information.

**Judge by function, never by name.** Every false positive in the 2026-09-18 session came from
this: `audit/docdeltas/PF10_*` looked like Canon and was delivery evidence; a registry
assertion demanded PF10 from a prompt-repair tool that never touches build notes; `rollback`
looked like a gap and has no consumer anywhere in 55 prompts. The ecosystem already knew this
rule for the word "drain". It generalises.

**Resolve from evidence; escalate only policy.** A decision belongs to the Product Owner when
it is policy, changes settled architecture, or is expensive to reverse. Everything else is the
coordinator's, and asking for cover on it costs two rounds. Establish what a thing does before
proposing to change it.

**"Non-blocking" is not a disposition.** Findings parked as non-blocking survived across
sessions and then took one pass to clear. Drive every finding to resolution in the session
that finds it, or name the specific Product Owner decision it needs.

**Evidence must be extracted programmatically.** Both defects found in the 2026-09-18
verification were in the evidence, not in Notion: a worker flattened curly quotes in three
captures, and the fetch corpus dropped a whole line from two prompts and altered a sentence in
a third. Byte comparison caught both; worker self-reports did not. Where fidelity matters,
slice file → Python → file and compare bytes centrally.

**Do not normalise without a consumer.** `rollback` differs between IA-10 and IA-20 and no
prompt in the release requires it. Structural symmetry is not a defect. Establish the consumer
before proposing the repair.

## 0. The coordinating session's role

The session holding this work is the **coordinator, integrator and decision owner**.
It does not personally perform every large analysis or repetitive operation.

The coordinator keeps, and never delegates:

- defining the governing rules a task runs under;
- assigning exact scopes;
- choosing the worker and the return format;
- reconciling contradictions between workers;
- integrating results into the record;
- protecting settled architecture;
- deciding when Product Owner input is genuinely necessary.

The coordinator delegates bounded work with an exact scope and a deterministic
return format: large corpus reviews, batch verification, repetitive prompt
inspection, consistency analysis, documentation reconciliation, structured diff
review, bounded semantic classification, cross-file comparison.

**A subagent must never invent policy, reinterpret a settled ruling, or introduce a
competing architecture.** Hand every agent the settled rules it must work under and
say plainly that its job is to apply them, not to revisit them. An agent that
reports a ruling looks wrong should say so and stop, not act on its own reading.

## 1. Mechanism — in-session subagents

Parallel work runs as **subagents of the coordinating session**. It does not run
as sibling remote sessions.

The reason is the return path, and it was verified rather than assumed. A sibling
cloud session receives a message but **cannot message back**, and the coordinating
session has no tool to read another session's transcript. Results would reach the
coordinator only by the Product Owner opening each transcript and pasting it —
introducing transcription error, inconsistent prose, and manual coordination, for
no gain. A subagent's final report returns directly into the coordinating
session's context.

**Model: Opus, for every parallel agent.** The agent interface exposes model
selection per agent. It exposes **no reasoning-effort parameter**, so depth
follows the coordinating session's configuration and is additionally stated as an
expectation in each agent's contract. Pinning a reasoning level independently is
a session-configuration action for the Product Owner; the coordinator cannot set
it per agent. This limitation is recorded rather than worked around.

## 2. Discovery is precomputed; agents classify

The coordinator computes the raw hit list mechanically — across all 55 prompt
bodies and all 55 graph parts — and hands each agent its slice with counts
stated. An agent's task is **classification and disposition, not search**.

This is the load-bearing decision of the standard. Coverage becomes arithmetic
rather than trust: an agent given forty-one hits must account for forty-one. A
survey-based model cannot prove coverage, because a clause an agent never saw is
invisible to the coordinator and to the Product Owner alike, and the agent will
faithfully report no finding.

Search is deterministic and belongs to the coordinator. Judgement is not, and is
what parallelism is actually for.

## 3. The reporting contract

Every agent returns structured JSON against this schema. Never prose.

### Envelope

| Field | Required | Meaning |
|---|---|---|
| `batch_id` | yes | the batch this agent owns |
| `prompt_ids_surveyed` | yes | must equal the assigned set exactly |
| `instrument_version` | yes | version of `gcfpe.storage-architecture.md` used |
| `base_commit` | yes | repository commit the agent read |
| `canon_resolved` | yes | which PF documents and addenda were resolved, by name and section |
| `coverage` | yes | one row per prompt × check class — see below |
| `findings` | yes | array; empty array if none |
| `cross_batch_observations` | yes | array; empty array if none |
| `unresolved_questions` | yes | array; empty array if none |
| `dependencies` | yes | array; empty array if none |
| `blocked` | yes | array; empty array if none |
| `recommended_actions` | yes | array; empty array if none |

**An absent array is a malformed return, not an empty one.**

### Coverage row

    { "prompt_id": "...", "check_class": "...",
      "result": "FINDING" | "CHECKED_NO_FINDING" | "NOT_CHECKED",
      "reason": "required when NOT_CHECKED" }

Silence is impossible by construction. *Checked and found nothing* and *never
looked* are different values, and only one of them is evidence.

### Finding

| Field | Meaning |
|---|---|
| `finding_id` | batch-scoped and stable, e.g. `B3-SA-07` |
| `prompt_id` | the prompt it belongs to |
| `class` | `STORAGE_ARCHITECTURE` · `SPECIFICATION_FORMAT_AUTHORITY` · `PF10_ADDENDUM_POSTURE` · `LINEAGE_PRESERVED` · `TERMINOLOGY` · `GRAPH_BODY_RECONCILIATION` · `OTHER` |
| `evidence_quote` | **verbatim** source text; a paraphrase is not evidence |
| `evidence_location` | section heading, or JSON path within the graph part |
| `interpretation` | why this is a defect — a separate field from the evidence |
| `proposed_disposition` | `REPAIR` · `NO_CHANGE` · `LINEAGE_PRESERVED` · `ESCALATE_SHARED_CONTRACT` · `BLOCKED` |
| `reaches_outside_batch` | boolean, plus the prompts or batches it touches |
| `confidence` | `HIGH` · `MEDIUM` · `LOW` |

`reaches_outside_batch` is how one shared-contract question arriving from several
agents is recognised as one question rather than counted several times.

## 4. Validation on receipt

The coordinator verifies every return **before accepting it**:

1. `prompt_ids_surveyed` equals the assigned set exactly.
2. Coverage rows equal prompts × check classes, with no `NOT_CHECKED` lacking a
   reason.
3. **Every `evidence_quote` is matched verbatim against the actual source.**

A quote that does not verify is rejected and the agent re-dispatched. Transcription
fidelity is therefore checked, not trusted — which is the property pasted prose
cannot offer at any level of formatting discipline.

## 5. Boundaries

A parallel agent **writes nothing**: no branch, no commit, no pull request, no
Notion write, no repository file. It reads, classifies, and returns.

It does not litigate a Product Owner action, and it does not decide a
shared-contract question — it records one as `ESCALATE_SHARED_CONTRACT` and moves
on.

The coordinator reconciles centrally, may re-dispatch an agent against a gap or a
contradiction without Product Owner involvement, and presents one consolidated
result. The Product Owner merges, rules on escalated shared-contract questions,
and authorizes each batch. None of that moves.

## 6. Pilot acceptance criteria — Phase 2

The standard is promoted to Phase 3 only if all of the following hold:

- all five returns are schema-valid;
- membership is exact for all five;
- no `NOT_CHECKED` row lacks a stated reason;
- every evidence quote verifies verbatim against source;
- contradictions between agents are detected, and either resolved from evidence
  or escalated;
- no agent wrote to the repository or to Notion.

A failure in any of these returns the mechanism to the Product Owner for a
decision before Phase 3 runs.

## 6A. Known unverified dependency

> Renumbered from §7 on 2026-09-18. Two sections carried the number 7; every citation of
> "§7" in this ecosystem means **verification isolation**, which keeps the number.

Subagent access to the Notion connector has **not** been confirmed. Agents
inherit the parent tool surface in principle, but the connector has cycled during
authoring and the limitation should not be discovered with five agents in flight.
A single throwaway agent against one prompt is run as a smoke test first.

If Notion proves unreachable from a subagent, the design still holds: the
coordinator fetches the prompt bodies and passes them as input, which §2 already
half-requires.


## 7. Verification must be isolated from the expected answer

Learned the hard way on 2026-09-18, and binding.

A verification pass was run by agents asked to fetch each repaired prompt back and
save it for comparison. One agent, trying to be helpful, **reconciled what it fetched
against the expected baseline** and corrected a transcription slip before writing its
file. Its output then matched the baseline — necessarily, because the baseline had
been used to produce it. A match obtained that way proves nothing.

The whole pass was discarded and redone under hard isolation:

- each agent could read **only** its own input manifest, and was explicitly forbidden
  from opening the expected-result file, the applied-edit files, or any sibling's
  output;
- extraction had to be **programmatic**, by an exact documented slice, never retyped
  or proofread;
- comparison against the expectation happened **only in the coordinator**, after the
  fact.

The rule: **a worker that produces evidence must not be able to see the answer that
evidence will be checked against.** When a subagent's output will be compared to an
expectation, isolate it from that expectation and do the comparison centrally.

## 8. What the coordinator validates on receipt

Never accept a structured return at face value. Validate, centrally, that:

- the returned set equals the assigned set exactly, with no additions or omissions;
- every claimed change actually differs from its input;
- no forbidden token, state or vocabulary survives in any returned text;
- no *new* controlled token was introduced that did not exist in the input;
- every identifier, route and rule the input carried still appears in the output.

This caught real defects on every run it was applied to, including in the
coordinator's own authored work.
