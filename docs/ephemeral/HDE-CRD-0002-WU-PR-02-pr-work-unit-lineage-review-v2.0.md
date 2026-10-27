---
artifact_type: PR_WORK_UNIT_LINEAGE_REVIEW
artifact_id: HDE-CRD-0002-WU-PR-02-PR-WORK-UNIT-LINEAGE-REVIEW
artifact_version: "2.0"
decision: ACCEPT
predecessor: docs/ephemeral/HDE-CRD-0002-WU-PR-02-pr-work-unit-lineage-review-v1.0.md (v1.0, REJECT on LR-1; blob d2336fb0e952; landed at ef3972b, #635; preserved unchanged)
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-02
work_unit_title: "Evidence tooling: attestation on Debian, closure probe, engine-core currency, Mirror labels, CRD admission (PR; Distillation; S06, S11, S12, S13, S22)"
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-02-pr-instruction-v1.0.md (v1.0, INSTRUCTION_READY; blob b98bf846287d)
PR_IMPLEMENTATION_PLAN_ID: cycle 1 docs/ephemeral/HDE-CRD-0002-WU-PR-02-pr-implementation-plan-v1.0.md (Proceeded; spent); cycle 2 docs/ephemeral/HDE-CRD-0002-WU-PR-02-pr-implementation-plan-v2.0.md (the corrective plan; blob 49d7a9920813; Proceeded)
PR_30_RESULT_ID: cycle 1 docs/ephemeral/HDE-CRD-0002-WU-PR-02-pr-implementation-result-v1.0.md; cycle 2 docs/ephemeral/HDE-CRD-0002-WU-PR-02-pr-implementation-result-v2.0.md (PR_CANDIDATE_PUBLISHED; blob 3ff4c3209540)
PR_35_RESULT_ID: cycle 1 docs/ephemeral/HDE-CRD-0002-WU-PR-02-pr-implementation-result-v1.4.md; cycle 2 docs/ephemeral/HDE-CRD-0002-WU-PR-02-pr-implementation-result-v2.1.md (blob 7a08b4ee28fc) and v2.2.md (blob d0a0fdb58a54), MERGE_PENDING; historical pre-merge evidence
PR_REFS: amthorn78/glow-hdengine-v2#634 (cycle 1, merged as 1d2c834) → amthorn78/glow-hdengine-v2#637 (cycle 2, LR-1 correction, merged as b26f44f)
entry_event: MERGE_OBSERVED for #637, delivered by the cycle-2 PR-35 session in the pasted handoff (no saved MERGE_OBSERVED artifact; NOT PRODUCED); merge verified independently (§3)
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
reviewer: the continuing whole-change HDE-CRD-0002 Implementation Agent, read-only PR-40 role; session https://claude.ai/code/session_01CCKsYD2yX5WgU3biWKb59j, the session of review v1.0
pr_sessions: cycle 1 PR-20/PR-30 https://claude.ai/code/session_01KTTzbrYjNwVoPN3AtpbN4a, PR-35 https://claude.ai/code/session_01QSP8xruxWCLpDqBGVVFiSK; cycle 2 PR-20/PR-30 https://claude.ai/code/session_014BSjYENRE9rSuw6D7QZs8A, PR-35 https://claude.ai/code/session_01LWQj7qeWSWF1rQ2A4NDZ8o
approved_lineage: Specification docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (v1.1); Implementation Audit docs/ephemeral/HDE-CRD-0002-implementation-audit-v1.0.md (v1.0); Implementation Plan docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (v1.1); Plan review docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (v1.1, IA-30 INITIAL_APPROVE)
return_owner: the same continuing whole-change HDE-CRD-0002 Implementation Agent
prompt: PR-40 — Review PR Work-Unit Lineage — 100926.1 (https://app.notion.com/p/3f44590a05eb81088487e918fd642a7f; page state as of 2026-10-12T02:29:38Z; read in full for review v1.0, applied again here)
prompt_release: GCFPE-20261009.1 / 100926.1
created_at: 2026-10-14T00:01:20Z
repository_state_reviewed: origin/main b26f44fa920b52f431a26d8087da43796ee20cd3 (tree 986c7e152047); no commit after it at review time
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.5.md (v13.5.5; blob c98831e8112d; unchanged since review v1.0; addenda 2.1 to 2.4)
pf10_addendum_created: none (PR-40 is not a qualifying approval prompt)
canon_conflict_register: CR-1, CR-2, CR-3 APPROVED_AS_CHANGED (Thoth); CR-4 APPROVED and CR-5 APPROVED_AS_CHANGED (Product Owner, docs/ephemeral/HDE-CRD-0002-WU-PR-01-po-disposition-cr-4-cr-5-v1.0.md); no new entry
next_prompt: PR-10 — Create PR Work-Unit Instructions — 100926.1 (https://app.notion.com/p/3f44590a05eb815d97d5f3930c7d3e8a), for WU-PR-03
---

# HDE-CRD-0002 WU-PR-02 — PR work-unit lineage review v2.0 (PR-40, plan cycle 2)

## 1. Decision

**ACCEPT.** WU-PR-02 is delivered with sufficient attributable evidence across its ordered lineage #634 → #637.
- Review v1.0 established every obligation of the unit except LR-1, and that evidence still holds: since `1d2c834` no file outside `docs/ephemeral/` changed except `tests/evidence/test_hdapi_v2_contract_inventory.py` (§2).
- #637 closes LR-1 exactly as review v1.0 §8 bounded it: four test-only lines, no tool, CI, catalog, member or governed-artifact change.
- Cycle 2 raised no review finding. The final head's CI is green on its classified lanes. Nothing remains unresolved inside the unit.

ACCEPT is this review's lineage result only. It is not QA, acceptance of HDE-CRD-0002, Ops, PF09/PF30 movement, release activation, merge authority or closure. No second acceptance receipt exists for this unit.

## 2. What was re-examined, and what is reused

PR-40 step 9: review v1.0 was re-read in full. Its §3 to §6 evidence on #634 is reused because `git diff 1d2c834 b26f44f`, excluding `docs/ephemeral/` and the corrected test file, is empty. In particular `tools/`, `ci/`, `.github/`, `catalog/`, every release member and every governed Index/Mirror artifact are byte-identical to `1d2c834`.

New for this cycle: #637's merge, attribution, change, local validation, hosted CI and review; plan v2.0 and results v2.0 to v2.2; the closure of LR-1.

## 3. Merge state and landed lineage

| Fact | Evidence |
| :- | :- |
| #637 merged | GitHub: `merged=true`, `merged_by amthorn78`, `merged_at 2026-10-13T23:52:58Z`, base `5e39ee2fcd84a76dfc6c96b6b477e9ea7431e2d1`, head `b3c85147e94a17b315ef0199b90a41219024012b`, 4 commits, 4 files, +472 |
| Method | SQUASH. `b26f44f` has one parent, `5e39ee2`; `b26f44f^{tree}` = `b3c8514^{tree}` = `986c7e1520470b062302c2323b3f1bfed1cda88e`; `5e39ee2` is an ancestor of `b3c8514` |
| #637 commits | `c8ac4ef` (C-1, the test) → `daf544a` (result v2.0) → `b5cae05` (result v2.1) → `b3c8514` (result v2.2) |
| #634 | merged as `1d2c834` (review v1.0 §3), an ancestor of `b26f44f` |
| Interstage commits | `ef3972b` (#635: review v1.0) and `5e39ee2` (#636: plan v2.0), both `docs/ephemeral/` only. Classified as non-lineage committed divergence (review and plan records), outside the attributable delta |
| Later divergence | none: `origin/main` = `b26f44f` |
| Attributable landed delta | #634: as review v1.0 §3 (EXACT). #637: `tests/evidence/test_hdapi_v2_contract_inventory.py` (+4) and results v2.0, v2.1, v2.2 (new). The direct delta equals the landed delta (identical trees). The code tree of `b26f44f` outside `docs/ephemeral/` equals that of `c8ac4ef`, the commit PR-30 validated |

**Merged-change attribution.** The `glow-merged-change-attribution-lock` collector ran for #634 in review v1.0 (EXACT, VALIDATED). It was not re-run for #637. #637's attribution is native: base ancestry, a single-parent squash, and equal head and landing trees, which is the skill's EXACT condition for a squash. No item is unproven.

## 4. The correction (LR-1) and its proof

**The landed change** equals plan v2.0 §6.1. Four lines were inserted in `test_epic034_pr04_superseded_rows_are_removed_when_outputs_absent`, after the `HUMAN_INDEX` monkeypatch:
- a two-line comment;
- a well-formed fixed label;
- `monkeypatch.setattr(indexer, "_current_release_label", lambda: label)`.

`ROOT`, the stale rows and the assertion are unchanged. This stays within review v1.0 §8 item 1:
- it is test-only;
- the updater's manifest refusal (CX-3) and label semantics (CX-1, IF-7) are untouched;
- it uses the same seam that the updater's own label test stubs.

**By this review**, on `b26f44f`, in a detached worktree of a scratch clone (CPython 3.12.3 with CI's install, pytest 8.4.2, `ruby` at `/usr/local/bin/ruby`, closed rails, `PYTHONPATH` = the worktree):

| Check | Result |
| :- | :- |
| The LR-1 test alone | 1 passed, exit 0. Review v1.0 §5 recorded 1 passed at `0cd7b84` and 1 failed at `c27c5e8` and `1d2c834` |
| The classifier's two changed-test targets: `tests/evidence/test_hdapi_v2_contract_inventory.py` and `tests/evidence/test_http_reader_ci_ownership.py` | 304 passed, exit 0; tree clean |
| Negative control: in the worktree, the `EPIC034_PR04_SUPERSEDED_INDEX_KEYS` exclusion in `_load_human_index` replaced by an empty set | the LR-1 test **fails**, exit 1, so it still checks supersession. File restored; status empty |

**By PR-30**, on `c8ac4ef`, whose code tree equals `b26f44f`'s (result v2.0 §4):
- LR-1 test: before 1 failed, after 1 passed; negative control failed as intended.
- Classifier: `lanes=evidence`, 2 targets.
- Changed-test step: 304 passed.
- All 24 updater-consuming test files: 1,406 passed.
- Evidence-lane checks: 0; evidence-lane tests: 130 passed.
- Release-lane set: 79 passed.
- Updater fixed point; governed files, tools, CI and catalog byte-identical to the base.
- Full `tests/` sweep: **4,529 passed, 3 skipped, 2 xfailed, 0 failed**. Review v1.0's sweep at `1d2c834` had 1 failed and 4,528 passed; the only difference is LR-1.

**Hosted CI.** The final head is `b3c8514`, whose tree is the merged tree.

| Run / job | Result |
| :- | :- |
| 38485717043 / 115598738558 | success, 23:40:59Z–23:47:35Z. The job log shows CHANGED_TESTS and EVIDENCE success and PRODUCT, COMPAT, DB, RAILS, QA and RELEASE skipped as classified, and it prints `CI_APPLICABILITY_AND_EXACT_HEAD_OK` |
| Earlier heads `daf544a` (38480660131) and `b5cae05` (38484682160) | success with the same lanes (results v2.1 §4, v2.2 §3) |
| `c8ac4ef` (38480619137) | cancelled, superseded |
| Post-merge push run 38486912140 on `b26f44f` | in progress at review time; not relied on |

**Codex code review.** The summary comment 6156901666 reads "Code Review Completed 2026-10-13T23:42:21Z" on `b3c8514`, trigger "New commits". GitHub shows 0 formal reviews and 0 review threads on #637; no finding was raised. The Codex security review is not part of the chain (PF10 addendum 2.3) and is not a gap.

## 5. Record corrections in cycle 2

Result v2.2 §2 corrects two statements of v2.0 and v2.1, both against hosted evidence:
- A record commit on #637 still selects the evidence lane, because the classifier compares base to head.
- A Codex review ran automatically on `b5cae05`.

The earlier records stay unchanged, as required. Neither statement affects the unit's delivery.

## 6. Requirement coverage across the work unit

All MET:
- **Requirements and acceptance.** S06, S11, S12, S13 and S22, with Plan v1.1 §7 acceptance items (1) to (5) (review v1.0 §6; unchanged by #637).
- **Obligations.** ID-1, ID-2 and PD-7; contracts D-1 to D-5; exclusions; security; migration; evidence obligations; PR descriptions; the carried K-2.
- **The S03 outcome across units.** NOT MET in review v1.0; now MET: the full sweep is clean (§4).
- **The plan's risk "Mirror consumers rejecting added fields".** Every updater-consuming test file passes (1,406).
- **The corrective scope** (review v1.0 §8 items 1 to 3 and its validation list): delivered and proven (§4). No updater change was needed, because the test-only correction keeps the test's intent. No classifier change (plan v2.0 PD-13).
- **#637's PR description.** It carries the template headings, the checks with counts, the D21-C statement and the nonclaims, and it claims nothing of #634's as its own.
- **Recovery.** None open. IF-35-1 (cycle-2 PR-35 records pushed to #637's branch) is a recorded vehicle decision with read-back.

## 7. Findings

- **LR-1:** closed by #637 (§4).
- **No new finding.**
- **Observations LR-O1, LR-O2 and LR-O3** (review v1.0 §7) stand with the IA as owner. The IA carries them into the WU-PR-03 instruction and the later member-changing and updater-changing instructions:
  - LR-O1: the CX-2 residual, the label is not owner proof, and the correction of the IA's advice.
  - LR-O2: run every updater consumer on an updater change.
  - LR-O3: the updater cannot run between a member change and the cut; the new label timing; a stale label on a byte-stable capture.
- **Carried observations:** OBS-W2-1 and OBS-W2-2 (WU-DOC-01); OBS-W2-3 (observation only); OBS-17 (`tests/qa/test_generate_epic_close_pack.py` passed locally in both cycles; QA tool and test owner through the IA); AQ-1 (WU-PR-07 only); PF10 addendum 2.2's items (the WU-PR-03 and WU-PR-06 instructions).
- **O-6 partial update** (result v2.1 §4): `ruby` is present on the hosted `ubuntu-24.04` runner (image 20261004.327.1), because the contract-inventory file passed. Its version is still unprinted.

## 8. CANON_CONFLICT_REGISTER

CR-1, CR-2, CR-3: APPROVED_AS_CHANGED (Thoth, Specification lineage). CR-4: APPROVED (Product Owner, `docs/ephemeral/HDE-CRD-0002-WU-PR-01-po-disposition-cr-4-cr-5-v1.0.md` §2). CR-5: APPROVED_AS_CHANGED (Product Owner, same record §3).

No new conflict: cycle 2 changed one test and three records and no canon. The `CX-<n>` labels are review-finding identifiers, distinct from this register.

## 9. NOT PRODUCED, NOT EXECUTED and pending values

- **NOT PRODUCED:** a saved MERGE_OBSERVED artifact for #637; any QA, Ops, acceptance or closure artifact; a PF10 addendum.
- **NOT EXECUTED by this review:** a second full `tests/` sweep on `b26f44f`. PR-30 ran it on the identical code tree `c8ac4ef`, and this review ran the LR-1 test, its changed-test targets and a negative control on `b26f44f`. The attribution collector for #637 (native attribution, §3). The Codex security review (deprecated).
- **Pending, not relied on:** post-merge push CI run 38486912140 on `b26f44f`.
- **Prompt-use provenance:** the installed writer is absent; usage is recorded in §12 only (pending, non-gating).

## 10. Next approved Plan stage

**WU-PR-03 → PR-10 — Create PR Work-Unit Instructions — 100926.1**, by this whole-change IA.
- **Basis.** Implementation Plan v1.1 §7 order: WU-PR-01 → WU-PR-02 → **WU-PR-03** → … WU-PR-03 is "Public, dev and CLI surfaces (PR; Conjunction)", an ordinary PR unit.
- **Dependencies.** "Third; after WU-PR-01 (registered owners …) and WU-PR-02 (label model before rows are regenerated)". Both are now accepted: WU-PR-01 by lineage review v2.0 (PF10 addendum 2.4), WU-PR-02 by this review.
- **No added prerequisite.** Addendum 2.2's downstream items belong to the WU-PR-03 instruction, addendum 2.3 sets the reviewer chain, and addendum 2.1 governs readings. AQ-1 gates only WU-PR-07's merge (Plan v1.1 §13).
- **No existing instruction.** No `HDE-CRD-0002-WU-PR-03-*` file exists on `main`.

**Carried into the WU-PR-03 instruction by its author, from the records:**
- LR-O1 and LR-O3 (review v1.0 §7), stated against Plan v1.1 §10.
- LR-O2, if WU-PR-03 touches the updater.
- PF10 addendum 2.2's WU-PR-03 items.
- OBS-17 as a qa-lane CI risk.
- O-6.

## 11. TypeSafe reading for the receiving session (PR-10, WU-PR-03)

Action sent (v6): "Write, as the whole-change implementation agent, one self-contained PR work-unit instruction for the third of ten planned units of an approved 22-requirement change: public, dev and CLI surface corrections (a not-found envelope on two web app factories, a dev route environment gate, a CLI help summary, removal of a dev harness, an endpoint catalog and its validator, and several operator documents) that change release members and so carry a same-version release manifest refresh and a twelve-step evidence convergence under the release-label model the previous unit just landed, re-verifying the repository baseline, the members and governed evidence writers the unit touches, its interfaces with later units, and the obligations carried from three earlier lineage reviews and a build-notes addendum, including how the new label timing and manifest refusal change the convergence order. No code is written and no live run occurs; a per-PR plan, Product Owner Proceed, implementation, review and lineage review follow."

- **TypeSafe v6: Opus 5.5, extra high.** Effort score 2.64 (confidence 0.69); rung probabilities low 0.00, medium 0.03, high 0.36, extra high 0.56, max 0.05, ultracode 0.00. Model probabilities Fable 5.1 0.21, Opus 5.5 0.79 (confidence 0.58). Twelve cells, computed from the two answers: Opus 5.5 at low 0.00, Opus 5.5 at medium 0.02, Opus 5.5 at high 0.28, Opus 5.5 at extra high 0.44, Opus 5.5 at max 0.04, Opus 5.5 at ultracode 0.00, Fable 5.1 at low 0.00, Fable 5.1 at medium 0.01, Fable 5.1 at high 0.08, Fable 5.1 at extra high 0.12, Fable 5.1 at max 0.01, Fable 5.1 at ultracode 0.00. Sent 2026-10-14T00:01:13Z. Nathan picks the cell.
- **Detail:** v6 sent 2026-10-14T00:01:13Z; HTTP 200 in 0.65 s; 4305 input and 54 output tokens; jev-1.13.0. Rung by rule: extra high (nearest to the score, halves up); model by rule: Opus 5.5 (P(most capable) 0.5 or more is Fable 5.1). Flags: none.
- **Notion row:** not written, as PR-40 directs. **Nathan's pick for PR-10:** not stated. **For this PR-40 session:** not stated (reading in result v2.1 §10). Review v1.0 §12 recorded an earlier PR-10 (WU-PR-03) reading as superseded and not used; this reading replaces it.

**Surface advice:** run PR-10 in the continuing whole-change HDE-CRD-0002 IA context, as a top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2` with Notion read access for the prompt. It needs:
- `docs/pfcanon/` and the HDE-CRD-0002 records on `main`;
- the WU-PR-03 surfaces: `adapter/factory.py`, `adapter/http_reader.py`, `engine/cli/main.py`, `tools/evidence/generate_a7_transport_proofs.py`, the endpoint catalog and its validator, `scripts/dev_start_reader.sh`, `VERIFY.sh` and `dev/reader_harness/`.

Re-measuring the baseline or rehearsing the re-cut convergence needs a Python 3.12 environment with CI's install, which needs package-index access. No live vendor, production or database access is needed. It writes only its instruction under `docs/ephemeral/`. This review's pull request should be merged first.

## 12. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / WU-PR-02 / PR-40 / lineage review 2 (plan cycle 2) |
| change / specification | CRD HDE-CRD-0002 / `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` v1.1 |
| work unit | WU-PR-02 (S06, S11, S12, S13, S22) |
| release | GCFPE-20261009.1 / 100926.1 |
| prompt | PR-40 — Review PR Work-Unit Lineage — 100926.1, https://app.notion.com/p/3f44590a05eb81088487e918fd642a7f (page state as of 2026-10-12T02:29:38Z) |
| role/stage | continuing whole-change IA / PR-40 |
| capture time | 2026-10-14T00:01:20Z |
| execution identity | https://claude.ai/code/session_01CCKsYD2yX5WgU3biWKb59j |
| inherited usage | review v1.0 §13; cycle 2: PR-20 plan 2, PR-30 implementation 2, PR-35 review resolution 2 (results v2.0 §11, v2.1 §11) |
| repository persistence | recorded here only (writer absent; pending, non-gating) |

## Canon relied on

Read on `main` at `b26f44f`; `docs/pfcanon/` is unchanged since `cc3dc33` (`git diff 1d2c834 b26f44f -- docs/pfcanon` is empty).

| Decision topic | Sources and sections |
| :- | :- |
| Review authority, re-review and verdict | PR-40 — Review PR Work-Unit Lineage — 100926.1 ("Execute" steps 1–10, step 9 reuse of the prior review; "Required result"; "Resolve the next approved Plan stage"; "Accepted-final lineage protection"); HDE Governance (`docs/pfcanon/PF04-Canon-HDE-Governance-v2.8.7.md`) §9.1.1 (Proceed per detailed PR plan; PR merges remain Product Owner actions) and §9.1.2 (canon on `main`; in-flight documents and Product Owner dispositions govern within their scope) |
| Review chain | PF10-HDE-Build-Notes v13.5.5 addendum 2.3 Rules 1–5; addendum 2.4 (precedent for a corrective-cycle ACCEPT and for the next-stage basis; K-2, OBS-17, O-6) |
| LR-1 closure and the unit's obligations | review v1.0 §6 to §8; HDE Schemas & Artifacts (`docs/pfcanon/PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.6.md`) §6.2 and §8.3 as read for review v1.0 (the label semantics and refusal #637 leaves unchanged); Specification v1.1 row S03; Implementation Plan v1.1 §7 (WU-PR-02 risks) |
| Next stage | Implementation Plan v1.1 §7 order and the WU-PR-03 block ("Dependencies and order"), §13 (AQ-1); PR instruction v1.0 §12 ("on ACCEPT, issues the next unit's instruction (WU-PR-03)") |
| TypeSafe reading | PF10 addendum 2.1 |
| Operative documentation | `AGENTS.md` (canon-first rule; evidence attribution; closed rails; pytest readiness; PR descriptions) |

In-flight records read: lineage review v1.0; plan v2.0 (§1 to §12); results v2.0, v2.1, v2.2 in full.
