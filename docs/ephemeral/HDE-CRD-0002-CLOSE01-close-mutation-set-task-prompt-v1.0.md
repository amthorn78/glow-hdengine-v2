---
artifact_type: ONE_TIME_TASK_PROMPT
artifact_version: "1.0"
logical_id: HDE-CRD-0002-CLOSE01-CLOSE-MUTATION-SET-TASK-PROMPT
work_unit_id: HDE-CRD-0002-CLOSE01
work_unit_kind: PR (Dev), Distillation phase block. The close mutation set of approved Implementation Plan v1.1 §9 item 5 and §7 WU-PR-07 "Terminal-state reachability" T0 to T7
change_id: HDE-CRD-0002
change_class: CRD
author: Isis (Isis-53), continuing Lead Developer and terminal closure authority for HDE-CRD-0002 (https://claude.ai/code/session_01NxRhYei7RDGmMPYdKEkpok)
requested_by: Nathan / Product Owner, 2026-10-26 ("create a task to create the close pack. The prompt should be created by you (Isis). I will need you to determine if this is an Ops or Dev task first. Either way, it will need to return to CL-C-10.")
ordered_by: docs/ephemeral/HDE-CRD-0002-CL-C-10-closure-decision-v1.1.md §4 (R-0 to R-7, after R-B4)
standing: One-time development-flow prompt for this change only. It is not a GCFPE release member, creates no standing route and is not stored in Notion. The missing standing route is recorded in docs/ephemeral/HDE-CRD-0002-PF10-build-notes-addendum-close-pack-process-gap-v1.0.md and GCFPE Modification Backlog MB-030
vehicle_rationale: Dev (PR), not Ops. The work writes tracked repository state through the canonical writers and lands by the Product Owner's merge. Canon basis: PF06 §3.5.2.1 ("The close PR MUST include the epic close-pack (canonical filenames)") and §3.5.2.3 (the trio "in the same authorized mutation set"); PF27 §3 "Definition" and "Not a PR (normative)"; PF06 §0.2 (an OPS-01 packaging run surfaces only "already-produced" close-pack artifacts). No step needs privileged access outside the repository
precondition: the B-4 remedy (CL-C-10 v1.1 §2, §4 R-B4) is merged and accepted, and the verification ESC-40 requires is recorded. Until then this prompt is not to be pasted
rehearsal: docs/ephemeral/HDE-CRD-0002-CLOSE01-close-rehearsal-record-v1.0.md
---

# HDE-CRD-0002-CLOSE01 — Produce and publish HDE-CRD-0002's close mutation set (one-time task prompt)

Paste everything from the next heading to the end of this file into a new top-level Claude Code session on repository `amthorn78/glow-hdengine-v2`.

Pasting it is the Product Owner's T0 authorization of HDE-CRD-0002's close mutation set (Plan v1.1 WU-PR-07 T0). It is also the Proceed for this exact work unit and no other, with this session as the vehicle: "a dedicated top-level close PR session acting under the Product Owner's authorization of that close PR" (WU-PR-07 (c)).

## Role and authority

- **Role.** You are the implementing agent for one PR work unit, **HDE-CRD-0002-CLOSE01**: the close mutation set of CRD HDE-CRD-0002.
- **Deliverable.** One close pull request ready for the Product Owner to merge, and one result record.
- **Merging.** You never merge, enable auto-merge or ask for a merge as routine. Nathan alone merges.
- **Scope of this Proceed.** Only the changes under "Allowed changes". No code, test, schema, workflow or ADR change. No QA rerun, Ops, vendor, database or deployment action. No PF-Canon or PF10 edit, no PF30 or board change, and no closure decision.
- **Closure authority.** Isis decides closure at CL-C-10, after the merge. The close report's `SATISFIED` is the close pack's review-trace-only posture. It is not Isis's closure, a Product Owner closeout or a drain.
- **Skill.** Use `glow-hde-pr-development` for PR mechanics only: publication, review correction, CI economy, current-head proof and merge readiness. Its PR-20 planning and PR-40 stages do not apply. Where it and this prompt conflict on scope, this prompt governs.

## Canon-first (before any change)

Follow `AGENTS.md` "Canon-first rule". Read these in full from `docs/pfcanon/` on `main`. Search the current PF10 (HDE Build Notes) for anything that overrides them, including the addenda recorded after 2.30 for the B-4 remedy.

- **PF06-Canon-Change-Process-Guide:**
  - §0.4.1.2 (the QA RCA & Doc Delta summary and its location);
  - §1.0.6;
  - §3.5.1;
  - §3.5.2.1 to §3.5.2.4;
  - §3.5.4.
- **PF12-Canon-HDE-Schemas-and-Artifacts:**
  - "Close-pack artifacts (deterministic path-of-record; baseline artifacts)";
  - "Change-container compatibility (normative)";
  - §8.17.
- **PF19-Canon-Glow-QA-Guide:**
  - "Close-pack truthfulness and same-run execution (normative)";
  - "Close report requirements (validator-bound; mechanical)";
  - §3.4.3.
- **PF04-Canon-HDE-Governance:**
  - §2.0.19;
  - the closeout-record list (deferrals, coverage ledger, accepted-deviation accounting, no-over-claim rule).
- **HDE Build Notes:** 2.13, 2.15, 2.16, 2.17, 2.19, 2.20, 2.24, and every later addendum on HDE-CRD-0002.
- **`docs/adr/hde/close_pack_writer_adr.md`:** "Decision" and "Stated limits", read with HDE Build Notes 2.17.
- **`AGENTS.md`:**
  - "Governed evidence rules";
  - "Evidence attribution, currentness and distinct decisions";
  - "HDE-EPIC039 current workflow posture";
  - "Pre-push check";
  - "PR descriptions".

Record in the result record every section you relied on. Never cite canon you did not read.

## Inputs (read in full)

| Path | What it is |
| :- | :- |
| `docs/ephemeral/HDE-CRD-0002-CL-C-10-closure-decision-v1.1.md` | The decision returning this work: B-4, the corrections to v1.0, and §4 |
| `docs/ephemeral/HDE-CRD-0002-CL-C-10-closure-decision-v1.0.md` | Delivered-scope disposition, retrospective, CR-9 and G-1 (§6), open items (§7), R-0 to R-7 (§8) |
| `docs/ephemeral/HDE-CRD-0002-CLOSE01-close-rehearsal-record-v1.0.md` | The rehearsal: method, outcomes, source-text rules RH-1 to RH-8 |
| `docs/ephemeral/HDE-CRD-0002-CLOSE01-reference-close-candidate-source-v1.0.json`, `docs/ephemeral/HDE-CRD-0002-CLOSE01-reference-doc-deltas-v1.0.md`, `docs/ephemeral/HDE-CRD-0002-CLOSE01-reference-drain-targets-v1.0.md` | The reference T1 inputs the rehearsal validated (with B-4 exempted) |
| `docs/ephemeral/HDE-CRD-0002-CLOSE01-rehearsal-driver-v1.0.py` | The rehearsal driver: a model of T1 to T6, the close-run publication call and the hosted job's checks |
| The ESC-40 `REMEDIATION_REVIEW` for B-4 and the remedy's PR-40 lineage review | The approved remedy and its acceptance; their paths are on `main` when this runs |
| `docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md` | §7 WU-PR-07 "Terminal-state reachability" (a) to (e); §9 item 5 |
| `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` and `docs/ephemeral/HDE-CRD-0002-specification-delta-v1.0.md` | S01 to S22; S01 removed |
| `docs/ephemeral/HDE-CRD-0002-QA50-qa-plan-v1.3.md` | Approved QA Plan v1.3: §6 matrix, §10 coverage, each check's "Surface / D-goal mapping:" line |
| The highest-version `docs/ephemeral/HDE-CRD-0002-QA120-qa-report-v*.md` and the QA-120 RCA | The authorized decision (verdict) and the RCA the summary lines come from |
| `audit/qa/hde-crd-0002/qa_step_logs_manifest.json` and the 21 primaries | The QA evidence of record |
| `schemas/close_candidate_source.v2.json`, `tools/qa/generate_epic_close_pack.py`, `tools/evidence/update_evidence_index.py` (`publish_crd_close_run_family`), `.github/workflows/epic-closeout-validation.yml` | The tools, as the remedy left them |

**Facts established at CL-C-10 v1.1.** Re-verify each one; do not rely on them.
- On `main` at `58a27859` there is no `audit/HDE-CRD-0002_*`, no `audit/docdeltas/hde-crd-0002_*` and no `audit/qa/hde-crd-0002/close/`.
- The QA step-logs manifest records 21 checks, all `PASS` (SHA-256 `203b8ca18c061a918f9ca25df0e9f4596cd770a2134e305cb21f235c2aed9874`). If ESC-40 required a re-verification, the current manifest and Report govern.
- The rehearsal's close-only diff was 38 paths. It selected the CI lanes `evidence` and `release`, with no changed tests.

## Allowed changes (Product Owner instruction for this PR)

This list is Nathan's explicit instruction for this pull request. Nothing outside it may be written.

1. **Causal inputs you author:**
   - `audit/HDE-CRD-0002_close_candidate_source.json` (schema `close_candidate_source.v2`);
   - `audit/docdeltas/hde-crd-0002_doc_deltas.md`;
   - `audit/docdeltas/hde-crd-0002_drain_targets.md`.
2. **Writer outputs:** `python tools/qa/generate_epic_close_pack.py --write` writes `audit/HDE-CRD-0002_close_report.md` and `audit/HDE-CRD-0002_MANIFEST.json`.
3. **Updater outputs:** `python tools/evidence/update_evidence_index.py` writes the Human Index, sentinel, Machine Mirror and its checksum, the orientation output, and the path proofs it owns.
4. **The close-run family** under `audit/qa/hde-crd-0002/close/<check_id>/`, written only by `tools.evidence.update_evidence_index.publish_crd_close_run_family`.
5. **RF-12.** Exactly these three replacements, each of whose old text must occur exactly once:
   - `README.md`: "the writer and the close-run family are capability only; no close pack or candidate source has been produced with this writer, under either schema, and no close-run family exists." → "the only close pack, candidate source and close-run family produced with this writer are HDE-CRD-0002's, under the v2 schema; no other has been produced, under either schema."
   - `AGENTS.md`: "The writer and the CRD close-run family are capability only: no close pack or candidate source has been produced with this writer, under either schema, and no close-run family exists; a close pack" → "The only close pack, candidate source and close-run family produced with this writer are HDE-CRD-0002's, under the v2 schema; no other has been produced, under either schema. A close pack"
   - `CHANGELOG.md`: "Capability only: no close pack or candidate source has been produced with this writer, under either schema, and no close-run family exists." → "Its first use is HDE-CRD-0002's own close pack, candidate source and close-run family, under the v2 schema; no other has been produced with it, under either schema."

   If the remedy changed any of these lines, stop and report (see "Stop conditions").
6. **The result record,** on its own branch (Execute step 11).

**Never change:**
- `audit/qa/hde-crd-0002/qa_step_logs_manifest.json` or anything under `audit/qa/hde-crd-0002/checks/`;
- `tests/evidence/test_evidence_index_missing_state.py`, `tests/evidence/test_evidence_skeleton.py` or `tools/qa/qa_harness.py` (FND-001 measure (2));
- any code, test, schema, workflow, ADR or `docs/pfcanon/` file.

Never hand-edit an Index, Mirror, hash sentinel, path proof, manifest, close report, close-run primary or orientation output.

## Execute

**Environment.**
- Use a full-history clone (`git rev-parse --is-shallow-repository` prints `false`) and CPython 3.12.
- Install what CI installs: `python -m pip install 'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e .`. Record `python -m pytest --version`.
- Run every repository tool under `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`, with `GIT_CONFIG_GLOBAL=/dev/null`.
- Capture each step's command line, exit status and output without a truncating pipe.

1. **Branch and preconditions (T0).** Create `close/hde-crd-0002-close01` from the current `origin/main` and record the base. Verify each precondition, and stop if any fails:
   - `docs/ephemeral/HDE-CRD-0002-CL-C-10-closure-decision-v1.1.md` and this prompt are on `main`;
   - an ESC-40 `REMEDIATION_REVIEW` approves a remedy for B-4;
   - its work unit's PR-40 lineage review accepts it;
   - the verification ESC-40 requires is recorded;
   - the highest-version QA-120 Report has `verdict: PASS`, and every ledger entry is `PASS`;
   - none of the close mutation set's output paths exists yet.
2. **T1: causal inputs, then commit C1.**
   - Start from the three reference files and copy them to their `audit/` paths. Then re-verify every value against the records on `main`, and change what no longer holds. Each check below is required:
     - **Current versions.** The Specification, QA plan, QA report and `plan_path` are each their family's highest tracked version (RH-7).
     - **Acceptance.** There is one row per S01 to S22. Each `MET` row binds `qa_manifest` and the primary of a `PASS` check whose current QA plan mapping names it. S01's row is G-1's (CL-C-10 v1.0 §6.2), and its limitation keeps G-1's substance. Each limitation is true of the records.
     - **The remedy.** Add one `allocation` row and one matching `deliverables` entry for the B-4 remedy's work unit and pull request. If the remedy produced records the source should bind, bind them.
     - **Deferrals and ledgers.** Deferrals CLC10-01 to CLC10-12 match the open items the current records hold. Add any new item, for example one ESC-40 named, with its ADR status (RH-3). The drain-targets ledger names every deferral ID. `follow_ups` stays empty (RH-2).
     - **ADR block.** It matches the ADR and HDE Build Notes as they now stand, including any amendment the remedy made.
     - **QA RCA summary lines.** They match the current QA-120 RCA.
     - **Text rules.** Every string obeys RH-1, and no string contains the current `HEAD` commit ID.
   - Write the source with `json.dumps(source, indent=2, sort_keys=True) + "\n"`. Validate it against `schemas/close_candidate_source.v2.json` with `jsonschema` before committing.
   - Apply the three RF-12 replacements.
   - Commit C1: the three inputs and the three RF-12 files only.
3. **T2 and T3, then commit C2.**
   - T2: `python tools/qa/generate_epic_close_pack.py --source audit/HDE-CRD-0002_close_candidate_source.json --write` on clean C1.
   - T3: `python tools/evidence/update_evidence_index.py`.
   - Commit C2.
4. **T4: same-run checks on clean C2.** Capture each of these seven:
   - the writer with `--check`;
   - `python tools/evidence/update_evidence_index.py --check`;
   - `python tools/evidence/orientation_demo.py --check`;
   - `ci/checks/check_mirror_schema.sh`;
   - `ci/checks/check_evidence_index_hash.sh`;
   - `python tools/evidence/validate_evidence_paths.py`;
   - `ci/checks/check_final_lf.sh`.

   Every one must exit 0, and the tree must stay clean.
5. **T5: the close-run family, then commit C3.**
   - Publish one `CheckResult` per captured T2, T3 and T4 step through `publish_crd_close_run_family(config, results, captured_at_utc=<the actual UTC time, second precision, ending Z>)`. Use `config = HarnessConfig(crd_id="HDE-CRD-0002", repo_root=<the updater's ROOT>)`, as the driver's `t5` block does.
   - Commit C3.
   - Prove `git diff --name-only C2 C3 -- audit/qa/hde-crd-0002/qa_step_logs_manifest.json audit/qa/hde-crd-0002/checks` is empty.
6. **T6: local re-validation on clean C3.**
   - Run the T4 set again; every check must exit 0.
   - Run the closeout workflow's seven checks under an interpreter with `requirements.txt` only, in that workflow's environment. Run the writer's `--check` with `jsonschema` only.
   - Run `python tools/ci/prepush_check.py lanes build-notes`, then `membership` with one `--path` per changed path.
   - Run the evidence-lane and qa-lane selections of `.github/workflows/ci.yml`. The evidence lane took about 19 minutes in the rehearsal.
   - The tree must stay clean.
7. **Failures before publication.** Nothing is pushed until step 6 passes.
   - If a step fails because of a causal input, reset the branch to its base and restart at T1 (Plan restart rule).
   - Record every local attempt, with its failing command and output, in the result record. Never repair a later step's output by hand.
   - A tool failure is a stop condition.
8. **Adversarial self-review.**
   - Re-read the diff against "Allowed changes".
   - Confirm that every claim in the close report rests on a bound tracked input or on same-run evidence in this PR.
   - Confirm that no QA byte changed, that the three FND-001 files are unchanged and that no token name was minted.
9. **Publish.** Push and open one pull request from `close/hde-crd-0002-close01` to `main`.
   - Title: `HDE-CRD-0002 CLOSE01: close mutation set — close pack, ledgers, close-run family`.
   - Body: follow `.github/pull_request_template.md` as `AGENTS.md` "PR descriptions" defines it. Add the "Repo index and acceptance crib notes" and the "Doc-Delta note" that PF06 §3.5.2.4 requires.
   - "What merging does": merging makes HDE-CRD-0002's close pack, its ledgers, the close-run family and their Index and Mirror registration current on `main`. It does not establish Isis closure, PF30 movement, canon drainage or board state.
10. **T7: drive to green.**
    - Subscribe to the PR's activity.
    - CI's `test` job must pass on the exact head and end `CI_APPLICABILITY_AND_EXACT_HEAD_OK`. The evidence lane must pass on it (FND-001 measure (2)).
    - Ask Nathan to dispatch `.github/workflows/epic-closeout-validation.yml` with `git_ref` set to the exact 40-character head and `candidate_source` set to `audit/HDE-CRD-0002_close_candidate_source.json` (CL-C-10 v1.0 R-7). Record its result.
    - Bringing `main` in restarts at T2: merge `main`, then repeat steps 3 to 6 as new commits.
    - Never use `[skip ci]`, push an empty commit or skip a test.
11. **Result record.** On a separate branch that touches only `docs/ephemeral/`, write `docs/ephemeral/HDE-CRD-0002-CLOSE01-close-mutation-set-result-v1.0.md`. It holds:
    - the PR number, base, C1, C2, C3 and final head;
    - every command with its exit status, including failed local attempts;
    - the T4 and T6 results;
    - the hosted `test` job and closeout-workflow results;
    - the T1 deviations from the reference inputs, with reasons;
    - the close report's posture;
    - the measures as observed (the WU-PR-07 measure as CL-C-10 v1.1 §4 states it, and FND-001 measure (2));
    - limitations, nonclaims and canon relied on;
    - a `GCFPE_PROMPT_USES`-style entry naming this prompt by path.

    Open it as its own pull request and read it back. Keeping it separate keeps the close PR's validated head unchanged.

## Stop conditions (terminal return to the Product Owner, no workaround)

- A precondition of step 1 fails.
- The writer, the updater or a validator refuses for a reason that is not a causal input you may correct, including any reappearance of B-4.
- The schema cannot express a required close-report element.
- An RF-12 old text does not occur exactly once.
- A step would change QA evidence, a protected file, or anything outside "Allowed changes".
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
Destination: CL-C-10 — Perform CRD Retrospective and Decide Closure — 100926.1
https://app.notion.com/p/3f44590a05eb819b8022f2a4cdd3b022
Receiving role: Isis, the continuing Lead Developer and terminal closure authority for CRD HDE-CRD-0002 (https://claude.ai/code/session_01NxRhYei7RDGmMPYdKEkpok); decide closure on the close mutation set CLOSE01 produced.
Change: HDE-CRD-0002 (CRD).
Manual prerequisite: the Product Owner has merged close PR amthorn78/glow-hdengine-v2#<number> into main. Paste this only after that merge.

Inputs:
- docs/ephemeral/HDE-CRD-0002-CLOSE01-close-mutation-set-result-v1.0.md — CLOSE01 result: close PR, commands, validators, CI, closeout workflow, measures
- docs/ephemeral/HDE-CRD-0002-CL-C-10-closure-decision-v1.1.md — DO_NOT_CLOSE decision whose return work CLOSE01 completed
- docs/ephemeral/HDE-CRD-0002-CL-C-10-closure-decision-v1.0.md — retrospective, delivered scope, CR-9 and G-1
- <b4-review-path> — ESC-40 remediation review approving the B-4 remedy
- docs/ephemeral/HDE-CRD-0002-CLOSE01-close-rehearsal-record-v1.0.md — rehearsal and finding B-4
- docs/ephemeral/HDE-CRD-0002-QA120-qa-report-v1.0.md — final QA Report, verdict PASS
- docs/ephemeral/HDE-CRD-0002-QA120-qa-rca-v1.0.md — final QA RCA
```

Before emitting:
- replace `<number>` with the close PR's number;
- replace `<b4-review-path>` with the remediation review's repository path;
- if a later QA-120 Report or RCA version exists, name it instead of v1.0.

The block may carry no other placeholder.

## TypeSafe reading for this session

Action sent (v8.2): "In a dedicated session, produce one new close pull request for an already QA-passed change request of 22 requirements, after a separate remedy to the close-pack writer has landed: verify and adopt a rehearsed reference close-candidate source and two short ledgers against the current records, update three documentation lines, then run the existing governed close-pack writer, the evidence-index updater, seven read-only validators and the close-run evidence publisher in a fixed, already approved step sequence under closed rails, re-validate locally, and hand the exact head to hosted CI and one manual validation workflow. An approved step list and a passing rehearsal exist; no product code changes and no live run against a provider occurs; the closure decision is re-run independently after the Product Owner merges."

The reading as printed by the script:

- **TypeSafe v8.2: Opus 5.5 at high.**
  - Effort score 2.31 (confidence 0.53). Rung probabilities: low 0.01, medium 0.23, high 0.21, extra high 0.54, max 0.01, ultracode 0.00.
  - Model probabilities: Fable 5.1 0.00, Opus 5.5 0.97, Sonnet 5.5 0.03, Haiku 5.5 0.00 (confidence 0.96).
  - Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.000, Fable 5.1 at high 0.000, Fable 5.1 at extra high 0.000, Fable 5.1 at max 0.000, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.010, Opus 5.5 at medium 0.223, Opus 5.5 at high 0.204, Opus 5.5 at extra high 0.524, Opus 5.5 at max 0.010, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.000, Sonnet 5.5 at medium 0.007, Sonnet 5.5 at high 0.006, Sonnet 5.5 at extra high 0.016, Sonnet 5.5 at max 0.000, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000.
  - Flags: none printed.
  - Sent 2026-10-26T02:05:22Z. Nathan picks the cell.
- **Detail (as printed):** v8.2 sent 2026-10-26T02:05:22Z; HTTP 200 in 0.19 s; 5497 input and 71 output tokens; jev-1.13.0. Rung by rule: high (nearest to the score, halves up); model by rule: Opus 5.5 (the most probable of the four options, a tie going to the higher-priced model).
- **Which request:** the installed skill's request v8.2 and `score_v8.py`, run once with session kind `review` and label "HDE-CRD-0002 CLOSE01 close mutation set (one-time task prompt v1.0)". No Notion row was written.
- **Picks.** Nathan's pick is not stated.
- **Supersedes** CL-C-10 v1.0 §14's reading, whose action assumed the writer works.

**Surface advice.**
- **Session.** A dedicated top-level Claude Code cloud session that Nathan creates. It is not a subagent, and it is separate from the Isis, Thoth and QA sessions.
- **Environment.** A full-history clone; CPython 3.12 with CI's install; a second interpreter with `requirements.txt` only and a third with `jsonschema` only; `ruby`, `bash` and `curl` on `PATH`. Allow about 20 minutes for the local evidence-lane run.
- **Access.** GitHub write for one branch and two pull requests. Nathan dispatches the closeout workflow. No production, Railway, vendor or database access.
