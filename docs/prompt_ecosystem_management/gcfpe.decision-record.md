---
artifact_type: PROMPT_ECOSYSTEM_DECISION_RECORD
artifact_version: "1.0"
created_date: 2026-09-17
status: BINDING
authority: Product Owner rulings, 2026-09-17
applies_to: GCFPE-20260914.1 / 091426.1 / 55 and the prompt-management ecosystem generally
---

# Prompt ecosystem decision record

Product Owner rulings that govern the prompt ecosystem, with the consequences that
follow from each. Recorded here rather than in a pull request discussion because
these decisions outlive the change that produced them.

## D1 — No Drive URL in the PF10 addendum contract

PF10 is referenced by **canonical name and its canonical location in `docs/pfcanon`**.
No separately carried direct URL to PF10 or to any addendum. PF10 is the canonical
location; that is where agents go to find it.

Applied as one canonical decision everywhere it appears, not reinterpreted per prompt.

## D2 — No drain owner

`drain_owner` is not specified anywhere: not as a contract value, not as an artifact
field, not as something a later prompt tracks or reports. The contradiction between
`drain_owner` as a required value and `drain_owner` in `forbidden_fields` is resolved
by **deleting the requirement**, not by reconciling the two.

## D3 — The detailed per-PR Implementation Plan is left alone

Evidence: PF10 2.14 binds "Epic or CRD Implementation Plan"; PF04 §9.1.1 names the
concrete types as `EPIC_IMPLEMENTATION_PLAN` and `CRD_IMPLEMENTATION_PLAN` and
distinguishes the detailed per-PR plan from them throughout; PF27 does not list the
per-PR plan among its governed artifacts and contains no occurrence of "per-PR".

No canonical home is created for it. PR-10 and PR-20 are not refactored to remove
duplication. Repair only on an actual contradiction or functional defect.

## D4 — The addendum-role token is removed

**The behavioural rule, which is what matters:** only a prompt that approves a
qualifying material change to an already-approved Specification or Plan may create a
`PF10_BUILD_NOTES_ADDENDUM`, and only on that approval. The addendum records the
approved change without rewriting the immutable approved base. Every other outcome
and every other prompt creates none.

The `PF10 addendum role` token is **removed** from prompt bodies and from
`global.json`'s `role_vocabulary`. Evidence for removal:

- nothing reads it — it appears in the graph only as `.node.pf10_addendum_role`, a
  leaf attribute, in zero edges, conditions, predicates or routes;
- no prompt body references any other prompt's role;
- four of the six declared producers used three different values for the same
  concept, because nothing authoritative defined it;
- the Project Prompt Contract Registry already carries the same fact in a better
  form — `outputs[].artifact` names the artifact rather than asserting a role, so it
  is derivable and checkable against the body.

Metadata is kept only where it provides concrete operational benefit. A second
encoding of a fact the registry already holds is not that.

## D5 — PF27 governs Ops Task Record and Remediation Review Record

PF27 explicitly claims both in its governed-artifacts list and contains their
templates (§3, §5), so PF27 is the structural authority.

**The general rule:** if Canon already provides the template for an artifact, use the
canonical template. If Canon does not, the required structure may remain in the
producing prompt.

This does not license rewriting every prompt that happens to share field names.
Repair only actual conflicts, incorrect bindings, or places where a prompt would
cause an artifact to diverge from the PF27 template.

## D6 — Drainage is removed from prompt behaviour entirely

**No prompt knows that drainage exists.** Prompt logic contains no manual drain,
drain owner, drain status, `MANUAL_DRAIN_REQUIRED`, `DRAIN_VERIFIED`,
`MANUAL_DRAIN_MISMATCH`, `READY_FOR_MANUAL_DRAIN`,
`NON_CANONICAL_PENDING_MANUAL_DRAIN`, pre-drain or post-drain state, waiting for
anyone to drain, blocking until a drain occurs, verifying that one occurred, or
reconciling drain evidence — **and no renamed equivalent.**

### The lifecycle, from every prompt's view

A qualifying approval creates the addendum. From the turn after it is created, the
addendum is part of PF10 and in force. **That is all.**

