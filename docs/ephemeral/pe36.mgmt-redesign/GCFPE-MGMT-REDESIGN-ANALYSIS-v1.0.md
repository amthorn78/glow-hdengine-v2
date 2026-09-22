---
artifact_type: GCFPE_MGMT_PROCESS_AUDIT_RCA_AND_REDESIGN_PLAN
artifact_version: "1.1"
created_date: 2026-09-22
session: PE36
status: STAGE_1_BUILT_STAGES_2_ONWARD_NOT_STARTED
authority: Product Owner request, 2026-09-22 — full review of the GCFPE MGMT change-process ecosystem
committed: true — branch docs/20260922-pe36-mgmt-redesign
pull_request: 468 — https://github.com/amthorn78/glow-hdengine-v2/pull/468
blocking_decisions: 0 — D-A, D-B and D-C answered by the Product Owner 2026-09-22 (§10)
decisions_recorded_durably: true — D20, gcfpe.decision-record.md, on this branch
revision_note: |
  v1.1, 2026-09-22 — adds the Modification Intake and Triage entrypoint (§6.0); the Modification
  naming and its measured collision (§5); the batching correction, a Modification is the unit of
  approval not of one thing (§3.2); targets and the gates they imply (§3.3); the blast-radius
  tiered gate with its Tier 0 limit (§3.4); closure computation as ANALYZE's primary mechanism,
  the readiness verdict and interaction cost (§4); and closure.py (§6.3a).
---

# GCFPE MGMT change process — audit, root-cause analysis, and redesign plan

**The short answer to "what happened":** the change-management prompt was refactored from
**52,009 characters that contained a method** down to **8,015 characters that contain a contract**,
and the method was not relocated anywhere. The only procedure left in it is a *"Batch method"* for
a batch sequence the Product Owner retired on 2026-09-18. So the live path through the prompt has
no method at all, and every change since has been improvised by whichever session was holding it.

That is measurable, not inferred, and §2 gives the measurements.

---

## 1. Current-state assessment

### 1.1 What the process is supposed to be

| layer | artifact | what it claims |
|---|---|---|
| the prompt | `GCFPE-MGMT-10 — Manage an Ecosystem Change — 091426.1` (Notion) | manage one authorized ecosystem repair case |
| the process doc | `ecosystem-change-management.md` v1.1 | five-step change lifecycle, classes A–E, seven-point definition of done |
| the execution doc | `execution-and-delegation-model.md` v3.0 | coordinator + subagents, precomputed hit lists, structured returns |
| the contract | `project-prompt-contract-registry.md` | machine-readable per-prompt contract, 5,301 lines |
| the routing | `docs/graph/parts/prompts/GCFPE-MGMT-10.json` | three reusable result states |
| the rulings | `gcfpe.decision-record.md` | D1–D19 |
| the boundaries | 5 policies + 3 installed skills | where work may be written, what a body may carry |

### 1.2 What the process actually is

**`GCFPE-MGMT-10` is not what runs when a change happens.** Every one of the last fourteen
repository changes was performed by a PE session working from a prose task brief and a succession
record. None of them invoked the prompt. The prompt's name appears in `docs/ephemeral/` only in
batch-era artifacts from 2026-09-14/15 and in incidental references.

The process that actually operates is: *a session receives a prose brief → invents a procedure →
invents an artifact format → hands to an independent reviewer → iterates until the reviewer stops
finding things.*

### 1.3 Measurements of the current state

