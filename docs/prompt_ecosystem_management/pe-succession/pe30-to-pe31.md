---
artifact_type: PROMPT_ENGINEER_SESSION_SUCCESSION_RECORD
artifact_version: "1.3"
created_date: 2026-09-18
status: BINDING
predecessor: PE30
successor: PE31
authority: Product Owner instruction, 2026-09-18
baseline: main @ 3c0b1fa (PR #415, squash-merged)
---

# PE30 → PE31 succession record

| | |
|---|---|
| Predecessor | **PE30** — `session_01VVXpW6iAbd6nHUcWWW6A7i` — **RETIRED 2026-09-18** |
| Successor | **PE31** — `session_0141Xnieh5hNkutjFgZaM3WS` — initialized 2026-09-18 |
| Initialized from | branch `docs/20260918-pe31-transition`, which carries this record |

PE30's transcript is not a system of record and is not available to PE31 by design.
Everything load-bearing is in this directory.

PE30 is retired. This is PE31's working context. It is written so that PE31 never needs
PE30's transcript: everything load-bearing is here or at a path named here.

**Read this with `authoritative-surfaces.md` and `gcfpe.decision-record.md`. Those three
documents are the whole inheritance.** Then `execution-and-delegation-model.md` before
delegating anything, and `ecosystem-change-management.md` before proposing any change — it
carries the defect-class catalogue that makes most findings recognisable on sight rather
than re-derived.

## Who PE31 is

The Prompt Engineer session for the Glow GCFPE prompt ecosystem. Nathan is Product
Owner. PE31 is the **coordinator, integrator and decision owner** — it defines governing
rules, assigns bounded scopes, reconciles contradictions, integrates results, protects
settled architecture, and decides when Product Owner input is genuinely needed. It
delegates heavy work rather than performing it personally. See
`execution-and-delegation-model.md`.

## What the project is for

Fifty-five GCFPE prompts, resident in Notion, are being repaired so they **fulfil their
contracts with the least possible friction, ambiguity, and opportunity for an agent to
block on process machinery instead of doing the work.** The system is optimized for
deterministic AI execution and increasing automation. Every decision is measured against
that standard.

## Baseline

| | |
|---|---|
| Candidate under repair | `GCFPE-20260914.1` / `091426.1` / **55 prompts**, `UNSELECTED_CANDIDATE` |
| Selected (live) release | `GCFPE-20260913.1` / `091326.2` / 54 — **never modified** |
| Repository | `main` @ `3c0b1fa` — PR #415 squash-merged; all nine branch commits landed |
| Graph proof token | `55 nodes · 227 edges · 55 state_routes · 571,513 bytes · sha256 d7832c73…` |

## Settled — do not reopen without new evidence

These are Product Owner rulings. Full text and consequences in `gcfpe.decision-record.md`
(D1–D10). Summarised so PE31 can recognise a violation on sight:

1. **Repository-first storage.** The repository is the persistent storage and versioning
   authority. Notion is the operational/indexing layer. **Drive is not a storage
   authority for this ecosystem at all.** One conditional sentence survives: a file goes
   to Drive only where Nathan directs that specific file.
2. **Persistent ecosystem-management material lives in the repository**, at
   `docs/prompt_ecosystem_management/` — the fourth open path.
3. **Derived output is never committed.** The assembled graph is built on demand and
   represented by its proof token.
4. **The PF10 Build Notes Addendum drainage lifecycle is retired from prompt behaviour
   entirely** — no drain step, gate, status, verification, or inference, and **no
   replacement check**.
5. **Current PF10 is the execution authority.** A later prompt reads it as part of its
   normal job. A historical PF10 read is retained **only as provenance where required —
   evidence, never an execution gate.**
6. **Legitimate PF Canon destination handling is preserved**, especially **PF09 rows**
   identifying where an approved change must land in Canon, plus canon-conflict and ADR
   records, `NEW_CANON`, `CANON_RECONCILIATION`, and the permanent Canon drainage target
   and owner. **Interpret by function, never by the word "drain".**
7. **Approved bases are immutable**; an approved delta is an overlay within its explicit
   scope.
8. **Only `CF-C-30`, `CF-E-30`, `IA-30`, `QA-70`, `RS-20`, `ESC-40`** may emit a PF10
   addendum, and only for a qualifying material approved delta to an already-approved
   base. It is drafted paste-ready; Nathan pastes and numbers it; from the next turn it
   is in force and no agent tracks, verifies, confirms, gates on, or asks about it.
9. **No duplicate metadata** where the Project Prompt Contract Registry already carries
   the governed fact. This is why the `PF10 addendum role` token was removed.
10. **Obsolete transition machinery is eliminated** wherever it makes an agent block on
    work that is already done.

**Standing constraints.** Nathan alone merges — a session never merges and never enables
auto-merge. The selected release is never touched. Anything mentioning `HDE-EPIC040` is
left untouched. `docs/pfcanon/` is read-only. Prompts are authored in Notion in place and
never mirrored into the repository. No repository write outside the four open paths
unless Nathan instructed that specific change in conversation.

## Completed and merged

- **Cross-cutting drainage removal.** 142 passage families / 280 occurrences rewritten
  across 54 of 55 prompts; `IA-60` carried only the D4 token. **Verified: 55 of 55 read
  back byte-identical to intent**, zero retired markers surviving, all 74 legitimate
  canon-drainage occurrences preserved, no prompt-ID or routing target lost, no new
  controlled token introduced. Report: `docs/ephemeral/gcfpe.drainage-removal.repair-report.md`.
- **D4 applied**: `PF10 addendum role` removed from all 55 bodies and all 55 graph nodes;
  `role_vocabulary` removed from the graph addendum contract.
- **`CL-20` renamed** to `CL-20 — Prepare Closure Memo and Post-Closure Record`,
  producing `CLOSURE_MEMO` and `POST_CLOSURE_RECORD`; all 13 title references, the page
  title, the Flow Index and the registry updated.
- **Graph contract**: `NATHAN_MANUAL_PF10_DRAIN` and its 10 transitions removed;
  producers route their qualifying approval directly to the receiver. The long-standing
  `RS-40.drain_verified` orphan route is closed. 236 → 227 edges.
- **Registry approved and current**: all 55 `evidence_contract` byte counts and SHA-256
  refreshed against the repaired bodies, in a convention proved against the pre-repair
  evidence first.
- **CI repaired.** The lane classifier did not know the documentation paths `ci.yml`
  ignores and killed every run at the sort step; the direct-DB contract scan read
  governance documents as source. Both now recognise the four documentation paths.
- **Skills edited but NOT published** — `glow-write-boundary` and `glow-artifact-storage`
  were updated for the fourth open path and the no-Drive-authority rule, but the edit
  reached PE30's container only and the sync is one-way. **Your copies are the old ones.**
  Stale `glow-write-boundary` does not know `docs/prompt_ecosystem_management/` and will
  treat writes to your own governing documents as forbidden. Nathan installs the updated
  skills in the Claude workspace; it is not a repository change and no session can do it.
  What the skills must say is governed by D7 and `authoritative-surfaces.md`.

## Obsolete — do not carry forward

- **Batch 2's `BATCH_2_BLOCKED` status.** Its blocker was Drive's lack of content-write
  for an existing file ID. The graph is no longer a Drive file. The blocker is dead (D10).
- **The four-state drain machine** and its interim one-check replacement (D8).
- **`docs/ephemeral/gcfpe.r20260914-1.graph-contract.md`** — deleted 2026-09-18. It was a
  committed copy of derived output that had drifted from its source and still carried the
  full retired machine.
- **`docs/ephemeral/gcfpe.plan.repair-checklist.md`** — a 2026-09-16 export, now labelled
  superseded. The Notion page is the authority.

## The release-scope trap — read this before editing any shared surface

The candidate `091426.1` has the drainage lifecycle **retired**. The selected release
`091326.2` **still has it, correctly**, because the repair has not been applied there and
that release is live.

Several workspace-level Notion surfaces — the Glow Operations Hub above all — carry
blocks for **both**. A block headed *"Current selection — GCFPE-20260913.1 / 091326.2"*
that describes `READY_FOR_MANUAL_DRAIN` and Drive storage is **correct as written for
that release and must not be edited**. Editing it would misrepresent the live system.

So: before "fixing" a drainage or Drive reference on a shared page, find its nearest
heading and establish which release it is scoped to. Only candidate-scoped and
ecosystem-wide text is in scope. When a surface serves both, the right move is to label
the scope rather than rewrite the block — which is what was done on the Operations Hub.

## Notion reconciliation performed 2026-09-18

| Surface | What changed |
|---|---|
| **PE Metaprompt** `3db4590a05eb8174be35d9e35acb3f77` | The generative authoring control. Four-state drain table deleted; addendum schema replaced with the paste-ready canonical format; PFCanon repointed from Drive to `docs/pfcanon/`; runtime artifacts repointed to `docs/ephemeral/`; pre-drain label, drain gate and "Nathan drains PF10" removed. |
| **Glow Operations Hub** `3ce4590a05eb814f8892f88ff8539308` | The canonical addendum format lives here. The struck one-check block removed; "PF10 drainage" removed from the worker output standard; an explicit release-scope note added distinguishing candidate from selected. |
| **Five family hubs** (Change Flow, IA, QA, Escalation, TW) | 14 edits. The shared drain gate on overlays replaced with the in-force-from-next-turn rule; Drive runtime store repointed to `docs/ephemeral/`; RS-40's verified-drain eligibility gate removed; CL-20 renamed; the CL lane's "post-closure drainage" purpose restated. |
| **Flow Index**, **Complete Prompt Set**, **Six-Batch Plan**, **Alpha Checklist**, **Repair Completion Checklist** | Reconciled in the same pass — see `reconciliation-backlog.md` for the finding list each was worked from. |

`reconciliation-backlog.md` in this directory holds the full audit output. Anything not
yet closed is listed there, so it is actionable rather than conversational.

## Remaining work, in priority order

**1. Drive → repository storage pass — DONE 2026-09-18.** 333 passages rewritten across
44 of 55 prompts; verified 44/44 by isolated readback; registry evidence recomputed for
all 44 from live captures. Report:
`docs/ephemeral/gcfpe.storage-pass.repair-report.md`. The coordinator decisions taken
under D7 (retiring `EPHEMERAL_DRIVE`, narrowing the `QA-10`/`QA-50` repository-authority
prohibitions) are recorded in `gcfpe.decision-record.md` under D7.

> Two scope figures in this record were wrong and are superseded by the report: PFCanon
> resolution through Drive was **42** prompts, not 39, and the surface was **333**
> occurrences, not 310. Both were pattern-derived. A first discovery pass in the
> executing session repeated the same mistake and undercounted by 97 lines before two
> workers caught it.

**2. Batch 2 — CLOSED 2026-09-18.** Product Owner authorised closure after a bounded
current-state verification. All 22 original contract findings had already closed on the
prompt side with no prompt edit required; the batch was held only because a graph
synchronisation could not be written to Drive. Every one of those redlines was verified
present in `docs/graph/parts/`. Four clause corrections were applied at closure (IA-20 ×2,
IA-50, IA-60), each with an established downstream consumer. `rollback` was deliberately
**not** added to IA-10: no prompt in the release requires it, so it would be normalisation
without functional purpose. Recorded on the six-batch plan page.

> **Do not reuse the Drive blocker to frame current decisions.** It is obsolete because
> this ecosystem no longer uses Drive, not because Drive became writable. Verified
> 2026-09-18: 0 of 55 bodies and 0 of 55 graph parts reference Drive as a store or
> authority, and no CI, tool or script has a Drive code path.

**3. The consolidated pass — Batches 3–6 are RETIRED (D12, 2026-09-18).** The Product
Owner approved replacing the remaining batch sequence with **one consolidated pass over the
37 remaining prompts plus one release-wide gate**. Four lanes run concurrently; findings
reconcile centrally; anything cross-cutting is decided once and applied uniformly. The gate
is a single corpus-wide verification: graph rebuild and closure, registry validator,
interface closure across all 55, isolated readback of everything changed.

> Do not execute Batches 3–6 as written. The Notion six-batch plan retains them as the
> historical record and the source of the finding lists; its Batch 3–6 sections are marked
> **superseded**. Mechanics: `execution-and-delegation-model.md` §0A. Lessons that bind the
> pass: §0B. Ruling: `gcfpe.decision-record.md` D12.

> **The consolidated pass ran and its gate passed on 2026-09-18.** 37 prompts in four
> concurrent lanes; 62 findings, all quotes machine-verified, none carried forward, no Product
> Owner decision required. 33 registry rows regenerated from the graph (D13); three body
> repairs applied and verified by isolated readback — `RS-40` (retired PF10 gate reinstated by
> function), `QA-10` (off-repository storage), `OPS-20` (stale prompt reference). Guards added
> and proved against eight injected regressions; assertions 499 → 721 (D14). Report:
> `docs/ephemeral/gcfpe.consolidated-pass.repair-report.md`.

**4. Then**: the dedicated workflow-skill review, the independent post-flight, and the
Product Owner promotion decision packet. **One Product Owner gate remains** — approving
promotion. The pass authorization was given and used on 2026-09-18.

**5. Nothing outstanding on the graph.** The proof token was reproduced at the gate by
`scripts/graph_parts.py build docs/graph/parts`, which ships with the `glow-graph-contract`
skill: `55 nodes · 227 edges · 55 state_routes · 571,513 bytes · sha256 d7832c73…`, validation
PASS, no orphan-route warning. **Before assuming a tool is missing, read
`authoritative-surfaces.md` and the skill list — reusable behaviour lives in skills, data lives
in the repository, and that is the design.**

## Known risks

- **A stale mirror is more dangerous than a missing document.** The committed assembled
  graph would have handed a future session the entire retired machine back. Prefer a
  proof token over a stored copy; label any snapshot that must be kept.
- **Lexical sweeps destroy legitimate Canon handling.** "Drain" names two unrelated
  concepts. Every pass must classify by function. This has been got wrong once already.
- **Heuristic scoping under-counts.** The drainage surface was first measured at 93
  families by a heuristic; reading every occurrence in context gave 142. Measure by
  reading, not by pattern, before reporting a scope figure.
- **A worker that can see the expected answer cannot verify it.** See §7 of
  `execution-and-delegation-model.md`.
- **Comparing captures to captures proves nothing.** 25 of 55 approved `evidence_contract`
  entries did not reproduce from the live Notion page — 24 by a trailing newline the page does
  not contain, and `ESC-40` by an 841-byte paragraph the live page has never had. The earlier
  check compared stored captures against each other and passed. **Always compare to the live
  page, and record the extraction convention in the evidence itself.**
- **A ruling with no guard is a one-time verification.** The thirteen retired drainage tokens
  had no registry assertion at all until 2026-09-18. See D14.
- **A retired behaviour comes back in different words.** `RS-40` rebuilt the PF10 drainage gate
  out of ordinary language and passed every token sweep. Test the function. See D14, FUNC-001.
- **A worker that retypes evidence corrupts it.** In the storage pass a readback worker
  silently flattened curly quotes to ASCII in three captures, and the pre-edit fetch
  corpus turned out to have dropped a whole line from two prompts and altered a sentence
  in a third. Live Notion was correct in every case. Where byte fidelity matters,
  extraction must be **programmatic by an exact documented slice**, never retyped, and
  compared by bytes rather than by a worker's report.
- **The local git remote-tracking ref goes stale in this container.** `git push` succeeds
  and the remote updates, but `refs/remotes/origin/...` does not advance, so the stop hook
  reports phantom unpushed commits. Check `git ls-remote` before believing it.

## Genuinely open — needs Product Owner input

- **Nothing is currently blocking.** The storage pass is complete (2026-09-18).
- **Deferred, not blocking:** a 13.6 MB evidence manifest in `docs/ephemeral/` embeds
  whole Python sources and PF Canon documents as escaped strings. Whether an artifact of
  that shape belongs in the ephemeral store is a storage-architecture question Nathan has
  not been asked.

**Investigated and closed, not open.** `audit/docdeltas/` holds 49 PF-named files
(`PF10_EPIC017_addendum.md`, `PF12_EPIC017_registry_and_mirror.md` and similar). An
earlier revision of this record listed them as a canon hazard needing a Product Owner
ruling. They are not. They are application-side doc-delta staging from HDE epic delivery,
committed 2026-08-25, each carrying a `path_proof.txt`, and they are referenced by
`README.md` as evidence anchors and by QA step reports as a D10 gate check. Removing or
moving them would break live evidence for no gain. The residual risk is only a **name
collision**, and `QA-10` §55 and `QA-50` §29 already close it by making any repository
file outside `docs/pfcanon/` a non-authority. That is why those prohibitions were
narrowed rather than deleted.

## Warnings against reintroducing superseded behaviour

Treat each of these as a defect on sight, wherever it appears — prompt body, graph part,
plan, checklist, report or Notion page:

`DRAIN_VERIFIED` · `MANUAL_DRAIN_REQUIRED` · `MANUAL_DRAIN_MISMATCH` ·
`READY_FOR_MANUAL_DRAIN` · `NON_CANONICAL_PENDING_MANUAL_DRAIN` · `drain_owner` ·
`drain_verification_anchor` · `PRE_DRAIN_BASELINE_EVIDENCE` ·
`pf10_reference_visibility_check` · `PF10_REFERENCE_VISIBILITY` ·
`NATHAN_MANUAL_PF10_DRAIN` · `pf10_addendum_role` · `POST_CLOSURE_DRAINAGE_STATUS` ·
the old `CL-20` title · a mandatory post-addendum confirmation check · any gate on an
addendum transition state · `Glow / Ephemeral Planning Files` as a destination · a
required direct Drive link · PFCanon resolved from Drive.

**And the converse, equally important:** never delete a PF09 row, a canon-conflict or ADR
record, a `NEW_CANON` or `CANON_RECONCILIATION` classification, or a permanent Canon
drainage target and owner. Those are legitimate Canon disposition and must survive.

## PE31's first actions, in order

1. **Read three documents and nothing else to orient**: this record,
   `authoritative-surfaces.md`, `gcfpe.decision-record.md`. Then
   `execution-and-delegation-model.md` before delegating anything.
2. **Close out `reconciliation-backlog.md`.** Most of it was applied on 2026-09-18; what
   remains is listed there. Re-run the same two isolated audits to confirm, rather than
   trusting this record.
3. ~~**Run the Drive → repository storage pass**~~ — **DONE 2026-09-18.** 333 passages,
   44 prompts, verified 44/44 by isolated readback.
4. ~~**Verify Batch 2 and close it**~~ — **CLOSED 2026-09-18.**
5. ~~**Batch 3**, then 4–6~~ — **RETIRED by D12.** Run the consolidated pass and the single
   release-wide gate instead. See item 3 of *Remaining work* above.

## How to report to Nathan

Binding, and load `glow-po-reporting` before writing to him. Added 2026-09-18 after a
session in which the work was sound and the reporting was not, which cost the Product
Owner more time than the work saved.

**Asking for a decision.** Give four things in order: what the thing actually does in
plain language; what concretely breaks in a real run if nothing changes; the options with
their costs; your recommendation and why. A schema difference is not an impact. If you
cannot say what the affected prompt does, you are not ready to ask — find out first.

Several decisions get a summary table (number, question, impact, recommendation), then
one section per decision in the same shape, ordered by impact.

**Ask only for what is genuinely his.** Policy, settled architecture, and expensive or
hard-to-reverse calls are Nathan's. An implementation consequence of a ruling he has
already made is yours — make it, say you made it, give the reason. Seeking cover on a
judgement you are equipped to make costs him two rounds.

**Corrections lead.** When you are correcting something you told him earlier, it is the
headline, at the top, before the new work. Never buried mid-paragraph, never surfacing
only as a changed number. What you said, what is true, what changes as a result.

**One structure per message.** Do not stack analyses with different shapes. If you have
several unrelated things, send the actionable one and say the rest is coming.

**"For the record" means a file or page was written.** Conversation is not a record —
this document says so about transcripts, and it applies to your own claims too. Record it
and name the path, or call it an observation.

**Establish behaviour before proposing a change.** Never propose an edit on the strength
of a rule, an assertion, or a filename. This ecosystem's recurring failure is judging by
name instead of function — "drain", "Drive", `PF10_*`, a required literal. A check that
fails on every member of a set is telling you about the check.

**Reporting completed work.** Lead with what changed and whether it is verified, then the
evidence, then what is left. Name paths, branches and PRs. Numbers beat adjectives.

## How to work

Coordinate; do not personally grind. Precompute discovery so coverage is arithmetic
rather than trust, hand each agent an exact scope and the settled rules, require a
structured return, and validate every return centrally. Isolate any agent whose output
will be checked against an expectation from that expectation.

Measure every decision against one standard: **does this make the ecosystem simpler,
more deterministic, more automatable, and less likely to stop an agent from completing
legitimate work?**

Ask Nathan only when proceeding under any assumption would be unsafe or would waste the
work if wrong. He has been explicit that settled rules should not come back for repeated
approval.
