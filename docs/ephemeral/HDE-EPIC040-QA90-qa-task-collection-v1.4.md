---
artifact_type: QA_TASK_COLLECTION
artifact_id: HDE-EPIC040-QA90-QA-TASK-COLLECTION
artifact_version: "1.4"
predecessor: docs/ephemeral/HDE-EPIC040-QA90-qa-task-collection-v1.3.md (TASK_READY; task T11, executed and ACCEPT at QA-110; SHA-256 c4ae999f9a38b7bcfabb66ac92ae542a1754682debd17fbd87c18fcc936de16b; preserved unchanged and not superseded). docs/ephemeral/HDE-EPIC040-QA90-qa-task-collection-v1.1.md remains the issued source of T01 to T10
state: TASK_READY
AUTHORING_CONTEXT: APPROVED_BASE_WITH_OVERLAYS
change_class: EPIC
change_id: HDE-EPIC040
change_name: Separation Pass 3
author: Kronos-23, continuing QA authority for HDE-EPIC040
session_disposition: RETAIN_EXISTING
role_session_ref: Kronos-23, Product Owner-selected continuing QA session (execution identity https://claude.ai/code/session_01PnD4YNbFZStRQWZ7TCM6jV)
invocation_binding: EPIC / HDE-EPIC040 / QA-90 / QA_PLAN v1.2 check 12
context_conflict: NONE
execution_posture: MANUAL_PROMPT_EXECUTION
prompt: QA-90 — Create Bounded QA Execution Task — 091426.1 (Notion 3db4590a05eb811e8582cf30238c5b9c; page as of 2026-09-24T15:56:22.252Z; read in full at this invocation)
ecosystem_release: GCFPE-20260914.1 (091426.1)
approved_base: docs/ephemeral/HDE-EPIC040-QA50-qa-plan-v1.2.md (QA_PLAN v1.2; SHA-256 330ffadf7e83a99259780a0e73c63f7b7084ddd131cb9c460eb8c29f5d714010; immutable)
approving_review: docs/ephemeral/HDE-EPIC040-QA70-qa-plan-review-v1.4.md (APPROVE by Isis-52, 2026-09-28T00:26:24Z; SHA-256 e2c3f7d4003dff36aa864e2a83556abf36cfa879a49dbbdfa2b227a53eb1c025)
qa_audit: docs/ephemeral/HDE-EPIC040-QA50-qa-audit-v1.0.md (SHA-256 1c561fea4668487005e4b857ccf54c024184898220176c62a61d037ca662e3df)
qa_evidence_reviews: docs/ephemeral/HDE-EPIC040-QA110-qa-evidence-review-v1.0.md (T01 to T10 ACCEPT; ruling LR-01; lessons K-01 to K-04; SHA-256 2d45e7f0d252a3009ffb9cc0fe3d51b9652a7929eeb798bd618f2c497ab34ac3); docs/ephemeral/HDE-EPIC040-QA110-qa-evidence-review-t11-v1.0.md (T11 ACCEPT; constraints on this task in its section 6; lessons K-05 and K-06; SHA-256 c7abc4441a87d942c471ffcaa5388599e876263b3d26b5d740464200ac24ac64)
execution_results: docs/ephemeral/HDE-EPIC040-QA100-qa-execution-results-t11-v1.0.md (the executor, venue, checkout, virtual environment and evidence branch that check 12 continues; SHA-256 0c884e8f6e56fdf959c68ec77860faef60ac1d2899494231745a3594e0dfe397)
selection: Product Owner, "Selection: check 12" in the QA-90 handoff of 2026-09-29 = QA Plan v1.2 check 12 `qa-closeout-deliverables`
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.4.5.md on main at 633ca5d (SHA-256 aa5ef8812c68b2b107e3da2bbc0c566f399559ab74de076728d350c4fa7860d7)
observed_revision: 633ca5d340110d8058b795c366f6041bd0747929 (origin/main at authoring; `git diff --name-only` from the tested source 0db3f0ef33e7a7a3aa85a2c221e06ac5581c7b8d lists only files under `docs/ephemeral/`, `docs/pfcanon/` and `docs/prompt_ecosystem_management/`). The QA-110 review of T11 and its checkpoint are on the working branch in pull request amthorn78/glow-hdengine-v2#552, not yet on main
routing: QA-100 — Execute Bounded QA Task — 091426.1, in the operator session the Product Owner opens with this collection's handoff
PF10_ADDENDUM_OUTPUT: NOT_PRODUCED_BY_QA-90 (QA-90 is not an addendum producer)
---

# HDE-EPIC040 — QA Task Collection v1.4 (QA-90): check 12 of QA Plan v1.2

## 1. Result

| Field | Value |
| --- | --- |
| Result | `TASK_READY` |
| Task | T12 `qa-closeout-deliverables`, Plan v1.2 check 12, attempt 1 (§4.2) |
| Selection | Product Owner "Selection: check 12" = Plan check 12 only. Checks 1 to 11 are executed and accepted and are not re-issued (§3) |
| Pre-execution findings | None. No `QA_PREEXECUTION_FINDING`: the Plan's check 12 block is complete, its dependency holds (checks 1 to 11 recorded), and every locus it uses exists at the tested source (§2.4, §2.5) |
| Normalizations | N-36 to N-45 (§4.10), plus N-01, N-02, N-03, N-05 and N-06 carried from collection v1.1. None changes the Plan's objective, target, rails, evidence identity or predicates |
| Applied from QA-110 review v1.0 | LR-01 item 6 (Run B checkout and branch); K-01 (no empty argument), K-02 (one command per fenced block), K-03 (`origin` checked before the first command), K-04 (dry-run through `CheckResult`; the recording is not a check command) |
| Applied from QA-110 review T11 v1.0 | Section 6 constraints: Run B checkout and branch at `380cf46`; the manifest predicate counts checks 1 to 11; T11's `DOC_DELTA:` line becomes DD-13; the path proofs cover T11's primary log with the ten earlier ones; the CLOSED prefix on every command; K-05 (not applicable: no vendor configuration is used) and K-06 (the executor identity comes from a captured file, never fixed text) |
| Authoring dry run | Every command block of §5 was extracted from this file and run in a scratch clone of the Run B branch at `380cf46` in seven scenarios, recorded through the real `record_check` wherever the task records; four draft defects were found and fixed (§2.4) |
| Evidence storage | Branch `qa/hde-epic040-qa100-plan-v1.2-run-20260929`, one fast-forward commit of 19 files, pushed, no pull request by the executor (§4.8) |
| Next stage | QA-100 — Execute Bounded QA Task — 091426.1, in the operator session the Product Owner opens with the handoff of this collection |
| Not done by QA-90 | Execution, evidence acceptance, a PASS declaration, selection of any step, a rerun, merge, PF-Canon or PF10 edits, addendum production |

## Canon relied on

Read from `docs/pfcanon/` on `main` at `633ca5d`; the working branch carries no change to `docs/pfcanon/`.

- **HDE Build Notes v13.4.5** (`docs/pfcanon/PF10-HDE-Build-Notes-v13.4.5.md`). Whole-document search at this invocation for `path proof`, `path_proof`, `qa-closeout`, `check 12`, `close-out`, `closeout`, `coverage accounting`, `doc delta`, `qa_step_logs_manifest`, `validate_evidence_paths` and `update_evidence_index`. The governing hit is 2.32 "HDE-EPIC040-QA110 — QA Evidence Review v1.0 (tasks T01 to T10 of QA Plan v1.2)": ruling LR-01 item 6 (checks 11 and 12 run in the Run B checkout and store on the Run B branch), lessons K-01 to K-04, routing of unissued checks to QA-90 on the Product Owner's selection, and "Path proofs remain unproduced until check 12". The other hits (2.6, 2.10, 2.12, 2.15, 2.19, 2.20, 2.23, 2.27, 2.28, 2.29, 2.33) record other work, list nonclaims or name path proofs as evidence companions; none sets a rule for check 12. Also relied on: 2.29 "PF10-CANON-001" (canon location; change documents in `docs/ephemeral/`); 2.34 "PF10-VENDOR-001", read in full at QA-110 T11 in this session: T12 makes no vendor call, and under its rule 4 the vendor configuration stays in the QA console's environment, so every T12 command carries the CLOSED prefix. PF10 sets no rule for path-proof writing, the doc-delta append or coverage accounting, so the documents below govern.
- **Glow QA Guide** (`docs/pfcanon/PF19-Canon-Glow-QA-Guide-v3.0.5.md`), each read in full at this invocation: §3.4.3 "Evidence layout: current-state first" (the manifest path proof is "required whenever the step-log manifest is created, refreshed, or governed"; a primary-log path proof is "Required whenever the primary log is governed evidence"; path grammar; no wildcard exception); §4.4.1 to §4.4.7 (current-state root; manifest requirements; bounded step-cluster manifest generation; "Manifest ledger-coverage proof": a ledger-bound claim needs lookup proof in the updater, the Human Evidence Index and the Machine Mirror, and a refreshed manifest path proof alone is not sufficient; non-empty primary logs; reconstruction from the primary log); §9.2.15.5 "Coverage vs QA Plan accounting". As read earlier in this session: §3.1.2, §3.3, §3.4.7 to §3.4.10, §10.6, §10.8, §11.1.
- **HDE Governance** (`docs/pfcanon/PF04-Canon-HDE-Governance-v2.8.6.md`): §2.0.19 "QA bootstrap & harness (EPIC021+)", `QA_LIVE_QA_RUN_OK` governance semantics and "KISS required outputs", read in full at this invocation: a check's manifest entry is derived from its own `primary.log` header; when the manifest bytes change, the co-located manifest path proof is refreshed from the new bytes "before the step is treated as complete"; the path proof records at least `path`, `size_bytes` and `sha256`; a ledger-coherence claim needs the updater's exit 0 and positive discoverability in three loci.
- **Change Process Guide** (`docs/pfcanon/PF06-Canon-Change-Process-Guide-v2.5.3.md`): §0.6.7 "Mechanical evidence (Live QA)" (the step-logs manifest is a governed artifact with a sibling path proof; a step that updates the manifest SHOULD show the entry in its primary log) and §1.1.4 "Live QA mechanical evidence expectations" (a step reusing the governed header or manifest workflow shows "that the step's manifest entry and sibling path-proof were refreshed for that step"), read at this invocation.
- **Plan Templates** (`docs/pfcanon/PF27-Canon-Plan-Templates-v2.0.4.md`), read at this invocation: "Step-log header schema expectations (required; v2)" (closed status set, exact status predicates, causal precedence, the fourteen required keys, including `evidence_artifacts`: "the check's own `primary.log` path and every primary artifact relied on"); Step-0B "Doc-delta surfaces (required; two-surface pair)" and its requirements (stable IDs, BLOCKERS and CAVEATS, append only when the Plan instructs it, prior content kept auditable, generated by commands); the check-block "Primary evidence artifact (required)" lines for the manifest and its path proof.
- **HDE Schemas and Artifacts** (`docs/pfcanon/PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.5.md`), read at this invocation: "Machine Evidence Mirror" (each governed artifact has a sibling `<artifact-path>.path_proof.txt`); "MTIME-UTC-SEMANTICS" (`mtime_utc` is capture-time provenance; validity is path, SHA-256, size, required fields and timestamp shape); §1.2 "Authority order" (PF12 owns canonical paths and path-proof naming).
- **Glow Infrastructure** (`docs/pfcanon/PF07-Canon-Glow-Infrastructure-v2.3.2.md`): §8.1 "Shared keys", `EVIDENCE_ROOT` (common relative paths `qa_step_logs_manifest.json`, `qa_step_logs_manifest.json.path_proof.txt`, `00_meta/doc_deltas.md`, `checks/<check_id>/primary.log`), read at this invocation.
- **Technical Writing Best Practices** (`docs/pfcanon/PF03-Reference-Technical-Writing-Best-Practices-v1.8.7.md`): "Truth and source fidelity", as read at QA-90 v1.1.

## 2. Sources and lineage

### 2.1 Approved base (immutable)

`docs/ephemeral/HDE-EPIC040-QA50-qa-plan-v1.2.md`, QA_PLAN v1.2, approved by `docs/ephemeral/HDE-EPIC040-QA70-qa-plan-review-v1.4.md`. Read at this invocation: the front matter, §1 to §8, §9.1, §10, §11, the §12 common rules, check blocks 1, 2 and 12, §13, §14, §15 and the provenance. The register of §2.3 was compared with §6 below. This collection packages check 12; it rewrites none of the Plan's content.

### 2.2 Overlays

| Overlay | Repository path | Effect on T12 |
| --- | --- | --- |
| PF10 addenda | `docs/pfcanon/PF10-HDE-Build-Notes-v13.4.5.md` | The addenda that Plan v1.2 §1 and §2.2 list. Added after the Plan's approval: 2.32 (the QA-110 review v1.0 below), 2.33 (the open-rails test; check 11 met it) and 2.34 (directed agents run vendor calls; vendor configuration in the environment). None changes check 12's content |
| QA-70 review v1.4 execution notes | `docs/ephemeral/HDE-EPIC040-QA70-qa-plan-review-v1.4.md` §6 | N-103: the delegation record (§4.1). N-104: the attempt statement (§4.2). N-101 and N-102 concern check 11 only. N-105: none |
| QA-110 review v1.0 | `docs/ephemeral/HDE-EPIC040-QA110-qa-evidence-review-v1.0.md` §4.2, §6.2, §8 | LR-01 item 6: T12 runs in the Run B checkout and stores on the Run B branch. LR-01 items 2 to 5 and 7 give the attempt lineage of checks 1 to 10 that T12's coverage accounting states. K-01 to K-04 applied (§1) |
| QA-110 review T11 v1.0 | `docs/ephemeral/HDE-EPIC040-QA110-qa-evidence-review-t11-v1.0.md` §5.2, §6 | The six constraints of its §6 (§1). K-06: the executor identity is captured in a file (§5 Part A) |
| PO disposition v1.0 | `docs/ephemeral/HDE-EPIC040-QA10-po-disposition-v1.0.md` | Q-1 and Q-2 map to checks 9 to 11; check 12 carries no Q item. Listed for completeness |

### 2.3 Aids (not overlays)

- `docs/ephemeral/HDE-EPIC040-QA50-qa-audit-v1.0.md`: loci L-41 and L-42 (the recording mechanism) and finding QA50-F01 (Index and Mirror publication is a follow-up), as Plan v1.2 cites them.
- `docs/ephemeral/HDE-EPIC040-QA100-qa-execution-results-t11-v1.0.md` §2, §3 and §6: the QA console, checkout, virtual environment, residual state and evidence branch that T12 continues.
- `docs/ephemeral/HDE-EPIC040-QA90-qa-task-collection-v1.1.md` §4 and T01 to T03, and `docs/ephemeral/HDE-EPIC040-QA90-qa-task-collection-v1.3.md` §4 and Part C: format lineage (the CLOSED prefix, the readiness line, the capture function, the body writers and the recording invocation). No task of either is re-issued here.

### 2.4 Read-only repository observations (authoring aids, not QA evidence)

At `633ca5d` (`main`), whose product code and tools equal the tested source `0db3f0ef` (`git diff --quiet 0db3f0ef 633ca5d -- tools engine adapter catalog ci` exits 0):

- `tools/evidence/update_evidence_index.py` `_refresh_path_proof(path, *, default_produced_at, check)`: `path` must be absolute under the module's own `ROOT` (the checkout root); with `check=False` it writes `<path>.path_proof.txt` with the fields `path`, `size_bytes`, `sha256`, `mtime_utc` (from the file's own modification time, or an existing proof) and `produced_at_utc` (`default_produced_at`, or an existing proof), and keeps an existing proof that still matches; with `check=True` it writes nothing and exits through `SystemExit` naming the fault (`MISSING_PROOF`, `PROOF_FIELDS`, `PROOF_PATH`, `PROOF_SHA`, `PROOF_SIZE`, `PROOF_MTIME`). Timestamps must be UTC with zero microseconds, for example `2026-09-29T07:06:05Z`. No HDE-EPIC040 path is in `NON_BACKDATED_PROOF_RELS`.
- `tools/evidence/validate_evidence_paths.py` checks only that every Machine Mirror path resolves inside the repository. The updater registers its paths explicitly; no HDE-EPIC040 QA path is registered.
- `tools/qa/qa_harness.py` `record_check`: validates the `CheckResult`, adds the check's own primary log to `evidence_artifacts`, publishes the primary log and the manifest entry together, verifies both and rolls back on error. It does not read the files named in `evidence_artifacts`.

