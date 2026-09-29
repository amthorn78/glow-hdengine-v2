---
artifact_type: CHANGE_CLOSURE_DECISION
artifact_title: Epic Retrospective and Closure Decision
artifact_version: "1.1"
logical_id: HDE-EPIC040-CL-E-10-CHANGE-CLOSURE-DECISION
predecessor: docs/ephemeral/HDE-EPIC040-CL-E-10-closure-decision-v1.0.md (decision CLOSE; superseded by this version at the Product Owner's direction)
voided: docs/ephemeral/HDE-EPIC040-CL-E-10-handoff-to-cl20-v1.0.md (issued from v1.0; void and must not be used)
change_id: HDE-EPIC040
change_class: EPIC
producing_prompt: CL-E-10 — Perform Epic Retrospective and Decide Closure — 091426.1
producing_prompt_url: https://app.notion.com/p/3db4590a05eb811a8578d75885c16cac?pvs=204
ecosystem_release: GCFPE-20260914.1
execution_posture: MANUAL_PROMPT_EXECUTION
authoring_context: APPROVED_BASE_WITH_OVERLAYS
decision_owner: Isis, continuing Lead Developer and terminal closure authority for HDE-EPIC040
decision_session: https://claude.ai/code/session_012tPq26JWVhCYZmcqTidpV2 (Product Owner selection recorded in v1.0 §1)
decision_time: 2026-09-29T18:39:19Z
decision: DO_NOT_CLOSE
state: CLOSURE_RETURNED_FOR_CLOSE_MUTATION_SET
return_work: docs/ephemeral/HDE-EPIC040-CLOSE01-closure-evidence-task-prompt-v1.0.md
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.4.9.md (SHA-256 83308abf41c507301b9f821ca1dc581e9c5a7670a2fe2df038b325535dce6a4e)
repository_head_read: origin/main c48a79a5c825428b28fd6b8fcb202fb461baf46e
pf10_addendum_produced: NONE (CL-E-10 is not a PF10_BUILD_NOTES_ADDENDUM producer)
---

# HDE-EPIC040 — Epic Retrospective and Closure Decision (CL-E-10), v1.1

## 0. Decision

| Field | Value |
| --- | --- |
| Decision | **`DO_NOT_CLOSE`** |
| State | `CLOSURE_RETURNED_FOR_CLOSE_MUTATION_SET` |
| Supersedes | v1.0 (`CLOSE`, `CHANGE_CLOSED`). v1.0 is preserved as issued. Its `CLOSE` and `CHANGE_CLOSED` no longer hold, and its CL-20 handoff is void |
| Why | The Change Process Guide §3.5 close mutation set is required closure evidence for an Epic, not post-closure administration. Three parts of it are missing: (1) the QA evidence of record is not on `main`; (2) the QA evidence has no Index or Mirror registration (QA50-F01); (3) no close pack exists |
| Return work | One close PR, specified in `docs/ephemeral/HDE-EPIC040-CLOSE01-closure-evidence-task-prompt-v1.0.md` (§3) |
| Resume point | CL-E-10 again, in the continuing Isis session, after the Product Owner merges the close PR |

## 1. Why v1.0 is superseded

- **The Product Owner's direction, 2026-09-29, verbatim:** "this is not really 'post closure' work, if a task needs to be done. This means we would need to run a fix for this, and then run CL-E-10."
- **Where canon agrees:**
  - Change Process Guide §3.5.1: epic-level acceptance occurs only after the required slices are adopted, **the Close Gate has been satisfied for the exact final candidate**, and the lifecycle decision is recorded.
  - Change Process Guide §3.5.2.1 to §3.5.2.4: the close mutation set carries:
    - the close pack;
    - an exact-source acceptance section;
    - a binary `SATISFIED` / `NOT SATISFIED` decision;
    - the Index and Mirror trio in the same mutation set as the governed evidence it registers;
    - same-run execution evidence.
- **v1.0's error.** v1.0 relied on Plan Templates §10's rule against requiring a close report "whose only function is to restate that decision". That rule has an exception: an owning source may independently require the artifact for a distinct proof function, and the review must then name the source and the function. Change Process Guide §3.5 is that owning source. Its distinct proof functions are:
  - registering the QA evidence in the Human Evidence Index and the Machine Mirror;
  - binding the manifest's `key_outputs` to the paths of record;
  - placing the QA RCA & Doc Delta summary where Change Process Guide §0.4.1.2 puts it.
- **Glow QA Guide §3.1.3 and `AGENTS.md` ("Permanent documentation and build-checklist drainage are not closure prerequisites")** cover drainage and board administration. They do not cover the close mutation set. v1.0 applied them beyond their scope.
- **Not an objective failure.** The missing evidence is not a failure of an approved objective or of QA, so ESC-30 is not the route. It is also not an "already-authorized correction": no approved plan unit owns the close PR. No flow prompt exists for it, so the return work is a one-time task prompt (alpha feedback: `docs/ephemeral/GCFPE-alpha-feedback-epic-closure-evidence-task-v1.0.md`).

## 2. What stands from v1.0

v1.0 §3 to §7 and §10 to §15 remain valid as evidence and analysis. They are not repeated here:
- evidence versions;
- inputs posture;
- delivered-scope disposition;
- closure trace;
- retrospective;
- Strategy Card assessment;
- carried register;
- open findings;
- addendum inventory;
- PF09 later-drain recommendation.

What changes from v1.0:
- **§8 (blocker determination).** Three rows are reclassified from "No" to **closure prerequisite**:
  - "QA evidence of record not on `main`";
  - "QA50-F01";
  - "Close pack absent".

  Every other row stands. In particular, the QA verdict `PASS`, the two deferrals blocked by environment, RA-09 and canon drainage remain non-blocking.
- **§9 (decision).** Replaced by §0 above.
- **§13 (post-closure administration).**
  - Items A-3 (land the QA evidence) and A-4 (close mutation set) move into the return work (§3).
  - A-1, A-2 and A-5 to A-9 stay post-closure, after a future `CLOSE`.

No finding in v1.0 is withdrawn. The retrospective, the Strategy Card assessment and the register are unchanged.

## 3. Exact return work

One PR work unit, **HDE-EPIC040-CLOSE01**, the close mutation set of Change Process Guide §3.5.
- **Specification:** `docs/ephemeral/HDE-EPIC040-CLOSE01-closure-evidence-task-prompt-v1.0.md`, which holds the complete instructions.
- **Proceed:** the Product Owner's invocation of that prompt is the Proceed for this exact unit.
- **Merge:** the Product Owner alone merges.

| # | Required outcome | Closes |
| --- | --- | --- |
| R-1 | The QA evidence of record (Run B, `787bb97`: 39 files under `audit/qa/hde-epic040/`, plus `audit/docdeltas/hde-epic040_doc_deltas.md` and its path proof) lands on `main` byte-identical to `787bb97`. The Run A branch (`e5b671c`) is not used | "Evidence of record not on `main`" |
| R-2 | An admitted Index and Mirror writer registration for the HDE-EPIC040 QA evidence, then the canonical updater run, so that the QA evidence and the close-pack files are registered in the Human Evidence Index, hash sentinel and Machine Mirror with path proofs | QA50-F01 |
| R-3 | The close pack through the governed generator: `audit/EPIC-040_close_report.md` and `audit/EPIC-040_MANIFEST.json` with path proofs, plus `audit/docdeltas/hde-epic040_drain_targets.md` | Close pack |
| R-4 | Same-run mechanical execution evidence under the epic QA root for every refresh or check that the close report claims | Close-pack truthfulness |
| R-5 | Exact-head CI result on the close PR head, and read-only validators passing locally | Close Gate for the exact final candidate |

**Return condition:**
- The close PR is merged by the Product Owner.
- CL-E-10 is re-invoked with the task's result artifact.
- If the task stops on a blocker, it returns that blocker to the Product Owner as that task's terminal result.

## 4. Nonclaims

- This decision closes nothing and authorizes no repository mutation outside the named task.
- It moves no PF09 status, edits no canon, and makes no board change.
- Merging the pull request that carries this record preserves the record and approves nothing (D21-C).

## Canon relied on

Read on `main` at `c48a79a`:
- PF06-Canon-Change-Process-Guide v2.5.3: §0.4.1.2 (location, as cited in the QA RCA); §0.4.1.3; §3.5.1; §3.5.2.1 to §3.5.2.4.
- PF12-Canon-HDE-Schemas-and-Artifacts v2.9.5: "Close-pack artifacts (deterministic path-of-record; baseline artifacts)".
- PF19-Canon-Glow-QA-Guide v3.0.5: §3.1.2; §3.1.3; "Close-pack truthfulness and same-run execution"; "Close report requirements".
- PF27-Canon-Plan-Templates v2.0.4: §10 scope rule and its owning-source exception.
- PF10-HDE-Build-Notes v13.4.9 (HDE Build Notes): no Close Gate or close-pack rule found.
- `AGENTS.md`: "Operating routes and authority".

In-flight documents: as listed in v1.0 §3, plus `docs/ephemeral/HDE-EPIC040-QA50-qa-audit-v1.0.md` (QA50-F01, L-44).

## Provenance

GCFPE_PROMPT_USES:
- Usage ID: HDE-EPIC040-CL-E-10-USE-02.
- Change: HDE-EPIC040 (EPIC).
- Specification: v1.1.
- Scope: HDE-SEPA005 and .1 to .5.
- Ecosystem release: GCFPE-20260914.1.
- Prompt: CL-E-10 — 091426.1, https://app.notion.com/p/3db4590a05eb811a8578d75885c16cac?pvs=204.
- Role and stage: Isis, CL-E-10.
- Capture time: 2026-09-29T18:39:19Z.
- Execution identity: https://claude.ai/code/session_012tPq26JWVhCYZmcqTidpV2.
- Repository persistence: PENDING / NON_GATING (no installed procedure).
- Earlier use: HDE-EPIC040-CL-E-10-USE-01 in v1.0.
