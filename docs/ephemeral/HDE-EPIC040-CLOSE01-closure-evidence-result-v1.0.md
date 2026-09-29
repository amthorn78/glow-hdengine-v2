---
artifact_type: ONE_TIME_TASK_RESULT
artifact_version: "1.0"
logical_id: HDE-EPIC040-CLOSE01-CLOSURE-EVIDENCE-RESULT
work_unit_id: HDE-EPIC040-CLOSE01
change_id: HDE-EPIC040
change_class: EPIC
task_prompt: docs/ephemeral/HDE-EPIC040-CLOSE01-closure-evidence-task-prompt-v1.0.md (v1.0; SHA-256 9ce3e4fb6a8bc51d00a206a6727b03e9f9f80ca1fe8bbb1d5a771751e4d49bb5)
ordered_by: docs/ephemeral/HDE-EPIC040-CL-E-10-closure-decision-v1.1.md (DO_NOT_CLOSE; return work R-1 to R-5; SHA-256 7c9a26e6e091bd51d4484cb4ee7413c670e5402db510dce6fee4b92b7b049f14)
proceed: Product Owner paste of the task prompt, 2026-09-29, with the stated prerequisite amthorn78/glow-hdengine-v2#556 merged (verified: d817abe on main)
execution_identity: https://claude.ai/code/session_01L7cH6zzbYhhwKE7fWdxp13
capture_time: 2026-09-29T18:55:08Z
repository_head_read: origin/main d817abe1b40a1b57d4fa41a933db911c5701d3fc
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.4.9.md (SHA-256 83308abf41c507301b9f821ca1dc581e9c5a7670a2fe2df038b325535dce6a4e; 478,593 bytes)
result: STOPPED_TERMINAL
stop_conditions_met:
  - "The generator or its schema cannot express a required close-report element."
  - "No admitted home exists for the execution evidence."
close_pr: NONE (not opened)
close_branch: NONE (close/hde-epic040-close01 was not created on origin)
repository_mutation_by_this_task: this record only (docs/ephemeral/)
---

# HDE-EPIC040-CLOSE01 — Result: stopped on two stop conditions, v1.0

## 0. Result

| Field | Value |
| --- | --- |
| Result | **`STOPPED_TERMINAL`**: returned to the Product Owner under the prompt's "Stop conditions". No workaround was attempted |
| Blocker B-1 (decisive) | `tools/qa/generate_epic_close_pack.py` and `schemas/epic_close_candidate_source.v1.json` cannot express the close-report elements that the prompt's step 4 and canon require (§1.1). The prompt allows only that generator to write the close report and forbids hand-editing its output |
| Blocker B-2 (independent) | No admitted home exists for same-run close-workflow evidence under `audit/qa/hde-epic040/` without adding a check to `qa_step_logs_manifest.json`, which the prompt forbids (§1.2) |
| Feasible, not performed | R-1 (land the 41 evidence files byte-identical) and R-2 (updater registration) are both feasible. R-1 was proven in a local scratch worktree only (§2). Nothing was pushed, because the close mutation set cannot be completed and a partial close branch would carry governed evidence changes that no PR in this work unit could finish |
| What remains open | The three closure prerequisites of CL-E-10 v1.1 §2 are all still open: QA evidence not on `main`; QA50-F01; no close pack |
| Owner | Product Owner: the route decisions in §4. The blockers are in shared closeout tooling (HDE-EPIC039 capability), not in HDE-EPIC040's delivered scope |
| Resume point | CLOSE01 step 1, under a revised one-time prompt that reflects the §4 decisions. Nothing needs to be undone |

## 1. Blockers

### 1.1 B-1: the close-pack generator cannot express the required close report

**Stop condition met:** "The generator or its schema cannot express a required close-report element. Do not hand-edit the output."

