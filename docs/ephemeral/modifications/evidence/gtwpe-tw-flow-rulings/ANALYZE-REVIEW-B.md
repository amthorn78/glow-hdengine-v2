3

GTWPE-TW-FLOW-RULINGS-ANALYZE-B: full ANALYZE review 1 of at most 2 (D26-A) of MODIFICATION-20261007-gtwpe-tw-flow-rulings, §A at `cc6b92331ce14a0d5244290a6f0b2a1f84484e25`. I found three required defects. In all three, the design departs from something Nathan ruled, and the record does not say so.
- **R-1.** The record narrows "If there is a spec involved, those docs are updated" by type of specification, and calls the narrowed rule Nathan's. It also contradicts its own ITEM-05. The first live run has a specification, but under this design it leaves PF30 untouched.
- **R-2.** The new TW-ALPHA release needs Nathan's waiver of `tw-flowmaster`'s readiness, as C2's and C3's releases did. The record calls the skill unaffected and asks for nothing.
- **R-3.** An addendum can leave a run undrained on the triage pass's reading alone. The run then records it as "already represented".

**What holds, by attack item.**
- **A1.** S-1 follows ruling 1's words. The execution prompt is Nathan's input to the run. E-045 lists "authorizations" among what broke the rule, and answer 2 gives the inputs as files. S-8 reads "at every phase" beyond the run. The record discloses that reading, and ITEM-07 can be dropped.
- **A2.** "Without one, neither" matches "if not, then not" and architecture §9 ("must not update PF20 or PF30 from PF10 alone"). The rest of A2 is in R-1 and L7.
- **A3.** Removing PF27's gate follows E-052's ruling ("all pf docs should be updated based on context and scope"). Plan v1.2 §1 states the gate only under "The same message also instructed:", which is PE37's summary, not Nathan's words. E-020's premise reverses, as risk 12 says. The canon quotations are accurate but incomplete (L5). "Every addendum accounted for" follows ruling 2, except where R-3 applies.
- **A7.** Everything the repository lets me test checks out:
  - The three request files' blobs and sizes.
  - A0's range: five commits, 22 files, all under `docs/ephemeral/`; canon last changed at `fffadb5`.
  - PF30.1's "CRD Plan": 15 times on 14 lines. PF20 has no HDE-EPIC040.
  - Every canon quotation I checked was found.
  - Every member's and control page's edit time equals an earlier readback on `main` (C3, C4, E-041). The page IDs equal PE40-INIT's.
  - Section counts: the TW prompts' counts equal C2's and C3's heading tables. GTWPE-FLOW-10's 20 equals C4 §P's heading list. GTWPE-MGMT-10's 24 equals the first repair's list.
  - Body quotations that the repository does not record could not be tested.

**Checks I ran, all read-only.**
- **The brief.** At `024425c` it is 12,962 bytes, sha256 `ae6a9c56b4f1901031fe63f55496c5819c5e03ef6c3fe0d115ccafb3aa5d67c6`. `024425c` adds only the two briefs to `cc6b923`.
- **The record.** At `cc6b923` it is 67,491 bytes, blob `4b72824`, sha256 `068dcacb…6e623`. I read it whole.
- **The record checks.** I ran `modification_validate.py` and `gtwpe_record_check.py` on the working-tree copy. Its blob equals `cc6b923`'s, and `docs/prompt_ecosystem_management/` is identical on `main` and the branch. Each returned 1/1, exit 0, at `ANALYZING`. Bytecode writing was off, and `git status` was clean afterwards.
- **What I did not do.** I read no Notion page, ran no agent and wrote no file. The harness auto-saved one oversized output of mine to its tool-results directory: a grep of `ERRORS.md`, holding no prompt body. I did not read it again.

REQUIRED

**R-1: R3, a silent breach of a Product Owner ruling.**
- **Path and likelihood.** Normal path. It is certain in the first live run, and in every run whose only specification is an Epic one (or, for PF20, only a CRD one).
- **The text.**
  - Front matter, ITEM-05: "PF20 and PF30 are updated as part of the run whenever a specification is involved, and not otherwise".
  - §A ITEM-05: "Nathan's rule replaces it: with a specification in the run's inputs, the run updates PF20 for an Epic Specification (TW-RECORD-10) or PF30 for a CRD Specification (TW-RECORD-20); without one, neither."
  - *The first live run*: "no CRD Specification, so PF30 is not revised".
  - *Addendum changes to PF20 and PF30*: "When no CRD Specification is in the run, PF30 is not revised".
  - S-6, which gives its source as "Ruling 3".
