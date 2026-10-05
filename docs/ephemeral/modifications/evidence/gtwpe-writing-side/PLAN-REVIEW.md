0

GTWPE-WRITING-SIDE-PLAN-A: full PLAN review 1 of MODIFICATION-20261005-gtwpe-writing-side, at c622a555f1ccecea564cf8a085b7c879906913e9.

The brief's sha256 matched. At 1d738502ebd7dd29db0fb1ea0bf5edbbefbb42a3 it is `59ac3178456de6a10d14bd8d76edaf280466a94474181ff8808b0a0963d408be` (10,881 bytes).

I found no required defect. The 8 body edits, the six catalog texts and the steps hold on the normal path. No new text weakens GTWPE-D1 in substance. Every failure path I traced ends loudly, with a return to Nathan.

I list 8 findings. Two matter most:
- **L1:** X4.2 was not adapted to X1.0's one-part branch. On that branch the run stops loudly instead of landing the other part.
- **L3:** E7's anchor, together with its kept prefix and suffix, puts a 147-character passage of 100526.1 into the evidence. That breaks §P's own "at most 96 characters" and the body's quoting rule.

REQUIRED

None.

LISTED (each line: attack item; finding; path; likelihood; consequence; smallest correction; whether in text a repair added. No repair has run on §P, so none is.)