**What the generator does.** It is HDE-EPIC039's epic-agnostic "closeout-candidate" writer and checker (`README.md` line 25; `docs/EVIDENCE_INDEX.md` line 56; `AGENTS.md` "HDE-EPIC039 current workflow posture"). The report it writes contains only:
- a fixed title and one fixed sentence;
- "Source bindings" (path, SHA-256 and size of each declared input);
- the source's `report_sections`;
- "Output bindings";
- "Explicit nonclaims".

**Why it cannot carry the required content** (all read at `d817abe`):

| Constraint | Location |
| --- | --- |
| A section heading must be one of four fixed labels: "Candidate boundaries", "Delivered scope", "Evidence posture", "Validation posture" | `tools/qa/generate_epic_close_pack.py:60` `REPORT_SECTION_HEADINGS`; enforced at `:1930` and `:1966`; schema `$defs.causal_report_heading` enum (line 194) |
| Every body line must be one of ten fixed sentences about candidate publication mechanics, for example "Candidate validation compares exact committed bytes." | `:66` `REPORT_BODY_LINES`; schema `$defs.causal_report_body_line` enum (line 167) |
| A heading may contain only `[A-Za-z0-9 _.,:;()/+'-]`, so the em dash in the required heading is rejected even if the enum were widened | `:96` `REPORT_HEADING_RE` |
| All five fixed nonclaims are mandatory. One renders as "No QA PASS, acceptance, or token satisfaction is claimed." | `:124` `NONCLAIM_TEXT`, `:139`; schema `nonclaims` `minItems` 5 (line 60) |
| The manifest carries `"candidate_posture": "candidate_only"` and an `outputs` map, not a `key_outputs` map | `:2146`, `:2161` |
| Tests pin these closed sets and assert that other headings or lines fail with `REPORT_SECTION_AMBIGUOUS` or `REPORT_NONCLAIM_CONTRADICTION` | `tests/qa/test_generate_epic_close_pack.py:418`, `:422`, `:743`, `:779` |

**Required elements the report therefore cannot carry:**

| Required element | Source of the requirement |
| --- | --- |
| Exact-source acceptance section binding AC040-01 to AC040-09 to the final candidate, checks, evidence, results and limits | Change Process Guide §3.5.2.1; prompt step 4 |
| Verification statement that the baseline artifacts exist at their canonical filenames | Change Process Guide §3.5.2.1 |
| Tracked-issue (`TI-*`) mapping, or a statement that none is cited | Change Process Guide §3.5.2.1 |
| Binary `SATISFIED` / `NOT SATISFIED`, labelled as formal close-pack posture | Change Process Guide §3.5.2.1; HDE Schemas & Artifacts, close report rules |
| Shipped deliverables; dedicated deferrals section with drain-target pointers or ADR status | HDE Schemas & Artifacts, "Close-pack artifacts" |
| Later-drain PF-canon statements in the exact vocabulary; separation of PF09 recorded status, later-drain status, implemented, OPS and evidence states | Same |
| Full approved PF09 scope (HDE-SEPA005 and .1 to .5) | Change Process Guide §3.5.2.4; HDE Schemas & Artifacts |
| Pointer to the manifest's `key_outputs` map (the generated manifest has none) | HDE Schemas & Artifacts, "Close-pack artifacts" |
| The QA RCA & Doc Delta summary, or a reference by exact path to `audit/EPIC-040_QA_RCA.md` | Change Process Guide §0.4.1.2 "Location"; §3.5.2.8 |
| The heading `QA Rails — Open/Close (Final PR)` verbatim, and an "Acceptance and evidence pointers" list | Glow QA Guide, "Close report requirements (validator-bound; mechanical)" |

In addition, the mandatory nonclaim "No QA PASS, acceptance, or token satisfaction is claimed." would contradict the exact-source acceptance section that the same report must carry.

**Externalizing the RCA does not help.** `audit/EPIC-040_QA_RCA.md` is not an output of this generator, the prompt authorizes no other writer for it, and the close report would still have to reference it by path, which it cannot.

