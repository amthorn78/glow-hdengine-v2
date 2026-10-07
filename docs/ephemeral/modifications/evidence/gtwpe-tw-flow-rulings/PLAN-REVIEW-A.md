4

GTWPE-TW-FLOW-RULINGS-PLAN-A, full PLAN review 1 of at most 2 (D26-A) of MODIFICATION-20261007-gtwpe-tw-flow-rulings, at `1f73053a9c80bf6a6f9d5e0de9f197dc9d2a008f`. I read §P whole, with §A, the front matter and every evidence file. I also ran `edits_check.py`, once clean and once with each of its injected faults.

I found four required defects:
- **R-1.** The hold-back covers PF10 changes only, but DR-1 makes the run account for and route every change that any source carries. So a specification's change belonging to an epic or CRD that is not closed is drafted, and nothing stops the run.
- **R-2.** The triage file gives each change either its documents or a reason, never both. In a run without a specification, the PF20 or PF30 part of a change that also has a general home is never accounted for. Addendum 2.14 is such a change today.
- **R-3.** TW-APPLY-10 is the only one of the six TW prompts that gets no files-only refusal. GTWPE-D2, the selection page, the Hub and P5 all say every TW prompt has one.
- **R-4.** The new handoff table still says rows H11 to H13 are carried unchanged, but this version changes H11.

Apart from these, the steps, the control texts and the readback arguments hold on the committed text. The first live run gets through intake, B1 and its endings; its risks are K-9 and L5. 25 findings are listed below.

REQUIRED

**R-1. R4, a plausible path with a silent outcome; also R2, a control page that states a rule the prompts do not carry.**
- **Text:**
  - TRIAGE-10-E04: "Account for every change in the sources it is given: every PF10 change, each addendum among them, and every change another source carries."
  - TRIAGE-10-E09 and E14 record, for every change, "the epic or CRD it belongs to, if any, and whether the files given show that change closed".
  - G-FLOW-10-E41 (B1 step 6): "Hold back each PF10 change that belongs to an epic or a CRD that the run's files do not show closed, since canon drains a change only after its QA and its closure decision … Then route each document the triage file names for a change not held back".
  - S-HOLD (DRAIN-10-E15, DRAIN-20-E15), RECORD-10-E10 and RECORD-20-E10: "A PF10 change is held back when …". The same limit is in G-FLOW-10-E25, E37 (check 6) and E47, and in GTWPE-D3's *Canon sets the timing*.
  - Against these, *SECTION*'s *Current operation* says: "A change that belongs to an epic or a CRD the run's files do not show closed waits for that closure, and the run lists it."
- **Evidence:**
  - DR-1 states its purpose: "A source other than PF10 that carried a change would have reached no document, silently." It widened the account and the routing (TRIAGE-10-E04, E05, E09, E14; G-FLOW-10-E05, E40 to E44, E50) but left every hold-back text limited to PF10. The closure the triage file records for a change from another source is read by nothing.
  - Canon's timing is not limited to PF10:
    - Change Process Guide, *Post-QA documentation drainage ordering (normative)*: "Drainage into canon, checklist rows, guides, or other document homes occurs only after all QA tasks for the epic are complete".
    - HDE Governance §9.1.1, *Historical drainage*: "a Specification or Plan alone does not supersede canon".
    - HDE CRD Records §2: a canon-changing CRD's results "are recorded in PF10-HDE-Build-Notes and drained to permanent canon through the owning process".
    - E41 gives the general reason itself.
  - This path is a designed use. TW-RECORD-20 takes a CRD's "actual specification-approval evidence", not its closure (RECORD-20-E10 and E11; G-FLOW-10-E15 sets no closure condition for a CRD record). HDE CRD Records §3.2 enters the record at registration. So a run given the Specification of a CRD still in flight goes like this:
    - The triage pass names the documents the CRD's changes bear on.
    - B1 step 6 routes them, because they are not PF10 changes and so are not held back.
    - The drains draft them, and S-HOLD does not apply.
    - TW-APPLY-10 applies the drafts.
  - An Epic Specification given without its closure decision fares the same way: its PF20 record waits, but its other changes are drafted.
  - **Refutation tried, and it fails.** No new text, and no kept text the repository shows, holds back a change that is not from PF10.