- L1 (A4, C6): X1.0 says that when one part is blocked "W4 then sends C4 with the other part's texts only". X4.2 is still written for both parts: its pre-read needs C1 to C6 each once, it sends "six replacements", and its readback needs every NEW text plus the readings `GTWPE-RUN-10` 1 in C5-NEW and `P4` 0. Read literally, a PART-02 block (C5 or C6 missing) fails X4.2's pre-read after W1 to W3 have run. That leaves «NEW» made but unselected, so PART-01 is half landed and Nathan must archive it. A PART-01 block fails X4.2's readback after W4 has correctly landed C4 to C6, and the failure path then has Nathan reverse that correct W4. So C6's "no path on which a part lands half" does not hold on this branch. Path: failure. Likelihood: low, since it needs a one-part precondition failure. Consequence: a loud stop (D26-B, IMPLEMENTATION_BLOCKED), not a silent one. Correction: one sentence in X4.2: "When X1.0 blocked a part, the pre-read, the send and the readback cover only the texts W4 sends, and the blocked part's readings are not made." Repair-added: no.
- L2 (A1, C3): E6 restates GTWPE-D1's combined-log exception as "one combined proof log it explicitly defines". It leaves out GTWPE-D1's "that clearly covers both outputs", and its "each proof log's link to its file" is singular, which does not fit a combined log. §P says the new texts cite GTWPE-D1 rather than copy it, but this clause is a partial copy that already differs from its source (DERIV-001). Path: normal path of a later Modification that changes a prompt writing both artifacts. Likelihood: low. No prompt writes both today (§A A.8), E3 and E4 put GTWPE-D1 itself in *Read these*, and E5 forbids any weakening. Consequence: an analysis that relies on E6's list could accept an explicitly defined combined log that does not clearly cover both outputs. Correction: "one combined proof log it explicitly defines that clearly covers both", and "its file or files". Repair-added: no.
- L3 (A5): §P says "A passage of 100526.1's body in §P or its evidence is at most 96 characters". E7's `prefix` (32 characters), `old` (96) and `suffix` (19) are recorded by edits.json and P3 as directly adjacent, so together they hold one contiguous 147-character passage of the body. That is longer than the plan's 96 and longer than the body's rule of "no passage longer than an edit's shortest unique anchor". E7's anchor is also not quite "the clause that edit removes": it is the 89-character clause plus the kept word it recapitalizes, 6 characters longer than the shortest anchor that makes the edit (90, ending at that word's first letter). edits_check.py measures only `old`, so neither the check nor the dry run saw this. It is not a D22 breach: 147 characters are no body, mirror, copy or corpus, and they serve the check in hand. Path: normal. Likelihood: certain, since it is already committed at c622a55. Consequence: 51 more characters of 100526.1 in the repository than the body's rule allows, and a false compliance statement in front of Nathan. Correction: drop E7's prefix and suffix, and check E7 by its new text alone (`Capture`, expected count 1 plus its case-sensitive count in 100526.1, by reading), with X1.7 (5) checking its place; this changes «H». Separately, the brief, which §P lists as an evidence file, quotes a 114-character line as 100526.1's *Read these* text; I cannot check that against the body. Repair-added: no.
- L4 (A3): C6-NEW puts the architecture over design v1.2 ("Where the architecture does not supersede it") and says the build is settled in §A. It sets no order between §A and v1.2 where §A departs from v1.2 on other authority: `gtwpe_redline.py` (v1.2 §8, dropped by the request's item 3), and the reader and lock that were never built (§A A.3). It also says the architecture "governs" without the architecture record's own scope line, which excludes GTWPE-MGMT-10 ("It does not change the TW change prompt"). ITEM-03's frozen wording has the same shape, so C6-NEW does not depart from the item. Path: normal path of later Modifications. Likelihood: low, because C5-NEW settles the three prompts and a reader would most likely take §A as controlling. Consequence: a later ANALYZE reads v1.2's script or lock as still applying and has to ask. Correction: "Where neither the architecture nor that analysis supersedes it, …". Repair-added: no.
- L5 (A3): C5-NEW's "the Flow Manager, a new prompt, and the TW prompts the build extends" reads as three kinds of member, though "a new prompt" describes the Flow Manager (§A A.2: the GTWPE gains one new prompt). Path: normal. Likelihood: certain to stand on the page once W4 lands, with a low chance of a misreading. Consequence: cosmetic. Correction: "the Flow Manager (a new prompt) and the TW prompts the build extends". Repair-added: no.
- L6 (A6): §A says "X4 records T-1 as settled", but no step of §P does so. X4.1's trigger findings start at 31deec4, which is after #572, and X5 returns only X4.1's findings. ITEM-01's disposition, whose source names T-1, carries the settlement only implicitly. Path: normal. Likelihood: certain. Consequence: negligible. Correction: add to X4.1 "and record T-1 as settled by ITEM-01, citing its disposition". Repair-added: no.
- L7 (A4): X1.0 (1) names PART-01's recovery as "a successor plan, Nathan's to order". On that branch, X5 then sets the record `COMPLETE` once PART-02 lands, and a `COMPLETE` record has no successor-plan route; the template's successor section is for a plan stopped before approval. So the recovery is in practice a new Modification. Path: failure. Likelihood: low. Consequence: loud, since IMPLEMENTATION_BLOCKED names the recovery point; cosmetic. Correction: "its recovery is a new Modification, Nathan's to order". Repair-added: no.
- L8 (A1): E8 is GTWPE-D1's guard, and nothing in this change fires it on a text that lacks the requirement. P2's ten faults fire edits_check.py, and P9 and K-2 say no TW page was read. So under D14's second part (GUARD-001) the guard is shipped but unproved. C2's readback will not prove it either, because C2 adds the requirement. Path: normal. Likelihood: certain. Consequence: a later report could call GTWPE-D1 guarded in D14's sense; the record itself claims only that ITEM-01 "ships its guard". Correction: none needed in the texts. A dry run could fire E8 by reading it against a synthetic bound-prompt text that lacks one minimum item, or X5's return can say the guard is unfired. Repair-added: no.

Claims

- **C1 holds on the normal path.** Every value is fixed once. Every Notion write has exact text: edits.json printed by script, and *The catalog texts* quoted in full. Every step's check could fail. Off the normal path, see L1 and L7.
- **C2 holds.** E3 and E4 (the record is read), E6 (the ANALYZE record), E8 (the readback by phrase) and E5 (never drops or weakens) carry ITEM-01. E7 carries ITEM-02. E1 and E2 are the identity lines. Nothing else is changed.
- **C3 holds, with L2.**
  - No new text weakens GTWPE-D1 in substance.
  - I found no breach of GTWPE-D1, D21-C, D22, D26-A to D26-E, or the merge rule as the second repair's E7 put it into the body. L3 breaks the body's stricter quoting rule, not D22.
  - I can check whether the new texts contradict kept body text only against the quoted passages and the earlier repairs' evidence. Nothing there conflicts, and K-3 stands.
- **C4 holds together with X1.7 (5).**
  - Check (4), the headings and the readings alone would not stop on a truncated tail of E5, E6 or E8 whose check phrases survive. The `proof` reading would fall, but that is read, not a stop. Check (5) catches it.
  - A duplicated edit doubles a count.
  - A misplaced edit cannot happen when each anchor is found once, and (5) checks the place.
- **C5 holds.** W1 to W4 are the only Notion writes, each within the authority it cites. A reversal of W4 would rest on Nathan's own new direction.
- **C6 holds for the send but not for the rest of X4.2 (L1).** W4 never sends a blocked part's text.

Attack list, answered

- **A1. E6 and E8 do not weaken GTWPE-D1 in substance.**
  - The combined log: L2.
  - Every minimum item: E6 and E8 both require it.
  - The link: E6 names it, and E8 covers it as minimum item 8.
  - A prompt that writes an artifact only after the change: E6 says "before or after the change", and E8 runs on the new page.
  - Retirement and merger: E6 says "adds, merges or retires", and E5 says "retirement". A skill is outside E6 and E8 but inside E5, and no skill writes either artifact today (§A A.2).
  - E8 can be applied mechanically once the later plan fixes the phrases for the requirement and for each item. Plan completeness already demands that (modification-template.md rule 4 and its §P paragraph). E8 itself names no phrase list.
  - K-2 stops a later repair loudly, at that plan's dry run or at its readback; it does not silently block or distort it. The growth comes from GTWPE-D1's own consequence ("leaves the requirement in full"), not from E8.
  - Guard status: L8.
- **A2. E5 is Nathan's rule as GTWPE-D1's "What follows" words it ("drop or weaken").**
  - "Drops" covers "omitted" and "lost", and "retirement" widens the rule.
  - The gloss names what GTWPE-D1 requires and binds any prompt that writes either file, as GTWPE-D1 does by function, so it does not narrow its scope.
  - After E3 and E4, "A ruling is not relitigated" follows both files' rulings, so it covers both records.
  - "The GTWPE's own", set against the GCFPE list before it, reads clearly as the GTWPE's own rulings.
- **A3. C5-NEW and C6-NEW carry ITEM-03.**
  - They agree with §A A.2 (one new prompt; the design's three prompts not built) and A.5 (C6 selects every member), apart from L4 and L5.
  - C6-NEW keeps the *Read these* line true. The catalog still names design v1.2 under design/, so the line resolves to v1.2 and its §6 handoff table, and rows H11 to H13 still resolve (§A risk 9).
  - C4's old text is the first sentence of the line the second repair wrote, so the history reads «M», then 5cbfc74, then f83c755.
  - C3-NEW's rendered form is the one the second repair's X4.2 observed.
  - X4.2's readings follow from P4: `GTWPE-RUN-10` 1 to 1, now in C5-NEW; `P4` 1 to 0; `GTWPE-DESIGN-v1.2` 1 to 1, now in C6-NEW.
  - No catalog old text occurs in any catalog new text, in either order, so each matches once and a second send fails rather than duplicates.
  - The gap is the blocked-part branch (L1).
- **A4. X1.0's per-part rule is sound, apart from L1 and L7.**
  - X1.0 follows the carry-on rule the brief quotes: PART-01 and PART-02 are independent (`after: []`), a precondition both parts share stops the run, and from W1 on D26-B freezes both parts, as D26-B requires.
  - X5 is right when one part was blocked before any write. `COMPLETE`, with that part's items `BLOCKED` and the other part's `VERIFIED`, passes modification_validate.py: its `_half_applied` fires only on a part that mixes applied and blocked items, and its own fixture holds a blocked PART-02 beside a landed PART-01.
  - Returning IMPLEMENTATION_BLOCKED, ending DECISION NEEDED, is design v1.2 §11.8's return for a named blocker.
- **A5. edits.json's mechanics hold, apart from L3.**
  - edits_check.py returns PASS, exit 0: 8 edits, 9 check phrases, 2 absent phrases, 4 readings, longest old 96 characters (E7).
  - In memory, with no file written, each of its eight codes fired on its own injected fault.
  - A cross-check the script does not make found:
    - no old inside another edit's old, new, prefix or suffix;
    - no check phrase inside kept text or an old alone;
    - each absent phrase only in its own old (`100526.1` in E1's and E2's, as P3 says).
  - Eight replacements in one call: E5, E6 and E8 keep their olds, so a second send could duplicate them. No path resends W3, E1 comes first and would no longer match, and X1.7 (4)'s exact counts would catch a duplicate.
  - Kept text: E1 is 33 + 10 characters and E2 is 14 + 10; E7's 32 + 96 + 19 is L3.
  - The readings' arithmetic matches:
    - `gtwpe_redline` 1 − 1 + 0 = 0;
    - `proof` 2 + 5 = 7 (E5 1, E6 3, E8 1);
    - `GTWPE-D1` 0 + 4 = 4;
    - `decision-record` 3 − 1 + 2 = 4.
- **A6. The steps hold, apart from L6.**
  - «V»'s rule gives 100526.2 for 2026-10-05, as the earlier repairs' rule did. It also makes X1.0 (2)'s free-title check hold by construction.
  - X2 going straight on to X4 is 100526.1's own X2, as the second repair ran it.
  - X4.1 starting from 31deec4 continues §A's A0 over 5cbfc74..31deec4, so 5cbfc74..«M» is covered. C4-NEW records «M» the same way the second repair recorded 5cbfc74. T-1 is L6.
  - W4's six texts and their readback: see A3.

Refuted (not findings)

- **GTWPE-MGMT-10 bound by GTWPE-D1 because edits.json is a set of replacements.** It is JSON for a prompt body, not a redlines Markdown file for a PF document, so P9 holds.
- **E5's gloss narrowing GTWPE-D1.** See A2.
- **E8 silently blocking a later repair of a TW writer.** See A1.
- **A concurrent, unselected 100526.2.** The version rule would give 100526.3, and the other run's own X4.2 pre-read would stop it loudly.

Canon relied on

- **`AGENTS.md`:** the canon-first rule; PF canon is read-only; the truncation guardrail.
- **HDE Governance (PF04) §9.1.6, read in full on origin/main at 31deec4.** Relied on for the maintenance interface, the disposition of every other member, the readback of changed published bodies, author/checker/acceptor, and the single-homing of GCFPE bodies. A short excerpt is no executable body (L3).
- **HDE Build Notes (PF10) 2.38 PF10-AINEUTRAL-001, read in full to the file's end marker.** Notion writes keep the authority canon requires, and the surface that performs them confers none (PO-1). The addendum index ends at 2.38. No addendum governs proof logs, prompt-body quoting or the GTWPE catalog.
- **A search of `docs/pfcanon/` at 31deec4 for "proof log":**
  - It found nine hits, in HDE Governance, the Change Process Guide, the Separation build checklist, HDE Schemas and Artifacts, the HDE Mechanics Guide, the Glow QA Guide ("proof logic") and HDE Phased Epics. Each, read in the context of its line, is an engine evidence log.
  - Canon is therefore silent on technical-writing proof logs, and GTWPE-D1 governs.
  - `docs/pfcanon/`, `AGENTS.md` and `docs/prompt_ecosystem_management/` are byte-identical at 31deec4 and c622a55.
- **Governing documents:**
  - `gtwpe/gtwpe.decision-record.md`: GTWPE-D1 and what follows from it.
  - `gcfpe.decision-record.md`: D14 with its note of 2026-09-23, and D20 to D26.
  - `modification-template.md` 2.1.
  - `ecosystem-change-management.md`.
  - `reviewer-prompt-template.md`, both templates, the second in use.
  - `notion-write-boundary.md`.
  - `prompt-body-content-policy.md`.
  - `modification_validate.py`'s part rules and fixture.
  - `gtwpe_record_check.py`'s header.
- **Precedent and sources:**
  - The second repair's record (§P and §E) and evidence, its PLAN-REVIEW.md included.
  - The first repair's edits.json.
  - Design v1.2 §11: the route table, §11.6 to §11.8, and the A0 and X4 rows.
  - Implementation plan v1.2 §4.
  - The target architecture record.

Method and disclosure

- **Files under review, at c622a55:**
  - the record: 99,172 bytes, sha256 f352c6e1…46bb045;
  - edits.json: 5,899 bytes, sha256 addb3d31…2ad53f, equal to «H»;
  - edits_check.py: 4,776 bytes, sha256 46f58885…e696c1.
  - The working-tree copies of the two evidence files hash the same, and 1d73850 adds only the brief.
- **Commands, all read-only:**
  - git `show`, `log`, `rev-parse`, `cat-file -t`, `ls-tree`, `grep`, `diff --stat` between commits, and `branch -a`;
  - `grep`, `sed`, `awk`, `cut`, `head`, `wc`, `sha256sum`, `ls`, `stat` and `date`;
  - edits_check.py once, on the committed edits.json through process substitution, with PYTHONDONTWRITEBYTECODE=1. Its exit code, 0, is its own;
  - python3 with PYTHONDONTWRITEBYTECODE=1, on JSON and source read from git show, for the in-memory faults and cross-checks.
- **Not run:** modification_validate.py and gtwpe_record_check.py, which the brief does not list. What I say of them rests on reading their source.
- **No actions outside reading.** I made no fetch; no Notion, Drive, GitHub or session action; ran no agent; and wrote no file.
- **One harness side effect.** The repository's own PostToolUse hook (`.claude/settings.json`, running `.claude/hooks/check_canon_relied_on.py`) runs after each Bash call. It keeps its state in `.git/canon_relied_on_hook.json`, which shows a modification time of 2026-10-05T13:25:34Z, during this review. I issued no command that writes that file, and it touches no tracked file.
- **100526.1 not read.** I did not read it (D22; the brief). What I say of its kept text rests on §A's and §P's readings, the brief, and the earlier repairs' evidence. Every passage of 100526.1 I quote here is already quoted in the record, its evidence, the brief or design v1.2. Every file I relied on was read whole or by the sections named, with no truncated read.
- **Not exercised, as for the dry run:** any Notion write; the duplication and its polling; Notion's rendering of the new texts (K-4); and E8 on a live TW page (K-2).
- **Review scope.** This is the D26-A PLAN review Nathan directed, not an automated code review. `AGENTS.md`'s review-scope line for CI-exempt paths does not apply to it.

DECISION NEEDED: This review found no required defect. Under Nathan's direction, no second reviewer or diff check follows, and the plan goes to him for approval with L1 to L8 as accepted risks. He can opt in to repairing any of them, priced as another round (D26-A rule 4). If he does, I would take L1 and L3: each is a one-sentence change, and L3's changes edits.json and so «H».
