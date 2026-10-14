---
artifact_type: CORRECTIVE_ARCHITECTURE_DECISION_RECORD
artifact_id: HDE-CRD-0002-WU-PR-03-CORRECTIVE-ARCHITECTURE-DECISIONS
artifact_version: "1.0"
artifact_state: COMPLETE
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-03
authority: Nathan / Product Owner, direction of 2026-10-14 in the continuing IA session: "I don't think PR03 was well planned, so what I want you to do is create a new PR-20 handoff, including a PF10 addendum with the proper architectural decisions to do this RIGHT."
author: the continuing whole-change Implementation Agent (IA) for HDE-CRD-0002, session https://claude.ai/code/session_01CCKsYD2yX5WgU3biWKb59j (author of the WU-PR-03 instruction v1.0 and of both WU-PR-03 rescope reviews)
decisions: AD-1 to AD-6 (§3); CR-7 and CR-8 APPROVED, alternative (a) each (§6)
addendum_ref: docs/ephemeral/HDE-CRD-0002-WU-PR-03-corrective-PF10-build-notes-addendum-v1.0.md (proposed PF10 addendum 2.7)
handoff_ref: docs/ephemeral/HDE-CRD-0002-WU-PR-03-corrective-architecture-decisions-v1.0-handoff.md (PR-20, corrective plan v2.0)
resolves: docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr35-rescope-review-v1.0.md (SPECIFICATION_CHANGE_REQUIRED on RP-4; RP-5 assessed) — the Product Owner decision it returned for is this direction
vehicle_state: amthorn78/glow-hdengine-v2#643 MERGED 2026-10-14T04:41:15Z as c98d41f (head dc45a35; tree equal); Codex P1 threads PRRT_kwDOP103ks6sJ4Y8 and PRRT_kwDOP103ks6sJ4Y_ open at merge; no open pull request for WU-PR-03; WU-PR-03 merged and not accepted (no PR-40 review)
repository_baseline: origin/main c98d41f3966d824c0fbc5cf2af0a141c1be5e247; docs/pfcanon/PF10-HDE-Build-Notes-v13.5.7.md is the controlled PF10 (addenda 2.1 to 2.6)
immutable_approved_base: Specification v1.1 → Implementation Plan v1.1 + review v1.1 → PR instruction v1.0, overlaid by Build Notes 2.6 and, from this record, 2.7. None is rewritten
capture_time_utc: 2026-10-14T05:10:00Z
---

# HDE-CRD-0002 WU-PR-03 — Corrective architecture decisions v1.0

Canon precedence rule for this derived artifact (Plan Templates, "Canon precedence for template use"): Applicable, active, non-superseded PF10 addenda supersede conflicting PF-Canon only for the exact scope they address; otherwise follow PF-Canon. A formally approved bounded Product Owner rescope may supersede conflicting PF-Canon only for the exact decision it adjudicates.

## 1. What this record does

On the Product Owner's direction, this record:
- re-plans WU-PR-03 as a corrective cycle on top of the merged #643;
- fixes six architecture decisions in advance (AD-1 to AD-6), recorded for PF10 as addendum 2.7;
- decides CR-7 and CR-8;
- hands the work to PR-20 for a corrective plan v2.0.

It authorizes no implementation, merge or Proceed. It edits no canon and no Specification.

**Status of the decisions.** The IA drafted them under the direction. They are approved by that direction and adopted into canon when the Product Owner publishes addendum 2.7. If the Product Owner rejects any decision, the handoff should not be run until this record is revised.

## 2. Why WU-PR-03's first plan needed five rescope items

The instruction this IA issued read canon section by section, not bullet by bullet, and treated the Specification's wording as the design rule. Five corrections followed across two cycles, each one a canon passage the instruction did not apply:

| Item | Canon the instruction missed or overrode | Effect |
| :- | :- | :- |
| RP-1 | HDE Architecture §3.8.1 start-helper bullet; HDE Mechanics Guide §5.6 | the plan required an `APP_ENV` default canon forbids |
| RP-3 | the label roster's own criterion (WU-PR-02 defect) | the evidence lane would have gone red |
| RP-2 | the updater validates the catalog | the convergence order failed |
| RP-4 | HDE Architecture §3.5; HDE Users Guide §1.1 | the catalog published three retired routes; it merged |
| RP-5 | HDE-CLI-API-Vendor-Ref §5.4 and §5.6 "explicit `APP_ENV=dev`" | the instruction chose a normalizing gate; it merged |

