1 distinct confirmed REQUIRED finding

Review GTWPE-P1R-R2-A of `design/GTWPE-DESIGN-v1.2.md` at `a08999e`. The file is 1,215 lines, 121,921 B, sha256 `1e35645a…`. This is full review 2 of 2 for PLAN (D26-A), the last round. Branch head `98ea4f4` only adds the round-2 brief after `a08999e`, and every file reviewed here is identical at both commits.

- **Four of full review 1's five required findings are fixed. RF-1 is fixed for the PE Metaprompt but not for GCFPE-MGMT-10.** A0 (a) compares GTWPE-MGMT-10's pinned source with the page the GCFPE register selects. That source is the unpromoted proposed body, which the register does not select. So every drift check reports a false change, and X4 can then re-pin the lineage to the wrong page. That is R2A-1 below.
- **The validator claim (C2) reproduces for the two-part pilot.** Tested in memory: with `tool` added, the record passes at all four statuses. Without it, each status fails on `tool` alone.

## Required findings

### R2A-1 · R1, with an R2/R4 path · A0 (a) treats the register's GCFPE-MGMT-10 as the source's current version, but the pinned source is a page the register does not select

- **Text.**
  - §11.4 A0 (a): "A fetch of the GCFPE register's current release entry … gives each one's selected version … A selected page other than the pinned one, or a pinned page edited after its pin, is a trigger finding."
  - §11.1 and §11.7 pin the proposed body, `3e34590a05eb811b93d2da9b4ef8106d`. §11.1 says it is "APPROVED_FOR_TESTING and not promoted, and GCFPE's promotion is not waited on".
  - X4: "re-pin each lineage source whose trigger finding this Modification settled, adopted or declined, to the page and edit time A0 found."
- **Evidence.**
  - **The register selects the live member, not the pinned page.**
    - `project-prompt-contract-registry.md` line 3283 binds GCFPE-MGMT-10 to page `3db4590a05eb81d1bb64ebcb3ca8eb54`, "GCFPE-MGMT-10 — Manage an Ecosystem Change — 091426.1", `lifecycle: ACTIVE`.
    - `pe36-to-pe37.md` line 52 says the proposed body "is APPROVED_FOR_TESTING and not promoted".
    - `authoritative-surfaces.md` line 86 calls the register (`3d24590a…fa1`) the "Sole selection authority".
    - The P1r dry run (check 4) found the two as separate pages: the proposed body, and "The live 091426.1 page", last edited 2026-09-24T15:38.
  - **So the check fires on every run.**
    - "A selected page other than the pinned one" is true for GCFPE-MGMT-10 at every A0 until promotion, starting with the pilot's first.
    - Each A0 records the same trigger finding, "with the D26-E search it calls for". That search checks GTWPE text against the pre-redesign body, which GTWPE-MGMT-10 deliberately does not follow. Each time, Nathan is asked to adopt or decline it.
    - A check that fires on every run cannot tell drift from the designed state (`CHK-001`).
  - **Settling the finding re-pins to the wrong page.**
    - X4 re-pins "to the page and edit time A0 found", which is the selected page `3db4590a…eb54`.
    - The catalog's lineage pin then names a body GTWPE-MGMT-10 is not derived from (§11.1). That is a silent wrong edit to the catalog block, a control page.
    - From then on, an in-place edit to the real source `3e34590a…` is neither "a selected page" nor "the pinned one", so no A0 reports it before promotion. This silently reopens E-019's miss.
    - GCFPE's own in-place edits to `091426.1` are reported as GTWPE drift instead.
  - **A new page is never a finding.** A page with the stable name that is neither selected nor pinned, such as a revised proposed body, is listed and passed over.
  - **Nobody checked this half.** W1's check of the new text (CHECKPOINT §11.4) searched the register for the PE Metaprompt only. The repair follows RF-1's suggested correction, which had the same gap.
- **Path, likelihood and consequence.**
  - Path: normal, every ANALYZE until the proposed body is promoted.
  - Likelihood: the false finding is certain. The wrong re-pin is likely at the first Modification that settles the finding.
  - Consequence: noise and a meaningless decision for Nathan at every ANALYZE, then the silent loss of the check E-019 added.
- **Smallest correction.**
  - In A0 (a), use the register's selection for the PE Metaprompt. Use it for GCFPE-MGMT-10 only once the proposed body is promoted.
  - Until then, compare the pinned page's edit time, and report any other page with the stable name that was created or edited after the pin.
  - In X4, re-pin a source to a different page only when the Modification adopted that page as the source. Otherwise, update only its edit time.
