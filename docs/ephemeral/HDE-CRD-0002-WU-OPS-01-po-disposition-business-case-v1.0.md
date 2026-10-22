---
artifact_type: PRODUCT_OWNER_DISPOSITION
artifact_id: HDE-CRD-0002-WU-OPS-01-PO-DISPOSITION-BUSINESS-CASE
artifact_version: "1.0"
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
OPS_UNIT_ID: WU-OPS-01
decision_owner: Nathan / Product Owner
decided_at: 2026-10-22, in the whole-change Implementation Agent session below (recorded 2026-10-22T04:35:00Z)
recorded_by: the whole-change HDE-CRD-0002 Implementation Agent, session "HDE-CRD-0002-2" (https://claude.ai/code/session_01U3QLYTkfUepeRbSGZNPj9N). This IA recorded and drafted the adopted text; the decision is the Product Owner's
decides: the decision returned by docs/ephemeral/HDE-CRD-0002-WU-DOC-01-documentation-completion-v1.1.md §6 and §7 (DOC-20, COMPLETE): WU-OPS-01's business case, due before OPS-10 (PF10 addendum 2.18, "Epic, task, and status effects")
approved_base_affected: none. WU-OPS-01's block is Implementation Plan v1.1 §7 as Plan delta 01 v1.1 P-9, P-18 and P-19 amend it (PF10 addendum 2.19)
repository_head_read: origin/main 5552f8b (#701)
pf10_addendum_created: none
---

# HDE-CRD-0002 WU-OPS-01 — Product Owner disposition: business case (v1.0)

## 1. Product Owner's words (verbatim)

> "adopt the draft business case, give me the OPS-10 handoff"

"The draft business case" is the one in DOC-20 v1.1 §7. It is reproduced in §2 without change.

## 2. Decision: the draft is adopted

### Business case for WU-OPS-01 (addendum 2.11 rule 1, as addendum 2.18 narrows it)

| Field | Content |
| :- | :- |
| Beneficiary | Glow users of the production HD Engine, and the Product Owner, who accepts HDE-CRD-0002 on evidence from the service users actually reach |
| Evidence | HDE-CRD-0002 changed production behaviour that only the deployed service can show. Unknown paths get the governed `ERR_NOT_FOUND` envelope instead of Flask HTML (S02, #643). Dev `GET /reader` is refused unless `APP_ENV` is exactly `dev` (S10, #643 and #646). Production vendor access goes through `--allow-prod-vendor` (S14, #651). The candidate's `release_id` on `main` is `77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e`. The DOC-20 session made no read of the production service, so whether production runs it was not measured |
| Benefit | The QA Plan's live steps (Plan v1.1 §9 item 3: S02 and S10 in the deployed target; S14's live vendor call) exercise the exact accepted candidate, so acceptance rests on what users receive, not on a local or older build |
| Measure | `GET /internal/version` on the production base URL reports `release_id` `77204764…c51e`, or the then-current accepted candidate's, at version `1.3.0`. It is recorded presence-only with path proofs under `audit/ops/hde-crd-0002/wu-ops-01/` (Plan delta 01 P-9). The task changes no production configuration |
| Cost ceiling | None (addendum 2.18 rule 1) |

## 3. Effect

- **WU-OPS-01's prerequisite is met:**
  - its dependency, "After WU-DOC-01", is met: DOC-20 v1.1 is `COMPLETE`;
  - its business case now exists.
- **Next stage:** OPS-10 — Create Bounded Ops Task — 100926.1, run by the whole-change Implementation Agent as task author and future acceptance owner. It creates the Ops task; it does not execute it.
- **After OPS-10:** OPS-20 execution by the Product Owner, the unit's owner and executor (Plan v1.1 §7), or by a delegate he names; then OPS-30 receipt review.
- **Then:** QA-10 becomes possible once WU-OPS-01 is planned (OPS-10) or executed (Plan v1.1 §9 item 1).
- **Not decided here:** the task's text, any execution, QA, acceptance or closure.

## 4. TypeSafe reading for the receiving session (OPS-10, WU-OPS-01)

Action sent (v8.2): "Write, as the whole-change implementation agent, one complete executable operations task record for an approved change's single Ops unit: the operator reads the production service's identity endpoint over HTTPS after the accepted candidate's commit has landed on main, confirms it reports the candidate's release identity, probes the presence of named production bindings without recording any value, and saves the captures with path proofs under a fixed audit directory; if the identity does not appear it re-reads after a delay, records each read, and only redeploys the previous commit when the service does not answer. The plan already fixes the target, success criterion, constraints and rollback; the task states the exact commands, expected outputs, stop conditions, redaction and evidence destinations from the infrastructure canon, with no production configuration change. It is a Markdown record only: the task is not executed here; the Product Owner executes it, and a receipt review follows."

- **TypeSafe v8.2: Opus 5.5 at high.**
  - Effort score 1.94 (confidence 0.10). Rung probabilities: low 0.19, medium 0.29, high 0.16, extra high 0.09, max 0.26, ultracode 0.01.
  - Model probabilities: Fable 5.1 0.02, Opus 5.5 0.58, Sonnet 5.5 0.38, Haiku 5.5 0.02 (confidence 0.44).
  - Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.004, Fable 5.1 at medium 0.006, Fable 5.1 at high 0.003, Fable 5.1 at extra high 0.002, Fable 5.1 at max 0.005, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.110, Opus 5.5 at medium 0.168, Opus 5.5 at high 0.093, Opus 5.5 at extra high 0.052, Opus 5.5 at max 0.151, Opus 5.5 at ultracode 0.006, Sonnet 5.5 at low 0.072, Sonnet 5.5 at medium 0.110, Sonnet 5.5 at high 0.061, Sonnet 5.5 at extra high 0.034, Sonnet 5.5 at max 0.099, Sonnet 5.5 at ultracode 0.004, Haiku 5.5 at low 0.004, Haiku 5.5 at medium 0.006, Haiku 5.5 at high 0.003, Haiku 5.5 at extra high 0.002, Haiku 5.5 at max 0.005, Haiku 5.5 at ultracode 0.000.
  - Flags: boundary between max and medium; model near tie between Opus 5.5 and Sonnet 5.5.
  - Sent 2026-10-22T04:34:24Z. Nathan picks the cell.
- **Detail:** v8.2 sent 2026-10-22T04:34:24Z; HTTP 200 in 0.59 s; 5521 input and 71 output tokens; jev-1.13.0. Rung by rule: high (nearest to the score, halves up). Model by rule: Opus 5.5 (the most probable of the four options, a tie going to the higher-priced model).
- **Which request:** the installed TypeSafe scoring skill's request v8.2 and `score_v8.py`, run once with session kind `planning`, before this record was saved.
- **Records:** the Notion row was not written. Nathan's pick for OPS-10 is not stated.

**Surface advice:** run OPS-10 in the continuing whole-change HDE-CRD-0002 Implementation Agent session on `amthorn78/glow-hdengine-v2` (this one, or a top-level session Nathan creates for that role), with Notion read access for the prompt.
- **Reads:**
  - Plan v1.1 §7 WU-OPS-01 with Plan delta 01 P-9, P-18 and P-19;
  - PF07-Canon-Glow-Infrastructure (the target and bindings);
  - PF27-Canon-Plan-Templates §3 (the Ops Task Record);
  - `engine/runtime/identity.py` and the `/internal/version` handler.
- **Writes:** only the task record under `docs/ephemeral/`.
- **Access:** no production access is needed to author the task. The session does not read or change the production service.
- **Order:** this record's pull request should be merged first.

## Canon relied on

Read on `main` at `5552f8b`; PF10 is v13.7.4.

| Topic | Sources and sections |
| :- | :- |
| Business-case fields; no ceiling; due before OPS-10 | PF10 addendum 2.18, rules 1 to 3 and "Epic, task, and status effects"; addendum 2.11 rules 1 to 4, read in this session |
| The decision returned and its draft | DOC-20 v1.1 §6 and §7 (this session's own) |
| WU-OPS-01 scope | Implementation Plan v1.1 §7 WU-OPS-01; Plan delta 01 v1.1 P-9, P-18 and P-19 (PF10 addendum 2.19), read in this session |
| Next stage | DOC-20 — Verify Final Repository Documentation Completion — 100926.1, "Resolve the next approved Plan stage" (an Ops unit goes to OPS-10); OPS-10 — Create Bounded Ops Task — 100926.1 (https://app.notion.com/p/3f44590a05eb81509957c43992c03625; page state of 2026-10-12T02:29:29.013Z), "Role and task", "Inputs" and "Execute", read in this session |
