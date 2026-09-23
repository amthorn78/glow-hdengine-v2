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

The guard carrying this ruling has been written ten times and defeated nine. Every
defeat took the same form: **the check selects, and the prohibited gate is written where
nothing selects.** v1 and v2 selected on phrasing and died to paraphrase and synonym.
v3 through v6 selected on location and died to a new location each time. v7 selected on
object shape and died to a clause that is not a branch. v8 closed the contract's key set
and died to the eight key names it had exempted so that a lawful promotion would not trip
it — four of the eight are absent from the candidate contract, so each was a free
top-level slot, and a complete prohibited gate written as an object under `promoted_at`
passed every check.

That eighth defeat is worth stating precisely, because it is the first one that came from
an **exemption** rather than a selector. The exemption was correct in intent: promotion
genuinely adds those keys. The error was waiving the **name**.

The ninth version waived the name and pinned the value **type** instead: lifecycle keys are
promotion metadata and are always scalars, so a container under one is the attack. That was
not enough, and the ninth defeat was found on its own bench before the version shipped.
`str` is a scalar, so the identical gate written as **prose** under `promoted_at` passed a
type-only pin cleanly. The tenth version pins the value's **form** as well: every lifecycle
value in every contract copy in this repository is a single token — an identifier, a release
id, a version, a status or an ISO-8601 timestamp — and a rule an agent can act on is prose,
which needs whitespace.

A third rule was written, measured and removed, and the record is kept in the guard's own
source so it is not reinvented: *lifecycle string values may not name PF10*. It failed twice.
It did not fire on `HALT_ON_PF10_DIVERGENCE`, because `\bPF10\b` finds no word boundary
against an underscore — the exact token it was added to catch. Widened, it rejected
`GCFPE-PF10-INTEGRITY-20260913.1`, a real `contract_id` in this repository, failing a lawful
contract. Even repaired it would have bought one round, because a rename to
`HALT_ON_BUILD_NOTES_DIVERGENCE` walks through it. **That is the v1/v2 mistake, and making it
a ninth time would have been worse than the hole.**

The tenth version stops enumerating what to inspect and enumerates what may exist:

- the routing surfaces are pinned whole, both keys, with no selector inside them;
- every branch-shaped object naming PF10 anywhere else in the contract is an error, with
  no allow-list — v8 carried an empty one, and its key was the first path segment only,
  so a single entry would have allowed that branch at any depth under that key;
- `pf10_addendum_contract` is exact over every nested key **path**, not just its top
  level, because `subset_errors` is a subset test and let unknown fields into a closed
  governance object — which is how v7 fell, and because v8's top-level-only enumeration
  let the same clause back in one level down, where it was caught only incidentally by
  two neighbouring checks written for other reasons;
- the contract's top-level key set is closed, with promotion lifecycle keys exempt by
  name and pinned to a scalar single-token value.

Together these close the **placement** axis. They were measured, not asserted: 18 of 18
recorded attack placements caught — all four lifecycle slots by object and again by prose,
both nested addendum positions, and every earlier defeat — at a fixture cost of 1 amended
expectation in 140, unchanged from v8, because neither the ninth nor the tenth version
amended a fixture at all. All five contract copies in the repository pass the lifecycle
form check unmodified, and a lawful promotion with scalar values stays clean.

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

**One further limit, recorded so it is not mistaken for coverage.** Several prohibited
placements are caught by checks written for unrelated reasons — a branch dropped into
`member_registry` trips that object's own schema check, and the addendum's two nested
objects carry exact checks of their own. That coverage is incidental. Where it was the
*only* thing standing behind a placement, the placement was treated as uncovered and the
guard was extended; where it merely doubles up, it is not counted as enforcement. A
residual that happens to be caught elsewhere today is still a residual.

### Amendment, 2026-09-20 — the tenth defeat, and the failure class it introduced

**Enforcement status at the time of writing: the installed build is v6.** Guard v11, described
below, is a packaged working copy that is **not installed** and has not been cleared by
independent review; its own report is
`docs/ephemeral/gcfpe.round18.d8-v11-derivation-guard.repair-report.md`, which records it as
`PACKAGED_AWAITING_INDEPENDENT_REVIEW`. The round-17 report's
`PACKAGED_AWAITING_INSTALLATION` belongs to the **v6** package and is not v11's status. Every
v11 behaviour and measurement in this amendment is a property of that uninstalled copy and is
recorded, with its environment, method and limitations, in the round-18 report; **none of it
describes enforcement currently in force.** What is
in force is v6, which carries the tenth defeat below and the nine before it. Read any
present-tense sentence about v11 accordingly.

The guard has now been written eleven times and defeated ten. The tenth defeat came from
neither a selector nor a waiver, and it is worth naming as its own class: **a lossy key
function.** The check compared *derived path strings*, and the derivation was not injective,
so two different contracts produced the same observed set and the comparison could not see a
difference that was really there.

Two placements, both inside `pf10_addendum_contract` — the one object this guard enumerates
exactly, and therefore the one place a hole is least excusable. Both were found by the
independent reviewer and both were reproduced here before being accepted.

**The tenth defeat.** Nested paths were flattened as `f"{prefix}.{key}"`. A key that already
contains a dot derives the identical string, so a top-level key inside the addendum named
exactly `producers.RS-20` derived a path already in the enumeration: nothing added, nothing
removed, every layer silent, all four gates green. Verified on `producers.RS-20`,
`producers.CF-C-30` and `native_outcome_normalization.PENDING`. The same value under an
ordinary key name is caught. The only difference was the dot. There were 22 dotted paths in
the enumeration, so 22 free slots.