- **Path:** normal, for a run whose files include a specification or other file carrying a change of an epic or CRD that those files do not show closed.
- **Likelihood:** low to medium.
- **Consequence:** silent. A review-ready pull request carries canon drafts of an unclosed change before its QA and closure, its account shows them drained, and the selection page tells Nathan such changes wait.
- **Smallest correction:** hold back every change, not only a PF10 change.
  - In G-FLOW-10-E41, write "each change, from PF10 or another source, that belongs to …".
  - In S-HOLD, RECORD-10-E10 and RECORD-20-E10, write "A change is held back when …".
  - Change E25, E37, E47, GTWPE-D3's bullet and A1-NEW to match.
  - Keep a CRD Specification's own PF30 record outside the hold-back, as TW-RECORD-20 already treats it.
- **In text the last repair added:** yes, DR-1.

**R-2. R3, a silent breach of the accounting Nathan approved (S-4 and S-6, as GTWPE-D4 records them); also R4.**
- **Text:**
  - TRIAGE-10-E14: "and either the eligible documents it bears on, by canon file name without its version, or the reason it cannot drain in this run: no eligible home, such as PF10 itself; or PF20 or the PF30 family with no specification among the files." F11 and *What the plan settles* say the same.
  - TRIAGE-10-E11: "PF20 and the PF30 family are eligible only when a specification is among the files given."
  - G-FLOW-10-E40 (B1 step 5) records "the account its triage file gives each change …: the documents it bears on, or why it cannot drain in this run". It stops a triage file that "names an ineligible document".
  - Against these, G-FLOW-10-E16 says: "Without a governing specification, PF20 and the PF30 family are not routed, and each change that bears on them is accounted for as waiting for one."
- **Evidence:**
  - §A ITEM-03, approved as S-4, accounts each addendum "for each document the addendum bears on; or why it cannot drain in this run (…; a PF20 or PF30 part with no specification in the run; …)". GTWPE-D4 adds: "each PF10 change that bears on them is accounted for as waiting for one".
  - HDE Build Notes 2.14 says "PF27 and PF30 adopt the same terms on their next revision". It is the addendum behind E-052. In a run with no specification:
    - The triage pass names PF27 for 2.14.
    - It cannot name PF30: PF30 is ineligible there, and naming it stops the run at B1 step 5.
    - The either/or form keeps a reason only for a change with no eligible document, so PF30's reason has nowhere to go.
    - `RUN.md` and the pull request then show 2.14 drained into PF27, and nothing more.
  - E16 alone asks for the waiting part, and the Flow Manager's account is the triage file's.
  - HDE Build Notes, *Precedence, versioning, and scope* §7: "Drained guidance is removed when PF10 is formally revised."
- **Path:** normal, for every run without a specification while PF10 holds an addendum that bears on a general document and on PF20 or PF30.
- **Likelihood:** medium; certain for 2.14 in such a run.
- **Consequence:** silent. The account shows the addendum drained; the part waiting for a specification appears nowhere, and a later PF10 revision can retire it.
- **Smallest correction:**
  - In TRIAGE-10-E14, F11 and *What the plan settles*, write: "the eligible documents it bears on …, and, for any part that cannot drain in this run, the reason".
  - In TRIAGE-10-E11 and B1 step 5, allow PF20 or the PF30 family to be named without a specification, with that reason only.
  - In G-FLOW-10-E40, write "and" for "or".
- **In text the last repair added:** partly. DR-1 reworded TRIAGE-10-E14, but the either/or form also stands in *What the plan settles*, which is older than that repair.

**R-3. R3, a silent breach of ruling 1 as S-1 and GTWPE-D2 apply it; also R2.**
- **Text:** none of TW-APPLY-10's 18 edits carries the refusal "an input given as anything but a file is not taken". TRIAGE-10-E06, DRAIN-10-E08, DRAIN-20-E08, RECORD-10-E10 and RECORD-20-E10 each add it. Against this:
  - GTWPE-D2: "A run, a pass or a TW prompt invoked directly that is given anything beyond the prompt to run and its files stops at intake and names what it was given."
  - *SECTION*: "Every TW prompt takes its inputs as files only".
  - HUB-NEW: "every TW prompt invoked directly … take files only".
  - P5's second row: "All six | Inputs are files: 'an input given as anything but a file is not taken'".
