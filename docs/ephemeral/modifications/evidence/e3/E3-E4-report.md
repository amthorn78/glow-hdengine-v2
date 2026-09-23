# E3 and E4 report — Amendment 1 (spec v2 §0, §3, §7, §9), revision 4

Revisions 3 and 4 are recorded in their own sections. Revision 2 of the E3/E4 run applied the plan's author's six settlements, received after the first
E4, re-ran E4 items 7–9, and measured four G06 alternatives. Items 1–6 and 10 do not read bodies, and nothing
they read has changed since the first run, so their results below are those of that run (2026-09-23).

**Inputs:**
- the execution branch working tree (E1 `ce7e5cd`, E2 `83794d3`; this stage commits nothing);
- the edited skill tree `/tmp/claude-0/e2/skills`;
- the working-tree registry.

Every command ran with `PYTHONDONTWRITEBYTECODE=1`. No `__pycache__` was created.

**Corpus policy (D22).**
- The 55 bodies were read from Notion fetch results by the session extractor and piped only in memory.
- No body, fragment or body hash is written here or anywhere.
- The only body words in this file are matched guard phrases of 12 words or fewer, the form §E asks for on clean-control hits.
- "Section #n" counts a body's headings from the top. It names a place without quoting it.

**Scripts,** in `docs/ephemeral/modifications/evidence/e3/` (committed with the evidence, reviewed in E5):

| script | what it does |
|---|---|
| `body_rules.py` | The E3 rules. Canonical texts are read verbatim from §3's code blocks; anchors are regexes. `apply(bodies)` returns the edited bodies and a per-body report |
| `run_e4.py` | E4 items 7, 8 and 9, in memory |
| `g06_alternatives.py` | Measures G06 alternatives (a)–(d) |

Usage: `<bodies JSON> | PYTHONDONTWRITEBYTECODE=1 python3 <script> /tmp/claude-0/e2/skills`


## Revision 4 (after repair round a1, commit `32e04d4`)

**What changed.**
- C-DISPATCH now ends with the sentence Nathan approved, "PR-40 is entered once per merge: …". `body_rules.py` reads it from the `D23` successor note in commit `37bf7e1` and appends it; it is not re-authored.
- The edited validator in `/tmp/claude-0/e2/skills` now carries the new checks from repair round a1.

**What was re-run.** E3 and E4 items 7, 8 and 9, with:
- the current working-tree registry, including G06 as approved in (b);
- the same session fetch results, in memory.

| check | result |
|---|---|
| C-DISPATCH | placed exactly once in PR-35 and once in RS-40 |
| other canonical texts | every one a body should carry occurs exactly once |
| anchors not found | unchanged: only RS-10 and RS-30's artifact-worded `ASK OK?`, as recorded above |
| totals | unchanged: S42 154, CTOP 54, convergence rewrites 79 |
| item 7 | PASS: `prompt_bodies_validated` 55 (all members), `prompt_body_checks_not_evaluated` `[]`, `errors` `[]`, exit 0 |
| item 8 | PASS: 0 findings on 55 rows, 1 484 assertions; role parity clean, and its two negative controls give `ROLE_PARITY` and `ROLE_CLAUSE` |
| item 9 | PASS: 43 of 43 registry-guard regressions exact, including G24 and G25 on the extended C-DISPATCH; G27's clean control fires on today's PR-20; guard row counts as specified |
| clean controls | G06, G15, G19, G20 and G21 are silent on all 54 edited main bodies, and so is every other guard |

No body text or hash was written, nothing was written to Notion, and nothing was committed. No `__pycache__` was created.

## Settlements applied (plan's author, after the first E4)

1. **C-PLACE, or the `ASK OK?` variant, and C-TOP form one paragraph** with a blank line before and after it. That paragraph sits directly after the handoff paragraph. PR-50's C-TOP is likewise its own paragraph.
2. **Same-session statements are converged.** 33 anchor classes (X01–X31, plus X17b and X29a; 32 of them fired, X07 matched nothing) rewrite every remaining line saying that PR-35 shares PR-30's session, or that one session spans both phases (table below).
   - Lines stay where PR-20 and PR-30 share one planning-and-build session, and where PR-35 re-enters its own session. After convergence, 20 such same-session phrases remain, all legitimate:
     - PR-35's own recovery or re-entry: PR-35 ×6; CL-20, CL-30, CL-40, CL-C-10, CL-E-10 and RS-40 ×1 each.
     - PR-30's own session: PR-30 ×5.
     - The PR-20/PR-30 session: PR-20 ×2.
     - Originating-owner and PR-30 returns: PR-20, RS-20 ×1 each.
