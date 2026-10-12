1 distinct confirmed REQUIRED finding.

# REVIEW-ANALYZE-DIFF — the one DIFF_CHECK of the ANALYZE repair, MODIFICATION-20261011-gcfpe-mb008-to-promotion

Reviewer: REVIEWER-ANALYZE-DIFF-C. I am not the author, and I was not reviewer A or reviewer B.
- **Brief:** `BRIEF-ANALYZE-DIFF.md` at `7a4465e7`.
- **Rubric and cap:** `BRIEF-ANALYZE-1-A.md` §3 and §5, applied unchanged.
- **What I checked:** `git diff 978d233e 90ccb082`, limited to the record and `scope-measurement.md`.
- **Canon:** `main` at `9312add2`.
- **Date:** 2026-10-11.

**Answer.** All three round-1 required findings are fixed: R-A1, B-1 and B-2.

One required defect remains in the repaired text. DN-B option 1, the recommended option, gives every session that emits a handoff a new Notion write under D28, and the record never mentions D25:
- D25-A limits CL-40 to the Candidate CRD Items List: CL-40 "writes no other Notion page".
- D25-B fixes the only exceptions to the read-only claims on nine handoff-emitting rows: "Nothing else is excluded."

The record targets no successor to D25, so adopting option 1 as written breaches D25 without anyone being told. The defect was already present, in substance, in round 1's option B2, and neither round-1 reviewer raised it. The repair rewrote that paragraph and kept it.

The count of distinct required defects went from 3 to 1, which more than halves. I list 13 further observations as LISTED.

## Disposition of the round-1 required findings

| Finding | Disposition | Basis |
|---|---|---|
| **R-A1** (R3) | **Fixed** | A-1 (record line 121) names D23-B, C-PLACE and C-ART. It puts the reading and the surface advice in the output artifact, and the line before the block names the cell, the flags and the artifact path. DN-B option 3 (line 143) carries a D23 successor for C-PLACE, and PART-02's rule targets name it (line 94). `scope-measurement.md` §2a-bis lists the places these texts are restated. I verified every skill line it cites against the installed trees, whose digests match `source-identities.md`: change-flow `SKILL.md:299`; glow-hde-pr-development `:170` (C-ART) and `:174`; session-relay-flowmaster `:285`; governance audit `:39` and `:40`. All four of reviewer A's corrections are applied. |
| **B-1** (R1) | **Fixed** | The repair separates surface advice from the reading in: the summary (line 47); §A.3 (line 82); ITEM-03; PART-02's name; §A.5 (lines 111–112); A-1. `scope-measurement.md` §2a re-dispositions change-flow `:301`, `validate_flowmaster.py:364` (verified: "surface/model/reasoning recommendation") and `epic-reengineering-interoperability.md:54–56`. Reviewer B suggested putting surface advice "beside the handoff". The repair puts it in the artifact instead, a consequence of the R-A1 fix that the record states. Gaps in the list of suppressing lines are listed below (L-C5 to L-C8). |
| **B-2** (R3) | **Fixed, with a new defect** | DN-B (lines 140–143) no longer says "as built". It replaces the skill's step 3, keeps the reading out of the block, and limits D28 to exactly three writes: create the row; correct it after a failed readback; set *Nathan's pick*. It says who sets the pick. I checked this against typesafe-scoring `SKILL.md` (freeze digest `3 088c77f3…`), steps 3–5. `scripts/score.py` makes no Notion call, so option 2's "without the Notion row" is feasible. The new defect, DIFF-C1, sits in the same rewritten option 1 and D28 text. |

## REQUIRED

### DIFF-C1 — R3: Option 1 and D28 give CL-40 and the read-only bodies a Notion write that D25 rules out, and no D25 successor is targeted

**Classification.**
- **Rubric class:** R3, a silent breach of a Product Owner ruling. Secondarily R2, if PLAN rewords the texts that apply D25 so that they fit.
- **Path:** normal. It is the recommended path: Nathan chooses option 1, and PLAN applies PART-02 to the 53 bodies.
- **Likelihood:**
  - High that the conflict arises. CL-40 is one of the 53 bodies: `body-scan.json` counts 3 `NEXT_PROMPT_HANDOFF` literals on it, and `closure-candidate.md` shows its own continuation edge.
  - Medium that it is then resolved without anyone being told:
    - The record says option 1 needs only D28, and that "D23-B, C-PLACE and C-ART stay as written".
    - The rule targets name only D28 and, under option 3, a D23 successor.
    - Scope freezes at approval.
    - D25 itself records that a destination rule has "no check that fires" (decision record line 1689).