- **In text the last repair added?** Yes. A0 (a) and X4's re-pin are RF-1's repair.
- **Refutation tried.**
  - The register might select the proposed body. The registry row and the succession record say it selects `091426.1`.
  - "Selected version" might mean a version string. §11.7 pins a page ID and an edit time, and A0 compares pages.
  - W1, running the pilot, would probably see the finding is false and record a pilot finding. That makes this defect the pilot's own first repair. It does not change the body the pilot publishes, or X4's literal re-pin.

## Listed findings

New this round. Each line gives the finding, then path and likelihood, then consequence, then whether it sits in text the last repair added.

- **R2A-L1.** §13.2 says PART-02's class B "is verified by an isolated readback". But §11.5 reads the page back "into the session's context", and §16's new row says "its prompt repair's readback is the session's own" (see `ecosystem-change-management.md` §2 Step 4) · normal (P3), certain · the record claims a verification the pilot does not do · yes.
- **R2A-L2.** PART-02's guard is "the phrase's absence", checked once. With no TW registry, nothing catches the phrase coming back (`GUARD-001`; definition of done item 3), and §16 does not list this as a risk · normal, certain · a one-time check stands in for a guard · yes.
- **R2A-L3.** The new release section's rows are checked only against "the plan's" rows, which the plan's author copies from the same page. No step compares the seven unchanged rows with the prior release's rows at X4, although this is a control page that `D22` lets the session compare · normal, low · a copying error silently selects the wrong version of an unchanged TW member · yes.
- **R2A-L4.** D-16 adopts "the one exception", and §2.1 and §12.3 allow only the pilot's release. But D-10, §4.4, §11.2 and §12.2 let any Modification make a TW-ALPHA release until G5 whenever its plan names it. §11.5's rollback after X4 is itself a second release · normal after P3, medium · G1 approves a single exception and a standing permission at once · yes.
- **R2A-L5.** §4's shared *Boundaries* still say GTWPE-MGMT-10 writes "the GTWPE's Notion pages", while §4.4 and §11.2 now add TW-ALPHA pages. This reopens the §4/§4.4 consistency that plan v1.2 §16.2 lists as settled (the diff check's listed #10) and that V1r checks · normal (P3), certain · a strict session refuses PART-02's writes, loudly · unchanged text the repair did not update.
- **R2A-L6.** The new sibling is a child of the selection page (§13.2), so X1's duplicate adds a child-page block to that live page, well before X4. §11.5 says "Nothing else on the page changes", §4.4 excludes anything beyond the three writes, and X4's readback checks headings only. Where the block lands is unverified; it may land inside the selected release's own section · normal, certain for the block · a live control page shows an unselected version, or a strict session stops · yes.
- **R2A-L7.** The cold run follows the published body, whose A0 now starts with `git fetch origin main`, under §7.2's clause "Do not run a git command that changes any state". §7.5's snapshot (local branches, HEAD, stash, remote heads) cannot see a fetch · normal (P3), medium · a silent, harmless breach of the brief, or a §A that differs from W1's · yes.
- **R2A-L8.** PART-02's selection "waits at X4 for the reader's merge" although `after: []`. A stalled or closed reader PR leaves the TW repair applied but unselected, and under `D26-B` a PART-01 failure stops both parts. That goes against D21-B ("Parts land independently") and repeats the kind of wait RB-2's repair removed · normal, low to medium · delay, and a loud stop on failure · yes.
- **R2A-L9.** Part of RB-2 remains. X2 still opens a pull request for a change that only "needs an install", and X3's "resume from main" and its blob check on "every changed file" then need that record-only PR merged · normal for a skill change after P6, medium · the record merge holds up the change, or X3 stops loudly after the install · yes.
- **R2A-L10.** X1 does not put PART-01's local, repairable work before PART-02's first Notion write. If §P orders PART-02 first, a routine PART-01 selftest failure becomes a `D26-B` stop · normal (P3), low · loud · partly.
- **R2A-L11.** The second exact-title search runs straight after the retitle. If Notion's search index lags (unverified), "exactly one page carries it" fails after an external write, and `D26-B` stops the pilot. Listing the parent's child pages, a control page, would check the same without search · normal, unverified · loud · yes.
- **R2A-L12.** Between the duplicate and the retitle, the copy carries the old title, and no step records its page ID before X2's push. A session lost in that window leaves a copy that neither the exact-title search nor the sweep can find, and a restarted EXECUTE duplicates again · failure, low · an unrecorded copy titled like the selected version · yes.
- **R2A-L13.** W1's phrase search (CHECKPOINT §11.4) returned ten results, the connector's default page size. So "only TW-MGMT-10's five versions among the TW prompts" may rest on a cut-off list; I withhold the claim that the search was complete (AGENTS.md truncation guardrail). The search also returned the HDE TW hub page. §13.2 omits it, A3 does not read it, and D-10 gives no route to change it · normal, low · a surviving mention outside the eight bodies is not reported · yes.
- **R2A-L14.** X4 moves the checked-through commit past its watched-path trigger findings whatever their disposition. An unanswered finding is reported once and never again, whereas a lineage pin moves only once its finding is settled · normal, medium · drift is reported once, then dropped · yes.
- **R2A-L15.** X4 leaves out "this Modification's own files" by path, so another actor's commit to the same path in the window is left out too. Two Modifications open at once can also move the checked-through commit backwards · normal with parallel work, low · a missed commit under `gtwpe/`, or repeated findings · yes.
- **R2A-L16.** A0 (a)'s searches set no page size and no rule for a pinned page missing from the results. At the default of ten results, a missing pinned page produces no finding · normal, low · a silent miss · yes.
- **R2A-L17.** D-17's permission, "The prompt's own version and human model header remain permitted", sits in §9.1.6's paragraph on GCFPE bodies. TW-MGMT-10's block also rates workload ("Approximate workload: 9–10/10", analysis F3), which that wording may not cover. Carrying the block through the PE (§11.10) also departs from the PE rule that the decision record says governs TW. D-17 does put the choice to Nathan · normal (P3), certain · as D-17 states · yes.
- **R2A-L18.** The pilot's `targets` are `[tool, prompt]`, but PART-02 also writes TW-ALPHA's selection page, a control page; §11.3 names `notion_control` only for the catalog block · normal, certain · the target set does not bring in the selection page's own check · yes.
- **R2A-L19.** The new release "states that the prior release's *Current operation* and limits still apply", and that text now sits under a *Historical* heading. If it names member versions (unverified), it contradicts the new TW-MGMT-10 row. After a second release, the pointers chain · normal, unverified · an ambiguous live selection · yes.
- **R2A-L20.** `tw-flowmaster` (SKILL.md line 331) records the catalog release it runs under and treats a mixed selection as a blocker. A TW run in flight at X4 may therefore stop, against §12.4's "finishes under TW-ALPHA" · normal, low · loud · yes.
- **R2A-L21.** §12.5's P3 row keeps "about 2M" while saying the repair "adds about 0.3M", so the stop at twice the estimate is either 4M or 4.6M · normal, certain · ambiguity only · yes.

