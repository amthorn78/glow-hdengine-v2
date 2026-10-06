1

GTWPE-TW-DOCUMENT-RULES-PLAN-DC: the check of the repair's diff (`D26-A` rule 2) for `PLAN` of MODIFICATION-20261006-gtwpe-tw-document-rules, `fd14d32..6679e4b`, after full review 1 of 1. I found one required defect, DC-R1, in the sentences the L5 repair rewrote. The repaired drains and TW-APPLY-10 still require every change-history entry to name the version, and they give every dated entry format the preparation date. HDE CRD Records §4.2's material-change row has no version column and dates each row by the decision it records, and §A names that row among the entries the drains draft. A drain that updates a PF30 record must therefore write a wrong date and a stray version into the row, which then passes every check, or be returned by TW-APPLY-10. The rest holds:
- R-1 and S-1 are fixed, and L5 is fixed for the formats it named.
- The session was right to count L5 and S-1 as required.
- The diff changes nothing the record does not name.

**The brief's hash matches.** `PLAN-DIFFCHECK-BRIEF.md` at `d15badab9a0ef4e2f6818715e88729c11aac2291` is 10,724 bytes, sha256 `7be65241579c8a87ee33a3c2564ce9aa1e65639da5cd1c1cee7831f21d74010b`, the value I was given. `d15bada` adds only that file to `6679e4b`.

**Checks I ran:**
- **Baseline.** `origin/main` as known locally is `b1bd769`. The branch changes nothing under `docs/pfcanon/`. `AGENTS.md` is byte-identical on `main`, at `6679e4b` and at `d15bada`.
- **The repair diff** touches four files, with 353 insertions and 18 deletions: the record, `edits.json`, and the added `PLAN-REVIEW-BRIEF.md` and `PLAN-REVIEW.md`.
- **`edits.json`, compared structurally at `fd14d32` and `6679e4b`.** Unchanged: `modification`, `rules`, `members`, `gtwpe_d1` and `absent_after`, and every edit's ID, member, rule key and `old`. Exactly 8 fields changed, each a `new`:
  - DC-HIST: DRAIN-10-06 and DRAIN-20-06;
  - REC-FIELDS-PF20: RECORD-10-09;
  - REC-CHECK: RECORD-10-12 and RECORD-20-14;
  - REC-FIELDS-PF30: RECORD-20-11;
  - AP-AUTH: APPLY-10-03;
  - AP-VERIFY: APPLY-10-09.
- **Hashes.**
  - `edits.json` at `6679e4b` is 39,555 bytes, sha256 `54fc3da0…6a0364`, which equals «H». At `fd14d32` it was 38,960 bytes, `fc3510c8…a0bb01`, as the record says.
  - `edits_check.py` (`02397646…`) is unchanged.
  - `ctl_check.py` (`4e968007…`) is unchanged, and byte-identical to `evidence/gtwpe-tw-repository-io/ctl_check.py` on `main`.
- **`PYTHONDONTWRITEBYTECODE=1 python3 edits_check.py edits.json`** prints `PASS: every check` and exits 0.
  - 57 edits: DRAIN-10 7, DRAIN-20 9, RECORD-10 14, RECORD-20 18, APPLY-10 9.
  - 8 GTWPE-D1 items read from the decision record.
  - Longest anchors: REC-FIELDS at 210 characters (both record prompts) and AP-REF at 145.
- **The eleven `--inject` faults.** Each exits 1 and is caught by its own code. Some also trip SHARED, OVERLAP or ABSENT.
- **Where I ran it.** The script ran in the working tree, at `d15bada`. Its `edits.json`, `edits_check.py`, `ctl_check.py`, record and GTWPE decision record equal `6679e4b`'s blobs by sha256, so the runs tested the committed bytes.

REQUIRED