**The second placement, from the same root.** A path was recorded for a list element only
when that element was itself a dict or a list. Every list inside the addendum is a list of
scalars, so none of their elements was covered at all, at any depth. A complete prohibited
gate appended to `forbidden_fields` passed all four gates, and reversing that list was
invisible. Three of the four lists were caught anyway, each by one unrelated value check;
by the rule this section already records, that is incidental coverage and not enforcement.
`forbidden_fields` had nothing behind it, because its only reader is a superset test.

The eleventh version, packaged and uninstalled, closes both structurally:

- a path is now a **tuple of typed segments** — dict keys as strings, list indices as
  integers — which is injective by construction, with no rejection rule and no vocabulary.
  A key carrying `.` or `[` is additionally reported as `AMBIGUOUS_KEY`, and messages render
  paths as JSON arrays, so an added and a removed path can never read as the same text;
- every list inside the addendum is pinned to its **exact element sequence**, order
  included, under the new code `PF10_ADDENDUM_LIST_VALUE_DRIFT`. An unenumerated list, a
  missing list and a list replaced by a scalar each report distinctly.

**A shape rule was proposed for the list elements and is refuted by measurement, recorded so
it is not proposed a third time.** The suggestion was to require every element to match the
bare single-token form already used for lifecycle values, on the reasoning that a field name
is a token and a gate needs whitespace. Two elements of the **lawful** `forbidden_fields`
are prose: *"any pinned PF document version"*, and *"any field describing this addendum's own
drainage state — not a Canon destination, Canon target, or PF09 row"*. That list does not
enumerate field names; it describes prohibited content, in English. The rule fails on the
contract as it stands. **That is the ninth defeat's mistake and the removed PF10-token
rule's mistake — a form pin that rejects lawful content — and it was not made again.** Shape
is unavailable on this axis, so the values are enumerated instead, which is what the object's
other three lists already were.

Measured against the packaged v11 copy on a scratch rig, not asserted, and not a claim about
installed enforcement. The run — environment pins, rig construction, per-placement results,
gate flags, fixture cost, responsible actor and limitations — is recorded in
`docs/ephemeral/gcfpe.round18.d8-v11-derivation-guard.repair-report.md`, which is the auditable
source for every figure in this paragraph; the validator sources themselves are not in this
repository and must not be, so the three sha256 identities in that report are how the packaged
copies are checked against it. **13 of 13** attack placements caught, including three dotted-key
targets, a nested dotted key, a bracket-shaped key, a key colliding with a list index, all
four lists, and a list reversal. Every earlier defeat stays caught — v8's object and v9's
prose under all lifecycle names, and the nested addendum clause — and a lawful promotion with
scalar lifecycle values stays clean. Fixture cost is **1 amended expectation in 140**:
appending to `exact_producer_set` now also drifts that list's element pin, so that case
expects both codes. The runner already supports an exact multi-code expectation and has
precedent for it; comparison stays exact equality, so the original code is still required to
fire. The guard block is byte-identical between the two validator copies.

**Also swept, and not a hole.** The layer-2 branch scan builds paths with the same dotted
derivation, but nothing selects on that path — it is a label in a report whose emptiness is
the only thing tested — so a collision there is cosmetic. A non-scalar element appended to
an addendum list is caught, then crashes an unrelated set-building step; that crash is
fail-closed and is the pre-existing class this section already records. Lifecycle values of
type `bool`, `int`, `float` or `None` receive no form check, which is the same waiver-by-type
shape as the ninth defeat one branch further down; **no change was made, because that value
space cannot express a directive.** A rule there would buy nothing, and this section already
records what writing rules that buy nothing has cost.


### Amendment, 2026-09-20 — v11 cleared by independent review, and installed

**This supersedes the enforcement-status statement in the amendment above, which said the
installed build was v6 and v11 was neither cleared nor installed.** That was true when written
and is left unedited under `AUTH-001`; this is its successor.

SFR-01 returned **`GUARD_HOLDS`** — the first verdict in this series with no defeat — and the
Product Owner installed v11. **The installed build is now v11.** Verified against the installed
bytes rather than the packages: all three file identities match, the previous v6 identities are
absent, the tree holds 321 files with no bytecode, and the guard block is byte-identical across
both validator copies. The installed build was exercised, not only hashed: all four gates green
from a scratch copy, and the round-18 bench reports 14 placements with none unexpected. Recorded
in `docs/ephemeral/gcfpe.round19.d8-v11-cleared-and-installed.md`.

**The guard has been written eleven times and defeated ten. v11 is the first to survive an
independent attack round.**

Three things from that round belong in this ruling rather than only in the report.

**The reviewer withdrew its own proposed remedy.** SFR-01 recorded that its token-shape rule for
`forbidden_fields` elements was wrong, that it had asserted the rule "costs nothing" without
running it against the lawful contract, and that this was the same error it had been naming in
v1, v2 and v9 — a form pin that rejects lawful content — made while pointing at it. Independent
review is not a second opinion to be weighed; it is a mechanism whose findings and whose
*remedies* both require reproduction before they are accepted. This section now records that a
refuted remedy is as valuable a result as a confirmed defeat.

**The argument for an exact enumeration is stronger than the argument it displaced.** The
standing objection to a pin is that it invites quiet editing. Editability was never the
variable; what matters is what the re-stamp costs. A hex string tells a reviewer nothing, while
`EXPECTED_ADDENDUM_LIST_VALUES` re-stamps as the literal prose being admitted — landing the list
injection requires pasting the prohibited gate sentence into guard source, in English, where a
reviewer reads it. That is a stronger property than the 45 paths, not an equal one, and it is
the reason exact element enumeration is the right shape for a closed governance object whose
content space is prose.

