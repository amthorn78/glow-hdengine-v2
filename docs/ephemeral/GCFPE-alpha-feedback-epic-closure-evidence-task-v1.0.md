---
artifact_type: ALPHA_FEEDBACK_BRIEF
artifact_version: "1.0"
subject: The GCFPE flow has no prompt path for evidence-based closure work that must precede the Epic closure decision (the Change Process Guide close mutation set)
requested_by: Nathan / Product Owner, 2026-09-29 ("What we are missing is a closure task prompt, for when there are closure actions to be done that are evidence based. record that as alpha feedback")
author: Isis, CL-E-10 for HDE-EPIC040, Claude Code session https://claude.ai/code/session_012tPq26JWVhCYZmcqTidpV2
route: GCFPE-MGMT-10 (prompt maintenance). Prompt bodies are in Notion and are not edited here. This session executes the flow, so it writes no Notion page (docs/prompt_ecosystem_management/notion-write-boundary.md)
prompts: CL-E-10, CL-20, CL-E-20 and CL-40 of release GCFPE-20260914.1 (091426.1); QA-120 of the same release. CL-E-10 and CL-20 Notion pages were read in full on 2026-09-29; CL-E-20, CL-40 and QA-120 were not re-read for this brief
related: docs/ephemeral/HDE-EPIC040-CL-E-10-closure-decision-v1.0.md (superseded); docs/ephemeral/HDE-EPIC040-CL-E-10-closure-decision-v1.1.md; docs/ephemeral/HDE-EPIC040-CLOSE01-closure-evidence-task-prompt-v1.0.md
---

# Alpha feedback: no prompt path for evidence-based closure work before the Epic closure decision

## 1. What happened

1. **QA-120 v1.0 for HDE-EPIC040 returned `PASS`.** It recorded three evidence-based closure items as "not QA blockers":
   - the QA evidence of record exists only on its branch at `787bb97`, not on `main`;
   - the QA evidence has no Index or Mirror registration (QA50-F01);
   - no close pack exists (`audit/EPIC-040_close_report.md`, `audit/EPIC-040_MANIFEST.json`).
2. **CL-E-10 v1.0 decided `CLOSE`.** It classified those three items as post-closure administration and routed them to CL-20, CL-E-20 and CL-40.
3. **The Product Owner rejected that classification on 2026-09-29.** In the Product Owner's words:
   - "this is not really 'post closure' work, if a task needs to be done. This means we would need to run a fix for this, and then run CL-E-10."
   - "It doesn't seem like we have a prompt path for this, which would be the obvious next step. It needs an ops task, or a dev PR?"
4. **CL-E-10 v1.1 therefore supersedes v1.0 with `DO_NOT_CLOSE`.** Its return work is a one-time closure evidence task. That task is written as a repository prompt, because no flow prompt exists for it.

## 2. What canon requires, and where the flow is silent

| Source | Requirement | Flow coverage |
| --- | --- | --- |
| Change Process Guide §3.5.1 | Epic-level acceptance occurs only after (a) every required mutation slice is adopted, (b) the Close Gate is satisfied for the exact final candidate, and (c) the lifecycle decision is recorded. "Only the close mutation set is required to carry the full close pack" | CL-E-10 records (c). No prompt produces (b) |
| Change Process Guide §3.5.2.1 to §3.5.2.4 | The close PR carries the close pack, an exact-source acceptance section, a binary `SATISFIED` / `NOT SATISFIED` decision, the Index and Mirror trio in the same mutation set, and same-run execution evidence | No prompt owns the close PR. QA-120 writes only under `docs/ephemeral/`. CL-E-10 and CL-20 write only under `docs/ephemeral/` and may not mutate evidence |
| Change Process Guide §0.4.1.3 | The Close Gate must confirm that the D0 artifact and the QA RCA & Doc Delta summary exist. The summary's governed placement is the close report or `audit/EPIC-###_QA_RCA.md` | No prompt places the summary. QA-120 stores its RCA in `docs/ephemeral/` (HDE Build Notes 2.29) |
| HDE Schemas & Artifacts, close-pack artifacts | Close report and manifest with path proofs; `audit/docdeltas/<epic-id>_doc_deltas.md` and `_drain_targets.md`; the QA step logs manifest | No prompt produces them |
| Glow QA Guide, close-pack truthfulness | A claimed Index, Mirror or path-proof refresh needs same-run mechanical evidence under the epic QA root | No prompt runs or records it |
| Plan Templates §10 | A closure review must not require a pre-existing close report whose only function is to restate the decision, except when an owning source requires it for a distinct proof function, which the review must name | CL-E-10 does not say that the Change Process Guide §3.5 close mutation set is such an owning source, with distinct proof functions (Index and Mirror trio, manifest binding). This made v1.0's misclassification easy |
| Glow QA Guide §3.1.3 and `AGENTS.md` "Operating routes and authority" | Permanent drainage and board administration follow closure | Correctly covered by CL-20, CL-E-20 and CL-40. But these rules cover drainage only, not the close mutation set, and CL-E-10 v1.0 read them as if they covered it |