**DC-R1: R1, and R2 as R-1 was.**
- **Class and path.** R1: a defect on the normal path of a drain that updates a PF30 record. R2 because `EXECUTE` would land these texts with every check passing.
- **Likelihood.** Low overall, because such drains are rare (PF30.1 holds one record, and it is closed). Certain on that path, because every CRD status change needs a row (HDE CRD Records §3.3).
- **In text the last repair added:** partly; see the last bullet.
- **Text, in `edits.json` at `6679e4b`:**
  - DC-HIST (DRAIN-10-06, DRAIN-20-06): "prepare it as a content redline in the target's own entry format, naming the version TW-APPLY-10 will derive, the baseline version bumped once by the target's established scheme, and, where that format dates an entry, the preparation date as the revision date".
  - AP-AUTH (APPLY-10-03): "which the package carries as a content redline in the document's own entry format, naming the version this plan derives and, where that format dates an entry, the date it derives."
  - Kept beside them, AP-AGREE (APPLY-10-04): "All version, date, change-history and gate values in the revised PF must agree with one another; a disagreement is a blocker returned to the preparer."
- **Evidence:**
  - **§A names this format.** §A, as Nathan approved it, lists it among the entries the drains draft: "an HDE CRD Records entry keeps its own material-change history (§4.2)" (record, lines 241–244).
  - **The row has no version.** HDE CRD Records §4.2 sets the row as `| Date | Affected fields | Approved change or deviation | Decision source | Build Notes reference |`. §3.3 makes every status change material and requires a row. §3.2 puts the update in the same entry.
  - **The row's Date is the decision's, not the revision's.** HDE-CRD-0001's five rows are dated 2026-09-05, 2026-09-05, 2026-09-06, 2026-09-07 and 2026-09-07 (§8, lines 435–439). All five were published in v0.9, effective 2026-09-07 (front matter). §4.4 makes the Closure decision's date authoritative.
  - **The conflict.** Take a drain that records a closure decided on one day and prepared on a later one. It meets a sentence it cannot meet in this format. "In the target's own entry format" conflicts with "naming the version", and because the format dates its rows, the rule gives the row "the preparation date".
  - **If the drain follows DC-HIST,** and TW-APPLY-10 runs the same day, AP-AUTH and AP-AGREE pass. The PF30 replacement then carries a history row dated with the preparation date, which contradicts the record's own Closure decision date. The version sits in a column that does not hold one. No check fails.
  - **If the drain keeps PF30's format and the decision date,** AP-AUTH and AP-AGREE return the package, and DC-HIST sends the next attempt back to the first branch.
  - **What the L5 repair did and did not do.** It fixed the undated formats: HDE CLI-API-Vendor Ref §11.1 and the HDE Copy Tonality Guide's change log. It left the version unconditional, and it gives every dated format the preparation date as a "revision date". Its new words "in the target's own entry format" now contradict "naming the version" for this format.
- **Refutation tried:**
  - (a) "A record's own history is not the document's change history." §A names it as one. The drain's words, "a change or revision history entry for this change", also match §4.2's "material-change history" row.
  - (b) "The version could go in the report." "Naming" attaches to the content redline, and AP-AUTH expects the version in the entry.
  - (c) "§4.2's Date is the revision date." HDE-CRD-0001's rows refute it.
  - (d) "No drain runs on PF30." S-1 rests on the same path, a drain on an existing PF20 or PF30 record, and the session counted that path plausible. If it is not a normal path, S-1 and DC-R1 drop to listed together.
- **Smallest correction:**
  - **In DC-HIST,** change "naming the version TW-APPLY-10 will derive, the baseline version bumped once by the target's established scheme, and, where that format dates an entry, the preparation date as the revision date" to "naming, where that format records them, the version TW-APPLY-10 will derive, the baseline version bumped once by the target's established scheme, and the preparation date as the revision date; a date the format gives another meaning, such as an HDE CRD Records material-change row's decision date, keeps that meaning".
  - **In AP-AUTH,** change "naming the version this plan derives and, where that format dates an entry, the date it derives" to "naming, where that format records them, the version and the revision date this plan derives".
  - **AP-AGREE** then reads its "date … values" as the revision's own. If Nathan wants that explicit, it takes "of this revision".
  - **Then:**
    - Run `edits_check.py` again: SHARED, OVERLAP, ABSENT, EXCLUDED and NODRAFT. None of the proposed words is an anchor, an absent phrase or excluded vocabulary.
    - Fix «H» again.
    - Re-read DC-HIST and AP-AUTH against HDE Governance §9.3.1, HDE CLI-API-Vendor Ref §11.1, the HDE Copy Tonality Guide's change log and HDE CRD Records §4.2.
  - K-4 then holds where a format records a revision date, which on `main` is HDE Governance §9.3.1.