**The remaining risk has moved, and the ruling should say where.** Every defeat since v7 was
inside `pf10_addendum_contract`, the one object enumerated exactly. That object is now closed
on the placement axis. What remains **on that axis** is **E3**: thirty-three `subset_errors`
call sites, of which exactly one object is exact-keyed. This is the limit of what machinery
covers, not the limit of the risk — the vocabulary residuals below stay open. SFR-01's sweep
confirmed no lossy derivation outside the two already recorded: `subset_errors` compares raw
values, so its limitation is that it is a subset test, which is a different failure mode from
the tenth defeat. There is **no cheap sweep** for
those thirty-three: closing them requires a decision about which are closed governance objects,
prompt by prompt, not a mechanical pass. A future round that widens the guard without making
that decision first will be selecting a subset again, which is how v3 through v6 died.

The vocabulary axis — residuals E1, E2 and residual 1 — is unchanged and remains enforced by
human review, not machinery.

**This amendment does not close §10.** The gate requires the dedicated skill-fit review to be
re-run against the final installed snapshot. That snapshot now exists for the first time; the
review has not yet been run.

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

## D17 — `GCFPE-20260914.1 / 091426.1 / 55` is promoted; every predecessor is archived intact

**Product Owner, 2026-09-21:** *"I approve promotion. Promote, document thoroughly, and move all
predecessors to archive."*

The three predicates the register entry set were met first, in order: complete behaviour
validation of the exact pinned snapshot, independent governance post-flight with no mandatory
unresolved finding (`PASS WITH WARNINGS`, **zero findings against the release**), and the Product
Owner's separate approval of that snapshot.

### The transaction order is part of the decision

The register entry specified it and it was followed: **prepare and verify every successor binding
first, update the stable selection register last, rerun production validation against the
activated state, archive only after that.** No write failed, none was ambiguous, and no receipt
was inferred. This is a coordinated transaction, not an atomic one — the ordering *is* the safety
property, because there is no cross-system rollback.

### No page asserts its own selection

Ten control bindings moved to `status: REGISTER_CONTROLLED`, each carrying the register's URL and
the rule that it is operative **if and only if** the register selects this release. The register
alone says "selected".

This is not decoration. The ecosystem's own rule is *"never infer selected, merged, accepted or
resumed from those surfaces — resolve the authority that owns that exact state."* A catalog that
declares itself selected is a second authority, and two authorities is how a release ends up half
promoted with nobody able to say which half. The pattern was already designed, in
`GCFPE-20260914.1-Production-Activation-Delta-Manifest.md`; this decision adopts it as standing.

### Archival is a move, never a copy

56 pages — 54 member prompts, the PE Metaprompt, and the predecessor catalog — were **moved** to
the existing archive. A move preserves the page, its ID and its body; nothing was deleted,
overwritten or reconstructed. All 56 were confirmed present under the destination afterwards.

The un-versioned *Glow HDE Prompt Flow Index* was deliberately left in place: it is the parent of
the stable register, and archiving it would have taken the selection authority with it. **Check
what a page parents before archiving it.**

### What promotion did not change

Alpha remains `ALPHA_STOPPED_PENDING_CHANGE_FLOW_REFACTOR`. **Selection is governance maintenance,
not Alpha execution.** `HDE-EPIC040` PR01–PR03 remain accepted-final, PR04 has not started, and
its PR-10 handoff remains `NOT_YET_APPROVED` until Nathan's manual decision. Merge and abort
remain Nathan-only actions.

### The activation delta beyond the register is a separate, open change

Promotion recorded the selection. It did **not** rewrite the `UNSELECTED_CANDIDATE` literals that
remain inside the 55 prompt bodies and the two bundled machine contracts. Those are a real
follow-on, they touch bytes an independent review was scoped to, and they are recorded as open
rather than quietly performed. A promotion that silently edited 55 validated bodies would have
voided the post-flight verdict that authorised it.

## D18 — Alpha is resumed; `ALPHA_RESUMED` is minted because no resumed state existed

**Product Owner, 2026-09-21:** *"You should also unblock the alpha."*

`HDE-EPIC040` had been held at `ALPHA_STOPPED_PENDING_CHANGE_FLOW_REFACTOR` since the Change Flow
prompt ecosystem was found defective. **That refactor is `GCFPE-20260914.1 / 091426.1 / 55`**,
selected earlier the same day under `D17`. The stop's own condition is therefore discharged, and
the Product Owner discharged it.

### The vocabulary had no word for this

Every Alpha token in the ecosystem named a *stop* or a *decision about* a stop:
`ALPHA_STOPPED_PENDING_CHANGE_FLOW_REFACTOR`, `ALPHA_STOPPED_PENDING_GOVERNANCE_CORRECTION`,
`ALPHA_STOPPED_PENDING_MANUAL_PF`, `READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION`. **There
was no token for Alpha actually running**, because in this Epic's recorded history it never has.

`ALPHA_RESUMED` is minted here rather than left to drift in. A state that is described in prose on
six surfaces and named on none of them is the shape of defect this record exists to prevent —
`D11` and `D15` are both instances of a value that no one could resolve to a single authority.

### Resuming is not a Proceed, and the two are recorded separately

