---
artifact_type: GCFPE_DECISION_BRIEF
artifact_version: "1.0"
created_date: 2026-09-20
release: GCFPE-20260914.1 / 091426.1 / 55
author: PE34
status: AWAITING_PRODUCT_OWNER_DECISION
answers_to: 'Product Owner answers of 2026-09-20 on the §10 run-10 findings'
covers: [SF10-04 usefulness investigation, SF10-07 decision brief, SF-05 explanation]
snapshot: 'installed tree 321 files, digest excluding manifest.json c321be051b90c346a24d26524e132e7b90732953c3cc289e3def511e5fcfbaeb'
changes_nothing: 'This artifact is analysis only. No skill, contract, registry or prompt body is changed by it.'
---

# GCFPE decision briefs — `SF10-04`, `SF10-07`, `SF-05`

Three of your six answers asked for analysis before a decision. This is that analysis, in the
order you asked. Every number in it was measured against the frozen installed tree and the
55-body corpus; nothing is carried forward from an earlier round unverified.

Your governing objective is the standard applied throughout: **the prompt flow works as
deterministically as possible and stays maintainable when later defects appear.** Where a change
would only satisfy a validator, that is said plainly and the change is not recommended.

---

# 1. `flowmaster-propagate` — what it is for, and whether it still matters

You asked four concrete questions before considering any change. Answers first, evidence under
each.

## 1.1 What depends on it

**One maintenance activity, and no workflow.** Four installed skills embed a marked copy of
`flowmaster-primary`'s core block, and propagation is the named mechanism for keeping those four
copies identical to the source:

| skill | embeds the core | core revision |
|---|---|---|
| `tw-flowmaster` | yes | 1.0.3 |
| `change-flow` | yes | 1.0.3 |
| `session-relay-flowmaster` | yes | 1.0.3 |
| `session-branch-flowmaster` | yes | 1.0.3 |
| `flowmaster-primary` (source) | — | 1.0.3 |

`change-flow` being on that list is the only reason this touches GCFPE at all: the GCFPE
orchestrator carries an embedded copy of the Flowmaster core.

**No prompt depends on it.** Zero of the 55 prompt bodies name `flowmaster-propagate`. It is not
in any prompt's execution path, any handoff, or any result contract.

## 1.2 Whether anything currently invokes it

**Nothing invokes it.** It is user-invoked only, by its own terms — "Act only when the user asks
to propagate, synchronize, or apply an approved Primary update."

It is, however, **named as the repair route in six places**, which is what makes retirement a
change rather than a deletion:

| location | what it says |
|---|---|
| `tw-flowmaster/SKILL.md:496` | "After a Primary core update, use `flowmaster-propagate` and then `flowmaster-validate`." |
| `change-flow/SKILL.md:568` | same instruction, for `CHANGE_FLOW_SPECIALIZATION_REVISION` |
| `session-relay-flowmaster/SKILL.md:723` | same instruction |
| `session-branch-flowmaster/SKILL.md:468` | same instruction |
| `flowmaster-primary/SKILL.md:254` | step 6 of the core-revision procedure |
| `flowmaster-validate/SKILL.md:136` | "A drifted core fails and identifies flowmaster-propagate as the repair route" |

`amthor-workspace-governance-audit/references/interoperability-contracts.md:11` also records that
the audit "may recommend propagation but never performs it."

## 1.3 What would stop working if it were retired

**Nothing at runtime, and nothing in the prompt flow.** The single concrete consequence is that
`flowmaster-validate` would still detect core drift and would then point at a skill that no longer
exists. That is a broken pointer in six places, not a lost capability.

## 1.4 Whether there is any realistic current use

**No — for two independent reasons, and the second is the decisive one.**

**First, there is nothing to propagate.** All five core blocks are byte-identical right now:

| | |
|---|---|
| core block sha256 | `4d8bb9bf1c9c85ae…` |
| characters | 18233 |
| revision | 1.0.3 |
| distinct blocks across all five skills | **1 — zero drift** |

