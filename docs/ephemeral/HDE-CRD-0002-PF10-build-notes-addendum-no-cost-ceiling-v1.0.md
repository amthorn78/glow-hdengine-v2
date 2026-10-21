## 2.19 Requirements and work units carry no cost ceiling; work continues until it is done

Timestamp: 102126 19:07 (UTC). Details: Withdraws the cost ceiling that addendum 2.11 added to every requirement and work unit, together with every gate, return, recording duty and decision that depends on it. Removes nothing else. The business case keeps its beneficiary, evidence, benefit and measure, and the real-input, emulation, finding-disposition, repeated-finding-class and P1 rules stand. Origin: the Product Owner's direction of 2026-10-21 in the continuing HDE-CRD-0002 Lead Developer session (Isis, https://claude.ai/code/session_012tPq26JWVhCYZmcqTidpV2). It followed the IA-30 change assessment 01 v1.1 question on WU-PR-08's ceiling.

### Source and authority

This addendum records the Product Owner's rule, in the Product Owner's words:
- "these ceiling concepts are practically meaningless. I don't know where they got introduced. Work is done until its done."
- "ok create a new PF10 addendum. there is no value to me in this concept."

Where the ceiling came from: the HDE-CRD-0002 WU-PR-06 postmortem proposed "a cost ceiling per unit", and it entered HDE Build Notes as part of addendum 2.11. The Product Owner's own words recorded in 2.11 ("Every PR must have a business case. It cannot simply be for the sake of evidence or CI." and "no work is ever done based on inputs the product will never have.") do not mention a ceiling.

Where this addendum conflicts with an earlier addendum or with an in-flight change document, this addendum governs for the scope below.

### Rule

1. **No cost ceiling.** A requirement or work unit states no cost ceiling: no budget in sessions, elapsed days, review rounds or pushes.
   - The business case of addendum 2.11 rule 1 consists of its beneficiary, evidence, benefit and measure.
   - The field "its cost ceiling: the most the work may spend before it returns to the Product Owner, in sessions and elapsed days" is withdrawn.
2. **Work continues until it is done.** Spend, elapsed time and the number of sessions, review rounds or pushes are not, by themselves, a reason to stop work or return it to the Product Owner.
   - Work returns to the Product Owner only where another rule sends it:
     - addendum 2.11 rule 8 (repeated finding class);
     - addendum 2.14 (a P1 decline);
     - a material change, rescope or Product Owner decision required by the governing prompt or canon.
   - A real need for Product Owner direction on scope or risk still goes to the Product Owner.
3. **Gates without a ceiling.** In addendum 2.11 rule 3:
   - Specification approval still blocks a requirement without a business case.
   - IA-30 checks each work unit's business case.
   - PR-10 carries the business case into the instruction.
   - The Proceed is given against the business case.
   - A unit whose business case is met still stops.
   - Withdrawn:
     - "and ceiling" in the IA-30 bullet;
     - "both" in the PR-10 bullet, read as including the ceiling;
     - "and PR-20 states how the plan stays within the ceiling";
     - the whole bullet beginning "A unit that passes its ceiling".
4. **Internal tooling.** Addendum 2.11 rule 2's last sentence reads "Internal tooling qualifies only when its expected saving, from observed incident data, exceeds its expected cost." Its comparison with a ceiling is withdrawn.
5. **No recording against a ceiling.** No session, checkpoint, result record, lineage review or Product Owner decision records spend against a ceiling, projects a pass of one, or sets one. PR-40 still records whether the unit's measure was met.
6. **Unchanged.** The following stand as written and as superseded before this addendum:
   - addendum 2.11 rules 4 to 8;
   - the real-input definition;
   - addendum 2.14 rules 1 to 4 and 6;
   - the CI-budget rules that addendum 2.11 left unchanged.

### Scope and supersession

Applies from this addendum to every Epic and CRD, including the remaining HDE-CRD-0002 units. Supersedes, for the cost-ceiling scope only:

- **Addendum 2.11:**
  - rule 1's cost-ceiling bullet;
  - rule 2's comparison "exceeds its ceiling" (restated by rule 4 above);
  - rule 3's ceiling clauses and its passing-the-ceiling bullet;
  - in "Deferred obligations and unresolved work", the clauses:
    - "and ceiling" (IA-30);
    - "and ceiling" (PR-10);
    - "PR-30 and PR-35 record spend against the ceiling in each checkpoint";
    - "the unit's actual cost against its ceiling and" (PR-40).