| authorised | not authorised |
|---|---|
| `PR-10 — Create PR Work-Unit Instructions — 091426.1` for `HDE-EPIC040-PR04`, by the retained whole-change IA | PR04 implementation, which needs the Product Owner's separate exact `PR-30` invocation |
| | a branch, a pull request, a merge, auto-merge |
| | a PF10 edit, a number allocation, an addendum drainage |
| | QA, Ops, release promotion, Epic closure, `PR-50` |

The detailed PR04 Plan that a `PR-30` Proceed would be issued against **does not yet exist**; it is
`PR-20`'s output. An agent must not treat the resumption as its precondition being met.

### Where the state lives

`ALPHA_RESUMED` is carried on the **Prompt Flow Index — 091426.1**, in the `Sole operative Alpha
state` block, which is the single operative record. The release register, the selected catalog,
the register entry and the Glow Operations Hub each state it consistently and point there. If they
ever disagree, the Flow Index block governs and the others are defects to correct.

### What it does not reopen

`PR01`–`PR03` remain `ACCEPTED_FINAL` and are not rerun. The approved Specification `v1.1`, the
Implementation Audit `v2.0` and the Implementation Plan `v2.1` remain immutable; resuming Alpha
progresses the current Plan, it does not re-author it. Merge and abort remain Nathan-only actions.

---

## D19 — A prose skill carries no advertised identity; its freeze digest is its identity

**Product Owner, 2026-09-22.** Asked whether the three prose skills revised in PE36's Task 01
should acquire a durable advertised identity — a `version:` frontmatter key or a revision
constant — as a standing convention, so future packages are distinguishable without the digest:
**"no"**.

### What was actually asked

`glow-workspace-currency`, `glow-artifact-storage` and `glow-write-boundary` carry no advertised
identity value of any kind. Measured, not assumed:

```
grep -rnE 'SKILL_TREE_SHA256|_REVISION|validator_revision|^version:' <the three skills>
→ no matches
frontmatter keys, all three: name, description
```

No skill in this workspace carries a `version:` field. The `FLOWMASTER_VALIDATE_REVISION` /
`validator_revision` mechanism belongs to `flowmaster-validate` and `change-flow`, which declare
revisions that reports quote.

### The ruling, and why it is the right one

**The digest is the identity. Nothing else is added.** This is the general form already stated in
`prompt-body-content-policy.md`: *"Governance state belongs to the artifact that governs it …
Skill identity belongs to the skill's own digest."* A `version:` line in frontmatter that loads
into every session is a second identity surface that can disagree with the digest, and the
disagreement surfaces at the worst moment — mid-handover, with two packages in hand.

It is also `NORM-001`: structure added for symmetry, with no consumer. Nothing reads a prose
skill's version. What distinguishes two packages in anyone's hands is the sha256 in the delivery
caption and the post-install digest comparison, and those already exist.

### The consequence for the packaging rule — read this before you invent a version

`skill-identity-and-freeze.md` requires that **advertised identity must be unspent**, diffed
against the previous package before packaging, with a match treated as a defect. That rule has
been broken three times and it is not weakened here.

**For a skill whose set of advertised identity values is empty, the diff is vacuous, not failing.**
Run it, record that it returned nothing, and package. **Do not create a version field in order to
have something to bump** — that is the specific action this ruling forbids, and a task brief
instructing a session to "bump each skill's own version" does not authorise it where there is no
version to bump. Report the discrepancy and proceed on the digest.

### What it does not change

The rule itself, for the skills that do advertise a revision — `flowmaster-validate`,
`change-flow` — is untouched and still absolute. Delivery hygiene is untouched: digest first in
the caption, one package per message, and the post-install digest comparison remains the only
control for the wrong-package case.

---

## D20 — The GCFPE MGMT change process is redesigned as one prompt with three modes

**Product Owner, 2026-09-22**, commissioning the work: *"It is time for a full review of the GCFPE
MGMT change-process ecosystem… My ideal end state is one persistent GCFPE MGMT prompt with three
explicit operating modes… This must remain one prompt, not three separate prompts."*

The audit, its measurements and the full design are
`docs/ephemeral/pe36.mgmt-redesign/GCFPE-MGMT-REDESIGN-ANALYSIS-v1.0.md`. This entry records the
rulings, not the analysis.

### What the audit established, in one line

**The change-management prompt lost its method.** `GCFPE-MGMT-10` went from 52,009 characters in
`091226.3` to 8,015 in `091426.1`; the sections that carried the procedure — *Execute the change*,
*Quality-control contract* — were deleted and relocated nowhere. Its only surviving procedure is a
*Batch method* for the sequence `D12` retired, so **the live path through the prompt contains no
procedure at all**, and every change since has been improvised.

### The three rulings

**D20-A — Scope.** The redesign covers `GCFPE-MGMT-10` **and the skill-change loop**. Packaging,
the reviewer prompt, the §10 verdict and install verification become named `EXECUTE` steps inside
one record rather than a parallel improvised process. Scoping to the prompt alone was rejected
because the measured friction — 30 repair rounds, 20 review rounds on PR #425, 11 versions of one
guard — lives in that loop.

**D20-B — The artifact is a Notion prompt body, not a skill.** It replaces the current
`GCFPE-MGMT-10` in place. It is explicitly invoked rather than probabilistically triggered
(`AF-003`), and the register, graph and registry already model it. **Consequence:** rewriting it is
a Class A change to a selected release member, its graph part and registry row move with it and are
rebuilt by script never hand-edited (`D13`), and `prompt-body-content-policy.md` governs what may
go in it — a `MODE` input is behaviour and qualifies; governance state does not.

