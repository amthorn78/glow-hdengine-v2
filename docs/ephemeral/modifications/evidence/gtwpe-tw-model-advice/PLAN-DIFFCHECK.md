0 distinct confirmed REQUIRED findings

GTWPE-TW-ADVICE-PLAN-DC: the PLAN diff check of MODIFICATION-20260930-gtwpe-tw-model-advice. I checked the diff 2673c25..e431d25 on the record and ctl_check.py, reading everything at e431d25. I followed the fenced block of PLAN-DIFFCHECK-BRIEF.md at 1a6696d (6,072 bytes between the fences).

All three required findings from review 1 are fixed, and the repair adds no new required defect. I have 9 listed findings, and 8 of them sit in text the repair added. This is the last round allowed by D26-A rule 2 and by Nathan's direction, so the plan now goes to Nathan.

## REQUIRED

None. I tried these candidates and refuted each one:
- **The row check against how Notion shows a mention.** Notion shows a mention as `<mention-page url="https://app.notion.com/p/<32 hex>"/>`. For a child page it puts the page's title inside the tag instead (pilot PF-27; the pilot's ROWS, "character for character"; the first repair's C3). Either way the line contains `app.notion.com/p/«ID»`. The row's ending "; «V»." is plain text after the mention, so it still holds. The repair's dashless 32-hex form of «ID» matches what Notion shows.
- **The save format.** `load()` handles the file the same way as the scratch `ctl.py` that read both real saves in the dry run (P5): a JSON list, the text split at `<content>\n`, and the same three keys.
- **The heading model.** SECTION and HUB-NEW each contain exactly one heading line, and each `old_str` is the anchor heading line alone. So after the write, the heading list is the pre-read's list with the anchor replaced by the new heading and the renamed one. X4.3 and X4.5 do not touch *Alpha 1* or the Hub.
- **The child pages X1.5 creates.** Every X4 pre-read now runs inside its own step, after X1.5.
- **An incomplete delivery.** X2's edit cell names all four files for the third call, and the verification checks against "the three SendUserFile calls", so a missing file would show as a mismatch (see DL-5).

## LISTED

Each line gives: finding | path | likelihood | consequence | in text the repair added.

- **DL-1.** ctl_check.py has only run on synthetic saves. Its first real run is X4.4's pre-read, which comes after X4.3 has already switched the selection page. A parse failure, a reported truncation or unknown block, or an anchor that is not an exact heading line would stop EXECUTE with the selection page on «R» while *Alpha 1*, *HDE TW* and the Hub still name TW-ALPHA-20260929.1. Correction: run `ctl_check.py pre` read-only on both saves in X1.0 (5), or move X4.4's and X4.6's pre-reads ahead of X4.3. | failure | low (the dry run parsed these saves the same way) | loud; the selection is split until D26-B's sweep | yes
- **DL-2.** X4.4 and X4.6 check headings, values and links, but not SECTION's or HUB-NEW's wording as sent, the row descriptions, the two fixed mentions in HUB-NEW, or that SECTION has exactly seven rows. An eighth row, such as TW-ASSESS-10 copied from the historical rows below, or a mangled sentence would pass. X4.3's check by reading has the same gap for wording. | failure | very low | silent wording error or extra row on a control page | yes
- **DL-3.** X4.4's `--has '«PA»'` also matches «S» when the approval and selection fall on the same day, so a missing or wrong «PA» on *Alpha 1* passes then. Correction: `--has "plan approval of «PA»."` | normal (same-day run) | low | silent, cosmetic | yes
- **DL-4.** X4.4 and X4.6 write their pre-read to a scratch state file and do not say to record it in §E. C1 and the *Full review* table say every pre-read is "recorded in §E". | normal | certain | the pre-read's heading list is not kept as evidence | yes
- **DL-5.** X2's verification does not name what the third SendUserFile call must carry, and the change note names the verdicts but not the brief. A delivery missing `D24-BRIEF-tw1.md` is caught only by comparing §E with the edit cell. Correction: "the third carries exactly the brief, both verdict files and the change note", and have the change note name the brief. | failure | low | an incomplete delivery under D24, visible only by comparison | yes
- **DL-6.** No step writes `CHANGE-NOTE-tw1.md`. X2 delivers it "as committed and pushed", and it has to come after X1.4 because it names the verdicts. | normal | certain | the executor has to infer the step | no (gap existed before; carried into the rewritten X2)
- **DL-7.** `python3 ctl_check.py` gives no path or working directory. X1.2's scripts have the same pattern. | normal | low | loud: file not found | yes
- **DL-8.** The *Full review* section says the listed findings are "not repaired, since Nathan has not opted in (`D26-A` rule 3)". The rule for that is rule 4; rule 3 defines what counts as required. | normal | certain | a wrong citation, cosmetic | yes
- **DL-9.** The repaired Values row writes «ID» as 32 dashless hex, but X1.5 (b) still says "«ID» is the returned ID". If the duplication returns a dashed ID and that is used in the X4.4 command, the row check fails on a correct write. | normal | low | loud, after X4.4's write | yes