| measure | value | how measured |
|---|---|---|
| `GCFPE-MGMT-10` body, ChatGPT era (`091226.3`) | **52,009 chars**, 6,975 words, 19 sections | archived Notion page |
| `GCFPE-MGMT-10` body, current (`091426.1`) | **8,015 bytes**, 6 sections | registry `evidence_contract` |
| retained | **~15%** of the original | ratio |
| artifacts in `docs/ephemeral/` | **255** | `find` |
| distinct `artifact_type` values | **~100** | `grep` over frontmatter |
| round-tracking page | **474,215 characters** | Notion fetch |
| repair rounds to reach a clean skill verdict | **30** | round-tracking headings |
| review rounds on a single PR (#425) | **20** | round-tracking headings |
| versions of one guard before it held | **11** (`GUARD_DEFEATED` ×9 recorded) | round-tracking headings |
| procedure documents cited by the prompt body | **0 of 5** | `grep` against the body |
| batch references in the 55 graph parts | **0** | `grep` |

---

## 2. Root causes

Ranked by how much friction each one causes. RC1–RC3 are the ones that matter; the rest compound.

### RC1 — The prompt lost its method, and the method was deleted rather than moved

The `091226.3` body carried nineteen sections including **`## Execute the change`** and
**`## Quality-control contract`**. The current body carries six sections and neither of those.

A `grep` for those sections' substance across `docs/prompt_ecosystem_management/` returns nothing.
**The method did not move into the repository. It was removed.**

What replaced it is a contract: *Native purpose · Entry contract · Batch method · Required result ·
Reusable result routing · Artifact and source boundaries*. That describes what the prompt needs and
what it returns. It does not describe how to do the work.

### RC2 — The only surviving method is for a construct that no longer exists

`## Batch method` is the sole procedure in the prompt. It is six steps, every one framed in batch
terms — *"For every batch member"*, *"the authorized batch"*, *"Record later-batch findings"*,
*"Do not run the dedicated workflow-skill review or independent post-flight before Batch 6."*

**D12 retired the batch sequence on 2026-09-18.** Batches 1 and 2 are complete; 3–6 are replaced by
one consolidated pass. No future authorization can name a batch, so no future invocation can reach
the batch path.

The non-batch path is one sentence: *"For a non-batch maintenance invocation, return the applicable
reusable graph result and the saved/read-back `GCFPE_ECOSYSTEM_CHANGE_REPORT`."* That is a result
specification. **The live path through this prompt contains no procedure whatsoever.**

Corroboration that the body is the stale surface and not the graph: the 55 graph parts contain
**zero** batch references. Under D13 the graph is authoritative for routing, and the graph never
modelled batches. The body alone carries the retired model.

### RC3 — The entry contract inverted the work, and contradicts the approved registry

| | `091226.3` | `091426.1` |
|---|---|---|
| intake | *"Minimal useful intake is the prompt name or affected ecosystem, expected result, actual/requested result, and an example if available."* | *"All six inputs below are **REQUIRED**."* |
| missing facts | *"Retrieve missing technical identifiers yourself. Ask only when a missing fact changes the repair or authority materially."* | four of the six inputs must be resolved before entry; two are the Product Owner's to produce |

**The prompt now demands as input the thing `ANALYZE` is supposed to produce as output.** Scope,
affected identities, governing sources and the complete control set must all exist before the
prompt will start — which is the analysis. That is why a change costs weeks: the analysis is done
by hand, by you, before the process is allowed to begin.

This is also a live contradiction with the approved machine-readable contract. The registry row for
`GCFPE-MGMT-10` still declares a **single** input:

```
inputs:
- Use the user's supplied error report, requested change, runtime/environment update or proposed new prompt.
```

The registry carries the old minimal intake. The body demands six. **Both are current, approved,
and they disagree.** Nothing detects this because no assertion compares them.

### RC4 — The method was rewritten elsewhere and never wired back

`ecosystem-change-management.md` §2 defines a genuine five-step lifecycle (classify, scope by
measurement, apply in one pass, verify in isolation, record). It was written 2026-09-18 under D12.
It is good, and it is the closest thing the ecosystem has to the deleted method.

**The prompt does not cite it.** Measured: the body contains zero references to
`ecosystem-change-management`, `execution-and-delegation-model`, `session-working-rules`,
`gcfpe.decision-record`, or `authoritative-surfaces`.

So the method exists, the prompt exists, and nothing connects them except a human remembering that
both exist. That is the gap the succession records have been manually bridging for six sessions.

### RC5 — There is no change-document format, so every change invents one

**255 artifacts, ~100 distinct `artifact_type` values.** A sample of what one ecosystem produced for
one campaign: `GCFPE_REPAIR_ROUND_REPORT`, `GCFPE_REPAIR_REPORT`, `GCFPE_CROSS_CUTTING_REPAIR_REPORT`,
`GCFPE_CONSOLIDATED_PASS_REPAIR_REPORT`, `GCFPE_BATCH_1_REPAIR_REPORT`, `GCFPE_BATCH_2_REPAIR_REPORT`,
`PROMPT_ECOSYSTEM_REPAIR_REPORT`, `GCFPE_SKILL_REPAIR_REPORT`, `GCFPE_GRAPH_REPAIR_REPORT`.

Nine names for "what this round repaired." Consequences that cost real time:

- **Nothing is diffable across changes.** Two rounds' reports cannot be compared mechanically.
- **Nothing is countable.** "How many changes are open" requires reading prose.
- **Nothing is resumable.** A successor cannot load state; it reads narrative and re-derives.
- **Every session spends part of its budget designing a document** instead of making the change.

Your instinct that this might need a standard change-document format is correct, and it is the
single highest-leverage supporting change. It does **not** need a separate formatting prompt — §6.

### RC6 — Review loops have no convergence criterion

PR #425 went twenty review rounds. One guard went eleven versions with nine recorded
`GUARD_DEFEATED` verdicts. The §10 skill review returned `SKILL_REPAIR_REQUIRED` at least nine
times across thirty rounds.

The structural cause: **a verdict binds to exact bytes, and any correction produces new bytes.**
So a single one-line fix costs a full repackage, a fresh independent review, an install and a digest
verification. `skill-packaging-and-delivery.md` already names the mitigation — *"batch small
corrections into one change rather than shipping them one at a time"* — but nothing enforces it,
and nothing stops a reviewer's new observation from restarting the cycle.

There is no rule anywhere that says **a review may not expand scope.** Without it, every review is
an opportunity to discover more work, and discovery during execution is unbounded by construction.

### RC7 — State lives in prose, in a 474,000-character page

The round-tracking page is the de facto state store for the whole campaign. It cannot be queried,
so every session reconstructs status by reading narrative — and it is where the stale-state defects
keep coming from. The install-verification correction earlier today is the same shape: a true
sentence became false and nothing detected it, because sentences are not fields.

### What did *not* cause this

Worth stating so the redesign does not over-correct:

- **Not the rigor.** The digest verification, the independent review and the isolated readback each
  caught real defects — including a wrong-package install that ran a full round behind green gates.
  The controls work. The problem is that they run against an undefined process.
- **Not the old prompt's size.** 52KB is not a virtue, and the campaign exists because that
  ecosystem was found defective. What mattered was that it carried an executable method and a
  minimal intake, not that it was long.
- **Not the people or the sessions.** Six PE sessions independently converged on inventing a
  procedure, because there was none to follow.

---

## 3. The proposed operating model — one prompt, three modes

One Notion-managed prompt body. One `MODE` input. Three mode blocks over a shared spine.

```
Modification Intake and Triage   prose dump → N item stubs, GROUPED into Modifications
   (standalone, outside the release — see §6.0)
        │
        ▼  one Modification, carrying one or many items
GCFPE-MGMT-10 — Manage an Ecosystem Change
├── SPINE          invariants true in every mode — stated exactly once
│                  identity · authority · write boundaries · source resolution
│                  · the Modification contract · prohibited actions · failure contract
├── MODE = ANALYZE     stub  → Modification §A         gate: PO approves the analysis
├── MODE = PLAN        Modification §A → Modification §P         gate: PO approves the plan
└── MODE = EXECUTE     Modification §P → Modification §E + change gate: PO merges / installs
```

**Why one prompt, mechanically, not just by preference.** Three prompt bodies would each need their
own registry row, graph part, evidence contract and identity, and each would drift separately — the
ecosystem has already demonstrated this exact failure with nine names for one report type (RC5) and
with two mutually incompatible validators advertising the same revision. One body means one
authority for the shared spine, and the spine is most of the risk.

**The mode is an input, not a separate artifact.** `MODE` is behaviour, so it belongs in a body
under `prompt-body-content-policy.md`. It is not governance state, it does not change on a release
event, and it carries no selection claim.

### 3.1 The rule that bounds the loops

> **A mode may not expand its own scope. Only `ANALYZE` may create scope.**
>
> This fixes *what a Modification contains*, not *how much it contains*. A Modification carries as
> many items as share a gate — see §3.2. Scope fixity is the loop bound; cardinality is not.

`PLAN` plans exactly what `ANALYZE` established and the Product Owner approved. `EXECUTE` applies
exactly what `PLAN` specified. Anything discovered later — by a session, a reviewer or a gate —
is recorded as a finding against the Modification and, if it is genuinely new scope, **becomes a
new Modification**. It never widens the one in flight.

This is what stops twenty review rounds. Today a reviewer's new observation restarts the cycle;
under this rule it opens a separate, separately-priced change, and the current one converges.

It is also the direct application of D12's finding — *splitting one shared rule across several
authorizations creates several chances to apply it several different ways* — to the time axis
rather than the batch axis.

### 3.2 A Modification is the unit of approval, not the unit of "one thing"

**Corrected 2026-09-22.** v1.0 of this plan implied one change at a time. That was wrong, and this
ecosystem's own rulings say so: `D12` requires a rule to be applied *in one authorization* across
every surface it reaches, and `skill-packaging-and-delivery.md` records that *"three separate
one-line fixes cost three independent reviews; one change carrying all three costs one."*

**Items group into a Modification when they share a rule, a verification, or a package/review/
install cycle.** Two couplings, with deliberately different failure semantics:

| `coupling` | what it is | if one item fails |
|---|---|---|
| **`ATOMIC`** | one rule applied across many surfaces; the items are one act | **The whole Modification stops.** Partial application is the documented defect — the 236→333 undercount would have left twelve prompts contradicting themselves two lines apart |
| **`INDEPENDENT`** | items that merely share a cycle | **Per-item.** The item takes `BLOCKED` with a named owner; the rest complete. `DISP-001` is satisfied because it is recorded and owned, not parked |

Rule-shaped work **must** be one `ATOMIC` Modification. Splitting it is the `D12` error.

**A Modification has one coupling.** If you need an atomic rule application *and* an unrelated
independent fix, that is two Modifications — mixing them invites the partial-application defect
this field exists to prevent.

*(Named `coupling`, not `shape: RULE`, because "a rule" is a **target** — §3.3 — and one word
doing two jobs is how `CHANGE_RECORD` happened.)*

**Several Modifications may be in flight at once** — `status` makes that queryable. The only
ordering constraint is that two Modifications touching the same surface must merge or serialise,
or they conflict.

Per-item dispositions are recorded in §E, so batching costs no granularity.

### 3.3 What a Modification targets, and why that decides the gates

**A Modification may target a prompt, a skill, a rule, or any combination.** Target kind is
independent of coupling, and it is what determines the required steps — so `PLAN` derives them
rather than a session recalling them.

| target | what executing it costs |
|---|---|
| **prompt** | authored in Notion in place; if it is a selected release member the change is Class A, and the graph part and registry row move with it — rebuilt by script, never hand-edited |
| **skill** | package → **independent §10 review** → only Nathan installs → post-install digest comparison |
| **rule** | pull request; a *new* ruling needs its D-number recorded **before** execution, not after |
| **graph** | rebuilt from parts, represented by its proof token, never committed as assembled output |
| **registry** | the assertion, plus an injected regression proving the guard fires (`GUARD-001`) |
| **Notion control page** | an established destination rule, or explicit task authorization |

**Combinations are where the cost hides.** A Modification touching a prompt *and* a skill pays
both the release-member path and the package/review/install cycle. That must be visible at
`ANALYZE`, not discovered in `EXECUTE`. PE36's Task 01 was exactly this shape: three skills, one
rule, and the decision record — one Modification, three target kinds.

### 3.4 The gate is tiered by blast radius, and the tier is measured

**This is the change that makes ordinary changes cheap.** Today every change is priced at corpus
scale — full graph rebuild, registry validator over all 55, interface closure across all 55 —
whether it is a corpus-wide rule or a typo in one method section. Nothing computes the actual
radius, so everything pays the maximum.

The radius is computable. From the 55 graph parts, in about twenty lines: upstream producers,
downstream consumers, and prompts sharing a result state. Measured on this corpus — 55 parts, 157
declared result states, every prompt carrying outbound handoffs:

```
PR-30           upstream 4   downstream 3   state-sharers 3   radius 7
QA-10           upstream 3   downstream 2   state-sharers 0   radius 4
GCFPE-MGMT-10   upstream 0   downstream 1   state-sharers 0   radius 1
```

> **Corrected 2026-09-22, by the script this section proposes.** v1.1 published
> `PR-30 upstream 5 / downstream 4`, `QA-10 downstream 4` and `GCFPE-MGMT-10 downstream 3`. Those
> came from a throwaway prototype that made two errors `closure.py` does not: it counted
> **boundaries** — `NATHAN_TERMINAL_RETURN`, `ORIGINAL_NATIVE_STAGE` — as downstream consumers,
> and it counted a prompt's **self-edges**. A terminal return to Nathan is not a consumer, and
> overstating it inflates the blast radius of every prompt in the corpus.
>
> The point is not the arithmetic. **The design was validated against its own author within
> minutes of the script existing** — which is precisely the argument for `closure.py` being a
> script rather than an instruction in a prompt body, and precisely `DERIV-001`: a fact a
> machine-readable source already carries is generated, never typed.

**The graph part is the interface contract, so "did the interface move?" is a diff on one JSON
file.**

| tier | entered when | gate |
|---|---|---|
| **0 — routing unaffected** | the rebuilt graph part is byte-identical and registry assertions pass | verify the edit landed. Radius 1 |
| **1 — bounded interface change** | the graph part changed | closure over the **computed** radius — upstream ∪ downstream ∪ state-sharers — not all 55 |
| **2 — corpus-wide rule** | one rule reaching many prompts | the full release-wide gate. `D12`'s case, and it should stay expensive |

Each tier is entered by measurement, never by a judgement of how large the change feels.

> **The limit of Tier 0, stated so it is not lost.** A byte-identical graph part proves the
> **routing** interface did not move. It does **not** prove the artifact's *content* contract did
> not — a body can change what an artifact says while keeping its state name, and the graph cannot
> see that. The registry's `evidence_contract` and assertions cover part of that gap, not all of
> it. **Tier 0 means "routing provably unaffected", not "provably harmless."** Anything that
> changes what a prompt *produces*, rather than how it *routes*, is Tier 1 regardless of what the
> graph part says.

---

## 4. The three modes — responsibilities, inputs, outputs, boundaries

### `MODE = ANALYZE`

| | |
|---|---|
| **Purpose** | Establish what the change actually is, what it reaches, and what it will cost |
| **Input** | The request, in whatever form it arrives — a defect report, a sentence, a finding ID, a policy instruction. **Minimal intake is restored:** subject, expected result, actual result, example if one exists |
| **Does** | **Computes the dependency closure from the graph parts** — upstream ∪ downstream ∪ state-sharers — and assigns the gate tier per §3.4. That is mechanical, not judgement. Then: resolves its own identifiers, searches both systems, classifies (A–E per `ecosystem-change-management.md` §2), names targets and coupling, and **measures remaining scope by broad match minus permitted exceptions, never by enumerating known phrasings** (`SCOPE-001`). Names contradictions, risks, and the defect classes it matches from §4's catalogue |
| **Outputs** | Modification §A: the **computed closure and gate tier**, targets, coupling, classification, measured scope with its method, dependency and ordering constraints, contradictions, risks, open questions for the Product Owner, the **readiness verdict** and the **interaction cost** below |
| **Must not** | Change anything. Propose a plan. Decide a policy question. Widen the request into adjacent work it happens to notice — that is recorded as a candidate for a separate Modification |
| **Exit** | Product Owner approves §A, answers any open questions, or redirects |

The Product Owner's job at this gate is to confirm the change is the one they meant, and to answer
only genuine policy questions. Everything evidence-resolvable is the prompt's.

#### Is this too much for one round? — answered by predicates, never by a score

A size score would be a fabricated number. The failure mode is not item count: forty items that
are one rule applied mechanically is easy — that is `D12`'s case — while three items where each
answer changes the next is brutal. PR #425 took **20 review rounds** not because it was large but
because every round discovered the next thing.

**Two conditions force a split, and both are derivable rather than judged:**

1. **Sequential discovery.** If item B's scope cannot be measured until item A has been executed,
   they cannot share a plan — `PLAN`'s own closure test is *"executable mechanically with no
   interpretation"*, and it fails by construction. `ANALYZE` asks per item *"can I measure this
   now?"*; an answer of "not until A lands" **is** the split point.
2. **Unmeasured scope.** An item `ANALYZE` could not measure by broad-match-minus-exceptions is
   `SCOPE-001` loaded and waiting.

**Everything else is cost, and the currency is round trips through the Product Owner** — not items.
That is what "weeks per change" actually measures.

```
interaction_cost =
    open questions needing a ruling     # each is a round trip, and can invalidate planned work
  + 2                                   # the ANALYZE and PLAN approvals, fixed
  + independent §10 review cycles        # one per skill package
  + install events
  + merge events
```

`ANALYZE` reports the number, its breakdown, and what a split would save — *"as one Modification:
8 interactions. Split as proposed: 4 and 3, and the first can proceed while the second waits on a
ruling."* **No threshold and no score.** The cost is visible; the Product Owner decides.

The section closes with one verdict, derived from the predicates above:

| verdict | means |
|---|---|
| **`READY`** | zero open rulings, every item's scope measured, no sequential discovery, one gate tier |
| **`SPLIT_RECOMMENDED`** | with the exact split points and the reason for each |
| **`NEEDS_RULING`** | N decisions would improve this; **advisory only, it never refuses** |

**Open questions are therefore the expensive thing**, which is correct and slightly
counterintuitive: three items and two rulings is a worse round than twenty items and none.

#### None of this blocks the Product Owner

**`readiness` is advisory and always has been.** It reports a conclusion; it does not refuse.
Every gate in this design exists to stop a **session** proceeding on its own judgement — none of
them exists to stop Nathan, and a process that tells him to wait for his own change has the
authority backwards.

Where a policy gate would otherwise fail, an `override` block waives it and records that the
waiver was deliberate:

```yaml
override:
  by: Nathan
  overrides: [scope_freeze]
  reason: "needed now"
```

`modification_validate.py` accepts it for `scope_freeze`, `readiness`, `modification_class`,
`gate_tier` and `deferral`, and rejects an override that is unattributed, unreasoned, or that
claims to waive a **well-formedness** check. That last line is the only limit: an override waives
a policy gate, but it cannot make a malformed record well-formed — a missing section is the
document failing to say what happened, and waiving it would only make the record lie.

The `reason` exists for a successor reading the record. **It is not a justification anyone is
owed**; "I need it" is complete.

### `MODE = PLAN`

| | |
|---|---|
| **Purpose** | Turn an approved analysis into an ordered, closed, verifiable list of changes |
| **Input** | The Modification with an approved §A. **Nothing else** — if §A is missing or unapproved, `PLAN` returns `PLAN_BLOCKED` rather than re-deriving the analysis |
| **Does** | Produces one ordered step list. Each step names its target surface, the exact edit, its authority, its verification, and its rollback. Resolves ordering from real dependencies. Identifies which steps are the Product Owner's actions (merge, install, promote) and which are the session's. States the guard that will catch reintroduction (`GUARD-001`) |
| **Outputs** | Modification §P: the ordered step list, the verification plan, the definition of done for this change, the Product Owner actions, and the explicit statement of what is **not** in scope |
| **Must not** | Apply anything. Add scope not in §A. Leave a step whose verification is "read it and check" — every step needs a check that can distinguish a correct result from an incorrect one (`CHK-001`, D11) |
| **Exit** | Product Owner approves §P |

**The closure test for a plan.** A plan is complete when it can be executed mechanically with no
interpretation. This is the ecosystem's own standard — *"if you write that a specification, redline,
or handoff is sufficient for its consumer, the test is whether that consumer could execute it
mechanically"* — and it is the gate that prevents `EXECUTE` from having to think, which is where
scope creep enters.

### `MODE = EXECUTE`

| | |
|---|---|
| **Purpose** | Apply the approved plan, verify each step, and report truthfully |
| **Input** | The Modification with an approved §P |
| **Does** | Works the step list in order. Verifies each step by the check §P named. Reads back every write before claiming it. Records the result of every step, including unchanged ones |
| **Outputs** | Modification §E: per-step and per-item disposition (`APPLIED` · `VERIFIED` · `BLOCKED` · `NOT_APPLICABLE` with reason), the evidence for each, the artifacts produced with their paths, the Product Owner actions remaining, and the **actual interaction cost against `ANALYZE`'s prediction** |
| **Must not** | Apply anything not in §P. Expand scope. Merge. Install. Promote. Decide a policy question. Silently skip a step — a skipped step is a recorded disposition, never an omission |
| **Exit** | Every step has a disposition; the Product Owner's remaining actions are named with their verification |

**Whether any of this estimating is actually any good is itself a claim**, so it is measured
rather than trusted. §E records actual interaction cost against the prediction on every
Modification. After three or four, there is calibration data in the record instead of opinion —
and if the prediction is bad, that surfaces on the pilot, which is one clause in one skill.

**If `EXECUTE` finds the plan is wrong**, it stops at that step, records `BLOCKED` with the
evidence, completes every independent step, and returns. It does not repair the plan in flight.
A wrong plan returns to `PLAN`; genuinely new scope returns to `ANALYZE` as a new Modification.

---

## 5. How state moves between modes

> **Naming, decided 2026-09-22.** The record is a **Modification**, not a "Change Record".
> Measured collision: `CRD` appears **2,694** times in `docs/`, "Change Flow" **733**, bare `CR`
> **53** — and `CHANGE_RECORD` already exists at `project-prompt-contract-registry.md:2310` as
> `GCFPE-MGMT-10`'s **own declared output artifact**. "Change Record / CR" would have collided with
> the thing it replaces, on the prompt being redesigned. `Modification` is free: zero bare
> occurrences across `docs/prompt_ecosystem_management/`, `docs/graph/` and all 55 graph parts.
> Spelled out rather than abbreviated to `MOD`, which sat one letter from `MODE`.
> Registry line 2310 is rewritten in stage 3, so the old name is retired rather than left as a
> second meaning.

**State moves in the Modification, and nowhere else.** Not in conversation, not in a succession
record, not in the round-tracking page.

```
request ──▶ ANALYZE ──▶ Modification §A ──[PO approval recorded in the Modification]──▶ PLAN
                                                                 │
                        Modification §P ◀────────────────────────────────── ┘
                          │
                          └──[PO approval recorded in the Modification]──▶ EXECUTE ──▶ Modification §E
```

Three properties make this safe:

1. **Each mode reads only the prior section and writes only its own.** `PLAN` cannot rewrite §A;
   `EXECUTE` cannot rewrite §P. A mode that believes a prior section is wrong records a finding and
   returns — it does not edit upstream. This is `AUTH-001` applied to the Modification's internal structure.
2. **The approval is a recorded field, not a remembered fact.** `analyze_approved_by` /
   `analyze_approved_date`, same for plan. A mode whose entry gate field is empty returns blocked.
   This is what makes the handoff survive a session ending mid-change, which the current process
   does not.
3. **The Modification is the resumption point.** A new session opens the Modification and knows exactly where the change
   is. No transcript, no succession record, no 474KB narrative.

**Session boundaries become irrelevant.** Today a change that spans sessions needs a succession
record written by hand. Under this model the Modification *is* the handoff, and the three modes may run in
one session or three.

---

## 6. Supporting elements — what is genuinely necessary

### 6.0 Modification Intake and Triage — **necessary, and it is the required entrypoint**

Added 2026-09-22 at the Product Owner's direction, closing a real gap in v1.0 of this plan: the
design assumed changes arrive one at a time. **They arrive as a prose dump containing several.**
Nothing downstream can split that, so nothing downstream can start.

A standalone prompt, **outside the release** — not a member of `GCFPE-20260914.1`, no graph part,
no registry row, no §10 review. That is deliberate: changing it must stay an ordinary edit rather
than a Class A change, because it will be tuned often.

| | |
|---|---|
| **Input** | whatever arrives — prose, bullets, a dump of complaints |
| **Does** | **split** into atomic candidates · **state** each as one sentence of requested outcome · **dedupe** against open Modifications, `AF-001`–`AF-005`, the reconciliation backlog and `D1`–`D19` · **dispose** each · **name the apparent surface**, one line, explicitly unmeasured · **group** the `NEW` items into proposed Modifications with a `shape`, per §3.2 |
| **Dispositions** | `NEW` · `DUPLICATE_OF <id>` · `ALREADY_RULED <D-number>` · `NOT_A_CHANGE` · `NEEDS_YOU` |
| **Outputs** | a Modification Intake Report carrying the **proposed grouping**, plus **a stub for every item** — including duplicates and already-ruled ones, so an item you raised has a visible record even when the answer is "we already decided this" |
| **Must not** | measure scope · classify A–E · plan · decide · write anything but stubs. Its grouping is a **proposal**; you approve it, and `ANALYZE` may revise it once, before approval fixes it |

**The boundary that stops it becoming a second `ANALYZE`.** Triage answers *"is this one change or
three, and is it new?"* `ANALYZE` answers *"what does this one change actually reach?"* Triage does
identification-level research only. If triage ever emits a scope measurement, that is the defect,
and it is greppable.

**Why a prompt here and a validator in §6.3 — the distinction is not arbitrary.** Splitting and
deduping a prose dump is judgement, and judgement is what a prompt is for. Formatting a finished
analysis is deterministic, and that is what a template and a validator are for. §6.4 declines the
second; this is the first.

**It needs no contract of its own**, because its only output is Modification stubs and `modification_validate.py`
already checks those. A bad triage emits stubs that fail validation or that `ANALYZE` rejects at
entry. The check is downstream and mechanical — the same principle as isolating verification from
the expected answer.

### 6.1 The Modification format — **necessary**

One document per change. Machine-readable frontmatter, human-readable body, three progressively
filled sections. Lives at `docs/ephemeral/modifications/MODIFICATION-<yyyymmdd>-<slug>.md`.

```yaml
---
artifact_type: GCFPE_MODIFICATION_RECORD
modification_id: MODIFICATION-20260922-notion-write-boundary-skills
status: INTAKE | ANALYZING | ANALYZED | PLANNING | PLANNED | EXECUTING | COMPLETE | BLOCKED | ABANDONED
coupling: ATOMIC | INDEPENDENT           # §3.2 — decides the failure semantics
targets: [prompt, skill, rule, graph, registry, notion_control]   # §3.3 — decides the gates
gate_tier: 0 | 1 | 2                     # §3.4 — computed, never judged
closure: {upstream: [], downstream: [], state_sharers: []}        # computed from docs/graph/parts
readiness: READY | SPLIT_RECOMMENDED | NEEDS_RULING    # advisory; never blocks
override:                                # the Product Owner waiving a policy gate
  by: ""
  overrides: []                          # scope_freeze readiness modification_class gate_tier deferral
  reason: ""
interaction_cost_predicted: 0
interaction_cost_actual: 0               # filled in §E; calibrates the prediction
modification_class: A | B | C | D | E    # classes A–E per ecosystem-change-management.md §2
items:                                   # one or many; frozen at ANALYZE approval
  - id: ITEM-01
    statement: "<one sentence of requested outcome>"
    disposition: ""                      # filled in §E
request: "<the request, as received, verbatim>"
requested_by: Nathan
analyze_approved_by: ""                   # empty blocks PLAN
plan_approved_by: ""                      # empty blocks EXECUTE
supersedes: ""
spawned_from: ""                          # the Modification that found this scope, if any
---
```

This one file replaces the ~100 ad-hoc artifact types for change work. `status` makes "what is open"
a query rather than a reading exercise, which directly addresses RC5 and RC7.

### 6.2 A Modification template — **necessary, trivial**

`docs/prompt_ecosystem_management/modification-template.md`. A file, not a prompt.

### 6.3 `modification_validate.py` — **necessary, and it is the cheapest control in the design**

A ~60-line script, `docs/prompt_ecosystem_management/modification_validate.py`, that checks structure and
gates: required frontmatter present, `status` in vocabulary, section present for the declared
status, entry-gate approval field non-empty before `PLAN`/`EXECUTE`, every §P step carrying a
verification, every §E step carrying a disposition. It also validates triage stubs, which is why
§6.0 needs no contract of its own.

This is what makes the mode gates **mechanical instead of advisory**, and it is the difference
between a design that holds and a design that is narrated. The ecosystem's own most expensive
lesson is that *narrating a rule is not applying it* — a rule was broken three times, twice in the
file that states it. A validator is the fix that documentation cannot be.

### 6.3a `closure.py` — **necessary, and it must be a script rather than prose**

A ~20-line script over `docs/graph/parts/prompts/*.json` returning, for any prompt: upstream
producers, downstream consumers, prompts sharing a result state, and the resulting gate tier.
Verified working against the live corpus while this plan was written.

**It is a script and not an instruction in the prompt body** because a prompt told to "compute the
closure" gives a different answer each time and a script does not. That is `DERIV-001`: where a
machine-readable source already carries a fact, the second copy is generated, never typed. It is
also what lets `ANALYZE` be fast — the expensive part of scoping becomes a query.

### 6.4 A separate *formatting* prompt — **still not necessary**

Declined, and §6.0 is not this. A prompt whose job is to make a finished analysis conform to the
template would be a fourth thing to version, review, keep consistent and drift from, and it would
add a probabilistic step (`AF-003`) where a file and a script are deterministic.

**Formatting is deterministic; triage is judgement.** The template and `modification_validate.py` do the
first. §6.0 does the second. Keeping them apart is what stops the intake layer from growing into a
second analysis engine.

### 6.5 Things deliberately not proposed

- **No new skill.** The three installed write-boundary skills already cover where work may land.
- **No workflow engine or orchestration layer.** D16 already ruled that a lane with no skill binding
  is fine; adding machinery is what produced the current sprawl.
- **No change to the graph-parts mechanism, the registry, or the freeze/digest controls.** They work.

---

## 7. What information lives where

The failure mode to avoid is the current one — the same fact in three places, drifting. One
authority per fact.

| information | lives in | never in |
|---|---|---|
| how to analyze, plan and execute a change | **the prompt body**, one copy, spine + three modes | the Modification, the succession record |
| settled rules, defect classes, definition of done | **`ecosystem-change-management.md`**, cited by the prompt | restated in the prompt body |
| Product Owner rulings | **`gcfpe.decision-record.md`**, next D-number | the prompt body, the Modification |
| what this specific change is, its scope, plan, results, approvals | **the Modification** | the prompt, the round-tracking page, conversation |
| where work may be written | **the three installed skills** | restated anywhere |
| routing and result states | **the graph parts** (D13) | hand-written in the body |
| selection and lifecycle | **the register** | any body (`prompt-body-content-policy.md`) |

**The prompt cites; it does not restate.** This is the rule that fixes RC4, and it is also the rule
that keeps the body small enough to stay maintainable. A citation that goes stale is one edit; a
restatement that goes stale is a contradiction nobody detects.

---

## 8. How this stays maintainable

1. **One body means one edit per behaviour change.** No three-way consistency problem.
2. **The spine is stated once.** Anything true in more than one mode lives in the spine; a fact
   appearing in two mode blocks is a defect, and is greppable.
3. **New defect classes go to the catalogue, not the prompt.** `ecosystem-change-management.md` §4
   already holds eleven classes; adding a twelfth costs one document edit and no prompt change.
4. **`modification_validate.py` absorbs new structural rules** without touching the prompt.
5. **Changes to the prompt itself run through the prompt**, as a Class A change with its own Modification.
   The process becomes self-hosting, which is the property it currently lacks — today, changing the
   change process requires improvising outside it.
6. **`status` makes the backlog queryable**, so a stale change is detectable by a script rather than
   by someone noticing.

---

## 9. Staged implementation plan

Each stage is independently valuable and independently reversible. **Nothing here has started.**
The §10 decisions are now answered, so stages 1–6 are unblocked in design but none is authorized
to execute; stage 0 is the only one complete.

| stage | what | output | risk |
|---|---|---|---|
| **0** | Answer the three decisions in §10 | **answered 2026-09-22; D-number not yet landed** | none |
| **1** | Modification format, template, `modification_validate.py`, `closure.py`, and the triage prompt | 5 files | **DONE** 2026-09-22 — 13/13 injected regressions caught; nothing governed touched |
| **2** | Author the new prompt body: spine + three modes | the new `GCFPE-MGMT-10` body | **highest** — it is a selected release member |
| **3** | Reconcile graph part and registry row to the new body; close the six-inputs-vs-one contradiction (RC3); remove the retired batch method (RC2) | graph parts + registry, rebuilt not hand-edited | medium — must use `glow-graph-contract` |
| **4** | **Pilot on one real, small, already-known change** end to end, all three modes | one completed Modification | low — chosen small on purpose |
| **5** | Fix what the pilot exposes; only then declare the model standing | revised body, D-number | low |
| **6** | Retrofit: open Modifications for the deferred items (`AF-001`–`AF-005`, reconciliation backlog) so the backlog becomes queryable | N Modifications at `status: ANALYZED` | low — recording only, no execution |

**Stage 4 is the one that must not be skipped.** Every failure in this ecosystem's history was a
claim made before the measurement that would have checked it, and "the new process works" is exactly
such a claim. One real change through all three modes is the cheapest possible test of it.

Suggested pilot candidate: **`AF-005`** — the one-clause hardening of `glow-workspace-currency`
deferred earlier today. It is small, fully specified, has a known scope, touches one surface, and
already has its correction text recorded. It would exercise all three modes and the full
package/review/install cycle without risking anything.

---

## 10. Risks, tradeoffs, and the decisions I need from you

### Risks I can manage

| risk | mitigation |
|---|---|
| **Bootstrap** — changing `GCFPE-MGMT-10` is itself a release-member change needing the broken process | Run stage 2 once as a PE-session change under explicit authorization, then self-host from stage 5. Accept one last improvised change to end improvisation |
| Rewriting the body voids nothing installed, but **does** change a selected release member | Treat as Class A, record the D-number before executing (`ecosystem-change-management.md` §2 Step 1) |
| The body must not acquire governance state | `prompt-body-content-policy.md`; `MODE` is behaviour and passes the test — it changes when behaviour changes, not on a release event |
| Graph and registry must move with the body | D13: rebuild parts by script via `glow-graph-contract`, never hand-edit |
| The new body could quietly reintroduce the entry-contract inversion | `modification_validate.py`'s gate checks are the guard, and stage 4 fires them |

### Tradeoffs worth naming

- **Three approval gates is more ceremony per change than none.** It is much less than what happens
  now, but it is not zero. For a genuinely trivial change the honest answer is that `ANALYZE` and
  `PLAN` collapse to a few lines each — the Modification stays, the prose shrinks. I would not add a "fast
  path" mode; a fourth mode is how this kind of design starts drifting.
- **A Modification per change means more files.** But they are one type, in one directory, with one schema,
  replacing ~100 types scattered across 255 files.

### The three decisions — ANSWERED by the Product Owner, 2026-09-22

**D-A. What is in scope for the redesign?** The thirty-round pain was mostly in the *skill repair
and §10 review* loop, not in `GCFPE-MGMT-10` itself. These are different machines.
 - *(a)* `GCFPE-MGMT-10` only — the ecosystem-change prompt.
 - *(b)* **`GCFPE-MGMT-10` plus the skill-change loop** — so packaging, reviewer prompt and install
   verification become `EXECUTE` steps inside a Modification rather than a parallel process.

**DECIDED: (b).** The skill-change loop comes inside the model. Packaging, the reviewer prompt,
the §10 verdict and install verification become named `EXECUTE` steps in a Modification rather
than a parallel improvised process. This is the branch that addresses RC6, and it makes stage 2
larger: the spine must carry the byte-binding rule — a verdict binds to exact bytes and does not
carry — and `PLAN` must treat "repackage, re-review, re-install" as one planned step with a cost,
not as an unbounded retry.

**D-B. Is the three-mode artifact a Notion prompt or an installed skill?**
 - *(a)* **A Notion prompt body** replacing the current `GCFPE-MGMT-10`.
 - *(b)* An installed skill.

**DECIDED: (a), a Notion prompt body.** Consequences that now bind stage 2: the body is authored
in Notion in place and never mirrored into the repository (`prompt-corpus-policy.md`); it is a
member of the selected release, so the rewrite is a Class A change needing its D-number recorded
before execution; the graph part and registry row move with it and are rebuilt by script, never
hand-edited (D13, `glow-graph-contract`); and `prompt-body-content-policy.md` governs what may go
in it — `MODE` qualifies as behaviour, governance state does not.

**D-C. What is `EXECUTE`'s authority boundary?** Binding rules say only you merge and only you
install. Within that:
 - *(a)* **`EXECUTE` applies changes directly** — Notion body edits, repository commits, pushes,
   opening a PR — and stops at merge/install.
 - *(b)* `EXECUTE` prepares a changeset and applies nothing.

**DECIDED: (a).** `EXECUTE` applies. The stop line is exactly merge and install, both of which
remain the Product Owner's and are recorded in Modification §E as remaining actions with their verification.
Because `EXECUTE` now writes, the spine must carry the write boundaries by citation — the four open
repository paths, `docs/pfcanon/` read-only, and the Notion default of read-only absent an explicit
task authorization or an established destination rule (`notion-write-boundary.md`). The Modification's
per-step `verification` field is what keeps a writing mode honest: every write is read back before
its step is marked `VERIFIED`.

### One thing I could not establish, and am not guessing about

I could not find a record of the **ChatGPT-era process itself** — only the prompt bodies it used.
So I can state with measurement *what the prompt lost*, but not *how you actually ran a change* in
those first few rounds that went well. If you remember the working loop — how much you specified up
front, how many passes it took, where it stopped — that would sharpen stage 2 considerably, and it
is the one input I cannot recover from the record.


---

## 11. Status of this document

**Nothing has been implemented.** This document is design only — no prompt, skill, graph part,
registry row or Notion prompt body has been changed by it.

It is committed on branch `docs/20260922-pe36-mgmt-redesign` and open as **pull request #468**.
Nathan merges; this session does not.

**The three decisions in §10 are recorded as `D20`** in
`docs/prompt_ecosystem_management/gcfpe.decision-record.md`, on this branch — scope, artifact form
and the `EXECUTE` boundary together, with the consequences that bind any session implementing
them. A successor session now has durable authority for all three.

What remains unauthorized is implementation. Stage 1 — the Modification format, its template,
`modification_validate.py`, `closure.py` and the triage prompt — is additive and touches nothing
governed, which makes it the safe first build. Stage 2, the Class A prompt rewrite, is the one that
needs its own explicit authorization.