**D20-C — `EXECUTE` applies changes directly.** Notion body edits, repository commits, pushes and
opening a pull request. **It stops at merge and install, both of which remain the Product Owner's**
and are recorded as remaining actions with their verification. Preparing a changeset and applying
nothing was rejected: it roughly doubles the cycle and reintroduces the hand-off cost the redesign
exists to remove.

### Consequences that bind any session implementing this

- **The record is a Modification**, never a "Change Record" or `CR`. Measured collision: `CRD`
  appears 2,694 times in `docs/`, "Change Flow" 733, bare `CR` 53 — and `CHANGE_RECORD` is already
  `GCFPE-MGMT-10`'s own declared output artifact at `project-prompt-contract-registry.md:2310`.
  Spelled out rather than abbreviated to `MOD`, which sits one letter from `MODE`.
- **A Modification is the unit of approval, not of "one thing."** Items batch when they share a
  rule, a verification or a package/review/install cycle. `coupling: ATOMIC` work must never be
  split across authorizations — that is the `D12` error — and `INDEPENDENT` items take a per-item
  disposition so one blocker does not hold the rest.
- **A Modification may target prompts, skills, rules or any combination**, and the target set
  derives the required gates rather than a session recalling them.
- **The gate is tiered by computed blast radius**, not applied at corpus scale to everything. The
  graph part is the interface contract, so tier entry is a diff on one JSON file. **Tier 0 means
  routing provably unaffected, not provably harmless** — anything changing what a prompt *produces*
  rather than how it *routes* is Tier 1 regardless.
- **Scope freezes at `ANALYZE` approval.** A mode may not expand its own scope; work discovered
  later becomes a new Modification. This is the rule that bounds the review loops, and it is
  independent of how much a Modification contains.
- **Readiness is decided by predicates, never a score.** Sequential discovery and unmeasured scope
  force a split; everything else is cost, counted in round trips through the Product Owner, with
  the prediction recorded against actual every time.

### What this does not decide

**It authorizes no implementation.** No prompt, skill, graph part, registry row or Notion prompt
body is changed by this ruling. The staged plan — the Modification format and its two scripts, the
prompt rewrite, the graph and registry reconciliation, and a pilot on one real small change — each
needs its own authorization, and the Class A prompt rewrite needs it most.

**The pilot is not optional.** *"The new process works"* is a claim, and this ecosystem's failures
are uniformly claims made before the measurement that would have checked them.

## D21 — One run is one Modification; parts carry failure; one session can carry the whole process

**Product Owner, 2026-09-23**, on the first triage run turning one list into six Modifications:
*"why do I need 6 handoffs?? We have a serious issue. We should be able to group multiple changes
in a single run, that is the WHOLE POINT of all this."* Then: *"really it would be ideal if a
prompt could do the whole process in one session with subagents, but even then, having one agent
per change seems like overkill."* And, on whether a merge approves anything: *"I merge to preserve
documentation."*

### What was wrong

`D20` made a Modification the unit of approval: items batched only when they shared a rule, a
verification or a cycle, and each Modification had one `coupling`. A list of six different rules
therefore became six Modifications — six analyses, six plans, six executions and twelve approvals.
That is one-at-a-time processing at a coarser grain, which the Product Owner had already rejected
on 2026-09-22: *"one change at a time through the system is just not realistic."* The shared-package
rule added the same morning cut review cycles but not the round trips; it treated the symptom.

### The rulings

**D21-A — One run is one Modification.** Everything handed in together goes through `ANALYZE`,
`PLAN` and `EXECUTE` together, with one approval per mode, and triage emits one handoff. `ANALYZE`
may still recommend moving a part to a separate run. That is advice, never a refusal.

**D21-B — Parts carry failure; the Modification does not.** A part is the changes that must land
together — one rule across its surfaces, above all, so splitting a rule stays the `D12` error. A
part lands whole or not at all. Parts land independently unless one is ordered `after` another.
Each part carries its own class A–E, because a batch mixes them. **`coupling` is retired.**

**D21-C — A merge preserves the record; it approves nothing.** Approval is the recorded field in
the Modification. Triage opens a pull request so its output can be merged whenever the Product
Owner wants it preserved.

**D21-D — One session can carry the whole process.** Triage, then `ANALYZE`, `PLAN` and `EXECUTE`,
pausing for the Product Owner's approval between modes and continuing in the same session once it
is recorded. A handoff is needed only when a fresh session takes over.

**D21-E — Delegate by workload, never by change.** A worker takes a measured slice of the work — a
lane of prompt bodies, a set of files — when parallel reading or independent verification pays for
it. Most Modifications need no worker, and none gets one agent per change. The independent §10 skill
review stays independent, by its own rule.

### Consequences that bind any session implementing this

- **This supersedes one consequence of `D20`**: "A Modification is the unit of approval, not of
  'one thing' … `coupling: ATOMIC` … `INDEPENDENT` items take a per-item disposition." Everything
  else in `D20` stands.
- Within one Modification, every part that changes a skill ships in one package, one review and
  one install. `shares_package_with` remains for two separate runs touching the same skill.
- The six drafts pushed on `docs/20260923-modification-intake-alpha-feedback-open-items` were
  produced under the superseded model. They are superseded, not adopted.

### The tested guard (`D14`)

`modification_validate.py` enforces the structure:

- every item is in exactly one part;
- a part names only real items;
- `after` names real parts and never forms a cycle;
- each part carries a class once past INTAKE;
- a part may not be partly applied and partly blocked, at `COMPLETE` or when the Modification
  stops.