The corrective cycle removes the cause as well as the symptoms:
- every surface question is decided here, with its canon basis;
- AD-6 makes the canon trace a deliverable that continuous integration enforces;
- what WU-PR-03 deliberately does not do is named, with an owner (AD-4).

## 3. Decisions

The binding text is in addendum 2.7. This table is the index.

| ID | Decision | In WU-PR-03 | Canon basis |
| :- | :- | :- | :- |
| AD-1 | Every served pair is catalogued once or excluded once with a basis. A new exclusion class (d) covers canon-retired routes. Five records are removed (23 → 18), and a fail-closed retired-path pin is added. S15 is read under canon | yes | HDE Architecture §3.5; HDE Users Guide §1.1; HDE Schemas & Artifacts §8.8 (inventory of "public surfaces and key internal/ops/dev endpoints") |
| AD-2 | Dev `GET`/`HEAD /reader` is served only when `APP_ENV` is exactly `dev` | yes (member change) | HDE-CLI-API-Vendor-Ref §5.4 "Gate", §5.6; HDE Schemas & Artifacts Reader surface routes; HDE Mechanics Guide §34 |
| AD-3 | The canonical dev runner binds `127.0.0.1`, has the debugger and reloader explicitly off, and has a test proving no CORS. The start-helper banner names the host | yes (member change; one script line) | HDE-CLI-API-Vendor-Ref §5.4 "bound only to a local interface"; HDE Mechanics Guide §34 "Required local capture profile" |
| AD-4 | Four gaps go to S19 (WU-PR-05) as named inputs: dev-harness routes mounted in production, retired `/ops` routes ungated in production, the normalizing dev/admin gate, and a dead after-request hook | no | HDE Architecture §3.2, §3.3, §3.5; HDE-CLI-API-Vendor-Ref §5.4; HDE Governance "Dev/admin APP_ENV gating" |
| AD-5 | One same-version re-cut. The catalog owner runs at step 3b, and both passes are byte-stable. The new `release_id` is the base for WU-PR-04 and WU-PR-05 | yes | HDE Governance §9.1.2 order of authority as applied by Plan v1.1 §10 and Build Notes 2.6 |
| AD-6 | Canon trace per decision and per route, in the plan and the result record. The enumeration test records each exclusion's class and basis | yes | AGENTS.md canon-first rule; HDE Governance §9.1.2 |

**Why AD-4 stays outside WU-PR-03.**
- **Specification.** It is the scope authority (HDE Governance §9.1.2), and no requirement in S02 to S18 covers production exposure of the sampler, conjunction or retired routes.
- **Design.** A correct fix is one factory-level split of non-public routes, applied to all of them, including the `POST /reader` refusal stub that shares the dev path. Doing it for `/reader` alone would leave one dev route unmounted and the rest mounted, with a stub whose `Allow` header points at a method production no longer serves.
- **Owner.** S19 is the requirement whose scope reaches exposure. It fixes confirmed findings within HDE-CRD-0002 or routes them with a reason.
- **Proof in the meantime.** The request-time refusal stays the S10 control, and the governed env-gate proof already records it (`/reader_success_unreachable=true` under `APP_ENV=prod`).
- **If the Product Owner wants these fixed in WU-PR-03 instead,** that is a Specification delta, and this record would be revised before PR-20 runs.

## 4. Scope of the corrective plan

| Locus | Change | Decision |
| :- | :- | :- |
| `tools/evidence/generate_a7_transport_proofs.py` | remove five records; add the canon-retired path set and the validator pin | AD-1 |
| `tests/http/test_endpoint_catalog.py` | exclusion class (d) with nine pairs and its basis; retarget the validator case that edited an `/ops/probe/env` record; add the retired-pin case | AD-1, AD-6 |
| `adapter/http_reader.py` (member) | `_reader_dev_env_explicit` exact comparison; `__main__` run call with the loopback host and explicit flags | AD-2, AD-3 |
| `tests/http/test_reader_a7_transport.py` | served `dev` only; extended refusal matrix | AD-2 |
| `scripts/dev_start_reader.sh` | banner host text only | AD-3 |
| a dev-runner profile test (location chosen by the plan inside existing owner registrations, or one ID-3-style registration if unavoidable) | the run-call arguments; no `Access-Control-*` header on `GET /reader`, on a preflight `OPTIONS` with `Origin`, or on an error response | AD-3 |
| `docs/server/reader_v1.md` | "exactly `dev`"; host `127.0.0.1` | AD-2, AD-3 |
| `catalog/manifest.json` and every regenerated family | by the cutter and the owners only | AD-5 |
| `docs/ephemeral/` | plan v2.0 and the result records | — |

