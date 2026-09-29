2 distinct confirmed REQUIRED findings

Review: GTWPE-PILOT-PLAN-A, full review 1 (of 1 planned) of the PLAN of MODIFICATION-20260929-gtwpe-pilot, at commit ae5c84f498b218b0b9f9489fee95c0fa9f7c4a22 (§P, with §A as input).

I checked it against:
- the four live control pages it edits that I may read;
- design v1.2 §11 to §18;
- the governing documents and PF canon on origin/main 633ca5d.

This is the first round, so there are no earlier findings to dispose of.

## REQUIRED findings

### RA-1 — R1 (normal path), with an R4 consequence: no step handles the update tool's asynchronous result

**Text or step.**
- The *Dry run*'s D11 says: "`notion-update-page` sets a page's title by `update_properties`; `update_content` takes `old_str` and `new_str` pairs, where each `old_str` must match the page exactly, and a pair fails if its `old_str` matches more than once".
- Every update write, W2 to W8 (X1.6, X1.7, X4.2 to X4.6), is followed at once by its readback.
- *How the plan runs* stops only on "A failed check, or a tool error".
- The record mentions asynchronous completion only for `notion-duplicate-page` (D11), which X1.4 polls.

**Evidence.** The `notion-update-page` schema, read for this review, documents a second result mode. Its `allow_async` parameter reads: "Default to true for page updates. Set to false only when the next step needs the updated page immediately … When this update operation is accepted for background execution, it returns an async_task result. Use get_async_task to wait for a succeeded status before taking a dependent action on the page … If omitted or false, the tool waits for a synchronous result when possible, but may still return a pollable async_task response if queued execution exceeds the synchronous wait deadline." `notion-get-async-task` is available. The plan sets no `allow_async` value and says nothing about an `async_task` result. So C1's "no interpretation" does not hold at any write.

**Path, likelihood, consequence.**
- Path: normal.
- Likelihood: certain at every write for an executor that takes the tool's stated default (true). Otherwise low per write, and highest for W8 on the Hub (about 177,000 characters).
- Consequence: a readback that runs before the queued write lands fails, and stops a healthy run under D26-B. The sweep can then record a page as unwritten while the queued write lands after it, so the failure record misstates what is live. For W5 in particular, PO-4's rollback ("archive «NEW»") would leave TW's selection page linking an archived page until a later sweep finds it.

**Smallest correction.** Add one rule under *How the plan runs*, and correct D11 to match: "Each `notion-update-page` call (W2 to W8) is sent with `allow_async: false`. If it still returns an `async_task`, poll `notion-get-async-task` until it reports success before the step's check; a failed task is a tool error. Before D26-B's sweep, any pending task is resolved the same way."

**In text the last repair added:** no.

### RA-2 — R4 (failure path): the rollback offered for HDE TW and the Glow Operations Hub restores the whole of a shared page

**Text or step.**
- X4.4's rollback reads "A newer note naming 090826.2, made the same way; or Nathan's restoration from page history". X4.5 (HDE TW) and X4.6 (the Hub) use it ("As X4.4").
- Failure-path step 4: "He archives «NEW» or restores a page from its history".
- PO-4: "archive «NEW», or restore a page from its history".
- K-8 expects other sessions to edit exactly these two pages.

**Evidence.**
- Both pages hold GCFPE sections beside TW's. The approved §A confines any write on them "to the TW section its heading names" (risk 10; SCOPE-002).
- A restore from Notion page history returns the whole page to an earlier version.
- The design's own rollbacks for control pages are writes made "the same way" (§11.5), not history restores. The failure path and PO-4 name only the restore.
- The sweep, and PO-4's check after Nathan acts, read what the pages say about TW. Nothing in the plan would notice lost GCFPE text.