- **In text the last repair added:** yes in wording: option 1 (line 141), the PART-02 row (line 94) and §2a-bis. In substance it was carried over from round 1's B2, "each handoff-emitting session runs the skill as built, including its uses-table row", which neither reviewer raised.

**The exact text.**
- Line 141: "It also creates the reading's row in the TypeSafe uses table, and corrects that row only after a failed readback … That needs a destination rule, **D28**, recorded before EXECUTE, authorizing exactly those three writes in that one data source and no other (`notion-write-boundary.md`). It would be the first broad Notion write by flow sessions since the 2026-09-22 policy. D23-B, C-PLACE and C-ART stay as written."
- Line 94: "rule: D28 under DN-B option 1 or 3, and a D23 successor under option 3".

**The evidence.**
1. **D25-A, the ruling.**
   - `gcfpe.decision-record.md:1643`: "Under it, `CL-40` updates the page in place with each change's new CRD candidates, and writes no other Notion page."
   - Its consequences, `:1668`: "no other flow prompt gains a Notion write."
   - `notion-write-boundary.md:111` restates "writes no other Notion page" and "authorizes `CL-40` alone".
2. **CL-40's candidate registry row.** In `docs/ephemeral/modifications/evidence/20261009-gcfpe-latest-alpha-analysis/execute/candidate-registry-nonderived.json`, CL-40 at 100926.1 has `mutations.allowed`: "Update the Notion page Candidate CRD Items List in place with this change's new CRD candidates, and no other Notion page; …". It is the only row of the 55 that has any Notion mutation.
3. **CL-40's candidate body.** I read it fresh: page `3f44590a05eb8155934dd1c4c2b5d1eb`, last edited 2026-10-09T20:11:12.358Z, equal to `body-scan.json`. It says:
   - "This prompt is read-only except for the bounded runtime exception below for the existing noncanonical Candidate CRD Items List."
   - "… it is the list's only store, and this prompt writes to it only as this section directs."
4. **The row is a Notion page.** The uses table is a Notion database, and the skill's step 4 writes the printed "Notion row" object "as the page properties".
5. **D25-B, the same pattern on more rows.**
   - `gcfpe.decision-record.md:1656` fixes the only exceptions to a body's read-only claim, its own committed artifacts and their pull request: "Nothing else is excluded. Every other limit a body states on what it may change still holds."
   - Nine handoff-emitting candidate rows pin that scoping sentence: CL-20, CL-30, CL-40, CL-E-20, DOC-20, ESC-25, PR-20, PR-40 and QA-10. GCFPE-MGMT-10 and PR-50 also pin it, but they emit no handoff.
   - Option 1 adds a Notion write to all nine.
6. **The record never mentions D25.** Searching the record at both `978d233e` and `90ccb082` finds no "D25" and no "Candidate CRD". §2a-bis lists only C-PLACE, C-ART and D23-B as texts the placement must keep.

**Consequence.** Under option 1, PLAN must give CL-40 the row write. It then does one of two things, and neither is flagged:
- **It leaves CL-40's body and registry row saying CL-40 writes only the Candidate CRD list.** A running CL-40 then either skips the row, so the pick for its handoff is never recorded with the reading as PF10 2.1 rule 2 requires, or writes against its own text.
- **It rewrites CL-40's D25-A text, its registry mutation and the nine D25-B read-only claims.** No D25 successor is recorded, and Nathan has been told only that D28 is needed.

Because D25 records no check that fires, a runtime breach is not caught either way.

**Smallest correction.** In DN-B options 1 and 3, the PART-02 row and §2a-bis:
1. Add D25-A and D25-B to §2a-bis as texts the placement must keep or amend:
   - D25-A: CL-40's "writes no other Notion page", its registry mutation and its read-only line;
   - D25-B: "Nothing else is excluded", on the nine rows.
2. State in options 1 and 3 how D28 relates to them, as one of two choices:
   - (a) D28 is recorded as a D25 successor that names CL-40's limit and those read-only claims, and CL-40's mutation and the boundary row are updated with it; or
   - (b) CL-40, and the nine read-only bodies if preferred, create no row and record the reading as under option 2.
3. Add choice (a) to PART-02's rule targets for options 1 and 3. Option 2 is unaffected.

## LISTED

One line each, with path, likelihood and consequence. "Repair" marks a line in text the repair added.

