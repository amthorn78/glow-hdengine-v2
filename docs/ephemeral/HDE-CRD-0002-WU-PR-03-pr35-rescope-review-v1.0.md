---
artifact_type: RESCOPE_REVIEW
artifact_id: HDE-CRD-0002-WU-PR-03-PR35-RESCOPE-REVIEW
artifact_version: "1.0"
artifact_state: COMPLETE
decision: SPECIFICATION_CHANGE_REQUIRED
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-03
items_assessed: RP-4 (Specification S15 boundary versus HDE Architecture §3.5; Product Owner decision required); RP-5 (within IA authority; alternative (a) supportable; not decided as an overlay by this state, §5)
request_ref: docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr35-rescope-request-v1.0.md (v1.0, RESCOPE_REQUEST, RESCOPE_REQUEST_PENDING_REVIEW; 27,411 bytes; read in full; on main via the #643 squash c98d41f)
request_author: the dedicated HDE-CRD-0002 WU-PR-03 PR-35 session, https://claude.ai/code/session_0136SjBtuTJwoEpceUd46T6C
reviewer: the continuing whole-change Implementation Agent (IA) for HDE-CRD-0002, this session https://claude.ai/code/session_01CCKsYD2yX5WgU3biWKb59j (author of the WU-PR-03 instruction v1.0 and of rescope review v1.0)
author_reviewer_independence: VERIFIED (distinct sessions and roles; this IA did not author the request or its prototype). Disclosure: both items concern rules this IA wrote (instruction ID-1, EC-8 via the Audit, §9.2; rescope review v1.0 B-6)
producing_prompt: RS-20 — Review Bounded Work-Unit Rescope — 100926.1 (https://app.notion.com/p/3f44590a05eb81be9566cd6397c9424c; retrieved revision last edited 2026-10-12T02:29:57.795Z); release GCFPE-20261009.1 / 100926.1
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
originating_stage_recorded: PR-35, PR_RETURN_PHASE PR-35, open pull request #643
vehicle_state_relied_on: amthorn78/glow-hdengine-v2#643 is MERGED (merged=true, merged by amthorn78 at 2026-10-14T04:41:15Z; head dc45a359c6d9c5fbae5f707ba1cae35d04e6d45c; base 1735d94; squash commit c98d41f, tree 1a888b8fc355 equal to the head tree). The merged head includes the PR-35 record commit carrying this request. The Codex P1 threads PRRT_kwDOP103ks6sJ4Y8 (RP-5) and PRRT_kwDOP103ks6sJ4Y_ (RP-4) were open at merge (result v1.1 §3). No open pull request for WU-PR-03 exists. WU-PR-03 is merged but not accepted (no PR-40 review). origin/main c98d41f; docs/pfcanon/PF10-HDE-Build-Notes-v13.5.7.md is now the controlled PF10 on main
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-instruction-v1.0.md (v1.0; overlaid by addendum 2.6 for the clauses of rescope review v1.0 §7.1 B-2)
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-implementation-plan-v1.1.md (v1.1, Proceeded)
IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (v1.1; immutable)
PLAN_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (v1.1, IA-30 INITIAL_APPROVE)
SPECIFICATION_ID: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (v1.1, SPECIFICATION_APPROVED)
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.7.md on main c98d41f (read: front matter, index, §2.6); docs/pfcanon/PF10-HDE-Build-Notes-v13.5.6.md as read for rescope review v1.0 (addenda 2.1–2.5). No addendum addresses Endpoint Catalog population of retired routes or the dev Reader APP_ENV comparison
pf10_addendum_created: none (SPECIFICATION_CHANGE_REQUIRED creates no addendum)
capture_time_utc: 2026-10-14T05:05:00Z
return_to: Nathan / Product Owner, terminally, for the RP-4 decision and its Specification-delta route (§6). No continuation prompt
canon_conflict_register: CR-1 to CR-6 carried unchanged; CR-7 PROPOSED, reviewed, escalated to the Product Owner; CR-8 PROPOSED, reviewed, IA supports (a) (§7)
---

# HDE-CRD-0002 WU-PR-03 — PR-35 Rescope Review v1.0

Canon precedence rule for this derived artifact (Plan Templates, "Canon precedence for template use"): Applicable, active, non-superseded PF10 addenda supersede conflicting PF-Canon only for the exact scope they address; otherwise follow PF-Canon. A formally approved bounded Product Owner rescope may supersede conflicting PF-Canon only for the exact decision it adjudicates.

## 1. Decision

**`SPECIFICATION_CHANGE_REQUIRED`.** One state for the one request. The state comes from RP-4.

- **RP-4 is a Product Owner decision.**
  - The approved Specification S15 requires every registered route to have a catalog entry or to be removed. Its intake brief names the three routes in question.
  - HDE Architecture §3.5 excludes the same three routes from the Endpoint Catalog and claims no removal.
  - Under canon, only two options satisfy both, and neither is this IA's to choose:
    - narrowing S15 for canon-retired routes is a Specification boundary;
    - removing production-mounted routes is a production change that canon expressly declines to promise.
- **RP-5 is within IA authority.** The exact comparison (alternative (a)) is supportable. RS-20 allows one state per request, and this request returns terminally on RP-4, so RP-5 is not approved as an overlay here. §5 holds the full assessment so the next RS-20 reuses it rather than repeating it.

**No addendum.** No handoff, no Proceed, no implementation or merge authority.

**Vehicle change.** #643 merged after the request was written (§2). `PR_RETURN_PHASE: PR-35` and the RS-40 resume route are no longer available. Any new implementation for WU-PR-03 is a corrective cycle under a lawful prospective PR owner (RS-20: merged-but-unaccepted findings).

## 2. Vehicle state and request completeness

**Vehicle.**
- #643 merged at 2026-10-14T04:41:15Z as squash `c98d41f`. The squash tree equals head `dc45a35`'s tree (`1a888b8f…`).
- The merged content includes `3a1b0a7` (the F1 fix), the PR-35 records and this request.
- It also includes the code both items concern: the five `/ops/*` rows, and the trimming, case-folding gate.
- The two P1 Codex threads were open at merge. No open pull request for WU-PR-03 remains.
- RS-20 routes a merged-but-unaccepted finding to a lawful prospective PR owner. It does not use RS-40, which needs the same open pull request.

**Request completeness.** The request carries every input RS-20 requires:
- findings, Specification, base, PF10, deltas, stage, lineage, completed work, impact, evidence, risks, exclusions and conflicts (§1–§9);
- the canon searches;
- a prototype of both deltas.

Its vehicle facts were true when it was written (04:00–04:05Z). The merge is later than the request, so the request is not defective on that account.

## 3. Evidence verified by this reviewer on `main` (`c98d41f`)

| Fact | Verified |
| :- | :- |
| `docs/ENDPOINTS_CATALOG.json` holds 23 rows, including `GET /ops/db/unavailable`, `GET /ops/probe/env`, and `POST`, `HEAD`, `OPTIONS /ops/writer/diagnostic` (the POST row with `route_id: ops.writer.diagnostic.v1`), each `classification: ops`, `internal: true`, `env_gate: operator-network-only` | yes |
| `adapter/http_reader.py::_reader_dev_env_explicit` returns `raw_app_env is not None and raw_app_env.strip().lower() == "dev"` (lines 378–383); `tests/http/test_reader_a7_transport.py` line 139 serves `"dev"`, `" DEV "`, `"Dev"`; `docs/server/reader_v1.md` line 17 states "surrounding whitespace and letter case ignored" | yes |
| HDE Architecture §3.5 "Current repository discrepancy": the three routes are "`RETIRED/NONCANONICAL` as architecture and excluded from the Endpoint Catalog … No repository removal, test migration, deployment convergence, or catalog mutation is claimed." Adopted routes: `/internal/version`, `/ops/rails/refusal` | read in full |
| HDE Users Guide §1.1 "Checked-in retired/noncanonical route drift (unsupported)": the same three routes, "Do not use as an operator workflow"; the rows "do not … promise removal, create a deprecation window, or imply compatibility support" | read |
| The exclusion text was on `main` before the Specification was approved: last `-S` change `f29d778` (2026-10-05); Specification review v1.1 `982071b` (2026-10-12) | yes |
| Specification v1.1 S15 (5(g), RA-14): "Reconcile the endpoint catalog with the routes the service registers"; acceptance intent "Every registered route has a catalog entry, or the route is removed; the audit mirror is produced by its owner". The candidate-item briefs v1.2 item (g) behind it lists `/ops/db/unavailable`, `/ops/probe/env` and `/ops/writer/diagnostic` among the uncatalogued routes. The Live QA table classes "S15 where it removes a registered route" as production-affecting and "S15 (catalog entries only)" as not | yes |
| Canon on the dev gate: HDE-CLI-API-Vendor-Ref §5.4 "Gate": "must be gated by `APP_ENV=dev`"; §5.6 table: `/reader` "explicit `APP_ENV=dev`"; HDE Schemas & Artifacts "Reader surface routes and distinct contracts (normative)": "explicitly gated by `APP_ENV=dev`"; HDE Mechanics Guide §34: "requires explicit `APP_ENV=dev`"; HDE Governance "Dev/admin APP_ENV gating (dev/test/local only)": allowed values are "exactly" `{"dev","test","local"}` | read |
| Canon normalizes `APP_ENV` in one place only: HDE-CLI-API-Vendor-Ref §5.5 resolves the compat production posture "by trimming and case-folding". That normalization widens refusal (fail-closed); on the dev gate, normalization widens serving | read |

## 4. RP-4: canon-retired routes in the Endpoint Catalog

### 4.1 Why the matter leaves this IA

- **The Specification names these routes.** S15's intake brief lists the three routes as uncatalogued. Its acceptance gives two compliant outcomes per route: a catalog entry, or removal.
- **Canon permits only one of them, and does not require it.** HDE Architecture §3.5 rules out the catalog entry. Neither it nor the Users Guide requires or promises removal.
- **Option (a) narrows S15.** Excluding the routes without removing them meets canon. It leaves S15's acceptance literally unmet for three routes the Specification specifically intended to reconcile. Reading S15 so that canon-retired routes are excluded narrows an approved Specification acceptance criterion. Canon precedence makes the catalog entry unlawful. It does not choose between the remaining options, because removal also satisfies both canon and S15. Choosing exclusion over removal is therefore a choice about Specification intent, not a consequence of precedence. In this change, Specification-versus-canon conflicts have been decided by the Specification owner or the Product Owner (CR-1 to CR-3 Thoth; CR-4 and CR-5 the Product Owner), not by the IA.
- **Option (b) is Material.** Removing the routes meets S15 literally and canon. But it:
  - changes production behavior (the production factory mounts the blueprint);
  - moves S15 into the production-affecting Live QA class, adding QA-10 Live QA scope;
  - reverses the Plan's EC-8 "remove none";
  - overlaps WU-PR-05's S19 review of the same routes (OBS-P3-4);
  - takes a step canon expressly declines to promise.

  That is risk needing Product Owner direction, and a protected production surface.
- **Option (c) is the Product Owner's by definition.** Keeping the rows overrides canon (the CR-4 pattern).

### 4.2 What breaks if nothing is decided

`main` now publishes three canon-retired routes as supported `ops` records in the governed catalog and its audit mirror. The Codex P1 finding on #643 is open. PR-40 cannot accept WU-PR-03 while S15 has no lawful completed reading, and QA cannot judge S15 either.

### 4.3 Options for the Product Owner, with this IA's recommendation

| Option | What the Product Owner decides | Cost | Assessment |
| :- | :- | :- | :- |
| **(a) Exclude, under canon (recommended)** | A bounded Product Owner disposition, or a Specification delta through Thoth, that S15 excludes canon-retired routes (HDE Architecture §3.5) from "every registered route", leaving their removal to its canon owner. The IA then approves the request's delta (a) through RS-20: five rows out (23 → 18), a fail-closed "retired route must not be cataloged" pin, and ID-1 exclusion class (d) holding the nine served pairs | 2 hand-edited files and 11 owner-produced files (request §3.4, prototyped: validators exit 0; 253 tests passed). No member change, no route change. S15 stays "catalog entries only" | Smallest change. Conforms to canon. Leaves production behavior unchanged |
| (b) Remove the three routes | Authorization of a production route removal inside HDE-CRD-0002 | `adapter/http_reader.py` (member: re-cut and full convergence); the tests that exercise the routes; `artifacts/proofs/writers_no_304.txt`; the ID-4 contract-inventory baseline; the architecture snapshot (a governed artifact the instruction holds unchanged); QA-10 Live QA for the removal; overlap with WU-PR-05 S19 | Meets S15 literally. A production change canon does not ask for |
| (c) Keep the rows | A Product Owner override of HDE Architecture §3.5 for the catalog, with canon drainage | None in code | The governed catalog keeps publishing routes canon calls unsupported |

## 5. RP-5: the dev `GET /reader` comparison (assessed; not decided as an overlay)

- **Classification.** A bounded implementation delta within IA authority. IF-10 (Plan v1.1) says "explicitly `dev`; … every other value … refuse". Canon says `APP_ENV=dev` explicitly (§3). This IA's instruction §9.2 ("Normalize … (strip, lower), but serve only `dev`") and rescope review v1.0 B-6 added the normalization.
- **Why the normalization is wrong here.** Canon normalizes only where doing so widens refusal (§3, last row). On the dev gate it widens serving. The rule is an instruction-level choice that departs from canon's wording. Correcting it overlays this IA's own instruction text, so it needs an `APPROVE` with an addendum, not `IN_SCOPE_REPAIR`.
- **It is not Material.** It changes no Specification outcome. S10 says "explicitly `dev`, `test` or `local`", narrowed to `dev` by the Plan, and exact comparison meets it. No other unit is touched.
- **Supportable delta.** The request's alternative (a):
  - `_reader_dev_env_explicit` returns `os.environ.get("APP_ENV") == "dev"`;
  - the served test keeps `dev` only, and the refusal matrix adds ` dev`, `dev `, `Dev` and `DEV`;
  - `docs/server/reader_v1.md` line 17 reads "exactly `dev`";
  - `_dev_admin_gate`, the sampler and conjunction gates, `VERIFY.sh`, the start helper and the catalog `env_gate` stay unchanged.
- **Cost.** It is a release-member change, so it needs a same-version re-cut and a full convergence from plan §6.10 step 2, with a new `release_id` for WU-PR-04 and WU-PR-05.
- **Why it is not approved now.**
  - RS-20 allows one state per request, and this request returns terminally on RP-4.
  - RP-4 and RP-5 must land in one corrective change in any case, so that one re-cut and one convergence cover both.
- **Re-entry.** This assessment is a complete prior result for that review: evidence §3, classification and delta above. The next RS-20 on WU-PR-03 reuses it without re-analysis, unless the code or canon it rests on has changed.
- **Observation.** `_dev_admin_gate` also normalizes, and HDE Governance and HDE-CLI-API-Vendor-Ref §5.11 say "exactly". That is pre-existing behavior outside WU-PR-03. This IA owns it and routes it at the next applicable instruction (OBS-RS2-1).

## 6. Return

This decision returns terminally to Nathan / Product Owner for the RP-4 choice in §4.3 and its Specification-delta route: a bounded Product Owner disposition, or a Specification revision through Thoth.

After the decision, the lawful sequence for the merged, unaccepted unit is:
1. **PR-40** (lineage review of #643 by this IA). It verifies the merge, CI and review state and defines the corrective scope.
2. **A corrective cycle** by the WU-PR-03 PR engineering session, as with WU-PR-02:
   - a corrective PR-20 plan under a new Proceed;
   - a rescope request for RP-5 and for RP-4 as the Product Owner decided it, reviewed through RS-20, which reuses §5 and the request's prototype.

This review emits no continuation prompt and invokes none of these.

## 7. Canon-conflict register

CR-1 to CR-6 carried unchanged:
- CR-1 to CR-3: `APPROVED_AS_CHANGED` (Thoth).
- CR-4: `APPROVED`, and CR-5: `APPROVED_AS_CHANGED` (Product Owner).
- CR-6: `APPROVED` (the IA, rescope review v1.0 §12).

| Field | CR-7 (RP-4) | CR-8 (RP-5) |
| :- | :- | :- |
| Classification | CANON_RECONCILIATION; Specification-level (S15 versus HDE Architecture §3.5) | CANON_RECONCILIATION; instruction-level (§9.2 and B-6 versus HDE-CLI-API-Vendor-Ref §5.4 and §5.6, HDE Schemas & Artifacts, HDE Mechanics Guide §34) |
| Sources and versions | Specification v1.1 S15 and briefs v1.2 (g); Plan v1.1 IF-6, EC-8; instruction ID-1; plan v1.1 §6.5. Versus HDE Architecture v2.4.6 §3.5 and HDE Users Guide v1.0.2 §1.1, on `main` `c98d41f` | Instruction v1.0 §9.2; plan v1.1 §6.2 and PD-5; rescope review v1.0 B-6. Versus HDE-CLI-API-Vendor-Ref v2.5.3 §5.4 and §5.6; HDE Schemas & Artifacts v2.9.6 Reader surface routes; HDE Mechanics Guide v3.5.8 §34; HDE Governance v2.8.7 dev/admin gating |
| Statement | The Specification requires the three routes catalogued or removed; canon excludes them from the catalog and claims no removal | The gate trims and case-folds; canon states explicit `APP_ENV=dev` |
| Alternatives | (a) exclude under canon; (b) remove; (c) Product Owner override | (a) exact comparison; (b) keep normalization |
| Recommended | (a) | (a) |
| Status | `PROPOSED`. Reviewed by this IA; decision owner: the Product Owner (escalated, §6) | `PROPOSED`. Reviewed by this IA, which supports (a); to be decided with the request's re-entry (§5) |
| Interim treatment | the five rows remain on `main` | the normalizing gate remains on `main` |
| Unresolved risk | catalog publishes unsupported routes until corrected | ` DEV ` or `Dev` serves the dev route. Production `APP_ENV` is `prod`, so production refuses either way |
| Drainage | under (a): HDE Schemas & Artifacts §8.8 population rule, HDE-CLI-API-Vendor-Ref §5.6 implementation state (Product Owner) | none under (a) |
| Reviewer / session / time | this IA, https://claude.ai/code/session_01CCKsYD2yX5WgU3biWKb59j, 2026-10-14T05:05:00Z | same |
| Reviewed artifact | request v1.0 §7 | request v1.0 §7 |
| History | PROPOSED 2026-10-14T04:00:00Z (request); reviewed and escalated by this review | PROPOSED 2026-10-14T04:00:00Z (request); reviewed by this review |

## 8. Evidence against each excluded decision

| Excluded | Reason |
| :- | :- |
| `APPROVE` | RP-4's recommended delta narrows an approved Specification acceptance criterion; its alternative is a Material production change. Neither is within IA authority (§4.1) |
| `REJECT` | Both findings are real and canon-backed (§3). Keeping the rows or the normalization would leave canon violated without a Product Owner decision |
| `REVISION_REQUIRED` | The request is complete and precise (§2). What is missing is authority, not evidence |
| `IN_SCOPE_REPAIR` | The base expressly requires cataloguing every served route (EC-8, ID-1) and normalizing the gate (§9.2). Neither correction is already authorized |

## 9. Working-state note

- Attempt 1 of this RS-20 invocation for this request. No prior decision exists for it.
- Writes: this review and its checkpoint, `docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr35-rescope-review-v1.0-checkpoint.md`, on this session's working branch, with one pull request for the Product Owner to merge. No handoff file: the return is terminal.
- No addendum, no Notion write, no code or evidence write.
- No reproduction was run for this decision. It rests on the canon and code facts in §3, and the request's prototype results are cited as the request records them. Re-entry reuses this file.

## 10. TypeSafe reading and surface advice

TypeSafe: not read. The return is terminal to the Product Owner, so there is no receiving session to score; the skill scores a session prompt. Surface advice: none for the same reason. The next session prompt (PR-40 for #643, after the decision) is scored by whoever issues it.

## 11. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / RS-20 / WU-PR-03 / rescope review 2 (PR-35 request) |
| change / specification | CRD HDE-CRD-0002 / `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` v1.1 |
| work unit | WU-PR-03; S15 (RP-4), S10 (RP-5) |
| release | GCFPE-20261009.1 / 100926.1 |
| prompt | RS-20 — Review Bounded Work-Unit Rescope — 100926.1, https://app.notion.com/p/3f44590a05eb81be9566cd6397c9424c (revision 2026-10-12T02:29:57.795Z) |
| role/stage | continuing whole-change IA / RS-20 review of a PR-35 request (vehicle merged before review) |
| capture time | 2026-10-14T05:05:00Z |
| execution identity | https://claude.ai/code/session_01CCKsYD2yX5WgU3biWKb59j |
| repository persistence | PENDING / NON_GATING (installed writer absent); recorded here only |

## Canon relied on

Read on `main` at `c98d41f`. Each decision topic is mapped to its sources.

- **Decision matrix, materiality, routing, merged-but-unaccepted handling (§1, §2, §6, §8):** RS-20 — Review Bounded Work-Unit Rescope — 100926.1 (Notion, read in full); PF04-Canon-HDE-Governance v2.8.7 §9.1.2 (canon over in-flight documents; correct lower-authority material only when authorized, otherwise report and stop; the approved Specification is the permanent intended-scope authority); PF27-Canon-Plan-Templates v2.0.5 "Canon precedence for template use"; `AGENTS.md` canon-first rule; precedent: the CANON_CONFLICT_REGISTER owners for CR-1 to CR-6.
- **RP-4 (§4):** PF02-Canon-HDE-Architecture v2.4.6 §3.5 in full; PF29-Canon-HDE-Users-Guide v1.0.2 §1.1 (surface table and "Checked-in retired/noncanonical route drift (unsupported)"); Specification v1.1 S15 row, the Live QA classification table and the briefs v1.2 item (g); Implementation Audit v1.0 S15; instruction v1.0 ID-1 and §14 (as quoted by the request and checked).
- **RP-5 (§5):** PF05-Canon-HDE-CLI-API-Vendor-Ref v2.5.3 §5.4 "Gate" bullet, §5.5 validation and environment-gating bullet, §5.6 `/reader` row; PF12-Canon-HDE-Schemas-and-Artifacts v2.9.6 "Reader surface routes and distinct contracts (normative)" (line 4687 passage); PF14-Canon-HDE-Mechanics-Guide v3.5.8 §34 route table; PF04-Canon-HDE-Governance v2.8.7 "Dev/admin APP_ENV gating (dev/test/local only)" (allowed-values bullets). A canon-wide search for trimming or case-folding of `APP_ENV` found only §5.5.
- **PF10:** PF10-HDE-Build-Notes v13.5.7 on `main` (front matter, index, addendum 2.6); addenda 2.1 to 2.5 as read in v13.5.6. Silent on both topics.
- **In-flight records:** request v1.0 (in full); result v1.1 §1, §3, §6; rescope review v1.0 B-6 and B-12.
- **Not re-read:** HDE Schemas & Artifacts §8.8 catalog-population prose. The request read it, and the decision does not rest on it, because HDE Architecture §3.5 states the exclusion directly.

---

**Status:** `RESCOPE_REVIEW` v1.0, decision `SPECIFICATION_CHANGE_REQUIRED`. RP-4 goes to the Product Owner (recommended: (a) exclude under canon). RP-5 is assessed as supportable and is carried for the corrective re-entry. No addendum; no continuation.