**Path, likelihood, consequence.**
- Path: failure, after W7 or W8 has landed (K-8's stop, or a stop at X4.7 or X5).
- Likelihood: low.
- Consequence: another session's later edits to those pages' GCFPE sections are reverted along with the TW section. They then survive only in page history.

**Smallest correction.** In X4.5's and X4.6's rollback, and in failure-path step 4, state that HDE TW and the Hub are not restored from page history. Their rollback is the reverse replacement: *HDE-NEW* back to `## Current TW follow-up — 2026-09-08`, and *HUB-NEW* back to `## Current Glow TW follow-up — 2026-09-08`. Nathan makes it by hand, or a newer note is written the same way.

**In text the last repair added:** no.

## LISTED findings

Each line gives: path; likelihood; consequence; in text the last repair added.

- **L1.** *The texts*' closing note says *Alpha 1* already heads earlier releases *Historical selected release — <release>*. On the live page Alpha 1 heads them "Historical selection — TW-ALPHA-20260907.2" and "….1", so W6 adds a third heading style to Alpha 1. Normal; certain; cosmetic, nobody is misled about the current release; no.
- **L2.** *Canon and rulings relied on* cites HDE Governance §9.1.6's "Preserve predecessor advice when still applicable". HDE Build Notes 2.31 PF10-HDR-001 supersedes that sentence ("the preservation of predecessor advice"). D-17 and the unchanged header permission still justify carrying the block. Normal (record only); certain; no effect on any write; no.
- **L3.** No step opens a record pull request: X2 says "No pull request", and X5 and the failure path only push. So D26-B step 1's failure record never "reaches main, in a record pull request", PO-3's merge has no pull request to merge, and §A's cost of 7 counts that merge. Nathan's 2026-09-28 ruling allows a pull request that gates nothing. Both paths; certain; the record reaches main only if Nathan opens one himself; no.
- **L4.** K-5 cites "B's L14, accepted at G1", but L14 is a half-written selection page (§A risk 5). The four pages disagreeing exists only under Q1 (b), ruled after G1, so only this plan's approval accepts it. Also, the pre-reads of X4.4 to X4.6 run after W5, so a moved anchor on Alpha 1, HDE TW or the Hub stops the run only after the selection has moved. Running all four pre-reads before W5 would make those stops clean. Failure; low; pages disagree until Nathan acts (loud); no.
- **L5.** W5 sends two replacements in one call. The schema calls each pair an "operation" and does not say whether one failing fails the whole call. A half-written selection page is therefore possible: two current sections, or a status naming a release whose section is marked historical. The tool error or the readback stops the run, but no K-row names this case. Failure; low (the pre-read has just found both anchors once); loud; no.
- **L6.** X1.4's six fetches run "one after another" with no interval, so they can stop a healthy but slow duplication after W1. Also, "populated" (first line and last heading) and X1.8 never check the body after its last heading, so a copy that stalled inside its last section would pass. Normal and failure; low and very low; a needless stop, or a selected body missing part of its last section (K-6 covers only unedited paragraphs); no.
- **L7.** X1.8 has no positive check of the rejoined sentence, "Use PE's supported identity/header scheme" (41 characters, within the quoting limit). A leftover such as a double space would pass all eight checks. Normal; very low (the replacement is exact); cosmetic; no.
- **L8.** The seven-row comparisons in X4.3 and X4.4 are made by reading (K-4, K-7). A precondition in X1.0 that the selection page and Alpha 1 still show 2026-09-08T07:15, in a search that fetches no body (both do today; this is D9's method), would prove the rows unchanged with nothing to misread. Failure; low; a misread carries a stale row; yes, this is the check the last repair added.
- **L9.** For any watched-path commit other than 633ca5d, X4.1's "the terms of the change" are chosen at EXECUTE (PF-11). The drift check is therefore not mechanical once main moves again. Findings go to Nathan and do not stop the run. Normal; moderate (PF10 changed twice on 2026-09-29); a judgment call, recorded; no.
- **L10.** X5 names neither the *Harness files* disclosure for EXECUTE's body fetches (design §11.6, D22 condition 5, PF-13) nor the cost against EXECUTE's estimate with its stop at twice it (D26-D). The body carries both, and no validator check would see an omission. Normal; low; silent if omitted; no.
- **L11.** The values table says values are fixed "at X1.1", but «NEW» and «M» are fixed at X1.3 and X4.1. Across midnight, «V», «R» and "Selected: «D»" keep X1.1's date, by design. A restart before W1 re-runs X1.1 without saying whether §E's earlier values stand. A copy left untitled by a failure before W2, if not archived, is invisible to X1.0 (4)'s title search, so a later run would make a second copy. Edge and failure cases; low; only the last has an effect, an orphan copy; no.
- **L12.** X4.2 leaves the lineage block untouched. The published body's R2-1 fix, as CHECKPOINT §12.2 records it, has X4 "record both again". With A0's values unchanged the result is the same, and not re-recording avoids absorbing a change made after A0. Normal; certain; none; a note for GTWPE-MGMT-10's first repair; no.
- **L13.** On the selection page and Alpha 1, the kept 2026-09-08 section still opens "This current section supersedes earlier dated TW operational guidance below", now under its historical heading. Design §11.5 requires the text to be kept. Normal; certain; cosmetic; no.
- **L14.** X1.3's authority cites design D-16, which governs the selection. D-10 is the rule that permits the new sibling. Normal; certain; none; no.
- **L15.** HDE Governance §9.1.3 still says standard ChatGPT is required for live Notion mutation and prompt publication, and no HDE Build Notes addendum supersedes it. This plan, like P2(b), does both from a Claude Code session under G1's D-13 and D20-C. Normal; certain; none for this run: a pre-existing, workstream-wide canon gap for PE37; no.

## The claims

- **C1** does not hold as stated: RA-1 at every write, and L9.
- **C2** holds. W1 to W8 are the only writes, each within D-10 and D-16, Q1 (b) and this plan's approval. Nothing is written to a page outside them. L14 is a citation slip.
- **C3** holds, on D2's counts and on §A's and the cold run's account of the sentence. E3 leaves "Use PE's supported identity/header scheme", and X1.8 separates the expected wrong results (gaps in L6 and L7).
- **C4** holds on the four pages I could read. Every anchor occurs once, and a script found rows 1 to 7 equal to *ROWS*, character for character.
- **C5** holds, except RA-1 (a sweep can misstate a write that lands late) and RA-2 (a destructive rollback on two shared pages).
- **C6** holds.
- **C7** holds on design §11.4's text. The command runs and lists only 633ca5d (see L9 and L12).
- **C8** holds. No pull request gates anything, Q1 (b) reaches all four pages, and the pilot exercises the change prompt (see L3).
- **A5:** the plan does exactly what the ruling says. It updates the four current-version notes with the section-and-heading pattern Q1 (b) names, and nothing more.

**Reproduced from the committed text:**
- D1: main's validator, run on in-memory copies, exits 0 at PLANNED. At EXECUTING it refuses without plan approval and passes with it.
- D3, D4, D5 and D7: on the live pages, every anchor occurs once, the heading and child-page counts match, and the rows are equal.
- D8: a scoped, highlights-off search finds no page with the 092926.1 title.
- D9: all eight members show the table's edit times.
- D10: the command lists only 633ca5d.

**Not exercisable here:** D2 (I read no prompt body) and D6 (I did not fetch the Hub). RA-1 corrects D11.

## Canon relied on

- **AGENTS.md:** the canon-first rule, PF canon read-only, and the truncation guardrail.
- **HDE Governance (PF04 v2.8.6, origin/main 633ca5d):** §9.1.3 *Artifact storage and execution-surface selection* and §9.1.6 *Prompt ecosystem governance and provenance*, each read in full.
- **HDE Build Notes (PF10 v13.4.5):** 2.29 PF10-CANON-001, 2.31 PF10-HDR-001 and 2.34 PF10-VENDOR-001, each read in full. I scanned the addendum headings and a canon search for prompt-ecosystem, Notion and execution-surface rules; they found no other governing rule.
- **In-flight documents:**
  - MODIFICATION-20260929-gtwpe-pilot.md at ae5c84f, read whole.
  - GTWPE-DESIGN-v1.2.md on origin/docs/20260925-gtwpe-w1 (unchanged since d0e3f85): §11 whole, and §12 to §18.
  - CHECKPOINT.md §8 and §12.1 to §12.4.
  - pilot/COLD-RUN-ANALYZE-R1.md, searched for the sentence under repair.
- **Governing documents (origin/main):**
  - gcfpe.decision-record.md: D20, D21, D22, D24, D26, and the D23-G successor of 2026-09-23 on TW.
  - modification-template.md, ecosystem-change-management.md, notion-write-boundary.md, prompt-body-content-policy.md and modification_validate.py.
- **Also read:**
  - the `notion-update-page` and `notion-duplicate-page` tool schemas;
  - the installed tw-flowmaster SKILL.md, searched, with its selected-catalog profile read. It resolves members by reading the selection page, so §A's "unaffected" holds.

## What this review did

- **Notion:** I fetched only the four permitted control pages (the selection page, Alpha 1, HDE TW and the GTWPE catalog), each returned inline. I ran two searches with highlights off. I fetched no prompt page and not the Hub, and made no Notion write.
- **Git:** read-only commands only (show, log, grep, ls-tree, rev-parse, merge-base, diff --stat, branch -a), and no fetch. I also ran one `git status --porcelain` on one directory, which may refresh git's index stat cache.
- **Scripts:**
  - main's validator, run from its blob on stdin against process-substituted copies, with PYTHONDONTWRITEBYTECODE=1;
  - one inline Python comparison of the plan's texts with the fetched page text, standard library only.
- **Files:** I wrote none, and no harness save appeared. My transcript holds control pages, the record and the design, and no prompt body.

DECISION NEEDED
