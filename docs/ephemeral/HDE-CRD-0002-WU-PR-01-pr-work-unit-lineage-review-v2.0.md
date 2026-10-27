---
artifact_type: PR_WORK_UNIT_LINEAGE_REVIEW
artifact_id: HDE-CRD-0002-WU-PR-01-PR-WORK-UNIT-LINEAGE-REVIEW
artifact_version: "2.0"
decision: ACCEPT
predecessor: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-work-unit-lineage-review-v1.0.md (v1.0, REJECT on LR-1; blob 2cfbb5ec33d8; landed at dc701f2, #628; preserved unchanged)
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-01
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-instruction-v1.0.md (v1.0, INSTRUCTION_READY)
PR_IMPLEMENTATION_PLAN_ID: cycle 1 docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-plan-v1.1.md (Proceeded; spent); cycle 2 docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-plan-v2.0.md (the corrective plan; Proceeded)
PR_30_RESULT_ID: cycle 1 docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-result-v1.0.md; cycle 2 docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-result-v2.0.md (PR_CANDIDATE_PUBLISHED)
PR_35_RESULT_ID: cycle 1 docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-result-v1.15.md; cycle 2 docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-result-v2.1.md (MERGE_PENDING; historical pre-merge evidence)
PR_REFS: amthorn78/glow-hdengine-v2#627 (cycle 1, merged as 7136040) → amthorn78/glow-hdengine-v2#630 (cycle 2, LR-1 correction, merged as bf7ad8c)
entry_event: MERGE_OBSERVED for #630, delivered by the cycle-2 PR-35 session in the pasted handoff (no saved MERGE_OBSERVED artifact; NOT PRODUCED); merge verified independently below
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
reviewer: the continuing whole-change HDE-CRD-0002 Implementation Agent, read-only PR-40 role (instruction v1.0 §12); session https://claude.ai/code/session_01CCKsYD2yX5WgU3biWKb59j, the session of review v1.0
pr_sessions: cycle 1 PR-30 https://claude.ai/code/session_011q4bUbzJCYk2KAF7eAceF8, PR-35 https://claude.ai/code/session_013LyxHxzJP2ohvmmNFamZt2; cycle 2 PR-20/PR-30 https://claude.ai/code/session_012kGFYdD1BYJnXh3TagQetg, PR-35 https://claude.ai/code/session_019rRACrhsBBtEbBGujNsEbR
return_owner: the same continuing whole-change HDE-CRD-0002 Implementation Agent
prompt: PR-40 — Review PR Work-Unit Lineage — 100926.1 (https://app.notion.com/p/3f44590a05eb81088487e918fd642a7f)
prompt_release: GCFPE-20261009.1 / 100926.1 (GCFPE Membership and Release Register, "Current selection — GCFPE-20261009.1 / 100926.1"; read 2026-10-13 for this review)
created_at: 2026-10-13T14:19:56Z
repository_state_reviewed: origin/main bf7ad8cf2a9a42d28d74ef4ffceb3f0cdb0cede8 (tree d04d3cf95c4d); no commit after it at review time
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.4.md (v13.5.4; unchanged since review v1.0; addenda 2.1, 2.2, 2.3)
pf10_addendum_created: none (PR-40 is not a qualifying approval prompt)
canon_conflict_register: CR-1, CR-2, CR-3 APPROVED_AS_CHANGED (Thoth); CR-4 APPROVED and CR-5 APPROVED_AS_CHANGED (Product Owner, docs/ephemeral/HDE-CRD-0002-WU-PR-01-po-disposition-cr-4-cr-5-v1.0.md); no new entry
next_prompt: PR-10 — Create PR Work-Unit Instructions — 100926.1 (https://app.notion.com/p/3f44590a05eb815d97d5f3930c7d3e8a), for WU-PR-02
---

# HDE-CRD-0002 WU-PR-01 — PR work-unit lineage review v2.0 (PR-40, plan cycle 2)

## 1. Decision

**ACCEPT.** The complete work unit WU-PR-01 is delivered with sufficient attributable evidence across its ordered lineage #627 → #630:
- Review v1.0 established every obligation of the unit except LR-1. That evidence still holds: no file #627 landed has changed since, other than the one test file #630 extends (§3).
- #630 closes LR-1 exactly as review v1.0 §10 bounded it. The record corrections it carries close LR-2 and LR-3.
- Cycle 2 raised no review finding, its final-head CI is green on all seven lanes, and nothing remains unresolved inside the unit.

ACCEPT is this review's lineage result only. It is not QA, acceptance of HDE-CRD-0002, Ops, PF09/PF30 movement, release activation, merge authority or closure. No second acceptance receipt exists for this unit.

## 2. What was re-examined, and what is reused

PR-40 step 9: review v1.0 was inspected in full. Its evidence on #627 (§3 to §5 of v1.0) remains valid and is reused, because:
- `git diff 7136040 bf7ad8c` outside `docs/ephemeral/` changes only `tests/evidence/test_rails_ci_workflow_integration.py` (+19 lines, a new function; no existing line changed);
- `docs/pfcanon/` and every other code, workflow, classifier, tool and test file are byte-identical to `7136040`.

New for this cycle: #630's merge, attribution, change, local validation, hosted CI and review; the corrective plan v2.0 and results v2.0/v2.1; the closure of LR-1, LR-2 and LR-3.

## 3. Merge state and landed lineage

| Fact | Evidence |
| :- | :- |
| #630 merged | GitHub: `merged=true`, `merged_by amthorn78`, `merged_at 2026-10-13T14:17:02Z`, base `afc333e`, head `1cbb2edb6345327aeb4e9da0140a704c87476709`, 3 commits |
| Method | SQUASH. `bf7ad8c` has one parent, `afc333e`; `bf7ad8c^{tree}` = `1cbb2ed^{tree}` = `d04d3cf95c4dc7e4420c0aa3600ec4fb58e421ee`; `afc333e` is an ancestor of `1cbb2ed` |
| #630 commits | `1ae422d` (C-1, the test), `b3645b9` (result v2.0), `1cbb2ed` (result v2.1) |
| #627 | merged as `7136040` (review v1.0 §3, re-confirmed: an ancestor of `bf7ad8c`) |
| Interstage commits | `dc701f2` (#628: review v1.0 and the CR-4/CR-5 disposition) and `afc333e` (#629: plan v2.0), both `docs/ephemeral/` only. Classified as non-lineage committed divergence (review and plan records), outside the attributable delta |
| Later divergence | none: `origin/main` = `bf7ad8c` |
| Attributable landed delta | #627: as review v1.0 §3 (EXACT). #630: `tests/evidence/test_rails_ci_workflow_integration.py` (+19), results v2.0 and v2.1 (new); direct delta equals landed delta (identical trees) |

**Merged-change attribution.** The `glow-merged-change-attribution-lock` collector was run for #627 in review v1.0 (EXACT, VALIDATED). It was not re-run for this cycle. The #630 attribution above is native: base ancestry, single-parent squash, and tree equality of head and landing commit, which is the skill's EXACT condition for a squash. No unproven item.

## 4. The correction (LR-1) and its proof

| Check | Result |
| :- | :- |
| Landed test = plan v2.0 §6.1 | identical text: `test_inactive_test_refusal_rejects_a_synthetic_inactive_path`, inserted after line 1156; the existing loop unchanged |
| Run on `bf7ad8c` (scratch clone, Python 3.12.3, CI's install, closed rails) | integration file **138 passed** (137 at `7136040`); the new test alone: 1 passed |
| Negative control (this review) | with the refusal at `ci/checks/classify_ci_changes.py` line 1533 replaced by `pass` in the scratch clone, the new test **fails**; classifier restored; clone `git diff` clean |
| Plan v2.0 §10 local validation (result v2.0 §5; v2.1 §4) | citations and env-pins exit 0; rails lane as `ci.yml` runs it, 138 passed; changed-test step 3,264 passed with a clean tree; classifier dry run seven lanes, 163 targets; `release_id_recompute.py --check-manifest-only` exit 0; diff against base = the test file only |
| Hosted CI, final head `1cbb2ed` | check `test`, run 38409638847: **success** (14:00:19Z → 14:14:23Z). The applicability step shows `PRODUCT`, `COMPAT`, `DB`, `RAILS`, `EVIDENCE`, `QA`, `RELEASE` true and success, and prints `CI_APPLICABILITY_AND_EXACT_HEAD_OK` (read from job 115338249358) |
| Earlier cycle-2 runs | 38406204161 on `1ae422d` cancelled by `cancel-in-progress`; 38406489803 on `b3645b9` success, rails lane 138 passed (result v2.1 §3) |
| Post-merge push CI on `bf7ad8c` | run 38412030631: in progress at review time; not relied on |
| Codex code review | final head `1cbb2ed` completed 2026-10-13T14:01:38Z (summary comment 6146788079); 0 reviews, 0 threads, 0 findings across the PR |
| Codex security review | not part of the chain (PF10 addendum 2.3); not a gap |

## 5. Record corrections (LR-2, LR-3)

Result v2.0 §6 corrects all three statements review v1.0 named, from a fresh GitHub Actions read of the 17 cycle-1 runs:
- LR-2: no inactive-refusal test was added in cycle 1; #630 adds it.
- LR-3 (a): run 38336691078 on `bb0f85c` concluded success at 02:35:56Z and was neither superseded nor cancelled.
- LR-3 (b): the runs on `26140fe` and `e13516b` were cancelled; the close-pack statement holds only for the six completed heads.

These values equal what this reviewer's evidence workers read in cycle 1 (review v1.0 §4). The historical records and #627's description stay unchanged, as review v1.0 §10 required.

## 6. Requirement coverage across the work unit

| Obligation | Status |
| :- | :- |
| S03, S04, S05; whole-change Plan acceptance (1) to (5) | MET (review v1.0 §5; unchanged by #630; (5) re-shown on `1cbb2ed`) |
| Deliverables (instruction §6; plan v1.1 §8), including the plan v1.1 §5.4/§5.5/§8 synthetic inactive-refusal case | MET; the last item by #630 |
| Interface contracts C-1 to C-6; disposition rules; exclusions; addendum 2.2 bounds; security (instruction §11; addendum 2.3 Rule 3); migration; nonclaims | MET (review v1.0 §5; #630 changes none of them: no classifier, workflow, tool, member, governed-artifact or canon change) |
| Corrective scope (review v1.0 §10; plan v2.0 §5) | MET: C-1 and C-2 exactly; no other file |
| Evidence obligations (plan v2.0 §12) | MET (result v2.0: recovery, base, change, checks with counts, ruby 3.3.6, corrections, register, nonclaims) |
| PR description (`AGENTS.md`) | #630: template headings, checks with counts, D21-C statement, nonclaims; no claim of #627's as its own |
| Review and CI (instruction §12 read under addendum 2.3) | MET for both PRs |
| Recovery | none open; IF-1 (result v2.0) and IF-35-1 (result v2.1, Nathan chose "Push to #630's branch") are recorded vehicle decisions with read-back |

## 7. Findings

| ID | Status after cycle 2 |
| :- | :- |
| LR-1 | **Closed** by #630 (§4) |
| LR-2, LR-3 | **Closed** by result v2.0 §6 (§5) |
| LR-4 (R-14) | Closed by CR-4 APPROVED (Product Owner) |
| LR-5 (PF10 in an implementation PR) | Closed by CR-5 APPROVED_AS_CHANGED (Product Owner) |

No new finding. Observations O-1 to O-6 and the carried items stay with the owners review v1.0 §6 names, with one partial update: O-6's hosted `ruby` is shown present on the `ubuntu-24.04` runner (the contract-inventory file passed), its version still unprinted (result v2.1 §3).

## 8. CANON_CONFLICT_REGISTER

| ID | Status | Owner / record |
| :- | :- | :- |
| CR-1, CR-2, CR-3 | APPROVED_AS_CHANGED | Thoth (Specification lineage) |
| CR-4 | APPROVED | Product Owner, `docs/ephemeral/HDE-CRD-0002-WU-PR-01-po-disposition-cr-4-cr-5-v1.0.md` §2 |
| CR-5 | APPROVED_AS_CHANGED | Product Owner, same record §3 |

No new conflict: cycle 2 changed one test and two records, and no canon.

## 9. NOT PRODUCED, NOT EXECUTED and pending values

- **NOT PRODUCED:** a saved `MERGE_OBSERVED` artifact for #630; any QA, Ops, acceptance or closure artifact; a PF10 addendum.
- **NOT EXECUTED by this review:** the changed-test step on `bf7ad8c` (run by PR-30 on the identical code tree `63e8a69` and by hosted CI on `b3645b9`; #630 changed no file among its 163 targets); the attribution collector for #630 (§3); the Codex security review (deprecated).
- **Pending, not relied on:** post-merge push CI run 38412030631 on `bf7ad8c`.
- **Prompt-use provenance:** installed writer absent; usage kept in §12.

## 10. Next approved Plan stage

**WU-PR-02 → PR-10 — Create PR Work-Unit Instructions — 100926.1**, by the whole-change Implementation Agent.

| Check | Evidence |
| :- | :- |
| Plan order | whole-change Plan v1.1 §7: WU-PR-01 → **WU-PR-02** → WU-PR-03 → … |
| Unit type | "WU-PR-02 — Evidence tooling: attestation on Debian, closure probe, engine-core currency, Mirror labels, CRD admission (PR; Distillation)": an ordinary PR unit, so PR-10 |
| Dependencies | "Second; no code dependency on WU-PR-01; lands before WU-PR-07 … and before any member-changing unit's convergence relabels rows." WU-PR-01 is now accepted; nothing upstream is open |
| Overlays | PF10 addendum 2.2 is scoped to WU-PR-01 (its downstream items go to the WU-PR-03 and WU-PR-06 instructions); addendum 2.3 sets the reviewer chain (Codex code review, PR-35, PR-40); addendum 2.1 governs TypeSafe readings. None adds a WU-PR-02 prerequisite |
| AQ-1 | gates only WU-PR-07's merge (Plan v1.1 §13) |
| Existing instruction | none: no `HDE-CRD-0002-WU-PR-02-*` file on `main` |

Carried into the WU-PR-02 instruction by its author (the IA), from the records: the merge's effect on `tools/evidence/regenerate_identity_closure.py` selection and `tests/evidence/test_release_attestation.py` lines 617–618 (review v1.0 workers, K-2); OBS-17 as a CI risk for the qa lane; O-6.

## 11. TypeSafe reading for the receiving session (PR-10, WU-PR-02)

Action sent (v6): "Write, as the whole-change implementation agent, one self-contained PR work-unit instruction for the second of ten planned units of an approved 22-requirement change: release-evidence tooling repairs (an attestation build under Debian-patched setuptools, a root-bound closure probe, a release-identity assertion in an evidence currency test, release labels on evidence-mirror rows, and extending the canonical evidence-index updater's change admission to a second change ID), re-verifying the repository baseline, the governed evidence writers the unit touches, its interfaces with later units and the observations carried from the first unit's lineage review. No code is written and no live run occurs; a per-PR plan, Product Owner Proceed, implementation, review and lineage review follow."

- **TypeSafe v6: Opus 5.5, high.** Effort score 2.34 (confidence 0.67); rung probabilities low 0.01, medium 0.06, high 0.56, extra high 0.33, max 0.04, ultracode 0.00. Model probabilities Fable 5.1 0.12, Opus 5.5 0.88 (confidence 0.76). Twelve cells, computed from the two answers: Opus 5.5 at low 0.01, Opus 5.5 at medium 0.05, Opus 5.5 at high 0.49, Opus 5.5 at extra high 0.29, Opus 5.5 at max 0.04, Opus 5.5 at ultracode 0.00, Fable 5.1 at low 0.00, Fable 5.1 at medium 0.01, Fable 5.1 at high 0.07, Fable 5.1 at extra high 0.04, Fable 5.1 at max 0.00, Fable 5.1 at ultracode 0.00. Sent 2026-10-13T14:19:55Z. Nathan picks the cell.
- **Detail:** v6 sent 2026-10-13T14:19:55Z; HTTP 200 in 0.7 s; 4268 input and 54 output tokens; jev-1.13.0. Rung by rule: high (nearest to the score, halves up); model by rule: Opus 5.5 (P(most capable) 0.5 or more is Fable 5.1). Flags printed by the script: none.
- **Notion row:** not written, as PR-40 directs.
- **Nathan's pick for PR-10:** not stated. **For this PR-40 session:** not stated.

**Surface advice:** run PR-10 as a top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2` in the continuing whole-change IA lineage, with Notion read access. It reads `docs/pfcanon/` and the HDE-CRD-0002 records on `main`, and the files WU-PR-02 names (`tools/evidence/build_release_attestation.py`, `tools/evidence/regenerate_identity_closure.py`, `tools/evidence/update_evidence_index.py`, `tests/evidence/test_engine_core_evidence.py`, `tests/evidence/test_evidence_index_missing_state.py`). Re-verifying the Debian setuptools failure (O-10) needs the distribution-patched setuptools; the cloud container (Ubuntu 24.04.5) has `python3-setuptools` 68.1.2-2ubuntu1.2 under `/usr/bin/python3.12`, observed by this review; no live vendor, production or database access is needed. It writes only its instruction under `docs/ephemeral/`. This review's pull request should be merged first.

## Canon relied on

Read on `main` (`docs/pfcanon/` unchanged since review v1.0 at `7136040`). The canon review v1.0 relied on applies in full; for this cycle's decision topics:
- **Review authority, decision values, reuse of a prior review, next-stage resolution:** PR-40 — Review PR Work-Unit Lineage — 100926.1 (read in full in this session), "Execute" steps 1 to 10, "Resolve the next approved Plan stage", "Accepted-final lineage protection"; PF04-Canon-HDE-Governance v2.8.7 §9.1.1 and §9.1.2; PF27-Canon-Plan-Templates v2.0.5 "Source-bound review authority and exact-fix limits".
- **Merge evidence and CI scope:** PF06-Canon-Change-Process-Guide v2.5.4 §0.2 (traceability through base, head and merge; Product Owner squash; classifier lane set as sufficient CI scope); PF27 "CI lane classification and automated budget-control discipline".
- **Review chain:** PF10-HDE-Build-Notes v13.5.4 addendum 2.3 (Rules 2 and 3).
- **Work-unit scope and its overlay:** PF10 v13.5.4 addendum 2.2; the CR-4/CR-5 Product Owner disposition.
- **Operative documentation:** `AGENTS.md` (canon-first rule, evidence attribution, PR descriptions, closed rails, pytest readiness).

**In-flight documents read:** review v1.0 (own, in full); plan v2.0 §1 to §12 (header and design in full); results v2.0 §5 to §9 and v2.1 §1 to §7; the CR-4/CR-5 disposition; whole-change Plan v1.1 §7 (WU-PR-02 entry and order) and §13. Prompt: PR-40 — Review PR Work-Unit Lineage — 100926.1. Register: current-selection section.

## 12. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / WU-PR-01 / PR-40 / lineage review 2 (plan cycle 2) |
| change | CRD HDE-CRD-0002 |
| specification | `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md`, v1.1 (approved) |
| work unit | WU-PR-01 |
| release | GCFPE-20261009.1 / 100926.1 |
| prompt | PR-40 — Review PR Work-Unit Lineage — 100926.1, https://app.notion.com/p/3f44590a05eb81088487e918fd642a7f |
| role/stage | whole-change IA / PR-40 lineage review |
| capture time | 2026-10-13T14:19:56Z |
| execution identity | https://claude.ai/code/session_01CCKsYD2yX5WgU3biWKb59j |
| repository persistence | recorded here only (installed writer absent; pending, non-gating) |

**Decision: ACCEPT.**