And no Primary-core change exists: `flowmaster-primary/SKILL.md` hashes to
`0665507735b10b94a4f2bb76d65947db1ee6368f12a32a03ac5a509f1e609345`, exactly the value pinned in
three bundled contracts and the validation profile, and asserted by the validator at line 2229.

**Second, its method cannot work in this environment, by construction.** You are right that it
was designed for an environment that manages its own skills. Specifically, it propagates by
**editing tracked files in a writable git checkout of the skills root**, and it verifies before
every write that the target `SKILL.md` "is a regular Git-tracked file and that its complete skill
directory is clean", rejecting "a dirty, hidden, untracked, ignored-only, symlink, or non-git
target".

Here the skills root is a one-way synced directory that is not a git checkout, and only you
install into it. So even with drift present and a Primary change approved, **the tool's own safety
preconditions can never be satisfied in this environment.** Its failure at
`propagate_core.py:151` is not a bug to repoint — it is the design meeting a different delivery
model.

## 1.5 Recommendation

**Retire it.** The invariant it maintains is real, but the route that maintains it here is already
proven and is not this tool.

When the v11 guard changed a file that lives inside two skills, the mechanism was: rebuild the
`.skill` packages, you install them, and the install is verified by full recursive diff against
the reviewed package. That is propagation by **rebuild-and-reinstall**, it already covers the
core-block case, and it is the only route that works when only you can install.

Two things follow, stated so they are not surprises:

1. **Retirement leaves six stale pointers.** Those six lines should name rebuild-and-reinstall
   instead. That is six one-line edits across five skills — itself a skill change needing
   independent review. It is cheap but it is not free, and it can ride whenever those skills are
   next opened rather than being done on its own.
2. **`flowmaster-validate`'s drift detection should stay.** Detecting that a specialization's
   embedded core has diverged is genuinely useful and is unaffected by how the repair is
   performed. Only the named repair route changes.

**Not recommended: repointing it.** Even with a corrected root, its git-tracked-and-clean
precondition is structurally unsatisfiable in a one-way synced tree. Repointing would produce a
tool that still cannot run, and a second round of the same finding.

---

# 2. `SF10-07` — the four CF Specification prompts

You asked for a plain-language brief on the actual prompt-flow impact, for each of the four
prompts, before choosing. The short version is that **the four are not one case**, and the two
obligations are not one obligation. Treating them as one block is what makes the question look
like a contract-versus-validator dispute.

## 2.0 The two obligations, in plain terms

`plan_writer_contract` puts seven flags on all fourteen listed prompts. Two of them are in
question here.

**`AUTHORING_CONTEXT`** is a field written onto an artifact with exactly one of two values:
`INITIAL_OR_PREAPPROVAL_AUTHORING` or `APPROVED_BASE_WITH_OVERLAYS`. Its job is to tell whoever
picks the artifact up next **whether what they are holding may still be rewritten**. Under the
immutable-base contract, a pre-approval artifact is freely revisable by its author through the
redline loop; an approved base is immutable and may only be extended by an explicitly scoped
overlay. The field is how a reader knows which regime applies without inferring it from which
prompt happened to produce the artifact.

**"Current-PF10 resolution"** means: before authoring, resolve and completely read the unique
current controlled PF10 Markdown in `docs/pfcanon/` plus every applicable active addendum, and
record their exact repository paths. PF10 is HDE Build Notes — the canon that constrains **how
work is built**.

## 2.1 The field is live, not bookkeeping

This matters more than the roster question, so it is measured first. **17 of the 55 bodies write
or read `AUTHORING_CONTEXT`**, and they are not all on the roster:

| | count | prompts |
|---|---|---|
| on the roster and using the field | 9 | ESC-30, IA-10, IA-20, PR-10, PR-20, QA-20, QA-50, QA-60, QA-80 |
| **using the field, not on the roster** | **8** | CL-E-20, CL-E-40, DOC-10, OPS-10, QA-70, QA-90, RS-10, RS-30 |
| on the roster, not using the field | 5 | CF-C-20, CF-C-40, CF-E-20, CF-E-40, **IA-40** |