> **Amended 2026-09-18 by D8.** This section originally required the receiving prompt to
> read PF10 and *confirm the expected update is visible* on the immediately following
> turn. That confirmation is struck. It was itself machinery — another step and another
> way to stop — and it contradicted this document's own rule that an agent may not
> litigate a Product Owner action. A later prompt resolves and reads current PF10 as
> part of its normal job and acts on what it finds. There is no confirmation step, no
> separate artifact, no status, no gate, and no validation procedure.

It is not a drain check, canonicalization check, synchronization check, ownership
check, content verification, byte comparison, reconciliation procedure, new status
machine, or new artifact requirement. Later prompts simply read current PF10 and work
from current Canon.

### Why

Historical evidence must never gate current execution. The originating failure was a
prompt refusing to continue after the PF10 update had already happened, because it
was still looking for an intermediate condition that no longer mattered. A
conversational override is available and is exactly what this removes — these
workflows are intended to become increasingly automated.

### Consequences

- `POST_CLOSURE_DRAINAGE_STATUS` is **removed**. CL-20 loses the producer roster, the
  storage contract, the drain evidence and the drain-state inputs; what it needs, it
  reads from current PF10. **Amended 2026-09-18:** under Product Owner authorization the
  prompt was renamed to **`CL-20 — Prepare Closure Memo and Post-Closure Record`** and
  now produces `CLOSURE_MEMO` **and** `POST_CLOSURE_RECORD` — the surviving inventory of
  already-produced addenda, without readback state, reference role or drain
  verification. The merged registry, graph part, Flow Index and four referring prompts
  all carry the new name.
- `PF10_REFERENCE_ROLE` is **deleted as a field**. What is retained is the factual
  provenance — the PF10 version or equivalent identity actually read at that point.
  **Record what was read; do not assign it a workflow state.** A field with allowed
  values invites later logic to branch on it; a recorded fact cannot become a gate.
- RS-40 loses its `DRAIN_VERIFIED` gate and keeps its resumption and routing
  responsibility. If current Canon says implementation may resume, it resumes.

### What must survive

Removal is scoped to drainage machinery, not to functionality sharing a paragraph
with it:

- **approved-base immutability** — independent, and one of the reasons the addendum
  mechanism exists at all;
- legitimate routing and resumption behaviour;
- historical and provenance facts;
- current PF10 as execution authority;
- any unrelated functional requirement in the same clause.

## D7 — The repository is the storage authority; Drive is not one at all

Ruled 2026-09-18, strengthening the 2026-09-17 repository-first decision.

**The repository is the persistent storage and versioning authority for this prompt
ecosystem. Notion is the operational and indexing layer. Google Drive is not a storage
authority at all** — not a default, not a fallback, not a place canon is resolved from.

Consequences:

- `Glow / Ephemeral Planning Files` is removed as an artifact destination; artifacts go
  to `docs/ephemeral/`, referenced by repository path.
- Direct-Drive-link requirements are removed; a repository path replaces the link.
- PFCanon is resolved from `docs/pfcanon/`, not by walking Drive folders.
- One conditional sentence survives: *"Google Drive is used only where Nathan directs a
  specific file there."* That is an escape hatch for a file he asks for, not an
  authority.
- Persistent ecosystem-management infrastructure lives in
  `docs/prompt_ecosystem_management/` — the fourth open repository path.

**Derived output is never committed.** The assembled graph contract is built from
`docs/graph/parts/` on demand and represented downstream by its proof token. The
committed copy at `docs/ephemeral/gcfpe.r20260914-1.graph-contract.md` was removed on
2026-09-18: it had drifted from its source and still carried the retired drainage
machinery, so a session reading it would have rebuilt exactly what the repair retired.

**Applied to prompt behaviour 2026-09-18.** The cross-cutting storage pass rewrote **333
passages across 44 of the 55 prompts**: artifacts now land at `docs/ephemeral/` by
repository path and PFCanon resolves from `docs/pfcanon/`. Verified 44/44 by isolated
readback, with zero surviving Drive-as-authority references and the single conditional
sentence preserved. Report: `docs/ephemeral/gcfpe.storage-pass.repair-report.md`.

> The scope figures in the earlier revision of this note (44 storage / 39 PFCanon) were
> measured by pattern. Measured against the live bodies the PFCanon figure is **42**, not
> 39, and the occurrence count is **333**, not 310.

### Applied under D7 — coordinator decisions, not new rulings