## 3. Why the prompts allowed it

| ID | Prompt | Cause |
| --- | --- | --- |
| C-1 | CL-E-10 | Step 5 lists post-closure work (memo, board, conditional ADR, PF09 maintenance, CL-40) but never names the close mutation set. Nothing says whether it precedes or follows the decision. "Cosmetic preferences or optional post-closure maintenance do not invent a new closure prerequisite" is easily read as covering governed close evidence |
| C-2 | CL-E-10 | `DO_NOT_CLOSE` routes only to "the existing owner for already-authorized correction" or ESC-30. ESC-30 is for failures of approved objectives. Missing close evidence is neither a QA failure nor an objective failure, and it has no existing authorized owner, so the decision has no lawful next prompt |
| C-3 | QA-120 | The Report may recommend `CLOSE` while listing evidence landing, Index and Mirror registration and the close pack as owner follow-ups. It does not classify them as Close Gate prerequisites |
| C-4 | Flow graph | No Ops or PR prompt consumes a closure finding. The IA and PR prompts start from an approved Implementation Plan and a PR-10 instruction, and no approved plan unit exists for the close PR. The Ops prompts execute environment actions, while the close PR is a repository mutation set. The Change Process Guide §3.5.2.1 OPS-02 provenance run is optional and bounded, and it does not produce the close pack |
| C-5 | IA-10 / IA-30 (inference, not verified in their bodies) | Implementation Plan v2.1 for HDE-EPIC040 has no close-pack unit. Either the planning prompts do not require one, or it was omitted. Not checked here |

## 4. Request

1. **Add a closure-evidence task path.** For example, a CL-E-05 "Prepare and Execute Epic Close Mutation Set" as a PR work unit, entered from QA-120 `PASS` and returning to CL-E-10. It lands the QA evidence of record and adds any missing evidence-writer registration. It runs the canonical Index and Mirror updater and generates the close pack with its ledgers and path proofs through the governed generator. It records same-run execution evidence and opens the close PR for Product Owner merge. A CRD variant follows HDE Schemas & Artifacts' change-container compatibility.
2. **CL-E-10.** State that Close Gate completion (Change Process Guide §3.5) is evidence that precedes the terminal decision for an Epic. It is not post-closure work, and it is distinct from drainage and board administration. Name the new path as the `DO_NOT_CLOSE` route for missing close evidence.
3. **QA-120.** Classify the landing of the evidence of record, the evidence-writer registration and the close pack as Close Gate prerequisites. The QA verdict may stay `PASS`.
4. **IA-10 / IA-30.** Decide whether an Epic Implementation Plan must carry the close mutation set as a planned unit, so that its Proceed exists before QA.

## 5. Interim handling for HDE-EPIC040

- CL-E-10 v1.1 decides `DO_NOT_CLOSE` and names the one-time task prompt `docs/ephemeral/HDE-EPIC040-CLOSE01-closure-evidence-task-prompt-v1.0.md` as the return work.
- The Product Owner's invocation of that prompt is the Proceed for that exact PR work unit.
- After the Product Owner merges the close PR, CL-E-10 runs again in the continuing Isis session.
- The one-time prompt is a development-flow prompt stored in `docs/ephemeral/`. It is not a release member and grants no standing route.

## 6. Acceptance for the prompt change

- An Epic that reaches QA-120 `PASS` has exactly one lawful next prompt for missing close evidence, and that prompt returns to CL-E-10.
- CL-E-10 cannot classify the close mutation set as post-closure administration.
- Drainage, board administration and PF09 maintenance remain post-closure and non-gating.

## 7. Decision needed

Whether GCFPE-MGMT-10 adds the closure-evidence path (request 1) and the clarifications (requests 2 to 4) to the next release. That is the Product Owner's selection through GCFPE-MGMT-10; nothing here changes a prompt.

## Canon relied on

Read on `main` at `c48a79a`:
- PF06-Canon-Change-Process-Guide v2.5.3: §0.4.1.3; §3.5.1; §3.5.2.1 to §3.5.2.4.
- PF12-Canon-HDE-Schemas-and-Artifacts v2.9.5: "Close-pack artifacts (deterministic path-of-record; baseline artifacts)", including change-container compatibility and "Acceptance-binding family coherence".
- PF19-Canon-Glow-QA-Guide v3.0.5: §3.1.2; §3.1.3; "Close-pack truthfulness and same-run execution"; "Close report requirements".
- PF27-Canon-Plan-Templates v2.0.4: §10 scope rule.
- PF10-HDE-Build-Notes v13.4.9 (HDE Build Notes): no rule on the Close Gate or the close pack was found; 2.29 for the storage of change-process records.
- `AGENTS.md`: "Operating routes and authority".