And downstream prompts genuinely **branch** on it, rather than merely recording it:

- `QA-70`: "In initial mode use `AUTHORING_CONTEXT: INITIAL_OR_PREAPPROVAL_AUTHORING`; in delta
  mode use `AUTHORING_CONTEXT: APPROVED_BASE_WITH_OVERLAYS`, preserve the approved QA Plan
  byte-for-substance, and review only the proposed overlay."
- `CL-E-20`: "Its `AUTHORING_CONTEXT` is `APPROVED_BASE_WITH_OVERLAYS`; it may create a new
  read-only revalidation artifact but may not rewrite any approved base."
- `OPS-10`: "Set `AUTHORING_CONTEXT` to exactly one of … from the actual supplied authority."

So the field decides, for a real reader, whether rewriting is permitted. **Absence of the field on
an artifact that could be in either state is a determinism gap, not a missing token.**

## 2.2 `IA-40` is the control case, and it passes

`IA-40` is on the roster and does **not** contain the string `AUTHORING_CONTEXT` — yet the check
does not fail it. Line 22 of its body:

> Resolve and completely read current controlled PF10 and every applicable active addendum before
> authoring. Record exact repository paths/scopes and preserve `INITIAL_OR_PREAPPROVAL_AUTHORING`
> or `APPROVED_BASE_WITH_OVERLAYS` as appropriate.

That satisfies all three of the check's tests. **This is the important finding for your decision:
the check is not asking for a field name for uniformity.** It is asking for two substantive
statements — that the prompt resolves current PF10 and active addenda before authoring, and that
it distinguishes the two authoring contexts. `IA-40` makes both statements in its own words and
passes. So the four CF failures are not a formatting complaint.

## 2.3 The four prompts, one at a time

### CF-C-40 and CF-E-40 — the strong case

**What they do now.** Each makes one bounded revision in the same Specification review lineage, in
**two distinct modes**: correct a *pending* Specification from Thoth redlines (pre-approval), or
author a pending `SPECIFICATION_DELTA` against an **approved, immutable** base. Their own bodies
say so at line 8.

**What fails today.** `CURRENT_PF10_MARKDOWN` and `ACTIVE_ADDENDA`. They pass the authoring-context
test only through the check's *semantic* fallback — they describe both modes in prose without ever
naming the two values.

**What breaks without the obligations — corrected, and it is less than this brief first claimed.**
An earlier revision of this section said a downstream reader must infer "is the base in front of me
immutable?" from lineage and prose. **That is wrong, and the repository says so.** The checked-in
contract ledger `docs/ephemeral/GCFPE-Batch-1-Contract-Ledger-v1.0-20260915.md` states for both
prompts, at lines 1382 and 2110: *"Both SPECIFICATION_PENDING; artifact_type distinguishes modes."*

So the discriminator already exists on the artifact. A whole `CRD_SPECIFICATION` or
`EPIC_SPECIFICATION` means the preapproval regime; `artifact_type: SPECIFICATION_DELTA` — which
CF-C-40's own body requires it to emit in approved-base mode — means the approved base is immutable
and only the overlay is in play. A reader does not have to infer the regime, and the ledger's own
consistency item B1-C40-C3 is about exactly that distinction being carried in the review package.

What `AUTHORING_CONTEXT` would add for these two prompts is therefore **a second encoding of
information the artifact already carries**, not a missing discriminator. The residual case —
distinguishing a *revised* pending Specification from an *initial* one, which `artifact_type` does
not separate — has no consumer that needs it: CF-C-30 reviews a pending Specification either way,
and its intake is the pending artifact plus the redline lineage.

**If the bodies acquire the obligations.** Operationally: CF-C-40/CF-E-40 would stamp the value
matching the mode they already determine at entry, so nothing new is demanded of the human. The
gain is uniformity with the nine roster prompts that carry the field; the cost is a second field
that can disagree with `artifact_type` and then has to be reconciled by whoever finds the
disagreement. The PF10 flag is a separate matter, treated in §2.4.

