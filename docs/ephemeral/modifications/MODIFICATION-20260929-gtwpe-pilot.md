---
artifact_type: GCFPE_MODIFICATION_RECORD
format: "2.1"
ecosystem: GTWPE
modification_id: MODIFICATION-20260929-gtwpe-pilot
status: ANALYZED
targets: [prompt, notion_control]
gate_tier: 1
closure:
  upstream: []
  downstream: []
  state_sharers: []
readiness: NEEDS_RULING
override:
  by: ""
  overrides: []
  reason: ""
interaction_cost_predicted: 7
interaction_cost_actual:
estimate:
  plan: "about 1.5 h and 1.5M tokens: §P, a dry run, and one full review by two reviewers"
  execute: "about 1 h and 0.5M tokens: the new page, the three selection writes, the catalog, and their readbacks; with Q1's option (b), about 1.25 h and 0.65M, for the writes and readbacks on three more pages"
reviews:
  - mode: ANALYZE
    kind: DRY_RUN
    date: 2026-09-29
    required_open: 0
    outcome: "By W1, read-only: the validator exits 0 on a copy at ANALYZED; A0 and A3 reproduce; the front matter and every table are well formed. No required defect. Design §13.2 gives ANALYZE no full review"
item_count_at_approval: 1
items:
  - id: ITEM-01
    statement: "TW-MGMT-10 no longer tells its author to use a PE Metaprompt feature that no longer exists, and nothing else it instructs changes."
    source: "TW-MGMT-10-ANALYSIS-20260924.md F6, its first half; PE-METAPROMPT-TEST-20260924.md D8; GTWPE design v1.2 §13.2, PART-02"
    disposition: ""
parts:
  - id: PART-01
    name: "Remove TW-MGMT-10's pointer to the PE Metaprompt's retired complexity profile"
    items: [ITEM-01]
    class: B
    after: []
request: "Start the pilot: run GTWPE-MGMT-10 on the one-instruction repair of the TW management prompt named in the design. Stop at the first point where Nathan must approve."
requested_by: Nathan
analyze_approved_by: "Nathan, 2026-09-29: \"Nathan approves the pilot's analysis (2026-09-29). The fix updates the current-version note on all four pages.\" This rules Q1: option (b)"
analyze_approved_date: 2026-09-29
plan_approved_by: ""
plan_approved_date: ""
supersedes: ""
spawned_from: ""
shares_package_with: []
---

# MODIFICATION-20260929-gtwpe-pilot

TW-MGMT-10, TW-ALPHA's maintenance prompt, stops telling its author to use a PE Metaprompt feature
that no longer exists. This is GTWPE-MGMT-10's pilot (GTWPE design v1.2 §13.2).

## Intake

Not through triage. The request reached W1 from PE37 at 2026-09-29T04:24:54Z, with Nathan's G1
approval ("yes") of the GTWPE design v1.2, which specifies this pilot (§13.2). It is recorded
verbatim in `docs/ephemeral/gtwpe.rewrite/CHECKPOINT.md` §12.1, on `docs/20260925-gtwpe-w1`.
PE37's words name only the prompt repair, the design's PART-02; the input reader, the design's
PART-01, is not in this Modification.

## §A — Analysis

*Written by MODE = ANALYZE. Frozen once approved.*

W1 ran this mode as a GTWPE-MGMT-10 session. It followed *GTWPE-MGMT-10 — Manage the GTWPE — 092926.1*,
fetched live at the start of the mode (page edited 2026-09-29T04:38:37.656Z, unchanged since its
publication). Where the body was silent or ambiguous, W1 recorded a pilot finding before acting
(*Pilot findings*, below).

**Revised on 2026-09-29, before approval, after the cold run** (design §13.2). The first version is
commit `483ce51`. The cold run found that TW names its current release on pages the route does not
write, and that the sentence to be repaired carries two other instructions. W1 verified both, and
found a fourth such page. This version adds them as Q1 and risk 7, sets readiness to `NEEDS_RULING`
and the interaction cost to 7, narrows ITEM-01 so that nothing else in the prompt changes, and
records the comparison under *Pilot findings*. GTWPE-MGMT-10 was fetched again for the revision, and
is unchanged.

