# HDE-CRD-0002 WU-PR-06: postmortem of the read-only pre-push check (S20)

```yaml
artifact_type: INCIDENT_RCA
artifact_id: HDE-CRD-0002-WU-PR-06-POSTMORTEM
version: v1.1
predecessor: docs/ephemeral/HDE-CRD-0002-WU-PR-06-postmortem-v1.0.md (v1.0; blob 4510ca5c829c; 31,668 bytes; sha256 349f9fdb69b5036a3a3385cc4bf3df6c20f16926ba8f7075e7f2a7d54338da12; preserved unchanged, and cited by PF10 v13.6.2 addendum 2.11)
revision: adds §17, the decisions taken after v1.0, and §18, an observation on addendum 2.11's rule cross-references. §1 to §16 are v1.0's text unchanged
change_id: HDE-CRD-0002
work_unit_id: WU-PR-06
requirement: S20
pr: https://github.com/amthorn78/glow-hdengine-v2/pull/660
pr_state_at_writing: open, MERGE_PENDING (result v1.24, head bd2dc3a); hosted CI run 39406716584 on bd2dc3a in progress
requested_by: Nathan (Product Owner), in the WU-PR-06 PR-20/PR-30 session, before PR-40
author_session: https://claude.ai/code/session_01NZEtMVb5HR3XYEmJ6W5cb6 (author of the PR-20 plan v1.0 and the PR-30 result v1.0 of this unit)
canon_read_on: origin/main 0442d23
analysis_state: COMPLETE
canon_change: NONE by this record. Sections 9 to 12 were proposals in v1.0. The Product Owner adopted §9 and §10 as PF10 v13.6.2 addendum 2.11, and §12 as D-4 (§17)
code_change: NONE
```

## 1. Finding

WU-PR-06 spent 24 Codex review rounds, 51 findings, 24 completed hosted CI runs (7.5 hours of runner time) and 21 hours of PR-35 work. The business case for it was never established.

- **The business function was done at PR-30.** S20's stated purpose was fewer failed paid CI runs. Its only evidence was PR04's 4 failed runs out of 19. Those 4 were catchable by running CI's own steps locally. The PR-30 tool already did that: it replayed all 16 steps of the real `ci.yml` locally and passed, and hosted CI passed on the same head.
- **Almost everything after PR-30 was built for inputs the product never has.** 49 of the 51 findings needed a `ci.yml`, `pyproject.toml`, `requirements-dev.txt`, environment or Git state that no commit on `main` has ever had, and no planned unit creates. The fixes for 41 of them were later deleted, or left unable to change any outcome, by the redesign PO-35-4.
- **Three causes:**
  1. Canon requires a Business Case only for Epics. A CRD requirement needs only a "warrant". S20 had none in the approved Specification, and nothing measured it.
  2. The design promised fidelity to external systems over open-ended inputs: replay whatever `ci.yml` a candidate has, and fail closed on any construct not understood. My plan v1.0 made that promise (PD-8). Every constructed input then became a real defect against the plan.
  3. Nothing told the reviewer, the PR-35 prompt or the round-7 decision to ask whether an input is real. Canon has no churn trigger for PR review. The loop stopped only when the Product Owner imposed the real-input test (PO-35-5, PO-35-6).

## 2. Scope and evidence standard

- **Covers:** WU-PR-06 from its Specification requirement (S20) to MERGE_PENDING on #660.
- **Primary sources:**
  - the Specification v1.1 and the candidate-item briefs v1.2;
  - Implementation Plan v1.1;
  - PR instruction v1.0 and PR plan v1.0;
  - PR implementation results v1.0 to v1.24;
  - the GitHub Actions run list for branch `claude/youthful-gauss-d9e0ab`;
  - the PR #660 record;
  - `git log` of `main`;
  - the PR-35 prompt (100926.1) in Notion.
- **Every number below is read from those sources.** Where something is inferred, the text says so.
- **Wall times** are each run's `created_at` to `updated_at`, which includes queue time.
- **Not covered:** WU-PR-03's corrective cycles, and HDE-CRD-0002 as a whole.

## 3. Timeline (UTC, 2026)