**Expected unchanged** (a needed change is a rescope finding):
- `adapter/factory.py`, `adapter/wsgi.py`, `engine/http/compat_handler.py` and `engine/presenter/**`;
- `engine/config/registry_loader.py`, `tools/evidence/update_evidence_index.py` and `tools/evidence/hdapi_v2_boundary_analyzer.py`;
- `tools/evidence/generate_hdapi_v2_contract_inventory.py` (verified: discovered records equal the baseline) and `ci/checks/classify_ci_changes.py` (unless the profile test needs a registration);
- `VERIFY.sh`, `.github/workflows/ci.yml`, frozen families and `artifacts/architecture/**`.

## 5. Corrective route

1. The Product Owner merges the pull request carrying this record, the addendum record and the handoff. The Product Owner publishes addendum 2.7 into PF10 when convenient; the corrective plan cites the record path until then.
2. **PR-20 — Create Detailed PR Implementation Plan — 100926.1:**
   - the dedicated WU-PR-03 PR engineering session writes corrective plan v2.0 from `main`;
   - it carries the plan v1.1 work that landed in #643 as already delivered, and plans only the delta;
   - it presents the plan at `AWAITING_PO_PROCEED`.
3. **Delivery.** The Product Owner's Proceed for plan v2.0, then PR-30, PR-35, and the Product Owner's merge.
4. **PR-40 — Review PR Work-Unit Lineage — 100926.1** by this IA, across #643 then the corrective pull request. It decides acceptance of WU-PR-03.

The precedent is WU-PR-02, where a merged unit was corrected by a second plan and pull request and accepted across both. By this direction, no separate PR-40 review of #643 alone runs first: its findings are already decided here.

**Records that stay as they are.** The PR-35 result v1.1 (`RESCOPE_PENDING`) and the PR-35 rescope request are historical records of #643. The open Codex threads on #643 stay as merged evidence. The corrective pull request's description names them as resolved by AD-1 and AD-2.

## 6. Canon-conflict register

**Carried unchanged:**
- CR-1, CR-2, CR-3: `APPROVED_AS_CHANGED` (Thoth);
- CR-4: `APPROVED`, and CR-5: `APPROVED_AS_CHANGED` (Product Owner);
- CR-6: `APPROVED` (the IA, rescope review v1.0 §12).

| Field | CR-7 | CR-8 |
| :- | :- | :- |
| Classification | CANON_RECONCILIATION (Specification S15 and Plan IF-6/EC-8 versus HDE Architecture §3.5) | CANON_RECONCILIATION (instruction §9.2 versus the explicit `APP_ENV=dev` passages) |
| Decision | **`APPROVED`**, alternative (a): exclusion under canon (AD-1) | **`APPROVED`**, alternative (a): exact comparison (AD-2) |
| Decided by | the Product Owner's direction of 2026-10-14, decisions drafted by the IA in this record | same |
| Reviewed artifacts | PR-35 rescope request v1.0 §7; PR-35 rescope review v1.0 §4 and §7 | same, §5 and §7 |
| Interim | the five records and the normalizing gate stay on `main` until the corrective pull request merges | same |
| Drainage | HDE Schemas & Artifacts §8.8 population rule; HDE-CLI-API-Vendor-Ref §5.6 implementation state (Product Owner) | none |
| History | PROPOSED 2026-10-14T04:00Z (request); reviewed and escalated 05:05Z (PR-35 rescope review); APPROVED 05:10Z (this record) | PROPOSED 04:00Z; reviewed 05:05Z; APPROVED 05:10Z |

## 7. Obligations this IA carries

