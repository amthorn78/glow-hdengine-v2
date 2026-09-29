---
artifact_type: ONE_TIME_TASK_PROMPT
artifact_version: "1.0"
logical_id: HDE-EPIC040-CLOSE01-CLOSURE-EVIDENCE-TASK-PROMPT
work_unit_id: HDE-EPIC040-CLOSE01
work_unit_kind: PR (the Change Process Guide §3.5 close mutation set)
change_id: HDE-EPIC040
change_class: EPIC
author: Isis, CL-E-10 for HDE-EPIC040 (https://claude.ai/code/session_012tPq26JWVhCYZmcqTidpV2)
requested_by: Nathan / Product Owner, 2026-09-29 ("create a one time closure task prompt (Ops or PR) as needed"; "help me fix this issue: The QA evidence of record at 787bb97 is still only on its branch, not on main.")
ordered_by: docs/ephemeral/HDE-EPIC040-CL-E-10-closure-decision-v1.1.md §3 (DO_NOT_CLOSE; return work)
standing: One-time development-flow prompt for this change only. It is not a GCFPE release member, creates no standing route, and is not stored in Notion (docs/ephemeral/GCFPE-alpha-feedback-epic-closure-evidence-task-v1.0.md)
vehicle_rationale: PR, not Ops. The work mutates tracked repository state (governed evidence, Index and Mirror, close pack, and possibly an evidence-writer registration in tooling). Change Process Guide §3.5.1 makes the close mutation set a PR-route mutation set that the Product Owner merges. Ops executes environment actions, and its §3.5.2.1 OPS-02 run is provenance-only
---

# HDE-EPIC040-CLOSE01 — Prepare and publish the Epic close mutation set (one-time task prompt)

Paste everything from the next heading to the end of this file into a new top-level session on repository `amthorn78/glow-hdengine-v2`. Pasting it is the Product Owner's Proceed for this exact work unit and for no other.

## Role and authority

- **Role.** You are the implementing agent for one PR work unit, **HDE-EPIC040-CLOSE01**: the close mutation set of the Change Process Guide §3.5 for Epic HDE-EPIC040.
- **Deliverable.** A close pull request that is ready for the Product Owner to merge, plus one result record.
- **Merging.** You never merge, enable auto-merge, or ask for a merge as routine. Nathan alone merges, by squash (Change Process Guide §3.5.1).
- **Scope of this Proceed.** It authorizes only the repository changes listed under "Allowed changes". It authorizes nothing else: no QA rerun, no Ops, no vendor or database call, no deployment, no PF-Canon edit, no PF09 or board change, no closure decision.
- **Closure authority.** The closure decision belongs to Isis at CL-E-10, which runs again after the merge. Any `SATISFIED` in the close report is the formal close-pack (Close Gate) posture only (HDE Schemas & Artifacts, close report rules). It is not Isis's closure, a Product Owner closeout, or a PF09 drain.
- **Skill.** Use the `glow-hde-pr-development` skill only for PR mechanics: publication, review correction, CI economy, current-head proof and merge readiness. Its PR-20 planning and PR-40 lineage stages do not apply. Where the skill and this prompt conflict on scope, this prompt governs.

## Canon-first (before any change)

Follow `AGENTS.md` "Canon-first rule". Read these in full from `docs/pfcanon/` on `main`, and search PF10 (HDE Build Notes, the current file) for anything that overrides them:

- **Change Process Guide:**
  - §0.2 (PR-route parity);
  - §0.4.1.1 to §0.4.1.3 (D0 artifact; QA RCA & Doc Delta summary, including its "Location" rule; execution gate);
  - §3.5.1;
  - §3.5.2.1 to §3.5.2.4;
  - §3.5.2.8.
- **HDE Schemas & Artifacts:**
  - "Close-pack artifacts (deterministic path-of-record; baseline artifacts)", including "Acceptance-binding family coherence" and "Evidence generator PASS coupling";
  - the path-proof, Human Evidence Index and Machine Mirror contracts.
- **Glow QA Guide:**
  - "Close-pack truthfulness and same-run execution";
  - "Close report requirements (validator-bound; mechanical)";
  - the manifest ledger-coverage proof rule;
  - §3.4.13;
  - §4.3.1.
- **Plan Templates:** §10 (closure review structure and later-drain fields).
- **`AGENTS.md`:**
  - "Governed evidence rules";
  - "Evidence attribution, currentness and distinct decisions";
  - "HDE-EPIC039 current workflow posture" (the generic close-pack generator);
  - "PR descriptions".

Record in the result record every section you relied on. Never cite canon you did not read.

## Inputs (read in full)

| Path | What it is |
| --- | --- |
| `docs/ephemeral/HDE-EPIC040-CL-E-10-closure-decision-v1.1.md` | The decision returning this work (§3: R-1 to R-5) |
| `docs/ephemeral/HDE-EPIC040-CL-E-10-closure-decision-v1.0.md` | Retrospective, delivered-scope disposition, open findings, PF09 later-drain recommendation (§3 to §7, §10 to §15 stand) |
| `docs/ephemeral/HDE-EPIC040-QA120-qa-report-v1.0.md` | Final QA Report, verdict `PASS`; per-criterion conclusions AC040-01 to AC040-09; deferrals; completion states; PF09 later-drain table |
| `docs/ephemeral/HDE-EPIC040-QA120-qa-rca-v1.0.md` | QA RCA & Doc Delta summary. Its governed placement (close-report section or `audit/EPIC-040_QA_RCA.md`) is part of this work |
| `docs/ephemeral/HDE-EPIC040-QA50-qa-plan-v1.2.md` | Approved QA Plan v1.2 (the close pack's `plan_path` candidate) |
| `docs/ephemeral/HDE-EPIC040-QA50-qa-audit-v1.0.md` | QA50-F01 and L-44: no admitted Index or Mirror writer registration for the QA evidence |
| `docs/ephemeral/HDE-EPIC040-QA110-qa-evidence-review-v1.0.md` | Ruling LR-01: Run B is the evidence of record; the Run A branch must not be merged |
| `docs/ephemeral/HDE-EPIC040-specification-v1.1-approved.md` | Specification, AC040-01 to AC040-09, PF09 scope HDE-SEPA005 and .1 to .5 |

Facts established at CL-E-10 (re-verify each one; do not rely on them):
- The evidence branch is `origin/qa/hde-epic040-qa100-plan-v1.2-run-20260929` at `787bb97b58b638d6b307cad6d76484c883c58aec`.
- It adds 41 files over tested source `0db3f0ef33e7a7a3aa85a2c221e06ac5581c7b8d`:
  - 39 under `audit/qa/hde-epic040/`;
  - `audit/docdeltas/hde-epic040_doc_deltas.md` and its path proof.
- It merges into `origin/main` `c48a79a` without conflict.
- Between `0db3f0ef` and `c48a79a`, `main` changed only `docs/ephemeral/`, `docs/pfcanon/` and `docs/prompt_ecosystem_management/`.
- `audit/EPIC-040_*` and `audit/docdeltas/hde-epic040_drain_targets.md` do not exist.

## Allowed changes (Product Owner instruction for this PR)

This list is Nathan's explicit instruction for this pull request. Outside it, nothing may be written.

1. The 41 evidence files from `787bb97`, **byte-identical**.
2. The evidence-writer registration that QA50-F01 requires. It goes only in the file or files where the canonical updater `tools/evidence/update_evidence_index.py` admits registrations, in the form existing registrations use, with any test that pattern requires.
3. Outputs written by the canonical updater:
   - `docs/evidence/INDEX.json`;
   - `docs/evidence/INDEX.sha256`;
   - `artifacts/evidence_index.jsonl` and its checksum;
   - `audit/gates/topology/orientation_demo.txt`;
   - the proof companions the updater owns.
4. The close-candidate source file that `schemas/epic_close_candidate_source.v1.json` defines. It must be a tracked file at `HEAD` before generation. Place it where the generator, its tests or its documentation establish; if none does, see "Stop conditions".
5. Outputs written by `tools/qa/generate_epic_close_pack.py --write`: `audit/EPIC-040_close_report.md` and `audit/EPIC-040_MANIFEST.json`, plus the path proofs HDE Schemas & Artifacts requires, produced by their canonical writer.
6. `audit/docdeltas/hde-epic040_drain_targets.md`, and its path proof if the family requires one. Only when no governed generator owns it may you author it directly, and then only in the format HDE Schemas & Artifacts defines.
7. Same-run close-workflow execution evidence under `audit/qa/hde-epic040/`, at the home that step 5 establishes.

Never modify the 12 existing check directories, `qa_step_logs_manifest.json`, or any byte from `787bb97`. Never hand-edit an Index, Mirror, hash sentinel, path proof, manifest, close report or orientation artifact (`AGENTS.md`).

## Execute

Rails: `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0` for every repository tool. Install dev dependencies (`python -m pip install -r requirements-dev.txt`) and record `python -m pytest --version`.

1. **Branch.** Create `close/hde-epic040-close01` from the current `origin/main`. Record the base commit.
2. **Land the evidence (R-1).**
   - Merge `origin/qa/hde-epic040-qa100-plan-v1.2-run-20260929` with a merge commit; do not cherry-pick or rewrite.
   - Prove byte identity with `git diff --exit-code 787bb97 HEAD -- audit/qa/hde-epic040 audit/docdeltas/hde-epic040_doc_deltas.md audit/docdeltas/hde-epic040_doc_deltas.md.path_proof.txt`.
   - Never use `qa/hde-epic040-qa100-plan-v1.2` (Run A, `e5b671c`).
3. **Registration (R-2, QA50-F01).**
   - Read the updater and its tests to find how an evidence family is admitted.
   - Add the HDE-EPIC040 QA root, and the close-pack family if it is not already admitted, in the existing pattern.
   - Run the tests covering the updater.
4. **Close-candidate source (R-3).** Read `schemas/epic_close_candidate_source.v1.json`, `tools/qa/generate_epic_close_pack.py` and `tests/qa/test_generate_epic_close_pack.py`. Author the source so the generated close report satisfies all of the following:
   - **Change Process Guide §3.5.2.1:**
     - an exact-source acceptance section binding AC040-01 to AC040-09 to the final candidate, the relied-upon checks, evidence, results and limits, with the evidence taken from QA Report §7.1;
     - the baseline-existence verification statement;
     - a tracked-issue mapping for every `TI-*` item the epic cites, or an explicit statement that none is cited;
     - the binary `SATISFIED` or `NOT SATISFIED`, labelled as formal close-pack posture.
   - **HDE Schemas & Artifacts:**
     - shipped deliverables;
     - a deferrals section: the two live requirements blocked by environment (QA Report §7.2), each with its drain-target pointer or ADR status;
     - the later-drain PF-canon statements from QA Report §14 in the exact vocabulary;
     - the distinction between current PF09 recorded status, supported later-drain status, implemented state, OPS state and governed evidence state;
     - the full approved PF09 scope (HDE-SEPA005 and .1 to .5), with no epic-local token names;
     - a pointer to the manifest's `key_outputs`.
   - **The QA RCA & Doc Delta summary**, embedded as a close-report section with proof-class separation, or externalized to `audit/EPIC-040_QA_RCA.md` and referenced by exact path. Its content comes from the QA-120 RCA.
   - **Glow QA Guide:**
     - the heading `QA Rails — Open/Close (Final PR)` verbatim;
     - an "Acceptance and evidence pointers" list of this epic's canonical pointer strings. HDE-EPIC040 has no acceptance map or token matrix, so name `audit/qa/hde-epic040/qa_step_logs_manifest.json` and the other actual governed pointers, not the EPIC-023 example.
   - **Nonclaims:** no Isis closure, no PF09 movement, no canon drainage, no board state, no deployment, no live-database or deployed-service behavior, and no ledger-bound claim beyond what step 6 proves.

   Commit the source before generating (the generator reads tracked files at `HEAD`).
5. **Execution-evidence home (R-4).**
   - Determine from the governed tooling (`tools/qa/qa_harness.py`, the updater and the generator) and from the Glow QA Guide and HDE Schemas & Artifacts rules where same-run close-workflow evidence lives under `audit/qa/hde-epic040/`, without changing the 12 existing checks or the QA manifest.
   - If exactly one admitted home exists, use it.
   - If none exists, stop (see "Stop conditions"). Inventing a new evidence family is forbidden.
6. **Generate and publish.** Run in this order, capturing each command's exact command line, stdout, stderr and exit code (captured without a truncating pipe) into the execution-evidence home:
   1. `python tools/qa/generate_epic_close_pack.py --source <source> --write`, then commit.
   2. `python tools/evidence/update_evidence_index.py`, which writes the Index, sentinel, Mirror, orientation and proof companions, including rows for the QA evidence and the close pack. Then commit.
   3. `python tools/qa/generate_epic_close_pack.py --source <source> --check`.

   If the tooling requires a different order to reach a stable, feedback-free state (Change Process Guide §3.5.1), follow the tooling and record why.
7. **Read-only validation.** Run each of the following and record the results:
   - `python tools/evidence/update_evidence_index.py --check`;
   - `python tools/evidence/orientation_demo.py --check`;
   - `python tools/evidence/validate_evidence_paths.py`;
   - `ci/checks/check_mirror_schema.sh`;
   - `ci/checks/check_evidence_index_hash.sh`;
   - `python tools/evidence/run_canonical_json_gate.py --check-only`;
   - `python tools/evidence/check_lf_endings.py`;
   - `ci/checks/check_env_pins.sh`;
   - `python -m pytest tests/qa/test_generate_epic_close_pack.py` and the updater's tests.

   Then prove that the QA step logs manifest is ledger-bound: the updater source, the Index and the Mirror each contain it (Glow QA Guide manifest ledger-coverage proof). Commit the execution evidence. After this commit, no further commit may change the governed bytes it describes.
8. **Adversarial self-review.**
   - Re-read the diff against "Allowed changes".
   - Confirm that every claim in the close report has same-run evidence, and that no byte from `787bb97` changed.
   - Confirm that no epic-local token name appears.
   - Confirm that the deferrals and QA50-F01's before and after states are truthful.
9. **Publish.** Push and open one PR from `close/hde-epic040-close01` to `main`.
   - Title: `HDE-EPIC040 CLOSE01: close mutation set — land QA evidence, register it, close pack`.
   - Body: follow `.github/pull_request_template.md` headings as `AGENTS.md` "PR descriptions" defines them. "What merging does" must say that merging makes the QA evidence, its Index and Mirror registration and the close pack current on `main`. It must also say that merging does not establish Isis closure, PF09 movement, canon drainage or board state.
10. **Drive to green.** Subscribe to the PR's activity. Resolve review threads and CI on the current head per the PR-mechanics rules.
    - CI must pass on the exact PR head (`CI_APPLICABILITY_AND_EXACT_HEAD_OK`).
    - Optionally, the Product Owner may dispatch `.github/workflows/epic-closeout-validation.yml` on that head. Record its result if it is run.
    - Never use `[skip ci]`, never push an empty commit, and never skip a test.
11. **Result record.** On a separate branch touching only `docs/ephemeral/`, write `docs/ephemeral/HDE-EPIC040-CLOSE01-closure-evidence-result-v1.0.md`. It must contain:
    - the PR number and final head;
    - the base;
    - every command with its exit code;
    - validator and CI results;
    - the byte-identity proof;
    - the registration change;
    - the close report's formal posture;
    - limitations and nonclaims;
    - canon relied on;
    - a `GCFPE_PROMPT_USES`-style provenance entry naming this prompt by path.

    It goes on a separate branch so that the close PR's validated head does not change. Open it as its own PR and read it back.

## Stop conditions (terminal return to the Product Owner, no workaround)

- Byte identity with `787bb97` cannot be preserved.
- The updater admits no registration pattern for the QA root or the close-pack family without a design decision.
- The generator or its schema cannot express a required close-report element. Do not hand-edit the output.
- No admitted home exists for the execution evidence.
- A canon conflict governs a step and PF10 does not resolve it.
- CI fails for a reason this PR cannot fix within "Allowed changes".

In each case:
- keep the branch and any PR as they are;
- write the result record with the exact blocker, evidence, owner and resume point;
- end with no continuation handoff.

## Handoff when the close PR is ready

End your final response with exactly one block:

```text
NEXT_PROMPT_HANDOFF
Destination: CL-E-10 — Perform Epic Retrospective and Decide Closure — 091426.1
https://app.notion.com/p/3db4590a05eb811a8578d75885c16cac?pvs=204
Receiving role and session: Isis, continuing Lead Developer and terminal closure authority for HDE-EPIC040 (https://claude.ai/code/session_012tPq26JWVhCYZmcqTidpV2).
Change: HDE-EPIC040 (Epic).
Manual prerequisite: the Product Owner has merged close PR amthorn78/glow-hdengine-v2#<number> into main. Paste this only after that merge.

Inputs:
- docs/ephemeral/HDE-EPIC040-CLOSE01-closure-evidence-result-v1.0.md — CLOSE01 result: close PR, commands, validators, CI, formal close-pack posture
- docs/ephemeral/HDE-EPIC040-CL-E-10-closure-decision-v1.1.md — DO_NOT_CLOSE decision whose return work CLOSE01 performed
- docs/ephemeral/HDE-EPIC040-CL-E-10-closure-decision-v1.0.md — retrospective and analysis that stand
- docs/ephemeral/HDE-EPIC040-QA120-qa-report-v1.0.md — final QA Report, verdict PASS
- docs/ephemeral/HDE-EPIC040-QA120-qa-rca-v1.0.md — final QA RCA
```

Replace `<number>` with the actual PR number before emitting. The block may carry no other placeholder.
