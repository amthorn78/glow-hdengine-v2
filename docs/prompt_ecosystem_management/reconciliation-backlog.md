---
artifact_type: PROMPT_ECOSYSTEM_RECONCILIATION_BACKLOG
artifact_version: "1.0"
created_date: 2026-09-18
status: LARGELY_CLOSED_2026-09-18
baseline: main @ 3c0b1fa (PR #415)
method: two isolated read-only audits against the settled rulings in gcfpe.decision-record.md
---

# Reconciliation backlog — documents that still present retired behaviour as active

> ## Closure status — 2026-09-18
>
> **Notion: reconciled.** 51 verified edits across ten surfaces. The two generative
> controls were done first and re-verified under isolation: the **PE Metaprompt** now
> returns **zero** retired or Drive-storage markers; the **Glow Operations Hub** retains
> only release-scoped and historical hits, which are correct, plus Drive links belonging
> to other Glow workstreams (the Drive map, HD Refs, Readings Authority, CRD list) that
> are outside this ecosystem's scope.
>
> **Repository: reconciled.** The committed assembled graph was deleted, the
> direct-handoff control copy superseded, the D6/D8 contradiction fixed, eight dated
> batch records banner-marked, and the machine-readable residues corrected.
>
> **Deliberately left for a ruling, not oversights:**
> - The Hub's `## Current selection — GCFPE-20260913.1 / 091326.2` blocks describe the
>   **selected** release, which still has the drainage lifecycle. Correct as written.
> - The Alpha checklist's `GCFPE-19` obligation contains *"without editing or draining
>   it"* — an open Product Owner obligation, not a negative-authority list entry.
> - The six-batch plan's `status` / `mutation_performed` front matter is a Product Owner
>   call about which phase the project is in.
> - A handful of `PF10 drainage` entries in negative-authority lists on historical
>   checklists — stale but inert, and on pages already marked superseded.


Audited 2026-09-18 against the merged baseline. Every finding below is a place where a
reader or a validator would take retired behaviour as current instruction.

**Severity ordering used here:** a *generative* control is worst, because anything
authored from it reacquires the retired machine. A *validator input* is next. A *live
checklist* is next. A dated record that merely reports what was true then is not a defect
and is excluded.

## The two generative controls — highest priority

These do not merely describe the retired lifecycle; they would rebuild it.

| Surface | Why it is generative |
|---|---|
| **PE Metaprompt 091426.1** (Notion) | The prompt-authoring control. It carries a full normative table of the four-state drain machine, mandates the retired addendum fields, names Drive as the PFCanon authority and **explicitly forbids the repository**. Any prompt authored from it reacquires all of it. |
| **Glow Operations Hub** (Notion) | Holds the canonical PF10 build-notes addendum format and the workspace operating policy. Still carries the struck one-check block, the manual drain as a live boundary step, and Drive as the artifact home. |

## Repository findings


### `docs/ephemeral/gcfpe.batch-1.contract-ledger.md`

- **CONTRADICTS_SETTLED** (line 422) — §11.1 states the interim mandatory confirmation check as the Product Owner's standing specification; that check is struck.  
  *Fix:* Mark §11.1 superseded and state that no post-addendum check survives.
- **CONTRADICTS_SETTLED** (line 432) — Records a retired token (`pf10_reference_visibility_check`) as the CLOSED current graph contract; global.json no longer contains it.  
  *Fix:* Add a superseded note to the B1-PAP-05/06 rows pointing at the drainage-removal repair report.
- **CONTRADICTS_SETTLED** (line 433) — Presents the retired `PF10_REFERENCE_VISIBILITY` vocabulary as the live replacement; it is gone from the graph.  
  *Fix:* Same superseded note; the vocabulary was removed with the check.

### `docs/ephemeral/gcfpe.batch-1.copy-repair-ledger.md`

- **CONTRADICTS_SETTLED** (line 250) — Fourth-pass record states the retired replacement check and vocabulary as the delivered global.json state.  
  *Fix:* Add a superseded note that both were later removed outright.

### `docs/ephemeral/gcfpe.batch-1.repair-report.md`

- **CONTRADICTS_SETTLED** (line 288) — States two retired tokens as the current graph contract; neither exists in docs/graph/parts/global.json at the merged baseline.  
  *Fix:* Add an in-place superseded note: both were removed when the mandatory check was struck.
- **CONTRADICTS_SETTLED** (line 281) — Presents the interim replacement check as the standing rule; no post-addendum check survives.  
  *Fix:* Mark the paragraph superseded and point at the drainage-removal repair report.

### `docs/ephemeral/gcfpe.batch-1.validation-report.md`

- **CONTRADICTS_SETTLED** (line 289) — Records the four drain-verification anchor fields as a MET criterion for the current addendum contract; they are retired and forbidden.  
  *Fix:* Mark Criterion 4's evidence superseded by the drainage-removal repair.

### `docs/ephemeral/gcfpe.batch-2.contract-ledger.md`

- **CONTRADICTS_SETTLED** (line 137) — Pre-edit tabletop cases are re-run before a final disposition, so E5 is a forward acceptance criterion requiring retired states.  
  *Fix:* Retire cases E2/E4/E5 or restate them without drain states.
- **CONTRADICTS_SETTLED** (line 134) — Same: a forward-looking expected result that requires the retired manual-drain terminal.  
  *Fix:* Restate as: exactly one paste-ready addendum; base unchanged.
- **CONTRADICTS_SETTLED** (line 89) — 'Expected repair' reads as a current instruction to build the retired drain terminal into IA-30.  
  *Fix:* Strike the manual-drain clause from the expected repair; the rest stands.

### `docs/ephemeral/gcfpe.batch-2.repair-report.md`

- **CONTRADICTS_SETTLED** (line 338) — §7 is presented as an exact redline still to be applied; applying R30 would reinstate the removed NATHAN_MANUAL_PF10_DRAIN node.  
  *Fix:* Mark §7 as a superseded computation, not an applicable redline.
- **CONTRADICTS_SETTLED** (line 438) — R50 and R51 (line 443) write boundary transitions for a node the merged graph no longer has; applying them rebuilds the retired machine.  
  *Fix:* Same: mark §7 superseded, and state that producers now route approvals directly to the receiver.
- **CONTRADICTS_SETTLED** (line 141) — Tabletop case G records the retired four-state machine as a PASS criterion for IA-30's current contract.  
  *Fix:* Mark case G superseded; the drainage branches no longer exist in IA-30.

### `docs/ephemeral/gcfpe.r20260914-1.handoff-control.md`

- **CONTRADICTS_SETTLED** (line 53) — States four retired drainage tokens plus the retired Drive store as the live addendum contract; this is the control copy a validator reads.  
  *Fix:* Rewrite the addendum clause as paste-ready with no status/canonicality/drain_owner/anchor fields and no Drive destination.
- **CONTRADICTS_SETTLED** (line 55) — Reinstates the retired four-state drain-verification machine (SOURCE_RESOLUTION_ERROR / MANUAL_DRAIN_REQUIRED / MANUAL_DRAIN_MISMATCH / DRAIN_VERIFIED) as active behaviour.  
  *Fix:* Delete the whole post-drain verification section; no replacement check.
- **CONTRADICTS_SETTLED** (line 209) — Machine-readable contract block declaring the retired drain-verification state machine as exhaustive and current.  
  *Fix:* Remove the `PF10_drain_verification` block entirely from the machine contract.
- **CONTRADICTS_SETTLED** (line 158) — Machine-readable PF10_overlay block still carries three retired tokens, including the drain_owner that D2 deleted outright.  
  *Fix:* Delete these three keys from `PF10_overlay`.
- **CONTRADICTS_SETTLED** (line 176) — Lists drain_verification_anchor among the addendum's required_fields; the field is retired and is now in forbidden_fields.  
  *Fix:* Remove the anchor entry (and the `status`/`canonicality`/`drain_owner` entries above it) from required_fields.
- **CONTRADICTS_SETTLED** (line 185) — Gates rescope continuation on DRAIN_VERIFIED in all three PR_RETURN_PHASE rows (185-187); RS-40 lost that gate.  
  *Fix:* Strike 'after fresh DRAIN_VERIFIED' from all three rows; continuation resolves current PF10 as its normal job.
- **CONTRADICTS_SETTLED** (line 73) — Describes the retired drain handoff as the live rescope route; the addendum is paste-ready and is in force from the next turn.  
  *Fix:* Replace with: qualifying APPROVE creates one paste-ready addendum; the receiver resolves current PF10.
- **CONTRADICTS_SETTLED** (line 273) — Deterministic fixture catalog rows 273-277 and 281 require the retired drain states as PASS conditions; §296 says the validator must execute these fixtures.  
  *Fix:* Delete PF10-POS-02 and PF10-NEG-02/03/04 and rewrite RS-RETURN-01 without 'after drain'.
- **CONTRADICTS_SETTLED** (line 49) — Section heading presents the manual-drain contract as a live part of the direct-handoff contract.  
  *Fix:* Rename to 'PF10 addendum contract' and keep only the producer set and qualifying predicate.

### `docs/prompt_ecosystem_management/gcfpe.decision-record.md`

- **CONTRADICTS_SETTLED** (line 89) — D6 still mandates a one-turn confirmation check that D8 in the same document strikes; an agent may not track, verify or confirm the paste, and there is no replacement check.  
  *Fix:* Rewrite D6's lifecycle paragraph to match D8: the addendum is in force from the next turn; later prompts simply read current PF10.

### `docs/ephemeral/gcfpe.batch-1.contract-ledger.md`

- **STALE_STATUS** (line 442) — The calibration note reports an open ESCALATE_SHARED_CONTRACT; D2 deleted the requirement and global.json now carries drain_owner only inside forbidden_fields as a guard.  
  *Fix:* Close the escalation in place, citing D2 and the surviving forbidden_fields guard.
- **STALE_STATUS** (line 416) — Defers to later batches work that the cross-cutting drainage removal already completed; neither element exists in global.json.  
  *Fix:* Mark closed by the cross-cutting repair rather than deferred.
- **STALE_STATUS** (line 463) — §11.2 'Known disagreement until Batches 2-5 run' is fully superseded; RS-40's intake states are gone.  
  *Fix:* Mark §11.2 closed by the drainage-removal repair.
- **STALE_STATUS** (line 213) — Records the orphan route as a known, expected, still-standing condition.  
  *Fix:* Note it as closed with the retired machine.

### `docs/ephemeral/gcfpe.batch-1.copy-repair-ledger.md`

- **STALE_STATUS** (line 240) — Defers work the cross-cutting repair already closed; neither element survives in the merged parts.  
  *Fix:* Mark closed by the drainage-removal repair.
- **STALE_STATUS** (line 257) — Superseded proof token and a build warning that no longer occurs.  
  *Fix:* Date-stamp as a 2026-09-17 capture.

### `docs/ephemeral/gcfpe.batch-1.repair-report.md`

- **STALE_STATUS** (line 299) — The cross-cutting drainage removal swept all 55 prompts; no prompt still implements the old machine.  
  *Fix:* Mark superseded: the disagreement was closed outside the batch sequence.
- **STALE_STATUS** (line 302) — The orphan route is closed; the builder no longer emits it.  
  *Fix:* Note that the route disappeared with the machine that declared it.
- **STALE_STATUS** (line 330) — Reports a standing build warning that no longer occurs.  
  *Fix:* Date-stamp §8's build evidence as a 2026-09-17 capture.
- **STALE_STATUS** (line 322) — Superseded by the merged parts' proof token 55 nodes / 227 edges / 55 state_routes.  
  *Fix:* Label it as the 2026-09-17 token and cite the current one.
- **STALE_STATUS** (line 338) — 'is still' reads as current status; the warning is gone.  
  *Fix:* Past-tense and date-stamp it.

### `docs/ephemeral/gcfpe.batch-1.validation-report.md`

- **STALE_STATUS** (line 12) — Batch 1 is closed at BATCH_1_REPAIRED_WITH_CORRECTIONS with blockers 0 and all eight defects closed; this report carries no superseded-by pointer.  
  *Fix:* Add `superseded_by: docs/ephemeral/gcfpe.batch-1.repair-report.md` to the front matter.
- **STALE_STATUS** (line 275) — Presented as a live-graph measurement; the node and all ten of its transitions were removed.  
  *Fix:* Note that delta_approve now routes directly to the receiver the approval names.
- **STALE_STATUS** (line 364) — The RS-40.drain_verified orphan route is closed and the merged parts build to 227 edges; §6 calls this 'the known Batch 3 orphan'.  
  *Fix:* Date-stamp the build block as a 2026-09-17 capture and note the current proof token.

### `docs/ephemeral/gcfpe.batch-2.repair-report.md`

- **STALE_STATUS** (line 8) — Front-matter verdict is the first thing a reader or scanner sees; the blocker it rests on is structurally dead.  
  *Fix:* Re-verdict to a current-state disposition and record the blocker as obsolete.
- **STALE_STATUS** (line 9) — The recorded blocker was 'Drive has no content-write for an existing file ID'; the graph is no longer a Drive file and storage is the repository.  
  *Fix:* Replace with a note that the blocker is obsolete under repository storage.
- **STALE_STATUS** (line 567) — §12's verdict block repeats the dead blocker as the batch's standing state.  
  *Fix:* Supersede §12 in place with the current disposition.
- **STALE_STATUS** (line 575) — Holds Batch 3 on a blocker that no longer exists; the graph is parts in the repository and is rebuilt by script.  
  *Fix:* Strike the hold; Batch 3 sequencing is governed by ordinary authorization.
- **STALE_STATUS** (line 509) — §8 'Smallest required decision' presents an open Product Owner decision about Drive write capability that the storage architecture already resolved.  
  *Fix:* Replace §8 with a note that repository storage removed the decision.
- **STALE_STATUS** (line 519) — §9 disposition table still shows the graph and the control copy BLOCKED on Drive capability.  
  *Fix:* Re-disposition both rows against repository storage.

### `docs/ephemeral/gcfpe.phase2.defect-inventory.md`

- **STALE_STATUS** (line 161) — §7's recommended sequence still opens with a step §6A of the same document records as completed on 2026-09-17.  
  *Fix:* Strike step 1 and renumber, or mark §7 superseded by §6A.
- **STALE_STATUS** (line 166) — Batch 2's prompts were already edited by the cross-cutting drainage removal, and its recorded blocker is dead; the batch now needs a bounded current-state verification, not a first-target run.  
  *Fix:* Restate the recommendation against the merged baseline.
- **STALE_STATUS** (line 139) — All 55 prompts were edited by the cross-cutting drainage repair, which the settled execution decision exempts from adversarial pre-verification.  
  *Fix:* Scope the sentence to batch-local findings, matching the decision record's execution decisions.

### `docs/ephemeral/gcfpe.storage-architecture.md`

- **STALE_STATUS** (line 219) — The Batch 1 repair report records both prior blockers retired, R1 'Retired by closing D4', blockers 0, nothing open.  
  *Fix:* Close R1 here, citing the Batch 1 repair report §1.
- **STALE_STATUS** (line 91) — Line 74 of the same document now says the storage conversion is 'one controlled cross-cutting pass, not batch-local work'; the two statements disagree.  
  *Fix:* Align §'The defect class' and 'Per-batch obligation' with the cross-cutting-pass statement.

### `docs/prompt_ecosystem_management/gcfpe.decision-record.md`

- **STALE_STATUS** (line 107) — D6's consequence does not record the CL-20 rename or its second deliverable POST_CLOSURE_RECORD, which the merged registry and graph part carry.  
  *Fix:* Add that CL-20 is renamed and now produces CLOSURE_MEMO and POST_CLOSURE_RECORD.

### `docs/prompt_ecosystem_management/project-prompt-contract-registry.md`

- **STALE_STATUS** (line 40) — The registry carries 55 prompt entries and all 55 source_snapshots read `completeness: COMPLETE`; the observation block understates by one.  
  *Fix:* Set `complete_body_count: 55`.

### `docs/ephemeral/gcfpe.batch-1.validation-report.md`

- **STALE_REFERENCE** (line 66) — Routing link to a superseded predecessor report in Drive; the current report is docs/ephemeral/gcfpe.batch-1.repair-report.md v7.0.  
  *Fix:* Point at the repository path, keeping the Drive ID only if it is stated as lineage.

### `docs/ephemeral/gcfpe.batch-2.repair-report.md`

- **STALE_REFERENCE** (line 157) — §7 targets a Drive-resident graph file that is no longer the artifact; the graph is per-prompt parts in the repository.  
  *Fix:* Note that the synchronization target moved to docs/graph/parts/ and §7 no longer applies as written.

### `docs/ephemeral/gcfpe.r20260914-1.handoff-control.md`

- **STALE_REFERENCE** (line 107) — Machine-readable store binding names the retired Drive folder; runtime artifacts land in docs/ephemeral/ by pull request.  
  *Fix:* Set `store: docs/ephemeral/` and replace the Drive producer actions with commit/push and repository path.
- **STALE_REFERENCE** (line 206) — Resolves PFCanon through a Drive folder; PFCanon is read from docs/pfcanon/.  
  *Fix:* Point `PFCanon_source` at `docs/pfcanon/`, keeping the Markdown-only rule.
- **STALE_REFERENCE** (line 32) — Binds the graph contract to a Drive file ID as a routing pointer; the graph is held as parts in docs/graph/parts/ and the assembled graph is never committed.  
  *Fix:* Replace the Drive URL and the `graph_contract` path with `docs/graph/parts/` plus the current proof token.
- **STALE_REFERENCE** (line 27) — Points at a pre-merge candidate workspace path that does not exist in the repository, and pins a graph hash superseded by the merged parts.  
  *Fix:* Rebind to docs/graph/parts/ and the current build proof token.
- **STALE_REFERENCE** (line 113) — Required producer action carries a direct Drive link; artifacts are referenced by repository path.  
  *Fix:* Replace with 'commit and push on the working branch; reference by repository path'.
- **STALE_REFERENCE** (line 170) — Addendum required_fields demand direct Drive URLs, including for PF10 addenda; D1 forbids a separately carried URL and Drive is not a storage authority.  
  *Fix:* Reference by canonical name and repository path; drop the Drive URL requirements.
- **STALE_REFERENCE** (line 253) — Alpha preparation gate still routes the handoff to the retired Drive folder.  
  *Fix:* Point it at docs/ephemeral/.

### `docs/ephemeral/gcfpe.storage-architecture.md`

- **STALE_REFERENCE** (line 105) — The table above now lists four open repository paths; `docs/prompt_ecosystem_management/` was added as the fourth.  
  *Fix:* Change 'three open paths' to 'four open paths'.

### `docs/prompt_ecosystem_management/project-prompt-contract-registry.md`

- **STALE_REFERENCE** (line 30) — An authority_source pointing at a pre-merge extraction workspace path that does not exist in the repository, repeated four times (lines 27-35) with no distinguishing note.  
  *Fix:* Collapse to one entry and either resolve the path in-repository or mark it as a pre-merge extraction record.

## Notion findings


### Glow HDE Prompt Flow Index — GCFPE-20260914.1 — 091426.1

`3db4590a05eb81de9736ea69bac61016` — Live navigation and operational-mapping index for the 55-member candidate release; carries the control bindings (catalog, manager, metaprompt, procedure, graph, hubs, Alpha controls) a reader follows to find the authoritative artifact.

- **CONTRADICTS_SETTLED** — Binds the assembled graph as a stored Drive file; the graph is per-prompt parts in docs/graph/parts and the assembled graph is derived output that is never stored or committed.  
  *Fix:* Replace the binding with docs/graph/parts/ and state that the assembled graph is rebuilt by script and never stored.
- **CONTRADICTS_SETTLED** — Names Drive as the storage authority for ephemeral/runtime artifacts; those are authored at docs/ephemeral/ and land by pull request.  
  *Fix:* Repoint to docs/ephemeral/ in amthorn78/glow-hdengine-v2, referenced by repository path.
- **CONTRADICTS_SETTLED** — Names Drive as the PFCanon source authority; PFCanon is read from docs/pfcanon/, read-only, and the Drive folder carries no authority.  
  *Fix:* Resolve PFCanon from docs/pfcanon/ read-only; keep the Markdown-only rule, drop the Drive route.
- **CONTRADICTS_SETTLED** — IA-lane evidence rule routes PF10 and lineage evidence through Drive rather than the repository.  
  *Fix:* Carry PF10 and lineage evidence by repository path; record the PF10 version actually read as provenance.
- **CONTRADICTS_SETTLED** — PR-10/PR-20 row still makes Drive a first-class source for PR work; repository is the source and storage authority.  
  *Fix:* Strike 'Direct Drive sources' and leave repository state inspection.
- **STALE_REFERENCE** — Five of the control bindings (procedure, direct-handoff/fixtures copy, corrected source manifest, candidate validation, behavior fixtures) still resolve to Drive file IDs; the 155-file Drive ephemeral record was imported into docs/ephemeral/.  
  *Fix:* Rebind each control to its docs/ephemeral/ path; keep the Drive IDs only as lineage, clearly labelled non-authoritative.

### GCFPE Expanded Prompt Repair Plan and Six-Batch Checklist — 20260915.1

`3dc4590a05eb81a9adf1d8f800863937` — The live six-batch repair plan and the workspace's most-read operational instruction: scope, storage architecture (4.5), specification-format authority (4.6), addendum posture (4.7), batch membership, per-batch state, and the 2026-09-18 cross-cutting drainage-removal record.

- **CONTRADICTS_SETTLED** — Front-matter key carries the retired `drain_owner` token as a live plan attribute, on the same page that declares the drainage lifecycle retired.  
  *Fix:* Delete the `pf10_drain_owner` key from the YAML header.
- **CONTRADICTS_SETTLED** — Batch 2's recorded blocker is dead: the graph is no longer a Drive file and storage is the repository.  
  *Fix:* Record the blocker as dead under 4.5 and re-state Batch 2's remaining work without it.
- **CONTRADICTS_SETTLED** — Presents a settled decision as open; storage was re-pointed to the repository on 2026-09-17 (4.5 of this same page).  
  *Fix:* Mark the decision closed — repository-first — and cite 4.5.
- **CONTRADICTS_SETTLED** — Batch 3's contract focus still commissions the retired four-state drain schema for RS-40 as future work.  
  *Fix:* Replace with: resumes the recorded phase on the qualifying approval, reading current PF10 as provenance; no intake state machine.
- **CONTRADICTS_SETTLED** — The RS-40.drain_verified orphan route is closed and the builder reports no warning; this section still presents it as standing.  
  *Fix:* Update the Batch 1 graph proof token section to the merged token and 'no warning'.
- **STALE_STATUS** — Graph proof token is 236 edges; the merged baseline rebuilds from parts to 55 nodes / 227 edges / 55 state_routes.  
  *Fix:* Restate as 55 nodes · 227 edges · 55 state_routes (sha256 cb9286cd…), or label the 236 token as a dated Batch 1 measurement.
- **STALE_STATUS** — Present tense claim in 6B and 'Carried to the owning batches'; RS-40's drain implementation and its orphan route are gone as of the cross-cutting removal.  
  *Fix:* Rewrite in past tense and point at the 2026-09-18 drainage-removal section, or delete the carried-work row.
- **STALE_STATUS** — The 'Also now stale' note is itself stale: the page's Batch 6 heading now reads 'post-closure record' and those checklist items no longer appear.  
  *Fix:* Delete the 'Also now stale' paragraph or re-scope it to whatever actually remains.
- **STALE_STATUS** — Header state contradicts 13 Execution, which records Batch 1 complete (`BATCH_1_REPAIRED`, PRs #409/#410) and 55 prompt bodies edited.  
  *Fix:* Advance `status` to the current phase and set `mutation_performed: true`.
- **STALE_STATUS** — Repository/PR work is now the required landing path for every batch artifact (4.4, 6A, PRs #409-#411), and PF10 drainage no longer exists as an action.  
  *Fix:* Remove 'PF10 drainage' and carve repository/PR work out of the withheld list.
- **STALE_REFERENCE** — Batch 2's record is still addressed by Drive file ID although the 155-file Drive ephemeral folder was imported into docs/ephemeral/.  
  *Fix:* Cite the docs/ephemeral/ path for the Batch 2 report and ledgers.
- **STALE_REFERENCE** — Names a repository path outside the permitted write paths and records the assembled graph as a committed artifact; the assembled graph is derived output that is never committed.  
  *Fix:* Label this as a dated 2026-09-16 record superseded by 4.5, and note the artifacts now live under docs/ephemeral/.

### GCFPE Alpha Establishment and Change Management Checklist — 091426.1

`3db4590a05eb812f87caed515836687f` — Live establishment/change-management checklist for the candidate release: governance-repair checkboxes, the open GCFPE-11/19/20 obligations, the operative Alpha tuple, and controlled-source rules a reader applies directly.

- **CONTRADICTS_SETTLED** — Open checklist item requires the retired four-state drain vocabulary to pass fixtures; there is no drain status or verification.  
  *Fix:* Reduce to: the exact PF10 producer set passes semantic fixtures.
- **CONTRADICTS_SETTLED** — Retired token presented as a live labelling rule.  
  *Fix:* Strike the pre-drain clause; record the PF10 version actually read as provenance, never a gate.
- **CONTRADICTS_SETTLED** — Drive named as the storage authority for runtime artifacts.  
  *Fix:* Repoint to docs/ephemeral/, landing by pull request.
- **CONTRADICTS_SETTLED** — Drive named as the PFCanon source authority.  
  *Fix:* Resolve PFCanon from docs/pfcanon/, read-only.
- **STALE_REFERENCE** — Stale negative authority: harmless at run time but tells a reader the PF10 drain machine still exists (same class the cross-cutting removal rewrote in the prompts). GCFPE-19's 'without editing or draining it' is the same defect.  
  *Fix:* Delete 'drain PF10' from the negative-authority list and the 'draining it' clause in GCFPE-19.

### Glow HDE Complete Prompt Set — GCFPE-20260914.1 — 091426.1

`3db4590a05eb81738ef1d846e3c0df8c` — The candidate catalog: the 55-member manifest plus candidate-wide invariants. This is the membership authority a reader uses to resolve a prompt by ID and title.

- **CONTRADICTS_SETTLED** — Old CL-20 title. The rename to 'CL-20 — Prepare Closure Memo and Post-Closure Record' updated the prompt page, the Flow Index topology table and the registry, but not this catalog row.  
  *Fix:* Update the row to 'CL-20 — Prepare Closure Memo and Post-Closure Record — 091426.1'.
- **CONTRADICTS_SETTLED** — Candidate-wide invariant publishes the retired four-state drain vocabulary as live contract for all 55 members.  
  *Fix:* Delete the invariant; the retired states have no subject.

### GCFPE Repair Completion Checklist — Recovery-Grounded — 20260914.1

`3db4590a05eb8104b04cc01ed90ec39f` — Phase-gated recovery/repair checklist built on the superseded v2.0 repair plan. Presents itself as live: an open next gate (P6-01), 96 unchecked instruction items across Phases 6-9, operating rules CTRL-01..10 and stop rules STOP-01..10.

- **STALE_STATUS** — The run and the v2.0 plan this checklist implements were superseded by the 20260915.1 six-batch plan and the 2026-09-17 validation restart; a reader still sees an open next gate and 96 live items.  
  *Fix:* Add a supersession banner naming the six-batch plan and mark the page historical, or re-scope it to the current phase model.
- **CONTRADICTS_SETTLED** — An operating rule making Drive the exclusive storage authority for repair evidence and runtime artifacts.  
  *Fix:* Repoint to docs/ephemeral/ landing by pull request.
- **CONTRADICTS_SETTLED** — Freezes the retired four-state drain vocabulary as a contract; P5-11 ('verified drain, pre-drain reference ... absent drain, mismatch') and P3-08's 'pre-drain reference label' repeat it.  
  *Fix:* Strike the four-state items and the pre-drain label from P2-08, P3-08 and P5-11.
- **CONTRADICTS_SETTLED** — Makes verified drain a gate on RS-40 resumption; there is no drain gate and RS-40's four-state machine is gone.  
  *Fix:* Reduce to: resolve current PF10, resume the recorded phase on the qualifying approval.
- **CONTRADICTS_SETTLED** — Unchecked, therefore live, instruction naming Drive as the PF10/canon source and reintroducing drained-vs-undrained overlay states.  
  *Fix:* Resolve PF10 from docs/pfcanon/; drop the drained/undrained distinction.
- **CONTRADICTS_SETTLED** — Three live Phase 6/8/9 items make Drive the persistence target for postflight, validation and the PR04 handoff.  
  *Fix:* Persist to docs/ephemeral/ and reference by repository path.
- **CONTRADICTS_SETTLED** — A stop rule that gates the Alpha handoff on drain verification.  
  *Fix:* Remove 'unverified drain' from STOP-08; CTRL-09/STOP-09/F-20's 'do not drain PF10' wording is the same stale-negative-authority class.
- **STALE_STATUS** — Edge count is not 227 and the six-batch plan independently records e622e3ce as stale before Batch 2; the current token is 55 nodes / 227 edges / 55 state_routes.  
  *Fix:* Label the checkpoint historical; do not present e622e3ce or 240 edges as current graph identity.
- **STALE_REFERENCE** — Governing-sources list points at the superseded v2.0 Drive plan and at Drive as the evidence destination.  
  *Fix:* Point governing sources at the Notion six-batch plan and docs/ephemeral/.

### Glow Operations Hub

`3ce4590a05eb814f8892f88ff8539308` — DISCOVERED. Workspace-level live control hub. Holds the canonical PF10 build-notes addendum format (the control the repair plan says was corrected), the current GCFPE PF10/source boundary, the GCFPE execution and transport boundary, the prompt-ecosystem worker output standard, and the global Notion/Drive/Library/Git operating policy.

- **CONTRADICTS_SETTLED** — The replacement check is retired: `pf10_reference_visibility_check` / `PF10_REFERENCE_VISIBILITY` were struck 2026-09-18 and no prompt carries it. This is the canonical addendum-format home, so the rule outlives the prompts that dropped it.  
  *Fix:* Delete the 'one check on the next turn' block and its seven sub-bullets; the addendum is assumed pasted and nothing is confirmed.
- **CONTRADICTS_SETTLED** — Requires the exact three fields the same page's canonical format now forbids, and stores the addendum in the Drive ephemeral folder; the Hub contradicts itself.  
  *Fix:* Label the 091326.2 selection block historical and point it at the canonical paste-ready format below it.
- **CONTRADICTS_SETTLED** — Presents the manual drain as a live step in the current PF10 boundary; it appears twice on the page, including inside the corrected 'Current GCFPE PF10 drafting and reference controls' section.  
  *Fix:* Strike the manual-drain sentence from both copies of the boundary paragraph.
- **CONTRADICTS_SETTLED** — The current GCFPE execution and transport boundary names Drive as the runtime artifact store.  
  *Fix:* Repoint to docs/ephemeral/, landing by pull request.
- **CONTRADICTS_SETTLED** — 'Current GCFPE prompt and artifact categories' makes Drive the artifact home for the ecosystem.  
  *Fix:* Restate as: repository is the storage and versioning authority; docs/ephemeral/ for working artifacts; Notion for prompts.
- **STALE_REFERENCE** — The workspace operating-policy table predates the repository-first decision and carries no carve-out for the prompt ecosystem, so a reader lands on Drive as the persistent home.  
  *Fix:* Add the prompt-ecosystem exception: repository is the storage authority; Drive only where Nathan directs a specific file.
- **STALE_REFERENCE** — Stale negative authority inside the canonical worker output standard; keeps the retired lifecycle visible to every worker session.  
  *Fix:* Remove 'PF10 drainage' from the list.

### HDE Change Flow — GCFPE-20260914.1 — 091426.1

`3db4590a05eb81d59059eb6b95ed5fcf` — DISCOVERED. Family hub for the CF-PO/CF-C/CF-E/CL/CL-C/CL-E/MGR lanes: live navigation to 18 member prompts plus a 'Shared controls' block a reader applies as standing instruction.

- **CONTRADICTS_SETTLED** — Old CL-20 title in the member table, while the child-page link lower on the same hub already reads 'CL-20 — Prepare Closure Memo and Post-Closure Record'.  
  *Fix:* Update the table row to the renamed title.
- **CONTRADICTS_SETTLED** — The hub's Native purpose still assigns post-closure drainage to the CL lane; CL-20 now produces CLOSURE_MEMO and POST_CLOSURE_RECORD.  
  *Fix:* Replace 'post-closure drainage/scans' with 'the closure memo, post-closure record and PF09 scans'.
- **CONTRADICTS_SETTLED** — Shared-controls block makes the manual drain plus verification a gate on using an overlay; there is no drain step or verification.  
  *Fix:* Replace with: a qualifying approval is in force from the next turn; read current PF10 and record the version read as provenance.
- **CONTRADICTS_SETTLED** — Drive named as the runtime artifact store in the shared-controls block.  
  *Fix:* Replace with docs/ephemeral/ in the repository, landing by pull request.

### HDE IA — GCFPE-20260914.1 — 091426.1

`3db4590a05eb8195a2ccf7c0959a8b6e` — DISCOVERED. Family hub for the IA/DOC/OPS/PR/RS lanes: live navigation to 21 member prompts, the PR and rescope phase map, and the same 'Shared controls' block.

- **CONTRADICTS_SETTLED** — The PR and rescope phase map still gates RS-40 on verified drain; RS-40 resumes on the qualifying approval, reading current PF10.  
  *Fix:* Restate as: RS-40 is eligible only for an existing open PR, resuming the recorded phase on the qualifying approval.
- **CONTRADICTS_SETTLED** — Same retired drain gate as the other four family hubs.  
  *Fix:* Replace with the paste-ready/assume-pasted rule.
- **CONTRADICTS_SETTLED** — Drive named as the runtime artifact store.  
  *Fix:* Replace with docs/ephemeral/ in the repository.

### PE Metaprompt 091426.1

`3db4590a05eb8174be35d9e35acb3f77` — DISCOVERED. The prompt-authoring control for the release, bound by the Flow Index and by 9 of the repair plan. It dictates how every candidate prompt is authored, revised and validated, so its rules propagate into new prompt bodies.

- **CONTRADICTS_SETTLED** — A full normative table of the retired four-state drain machine, reinforced later by 'Use the four post-drain states above as an exhaustive and mutually exclusive vocabulary' and by the RS-40 result row.  
  *Fix:* Delete the table, the vocabulary paragraph and the RS-40 four-state result cell.
- **CONTRADICTS_SETTLED** — Mandates the exact addendum fields the Operations Hub's canonical format now forbids, plus Drive storage; the minimum-schema paragraph that follows repeats them.  
  *Fix:* Replace the addendum schema with the canonical paste-ready format: one heading, the rule, nothing else.
- **CONTRADICTS_SETTLED** — Not only names Drive as the PFCanon authority but explicitly forbids the repository, which is the source of record (docs/pfcanon/, read-only).  
  *Fix:* Resolve PFCanon from docs/pfcanon/ read-only; keep the Markdown-only rule and the Google Docs/DOC/DOCX prohibition.
- **CONTRADICTS_SETTLED** — Drive named as the storage authority for every runtime/planning artifact the metaprompt causes to be written; the GCFPE overlay repeats it for ledgers, manifests, reports, addenda and handoffs.  
  *Fix:* Repoint both clauses to docs/ephemeral/, landing by pull request.
- **CONTRADICTS_SETTLED** — Retired token embedded in the authoring contract, so any prompt authored from it reacquires the label.  
  *Fix:* Strike the pre-drain clause; record the PF10 version actually read as provenance.
- **CONTRADICTS_SETTLED** — States a drain gate as the current Product Owner contract; the approval itself is what continues the work.  
  *Fix:* Replace with: the addendum is paste-ready and in force from the next turn; no agent tracks, verifies or gates on the paste.
- **STALE_REFERENCE** — Completion checklist still verifies Drive routing as a quality gate.  
  *Fix:* Verify repository artifact routing (docs/ephemeral/, docs/graph/parts/, docs/pfcanon/) instead.

## Also carrying the same shared-controls block

The five family hubs publish an identical shared-controls block containing the retired
drain gate and Drive as the runtime artifact store. Fixing one text fixes all five:

Change Flow `3db4590a05eb81d59059eb6b95ed5fcf` · IA `3db4590a05eb8195a2ccf7c0959a8b6e` ·
QA `3db4590a05eb814d96d3dcfa8835f96d` · Escalation `3db4590a05eb81cd938de84cfffead9c` ·
TW `3db4590a05eb811b9c14f2ae89c28df7`

## What is explicitly NOT a defect

Dated reports, receipts and session records that describe what was true at the time.
They are history. Leave them, and add a superseded pointer only where they read as
current status or as forward-looking work that is now done.

**And never "fix" these — they are legitimate Canon disposition:** PF09 rows,
canon-conflict and ADR records, `NEW_CANON`, `CANON_RECONCILIATION`, the permanent Canon
drainage target and owner. Interpret by function, never by the word "drain".