On `origin`, observed at this invocation (2026-09-29):

- Branch `qa/hde-epic040-qa100-plan-v1.2-run-20260929` is at `380cf46fda95686ccf71f256521e63ca0eb5c9e1`. Its manifest has 11 entries, all `PASS`, each with the concrete `log_path` and a status equal to its primary-log header status. `git diff --name-only 0db3f0ef 380cf46` lists 25 paths, all under `audit/`, so its product tree is the tested source.
- The headers' `evidence_artifacts` name, besides each check's own primary log, 14 supplementary files: the manifest; both doc-delta surfaces; the four golden-comparison files; `http_probes.jsonl` and `gunicorn_server.log`; and the five check 11 files. They are the files of §5 command 10.
- Both doc-delta surfaces are 2,867 bytes, identical, SHA-256 `c79379566ea01cd6acff71f6cba3e3caa9edb5bc7748f42e8e3b3f7944e3a2c2`, ending in one LF. In the primary logs of checks 3 to 11, exactly one line starts `DOC_DELTA:`, line 488 of the check 11 log.
- None of the 14 remote branches holds `audit/qa/hde-epic040/checks/qa-closeout-deliverables/` or any path proof under `audit/qa/hde-epic040/` or for `audit/docdeltas/hde-epic040_doc_deltas.md`. Check 12 has never been executed.

In the QA console, as the QA-100 result of T11 records its residual state (this Kronos session cannot reach the console, and §4.3 checks each item again before anything runs): the QA checkout `/home/nathan/hde-epic040-qa` is on the Run B branch at `380cf46` with a clean working tree; the virtual environment `/tmp/hde-epic040-qa-v1.2/venv` has Python 3.12.3 and an editable install of the checkout; the vendor keys remain in the environment the Product Owner configured.

Dry run of this collection (Kronos-23, 2026-09-29; K-04). It tests instruction syntax and flow only. It is not an execution of check 12 and produced no QA evidence.

- Setup: the 33 bash blocks of §5 were extracted mechanically from this file and run in order in a scratch clone of the Run B branch at `380cf46`, made with umask 022, with a Python 3.12.3 virtual environment holding the project's editable install. Only the scratch directory and the virtual-environment path were substituted; the clone stood in for the checkout.
- Environment: each block ran in a fresh bash with an empty environment plus fake values of `HD_API_KEY`, `GEO_API_KEY`, `HD_API_BASE_URL` and `DATABASE_URL`, so the CLOSED prefix was exercised.
- Executor judgement: the W3 result lines and the C3 files were composed by the dry-run script from the captures, as the executor composes them.
- Scenarios: seven, recorded through C4 with the real `tools.qa.qa_harness` wherever the task records:

| Scenario | What happened | Recorded status |
| --- | --- | --- |
| Clean run | Commands 4 and 5 printed 11; command 9 printed 15; command 11 printed 25; command 13 printed `appended 1` and `DD-13 open-rails-showcompat-vendor`; command 17 printed `check mode passed 13`; commands 19 and 20 exit 0; command 22 printed 12 `COVERAGE` lines and the `DEFERRED` line; C5 wrote and checked both step 8 proofs | `PASS`, exit 0, 23 commands, 16 evidence artifacts; manifest 12 entries; `git status` listed exactly the 19 files of §4.8 |
| Doc-delta surfaces differ before the append | Command 12 exit 1; command 13 refused with `DOC_DELTA_APPEND_REFUSED` and wrote nothing; command 14 exit 1 | `FAIL_TOOLING`, 23 commands |
| Manifest without the check 11 entry | Commands 4 and 5 printed 10; commands 6 to 23 not run | `TOOLING_BLOCKED`, 5 commands, 1 evidence artifact (its own log) |
| A supplementary file missing (`vendor_run_ab.json`) | Command 10 exit 1 naming that file; every other command ran | `FAIL_TOOLING`, 23 commands |
| A primary log missing (check 7) | Command 10 exit 1 naming the log; stop after command 10. `record_check` refuses a manifest whose entry has no primary log ("manifest primary log is missing or empty"), which is why §4.6 sends this case to Kronos | Not recorded; `TOOLING_BLOCKED` for Kronos to record |
| Command 13 repeated by mistake as `13r` | `13r` refused and wrote nothing; the appended section appears once; both executions are in the body | `PASS`, exit 0, 24 commands |
| Evidence index sentinel altered in the scratch copy | Command 19 exit 1 (`STALE:` on `docs/evidence/INDEX.sha256`); command 20 exit 0 | `FAIL_TOOLING`, exit 0 (command 20), 23 commands |

- In every recorded scenario the primary log had a 14-key `pf27.step_log_header.v2` header with no empty argv part, all five body sections and one final LF. No fake value appeared in any file of the checkout or the scratch directory.
- The dry run found four defects in the draft, all fixed before issue:
  1. A repeat of `q12 13` would have overwritten the first execution's captures. Repeats now use a suffixed label (§4.6), and W2 prints every label in `cmds.txt`.
  2. The coverage line of check 11 read "attempt attempt 1". The field is now "attempt lineage".
  3. A missing primary log made the recording fail. §4.6 now stops after command 10 in that case.
  4. C4 listed the doc-delta surfaces when the gate had stopped the check. It now lists them only when command 12 ran.

### 2.5 Pre-execution assessment

Isis-52 approved exactly Plan v1.2 (review v1.4 `reviewed_plan` SHA-256 equal to the base above). Check 12 is inside the Plan's scope (Plan §2 D11, §10, §13). Its dependency holds: checks 1 to 11 are recorded on the Run B branch, each `PASS`, and each is `ACCEPT` at QA-110. Every command, tool and file it uses exists at the tested source (§2.4). No part of the block has a substantive defect that survives faithful normalization.

Canon observations that change nothing in T12:

- The Plan writes the path proofs of checks 1 to 11 at check 12 rather than as each check was recorded. Glow QA Guide §3.4.3 and HDE Governance §2.0.19 ask for a manifest path proof whenever the manifest changes. The approved Plan's design (Plan §8) and the QA-110 acceptances already record the gap as "path-proof binding not yet produced (check 12)". T12 closes it for the final bytes: step 3 proves the eleven earlier primary logs, and step 8 proves the manifest and T12's own log after the last manifest change. No decision of this task depends on the earlier gap.
- A ledger-bound manifest is not claimed (Plan §8; Glow QA Guide §4.4.3; HDE Governance §2.0.19). Step 4 shows only that the QA files do not disturb the governed evidence checks; it registers nothing in the Human Evidence Index or the Machine Mirror (QA50-F01, a follow-up for the evidence owner).

### 2.6 Carried lineage

- Attempt lineage: §4.2.
- `CANON_CONFLICT_REGISTER`: §6, carried unchanged from the QA-110 review T11 v1.0 §7 (C040-01 to C040-10); QA-90 adds no entry.
- PR lineage: Plan v1.2 carries no `PR_RETURN_PHASE`; none is created here.
- Deferred requirements (live Gate readiness; live DB Reader success): Plan §2. They are not checks and have no task; T12's coverage accounting names them.

## 3. Selection reconciliation

The Product Owner's selection "Selection: check 12" names Plan check 12 by the only numbering the approved Plan defines (Plan §10, §11).

| Plan # | `check_id` | Selected | Task | Attempt | Executor | Depends on | State at authoring |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 to 10 | checks 1 to 10 | Earlier selection "Tasks: 1-10" | T01 to T10 in collection v1.1 | per ruling LR-01 | Q | per Plan §11 | Executed; each `ACCEPT` at QA-110 review v1.0; not re-issued |
| 11 | `open-rails-showcompat-vendor` | Earlier selection "Task: 11" | T11 in collection v1.3 | 1 | P, executed by a directed agent under HDE Build Notes 2.34 | checks 1 and 8 | Executed; `ACCEPT` at QA-110 review T11 v1.0; not re-issued |
| 12 | `qa-closeout-deliverables` | Yes | T12 (this collection) | 1 | Q | every other check recorded, any status | Ready: checks 1 to 11 recorded on the Run B branch |

Counts: 12 Plan checks; 1 selected here; 1 task, attempt 1; 0 conditional; no check left unselected. The deferred requirements of Plan §2 are not checks and are not counted.

When T12 is recorded and accepted, every check of the approved Plan has a task and an execution, and the run can go to QA-120 (Glow QA Guide §9.2.15.5).

## 4. Common execution contract

### 4.1 Executor, delegation and venue (Plan §6, §7.1; review v1.4 N-103)

Delegation record:

- **Executor: the QA/infra executor.** It is the operator session in which the Product Owner runs QA-100 — Execute Bounded QA Task — 091426.1 with the handoff of this collection. It acts in the repository's QA/Verifier role (`AGENTS.md`). It is neither the Product Owner nor Kronos. Plan §7.1 assigns check 12 to it, as a class 2 check handled outside the Product Owner's Live QA time. It runs every command of §5. Its execution identity is PENDING at QA-90, because the session does not exist yet; it writes that identity to `executor_identity.txt` in Part A, and the QA-100 result records it. If no identity can be recorded, T12 does not run (Plan §6).
- Delegating act: the Product Owner's selection of check 12 and the Product Owner opening that QA-100 session with this collection's handoff. This record creates no authority beyond it.
- Capability: T12 makes no vendor call, reads or prints no secret value and connects to no database, so an automated execution agent may be the executor (Plan §7.1). The vendor keys in the console's environment are unset for every command by the CLOSED prefix (§4.4).
- **Venue (LR-01 item 6):** the Product Owner-controlled Linux shell where checks 1 to 11 ran (Run B), in the one QA checkout `/home/nathan/hde-epic040-qa`, from its root, so that one QA root and one manifest hold all twelve checks (Plan §7.1). Not production and not a deployed service.

