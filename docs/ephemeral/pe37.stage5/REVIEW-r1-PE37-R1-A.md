1 distinct confirmed REQUIRED finding.

---
artifact_type: REVIEW_RECORD
reviewer: PE37-R1-A (fresh-context subagent, brief docs/ephemeral/pe37.stage5/REVIEW-BRIEF-r1.md @ 772d9f7)
reviewed: stage 5 rule package, git diff 4c57d92 dc023a5, plus Notion page 3e34590a05eb811b93d2da9b4ef8106d
round: full review 1 of at most 2 (D26-A)
date: 2026-09-24
---

# Stage 5, review round 1: PE37-R1-A

**Answer.** There is one required finding. `RESUME-PROCEDURE.md` step 3 keeps "the 19 Notion edits" as
they stand, and changes only PART-11's proposed-page step. Taken literally, the resumed plan then
still writes `PART-11-TRACK-01`. That edit puts a dated paragraph on the redesign tracking page
saying the proposed body's twelve contradictions "are not resolved" and "wait for stage 5". Stage 5
has now resolved them. The write's anchor is still present, and its only check is a readback, so it
lands without any warning. Claims C2, C3, C4, C5 and C7 held when I reproduced them. C1 and C6 hold
with the LISTED gaps below.

**What I ran.** I extracted `dc023a5`'s `docs/prompt_ecosystem_management` and `docs/ephemeral` to a
scratch directory, with `PYTHONDONTWRITEBYTECODE=1`, and ran these:
- The selftest passed 64/64.
- The four Modification records passed 4/4.
- `guard_proof.py`: every check fires (17, 8, 3, 3, 2 and 1 failing cases, and 16 for `_d26_checks`).
- Each of the 11 `edits.json` anchors counts 1.

I read the MGMT-10 proposed page and the tracking page `3e34590a05eb81e7927efe0541258916` through
the Notion connector, into context only. I made no file of either and did not hash or store them.

## REQUIRED

### RQ-1: R2, a silent wrong edit to a control page (normal path)

- **Exact text.** `RESUME-PROCEDURE.md`, step 3 in detail, item 2:
  - "**the content as it stands:** … the 11 repository texts and the 19 Notion edits";
  - "**PART-11 is verified, not applied.** … PART-11's step becomes a check that `R-ITEM23-gate`
    and `R-ITEM40` read 0."
- **Evidence.**
  - The stopped Modification's §P has two PART-11 steps
    (`MODIFICATION-20260923-closeout-residuals.md:849-850`):
    - step 18, the proposed MGMT-10 body;
    - step 19, "Notion: the D20 redesign tracking page | `PART-11-TRACK-01` (spec §7.3; X5.6) |
      Decision 11 | readback".
  - The procedure turns only step 18 into a check. It keeps `PART-11-TRACK-01` among "the 19 Notion
    edits". Of the 24 in `plan/notion/edits.json`, 5 are stop-only machinery, which leaves 19.
  - Its `new_str` (`plan/notion/edits.json`, id `PART-11-TRACK-01`) says three things:
    - "input for stage 5 — the proposed body's design-level contradictions";
    - "**They are not resolved by that Modification** … so they wait for stage 5. That Modification
      changes the proposed body only to remove the classes it removes";
    - then it lists the contradictions as open.
  - Stage 5 has now resolved all twelve and applied ITEM-23 and ITEM-40 itself
    (`MGMT-10-REVISION.md`). I confirmed this on the page.
  - The edit's `old_str`, "**The three decisions below are recorded as", still occurs once on the
    tracking page as fetched. So a fresh-fetch dry run passes it.
  - Its verification is readback only. Step 3.5's diff check covers the successor's diff, which does
    not contain the edit.
- **Path, likelihood and consequence.**
  - Path: the normal path.
  - Likelihood: high. The procedure tells the session to keep the edit. It is only missed if the
    session happens to read "PART-11 is verified, not applied" as covering both steps.
  - Consequence: the tracking page is the redesign's status page. It would then carry a new dated
    claim, false when written, that the MGMT-10 body's contradictions are open and that the
    follow-up edits the proposed body. A successor reading it could reopen stage 5 work or re-edit
    the page. Nothing flags it.
- **Smallest correction.** In step 3 item 2, add one line: "`PART-11-TRACK-01` (§P step 19) is
  withdrawn: stage 5 resolved the contradictions it records as open
  (`docs/ephemeral/pe37.stage5/MGMT-10-REVISION.md`). That leaves 18 Notion edits." Optionally,
  replace it with a line that records the resolution.
- **In text the last repair added?** No. It is in `RESUME-PROCEDURE.md` as added in `a8f752f`. The
  last repair, `dc023a5`, touched only the waiver attribution.

## LISTED

- **L1 (normal path, certain, loud).** Three of the 19 Notion edits have lost their anchors on the
  tracking page, so step 3.4's fresh-fetch dry run fails. This is D26-F trigger 2, and the plan
  returns to Nathan before approval. The procedure does not anticipate it.
  - `TRACK-STATUS-01` looks for `FOLLOW_UP_MODIFICATION_AT_INTAKE`. The status now reads
    `STAGE_5_PROCESS_FIX_IN_PROGRESS_PE37`.
  - `TRACK-STATUS-02` looks for "which is at `INTAKE` with `ANALYZE` in progress", which is gone.
  - `TRACK-STATUS-03` looks for "`INTAKE`, branch". The row now reads "`PLANNED`, not approved".
  - Not in the last repair's text.