Carried from full review 1, still open and now exercised by the pilot:

- **A's L10 and L12, B's L13.** An edit is "its shortest unique anchor and its new text", and the readback checks "new text present, anchor absent". PART-02 is a deletion, so leftover or over-deleted text passes · normal (P3), low · a silent partial edit of TW-MGMT-10 · no.
- **A's L14.** PLAN reviewers read no prompt body, so only its author checks PART-02's edit in place · normal (P3), certain · no.
- **A's L26.** §9.1.6's sentences that PF10 2.31 keeps separate published selection from observed runtime correction, and say "publication readback" is "not runtime validation". The pilot records PART-02 as VERIFIED and COMPLETE on readback alone, with no failing case kept for retest · normal (P3), certain · no.
- **A's L2, B's L1.** The token measure re-reads harness transcripts that hold prompt bodies. The pilot now reads nine TW bodies, and neither §11.6 nor §16 names that re-read · normal, likely · no.
- **A's L6, B's L5.** No pull request carries the COMPLETE record, so after the pilot `main` holds it at EXECUTING · normal, certain · partly.
- **A's L7, B's L4.** PROMOTION_CHECKPOINT_REQUIRED has no route to a later selection · normal where a plan names no selection, certain · no.
- **A's L24, B's L22.** D-14 names the kickoff's branch rule but not `glow-write-boundary`'s "One branch per session, one PR per branch" (line 99 of the installed skill) · normal (P3), certain · no.
- **A's L28, B's L9.** The failure record's destination and "the freeze" are undefined · failure, low, loud · no.
- **A's L9.** Nothing checks what the cold-run worker wrote before P4 builds the post-check · normal (P3), low · no.
- **A's L18, B's L16.** §12.2 has P4 update the catalog block, while §11.7 lets only EXECUTE change it. P4's own `gtwpe/` commits become the next A0's trigger findings · normal (P4), certain · no.
- **B's L6.** X3 compares against "the branch's blob", which no step records, and merged branches are deleted · failure, low, loud · no.