Three passages could not be resolved by substitution and were decided centrally so that
one concept did not acquire several encodings across prompts:

- **`EPHEMERAL_DRIVE` is retired**, replaced by the existing sibling
  `REPOSITORY_CONTROLLED` in all eight prompts that carried it. Under D7 the class it
  named no longer exists. It was not renamed: minting a replacement would create a token
  nothing validates, and the sibling already covers the case. It appeared in no graph
  part and no registry field.
- **`QA-10` §55 and `QA-50` §29 were narrowed, not deleted.** Both forbade treating a
  repository file as PFCanon authority — correct when Drive was authority, inverted under
  D7, and `QA-10` named `docs/pfcanon` explicitly. `docs/pfcanon/` is now carved out as
  the authority and the prohibition still covers every other repository file, because the
  hazard is real: `audit/docdeltas/` holds PF-named files that are not controlled canon.

**Drive references are interpreted by function, never by the word** — the same rule D9
states for "drain". `global.json`'s eleven Drive URLs are pinned historical captures
scoped `REPAIR_BASELINE_EVIDENCE_ONLY_NOT_A_RUNTIME_CURRENT_PF10_ALIAS`. They are
provenance and must survive; the graph needed no change in this pass.

## D8 — No mandatory post-addendum check, and no replacement for it

Ruled 2026-09-18.

The original intent was always simple: a qualifying producer creates the addendum; on
the next turn PF10 is current; nothing ever blocks later work on an addendum transition
state.

The 2026-09-17 mandate retired the four-state drain machine but kept **one** mandatory
confirmation check in its place. That check was itself machinery — another step, another
way to stop, and it contradicted the same section's rule that *an agent may not litigate
a Product Owner action.* The prompts had already resolved the contradiction in favour of
not checking.

**The mandatory check is struck.** PF10 is the canonical authority throughout the
system, so a later prompt resolves and reads current PF10 as part of its normal job and
acts on what it finds. If that read happens to show the expected reference, nothing
further is required or recorded. There is no confirmation step, no separate artifact, no
status, no gate, no validation procedure. Where a record must show what it read, it
records the PF10 version actually read **as provenance — evidence, never a gate**.

The interim `pf10_reference_visibility_check` and its `PF10_REFERENCE_VISIBILITY`
vocabulary are removed from the graph with it.

**The standard for any future rule of this kind:** does it make the ecosystem simpler,
more deterministic, more automatable, and less likely to stop an agent from completing
legitimate work? A rule that fails that test does not earn its place.

### Amendment, 2026-09-20 — the enforcement limit, stated so it is not rediscovered

Product Owner instruction, 2026-09-20. This amends how D8 is **enforced**. It does not
change what D8 prohibits, and it strikes nothing further.

The guard carrying this ruling has been written eight times and defeated seven. Every
defeat took the same form: **the check selects, and the prohibited gate is written where
nothing selects.** v1 and v2 selected on phrasing and died to paraphrase and synonym.
v3 through v6 selected on location and died to a new location each time. v7 selected on
object shape and died to a clause that is not a branch.

The eighth version stops enumerating what to inspect and enumerates what may exist:

- the routing surfaces are pinned whole, both keys, with no selector inside them;
- every branch-shaped object naming PF10 anywhere else in the contract is an error unless
  allow-listed;
- `pf10_addendum_contract` is key-exact, because `subset_errors` is a subset test and let
  unknown fields into a closed governance object — which is how v7 fell;
- the contract's top-level key set is closed, with promotion lifecycle keys exempt.

Together these close the **placement** axis. They were measured, not asserted: 13 of 13
recorded attack placements caught, at a fixture cost of 1 amended expectation in 140.

**What they do not close, verified by execution and accepted here rather than left for a
ninth round to discover:**

1. **A branch that never names PF10, placed inside an existing contract key.** A terminal
   branch reading *"the current controlled Build Notes record differs from the previously
   approved addendum baseline"* passes. "Build Notes" is PF10's own title; an author
   writing naturally may never type the token.
2. **A prohibited rule written into an existing field's value.** Every key check is a
   key-*name* check; none reads values for prohibited semantics.
3. **A clause inside any object other than `pf10_addendum_contract`**, which is the only
   object enumerated exactly.