### Consult

- **Repository**, `origin/main` at `4ad12fe`, and at `f4be532` for the revision: no Modification
  record names TW-MGMT-10 or the complexity profile. `git grep` finds the terms only in two archived
  GCFPE procedures under `docs/prompt_ecosystem_management/operating-procedures/archive/`. Before
  A1, no `docs/*-modification-gtwpe-*` branch existed on `origin`. The approved design is not on
  `main`; it is on `docs/20260925-gtwpe-w1`, where G1 approved it (pilot finding PF-7).
- **Notion**: a search for TW-MGMT-10 lists 090726.1, 090726.2, 090726.3, 090826.1 and 090826.2,
  edited 2026-09-08T07:07; no later version exists. TW-ALPHA's selection page, *Glow Technical
  Writing Ecosystem*, is unchanged since 2026-09-08T07:15, and still selects TW-ALPHA-20260908.1.
  Three more pages name that release as current, and TW-MGMT-10 090826.2 as TW's maintenance
  prompt (*Scope*, *The pages that name the current release*).

### Drift check (A0)

`git fetch origin main`; the commit examined is `4ad12fe4be4c8149b9159adb1abe7812a8b5da50`.

**(a) The lineage sources.** Searched with highlights off; the register's *Current selection*
section read from a fetch of the register page, a control page.

| Source | Recorded in the catalog | Found | Trigger finding |
|---|---|---|---|
| GCFPE-MGMT-10 | Pinned: the proposed body, 2026-09-24T11:00:24.691Z. Selected: `091426.1` (`3db4590a…eb54`), 2026-09-24T15:38 | Proposed body at 11:00; `091426.1` at 15:38; the register selects `091426.1` | None |
| PE Metaprompt | Pinned and selected: `091426.1` (`3db4590a…3f77`), 2026-09-23T17:17:22.217Z | `091426.1` at 17:17; the register selects it; no later version exists | None |

Before R2-1's fix this check reported GCFPE-MGMT-10's standing difference every time. It reports nothing now.

**(b) The watched paths.** `git log 0db3f0e..4ad12fe` over the watched paths finds two commits:

| # | Commit | What changed | `D26-E` search | Result |
|---|---|---|---|---|
| TF-1 | `feb14e5`, 2026-09-29T04:06Z, #548 | `modification_validate.py` accepts the target class `tool`; `modification-template.md` lists it | `git grep -n -i -E 'no target class for a tool\|P2\(a\) adds' origin/main -- docs/prompt_ecosystem_management/`: 0. GTWPE-MGMT-10's body names `tool` as a class | Nothing contradicts it. It is the change the GTWPE depends on |
| TF-2 | `4ad12fe`, 2026-09-29T04:11Z | PF10 becomes v13.4.4, adding 2.32 (HDE-EPIC040 QA evidence review) and 2.33 (PF10-OPENRAILS-001, a live open-rails test in every QA plan for a production-functional surface) | `git grep -n -i -E 'open-rails\|OPENRAILS\|closed-rails' origin/main -- docs/prompt_ecosystem_management/`: 0. GTWPE-MGMT-10 holds no QA-plan text and cites PF10 without a version | Nothing contradicts it in the GTWPE's current text. P4's run prompts must read current canon, which already carries it |

Adopting either is Nathan's choice. Neither calls for a change, so adopting them means X4 moves the
checked-through commit past them.

