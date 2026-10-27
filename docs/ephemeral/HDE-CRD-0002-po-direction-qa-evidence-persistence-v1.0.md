---
artifact_type: PRODUCT_OWNER_DIRECTION
artifact_id: HDE-CRD-0002-PO-DIRECTION-QA-EVIDENCE-PERSISTENCE
artifact_version: "1.0"
predecessor: none
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
subject: where QA evidence is kept; the evidence-only commit default
decision_owner: Nathan / Product Owner
decided_at: 2026-10-25 (UTC), in the HDE-CRD-0002 QA-100 execution session below (recorded 2026-10-25T00:42:00Z)
recorded_by: the HDE-CRD-0002 QA-100 executor, Claude Code CLI agent (Claude Opus 5.5), local session abab87ae-fdb9-4eb6-b2b9-de5380cee6cb (id taken from the session scratchpad path). Recorder only; the direction is the Product Owner's
state: APPLIED_TO_THIS_RUN; the general rule is OPEN (§5)
repository_head_read: origin/main 2e03a2686af87ab0607c6cfb9afb4ad79bcdb171
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.7.8.md (SHA-256 42459e54e4a14eb89a1cd3be80eae8458a5b1c2c50e1fca1b1ce9882b05e6f9b); searched, silent on an evidence-only commit default
pf10_addendum_created: none (QA-100 is not an addendum producer; this record edits no PF file)
---

# HDE-CRD-0002 — Product Owner direction: QA evidence is persisted in the repository (v1.0)

## 1. Product Owner's words (verbatim)

> "you never asked me where i wanted the evidence.QA  evidence needs to be PERSISTED in the repo, not kept in tmp. this needs to be re-litigated"

## 2. What happened

The QA-100 executor published checks 1 to 12, 14 and 15 through the canonical writer, into a scratch evidence checkout. That checkout is a clone of the repository in the session scratchpad.

It did not commit them. No evidence-only commit grant had been stated, and the task collection's default reads "Without the grant, the Product Owner commits".

The executor applied that default without asking the Product Owner where the evidence should go.

## 3. Direction

| # | Direction |
| :- | :- |
| E-1 | QA evidence is persisted in the repository. It is never left only in temporary or scratch storage |
| E-2 | The default that leaves published evidence uncommitted unless a grant is stated is to be re-litigated |

## 4. Applied to this run

The executor treats E-1 as the evidence-only commit grant that QA Plan v1.2 §2 requested. It uses the grant within that section's bounds:
- one branch, `qa/hde-crd-0002-evidence`, through one pull request;
- only `audit/qa/hde-crd-0002/**`, the ten updater-owned graph files, and its own QA-100 result record under `docs/ephemeral/`;
- no other path, no merge, no force-push.

First evidence commit: `e97c3bba58e4be35ca0251d361d3ee3c0bc39881`, pushed on `qa/hde-crd-0002-evidence`. It holds checks 1 to 12, 14 and 15: 30 added files under `audit/qa/hde-crd-0002/` and the ten graph files. Check 13 follows in a later commit on the same branch.

## 5. The rule as it stands, and where it is re-litigated (OPEN)

Canon searched on `main` at `2e03a268` for "evidence-only commit", "evidence commit" and "direct repository evidence commit".

- **PF canon has no rule that keeps published QA evidence out of the repository.** The Glow QA Guide places evidence under `audit/qa/<id>/checks/<check_id>/` (PF19-Canon-Glow-QA-Guide §3.4.3, §4.4) and treats evidence that is present but not indexed as a QA failure (§3.5.7). Neither section makes committing the evidence depend on a separate grant.
- **The default comes from the in-flight documents and the prompt:**
  - QA Plan v1.2 §2 "Evidence-only commit permission (requested; bounded; effective only when the Product Owner grants it at task execution)", plus §4 and §5.6;
  - QA task collection v1.0 §4.8, §7 and §9;
  - the QA-100 prompt, "QA-100 — Execute Bounded QA Task — 100926.1", Execute step 4: "If a direct repository evidence commit is explicitly authorized, commit only its exact evidence files/path".

| Owner | Where the default lives | Re-litigation route |
| :- | :- | :- |
| Kronos (QA-50, QA-80, QA-90) | QA Plan and task collection evidence-commit wording for later HDE-CRD-0002 QA runs | The Product Owner's direction is in force for this change; the immutable approved Plan v1.2 text is not edited |
| GCFPE-MGMT-10 maintenance owner | The QA-100 prompt's Execute step 4 and the QA-90 prompt's commit-grant wording | Prompt-defect report (§6) |
| Product Owner | PF canon, if the rule is made permanent there | A canon drainage decision; this record does not drain it |

## 6. Prompt-defect report (QA-100 prompt; for the GCFPE-MGMT-10 maintenance owner)

| Field | Value |
| :- | :- |
| Prompt | QA-100 — Execute Bounded QA Task — 100926.1, https://app.notion.com/p/3f44590a05eb8182a201f0e177dad431 (page state 2026-10-12T02:30:45.204Z) |
| Expected | Published QA evidence is persisted in the repository (Product Owner direction E-1). Where the execution arrangement leaves the commit scope unstated, the executor asks the Product Owner before execution rather than leaving the evidence uncommitted |
| Actual | Execute step 4 commits evidence only when a direct repository evidence commit is "explicitly authorized". With the grant unstated, the executor left the published evidence uncommitted in a scratch clone |
| Evidence | This record §2; QA task collection v1.0 §4.8; QA Plan v1.2 §2 |

## Canon relied on

Searched on `main` at `2e03a268`:
- PF19-Canon-Glow-QA-Guide v3.0.6 §3.4.3, §3.5.7 and §4.4, as cited by QA Plan v1.2 §5.1;
- HDE Build Notes v13.7.8 (searched; silent).

Repository rules: `AGENTS.md` "Canon-first rule" and "PF canon is read-only unless the prompt explicitly directs a change".

## Provenance

Recorded during GCFPE-USE-HDE-CRD-0002-QA-100-20261024-01 (QA-100 — Execute Bounded QA Task — 100926.1; release GCFPE-20261009.1). The QA-100 execution results record cites this direction.