- **WU-PR-05 instruction (PR-10):** the AD-4 gaps as named S19 inputs, each with canon basis and current evidence. The four gaps:
  - production mount of dev-harness routes and the `POST /reader` stub;
  - the retired `/ops` routes ungated in production, including `/ops/probe/env`'s process data (OBS-P3-4);
  - `_dev_admin_gate` normalization (OBS-RS2-1);
  - the dead after-request hook (OBS-P3-1).

  OBS-P3-3 (`adapter/wsgi.py`'s 405 has no `Allow`) goes with them as an S02-adjacent note.
- **WU-PR-08 instruction:** S17's port and bind statements describe the loopback bind.
- **WU-PR-04, WU-PR-05 and WU-PR-08 instructions:**
  - the refresh base is the corrective `release_id`;
  - the 22-path roster stays;
  - step 3b applies when a unit changes the catalog validator.
- **WU-DOC-01:** `AGENTS.md` and `README.md` state the start command with `APP_ENV=dev` and the loopback bind.
- **Instruction practice from here on:** each instruction names the canon bullets it relies on and maps each touched route to its canon posture before it binds a disposition rule.

## 8. TypeSafe reading and surface advice for the receiving session (PR-20, WU-PR-03 corrective plan v2.0)

Action sent (v6): "Write, as a dedicated PR engineering session, a new corrective detailed PR implementation plan, not yet reviewed, for a work unit whose first pull request already merged: apply a Product Owner-directed architecture addendum across about ten hand-edited files (remove five endpoint-catalog rows for three canon-retired routes and add a fail-closed validator pin and a fourth exclusion class to the route-enumeration test; make a dev route's environment gate an exact comparison; harden the dev runner with a loopback bind, explicit debugger and reloader off, a no-CORS test and one start-script banner line; update two documents), then plan a same-version release re-cut with governed-evidence convergence through about thirty owner tools and a full test sweep. A task list exists (the addendum's numbered decisions), the prior plan and a scratch prototype of two of the changes exist, and every changed clause must be carried exactly. No code is merged and no live provider call occurs; a Product Owner Proceed, implementation, and independent code and lineage reviews follow."

- **TypeSafe v6: Opus 5.5, high.** Effort score 2.43 (confidence 0.66).
  - Rung probabilities: low 0.00, medium 0.03, high 0.54, extra high 0.39, max 0.03, ultracode 0.01.
  - Model probabilities: Fable 5.1 0.10, Opus 5.5 0.90 (confidence 0.80).
  - Twelve cells, computed from the two answers:
    - Opus 5.5 at low 0.00, Opus 5.5 at medium 0.03, Opus 5.5 at high 0.49, Opus 5.5 at extra high 0.35, Opus 5.5 at max 0.03, Opus 5.5 at ultracode 0.01;
    - Fable 5.1 at low 0.00, Fable 5.1 at medium 0.00, Fable 5.1 at high 0.05, Fable 5.1 at extra high 0.04, Fable 5.1 at max 0.00, Fable 5.1 at ultracode 0.00.
  - Flags: boundary between extra high and high. Sent 2026-10-14T04:59:57Z. Nathan picks the cell.
- **Detail:** v6 sent 2026-10-14T04:59:57Z; HTTP 200 in 0.54 s; 4325 input and 54 output tokens; jev-1.13.0. Rung by rule: high (nearest to the score, halves up). Model by rule: Opus 5.5 (P(most capable) 0.5 or more is Fable 5.1). Flags: boundary between extra high and high.
- No Notion row was written. **Nathan's pick for PR-20 (corrective plan v2.0):** not stated.

**Surface advice:**
- Run PR-20 as a top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, with Notion read access for the prompt. Use the dedicated WU-PR-03 PR engineering role; Nathan chooses whether to reuse the earlier planning session or start a new one.
- It needs a Python 3.12 environment with CI's install, `ruby`, `bash` and `curl`, closed rails and a scratch worktree. With them it can prototype the delta and rehearse the re-cut convergence before presenting the plan.
- It needs no live vendor, production or database access. It writes only plan v2.0 (and an optional prototype diff) under `docs/ephemeral/`. The carrying pull request should be merged first.

## 9. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / WU-PR-03 / Product Owner-directed corrective architecture decisions 1 |
| change / specification | CRD HDE-CRD-0002 / `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` v1.1 |
| work unit | WU-PR-03 (S02, S07, S09, S10, S15, S18) |
| release | GCFPE-20261009.1 / 100926.1 |
| prompt | none: a direct Product Owner instruction in the continuing IA session. Receiver contract named: PR-20 — Create Detailed PR Implementation Plan — 100926.1, https://app.notion.com/p/3f44590a05eb819fbea5dcd966a750ba (revision 2026-10-12T02:29:47.327Z) |
| role/stage | continuing whole-change IA, under Product Owner direction |
| capture time | 2026-10-14T05:10:00Z |
| execution identity | https://claude.ai/code/session_01CCKsYD2yX5WgU3biWKb59j |
| repository persistence | PENDING / NON_GATING (installed writer absent); recorded here only |

## Canon relied on

Read on `main` at `c98d41f`. Each decision is mapped to the sections read in full.

- **AD-1:**
  - PF02-Canon-HDE-Architecture v2.4.6 §3.5 in full and §3.4 in full (the health probes are "Future concepts [Speculative]"; this decision does not change them);
  - PF29-Canon-HDE-Users-Guide v1.0.2 §1.1;
  - PF12-Canon-HDE-Schemas-and-Artifacts v2.9.6 §8.8 in full (purpose, "machine-readable inventory of HTTP endpoints (public surfaces and key internal/ops/dev endpoints)", the record fields and classification set, the Reader surface and success-proof designation, the env-gate pairing);
  - PF05-Canon-HDE-CLI-API-Vendor-Ref v2.5.3 §5.6 in full.
- **AD-2:**
  - PF05 §5.4 in full (Route and gate);
  - PF05 §5.5, the validation and environment-gating bullet;
  - PF12 §8.8 "Reader surface routes and distinct contracts";
  - PF14-Canon-HDE-Mechanics-Guide v3.5.8 §34 (runner, required profile and route table);
  - PF04-Canon-HDE-Governance v2.8.7 "Dev/admin APP_ENV gating (dev/test/local only)".
- **AD-3:** PF05 §5.4 "Gate" and "Documented local-style access"; PF14 §34 "Required local capture profile", "Shared environments" and "Current repository posture".
- **AD-4:**
  - PF02 §1.3 "Separation of surfaces";
  - PF02 §3.2, "A7 proof surface" bullet: "Non-prod entries must be unreachable in production";
  - PF02 §3.3 in full: "Harness is dev-only; never mounted in production" and the "Current repository discrepancy";
  - PF02 §3.5;
  - PF05 §5.4 "Gate";
  - PF04 dev/admin gating;
  - Specification v1.1 S19 and the Exclusions.
- **AD-5:** Plan v1.1 §10; Build Notes 2.6 (step 3b, roster); AGENTS.md release identity.
- **AD-6:** AGENTS.md canon-first rule; PF04 §9.1.2 "Canon precedence and persistent sources".
- **Precedence and authority:** PF04 §9.1.2 (the Specification as the permanent scope authority; canon over in-flight documents); PF27-Canon-Plan-Templates v2.0.5 "Canon precedence for template use" and its addendum-form paragraph; PF10-HDE-Build-Notes v13.5.7 (front matter rules, index, addendum 2.6; next number 2.7).
- **In-flight records:**
  - Specification v1.1 (S09, S10, S15, S19, Exclusions, Live QA classes);
  - Implementation Audit v1.0 EC-4 and EC-8;
  - Plan v1.1 IF-6 and IF-10;
  - Plan review v1.0 R1;
  - instruction v1.0 (§4, §6, §7, §9.2, §14, §15);
  - WU-PR-03 plan v1.1 (§6.2, §6.5);
  - rescope review v1.0 (B-1, B-6) and addendum record 2.6;
  - PR-35 result v1.1 §3 and §6;
  - PR-35 rescope request v1.0 (in full) and PR-35 rescope review v1.0;
  - #643's merge facts.
- **Code measured at `c98d41f`:** the served set of the three factories (53 pairs); the catalog (23 records); `_reader_dev_env_explicit`; `_dev_admin_gate`; the `__main__` run call; the absence of CORS code; the start-helper banner; the env-gate proof.
