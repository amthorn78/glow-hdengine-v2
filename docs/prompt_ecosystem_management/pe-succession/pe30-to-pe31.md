---
artifact_type: PROMPT_ENGINEER_SESSION_SUCCESSION_RECORD
artifact_version: "1.0"
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
documents are the whole inheritance.**

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
| Graph proof token | `55 nodes · 227 edges · 55 state_routes · 571,493 bytes · sha256 3b54d620…` |

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

**1. Drive → repository storage pass.** One controlled cross-cutting pass, not
batch-local. Measured against the live bodies: **44 of 55 prompts** still name
`Glow / Ephemeral Planning Files` or a direct Drive link as the artifact destination;
**39 of 55** still resolve PFCanon by walking `Glow / Core Docs / PFCanon` in Drive.
Three carry both. 145 passage families / 310 occurrences; roughly 124 families resolve by
deterministic substitution, ~21 need authoring. **The 11 Batch 1 prompts are already
converted and are the wording to converge on** — repository paths throughout, keeping the
single conditional Drive sentence. Do not invent new phrasing.

**2. Batch 2 bounded current-state verification.** Not a re-run. Answer three questions
against the merged bodies: is the recorded blocker obsolete (it is — D10); are there
remaining actual defects under current rules; do its seven prompts (`IA-10`, `IA-20`,
`IA-30`, `IA-40`, `IA-50`, `IA-60`, `UTIL-10`) fulfil their contracts. If clean, close it.
Do not manufacture work because it was historically marked blocked. **Sequence after the
storage pass**, because all seven prompts are in that pass and verifying first would
certify bodies about to change.

**3. Batch 3**, then Batches 4–6 per the Notion plan.

**4. Later**: the dedicated workflow-skill review after Batch 6, then the independent
post-flight, then the Product Owner promotion decision packet.

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
- **The local git remote-tracking ref goes stale in this container.** `git push` succeeds
  and the remote updates, but `refs/remotes/origin/...` does not advance, so the stop hook
  reports phantom unpushed commits. Check `git ls-remote` before believing it.

## Genuinely open — needs Product Owner input

- **Nothing is currently blocking.** The storage pass is settled in principle (D7) and
  needs no further ruling to execute.
- **Deferred, not blocking:** a 13.6 MB evidence manifest in `docs/ephemeral/` embeds
  whole Python sources and PF Canon documents as escaped strings. It is excluded from the
  contract scan now, but whether an artifact of that shape belongs in the ephemeral store
  at all is a storage-architecture question Nathan has not been asked.

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
3. **Run the Drive → repository storage pass** across the 44 + 39 prompts. One
   controlled cross-cutting pass. Converge on the Batch 1 wording; do not invent new
   phrasing. Verify by isolated readback, comparing centrally.
4. **Verify Batch 2 against the merged bodies** and close it if clean.
5. **Batch 3**, then 4–6.

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
