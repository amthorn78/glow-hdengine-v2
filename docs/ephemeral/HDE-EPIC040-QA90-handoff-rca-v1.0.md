---
artifact_type: RCA_BRIEF
artifact_id: HDE-EPIC040-QA90-HANDOFF-RCA
artifact_version: "1.0"
change_class: EPIC
change_id: HDE-EPIC040
subject: QA-70 → QA-90 handoff carried no task selection and no operational rails configuration
author: Isis (Isis-50 session), author of the failed handoff
requested_by: Nathan / Product Owner, 2026-09-27
related: docs/ephemeral/HDE-EPIC040-QA70-qa-plan-review-v1.0.md; docs/ephemeral/HDE-EPIC040-QA50-qa-plan-v1.0.md
---

# RCA: QA-90 task-creation handoff

## 1. What failed

The QA-70 handoff to QA-90 named the approved Plan but gave you no place to state which checks to turn into tasks, and no operational rails configuration. Getting to something usable took four follow-ups:

| # | You asked | What was missing |
|---|---|---|
| 1 | Which tasks does the handoff specify? | None. Task selection is yours, but the handoff had no slot for it, and my QA-70 reply ended "NOTHING NEEDED" instead of asking you |
| 2 | Rails disposition is the main determiner | The Plan groups checks by acceptance goal. Rails appear only as environment classes (ENV-C/S/V/D) in a separate table |
| 3 | Why must I unset all the variables? | The Plan says "Must be UNSET" without saying this is per command. It reads as a Codespaces config change |
| 4 | The list was out of sequence | I grouped by rails batch and moved check 15 ahead of checks 11–14, breaking the execution order |

## 2. Root causes

| # | Cause | Type | Owner |
|---|---|---|---|
| RC-1 | The QA handoff contract forbids placeholders and says a handoff must not restate artifact contents. QA-90's one Product Owner input, the task selection, therefore has no field in any handoff that reaches it | Prompt contract gap (QA-70 and the shared handoff rule) | GCFPE-MGMT-10 maintenance owner |
| RC-2 | I treated task selection as something QA-90 would ask for later, rather than a decision to put to you at QA-70 | Reporting error (glow-po-reporting: a pending decision must end DECISION NEEDED) | Isis (me) |
| RC-3 | The Plan has no single operational table giving, per check in execution order, the rails, set and unset variables, and the command form. The data exists in §5.2 and §11, but no table assembles it | Plan presentation gap; the content is correct | Kronos (QA Plan author); informational, no redline |
| RC-4 | "Must be UNSET" is not stated as per-command (`env -u`). Plan §12 already allows that as syntax normalization, but neither the Plan nor my review said so | Wording gap | Kronos / Isis |
| RC-5 | I re-sorted the list by batch instead of keeping Plan order | Execution error | Isis (me) |

The Plan's content was right. The failure was in how it reached you: no input slot, no operational view, and the wrong closing state.

## 3. Corrective actions

| Action | Where | Status |
|---|---|---|
| Handoff with an explicit task-selection slot and the operational table | §4 and §5 below | Done |
| Per-command `env -u` stated as the unset method; no Codespaces change | §5 and the handoff | Done |
| Report RC-1 to GCFPE-MGMT-10: a handoff into QA-90 must carry a Product Owner task-selection field (or ALL), and the sending stage must ask for it | Prompt maintenance | **Pending your go-ahead**; I don't edit prompts |
| Future QA-70 approvals end DECISION NEEDED with the selection question and this table | My practice | Adopted |

## 4. Handoff for QA-90 (fill in the selection)

```text
NEXT_PROMPT_HANDOFF

Run QA-90 — Create Bounded QA Execution Task — 091426.1
https://app.notion.com/p/3db4590a05eb811e8582cf30238c5b9c

Receiver: Kronos, the continuing QA author for HDE-EPIC040, in the existing Kronos session (session_disposition: RETAIN_EXISTING).
Change: EPIC / HDE-EPIC040 / Separation Pass 3. Execution posture: MANUAL_PROMPT_EXECUTION.

TASK SELECTION (Product Owner) — check numbers from the table in docs/ephemeral/HDE-EPIC040-QA90-handoff-rca-v1.0.md §5, or ALL:
>>> ____________________________________________ <<<

Inputs:
- docs/ephemeral/HDE-EPIC040-QA50-qa-plan-v1.0.md — QA_PLAN v1.0, approved by the review below
- docs/ephemeral/HDE-EPIC040-QA70-qa-plan-review-v1.0.md — QA_PLAN_REVIEW v1.0, APPROVE; QA-90 constraints in §6
- docs/ephemeral/HDE-EPIC040-QA90-handoff-rca-v1.0.md — §5 operational rails table: use it for each task's environment
- docs/ephemeral/HDE-EPIC040-QA50-qa-audit-v1.0.md — QA_AUDIT v1.0
- docs/ephemeral/HDE-EPIC040-QA20-live-qa-guide-v1.0.md — LIVE_QA_GUIDE v1.0
- docs/ephemeral/HDE-EPIC040-QA10-po-disposition-v1.0.md — Product Owner disposition (Q-1, Q-2)
- docs/pfcanon/PF10-HDE-Build-Notes-v13.3.9.md — current PF10

Environment handling: apply each check's unset variables per command with `env -u`, never by changing the Codespaces configuration or secrets (syntax normalization under Plan §12).
```