**This limit is accepted, not overlooked.** Widening the token list to `PF-10`, `PF 10` or
`Build Notes` buys exactly one round; that is how v1 and v2 died, and repeating it would be
the ninth instance of the same mistake. The vocabulary axis is therefore **enforced by human
review, not by machinery**, and no future round should record its existence as a new defeat.

A guard comment that claims more coverage than this is itself a defect. Two shipped guards
carried such comments, and in both cases the comment stopped a reviewer from running the
injection that would have exposed them. The installed guard states these three residuals in
its own source.

## D9 — `forbidden_fields` is scoped to the addendum, never to Canon disposition

Ruled 2026-09-18.

`pf10_addendum_contract.forbidden_fields` keeps its three drainage entries as an active
guard against reintroducing the retired fields. **That prohibition is strictly scoped to
the PF10 Build Notes Addendum lifecycle.**

It places no restriction on Canon disposition. These remain legitimate and must be
preserved intact:

- canon-conflict and ADR records;
- `NEW_CANON` and `CANON_RECONCILIATION` classifications;
- the permanent Canon drainage target and owner;
- the appropriate Canon target and responsible destination for an approved change;
- **PF09 rows identifying where an approved change must ultimately land in PF Canon.**

**Interpret by function, never by the word.** A validator must not reject a field because
its name or value contains "drain". Verified against the repaired bodies before this was
recorded: PF09 references, canon-conflict registers, `NEW_CANON`, `CANON_RECONCILIATION`,
permanent drainage target/owner, CRD candidates and ADR references all survive the
drainage sweep at counts identical to the pre-repair bodies.

## D10 — Batch 2's recorded blocker is obsolete

Ruled 2026-09-18.

Batch 2 was held at `BATCH_2_BLOCKED` on: *"Drive has no content-write for an existing
file ID, so the synchronized graph, the rebound control copy and report v1.1 cannot be
persisted."*

That blocker is **structurally dead**, not merely stale. The graph is no longer a Drive
file — it is held as parts in the repository and the assembled artifact is deliberately
never persisted. Storage authority is the repository.

A batch status is not preserved for its own sake. Batch 2 needs a bounded current-state
verification against the merged bodies, not a re-run: is the blocker obsolete, are there
remaining actual defects under current rules, do its prompts fulfil their contracts. If
clean, it closes. Work is not manufactured because a batch was historically marked
blocked.

## Repair scope — measured 2026-09-18

| | |
|---|---|
| Prompts containing drainage-related language | **54 of 55** |
| Line occurrences | **367** |
| Repeated passage families (3+ prompts) | **30**, covering **214** occurrences |
| Low-repeat and one-off passages | **141**, covering **153** occurrences |

> ⚠️ **Supersedes the earlier figure of 36 prompts / 162 occurrences.** That count
> matched only the three uppercase drain-state tokens. Matching drainage language in
> any form finds 54 prompts and 367 occurrences. The earlier number is superseded and
> must not be used as a scope estimate.

### The surface that actually needs repair

Separating the retired PF10 addendum lifecycle from legitimate canon drainage — the
distinction in D6's *What must survive* — classifies every occurrence by **what the
word is doing in that sentence**, not by where it sits:

| | Distinct passages | Occurrences |
|---|---|---|
| **Require rewrite** — retired lifecycle present | **142** | **280** |
| **Legitimate canon drainage** — preserve unchanged | 18 | **74** |
| **`CL-20` title references** — carried by the rename, not the sweep | 11 | 13 |

> ⚠️ **Supersedes the earlier figure of 93 passages / 218 occurrences** recorded in an
> earlier revision of this document. That split was produced by a heuristic that
> bucketed a passage as no-edit whenever its drain-word sat near register or ownership
> language. Reading every occurrence in context moved **49 families / 62 occurrences**
> from no-edit to rewrite. The mis-bucketed passages fall into two kinds:
>
> - passages that **gate on the retired lifecycle** — *"only after verified drainage
>   does RS-40 resume"*, *"its exact manual-drain prerequisite; PR-20 may not rely on it
>   before verified drain"*, `drain_verification_anchor`, `DRAIN_VERIFIED`. These are the
>   machine itself and could not be left standing.
> - **stale negative authority** — *"this prompt does not implement, plan, run QA, merge,
>   drain PF10, or rewrite an approved base"*. Prohibiting an action that no longer
>   exists is harmless at run time but tells a future reader the machine is still there,
>   which is precisely what D6 retires. These are single list-item deletions; the rest
>   of each prohibition survives.