**Other writers.** Only epic-specific tools emit the required heading: `tools/qa/epic021_qa.py` and `tools/qa/run_hde_epic024_harness.py`. The epic-specific generators `generate_epic025` to `generate_epic029_close_pack.py` belong to other epics. None is authorized by this prompt (Allowed changes, item 5).

PF10 v13.4.9 was searched for `generate_epic_close_pack`, `close-pack`, `close report`, `closeout candidate`, `EPIC039` and `SATISFIED`. It contains no rule that modifies these close-report requirements or the generator's scope, so the requirements above govern.

### 1.2 B-2: no admitted home for same-run close-workflow evidence

**Stop condition met:** "No admitted home exists for the execution evidence."

- **Canon.** Close-workflow execution evidence must be preserved under the epic QA root as step-scoped mechanical outputs (Glow QA Guide, "Close-pack truthfulness and same-run execution"; §3.4.12: outputs go under `audit/qa/<epic-id>/checks/<check_id>/` as the check's `primary.log` or check-scoped sidecars). Each check that produces evidence has exactly one primary log referenced by the manifest for that check (Glow QA Guide §4.4.4).
- **Tooling.** `tools/qa/qa_harness.py` publishes a check only through the manifest (`_preflight_manifest(config)` at lines 2041 and 2467).
- **Precedent.** Earlier close workflows were manifest-listed checks: HDE-EPIC027 `gate_update_evidence_index_write`, `gate_orientation_demo_check` and the other `gate_*` checks; HDE-EPIC029 `po-precommit` and `po-postcommit`.
- **The prompt forbids every admitted option.** A new check needs a new entry in `qa_step_logs_manifest.json`. Adding sidecars to an existing check changes one of the 12 check directories. Both are forbidden ("Never modify the 12 existing check directories, `qa_step_logs_manifest.json`, or any byte from `787bb97`"). `00_meta/` holds only the doc-delta copy and, by canon, Moon Loop `delta/` records. Any other location would be a new evidence family, which the prompt forbids.

## 2. Verified and feasible parts (nothing pushed)

### 2.1 R-1: landing the QA evidence

Each CL-E-10 fact was re-verified at `d817abe`:

| Fact | Result |
| --- | --- |
| Evidence branch head | `origin/qa/hde-epic040-qa100-plan-v1.2-run-20260929` = `787bb97b58b638d6b307cad6d76484c883c58aec` |
| Run A branch, not used | `origin/qa/hde-epic040-qa100-plan-v1.2` = `e5b671c4fd28bbce31ac0ce3cd46e1bc39fa077c` |
| Paths added over tested source `0db3f0ef` | 41, all `A`: 39 under `audit/qa/hde-epic040/`, plus `audit/docdeltas/hde-epic040_doc_deltas.md` and its path proof |
| `0db3f0ef` is an ancestor of `origin/main`, and is the merge base with the evidence branch | Yes |
| Paths `main` changed since `0db3f0ef` | Only `docs/ephemeral/` (41), `docs/pfcanon/` (1) and `docs/prompt_ecosystem_management/` (2). `main` moved from `c48a79a` to `d817abe` by amthorn78/glow-hdengine-v2#556, which adds five files under `docs/ephemeral/` only |
| `audit/EPIC-040_*`, `audit/docdeltas/hde-epic040_drain_targets.md` | Absent |

Byte-identity proof, in a detached scratch worktree of `origin/main` outside the repository (removed afterwards):

| Command | Exit |
| --- | --- |
| `git merge --no-ff --no-edit origin/qa/hde-epic040-qa100-plan-v1.2-run-20260929` | 0 (no conflict) |
| `git diff --exit-code 787bb97b58b638d6b307cad6d76484c883c58aec HEAD -- audit/qa/hde-epic040 audit/docdeltas/hde-epic040_doc_deltas.md audit/docdeltas/hde-epic040_doc_deltas.md.path_proof.txt` | 0 |
| `git diff --name-only origin/main HEAD` | 41 paths |

### 2.2 R-2: updater registration pattern (QA50-F01)

- **Before (unchanged):** no HDE-EPIC040 QA registration exists in `tools/evidence/update_evidence_index.py`, the Human Evidence Index or the Machine Mirror (QA Audit L-44 and QA50-F01; QA-120 Report §6).
- **Admitted pattern found:** a per-epic list of `artifact_key`, `discovered_physical_path` and `epic_id` entries, for example `EPIC029_PRIMARY_ARTIFACTS` at `tools/evidence/update_evidence_index.py:664`. It covers the QA manifest, doc deltas, drain targets, close report, close manifest and check primary logs. The list is spread into the Human Index load (`:3854`) and mirrored by a target list in `tests/ops/test_evidence_index.py:44` (`EPIC029_TARGETS`).
- **Consequence:** registration needs no design decision, so it is not a stop condition. It was not applied. Registering the close-pack paths before a close pack exists would point Index rows at files that do not exist.

## 3. Commands and checks run

All commands were read-only in the repository (`git fetch`, `git rev-parse`, `git merge-base`, `git diff`, `git show`, `grep`, `sed`, `sha256sum`), except the scratch worktree merge in §2.1, which was outside the repository tree and removed.

| Check | Result |
| --- | --- |
| `git merge-base --is-ancestor 0db3f0ef… origin/main` | 0 |
| Scratch merge and byte-identity diff | 0 and 0 (§2.1) |
| Prompt step 7 read-only validators, updater tests, close-pack generator tests | **Not run.** No governed byte was changed, so there was nothing to validate. `requirements-dev.txt` was not installed and `python -m pytest --version` was not recorded, because no pytest-dependent check ran |
| CI | None. No close PR exists. The PR carrying this record changes `docs/ephemeral/` only, which `ci/checks/classify_ci_changes.py` exempts from every lane (`AGENTS.md`, "Code review scope") |
| `.github/workflows/epic-closeout-validation.yml` | Not dispatched, since there is no candidate |

## 4. Decisions needed from the Product Owner

| # | Question | Effect if left open | Recommendation |
| --- | --- | --- | --- |
| D-1 | How is a canon-conforming close report to be written for HDE-EPIC040? | No close pack can be produced, so CL-E-10 cannot record `CLOSE` on the v1.1 basis. The same gap applies to every later epic that uses the generic generator | (a) Authorize a bounded tooling work unit that lets the governed generator (or a new governed writer beside it) render the required elements, then reissue CLOSE01 |
| D-2 | Where does same-run close-workflow evidence live? | R-4 cannot be met without a manifest change | Allow one new manifest-listed check (for example `close-gate-workflow`) written through `tools/qa/qa_harness.py`, as HDE-EPIC027 and HDE-EPIC029 did |
| D-3 | Should R-1 and R-2 land now as an evidence-only QA PR? | Two of the three missing parts stay open until D-1 is delivered | Yes. Change Process Guide §3.5.2.8 permits "an evidence-only QA PR … that merges before the close PR", with the Index and Mirror trio in the same mutation set. §2 shows it is ready |

Options for D-1:
- **(a) Tooling work unit.** Extend `schemas/epic_close_candidate_source.v1.json` and `tools/qa/generate_epic_close_pack.py`, or add a separate governed close-report writer. It must be able to render the §1.1 elements, remove or scope the "No QA PASS…" nonclaim for a final close pack, and emit `key_outputs`. Cost: implementation, tests, review and CI on heavily tested tooling (a 4,274-line test file). HDE Schemas & Artifacts requires such generator changes to go "through the authorized change lane". This fixes the gap for later epics too.
- **(b) Exceptional closure record.** Only the Product Owner may authorize this (Change Process Guide §3.5.1). It closes HDE-EPIC040 outside ordinary Close Gate completion and must list every Close Gate element not achieved. Cost: no close pack for this epic, and the tooling gap stays open for the next one.

Recommendation: (a), with D-3 done first so the evidence and QA50-F01 are no longer waiting on the tooling.

## 5. Limitations

- **Inputs not read in full.** QA Plan v1.2, the QA Audit, the QA-110 review and Specification v1.1 were read only in the passages cited here: QA50-F01, L-44, LR-01, and the AC040 criteria as restated in QA Report §7.1. Neither blocker depends on them. They must be read in full before a close report is authored.
- **R-1 is proven only in a scratch worktree** at `d817abe`. It must be re-proven on the actual branch when the work resumes.
- **Registration read, not tested.** The registration pattern was read from source, and its tests were not run.

## 6. Nonclaims

- No close pack, Index or Mirror change, path proof, evidence landing, QA50-F01 closure or Close Gate completion.
- No Isis closure, PF09 movement, canon drainage, board state, deployment, live-database or deployed-service claim, and no ledger-bound manifest claim.
- No PF-Canon edit and no PF10 addendum. No QA rerun, Ops, or vendor or database call.
- Merging the pull request that carries this record preserves the record and approves nothing (D21-C).

## Canon relied on

Read on `main` at `d817abe` (`docs/pfcanon/`).

- **PF06-Canon-Change-Process-Guide v2.5.3.** Read in full: §0.2; §0.4.1, §0.4.1.1 to §0.4.1.3; §3.5.1; §3.5.2.1 to §3.5.2.4; §3.5.2.8.
- **PF12-Canon-HDE-Schemas-and-Artifacts v2.9.5.** Read in full: "Close-pack artifacts (deterministic path-of-record; baseline artifacts)", including "Acceptance-binding family coherence" and "Evidence generator PASS coupling". Searched, not read in full: the Human Evidence Index, Machine Mirror and path-proof statements (search hits at lines 26 to 96, 385 and 394). §8.3 was not read; nothing here depends on it.
- **PF19-Canon-Glow-QA-Guide v3.0.5.** Read: "Close-pack truthfulness and same-run execution"; "Close report requirements (validator-bound; mechanical)"; §3.4.12; §3.4.13; §4.3.1; "Bounded step-cluster manifest generation"; "Manifest ledger-coverage proof"; the §4.4.4 opening rule; the close-pack truthfulness learning in the HDE-EPIC027 learnings.
- **HDE Build Notes v13.4.9.** Searched as stated in §1.1. No overriding rule was found.
- **PF27-Canon-Plan-Templates v2.0.4 §10.** Not read at this invocation, and not relied on.
- **`AGENTS.md`.** "Canon-first rule"; "Governed evidence rules"; "Evidence attribution, currentness and distinct decisions"; "HDE-EPIC039 current workflow posture"; "PR descriptions"; "Code review scope".

In-flight documents read in full: the task prompt; CL-E-10 decisions v1.1 and v1.0; QA-120 Report v1.0 and RCA v1.0. Read in part: see §5.

## Provenance

GCFPE_PROMPT_USES:
- Usage ID: HDE-EPIC040-CLOSE01-USE-01.
- Change: HDE-EPIC040 (EPIC), Specification v1.1; scope HDE-SEPA005 and .1 to .5.
- Prompt: `docs/ephemeral/HDE-EPIC040-CLOSE01-closure-evidence-task-prompt-v1.0.md`, v1.0, a one-time task prompt with no Notion page.
- Role and stage: implementing agent, HDE-EPIC040-CLOSE01.
- Capture time: 2026-09-29T18:55:08Z.
- Execution identity: https://claude.ai/code/session_01L7cH6zzbYhhwKE7fWdxp13.
- Result: `STOPPED_TERMINAL` (B-1, B-2).
- Repository persistence: PENDING / NON_GATING. No `docs/changes/GCFPE_PROMPT_PROVENANCE.md` procedure exists on `main` at `d817abe`.