Each check has an injected must-fail regression. Of the 39 selftest cases, 6 fail with the parts
checks disabled and 2 fail with the half-applied check disabled. A Modification abandoned at
INTAKE is not asked for analysis fields it never reached, and a must-pass case holds that.

## D22 — A transient file the tooling makes in order to read a prompt body is a read, not a copy

**Product Owner, 2026-09-23:** *"allow save to disk, and re-write the rule where needed so it is
rationally conditional and not automatic."*

### What was wrong

`prompt-corpus-policy.md` prohibited, "absolutely", persisting a prompt body anywhere outside
Notion. The Claude Code harness saves any tool result above roughly 30 KB to a session file on
its own, before the session sees it. Thirteen of the 55 `091426.1` bodies are over that size,
among them `PR-10`, `PR-20`, `PR-30`, `PR-40`, `OPS-30` and `QA-10`. Read literally, the rule
made those thirteen unreadable. That blocked `AF-004`'s scan and the scope measurement for
`MODIFICATION-20260923-alpha-feedback-open-entries`. The policy exists to stop a parallel
corpus: a mirror, a cache, a backup, a byte-identity check. It never meant to stop a read, and
its own text says so: *"I just don't want them copied to disk. How will you ever do any work if
you cannot read them."*

### The ruling

**The test is what a file is for, not where the bytes happen to sit.** A file that exists only
because the tooling delivered or needed the body that way is part of the read. It is allowed
under five conditions, and all five must hold:

1. it is outside the repository and outside any shared, synced or uploaded store;
2. it serves only the read or check in hand, and is never a source for later work — the next
   read goes back to Notion;
3. it is never hashed, byte-compared or otherwise used as the body's identity;
4. it is deleted when that read or check is done, and at the latest when the task ends. Where
   the harness does not let the session delete a file in its own session store, the file is left
   to the harness's teardown and never read again;
5. the session says in its report that it happened.

Everything the policy was written against stays prohibited, without exception: mirrors,
exports, snapshots, backups, a cache reused across tasks or sessions, a committed or uploaded
body, accumulation into a corpus, body hashes or byte comparison, and any procedure that
requires a local corpus before work can proceed.

### Consequences

- `prompt-corpus-policy.md` carries the amendment as a successor section. The 2026-09-21
  directive is preserved verbatim above it (`AUTH-001`).
- `prompt-validation-procedure.md` steps 3 and 6 and `postflight-procedure.md` are corrected in
  place. A scratch file feeding `--bodies-stdin` is permitted under the same five conditions. The
  validator still has no path option, because a path option invites a standing directory.
- The auto-saved Notion fetch files from 2026-09-23 in this session were ordinary operational
  pages, not prompt bodies. No correction is owed for them.

### The tested guard (`D14`)

**None yet, and this is recorded rather than implied.** The conditions govern session behaviour,
and no repository check can see a harness session directory. The standing guard is condition 5:
the report makes every such file visible. A guard that fires is owed to the next change that
touches a validator or skill. Until then, this ruling is applied but not guarded.

### Refined the same day — a session cannot always delete its own session file

The first measurement under `D22` found that the Claude Code harness refuses a session's `rm` on
its own tool-results directory ("Session Transcript Tampering"). The workers did not work around
the refusal. Condition 4 as first written could not be met. It now reads: deleted where the session
can delete it; otherwise left to the harness's teardown and never read again. Everything else in the
ruling stands. The first files left this way were two for `PR-10` and two for `OPS-30`, disclosed in
the 2026-09-23 ANALYZE record for `MODIFICATION-20260923-alpha-feedback-open-entries`.

## D23 — The Alpha Feedback rule changes: artifacts hold results, handoffs are short, implementors have latitude, PR-35 has its own session, releases stop copying unchanged prompts

**Product Owner, 2026-09-23.** He approved the analysis of
`MODIFICATION-20260923-alpha-feedback-open-entries` with "approve, all agreed", covering its three
rulings, and its plan with "yes approve". On the same day he ruled that a PR-40 reject re-plans
through PR-20: *"if a whole PR cycle fails validation, then it means it was badly executed and yes,
needs to route back to PR-20."*

This entry records the rulings. **The exact wording each rule is applied with is the canonical
wording in that Modification's §P** (`docs/ephemeral/modifications/`). It is cited there, not
restated here, so the two cannot drift (`DERIV-001`).

### The rulings

**D23-A — Results live in the artifact (`AF-008`).** Every result a session produces, test results
above all, is written to its output artifact before a handoff is emitted. A handoff names the
artifact and never carries the only copy of a fact.

**D23-B — A handoff is short (`AF-008`).** A handoff carries:
- the destination prompt by full name, version and direct Notion URL;
- the receiving role and session;
- each input artifact by repository path, with a one-line label;
- the pull request reference when the receiver continues an existing PR;
- only the minimum context for a condition the artifacts do not record.

It carries no branch or commit, and restates nothing the named prompt, canon or files hold. The
block ends the response, after at most a few lines. **This reverses the "complete, self-contained
handoff carrying status, completed work, decisions, constraints" rule** in `handoff_contract`.

