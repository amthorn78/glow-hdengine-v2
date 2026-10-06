0

GTWPE-TW-DOCUMENT-RULES-PLAN-DC2: the second check of a repair's diff for `PLAN` of MODIFICATION-20261006-gtwpe-tw-document-rules, `87b6058..8bd0b38`. It runs past `D26-A`'s cap on Nathan's `review_cap` override of 2026-10-06.

**Result: no required defect. DC-R1 is fixed.**
- The repair applied the first checker's two strings byte for byte and changed nothing in `edits.json` beyond the three texts it names.
- A drain that updates a PF30 record now gives the material-change row its decision date and no version. TW-APPLY-10 accepts that row on the natural reading of AP-AUTH and AP-AGREE.
- I list five findings, three of them in the repair's own text. None of those three can lead to more than a loud return to the preparer.
- DC2-L4 is outside this diff. It is a re-dating with no stop, and it needs a misreading.

**The brief's hash matches.** `PLAN-DIFFCHECK-2-BRIEF.md` at `e7d04086be45569c25c63372cc535651df5d7e51` is 9,854 bytes, sha256 `5b98896b37cf398f2768a79be9086ec4ecc47b83dd61b87b18d4b759b66a85ed`, the value I was given. `e7d0408` adds only that file to `8bd0b38`.

REQUIRED

None.

LISTED (each: attack item; path; likelihood; consequence; whether it is in text the last repair added)