- **Addendum 2.12:** the treatment of a missing ceiling as a gap (LR6-O3's "ceiling") and the "cost ceiling in sessions and elapsed days" in the decision returned for WU-PR-07.
- **Addendum 2.13:** the ceiling statements and the rule that a projected pass of the ceiling is material. These are historical for the completed WU-PR-07.
- **Addendum 2.14:** rule 5 ("Budget") in full.
- **Addendum 2.15:** the sentence that a projected pass of the unit's cost ceiling returns to the Product Owner.
- **Addendum 2.16:**
  - "Cost against the ceiling" and "The unit did not pass its cost ceiling", kept as historical facts of the completed WU-PR-07;
  - "cost ceiling" among WU-PR-08's unmet prerequisites and among the decisions returned to the Product Owner.
- **Addendum 2.18:** the sentence "Its business case and cost ceiling are in the Product Owner decision record §2 (addendum 2.11 rule 1)", read as "Its business case is in the Product Owner decision record §2".

Everything else in those addenda is unchanged. Earlier ceiling decisions and cost-against-ceiling records stay as historical facts with no current effect.

### Epic, task, and status effects

- **No status change.** No epic, CRD, task, PF09 or PF30 row changes status by this addendum.
- **HDE-CRD-0002 WU-PR-08:**
  - Its business case is the beneficiary, evidence, benefit and measure of `docs/ephemeral/HDE-CRD-0002-WU-PR-08-po-disposition-scope-v1.0.md` §2. Its "Cost ceiling" row is not in force.
  - The ceiling-related text of `docs/ephemeral/HDE-CRD-0002-implementation-plan-change-assessment-v1.1.md` is not in force:
    - in §1, the ceiling bullet;
    - in P-7, "and the ceiling as the Product Owner sets it" and "The ceiling is the one the Product Owner sets in the recorded decision that §5 asks for";
    - in §5, "The ceiling question";
    - in §6, the ceiling row;
    - in §7, the condition "with the ceiling recorded".
  - The Plan delta carries no ceiling for WU-PR-08, and IA-30's delta review does not wait on one.
  - The assessment's corrected fact stands: WU-PR-08 changes the CI classifier, so its pull request runs all seven lanes.
- **HDE-CRD-0002 WU-PR-07:** its adopted ceiling (`docs/ephemeral/HDE-CRD-0002-WU-PR-07-po-disposition-business-case-v1.0.md`) and the recorded cost against it are historical. The unit is accepted.
- **HDE-CRD-0002 WU-DOC-01 and WU-OPS-01:** their business cases, due before DOC-10 and OPS-10, state beneficiary, evidence, benefit and measure only.

### Required canon drainage

None of its own. Permanent PF canon states no cost ceiling for requirements or work units (searched; see Evidence anchors). Addendum 2.11's drainage targets, below, carry the business case without a ceiling:
- HDE Governance §9.7.7;
- Plan Templates "Business Case (MUST)";
- HDE CRD Records §4.1.

### Deferred obligations and unresolved work

- **Prompt wording changes.** Addendum 2.11's prompt changes are unperformed and held in the GCFPE Modification Backlog. When made, they omit every ceiling clause:
  - IA-30 "and ceiling";
  - PR-10 "and ceiling";
  - PR-20 "stays within the ceiling";
  - PR-30 and PR-35 "record spend against the ceiling";
  - PR-40 "actual cost against its ceiling".

  Owner: GCFPE-MGMT-10 and the Product Owner.
- **PF10 numbering and publication:** the Product Owner. This record follows addendum 2.18, which is pending publication.

### Scope boundaries and nonclaims

- This addendum changes no prompt, skill, AGENTS.md or permanent PF document. It edits no in-flight record. The records named above are read under it.
- It is not a QA verdict, acceptance, closure, Plan approval or PR Proceed.

### Evidence anchors

- **Direction:** the Product Owner's direction, quoted above, given on 2026-10-21 in session https://claude.ai/code/session_012tPq26JWVhCYZmcqTidpV2.
- **Canon searched on origin/main `a78b3509`:** "ceiling" across `docs/pfcanon/`.
  - HDE Build Notes: addenda 2.11 to 2.16, each read at its ceiling passages; addenda 2.11 and 2.14 read in full at their rules.
  - Other hits are unrelated:
    - HDE Governance (retry delay `exp_ceiling_ms`);
    - HDE CLI/API/Vendor Reference (retry `ceiling_ms`);
    - HDE Mechanics Guide (a vendor request ceiling);
    - Glow QA Guide (a review file ceiling).
  - Read: HDE Build Notes front matter §5 "Individual-addendum supersession" and §9 "Operational rule for agents".
- **In-flight HDE-CRD-0002 records naming a ceiling** (searched in `docs/ephemeral/`): the WU-PR-06 postmortem v1.0 and v1.1, the WU-PR-07 business-case record and its PR records, the WU-PR-08 scope decision record, the addendum 2.18 record, and the Plan change assessment v1.0 and v1.1.
- **Notion:** the GCFPE Modification Backlog carries the unperformed prompt changes, including "Record spend against the unit's ceiling in each checkpoint". The 100926.1 prompts the search returned (IA-30, PR-10, RS-20) were last edited on 2026-10-12, before addendum 2.11. The other prompts were not opened.

### Relationship to existing HDE Build Notes guidance

This addendum narrows addendum 2.11 by removing its cost ceiling, and supersedes the ceiling passages of addenda 2.12 to 2.16 and 2.18 listed above. It keeps the rest of addendum 2.11 and addendum 2.14, which remain authoritative for their distinct scopes.