3. **QA-10's `CONTROL_NOTION` sentence takes C-NOTION.** It is the step-3 sentence.
4. **"material boundary" in a routing line before C-LAT becomes "material change (D23-C)".** This applies in 4 bodies: DOC-10, PR-10, PR-35 and PR-40.
5. **"end `ASK OK?`" outside ASK4:**
   - QA-50 describes the final response, so it gets the full ASK4 treatment: its old clause is removed and the `ASK OK?` variant is placed.
   - OPS-30 and ESC-30 describe saved artifacts ("ending `ASK OK?`", "End the pending proposal `ASK OK?`"), so they are left.
   - RS-10 and RS-30 are likewise artifact wording and are left.
6. **C-PR30-ENTRY is `NOT_APPLICABLE`.** PR-30 has no PR-40 return context, so nothing is placed.

## Verdict

- **Item 7 passes.** All 55 bodies validated; `errors` is `[]` and `prompt_body_checks_not_evaluated` is `[]`.
- **Item 8: 0 findings on all 55 rows (1 484 assertions).** This follows Nathan's approval of G06 alternative (b), which the registry now carries (section "G06, revision 3"). The 3 G06 hits recorded in revision 2 (CL-C-10, CL-E-10 and RS-40) were pre-existing "contains no `NEXT_PROMPT_HANDOFF`" sentences, and they are cleared.
- **Item 9 passes.** All 43 of 43 regressions give exactly their own finding. The G27 clean control fires on today's PR-20.
- **Items 1–6 and 10** are unchanged from the first run and pass.
- **G06 alternatives:** Nathan approved (b), and it is applied to the registry. The measurements below are kept as the record: (b) and (d) cleared all three hits and kept both regressions exact, but (d) is a weakening; (c) lost the end-of-paragraph regression.

## Anchors not found

- **RS-10 and RS-30 have no old `ASK OK?` clause that describes the response.** Their "ending `ASK OK?`" describes the saved artifact. The variant is placed, and G08A passes.
- **C4P (C-PR30-ENTRY) is `NOT_APPLICABLE`.** This follows settlement 6.

No other anchor missed.

## E3: totals over 55 bodies

| rule | count |
|---|---|
| S42 | 154 header lines deleted, in 55 bodies (3 each, or 2 where the body has no `Set:` line); 0 remain |
| S03 | 8: the 7 step-3 bodies and QA-10 |
| S04 | 6 |
| S05 | 10 |
| S08 (C-ART) | 53 |
| S13 (C-HANDOFF) | 53 |
| S13V ("contain(s)" → "ends with") | 25 |
| S18 (C-PLACE) | 48 |
| S18A (`ASK OK?` variant) | 5: the ASK4 bodies and QA-50. The old clause was removed in QA-60, QA-80 and QA-50 |
| CTOP | 54 |
| S20 (C-DEC) | 3 |
| S22 (C-LAT) | 10 |
| step-22 literal after C-LAT | 2 |
| "material change (D23-C)" before C-LAT | 4 |
| S32 (C-SESSION) | 19 |
| S37 (C-SUB) | 2 |
| S39 (C-DISPATCH) | 2 |
| W4 | 1 |
| C4R (C-REPLAN) | 1 |
| C4E (C-PR20-ENTRY) | 1 |
| C4Q (C-PROCEED) | 2 |
| S13P | 8 |
| convergence (CONV-*) | 79 rewrites by 32 classes |

Every canonical text that a body should carry occurs in it exactly once.

### Convergence classes (settlement 2)

