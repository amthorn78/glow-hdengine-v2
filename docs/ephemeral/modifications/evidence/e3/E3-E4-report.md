# E3 and E4 report — Amendment 1 (spec v2 §0, §3, §7, §9)

Run 2026-09-23 on the execution branch working tree (E1 `ce7e5cd`, E2 `83794d3`, nothing committed by this
stage), the edited skill tree `/tmp/claude-0/e2/skills` and the working-tree registry. Every command ran with
`PYTHONDONTWRITEBYTECODE=1`; no `__pycache__` was created.

**Corpus policy (D22).** The 55 bodies were read from Notion fetch results by the session extractor and piped
in memory. No body, fragment or body hash is written here or anywhere. The only body words in this file are
the matched guard phrases of at most 12 words that §E asks for on clean-control hits. Section numbers
("section #n") count the body's headings from the top; they name a place without quoting it.

**Scripts** (committed with the evidence, reviewed in E5):
- `docs/ephemeral/modifications/evidence/e3/body_rules.py` — the E3 body rules. Canonical texts are read
  verbatim from §3's code blocks; anchors are regexes. `apply(bodies)` returns the edited bodies and a per-body report.
- `docs/ephemeral/modifications/evidence/e3/run_e4.py` — E4 items 7, 8 and 9, in memory.

Command: `<bodies JSON> | PYTHONDONTWRITEBYTECODE=1 python3 run_e4.py /tmp/claude-0/e2/skills`

## Verdict

- **Item 7 passes:** the validator ran with all 55 bodies validated, `ok: true`, `errors: []` and `prompt_body_checks_not_evaluated: []`.
- **Item 8 fails on 14 rows (16 findings).** None comes from a canonical text. Each one is a pre-existing body phrase that a forbidden guard catches (see "Clean-control hits"). Under §12 they are not exempted, and they go to Nathan.
- **Item 9 passes:** 43 of 43 regressions produced exactly their own finding. G27's clean control on today's unedited PR-20 produced its finding. Role parity and its two negative controls behave as expected.
- **Items 1–6 and 10 did not move:** they are identical to E2.
- **Four placements could not be made by pattern:** C-PR30-ENTRY, the old `ASK OK?` clause in RS-10 and RS-30, and a set of prose lines that no §3 rule anchors. They are listed below and were not improvised.

## Anchors not found (not improvised)

1. **C4P, C-PR30-ENTRY (PR-30).** PR-30 carries no PR-40 return-context sentence: no sentence in it
   says a PR-40 finding returns to PR-30, and it states that PR-40 is not a PR-30 destination. The pattern
   `PR-40 … return(s)/REJECT … PR-30` matches nothing, so C-PR30-ENTRY is **not placed**. That matches
   child C9's "it never had a PR-40 return context". Nathan decides whether it is added, and where.
2. **S18A, RS-10 and RS-30: no old `ASK OK?` clause to move.** Neither body says the response "ends
   `ASK OK?`". Each says its saved artifact is written "ending `ASK OK?`", which is the artifact's state and
   is not matched by G08. The `ASK OK?` variant is placed and G08A passes, but that artifact wording is left
   as it is.
3. **Not covered by any §3 anchor, so left unchanged.** Each is listed as an occurrence count, with no text.
   - **Same-session wording.** It survives outside the replaced continuity lists: "same session" /
     "same-session" / "dedicated PR-development session" remain in PR-10 (2/3), PR-20 (3/2), PR-30 (4/3),
     PR-35 (8/1), PR-40 (1/1), RS-40 (2/2), QA-10 (1/1), OPS-30 (1/1), and "same session" 1–2× in the
     CL-*, DOC-*, ESC-*, QA-50 and RS-10 boilerplate.
   - **Role lines.** PR-30's and PR-35's role lines still say "same dedicated PR … session", and PR-35's
     package keeps `session_disposition: RETAIN_EXISTING`.
   - **`material boundary` outside the placements.** Routing sentences that come *before* C-LAT keep
     "material boundary", because the step-22 literal says "as defined above": 1 each in PR-10, PR-35,
     PR-40 and DOC-10. Other occurrences outside the placements: CL-20 1, QA-10 2.
   - **"end `ASK OK?`" outside ASK4.** It remains in QA-50 (1), OPS-30 (2) and ESC-30 (1), and in DOC-10
     as "ending" (1). Of these, G08 matches only QA-50, which is not a G08 row.
   - **CONTROL_NOTION in QA-10.** It remains once. QA-10 is not a step-3 body, and G01 fires there (below).