**Re-run for the revision.** `git fetch origin main`: `origin/main` is
`f4be5329220ab6e75db85b2eb19ba20f71c8d775`. `git log 4ad12fe..f4be532` over the watched paths finds
no commit. The one new commit, `f4be532` (#550), adds three HDE-EPIC040 QA files under
`docs/ephemeral/`. The two lineage searches return the same pages at the same edit times, and the
register page is still at 2026-09-23T17:43, the edit time at which A0 read its *Current selection*
section. No trigger finding. The commit examined is now `f4be532`, and X4's check starts from it.

### Per part: closure, tier, class and targets

**PART-01** changes *TW-MGMT-10 — Manage the Glow TW Ecosystem — 090826.2*
(`3d54590a05eb81a8b55afabc42298df9`), TW-ALPHA's selected maintenance prompt. It was read live
again for the revision: edited 2026-09-08T07:07:26.670Z, unchanged.

- **Targets.** `prompt`: a TW-ALPHA member, by a new versioned sibling under its parent, and
  selected by the three writes on TW-ALPHA's selection page (design D-16). `notion_control`: the
  GTWPE catalog, which X4 updates in every `EXECUTE`, and TW-ALPHA's selection, which the body's
  route table groups with the catalog (pilot finding PF-1). Q1 decides whether the selection
  writes also reach the three other pages that name the current release.
- **Closure.** The rule reads it from the *Current operation* that TW-ALPHA-20260908.1 records.
  That section records the relationships among TW-ASSESS-10, the two drains, TW-APPLY-10 and the
  two record prompts. TW-MGMT-10 appears only in the member list, as the "Sole TW prompt
  maintenance owner". So `upstream`, `downstream` and `state_sharers` are all empty.
- **Tier 1.** The part changes what TW-MGMT-10 makes its author do, and none of the recorded
  relationships. No consumer is named, so the gate is the member's own checks.
- **Class B, rule application.** The PE Metaprompt's general rules also govern TW
  (`gcfpe.decision-record.md`, *Successor, 2026-09-23 — `D23-G` reaches the PE Metaprompt*). The
  selected PE, `091426.1`, read in full on 2026-09-29, has no complexity profile, and its authoring
  exclusion bars workload-rating fields. The part carries that settled state to a consumer the PE's
  change did not reach (PE test D8). Class B is verified by an isolated readback and a guard search
  (`ecosystem-change-management.md` §2). TW has no registry (TW-MGMT-10 analysis F8), so the guard
  is the phrase's absence: in the new page's readback, and for the other seven members in A3's
  reading. Class D was considered and set aside: its verification is a registry assertion.

**Every other member** (HDE Governance §9.1.6):

| Member | Disposition | Reason |
|---|---|---|
| TW-ASSESS-10 090826.2 | Unaffected | No reference to the PE. Its own five-dimension workload description is its contract, not a pointer to the PE (*Scope*) |
| TW-TRIAGE-10 090726.2 | Unaffected | No reference to the PE or the profile |
| TW-DRAIN-10 090826.1 | Unaffected | The same |
| TW-DRAIN-20 090826.1 | Unaffected | The same |
| TW-RECORD-10 090726.2 | Unaffected | The same |
| TW-RECORD-20 090726.2 | Unaffected | The same; its one "profile" is PF27's CRD profile |
| TW-APPLY-10 090826.1 | Unaffected | The same |
| GTWPE-MGMT-10 092926.1 | Unaffected | It does not cite TW-MGMT-10's authoring instructions |

**Interfaces outside the membership**, added in the revision:

| Interface | Disposition | Reason |
|---|---|---|
| PE Metaprompt 091426.1, the authoring control | Unaffected | A GCFPE control, which no GTWPE Modification changes |
| `tw-flowmaster`, the installed TW flow skill | Unaffected | Its `SKILL.md` has no match for `TW-MGMT-10`, `090826.2` or the page ID. Its "Selected-catalog TW profile" is another function (`NAME-001`). It resolves the drain and application prompts from the selection page, whose rows for them this part leaves unchanged |

### Scope, and how it was measured

**Method.** The eight bodies TW-ALPHA-20260908.1 selects were each fetched in full in this mode.
Each fetch came back inline and complete, and each edit time equals the one P1 recorded. Three
case-insensitive matches were counted over the eight fetch results by a script, `a3_measure.py`,
run in W1's scratchpad (pilot finding PF-2):

| Broad match | Hits | Where |
|---|---|---|
| A. The PE: `\bPE\b\|Metaprompt\|Prompt Engineer` | 16, which are 11 distinct references | TW-MGMT-10 only; 0 in the other seven |
| B. The feature: `five-dimension\|five dimensions\|complexity` | 5 | TW-MGMT-10 2, in one sentence; TW-ASSESS-10 3 |
| C. `profile` | 19 | Every body's model-guidance block 2, which is 16; TW-MGMT-10 1; TW-ASSESS-10 1; TW-RECORD-20 1 |

**Permitted exceptions,** each checked against the selected PE, read in full on 2026-09-29:

- Ten of TW-MGMT-10's eleven references name features the selected PE has: its use for prompt
  engineering; its selection; not reimplementing it; its design controls; not replacing it;
  retrieving it; its PF03, PF06 and PF10 compatibility check; its modes and permission levels;
  authoring through it; and its `MMDDYY.N` scheme. The compatibility check's source location,
  `Glow / Core Docs / PFCanon` in Drive, is a separate defect: TW-MGMT-10 analysis F1, which every
  TW worker shares.
- TW-ASSESS-10's own five-dimension workload description (its step 4, its return and one research
  sentence) and the sixteen workload profiles in the model-guidance blocks name neither the PE nor
  its feature. They are the model-advice content of TW-MGMT-10 analysis F3, which this Modification
  does not change (design D-17).