- **L-C1 (R-A1; repair).** The line before the block shows "the cell, the flags" but no probabilities. That is not a breach: C-PLACE allows naming what was produced, and the artifact holds the full reading. But the skill's *What not to do* says "Do not paraphrase a reading, … or omit a probability", and PF10 2.1 rule 2 says "as the skill prints it". Normal path; medium likelihood. Consequence: Nathan may pick from a headline. Naming only the reading and its path, as reviewer A's correction did, avoids this.
- **L-C2 (R-A1; repair; refines L-B4).** "The line before the block" can be read as the line immediately before it. `session-working-rules.md` §2 reserves that line for the named state, and C-PLACE's variant gives it to `ASK OK?` in five bodies (QA-50, QA-60, QA-80, RS-10, RS-30). Normal path; medium likelihood. Consequence: two rules claim one line. "One of the few lines before the block" avoids it.
- **L-C3 (R-A1; repair).** §10 says §2a-bis "lists every place the texts are restated". It omits glow-hde-pr-development `scripts/validate_glow_hde_pr_development.py:85` ("never carries the only copy") and the registry pins of C-ART and of C-PLACE's first sentence on 53 rows. No consequence: C-ART is kept in every option, and option 3 amends C-PLACE's second sentence, which nothing pins.
- **L-C4 (R-A1 and B-2; repair).** §2a-bis omits C-NOTION. It is carried by PR-10, PR-20, PR-30, PR-40, OPS-10, OPS-20, OPS-30, QA-10 and the relay (`SKILL.md:274`): Notion holds "the maintenance surfaces a destination rule names; this prompt … writes to it only where its task instruction directs a write". Under option 1 the uses table becomes a destination for flow sessions. Class B wording; normal path; low likelihood. Consequence: wording that PLAN must reconcile.
- **L-C5 (B-1; repair).** §A.5 names only change-flow `:301` and `validate_flowmaster.py:364` as suppressing surface advice.
  - By the repair's own test (the terms "capability appraisal" and "eligibility/suitability"), session-relay-flowmaster `:283`, the audit's `SKILL.md:41` and `interoperability-contracts.md:56` qualify too.
  - flowmaster-validate `SKILL.md:161` is covered only by "Conflicts the same way".
  - Normal path; medium likelihood. Consequence: the audit flags the surface rule, which is a loud failure, and D26-E's sweep should catch it.
  - The skills' broad match did not include `surface`, `eligib`, `suitab` or `capabilit`. My own run of those stems over the five skills found no further suppressing line.
- **L-C6 (B-1; repair).** §A.5 now says "no page gives AI advice or surface advice". The body scan had no class for surface advice: T3 covers model, reasoning or effort only, and T6 sentences are counted but not quoted. Surface advice can also be written without any of the scan's stems. The evidence does not support this claim. Low likelihood; PLAN's fresh reads would find any surface advice that exists.
- **L-C7 (B-1; repair).** The texts that most directly put surface outside the bodies are not named. They are the T5 sentences on PR-10, PR-20, PR-30, PR-35 and PR-40, for example "Runtime surface, configuration, available tools and channel selection are operator decisions outside this reusable prompt". The record names the T1 sentences instead. Normal path; low likelihood. Consequence: a body that both disclaims surface and gives surface advice.
- **L-C8 (B-1; repair).** Two counts are stale or overstated. Cosmetic.
  - §A.5 still says "6 conflicting lines in 5 skills", although §2a now marks `validate_flowmaster.py:359–366` as "Partly conflicts".
  - A-1's "five skills forbid both" overstates glow-hde-pr-development `:184`, which names no eligibility, suitability or capability term.