| When | Event |
| :- | :- |
| Intake | Briefs v1.2 item 7: "Each PR session re-derives the same checks by hand or skips them … PR04 had 4 failed CI runs out of 19." The warrant is a forecast: "It would reduce paid CI failures and the rescopes caused by unchecked lane or release impact." |
| Specification v1.1 | S20 is adopted: "One read-only pre-push and pre-plan check with its own test", including "a `ci.yml` replay". The "Why warranted" line covers S02, S03, S06, S10, S14, S19, S21 and S22. It does not cover S20. Constraints name the risk: "S20 duplicates CI logic and must track `ci.yml` changes." No limit or mitigation is set. |
| PR-10 (#658) | Instruction ID-8: replay the steps "from the head's `.github/workflows/ci.yml` text with the Python standard library", with no dependency. The final audit prints "only when CI's own rule would print it". |
| PR-20 (#659) | My plan v1.0, §5.7 and PD-8: a strict YAML-subset parser that "fails closed on any construct it does not understand", plus "substituted outcomes for the three exclusions", including the install step. |
| 19 Oct 13:00 | PR-30 opens #660 (PR_CANDIDATE_PUBLISHED). Owner test 21 passed. The local replay ran all 16 steps and passed (`CI_APPLICABILITY_AND_EXACT_HEAD_OK`). Hosted CI passed on `d2ed4fc`. |
| 19 Oct, rounds 1 to 6 | CX6-1 to CX6-11: the install check and the YAML reader do not model pip, PEP 440 or GitHub Actions closely enough. Each is fixed. |
| 19 Oct, round 7 | PO-35-1 declines CX6-12. PO-35-2: asked "What rule should I apply to further findings of that kind?", with "Fix if real and small (recommended)", the answer is "Fix every finding". |
| 19 Oct, round 8 | CX6-15, the one P1: a candidate's steps inherited the caller's environment, secrets included. A real finding. PO-35-3: an allowlisted child environment. CX6-16 and CX6-17 are fixed. |
| 19 to 20 Oct, rounds 9 to 21 | CX6-18 to CX6-45 are each fixed under PO-35-2. The tool grows to a pushed peak of 2,132 lines. |
| 20 Oct 07:22, after round 22 (CX6-46 to CX6-48) | PR-35 escalates. PO-35-4: pin `ci.yml` by SHA-256, reduce the install check to presence only (the PR-30 rule), and run the classifier only in copies. PO-35-5 replaces PO-35-2: fix only a wrong result on "the repository's real ci.yml, real install step or real tree", or a breach of the read-only or no-secrets guarantees. CX6-46 and CX6-48 are fixed under PO-35-5. CX6-47 is resolved by the pin. |
| 20 Oct, round 23 | CX6-49 is declined under PO-35-5. CX6-50 is fixed. |
| 20 Oct 10:08 | PO-35-6: "A snapshot-precision finding is a hypothetical-input finding unless it shows a write that the tool itself or code it runs in the checkout can make." CX6-51 is declined. |
| 20 Oct 10:16 | MERGE_PENDING (result v1.24, `bd2dc3a`). |

## 4. Cost

| Measure | Value |
| :- | :- |
| Codex review rounds | 24 |
| Findings | 51: 50 P2 and 1 P1. 47 fixed, 1 resolved by the pin (CX6-47), 3 declined as stated limits (CX6-12, CX6-49, CX6-51) |
| Hosted CI runs on #660 | 25: 23 success, 1 failure (`7a3b7b2`, an intermittent close-pack test) and 1 in progress |
| Hosted CI wall time, completed runs | 451.6 minutes (7.5 hours) |
| PR-35 elapsed time | 21 h 16 min, from PR open (13:00Z, 19 Oct) to MERGE_PENDING (10:16Z, 20 Oct) |
| Commits on #660 | 50 |
| Result records | 25 (v1.0 to v1.24) |
| `tools/ci/prepush_check.py` | 1,229 lines at PR-30; 2,132 at the pushed peak; 1,755 at head |
| Owner test | 552 lines and 21 cases at PR-30; 1,229 lines and 141 cases at the peak; 1,070 lines and 137 cases at head |
| PR diff | +6,789 lines in 28 files |

**Sibling units, same CRD and same reviewer.** Codex code-review findings on the final pull request of each unit:

| Unit | Pull request | Findings |
| :- | :- | :- |
| WU-PR-01 | #630 | 0 |
| WU-PR-02 | #637 | 0 |
| WU-PR-04 | #651 | 1 (P1) |
| WU-PR-05 | #656 | 1 (P2) |
| WU-PR-06 | #660 | 51 |

The figures for the other units come from PF10 addenda 2.4, 2.5, 2.9 and 2.10. The volume came from what WU-PR-06 built, not from the reviewer.

## 5. The business case, tested

| Question | Answer from the record |
| :- | :- |
| Who benefits? | PR sessions and the Product Owner, through fewer failed hosted runs and fewer rescopes. |
| What evidence shows the problem? | One incident: PR04 (#467), with 4 failed runs out of 19. The briefs list #467, #492, #501 and #508 as intake evidence. No count of avoidable failures across them was recorded. |
| What would the benefit be? | Fewer failed hosted runs. This was never quantified. |
| How would it be measured? | No measure was defined. |
| What was the cost ceiling? | None was set. |
| Was the problem catchable? | Yes. #467's description names its failed runs: the changed-test step (4 tests), an owner-guard tuple that omitted a new consumer, a test that wrote a timestamp into a tracked file and failed the clean-tree check, and one rails-lane failure. Each is a CI step that runs locally. #467's session then reproduced "All seven lanes … directly under closed rails". |
| When was the function delivered? | At PR-30: the replay ran all 16 steps of the real `ci.yml` and passed. |
| What did the unit cost against its evidence? | 24 completed hosted runs, six times the 4 failed runs that were the whole of its evidence, plus 21 hours of PR-35 work. |

**The conclusion.** S20 was a reasonable hypothesis with one data point. It became a requirement without a beneficiary measure or a cost ceiling. Once the work began, nothing in the process asked whether the next round of fixes bought anything.

## 6. The 51 findings by class

Each class is defined by where the triggering input would have to come from.

| Class | What the finding asked the tool to model | Findings | Count | Was the input real? |
| :- | :- | :- | :- | :- |
| A. Python packaging | pip resolution, PEP 440/508/621, extras, build backends, editable metadata, install-step text | CX6-1, 2, 3, 4, 5, 7, 8, 11, 14, 23, 27, 28, 30, 34, 35 | 15 | No, except CX6-1: the caller's versions can drift from CI's, but hosted CI still decides. `pyproject.toml` and `requirements-dev.txt` have one commit each on `main` (their creation, 2026-08-06). `requirements-dev.txt` has never had an extra, and `build-backend` has never changed. |
| B. GitHub Actions and YAML | runner labels, action revisions, step conditions, loose equality, `env` shapes, duplicate keys, tabs, block and flow scalars, job sets, output files | CX6-6, 9, 10, 12, 13, 18, 20, 21, 22, 25, 26, 29, 31, 32, 33, 36, 37, 38, 39, 40, 41, 42, 44, 45, 47, 49 | 26 | No. Each needs a `ci.yml` edit no commit has made. Across its 10 commits on `main`: `runs-on` was always `ubuntu-latest`, no tab ever appeared, and the actions were always `checkout@v4` and `setup-python@v5`. `persist-credentials` has been `false` since it was added. (CX6-25's second job did exist before the HDE-EPIC039 consolidation to the one `test` job.) No planned unit edits `ci.yml`. |
| C. Self-check precision | the before-and-after snapshot missing a write that nothing makes | CX6-16, 19, 24, 43, 46, 48, 50, 51 | 8 | No observed path. Each finding was confirmed only by constructing its condition: a write into `.git` or into ignored files in a scratch repository, or a `TMPDIR` inside the checkout. After PO-35-4, no repository code runs in the caller's checkout (PO-35-6). |
| D. Real | caller secrets reached child processes (P1); the sweep reported PASS without its tools when no test was uncovered | CX6-15, CX6-17 | 2 | Yes. The caller's environment holds real keys, and "zero uncovered tests" is the real state after WU-PR-01. |

**What became of the fixes.**
- PO-35-4 returned the install check to presence only: "This is plan §5.7's original rule for the install step, before IF-35-7, IF-35-12 and IF-35-14 added the modelling" (result v1.22, IF-35-23). The class A modelling was deleted.
- The pin refuses any `ci.yml` other than the pinned one before parsing it. The class B fixes can therefore no longer change an outcome.
- Together that is 41 findings' worth of work.
- Codex was measuring the code against the plan's own promise. For example, CX6-42: "omitting them from this guard violates the replay parser's fail-closed contract".

## 7. Causal chain

| Stage | What happened | What would have stopped it | Owner of the gap |
| :- | :- | :- | :- |
| Intake and Specification | S20 entered with a forecast for a warrant, no measure and no ceiling. The Lead Developer finding says "each requirement below is an observed defect or gap with a cited source". S20's source was a convenience need, not a defect. | A business case per requirement, with a ceiling. | Canon: PF04 §9.7.7 and PF27 "Business Case (MUST)" apply to Epics only. The CRD record (PF30.1 §4.1) asks only for "Warrant" for the whole change. |
| Specification review | The duplication risk was named ("S20 duplicates CI logic") but not bounded. | The same rule, checked at approval. | The CRD Specification approval route. |
| Implementation Plan and IA-30 | S20 was allocated to WU-PR-06 with no budget. | A cost ceiling per unit. | IA-30. |
| PR-10, ID-8 | The bar was set to "runs what CI would run", reading the head's `ci.yml` and adding no YAML dependency. That made the tool a GitHub Actions emulator over any candidate workflow. | Pin what you depend on; do not emulate external systems. | PR-10 has no such rule. |
| PR-20, my plan v1.0 (PD-8) | I promised the parser would fail closed on any construct it did not understand, and I gave the excluded steps substituted outcomes. That turned an open-ended input language into a contract to defend. **This one is mine.** A pin (as PO-35-4 later chose) or a stated precondition was available at planning time. | A real-input set stated per component, with one refusal outside it. | PR-20 has no such rule. |
| PR-30 | The function was delivered and working. | A check: "business case met; further work needs a new case". | No such check exists. |
| PR-35, rounds 1 to 6 | Each P2 was classified as "substantive in-scope correction" and fixed. The PR-35 prompt's only decline classes are "already resolved, duplicate/superseded, unsupported/out of scope, evidence pending, or material change". | A real-input disposition rule. | The PR-35 prompt, step 3. |
| PR-35, round 7 | PO-35-2, "Fix every finding", was chosen over the recommended "Fix if real and small". | The same disposition rule, standing, so that a blanket decision is still read against real inputs. | No standing rule; the decision fell to the Product Owner mid-loop. |
| PR-35, rounds 8 to 22 | Same-class findings recurred for 15 more rounds. The instruction's materiality test includes "budget, schedule or risk needing Product Owner direction", but no budget existed, so it never tripped. | A design escalation when the same class repeats; a ceiling that makes overrun material. | Canon's churn rules (PF06 §1.1.4; PF27 "QoS stop-rule: iteration churn escalation") cover Live QA only. |
| Codex code review | It reported constructed-input findings as P2. | Review guidelines that require a real input. | AGENTS.md "Code review guidelines" excludes Markdown and CI-exempt paths only. |

## 8. What went right

- **PR-30 delivered a working tool in one session:** the replay passed all 16 steps of the real `ci.yml`, and hosted CI was green.
- **The one real security finding was caught and fixed:** CX6-15 (P1), caller secrets reaching child processes.
- **CI was not the problem.** 23 of 24 completed runs passed. The cost was revalidating each fix, not failures.
- **PR-35 escalated with options, and the redesign worked.** PO-35-4, PO-35-5 and PO-35-6 ended the loop within three rounds and shrank the tool by 377 lines from its pushed peak.
- **The records were complete enough to make this postmortem exact.**

## 9. Proposed canon corrections (PROPOSED; not adopted)

These are proposals for the Product Owner. PF canon is read-only to agents. A change goes in as a PF10 addendum or as the Product Owner's own canon edit.

**R-1. A business case for every requirement and work unit.** Every Specification requirement, Epic or CRD, and every work unit states:
1. **Beneficiary:** who gains (Glow users, the production operator, or the delivery team).
2. **Evidence:** the observed incidents or measurements that show the problem, cited. A forecast is not evidence.
3. **Benefit:** what changes for the beneficiary, in user outcome, risk, time or money.
4. **Measure:** how the benefit is checked after delivery.
5. **Cost ceiling:** the most the work may spend before it returns to the Product Owner, in sessions and elapsed days. This is a business-case budget, not a CI-budget control.

These are not a business case:
- more complete or more faithful evidence, CI, tooling or records, for their own sake;
- conformance to canon;
- "could prevent", with no observed incident.

Internal tooling qualifies only when its expected saving, from observed incident data, exceeds its ceiling.

**R-2. Where the business case is checked, and when it ends.**
- Specification approval treats a requirement without a business case as a blocker, for CRDs and Epics alike.
- IA-30 checks each work unit's business case and ceiling.
- PR-10 carries both into the instruction.
- PR-20 states how the plan stays within the ceiling.
- The Proceed is given against them.
- A unit whose business case is met stops. Further work on it needs a new business case.
- A unit that passes its ceiling has a change of "budget, schedule or risk needing Product Owner direction". That is material under the existing definition, and the work returns to the Product Owner before it continues.

**R-3. Real inputs only.** Requirements, designs, tests, fixes and review dispositions rest on real inputs. An input is real when it:
- (a) exists on `main`, or in an approved unit's planned deliverable;
- (b) occurs in the product's real operating environment: the deployed services, the hosted CI runner, the operator's shell, the vendor's responses; or
- (c) can be supplied by a user, a vendor or an attacker through an interface the product exposes.

An input constructed only to exercise code justifies no requirement, design element, test, fix or blocking finding. An input outside the real set gets one refusal or a stated limit, never a model of it.

**R-4. No emulation of external systems.** A tool or test does not reimplement the behavior of an external system: GitHub Actions, pip and Python packaging, YAML, a vendor API, PostgreSQL. It pins the exact input it supports and refuses any other, or it calls the real system.

**R-5. Finding disposition.**
- A review finding, from Codex or from a person, is fixed when it shows a wrong result, a crash or a guarantee breach on a real input (R-3).
- Otherwise, the reply on the thread gives the traced path and the stated limit, and the thread is resolved.
- Declining a P1 or a security finding goes to the Product Owner first.
- A blanket instruction to fix every finding on a PR is read under this rule.

This makes PO-35-5 and PO-35-6 the standing default.

**R-6. Design escalation on a repeated finding class.**
- When two consecutive review rounds on one PR raise findings of the same class (the same component or contract), the session stops fixing instances.
- It asks the Product Owner one design question: narrow the design, accept a stated limit, or rescope.
- This is a design trigger by finding class. It is not a push count, a pause threshold or a CI-budget control. It leaves the Change Process Guide §0.2 rule ("There is no five-update circuit breaker") unchanged.

**Effect on WU-PR-06, had these been in force:**
- R-1 would have stopped S20 at the Specification, or given it a ceiling.
- R-4 would have led the PR-20 plan to the pin it eventually adopted.
- R-6 would have tripped at round 2, when CX6-2 and CX6-3 repeated CX6-1's class.

## 10. Draft PF10 addendum text (candidate, not adopted)

If the Product Owner adopts R-1 to R-6, this is the candidate text. On instruction, I would create it as a `PF10_BUILD_NOTES_ADDENDUM` file in the form of addendum 2.3 (`docs/ephemeral/HDE-CRD-0002-PF10-build-notes-addendum-codex-security-review-deprecation-v1.0.md`). Its number would be the next continuous one, 2.11 if no other addendum lands first.

> ## 2.11 Every requirement and work unit carries a business case; work rests on real inputs only
>
> Timestamp: <adoption time> (UTC). Details: records the Product Owner's rule that no work is done without a business case, or on inputs the product will never have. Origin: the HDE-CRD-0002 WU-PR-06 postmortem v1.0.
>
> ### Source and authority
> The Product Owner: "Every PR must have a business case. It cannot simply be for the sake of evidence or CI." and "no work is ever done based on inputs the product will never have."
>
> ### Rules
> 1. **Business case.** Every Specification requirement (Epic or CRD) and every work unit states its beneficiary, its evidence (observed, cited; a forecast is not evidence), its benefit, its measure and its cost ceiling in sessions and elapsed days. More complete or more faithful evidence, CI, tooling or records for their own sake, conformance to canon, and "could prevent" without an observed incident are not a business case.
> 2. **Gates.** Specification approval blocks a requirement without one. IA-30 checks each unit's business case and ceiling. PR-10 carries them, PR-20 plans within them, and the Proceed is given against them. A unit whose business case is met stops; more work needs a new case. Passing the ceiling is material ("budget, schedule or risk needing Product Owner direction").
> 3. **Real inputs.** An input is real when it exists on `main` or in an approved unit's planned deliverable, occurs in the product's real operating environment, or can be supplied by a user, vendor or attacker through an exposed interface. A constructed input justifies no requirement, design element, test, fix or blocking finding; it gets one refusal or a stated limit.
> 4. **No emulation.** A tool or test pins the external input it supports and refuses others, or calls the real system; it does not reimplement an external system.
> 5. **Finding disposition.** A finding is fixed when it shows a wrong result, crash or guarantee breach on a real input. Otherwise the reply gives the traced path and the stated limit, and the thread is resolved. Declining a P1 or security finding goes to the Product Owner first.
> 6. **Repeated finding class.** Two consecutive review rounds on one PR with findings of the same class stop instance fixes; the session asks the Product Owner one design question (narrow, stated limit, or rescope). This is a design trigger, not a push count, pause threshold or CI-budget control.
>
> ### Scope and supersession
> Applies from adoption to every Epic and CRD, including units of in-flight changes not yet at PR-10. It extends the Epic Business Case rule of HDE Governance §9.7.7 and Plan Templates "Business Case (MUST)" to CRD requirements and to work units. It adds a PR-review trigger beside the Live QA churn rules. It does not change the CI-budget rules of the Change Process Guide §0.2 or Plan Templates "CI lane classification and automated budget-control discipline". It establishes no QA, acceptance, merge or closure.

## 11. Prompt changes to route to GCFPE-MGMT-10

| Prompt | Change |
| :- | :- |
| CF-C-30 and CF-E-30 (Specification approval) | Check R-1 per requirement; a requirement without a business case is a blocker. |
| IA-30 | Check each unit's business case and ceiling. Flag any acceptance criterion that depends on emulating an external system (R-4). |
| PR-10 | Carry the unit's business case and ceiling into the instruction. Do not set fidelity targets against external systems; use a pin or a stated precondition. |
| PR-20 | State each component's real-input set and how inputs outside it are refused. Make no promise of fail-closed handling over an open-ended input language. |
| PR-30 and PR-35 | Record spend against the ceiling in each checkpoint. In PR-35 step 3, add the class "constructed input (R-3): traced path and stated limit". In step 4, "resolve all … substantive in-scope findings" applies to real-input findings. Add the R-6 trigger. |
| PR-40 | Record the unit's actual cost against its ceiling, and whether its measure was met. |
| `glow-hde-pr-development` skill | Same as PR-35, through the skill's owner. |

## 12. Proposed AGENTS.md text ("Code review guidelines")

This needs the Product Owner's explicit instruction before anyone edits AGENTS.md.

> - Report a finding only when its triggering input is real:
>   - it exists in this repository on the PR head or `main`;
>   - it occurs in the product's real operating environment (the hosted CI runner, the deployed service, the operator's shell); or
>   - a user, vendor or attacker can supply it through an interface the product exposes.
> - Do not report a finding that needs a hypothetical future edit to a file the PR does not change, such as `.github/workflows/*.yml`, `pyproject.toml` or `requirements*.txt`.
> - Where a tool pins the input it supports and refuses any other, a different input is not a defect.

## 13. Remaining HDE-CRD-0002 units: business-case screen

This is a first screen from the Implementation Plan v1.1 and the Specification v1.1. It is not a decision.

| Unit | Scope | Business case | Real-input check | Screen |
| :- | :- | :- | :- | :- |
| WU-PR-07 | S21: close-pack writer for Epic and CRD identities, close-run evidence family, ADR draft | The beneficiary is the close process. The evidence is one incident: HDE-EPIC040 needed exceptional closure. No benefit is stated in product terms, and there is no measure or ceiling. | Real: this CRD's own close. | **The highest risk of a repeat.** It is governed evidence machinery (T0 to T7, a new evidence family, an ADR) whose only beneficiary is closure. It needs an R-1 business case before its PR-10, weighed against cheaper options such as a canon change to the close-report requirement or keeping exceptional closure. |
| WU-PR-08 | S01: every release member in the wheel. S16: `GEO_API_KEY` in `.env.example`. S17: `docs/ADAPTER_009.md` corrections. The release 1.4.0 cut. | S01's acceptance is "A regular wheel install admits the complete release outside a source checkout". | **Open for S01.** Whether production ever installs from a wheel is unknown. The Railway build command and deploy trigger are a PF07-gap that WU-OPS-01 discovers only after WU-PR-08. S16, S17 and the cut are real. | Establish the Railway build command and deploy trigger (a read-only fact) before WU-PR-08's PR-10. If production runs from a source checkout, S01 serves an install mode the product does not use. |
| WU-DOC-01 | Final repository documentation | Operators and agents read these documents. | Real. | Proceed. It shrinks with any scope that is dropped. |
| WU-OPS-01 | Place the QA candidate in production; record the deployment facts | S02 (a live public production defect) and S10 (a fail-open security default) reach users only when deployed. | Real. | The strongest business case left in the CRD. Whether WU-PR-03's merged fixes for S02 and S10 are already live depends on the same unknown deploy trigger. |

## 14. Decisions for the Product Owner

| # | Question | Impact | Recommendation |
| :- | :- | :- | :- |
| D-1 | WU-PR-06's fate before PR-40 | PR-40 waits on it | Merge #660 with a measure and a stop date (option A) |
| D-2 | Adopt R-1 to R-6 as a PF10 addendum (§10) | Prevents a recurrence in every later change | Adopt. On your instruction, I create the addendum file. |
| D-3 | Apply R-1 and R-3 to the remaining units now | WU-PR-07 and S01 are the next likely repeats | Yes: a business case for S21 before its PR-10; the Railway build and deploy facts before WU-PR-08's PR-10 |
| D-4 | Add the §12 text to AGENTS.md "Code review guidelines" | Cuts constructed-input findings at the source | Adopt (needs your explicit instruction) |
| D-5 | Route §11 to GCFPE-MGMT-10 | Makes the rules executable in the prompts | Yes |

**D-1 options.**
- **A. Merge #660 and attach a measure.** Merge after hosted CI on `bd2dc3a` passes, then run PR-40. Each later unit's PR-40 records any hosted CI failure that a local replay would have caught. If none is recorded by HDE-CRD-0002's QA-10, the replay is removed in a later change.
  - Cost: one PR-40 session.
  - Upkeep: the pin is updated when `ci.yml` changes, and no planned unit changes it.
  - Benefit: the tool is available before WU-PR-08, which runs every lane.
- **B. Close #660 unmerged and remove S20 through a Specification delta.** Cost: a Specification-delta cycle. The work is discarded, and there is no upkeep. This is the strictest reading of R-1.
- **C. Strip the replay and merge the four small reports.** Cost: another review cycle on new code, which is the pattern this postmortem describes. Not recommended.

**Recommendation: A.** The work is already paid for and works on the real inputs. What remains costs one session. The measure turns the missing business case into a test with a stop date. Choose B if you would rather not carry unproven code at all.

## 15. Canon relied on

Read on `origin/main` `0442d23`:
- **PF04-Canon-HDE-Governance v2.8.7:**
  - §9.7.7, "Business Case section required (Epic Specifications)";
  - "Specification review boundary" ("applicable practical Business Case content").
- **PF27-Canon-Plan-Templates v2.0.5:**
  - "Business Case (MUST)";
  - §2A, "HDE-CRD-Specification Profile and PF30 Record Contract" (the CRD intake prompts; "The change lanes differ by origin, identity, and controlling work register, not by implementation, QA, evidence, review, or closure rigor");
  - "Source-bound review authority and exact-fix limits";
  - "CI lane classification and automated budget-control discipline";
  - "QoS stop-rule: iteration churn escalation".
- **PF30.1-Canon-HDE-CRD-Records v0.9.1:** §4.1, "Initial registration" (the "Observed need", "Warrant" and "Lead Developer finding" fields).
- **PF06-Canon-Change-Process-Guide v2.5.4:**
  - §0.2, "Policy and principles" ("There is no five-update circuit breaker");
  - §1.1.4, "Live QA mechanical evidence expectations" (the QoS stop-rule, threshold 2, Live QA only).
- **PF10-HDE-Build-Notes v13.6.1:**
  - searched for "business case", "hypothetical", "churn", "edge case", "Codex review" and "finding": no rule on business cases or hypothetical-input findings;
  - addendum 2.3, read for the addendum form;
  - addenda 2.4, 2.5, 2.9 and 2.10, read for the sibling Codex counts.
- **In-flight HDE-CRD-0002 documents:**
  - Specification v1.1 (the observed need, "Why warranted", S20, Constraints);
  - candidate-item briefs v1.2, item 7;
  - Implementation Plan v1.1 §7 (WU-PR-06, WU-PR-07, WU-PR-08, WU-DOC-01, WU-OPS-01);
  - WU-PR-06 PR instruction v1.0 (ID-8, §8 G-3, §14 "Material");
  - PR plan v1.0 (§5.7, PD-8);
  - results v1.0 to v1.24.
- **Prompt:** PR-35, "Resolve PR Reviews and Reach Merge Readiness", 100926.1 (Notion): "Review-first and action-efficient execution" steps 3 and 4; "Material rescope boundary".
- **AGENTS.md:** "Code review guidelines"; the canon-first rule; "PF canon is read-only unless the prompt explicitly directs a change".
- **The search found canon silent on:**
  - a business case for CRD requirements and for work units;
  - hypothetical-input review findings;
  - churn escalation in PR review.

## 16. Evidence locators

| Evidence | Locator |
| :- | :- |
| Findings and decisions | `docs/ephemeral/HDE-CRD-0002-WU-PR-06-pr-implementation-result-v1.1.md` to `v1.24.md` on `claude/youthful-gauss-d9e0ab`. PO-35-2: v1.7 §2a. PO-35-4 and PO-35-5: v1.22 §2a. PO-35-6: v1.24 §2a. |
| Hosted CI | the GitHub Actions runs for branch `claude/youthful-gauss-d9e0ab`, run numbers 3750 to 3774 |
| Input history | `git log -p origin/main -- .github/workflows/ci.yml pyproject.toml requirements-dev.txt` at `0442d23` |
| S20's origin | `docs/ephemeral/HDE-CRD-0002-candidate-item-briefs-v1.2.md` item 7; `docs/ephemeral/HDE-CRD-0002-specification-v1.1.md` |
| The design promise | `docs/ephemeral/HDE-CRD-0002-WU-PR-06-pr-instruction-v1.0.md` ID-8; `docs/ephemeral/HDE-CRD-0002-WU-PR-06-pr-implementation-plan-v1.0.md` §5.7 and PD-8 |

## 17. Decisions taken after v1.0

| # | Decision | Where it is recorded |
| :- | :- | :- |
| D-2 | **Adopted.** The Product Owner supplied PF10 v13.6.2 with addendum 2.11, "Every requirement and work unit carries a business case; work rests on real inputs only" (timestamp 102026 10:35 UTC). It states that entry into HDE Build Notes is adoption. At 10:44:07Z he directed it into #660: "Commit. This PF10 version to the current PR and remove the old version." | `b0e2299` on `claude/youthful-gauss-d9e0ab`; result v1.25 §2. Under the canon-first rule, governing canon is `main`'s, so 2.11 governs once #660 merges. Until then, `main` has v13.6.1. |
| D-3 | **Settled by 2.11.** "The rules apply immediately to the remaining HDE-CRD-0002 units." The business-case work for WU-PR-07 and the S01 real-input fact for WU-PR-08 are owned by the Product Owner, before their PR-10s. | 2.11, "Epic, task, and status effects" and "Deferred obligations and unresolved work" |
| D-4 | **Adopted.** Nathan, 2026-10-20: "make the d4 changes in a new PR". The §12 rule is added to AGENTS.md "Code review guidelines". This is also one of 2.11's "Required canon drainage" targets. | amthorn78/glow-hdengine-v2#661, `AGENTS.md` commit `2b8eb9c` |
| D-5 | **Routed.** Nathan, 2026-10-20: "send the d5 findings to the GCPFE modification backlog in notion". §11 is recorded as MB-013 to MB-019. Before writing, each target's 100926.1 body was read in full, as was `glow-hde-pr-development` 1.4.0. None has a business-case, real-input, repeated-finding or spend rule. These are the prompt changes 2.11 lists as deferred obligations for `GCFPE-MGMT-10`. | GCFPE Modification Backlog (Notion `3e54590a05eb81eb818fd0f42045167a`), MB-013 to MB-019, read back after writing |
| D-1 | **Open.** WU-PR-06's fate. 2.11: "Its disposition is the Product Owner's decision and is not made by this addendum." | — |

## 18. Observation: addendum 2.11's rule cross-references use this record's old numbering

Addendum 2.11 numbers its rules 1 to 8:

| 2.11 rule | Content | This record's rule |
| :- | :- | :- |
| 1 and 2 | business case | R-1 |
| 3 | gates | R-2 |
| 4 and 5 | real inputs | R-3 |
| 6 | no emulation | R-4 |
| 7 | finding disposition | R-5 |
| 8 | repeated finding class | R-6 |

Eleven cross-references inside 2.11 still use this record's R-numbers, so they point at the wrong rule. Line numbers below count from 2.11's heading (line 1,181 of `PF10-HDE-Build-Notes-v13.6.2.md` at `b0e2299`).

| 2.11 line | Text | Points at | Meant |
| :- | :- | :- | :- |
| 32 (rule 7) | "on a real input (rule 3)" | rule 3, gates | rule 4 |
| 41 (Scope) | "stays a fix under rule 5" | rule 5, constructed input | rule 7 |
| 75 (Effect) | "rule 4 would have led the PR-20 plan to the pin" | rule 4, real inputs | rule 6 |
| 75 (Effect) | "rule 6 would have tripped at round 2" | rule 6, no emulation | rule 8 |
| 80 (Effects) | "screen of them under rules 1 and 3" | rule 3, gates | rules 1 and 4 |
| 80 (Effects) | "open for S01 on rule 3" | rule 3, gates | rule 4 |
| 92 (Drainage) | "Add the rule 5 disposition" | rule 5, constructed input | rule 7 |
| 92 (Drainage) | "and the rule 6 trigger" | rule 6, no emulation | rule 8 |
| 97 (Deferred) | "constructed input (rule 3)" | rule 3, gates | rules 4 and 5 |
| 97 (Deferred) | "the rule 6 trigger is added" | rule 6, no emulation | rule 8 |
| 113 (Relationship) | "its findings are read under rule 5" | rule 5, constructed input | rule 7 |

**Effect.** Each rule's title makes the intended meaning recoverable. Still, an agent following rule 7's "(rule 3)" reaches the gates rule rather than the definition of a real input, and a `GCFPE-MGMT-10` run taking the deferred prompt changes reads two wrong rule numbers.

**Disposition.** PF canon is read-only to agents, so this record changes nothing. #660 is not merged, so a corrected PF10 file from the Product Owner, committed at his direction like `b0e2299`, would fix all eleven before they reach `main`.

**Nonclaims.**
- This record changes no canon, prompt, skill or AGENTS.md.
- It approves nothing and establishes no QA, acceptance, merge or closure.
- It is not the PR-40 lineage review.