- TW-RECORD-20's "PF27's relevant CRD profile" is an unrelated term.

**Remainder: 1.** TW-MGMT-10's "Use PE's five-dimension descriptive complexity profile", in its
section *Impact, design and complete authoring*. That sentence gives three instructions: (i) this
one; (ii) through the same verb, the PE's "supported identity/header scheme", which the selected PE
has (design D-5); and (iii) after a semicolon, a TW rule to keep "human guidance non-operative"
after the two identity lines. Only (i) is in scope (risk 7). `PLAN` sets the exact edit.

This part applies a rule and changes none, so no `D26-E` search is due. The measurement above is the
search for the retired feature across TW-ALPHA.

**The pages that name the current release**, measured in the revision. Method: each page that
TW-MGMT-10's own selection procedure names, "the exact TW catalog/current checkpoint selection" and
"TW navigation in HDE TW and Glow Operations Hub" (its section *Versioned Notion publication and
exact selection*), was fetched whole on 2026-09-29. Its current sections were read for three
statements: that TW-ALPHA-20260908.1 is selected, that TW-MGMT-10 is 090826.2, and a link to that
page as TW's maintenance prompt. Sections headed as historical were left out. The Glow Operations
Hub came back as a save of about 177,000 characters, and a script counted over the whole of its
text: `TW-MGMT-10` 3 times (1 in the current TW section, 2 in the historical one), the page ID once
(the current TW section), and `090826` 8 times (3 in the current TW section; 5 in GCFPE sections,
naming GCFPE's own 090826.1 release).

| Page | Its current TW section | Names the release as selected | States TW-MGMT-10 is 090826.2 | Links that page as the maintenance prompt | Written by the route (D-10) |
|---|---|---|---|---|---|
| *Glow Technical Writing Ecosystem*, the selection page, edited 2026-09-08T07:15 | The status line, and *Selected follow-up — TW-ALPHA-20260908.1* | yes | yes | yes | yes |
| *Alpha 1 — Implementation and Validation*, `3d44590a05eb81fe991ff0114cb43029`, 2026-09-08T07:15 | *Selected follow-up — TW-ALPHA-20260908.1* | yes | yes | yes | no |
| *HDE TW*, `3c74590a05eb8176baf8cb59f1631f3c`, 2026-09-23T17:44 | *Current TW follow-up — 2026-09-08* | yes | yes | yes | no |
| *Glow Operations Hub*, `3ce4590a05eb814f8892f88ff8539308`, 2026-09-24T16:03 | *Current Glow TW follow-up — 2026-09-08* | yes | yes | yes | no |

TW's own releases updated all four: *Alpha 1*'s *Coded naming final checkpoint* records "Hub, this
checkpoint, HDE TW navigation and Operations Hub TW navigation are synchronized". The 2026-09-08
release also updated four Drive reference files, by the Operations Hub's account. They were not
read: the workspace's write boundary sends a file to Drive only where Nathan directs that file.

### Contradictions and risks

1. **The model-advice content stays.** After the repair, TW-MGMT-10 still carries its
   model-guidance block and still tells its author to maintain workload profiles, which the
   selected PE's authoring exclusion bars (analysis F3). Design D-17, approved at G1, carries
   everything outside the approved edit unchanged. Removing it is a separate, larger repair that
   reaches TW-ASSESS-10's role. The block itself shows a five-dimension profile that no PE feature
   defines, and D-17 accepts that. An author who applied the PE's exclusion to the new version
   would remove the block, and D-17 is not among the body's PE workarounds (pilot finding PF-6).
   The scope freeze bars `PLAN` from adding that removal, so the likely outcome is a stop, not a
   silent deletion.
2. **The canon source stays.** TW-MGMT-10 and every TW worker still read PF canon from Drive
   (analysis F1). Fixing it in one prompt would split a rule (`ecosystem-change-management.md` §1).
3. **`GUARD-001` matches.** No standing guard can ship with this repair: TW has no registry, so
   the guard is the one-time absence check above. Both design reviewers listed it (R2A-L2; B's L4),
   and G1 accepted the listed findings. Four earlier TW-MGMT-10 versions stay beside the selected
   one, each carrying the clause. The route duplicates the current version, so only a revision made
   outside the GTWPE from an older page could bring the clause back.
4. **Notion writes need the plan's approval.** G2 covered only the GTWPE parent page and
   GTWPE-MGMT-10. `PLAN` names each write this part needs: the new sibling page, the three
   selection writes, the catalog update, and any writes Q1's ruling adds. Nathan's `PLAN` approval
   is then their task-level authorization (`notion-write-boundary.md`).
5. **Known limits on this route**, listed by the design reviews and accepted at G1:
   - The copy becomes a child page of TW's live selection page when X1 makes it, before X4 selects
     it (R2A-L6; B's L12).
   - The second title search may meet Notion's index lag, after an external write (R2A-L11; B's L9).
   - The readback is this session's own, not an isolated worker's (R2A-L1; B's L3).
   - The seven unchanged rows of the new release are checked only against the plan (R2A-L3; B's L8).
   - A selection page left half-written has no rollback (B's L14).
6. **Out of this Modification:** the design's PART-01, the input reader, which PE37 routes. So this
   pilot does not exercise the tool route: X2's pull request, X3's merge detection, and V3's
   reader checks (finding PF-D1, for Nathan).
7. **One sentence, three instructions.** Removing the whole sentence would also remove (ii) and
   (iii): a silent wrong edit to a body. §P's edit must remove clause (i) alone, and its
   verification must find (ii) and (iii) still present in the new version.
8. **TW names its current release on four pages, and the route writes one** (Q1; `DERIV-001`).
   After X4, under D-10 as approved, *Alpha 1*, *HDE TW* and the *Glow Operations Hub* would go on
   naming TW-ALPHA-20260908.1, and linking 090826.2 as TW's maintenance prompt, with nothing to
   mark them stale.
9. **The selection page's headings.** Its current release is headed *Selected follow-up —
   TW-ALPHA-20260908.1*, not *Selected release — …*, so the third selection write anchors on that
   heading. Its earlier releases already carry *Historical selected release — <release>*, the
   heading the route writes.
10. **Shared pages (`SCOPE-002`).** *Alpha 1* still has a section headed *Current selection* over
    TW-ALPHA-20260907.3, stale since 2026-09-08; it predates this work (candidate C6). *HDE TW* and
    the *Glow Operations Hub* hold GCFPE sections beside TW's, so any write there under Q1 (b) is
    confined to the TW section its heading names.
11. **The decision record's scope note.** Its successor of 2026-09-23 keeps TW outside `D23-G`, for
    GCFPE's work. This workstream's authority is Nathan's GTWPE plan (G0) and design (G1), and no
    entry says so. This Modification needs none; noted for PE37.

### Defect classes matched (`ecosystem-change-management.md` §4)

- `SCOPE-001`: the PE's change reached no TW prompt (PE test D8). This scope is measured by broad
  match minus exceptions.
- `GUARD-001`: risk 3.
- `DERIV-001`: one fact, TW's current release, stated independently on four pages (risk 8; Q1).
- `SCOPE-002`: risk 10.
- `NAME-001`: TW-ASSESS-10's five-dimension workload description, the model-guidance profiles and
  `tw-flowmaster`'s "profile" are classed by function, not by word.

### Candidates for separate Modifications (recorded, not taken)

- **C1**: the design's PART-01, the input reader, which PE37 routes.
- **C2**: the other half of F6. TW-MGMT-10's source register asks for "useful fingerprints", which
  `D22` forbids for a prompt body: a one-clause repair of the same kind.
- **C3**: the process half of D8. After a PE change, search every non-GCFPE consumer for text the
  change contradicts.
- **C4**: the lasting fix for `DERIV-001`: one page states TW's current release, and the others
  point to it. Under Q1 (a), it would also bring the three pages up to date.
- **C5**: TW-MGMT-10 analysis F1 to F5 and F7, which the GTWPE retires with TW-ALPHA at G5.
- **C6**: *Alpha 1*'s stale *Current selection* heading (risk 10).

### Open questions for the Product Owner

**Q1 — When the repaired TW-MGMT-10 is selected, which pages change?**

- **What it is.** TW names its current release, and TW-MGMT-10 090826.2 as its maintenance prompt,
  on four pages (*Scope*). GTWPE-MGMT-10 and design D-10 let the route write only the selection
  page, and nothing else in Notion. TW-MGMT-10's own selection procedure updates all four.
- **If nothing changes.** After X4, three pages silently go on naming the superseded release and
  linking the unrepaired prompt as TW's maintenance prompt. Anyone who starts from one of them uses
  the old version. Before G5, only GTWPE-MGMT-10 changes TW, so this recurs with every TW repair.
- **Options.**
  - **(a)** D-10 as written: the selection page only. The three other pages are listed as an
    accepted risk until G5, when TW-ALPHA retires. No added cost.
  - **(b)** Extend D-10, for this Modification, to the current TW section of *Alpha 1*, *HDE TW*
    and the *Glow Operations Hub*, following TW's own release procedure: about two writes a page,
    each read back. The Operations Hub is a page of about 177,000 characters shared with GCFPE, so
    its write is confined to the TW section. About 15 minutes and 0.15M tokens more in `EXECUTE`.
  - **(c)** Select nothing. `PLAN` does not name the selection, the new page waits unselected, and
    `EXECUTE` ends with `PROMOTION_CHECKPOINT_REQUIRED`. Nothing goes stale, and the pilot does not
    test the selection route.
- **Recommendation: (b).** It keeps one fact true on all four pages for a few writes, and it tests
  the route TW actually uses. The lasting fix is C4.
- **Why it is Nathan's.** It widens the Notion destination rule that G2 set (D-10;
  `notion-write-boundary.md`), onto shared control pages.

### Readiness and interaction cost

`NEEDS_RULING`, for Q1. It is advice, not a refusal. No item waits on another item's execution,
and the scope is measured.

    interaction_cost = 1 open ruling + 2 + 3 review rounds + 0 skill reviews + 0 installs + 1 merge = 7

- The three review rounds are this mode's dry run, and `PLAN`'s dry run and one full review
  (design §13.2).
- The merge is the record's pull request. Nothing waits on it (`D21-C`), but it is Nathan's action,
  and the GCFPE counts it (`MODIFICATION-20260923-closeout-residuals.md` §A: "Merges count the
  record PR"). The body does not say (PF-15).
- There is one part, so a split saves nothing. Q1's option (b) adds writes, not round trips.
- The first version gave 5: no open ruling, and no merge counted.

The estimate is in the front matter. Twice either figure is where the session stops.

### Dry run (A6)

On 2026-09-29, by W1, read-only, before the status changed:

1. `modification_validate.py` on a copy of this record at `ANALYZED`: exit 0, 1/1 passed.
2. `a3_measure.py`, run again: the same counts in all eight bodies.
3. A0 (b), run again on `origin/main` at `4ad12fe`: the same two commits.
4. The front matter parses, and every table has a consistent column count.

No required defect was found. Design §13.2 gives `ANALYZE` a dry run and no full review.

**After the revision**, the same checks ran again before A7: the validator on the revised record at
`ANALYZED`, exit 0; A0 re-run at `f4be532` (above); the four pages re-read (*Scope*); and the front
matter and tables checked. No required defect. The cold run is the design's pilot check (§13.2),
listed apart from its reviews, so it is not a round in `reviews`.

### Pilot findings against GTWPE-MGMT-10 092926.1

**The comparison** (design §13.2). The cold run returned the §A it would write, captured unedited as
`docs/ephemeral/gtwpe.rewrite/pilot/COLD-RUN-ANALYZE-R1.md` on `docs/20260925-gtwpe-w1` (the
handback: 37,737 bytes, sha256 `708c41a6d0d7ff2425b8337ad4fe785df0dd41f3b45b2e78aef00c7686371605`).
Against the first version of this §A, `483ce51`:

- **The same:** one item in one part; class B and tier 1; targets `[prompt, notion_control]`; empty
  closure; one instance, in TW-MGMT-10's authoring section; no lineage trigger and the same two
  watched-path commits; the PE's general rules governing TW; no full `ANALYZE` review.
- **Different, and adopted once W1 had verified them:**
  - Q1. The cold run found the release named on three pages and left the Operations Hub
    unmeasured. W1 confirmed the three and found the Operations Hub is the fourth.
  - The sentence's three instructions (risk 7). The first version named the second only.
  - The body's PE workarounds omit D-17 (risk 1; PF-6).
  - The interaction cost: 7 against 5 (PF-15).
  - The defect classes `DERIV-001`, `SCOPE-002` and `NAME-001`; candidates C2 to C5; and
    `tw-flowmaster` and the PE as interfaces. W1 added C6, and checked `tw-flowmaster` itself.
- **Different because of the cold run's brief, not the body:** it measured TW-MGMT-10 alone, since
  it could fetch no other body; and it read A0 (a) by the register's edit time, since it could
  write no file (PF-D2).

**Findings against the body.** Each becomes an item of GTWPE-MGMT-10's first repair (design
§13.2). Both runs met most of them, and did the same thing unless the row says otherwise.

| # | Where | Finding | Effect | What W1 did |
|---|---|---|---|---|
| PF-1 | *The record*, `targets`; the route table; X4 | `notion_control` is defined as the GTWPE catalog. The route table groups TW-ALPHA's selection with it, X4 updates the catalog in every `EXECUTE`, and no target class names the selection | Ambiguous | Listed `notion_control` |
| PF-2 | A3; *Reading prompt bodies* | A3's check wants "the search command and its count", but a body fetched inline can be counted only by reading the transcript, which the harness-file rule allows only for "the fetch, its readback, or the capture" | Normal path | Counted by a script over the eight fetch results, within A3, and disclosed it |
| PF-3 | A6 | The dry run is defined only as "every normal-path gate and readback", and no place is named for its evidence | Low | Recorded it in §A |
| PF-4 | *What this prompt may change*; *Notion writes*; the route table; also design §11.5 and D-10 | TW's selection is written on one page. TW names its current release on four, and TW-MGMT-10's own selection procedure updates all four | Silent: three pages go on naming a superseded prompt | Q1 |
| PF-5 | Consult; A3 | For a prompt change, no step looks for the pages that name the member's current version. The first version of this §A missed three; the cold run found them from TW-MGMT-10's own text | Silent miss | Measured them (*Scope*) |
| PF-6 | *Relation to the PE Metaprompt* | The four PE workarounds do not include D-17, so an author applying the PE's authoring exclusion meets a conflict the body does not resolve | Loud, because of the scope freeze | Risk 1 |
| PF-7 | *Read these* | The design is named by directory only, and it is not on `main` until W1's branch merges | Loud | Read it from `docs/20260925-gtwpe-w1` |
| PF-8 | Entry contract; A1 | The branch's base and slug are unstated, and A1's commit is implied only by its check | Low | Branched from `origin/main`; slug `pilot`, from design §13.2; committed at A1 |
| PF-9 | Entry contract; *One session* (`D26-C`) | No rule covers a record or branch that already carries the ID, as a restarted `ANALYZE` would meet after A1 | Loud | Not met by W1. The cold run met it, since it ran after W1's A1 |
| PF-10 | A0 (a) | The register is a large control page, which the harness saves to a file. The body does not say how to read one section of it | Low | Read the save at that section, then deleted it. The cold run compared edit times |
| PF-11 | A0 (b) | "The `D26-E` search it calls for" names no text or corpus for a change to a watched source | Low | Searched the GTWPE's own text for text the change contradicts |
| PF-12 | *Reviews are bounded*; `EXECUTE`'s capture paragraph | The review brief template has each reviewer write its own record, while a worker writes nothing. The capture procedure sits in the `EXECUTE` block, though reviews run in `ANALYZE` and `PLAN` | Normal path at `PLAN` | Not yet met; `PLAN`'s full review will meet both |
| PF-13 | *Reading prompt bodies* | The body requires a *Harness files* section, which template 2.1 lacks and the validator does not check | Low | Put it inside §A |
| PF-14 | *The record*, `estimate`; *Reviews are bounded*, rule 4 | No meter a session can read gives the token measure. The only one, a script over transcripts' usage fields, is a harness-file read the body does not permit. A worker's transcript also under-records its output: the cold run's records 1,490 output tokens over 88 messages, against about 12,600 in its return alone | The stop rule cannot be applied as written | Measured by script, and disclosed it |
| PF-15 | *Readiness* | Whether a `DRY_RUN` is a review round, and whether a merge that nothing waits on counts, are unstated | Low | Counted both |
| PF-16 | *Readiness* | Which predicate wins when `SPLIT_RECOMMENDED` and `NEEDS_RULING` both hold, and whether a measurable scope left unread is "unmeasured", are unstated | Low | Not met by W1 |
| PF-17 | *Reading prompt bodies* | The quoting limit is an edit's shortest unique anchor, which does not exist until `PLAN` | Low | Kept every quote from a body no longer than the defective clause |
| PF-18 | Throughout | No skill is named. The workspace's write-boundary skill governs every session's writes | Low | Loaded it at the start of the session |
| PF-19 | A2; *The record*, `closure`; A3 | For a TW-ALPHA member, three things are unstated: which members "every other member of that ecosystem" means; whether a result code shared only by name makes a state sharer; and what A3 measures over, the eight selected bodies, which only the design names | Low | TW-ALPHA's seven and GTWPE-MGMT-10; empty closure; the eight bodies |
| PF-20 | `EXECUTE`'s capture paragraph | A capture goes to "the record's file", which could be the record or an evidence file beside it; no evidence path is named | Low | The cold run's return is the design's pilot evidence, so W1 captured it on its own branch |

**Findings against the design, for Nathan** (§13.2, *After it*):

- **PF-D1.** The request carries only the prompt repair, so this pilot does not exercise the tool
  route: X2's pull request, X3's merge detection, and V3's reader checks. They are first exercised
  when PE37 routes the reader (C1).
- **PF-D2.** The cold run's brief lets it fetch only GTWPE-MGMT-10 and the bodies the request names,
  and write nothing, so its return cannot test A3 across TW-ALPHA or A0 (a)'s reading of the register.
- **PF-D3.** §11.5 and D-10 write TW-ALPHA's selection on one of the four pages that state it
  (PF-4; Q1).

### Harness files (`D22` condition 5)

- **This session's transcript** holds, from this mode, the eight TW bodies and GTWPE-MGMT-10's body
  fetched at its start; for the revision, GTWPE-MGMT-10's and TW-MGMT-10's bodies fetched again;
  and bodies from earlier phases. `a3_measure.py` and a second count for `profile` read the eight
  fetch results within A3, and printed counts and matching lines only. `cost.py` read its usage
  fields, and printed numbers only (PF-14). Nothing hashed, compared or kept a body. It is left to
  teardown.
- **The cold run's transcript**, `subagents/agent-ab5c6760d50100f76.jsonl` in this session's
  directory, holds GTWPE-MGMT-10's and TW-MGMT-10's bodies. It was opened by the capture script for
  the worker's final handback, by a tool-use scan for the post-check (design §7.5), and by `cost.py`
  for its usage fields. It is left to teardown.
- **Two tool-results saves**, both of control pages: the GCFPE register, read at its *Current
  selection* section; and the Glow Operations Hub, counted by script for the revision. Both were
  deleted (exit 0).
- No transient file holds a prompt body.