The 18 preserved families are the Canon-maintenance process, not the addendum machine:
`CANON_CONFLICT_REGISTER`'s *permanent drainage target/owner*, *permanent Canon drainage
ownership*, and *drain PF Canon* in negative-authority lists. A lexical sweep for the
word would have deleted all of them.

**The repair is a rewrite, not a removal.** Nearly every family carries surviving
behaviour — the R1 workflow, PFCanon resolution, approved-base immutability, the D4
producer rule, canon-conflict handling, PR routing, handoff and terminal rules are all
interleaved with drainage clauses in the same sentences. Lexical deletion of the word
would take functioning behaviour with it. Three moves cover the whole surface:

1. **Delete** the drainage clause from an otherwise valid surviving instruction.
2. **Replace an obsolete drainage gate** with the qualifying approval itself, or with
   reading current PF10 where current PF10 is what the step actually needs.
3. **Replace a drainage enum or status** with a recorded provenance fact where
   historical evidence must be preserved, in these words: *"Record the PF10 version
   actually read as provenance; it is evidence of what was read, never a gate on later
   work."*

Sixteen passages were whole-line or whole-block deletions — the `status`,
`canonicality`, `drain_owner` and `drain_verification_anchor` fields of the addendum
contract, and the four-value drain-verification enums. Where deleting an enum left its
lead-in sentence introducing nothing, the lead-in was folded into prose rather than
left dangling; where it left a bullet with no list, the bullet was folded in or removed.
No replacement status token, enum or gate was introduced anywhere.

## Execution decisions

**Drainage removal is one cross-cutting repair**, outside the six-batch sequence,
because it is one global rule and splitting it across six authorizations creates six
chances to apply it six different ways. This is an exception for this shared rule
only; it is not a licence to collapse the batch structure, and batch-local review of
unrelated changes still happens in its batch.

**Drainage findings are not adversarially verified before repair.** D6 resolves the
substantive question, so occurrence-by-occurrence litigation buys nothing. This is
not a licence for blind string deletion — see *What must survive*. Verification is
retained where a false positive would cause a wrong functional edit, including the
storage-architecture and specification-format findings.

**The Project Prompt Contract Registry is re-pointed to the current release before
approval**, not approved stale and updated afterward.

## D11 — Contract assertions validate behaviour, not wording

Ruled 2026-09-18 by the Product Owner's standing instruction that known findings are driven
to resolution rather than carried as non-blocking backlog.

The Project Prompt Contract Registry asserted prompt correctness through `required_literals`
— exact substrings that the governance audit tests with `if value not in text`. Measured
against the live bodies, **70 of 269 assertions failed while behaviour was correct**, and the
largest single assertion, `select only the controlled Markdown lane`, was **absent from all
55 bodies and had never been present in any of them**.

**A check that fails on every member of a set carries no information.** It did not flag the
44 prompts that named Drive as the Canon authority before the storage pass; it failed
identically before and after. Meanwhile `forbidden_literals`, `required_regex` and
`forbidden_regex` were empty on all 55 rows, so nothing detected wrong-source resolution at
all.

**The ruling:** an assertion must distinguish a correct prompt from an incorrect one. Where a
behavioural requirement can be checked, check the behaviour — the named location, the failure
state, the prohibited source — not the sentence a prompt happens to use to express it.

Applied 2026-09-18:

- Removed `select only the controlled Markdown lane` (45 rows) and the two exact header
  literals (55 rows each). The release carries **two header conventions** — eleven prompts use
  `Prompt version: \`091426.1\`` where forty-four use `Prompt Version: 091426.1` — and both
  declare the identity the rule exists to guarantee.
- Added `required_regex` on all 55 rows: header version and release tolerant of both
  conventions, plus `docs/pfcanon/` as the Canon source.
- Added `forbidden_regex` on all 55 rows guarding D7: `Glow / Core Docs / PFCanon`,
  `Glow / Ephemeral Planning Files`, `drive.google.com`, `EPHEMERAL_DRIVE`. **This guard did
  not previously exist in any form.**
- `GCFPE-MGMT-10`: dropped the `PF10` assertion — it repairs prompts, not builds — and the
  `NEXT_PROMPT_HANDOFF` assertion, because all four of its result states return terminally to
  the Product Owner and the handoff contract requires zero blocks on a terminal result. PR-50
  is the same and its row already omitted it.