- **L-C9 (B-1; repair).** The dispositions shorten rule 3 to "an agent's own model or reasoning recommendation". Rule 3 forbids any "recommendation, assessment or ranking of model, reasoning level or effort". Normal path; low likelihood. Consequence: a rewrite of change-flow `:301` to the short form drops assessment, ranking and effort.
- **L-C10 (B-2; repair).** "Tell any session your pick and it sets that one field" puts no bound on which session. It includes a session outside GCFPE, and the producing session after its handoff, against D23's clarification rule 3, "A prompt's job ends at the handoff". D28's set of actors is unstated. Low likelihood; Nathan's own instruction authorizes the write.
- **L-C11 (B-2; carried from round 1's B1).** Option 2 records the pick in the receiving session's artifact and the reading in the producing session's. Rule 2's "the pick is recorded with the reading" then holds only by cross-reference. Arises only if option 2 is chosen; low likelihood.
- **L-C12 (repair).** PART-02 stays class B, yet options 1 and 3 need D28, and option 3 also a D23 successor. `ecosystem-change-management.md` §6 calls new settled behaviour a Class A rule change. The point is visible to Nathan in DN-B; the label is wrong only if option 1 or 3 is chosen. The same kind of finding as L-A4 and L-B7.
- **L-C13 (B-1; repair).** Surface advice reaches Nathan only through the artifact path. The line before the block names the cell, the flags and the path, but not the advice. PF04 §9.1.3, "Every downstream-session prompt must receive … advice for execution surface", is met only if "receive" covers an artifact the handoff names. Visible; low likelihood.

## Checks run, and checks not run

**Read in full.**
- This brief.
- `BRIEF-ANALYZE-1-A.md`, including §3 and §5.
- Both round-1 reviewer records.
- The diff.
- At `90ccb082`: the complete repaired record, `scope-measurement.md`, `worker-brief.md` and `body-scan.json`.

**Canon at `9312add2`.**
- PF10 v13.5.2, complete: 13,583 B, sha256 `c53dac75…`, ending at `<eof>`.
- PF04 v2.8.7, §9.1.2 to §9.1.6, with §9.1.3 in full.

**Controls read.**
- The decision record:
  - D23: its rulings, its clarification and its successors;
  - D25, in full;
  - D26-A.
- `notion-write-boundary.md`.
- `session-working-rules.md` §2.
- `ecosystem-change-management.md` §6.
- `MODIFICATION-20260923-alpha-feedback-open-entries`: its canonical wording (C-NOTION, C-ART, C-HANDOFF, C-PLACE) and its step table.
- `EXECUTION-SPEC-20260923-closeout-residuals` §3.2.
- CL-40's row in the selected registry and in the candidate registry.

**Reproduced.**
- `freeze.py` over six installed skills (change-flow, flowmaster-validate, glow-hde-pr-development, session-relay-flowmaster, the governance audit, typesafe-scoring): all match `source-identities.md`.
- Every skill line the repair cites: verified line by line.
- A grep of the five skills for C-PLACE, C-ART and surface-related stems.
- `body-scan.json`:
  - the handoff preamble on 54 pages, which is 53 members plus PE;
  - T1–T6 totals of 10, 31, 0, 0, 17 and 119.
- The candidate registry:
  - 53 rows pin C-ART;
  - 11 rows pin D25-B's scoping sentence, 9 of them handoff-emitting;
  - only CL-40 has a Notion mutation.
- typesafe-scoring `SKILL.md` and `score.py`: steps 3–5, and no Notion call in the script.
- `modification_validate.py`, with `PYTHONDONTWRITEBYTECODE=1`: the record passes; 16 of 16 records pass.
- **Fresh Notion read:** CL-40's candidate body, one fetch, returned inline.

**Not run.**
- Closure, the builds, the contract probe, and the other seven digests. They are outside the diff, and both round-1 reviewers reproduced them.
- No other Notion page was read.
- I did not check whether PE carries C-ART.
- For the nine D25-B bodies I checked the registry pins, not the body sentences in Notion.

**D22.** I made one prompt-body fetch. It returned inline, and nothing was copied, saved or hashed. My scratchpad held only repository files (the diff and `body-scan.json`), and I deleted them. I did not open the workers' transient files.

**Canon relied on:**
- `AGENTS.md`, the canon-first rule.
- PF10-HDE-Build-Notes v13.5.2, complete; addendum 2.1, rules 1–5 and its superseded-passages table.
- PF04-Canon-HDE-Governance v2.8.7, §9.1.2, §9.1.3 (in full), §9.1.4, §9.1.5 and §9.1.6.
- In-flight: the record under review and its evidence; `MODIFICATION-20260923-alpha-feedback-open-entries` §P; `EXECUTION-SPEC-20260923-closeout-residuals` §3.2.
- Controls: `gcfpe.decision-record.md` D23, D25 and D26-A; `notion-write-boundary.md`; `session-working-rules.md`; `ecosystem-change-management.md` §6; `project-prompt-contract-registry.md` and the candidate registry; `modification_validate.py`.

**DECISION NEEDED.** This was the last review D26-A allows for ANALYZE. Nathan decides two things:
1. Whether to accept DIFF-C1 as a risk, or to opt into its correction, which is priced as another round.
2. DN-A to DN-F.

Every open finding goes with it: DIFF-C1, round 1's 33 LISTED findings and the 13 above.