### 4.2 Attempts (Plan §7.3; review v1.4 N-104)

- T12 is attempt 1 of check 12 under Plan v1.2: no execution of check 12 is recorded or stored on any branch (§2.4). The `06b04a9` executions of Plan v1.0 hold no close-out check and are not attempts of T12, as collection v1.1 §4.2 decided for checks 1 to 10.
- One ordinary rerun (attempt 2) exists only through Kronos's QA-110 decision and a new QA-90 task, after an attempt 1 that ends `FAIL_TOOLING` or `TOOLING_BLOCKED` from an execution or evidence fault (Plan §7.3; Glow QA Guide §10.6). A QA-created evidence-assembly defect of this check (the doc-delta append, a path proof) may instead be corrected by a Moon Loop that Kronos decides at QA-110 (Plan §7.4). Task authoring and syntax normalization are not attempts (Glow QA Guide §9.2.15.5). This collection authorizes no rerun and no Moon Loop.

### 4.3 Setup (executor, before Part A; not check commands)

These read-only checks establish the starting state (K-03). Record each output in the QA-100 result. If any expectation fails, stop, run nothing else, and report.

1. From `/home/nathan/hde-epic040-qa`: `git rev-parse HEAD` prints `380cf46fda95686ccf71f256521e63ca0eb5c9e1`; `git branch --show-current` prints `qa/hde-epic040-qa100-plan-v1.2-run-20260929`; `git status --porcelain --untracked-files=all` prints nothing.
2. `git fetch origin`, then `git ls-remote --heads origin qa/hde-epic040-qa100-plan-v1.2-run-20260929` prints `380cf46fda95686ccf71f256521e63ca0eb5c9e1`. Then this loop over every remote branch prints nothing; if it prints a path, stop and report: another execution exists.

   ```bash
   for b in $(git for-each-ref --format='%(refname:short)' refs/remotes/origin); do git ls-tree -r --name-only "$b" -- audit/qa/hde-epic040/checks/qa-closeout-deliverables audit/qa/hde-epic040/qa_step_logs_manifest.json.path_proof.txt; done
   ```

3. `test -e audit/qa/hde-epic040/checks/qa-closeout-deliverables` exits 1; `find audit/qa/hde-epic040 -name '*.path_proof.txt'` prints nothing; `test -e audit/docdeltas/hde-epic040_doc_deltas.md.path_proof.txt` exits 1.
4. `test -e /tmp/hde-epic040-qa-v1.2/qa-closeout-deliverables` exits 1: no capture file from an earlier attempt may exist. If it exists, stop and report; do not delete it.
5. `/tmp/hde-epic040-qa-v1.2/venv/bin/python --version` prints `Python 3.12.` and a patch number. If the virtual environment is missing, re-create it exactly as collection v1.1 T01 commands 6 and 7 did and record the installed versions; that is setup, not a check command.
6. Storage authorization: ask the Product Owner now, before Part A, for the instruction to store the evidence of §4.8 (branch `qa/hde-epic040-qa100-plan-v1.2-run-20260929`, the 19 files listed there, one pushed commit, no pull request). Record the answer in the QA-100 result.
7. `mkdir -p /tmp/hde-epic040-qa-v1.2/qa-closeout-deliverables`.

### 4.4 Rails prefix (Plan §5.2; N-01)

One literal prefix, written in full in every check command and in the recording and finalization commands:

- CLOSED prefix: `env -u DATABASE_URL -u HD_API_KEY -u GEO_API_KEY -u HD_API_BASE_URL -u HDAPI_BASE_URL -u DB_BRIDGE_URL -u DB_FORCE_BRIDGE -u DB_ALLOW_BRIDGE_IN_PROD -u ENGINE_ENV PATH=/tmp/hde-epic040-qa-v1.2/venv/bin:$PATH SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC`

It applies the closed posture per command, so the vendor configuration held in the console's environment (HDE Build Notes 2.34 rule 4; QA-100 T11 result D-03) never reaches a T12 command. With the virtual environment first on `PATH`, `python` resolves to the tested install (N-02). Rails never change inside T12.

### 4.5 Capture function and body (Plan §8, §12; N-36)

Scratch directory: `/tmp/hde-epic040-qa-v1.2/qa-closeout-deliverables/`, outside the repository and never committed.

Every check command is run through one shell function, `q12`, defined in Part A:

```bash
q12() { Q=/tmp/hde-epic040-qa-v1.2/qa-closeout-deliverables; c=$(cat); printf '%s\n' "$c" >> "$Q/argv.txt"; printf '%s\n' "$c" > "$Q/c$1.argv"; eval "$c" > "${2:-$Q/c$1.out}" 2> "$Q/c$1.err"; echo $? > "$Q/c$1.rc"; printf '[%s] exit=%s :: %s\n' "$1" "$(cat "$Q/c$1.rc")" "$c" >> "$Q/cmds.txt"; printf '[%s] exit=%s\n' "$1" "$(cat "$Q/c$1.rc")"; }
```

`q12 K` reads one command line from a quoted here-document, appends it to `argv.txt` and writes it to `cK.argv`, runs it with stdout to `cK.out`, stderr to `cK.err` and its exit code to `cK.rc`, appends `[K] exit=N :: command` to `cmds.txt`, and prints `[K] exit=N`. Because the here-document delimiter is quoted, the command line is recorded exactly as run. The function evaluates no predicate; it is the capture glue that QA-110 accepted for checks 10 and 11 (review v1.0 D-07). An executor whose shell does not keep functions between invocations defines `q12` in the same invocation as each command.

`argv.txt` holds the check commands actually run, in order, and only those: 23 when none is skipped or repeated. Not check commands, and not in `argv.txt` (K-04): the setup of §4.3, the identity line, the writers W1 to W4, the recording inputs C3, the recording C4, the finalization C5, the verification C6 and the storage steps of §4.8.

`body.txt` receives the Plan §8 sections in order, each by redirection from captures: `=== CONTEXT ===` (W1, before command 1), `=== COMMANDS ===` and `=== OUTPUT ===` (W2, after command 23), `=== PREDICATES ===` (W3: observed values, then one result line per [E] predicate, the [K] predicates as `pending QA-110` and the two-layer statement), and `=== LIMITS ===` (W4).

### 4.6 Stop rules (Plan check 12; Plan §11)

- **Dependency gate (commands 3 to 5).** If command 3 exits non-zero, or command 4 or command 5 does not print `11`, not every other check is recorded: run no further check command, go to Part C, and record the check `TOOLING_BLOCKED` (Plan §11). The reason names what the gate found.
- **Readiness (commands 6 to 9).** If command 6 does not print `Python 3.12.` and a patch number, command 7 does not exit 0 and print `/tmp/hde-epic040-qa-v1.2/venv/bin/python`, or command 9 does not print `15`: run no further check command, go to Part C, and record `TOOLING_BLOCKED`. If command 7 fails because `tools.qa.qa_harness` cannot be imported after a good install, the recording cannot run: keep every file, stop, and report the failure signature to Kronos, who records the check `FAIL_TOOLING` at QA-110.
- **A missing primary log (command 10).** If command 10's standard error names one of the eleven primary logs, a primary log of a recorded check is missing: run no further check command. The check is `TOOLING_BLOCKED` (Plan check 12), but the harness cannot record it, because `record_check` refuses a manifest whose entry has no primary log (§2.4). Complete W2 to W4 and C3, keep every file, do not run C4 or store, and report to Kronos, who records the outcome at QA-110.
- **Otherwise run commands 10 to 23 in order, each exactly once, whatever their exit codes.** Each is separate evidence, and the status follows §4.7. Command 13 (the append) and command 16 (the proof writer) are not repeated: if command 13 is run again by mistake, its guard refuses and writes nothing, and E4 is judged from the first execution.
- **Operator error:** a mistyped command is repeated once, under the label of the first execution followed by `r` (for example `q12 13r`), so that the first execution keeps its captures and both executions appear in `argv.txt`, `cmds.txt` and the body. The reason goes in the QA-100 result. It is not an attempt.
- **Recording failure:** if C4 exits non-zero, keep every file, stop, do not store, and report the failure signature to Kronos, who records the check `FAIL_TOOLING` at QA-110 (Plan §12 item 4). No status is inferred.
- **Finalization failure:** if C5 does not show both proofs written and passing check mode, report its output; continue with C6 and the storage of §4.8. Kronos judges the step 8 proofs at QA-110.

### 4.7 Status (Plan check 12; Plan Templates causal precedence)

The executor determines the step-log status from the [E] predicates of §5 Part C (W3), in this precedence:

1. `FAIL_TOOLING`: a supplementary file named in a primary log is missing or unreadable (command 10 exits non-zero and its standard error names a file that is not one of the eleven primary logs); the doc-delta surfaces differ before or after the append (command 12 or 14 exits non-zero), or the append refused or failed (command 13 exits non-zero); a path proof was not written or fails check mode (command 16 or 17 exits non-zero); step 4 fails with the QA files present (command 19 or 20 exits non-zero; Kronos classifies the cause at QA-110); or the coverage accounting was not written (command 22 exits non-zero or command 23 does not print `12`).
2. `TOOLING_BLOCKED`: the dependency gate or the readiness line does not hold (§4.6); or a primary log of a recorded check is missing (command 10's standard error names one of the eleven primary logs; Plan check 12), which Kronos records at QA-110 (§4.6).
3. `FAIL_BEHAVIOR`: not applicable. This check makes no product-behavior claim (Plan check 12).
4. `PASS`: E1 to E7 all hold.

Commands 1, 2, 15, 18 and 21 are attribution or capture only and do not change the status. `status_reason` is empty only for `PASS`. The [K] predicates are Kronos's at QA-110 and do not enter the step-log status (Plan §12 two result layers).

### 4.8 Evidence files and commit boundary (Plan §7.2; ruling LR-01 item 6; storage authorization §4.3 item 6)

Evidence storage is not a check and is part of no PASS predicate.

- Where: the existing branch `qa/hde-epic040-qa100-plan-v1.2-run-20260929`, checked out in the QA checkout, as one new commit on `380cf46fda95686ccf71f256521e63ca0eb5c9e1`.
- Permitted files, and nothing else; only those that exist are added, and a missing one is reported, not created:
  - modified: `audit/qa/hde-epic040/qa_step_logs_manifest.json`, `audit/docdeltas/hde-epic040_doc_deltas.md`, `audit/qa/hde-epic040/00_meta/doc_deltas.md`;
  - new: `audit/qa/hde-epic040/checks/qa-closeout-deliverables/primary.log`;
  - new path proofs: `audit/qa/hde-epic040/checks/d0-discovery/primary.log.path_proof.txt`, `audit/qa/hde-epic040/checks/step-0b-doc-delta-capture/primary.log.path_proof.txt`, `audit/qa/hde-epic040/checks/ac040-08-evidence-validators/primary.log.path_proof.txt`, `audit/qa/hde-epic040/checks/ac040-02-03-catalog-config/primary.log.path_proof.txt`, `audit/qa/hde-epic040/checks/ac040-04-05-admission-identity/primary.log.path_proof.txt`, `audit/qa/hde-epic040/checks/ac040-06-golden-comparison/primary.log.path_proof.txt`, `audit/qa/hde-epic040/checks/ac040-07-gate-ingress-offline/primary.log.path_proof.txt`, `audit/qa/hde-epic040/checks/ac040-04-09-compat-cli-offline/primary.log.path_proof.txt`, `audit/qa/hde-epic040/checks/ac040-09-reader-http-in-process/primary.log.path_proof.txt`, `audit/qa/hde-epic040/checks/sec-reader-http-live/primary.log.path_proof.txt`, `audit/qa/hde-epic040/checks/open-rails-showcompat-vendor/primary.log.path_proof.txt`, `audit/qa/hde-epic040/checks/qa-closeout-deliverables/primary.log.path_proof.txt`, `audit/qa/hde-epic040/qa_step_logs_manifest.json.path_proof.txt`, `audit/docdeltas/hde-epic040_doc_deltas.md.path_proof.txt`, `audit/qa/hde-epic040/00_meta/doc_deltas.md.path_proof.txt`.
- Steps, from the checkout root, after C6:
  1. `git status --porcelain --untracked-files=all` lists exactly the three modified files and the sixteen new files above. Any other path is reported and not added.
  2. `git ls-remote --heads origin qa/hde-epic040-qa100-plan-v1.2-run-20260929` still prints `380cf46fda95686ccf71f256521e63ca0eb5c9e1`. If not, stop and report.
  3. `git add --` followed by the permitted paths that exist, named one by one.
  4. `git diff --cached --name-only` lists exactly those paths.
  5. `git commit -m "HDE-EPIC040 QA-100: evidence for QA Plan v1.2 check 12, attempt 1; tested source 0db3f0ef33e7a7a3aa85a2c221e06ac5581c7b8d"`, plus any attribution lines the session's own rules require. If the checkout has no committer identity, pass one for this command only through the `-c user.name` and `-c user.email` options of `git`, and record it (as the T11 result's D-04 did).
  6. `git push origin qa/hde-epic040-qa100-plan-v1.2-run-20260929` (a fast-forward), retried on a network error only.
  7. `git ls-remote --heads origin qa/hde-epic040-qa100-plan-v1.2-run-20260929` prints the local `HEAD`; each pushed blob's SHA-256 equals the digest C6 printed.