- **The evidence.**
  - Ruling 3 (PE40-INIT; E-046). PE39 had told Nathan that PF20 was left out of the first run. He answered: "PF20 and PF30 must be updated as part of this. of course."
  - His ruling on E-046 and E-052: "If there is a spec involved, those docs are updated. if not, then not. its basic." E-052 asked whether 2.14's change ("PF27 and PF30 adopt the same terms on their next revision") can reach PF30.
  - PE40's own restatement in E-046: "PF20 and PF30 are updated whenever the run's inputs include a specification".
  - The first live run has a specification (HDE-EPIC040), and 2.14 bears on PF30.1. On his words, PF30 is updated in that run. On the record's design it is not, and 2.14's PF30 part waits for a CRD Specification run that may never come.
  - No section names this departure: *Contradictions and risks* does not, and *Open questions* says "None". The record's own Intake makes E-054's lesson binding: "a canon reading that points elsewhere is a defect to fix". The scope of each document (HDE Phased Epics §0; HDE CRD Records §1) is exactly such a reading.
  - Downstream, GTWPE-D4 would write "what follows" into a BINDING record. EXECUTE would then mark ITEM-05 against a statement the design does not meet.
- **Refutation attempted.** S-6 sits in a table "listed for his approval", and matching by type is one fair reading of "context and scope". But the record never tells Nathan that its rule differs from his words for the very run he spoke about. It also labels the narrowed rule his, and its frozen ITEM-05 says the opposite of the design. Not refuted.
- **The smallest correction.** Choose one:
  - name the divergence and its first-run consequence in *Contradictions and risks*, and put it to Nathan as an open question (readiness `NEEDS_RULING`, interaction cost +1); or
  - restate S-6 in his words: with any specification in the run, PF20 and PF30 are each updated on context and scope, each through its own prompt. The first run's PF30.1 would then take 2.14's terms through TW-RECORD-20.

  Either way, make ITEM-05's statement and §A agree, and stop calling the narrowed rule "Nathan's rule".
- **In text the last repair added:** no.