- **Evidence:**
  - By script over `edits.json`, the phrase is in the new texts of five members and absent from TW-APPLY-10's.
  - C2's and C3's texts for TW-APPLY-10 carry no such rule. "They come as attached files or repository paths, never from Google Drive or ChatGPT Library" says where its files come from, not what it refuses.
  - TW-APPLY-10 loses its non-file inputs one at a time (E11 to E13, E16 to E18), but nothing refuses non-file input in general.
- **Path:** a failure upstream. A direct or relayed invocation carries words beyond files, which is the E-045 failure. Within a run, the Flow Manager sends files only (G-FLOW-10-E26).
- **Likelihood:** low.
- **Consequence:** silent. TW-APPLY-10 takes the extra words. The selection page, the Hub and the decision record state a rule its body does not carry.
- **Smallest correction:** add one TW-APPLY-10 edit in *Intake and preparation-state verification*. After "They come as attached files or repository paths, never from Google Drive or ChatGPT Library.", add: "An input given as anything but a file is not taken: stop and name it." Give it its own anchor check and readback.
- **In text the last repair added:** no.

**R-4. R2, a silent wrong statement in a governed document.**
- **Text:** in `gtwpe.handoffs.md` 1.1, the opening paragraph is unchanged from 1.0: "Rows H11 to H13, GTWPE-MGMT-10's, are carried unchanged." But its H11 now reads "A defect in a run, carried by Nathan as the files that record it | the files, attached or by repository path, …".
- **Evidence:**
  - A `diff` against `main` shows H11 changed and that sentence untouched.
  - C4's review found 1.0's H11 to H13 identical to design v1.2 §6, whose H11 asks for "the failing stage, evidence, the run ID".
  - X1.4's `D26-E` search does not reach this sentence.
- **Path:** normal; X1.4 lands it.
- **Likelihood:** certain for the wrong text; its effect is low. A reader sent to design §6 for H11 would find a request form that is not files.
- **Consequence:** a false statement in a binding file that no check sees.
- **Smallest correction:** write "Rows H11 to H13, GTWPE-MGMT-10's, are carried; H11 takes files only from version 1.1 (GTWPE-D2)." Then fix «HT» again.
- **In text the last repair added:** no.

LISTED

Each line ends: [path; likelihood; consequence; repair text = DR-1 to DR-5?]
- **L1 (A1).** E36 says "each change the triage file routed to it is already represented there", and F8 says "each change routed to the document". Read with the triage file as the router, a change that B1 step 6 holds back is counted as represented when its document returns `no redlines` or `no changes`. A run whose other changes are all represented then meets E43's `RUN_NO_CHANGE`. K-7 shows the intended reading leaves held-back changes out, and B1 step 6 still lists them. Fix: "each change not held back that the triage file names for it". [normal, with a held-back change; low; wrong result code, though the wait stays visible; yes, E36]
- **L2 (A2, C6).** *What the plan settles* still reads "for each PF10 change in source order" and keeps §A's form of the endings ("every PF10 change … or the run has no PF10 source and changes no document"). E42, E43, E50, F11 and GTWPE-D3 use every change and "the account holds none". So for a run with no PF10 source whose account holds a change that cannot drain, the settlement gives `RUN_NO_CHANGE` and the edits give `RUN_STOPPED`. C6's "exactly as *What the plan settles* says" therefore fails. [edge; low; record text only, and the edits are the safer form; left by DR-1]
- **L3 (A5, C4).** GTWPE-D2 to GTWPE-D4 say Nathan accepted their consequences "when he approved the analysis". Some of those consequences were added by §P, not §A:
  - GTWPE-D3: DR-1's every-change account and its `RUN_NO_CHANGE` form, and the stop for B's L12.
  - GTWPE-D3 and GTWPE-D4: P-2's `no changes`.
  - GTWPE-D2: P-3's "a path on a branch", and the handoff-content rule set aside.

  So C4's "his words and §A's approved readings, and nothing more" does not hold. After plan approval, only the occasion named is wrong. Fix: "when he approved the analysis and the plan". [normal; certain; low, provenance; partly DR-1]