- Never committed: anything in the scratch directory; any tracked file outside the list above that a command changed (command 21 lists it for Kronos); any product, test, tool, schema, catalog, CI, Index, Mirror, PF or `docs/` file.
- Not done: no force-push, rebase, merge or amend; no pull request by the executor. The Product Owner decides any pull request and merge. Run A's branch stays untouched and is never merged as the QA root (LR-01 item 6).
- The QA-100 result record under `docs/ephemeral/` is QA-100's own output, stored under its own working-branch rule from a checkout other than the QA checkout.

### 4.9 Cleanup and recovery (Plan §7.5)

- Keep the QA checkout, the virtual environment and the scratch directory after T12. Nothing is deleted.
- No command connects to a database or changes database state, and no server is started, so no database or server recovery exists.
- No secret value is handled. If one is nevertheless found in any file T12 produced, move that file out of the repository into the scratch directory, do not commit it, record the check `FAIL_TOOLING`, and report (Plan §7.5).

### 4.10 Normalizations (Plan §12; Glow QA Guide §3.4.7, §3.4.10; QA-90 Execute step 5)

Each clarifies an unchanged Plan operation and changes no objective, proof target, rails posture, evidence identity or predicate. `provenance.txt` lists them.

| ID | Plan locus | Normalization | Reason |
| --- | --- | --- | --- |
| N-01, N-02, N-03, N-05, N-06 | As in collection v1.1 §4.9 | The CLOSED prefix per command; the virtual environment first on `PATH`; R2 prints `sys.executable`; the recorded statuses are read from `python -m json.tool` of the manifest; a compound command is one `sh -c` argv | Carried unchanged |
| N-36 | §8, §12 (captures, body, recording) | The capture function `q12` and the writers W1 to W4 (§4.5), the form of collection v1.3 N-20 | Every executed argv is recorded exactly as run, and the body is composed only from captures |
| N-37 | §11 (check 12 depends on "every other check recorded (any status)") | Commands 3 to 5: the manifest read with `python -m json.tool`, then two counts with `grep -c -F`: all entries (expected 11) and the entries of checks 1 to 11 by name (expected 11) | The dependency becomes two baseline values compared with literal expectations |
| N-38 | §12 readiness ("the posture of §5.2 is applied and recorded") | Command 9 counts the fifteen expected posture and presence lines of command 8 with `grep -c -x -F` (expected 15) | A baseline count instead of reading fifteen lines by eye |
| N-39 | Check 12 step 1 ("every supplementary file named in those primary logs") | The supplementary files are the `evidence_artifacts` of each recorded primary-log header other than the log itself: 14 files, the manifest included (§2.4). Command 10 hashes the manifest, the eleven primary logs and the other thirteen files in one `sha256sum`; command 11 counts 25 lines | Makes "named" mechanical: the header list is the recorded one |
| N-40 | Check 12 step 2 (the doc-delta append) and Plan Templates Step-0B | Command 12 compares the surfaces before the append. Command 13, the Plan-named writer, appends to both surfaces the same bytes: a blank line, the heading `## QA-DISCOVERED CAVEATS (check qa-closeout-deliverables)`, a source line (class CAVEAT; Drives decision: No), and one list item per `DOC_DELTA:` line of checks 3 to 11 in Plan order, numbered from DD-13, with the source check and the line verbatim; or, when there is none, the line `No new deltas found during execution.`. It refuses and writes nothing when the surfaces differ, lack a final LF, or already hold that heading | The existing rows keep their bytes (Step-0B: prior content stays auditable); stable IDs and classes; no interpretation of a line's prose; no double append |
| N-41 | Check 12 step 3 (`_refresh_path_proof(path, default_produced_at=<UTC now>, check=False)` then `check=True`) | `<UTC now>` is computed in the command as the current UTC time with zero microseconds and a `Z` suffix; each path is the updater's own `ROOT` joined with the repository-relative path; the thirteen proofs are written by command 16 and checked by command 17; command 18 prints them into the body | The form `_refresh_path_proof` accepts (§2.4); the primary log alone shows each proof's content (Glow QA Guide §4.4.6) |
| N-42 | Check 12 step 6 (coverage accounting) | Command 22, one `sh -c` of baseline commands (`printf`, `grep -o`), prints one `COVERAGE` line per check in Plan order: the manifest entry (status and `log_path`), the attempt lineage of the QA-110 rulings, the header's `evidence_artifacts` and, for a non-PASS entry, a pointer to its recorded reason; then a `DEFERRED` line for the two deferred requirements. Command 23 counts the check lines (expected 12) | The accounting is written from the recorded manifest and headers, not typed. It evaluates no decisive predicate; command 23 and [K] K5 verify it |
| N-43 | Check 12 step 7 (recording) | `evidence_artifacts` lists the two doc-delta surfaces when command 12 ran, and the thirteen path proofs of step 3 that exist at recording; the harness adds the primary log. `captured_env` holds the six closed values | Only artifacts that exist are listed (collection v1.3 N-30); every command ran under the closed posture |
| N-44 | Check 12 step 8 (finalization) | C5 calls `_refresh_path_proof` as command 16 and 17 do, for the check's own primary log and the manifest, after C4; its captures stay in the scratch directory and the QA-100 result, outside the primary log | The Plan places step 8 outside the primary log |
| N-45 | Plan §5.3 (source identity, attribution only) | Commands 1 and 2 record the checkout `HEAD` and the files that differ from the tested source, before the gate | Read-only observations for attribution only, never a PASS gate (Glow QA Guide §3.4.9; C040-09) |

### 4.11 Return to QA-110

QA-100 returns one `QA_EXECUTION_RESULT` for T12 to QA-110 — Review QA Evidence and Route the Next Action — 091426.1, in the continuing Kronos-23 session. It gives: task, `check_id`, attempt 1, the step-log status and reason as recorded, the final decisive command's exit code, the primary-log path, the SHA-256 and size of the 19 stored files, the finalization output of C5, the normalizations applied, deviations (including any operator-error repeat or recording failure), the setup observations of §4.3, the storage authorization, residual state and the resume point; plus the executor identity, the checkout `HEAD` at execution, the evidence branch and its pushed commit. QA-110 evaluates K1 to K5 and the step 8 proofs, forms the per-task result, dispositions any fault and decides any attempt 2 or Moon Loop.

## 5. Task T12 `qa-closeout-deliverables` — Close-out deliverables and coverage

- Plan block: CHECK 12 (Plan v1.2 L825 to L855). Class 2, local/offline (no vendor); pre-flight / internal; handled by the QA/infra executor outside the Product Owner's Live QA time. D11; AC040-01 and AC040-08 (evidence integrity of the QA run); PF06 §0.4.1. PF anchors: PF06-Canon-Change-Process-Guide §0.4.1; PF19-Canon-Glow-QA-Guide §3.4.3, §4.4.3, §9.2.15.5.
- Change HDE-EPIC040 (Epic); approved Plan `docs/ephemeral/HDE-EPIC040-QA50-qa-plan-v1.2.md`; approving review `docs/ephemeral/HDE-EPIC040-QA70-qa-plan-review-v1.4.md`; QA Audit `docs/ephemeral/HDE-EPIC040-QA50-qa-audit-v1.0.md`; attempt 1 (§4.2); tokens `[]`.
- Dependencies: every other check recorded, any status (Plan §11); checks 1 to 11 are recorded on the Run B branch.
- Environment and target: the QA console of §4.1, checkout `/home/nathan/hde-epic040-qa`, the closed posture (§4.4); the target is the QA run's own evidence under `audit/qa/hde-epic040/` and `audit/docdeltas/hde-epic040_doc_deltas.md`, with the governed evidence checks of the tested source tree. No vendor, no database, no server, not production.
- Inputs: the manifest, the eleven primary logs and the thirteen other supplementary files of command 10; both doc-delta surfaces; `tools/evidence/update_evidence_index.py`, `tools/evidence/validate_evidence_paths.py`, `tools/qa/qa_harness.py`.
- Outputs (QA-created): the appended doc-delta surfaces; the thirteen path proofs of step 3; `audit/qa/hde-epic040/checks/qa-closeout-deliverables/primary.log` and its manifest entry, written by the recording; the path proofs of that primary log and of the manifest, written by the finalization (step 8).
- Final decisive command: command 20 (`python tools/evidence/validate_evidence_paths.py`); `final.rc` is its exit code. Commands 21 to 23 run after it and do not change `final.rc`.

Each command below is complete in its own block (K-02). A block that starts `q12` is three lines: the `q12` line, the command, and `EOF`; paste all three together. After each `q12` block the terminal shows `[K] exit=N`.

### Part A — identity, capture function and CONTEXT

After §4.3 setup. Record the executor identity, one line, in the form of this example (the QA-100 T11 identity), with your own values:

```bash
printf '%s\n' 'Claude Code local VS Code session f0edea78-3120-4040-92a1-020776ba5a6f, QA/infra executor delegated by the Product Owner' > /tmp/hde-epic040-qa-v1.2/qa-closeout-deliverables/executor_identity.txt
```

Define the capture function:

```bash
q12() { Q=/tmp/hde-epic040-qa-v1.2/qa-closeout-deliverables; c=$(cat); printf '%s\n' "$c" >> "$Q/argv.txt"; printf '%s\n' "$c" > "$Q/c$1.argv"; eval "$c" > "${2:-$Q/c$1.out}" 2> "$Q/c$1.err"; echo $? > "$Q/c$1.rc"; printf '[%s] exit=%s :: %s\n' "$1" "$(cat "$Q/c$1.rc")" "$c" >> "$Q/cmds.txt"; printf '[%s] exit=%s\n' "$1" "$(cat "$Q/c$1.rc")"; }
```

**W1.** CONTEXT section (writer, not a check command). The executor and the host come from captures, never from fixed text (K-06):

```bash
sh -c 'Q=/tmp/hde-epic040-qa-v1.2/qa-closeout-deliverables; { printf "=== CONTEXT ===\n"; printf "TASK: T12 of docs/ephemeral/HDE-EPIC040-QA90-qa-task-collection-v1.4.md; QA Plan v1.2 CHECK 12 qa-closeout-deliverables (docs/ephemeral/HDE-EPIC040-QA50-qa-plan-v1.2.md); attempt 1\n"; printf "EXECUTOR: "; cat "$Q/executor_identity.txt"; printf "HOST: %s\n" "$(uname -n)"; printf "CHECKOUT: %s\n" "$(pwd)"; printf "TESTED_SOURCE: 0db3f0ef33e7a7a3aa85a2c221e06ac5581c7b8d (commands 1 and 2 record the checkout HEAD and the files that differ from it)\n"; printf "RAILS: CLOSED prefix on every command (collection v1.4 section 4.4)\n"; } >> "$Q/body.txt"'
```

### Part B — check commands 1 to 23

**1.** Checkout `HEAD`, for attribution only (N-45). Expected `380cf46fda95686ccf71f256521e63ca0eb5c9e1`.

```bash
q12 1 <<'EOF'
env -u DATABASE_URL -u HD_API_KEY -u GEO_API_KEY -u HD_API_BASE_URL -u HDAPI_BASE_URL -u DB_BRIDGE_URL -u DB_FORCE_BRIDGE -u DB_ALLOW_BRIDGE_IN_PROD -u ENGINE_ENV PATH=/tmp/hde-epic040-qa-v1.2/venv/bin:$PATH SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC git rev-parse HEAD
EOF
```

**2.** Files that differ from the tested source, for attribution only. Expected: 25 paths, all under `audit/`.

```bash
q12 2 <<'EOF'
env -u DATABASE_URL -u HD_API_KEY -u GEO_API_KEY -u HD_API_BASE_URL -u HDAPI_BASE_URL -u DB_BRIDGE_URL -u DB_FORCE_BRIDGE -u DB_ALLOW_BRIDGE_IN_PROD -u ENGINE_ENV PATH=/tmp/hde-epic040-qa-v1.2/venv/bin:$PATH SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC git diff --name-only 0db3f0ef33e7a7a3aa85a2c221e06ac5581c7b8d HEAD
EOF
```