**If the contract drops them.** Nothing breaks immediately; the ambiguity above stays, and the
next person to touch an approved Specification delta is the one who pays for it.

### CF-C-20 and CF-E-20 — the weak case

**What they do now.** Each authors **one** pending Specification from a complete class-specific
kickoff, and nothing else. Their own bodies: "This prompt never receives or rewrites an approved
base."

**What fails today.** All three markers, including authoring context — because there is nothing to
distinguish. They have exactly one mode.

**What breaks without the obligations.** Nothing in flow. Their artifacts are always pre-approval,
and the next actor (CF-C-30/CF-E-30) knows that from the artifact's `state:
SPECIFICATION_PENDING`, which the body already requires.

**If the bodies acquire the obligations.** The field becomes a constant. The only gain is that a
reader does not have to know which prompt produced the artifact to know its regime — real, but
small.

**If the contract drops them.** Nothing breaks. The roster shrinks to the prompts whose artifacts
can actually take both values.

## 2.4 Why CF-C-20 and CF-E-20 say PF10 is not a universal prerequisite

Their sentence is, on the evidence, **correct and worth keeping**.

A Specification states **what the change is**. PF10 — HDE Build Notes — constrains **how work is
built**: plans, QA, ops, implementation. That is why the ten roster prompts that carry the PF10
obligation are Plan-family and QA-family writers (IA-10, IA-20, IA-40, PR-10, PR-20, QA-20, QA-50,
QA-60, QA-80, ESC-30) and the four that do not are the Specification authors.

CF-C-20's body does not skip canon — it resolves the canon it actually needs, and says so:
"Resolve the CRD Specification format from the canon referenced for this change, through this
prompt's PFCanon source contract below, and cite the exact canon and section resolved." It even
fails closed: "If that canon cannot be resolved and read, return `SOURCE_RESOLUTION_ERROR`."

So the sentence is not an opt-out from canon. It refuses **one specific universal prerequisite**
that the artifact does not depend on. Two practical consequences of removing that refusal: every
Specification would wait on a PF10 read it does not use, and an author would be invited to shape
the Specification to build notes before the change has been specified at all. Both make the flow
slower and less deterministic, not more.

And CF-C-40/CF-E-40 already express the right version of this, conditionally: "retain current
PF10/overlay evidence only when the branch relies on it."

## 2.5 Recommendation

**Split the two flags rather than choosing one of the two options.** Neither "all four bodies
acquire both obligations" nor "drop all four from the roster" matches what the flow needs.

**Revised after the `artifact_type` correction in §2.3.** The earlier version of this
recommendation asked CF-C-40 and CF-E-40 to acquire `AUTHORING_CONTEXT` on the strength of an
ambiguity that the contract ledger shows does not exist. With that removed, the four prompts land
in the same place:

| prompt | `AUTHORING_CONTEXT` | current-PF10 resolution |
|---|---|---|
| **CF-C-40, CF-E-40** | **drop the flag** — `artifact_type` already distinguishes the two regimes on the artifact itself, per the contract ledger | **drop the flag** — keep their existing conditional wording, which is already the correct rule |
| **CF-C-20, CF-E-20** | **drop the flag** — one mode only, and `state: SPECIFICATION_PENDING` already carries the regime | **drop the flag** — their governing canon is the Specification format canon, which they already resolve and cite |

**That is your second original option — the contract drops the four Specification authors from
both flags** — and it is now the recommendation. It is not "drop them from the roster" wholesale:
the other twelve `plan_writer_contract` entries keep both obligations, and the field itself stays
mandatory on the nine roster prompts and eight non-roster prompts that genuinely consume it
(QA-70 branches on its value; CL-E-20 and OPS-10 read it).

Why this rather than adding the field:

- The information is already on the artifact. A second encoding that can disagree with the first
  is a maintenance liability, not a determinism gain — and reconciling a disagreement between
  `artifact_type` and `AUTHORING_CONTEXT` would fall to whoever next touches an approved
  Specification delta.
- It removes a blanket PF10 obligation from artifacts that do not depend on PF10, which is the
  judgement CF-C-20 and CF-E-20 already state in their own words.
- It keeps the validator honest: after the change every prompt the check tests actually owes what
  it tests for, so no permanently-red row is left behind.

**Cost: no prompt body changes at all, and one contract change.** `plan_writer_contract` drops the
four Specification authors from `evaluated_prompt_ids`, or scopes its two flags so they do not
apply to them. The contract is bundled in both `change-flow` and `flowmaster-validate`, so this is
a skill change needing independent review, and the validator's `EXPECTED_WRITERS` literal must move
in lockstep — which the existing `PLAN_WRITER_SET` check already enforces in both directions, so a
half-done change fails loudly rather than quietly.

**The option not to take:** requiring all four bodies to acquire both obligations. It would add a
PF10 prerequisite to artifacts that do not use PF10 and a second regime field beside one that
already works, and it would need four Notion body edits to buy that.

---

# 3. `SF-05` — D14's behavioural half, in plain language

You asked to understand the issue before directing a mechanism. The single most useful fact is in
§3.6: **the prohibited behaviour is not present in the current system — established by reading all
72 terminal branches, not by a keyword filter — and `SF-05` is a gap in what the available
mechanisms can express, not an open defect in the flow.**

## 3.1 The behaviour D14 is meant to guarantee

D14 says a settled ruling is enforced **against behaviour**, not against vocabulary, and that no
ruling counts as applied until a guard exists that would catch its reintroduction and has been
fired by an injected regression.

The specific behaviour here belongs to **D8**. D8's intent, in its own words: "a qualifying
producer creates the addendum; on the next turn PF10 is current; nothing ever blocks later work on
an addendum transition state." A later prompt "resolves and reads current PF10 as part of its
normal job and acts on what it finds. If that read happens to show the expected reference, nothing
further is required or recorded."

So the guarantee, agent-facing, is: **no prompt may make an agent compare current PF10 against
what an addendum says it should be, and stop because they differ.** Reading PF10 is normal work.
Recording what was read is provenance. Stopping on a comparison is the prohibited machinery.

Why it matters to a person running the flow: such a gate stops legitimate work at a step that
produces nothing, and it asks an agent to litigate a Product Owner action — which the same canon
section forbids.

D14 was ruled on a real instance, not a hypothetical: `RS-40` "compared current PF10 against an
addendum's normalized delta and **stopped terminally on a mismatch** — the retired drainage
lifecycle reinstated by function, in a body containing none of the thirteen retired tokens."

## 3.2 What `CTR-002` checks today, and why those literals were chosen

`CTR-002` is one composite rule applied to all 55 registry rows. Per row it asserts:

| part | assertion |
|---|---|
| required literal | `PF10` |
| required regex | `docs/pfcanon/` |
| forbidden regex | `state the mismatch` |
| forbidden regex | `[Cc]ompare the current PF10` |

The positive half is sound and is not in question: every body must reference PF10 and must resolve
it from the controlled `docs/pfcanon/` source.

The two forbidden phrases are the negative half — the D8 prohibition. They were chosen the
obvious way: they are the words the **actual** violating bodies used when the defect was found.
That is a reasonable first move; it is also, exactly, a vocabulary selector.

## 3.3 Why a violating wording can contain neither literal

Because the prohibited thing is a **three-part behaviour**, and each part has unlimited phrasings:

1. read current PF10, **and**
2. compare it against an addendum-derived expectation, **and**
3. stop, block, or return terminally because they differ.

A body can do all three while using neither phrase — for example by instructing an agent to
"resolve the current Build Notes and, where the recorded reference does not match the addendum's
normalized delta, return `DIVERGENCE_BLOCKED` to its owner." No "state the mismatch"; no "compare
the current PF10"; the prohibited gate, complete.

This is the same failure the contract guard suffered nine times, and the decision record is blunt
about it: "the check selects, and the prohibited gate is written where nothing selects. v1 and v2
selected on phrasing and died to paraphrase and synonym." **A wider word list buys one round.**
That is why your instruction not to widen it is the right one.

## 3.4 Why the structural fix cannot be reused here

v11 works on the contract because the contract is a **machine-readable structure with a finite
grammar**. v11 stopped enumerating what to inspect and enumerated what may exist: the routing
surfaces are pinned whole, and "every branch-shaped object naming PF10 anywhere else in the
contract is an error, with no allow-list."

That sentence has no meaning over prose. A prompt body is natural language: there are no objects,
no keys, no branch shapes — nothing to enumerate, and no way to say "everything except this is
forbidden." The registry's mechanism is regex over body text, so the only expressible rules are
"this string must appear" and "this string must not appear." **The structural fix is not
expressible there because the medium has no structure to pin.**

## 3.5 Mechanism options

Four options, with what each costs and how each is maintained. Measurements are from the current
corpus.

### Option A — move the rule onto the graph, but it needs a typed field first (recommended, with a cost)

The prohibited behaviour must end in a **stop**, and stops are structural: declared rows in
`state_routes` carrying `terminal_for_invocation`, `next_prompt_handoff_count` and `destinations`.
So the rule can be stated where the stop lives:

> No branch whose condition depends on comparing current PF10 against an addendum-derived
> expectation may be terminal or emit a blocking result.

**Correction to an earlier version of this section, which called this "vocabulary-free". It is
not, as written.** `terminal_for_invocation` is typed, but the property that *selects* which
branches the rule is about — whether a branch's condition compares PF10 against an
addendum-derived expectation — lives in `condition`, which is free text. Selecting on it is a
prose match, so a paraphrased comparison escapes selection before the terminal check ever runs.
That is `SF-05`'s own failure reproduced inside the proposed remedy, and it would have shipped as a
recommendation if it had not been caught in review.

**What makes A a guard rather than a measurement: a typed per-branch declaration.** Add one
enumerated field to each `state_routes` row — for example `pf10_dependency` valued `NONE`,
`READ_ONLY`, `SOURCE_AVAILABILITY` or `COMPARISON` — and then the pin needs no prose at all:

- no row may carry `pf10_dependency: COMPARISON`, at any depth, with no allow-list — this is D8's
  prohibition expressed over an enum;
- a row may be terminal with `SOURCE_AVAILABILITY` (RS-40's case) and not with `READ_ONLY`.

That is v11's own lesson applied to the body axis: stop enumerating what to inspect, enumerate what
may exist.

**What it costs, stated rather than glossed:** the field must be added to 280 rows across the
bundled contract copies, the validator must assert the enum and the pin, and the authoring rule
must require whoever writes a branch to declare its dependency. That is a schema change, not a
free adoption.

**What it does and does not buy.** A false declaration — writing `NONE` on a branch that does
compare — still evades it. But that is a different failure class from paraphrase: it requires an
author to state something untrue in a typed field, which is auditable and attributable, where a
paraphrase is neither. Moving the failure mode from "phrasing walks through the check" to "someone
must misdeclare" is the actual gain, and it is worth claiming only in those terms.

**Known hole, stated plainly.** A body could instruct a stop that the graph does not declare. The
validator pins the contract's `state_routes` against the contract's own
`member_registry.result_states` (`covered_states == set(registered_states)`), but **nothing checks
a body's announced result states against either.** Option A′ narrows that gap and, as measured
below, does not close it.

### Option A′ — require each body to carry its own declared result states (narrows the gap; does not close it)

Each member declares its `result_states` in the contract. Require that a body contain every state
it is declared to be able to return.

**Correction to an earlier version of this section, which claimed this makes "a body that announces
an undeclared stop fail". It does not.** The check proves only `declared_states ⊆ body_tokens`. A
body can keep every declared token, add an undeclared `DIVERGENCE_BLOCKED`, and pass — which is
precisely the regression this brief uses as its own worked example of the prohibited gate.

**The converse direction was measured and is not cheaply expressible.** The contract declares 75
distinct state tokens; the 55 bodies contain **239** `ALL_CAPS_UNDERSCORE` tokens, of which **180
are not declared states** — they are artifact types (`CHANGE_CLOSURE_DECISION`), authoring contexts
(`APPROVED_BASE_WITH_OVERLAYS`), field names (`AUTHORING_CONTEXT`, `CHANGE_ID`), ids
(`CHANGE_AUDIT_TRIAGE_ID`) and review modes. A naive "reject undeclared states" check would raise
180 candidates on a clean corpus. Distinguishing an *announced result state* from an artifact type
requires reading the token's position in prose, which is the same wall Option A hits — and a
terminal instruction expressed with no state token at all is invisible to token scanning entirely.

So A′ is worth adopting for what it is — every prompt must at least name each state it can return,
which the graph already knows — and must not be described as closing the body-to-graph hole.

Measured: **157 declared result-state token slots across the 55 members; 52 of 55 bodies contain
all of theirs.** Three bodies miss exactly one each:

| prompt | missing token | what the body says instead |
|---|---|---|
| PR-10 | `DRAFT` | lowercase prose — "preserve the instruction draft", "as a draft" |
| CL-20 | `POST_CLOSURE_PENDING` | uses the artifact name `POST_CLOSURE_RECORD`; the state token is absent |
| OPS-20 | `NOT_EXECUTED` | no occurrence in any case form |

**Adoption cost is therefore three single-token body edits** — or two, if the comparison is
case-insensitive, which would absorb PR-10's prose variant. That is a small, bounded, statable
price, and unlike a word list it does not decay: the tokens come from the contract, so the check
tracks the graph automatically when the graph changes.

### Option B — a positive provenance requirement

D8 already says a record showing what it read records "the PF10 version actually read **as
provenance — evidence, never a gate**", and D14's applied form added that requirement "where a
prompt takes a fresh current-PF10 read". A positive requirement is harder to evade than a
prohibition, because the author must **add** text rather than avoid text.

Measured: **54 of 55 bodies mention PF10; 39 of those contain "provenance"; 15 do not** — CF-C-10,
CF-C-20, CF-C-30, CF-C-40, CF-E-10, CF-E-20, CF-E-30, CF-E-40, CF-PO-10, IA-10, IA-20, IA-40,
IA-50, IA-60, MGR-10.

So as a blanket rule it costs **15 body edits**, and the narrower version — "where a prompt takes a
fresh read" — needs a definition of "takes a fresh read" that is itself a phrase judgement. Useful
as a supplement; not a mechanism on its own.

### Option C — leave it with human review, as now

Honest about what it is: the vocabulary axis has been enforced by human review since round 19, and
that review has worked. It does not scale, it is not repeatable, and it cannot be fired by an
injected regression, so under D14 it does not count as a guard.

### Option D — widen the word list

Rejected, per your instruction and the record. It failed v1–v2 and again v3–v6, and the decision
record's judgement on making the same mistake a ninth time was that it "would have been worse than
the hole."

## 3.6 Does `SF-05` have to block §11?

**No — and this is the part that should carry your decision.**

Two separate questions were being answered as one:

| question | answer |
|---|---|
| Does any current prompt implement the prohibited PF10-comparison gate? | **No**, on a complete enumeration — see below. |
| Can the registry, or the graph as currently typed, express the rule that would catch one if it appeared? | **No.** The registry's mechanism is regex over prose; the graph's `condition` is also prose. A typed field would be needed, per Option A. |

**How the first answer was established, after the first attempt was wrong.** An earlier version of
this brief selected branches by regex over `condition` — "names PF10, Build Notes or an addendum" —
and reported 37 hits. That is a vocabulary selector, so a paraphrased comparison could have escaped
the selection and the clean result would have been an artefact of the filter.

The defect can only live in a branch that **stops**, and there are exactly **72 terminal branches**
in the graph. All 72 were printed and read in full, with no selection of any kind.

Most conditions are **disjunctive** — they list several alternative stop reasons in one branch — so
they do not partition into disjoint buckets, and any single tally of them would be invented
precision. What can be counted exactly are the distinctive ones:

| stop reason | count | branches |
|---|---|---|
| a source-backed finding assessed as **unsupported** | 3 | CF-C-30, CF-E-30, IA-30 |
| the matter belongs to **another native lane** | 3 | IA-30, IA-40, QA-80 |
| a **promotion checkpoint** is outstanding | 1 | GCFPE-MGMT-10 |
| **PF10 itself cannot be resolved** | 1 | RS-40 `source_resolution_error` |
| a terminal record after a Nathan-only abort | 1 | PR-50 |
| a completed cycle or terminal return | 3 | CL-40, MGR-10, GCFPE-MGMT-10 |

The remaining 60 stop on some combination of an unresolvable source, authority, owner, identity or
access fact and a required Product Owner decision — most naming more than one as alternatives,
which is why they are not split further here.

**None of the 72 stops because a comparison between current PF10 and an addendum-derived
expectation found a difference.** The closest is RS-40's `source_resolution_error` — "unique current
controlled PF10 Markdown unresolved; make no inference from the failure" — which stops because the
canonical source cannot be read, not because a comparison differed, and which explicitly forbids
inferring anything from the failure. D8 strikes a mandatory *comparison* gate; it does not require
an agent to proceed without its canon. All 72 also carry `next_prompt_handoff_count: 0`, so D15's
invariant holds across the set.

**What this establishes and what it does not.** It establishes that the prohibited behaviour is
absent from the declared graph, by enumeration rather than by filter. It does not establish that no
body instructs a stop the graph never declared — that is the hole Option A′ narrows without closing.

`SF-05` is the second, not the first. It is a **mechanism gap**: the flow is currently clean and
there is no guard that would keep it clean automatically. Under D14 that is a real deficiency —
"no ruling is considered applied until a guard exists that would catch its reintroduction" — but it
is not an open defect in the prompt flow, and it does not make §11's output wrong.

## 3.7 Recommendation

**Revised after review.** The earlier version of this recommendation said A "costs nothing to
adopt" and that A + A′ would make `SF-05` a fireable guard. Both were overstated, and the honest
version is narrower:

- **A, with the typed `pf10_dependency` field, is the only option on the table that can become a
  guard D14 would accept.** Without the field it is a measurement, not a guard. Cost: an enumerated
  field on 280 rows in the bundled contract copies, validator support for the enum and the pin, and
  an authoring rule. It shifts the failure mode from paraphrase to misdeclaration, which is the real
  gain and the only one worth claiming.
- **A′ is worth adopting for what it is** — every prompt names each state it can return, for three
  single-token edits, self-maintaining because the tokens come from the contract — **and it does not
  close the body-to-graph hole.** Its converse is not cheaply expressible: 180 of the 239 ALL-CAPS
  tokens in the corpus are not states.
- **B** remains a later supplement at 15 body edits; decide separately.
- **Do not widen the word list.** That is unchanged and it is the one thing every option here
  agrees on.

**So the honest answer to "what concrete mechanism options exist" is: one, at a stated cost.** The
others narrow the gap. If the typed field is too much for now, the defensible interim position is
A′ plus the enumeration in §3.6 repeated each round — which is a recurring manual check, not a
guard, and should be called that.

`SF-05` is not parked, and nothing here changes the registry or widens a word list.

**On §11:** the finding does not need to hold post-flight, because the behaviour is absent today
and measurably so. If you want the guard in place first, A costs no body changes and can be built
and reviewed on its own.

**What I have not done:** no registry change, no word-list change, no body edit, and `SF-05` is not
parked. A and A′ are proposals with measured adoption costs, awaiting your decision.

---

# 4. What this artifact changes

Nothing. It is analysis. The three items you approved — the `SF10-03` validator fix, the
`SF10-05` disclaimer, and the `SF10-06` check change — are prepared separately as working copies
with bench evidence, for independent review before adoption, and are not installed.