## Prior required findings, and the trend

| # | Disposition |
|---|---|
| R-1 | **Fixed.** X4.2 to X4.6 each make their own pre-read, after X1.5, and check the readback against it. X4.3 and X4.5 allow for X1.5's child pages. No fixed heading count remains; 31 and 138 now appear only as P5's dry-run results. What is left is DL-4. |
| R-2 | **Fixed.** ctl_check.py is committed and named in both rows. X4.4 checks both headings, the heading list against the pre-read, «S», «PA», and each of the seven rows' «ID» link and «V» ending. X4.6 checks «R», «V», «PA» and «ID:MGMT-10». What is left is DL-1, DL-2 and DL-3. |
| R-3 | **Fixed.** Each archive goes alone, captioned first with its sha256. The brief, both verdicts and the change note follow in one message, each with `tw1` in its name. The change note says what each archive replaces and what Nathan should see: I checked that both revision strings exist in skill_edits.py. It also tells him to install both together and states D24's freeze. What is left is DL-5 and DL-6. |

- **Trend:** required findings went from 3 to 0, so the halving test is met.
- **Most findings in text the repair added:** 8 of the 9 listed findings are, so D26-A rule 5's second signal is met. It changes nothing here, because no further round is allowed.

## The attack list, answered

- **A1.**
  - **The heading model:** exact for both pages (see REQUIRED).
  - **The section extraction:** it runs from the first occurrence of the new heading to the next line holding the renamed heading. That is correct, because «R» does not yet occur on either page.
  - **The save formats:** the list form is the one the dry run read; the plain-dict form is an unused fallback.
  - **Mentions:** they show either as a self-closing tag or with a title inside. Both keep the `app.notion.com/p/<id>` link and the "; «V»." ending.
  - **Could a check pass on a wrong write?** Only for wording, an extra row, or «PA» hidden by «S» (DL-2, DL-3).
  - **Could a check fail on a correct write?** Only if a real save does not parse, which no run has tested (DL-1), or with a dashed «ID» (DL-9).
- **A2.** X4.3 and X4.5 are now mechanical: a pre-read inside the step, recorded in §E, and a readback stated relative to it. Their child-page lists include X1.5's pages. The pilot shows a duplicate does not push the anchor lines down: after its X1 duplication, its X4.3 pre-read still found S-OLD as the page's first line.
- **A3.** Three calls, two with one archive each and one carrying the four .md files, satisfy "one .skill per message". They also match the closeout-residuals precedent (P-109, "An eighth call carries the brief and both verdicts"). The verification tells a complete delivery from an incomplete one only by comparing §E with the edit cell (DL-5).
- **A4.** I found no contradiction with the Evidence files table, X1.3, X1.4, *The D24 brief*, the change note or PO-1 to PO-4. A grep finds no bare `packages.json`, `D24-BRIEF.md` or `CHANGE-NOTE.md` left.

## Claims

- **C1** holds, except that X4.4 and X4.6 do not record their pre-read in §E (DL-4).
- **C2** holds (DL-2 and DL-3 are what is left).
- **C3** holds.
- **C4** holds by reading.

## Canon relied on

- AGENTS.md.
- HDE Governance (PF04) §9.1.6, read in full.
- HDE Build Notes (PF10) 2.38 PF10-AINEUTRAL-001 and 2.31 PF10-HDR-001, read in full, plus 2.29 PF10-CANON-001's storage rule. All from the local `origin/main`, `f83c755`, which I did not fetch.
- In flight: gcfpe.decision-record.md D20 to D26; modification-template.md (its rules and front matter); ecosystem-change-management.md §2 steps 3 to 5, §4 CHK-001 and CHK-002, §5 and §6; reviewer-prompt-template.md; skill-packaging-and-delivery.md.
- The pilot's and the first repair's records, for how Notion shows mentions and for the delivery and diff-check precedents.
- I did not re-review edits.json, guard_proof.py, or skill_edits.py beyond its revision strings; the repair does not change them.

## Method and disclosure

- **What I ran:** reading only. `git show`, `git diff`, `git log`, `git grep`, `git cat-file` and `git rev-parse`, plus grep, sed, awk, cat, wc and sha256sum. PLAN-REVIEW.md is 15,510 bytes with sha256 `470d1e1b…46fe1d2d`, as the record states.
- **git status:** I ran `git status --short` once. Git may refresh its index cache on that command; no ref, commit, tracked file or working file changed.
- **The scratchpad:** I read the author's scratch `ctl.py` and the synthetic saves under `scratchpad/cc/`, with ls and cat only. I used them only to judge how likely DL-1 is. They hold no Notion content.
- **What I did not do:** write any file, run any script or Python, access Notion, GitHub, Drive or any session, or start an agent.

DECISION NEEDED: Nathan approves the plan (PO-1) with DL-1 to DL-9 as accepted risks, alongside L1 to L21, or opts in to repairing any of them. DL-1 is the one worth a look: moving X4.4's and X4.6's pre-reads ahead of X4.3 is a one-line change.