**3.** Dependency gate: the manifest as recorded (N-05, N-37). Expected exit 0.

```bash
q12 3 <<'EOF'
env -u DATABASE_URL -u HD_API_KEY -u GEO_API_KEY -u HD_API_BASE_URL -u HDAPI_BASE_URL -u DB_BRIDGE_URL -u DB_FORCE_BRIDGE -u DB_ALLOW_BRIDGE_IN_PROD -u ENGINE_ENV PATH=/tmp/hde-epic040-qa-v1.2/venv/bin:$PATH SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC python -m json.tool audit/qa/hde-epic040/qa_step_logs_manifest.json
EOF
```

**4.** Number of manifest entries. Expected `11`.

```bash
q12 4 <<'EOF'
env -u DATABASE_URL -u HD_API_KEY -u GEO_API_KEY -u HD_API_BASE_URL -u HDAPI_BASE_URL -u DB_BRIDGE_URL -u DB_FORCE_BRIDGE -u DB_ALLOW_BRIDGE_IN_PROD -u ENGINE_ENV PATH=/tmp/hde-epic040-qa-v1.2/venv/bin:$PATH SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC grep -c -F -e '"check_id": "' /tmp/hde-epic040-qa-v1.2/qa-closeout-deliverables/c3.out
EOF
```

**5.** Entries of checks 1 to 11 by name. Expected `11`.

```bash
q12 5 <<'EOF'
env -u DATABASE_URL -u HD_API_KEY -u GEO_API_KEY -u HD_API_BASE_URL -u HDAPI_BASE_URL -u DB_BRIDGE_URL -u DB_FORCE_BRIDGE -u DB_ALLOW_BRIDGE_IN_PROD -u ENGINE_ENV PATH=/tmp/hde-epic040-qa-v1.2/venv/bin:$PATH SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC grep -c -F -e '"check_id": "d0-discovery"' -e '"check_id": "step-0b-doc-delta-capture"' -e '"check_id": "ac040-08-evidence-validators"' -e '"check_id": "ac040-02-03-catalog-config"' -e '"check_id": "ac040-04-05-admission-identity"' -e '"check_id": "ac040-06-golden-comparison"' -e '"check_id": "ac040-07-gate-ingress-offline"' -e '"check_id": "ac040-04-09-compat-cli-offline"' -e '"check_id": "ac040-09-reader-http-in-process"' -e '"check_id": "sec-reader-http-live"' -e '"check_id": "open-rails-showcompat-vendor"' /tmp/hde-epic040-qa-v1.2/qa-closeout-deliverables/c3.out
EOF
```

If command 3 exited non-zero, or command 4 or 5 did not print `11`, stop here (§4.6) and go to Part C.

**6.** Readiness R1. Expected `Python 3.12.` and a patch number.

```bash
q12 6 <<'EOF'
env -u DATABASE_URL -u HD_API_KEY -u GEO_API_KEY -u HD_API_BASE_URL -u HDAPI_BASE_URL -u DB_BRIDGE_URL -u DB_FORCE_BRIDGE -u DB_ALLOW_BRIDGE_IN_PROD -u ENGINE_ENV PATH=/tmp/hde-epic040-qa-v1.2/venv/bin:$PATH SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC python --version
EOF
```

**7.** Readiness R2 (N-03). Expected exit 0 and `/tmp/hde-epic040-qa-v1.2/venv/bin/python`.

```bash
q12 7 <<'EOF'
env -u DATABASE_URL -u HD_API_KEY -u GEO_API_KEY -u HD_API_BASE_URL -u HDAPI_BASE_URL -u DB_BRIDGE_URL -u DB_FORCE_BRIDGE -u DB_ALLOW_BRIDGE_IN_PROD -u ENGINE_ENV PATH=/tmp/hde-epic040-qa-v1.2/venv/bin:$PATH SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC python -c "import sys, tools.qa.qa_harness, engine; print(sys.executable)"
EOF
```

**8.** Readiness R3: the closed posture as applied, presence only.

```bash
q12 8 <<'EOF'
env -u DATABASE_URL -u HD_API_KEY -u GEO_API_KEY -u HD_API_BASE_URL -u HDAPI_BASE_URL -u DB_BRIDGE_URL -u DB_FORCE_BRIDGE -u DB_ALLOW_BRIDGE_IN_PROD -u ENGINE_ENV PATH=/tmp/hde-epic040-qa-v1.2/venv/bin:$PATH SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC sh -c 'for k in SAFE_MODE ALLOW_NETWORK APP_ENV LC_ALL LANG TZ; do echo "$k=$(printenv "$k")"; done; for k in DATABASE_URL HD_API_KEY GEO_API_KEY HD_API_BASE_URL HDAPI_BASE_URL DB_BRIDGE_URL DB_FORCE_BRIDGE DB_ALLOW_BRIDGE_IN_PROD ENGINE_ENV; do if printenv "$k" > /dev/null; then echo "$k=SET"; else echo "$k=UNSET"; fi; done'
EOF
```

**9.** Count of the fifteen expected lines of command 8 (N-38). Expected `15`.

```bash
q12 9 <<'EOF'
env -u DATABASE_URL -u HD_API_KEY -u GEO_API_KEY -u HD_API_BASE_URL -u HDAPI_BASE_URL -u DB_BRIDGE_URL -u DB_FORCE_BRIDGE -u DB_ALLOW_BRIDGE_IN_PROD -u ENGINE_ENV PATH=/tmp/hde-epic040-qa-v1.2/venv/bin:$PATH SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC grep -c -x -F -e SAFE_MODE=1 -e ALLOW_NETWORK=0 -e APP_ENV=dev -e LC_ALL=C -e LANG=C -e TZ=UTC -e DATABASE_URL=UNSET -e HD_API_KEY=UNSET -e GEO_API_KEY=UNSET -e HD_API_BASE_URL=UNSET -e HDAPI_BASE_URL=UNSET -e DB_BRIDGE_URL=UNSET -e DB_FORCE_BRIDGE=UNSET -e DB_ALLOW_BRIDGE_IN_PROD=UNSET -e ENGINE_ENV=UNSET /tmp/hde-epic040-qa-v1.2/qa-closeout-deliverables/c8.out
EOF
```

If command 6, 7 or 9 differs from its expectation, stop here (§4.6) and go to Part C.

**10.** Step 1, manifest capture ([K] inputs; N-39): the SHA-256 of the manifest, the eleven primary logs and the thirteen other supplementary files, before anything is written. Expected exit 0.

```bash
q12 10 <<'EOF'
env -u DATABASE_URL -u HD_API_KEY -u GEO_API_KEY -u HD_API_BASE_URL -u HDAPI_BASE_URL -u DB_BRIDGE_URL -u DB_FORCE_BRIDGE -u DB_ALLOW_BRIDGE_IN_PROD -u ENGINE_ENV PATH=/tmp/hde-epic040-qa-v1.2/venv/bin:$PATH SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC sha256sum audit/qa/hde-epic040/qa_step_logs_manifest.json audit/qa/hde-epic040/checks/d0-discovery/primary.log audit/qa/hde-epic040/checks/step-0b-doc-delta-capture/primary.log audit/qa/hde-epic040/checks/ac040-08-evidence-validators/primary.log audit/qa/hde-epic040/checks/ac040-02-03-catalog-config/primary.log audit/qa/hde-epic040/checks/ac040-04-05-admission-identity/primary.log audit/qa/hde-epic040/checks/ac040-06-golden-comparison/primary.log audit/qa/hde-epic040/checks/ac040-07-gate-ingress-offline/primary.log audit/qa/hde-epic040/checks/ac040-04-09-compat-cli-offline/primary.log audit/qa/hde-epic040/checks/ac040-09-reader-http-in-process/primary.log audit/qa/hde-epic040/checks/sec-reader-http-live/primary.log audit/qa/hde-epic040/checks/open-rails-showcompat-vendor/primary.log audit/docdeltas/hde-epic040_doc_deltas.md audit/qa/hde-epic040/00_meta/doc_deltas.md audit/qa/hde-epic040/checks/ac040-06-golden-comparison/compare_match_run1.json audit/qa/hde-epic040/checks/ac040-06-golden-comparison/compare_match_run2.json audit/qa/hde-epic040/checks/ac040-06-golden-comparison/tmp_goldens_altered.json audit/qa/hde-epic040/checks/ac040-06-golden-comparison/compare_mismatch_report.json audit/qa/hde-epic040/checks/sec-reader-http-live/http_probes.jsonl audit/qa/hde-epic040/checks/sec-reader-http-live/gunicorn_server.log audit/qa/hde-epic040/checks/open-rails-showcompat-vendor/vendor_request.txt audit/qa/hde-epic040/checks/open-rails-showcompat-vendor/vendor_run_ab.json audit/qa/hde-epic040/checks/open-rails-showcompat-vendor/vendor_run_ba.json audit/qa/hde-epic040/checks/open-rails-showcompat-vendor/reader_v1_ab.json audit/qa/hde-epic040/checks/open-rails-showcompat-vendor/reader_v1_ba.json
EOF
```

If command 10's standard error names one of the eleven primary logs, stop here (§4.6).

**11.** Number of digests captured. Expected `25` followed by the capture path.

```bash
q12 11 <<'EOF'
env -u DATABASE_URL -u HD_API_KEY -u GEO_API_KEY -u HD_API_BASE_URL -u HDAPI_BASE_URL -u DB_BRIDGE_URL -u DB_FORCE_BRIDGE -u DB_ALLOW_BRIDGE_IN_PROD -u ENGINE_ENV PATH=/tmp/hde-epic040-qa-v1.2/venv/bin:$PATH SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC wc -l /tmp/hde-epic040-qa-v1.2/qa-closeout-deliverables/c10.out
EOF
```

**12.** Step 2, the two doc-delta surfaces before the append. Expected exit 0 (identical).

```bash
q12 12 <<'EOF'
env -u DATABASE_URL -u HD_API_KEY -u GEO_API_KEY -u HD_API_BASE_URL -u HDAPI_BASE_URL -u DB_BRIDGE_URL -u DB_FORCE_BRIDGE -u DB_ALLOW_BRIDGE_IN_PROD -u ENGINE_ENV PATH=/tmp/hde-epic040-qa-v1.2/venv/bin:$PATH SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC cmp audit/docdeltas/hde-epic040_doc_deltas.md audit/qa/hde-epic040/00_meta/doc_deltas.md
EOF
```

**13.** Step 2, the doc-delta append: the Plan-named QA-created writer (Plan §12; N-40). Run once. Expected exit 0 and `appended 1`, then `DD-13 open-rails-showcompat-vendor`.

```bash
q12 13 <<'EOF'
env -u DATABASE_URL -u HD_API_KEY -u GEO_API_KEY -u HD_API_BASE_URL -u HDAPI_BASE_URL -u DB_BRIDGE_URL -u DB_FORCE_BRIDGE -u DB_ALLOW_BRIDGE_IN_PROD -u ENGINE_ENV PATH=/tmp/hde-epic040-qa-v1.2/venv/bin:$PATH SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC python -c "import sys; from pathlib import Path; ids = ('ac040-08-evidence-validators', 'ac040-02-03-catalog-config', 'ac040-04-05-admission-identity', 'ac040-06-golden-comparison', 'ac040-07-gate-ingress-offline', 'ac040-04-09-compat-cli-offline', 'ac040-09-reader-http-in-process', 'sec-reader-http-live', 'open-rails-showcompat-vendor'); a = Path('audit/docdeltas/hde-epic040_doc_deltas.md'); b = Path('audit/qa/hde-epic040/00_meta/doc_deltas.md'); x = a.read_bytes(); h = '## QA-DISCOVERED CAVEATS'; (not x == b.read_bytes() or not x.endswith(b'\n') or h.encode('utf-8') in x) and sys.exit('DOC_DELTA_APPEND_REFUSED: the two surfaces differ, lack a final LF, or already hold the appended section; nothing written'); rows = [(i, l) for i in ids for l in Path('audit/qa/hde-epic040/checks/' + i + '/primary.log').read_text(encoding='utf-8').splitlines() if l.startswith('DOC_DELTA:')]; t = '\n' + h + ' (check qa-closeout-deliverables)\n\nSource: every line starting DOC_DELTA: in the primary logs of QA Plan v1.2 checks 3 to 11, in Plan order. Class: CAVEAT. Drives decision: No.\n\n' + (''.join('- DD-%02d (source check %s): %s\n' % (13 + n, i, l) for n, (i, l) in enumerate(rows)) if rows else 'No new deltas found during execution.\n'); [p.write_bytes(x + t.encode('utf-8')) for p in (a, b)]; print('appended', len(rows)); [print('DD-%02d' % (13 + n), i) for n, (i, l) in enumerate(rows)]"
EOF
```