**R-2: R3, a silent breach of a Product Owner ruling; also R1, readiness on the normal path.**
- **Path and likelihood.** Normal path (EXECUTE's selection writes). Certain.
- **The text.**
  - *Member dispositions*: "`tw-flowmaster` 1.3.0, `flowmaster-validate` 3.3.2 | Unaffected | They do not run this release (the selection page), and C6 retires the Flowmaster".
  - `readiness: READY`; *Open questions*: "None"; `override` is empty. "waive" occurs nowhere in the record.
- **The evidence.**
  - The change selects a new TW-ALPHA release (*What changes*).
  - HDE Governance §9.1.6: "Reconcile all affected producers, consumers, ... and interacting skills in one coherent successor selection ... An edited subgroup is not ready while an affected counterpart remains incompatible." The record's canon table cites this sentence for "the one part" and leaves out the interacting skills.
  - Nathan's waivers are per release:
    - C2's override: "he waives HDE Governance §9.1.6's interacting-skill readiness for tw-flowmaster, so the new TW-ALPHA release is selected in this Modification".
    - C3's risk 1, "for that release only", and its Q-1, "(a) Waive ... again, for this release", with readiness `NEEDS_RULING`.
    - C4's disposition: "under Nathan's waivers for TW-ALPHA-20261006.1 and TW-ALPHA-20261006.2 ... No TW-ALPHA release changes here, so no new waiver is needed".
- **The consequence.** The release would be selected with an incompatible interacting skill and no waiver of his covering it, and readiness and cost would be understated. A Flowmaster run against it would stop loudly (C3's risk 1). So the harm is a waiver that was never asked for, not a wrong document.
- **The smallest correction.**
  - Mark both skills Affected (interacting skills, §9.1.6).
  - Add Q-1 as C3 worded it: (a) waive for this release, on C2's grounds, recommended; or (b) update the skill.
  - Set readiness to `NEEDS_RULING` and `interaction_cost_predicted` to 10.
- **In text the last repair added:** no.

**R-3: R3, a silent breach of a Product Owner ruling; also R4.**
- **Path and likelihood.** Normal path: any run with a PF10 source. Low for each addendum, plausible across 38.
- **The text.**
  - ITEM-03, *What follows, for the plan*: "where it is already represented, by the triage pass's reading or a drain's verified `no redlines`", and "`RUN_NO_CHANGE` remains only for a run in which every addendum is shown already represented".
  - S-4, and ITEM-04's repair 3 ("or why none in this run").
- **The evidence.**
  - Ruling 2 and E-044: "if there are addenda in PF10, that means they need to be drained, otherwise they would not be in there. Whether or not an addendum states an explicit drain target, it needs to be drained."
  - When a drain finds a change already represented, it gives "an exact equivalence location" (the record's own quotation). C4 made "a drain's verified `no redlines`" the authoritative "not affected" when in doubt (C4 §A ITEM-01, *Triage*). A triage reading carries neither safeguard.
- **The consequence.** Suppose the triage pass misreads an addendum as already represented. It is never drained, yet `RUN.md` and the pull request show it as accounted for. The run can then end `RUN_NO_CHANGE` or `RUN_REVIEW_READY`. That is the silent outcome E-044 was ruled against, now under an "every addendum accounted for" label.
- **The smallest correction.**
  - Count an addendum "already represented" only on a drain's verified `no redlines`, with its exact equivalence location, for each document the addendum bears on.
  - The triage pass's reading routes those documents to their drains and never closes an addendum by itself.
  - Change S-4's wording to match.
- **In text the last repair added:** no.

LISTED (each: attack item; path; likelihood; consequence; in repair text)

- **L1** (A5; normal; medium; old text could survive unless PLAN works from *Scope*, though PLAN's D26-E search should catch it loudly; partly: D5 added TW-DRAIN-20's *Development-board independence* to *Scope* only): ITEM-02's table omits passages that *Scope* counts as reached by ruling 1, and *Scope* says "the passages reached are the text they contradict". The omitted sections:
  - GTWPE-FLOW-10's *B5* and *Redo from canon*;
  - the drains' *Authority and sources* and *General PF preparation*;
  - TW-DRAIN-20's *Development-board independence* and *PF09 coverage*;
  - the *Authority and sources* of the record prompts and of TW-APPLY-10;
  - TW-APPLY-10's *Intake and preparation-state verification* and *Invalidity, failure and return*.

  So claim C3 does not hold as written.
- **L2** (A5, A7; normal; low; a loud failure at PLAN's anchors; no): ITEM-02's row "All six TW prompts, *Turn preflight* item 3 and *Output identity*" cannot include TW-TRIAGE-10. Its headings are only *Coded identity and relationships*, *Purpose and authority*, *Source identity and routing* and *Output* (C2's heading table), as the record's own *Scope* row shows. The row should read "the five document prompts".
- **L3** (A5; normal; low; no effect, since every member changes; no): `closure.state_sharers` lists only the two drains. C3 found that all five document prompts share `PARTIAL_PACKAGE` in their common save-recovery rules, correcting C2's drains-only reading. It recorded `[TW-APPLY-10, TW-DRAIN-10, TW-DRAIN-20, TW-RECORD-10, TW-RECORD-20]`, and the bodies are unchanged since.
- **L4** (A5; normal; low; one stale table line and an unexplained choice of rows; partly: D9 added F9):
  - *Scope* reaches F3, F5, F6 and F9 "lightly" for a single stated reason, yet *What changes* changes F6 and F9 but not F3 or F5, and gives no reason.
  - *What changes* omits the *Common rules* change that *Scope* names.
  - The table's "F2 to F8 below name the outcomes" goes stale once the triage rows are added.
- **L5** (A3, A4; normal, for a run between an epic's QA PASS and its closure; low today, since HDE-EPIC040 closed on 2026-09-29 by CL-E-10 v1.2; drafts that drain an unclosed epic go unflagged; the PF20 part would likely stop loudly at TW-RECORD-10's completed-posture input, F7; no): ITEM-03 and S-4 take canon's drainage timing from the Change Process Guide's post-QA ordering only. Canon sets two later points:
  - HDE Governance §9.1.5 ("Post-closure maintenance records actual PF10 drainage first") and §2.0.19's *Post-closure maintenance ordering* put drainage after the Isis closure decision.
  - The Change Process Guide §3.5.1 ("added there once, at epic close ... In-flight epics MUST NOT be recorded there") and §1.1.2 do the same for PF20's epic record.

  S-6 carries no closure condition.
- **L6** (A4; normal; medium; a canon conflict decided without being named; no): ITEM-05's *Canon* bullet concludes "it conflicts with no canon, since the run Nathan starts with a specification is such an action". That is PE40's canon reading, which E-054 records as withdrawn. The bullet also reads only §9.1.1's historical-drainage sentence. §9.1.1 says more:
  - PF20 and PF30 are "historical/reference homes only ... The active workflow MUST NOT create, update or synchronize their entries";
  - "Preserve existing PF20/PF30 content and original identities as dated history".

  S-7's in-place update of an existing CRD record follows HDE CRD Records §3.2 and §4.2, and the Change Process Guide §1.0.6, over that clause. That decides part of E-010, whose interim posture is "the record prompts follow §9.1.1", while the record says E-010 "stays his".
- **L7** (A2; normal; medium; edits across many sections of PF20, 952,515 bytes, and of PF30, with no redline package and no diff check; no):
  - Risk 6 resolves S-7's departure from "they only get one SECTION" by recency, and from C1's approved R2 ("PF20 and PF30 add one section each"). But "DON't need the redliner" does not contradict "one SECTION".
  - S-7 removes the record prompts' only drift check ("differs from its original only by the inserted entry and its control fields") and names nothing in its place. Nathan called that discipline "an important determinism and drift control".
  - The *GTWPE-D1* table extends "that nothing else changed" only to an existing record's update.
- **L8** (A4; normal; medium; an execution prompt that pins a PF version against canon, or no form that names PF10 by filename alone; no): risk 14 says HDE Governance §9.1.6's reference rule concerns the durable bodies. But §9.1.6 also covers "temporary repair/review/handoff prompts" ("versionless document name"; no "version-pinned external filenames"), and HDE Build Notes 2.14 says "Do not pin a PF file version in a prompt". A filenames-only execution prompt naming `PF10-HDE-Build-Notes-v13.5.md` satisfies ruling 1 and pins a version. The record settles this conflict between his ruling and canon in a risk without naming it. §9.1.6's carve-out for "exact source binding in run artifacts" may cover the case; PLAN must say whether it does.
- **L9** (A1; normal; certain; Nathan loses the TW prompts' optional selections when he invokes them himself; no): risk 2 calls this "a behaviour his ruling requires". But ruling 1's words address a run and its handoffs, and ITEM-04 point 5 treats direct invocations as outside his rulings. S-3's reach into direct invocations is a reading, and should be put to him as one.
- **L10** (A1; failure path: a held-back PF10 change; low; loud, since check 6 stops the document again on every resume; no): S-3 removes the only way Nathan's "leave it out" decision reaches the passes ("His decision to leave it out is a selected boundary that excludes the change, and every invocation for those documents carries it", C4's `draft-repairs.json`, R-1). S-1 leaves the decision file's form to PLAN.
- **L11** (A5; normal; low; a handoff that carries more than files, or an exception nobody stated; no): the triage pass's per-addendum return is inline ("its triage is a return, not an artifact"). ITEM-02, though, says no handoff passes anything but files, and *Scope* reads a pass's return as "its outcome and the paths of what it wrote". PLAN must make the return a file or list it as an exception.
- **L12** (A3; normal; low; a run with no defined ending; no): take a run in which every addendum is held back, has no eligible home or waits on a specification, and no draft exists. It is not `RUN_NO_CHANGE`, because not every addendum is "shown already represented", and it has nothing to make `RUN_REVIEW_READY`. ITEM-03 does not say how such a run ends.
- **L13** (A6; normal; low; GTWPE-D3 could leave out ITEM-04's ruling; no): ITEM-01 records "ruling 1, both sentences", but ruling 1 has six sentences in two quotations. It records "ruling 2's two sentences", but ruling 2 has three, and the third, "part of this run is to have a prompt evaluate the drain targets", is ITEM-04's basis.
- **L14** (A6; low; no item changes; no): claim C1 overstates. The Intake does not map:
  - E-053's "PF20 and PF30 had their own special prompts. I guess they were just lost or ignored.";
  - E-046's "of course there is PF20" and "I feel like you have engineered all of this wrong. I am very concerned";
  - "this is meaningless distinction" (E-046, E-054);
  - E-042's "I don't think we need to go back to plan for this, the agents will be smart enough to get around this.", which bears on the record's E-042 candidate.
- **L15** (A6; normal; low; part of C5 settled without saying so; no): S-5 makes TW-TRIAGE-10 a pass inside the Flow Manager's run. That goes against C1's approved §A A.2 ("The Change Manager is TW-TRIAGE-10, extended") and Nathan's answer 1, that the two roles "should not be treated as the same session or role". Yet ITEM-04 says "Recorded, not decided here".
- **L16** (A7; low; the stated method and number do not reproduce, SCOPE-001; no): `git grep` with ruling 1's terms finds 5 lines (7 ignoring case) in `gtwpe.decision-record.md`, not "three lines"; the extra lines are the file's own name, "decision record". It finds 2 lines (4 ignoring case) in `gtwpe_record_check.py`, not "one line".
- **L17** (A5; low; template conformance; no): PART-01 has no `name`. The template says "keep the keys", and every earlier GTWPE record names its part. Neither validator checks this.
- **L18** (A8; normal; high; cost understated; no):
  - `interaction_cost_predicted` 9 assumes no ANALYZE repair, no diff check and two merges. C2 to C4's actuals broke each of these assumptions: 14, 11 and 13 against 8, 7 and 7, and C4 also merged its branch pull request at `ANALYZED` and merged a failure record.
  - R-2 alone makes the prediction 10.
  - The estimate has no token figure, though D26-D asks for "a time and token estimate". C2 to C4 gave none either.
- **L19** (A5; low; incomplete dispositions; no): *Member dispositions* omits interfaces that C4's table carried: `glow-artifact-storage`, `glow-workspace-currency`, and the GCFPE register and Flow Index. §9.1.6 asks for each to be compared, with a reason.
- **L20** (A4; normal; low; a paraphrase of the old behaviour could escape a term search; no): *Defect classes* does not match FUNC-001, although ruling 1 retires a behaviour (passing context) that a body can express without any of the listed terms. PLAN's D26-E search should state the functional test: does anything make a run or pass take, or a handoff carry, anything but the prompt to run and files?

## Canon relied on

- **`AGENTS.md`:** the canon-first rule; PF canon read-only; evidence attribution. Its code-review scope line does not apply to this D26-A review.
- **PF canon, from `docs/pfcanon/` on `main` at `128836a`** (the local `origin/main`, not fetched; unchanged since `fffadb5`):
  - **HDE Governance (PF04):**
    - §9.1.1 in full, with *Historical drainage*;
    - §9.1.5 and §9.1.6 in full;
    - §2.0.19's closeout bullets *QA-first closeout ordering* and *Post-closure maintenance ordering*;
    - §9.7.1's PF20/PF30 line.
  - **Change Process Guide (PF06):** *Post-QA documentation drainage ordering (normative)* in §3.5.2.8; §3.5.1 *Requirement*; §1.1.2; §1.0.3 to §1.0.6.
  - **HDE Build Notes (PF10):**
    - front matter: *Purpose*, and *Precedence, versioning, and scope* §1 to §9;
    - 2.14 in full;
    - 2.29's source, location and storage sections; 2.38's source and rule;
    - 2.1 and 2.37, by search.
  - **HDE CRD Records (PF30.1):** §0 to §6 in full; §7's headings; "CRD Plan", by search.
  - **HDE Phased Epics (PF20):** front matter and §0 in full, with *Drain posture*; record headings, by search.
  - **The canon search:** `git grep` over `docs/pfcanon/` for PF20, PF30, Phased Epics, CRD Records, drain, ordering, closure and HDE-EPIC040.
- **Governing documents in `docs/prompt_ecosystem_management/`:**
  - `gcfpe.decision-record.md`: D20 to D26, with D23's clarification on subagents;
  - `modification-template.md` and `ecosystem-change-management.md`, whole;
  - `reviewer-prompt-template.md`: the second template;
  - `notion-write-boundary.md`: the policy and the read-only default;
  - `prompt-body-content-policy.md`: the rule;
  - `gtwpe/gtwpe.decision-record.md` and `gtwpe/gtwpe.handoffs.md`, whole;
  - the main paths of `modification_validate.py` and `gtwpe/gtwpe_record_check.py`.
- **The request and the change's own records:**
  - the record at `cc6b923`, whole, and this brief at `024425c`;
  - `PE40-INIT-20261007.md` and `GTWPE-TARGET-ARCHITECTURE-20260929.md`, whole;
  - `ERRORS.md`: E-043 to E-054 in full, and every other row's disposition;
  - `CHECKPOINT.md` §8; implementation plan v1.2 §1 and §2.1;
  - C1's §A A.2 to A.6;
  - C2's front matter and heading table;
  - C3's front matter, *Per part*, risk 1, Q-1 and heading table;
  - C4's front matter, §A ITEM-01 to ITEM-06, *Per part*, *Member dispositions*, *Readiness*, §P's page structure and §E's cost;
  - the first repair's D3;
  - `gtwpe-tw-repository-io/edits-2.json`, `gtwpe-tw-document-rules/edits.json`, `gtwpe-writing-side/edits.json` and `gtwpe-flow-manager/draft-repairs.json`;
  - the front matter of `HDE-EPIC040-CL-E-10-closure-decision-v1.0.md` to `v1.2.md`.

IN FLIGHT: R-1 to R-3 go to repair. Then D26-A allows a second full review or a check of the repair's diff, after which §A goes to Nathan with L1 to L20 listed.
