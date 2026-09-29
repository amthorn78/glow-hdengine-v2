---
artifact_type: LEAD_DEVELOPER_DECISION_RECORD
artifact_version: "1.0"
logical_id: HDE-EPIC040-LEAD-DEV-CLOSE-GATE-DECISIONS
change_id: HDE-EPIC040
change_class: EPIC
decision_owner: Isis, continuing Lead Developer and terminal closure authority for HDE-EPIC040 (https://claude.ai/code/session_012tPq26JWVhCYZmcqTidpV2)
decision_time: 2026-09-29T19:01:59Z
product_owner_direction:
  - '"I need you to make the decisions. you are lead dev" (2026-09-29)'
  - '"We cannot run QA again though, that is too big of an ask. If this calls for a future QA improvement, we can log it as a canon change needed" (2026-09-29)'
inputs:
  - docs/ephemeral/HDE-EPIC040-CL-E-10-closure-decision-v1.1.md (DO_NOT_CLOSE; return work R-1 to R-5)
  - docs/ephemeral/HDE-EPIC040-CLOSE01-closure-evidence-task-prompt-v1.0.md (one-time task prompt; stopped)
  - docs/ephemeral/HDE-EPIC040-CLOSE01-closure-evidence-result-v1.0.md (stop record, blockers B-1 and B-2; amthorn78/glow-hdengine-v2#557, not merged at this decision)
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.4.9.md
repository_head_read: origin/main d817abe1
---

# HDE-EPIC040 — Lead Developer decisions on the Close Gate (after CLOSE01 stopped)

Product Owner guidance applied to every decision below: "it is generally too easy for this whole app to become an evidence engine. that is not its point. evidence is only there to support development." Each decision takes the smallest step that serves development. No new evidence family, QA check or close-pack machinery is created for HDE-EPIC040.

## 0. Decisions

| # | Question | Decision |
| --- | --- | --- |
| D-3 | Land the QA evidence of record and register it (QA50-F01) | **Yes, now.** One PR work unit, HDE-EPIC040-QAEV01 (`docs/ephemeral/HDE-EPIC040-QAEV01-evidence-landing-task-prompt-v1.0.md`). It executes no QA check |
| D-1 | How HDE-EPIC040 reaches closure when no governed writer can produce a canon-conforming close report | **Exceptional closure** under Change Process Guide §3.5.1, recorded by CL-E-10 v1.2 after QAEV01 merges. It **requires one explicit Product Owner authorization** (§2). The close-report writer gap goes to a CRD candidate and a canon change (§4) |
| D-2 | Where the close workflow's same-run evidence lives | **No action for HDE-EPIC040.** No close pack will be claimed, so no close-workflow evidence is needed. Adding a check to the approved QA manifest would amount to QA work, which the Product Owner has ruled out. It is logged as a canon change needed (§4, CC-2) |

## 1. Correction to my CLOSE01 prompt

- **The defect.** CLOSE01 v1.0 directed the close report through `tools/qa/generate_epic_close_pack.py` without my having checked that tool's schema.
- **What the schema allows** (`schemas/epic_close_candidate_source.v1.json`, verified at this decision):
  - four fixed H2 headings (`Candidate boundaries`, `Delivered scope`, `Evidence posture`, `Validation posture`);
  - ten fixed body sentences about publication mechanics;
  - all five fixed nonclaims, including `no_qa_acceptance_or_token_satisfaction`.
- **What it therefore cannot express:**
  - the Change Process Guide §3.5.2.1 acceptance section and its `SATISFIED` / `NOT SATISFIED`;
  - the HDE Schemas & Artifacts deferrals and later-drain statements;
  - the QA RCA summary;
  - Glow QA Guide's verbatim `QA Rails — Open/Close (Final PR)` heading.
- **Outcome.** CLOSE01 correctly stopped (B-1). CLOSE01 v1.0 is closed as stopped and will not be reissued. Its R-1 and R-2 move to QAEV01, and R-3 to R-5 are not pursued (§2).

## 2. D-1: exceptional closure

**Why not the ordinary Close Gate.** The ordinary route needs:
- a governed writer able to produce the canon close report, which does not exist (B-1);
- same-run close-workflow evidence under the epic QA root, which would need an added QA check (B-2).

Building the writer is a cross-epic tooling change outside HDE-EPIC040's Specification: HDE Schemas & Artifacts says such generators are "updated through the authorized change lane", so it is a CRD. The added check is QA work that the Product Owner has ruled out. Holding HDE-EPIC040 open for both would keep a delivered, QA-`PASS` epic open indefinitely for a tooling gap that is not its own.

**Why exceptional closure fits.** Change Process Guide §3.5.1 provides it for this case: "Failure or withdrawal of an ordinary Close Gate lifecycle … Only an explicit Product Owner decision may authorize closure of one identified epic outside ordinary Close Gate completion." The stopped CLOSE01 lineage (#557) is that stopped lifecycle.

**The authority limit.** Canon reserves this one authorization to the Product Owner. Your delegation of decisions to me does not substitute for it, so I am not claiming it.

> **I need from the Product Owner:** "I authorize exceptional closure of HDE-EPIC040 outside ordinary Close Gate completion."

Everything else is decided here.

**What CL-E-10 v1.2 will record, per Change Process Guide §3.5.1 "Exceptional closure record":**
- the epic, the Product Owner authority, the exception scope and the accepted delivered outcome;
- the stopped CLOSE01 lineage and #557's merge posture, and QAEV01's landing (commit on `main`);
- every ordinary Close Gate element not achieved: the close report, close manifest, close-pack completion, `SATISFIED` posture, merged close PR and QA RCA governed placement. No acceptance map or token matrix exists;
- the QA, implementation, OPS and repository facts, each in its own proof class;
- that PF09 movement, board movement, PF-Canon drainage and phase exit have not occurred;
- the routed debt (§4);
- that the exception is specific to HDE-EPIC040, does not establish ordinary Close Gate completion and is no default for other epics.

## 3. D-3: QAEV01

**Why a PR, and within what boundary.**
- The route is Change Process Guide §3.5.2.8: Live QA evidence may land "in an evidence-only QA PR … that merges before the close PR". The Index and Mirror trio lands in the same mutation set.
- Change Process Guide §0.7 limits evidence-only QA branches to governed artifacts. It forbids app or service code, migrations, runtime configuration, vendor rails and endpoint behavior.
- The trio can only be written by the canonical updater, which admits an epic's QA evidence through a per-epic registration list in `tools/evidence/update_evidence_index.py`. The `EPIC029_PRIMARY_ARTIFACTS` pattern and its tests in `tests/ops/test_evidence_index.py` show this.

**Decision.** QAEV01 may add that registration entry and its test as evidence tooling. This is not app, service, runtime or endpoint code, and without it §3.5.2.8's same-mutation-set trio cannot exist. §0.7's allowed-artifact list predates QA-root landing, which §3.5.2.8 itself adds. This interpretation is logged as CC-3 for the maintainer.

**Scope.**
- Land the 41 files from `787bb97` byte-identical.
- Add the registration and its test.
- Run the canonical updater.
- Run the read-only validators.
- Nothing else: no QA check execution, no close pack, no change to any QA-root byte.

## 4. Logged for later owners (not HDE-EPIC040 closure prerequisites)

| ID | Item | Type | Owner and route |
| --- | --- | --- | --- |
| CC-1 | No governed writer can produce a canon-conforming epic close report. The generic generator is neutral by design (B-1) | Canon change needed: Change Process Guide §3.5.2 and HDE Schemas & Artifacts close-pack rules state no writer, while HDE Build Notes and `AGENTS.md` name only the neutral generic generator. Also a CRD candidate: extend the generic writer or add a governed close-report writer | Change Process Guide and HDE Schemas & Artifacts maintainers (canon). Dev side **registered as Candidate CRD Items List item 8** (https://app.notion.com/p/3e54590a05eb813c8d89d065026f694d), at the Product Owner's direction of 2026-09-29 |
| CC-2 | Glow QA Guide "Close-pack truthfulness and same-run execution" requires close-workflow evidence under the epic QA root. Every admitted home is a check in the approved QA manifest, which cannot change after the QA verdict without QA work (B-2) | Canon change needed: define a post-verdict close-workflow evidence home, or let the close mutation set carry that evidence outside the QA manifest | Glow QA Guide and HDE Schemas & Artifacts maintainers. The tooling side is included in CRD candidate item 8 |
| CC-3 | Change Process Guide §0.7's allowed-change list omits QA-root artifacts and evidence-writer registration, both of which §3.5.2.8 landing needs | Canon change needed (CONSISTENCY) | Change Process Guide maintainer |
| CC-4 | Plan the close mutation set in the Epic Implementation Plan so that its writer and evidence home are proven before QA | Process change; already requested in `docs/ephemeral/GCFPE-alpha-feedback-epic-closure-evidence-task-v1.0.md` request 4 | GCFPE-MGMT-10 |

These join the carried register as documentation or tooling debt. They are not entered as HDE-EPIC040 conflicts, because no HDE-EPIC040 deliverable depends on resolving them once exceptional closure is authorized.

## 5. Sequence

1. The Product Owner authorizes exceptional closure (§2). This can happen at any point before step 4.
2. The Product Owner starts QAEV01 with its prompt. That is the Proceed for that unit.
3. The Product Owner merges the QAEV01 PR.
4. CL-E-10 v1.2 in this Isis session: `CLOSE` with the exceptional closure record. Then CL-20.

## Canon relied on

Read on `main`:
- PF06-Canon-Change-Process-Guide v2.5.3: §0.7; §3.5.1 (including "Exceptional closure record."); §3.5.2.1 to §3.5.2.4; §3.5.2.8; §4.5.
- PF12-Canon-HDE-Schemas-and-Artifacts v2.9.5: "Close-pack artifacts (deterministic path-of-record; baseline artifacts)".
- PF19-Canon-Glow-QA-Guide v3.0.5: "Close-pack truthfulness and same-run execution"; "Close report requirements".
- PF10-HDE-Build-Notes v13.4.9 (HDE Build Notes): no Close Gate, close-pack or exceptional-closure rule found.
- `AGENTS.md`: "HDE-EPIC039 current workflow posture"; "Governed evidence rules".

Repository reads: `schemas/epic_close_candidate_source.v1.json`; `tools/evidence/update_evidence_index.py` (per-epic registration lists).