- `RS-40`: dropped the brittle `controlled Markdown` literal; the body says
  `controlled PF10 Markdown`.

Result: **499 assertions evaluated, 0 failing**, up from 269 evaluated with 71 failing. The
new guard was tested against five injected regressions — Canon resolved from Drive folders,
artifacts saved to the Drive folder, a direct Drive link, a reintroduced `EPHEMERAL_DRIVE`
token, and a dropped Canon location — and caught all five, while passing a clean control.

### Registry rows corrected to match actual behaviour

The registry describes intended prompt behaviour. Where a row and a body disagreed, the body
and the graph were authoritative and the row was stale:

- `IA-40`: removed `WRONG_ROUTE_APPROVED_BASE`, a state the body never emits (it emits
  `WRONG_NATIVE_LANE`); added `MATERIAL_PLAN_DELTA` / `PLAN_DELTA_PENDING`, which IA-30
  explicitly routes to and consumes.
- `IA-50`: removed the `ESC-40` consumer — the body states *"Do not route to ESC-30 or
  ESC-40"*, and Batch 2 redline R25 removed the matching graph edge.
- `IA-60`: removed the `ESC-30` consumer, on the same evidence and redline R26.
- `authority_sources`: four duplicate entries pointing at a pre-merge extraction workspace
  collapsed to one, labelled `HISTORICAL_LINEAGE_NOT_A_RESOLVABLE_PATH`.

## D12 — The batch sequence is retired; changes are managed by rule, not by batch

Ruled 2026-09-18 by the Product Owner, approving the strategic assessment of the repair
process. **Batches 3–6 are replaced by one consolidated pass over the 37 remaining prompts
plus one release-wide gate.**

The six-batch model assumed defects are per-prompt and lane-shaped. Two completed batches
show they are per-rule and corpus-shaped. Batch 1's own report: *"Root cause found at the
control, not the prompts."* Batch 2 closed **22 of 22** contract findings on the prompt side
with **zero prompt edits required**; it was held only by a graph synchronisation that could
not be written to Drive. Meanwhile the two repairs that did change prompt bodies — drainage
removal and the Drive → repository storage pass, 333 passages across 44 prompts each — were
single rulings applied corpus-wide, and both were executed **outside** the batch sequence.

Splitting one shared rule across several authorizations creates several chances to apply it
several different ways. Per-batch rechecking re-verifies the same concerns four more times
with different eyes, which is where inconsistent application comes from. A single corpus-wide
gate cannot produce four different answers.

**The ruling has three parts:**

1. **Execution** — one sweep, four lanes concurrent, findings reconciled centrally,
   cross-cutting decisions taken once and applied uniformly. One release-wide gate: graph
   rebuild and closure, registry validator, interface closure across all 55, isolated readback
   of everything changed. Recorded in `execution-and-delegation-model.md` §0A.
2. **Lessons** — seven binding lessons carried from Batches 1 and 2, recorded in
   `execution-and-delegation-model.md` §0B.
3. **Change management** — a standing process for changes after this release, with a
   defect-class catalogue, a seven-point definition of done, and an explicit authorization
   boundary. Recorded in `ecosystem-change-management.md`, a new document in this directory.

**Product Owner gates that survive:** authorizing the consolidated pass, and approving
promotion at the gate. The batch-by-batch authorization checkpoints are removed because they
bounded the wrong thing — they bounded prompts, and the defects were in rules.

**Consequence for the Notion plan.** The GCFPE Expanded Prompt Repair Plan and Six-Batch
Checklist remains the historical record of Batches 1 and 2 and the source of the finding
lists. Its Batch 3–6 sections are **superseded, not deleted**, and are marked as such on the
page so no future session executes them.

## D13 — The graph is the authority for routing and result states; the registry derives them

Ruled 2026-09-18 during the consolidated pass, under the Product Owner's standing instruction
that findings are driven to resolution rather than carried.

The consolidated pass raised 62 findings. **33 of them had a single cause**: the registry's
`outputs[].consumers`, `outputs[].states` and `required_interfaces` had been authored by hand
rather than derived, and had drifted from the prompts. 28 rows disagreed on consumers and 15 on
output states.

