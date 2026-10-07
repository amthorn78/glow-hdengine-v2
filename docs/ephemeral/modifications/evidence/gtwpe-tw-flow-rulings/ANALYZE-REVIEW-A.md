1

GTWPE-TW-FLOW-RULINGS-ANALYZE-A: full ANALYZE review 1 of at most 2 (D26-A) of MODIFICATION-20261007-gtwpe-tw-flow-rulings, §A at cc6b92331ce14a0d5244290a6f0b2a1f84484e25. I found one required defect. ITEM-05 and S-6 send every Epic Specification's history to PF20, and the record says this "conflicts with no canon". Canon admits only closed epics to PF20, and only once, at close. §A never states that limit, and the first live run as named does not meet it.

What holds:
- The request is verbatim, and its three files match the Intake's blobs and byte counts.
- The closure lists in the front matter equal what the handoff table gives for the eight changed members.
- S-1's reading, that a run's resume, a stop decision and a rollover decision reach it as files, follows from "the only inputs should be the filenames".
- ITEM-06 holds: PF09 already takes TW-DRAIN-20 and then TW-APPLY-10.
- Updating an existing PF30 record in place matches HDE CRD Records §4.2 and §6.
- Every body quotation I could test against the repository is found as quoted.

**Checks I ran, all read-only:**
- **The brief.** 12,962 bytes, sha256 `15fb79b23ac856d2f4978b5fe3ac792a0b20d33bf7bfefcf73beda0334dfa488`. Commit 024425c adds only the two briefs to cc6b923.
- **The record at cc6b923.** 67,491 bytes and 753 lines, blob `4b72824`, sha256 `068dcacb…6e3623`. The working-tree copy is byte-identical, and the tree is clean.
- **The request files at 128836a.** Their blobs and byte counts equal the Intake table's.
- **The drift range.** `git log b65e918..128836a` lists five commits (#584, #586 to #589) that change 22 files, all under `docs/ephemeral/`.
- **The record checks.** `gtwpe_record_check.py` and `modification_validate.py`, run with PYTHONDONTWRITEBYTECODE=1, each exit 0 on the record at ANALYZING. Each also exits 0 at ANALYZED, fed through a pipe (`<(sed …)`), so no file was written.
- **The tables.** 15 tables, each with one column count in every row.
- **Counts in canon.** `git grep -c HDE-EPIC040` finds nothing in PF20. "CRD Plan" occurs 15 times on 14 lines of PF30.1.
- **Body quotations.** Checked against the repository's copies:
  - C3's `edits.json`: "the inserted entry and its control fields", "also records", the rollover sentence and "such as an HDE CRD Records material-change row's decision date".
  - C2's `edits-2.json`: TW-TRIAGE-10's "directly or through a session he started that runs this prompt as a pass".
  - C4's §P, P5 table, read from the live bodies at the time: the drains' optional selections and READY carry-over, TW-APPLY-10's no-change report, the output-identity clause, TW-RECORD-20's rollover clause and TW-RECORD-10's completed-posture rule.
  - C4's §P, *The new page*: GTWPE-FLOW-10 has twenty headings, which is consistent with 20 sections.
- **What I could not check.** I read no Notion body, as GTWPE-MGMT-10 100526.2 requires, so the section counts in *Scope* rest on the authoring session's readings.
- **Nothing written.** No file, no git state change, and no Notion, GitHub or session action.

REQUIRED

R-1: R3, a silent breach of a Product Owner ruling. The ruling is canon's archive-on-close rule for PF20, with the canon-first rule's bar on claiming conformance to canon that was not read. It also has an R2 consequence in the GTWPE decision record. Normal path: any run with an Epic Specification whose epic the run's files do not show closed. Likelihood: certain for the first live run as PE40-INIT names it, and low to moderate for in-flight epics generally.
- **Text, at cc6b923:**
  - ITEM-05, *The authorization gate*: "Nathan's rule replaces it: with a specification in the run's inputs, the run updates PF20 for an Epic Specification (TW-RECORD-10) or PF30 for a CRD Specification (TW-RECORD-20); without one, neither." S-6 settles this.
  - ITEM-05, *Canon*: "Read for the canon-first rule only: it conflicts with no canon, since the run Nathan starts with a specification is such an action."
  - ITEM-05, *The first live run*: "an Epic Specification, so PF20 is updated through TW-RECORD-10, and HDE Phased Epics has no HDE-EPIC040 record yet […], so the record is new".
  - ITEM-01: GTWPE-D4 records the rule "with what follows from each, as GTWPE-D1 is written". GTWPE-D1's "what follows" includes a canon statement.
  - *Canon and rulings relied on* cites no Change Process Guide section except the post-QA ordering, and no Plan Templates section.
- **Evidence:**
  - **Canon admits only closed epics to PF20, once, at close.**
    - Change Process Guide §1.1.2: "The final historical record is archived in PF20 only at epic close."
    - Change Process Guide §3.5.1: "HDE Phased Epics is historical-only: the epic record is added there once, at epic close, as the final archived entry. In-flight epics MUST NOT be recorded there."
    - Change Process Guide §6.3: "After an authorized close, PF20-Reference-HDE-Phased Epics MAY record the final historical epic disposition."
    - Plan Templates §2, *Historical-only posture (normative)*: "PF20 HDE-Phased Epics MUST contain only completed epic records"; "In-flight epics MUST NOT be added"; "Archive-on-close: the epic record is added to HDE-Phased Epics only once, at epic close".
    - No addendum in HDE Build Notes v13.5 overrides these. Its only lines on PF20 or Phased Epics are 2.1's board routing and 2.30's note on historical records.
  - **Canon governs here.** Under `AGENTS.md`, canon governs an in-flight ruling unless PF10 supersedes it. HDE Build Notes 2.29 says "An artifact neither states nor implies conformance to canon that was not read". So "If there is a spec involved, those docs are updated" holds for PF20 only once the epic is closed. That is a timing rule, like the post-QA hold-back, and §A's own "Canon bears on timing, not on whether" fits it. §A does not apply it.
  - **The GTWPE's own approved design recorded the rule.** Design v1.2 says "PF20 takes completed Epics only and adds each 'only once, at epic close' (PF27 §2; PF06 §1.1.2, §3.5.1, §6.3). Specification approval alone is insufficient". Its §10.4 says "its history goes to PF20, at close".
  - **Only TW-RECORD-10's own rule enforces it now.** That rule is "establish that actual completed/historical posture from supplied evidence", otherwise "ask" (C4 §P, P5, quoting the live body). It is backed by F7's "for an Epic, the evidence of its completed or historical posture". §A never mentions either. ITEM-05's logic, that a specification in the run means PF20 is updated, reads that rule as one more gate to remove.
  - **The first live run cannot establish closure.**
    - CL-E-10 v1.2 closed HDE-EPIC040 (CLOSE, exceptional closure, 2026-09-29T19:53:33Z).
    - That decision is `docs/ephemeral/HDE-EPIC040-CL-E-10-closure-decision-v1.2.md`, which is not one of the run's two files.
    - HDE Build Notes 2.37 says the QA PASS "is not closure".
  - **Refutation tried.** If TW-RECORD-10's posture rule survives PLAN, the run-time outcome is a loud stop. That limits the finding but does not remove it: §A neither keeps the rule nor names the canon, and the decision-record entry would be wrong either way.
- **Consequence.**
  - **In the decision record.** GTWPE-D4 enters the BINDING record with an unconditional PF20 rule and a claim that it conflicts with no canon, and it binds C5 and C6.
  - **If PLAN keeps TW-RECORD-10's posture rule.** The PF20 pass stops (S4) whenever closure evidence is not among the run's files. That includes the first live run, which §A predicts will update PF20.
  - **If PLAN drops it as a gate under S-6.** A run drafts an in-flight epic's PF20 record against canon and presents it as review-ready, with every check passing.
- **Smallest correction.** Canon settles this, so nothing goes to Nathan:
  - In ITEM-05 and S-6, say that PF20 takes an Epic Specification's record only when the run's files show the epic closed, citing the sections above. Otherwise the PF20 part is accounted for as waiting for close, a reason in ITEM-03 beside the post-QA hold-back.
  - Keep TW-RECORD-10's completed-posture requirement, with its evidence given as a file.
  - Replace "it conflicts with no canon" with that limit. Add Change Process Guide §1.1.2, §3.5.1 and §6.3 and Plan Templates §2 to *Canon and rulings relied on*.
  - In *The first live run*, say that the inputs must include HDE-EPIC040's closure decision; otherwise its PF20 part waits.
- **In text the last repair added:** no. The dry run's corrections, D5 to D9, did not touch ITEM-05, S-6 or the canon table.

LISTED (each line: attack item; path; likelihood; consequence; whether it is in text the last repair added)
- **L1 (A2, S-6).** The Epic-to-PF20 and CRD-to-PF30 split is not in ruling 3's words. Nathan said "PF20 and PF30 must be updated as part of this" when told PF20 was left out of the first run, an Epic run, and "those docs" names both. The split is defensible on architecture §9 ("must not update PF20 or PF30 from PF10 alone") and design v1.2 §10.4, but §A cites neither and presents the split as his rule. Normal; low to moderate; the first live run then leaves PF30, including 2.14's PF30 terms, untouched without Nathan being shown the narrowing; not in repair text.
- **L2 (A2, S-7, risk 6).** "DON't need the redliner" does not supersede "they only get one SECTION": the two agree, since his reason for no redliner was the single section. S-7 widens TW-RECORD-20 to 2.14's terms across a volume (15 hits on 14 lines) and to existing-record updates in one direct pass. That resolves a conflict among his words and belongs in *Open questions*, which says "None". Normal; moderate; multi-location canon edits lose the redline-and-report "determinism and drift control" he named; not in repair text.
- **L3 (A1, S-8, readiness).** ITEM-07 says "Nathan's approval settles it" and differs from PE40's check. By the template's rule that is an open question, so readiness would be NEEDS_RULING and the cost one higher, yet *Open questions* says None. §A also never says that Nathan's own sentence request to GTWPE-MGMT-10, or an H11 defect report, must first be put in a file. Normal; certain; Nathan approves a change to his own intake without it being stated; not in repair text.
- **L4 (A1, ITEM-07).** Files only does not close E-048's route. A facilitator's interpretations handed over as a file are still "the files that record it". The Intake's own rule, that the request is Nathan's words and other text in the files is a claim, is not carried into the entry contract. Failure; moderate; E-048 can recur silently; not in repair text.
- **L5 (A3, S-4).** "already represented, by the triage pass's reading" lets one pass's judgment account for an addendum, without the drains' "exact equivalence location". A PF10 run can still end RUN_NO_CHANGE with no drain run, which is E-044's outcome, against "if there are addenda in PF10, that means they need to be drained, otherwise they would not be in there". Normal; low to moderate; addenda left undrained, though recorded; not in repair text.
- **L6 (A3, S-4).** The accounting reasons omit supersession (HDE Build Notes *Precedence* §5 and §7, which the canon table cites). A wholly superseded addendum is not drained, not represented, not held back, not waiting for a specification and not homeless. Normal; low; a stop or a wrong account; not in repair text.
- **L7 (A5, ITEM-02, the new triage rows).** TW-TRIAGE-10 writes nothing (the GTWPE-D1 table: "its triage is a return"), so its per-addendum accounting reaches GTWPE-FLOW-10 inline. That handoff passes more than files, which ITEM-02's statement forbids and no listed exception covers. Normal; certain; PLAN must add a file or an exception, which changes §A; partly in repair text (D9 amended the exceptions).
- **L8 (A5/A7, C3).** ITEM-02's table is not complete against *Scope*:
  - It omits GTWPE-FLOW-10's B5 and *Redo from canon*, and TW-APPLY-10's *Intake and preparation-state verification*, all of which ruling 1 reaches.
  - It omits F2's "or `none`", though it lists F1's.
  - No exception covers the branch and pull request that a TW prompt's intake requires ("An invocation that names no such path or branch is a missing input") in a direct invocation, which S-5 and risk 2 keep.
  - Path: normal for direct invocations; high; a loud stop at intake, or PLAN rewriting §A; partly in repair text (D9).
- **L9 (A5, the handoff table).** *Scope* reaches F3, F5, F6 and F9 lightly and says *Common rules* gain the rule. *What changes* and *Per part*'s tier list name F6 and F9 only, and *What changes* omits *Common rules*. Normal; moderate; the BINDING table and the bodies can disagree after EXECUTE; partly in repair text (D9 added F9 to the tier list).
- **L10 (A5).** *Scope* gives TW-TRIAGE-10 two ruling-3 sections, but *What changes* and *Member dispositions* give it ITEM-02 to ITEM-04, not ITEM-05. Normal; low; item dispositions misattributed at EXECUTE; not in repair text.
- **L11 (A5, D26-E).** The catalog's *Approved design* entry is on the route and still names C1's §A and design v1.2 as governing "where neither … supersedes". Both carry rules these rulings reverse:
  - C1 §A R11: "PF27 changes only when a specification exists (Nathan, 2026-09-25)".
  - C1 §A A.2 and A.5: TW-TRIAGE-10 as the Change Manager.
  - Design v1.2: "PF27 is never a target in a run without (b)".
  - X4 changes only the rows and the commit, and the D26-E search did not cover this entry. Failure (C5's ANALYZE reads the catalog); low to moderate; superseded rules read as current; partly in repair text (D8).
- **L12 (A3/A6).** Two reversals of C1's approved §A are missing from the S table that his approval is said to accept. One is the PF27 gate (R11, attributed to him; E-052 says "the fix's analysis states this for Nathan's approval"). The other is C5's identity: A.2 and A.5 made TW-TRIAGE-10 the Change Manager, and S-5 makes it the run's pass "instead", while saying "Recorded, not decided here". Normal; moderate; approval given without seeing them as reversals; not in repair text.
- **L13 (A6, ITEM-08).** ITEM-08 says "what is found wrong is fixed", but known defects in GTWPE-MGMT-10, which this change re-versions, are left as optional candidates: E-033's "until G5" in six places and C3's F-1, "eight members" where TW-ALPHA has six. Normal; certain; another re-version of the same page, against "Fix it"; not in repair text.
- **L14 (A4, risk 14).** HDE Build Notes 2.14 says "Do not pin a PF file version in a prompt, artifact, plan, ledger, report, or addendum", with no one-off exception. HDE Governance §9.1.6 applies the versionless rule to "temporary repair/review/handoff prompts" too. Risk 14 carves out the execution prompt and says both rules ask it only of durable bodies, so the conflict with ruling 1's filenames goes unnamed; a versionless name under `docs/pfcanon/`, resolved on `main`, would meet both. Normal; moderate; execution prompts pin versions against 2.14; not in repair text.
- **L15 (A8).** The predicted cost of 9 counts only the planned rounds. The calibration it quotes ran 1.6 to 1.9 times prediction (C2 +6, C3 +4, C4 +6, from rulings, diff checks and extra merges), which puts a calibrated figure at about 14 to 17, before L2 or L3 add an open ruling. Normal; high; cost under-reported to Nathan; not in repair text.
- **L16 (A6, the Intake).** C1's "maps every one of his words" overstates. The table omits E-053's "PF20 and PF30 had their own special prompts. I guess they were just lost or ignored.", ruling 2's first sentence and E-046's "this is meaningless distinction", each used elsewhere in §A. §A also never says whether the rulings bear on E-007 (PE defect D5, the PE's handoff rule that PLAN authors under), though the Intake promises that for every OPEN row. Low; not in repair text.
- **L17 (A6, ITEM-01).** "ruling 1, both sentences" and "ruling 2's two sentences" count quotations, not sentences. Read literally, GTWPE-D3 could omit ruling 2's "part of this run is to have a prompt evaluate the drain targets", leaving the ruling behind ITEM-04 unrecorded. Normal; low; not in repair text.
- **L18 (A1).** The H13 exception admits any text in an approval. That is the route E-039 records for a facilitator's commitments reaching GTWPE-MGMT-10, H13's own fields are only the Modification ID and the mode, and ruling 1's "at every phase" may reach it. Low; not in repair text.
- **L19 (A7, scope).** Ruling 2's reach for GTWPE-FLOW-10 omits B6 and the pull-request bullet. Per C4 §A ITEM-01, *Completion*, and §E's `merg` hits ("in the pull-request bullet and again in B6 step 5"), these carry "what was not drained and why", which S-4's per-addendum accounting changes. Normal; low, since PLAN's counts may catch it; not in repair text.
- **L20 (A2/A7, S-3).** With no selected boundary, a PF20 pass reads PF20 (952,515 bytes) and PF10 v13.5 (489,946 bytes) whole: about 480,000 tokens at 3.0 bytes a token, before the specification and PF03. §A does not test S1 against this. Normal; likelihood unknown; a capacity stop with no way to narrow; not in repair text.
- **L21 (A5).** *Member dispositions* drops `glow-artifact-storage` and `glow-workspace-currency`, which C4 dispositioned as interacting interfaces, though S-1 now has Nathan place decision files. Low; not in repair text.
- **L22 (A5, ITEM-02).** ITEM-02 can be VERIFIED while the top callout on the Operations Hub still says "GTWPE-FLOW-10 100726.1 still asks for more than filenames; that fix is open" (N-1, outside the route). So "clear in the operations hub" is not met at COMPLETE unless N-1 is done with X4. Low; not in repair text.

## Canon relied on
- **PF canon**, from `docs/pfcanon/` on `main` at 128836a. The branch does not change it.
  - HDE Governance: §9.1.1, in full, including *Historical drainage* and the runtime table; §9.1.6, in full.
  - HDE Build Notes:
    - Front matter, *Precedence, versioning, and scope* §1 to §9, and *Cross-references*.
    - 2.14, 2.29, 2.30 and 2.38, in full.
    - 2.37's "It is not closure".
    - The addendum list by heading, and a search for "PF20", "Phased Epics" and "CRD-0001".
  - Change Process Guide:
    - §1.1.2 *Multi-PR epics*.
    - §3.5.1 *Requirement*.
    - §3.5.2.8, *Post-QA documentation drainage ordering (normative)*.
    - §6.3 *Close-out epic required*.
    - Every line naming PF20 or HDE Phased Epics.
  - Plan Templates: §2 *HDE-EPIC-Plan*, *Historical-only posture (normative)*, and its other PF20 lines.
  - HDE CRD Records: §0, §1, §2, §4.1, §4.2, §4.4, §5 and §6.
  - HDE Phased Epics: front matter and §0 in full, including *Drain posture*, *Build Notes posture* and *Scope note*.
  - Technical Writing Best Practices: front matter, §1, §2, §4 to §8 and §10.
- **`AGENTS.md`:** the canon-first rule; PF10's authority; PF canon read-only; the operating workflow, including the truncation guardrail; evidence attribution.
- **`docs/prompt_ecosystem_management/`:**
  - `gcfpe.decision-record.md`: D20 to D26, in full, including D23's rulings, clarification and successors.
  - `modification-template.md`, `ecosystem-change-management.md` and `prompt-body-content-policy.md`: whole.
  - `reviewer-prompt-template.md`: the second template.
  - `notion-write-boundary.md`: the policy as issued and the read-only default.
  - `gtwpe/gtwpe.decision-record.md` and `gtwpe/gtwpe.handoffs.md`: whole.
  - The header of `gtwpe/gtwpe_record_check.py`.
- **In flight:**
  - The record at cc6b923, whole.
  - The three request files, whole: `PE40-INIT-20261007.md`; `ERRORS.md`, front matter and E-001 to E-054; `GTWPE-TARGET-ARCHITECTURE-20260929.md`.
  - `CHECKPOINT.md` §8.
  - `GTWPE-IMPLEMENTATION-PLAN-v1.2.md` §1 and §16.4.
  - Design v1.2, by search, with its §10.3 and §10.4.
  - C1's front matter, §A A.1 to A.7 and catalog texts.
  - C2's to C4's front matter and cost sections.
  - C3's release-note texts.
  - C4:
    - §A: ITEM-01 to ITEM-09, *Per part*, *Member dispositions*, *Scope*, *Open questions* and *Readiness*.
    - §P: *The new page*, *The new page's checks*, *The steps*, *Dry run* (P5 and P10) and *The catalog texts*.
    - §E: X1.3.
  - The edit files `gtwpe-writing-side/edits.json`, `gtwpe-tw-repository-io/edits-2.json`, `gtwpe-tw-document-rules/edits.json` and `gtwpe-tw-model-advice/edits.json`.
  - `docs/ephemeral/HDE-EPIC040-CL-E-10-closure-decision-v1.2.md`, front matter and §0.

IN FLIGHT: R-1 goes to repair, and canon settles it, so no question goes to Nathan. Within D26-A's cap, a second full review or one check of the repair's diff follows. The analysis then goes to Nathan with L1 to L22 listed; L1, L2, L3 and L12 are his choices.
