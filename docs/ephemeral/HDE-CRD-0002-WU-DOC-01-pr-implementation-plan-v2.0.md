---
artifact_type: PR_IMPLEMENTATION_PLAN
artifact_id: HDE-CRD-0002-WU-DOC-01-PR-IMPLEMENTATION-PLAN
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-WU-DOC-01-pr-implementation-plan-v2.0.md
artifact_version: "2.0"
artifact_state: AWAITING_PO_PROCEED
hold_label: "ASK OK? — PR IMPLEMENTATION PLAN"
plan_cycle: 2, the corrective re-plan after PR-40 REJECT (PR-20 "Re-plan entry", reject_replan)
predecessor: docs/ephemeral/HDE-CRD-0002-WU-DOC-01-pr-implementation-plan-v1.0.md (v1.0; blob b019aeea0ff3; cycle 1, Proceeded once and spent; landed as amthorn78/glow-hdengine-v2#692, squash 4c9bbfc) with its companion docs/ephemeral/HDE-CRD-0002-WU-DOC-01-pr-implementation-plan-v1.0-prototype.diff (blob ced9d9b33e19). Both are preserved unchanged. This v2.0 plans only the bounded correction; it does not restate or reopen v1.0's landed scope
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-DOC-01
DOCUMENTATION_UNIT_ID: WU-DOC-01
work_unit_title: "Final repository documentation (DOC; after WU-PR-08)"
PR_WORK_UNIT_LINEAGE_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-WU-DOC-01-pr-work-unit-lineage-review-v1.0.md (PR-40, decision REJECT, reject_replan; findings LRD-F1 and LRD-F2; bounded correction §6; blob e2329d66c645; landed by #693 as b00a26c)
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-DOC-01-pr-instruction-v1.0.md (v1.0, INSTRUCTION_READY; blob c49ff720ffd2; unchanged)
IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (v1.1; blob abffa2ccbd44; immutable) §7 WU-DOC-01, with Plan delta 01 docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-v1.1.md (P-8)
SPECIFICATION_ID: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (v1.1; blob c4802a5a7fa3), with Specification delta 01 docs/ephemeral/HDE-CRD-0002-specification-delta-v1.0.md (DELTA_APPROVE by docs/ephemeral/HDE-CRD-0002-specification-delta-review-v1.0.md)
PLAN_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (IA-30 INITIAL_APPROVE; blob 0cc0276524b2), with docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-review-v1.1.md (IA-30 DELTA_APPROVE)
IMPLEMENTATION_AUDIT_ID: docs/ephemeral/HDE-CRD-0002-implementation-audit-v1.0.md (AUDIT_COMPLETE; blob b39ac9f276db) — lineage only
cycle_1_records: PR-30 result docs/ephemeral/HDE-CRD-0002-WU-DOC-01-pr-implementation-result-v1.0.md (PR_CANDIDATE_PUBLISHED; blob 4ce4ff1d0588); PR-35 result docs/ephemeral/HDE-CRD-0002-WU-DOC-01-pr-implementation-result-v1.1.md (MERGE_PENDING, historical pre-merge evidence; blob e7893fbca6e3)
business_case_ref: docs/ephemeral/HDE-CRD-0002-WU-DOC-01-po-disposition-business-case-v1.0.md §2 (blob 28b3deb24cb9; unchanged; no ceiling, addendum 2.18)
RESCOPE_REVIEW_ID: none
REMEDIATION_REVIEW_ID: none
AUTHORING_CONTEXT: APPROVED_BASE_WITH_OVERLAYS
immutable_approved_base: Specification v1.1 (approved) → Implementation Plan v1.1 + IA-30 review v1.1 (approved) → PR instruction v1.0 (issued by the IA under DOC-10)
effective_baseline: approved base + applicable PF10 overlays — addendum 2.19 (Plan delta 01; P-8 sets the unit's scope), addendum 2.21 (routes the stale-document list to this unit), addenda 2.11 rules 4 to 8 and 2.18 (business case without ceiling; real inputs; finding disposition), addendum 2.14 (P1), addendum 2.3 (reviewer chain). Lineage review v1.0 §6 binds the corrective scope ("What the re-plan covers")
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.7.4.md (blob 1343ae09018e; 433,368 bytes; sha256 8ac9723214bd90d12f8cf723e0a1f060ddaf73bc4f91c555447de7c6016d37ff; the only PF10 file on main at b00a26c; docs/pfcanon/ last changed by e56788c)
pf10_addendum_paths: docs/pfcanon/PF10-HDE-Build-Notes-v13.7.4.md §2.11, §2.14, §2.18, §2.19, §2.21 (read in full in this session: 2.11, 2.14, 2.18, 2.21; 2.19 at P-8 and its WU-DOC-01 summary lines), and §2.3 (carried from plan v1.0)
pf10_addendum_created: none (PR-20 is not a qualifying approval prompt)
companion_prototype_diff: docs/ephemeral/HDE-CRD-0002-WU-DOC-01-pr-implementation-plan-v2.0-prototype.diff (git diff b00a26c → prototype head b313061; 1 file, +2/−2; 22 lines; 3,880 bytes; sha256 40e19bd145af12563a4385b7e7ed783f0b5c10c7c765b5ff5d25b17f006e39c3; `git apply --check` clean on b00a26c)
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
session_disposition: INITIAL_DEDICATED_ASSIGNMENT (the new dedicated WU-DOC-01 PR engineering session for plan cycle 2, created by Nathan / Product Owner)
role_session_ref: https://claude.ai/code/session_01WPAu8VRbMGFAKxrRj6WGur (PR-20 now; PR-30 after the Proceed)
author: dedicated HDE-CRD-0002 WU-DOC-01 PR engineering session (PR-20, plan cycle 2)
return_owner: the continuing whole-change HDE-CRD-0002 Implementation Agent (PR-40 after the corrective merge, then DOC-20; RS-20 for any rescope; DOC-10 for an instruction defect)
prompt: PR-20 — Create Detailed PR Implementation Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb819fbea5dcd966a750ba; page state as of 2026-10-12T02:29:47.327Z; fetched and read in full in this session)
prompt_release: GCFPE-20261009.1 / 100926.1
created_at: 2026-10-22T02:50:00Z
repository_baseline: origin/main b00a26c01e3ff1bd1e9a65b0b52cb7563d3cd889 (tree 48f7f0dd5971; #693). git diff 4c9bbfc..b00a26c adds only the lineage review under docs/ephemeral/; outside docs/ephemeral/ the tree is #692's landed tree
working_branch: claude/vigilant-johnson-x9jwdm, from b00a26c (documents under docs/ephemeral/ only)
canon_conflict_register: CR-1 to CR-8 carried unchanged, all decided; no new entry (§17)
next_prompt: PR-30 — PR Implementation Proceed — 100926.1 (https://app.notion.com/p/3f44590a05eb8148a538f5c80588db14), on Nathan's Proceed for exactly this v2.0
---

# HDE-CRD-0002 WU-DOC-01 — PR Implementation Plan v2.0 (corrective, plan cycle 2)

## 1. Result

**AWAITING_PO_PROCEED for v2.0.** This is the complete corrective plan for WU-DOC-01 after the PR-40 lineage review v1.0 returned REJECT with findings LRD-F1 and LRD-F2.

- **The work:** two sentence corrections in one file, `docs/qa_harness_pattern.md` (lines 14 and 97). Both are drafted to their exact text (§6). The companion diff carries them byte for byte; PR-30 applies it with `git apply`.
- **The sweep:** the whole page was re-read against `tools/qa/qa_harness.py` and `tools/evidence/update_evidence_index.py` at `b00a26c` for any other statement within Q-1's or A-4's subject (§5). No third stale statement in that subject was found. One stale citation outside that subject (line 120) is recorded and routed, not edited (RF-11).
- **The prototype** passed every check on a throwaway clone of `b00a26c` (§11): the six document-reading test files (**1,248 passed**, CPython 3.12.3, CI's full install), the citation check, the direct-DB contract check, the pre-push `lanes` report (`documentation_only`, one path) and `membership` (`not-member`), and only the planned path changed.
- **What stands:** everything else #692 landed stands as landed (lineage review §5, §6 "Nothing else in the ten documents is reopened").
- **#692 is landed history.** The earlier Proceed is spent. PR-30 opens a new pull request on a new branch; it never resumes, reuses or pushes to #692 or its branch `claude/sharp-carson-5ttoho`.
- **Not done here:** no implementation, publication of the correction, merge, Ops, QA, acceptance or closure.

## 2. Lineage and sources read in this session

| Source | Identity | How read |
| :- | :- | :- |
| PR-20 prompt | PR-20 — Create Detailed PR Implementation Plan — 100926.1 | fetched and read in full ("Re-plan entry"; "Execute" 1 to 10; "Required result"; "Next step and recovery"; "Save and hand off"; "Mandatory single-block handoff") |
| PR-30 prompt (receiver contract) | PR-30 — PR Implementation Proceed — 100926.1 | fetched and read in full ("Inputs"; "Product Owner Proceed and engineering boundary": "Only a PR-40 `REJECT` re-plan creates a new plan, and that plan receives its own Proceed") |
| Lineage review (REJECT) | `docs/ephemeral/HDE-CRD-0002-WU-DOC-01-pr-work-unit-lineage-review-v1.0.md` (blob `e2329d66c645`) | in full |
| PR instruction | `docs/ephemeral/HDE-CRD-0002-WU-DOC-01-pr-instruction-v1.0.md` (blob `c49ff720ffd2`) | in full |
| Plan cycle 1 | `docs/ephemeral/HDE-CRD-0002-WU-DOC-01-pr-implementation-plan-v1.0.md` (blob `b019aeea0ff3`) | in full |
| Cycle-1 PR-35 result | `docs/ephemeral/HDE-CRD-0002-WU-DOC-01-pr-implementation-result-v1.1.md` (blob `e7893fbca6e3`) | in full |
| Business case | `docs/ephemeral/HDE-CRD-0002-WU-DOC-01-po-disposition-business-case-v1.0.md` | in full |
| PF10 | `docs/pfcanon/PF10-HDE-Build-Notes-v13.7.4.md` | addenda 2.11, 2.14, 2.18 and 2.21 in full; 2.19 at P-8 and its WU-DOC-01 summary |
| The page | `docs/qa_harness_pattern.md` at `b00a26c` (120 lines; 15,816 bytes; blob `9810fb12fc49`; sha256 `ca65a899…5b051feb`) | in full |
| Code | `tools/qa/qa_harness.py` (blob `4484408aa713`), `tools/evidence/update_evidence_index.py` (blob `ad441edbea3c`), `AGENTS.md` (blob `cd549f509900`), `.github/workflows/ci.yml` install step, `docs/EVIDENCE_INDEX.md` line 62 | at the lines cited in §5 |

## 3. Business case and real inputs

- **Business case:** carried unchanged from the disposition record §2. Beneficiary: agents and operators who take repository workflow from `AGENTS.md` and `README.md`. Measure: each statement WU-DOC-01 changes matches merged `main`, checked at DOC-20. No ceiling (addendum 2.18 rule 1).
- **Why this correction serves it:** HDE-CRD-0002's own QA sessions publish through the composed writer. Line 14 tells them HDE-CRD-0002 cannot be published; line 97 gives an install that fails the CLI tests (lineage review §6).
- **Real inputs (addendum 2.11 rule 4):** the page as it stands on `main` (a), read by the next real consumer, HDE-CRD-0002's QA sessions, in the operator's shell (b). The correction depends on no constructed input.
- **Measure state carried:** the lineage review records the measure as "met for every changed statement checked, and not yet fully established" (review §5). This plan's §6 adds the two corrected statements and their proofs to the statement list DOC-20 verifies; plan v1.0 §6 remains the list for everything else.

## 4. Baseline (verified at `b00a26c`)

- `origin/main` is `b00a26c` (#693). `git diff --name-status 4c9bbfc b00a26c` lists only `A docs/ephemeral/HDE-CRD-0002-WU-DOC-01-pr-work-unit-lineage-review-v1.0.md`; `git diff --quiet 4c9bbfc b00a26c -- . ':(exclude)docs/ephemeral'` succeeds.
- `git diff a85067c b00a26c -- . ':(exclude)docs/ephemeral'` is the ten documents of plan v1.0 (+137/−57), as the review measured.
- `docs/qa_harness_pattern.md` is 120 lines (112 before #692). The two findings' lines on `main`: line 14 ends "The composed writer currently admits only `HDE-CRD-0001`."; line 97 reads "follow AGENTS.md readiness: install `requirements-dev.txt` with that interpreter …".
- **Consumers of the page:** `git grep qa_harness_pattern` over `tests`, `ci`, `tools`, `scripts`, `.github`, `engine` and `adapter` finds none. In canon, PF20-Reference-HDE-Phased-Epics names it as a titles-only pointer ("operator guidance, not PF canon") and PF30.1-Canon-HDE-CRD-Records names it among HDE-CRD-0001's affected surfaces; neither states its content.
- **Release:** `1.3.0`, 45 members, `release_id` `77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e` (pre-push `membership`, §11). The page is not a member.
- **CI path:** the page is outside the eight storage prefixes, so the workflow filter starts the `test` job; the classifier gives `documentation_only`, `needs_python=false`, and the job ends with `CI_APPLICABILITY_AND_EXACT_HEAD_OK` (instruction §5.4; review §3). Codex code review excludes Markdown (`AGENTS.md` "Code review guidelines").

## 5. Sweep of the page (lineage review §6, "What the re-plan covers")

Every statement on the page within Q-1's subject (CRD admission; the close-run API) or A-4's subject (pytest guidance), checked against the code at `b00a26c`.

| Line | Statement | Proof at `b00a26c` | Disposition |
| -: | :- | :- | :- |
| 7 | `HarnessConfig` positional fields `epic_id=None`, `repo_root=None`, `step_names=()`; `crd_id` keyword-only; exactly one identity | `qa_harness.py:58-68` | current; no change |
| 12 | `HarnessConfig(crd_id="HDE-CRD-0001", …)` selects `audit/qa/hde-crd-0001/`; Epic-only fields `None` | `qa_harness.py:69-82` (`qa_root = root/"audit"/"qa"/crd_id.lower()`); probe: `HDE-CRD-0002` → `audit/qa/hde-crd-0002`, `HDE-CRD-0003` → `audit/qa/hde-crd-0003` | **example, not an admission claim** (the review's reading confirmed): it shows the derivation, true for every valid ID; no change |
| 14 | "CRD identity uses a full-string ASCII match of `HDE-CRD-[0-9]{4,}` …; accepts `HDE-CRD-10000`; syntax support … grants [no] governed-publication admission" | `qa_harness.py:23` (`CRD_RE = re.compile(r"HDE-CRD-[0-9]{4,}\Z")`, `fullmatch` at line 70) | current; no change |
| 14 | "The composed writer currently admits only `HDE-CRD-0001`." | `update_evidence_index.py:51-54` (`ADMITTED_CRD_QA` admits `HDE-CRD-0001` and `HDE-CRD-0002`); refusal at 5180-5186 and 5238-5244; probe: `HDE-CRD-0003` refused by both publishers with "admits only HDE-CRD-0001, HDE-CRD-0002" | **LRD-F1: change (C-1)** |
| 44 | "For `HDE-CRD-0001`, current primaries are `audit/qa/hde-crd-0001/checks/<check_id>/primary.log` and the manifest is `audit/qa/hde-crd-0001/qa_step_logs_manifest.json` …" | `update_evidence_index.py:3933-3944` (`_crd_qa_entry`: `checks/<id>/primary.log`, `qa_step_logs_manifest.json` under the admitted root); `qa_harness.py` `checks_root = config.qa_root / "checks"` (line 2438) | **example, true, scoped to the CRD it names**; it claims nothing about admission, and line 12 gives the general derivation; no change |
| 69 | CRD `additional_files` must stay within the active QA root | `qa_harness.py:2439-2445` | current; no change |
| 73-79 | `publish_crd_check_family(config, results, *, captured_at_utc=None, coherence_verifier=None)`; returns primaries and manifest; module must belong to `config.repo_root`; admitted CRDs per `ADMITTED_CRD_QA`, today `HDE-CRD-0001` and `HDE-CRD-0002`; nonempty family and coherent graph required first | `update_evidence_index.py:5166-5219` (signature; `repo_root != ROOT` refusal; `_run_once(check=True)` before the transaction) | current (corrected by #692); no change |
| 81 | one outer `_WriteTransaction`; optional read-only `coherence_verifier` after writes; recovery bounds | `update_evidence_index.py:5205-5219` | current; no change |
| 83 | "CRD keys use the admitted key prefix, for example `audit.qa.hde_crd_0001.qa_step_logs_manifest` …" | `_crd_qa_entry` (`f"{key_prefix}.{suffix}"`, suffixes `qa_step_logs_manifest` and `checks.<id>.primary.log`) | example of the admitted prefix (corrected by #692); no change |
| 85 | no CRD CLI wrapper and no updater `--crd-id` flag; `--check` is read-only | `update_evidence_index.py:5294-5310` (arguments `--check`, `--rebind-sanity-log`, `--epic-id` only); `qa_harness.py` has no `argparse` or `__main__` | current; no change |
| 87-93 | `publish_crd_close_run_family(config, results, *, captured_at_utc=None, coherence_verifier=None)`; writes `audit/qa/<crd-dir>/close/<check_id>/primary.log` and its path proof; requires the recorded QA family; replaces the whole family; writes neither the manifest nor a `checks/` primary; same recovery bounds; membership rule in `docs/EVIDENCE_INDEX.md` | `update_evidence_index.py:4008-4042` and 5222-5290 | current (added by #692); no change |
| 97 | `run_pytest_check` uses the same interpreter for readiness and execution through `sys.executable -m pytest` | `qa_harness.py:2184-2195` | current; no change |
| 97 | "follow AGENTS.md readiness: install `requirements-dev.txt` with that interpreter and confirm `python -m pytest --version`" | `AGENTS.md:55` (install what CI installs, `python -m pip install 'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e .`; "Without `-e .` the `hdctl` console script is missing"); `ci.yml` install step (`'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e .`) | **LRD-F2: change (C-2)** |
| 97 | closed-rails defaults (`LC_ALL=C`, `LANG=C`, `TZ=UTC`, `SAFE_MODE=1`, `ALLOW_NETWORK=0`, applicable `APP_ENV`) | `AGENTS.md` "Operating workflow", closed-rails default | current; no change |
| 99 | Epic viability "performs same-interpreter collection" | `qa_harness.py:3266-3277` (`sys.executable -m pytest --collect-only`) | current; no change |
| 101 | both viability functions refuse CRD mode; `replace_legacy_family_ids` and `admit_new_check_ids` refused for CRD | `qa_harness.py:3479-3480`, 3921-3922, 2429-2430 | current; no change |

**Count:** 16 rows; 2 changes (LRD-F1, LRD-F2); 14 confirmed current, of which 3 are examples (lines 12, 44, 83).

**Outside the two subjects, recorded only:** line 120 cites "PF10 — HDE Build Notes §2.8" for the rule "distinguish tested state, later evidence-storage commit and review-time HEAD". In PF10 v13.7.4, addendum 2.8 is the HDE-CRD-0002 WU-PR-03 lineage review (line 876), and a search of PF10 for "tested state", "evidence-storage" and "review-time" finds nothing; the rule's text is in `AGENTS.md` "Evidence attribution, currentness and distinct decisions" (line 108). This is not within Q-1's or A-4's subject, and the review reopens nothing else, so it is routed as RF-11 (§16), not edited.

## 6. Exact changes (the statement-to-proof list DOC-20 verifies for this cycle)

The exact bytes are in the companion diff.

### C-1 (LRD-F1), `docs/qa_harness_pattern.md` line 14, last sentence

- **Old:** "The composed writer currently admits only `HDE-CRD-0001`."
- **New:** "The composed writers admit only the CRDs in the updater's source-owned `ADMITTED_CRD_QA` table, today `HDE-CRD-0001` and `HDE-CRD-0002` (see Governed CRD publication)."
- **Proof:** `tools/evidence/update_evidence_index.py:51-54` (the table); 5180-5186 (`publish_crd_check_family` refusal) and 5238-5244 (`publish_crd_close_run_family` refusal); the probe in §11.3. "Writers" is plural because both composed publishers apply the table. The wording matches line 79 and `docs/EVIDENCE_INDEX.md` line 62, as the review's bounded correction asks.

### C-2 (LRD-F2), `docs/qa_harness_pattern.md` line 97, second sentence

- **Old:** "When a selected check uses pytest, follow AGENTS.md readiness: install `requirements-dev.txt` with that interpreter and confirm `python -m pytest --version` before execution."
- **New:** "When a selected check uses pytest, follow the AGENTS.md pytest readiness rule: with that interpreter, install what CI installs, `python -m pip install 'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e .`, and confirm `python -m pytest --version` before execution. Without `-e .` the `hdctl` console script is missing."
- **Proof:** `AGENTS.md:55`, the "Pytest readiness rule" as #692 landed it; `.github/workflows/ci.yml`, step "Install applicable validation dependencies" (the same arguments); instruction §5.5 (five `hdctl` failures without `-e .`). "With that interpreter" keeps the page's point: `run_pytest_check` runs readiness and tests through `sys.executable` (`qa_harness.py:2194-2195`).
- **Form chosen (PD-2):** the command is stated, as `AGENTS.md` states it, rather than a bare pointer, because the page's reader runs it with a specific interpreter. The sentence names its source, so a later change to the `AGENTS.md` rule has one place to check.

## 7. Files and requirement-to-change/test map

| Item | File | Requirement / obligation | Test or check |
| :- | :- | :- | :- |
| C-1 | `docs/qa_harness_pattern.md` | instruction §6.5 Q-1 ("CRD admission per E-1"); S22; instruction §9.3 | no test reads the page (§4); proof is the code and the probe (§11.3); DOC-20 re-checks on merged `main` |
| C-2 | `docs/qa_harness_pattern.md` | instruction §6.2 A-4 and DOC10-F2; §9.3 | as C-1; the install itself is exercised by §10 item 1 |

- **Files changed:** one, `docs/qa_harness_pattern.md` (`M`).
- **Not changed:** every other document, code, test, workflow, schema, canon, governed artifact and release member (instruction §7). The plan's own record and companion diff are under `docs/ephemeral/`.
- **Plan v1.1 §7 acceptance** "`tests/unit/test_check_agents_md_citations.py` passes": `AGENTS.md` is not changed; the test is still run (§10).

## 8. Implementation sequence for PR-30

1. **Recover first.** Inspect local roots, worktrees, branches and open PRs for WU-DOC-01, and `docs/ephemeral/HDE-CRD-0002-WU-DOC-01-*`. Resume the most advanced consistent cycle-2 state. Create nothing that already exists. #692 and its branch `claude/sharp-carson-5ttoho` are landed history and are not a recovery target.
2. **Check the base.** `git fetch origin main`. `git diff --stat b00a26c origin/main -- docs/qa_harness_pattern.md` must be empty.
   - If it is not, run `git apply --check` of the companion diff on `origin/main`.
   - If it does not apply, or a changed line touches line 14 or 97, stop and return to this PR-20 session through same-owner recovery. Do not hand-merge.
3. **Branch** from `origin/main`: the harness-designated branch for the PR-30 session, new for cycle 2.
4. **Apply** `git apply docs/ephemeral/HDE-CRD-0002-WU-DOC-01-pr-implementation-plan-v2.0-prototype.diff`, read from `main`. Then `git diff --name-status origin/main` must list exactly `M docs/qa_harness_pattern.md`.
5. **Validate** as §10 items 1 to 5.
6. **Commit once**, `docs: correct CRD admission and pytest readiness in the QA harness guide (HDE-CRD-0002 WU-DOC-01, LRD-F1, LRD-F2)`, with the attribution lines the session requires.
7. **Write the PR-30 result record** under `docs/ephemeral/` as the next free result version (v2.0, matching this plan cycle). It holds the applied-diff sha256, the test counts, the `lanes` and `membership` output and the CI state known at writing.
8. **Push and open a new PR.** The description uses the `.github/pull_request_template.md` headings under the `AGENTS.md` "PR descriptions" rules. "Why" cites the lineage review's LRD-F1 and LRD-F2. "What merging does" states what becomes current on `main` and that merging does not establish QA, acceptance or closure.
9. **Return** `PR_CANDIDATE_PUBLISHED` with the PR-35 handoff.

## 9. PR split and merge dependencies

- **One PR.** One file, two independent sentences; no reason to split (PD-1).
- **Merge dependency:** this plan's own record PR should merge first, so PR-30 reads the companion diff from `main`. The merge is the Product Owner's manual act.
- **No other PR** is a prerequisite. #692 is merged; this PR does not depend on reopening it.
- **Downstream:** PR-40 (the whole-change IA) reviews the corrected unit across #692 and the new PR; then DOC-20; then WU-OPS-01's business case before OPS-10.

## 10. Validation PR-30 runs (PR-35 re-runs items 2 and 3 on the final head)

Run everything under closed rails (`env -i PATH=… HOME=… SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC`), with no vendor, database or GitHub key passed to a child.

1. **Install:** CPython 3.12, CI's full install, `python -m pip install 'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e .`, into a venv bound to a throwaway copy or a dedicated environment. Then `python -m pytest --version`.
2. **Citation check:** `python ci/checks/check_agents_md_citations.py` prints `AGENTS_MD_CITATIONS_OK`; `tests/unit/test_check_agents_md_citations.py` passes.
3. **The six document-reading test files** (instruction §5.5): `tests/unit/test_check_agents_md_citations.py`, `tests/unit/test_check_direct_db_contract.py`, `tests/bodygraph/test_check_magic10_gate_readiness.py`, `tests/evidence/test_rails_ci_workflow_integration.py`, `tests/cli/test_cli_usage_and_errors.py`, `tests/qa/test_generate_epic_close_pack.py`. Zero failures. Prototype: **1,248 passed**. None reads this page; the run shows the change breaks no document consumer and keeps the unit's acceptance test green.
4. **Pre-push reports** on the committed head:
   - `python tools/ci/prepush_check.py --base origin/main --head HEAD lanes build-notes` → `reason=documentation_only;paths=1;lanes=none`, PF10 path and sha256 recorded;
   - `python tools/ci/prepush_check.py --head HEAD --path docs/qa_harness_pattern.md membership` → `not-member`, `release_id` unchanged.
5. **Changed paths:** `git diff --name-status origin/main...HEAD` lists `docs/qa_harness_pattern.md` only (before the result record), and the applied diff's sha256 equals the companion's.
6. **Hosted CI (PR-35):** the `test` job succeeds on the final head, shows `reason=documentation_only`, skips setup, install and the lanes (`needs_python=false`), and prints `CI_APPLICABILITY_AND_EXACT_HEAD_OK`. Items 2 and 3 are therefore local-only evidence.

Codex code review excludes Markdown, so no Codex finding is expected. A human or other review comment is dispositioned under addendum 2.11 rule 7 and addendum 2.14.

## 11. Prototype record

### 11.1 Construction

- **Clone:** a throwaway clone of `b00a26c` in the session scratchpad, branch `proto`.
- **Edits:** a scratch script of 2 exact old→new replacements, each required to match exactly once. The script is not committed; the diff is the deliverable.
- **Commit:** prototype head `b313061be83a6af29f8d22b505e85681b0896928`.
- **Diff:** `git diff b00a26c b313061` = the companion. 1 file, +2/−2; 3,880 bytes; sha256 `40e19bd145af12563a4385b7e7ed783f0b5c10c7c765b5ff5d25b17f006e39c3`; `git apply --check` clean on `b00a26c` (run in the working checkout).

### 11.2 Results on the prototype head (2026-10-22 UTC)

Venv: CPython 3.12.3, `pip install 'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e .` exit 0; pytest 8.4.2. `env -i` closed rails with `APP_ENV=dev` and `PYTHONDONTWRITEBYTECODE=1`.

| Check | Result |
| :- | :- |
| The six document-reading test files | **1,248 passed** in 86.19 s; exit 0 (02:45:00Z to 02:46:26Z) |
| `check_agents_md_citations.py` | `AGENTS_MD_CITATIONS_OK`, exit 0 |
| `check_direct_db_contract.py` | `DIRECT_DB_CONTRACT_OK` |
| `prepush_check.py --base b00a26c… --head HEAD lanes build-notes` | `CI_CHANGE_CLASSIFICATION:event=pull_request;reason=documentation_only;paths=1;lanes=none`; build-notes `docs/pfcanon/PF10-HDE-Build-Notes-v13.7.4.md` 433,368 bytes sha256 `8ac97232…6d37ff`; `PREPUSH_CHECK_RESULT: PASS`; repository unchanged |
| `prepush_check.py --head HEAD --path docs/qa_harness_pattern.md membership` | `not-member`; `1.3.0`, roster 45, `release_id` `77204764…c51e`; PASS |
| `git diff --name-status b00a26c HEAD` | `M docs/qa_harness_pattern.md` |
| Clone clean after the runs | yes (`git status --short` empty) |

An earlier run of the citation check and the two pre-push reports in a CPython 3.13.16 venv gave the same results; it was replaced by the 3.12 venv, CI's version, and only the 3.12 results above are relied on.

### 11.3 Probe at `b00a26c` (closed rails; no write)

- `ADMITTED_CRD_QA` = `{HDE-CRD-0001: (audit/qa/hde-crd-0001, audit.qa.hde_crd_0001), HDE-CRD-0002: (audit/qa/hde-crd-0002, audit.qa.hde_crd_0002)}`.
- `HarnessConfig(crd_id=…)`: `HDE-CRD-0001` → `audit/qa/hde-crd-0001`; `HDE-CRD-0002` → `audit/qa/hde-crd-0002`; `HDE-CRD-0003` → `audit/qa/hde-crd-0003` (local configuration accepts it).
- `publish_crd_check_family(HDE-CRD-0003 config, [])` → `ValueError: governed CRD publication admits only HDE-CRD-0001, HDE-CRD-0002; refused HDE-CRD-0003`.
- `publish_crd_close_run_family(…)` → `ValueError: governed CRD close-run publication admits only HDE-CRD-0001, HDE-CRD-0002; refused HDE-CRD-0003`.
- Both refusals occur before any write (the admission check is the first statement of each function).

## 12. Interface contracts (instruction §8)

| Contract | Met by |
| :- | :- |
| IF-4, IF-5 (the updater) | C-1 describes `ADMITTED_CRD_QA` and both publishers at `b00a26c` |
| DOC-20 | §6 adds C-1 and C-2 to plan v1.0 §6's statement list |
| WU-OPS-01 | no Ops fact is stated |
| G-1, H-4, IF-7 | unaffected; delivered by #692 and not reopened |

## 13. Security and migration

- No secret, token, key value or base URL in the change; the install command names files only.
- Closed rails for every run; no live vendor, production or database access occurred.
- Migration: none. Rollback is a revert of the new PR.

## 14. Risks and recovery

| ID | Risk | Treatment |
| :- | :- | :- |
| RK-1 | `main` changes the page before PR-30 | §8 step 2; a conflict returns to this PR-20 session; no hand merge |
| RK-2 | PR-30 pushes to #692's branch by recovery reflex | §8 steps 1 and 3: new branch, new PR; #692 is landed history |
| RK-3 | The `AGENTS.md` readiness rule changes later and C-2 goes stale | C-2 names its source; DOC-20 re-checks on merged `main` |
| RK-4 | Another CRD is admitted later and C-1's "today" list goes stale | the sentence points to the table, as line 79 does; the updater's next admission change owns both lines |

- **Recovery:** resume from the last saved artifact; the prototype lives only in throwaway clones.
- **An instruction defect** returns to the IA through DOC-10. **Abort** is only Nathan's manual PR-50.

## 15. Decisions taken in this plan (within approved scope)

| ID | Decision | Reason |
| :- | :- | :- |
| PD-1 | One PR, one commit | two sentences in one file |
| PD-2 | C-2 states the install command, citing `AGENTS.md` | the page's reader runs it with a specific interpreter; the review allows either form |
| PD-3 | Lines 12, 44 and 83 stay as examples | each is true, names the CRD it shows, and makes no admission claim; line 12 gives the general derivation and line 79 the admission rule |
| PD-4 | Line 120's `§2.8` citation is routed, not edited (RF-11) | outside Q-1's and A-4's subjects; the review reopens nothing else (instruction §9.3) |
| PD-5 | Plan version 2.0, result version 2.0 | the cycle-2 convention of WU-PR-01 and WU-PR-02 (plan v2.0 after a REJECT) |

No Product Owner question arises: neither change touches `AGENTS.md`, the review-scope rule, or anything instruction §9.2 reserves.

## 16. Findings outside this unit's bound (recorded and routed, not changed here)

| ID | Finding | Proposed owner |
| :- | :- | :- |
| RF-11 | `docs/qa_harness_pattern.md:120` cites "PF10 — HDE Build Notes §2.8" for the tested-state / evidence-storage / review-time distinction. In PF10 v13.7.4, §2.8 is the WU-PR-03 lineage review; the rule is stated in `AGENTS.md` "Evidence attribution, currentness and distinct decisions". The citation is pre-existing and outside this correction's subject | the Product Owner, as a later documentation candidate |
| RF-1 to RF-10 | plan v1.0 §16 | unchanged, as plan v1.0 routes them |

## 17. Carried items and canon-conflict register

- **Carried unchanged:** plan v1.0 §17 (DOC10-O1; O-19 code; OBS-8; OBS-P3-13; PR35-C1 and LR8-F1; the canon doc-deltas; the S21 ADR revision; WU-OPS-01's business case); lineage review §9 (the IA lesson on "the rest of the page stays"; LRD-O1).
- **`CANON_CONFLICT_REGISTER`:** CR-1 to CR-3 APPROVED_AS_CHANGED by Thoth; CR-4 APPROVED and CR-5 APPROVED_AS_CHANGED by the Product Owner; CR-6 APPROVED (a) by the IA through RS-20; CR-7 and CR-8 APPROVED (a) each by the Product Owner. **No new conflict:** both findings and RF-11 are repository-documentation drift against code, `AGENTS.md` and PF10's numbering, not canon conflicts.

## 18. PR-30 and PR-35 obligations

- **PR-30** (this dedicated session, after Nathan's Proceed for exactly v2.0): recover first; apply only the companion diff; run §10 items 1 to 5; commit once; write result v2.0; push a new branch and open a new PR; return `PR_CANDIDATE_PUBLISHED` with a PR-35 handoff. PR-30 does not own review correction, current-head CI readiness or merge.
- **PR-35** (its own dedicated session): retrieves every review thread and dispositions any finding (addendum 2.11 rule 7; addendum 2.14); corrects in-scope defects with a coherent push; re-runs §10 items 2 and 3 on the final head; verifies item 6, the remote-head identity and mergeability; returns `MERGE_PENDING` without merging. No `[skip ci]` without Nathan's direct instruction.
- **Merge:** Nathan merges manually.
- **After the merge:** PR-40 (the whole-change IA) reviews the landed lineage of the unit; then DOC-20.
- **Nonclaims:** no QA, acceptance, Ops, deployment, PF09 or PF30 movement, drainage or closure.

## 19. TypeSafe reading for the receiving session (PR-30, WU-DOC-01, plan v2.0)

Action sent (v8.2): "Implement, in a new dedicated session after a Product Owner Proceed, a re-planned correction to one merged documentation work unit that a lineage review rejected: apply a planned two-sentence correction to one existing 120-line Markdown harness guide (one sentence about which change identities a writer admits, one about the test-dependency install rule), where the plan gives the exact replacement text and a one-file prototype diff that already applies cleanly and passes; recover any existing work first, check the base has not moved, run the local tests that read the repository documents with the full CI install plus the pre-push lane and membership reports, commit once and publish a new pull request. No code changes and no live provider run occur; a separate review-correction session, CI, a lineage review and a completion verification follow."

- **TypeSafe v8.2: Opus 5.5 at medium.** Effort score 1.36 (confidence 0.76); rung probabilities low 0.00, medium 0.66, high 0.32, extra high 0.02, max 0.00, ultracode 0.00. Model probabilities Fable 5.1 0.00, Opus 5.5 0.86, Sonnet 5.5 0.14, Haiku 5.5 0.00 (confidence 0.81). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.000, Fable 5.1 at high 0.000, Fable 5.1 at extra high 0.000, Fable 5.1 at max 0.000, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.000, Opus 5.5 at medium 0.568, Opus 5.5 at high 0.275, Opus 5.5 at extra high 0.017, Opus 5.5 at max 0.000, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.000, Sonnet 5.5 at medium 0.092, Sonnet 5.5 at high 0.045, Sonnet 5.5 at extra high 0.003, Sonnet 5.5 at max 0.000, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Sent 2026-10-22T02:47:06Z. Nathan picks the cell.
- **Flags:** none printed.
- **Detail:** v8.2 sent 2026-10-22T02:47:06Z; HTTP 200 in 0.6 s; 5507 input and 71 output tokens; jev-1.13.0. Rung by rule: medium (nearest to the score, halves up); model by rule: Opus 5.5 (the most probable of the four options, a tie going to the higher-priced model).
- **Which request:** the installed TypeSafe scoring skill's request v8.2 and `score_v8.py`, run once with session kind `implementation`, before this record was saved. The script's label read "PR-30 — HDE-CRD-0002 WU-DOC-01 (re-plan, plan v1.1)"; the plan was then numbered v2.0 (PD-5). The label is not part of the action text and was not re-run.
- **Records:** the Notion row was not written (a development-flow session, read-only toward Notion). Nathan's pick for PR-30 is not stated. Nathan's pick for this PR-20 session is not stated; its reading is lineage review v1.0 §12.

**Surface advice:** run PR-30 in this same dedicated top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, entered by Nathan's Proceed.
- **Environment:** CPython 3.12 (`/usr/bin/python3.12` is present; the default `python3` is 3.13) with CI's full install in a venv bound to a throwaway copy; git, bash, `curl` and `ruby` on `PATH` for the pre-push check; closed rails through `env -i`.
- **Run times observed:** the six test files about 86 s; each pre-push report about 3 s.
- **Access:** no live vendor, production or database access.
- **Order:** this plan's pull request should be merged first, so the companion diff is on `main`.

## 20. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / WU-DOC-01 / PR-20 / plan 2 (cycle 2) |
| change / specification | CRD HDE-CRD-0002 / `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` v1.1, with Specification delta 01 |
| unit | WU-DOC-01 |
| release | GCFPE-20261009.1 / 100926.1 |
| prompt | PR-20 — Create Detailed PR Implementation Plan — 100926.1, https://app.notion.com/p/3f44590a05eb819fbea5dcd966a750ba (page state as of 2026-10-12T02:29:47.327Z). Receiver contract read: PR-30 — PR Implementation Proceed — 100926.1, https://app.notion.com/p/3f44590a05eb8148a538f5c80588db14 (page state as of 2026-10-12T02:30:08.672Z) |
| role/stage | dedicated WU-DOC-01 PR engineering session / PR-20 (re-plan entry) |
| capture time | 2026-10-22T02:50:00Z |
| execution identity | https://claude.ai/code/session_01WPAu8VRbMGFAKxrRj6WGur |
| inherited usage | lineage review v1.0 §13 (PR-40); result v1.1 (PR-35); result v1.0 and plan v1.0 (PR-30, PR-20); instruction v1.0 (DOC-10) |
| repository persistence | recorded here only. `docs/changes/GCFPE_PROMPT_PROVENANCE.md` is absent on `main`; persistence is pending and non-gating |

## Canon relied on

Read on `main` at `b00a26c`. `docs/pfcanon/` was last changed by `e56788c`; PF10 is v13.7.4 (path and hash in the front matter). This branch does not change `docs/pfcanon/`.

| Topic | Sources and sections | How it governs |
| :- | :- | :- |
| PR-20 operation and re-plan entry | PR-20 — Create Detailed PR Implementation Plan — 100926.1, read in full ("Inputs", re-plan entry; "Execute" 1 to 10; "Required result"; "Next step and recovery"; "Save and hand off"; "Mandatory single-block handoff") | §1, §8, §18: a new plan, a new PR, ending at `AWAITING_PO_PROCEED` |
| New plan, own Proceed | PR-30 — PR Implementation Proceed — 100926.1, "Product Owner Proceed and engineering boundary" | §1, §18 |
| The findings and the bounded correction | lineage review v1.0 §6 and §11 | §5, §6 |
| Real inputs; finding disposition | PF10 addendum 2.11 rules 4 to 8, read in full | §3; §10 (review dispositions) |
| Business case without ceiling; PR-40 records the measure | PF10 addendum 2.18 rules 1 to 6, read in full | §3 |
| P1 | PF10 addendum 2.14, read in full | §10, §18 |
| Unit scope | PF10 addendum 2.19 P-8 and its WU-DOC-01 summary; instruction §6.2 A-4, §6.5 Q-1, §9.3 | §5, §7 |
| Routed stale-document list | PF10 addendum 2.21, read in full ("Required canon drainage"; "Deferred obligations") | §3 |
| Reviewer chain | PF10 addendum 2.3 (carried from plan v1.0); `AGENTS.md` "Code review guidelines" | §4, §10 |
| Source fidelity | PF03-Reference-Technical-Writing-Best-Practices "Truth and source fidelity" (carried from plan v1.0, not re-read here) | §6: each changed sentence cites the code that controls it |
| The page's canon references | PF20-Reference-HDE-Phased-Epics line 3331 and PF30.1-Canon-HDE-CRD-Records line 387, read at those lines | §4: pointers only; no canon states the page's content |
| Repository rules | `AGENTS.md` "Operating workflow" (pytest readiness rule; pre-push check; closed rails; redaction; PR descriptions) | §6 C-2, §10 |

**Search:** `git grep -c -i -E 'qa_harness_pattern|ADMITTED_CRD_QA|re-plan|reject_replan|WU-DOC-01' origin/main -- docs/pfcanon/`: PF10 46, PF20-Reference-HDE-Phased-Epics 1, PF30.1-Canon-HDE-CRD-Records 1. The PF10 hits bearing on this re-plan are addenda 2.11, 2.14, 2.18, 2.19 and 2.21; the other two are the pointers in §4.