**The disagreement was adjudicated by two independent instruments, which agreed with each other
and against the registry**: the machine-readable graph parts, and four workers who read the
bodies blind — without the graph, without each other's work, and without the registry's answer.

The sharpest case: `PR-30`'s declared success state was `MERGE_PENDING`, which its own body
forbids; its actual success state `PR_CANDIDATE_PUBLISHED` was undeclared; the lane's busiest
edge `PR-30 → PR-35` was absent while a twice-prohibited `PR-30 → PR-40` edge was declared.

**The ruling:** routing and result states are **derived** into the registry from
`docs/graph/parts/`, never authored independently there. The graph's outbound edges give
`consumers` and `required_interfaces`; `node.result_states` gives `outputs[].states`. Where the
registry and the graph disagree, the graph wins and the registry is regenerated. A change to
routing is made in the parts and flows to the registry, so the two cannot drift apart again.

Applied 2026-09-18: 33 rows regenerated; all 55 rows now agree with the graph on both consumers
and required interfaces.

**What this ruling does not cover.** `inputs`, `function`, `mutations` and `failure_contract`
remain authored against the body, because the graph does not model them. The registry schema
also carries a flat consumer list and cannot express per-state routing; the graph expresses it
through edge state predicates. That is a schema limit, recorded rather than worked around.

## D14 — A settled ruling is enforced by function, and every ruling carries a tested guard

Ruled 2026-09-18, on the evidence of the two body defects the consolidated pass found.

Both had survived every previous sweep because **they violated a settled ruling without using
any of its banned words**:

- `RS-40` compared current PF10 against an addendum's normalized delta and **stopped terminally
  on a mismatch** — the retired drainage lifecycle reinstated by function, in a body containing
  none of the thirteen retired tokens.
- `QA-10` permitted writing its governed artifacts **off-repository** — a D7 violation naming no
  Drive location, so the Drive-marker guard could not see it.

**The ruling has two parts.**

**First, a ruling is enforced against behaviour.** Verifying that the banned vocabulary is
absent does not establish that the retired behaviour is gone. Each pass must ask what the
prompt makes an agent *do*.

**Second, no ruling is considered applied until a guard exists that would catch its
reintroduction, and that guard has been fired by an injected regression.** The audit had **no
guard at all** for the thirteen retired drainage tokens: the removal had been verified once and
nothing prevented their return.

Applied 2026-09-18. Guards added across all 55 rows for the retired tokens, the off-repository
permission, and the PF10 comparison-and-stop; a positive requirement added where a prompt takes
a fresh current-PF10 read, that it also state the provenance rule. Assertions rose from 499 to
721. All eight injected regressions were caught, the clean control passed, and a negative
control confirms the guard does not fire on legitimate Canon drainage text, which must survive.

## D15 — Ten qualifying-approval branches were still marked terminal after drainage removal

Found 2026-09-18 while repairing the workflow skills, by a validator that had never been able
to run against the current graph.

The graph's own invariant is that a public result branch marked `terminal_for_invocation: true`
emits **zero** handoffs. Ten branches violated it: they were marked terminal **and** declared
`next_prompt_handoff_count: 1`.

All ten belong to the six PF10 addendum producers — `CF-C-30`, `CF-E-30`, `ESC-40`, `IA-30`,
`QA-70`, `RS-20`. That is the whole explanation. Before D6 these branches terminated at the
`NATHAN_MANUAL_PF10_DRAIN` boundary, so `terminal_for_invocation: true` was correct and the
handoff count was zero. The drainage removal re-pointed each branch to its real receiver and
set the handoff count to 1, but **left the terminal flag set**.

The branch conditions had already been corrected — they read *"resume PR-30 directly on the
qualifying approval"* and *"the exact native receiver reads current PF10"*. Only the flag was
stale, so nothing in prose revealed it.

**Why it survived every earlier check.** The consolidated pass verified edges, consumers,
states and closure, but not this invariant. The one instrument that tests it,
`flowmaster-validate`, could not run at all (F6), and the graph copy bundled with it was the
pre-D6 240-edge version, in which these branches were genuinely terminal. A stale copy and a
broken validator concealed each other.

**Corrected 2026-09-18**: `terminal_for_invocation` set to `false` on all ten branches in
`docs/graph/parts/`. Zero violations remain across all 55 parts.

