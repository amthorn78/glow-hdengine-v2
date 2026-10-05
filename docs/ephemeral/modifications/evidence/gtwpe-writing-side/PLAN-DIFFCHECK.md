1

GTWPE-WRITING-SIDE-PLAN-DC: the check of the repair's diff (`D26-A` rule 2) for `PLAN` of MODIFICATION-20261005-gtwpe-writing-side, over c0c66901794dba5e5bf6765084398d656560ce3a..44a297345c8cd9752a0fc7fa986d60bc07923df8, after full review 1 of 1.

The brief's sha256 matched. At 05d032cae7da5e0258ede4058d9f64e99b30a8f5 it is `322b0391f05c65f932889a246d0ccebd296cdd790c114dd45527e7191abc1f32` (8,059 bytes).

Seven of the eight repairs hold as written, and both checks exit 0 on the committed files. The eighth, L6, does not. It puts the T-1 rule in X4.1, and X4.1 runs before ITEM-01 can be `VERIFIED`. So every successful run would record T-1 as still open. That is one required defect, in text the repair added. Five more findings are listed.

REQUIRED

R-1. R1, normal path.

The text, added by the repair for L6, is in X4.1:
- Edit cell: "Then record §A's trigger finding T-1, the GTWPE decision record, as settled by ITEM-01, citing ITEM-01's disposition, when that disposition is `VERIFIED`".
- Verification cell: "T-1 is recorded as settled, with ITEM-01's disposition cited, or, if ITEM-01 is not `VERIFIED`, as still open".

Evidence:
- **Steps run in order.** *How the plan runs* says each step's check must pass before the next starts.
- **X4.1 comes too early.** It runs before X4.2, X4.3 and X5. X4.2's W4 selects «NEW» (C1 to C3), which is where PART-01 lands. X5 is the step that records item dispositions ("Record every step's and item's disposition").
- **ITEM-01 has no disposition yet at X4.1.** Its `disposition` is empty, and no step before X5 sets it, except X1.0's `BLOCKED` path. Every earlier GTWPE record sets item dispositions at X5: the pilot (its plan's X5), and the first repair, the TW model advice and the second repair (their §E X5 rows).
- **So X4.1's own check records T-1 as still open.** On the normal path, ITEM-01 is not `VERIFIED` at X4.1, and cannot honestly be, since its part has not landed. X4.1's check is then met by recording T-1 "as still open".
- **Nothing revisits T-1.** X5 sets ITEM-01 to `VERIFIED` and returns `ECOSYSTEM_CHANGE_COMPLETE` with X4.1's trigger findings.
- **The finished record contradicts itself and its sources.** The `COMPLETE` record says T-1 is still open, while ITEM-01, whose `source` names T-1, is `VERIFIED`. That contradicts §A's *Drift check* ("X4 records T-1 as settled"). It also falls short of the L6 wording in Nathan's opt-in ("X4.1 also records T-1 as settled by ITEM-01, citing its disposition").
- **The disclosure does not match what the text does.** The *Repair round* explains the added "otherwise as still open" as "since T-1 is settled only if ITEM-01 lands", which presents it as the failure case. By step order, it is the case on every run.
- **The other reading fails too.** If ITEM-01 counted as `VERIFIED` from X1.7, T-1 would be recorded as settled before X4.2 selects «NEW», and would stay settled if X4.2 then failed.

Likelihood: high. It is certain on a literal run of the steps, and is avoided only by departing from them.

Consequence: low.
- The record carries a wrong status for T-1, and X5's return may carry it to Nathan.
- A later reader may treat GTWPE-D1's adoption as open, at the cost of a round trip.
- Nothing stops, and no prompt body or control page is affected.

Smallest correction: move the sentence and its verification clause from X4.1 to X5, after the item dispositions are recorded. There it reads "record T-1 as settled by ITEM-01, citing its disposition, when that is `VERIFIED`; otherwise as still open". Return T-1's status beside X4.1's trigger findings.

In text the last repair added: yes.