**D23-C — Implementors have latitude; "material" is defined (`AF-009`, with `AF-010`'s merged scope).**
- **"Material" means a change to the Epic-level commitment:** its outcome or objective; approved
  acceptance criteria; a protected architectural, security, data-model or external-contract
  boundary; the scope of several planned work units; an accepted dependency or cross-team
  commitment; or budget, schedule or risk needing Product Owner direction. A planned approach found
  incomplete, impractical or inferior is not by itself material.
- **Everything obvious, necessary and consistent with the objective** is decided, implemented and
  tested by the implementor, and recorded under *In-flight decisions* in `PR_IMPLEMENTATION_RESULT`.
- **Scope: the PR lane.** The ESC remediation lane keeps its own threshold.

**D23-D — PR-35 runs in its own dedicated session (`AF-011`).** PR-30 and PR-35 remain two phases of
one work unit, sharing everything except the session. **This reverses the same-session contract,
and re-pins R1 row GCF-17.**

**D23-E — The PR-35 session subscribes to its pull request** where the surface allows, and PR-40 is
dispatched when that subscription observes Nathan's merge (`AF-011`). The observed merge event
replaces Nathan's pasted merge assertion as PR-40's trigger. PR-40 still verifies the merged state
independently, and no agent merges. **This reverses `direct_PR35_to_PR40_automatic_edge: false`.**

**D23-F — A PR-40 reject re-plans.** An in-scope defect found by PR-40 in landed work goes back to
PR-20 for a new plan, in a new dedicated implementor session that Nathan seeds, with a new Proceed.
**This reverses "never a second Proceed" for that case, and re-pins R1 row GCF-15.** Carried by
`MODIFICATION-20260923-pr40-reject-replans`.

**D23-G — Releases stop copying unchanged prompts (`AF-012`, GCFPE only).**
- Membership and each member's current version live in the register and the complete-prompt-set
  catalog.
- A changed member gets a successor page. An unchanged member keeps its page, and the register
  records it in the new release.
- Bodies carry no release-bound header line.
- **This supersedes the `Prompt version:` and `Ecosystem release:` allowance in
  `prompt-body-content-policy.md`, and `D11`'s in-body version assertion.**

**Class B, not ruled here:**
- the Notion read-only message (`AF-006`), which applies the 2026-09-22 policy;
- the governance-line scan (`AF-004`);
- PR-35 owning review correction, which applies `D13` and PR-30's own body;
- the `flowmaster-validate` wording of `D22`.

### What it does not decide

- **It authorizes only what the plans say.** Where a plan proves incomplete, the part returns to
  PLAN.
- **The Flow Index Alpha-state block (`D18`) is untouched.**
- **The TW ecosystem and the PE Metaprompt are outside `D23-G`.**

### The tested guard (`D14`)

Each ruling gets a registry assertion with an injected must-fail regression, as listed in the
Modification's §P. **Until those land, `D23` is ruled but not applied.**

### Correction, 2026-09-23 — D23-F names the wrong R1 row

Found by the EXECUTE preflight of the plan and confirmed against the bundled oracle
(`flowmaster-validate/references/glow-hde-canonical-change-flow-r1.json`). D23-F above is left as
written (`AUTH-001`); this is its successor.

- **`STOP_SECOND_APPROVAL_OBJECT_REQUESTED` is on GCF-16, not GCF-15.** GCF-15's stop conditions are
  `STOP_PLAN_IDENTITY_MISMATCH or STOP_PO_PROCEED_NOT_INVOKED`.
- **GCF-16 already allows the re-plan.** Its approval contract is "bounded to one Plan; it does not
  authorize … another Plan", and its recovery owner is "remove the invented gate or replan/reinvoke".
  A new Proceed on a new plan is therefore a new traversal, not a second approval object. GCF-16 needs
  no change.
- **The re-plan does change GCF-17.LINEAGE, PR-40's row.** Its `next` rows are GCF-19 and GCF-20
  only, so PR-40 has no R1 transition back to planning. D23-F therefore re-pins **GCF-17.LINEAGE**,
  whose `next` gains GCF-14, and not GCF-15. It is revised in one oracle revision together with
  GCF-17 (D23-D).

This corrects a fact, not a ruling. How the oracle revision is made, whether by a successor oracle
or an in-place re-pin, is a proposal in the Modification's plan amendment and awaits approval.

### Clarification, 2026-09-23 — main-ecosystem prompts are never run as subagents, and nothing creates a session automatically (D23-D, D23-E, D23-F)

**Product Owner, 2026-09-23, in three messages:**
- *"just to be clear, I definitely do not want PR-35 running as a subagent ever"*;
- *"none of these should be subagents … I don't want any automated session creation of any kind in
  the main ecosystem."*;
- *"subagents may be used as workers within task, but the main prompts in the ecosystem must not be
  run as subagents. The exception is the MGMT which is not part of the main ecosystem"*.

**The rule, for the main ecosystem.** That is every GCFPE prompt except `GCFPE-MGMT-10`.
1. **Every prompt runs as its own top-level session.** No prompt is ever run as a subagent, forked
   agent or workflow agent of another session. This covers PR-35 in its own session (D23-D), PR-40
   after the merge (D23-E), and PR-20 for a re-plan (D23-F).
2. **Nothing creates a session automatically.** No session creates, launches or schedules another
   session, by any tool or mechanism. **Nathan creates every session and starts it by pasting the
   handoff.**
3. **A prompt's job ends at the handoff.** It emits a paste-ready `NEXT_PROMPT_HANDOFF` block and
   returns control.

**What it allows.** A session may use subagents as **workers within its own task**. The prompt
itself still runs top-level. Its workers carry out bounded parts of the task under it, and none of
them runs another prompt.

**What it excepts.** `GCFPE-MGMT-10`, the maintenance prompt, is not part of the main ecosystem,
and neither rule binds it. Nor do they bind maintenance work generally, such as preflight readers and
the `D24` skill reviewers. `execution-and-delegation-model.md` governs that work, and it gains a scope
line: its subagents are maintenance workers, and never a way to run a main-ecosystem prompt.

**What it corrects in this record's own wording:**
- **D23-E.** "PR-40 is dispatched" means that the subscribed PR-35 session **emits** the PR-40
  handoff when it observes the merge, and Nathan pastes it into a new session he creates. The
  observed merge event replaces Nathan's merge *assertion*, the fact PR-40 is entered on. It does
  not replace his paste. The subscription wakes the session that made it and creates nothing, so it
  stays.
- **The PART-11 ruling as first recorded.** It said "dispatch is a paste, or a session launch where
  the surface provides one", and the plan's C-DISPATCH repeated it. The launch option is withdrawn.
  Dispatch is a paste.

**Guard.** The Modification's plan amendment carries this into:
- the canonical wording, including C-TOP, which goes into every main-ecosystem body;
- the R1 row;
- PR-35's role in the graph, the contract and the registry;
- the skills.

Each surface gets a guard with an injected must-fail regression (`D14`). That includes a guard on
every main-ecosystem row against running a prompt as a subagent or creating a session. It is scoped
so that it does not forbid workers. PR-20's and PR-40's roles are unchanged: body-level C-TOP and its
guards carry the rule for them.

### Successor, 2026-09-23 — Amendment 1 approved

**Product Owner, 2026-09-23:** *"yes"*, approving Amendment 1 of
`MODIFICATION-20260923-alpha-feedback-open-entries` as written, with the follow-up's plan. That
approval also covers his reading of the A1-7 routing diff: `fecc319bdd4ce7ee6201cb77d7231861`, 284
rows, 229 edges.

**What it adds to D23:**
- **D23-D and D23-F.** The R1 oracle gets a successor, not an in-place edit. Three rows change:
  GCF-17, GCF-17.LINEAGE and GCF-14 (A1-1).
- **D23-E.** The observed-merge route is `MERGE_OBSERVED`, from PR-35 and from RS-40, handed to
  PR-40 by paste. The parenthetical above is corrected: `direct_PR35_to_PR40_automatic_edge` stays
  `false`, and the new edges are recorded in `observed_merge_edges`. Nathan's merge assertion stays
  as the fallback, only where no `MERGE_OBSERVED` result was returned for the merge (A1-5).
- **D23-G.** 091426.1's bodies are edited in place, and their release header lines go now. C-VERSION's
  successor-page rule applies from the next release (A1-3).
- **The rule on subagents and session creation.** It is carried into every main-ecosystem body by
  C-TOP (A1-8).

### Successor, 2026-09-23 — the triage prompt is also outside the main ecosystem

**Product Owner, 2026-09-23:** *"the triage prompt can also run as subagent"*.

*Modification Intake and Triage* is a maintenance prompt, like `GCFPE-MGMT-10`. The clarification
above excepts `GCFPE-MGMT-10`, and this adds the triage prompt, so neither rule in that clarification
binds it: it may run as a subagent.

The triage prompt is not one of the 55 registry members, so no C-TOP guard applies to it and nothing
in Amendment 1 changes.

### Successor, 2026-09-23 — PR-40 is entered once per merge (D23-E)

**Product Owner, 2026-09-23:** *"ok"*. He approved a sentence that the §10 review round a1 proposed.
Both reviewers found the same double-dispatch window.

C-DISPATCH gains one sentence:

> PR-40 is entered once per merge: paste the `MERGE_OBSERVED` handoff when one arrives, otherwise
> the fallback block. Once either has been pasted, the other is void.

## D24 — The independent skill review is run by reviewer subagents; Nathan installs approved packages

**Product Owner, 2026-09-23:** *"It would be ideal if you could use sub agents to do the skill
reviews, then just give me the approved skills to install before promotion"*, then *"make it the
standing rule."*

### What changes

Until now, Nathan carried a reviewer prompt from the authoring session to a separate review session,
and carried the verdict back. From now on:

- **The authoring session runs the independent §10 review itself**, by spawning reviewer subagents.
- **Nathan receives only approved packages**, each with its digest and its verdicts, and installs
  them.

### What keeps the review independent

The review must still be done by a party that did not author the change (standing rule,
2026-09-21). A reviewer subagent qualifies only if all of these hold:

1. **Fresh context.** It is a new agent with no access to the authoring conversation — never a
   forked or context-inheriting agent.
2. **A brief on record.** Its only brief is the canonical `reviewer-prompt-template.md`, filled and
   committed under `docs/ephemeral/` *before* the reviewer is spawned, so the brief cannot be
   tailored out of sight.
3. **Primary evidence.** It works from the packages and the repository, not from the author's
   summary. It reproduces the baseline and the digests before it reviews.
4. **Its own record.** It writes its verdict to its own record file (`SECTION-10-REVIEW-<round>-<id>.md`),
   and the author never edits it (`AUTH-001`).
5. **Two reviewers.** At least two, each independent of the other. A package is approved only when
   both return `SKILL_FIT_CONFIRMED` against the same digests. Any `SKILL_REPAIR_REQUIRED` finding
   is repaired and re-reviewed by fresh reviewers on the new bytes.
6. **Scoped to bytes.** A verdict covers exact bytes and does not carry, as before.

### What does not change

- Nathan alone installs, and the post-install digest comparison is still mandatory.
- The freeze rule still holds: nothing is installed while a review runs.
- The verdict vocabulary is unchanged.
- A handover still identifies each `.skill` by its digest.

### The tested guard (`D14`)

None is mechanical. **A delivery is incomplete unless it carries** the committed brief and two
verdict files, each bound to the delivered digests. That is checked by reading the delivery, and
this entry says so rather than implying a guard exists.