- **L2 (failure path, low, possibly silent).** On the MGMT-10 page, EXECUTE's "undo its repository
  steps" can reach another part's work. One text commit (X2.2) carries several parts' texts; one
  entry, `P29-D25`, holds both D25-A (PART-06) and D25-B (PART-05). "Undo" is not defined for a
  shared commit. For this run, `RESUME-PROCEDURE.md` step 5.1 sends the likeliest pre-write failure,
  a D24 rejection, back to Nathan. Not in the last repair's text.
- **L3 (documentation).** D26 says "It reopens none of D20, D21, D22, D23 or D24 otherwise", but
  D26-B is a carve-out from D21-B. Unlike D20, neither D21 nor D24 condition 5 carries a pointer to
  D26. This is deliberate for D24, where the D25 anchor is at stake, but a reader of D21-B or D24
  alone sees the old rule. Claim C1 ("supersedes only …") also leaves out DISP-001, which D26
  itself lists. Not in the last repair's text.
- **L4 (documentation, D26-E on the package itself).** Old text survives in
  `modification_validate.py:464`: "scope freeze is the rule that bounds the review loops". D26
  supersedes it. Not in the last repair's text.
- **L5 (validator, low).** A record that states a format below 2.1 escapes the D26 checks without
  warning. `format: "2"`, `"2.0"` and `"1.0"` all parse to a version below (2, 1). C2 still holds,
  because it is about records with no format. Not in the last repair's text.
- **L6 (validator, loud).** The SKILL cap counts full rounds per Modification. D26-A says two
  *consecutive* `SKILL_REPAIR_REQUIRED` rounds. A Modification with two separately reviewed
  packages, both approved, fails validation at a third round and needs a `review_cap` override.
  Not in the last repair's text.
- **L7 (validator, loud).** A PLAN `DRY_RUN` row that is malformed in one field reports a shape
  error and also a misleading "DRY RUN FIRST". Dry-run-first is guarded only for PLAN. D26-A rule 1
  applies to ANALYZE and skill reviews too, and D26's list of unguarded behaviours does not name
  that gap. Not in the last repair's text.
- **L8 (template).** Rule 8 says non-required findings are "listed in §P as an accepted risk". For
  an ANALYZE review, that conflicts with rule 1, under which ANALYZE writes only its own section.
  Not in the last repair's text.
- **L9 (template).** Rule 5's `NOT_RUN` is not in the disposition vocabulary
  (`APPLIED VERIFIED BLOCKED NOT_APPLICABLE`). Only item dispositions are validated, and only at
  COMPLETE, so this shows up late and loudly if at all. Not in the last repair's text.
- **L10 (resume, R3 considered and refuted).** The kickoff calls the page "approved for testing".
  That approval (2026-09-22) predates the stage 5 revision, and no step asks Nathan to re-approve
  the page for testing. It is disclosed in the page's `revised_stage5` line and in
  `MGMT-10-REVISION.md`, and the task brief Nathan authorized directs this session. So it is not
  silent. Not in the last repair's text.
- **L11 (resume).** `MGMT-10-REVISION.md` and the resume procedure's authority cite `TASK-01`. That
  file exists only on the unmerged PR #480, and no step makes merging it a prerequisite. C6's list
  also leaves out the stage 5 review and report before step 1. Not in the last repair's text.
- **L12 (parked plan).** `plan/skills/fill_brief.py` stamps `reviewer-prompt-template.md v1.1` into
  the D24 brief it writes, and the template is now 1.2. The skill template block itself is
  unchanged, so this is cosmetic. Not in the last repair's text.
- **L13 (MGMT-10 page).** "Must not: change anything outside its own section …" in ANALYZE sits
  beside ANALYZE creating the whole record file and branch for a raw request. PLAN's "Input is …
  nothing else" sits beside the kickoff's second input, `RESUME-PROCEDURE.md`. Both are minor
  residues of census items 1 and 7. Not in the last repair's text.

## The attack list, disposed

- **A1.** After the first external write, the page sends every failure down D26-B's path, stated
  twice, so I found no silent path to carrying on. Before it, see L2.
- **A2.** The deferral holds. Nothing live consumes `PRODUCT_OWNER_ACTION_PENDING`. The page says it
  hands off to no prompt and selects nothing, and the parked `land.py` checks only gates for
  `GCFPE-MGMT-10-PROPOSED`.
- **A3.** Within D26-A, which sets a maximum, not a minimum, and within decision 2 (revised): "one
  fresh rehearsal … No review loop". One diff check is not a loop. RQ-1 is the gap that having no
  full review leaves uncaught.
- **A4.** Nothing substantive goes beyond the recovery analysis §7 or the task brief §1. D26-A rule
  6 drops the analysis's words "that Nathan approved", which only makes it stricter. See L3.
- **A5.** `_waived` and the order of the ledger checks behave as documented. A row that is
  well-formed except for one field is excluded from the caps but reported loudly. `estimate` is
  required at ANALYZED through COMPLETE and not at terminal states, as the brief asks. No legacy
  record fails. See L5–L7.
- **A6.** `canon.py` and `registry/guard_tests.py` read only the D23-E successor, which is
  unchanged. `apply_texts.py` does not assume D24 ends the file. All 11 anchors count 1, and so do
  the anchors of X5.2 and close. I found no broken assertion.

IN FLIGHT