- **DC2-L1 (A1, A2; AP-AUTH beside the unchanged AP-AGREE).**
  - **The texts.** The drains now say "a date the format gives another meaning, such as an HDE CRD Records material-change row's decision date, keeps that meaning". TW-APPLY-10 has only AP-AUTH's "naming, where that format records them, the version and the revision date this plan derives", beside AP-AGREE's "All version, date, change-history and gate values in the revised PF must agree with one another".
  - **The gap.** Whether a format's date is "the revision date" is now each prompt's own judgement, and TW-APPLY-10 makes it without the drains' example.
  - **HDE CRD Records: settled.** Canon settles it there. HDE-CRD-0001's five rows are dated 2026-09-05 to 2026-09-07, yet all were published in v0.9, effective 2026-09-07. Read strictly, AP-AGREE would fail every PF30.1 revision on those historical dates, so the strict reading is not the natural one.
  - **HDE Governance §9.3.1: open.** Canon settles it for neither prompt. Its only dates are in the `GOV-YYYYMMDD-…` ID and in §9.4's "Date / Author", and PF04 defines neither. At `87b6058` both prompts dated them by rule.
  - **Path and likelihood.** Normal path (a PF30 record update; a PF04 normative change); low.
  - **Consequence.** When the two prompts judge differently, TW-APPLY-10 returns a correct package with a diagnostic (AP-AGREE; AP-VERIFY's "Any failure stops application"). The drain then resubmits the same date. That is a loud stop that ends with Nathan, never a pass with no stop.
  - **In repair text:** yes.
  - **Smallest correction, if Nathan opts in:** add DC-HIST's own clause to AP-AUTH ("; a date the format gives another meaning keeps that meaning"), or add the first checker's "of this revision" to AP-AGREE.
- **DC2-L2 (A2; K-4).**
  - **The text.** K-4's "as HDE Governance §9.3.1's does on `main`" states the plan's reading as if it were canon's. §9.3.1 gives no meaning to the date in its ID or in §9.4's "Date / Author".
  - **EPIC_BOUND entries.** Such an entry must carry "the same PF04 version, ID" as the epic's Doc-Delta files, so its date is the epic Doc-Delta's own, which the repaired DC-HIST keeps. K-4's preparation date and its next-day return do not reach it.
  - **Path, likelihood, consequence.** Normal path; certain. Nathan would accept a risk stated more firmly, and slightly wider, than canon supports. No text sent to Notion is affected.
  - **In repair text:** yes.
- **DC2-L3 (A4, C2; *Repair round 2 (PL3)*'s table).**
  - **The text.** Its row on *The edits, by rule* says of the DC-HIST and AP-AUTH rows: "Each now describes the repaired text: … and a date the format gives another meaning, such as an HDE CRD Records material-change row's decision date, keeps that meaning".
  - **The mismatch.** Neither the AP-AUTH row nor AP-AUTH's text carries that clause.
  - **Path, likelihood, consequence.** Record text only; certain. A reader of the account may take TW-APPLY-10 to carry the clause that DC2-L1 turns on.
  - **In repair text:** yes.
- **DC2-L4 (outside this diff; AP-REF on PF30.1).**
  - **The text.** AP-REF's guard is "only when it exactly duplicates the document-control value it restates". It does not exclude HDE-CRD-0001's "Last material update: `2026-09-07`", which exactly duplicates PF30.1's Effective date `2026-09-07`. Only the word "restatement" excludes it.
  - **Relation to L4.** L4 records this coincidence for the record prompts, where REC-CHECK stands against it, and names AP-REF's "only when it exactly duplicates" as the guard those prompts lack. On TW-APPLY-10's side that guard does not exclude this field.
  - **Path and likelihood.** Normal path: the first TW-APPLY-10 run on PF30.1, while its Effective date is still `2026-09-07`. Nathan's opt-in now names that path normal for PF30 record updates. Low: the natural reading takes a CRD record's own field as that record's history, not as a restatement of the volume's date.
  - **Consequence.** A closed record's "Last material update" is re-dated to the execution date, with no stop. TW-APPLY-10's kept "Report old/new values" would show it.
  - **In repair text:** no. This repair left AP-REF unchanged.
- **DC2-L5 (procedure; in flight).**
  - **What is missing.** In four places the record stops at PL4, though this round should reach them:
    - *Cost of this mode*: time only to PL4, and interaction cost "8 so far", which is 9 with this round;
    - *Harness files*: nothing for the script that applied this repair, or for this check's transcript;
    - *Canon and rulings relied on, for `PLAN`*: no entry for Nathan's opt-in of 2026-10-06;
    - the `reviews` ledger: no entry for this round.
  - **Path.** In flight. *Repair round 2 (PL3)* keeps the record at `PLANNING` "until the check of its diff returns", so this is the session's next step.
  - **Likelihood and consequence.** Certain. Without these updates, Nathan's approval would rest on a record whose cost, harness and rulings sections end before his opt-in.
  - **In repair text:** no.

**Prior required findings, and the trend:**
- **DC-R1: fixed.** DC-HIST in both drains and AP-AUTH now carry the first checker's correction exactly.
  - A PF30 material-change row gets no version, since §4.2's format records none, and it keeps its decision date.
  - TW-APPLY-10's AP-AUTH asks for neither.
  - The repaired text carries DC2-L1 to DC2-L3. All three are listed; none is required.
- **R-1, S-1 and L5 stay fixed.**
  - The repair touched no text that R-1 or S-1 rests on.
  - It rewrote L5's clause. HDE CLI-API-Vendor Ref §11.1 ("One line per version") and the HDE Copy Tonality Guide's change log still get a version and no date.
- **Trend:**
  - Required findings went from 3 (full review, with the session's counts) to 1 (first diff check) to 0 (this check), so `D26-A` rule 5's halving test passes.
  - Of this round's five findings, three sit in text the last repair added. Under rule 5 that sends the plan back to Nathan, which the cap and his direction already do.

**Checks I ran:**
- **Baseline.**
  - `origin/main` as known locally is `b1bd769`; I fetched nothing.
  - Local `main` (`f83c755`) is an ancestor of it, with no difference under `docs/pfcanon/`.
  - `b1bd769` is an ancestor of `8bd0b38`. The branch changes eight files against it, all under `docs/ephemeral/modifications/`.
  - `AGENTS.md`, `gcfpe.decision-record.md`, `modification-template.md`, `ecosystem-change-management.md` and `reviewer-prompt-template.md` have the same blobs on `main` and at `8bd0b38`.
- **The repair diff** changes two files, 43 insertions and 12 deletions: the record and `edits.json`.
- **`edits.json`, compared structurally at `87b6058` and `8bd0b38`.**
  - Unchanged: `modification`, `rules`, `members`, `gtwpe_d1`, `absent_after`, and every other field of all 57 edits.
  - Exactly three fields changed, each a `new`: DRAIN-10-06 and DRAIN-20-06 (DC-HIST), and APPLY-10-03 (AP-AUTH).
- **Exactness.**
  - I took both strings from `PLAN-DIFFCHECK.md` (25,078 bytes, sha256 `2739e934…e97997`) by pattern.
  - Each old string occurs once in its `new` at `87b6058`. Replacing it gives `8bd0b38`'s text exactly, in all three.
  - The record's *Diff check (PL3)* carries the same strings once its line breaks are joined.
  - DC-HIST is identical in both drains.
- **Hashes.**
  - `edits.json` at `8bd0b38` is 39,797 bytes, sha256 `395394d128a1dae29b220703a4b6579cc413a293d3491b746faf23ff255029a9`, equal to «H».
  - At `87b6058` it was 39,555 bytes, `54fc3da0…6a0364`, and at `fd14d32` 38,960 bytes, `fc3510c8…fa0bb01`, as the «H» row says.
  - `edits_check.py` (`02397646…`) and `ctl_check.py` (`4e968007…`) are the same blobs at both commits.
- **`edits_check.py` on the committed bytes.** I piped its own blob to `python3 -I` with `PYTHONDONTWRITEBYTECODE=1`, passing `edits.json` and the GTWPE decision record by process substitution.
  - It prints `PASS: every check` and exits 0.
  - 57 edits: DRAIN-10 7, DRAIN-20 9, RECORD-10 14, RECORD-20 18, APPLY-10 9.
  - 8 GTWPE-D1 items read from the decision record.
  - Longest anchors: REC-FIELDS at 210 characters (both record prompts) and AP-REF at 145.
  - Each of the eleven `--inject` faults exits 1 and is caught by its own code. `excluded`, `overlap`, `oneline` and `differ` also trip SHARED, OVERLAP or ABSENT.
- **The two texts' history.** I read AP-AUTH and DC-HIST at `88a0383`, `fd14d32`, `6679e4b`, `87b6058` and `8bd0b38`.
- **The validators, read but not run.**
  - `modification_validate.py` lists `review_cap` in `OVERRIDABLE`, and `_review_caps` skips the cap when it is named.
  - `gtwpe_record_check.py` checks for *Harness files* from `PLANNED`, and for *Dry run* subsections. It reads no override, so neither the `PLANNING` status nor the second override name trips it.
- **The clock.**
  - Commit times: `87b6058` 14:20:02Z, `8bd0b38` 16:03:00Z, `e7d0408` 16:03:58Z.
  - The mode's 8-hour meter from 12:30:32Z ends at 20:30:32Z.
  - This check ran after 16:04Z and finished by about 16:30Z, inside the meter.

**Attack items, answered:**
- **A1 (AP-AGREE beside the repaired AP-AUTH).**
  - **Return a correct row?** Only on a reading that holds every date or change-history value in the revised PF to the revision's own. That reading would also fail every PF30.1 revision on HDE-CRD-0001's dated rows, so it is not the natural one. AP-AGREE follows AP-AUTH's list of the revision's own fields, and AP-AUTH no longer asks a format that has no revision date for one. A run that reads it strictly returns the package with a diagnostic: loud (DC2-L1).
  - **Let a wrong row through?** A row given the preparation date, prepared and applied on one day, passes AP-AUTH and AP-AGREE without a stop. But only a drain that breaks DC-HIST's named example writes that row, and TW-APPLY-10 has never compared a content redline's dates with their sources. The repair removed the instruction that made that row the normal path. A stray version needs the same breach, of "where that format records them".
  - **Verdict.** Neither outcome is a required defect.
- **A2 (each format).**
  - **HDE CRD Records §4.2 and §7**, `| Date | Affected fields | Approved change or deviation | Decision source | Build Notes reference |`:
    - the row gets no version, and the decision's date, as in HDE-CRD-0001's rows and as §4.4 makes the closure decision's date authoritative;
    - AP-AUTH asks for neither, so TW-APPLY-10 accepts the row;
    - the volume's own version and dates stay Apply's, under §3.2's "normal PF document versioning".
  - **HDE Governance §9.3.1:**
    - the `<PF04-version>` field takes the derived version;
    - a `NON_EPIC` entry's ID and its §9.4 "Date / Author" take the preparation date if both prompts read them as the revision date, and K-4 then holds; DC2-L1 and DC2-L2 cover the rest;
    - an `EPIC_BOUND` entry keeps the epic files' ID. At `87b6058` a drain could have dated that ID with the preparation date, against §9.3.1's "MUST carry the same … ID", so the repair helps there.
  - **HDE CLI-API-Vendor Ref §11.1 and the HDE Copy Tonality Guide's change log:**
    - §11.1 says "One line per version", with entries such as "v2.4.6 — … Sentinel updated: NO."; the guide's log has entries such as "**v1.2.0**: …";
    - both get a version and no date, as after L5's repair, and TW-APPLY-10 accepts them.
  - **No other formats.** A canon-wide search on `main` finds no other in-document version or date log. Glow QA Guide §13 is an event history, and HDE Schemas and Artifacts §9 attaches its Doc-Delta to the change.
  - **K-4** now agrees with DC-HIST; its example is DC2-L2.
  - **Not findings, outside this diff:**
    - The row's Build Notes reference column meets HDE Build Notes 2.30 PF10-CITE-001, under which a PF document "names HDE Build Notes, at most, by title". Yet §7 asks for an "exact HDE Build Notes reference", and HDE-CRD-0001 cites "§2.16". How a drain resolves that is in its body, which I did not read.
    - The record's "Last material update", whose meaning canon does not fix, is not part of the entry. The one interaction with it that I could reproduce is DC2-L4.
- **A3 (each sentence in its prompt).**
  - **Both read as one sentence.** DC-HIST's is the second sentence of its new text, in three clauses joined by semicolons. AP-AUTH's is the end of its section's first sentence.
  - **DC-HIST agrees with the kept text.** A decision date predates execution by nature, but DC-HIST keeps it for its meaning, not "to force a change". The row goes with a material change, so it is not an identity-only redline. Where a format records a revision date, the preparation date stands as at `87b6058`, under K-4.
  - **AP-AUTH agrees with AP-DATE.** AP-AUTH's "revision date this plan derives" is AP-DATE's execution date. AP-DATE's "any other control date that records this revision" does not reach a decision date.
  - **Two old wording points, not counted.** "The report names it" now follows the new clause, but "that entry" in the next clause fixes the referent, and the same weak antecedent has stood since `88a0383`. "This plan" has stood in AP-AUTH since `88a0383` too.
- **A4 (the diff, the descriptions, the override).**
  - **What the diff changes.** Only what *Repair round 2 (PL3)* names: the status (its last line), the override (its `review_cap` bullet), «H» (*What changed in the evidence*), the DC-HIST and AP-AUTH rows, K-4, DC-R1's and DC-L1's rows, and the three `new` texts.
  - **What it does not change.** No anchor, member, count, value, step, Notion write, control text or readback string. None of the new words is an anchor, an absent phrase, excluded vocabulary or a `D26-E` term.
  - **The descriptions.** The rows, K-4 and DC-L1's row match the texts; the section's own account is DC2-L3. Two passages that still mention DC-R1 read true, as a conditional and as history: DC-L6's row ("would settle the drains' side") and *Diff check (PL3)* ("and open").
  - **The override.** It matches Nathan's "overriding review_cap for one more round" and his "one check of that repair's diff by a fresh checker". `review_cap` is in modification-template.md rule 8 and in `OVERRIDABLE`.
  - **A limit, not a finding.** Once `review_cap` is named, the validator waives the cap wholesale. "The waiver covers that one round" is therefore kept by the session and by Nathan's direction, not by a check. No path runs another round.

**The claims, in one line each:**
- **C1 holds** (A2). TW-APPLY-10 accepts the row on the natural reading; DC2-L1 is the loud exception.
- **C2 holds** for the DC-HIST and AP-AUTH rows, K-4's condition and DC-L1's row. DC-R1's row carries Nathan's likelihood in his words. K-4's example is DC2-L2, and the section's account is DC2-L3.
- **C3 holds where the repository can show it.**
  - Verified: the three `new` texts; «H»; `edits_check.py` with 11 of 11 faults caught; nothing else changed; the override naming `review_cap` for one round.
  - "Verbatim" cannot be checked. Nathan's message appears in no committed file or ref except this record.
  - Every fact in it that the repository holds checks out: «H» `54fc3da0…6a0364` at `87b6058`; `main` at `b1bd769`; the branch only under `docs/ephemeral/`; DC-R1 against §4.2.
- **C4 holds.** The repair adds no required defect.

**Method and disclosure:**
- **Read-only throughout.**
  - Against commits: `git show`, `diff`, `log`, `rev-parse`, `ls-tree`, `cat-file`, `grep`, `for-each-ref` and `merge-base`.
  - Shell tools: `grep`, `sed`, `cut`, `wc`, `od`, `sha256sum`, `stat` and `date`.
  - `python3 -I`, reading committed blobs through pipes and process substitution.
  - `edits_check.py`, run from its committed blob with `PYTHONDONTWRITEBYTECODE=1`.
  - Each exit code I quote is the script's own, from a plain `out=$(…)` capture whose last command is the script.
- **No fetch**, and no Notion, Drive, GitHub, session or agent action. I wrote no file.
- **One side effect, not my act.** The repository's PostToolUse hook rewrote `.git/canon_relied_on_hook.json` during this check (16:22:02Z, 80 bytes), as it did for the earlier rounds.
- **Not read:** any TW prompt body or Notion page (`D22`; the brief).
  - The kept sentence "Do not add identity-only redlines or predate execution to force a change" occurs in no committed file, so I took it as the brief quotes it.
  - What I say of other kept body text rests on §A, §P, `edits.json` and the earlier rounds.
- **Not run:** `modification_validate.py` and `gtwpe_record_check.py`, which the brief does not list; I read their source.
- **Not checkable from the repository:** that *Repair round 2 (PL3)* quotes Nathan verbatim, and that each repaired passage was read again "in P3's fetches".
- **Not exercised,** as for the dry run: any Notion write, the duplication and its polling, and how Notion renders the new texts (K-5).
- **Scope.** This is the `D26-A` PLAN diff check Nathan directed, not an automated code review, so `AGENTS.md`'s line on CI-exempt paths does not apply.

## Canon relied on
- **`AGENTS.md`**, read first. It is the same blob on `main` and at `8bd0b38`. I relied on:
  - the canon-first rule;
  - PF10's authority in the canon;
  - PF canon is read-only;
  - the truncation and exit-code guardrail;
  - evidence attribution, currentness and distinct decisions;
  - the code-review-scope line.

  This block is required by the brief's §1, after ledger E-036.
- **PF canon, `docs/pfcanon/` on `main` at `b1bd769`**, unchanged on the branch:
  - HDE CRD Records (PF30.1) v0.9: the whole document. I relied on its front matter, §1, §3.2, §3.3, §4.1, §4.2, §4.4, §6, §7 (*Record control*, *Material-change history*) and §8's HDE-CRD-0001 record.
  - HDE Governance (PF04) v2.8.6: §0.1; §9.2; §9.3; §9.3.1 in full; §9.4.
  - HDE CLI-API-Vendor Ref (PF05) v2.5.2: §0.1; §11.1; §11.2.
  - HDE Copy Tonality Guide (PF15) v1.2.0: its header and change log.
  - Glow QA Guide (PF19) v3.0.5: §0.1; §13's opening, maintenance rule and classification.
  - HDE Schemas and Artifacts (PF12) v2.9.5: §9.1 and the opening of §9.2.
  - HDE Build Notes (PF10) v13.5:
    - 2.29 PF10-CANON-001 and 2.30 PF10-CITE-001, in full;
    - whole-document searches for change log, change and revision history, material change, last material update, Last Update Gate, effective date, document control, PF30, CRD record, decision date, §4.2, §9.3, redline and TW, which found no addendum on the formats above.
  - Canon-wide searches on `main` for change-log, revision-history and history headings, version or date history tables, version-line logs, and change-history terms.
- **Governing documents in `docs/prompt_ecosystem_management/`**, the same blobs on `main` and at `8bd0b38`:
  - `gcfpe.decision-record.md`: D20, D21 (D21-C), D22, D24, D25 and D26 (D26-A to D26-F, and its tested guard), in full; D23's rulings and its first correction.
  - `modification-template.md`: rules 1 to 8; *The Product Owner is never blocked*; the template's status and override vocabularies; its §P section with *Open findings*; *Validate before claiming a mode is done*.
  - `ecosystem-change-management.md`: §2 steps 3 to 5; §4's `SCOPE-001`, `NORM-001`, `EVID-001` and `DISP-001`; §5; §6.
  - `reviewer-prompt-template.md`: the *ANALYZE and PLAN review brief* template. The brief's §3 and §5 match it, and its §6 differs only in the disclosed record-path sentence.
  - `modification_validate.py` and `gtwpe/gtwpe_record_check.py`: source, read only. `gtwpe/gtwpe.decision-record.md` through `edits_check.py`'s `PROOF` read.
- **In flight:**
  - the brief at `e7d0408`;
  - the record at `8bd0b38`: its front matter, §A's *The change, settled*, and §P whole, with the repair diff `87b6058..8bd0b38`;
  - `edits.json` at `8bd0b38`, with every drain and TW-APPLY-10 edit read, and at `87b6058` for the comparison; AP-AUTH and DC-HIST also at `88a0383`, `fd14d32` and `6679e4b`;
  - `edits_check.py`, read and run; `ctl_check.py`, by hash;
  - `PLAN-DIFFCHECK.md`, whole;
  - Nathan's opt-in of 2026-10-06 as *Repair round 2 (PL3)* quotes it, and his approval in `analyze_approved_by`.

DECISION NEEDED: the check found no required defect, so by Nathan's direction the plan at `8bd0b38` returns to him for approval (PO-1), after the session records this round (DC2-L5). Approving it accepts every open finding §P lists, with DC2-L1 to DC2-L4 added. Repairing any of them is his opt-in, and checking such a repair would need another `review_cap` override.