**14.** Step 2 verification ([E]; the writer's verifying predicate, Plan §12): the two surfaces after the append. Expected exit 0.

```bash
q12 14 <<'EOF'
env -u DATABASE_URL -u HD_API_KEY -u GEO_API_KEY -u HD_API_BASE_URL -u HDAPI_BASE_URL -u DB_BRIDGE_URL -u DB_FORCE_BRIDGE -u DB_ALLOW_BRIDGE_IN_PROD -u ENGINE_ENV PATH=/tmp/hde-epic040-qa-v1.2/venv/bin:$PATH SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC cmp audit/docdeltas/hde-epic040_doc_deltas.md audit/qa/hde-epic040/00_meta/doc_deltas.md
EOF
```

**15.** Digests of both surfaces after the append (capture only).

```bash
q12 15 <<'EOF'
env -u DATABASE_URL -u HD_API_KEY -u GEO_API_KEY -u HD_API_BASE_URL -u HDAPI_BASE_URL -u DB_BRIDGE_URL -u DB_FORCE_BRIDGE -u DB_ALLOW_BRIDGE_IN_PROD -u ENGINE_ENV PATH=/tmp/hde-epic040-qa-v1.2/venv/bin:$PATH SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC sha256sum audit/docdeltas/hde-epic040_doc_deltas.md audit/qa/hde-epic040/00_meta/doc_deltas.md
EOF
```

**16.** Step 3, path proofs of the before-record set, written (N-41). Run once. Expected exit 0, a `default_produced_at` line and thirteen proof paths.

```bash
q12 16 <<'EOF'
env -u DATABASE_URL -u HD_API_KEY -u GEO_API_KEY -u HD_API_BASE_URL -u HDAPI_BASE_URL -u DB_BRIDGE_URL -u DB_FORCE_BRIDGE -u DB_ALLOW_BRIDGE_IN_PROD -u ENGINE_ENV PATH=/tmp/hde-epic040-qa-v1.2/venv/bin:$PATH SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC python -c "import datetime as d; import tools.evidence.update_evidence_index as u; ids = ('d0-discovery', 'step-0b-doc-delta-capture', 'ac040-08-evidence-validators', 'ac040-02-03-catalog-config', 'ac040-04-05-admission-identity', 'ac040-06-golden-comparison', 'ac040-07-gate-ingress-offline', 'ac040-04-09-compat-cli-offline', 'ac040-09-reader-http-in-process', 'sec-reader-http-live', 'open-rails-showcompat-vendor'); ps = ['audit/qa/hde-epic040/checks/' + i + '/primary.log' for i in ids] + ['audit/docdeltas/hde-epic040_doc_deltas.md', 'audit/qa/hde-epic040/00_meta/doc_deltas.md']; t = d.datetime.now(d.timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z'); [u._refresh_path_proof(u.ROOT / p, default_produced_at=t, check=False) for p in ps]; print('default_produced_at', t); [print(p + '.path_proof.txt') for p in ps]"
EOF
```

**17.** Step 3, the same thirteen proofs in check mode ([E]). Expected exit 0 and `check mode passed 13`.

```bash
q12 17 <<'EOF'
env -u DATABASE_URL -u HD_API_KEY -u GEO_API_KEY -u HD_API_BASE_URL -u HDAPI_BASE_URL -u DB_BRIDGE_URL -u DB_FORCE_BRIDGE -u DB_ALLOW_BRIDGE_IN_PROD -u ENGINE_ENV PATH=/tmp/hde-epic040-qa-v1.2/venv/bin:$PATH SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC python -c "import datetime as d; import tools.evidence.update_evidence_index as u; ids = ('d0-discovery', 'step-0b-doc-delta-capture', 'ac040-08-evidence-validators', 'ac040-02-03-catalog-config', 'ac040-04-05-admission-identity', 'ac040-06-golden-comparison', 'ac040-07-gate-ingress-offline', 'ac040-04-09-compat-cli-offline', 'ac040-09-reader-http-in-process', 'sec-reader-http-live', 'open-rails-showcompat-vendor'); ps = ['audit/qa/hde-epic040/checks/' + i + '/primary.log' for i in ids] + ['audit/docdeltas/hde-epic040_doc_deltas.md', 'audit/qa/hde-epic040/00_meta/doc_deltas.md']; t = d.datetime.now(d.timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z'); [u._refresh_path_proof(u.ROOT / p, default_produced_at=t, check=True) for p in ps]; print('check mode passed', len(ps))"
EOF
```

**18.** The thirteen proofs, printed into the body (capture only).

```bash
q12 18 <<'EOF'
env -u DATABASE_URL -u HD_API_KEY -u GEO_API_KEY -u HD_API_BASE_URL -u HDAPI_BASE_URL -u DB_BRIDGE_URL -u DB_FORCE_BRIDGE -u DB_ALLOW_BRIDGE_IN_PROD -u ENGINE_ENV PATH=/tmp/hde-epic040-qa-v1.2/venv/bin:$PATH SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC cat audit/qa/hde-epic040/checks/d0-discovery/primary.log.path_proof.txt audit/qa/hde-epic040/checks/step-0b-doc-delta-capture/primary.log.path_proof.txt audit/qa/hde-epic040/checks/ac040-08-evidence-validators/primary.log.path_proof.txt audit/qa/hde-epic040/checks/ac040-02-03-catalog-config/primary.log.path_proof.txt audit/qa/hde-epic040/checks/ac040-04-05-admission-identity/primary.log.path_proof.txt audit/qa/hde-epic040/checks/ac040-06-golden-comparison/primary.log.path_proof.txt audit/qa/hde-epic040/checks/ac040-07-gate-ingress-offline/primary.log.path_proof.txt audit/qa/hde-epic040/checks/ac040-04-09-compat-cli-offline/primary.log.path_proof.txt audit/qa/hde-epic040/checks/ac040-09-reader-http-in-process/primary.log.path_proof.txt audit/qa/hde-epic040/checks/sec-reader-http-live/primary.log.path_proof.txt audit/qa/hde-epic040/checks/open-rails-showcompat-vendor/primary.log.path_proof.txt audit/docdeltas/hde-epic040_doc_deltas.md.path_proof.txt audit/qa/hde-epic040/00_meta/doc_deltas.md.path_proof.txt
EOF
```

**19.** Step 4, governed-graph non-interference: the evidence updater in check mode, with the QA files present. Expected exit 0.

```bash
q12 19 <<'EOF'
env -u DATABASE_URL -u HD_API_KEY -u GEO_API_KEY -u HD_API_BASE_URL -u HDAPI_BASE_URL -u DB_BRIDGE_URL -u DB_FORCE_BRIDGE -u DB_ALLOW_BRIDGE_IN_PROD -u ENGINE_ENV PATH=/tmp/hde-epic040-qa-v1.2/venv/bin:$PATH SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC python tools/evidence/update_evidence_index.py --check
EOF
```

**20.** Step 4, the evidence path validator (the final decisive command). Expected exit 0.

```bash
q12 20 <<'EOF'
env -u DATABASE_URL -u HD_API_KEY -u GEO_API_KEY -u HD_API_BASE_URL -u HDAPI_BASE_URL -u DB_BRIDGE_URL -u DB_FORCE_BRIDGE -u DB_ALLOW_BRIDGE_IN_PROD -u ENGINE_ENV PATH=/tmp/hde-epic040-qa-v1.2/venv/bin:$PATH SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC python tools/evidence/validate_evidence_paths.py
EOF
```

**21.** Step 5, tracked-file observation (attribution only, non-gating). Expected: ` M` lines for the two doc-delta surfaces and `??` lines for the thirteen proofs. Any other path is listed for Kronos and is never committed.

```bash
q12 21 <<'EOF'
env -u DATABASE_URL -u HD_API_KEY -u GEO_API_KEY -u HD_API_BASE_URL -u HDAPI_BASE_URL -u DB_BRIDGE_URL -u DB_FORCE_BRIDGE -u DB_ALLOW_BRIDGE_IN_PROD -u ENGINE_ENV PATH=/tmp/hde-epic040-qa-v1.2/venv/bin:$PATH SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC git status --porcelain
EOF
```

**22.** Step 6, coverage accounting (N-42). Expected exit 0, twelve `COVERAGE` lines in Plan order and one `DEFERRED` line.

```bash
q12 22 <<'EOF'
env -u DATABASE_URL -u HD_API_KEY -u GEO_API_KEY -u HD_API_BASE_URL -u HDAPI_BASE_URL -u DB_BRIDGE_URL -u DB_FORCE_BRIDGE -u DB_ALLOW_BRIDGE_IN_PROD -u ENGINE_ENV PATH=/tmp/hde-epic040-qa-v1.2/venv/bin:$PATH SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC sh -c 'M=audit/qa/hde-epic040/qa_step_logs_manifest.json; p() { e=$(grep -o -E "\"$2\":[{][^}]*[}]" "$M"); a=$(grep -o -m 1 -E "\"evidence_artifacts\":\[[^]]*\]" "audit/qa/hde-epic040/checks/$2/primary.log"); case "$e" in *\"status\":\"PASS\"*) f="none at execution; the per-task result is decided by Kronos at QA-110";; *) f="the blocking precondition is the status_reason in the primary-log header of this check; the follow-up is decided by Kronos at QA-110 (Plan section 7.3)";; esac; printf "COVERAGE %s %s | manifest entry %s | attempt lineage %s | evidence %s | follow-up %s\n" "$1" "$2" "${e:-absent}" "$3" "${a:-absent}" "$f"; }; R="Run A executed it first (branch qa/hde-epic040-qa100-plan-v1.2 at e5b671c), which is attempt 1; the Run B execution at 345148b is the evidence of record and is not an authorized attempt 2 (QA-110 review v1.0 ruling LR-01 items 2 to 5)"; p 1 d0-discovery "$R"; p 2 step-0b-doc-delta-capture "$R"; p 3 ac040-08-evidence-validators "one recorded execution (Run B at 345148b); attempt 1 unless Run A executed it, which is unknown (QA-110 review v1.0 ruling LR-01 items 2, 3 and 7)"; p 4 ac040-02-03-catalog-config "$R"; p 5 ac040-04-05-admission-identity "$R"; p 6 ac040-06-golden-comparison "$R"; p 7 ac040-07-gate-ingress-offline "$R"; p 8 ac040-04-09-compat-cli-offline "$R"; p 9 ac040-09-reader-http-in-process "$R"; p 10 sec-reader-http-live "$R"; p 11 open-rails-showcompat-vendor "attempt 1 (Run B stream at 380cf46; QA-110 review T11 v1.0)"; printf "COVERAGE 12 qa-closeout-deliverables | manifest entry written by the recording of this check | attempt lineage attempt 1 (task T12 of QA-90 collection v1.4) | evidence audit/qa/hde-epic040/checks/qa-closeout-deliverables/primary.log with the path proofs of Plan check 12 steps 3 and 8 | follow-up per the header of this primary log\n"; printf "DEFERRED QA Plan v1.2 section 2: live Gate readiness and live DB Reader success are deferred requirements, not checks; no command ran for them (Glow QA Guide section 3.3)\n"'
EOF
```

**23.** Count of the check lines of the coverage accounting. Expected `12`.

```bash
q12 23 <<'EOF'
env -u DATABASE_URL -u HD_API_KEY -u GEO_API_KEY -u HD_API_BASE_URL -u HDAPI_BASE_URL -u DB_BRIDGE_URL -u DB_FORCE_BRIDGE -u DB_ALLOW_BRIDGE_IN_PROD -u ENGINE_ENV PATH=/tmp/hde-epic040-qa-v1.2/venv/bin:$PATH SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC grep -c -E '^COVERAGE ([1-9]|1[0-2]) ' /tmp/hde-epic040-qa-v1.2/qa-closeout-deliverables/c22.out
EOF
```

### Part C — body, recording, finalization and verification

**W2.** COMMANDS and OUTPUT sections (writer, not a check command). It prints the captures of every label in `cmds.txt`, in execution order, repeats included. Expected last line `W2_WRITTEN`.

```bash
sh -c 'Q=/tmp/hde-epic040-qa-v1.2/qa-closeout-deliverables; { printf "=== COMMANDS ===\n"; cat "$Q/cmds.txt"; printf "=== OUTPUT ===\n"; for k in $(sed -n -e "s/^\[\([^]]*\)\] exit=.*/\1/p" "$Q/cmds.txt"); do printf "[%s] exit=%s\n" "$k" "$(cat "$Q/c$k.rc")"; printf "[%s] stdout:\n" "$k"; cat "$Q/c$k.out"; printf "[%s] stderr:\n" "$k"; cat "$Q/c$k.err"; done; } >> "$Q/body.txt"; echo W2_WRITTEN'
```

**W3.** PREDICATES, observed values (writer, first half; not a check command):

```bash
sh -c 'Q=/tmp/hde-epic040-qa-v1.2/qa-closeout-deliverables; o() { if [ -e "$Q/c$1.rc" ]; then printf "command %s: exit=%s stdout=%s\n" "$1" "$(cat "$Q/c$1.rc")" "$(tr "\n" " " < "$Q/c$1.out" | cut -c 1-300)"; else printf "command %s: not executed\n" "$1"; fi; }; { printf "=== PREDICATES ===\n"; printf "Observed values, from the capture files:\n"; for k in 3 4 5 6 7 9 10 11 12 13 14 16 17 19 20 22 23; do o "$k"; done; } >> "$Q/body.txt"'
```

Then append one result line per [E] predicate, `PASS` or `FAIL` with the observed value, by `printf` into `body.txt`, in this form and order:

| Line | Predicate (Plan check 12) | Holds when |
| --- | --- | --- |
| `E1 dependency gate` | Every other check recorded (Plan §11) | command 3 exit 0; commands 4 and 5 printed `11` |
| `E2 readiness line` | Python 3.12, the tested install, the closed posture | command 6 printed `Python 3.12.`; command 7 exit 0 and printed `/tmp/hde-epic040-qa-v1.2/venv/bin/python`; command 9 printed `15` |
| `E3 step-1 digests captured` | The step-1 digests are captured | command 10 exit 0; command 11 printed `25` |
| `E4 doc-delta surfaces byte-identical after the append` | Plan step 2 | commands 12, 13 and 14 exit 0 |
| `E5 path proofs pass check mode` | Plan step 3 | commands 16 and 17 exit 0; command 17 printed `check mode passed 13` |
| `E6 governed graph with the QA files present` | Plan step 4 | commands 19 and 20 exit 0 |
| `E7 coverage accounting written` | Plan step 6 | command 22 exit 0; command 23 printed `12` |

**W4.** The [K] predicates, the two-layer statement and LIMITS (writer; not a check command):

```bash
sh -c 'Q=/tmp/hde-epic040-qa-v1.2/qa-closeout-deliverables; { printf "[K] K1 the manifest whose digest command 10 recorded holds exactly one entry for each of checks 1 to 11 of QA Plan v1.2 section 11, all recorded before this check: pending QA-110\n"; printf "[K] K2 each log_path is the concrete primary-log path that the check block states: pending QA-110\n"; printf "[K] K3 each primary log is non-empty, LF-terminated and starts with a pf27.step_log_header.v2 header whose status equals the manifest status: pending QA-110\n"; printf "[K] K4 every supplementary file named in a primary log exists with the recorded SHA-256: pending QA-110\n"; printf "[K] K5 the coverage accounting lists every check of QA Plan v1.2 section 11: pending QA-110\n"; printf "[K] Step 8 each finalization path proof (this primary log; the manifest) has the sha256 and size_bytes of its file: pending QA-110\n"; printf "Step-log status attests the execution layer only; [K] predicates are evaluated by Kronos at QA-110.\n"; printf "=== LIMITS ===\n"; printf "Proof class: local/offline integrity of the QA run evidence under the closed posture; no vendor, database, server or network; no product-behavior claim (FAIL_BEHAVIOR not applicable).\n"; printf "The path proofs bind the path, size and SHA-256 of each QA file; mtime_utc is capture-time provenance (PF12-Canon-HDE-Schemas-and-Artifacts MTIME-UTC-SEMANTICS).\n"; printf "Step 4 shows that the governed evidence checks pass with the QA files present; it registers no QA file in the Human Evidence Index or the Machine Mirror, and the manifest is not claimed to be ledger-bound (PF19-Canon-Glow-QA-Guide section 4.4.3; QA Plan v1.2 section 8).\n"; printf "The path proofs of this primary log and of the final manifest are written after this log is recorded (QA Plan v1.2 check 12 step 8), outside this log.\n"; printf "Nonclaims: no QA PASS for the change, acceptance, closure, PF09 status change, close-pack, Index or Mirror publication, deployment, token, new public route or flag, or PF edit follows from this result.\n"; } >> "$Q/body.txt"'
```

**C3.** Recording inputs, each written by `printf` or `cp` from the captures:

- `status.txt`: line 1 the status of §4.7; line 2 the causal reason, absent for `PASS`.
- `final.rc`: a copy of `c20.rc`; if command 20 did not run, a copy of the `.rc` file of the last check command that ran.
- `provenance.txt`, one line: `QA Plan v1.2 CHECK 12 qa-closeout-deliverables (docs/ephemeral/HDE-EPIC040-QA50-qa-plan-v1.2.md); QA-90 collection v1.4 task T12 (docs/ephemeral/HDE-EPIC040-QA90-qa-task-collection-v1.4.md); attempt 1; executed and recorded by ` followed by the identity in `executor_identity.txt`, then `; normalizations: N-01, N-02, N-03, N-05, N-06, N-36 to N-45` and any executor normalization, with its reason.

**C4.** Recording (Plan check 12 step 7; not a check command and not in `argv.txt`; N-43). Expected: exit 0 and two printed paths, the primary log and `audit/qa/hde-epic040/qa_step_logs_manifest.json`.

```bash
env -u DATABASE_URL -u HD_API_KEY -u GEO_API_KEY -u HD_API_BASE_URL -u HDAPI_BASE_URL -u DB_BRIDGE_URL -u DB_FORCE_BRIDGE -u DB_ALLOW_BRIDGE_IN_PROD -u ENGINE_ENV PATH=/tmp/hde-epic040-qa-v1.2/venv/bin:$PATH SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC python -c "import shlex; from pathlib import Path; from tools.qa.qa_harness import HarnessConfig, CheckResult, Status, record_check; s = Path('/tmp/hde-epic040-qa-v1.2/qa-closeout-deliverables'); ids = ('d0-discovery', 'step-0b-doc-delta-capture', 'ac040-08-evidence-validators', 'ac040-02-03-catalog-config', 'ac040-04-05-admission-identity', 'ac040-06-golden-comparison', 'ac040-07-gate-ingress-offline', 'ac040-04-09-compat-cli-offline', 'ac040-09-reader-http-in-process', 'sec-reader-http-live', 'open-rails-showcompat-vendor'); dd = ('audit/docdeltas/hde-epic040_doc_deltas.md', 'audit/qa/hde-epic040/00_meta/doc_deltas.md') if (s / 'c12.rc').is_file() else (); ea = tuple(p for p in dd + tuple('audit/qa/hde-epic040/checks/' + i + '/primary.log.path_proof.txt' for i in ids) + tuple(p + '.path_proof.txt' for p in dd) if Path(p).is_file()); st = (s / 'status.txt').read_text(encoding='utf-8').splitlines(); cmd = tuple(tuple(shlex.split(x)) for x in (s / 'argv.txt').read_text(encoding='utf-8').splitlines() if x.strip()); r = CheckResult(check_id='qa-closeout-deliverables', check_name='Close-out deliverables and coverage', status=Status(st[0].strip()), status_reason=' '.join(x.strip() for x in st[1:] if x.strip()), command=cmd, command_provenance=(s / 'provenance.txt').read_text(encoding='utf-8').strip() if cmd else 'Not executed', exit_code=int((s / 'final.rc').read_text(encoding='utf-8').strip()) if cmd else None, output=(s / 'body.txt').read_text(encoding='utf-8'), evidence_artifacts=ea, intended_tokens=(), pf_refs=('PF06-Canon-Change-Process-Guide', 'PF19-Canon-Glow-QA-Guide'), captured_env=(('LC_ALL', 'C'), ('LANG', 'C'), ('TZ', 'UTC'), ('SAFE_MODE', '1'), ('ALLOW_NETWORK', '0'), ('APP_ENV', 'dev'))); print(*record_check(HarnessConfig('HDE-EPIC040', Path.cwd()), r))"
```

**C5.** Finalization (Plan check 12 step 8; not a check command; N-44): the path proofs of this check's primary log and of the manifest, written and then checked. Run each once, in order. Expected: `f1.rc` 0 with two proof paths, then `f2.rc` 0 with `check mode passed 2`.

```bash
env -u DATABASE_URL -u HD_API_KEY -u GEO_API_KEY -u HD_API_BASE_URL -u HDAPI_BASE_URL -u DB_BRIDGE_URL -u DB_FORCE_BRIDGE -u DB_ALLOW_BRIDGE_IN_PROD -u ENGINE_ENV PATH=/tmp/hde-epic040-qa-v1.2/venv/bin:$PATH SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC python -c "import datetime as d; import tools.evidence.update_evidence_index as u; ps = ['audit/qa/hde-epic040/checks/qa-closeout-deliverables/primary.log', 'audit/qa/hde-epic040/qa_step_logs_manifest.json']; t = d.datetime.now(d.timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z'); [u._refresh_path_proof(u.ROOT / p, default_produced_at=t, check=False) for p in ps]; print('default_produced_at', t); [print(p + '.path_proof.txt') for p in ps]" > /tmp/hde-epic040-qa-v1.2/qa-closeout-deliverables/f1.out 2> /tmp/hde-epic040-qa-v1.2/qa-closeout-deliverables/f1.err; echo $? > /tmp/hde-epic040-qa-v1.2/qa-closeout-deliverables/f1.rc; cat /tmp/hde-epic040-qa-v1.2/qa-closeout-deliverables/f1.rc /tmp/hde-epic040-qa-v1.2/qa-closeout-deliverables/f1.out /tmp/hde-epic040-qa-v1.2/qa-closeout-deliverables/f1.err
```

```bash
env -u DATABASE_URL -u HD_API_KEY -u GEO_API_KEY -u HD_API_BASE_URL -u HDAPI_BASE_URL -u DB_BRIDGE_URL -u DB_FORCE_BRIDGE -u DB_ALLOW_BRIDGE_IN_PROD -u ENGINE_ENV PATH=/tmp/hde-epic040-qa-v1.2/venv/bin:$PATH SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC python -c "import datetime as d; import tools.evidence.update_evidence_index as u; ps = ['audit/qa/hde-epic040/checks/qa-closeout-deliverables/primary.log', 'audit/qa/hde-epic040/qa_step_logs_manifest.json']; t = d.datetime.now(d.timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z'); [u._refresh_path_proof(u.ROOT / p, default_produced_at=t, check=True) for p in ps]; print('check mode passed', len(ps))" > /tmp/hde-epic040-qa-v1.2/qa-closeout-deliverables/f2.out 2> /tmp/hde-epic040-qa-v1.2/qa-closeout-deliverables/f2.err; echo $? > /tmp/hde-epic040-qa-v1.2/qa-closeout-deliverables/f2.rc; cat /tmp/hde-epic040-qa-v1.2/qa-closeout-deliverables/f2.rc /tmp/hde-epic040-qa-v1.2/qa-closeout-deliverables/f2.out /tmp/hde-epic040-qa-v1.2/qa-closeout-deliverables/f2.err
```

**C6.** Verification (not a check command). Expected: `manifest parses`, `12`, the `qa-closeout-deliverables` entry with the header's status, the header's first characters `{"captured_env"` and `"schema_version":"pf27.step_log_header.v2"`, a final `\n`, then the SHA-256 of the 19 files of §4.8 for the QA-100 result and the storage check:

```bash
env -u DATABASE_URL -u HD_API_KEY -u GEO_API_KEY -u HD_API_BASE_URL -u HDAPI_BASE_URL -u DB_BRIDGE_URL -u DB_FORCE_BRIDGE -u DB_ALLOW_BRIDGE_IN_PROD -u ENGINE_ENV PATH=/tmp/hde-epic040-qa-v1.2/venv/bin:$PATH SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC sh -c 'M=audit/qa/hde-epic040/qa_step_logs_manifest.json; L=audit/qa/hde-epic040/checks/qa-closeout-deliverables/primary.log; python -m json.tool "$M" > /dev/null && echo "manifest parses"; grep -o -F "\"check_id\":\"" "$M" | wc -l; grep -o -E "\"qa-closeout-deliverables\":[{][^}]*[}]" "$M"; head -c 15 "$L"; echo; grep -o -m 1 -E "\"schema_version\":\"[^\"]*\"|\"status\":\"[A-Z_]*\"" "$L"; tail -c 1 "$L" | od -An -c; sha256sum "$M" audit/docdeltas/hde-epic040_doc_deltas.md audit/qa/hde-epic040/00_meta/doc_deltas.md "$L" audit/qa/hde-epic040/checks/*/primary.log.path_proof.txt "$M.path_proof.txt" audit/docdeltas/hde-epic040_doc_deltas.md.path_proof.txt audit/qa/hde-epic040/00_meta/doc_deltas.md.path_proof.txt'
```

Then store the evidence under §4.8.

**[K] predicates (Kronos at QA-110; Plan check 12):** K1 to K5 and the step 8 proofs, exactly as W4 writes them, from the manifest, the primary logs and supplementary files whose digests command 10 captured, the body and the two finalization proofs. A false [K] predicate makes the per-task result `FAIL_TOOLING` (Plan check 12: "at QA-110, if the manifest and a primary log disagree or a supplementary file is missing or changed").

**Nonclaims (Plan check 12, §8, §13, §15):** the check proves the integrity of the QA run's own evidence, the doc-delta append, the path proofs, the governed evidence checks with the QA files present, and the coverage accounting that QA-120 uses. It makes no product-behavior claim, does not claim a ledger-bound manifest, and registers nothing in the Human Evidence Index or the Machine Mirror. It is not the QA-120 Report, the RCA or a close pack.

## 6. CANON_CONFLICT_REGISTER (carried)

Carried unchanged from the QA-110 review T11 v1.0 §7, which carried C040-01 to C040-09 from Plan v1.2 §2.3 through collection v1.3 §6 and review v1.0 §9, and entered C040-10. QA-90 adds no entry and changes no field. C040-09's interim treatment applies to T12: read-only git observations for attribution only, never a PASS gate; the tracked harness APIs (`tools.qa.qa_harness`, `_refresh_path_proof`) through `python -c`; no script file; no decisive evaluator written at run time. PF10 references in the rows use the v13.3.9 numbering, which v13.4.2 to v13.4.5 keep for 2.2 to 2.28. A proposal here is not approval.

| ID | Classification | Sources and clauses | Decision and status | Reviewer, artifact, time | Interim treatment | Drainage target and owner | Full history |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C040-01 | CANON_RECONCILIATION | Pinned source/scope predicate | APPROVED exactly as proposed | Thoth-17, Specification v1.0 (represented by approved v1.1), 2026-09-08T13:23:24Z | Resolved | None pending | Plan v2.1 §§11.1–11.2; PF10 v13.3.9 §2.2, §2.4 |
| C040-02 | CANON_RECONCILIATION | PF12 filename and body version | APPROVED | Thoth-17, same decision | Resolved | None pending | Plan v2.1 §§11.1–11.2; PF10 §2.2, §2.4 |
| C040-03 | CANON_RECONCILIATION | PF14 filename and body version | APPROVED | Thoth-17, same decision | Resolved | None pending | Plan v2.1 §§11.1–11.2; PF10 §2.2, §2.4 |
| C040-04 | CANON_RECONCILIATION | PF19 filename and body version | APPROVED | Thoth-17, same decision | Resolved | None pending | Plan v2.1 §§11.1–11.2; PF10 §2.2, §2.4 |
| C040-05 | CANON_RECONCILIATION | PF14 §6.7 superseded precomputed-score test instructions | APPROVED, alternative A | Isis-49, Plan v1.0 review, 2026-09-09T03:57:16Z | PF10 §2.3 governs | PF14 §6.7; PF14 maintainer; pending, non-gating | Plan v2.1 §11.2; PF10 §2.3 |
| C040-06 | NEW_CANON | 36-row Channel taxonomy and 16-case existing-state conformance | APPROVED, alternative A | Isis-50, Implementation Plan Review v2.0, 2026-09-09T11:48:08Z | PF10 §2.5 governs | PF12 §2.1, PF01 §§6.1–6.2; their maintainers; pending | Plan v2.1 §11.3; `docs/ephemeral/HDE-EPIC040-C040-06-HD-mechanics-ADR-v1.0.md`; PF10 §2.5 |
| C040-07 | NEW_CANON | Full Magic-10 exposure via Reader v2 versus Specification line 265 and PF01, PF04, PF05, PF12 statements | PO decision 2026-09-26; delivered by PR06a | Product Owner; PF10 §2.23 | PF10 §2.23 governs; QA tests `?v=2` | PF01, PF04, PF05, PF12, with PF14 and PF29 consequences; their maintainers; pending | PF10 §2.23, §2.24 |
| C040-08 | CANON_RECONCILIATION | Reader v1 error envelope versus schema | Alternative A; delivered by PR06b | PF10 §2.25 decision record | PF10 §2.25 governs; QA asserts the four-key envelope | PF01 §2.3, PF04 §8.1.2; their maintainers; pending | PF10 §2.25, §2.26 |
| C040-09 | CANON_CONFLICT (QA process) | PF07-Canon-Glow-Infrastructure §2.8 ("Live QA runbooks MUST NOT include git operations"; "QA plans MUST NOT create new scripts at run time") versus PF19-Canon-Glow-QA-Guide §3.4.9 (read-only repository observations may establish source) and §3.6, and PF27-Canon-Plan-Templates ("Embedded harness checks"; QA-only harness scaffolding permitted) | `APPROVED_AS_CHANGED`. Proposed: alternative (a), PF19 and PF27 govern the execution rail and plan shape; alternative (b), forbid all git reads and embedded helpers, which loses the tested-source attribution PF19 §10.8 requires, was not adopted. Change: the approval covers invoking tracked, tested entrypoints (`tools.qa.qa_harness`, `_refresh_path_proof`) through `python -c`; it does not cover newly written decisive evaluators, which Glow QA Guide §3.4.8 governs. Rationale: Glow Infrastructure §2.1 is names-only ("No procedures or policy here") and §2.8 routes the Live QA execution rail to the Glow QA Guide, so Glow QA Guide §3.4.9 (read-only repository observation for attribution, never a PASS predicate) and Plan Templates govern | Isis, continuing QA Plan reviewer (execution identity https://claude.ai/code/session_015Y2tpUnUNcpBoCzwN3aRXq); reviewed QA Plan v1.0 and QA Audit v1.0; decision in `docs/ephemeral/HDE-EPIC040-QA70-qa-plan-review-v1.1.md` §3, "Decisions carried to this review"; 2026-09-27 | Applied in this Plan: read-only git observations for attribution only, never a PASS gate; no script file is created; tracked harness APIs through `python -c`; no decisive evaluator written at run time (§12). Unresolved risk: a reader who applies PF07 §2.8 literally until its wording is drained | PF07 §2.8 wording; PF07 maintainer; documentation drainage only | Original proposal: QA Audit v1.0 §11 (`PROPOSED`, 2026-09-27). QA-70 review v1.0 §4: APPROVED as proposed; that review was rejected by the Product Owner on 2026-09-27 and is history only (RCA v1.1, C2). QA-70 review v1.1 §3: `APPROVED_AS_CHANGED` (current) |
| C040-10 | CANON_CONFLICT (vendor execution authority) | Barring an automated agent from the vendor call or requiring the Product Owner as executor: Glow QA Guide §3.3 and §3.5.7; HDE CLI/API Vendor Ref §3.7 and §7.1.8a; HDE Governance §3.4 ("Controlled vendor-backed no-user validation") and §11.1; HDE Mechanics Guide §1.1 and §17.9.4; Plan Templates "Artifact execution boundary" and "Proof-class and controlled vendor-smoke boundary"; HDE Build Checklist Fermentation, HDE-FERM008 and HDE-FERM008.2. Versus Product Owner-delegated execution: HDE Governance §3.4 ("HDAPI v2 open-rails vendor proof posture") and §9.1; Change Process Guide "Ops tasks"; Plan Templates "Execution authority (normative)", which are written for Ops tasks | Product Owner decision, 2026-09-29, recorded as HDE Build Notes addendum 2.34 PF10-VENDOR-001 (v13.4.5). A directed agent executes live vendor calls, including open-rails HumanDesignAPI calls in QA checks; "PO-only" names the authorizing principal; vendor configuration comes from environment variables. The listed bars are superseded for that scope | Product Owner; HDE Build Notes v13.4.5 addendum 2.34 (Timestamp 092926 06:04 UTC); direction given in the QA-100 session that executed T11 | PF10 2.34 governs; T11's delegated execution is authorized (QA-110 review T11 v1.0 §4.3) | The passages in 2.34's superseded-passage table; their maintainers; pending (2.34: "Drainage into the listed documents is unperformed") | Observed as a canon tension in collection v1.3 §7 on 2026-09-29, and not entered then because no decision of the change depended on it. It became decisive when the Product Owner directed the QA-100 session to execute T11's vendor commands (result D-01), and was decided the same day by addendum 2.34. Entered by the QA-110 review T11 v1.0 |

Affected requirements for C040-09: AC040-08 and AC040-09 evidence attribution (K040-REQ-012, K040-REQ-013). Affected requirements for C040-10: the vendor-backed part of AC040-04 and AC040-09 (Plan check 11) and PO Q-2.

## 7. Constraints, open inputs and unresolved items

| Item | Owner | Status |
| --- | --- | --- |
| Executor identity (§4.1) | The QA-100 operator session; recorded in Part A | PENDING until that session exists |
| Storage authorization (§4.3 item 6) | Product Owner, asked at the start of the QA-100 session | PENDING |
| Evidence commit on `qa/hde-epic040-qa100-plan-v1.2-run-20260929` | The QA-100 executor under §4.8 | PENDING until execution; any pull request and merge are the Product Owner's |
| Per-task result, K1 to K5, the step 8 proofs, any attempt 2 or Moon Loop | Kronos-23 at QA-110 | After QA-100 |
| The QA-120 Report and the separate RCA, including lessons K-01 to K-06 and the deviations of both QA-110 reviews | Kronos-23 at QA-120 | After T12 is accepted |
| Index and Mirror registration of the HDE-EPIC040 QA evidence (QA50-F01) | Evidence owner, through the whole-change IA PR route (Plan §14) | Follow-up; not part of check 12 |
| Drainage of DD-01 to DD-13 and of C040-05 to C040-10 | Their named maintainers | Documentation drainage only; never a blocker for a step verdict (Plan §13) |
| Run A's T03 outcome and T10 receipt (QA-110 review v1.0 LR-01 item 7) | Product Owner | Open, non-gating; unchanged |
| QA-110 review T11 v1.0 and its checkpoint and handoff on `main` | Product Owner (merge of pull request amthorn78/glow-hdengine-v2#552, which also carries this collection) | Open |
| Repository persistence of `GCFPE_PROMPT_USES` | The authorized repository writer under an installed `docs/changes/GCFPE_PROMPT_PROVENANCE.md` procedure | PENDING / NON_GATING: no such procedure at `633ca5d` |

## 8. Working state

| Field | Value |
| --- | --- |
| Stage | QA-90 complete for the selection "check 12"; next QA-100 |
| Collection | This file, v1.4, `TASK_READY` |
| Checkpoint | `docs/ephemeral/HDE-EPIC040-QA90-checkpoint-v1.4.md` |
| Handoff | `docs/ephemeral/HDE-EPIC040-QA90-handoff-to-qa100-v1.4.md` |
| Resume point for QA-100 | §4.3 setup, then §5 Part A |

## 9. Nonclaims

This collection executes nothing and produces no evidence. It establishes no QA PASS, acceptance, closure, PF09 status movement, PF-Canon drainage, PF10 addendum, deployment, release activation, token satisfaction, close pack, ledger-bound manifest or Index/Mirror publication. Every artifact named in §5 is NOT RUN until T12 executes.

## Provenance

GCFPE_PROMPT_USES (without a fenced block, per Plan Templates "Template-safe placeholders and omission syntax"):

- usage_id: GCFPE-USE-HDE-EPIC040-QA-90-20260929-03
  - change: EPIC / HDE-EPIC040 (Specification v1.1)
  - requirements and components: AC040-01 and AC040-08 (evidence integrity of the QA run), D11, as mapped by Plan v1.2 check 12
  - prompt: QA-90 — Create Bounded QA Execution Task — 091426.1; Notion 3db4590a05eb811e8582cf30238c5b9c; page as of 2026-09-24T15:56:22.252Z (read in full at this invocation); release GCFPE-20260914.1
  - role_stage: Kronos-23, QA-90 (selection "check 12")
  - capture_time: 2026-09-29T07:21:27Z
  - execution_identity: https://claude.ai/code/session_01PnD4YNbFZStRQWZ7TCM6jV
  - result: QA_TASK_COLLECTION v1.4, TASK_READY, task T12 at attempt 1, routed to QA-100
  - task_and_attempt_mapping: T12 `qa-closeout-deliverables`, attempt 1; result mapping PENDING until QA-100
  - repository_persistence: PENDING / NON_GATING (no installed `docs/changes/GCFPE_PROMPT_PROVENANCE.md` at `633ca5d`; owner: the authorized repository writer under that procedure once it is installed)
- Earlier uses, each recorded in its own artifact: GCFPE-USE-HDE-EPIC040-QA-110-20260929-02 (QA-110 review T11 v1.0); GCFPE-USE-HDE-EPIC040-QA-100-20260929-02 (QA-100 result T11 v1.0); GCFPE-USE-HDE-EPIC040-QA-90-20260929-02 (collection v1.3); GCFPE-USE-HDE-EPIC040-QA-90-20260929-01 (collection v1.2); GCFPE-USE-HDE-EPIC040-QA-110-20260929-01 (review v1.0); GCFPE-USE-HDE-EPIC040-QA-100-20260929-01 (results v1.1); GCFPE-USE-HDE-EPIC040-QA-90-20260928-01 (collection v1.1).