- **In text the last repair added: partly.** The clauses are the repair's: "in the target's own entry format" and "where that format dates an entry". The behaviour predates the repair: an unconditional version, and the preparation date on a dated row. The full review did not raise it.

LISTED (each line: attack item; path; likelihood; consequence; whether it is in text the last repair added)
- **DC-L1 (A3; K-4 in §P's *Open findings*).** K-4 still says "A drain dates the change-history entry it prepares with the preparation date", unconditionally. After the L5 repair that holds only where the format dates an entry, which on `main` is HDE Governance §9.3.1 (the `GOV-YYYYMMDD-…` ID and §9.4's "Date / Author"). Normal path; certain. Nathan would accept a risk stated wider than it is; no sent text is affected. Not in repair text: the repair left K-4 unchanged.
- **DC-L2 (A2; §P's *The edits, by rule*, the DC-HIST row).** The row summarizes the exception as "canon's own, as in a template or a record kept as history, stays", which reads as any marker already in canon. The edit says "unless canon requires that exact language there". This is plan text only, and the sent text governs. Normal path; low. The plan Nathan approves states a looser rule than the prompts carry. In repair text: yes.
- **DC-L3 (A2; DC-HIST and AP-VERIFY).** "a record kept as history" has no bound. Canon binds only PF20 and PF30 to keep records as history: HDE Governance §9.1.1, and HDE Phased Epics §0's drain posture. A drain on another PF could keep a real marker by calling its section history. On `main` there is none to keep: TODO and FIXME occur only in Plan Templates' prohibitions, and TBD occurs only in rule text, in Glow Infrastructure's own convention ("Replace TBD as facts are confirmed") and in HDE Phased Epics §2.6.1. Normal path; low. A kept marker would be visible in the redlines and the proof log. In repair text: yes.
- **DC-L4 (A1; rollover; REC-FIELDS-PF30 and REC-CHECK).** Two rules read naturally of the updated active volume, and neither names the review copy:
  - REC-FIELDS-PF30's "every other byte stays as canon has it, … earlier records among them";
  - REC-CHECK's "each updated file … carry no `Draft`".

  The review copy carries Document status `Draft` (HDE CRD Records §6) and no record (REC-VOL). A literal run could hold the review copy to these rules and stop, or copy HDE-CRD-0001 into it. Rollover path; very low, because only Nathan decides a rollover and REC-VOL is explicit. The outcome is a loud stop, or a review copy he reviews. In repair text: partly; the old REC-CHECK ("no … remains") had the same gap.
- **DC-L5 (A1; REC-FIELDS-PF30's "The inserted record … carry no … placeholder").** Unlike DC-HIST and AP-VERIFY after S-1's repair, this sentence has no "unless canon requires" clause. HDE Governance §9.1.1 allows a record entered with planned state only. Such a record carries HDE CRD Records §7's `Pending` and `Not completed` values, and HDE Governance §9.7.11 calls "pending" non-conforming in acceptance artifacts. Normal path for a CRD not yet closed; low, because historical drainage usually follows closure and §7 defines those as values. A loud stop. In repair text: partly; the sentence was rewritten without the clause.
- **DC-L6 (A3; REC-FIELDS, kept clause).** "Any change or revision history entry the document's own rules require", brought forward "as one set that agrees" with the execution date, could be read to reach an inserted CRD record's own material-change rows. This is DC-R1's root on the record prompts' side. "Any other control date that records this revision" excludes decision dates, and I could not make the misreading the natural one. Normal path for a closed CRD's record; low. Misdated rows, or a stop. Not in repair text; unchanged since `88a0383`.
- **DC-L7 (procedure; §P's *Open findings, accepted as risks*).** At `6679e4b` this table holds K-1 to K-15 only. The review's L1 to L4 and L6 to L15, and this check's findings, are not yet there. They must be added, with their reasons, for Nathan's approval to accept them (template rule 8 and its §P section; `D26-A` rule 4; `DISP-001`). In flight, for PL4; certain. Without them his approval accepts none of them. Not in repair text.

**Prior required findings, and the trend:**
- **R-1: fixed.** REC-FIELDS-PF20 and REC-FIELDS-PF30 now hold only the inserted entry and the control fields to the no-Draft rule, and keep every other byte. REC-CHECK checks the same. On `main`'s PF20 and PF30.1, a normal run meets REC-OUT, REC-FIELDS and REC-CHECK together (A1). The rollover wording is DC-L4.
- **S-1: fixed.** DC-HIST and AP-VERIFY now except what canon requires there, so HDE Phased Epics §2.6.1's TBD stays and passes (A2). DC-L2 and DC-L3 remain.
- **L5: fixed for the formats it named.** HDE CLI-API-Vendor Ref §11.1 and the HDE Copy Tonality Guide's change log stay undated. HDE Governance §9.3.1 stays dated, and K-4 holds there (A3). DC-R1 is a distinct defect left in the same two sentences. DC-L1 is K-4's stale wording.
- **Trend:** from 3 confirmed required findings (review 1, with the session's counts) to 1 (this check). The count has halved, so `D26-A` rule 5's halving test passes. Of this round's 8 findings, 2 sit wholly and 3 partly in text the last repair added.
- **The cap.** This check is the last round the cap allows (`D26-A` rule 2; Nathan's approval), so the plan goes to Nathan with DC-R1 and every listed finding open.

**Attack items, answered:**
- **A1 (R-1's repair).** On the normal path, a record run now meets every rule at once on `main`'s files.
  - **PF20.** TW-RECORD-10 copies PF20, inserts its entry after §2.25, and brings forward the version, the effective date and the gate. §1's fourteen `\<allocated\>` entries ("MAY remain `<allocated>` indefinitely") stay, and so does §2.6.1's TBD, as HDE Governance §9.1.1 and PF20 §0's drain posture require.
  - **PF30.1.** TW-RECORD-20 does the same. The new record goes in §8 after HDE-CRD-0001 and before `\<eof\>`, and the §7 template stays.
  - **Nothing left stale.** Neither document indexes its records outside the record sections; only the gate names the latest one. Keeping every other byte therefore leaves nothing stale.
  - **On a rollover.** Volume status and *Next volume* are fields of PF30.1's "Front Matter — Document Control". "The control fields" therefore covers REC-VOL's changes to them, and "every other byte" does not reach them. REC-FIELDS' own control fields are exactly what "every other byte" excludes. The review copy is DC-L4.
  - **A stale status outside the header.** On `main` neither file has one. PF30.1's "remains active until the Product Owner determines …" (§1) and "is Active at initial canonical publication" (§6) stay true after a rollover. The records' statuses are history that the record prompts may not revise.
  - **L4.** "Earlier records among them" now tells a run to leave HDE-CRD-0001's "Last material update" alone, which lowers L4's risk. L4's own text is unchanged, as the record says.
- **A2 (S-1's repair).** Faithful.
  - **The words.** "Unless canon requires that exact language there" is ITEM-03's "except where canon requires it". It is also the target architecture §4's "unless that exact language is independently required by the canonical document format", widened from the document's own format to canon. PF20 needs that widening, because a rule in another document, HDE Governance §9.1.1, keeps PF20's history.
  - **The placeholder bullet.** §4's placeholder bullet has no exception, but it forbids what a writer leaves. A template's placeholders and a dated history are canon's own content. Removing them would leave the document unfit to replace canon, which fails §4's own test.
  - **Not silent.** §A's ITEM-03 called the review copy "the one exception". The repair adds two cases of the same principle, and *Repair round (PL3)* and the selection page say so openly, so it is not a silent breach.
  - **A real drafting marker.** See DC-L3 and DC-L2. On `main` there is none to keep.
  - **The session was right about the old wording.** Its exception was keyed to "the document's own canonical format", which does not require "TBD" in §2.6.1. It ordered a drain to "remove any such marker anywhere in the target". PF20 is a Build Notes drain target (§0: "During drains, do not mass-edit historical epic records"). So a drain on PF20 would have been told to rewrite a dated record, and AP-VERIFY would have stopped a drain that kept it.
- **A3 (L5's repair).**
  - **Undated formats.** HDE CLI-API-Vendor Ref §11.1 ("One line per version"; entries such as "v2.4.6 — … Sentinel updated: NO.") and the HDE Copy Tonality Guide's change log ("**v1.2.0**: …") carry a version and no date. Their entries now name the version and no date.
  - **HDE Governance §9.3.1.** Its grammar opens with `<PF04-version>`. Its entry is dated by its `GOV-YYYYMMDD-<shortslug>` ID and by the nested §9.4 record's "Date / Author", so it takes the preparation date, and K-4 holds there.
  - **Agreement.** For these three formats, DC-HIST and AP-AUTH agree with each other, with AP-AGREE and with AP-VERIFY.
  - **HDE Schemas and Artifacts** attaches its Doc-Delta to the change instead of logging it in the document (§9.1, §9.2). No in-document entry is drafted there, and the repair does not change that.
  - HDE CRD Records §4.2 is DC-R1. K-4's wording is DC-L1.
- **A4 (the counts).** Both are right under `D26-A` rule 3, and neither needed Nathan's opt-in.
  - **L5** is a normal-path defect. Every drain on HDE CLI-API-Vendor Ref or the HDE Copy Tonality Guide that logs a normative change would add a date their entries do not carry, or would meet AP-AUTH's expectation of one. Rule 3 counts a normal-path defect whatever its size.
  - **S-1** is R4, and a normal-path defect for PF20's Build Notes drains. The hygiene rule ordered a destructive edit to a dated record, and nothing would have flagged it, because the rule itself authorized the edit.
- **A5 (the diff and the account).**
  - **The diff changes nothing *Repair round (PL3)* and the added sections do not name.** Its hunks in the record are:
    - the `reviews` entry and «H»;
    - five rows of *The edits, by rule*;
    - the two *SECTION* sentences and A1-NEW;
    - *Full review (PL3)* and *Repair round (PL3)*;
    - three *Harness files* entries.

    In `edits.json` it changes the eight `new` texts above. No anchor, member, edit count, value, step or Notion write changed. No readback string uses the changed words (X4.3, and X4.4's and X4.6's `--has` strings).
  - ***Full review (PL3)*'s account is true where the repository can check it:**
    - the brief is 13,907 bytes, sha256 `97460f5f…`, identical at `3a12db1` and `6679e4b`;
    - `3a12db1` was committed at 13:09:07Z;
    - `PLAN-REVIEW.md` is 20,443 bytes, sha256 `302b5671…`, ends in one LF, has first line `1`, and carries its Canon block;
    - the review found 1 required and 15 listed findings.
  - **R-1's evidence reproduces on `main`:**
    - 46 PF30.1 lines have a backtick directly before `<` (45 by the reviewer's count, 48 counting any backticked `<…>`);
    - §2.6.1 reads "Date completed: TBD";
    - §1 holds fourteen `\<allocated\>` entries;
    - §9.1.1's sentence is as quoted.
  - **Times and tokens.** The 32 minutes and 548,728 tokens are the harness's figures, and the repository cannot check them. They fit the commit times: `3a12db1` at 13:09:07Z, the reviewer's hook note at 13:36:13Z, `6679e4b` at 13:49:09Z.
  - **The ledger.** The `reviews` entry's `required_open: 3` counts the round's confirmed required defects before the repair, as its outcome says.

**The claims, in one line each:**
- C1 holds (A1).
- C2 holds (A2).
- C3 holds for the three formats, not for HDE CRD Records §4.2 (A3, DC-R1).
- C4 holds (A5).
- C5 holds (A5, and the checks above).
- C6: the counts are right, and the repair creates no new required defect, but it did not close L5's class: DC-R1 sits in the sentences it rewrote.

**Method and disclosure:**
- **Read-only throughout:**
  - `git show`, `diff`, `log`, `rev-parse`, `ls-tree` and `grep`, against commits;
  - `grep`, `sed`, `awk`, `cut`, `wc`, `od`, `sha256sum`, `stat` and `date`;
  - `python3 -I`, reading committed blobs through pipes and process substitution, to print and compare `edits.json`;
  - `edits_check.py` with `PYTHONDONTWRITEBYTECODE=1`. Each exit code I quote is the script's own, from a direct run or a plain `out=$(…)` capture.
- **No fetch.** `origin/main` as known locally is `b1bd769`, the commit the brief names. No Notion, Drive, GitHub, session or agent action. I wrote no file.
- **One side effect, from the harness, not my commands.** The repository's PostToolUse hook rewrites `.git/canon_relied_on_hook.json` after each shell command. The file changed during this check, at 13:51:37Z and again at 14:10:26Z. I saw no output that the harness saved to a file.
- **Not read:** any TW prompt body or Notion page (`D22`; the brief). What I say of kept body text rests on §A, §P, `edits.json` and the full review.
- **Not run:** `modification_validate.py`, `gtwpe_record_check.py` and `ctl_check.py`, which the brief does not list.
- **Not exercised, as for the dry run:** any Notion write, the duplication and its polling, and how Notion renders the new texts (K-5).
- **Scope.** This is the `D26-A` PLAN diff check Nathan directed, not an automated code review, so `AGENTS.md`'s line on CI-exempt paths does not apply.

## Canon relied on
- **`AGENTS.md`**, read first; identical on `main`, at `6679e4b` and at `d15bada`. I relied on:
  - the canon-first rule;
  - PF canon is read-only;
  - the truncation and exit-code guardrail;
  - evidence attribution, currentness and distinct decisions;
  - the code-review-scope line.

  This block is required by the brief's §1, after ledger E-036 (`docs/ephemeral/gtwpe.rewrite/ERRORS.md` on `main`; I read row E-036).
- **PF canon, `docs/pfcanon/` on `main` at `b1bd769`**, unchanged on the branch:
  - HDE CRD Records (PF30.1): the whole document, with §3.2, §3.3, §4.2, §4.4, §6, §7 and §8's HDE-CRD-0001 record relied on;
  - HDE Phased Epics (PF20): front matter; §0 in full, with its template, drain and Build Notes postures; *Phase Exit Criteria*; §1 in full; §2's opening and its heading list; §2.6.1;
  - HDE Governance (PF04): §0.1; §9.1.1 in full; §9.2; §9.3 and §9.3.1 in full; §9.4; §9.7.11; the TBD line of §9.7.7;
  - HDE CLI-API-Vendor Ref (PF05): §0.1; §11.1; §11.2;
  - HDE Copy Tonality Guide (PF15): its header and change log;
  - HDE Schemas and Artifacts (PF12): §0.1; §9.1 and §9.2;
  - Glow Infrastructure (PF07): its front matter and its TBD lines, among them the note "Replace TBD as facts are confirmed";
  - Plan Templates (PF27), Change Process Guide (PF06) and Glow QA Guide (PF19): only the lines a search for TBD, TODO and FIXME found;
  - canon-wide searches on `main`: change-log, revision-history and Doc-Delta headings; dated or versioned history tables; TODO, TBD, FIXME, XXX, "fill later", `[OPEN]` and Draft.
- **Governing documents in `docs/prompt_ecosystem_management/`**, identical on `main` and at `6679e4b`:
  - `gcfpe.decision-record.md`: D20, D21 (D21-C), D22, D24, D25 and D26 (D26-A to D26-F), in full; D23's rulings and its first successor sections;
  - `modification-template.md`: rules 1 to 8, *The Product Owner is never blocked*, the §P template and its *Open findings* section;
  - `ecosystem-change-management.md`: §2 steps 3 and 4; §4's `SCOPE-001`, `EVID-001` and `DISP-001`; §5;
  - `gtwpe/gtwpe.decision-record.md`: GTWPE-D1;
  - I did not open `reviewer-prompt-template.md`. I took the brief's fixed text as given.
- **In flight:**
  - the brief at `d15bada`;
  - the record at `6679e4b`, whole (front matter, §A and §P), and the repair diff `fd14d32..6679e4b`;
  - `edits.json` at `fd14d32` and `6679e4b`, all 57 edits; `edits_check.py`, read and run; `ctl_check.py`, by hash;
  - `PLAN-REVIEW.md`, whole; `PLAN-REVIEW-BRIEF.md`, by hash and size;
  - the target architecture on `main`: PE37's reading and "The target architecture, verbatim", with §4 and §5 relied on;
  - Nathan's approval in `analyze_approved_by`.

DECISION NEEDED: this check is the last round the cap allows (`D26-A` rule 2), so the plan goes to Nathan with DC-R1 open. He decides whether DC-R1 is repaired before he approves the plan, or accepted as a listed risk. A repair would be checked again only on his `review_cap` override. The plan must also carry every listed finding as an accepted risk, with its reason: the review's L1 to L4 and L6 to L15, and DC-L1 to DC-L7.