| class | rewrite (C-SESSION wording) | bodies (count) |
|---|---|---|
| X01 | "continues in the same session to PR-35" → "continues to PR-35 in its own dedicated session" (the boilerplate phase line) | CL-E-20 1, CL-E-30 1, CL-E-40 1, DOC-10 1, DOC-20 1, ESC-10 1, ESC-25 1, ESC-30 1, ESC-40 1 |
| X02 | "same-session PR-35 review/CI convergence" → "PR-35 review/CI convergence in its own dedicated session" | DOC-10 1 |
| X03 | "hands the same dedicated PR-development session to PR-35 without another Proceed, session, …" → "hands off to PR-35 in its own dedicated session without another Proceed, …" | OPS-30 1, PR-10 1, PR-20 1, PR-30 1, PR-40 1, QA-10 1 |
| X04 | postpublication "branch preserves the same session, workspace/worktree" → "… the recorded phase's own dedicated session, workspace/worktree" | OPS-30 1, PR-10 1, PR-20 1, PR-30 1, PR-40 1, QA-10 1 |
| X05 | "resumes the recorded phase in the same PR session" → "… in its own dedicated session" | CL-20 1, CL-40 1, CL-C-10 1, CL-E-10 1 |
| X06 | "the same session/workspace/worktree/branch/open PR" → "the recorded phase's own dedicated session and the same workspace/worktree/branch/open PR" | PR-10 1, PR-20 1, PR-30 1, RS-10 1 |
| X08 | "exactly one complete same-session handoff to (selected) PR-35" → "… handoff to PR-35 in its own dedicated session" | CL-20 1, CL-30 1, CL-40 1, CL-C-10 1, CL-E-10 1, PR-30 1 |
| X09 | "same-session PR-35 handoff" → "PR-35 handoff to PR-35's own dedicated session" | PR-20 1, PR-30 1, RS-40 1 |
| X10 | PR-30: "directly to this same dedicated PR-development session" → "directly to PR-35's own dedicated session" | PR-30 1 |
| X11 | RS-40: continue to PR-35 "in this same dedicated PR-development session" → "in PR-35's own dedicated session" | RS-40 1 |
| X12 | RS-40: "according to the recorded phase, in the same PR session" → "… in that phase's own dedicated session" | RS-40 1 |
| X13 | RS-40 role line → W-2's RS-40 role string (§3.4) | RS-40 1 |
| X14 | RS-40 Required inputs "original Product Owner Proceed; same dedicated PR-development session," → "…; the recorded phase's own dedicated session," | RS-40 1 |
| X15 | PR-35 role sentence → W-1's first sentence (§3.4) | PR-35 1 |
| X16 | "PR-35 is a same-session continuation inside" → "PR-35 is a phase continuation, in its own dedicated session, inside" | PR-35 1 |
| X17 | in a "PR-35 … adds no / neither merges nor adds a …" list, "session," → "session beyond its own dedicated PR-35 session," (registry wording) | CL-20 1, CL-30 1, CL-40 1, CL-C-10 1, CL-E-10 1, PR-20 1, PR-35 1 |
| X17b | the same list drops "cross-session route" (V-1: the PR-30 → PR-35 route now crosses sessions) | CL-20 1, CL-30 1, CL-40 1, CL-C-10 1, CL-E-10 1, PR-35 1 |
| X18 | PR-35 "Require one complete same-session package containing:" → "Require one complete PR-35 handoff package containing:" | PR-35 1 |
| X19 | PR-35 package bullet "the same dedicated PR-session reference and `session_disposition: RETAIN_EXISTING`" → "the dedicated PR-35 session reference and `session_disposition: NEW_DEDICATED` (`RETAIN_EXISTING` on re-entry to that PR-35 session)" | PR-35 1 |
| X20 | QA-50 "PR-30 and PR-35 are same-session phases of one PR work unit and original Proceed." → "PR-30 and PR-35 are two phases of one work unit, run in two dedicated sessions, under one original Proceed." | QA-50 1 |
| X21 | QA-60 "Preserve PR-30/PR-35 as one PR work unit, dedicated session, vehicle," → "… as two phases of one PR work unit, run in two dedicated sessions, with one vehicle," | QA-60 1 |
| X22 | PR-10 "PR-30 then hands the same dedicated PR-development session, …, directly to PR-35 — …" → the session item dropped and ", which runs in its own dedicated session" appended | PR-10 1 |
| X23 | PR-10 "one dedicated PR-development session, … PR-30/PR-35 phase ownership" → "the PR-30 and PR-35 phases' two dedicated sessions, …" | PR-10 1 |
| X24 | PR-20 heading "PR-35 SAME-SESSION REVIEW AND READINESS PHASE" → "PR-35 REVIEW AND READINESS PHASE IN ITS OWN DEDICATED SESSION" | PR-20 1 |
| X25 | PR-20 PR-35 package "one continuing PR-development session;" → "PR-35's own dedicated session, entered from PR-30's handoff;" | PR-20 1 |
| X26 | PR-20 "and hand the same dedicated PR-development session to PR-35." → "and hand off to PR-35 in its own dedicated session." | PR-20 1 |
| X27 | PR-40 input "the dedicated PR session identity" → "the PR-30 and PR-35 session identities" (the registry's :3708 wording) | PR-40 1 |
| X28 | PR-40 result "dedicated PR session and whole-change IA context" → "PR-30 and PR-35 sessions and whole-change IA context" | PR-40 1 |
| X29 | the same, mid-sentence | OPS-20 1 |
| X29a | "one PR session per planned PR work unit." → "one planned PR work unit run in two dedicated sessions, PR-30's and PR-35's." | OPS-10 1, PR-10 1, PR-20 1, PR-30 1, PR-40 1 |
| X30 | ESC-40, PR-35 route "in that same session/open PR." → "in the recorded phase's own dedicated session and the same open PR." | ESC-40 1 |
| X31 | "preserving the same PR session when one exists" → "preserving the recorded phase's own dedicated session when one exists" | PR-10 1, PR-20 1 |

Placement choices a reviewer should check (E5, "the body rules script's anchors"):
- **C-HANDOFF** keeps the block-shape sentence or sentences verbatim, apart from the S13V verb. It replaces the run of field-list sentences that follows, up to the first sentence about terminal or no-block behaviour, which is kept.
- **C-PLACE and C-TOP** form their own paragraph after the handoff paragraph.
- **C-ART** goes first in the first result/output-headed section that names the registry output artifact. C-DEC follows it.
- **C-LAT placement.** C-LAT goes directly under the first of these that the body has:
  1. a heading naming rescope or an RS route;
  2. failing that, the first section with a line routing to RS-10 or RS-20;
  3. failing that, one routing to any RS prompt;
  4. failing that, the first heading naming "material". IA-30 falls through to this and uses section #11.
- **C-SUB** goes under PR-35's review heading and under RS-40's `PR_RETURN_PHASE: PR-35` heading.
- **C-DISPATCH** goes after the `MERGE_PENDING — Ready to merge` line.
- **X19** is the only convergence that adds a clause of its own: "(`RETAIN_EXISTING` on re-entry to that PR-35 session)". Without it, the package's `NEW_DEDICATED` would contradict PR-35's own re-entry handoffs.

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
| CL-20 | S42 3, S32 1, CONV-X05 1, CONV-X08 1, CONV-X17 1, CONV-X17b 1, S08 1, S13V 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1 | — | S08: section #13 (result heading naming the output artifact); S13: section #24 (field list on the next line); 3 field-list sentence(s) replaced, 0 kept after it |
| CL-30 | S42 3, S32 1, CONV-X08 1, CONV-X17 1, CONV-X17b 1, S08 1, S13V 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1 | — | S08: section #12 (result heading naming the output artifact); S13: section #24 (field list on the next line); 3 field-list sentence(s) replaced, 0 kept after it |
| CL-40 | S42 3, S32 1, CONV-X05 1, CONV-X08 1, CONV-X17 1, CONV-X17b 1, S08 1, S13V 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1 | — | S08: section #10 (result heading naming the output artifact); S13: section #15 (field list on the next line); 3 field-list sentence(s) replaced, 0 kept after it |
| CL-C-10 | S42 3, S32 1, CONV-X05 1, CONV-X08 1, CONV-X17 1, CONV-X17b 1, S08 1, S13V 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1 | — | S08: section #13 (result heading naming the output artifact); S13: section #15 (field list on the next line); 3 field-list sentence(s) replaced, 0 kept after it |
| CL-E-10 | S42 3, S32 1, CONV-X05 1, CONV-X08 1, CONV-X17 1, CONV-X17b 1, S08 1, S13V 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1 | — | S08: section #13 (result heading naming the output artifact); S13: section #15 (field list on the next line); 3 field-list sentence(s) replaced, 0 kept after it |
| CL-E-20 | S42 3, S32 1, CONV-X01 1, S08 1, S13V 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1 | — | S08: section #10 (result heading naming the output artifact); S13: section #6 (same line); 3 field-list sentence(s) replaced, 1 kept after it |
| CL-E-30 | S42 3, S32 1, CONV-X01 1, S08 1, S13V 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1 | — | S08: section #10 (result heading naming the output artifact); S13: section #6 (same line); 3 field-list sentence(s) replaced, 1 kept after it |
| CL-E-40 | S42 3, S32 1, CONV-X01 1, S08 1, S13V 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1 | — | S08: section #10 (result heading naming the output artifact); S13: section #6 (same line); 3 field-list sentence(s) replaced, 1 kept after it |
| DOC-10 | S42 3, S32 1, CONV-X01 1, CONV-X02 1, S22 1, S22-before 1, S22-literal 1, S08 1, S13V 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1, C-LAT 1 | — | S22: section #12 (first section with a sentence routing to RS-10/RS-20); 'material boundary' replaced 1 in routing sentences after C-LAT; 1 before C-LAT replaced by 'material change (D23-C)'; 0 occurrence(s) remain in the body; S08: section #11 (result heading naming the output artifact); S13: section #6 (same line); 3 field-list sentence(s) replaced, 1 kept after it |
| DOC-20 | S42 3, S32 1, CONV-X01 1, S22 1, S08 1, S13V 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1, C-LAT 1 | — | S22: section #12 (first section with a sentence routing to RS-10/RS-20); 'material boundary' replaced 0 in routing sentences after C-LAT; 0 before C-LAT replaced by 'material change (D23-C)'; 0 occurrence(s) remain in the body; S08: section #11 (result heading naming the output artifact); S13: section #6 (same line); 3 field-list sentence(s) replaced, 1 kept after it |
| ESC-10 | S42 3, S32 1, CONV-X01 1, S08 1, S13V 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1 | — | S08: section #11 (result heading naming the output artifact); S13: section #6 (same line); 3 field-list sentence(s) replaced, 1 kept after it |
| ESC-25 | S42 3, S32 1, CONV-X01 1, S08 1, S13V 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1 | — | S08: section #11 (result heading naming the output artifact); S13: section #6 (same line); 3 field-list sentence(s) replaced, 1 kept after it |
| ESC-30 | S42 3, S32 1, CONV-X01 1, S08 1, S13V 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1 | — | S08: section #11 (result heading naming the output artifact); S13: section #6 (same line); 3 field-list sentence(s) replaced, 1 kept after it |
| ESC-40 | S42 3, S32 1, CONV-X01 1, CONV-X30 1, S08 1, S13V 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1 | — | S08: section #12 (result heading naming the output artifact); S13: section #6 (same line); 3 field-list sentence(s) replaced, 1 kept after it |
| GCFPE-MGMT-10 | S42 2 | — | — | — |
| IA-10 | S42 3, S08 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1 | — | S08: section #11 (result heading naming the output artifact); S13: section #13 (same line); 3 field-list sentence(s) replaced, 1 kept after it |
| IA-20 | S42 3, S08 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1 | — | S08: section #7 (first result heading (artifact not named in it)); S13: section #8 (same line); 3 field-list sentence(s) replaced, 1 kept after it |
| IA-30 | S42 3, S22 1, S08 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1, C-LAT 1 | — | S22: section #11 (no section routes to RS; first heading naming 'material'); 'material boundary' replaced 0 in routing sentences after C-LAT; 0 before C-LAT replaced by 'material change (D23-C)'; 0 occurrence(s) remain in the body; S08: section #13 (result heading naming the output artifact); S13: section #14 (same line); 1 field-list sentence(s) replaced, 1 kept after it |
| IA-40 | S42 3, S08 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1 | — | S08: section #10 (first result heading (artifact not named in it)); S13: section #11 (same line); 2 field-list sentence(s) replaced, 1 kept after it |
| IA-50 | S42 3, S08 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1 | — | S08: section #5 (first result heading (artifact not named in it)); S13: section #7 (same line); 2 field-list sentence(s) replaced, 1 kept after it |
| IA-60 | S42 3, S08 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1 | — | S08: section #5 (result heading naming the output artifact); S13: section #7 (same line); 2 field-list sentence(s) replaced, 1 kept after it |
| MGR-10 | S42 2, S05 1, S08 1, S13V 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1 | — | S08: section #4 (result heading naming the output artifact); S13: section #6 (same line); 1 field-list sentence(s) replaced, 0 kept after it |
| OPS-10 | S42 3, S03 1, CONV-X29a 1, S08 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1, C-NOTION 1 | — | S08: section #11 (result heading naming the output artifact); S13: section #22 (same line); 4 field-list sentence(s) replaced, 2 kept after it |
| OPS-20 | S42 3, S03 1, CONV-X29 1, S08 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1, C-NOTION 1 | — | S08: section #12 (result heading naming the output artifact); S13: section #22 (same line); 4 field-list sentence(s) replaced, 2 kept after it |
| OPS-30 | S42 3, S03 1, CONV-X03 1, CONV-X04 1, S08 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1, C-NOTION 1 | — | S08: section #13 (result heading naming the output artifact); S13: section #23 (same line); 4 field-list sentence(s) replaced, 2 kept after it |
| PR-10 | S42 3, S03 1, CONV-X03 1, CONV-X04 1, CONV-X06 1, CONV-X22 1, CONV-X23 1, CONV-X29a 1, CONV-X31 1, S22 1, S22-before 1, S08 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1, C-NOTION 1, C-LAT 1 | — | S22: section #16 (heading names rescope or an RS route); 'material boundary' replaced 0 in routing sentences after C-LAT; 1 before C-LAT replaced by 'material change (D23-C)'; 0 occurrence(s) remain in the body; S08: section #13 (result heading naming the output artifact); S13: section #24 (same line); 4 field-list sentence(s) replaced, 2 kept after it |
| PR-20 | S42 3, S03 1, CONV-X03 1, CONV-X04 1, CONV-X06 1, CONV-X09 1, CONV-X17 1, CONV-X24 1, CONV-X25 1, CONV-X26 1, CONV-X29a 1, CONV-X31 1, C4E 1, S22 1, S08 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1, C-NOTION 1, C-LAT 1, C-PR20-ENTRY 1 | — | C4E: end of section #2; S22: section #18 (heading names rescope or an RS route); 'material boundary' replaced 0 in routing sentences after C-LAT; 0 before C-LAT replaced by 'material change (D23-C)'; 0 occurrence(s) remain in the body; S08: section #13 (result heading naming the output artifact); S13: section #26 (same line); 4 field-list sentence(s) replaced, 2 kept after it |
| PR-30 | S42 3, S03 1, S32 1, CONV-X03 1, CONV-X04 1, CONV-X06 1, CONV-X08 1, CONV-X09 1, CONV-X10 1, CONV-X29a 1, C4Q 1, S13P 4, S22 1, S22-literal 1, S08 1, S20 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1, C-NOTION 1, C-DEC 1, C-SESSION 1, C-LAT 1 | — | C4P: NOT_APPLICABLE (settled): PR-30 has no PR-40 return context, so C-PR30-ENTRY is not placed; S22: section #5 (first section with a sentence routing to RS-10/RS-20); 'material boundary' replaced 1 in routing sentences after C-LAT; 0 before C-LAT replaced by 'material change (D23-C)'; 0 occurrence(s) remain in the body; S08: section #13 (result heading naming the output artifact); S13: section #20 (same line); 4 field-list sentence(s) replaced, 2 kept after it |
| PR-35 | S42 3, S32 1, CONV-X15 1, CONV-X16 1, CONV-X17 1, CONV-X17b 1, CONV-X18 1, CONV-X19 1, C4Q 1, S13P 4, S37 1, S39 1, S22 1, S22-before 1, S08 1, S20 1, S13V 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1, C-DEC 1, C-SESSION 1, C-LAT 1, C-SUB 1, C-DISPATCH 1 | — | S37: section #6; S39: section #9; S22: section #8 (heading names rescope or an RS route); 'material boundary' replaced 0 in routing sentences after C-LAT; 1 before C-LAT replaced by 'material change (D23-C)'; 0 occurrence(s) remain in the body; S08: section #10 (result heading naming the output artifact); S13: section #12 (same line); 5 field-list sentence(s) replaced, 0 kept after it |
| PR-40 | S42 3, S03 1, CONV-X03 1, CONV-X04 1, CONV-X27 1, CONV-X28 1, CONV-X29a 1, C4R 1, W4 1, S22 1, S22-before 1, S08 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1, C-NOTION 1, C-LAT 1, C-REPLAN 1, W4 1 | — | C4R: branch of 10 lines replaced; S22: section #17 (heading names rescope or an RS route); 'material boundary' replaced 0 in routing sentences after C-LAT; 1 before C-LAT replaced by 'material change (D23-C)'; 0 occurrence(s) remain in the body; S08: section #14 (result heading naming the output artifact); S13: section #25 (same line); 4 field-list sentence(s) replaced, 2 kept after it |
| PR-50 | S42 3, CTOP 1 | C-TOP 1 | — | — |
| QA-10 | S42 3, S03 1, S04 6, CONV-X03 1, CONV-X04 1, S08 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1, C-NOTION 1 | — | S08: section #19 (result heading naming the output artifact); S13: section #31 (same line); 4 field-list sentence(s) replaced, 2 kept after it |
| QA-100 | S42 3, S08 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1 | — | S08: section #8 (result heading naming the output artifact); S13: section #9 (same line); 1 field-list sentence(s) replaced, 1 kept after it |
| QA-110 | S42 3, S08 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1 | — | S08: section #8 (result heading naming the output artifact); S13: section #9 (same line); 1 field-list sentence(s) replaced, 1 kept after it |
| QA-120 | S42 3, S08 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1 | — | S08: section #7 (result heading naming the output artifact); S13: section #8 (same line); 1 field-list sentence(s) replaced, 1 kept after it |
| QA-20 | S42 3, S32 1, S08 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1 | — | S08: section #8 (result heading naming the output artifact); S13: section #9 (same line); 3 field-list sentence(s) replaced, 1 kept after it |
| QA-50 | S42 3, CONV-X20 1, S08 1, S13 1, S18A-old-clause-removed 1, S18A 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, ASK-VARIANT 1 | — | S08: section #11 (result heading naming the output artifact); S13: section #12 (same line); 1 field-list sentence(s) replaced, 1 kept after it |
| QA-60 | S42 3, CONV-X21 1, S08 1, S13 1, S18A-old-clause-removed 1, S18A 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, ASK-VARIANT 1 | — | S08: section #9 (result heading naming the output artifact); S13: section #10 (same line); 1 field-list sentence(s) replaced, 1 kept after it |
| QA-70 | S42 3, S32 1, S08 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1 | — | S08: section #9 (result heading naming the output artifact); S13: section #10 (same line); 1 field-list sentence(s) replaced, 1 kept after it |
| QA-80 | S42 3, S08 1, S13 1, S18A-old-clause-removed 1, S18A 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, ASK-VARIANT 1 | — | S08: section #7 (first result heading (artifact not named in it)); S13: section #8 (same line); 1 field-list sentence(s) replaced, 1 kept after it |
| QA-90 | S42 3, S08 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1 | — | S08: section #8 (result heading naming the output artifact); S13: section #9 (same line); 1 field-list sentence(s) replaced, 1 kept after it |
| RS-10 | S42 3, CONV-X06 1, S22 1, S08 1, S13 1, S18A 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, ASK-VARIANT 1, C-LAT 1 | S18A: old `ASK OK?` clause absent | S22: section #7 (first section with a sentence routing to RS-10/RS-20); 'material boundary' replaced 0 in routing sentences after C-LAT; 0 before C-LAT replaced by 'material change (D23-C)'; 0 occurrence(s) remain in the body; S08: section #7 (result heading naming the output artifact); S13: section #8 (same line); 2 field-list sentence(s) replaced, 1 kept after it |
| RS-20 | S42 3, S22 1, S08 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1, C-LAT 1 | — | S22: section #8 (first section with a sentence routing to an RS prompt); 'material boundary' replaced 0 in routing sentences after C-LAT; 0 before C-LAT replaced by 'material change (D23-C)'; 0 occurrence(s) remain in the body; S08: section #8 (result heading naming the output artifact); S13: section #9 (same line); 1 field-list sentence(s) replaced, 1 kept after it |
| RS-30 | S42 3, S08 1, S13 1, S18A 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, ASK-VARIANT 1 | S18A: old `ASK OK?` clause absent | S08: section #7 (first result heading (artifact not named in it)); S13: section #8 (same line); 3 field-list sentence(s) replaced, 1 kept after it |
| RS-40 | S42 3, S32 1, CONV-X09 1, CONV-X11 1, CONV-X12 1, CONV-X13 1, CONV-X14 1, S37 1, S39 1, S08 1, S20 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1, C-DEC 1, C-SESSION 1, C-SUB 1, C-DISPATCH 1 | — | S37: section #6; S39: section #6; S08: section #7 (first result heading (artifact not named in it)); S13: section #8 (same line); 1 field-list sentence(s) replaced, 1 kept after it |
| UTIL-10 | S42 3, S08 1, S13 1, S18 1, CTOP 1 | C-ART 1, C-HANDOFF 1, C-TOP 1, C-PLACE 1 | — | S08: section #6 (first result heading (artifact not named in it)); S13: section #7 (same line); 2 field-list sentence(s) replaced, 1 kept after it |

## E4 gate

| item | result | flags and counts |
|---|---|---|
| 1 Graph | PASS (first run) | 55 nodes, 229 edges, 55 state routes, `validation PASS`, no WARNING. Embedded JSON 575 074 B, `ae2bd159…`. Byte-identical to both bundled copies |
| 2 Parity and routing | PASS (first run) | `validate_graph_contract` `[]` for both copies; `routing_surface` `('fecc319bdd4ce7ee6201cb77d7231861', 284)` |
| 3 Live suites | PASS (first run) | `FLOWMASTER_SUITE_PASS` (default and candidate root), v4 `ok`, `gcfpe-current` `ok`, `cf-validator` PASS. All outputs equal E2's |
| 4 Historical layer | PASS (first run) | All 12 outputs equal the §2 baseline |
| 5 v4 fixtures | PASS (first run) | `fixture_suite_ok: true`, 228/228 |
| 6 Other packages | PASS (first run) | PR skill PASS; relay self-test 230; `amthor` 34 OK; registry structure valid |
| 7 Bodies | PASS | `prompt_bodies_validated` 55 (all members); `prompt_body_checks_not_evaluated` `[]`; `errors` `[]`; exit 0 |
| 8 Registry assertions | PASS: 0 findings | 55 rows, 1 484 assertions, with G06 as approved in (b). §7.7 role parity: clean `[]`; the registry-only removal gives `ROLE_PARITY`; removal from both gives `ROLE_CLAUSE` |
| 9 Regressions | PASS | 43/43 registry-guard regressions exact; G27's clean control on unedited PR-20 gives its finding; guard row counts as specified, plus G25B |
| 10 Closure and records | PASS (first run) | Equal to §4.10 V5; DOC-20 radius 25; `modification_validate.py` 2/2 ok |

### Clean-control hits

None. No guard hits any of the 54 edited main bodies, and that includes G06, G15, G19, G20 and G21. Revision 2 recorded three G06 hits, on CL-C-10, CL-E-10 and RS-40. Each came from a body's own "contains no `NEXT_PROMPT_HANDOFF`" sentence, and G06 (b) clears all three.

## G06, revision 3 (Nathan approved alternative (b), 2026-09-23)

`docs/ephemeral/modifications/evidence/e3/g06_apply.py` applied it to the working-tree registry. The method is the one in `e1_registry_apply.py`:
- a line-anchored replacement of the exact two-line entry, `value` then `rule_id: TOP-001`;
- once per row, on the 53 NPH53 rows, with no YAML round trip of the file.

The final G06 value, `forbidden_regex`, `rule_id: TOP-001`:

```
(?<!\bno )(?<!\bno `)NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n)){0,1500}?(?<!\bno )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit (?:SHA|hash|identity|id)\b|\bremote head\b)
```

Checks, all passing:
- **Semantic diff through `load_data`:** only the G06 value changes, on exactly 53 rows. Every other key and row is unchanged.
- **Assertion count:** unchanged at 1 484.
- **YAML single-quote round trip** of the new entry: equal.
- **Structure check** (`validate_project_prompt_registry.py`): `{"valid": true, "problems": []}`, exit 0.
- **D13 drift** against `docs/graph/parts`: `[]`.
- **G06's clean control over the 54 edited bodies:** 0 hits.
- **Both §7.3 G06 regressions on PR-35** (the sentence after the token, and the sentence at the end of the C-HANDOFF paragraph): each exact, 1 finding (TOP-001).
- **Canonical texts:** all 18 of them and the seven combined paragraphs are silent.
- **Items 7 and 9 after the change:** item 7 still has all 55 bodies validated and no errors; item 9 is still 43 of 43 regressions exact, and G27's clean control still fires.

**Spec-facing change.** This value supersedes spec §7.3's G06 entry. It adds `(?<!\bno )(?<!\bno `)` before the token, so a negated mention of the token no longer opens a window. The term list, the window and its blank-line stop are unchanged. The §7.4 G06 limit gains one line: a `NEXT_PROMPT_HANDOFF` preceded directly by "no " or "no `" does not open a window.

### G06 alternatives, measured

What each one was measured on:
- **Bodies:** all 54 edited main bodies.
- **Regressions:** both §7.3 G06 regressions on PR-35. The sentence " It carries the same session, worktree, branch, PR and head commit." is inserted (1) directly after the token sentence and (2) at the end of the C-HANDOFF paragraph. Each must yield exactly the alternative's own finding.
- **Canonical texts:** all 18 §3 texts in `body_rules.T` and the seven §7.3 combined paragraphs.

| alternative | value change | hits on the 54 edited bodies | G06 regression, sentence after the token | G06 regression, sentence at the end of the C-HANDOFF paragraph | canonical texts (18) and combined paragraphs (7) matched |
|---|---|---|---|---|---|
| (a) | as registered | 3: CL-C-10: "under `docs/ephemeral/` in the repository, committed and pushed on the working branch"; CL-E-10: "under `docs/ephemeral/` in the repository, committed and pushed on the working branch"; RS-40: "no session. Resume only PR-35 responsibilities: reverify same vehicle and remote head" | exact | exact | 0 |
| (b) | `(?<!\bno )(?<!\bno `)` before the token | 0 | exact | exact | 0 |
| (c) | window also stops at C-HANDOFF's "unlinked filenames." and at a heading line | 0 | exact | NOT exact (no finding) | 0 |
| (d) | "working branch" and "remote head" removed (**a weakening**) | 0 | exact | exact | 0 |

- **(b)** clears all three hits, keeps both regressions exact and leaves every canonical text clean. It relaxes nothing for a handoff token that is not negated.
- **(c)** clears the hits but loses regression (2): a sentence appended after "unlinked filenames." falls outside the window.
- **(d)** clears the hits and keeps both regressions, but it no longer catches "working branch" or "remote head" anywhere. **It is a weakening.**

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
| G01 | forbidden_regex | 55 | 0 | 0 | 0 |
| G02 | forbidden_regex | 55 | 0 | 0 | 0 |
| G03 | forbidden_regex | 1 | 0 | 0 | 0 |
| G04 | forbidden_regex | 10 | 0 | 0 | 0 |
| G05 | required_regex | 53 | 0 | 0 | 0 |
| G06 | forbidden_regex | 53 | 0 | 0 | 0 |
| G07 | required_regex | 53 | 0 | 0 | 0 |
| G08 | forbidden_regex | 4 | 0 | 0 | 0 |
| G08A | required_regex | 4 | 0 | 0 | 0 |
| G09 | required_regex | 3 | 0 | 0 | 0 |
| G10 | required_regex | 10 | 0 | 0 | 0 |
| G11 | required_regex | 10 | 0 | 0 | 0 |
| G12 | forbidden_regex | 55 | 0 | 0 | 0 |
| G13 | forbidden_regex | 55 | 0 | 0 | 0 |
| G14 | forbidden_regex | 55 | 0 | 0 | 0 |
| G15 | forbidden_regex | 54 | 0 | 0 | 0 |
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