Round 1's listed findings that v1.2 resolved:
- A's L11: the copy is now retitled (with RB-1).
- A's L13 and B's L12: the destination rule now covers editing the copy.
- A's L19 and B's L18: sources are now re-pinned (for the PE Metaprompt).
- A's L20: A0 now fetches first.
- A's L25 and B's L21: the pilot now changes a prompt page.
- A's L27: covered by RB-2's fix.

## Prior required findings, and the trend

| Finding | Disposition |
|---|---|
| RF-1 (R4) | **Fixed for the PE Metaprompt.** A successor page that the register binds is "a selected page other than the pinned one", and X4 re-pins to what A0 found, so nothing is lost between A0 and X4. **Fixed with a new defect for GCFPE-MGMT-10** (R2A-1) |
| RF-2, also RB-4 (R1) | **Fixed.** X4 re-scans from the commit §A recorded to the merge commit or `origin/main`, the next A0 starts at the new pin, A0 fetches first, and the first pin is `0db3f0e`. Every watched-path commit is examined by some drift check. What remains: L14, L15 |
| RB-1 (R1) | **Fixed.** The copy is retitled once populated, a second exact-title search requires exactly one page, and the readback checks title and parent. What remains: L11, L12 |
| RB-2 (R1) | **Fixed for the prompt-only path it named.** What remains: L8, and L9 (install-only changes) |
| RB-3 (R3) | **Fixed.** §7.4, §11.4 and §11.6 open only the transcript the agent ID names, and never scan the directory |
| P1r-5 (R3; W1's own, recorded as open) | **Not fixed, and its recorded route would not fix it.** §15 and §16 say "Fixed in P4 with RQ-3's fix", but S1's rule (§5.1) and P4's cases (§13.3) refuse only by an identity-pattern title or an `AI Prompts` path, which is exactly the gap P1r-5 names. Smallest correction: add the case to §5.1 and §13.3, for example by refusing any page the register or the TW selection page binds as a prompt |

**Trend.**
- Required findings went from 6 (dry run) to 5 (full review 1) to 1 (this round), so the count halves.
- Counting P1r-5, which the design carries as open, 2 required findings remain open.
- R2A-1 sits in text the last repair added, and so do nearly all the new listed findings. D26-A rule 5's second signal therefore holds.
- No round follows. The output goes to Nathan at G1 with every open finding listed.

## Claims

| Claim | Holds? |
|---|---|
| C1 | RF-2/RB-4, RB-1, RB-2 and RB-3: yes. RF-1: only for the PE Metaprompt (R2A-1) |
| C2 | Yes for the validator, reproduced in memory. The record had `targets: [tool, prompt]`, both parts class B, tier 1, three items, `item_count_at_approval: 3`, and reviews ANALYZE DRY_RUN, PLAN DRY_RUN, PLAN FULL. It passes at ANALYZED, PLANNED, EXECUTING and COMPLETE with `tool` added, and fails at each only on `tool` as on `main`. Every step names a check, but A0's check passes on a false finding (R2A-1) |
| C3 | In substance, yes, and D-16 and D-17 are put to Nathan. The class B verification claim does not match the route (L1). The "only TW-MGMT-10" premise rests on a possibly cut-off search (L13), which A3's reading covers for the eight bodies |
| C4 | Yes for the routes, and no body copy is needed. A rollback after X4 is a new release made by a new Modification (L4). D22 holds except the carried token-measure re-read |
| C5 | No, as written: L4, L5, L6 |
| C6 | Yes for the PE Metaprompt and the watched paths. No for GCFPE-MGMT-10 (R2A-1). A watched-path finding is reported once (L14) |
| C7 | Yes. RQ-1 to RQ-3 are unchanged, and the build order is plan v1.2 §16.1 with P3 extended. The plan's P3 row and §2.5 wording are PE37's to update (CHECKPOINT §11.1) |
| C8 | The three target rulings hold: GTWPE-MGMT-10 writes no canon file, and §8.7 is unchanged. "Cannot gate" holds for prompt-only changes; see L8 and L9. On the G0 direction: the pilot now runs the prompt-repair route Nathan needs. But R2A-1 would put a meaningless adopt-or-decline question, in the code words he rejects, to him at every ANALYZE |

**Attack list.**
- **A1 (TW-ALPHA's selection).** None of the three writes, as specified, is a silent wrong edit. But the rows are checked only against the plan (L3), and a child-page block lands on the page (L6). The rollback is real, but it takes a second release made by a new Modification (L4). D-16 is put to Nathan. Closure follows the pointer to the earlier release (L19).
- **A2 (PART-02's class and verification).** Class B is defensible. Its verification is neither isolated (L1) nor a standing guard (L2). A3's reading is consistent with `SCOPE-001` and §11.6. The chosen defect is the smallest the analyses name, with L13's caveat.
- **A3 (walking the pilot).** C2 holds. See L10, L8, L12, and the carried items on the COMPLETE record and PROMOTION_CHECKPOINT_REQUIRED.
- **A4 (the drift check).** Nothing slips between A0 and X4, or between two Modifications. The register entry was reached by searching within the register. Minute resolution misses only an edit made in the pin's own minute. The GCFPE-MGMT-10 half fails (R2A-1).
- **A5 (the prompt-page route).** No silent wrong edit beyond the carried extent risk. A copy that lands under another parent fails the parent check, loudly. See L11 and L12.
- **A6 (D-17).** No breach of §9.4: the TW page is not a GTWPE body. See L17.
- **A7 (capture).** Capture no longer scans the directory, and the post-check lists file names only. The token measure's re-read is carried.
- **A8 (unchanged against new text).** §4.4 agrees with §11.2 and §11.5. §4's Boundaries do not (L5). §12.3 agrees with D-16 but not with D-10 (L4). §15 and §16 match §0.2 except P1r-5's route. §17 matches CHECKPOINT §10.4 and §11.2.

## Canon relied on

- **`AGENTS.md`** at `origin/main` `0db3f0e`, blob `548769ac`, identical at `a08999e`. Applied: the canon-first rule; PF canon is read-only; the truncation guardrail (used in L13); evidence attribution. Its *Code review scope* line applies to automated code review, not to this commissioned D26-A review.
- **Canon-first search.** `git grep` over `docs/pfcanon/` on `origin/main` for prompt-ecosystem, Technical Writing, TW-ALPHA, tw-flowmaster, GCFPE, readback and model-header terms. Governing sections read:
  - PF04 — HDE Governance §9.1.6, in full;
  - PF10 — HDE Build Notes, addendum 2.31 (PF10-HDR-001), in full;
  - PF10 — HDE Build Notes, addendum 2.29 (PF10-CANON-001), its *Scope boundaries and nonclaims* and *Unresolved work* only.
- **In-flight documents**, at `a08999e` unless stated:
  - `design/GTWPE-DESIGN-v1.2.md`, whole, and the v1.1 to v1.2 diff, whole;
  - `CHECKPOINT.md`, whole;
  - `design/REVIEW-P1r-R1-A.md` and `-B.md`, whole;
  - `TW-MGMT-10-ANALYSIS-20260924.md`, `TW-BASELINE-20260924.md` and `PE-METAPROMPT-TEST-20260924.md`, whole;
  - `design/P1-SOURCE-NOTES.md`, whole;
  - `design/DRY-RUN-P1r.md`, check 4 only;
  - plan v1.2 and `ERRORS.md` at `0ecb6a1`, whole.
- **Governing documents** in `docs/prompt_ecosystem_management/`, byte-identical at `a08999e`, `0db3f0e` and `origin/main`:
  - `gcfpe.decision-record.md`, D20 to D26 with D23's successors, including "`D23-G` reaches the PE Metaprompt";
  - read whole: `modification-template.md`, `ecosystem-change-management.md`, `notion-write-boundary.md` and `prompt-body-content-policy.md`;
  - `modification_validate.py`, lines 1 to 520;
  - `reviewer-prompt-template.md`, its front matter and the second template from its fixed §3 on;
  - `pe-succession/pe36-to-pe37.md`, lines 45 to 82;
  - `authoritative-surfaces.md`, line 86;
  - `project-prompt-contract-registry.md`, the GCFPE-MGMT-10 row.
- **Installed skills**, searched only: `tw-flowmaster` (line 331), `flowmaster-validate` (it pins no TW-ALPHA release) and `glow-write-boundary` (its path rules and line 99).

## What I ran, and writes

- **Git.** Read-only commands only. No fetch.
- **Validator.** Its source from `a08999e`, run in memory with `python3 -B`, reading synthetic records through an in-memory patch. No file was written, and `--selftest` was not run.
- **Notion.** The connector's tool definitions were loaded locally. I made no Notion call and read no prompt body.
- **Writes.** None. `git status` is clean, and HEAD, branches and stash are unchanged. The harness's `tool-results/` directory still holds only its two files from 2026-09-28, which I listed by name and did not open.

DECISION NEEDED