LISTED (each line: finding; path; likelihood; consequence; correction; whether in text the repair added)
- L-1 (A5, C5): The *Repair round* says "Nothing else in §P changed", but the diff also adds to *Harness files*' Scratch bullet (the pre-repair copy of `edits.json`, deleted). The addition is true. Path: normal. Likelihood: certain. Consequence: cosmetic. Correction: name it beside the *Evidence files* sentence. Repair-added: yes.
- L-2 (A1, C3): `edits.json`'s `checks` still says each check phrase occurs 0 times in 100526.1 "(dry run P3)". For E7's new phrase `Capture`, that count comes from *Readings for the repair*, not from P3. Path: normal. Likelihood: certain. Consequence: cosmetic, since §P records the count and committed evidence agrees with it. Correction: none now, because editing `edits.json` changes «H»; amend it if the file changes again. Repair-added: no, but the repair's change to E7 makes this unchanged field stale.
- L-3 (A2, C4): P10 fires `e8_guard_proof.py`'s own statement of E8's rule. That statement is a case-insensitive presence check, with the requirement phrase hard-coded as "separate proof log" and the eight items parsed from GTWPE-D1. The script does not read E8's committed text in `edits.json`, so its result would not change if E8's wording did. P10's "taken from `GTWPE-D1` in the decision record" is exact for the items; for the requirement it holds only in wording. Path: normal. Likelihood: low. Consequence: P10 could later be cited as having fired E8's committed text. Correction: none needed to the texts, or say "E8's rule as the script states it". Repair-added: yes.
- L-4 (A3, L1): On the one-part branch, X4.2's added "the readback cover only the texts W4 sends" can be read to drop the page-preservation checks: the opening paragraph, lineage pins, headings and child pages. Path: failure branch (a part blocked at X1.0). Likelihood: low. Consequence: negligible. Each W4 replacement matches once, so collateral change is implausible, and the opposite misreading, checking a text W4 did not send, stops loudly. Correction: "the page-preservation checks are made on every branch". Repair-added: yes.
- L-5 (D26-D): *Cost of this mode* still ends at PL4, about 1 h in. *Nathan's directions* still gives this mode's stop as 15:40Z, though the repair began at about 15:53Z. The round's own text puts the wait for Nathan off the meter, so on-meter time is about 1 h plus the round, under twice the 1.5 h estimate. Path: normal. Likelihood: certain until the round is recorded. Consequence: the cost on the record lags. No stop rule is breached, since Nathan directed the round. Correction: update both when this check enters `reviews`. Repair-added: no.

Prior round and trend
- **Trend.** Full review 1 (`PLAN-REVIEW.md`) found 0 required defects, so no prior required finding needs a disposition. The count went from 0 to 1, which does not halve.
- **Rule 5 signal.** R-1 and L-1, L-3 and L-4, four of this round's six findings, sit in text the repair added. That is `D26-A` rule 5's non-convergence signal. This was the one diff check rule 2 allows.
- **The eight findings Nathan opted to repair:**
  - L1: fixed, with residue L-4.
  - L2 to L5: fixed.
  - L6: fixed with a new defect, R-1.
  - L7: fixed.
  - L8: fixed, with caveat L-3.

Claims
- **C1 holds except for L6.**
  - L1 to L5, L7 and L8 are each repaired where the table says, in the reviewer's own words.
  - L3's restated sentence is true (A1).
  - L6's added branch does not do what its disclosure says (R-1).
- **C2 holds.**
  - «H» `f451dff65c33e506789891709fd928e5b92bfa91fc3116637b129c8280373113` is the sha256 of `edits.json` at 44a2973, 5,815 bytes. The earlier value, `addb3d31…2ad53f` at 5,899 bytes, reproduces at c622a55 and c0c6690.
  - `edits_check.py` returns `PASS`, exit 0: 8 edits, 9 check phrases, 2 absent phrases, 4 readings, longest old 96 characters (E7).
  - `e8_guard_proof.py` exits 0. It reads 8 items. The complete text passes, each text lacking one item fails on that item alone, and the text with no separate proof log fails on the requirement alone.
  - I ran both on the committed bytes through process substitution, and again from the working tree, whose copies equal the committed blobs.
- **C3 holds, given the reading, and committed evidence supports the reading** (see *Refuted*, first bullet).
  - On a page E7 did not edit, `Capture` reads 0 and the absent phrase reads 1, so each check fails. After E7 they read 1 and 0.
  - The anchor occurs once (P3), so E7 cannot land elsewhere, and X1.7 (5) reads its place.
- **C4 holds.** The script reads only the decision record and only prints; with PYTHONDONTWRITEBYTECODE=1 it writes nothing. See L-3.
- **C5 does not hold.** *Harness files* also changed (L-1), and the repair adds R-1.

Attack list, answered
- **A1 (L3).**
  - Dropping the prefix and suffix weakens X1.7 (4) for E7, but only in principle. Check (4) now proves the clause is gone (the absent phrase) and the new word is there (`Capture` 1). It no longer proves the join with the kept text on either side.
  - No plausible landing shows `Capture` once with E7 partial or misplaced. The anchor occurs once, a single-match replacement lands whole or fails, and check (5) reads the place.
  - The restated sentence holds:
    - E7's anchor is 96 characters: the 89-character clause plus the 7-character kept word.
    - Every other anchor is at most 30 characters (E6). E1 and E2 with their kept text are 43 and 24.
    - None of §P's quoted strings is a passage of 100526.1 over 96 characters. The fenced lines over 96 are catalog texts.
    - Neither script holds a body passage.
    - The brief's line is 114 characters, quoted in `PLAN-REVIEW-BRIEF.md`'s A3 as 100526.1's *Read these* line. I cannot check it against the body.