## E3: what each rule placed

Totals over 55 bodies:
- S42: 154 header lines deleted in 55 bodies (3 each, or 2 where the body has no `Set:` line). 0 remain.
- S03: 7 (C-NOTION).
- S04: 6 (QA-10).
- S05: 10.
- S08: 53 (C-ART).
- S13: 53 (C-HANDOFF).
- S13V: 25 bodies moved "contain(s)" to "ends with". The plan's estimate was 16. The 25 are:
  - CF-C-10..40, CF-E-10..40 and CF-PO-10;
  - CL-20, CL-30, CL-40, CL-C-10 and CL-E-10..40;
  - DOC-10, DOC-20, ESC-10, ESC-25, ESC-30, ESC-40, MGR-10 and PR-35.
- S18: 49 (C-PLACE).
- S18A: 4 (the `ASK OK?` variant). The old "end `ASK OK?`" clause was removed in QA-60 and QA-80.
- CTOP: 54 (53 with the handoff placement, plus PR-50 beside its return rule).
- S20: 3 (C-DEC).
- S22: 10 (C-LAT). The step-22 literal was placed twice: DOC-10 and PR-30.
- S32: 19 (C-SESSION). The bodies are:
  - CL-20, CL-30, CL-40, CL-C-10 and CL-E-10..40;
  - DOC-10, DOC-20, ESC-10, ESC-25, ESC-30 and ESC-40;
  - PR-30, PR-35, QA-20, QA-70 and RS-40.
