---
artifact_type: PE_WORK_RECORD
created_date: 2026-09-24
session: PE37 (`session_018teDumz2XyKdoXF9p3BKFM`)
task: docs/ephemeral/pe37.stage5/TASK-01-stage5-process-fix.md, §6
page: Notion 3e34590a05eb811b93d2da9b4ef8106d, GCFPE-MGMT-10 PROPOSED BODY (D20 redesign)
---

# The MGMT-10 proposed body, revised for D26

**The page was revised in place on 2026-09-24 at 11:00Z, with 22 search-and-replace edits, and all
22 were read back from the page as written.** It is not live: the live `091426.1` body, the
register, the registry and the graph are untouched. Before this revision the page had last been
edited on 2026-09-23 at 00:49Z. Notion page history holds that version.

**Read disclosure (`D22` condition 5).** The body was read twice through the Notion connector, once
before editing and once to read it back. Both reads were into the session's context only. No file
was made, and nothing was copied, hashed or stored.

## What D26 put into the body

| Where | Change |
|---|---|
| Spine › *Scope freezes* | "This is what bounds review loops…" becomes "It bounds scope, not review rounds. *Reviews are bounded*, below, bounds those (`D26`)." |
| Spine › new *Reviews are bounded (`D26`)* | the five rules of D26-A, the second review brief, the `reviews` ledger, and D26-F's multi-agent mode |
| Spine › *One session* | resume only at checkpoints (D26-C); within a session, keep what is safe after compaction |
| Spine › *The record* | upstream findings return to Nathan with a `DECISION NEEDED` (template rule 1); the format 2.1 transition |
| Spine › *Failure contract* | a pointer to D26-B |
| `ANALYZE` | `interaction_cost` counts `ANALYZE` and `PLAN` review rounds; the `estimate` (D26-D) |
| `PLAN` | normal path mechanical; the old-text search (D26-E); the failure-path ending (D26-B); dry run first and the cap; returned with open findings listed and the estimate restated; a stopped plan resumes as a successor section |
| `EXECUTE` | the D22 carve-out and the failure procedure (D26-B); `NOT_RUN` after a stop; waiting for Nathan's merges and installs |
| *Read these* | adds `reviewer-prompt-template.md`; *session-working-rules* now names *loops* |

## The census's twelve contradictions

From `docs/ephemeral/modifications/evidence/closeout-residuals/ANALYZE-anchor-census.md`, *The
proposed MGMT-10 body*, in its order.

| # | Contradiction | Resolution |
|---|---|---|
| 1 | `ANALYZE` "Must not: change anything", yet it commits its section | **Resolved.** "Must not: change anything outside its own section of the record, its frontmatter fields and its evidence files" |
| 2 | `PLAN` "Must not: apply anything", yet it commits its plan | **Resolved.** "apply anything outside its own section of the record and its evidence files" |
| 3 | "reads and writes exactly one Modification" against `ANALYZE`'s "change anything" | **Resolved** by 1, and by *The record* now saying each mode writes its own section, frontmatter fields and evidence files |
| 4 | `EXECUTE`'s "new scope becomes a new Modification": writer unstated, against "exactly one" | **Resolved.** The mode records a finding and returns to Nathan; a later triage or `ANALYZE` run creates the new record with `spawned_from`. *The record* says the same |
| 5 | Result routing has no code for a mode returned pending approval; one session can span modes | **Resolved.** New result `PRODUCT_OWNER_ACTION_PENDING`, not terminal; one result per return, once per mode |
| 6 | "Every artifact is … Markdown under `docs/ephemeral/`" misses graph parts and rule changes | **Resolved.** The sentence names all three writable paths and what goes in each |
| 7 | Raw-request `ANALYZE` has no id, yet the prompt says find the Modification by its id | **Resolved.** For a raw request, `ANALYZE` creates the file from the template at format 2.1 and opens `docs/<yyyymmdd>-modification-<slug>`, which the find rule searches |
| 8 | "An open pull request is a complete outcome" against `ECOSYSTEM_CHANGE_COMPLETE` | **Resolved.** An open pull request completes a mode's return; the change is complete only when `EXECUTE` has verified what landed |
| 9 | Post-install verification cannot finish inside `EXECUTE`, which stops at install | **Resolved.** `EXECUTE` returns `PRODUCT_OWNER_ACTION_PENDING` at a merge or install, then continues from that checkpoint on `main` and closes with the digest comparison |
| 10 | Native purpose excludes release selection, while `PLAN` moves registry rows | **Resolved.** Moving the graph part and registry row of a prompt the Modification edits is part of the change (`D20-B`); choosing what a release selects is not |
| 11 | Who writes `analyze_approved_by` / `plan_approved_by` when modes chain | **Resolved.** The session writes them, only on Nathan's approval, with his words quoted; never from a merge or silence |
| 12 | The page's YAML governance state against "a body carries behaviour, never governance state" | **Resolved.** The preamble now says the block and preamble are page state, and the body begins below the rule |

**Deferred by name, with reasons:**
- **The registry row.** `PRODUCT_OWNER_ACTION_PENDING` is a new result code. The live `GCFPE-MGMT-10`
  registry row and graph part declare three results. They move at promotion (stages 2–3), when this
  body becomes live, because nothing live changes in stage 5.
- **The census's A1–A5 on this page.** The census lists this page as carrying A1–A5 by effect. By
  reading the page, none of R-ITEM40's literal patterns occurs in it before or after this revision.
  A5's effect, a storage sentence that leaves out `docs/prompt_ecosystem_management/`, is resolved
  by contradiction 6. Nothing further is edited here, so PART-11's verification is the check.

## ITEM-23 and ITEM-40, in step with the follow-up

The follow-up's PART-11 planned two edits to this page, and both are applied here exactly as its
engine defines them (`…/closeout-residuals/plan/engine/`):

| Rule | Engine definition | Applied |
|---|---|---|
| `R-ITEM23` | delete each `Prompt version:` / `Ecosystem release:` / `Set:` label line; expected 2 on this page | the two lines `Prompt version: *(stamped at promotion)*` and `Ecosystem release: *(stamped at promotion)*` deleted |
| `LGCFPE-MGMT-10-PROPOSED-1` | replace "are left unstamped on purpose — those are set when the register promotes it" with its `new_text` | replaced, verbatim |

**The gates, by reading the page back:** `R-ITEM23-gate` reads 0 (no line begins with one of the
three labels followed by a colon) and `R-ITEM40` reads 0. This check was done by reading, not by
running the engine. `D22` allows a transient read file but not a retyped body, and the connector
returns the body only into context. PART-11's own verification in the resumed plan is the
mechanical check.

**What the resumed plan must say:** PART-11 is **verified, not applied**. Its `R-ITEM23` expects 2
matches on this page and will now find 0. The resumed plan records that difference as the result
of stage 5, not as a defect (`RESUME-PROCEDURE.md`, step 3).

## What this revision does not do

It does not promote the body, change its testing approval, or change the register, the registry
row, the graph part or the live `091426.1` body. Nathan's `APPROVED_FOR_TESTING` of 2026-09-22 was
given to the earlier text, and the page's status block now says so (`revised_stage5`).