- **L4 (A2).** DR-1 credits "any other file or collection of source material that contains the change context" to Nathan's answer 2; the words are answer 5's. [—; certain; none; yes]
- **L5 (A2, A3).** DR-1's "every change another source carries" has no unit for a specification's changes, while B1 step 5 stops a triage file that "leaves a change unaccounted for". The Flow Manager and the triage pass may count the HDE-EPIC040 Specification's changes differently. [normal, the first live run; medium; loud S4; yes]
- **L6 (A4).** F2 and the kept first invocation items pass the prompt's "selected version, page and edit time" and "that it runs as a pass inside the session Nathan started". GTWPE-D2's list of what an invocation gives leaves these out, and its exceptions do not name them. A pass that reads S-INTAKE's refusal strictly may stop. [normal; low; loud; no]
- **L7 (A4).** TW-APPLY-10 keeps C3's "Other header, title or invocation-tag changes need separately explicit authorization and exact validated edits". It is not brought to "given as a file", as the drains' S-HEADER-AUTH is. Whether the exception "TW-APPLY-10's header contract" keeps it at (g)(10) is a judgement call. [normal; low; a stop at readback, or a non-file authorization kept; no]
- **L8 (A4; cannot be checked here).** C4's ITEM-04 gives the sentence before E06's anchor as "every other instruction in it is read within those limits". If the body carries it, E06's new rule follows a clause that still accepts other instructions, and the `D26-E` table has no `instruction` term. [normal; low; ambiguous intake; no]
- **L9 (A3; cannot be checked here; R3 if the body says it).** C4's §A ITEM-01 and its risk 4 make a B5 consistency fix "a drain and an apply again". No edit touches B5 or *Redo from canon*, and §A did not measure them for ruling 3. The `D26-E` terms would not catch "the document's drain … then TW-APPLY-10". If the body says this, a B5 finding on the PF20 or PF30 draft sends it through the redliner, against E-053 and GTWPE-D4. The session can read the live body. [redo; low to medium; silent; no]
- **L10 (A4; cannot be checked here).** §A's *Scope* counts *B5* and *Redo from canon* among ruling 1's sections, but no edit reaches them and §P names no exception for them. B5's reviewer subagent is not held to a committed brief's path, as G-MGMT-10-E15 now holds GTWPE-MGMT-10's reviewers. [normal; low; possible context in a handoff; no]
- **L11 (A3).** Take an Epic Specification without its closure decision, where the only change not held back that names PF20 is already represented. RECORD-10-E20 then names the missing evidence "in the conversation" instead of returning `no changes`, and the run stops (S4), although B1 step 6 means the record to wait. P5's "so the pass has other changes to make" does not follow. [K-10's path; low to medium; loud; no]
- **L12 (A3).** RECORD-20-E18 ("no change to any PF30 volume") and E13 ("the volume the changes bear on") cut against the one volume each pass is assigned. With a second volume, a pass may write a volume it was not given. [normal; low, one volume today; loud at the after-pass checks; no]
- **L13 (A3, A4).** GTWPE-FLOW-10 speaks of a "governing specification" (E14 to E16, E41), while S-6, GTWPE-D4 and TRIAGE-10-E11 speak of a specification among the files. With files only, nothing marks which specification governs. If the Flow Manager does not treat the run's specification as governing, B1 step 5 stops the run on PF20 or PF30. [normal; low; loud; no]
- **L14 (A4).** HUB-NEW says GTWPE-MGMT-10 takes "no … authorization or other context", leaving out GTWPE-D2's exceptions: the mode, the Modification ID and Nathan's approvals (H13). G-MGMT-10-E03's "its subject, given only as files" likewise drops PLAN's and EXECUTE's Modification ID. [normal; low; loud at worst; no]
- **L15 (A4).** G-MGMT-10-E06 lists a run's `RUN.md` as a request file, then makes "Nathan's words in those files" the request. A `RUN.md` holds none, so H11 carried as a `RUN.md` alone gives `ANALYZE` no request. [normal; low to medium; loud; no]
- **L16 (A4).** The PE Metaprompt's handoff-content rule is set aside on ruling 1 and GTWPE-D2, not within *Relation to the PE Metaprompt*. Its workarounds, as the repository shows them, do not name this rule, so the set-aside holds only while the decision record is read first. [authoring; low; drift at a later revision; no]
- **L17 (A9).** The triage file and decision files travel among "The sources" (E29), and the drains build a change ledger "for every incoming source". TW-APPLY-10 sets its Last Update Gate from "the sources that justified the update". Nothing says the triage file is not a gate source. [normal; low; a uniform gate error that B4 cannot see; DR-1 widened E29]
- **L18 (A9).** GTWPE-FLOW-10 grows by a net 2,453 characters to about 30,000, near the harness's ~30 KB save threshold. X1.3 (g) reads the page "whole, into this session's context", and the plan provides for saves only on control pages. [normal; medium; a `D22` save to read and disclose; no]
- **L19 (A3).** On `RESUME`, an attached decision file has no commit step: B1 step 4 commits attachments only at intake, while passes read by repository path. [resume; low; loud; no]
- **L20 (A3).** A run that stops because a change cannot drain still returns a resume line, though no decision file can make that change drain. [stop; low; one futile resume; no]
- **L21 (A6).** `closure.state_sharers` leaves out TW-RECORD-10 and TW-RECORD-20, which now share `no changes` (this adds to B's L3). [—; certain; none, since every member changes; no]
- **L22 (A8).** `SELECT` and `EXCLUDED` test only whether a form is new to an edit, so new text may repeat a form its old text holds; TRIAGE-10-E03 and E14 keep "model advice". `OVERLAP` cannot see anchors that overlap in the body. I found no edit that defeats a check. [—; low; a blind spot; no]
- **L23 (A10).** K-24 and *Harness files* leave out one fact. The PE Metaprompt's general rules, which are §P's authoring control, were read only before the compaction (lines 36 to 128, 173 to 207 and 291 to 353 of the first save). After it, only the title, edit time and line 194 were read, yet DR-1 to DR-5 were authored after it. So "relies only on the checks made after the fetches" overstates. Otherwise the disclosure is complete. [—; certain; low; no]
- **L24 (A9).** The readback's `D26-E` table drops several of §A's ruling 1 terms: `the change`, `supporting material`, `decision`, `direction`, `statement`, `run name`, `RESUME`, `invocation` and `handoff`. The broad match after the edits is narrower than the measurement it verifies. [normal; low; a surviving passage would be silent; no]
- **L25 (cosmetic).** TW-TRIAGE-10 keeps the title "Identify PF10 Drain Targets" although it now accounts for every change (compare §A risk 7). *The edits, by rule* defines no R5. Its table labels RECORD-10 and RECORD-20 E09 to E21 "(R4, R2)", where `edits.json` says R4. [—; certain; none; partly]

WHAT HOLDS, CLAIM BY CLAIM
- **C1.** Holds. No item, member, target or Notion write is added. ITEM-07, S-1 to S-8, DC-L1 and Q-1 (a) are each applied; DC-L1's exact `no redlines` is untouched. DR-1 widens ITEM-03's account (L2, L3).
- **C2.** Fails at R-1 to R-3, and holds otherwise. `EXCLUDED` and `PROOF` pass. No new text pins a PF version or uses "CRD Plan" or "Epic Plan".
- **C3.** Every return is consumed, and every input but R-3's is met. F1 to F11 and H11 match both sides, apart from F11's either/or (R-2) and the opening sentence (R-4).
- **C4.** All 11 block quotations are verbatim, checked by script against PE40-INIT, the ledger and `analyze_approved_by`; the inline quotations are found too. The consequences go beyond §A as L3 describes.
- **C5.** P-1 to P-5 are correct, and none of them adds an item, member, target or write.
- **C6.** Fails at R-1 and L2.
- **C7.** Holds. Every check can fail, X1.0 and the pre-reads guard each write, the failure path is `D26-B`, and no rollback needs a copy of a body.
- **C8.** Holds on the committed text. SEL-1 goes before SEL-2 and CAT-FLOW before CAT-MGMT, and no old text occurs in an earlier new text of its call. Every `--has` and `--row` argument in X4.4 and X4.6 is present in A1-NEW and HUB-NEW, in the form `ctl_check.py post` matches.
- **C9.** K-1 to K-25 are rightly listed, but R-1 to R-4 are absent from them. The Product Owner actions and the scope are complete.

CHECKS I RAN, ALL READ-ONLY
- **The brief.** 13,242 bytes, sha256 `154caacf8c232f85675bafd4ea17545fafdf90fd3a6c115ad66258289bdc0d3f`. `f77a77b` adds only the two briefs to `1f73053`.
- **The record.** At `1f73053` it is 194,431 bytes and 1,758 lines, sha256 `fc9cec869dddc6972430791fee7a3842161cf60257b3b9a5f605cc8473a6fb08`.
- **The evidence fingerprints.** Each matches «H», «HD» and «HT», and `ctl_check.py` matches its stated sha256.
- **`edits_check.py`.** It passes with exit 0: 8 members, 200 edits and 8 proof-log items. Each of the 11 injected faults exits 1 under its own code.
- **The two `gtwpe/` files.** Each was diffed against `main` at `128836a`.
- **Anchors, against the C2, C3 and C4 edit files.** Where a TW anchor overlaps an earlier new text, it holds that text whole. Eight anchors in GTWPE-FLOW-10 (E29, E37, E38, E40, E42, E43, E47 and E50) contain C4's repaired clauses. The other anchors cannot be checked in the repository.

METHOD AND DISCLOSURE
- **Commands.**
  - `git`: `show`, `diff`, `log`, `ls-tree`, `grep`, `cat-file`, `rev-parse` and `status --short`.
  - Shell: `grep`, `sed`, `wc`, `sha256sum` and `ls`.
  - `python3 -I -c`, printing only.
  - `edits_check.py`, run under `PYTHONDONTWRITEBYTECODE=1`.
- **No other actions.** I made no fetch, no Notion, Drive, GitHub, session or agent action, and no file write. The tree is clean, and `.git/index` has not changed since 13:30:43Z.
- **Side effects that were not mine.** The repository's PostToolUse hook updated `.git/canon_relied_on_hook.json`. The harness saved one oversized output of mine, a grep of `ERRORS.md` (49.4 KB of repository text, no prompt body), as `tool-results/b3hsq0bs0.txt`. I did not read it.
- **`D22`.** I read no prompt body.
- **Not run:** the two record checks, which the brief does not list.
- **Not exercised:** Notion and its rendering.

## Canon relied on
- **`AGENTS.md`:**
  - the canon-first rule;
  - PF canon is read-only;
  - the truncation guardrail;
  - evidence attribution;
  - the code-review scope line, which does not apply to this D26-A review.
- **PF canon, from `docs/pfcanon/` on `origin/main` at `128836a`** (the local ref, not fetched):
  - Change Process Guide: *Post-QA documentation drainage ordering (normative)*, in full; its sentence "HDE Phased Epics is historical-only".
  - HDE Governance: §2.0.19, *Post-closure maintenance ordering*; §9.1.1, its post-closure drainage row and *Historical drainage*; §9.1.5, its drainage lines; §9.1.6, in full.
  - HDE Build Notes: *Precedence, versioning, and scope*, §1 and §7 to §9; 2.14, its two rules; the headings of 2.1 to 2.38.
  - HDE CRD Records: §1, §2 and §3.2.
  - Plan Templates: §2, *Historical-only posture (normative)*.
  - The search: `git grep` for `drain`, `addend` and the historical-only and drainage-ordering rules.
- **Governing documents in `docs/prompt_ecosystem_management/`:**
  - `gcfpe.decision-record.md`: D20, D21, D22 and D26 in full; D23 to D25 by heading only.
  - `ecosystem-change-management.md`, whole.
  - `modification-template.md`, rules 1 to 8.
  - `reviewer-prompt-template.md`, the second template.
  - `notion-write-boundary.md`, whole.
  - `gtwpe/gtwpe.decision-record.md` and `gtwpe/gtwpe.handoffs.md`, whole.
- **In flight:**
  - the record at `1f73053`, its evidence and this brief;
  - PE40-INIT, whole;
  - the ledger, E-044 to E-048 and E-051 to E-054;
  - the architecture record, whole;
  - `CHECKPOINT.md` §8, the three rulings of 2026-09-28;
  - C4's record, §A and §P where cited, with `draft-repairs.json` and its three review records;
  - the C2, C3, C1 and first-repair edit files;
  - the HDE-EPIC040 closure decision v1.2, its front matter.

IN FLIGHT: R-1 to R-4 go to repair, then to the second full review or the check of the repair's diff (D26-A rule 2). L1 to L25 stay listed unless Nathan opts in to repairing any of them.