**The proof token changes as a result**, and this is the first time it has moved since the
repair began:

| | |
|---|---|
| Before | `55 nodes · 227 edges · 55 state_routes · 571,493 bytes · sha256 3b54d620…` |
| After | `55 nodes · 227 edges · 55 state_routes · 571,513 bytes · sha256 d7832c73…` |

Node, edge and state_route counts are unchanged; only the ten flags moved. Any document still
citing `3b54d620…` predates this correction.

> **The token moved again on 2026-09-18**, after the workflow-skill repair found three further
> defects in `docs/graph/parts/` that this rebuild did not touch: `PF10_REFERENCE_NOT_VISIBLE` still
> listed as an invocation-terminal result although **D8** retired the visibility check that produced
> it; the `CL-20` **predecessor** title rewritten to the candidate name although the `091326.2` page
> it records is still called *"CL-20 — Prepare Post-Closure Drainage and Closure Memo"* (`SCOPE-002`);
> and `flowmaster_primary_core_sha256` pinned at `495c2ca6…` against a measured `4d8bb9bf…`. All
> three were found by validators that had never been able to run. Corrected under Product Owner
> authorization; node, edge and state_route counts are unchanged.
>
> | | |
> |---|---|
> | Before | `55 nodes · 227 edges · 55 state_routes · 571,513 bytes · sha256 d7832c73…` |
> | After | `55 nodes · 227 edges · 55 state_routes · 571,479 bytes · sha256 021058dd…` |
>
> **Any document citing `d7832c73…` / `571,513` predates this correction.** The current token lives
> in `authoritative-surfaces.md`; the dated succession records keep the token current when they were
> written and are history, not instruction.

**The general lesson, added to the catalogue as `PAIR-001`:** a stale copy and a disabled
checker hide each other, and neither looks broken on its own. When a validator cannot run,
treat the invariants it alone enforces as unverified rather than as passing.

## D16 — No DevOps skill exists, and the Ops lane needs none

Decided 2026-09-19 by the Product Owner, in response to the round-5 skill-fit review, which
reported that OPS-20 has no primary skill and that its natural support skill is both forbidden
and absent.

**The ruling: "we do not need any devops skill period."**

`glow-hde-devops` is retired. None is installed, none is required, and none is to be created.
The candidate contract already replaced the named support-skill binding with an unnamed
capability policy, and the approved registry already forbids the literal `glow-hde-devops` on
all 55 rows under `SRC-001`. Both are correct and stay.

**What this settles about OPS-20.** The review recorded it as the one prompt whose declared
role is a standalone environment operator outside a PR work unit, with `glow-hde-pr-development`
excluding standalone Ops by name and `change-flow` disclaiming substitution for "an authorized
environment operator". That is not a gap to be filled. **OPS-20 and the Ops lane execute
natively, by their named human or agent operator, with no skill binding**, and the current
state is correct by design. The §10 questions it turned on — every prompt that *needs* a
primary skill has exactly one, and no prompt contract requires a capability no installed skill
safely supplies — are answered: OPS-20 needs no primary skill.

**What this settles about the registry pointer.** The approved registry names
`workspace_skill_registry_id: WSR-20260914.1-OBSERVATIONAL`, and that observational registry
still carries a `glow-hde-devops` row at `lifecycle: ACTIVE`. The row is **not** corrected,
because that document is an observation: it is `status: DRAFT`, `approved_by: null`, and
self-classified `INVENTORY_EVIDENCE_NOT_APPROVED_EXPECTED_STATE`, captured from a checkout
(`/root/.codex/skills/remote-skills`) that does not exist in the current environment. Editing
its rows would falsify a dated observation, exactly as rewriting a historical Before/After
token table would. It records what was seen on its date, and what was seen was accurate then.

The defect was never the observation. It was that an **approved** artifact took its
skill-identity model from an **unapproved** one. A disposition note now sits beside the pointer
recording that the observational registry is evidence only, confers no lifecycle, and is
governed for `glow-hde-devops` by this decision.

**The general lesson, added to the catalogue as `AUTH-001`:** an approved artifact must not
draw authority from an unapproved one. When it does, the contradiction surfaces as a disagreement
about a fact, and the repair instinct is to change the fact in whichever document is easier to
edit. The correct repair is to fix the authority relationship and leave the observation intact.