## 5. Checks in execution order, with operational rails

Prefixes (put the prefix in front of each command; `env -u` removes a variable for that command only):

- **C (closed):** `env -u DATABASE_URL -u HD_API_KEY -u GEO_API_KEY -u HD_API_BASE_URL -u HDAPI_BASE_URL -u DB_BRIDGE_URL -u DB_FORCE_BRIDGE -u DB_ALLOW_BRIDGE_IN_PROD -u ENGINE_ENV LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev`
- **S (closed, production-posture server):** the C prefix with `APP_ENV=prod PORT=8000` on the server command; client commands use C
- **V (open, vendor):** `env -u HDAPI_BASE_URL -u DATABASE_URL -u DB_BRIDGE_URL -u DB_FORCE_BRIDGE -u DB_ALLOW_BRIDGE_IN_PROD -u ENGINE_ENV LC_ALL=C LANG=C TZ=UTC SAFE_MODE=0 ALLOW_NETWORK=1 APP_ENV=dev` — requires `HD_API_BASE_URL`, `HD_API_KEY`, `GEO_API_KEY` already in the environment
- **D (closed, live database):** `env -u HD_API_KEY -u GEO_API_KEY -u HD_API_BASE_URL -u HDAPI_BASE_URL -u DB_BRIDGE_URL -u DB_FORCE_BRIDGE -u DB_ALLOW_BRIDGE_IN_PROD -u ENGINE_ENV LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev` — requires `DATABASE_URL` in the environment; the server command uses `APP_ENV=prod PORT=8000`

| # | Check ID | Rails | Prefix | Live contact | Depends on | Run by |
|---|---|---|---|---|---|---|
| 1 | `d0-discovery` | Closed | C | None | — | Delegable |
| 2 | `step-0b-doc-delta-capture` | Closed | C | None | 1 | Delegable |
| 3 | `ac040-08-evidence-validators` | Closed | C | None | 1 | Delegable |
| 4 | `ac040-02-03-catalog-config` | Closed | C | None | 1 | Delegable |
| 5 | `ac040-04-05-admission-identity` | Closed | C | None | 1 | Delegable |
| 6 | `ac040-06-golden-comparison` | Closed | C | None | 1 | Delegable |
| 7 | `ac040-07-gate-ingress-offline` | Closed (command 1 only: `SAFE_MODE=0`, still no network or DSN) | C | None | 1 | Delegable |
| 8 | `ac040-04-09-compat-cli-offline` | Closed | C | None | 1 | Delegable |
| 9 | `ac040-09-reader-http-in-process` | Closed | C | None | 1 | Delegable |
| 10 | `sec-reader-http-live` | Closed | S | Local server only (127.0.0.1:8000) | 1, 9 | Delegable |
| 11 | `open-rails-showcompat-vendor` | **Open** | V | HumanDesignAPI | 1, 8 | You only |
| 12 | `live-db-gate-readiness` | Closed + live DB | D | Shared Postgres, read-only | 1, 7 | You only |
| 13 | `live-db-reader-refusal` | Closed + live DB | D (server `APP_ENV=prod`) | Shared Postgres, read-only; local server | 1, 10 | You only |
| 14 | `live-db-reader-success` | Closed + live DB | D (server `APP_ENV=prod`) | Shared Postgres, read-only; local server | 12 (READY, ≥ 2 IDs), 13 | You only |
| 15 | `qa-closeout-deliverables` | Closed | C | None | All selected checks recorded | Delegable |

Rules for any selection:
- Check 1 is always required.
- Check 15 always runs last.
- A selected check whose dependency is not selected, or not PASS, is recorded `TOOLING_BLOCKED` without running.
- Check 11 also needs your confirmation that the birth tuples are synthetic (QA-70 review §5).
- Checks 12 and 14 need your list of existing user IDs.