- S37: 2 (C-SUB).
- S39: 2 (C-DISPATCH).
- W4: 1.
- C4R: 1 (C-REPLAN; the 10-line existing-PR-owner branch).
- C4E: 1 (C-PR20-ENTRY, at the end of PR-20's inputs section).
- C4Q: 2 (C-PROCEED in PR-30 and PR-35, the only bodies with the single-Proceed sentence).
- S13P: 8 deletions (PR-30 step 6: 4; PR-35 package bullet: 4).
- C4P: 0 (above).

Every canonical text a body should carry occurs in it exactly once. The one exception is C-PR30-ENTRY in PR-30, which occurs 0 times (above).

Placement choices a reviewer should check (E5, "the body rules script's anchors"):
- C-HANDOFF keeps the block-shape sentence or sentences verbatim, apart from the S13V verb. It replaces the
  run of field-list sentences that follows, up to the first sentence stating terminal or no-block behaviour,
  which is kept. In the CL-20 family the field list is the next paragraph, and it is replaced whole.
- C-PLACE, or its variant, then C-TOP, go as new paragraphs directly after the handoff paragraph.
- C-ART goes first in the first result/output-headed section that names the registry output artifact. C-DEC
  follows it.
- C-LAT goes directly under the first heading naming rescope or an RS route. Failing that, it goes in the
  first section with a sentence routing to RS-10/RS-20, then to any RS prompt. IA-30 has none of these, so it
  falls back to its first heading naming "material" (section #11).
  - The step-22 literal replaces "material boundary" in lines after C-LAT that route to RS or rescope.
  - RS-10's and RS-20's C-LAT sits under their routing sections (#7 and #8).
- C-SUB goes under PR-35's review-first heading and RS-40's `PR_RETURN_PHASE: PR-35` heading.
- C-DISPATCH goes after the `MERGE_PENDING — Ready to merge` line.

Per body:

| body | rules applied (count) | canonical texts placed (occurrences) | anchors not found | placement notes |
|---|---|---|---|---|
| CF-C-10 | S42 2, S05 1, S08 1, S13V 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1 | — | S08: section #4 (result heading naming the output artifact); S13: section #6 (same line); 1 field-list sentence(s) replaced, 0 kept after it |
| CF-C-20 | S42 2, S05 1, S08 1, S13V 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1 | — | S08: section #5 (result heading naming the output artifact); S13: section #7 (same line); 1 field-list sentence(s) replaced, 0 kept after it |
| CF-C-30 | S42 2, S05 1, S08 1, S13V 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1 | — | S08: section #7 (first result heading (artifact not named in it)); S13: section #9 (same line); 1 field-list sentence(s) replaced, 0 kept after it |
| CF-C-40 | S42 2, S05 1, S08 1, S13V 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1 | — | S08: section #7 (result heading naming the output artifact); S13: section #8 (same line); 1 field-list sentence(s) replaced, 0 kept after it |
| CF-E-10 | S42 2, S05 1, S08 1, S13V 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1 | — | S08: section #4 (result heading naming the output artifact); S13: section #6 (same line); 1 field-list sentence(s) replaced, 0 kept after it |
| CF-E-20 | S42 2, S05 1, S08 1, S13V 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1 | — | S08: section #5 (result heading naming the output artifact); S13: section #7 (same line); 1 field-list sentence(s) replaced, 0 kept after it |
| CF-E-30 | S42 2, S05 1, S08 1, S13V 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1 | — | S08: section #7 (first result heading (artifact not named in it)); S13: section #9 (same line); 1 field-list sentence(s) replaced, 0 kept after it |
| CF-E-40 | S42 2, S05 1, S08 1, S13V 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1 | — | S08: section #7 (result heading naming the output artifact); S13: section #8 (same line); 1 field-list sentence(s) replaced, 0 kept after it |
| CF-PO-10 | S42 2, S05 1, S08 1, S13V 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1 | — | S08: section #6 (result heading naming the output artifact); S13: section #7 (same line); 1 field-list sentence(s) replaced, 0 kept after it |
| CL-20 | S42 3, S32 1, S08 1, S13V 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1 | — | S08: section #13 (result heading naming the output artifact); S13: section #24 (field list on the next line); 3 field-list sentence(s) replaced, 0 kept after it |
| CL-30 | S42 3, S32 1, S08 1, S13V 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1 | — | S08: section #12 (result heading naming the output artifact); S13: section #24 (field list on the next line); 3 field-list sentence(s) replaced, 0 kept after it |
| CL-40 | S42 3, S32 1, S08 1, S13V 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1 | — | S08: section #10 (result heading naming the output artifact); S13: section #15 (field list on the next line); 3 field-list sentence(s) replaced, 0 kept after it |
| CL-C-10 | S42 3, S32 1, S08 1, S13V 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1 | — | S08: section #13 (result heading naming the output artifact); S13: section #15 (field list on the next line); 3 field-list sentence(s) replaced, 0 kept after it |
| CL-E-10 | S42 3, S32 1, S08 1, S13V 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1 | — | S08: section #13 (result heading naming the output artifact); S13: section #15 (field list on the next line); 3 field-list sentence(s) replaced, 0 kept after it |
| CL-E-20 | S42 3, S32 1, S08 1, S13V 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1 | — | S08: section #10 (result heading naming the output artifact); S13: section #6 (same line); 3 field-list sentence(s) replaced, 1 kept after it |
| CL-E-30 | S42 3, S32 1, S08 1, S13V 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1 | — | S08: section #10 (result heading naming the output artifact); S13: section #6 (same line); 3 field-list sentence(s) replaced, 1 kept after it |
| CL-E-40 | S42 3, S32 1, S08 1, S13V 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1 | — | S08: section #10 (result heading naming the output artifact); S13: section #6 (same line); 3 field-list sentence(s) replaced, 1 kept after it |
| DOC-10 | S42 3, S32 1, S22 1, S22-literal 1, S08 1, S13V 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1, C-LAT 1 | — | S22: section #12 (first section with a sentence routing to RS-10/RS-20); 'material boundary' replaced 1 in routing sentences after C-LAT; 1 routing sentence(s) before C-LAT left unchanged; 1 occurrence(s) remain in the body; S08: section #11 (result heading naming the output artifact); S13: section #6 (same line); 3 field-list sentence(s) replaced, 1 kept after it |
| DOC-20 | S42 3, S32 1, S22 1, S08 1, S13V 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1, C-LAT 1 | — | S22: section #12 (first section with a sentence routing to RS-10/RS-20); 'material boundary' replaced 0 in routing sentences after C-LAT; 0 routing sentence(s) before C-LAT left unchanged; 0 occurrence(s) remain in the body; S08: section #11 (result heading naming the output artifact); S13: section #6 (same line); 3 field-list sentence(s) replaced, 1 kept after it |
| ESC-10 | S42 3, S32 1, S08 1, S13V 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1 | — | S08: section #11 (result heading naming the output artifact); S13: section #6 (same line); 3 field-list sentence(s) replaced, 1 kept after it |
| ESC-25 | S42 3, S32 1, S08 1, S13V 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1 | — | S08: section #11 (result heading naming the output artifact); S13: section #6 (same line); 3 field-list sentence(s) replaced, 1 kept after it |
| ESC-30 | S42 3, S32 1, S08 1, S13V 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1 | — | S08: section #11 (result heading naming the output artifact); S13: section #6 (same line); 3 field-list sentence(s) replaced, 1 kept after it |
| ESC-40 | S42 3, S32 1, S08 1, S13V 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1 | — | S08: section #12 (result heading naming the output artifact); S13: section #6 (same line); 3 field-list sentence(s) replaced, 1 kept after it |
| GCFPE-MGMT-10 | S42 2 |  | — | — |
| IA-10 | S42 3, S08 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1 | — | S08: section #11 (result heading naming the output artifact); S13: section #13 (same line); 3 field-list sentence(s) replaced, 1 kept after it |
| IA-20 | S42 3, S08 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1 | — | S08: section #7 (first result heading (artifact not named in it)); S13: section #8 (same line); 3 field-list sentence(s) replaced, 1 kept after it |
| IA-30 | S42 3, S22 1, S08 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1, C-LAT 1 | — | S22: section #11 (no section routes to RS; first heading naming 'material'); 'material boundary' replaced 0 in routing sentences after C-LAT; 0 routing sentence(s) before C-LAT left unchanged; 0 occurrence(s) remain in the body; S08: section #13 (result heading naming the output artifact); S13: section #14 (same line); 1 field-list sentence(s) replaced, 1 kept after it |
| IA-40 | S42 3, S08 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1 | — | S08: section #10 (first result heading (artifact not named in it)); S13: section #11 (same line); 2 field-list sentence(s) replaced, 1 kept after it |
| IA-50 | S42 3, S08 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1 | — | S08: section #5 (first result heading (artifact not named in it)); S13: section #7 (same line); 2 field-list sentence(s) replaced, 1 kept after it |
| IA-60 | S42 3, S08 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1 | — | S08: section #5 (result heading naming the output artifact); S13: section #7 (same line); 2 field-list sentence(s) replaced, 1 kept after it |
| MGR-10 | S42 2, S05 1, S08 1, S13V 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1 | — | S08: section #4 (result heading naming the output artifact); S13: section #6 (same line); 1 field-list sentence(s) replaced, 0 kept after it |
| OPS-10 | S42 3, S03 1, S08 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1, C-NOTION 1 | — | S08: section #11 (result heading naming the output artifact); S13: section #22 (same line); 4 field-list sentence(s) replaced, 2 kept after it |
| OPS-20 | S42 3, S03 1, S08 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1, C-NOTION 1 | — | S08: section #12 (result heading naming the output artifact); S13: section #22 (same line); 4 field-list sentence(s) replaced, 2 kept after it |
| OPS-30 | S42 3, S03 1, S08 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1, C-NOTION 1 | — | S08: section #13 (result heading naming the output artifact); S13: section #23 (same line); 4 field-list sentence(s) replaced, 2 kept after it |
| PR-10 | S42 3, S03 1, S22 1, S08 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1, C-NOTION 1, C-LAT 1 | — | S22: section #16 (heading names rescope or an RS route); 'material boundary' replaced 0 in routing sentences after C-LAT; 1 routing sentence(s) before C-LAT left unchanged; 1 occurrence(s) remain in the body; S08: section #13 (result heading naming the output artifact); S13: section #24 (same line); 4 field-list sentence(s) replaced, 2 kept after it |
| PR-20 | S42 3, S03 1, C4E 1, S22 1, S08 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1, C-NOTION 1, C-LAT 1, C-PR20-ENTRY 1 | — | C4E: end of section #2; S22: section #18 (heading names rescope or an RS route); 'material boundary' replaced 0 in routing sentences after C-LAT; 0 routing sentence(s) before C-LAT left unchanged; 0 occurrence(s) remain in the body; S08: section #13 (result heading naming the output artifact); S13: section #26 (same line); 4 field-list sentence(s) replaced, 2 kept after it |
| PR-30 | S42 3, S03 1, S32 1, C4Q 1, S13P 4, S22 1, S22-literal 1, S08 1, S20 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1, C-NOTION 1, C-DEC 1, C-SESSION 1, C-LAT 1, C-PR30-ENTRY 0 | C4P: no PR-40 return-context sentence in PR-30 (pattern: PR-40 ... return/REJECT ... PR-30) | S22: section #5 (first section with a sentence routing to RS-10/RS-20); 'material boundary' replaced 1 in routing sentences after C-LAT; 0 routing sentence(s) before C-LAT left unchanged; 0 occurrence(s) remain in the body; S08: section #13 (result heading naming the output artifact); S13: section #20 (same line); 4 field-list sentence(s) replaced, 2 kept after it |
| PR-35 | S42 3, S32 1, C4Q 1, S13P 4, S37 1, S39 1, S22 1, S08 1, S20 1, S13V 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1, C-DEC 1, C-SESSION 1, C-LAT 1, C-SUB 1, C-DISPATCH 1 | — | S37: section #6; S39: section #9; S22: section #8 (heading names rescope or an RS route); 'material boundary' replaced 0 in routing sentences after C-LAT; 1 routing sentence(s) before C-LAT left unchanged; 1 occurrence(s) remain in the body; S08: section #10 (result heading naming the output artifact); S13: section #12 (same line); 5 field-list sentence(s) replaced, 0 kept after it |
| PR-40 | S42 3, S03 1, C4R 1, W4 1, S22 1, S08 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1, C-NOTION 1, C-LAT 1, C-REPLAN 1, W4 1 | — | C4R: branch of 10 lines replaced; S22: section #17 (heading names rescope or an RS route); 'material boundary' replaced 0 in routing sentences after C-LAT; 1 routing sentence(s) before C-LAT left unchanged; 1 occurrence(s) remain in the body; S08: section #14 (result heading naming the output artifact); S13: section #25 (same line); 4 field-list sentence(s) replaced, 2 kept after it |
| PR-50 | S42 3, CTOP 1 | C-TOP 1 | — | — |
| QA-10 | S42 3, S04 6, S08 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1 | — | S08: section #19 (result heading naming the output artifact); S13: section #31 (same line); 4 field-list sentence(s) replaced, 2 kept after it |
| QA-100 | S42 3, S08 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1 | — | S08: section #8 (result heading naming the output artifact); S13: section #9 (same line); 1 field-list sentence(s) replaced, 1 kept after it |
| QA-110 | S42 3, S08 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1 | — | S08: section #8 (result heading naming the output artifact); S13: section #9 (same line); 1 field-list sentence(s) replaced, 1 kept after it |
| QA-120 | S42 3, S08 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1 | — | S08: section #7 (result heading naming the output artifact); S13: section #8 (same line); 1 field-list sentence(s) replaced, 1 kept after it |
| QA-20 | S42 3, S32 1, S08 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1 | — | S08: section #8 (result heading naming the output artifact); S13: section #9 (same line); 3 field-list sentence(s) replaced, 1 kept after it |
| QA-50 | S42 3, S08 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1 | — | S08: section #11 (result heading naming the output artifact); S13: section #12 (same line); 1 field-list sentence(s) replaced, 1 kept after it |
| QA-60 | S42 3, S08 1, S13 1, S18A-old-clause-removed 1, S18A 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, ASK-VARIANT 1 | — | S08: section #9 (result heading naming the output artifact); S13: section #10 (same line); 1 field-list sentence(s) replaced, 1 kept after it |
| QA-70 | S42 3, S32 1, S08 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1 | — | S08: section #9 (result heading naming the output artifact); S13: section #10 (same line); 1 field-list sentence(s) replaced, 1 kept after it |
| QA-80 | S42 3, S08 1, S13 1, S18A-old-clause-removed 1, S18A 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, ASK-VARIANT 1 | — | S08: section #7 (first result heading (artifact not named in it)); S13: section #8 (same line); 1 field-list sentence(s) replaced, 1 kept after it |
| QA-90 | S42 3, S08 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1 | — | S08: section #8 (result heading naming the output artifact); S13: section #9 (same line); 1 field-list sentence(s) replaced, 1 kept after it |
| RS-10 | S42 3, S22 1, S08 1, S13 1, S18A 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, ASK-VARIANT 1, C-LAT 1 | S18A: old `ASK OK?` clause absent | S22: section #7 (first section with a sentence routing to RS-10/RS-20); 'material boundary' replaced 0 in routing sentences after C-LAT; 0 routing sentence(s) before C-LAT left unchanged; 0 occurrence(s) remain in the body; S08: section #7 (result heading naming the output artifact); S13: section #8 (same line); 2 field-list sentence(s) replaced, 1 kept after it |
| RS-20 | S42 3, S22 1, S08 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1, C-LAT 1 | — | S22: section #8 (first section with a sentence routing to an RS prompt); 'material boundary' replaced 0 in routing sentences after C-LAT; 0 routing sentence(s) before C-LAT left unchanged; 0 occurrence(s) remain in the body; S08: section #8 (result heading naming the output artifact); S13: section #9 (same line); 1 field-list sentence(s) replaced, 1 kept after it |
| RS-30 | S42 3, S08 1, S13 1, S18A 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, ASK-VARIANT 1 | S18A: old `ASK OK?` clause absent | S08: section #7 (first result heading (artifact not named in it)); S13: section #8 (same line); 3 field-list sentence(s) replaced, 1 kept after it |
| RS-40 | S42 3, S32 1, S37 1, S39 1, S08 1, S20 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1, C-DEC 1, C-SESSION 1, C-SUB 1, C-DISPATCH 1 | — | S37: section #6; S39: section #6; S08: section #7 (first result heading (artifact not named in it)); S13: section #8 (same line); 1 field-list sentence(s) replaced, 1 kept after it |
| UTIL-10 | S42 3, S08 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1 | — | S08: section #6 (first result heading (artifact not named in it)); S13: section #7 (same line); 2 field-list sentence(s) replaced, 1 kept after it |

## E4 gate

| item | result | flags and counts |
|---|---|---|
| 1 Graph | PASS | `graph_parts.py build`: 55 nodes, 229 edges, 55 state routes, `validation PASS`, no WARNING. Embedded JSON 575 074 B, `ae2bd159…`. Byte-identical to both bundled copies |
| 2 Parity and routing | PASS | `validate_graph_contract` `[]` for both contract copies; `validate_contract` `[]`; `routing_surface` `('fecc319bdd4ce7ee6201cb77d7231861', 284)` for both |
| 3 Live suites | PASS, unchanged | `fm-default` and `fm-candidate`: `FLOWMASTER_SUITE_PASS`, `suite_ok: true`, 0 findings. v4 `ok: true`; `gcfpe-current` `ok: true`; `cf-validator` PASS. Every live output is equal to E2's run (rootless stdout digest) |
| 4 Historical layer | PASS, unchanged | All 12 outputs are equal to the §2 baseline: validators strength-middleware, epic-alpha, epic-reengineering, integrated-readiness, pre-guide-correction, final-scan and alpha-feedback; fixture runners strength-middleware 216, epic-alpha 197/197, integrated-readiness 65/65, final-scan 26/26 and alpha-feedback 38/38 |
| 5 v4 fixtures | PASS | `fixture_suite_ok: true`, 228/228 (current runner 228/228; change-flow fixtures 32/32). Same counts as E2 |
| 6 Other packages | PASS | PR skill PASS; relay self-test PASS, 230 cases; `amthor` fixture suite 34 OK; registry structure `{"valid": true, "problems": []}` |
| 7 Bodies | PASS | `prompt_bodies_validated` 55 (all members); `prompt_body_checks_not_evaluated` `[]`; `errors` `[]`; exit 0 |
| 8 Registry assertions | **FAIL: 16 findings on 14 rows** | 55 rows, 1 484 assertions, `_evaluate_assertions` from the edited `amthor` copy. Findings: G06 (TOP-001) on 13 rows; G01 (CTR-001) on QA-10; G15 (CTR-001) on RS-40. Every other row has zero findings. §7.7 role parity: clean `[]`; clause removed from the registry only → `ROLE_PARITY` alone; clause removed from both → `ROLE_CLAUSE` alone. No snapshot, no hash |
| 9 Regressions | PASS | 43/43 registry-guard regressions give exactly their own `(rule_id, summary)`; G27's clean control on unedited PR-20 gives its finding. Guard row counts equal §7.10 plus G25B (PR-40, 1). Skill, contract, fixture and oracle regressions were E2's and are not re-run here |
| 10 Closure and records | PASS | See the closure table below. `modification_validate.py`: 2/2 ok |

Closure table for item 10:
- It is equal to §4.10 V5 for all seven prompts listed there.
- Radii: PR-10 24; PR-20 22; PR-30 6; PR-35 7; PR-40 11, whose downstream is [PR-10, PR-20, RS-10] and whose upstream now includes PR-35; RS-40 5; DOC-10 22.
- DOC-20: upstream [], downstream [DOC-10, PR-40, QA-10, RS-10], radius 25.

### Clean-control hits on real edited bodies (not exempted; for Nathan)

| guard | body | matched phrase (≤12 words) | on the unedited body too | cause |
|---|---|---|---|---|
| G06 | CF-C-10, CF-C-20, CF-C-30, CF-C-40, CF-E-10, CF-E-20, CF-E-30, CF-E-40, CF-PO-10, MGR-10 | "under `docs/ephemeral/` in the repository, committed and pushed on the working branch" | yes | The artifact-storage boilerplate that follows the handoff section says "working branch". After the edit it falls within 1 500 characters of C-PLACE's `NEXT_PROMPT_HANDOFF` token; with that token masked the edited body is clean |
| G06 | CL-C-10, CL-E-10 | same phrase | yes | Within the window of the body's own third `NEXT_PROMPT_HANDOFF` mention, not a canonical text |
| G06 | RS-40 | "no session. Resume only PR-35 responsibilities: reverify same vehicle and remote head" | yes | The body's own "contains no `NEXT_PROMPT_HANDOFF`" terminal-stop sentence sits about 1 200 characters before the PR-35 phase's "remote head" (7.4 foresaw such hits) |
| G01 | QA-10 | "CONTROL_NOTION" | yes | QA-10 is not a step-3 body; its own `CONTROL_NOTION` mention is outside the step-3 sentence |
| G15 | RS-40 | "Proceed; same dedicated PR-development session" | yes | RS-40's Required-inputs list, which is not a continuity list and so not replaced by C-SESSION |

G19, G20 and G21 have no hits on any of the 54 edited bodies, and neither do G02–G05, G07–G14, G16–G18 or G22–G27. Off-row, for information: G08 matches QA-50 ("end `ASK OK?`"), which is not a G08 row.

### Every registry-guard regression (§7.3; G25B from the addendum)

| guard | row | exact own finding | findings added |
|---|---|---|---|
| G01 | PR-10 | yes | 1 (CTR-001) |
| G02 | PR-10 | yes | 1 (CTR-001) |
| G03 | QA-10 | yes | 1 (CTR-001) |
| G04 | CF-C-10 | yes | 1 (CTR-001) |
| G05 | PR-35 | yes | 1 (CTR-002) |
| G06 | PR-35 | yes | 1 (TOP-001) |
| G06 | PR-35 | yes | 1 (TOP-001) |
| G07 | PR-35 | yes | 1 (TOP-001) |
| G07 | QA-60 | yes | 1 (TOP-001) |
| G08 | QA-60 | yes | 1 (CTR-002) |
| G08A | QA-60 | yes | 1 (TOP-001) |
| G08A | RS-30 | yes | 1 (TOP-001) |
| G09 | PR-35 | yes | 1 (CTR-002) |
| G09 | RS-40 | yes | 1 (CTR-002) |
| G10 | PR-35 | yes | 1 (CTR-002) |
| G11 | PR-35 | yes | 1 (CTR-002) |
| G12 | PR-35 | yes | 1 (SRC-001) |
| G12 | PR-35 | yes | 1 (SRC-001) |
| G13 | PR-35 | yes | 1 (INV-003) |
| G13 | PR-35 | yes | 1 (INV-003) |
| G14 | PR-35 | yes | 1 (SRC-001) |
| G14 | PR-35 | yes | 1 (SRC-001) |
| G15 | PR-35 | yes | 1 (CTR-001) |
| G15 | QA-10 | yes | 1 (CTR-001) |
| G16 | PR-35 | yes | 1 (CTR-002) |
| G16 | RS-40 | yes | 1 (CTR-002) |
| G17 | PR-35 | yes | 1 (CTR-002) |
| G17 | PR-30 | yes | 1 (CTR-002) |
| G18 | PR-35 | yes | 1 (CTR-002) |
| G18 | PR-50 | yes | 1 (CTR-002) |
| G19 | PR-35 | yes | 1 (CTR-001) |
| G20 | PR-35 | yes | 1 (CTR-001) |
| G21 | PR-35 | yes | 1 (CTR-001) |
| G22 | PR-35 | yes | 1 (CTR-001) |
| G23 | PR-35 | yes | 1 (CTR-002) |
| G23 | RS-40 | yes | 1 (CTR-002) |
| G24 | PR-35 | yes | 1 (CTR-002) |
| G24 | RS-40 | yes | 1 (CTR-002) |
| G25 | PR-35 | yes | 1 (CTR-002) |
| G25 | RS-40 | yes | 1 (CTR-002) |
| G25B | PR-40 | yes | 1 (CTR-002) |
| G26 | PR-40 | yes | 1 (CTR-001) |
| G27 | PR-20 | yes | 1 (CTR-002) |

### Clean control of every guard over the 54 edited main bodies

| guard | list | rows | forbidden hits on its rows | forbidden hits on other main bodies | required absent on its rows |
|---|---|---|---|---|---|
| G01 | forbidden_regex | 55 | QA-10: "CONTROL_NOTION" | 0 | 0 |
| G02 | forbidden_regex | 55 | 0 | 0 | 0 |
| G03 | forbidden_regex | 1 | 0 | 0 | 0 |
| G04 | forbidden_regex | 10 | 0 | 0 | 0 |
| G05 | required_regex | 53 | 0 | 0 | 0 |
| G06 | forbidden_regex | 53 | CF-C-10: "under `docs/ephemeral/` in the repository, committed and pushed on the working branch"; CF-C-20: "under `docs/ephemeral/` in the repository, committed and pushed on the working branch"; CF-C-30: "under `docs/ephemeral/` in the repository, committed and pushed on the working branch"; CF-C-40: "under `docs/ephemeral/` in the repository, committed and pushed on the working branch"; CF-E-10: "under `docs/ephemeral/` in the repository, committed and pushed on the working branch"; CF-E-20: "under `docs/ephemeral/` in the repository, committed and pushed on the working branch"; CF-E-30: "under `docs/ephemeral/` in the repository, committed and pushed on the working branch"; CF-E-40: "under `docs/ephemeral/` in the repository, committed and pushed on the working branch"; CF-PO-10: "under `docs/ephemeral/` in the repository, committed and pushed on the working branch"; CL-C-10: "under `docs/ephemeral/` in the repository, committed and pushed on the working branch"; CL-E-10: "under `docs/ephemeral/` in the repository, committed and pushed on the working branch"; MGR-10: "under `docs/ephemeral/` in the repository, committed and pushed on the working branch"; RS-40: "no session. Resume only PR-35 responsibilities: reverify same vehicle and remote head" | 0 | 0 |
| G07 | required_regex | 53 | 0 | 0 | 0 |
| G08 | forbidden_regex | 4 | 0 | QA-50: "end `ASK OK?`" | 0 |
| G08A | required_regex | 4 | 0 | 0 | 0 |
| G09 | required_regex | 3 | 0 | 0 | 0 |
| G10 | required_regex | 10 | 0 | 0 | 0 |
| G11 | required_regex | 10 | 0 | 0 | 0 |
| G12 | forbidden_regex | 55 | 0 | 0 | 0 |
| G13 | forbidden_regex | 55 | 0 | 0 | 0 |
| G14 | forbidden_regex | 55 | 0 | 0 | 0 |
| G15 | forbidden_regex | 54 | RS-40: "Proceed; same dedicated PR-development session" | 0 | 0 |
| G16 | required_regex | 3 | 0 | 0 | 0 |
| G17 | required_regex | 3 | 0 | 0 | 0 |
| G18 | required_regex | 54 | 0 | 0 | 0 |
| G19 | forbidden_regex | 54 | 0 | 0 | 0 |
| G20 | forbidden_regex | 54 | 0 | 0 | 0 |
| G21 | forbidden_regex | 54 | 0 | 0 | 0 |
| G22 | forbidden_regex | 2 | 0 | 0 | 0 |
| G23 | required_regex | 2 | 0 | 0 | 0 |
| G24 | required_regex | 2 | 0 | 0 | 0 |
| G25 | required_regex | 2 | 0 | 0 | 0 |
| G25B | required_regex | 1 | 0 | 0 | 0 |
| G26 | forbidden_regex | 1 | 0 | 0 | 0 |
| G27 | required_regex | 1 | 0 | 0 | 0 |