- **A2 (L8).**
  - The parser reads GTWPE-D1's eight items verbatim. The script itself checks that each deficient text fails on its own item alone.
  - It cannot pass on a parsing error. In memory, five injected faults each exited 1:
    - an item deleted (7 read);
    - a blank quote line inside the list (4 read);
    - dashed bullets (0 read);
    - a duplicated item (9 read);
    - the anchor sentence reworded (StopIteration).
  - A reworded item with eight still read passes, by design.
  - P10's row claims no more than the script shows, apart from L-3.
- **A3 (L1 and L6).**
  - X4.2 is mechanical on the one-part branch. The send is X1.0's "C4 with the other part's texts". Each readback check names its text or that text's old phrase. All three readings belong to C5 and C6, so none is made when PART-02 is blocked, and all are made when PART-01 is. The residue is L-4.
  - X4.1's T-1 rule is inconsistent with ITEM-01's disposition and with X5's return: R-1.
- **A4 (L2, L4, L5, L7).** Each new text reads correctly in place.
  - E6 now carries GTWPE-D1's "clearly covers both", and "its file or files" fits a combined log. It still ends without a full stop, as A2's cell does. Its check phrases and the `proof` reading of 7 still hold.
  - C5-NEW matches §A A.2. The Flow Manager is the one new prompt; the Change Manager and the record roles are TW prompts the build extends.
  - C6-NEW now orders §A above design v1.2, an order ITEM-03's frozen wording leaves open. Nathan's opt-in gives that wording, and §A's own departures from v1.2 (A.3) support it.
  - The six catalog texts still each match once, in order: no old text occurs in an earlier new text or in its own. X4.2's readings follow: `GTWPE-RUN-10` 1 in C5-NEW, `P4` 0, `GTWPE-DESIGN-v1.2` 1 in C6-NEW.
  - X1.0 (1) agrees with X5's `IMPLEMENTATION_BLOCKED` return, and no "successor plan" remains.
  - None of these contradicts §A, GTWPE-D1 or the rest of §P.
  - `e8_guard_proof.py` is dry-run evidence, like `edits_check.py`, and no prompt runs it. It is not the script guard §A A.3 rules out.
- **A5.** Beyond the table's eight rows, the diff changes four things:
  - the status line, PLANNED to PLANNING, which the round's prose names;
  - the *Evidence files* rows, which it names;
  - *Harness files*' Scratch bullet, which it does not name (L-1);
  - in 44a2973, `e8_guard_proof.py`'s default path, which *Checks after the repair* names.
  - §A is untouched.

Refuted (not findings)
- **The premise of C3, that `Capture` occurs 0 times in 100526.1.**
  - Design v1.2 §11.6, GTWPE-MGMT-10's specification, has a sentence beginning with a capitalized "Capture". The body does not carry it in that form: the first repair's E24 anchor, which is exact body text, begins "A capture" in lower case.
  - The paragraph title *Capturing a reviewer's or worker's return* and the first repair's E29 account for the two `Capturing` and for `captured`.
  - No edit in the first or second repair's evidence holds `Capture`.
- **X1.7 (4) loosened for E7.** There is no plausible path to exploit it (A1).
- **`e8_guard_proof.py` passing on a parse error.** It cannot (A2).
- **The second commit.** At 4cc7b54, the script fails when run from `git show` through process substitution, even with a path given (IndexError at `parents[4]`, exit 1). At 44a2973, it runs that way with a path given, exit 0. With no path it still fails loudly, which fits its usage line.
- **P3's row and the PLAN `DRY_RUN` ledger entry still name E7's kept text.** They are dated records of that run. *Readings for the repair* says every anchor is as P3 found it.

Canon relied on
- `AGENTS.md`: the canon-first rule; PF canon is read-only; the truncation guardrail; evidence attribution (the tested state is 44a2973's committed bytes).
- **HDE Governance (PF04) §9.1.6**, read in full at 31deec4. I relied on three of its rules:
  - complete changed published bodies are read back;
  - GCFPE bodies are not mirrored in the repository as executable bodies;
  - the actual author, checker and acceptor are recorded.
- **HDE Build Notes (PF10):**
  - 2.29 PF10-CANON-001 (canon consultation; change-process storage in `docs/ephemeral/`) and 2.38 PF10-AINEUTRAL-001, each read in full.
  - The addendum index through 2.38, the last addendum; the file ends after it.
  - No addendum governs proof logs of technical-writing artifacts, prompt-body quoting, the GTWPE catalog or review rounds.
- **Search.** A `git grep` of `docs/pfcanon/` at 31deec4 for "proof log", "mirrored as executable", "read back complete changed", "AINEUTRAL", "prompt body", "GTWPE" and "technical writing prompt".
  - The "proof log" hits are evidence logs for the engine's own checks. Canon is silent on GTWPE proof logs, so GTWPE-D1 governs.
  - `docs/pfcanon/`, `AGENTS.md` and `docs/prompt_ecosystem_management/` are byte-identical at 31deec4 and 44a2973.
- **Governing documents, at 31deec4:**
  - `gcfpe.decision-record.md`: D14 with its note of 2026-09-23, and D20 to D26;
  - `modification-template.md` 2.1;
  - `ecosystem-change-management.md` 1.2;
  - `gtwpe/gtwpe.decision-record.md`: GTWPE-D1.
- **In flight:**
  - the record's §A: *Drift check* and T-1, A.2 and A.3;
  - §P at 44a2973;
  - `PLAN-REVIEW.md` and `PLAN-REVIEW-BRIEF.md`.
- **Precedent:**
  - the second repair's §P and §E;
  - the first repair's `edits.json` (E24 and E29);
  - the X2 and X5 rows of the pilot, first-repair and TW-model-advice records;
  - design v1.2 §11.6.

Method and disclosure
- **Repository:** /home/user/glow-hdengine-v2. Paths here are relative to it.
- **Files at 44a2973:**
  - the record: 111,095 bytes, sha256 `0990073e0ea195113f1e1e22e497f3c02b7295d09aeaa12783102ad72e345943`;
  - `edits.json`: 5,815 bytes, sha256 «H»;
  - `edits_check.py`: 4,776 bytes, sha256 `46f58885fd19e4bfb3284b69e51d794212f0e54f818273b70ade543109e696c1`, unchanged since c622a55;
  - `e8_guard_proof.py`: 3,577 bytes, sha256 `7c6e00c1b9a4116e09487b31e7152914b30b58bfaac9fb0eabc6e793e62c97c8`.
  - The repair is two commits, 4cc7b54 and 44a2973. 05d032c adds only the brief.
- **Commands, all read-only:**
  - git `show`, `diff`, `log`, `grep`, `cat-file`, `rev-parse`, `merge-base` and `ls-tree`;
  - `grep`, `sed`, `cut`, `wc`, `sha256sum`, `stat`, `ls`, `cat` and `date`;
  - python3 with PYTHONDONTWRITEBYTECODE=1, on bytes from `git show` through process substitution, in memory.
  - Each exit code I cite is the producer's own (`out=$(…); rc=$?`).
- **Not run:** `gtwpe_record_check.py` and `modification_validate.py`, which the brief does not list. What the record says of them rests on the record.
- **No action beyond reading.** I made no fetch and ran no `git status`. I took no Notion, Drive, GitHub or session action, ran no agent and wrote no file.
- **One harness side effect.** The repository's PostToolUse hook (`.claude/settings.json`, running `.claude/hooks/check_canon_relied_on.py`) runs after each Bash call. It keeps its state in `.git/canon_relied_on_hook.json`, which was modified during this check (seen at 2026-10-05T16:15:15Z). I issued no command that writes it, and it is not a tracked file.
- **100526.1 not read** (D22; the brief). The only body text I quote is a few words already in the record or its committed evidence.
- **Not exercised:** every Notion write; how Notion renders the new texts; E8 on a live TW page.
- **Scope.** This is the `D26-A` check Nathan directed, not an automated code review, so `AGENTS.md`'s line on CI-exempt paths does not apply.

DECISION NEEDED:
- This check found one required defect, R-1, in text the repair added. X4.1 records T-1 before ITEM-01 can be `VERIFIED`, so every successful run would end with T-1 recorded as still open.
- The required count rose from 0 to 1, and most of this round's findings sit in repaired text (`D26-A` rule 5). This was the one diff check rule 2 allows, so the plan goes to Nathan with R-1 and L-1 to L-5 open.
- Nathan's choice is one of these:
  - approve the plan at 44a297345c8cd9752a0fc7fa986d60bc07923df8 with R-1 and L-1 to L-5 as accepted risks;
  - or direct R-1's correction, a one-sentence move from X4.1 to X5. That changes the plan after its last allowed check, so any further review is his call.
