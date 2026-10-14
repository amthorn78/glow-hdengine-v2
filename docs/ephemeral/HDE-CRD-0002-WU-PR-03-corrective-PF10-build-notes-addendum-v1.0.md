---
artifact_type: PF10_BUILD_NOTES_ADDENDUM
addendum_id: HDE-CRD-0002-WU-PR-03-CORRECTIVE-1
proposed_pf10_number: "2.7 (next continuous number after addendum 2.6 of the current controlled PF10; allocation and publication are the Product Owner's)"
origin: Product Owner direction of 2026-10-14 to re-plan WU-PR-03 and record its architectural decisions in a PF10 addendum ("create a new PR-20 handoff, including a PF10 addendum with the proper architectural decisions to do this RIGHT"). Not produced by one of the six GCFPE addendum-producer prompts; authored by the continuing whole-change Implementation Agent under that direction
decision_record: HDE-CRD-0002-WU-PR-03-CORRECTIVE-ARCHITECTURE-DECISIONS v1.0, docs/ephemeral/HDE-CRD-0002-WU-PR-03-corrective-architecture-decisions-v1.0.md
immutable_base: HDE-CRD-0002-SPECIFICATION v1.1 (docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md) → Implementation Plan v1.1 + IA-30 review v1.1 (docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md, docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md) → WU-PR-03 PR instruction v1.0 (docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-instruction-v1.0.md)
applicable_prior_addenda: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.7.md §2.2 (WU-PR-03 downstream item), §2.3 (review chain), §2.5 (carried LR-O1 to LR-O3), §2.6 (start-helper propagation, label roster, step 3b). This addendum supersedes §2.6 only where its "Overlaid base clauses" says so
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.7.md on main c98d41f (front matter, index, §2.6); provenance, not a gate
resolves: the PR-35 rescope request v1.0 items RP-4 and RP-5 (docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr35-rescope-request-v1.0.md), returned to the Product Owner by docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr35-rescope-review-v1.0.md (SPECIFICATION_CHANGE_REQUIRED)
return_phase: PR-20 — Create Detailed PR Implementation Plan — 100926.1, corrective plan v2.0 for WU-PR-03, by the dedicated WU-PR-03 PR engineering session (no Proceed, vehicle or open pull request exists for the corrective work; PR_RETURN_PHASE not applicable)
capture_time_utc: 2026-10-14T05:10:00Z
---

## 2.7 HDE-CRD-0002 WU-PR-03 corrective cycle: canon route postures govern the Endpoint Catalog, the dev Reader gate compares APP_ENV exactly, and the canonical dev runner meets the required local capture profile

Timestamp: 101426 05:10 (UTC) Details: Records the architecture decisions for the corrective cycle of work unit WU-PR-03 of HDE-CRD-0002 (public, dev and CLI surfaces; requirements S02, S07, S09, S10, S15, S18). The unit's first pull request, amthorn78/glow-hdengine-v2#643, merged as `c98d41f` with two open review findings.
- Origin: the Product Owner's direction of 2026-10-14 to re-plan the unit with its architecture decided in advance. The decisions were authored by the whole-change Implementation Agent.
- Evidence: canon read on `main` at `c98d41f`, the served route set measured there, the PR-35 rescope request v1.0 and its prototype, and the governed env-gate proof.

### Decision and approval status

These six decisions govern the WU-PR-03 corrective plan and its implementation.
- They are made under the Product Owner's direction. They take effect for the corrective cycle once the Product Owner publishes them as Build Notes.
- They resolve the two review findings that #643 merged with:
  - five Endpoint Catalog rows publishing three canon-retired routes;
  - a dev Reader gate that trims and case-folds `APP_ENV`.
- They settle in advance the remaining canon questions on the unit's surfaces, so that the corrective plan needs no further rescope for them.

The Specification is not edited. The immutable base is not rewritten; the clauses this addendum overlays are listed below. The canon-conflict register entries CR-7 and CR-8 are decided `APPROVED`, alternative (a) each, by this direction.

### Base and what landed

- **What #643 landed on `main`:**
  - the governed not-found envelope (S02);
  - the help text (S07);
  - the dev harness retirement and the `VERIFY.sh` repoint (S09);
  - the request-time `/reader` gate (S10);
  - a 23-row Endpoint Catalog with the Aux record and its validator (S15);
  - the document corrections (S18);
  - the classifier registrations (ID-3) and the contract-inventory baseline (ID-4);
  - the start-helper propagation and the 22-path label roster (Build Notes 2.6);
  - a same-version release refresh with `release_id` `72fca4c341d871dc75a828140ee1494714b322a13656bac93f66164060ea390f`.
- **Corrective delta only.** All of that stands except where a decision below changes it. The corrective cycle is a delta on `main`, not a re-implementation.

### Architecture decisions

**AD-1 — Route postures govern Endpoint Catalog population.**
- **Accounting rule.** Every `(method, path)` that `adapter/factory.py`, `adapter/http_reader.py::create_app` or `adapter/wsgi.py` serves is accounted for exactly once: either by one Endpoint Catalog record, or by one exclusion class with its basis. There are 53 distinct pairs at `c98d41f`.
- **The exclusion classes:**
  - (a) governed refusal;
  - (b) alias of a canonical record;
  - (c) framework-implicit method;
  - (d) **canon-retired route.** HDE Architecture §3.5 "Current repository discrepancy" and HDE Users Guide §1.1 mark `/ops/db/unavailable`, `/ops/probe/env` and `/ops/writer/diagnostic` `RETIRED/NONCANONICAL` and exclude them from the Endpoint Catalog.
- **Class (d) holds nine pairs:** `GET`, `HEAD`, `OPTIONS` of `/ops/db/unavailable` and of `/ops/probe/env`, and `POST`, `HEAD`, `OPTIONS` of `/ops/writer/diagnostic`.
- **Catalog changes.** The five catalog records for those routes are removed. The catalog goes from 23 records to 18, and the exclusions from 30 to 35. The catalog owner's validator refuses, fail-closed, any record whose path is canon-retired.
- **Unchanged:**
  - every other record, including `/internal/healthz` and `/internal/readyz` of `adapter/wsgi.py`, which no canon retires;
  - the `success_endpoints` designation (`GET /reader`);
  - every route. No route is added, removed or changed.
- **S15 reading.** Specification S15 ("Every registered route has a catalog entry, or the route is removed") is read under canon precedence. A registered route that canon explicitly retires and excludes from the Endpoint Catalog is accounted for by that exclusion, and its removal stays with its canon owner.

**AD-2 — The dev Reader gate compares `APP_ENV` exactly.**
- **Rule.** `GET /reader` and its `HEAD` are served only when `APP_ENV` is exactly the string `dev`. There is no trimming and no case-folding.
- **Refused.** Unset, empty and every other value refuse with `403` `ERR_READER_FORBIDDEN`, as before. That includes ` dev`, `dev `, `Dev`, `DEV`, `test` and `local`. Version validation stays first.
- **Basis.** HDE-CLI-API-Vendor-Ref §5.4 "Gate" and §5.6 (`/reader`: "explicit `APP_ENV=dev`"); HDE Schemas & Artifacts "Reader surface routes and distinct contracts (normative)"; HDE Mechanics Guide §34. Canon normalizes `APP_ENV` only where normalization widens refusal (the compat production posture, HDE-CLI-API-Vendor-Ref §5.5). On this gate it would widen serving.
- **Unchanged:** the catalog `env_gate` (`APP_ENV=dev`), `VERIFY.sh`'s exact requirement and the start helper's propagation.

**AD-3 — The canonical dev runner meets the required local capture profile.** The runner is the dev harness that S09 made canonical.
- `python -m adapter.http_reader` binds `127.0.0.1` only. There is no host override, and port `8000` remains the default with an explicit `PORT` override.
- It sets Flask `debug=False`, `use_debugger=False` and `use_reloader=False` explicitly.
- It emits no CORS response header. No `Access-Control-*` header appears on any response, including a cross-origin preflight `OPTIONS`. A test proves this, because canon requires a test-backed disabled-CORS declaration.
- The start helper's banner names the actual host. One line of `scripts/dev_start_reader.sh` changes; its `APP_ENV` propagation is unchanged.
- **Basis:** HDE-CLI-API-Vendor-Ref §5.4 "Gate" ("bound only to a local interface (for example, `127.0.0.1`)") and HDE Mechanics Guide §34 "Required local capture profile".
- **Shared environments.** A shared environment that needs another bind uses an infrastructure-provided start command (HDE Mechanics Guide §34 "Shared environments"), not this runner.

**AD-4 — Production exposure of non-public routes is decided once, in the HDE-CRD-0002 security review, not in WU-PR-03.** No WU-PR-03 requirement covers these four canon gaps, and fixing them changes the production behavior of routes outside S02 to S18:
1. The production factories mount dev-harness routes:
   - the routes: `GET`/`HEAD /reader`, `POST /internal/dev/sampler` and the three `/dev/*/conjunction` routes;
   - the canon: HDE Architecture §3.2 "Non-prod entries must be unreachable in production" and §3.3 "Harness is dev-only; never mounted in production", with its "Current repository discrepancy"; HDE-CLI-API-Vendor-Ref §5.4 "must not be mounted in production builds or non-dev deploys";
   - the unprefixed `POST /reader` refusal stub shares this path.
2. The three canon-retired `/ops` routes stay mounted and ungated in the production factory. `/ops/probe/env` returns process identity and start time.
3. The dev/admin gate used by the sampler and conjunction routes trims and case-folds, although HDE Governance "Dev/admin APP_ENV gating" allows "exactly" `dev`, `test` and `local`.
4. `adapter/http_reader.py::create_app`'s after-request hook never fires.

**Why they are decided there:**
- A correct fix is one factory-level design applied uniformly to every non-public route. Requirement S19 (the HDE-CRD-0002 code security review, work unit WU-PR-05) is the only HDE-CRD-0002 requirement whose scope reaches their exposure. S19 fixes each confirmed finding within HDE-CRD-0002 or routes it to an owner with a reason.
- Until then, the S10 control for `/reader` is the request-time refusal. That matches the governed env-gate proof, which records `/reader_success_unreachable=true` under `APP_ENV=prod`.

**AD-5 — One corrective release refresh.**
- **Trigger.** AD-2 and AD-3 change the release member `adapter/http_reader.py`. The unit therefore cuts a same-version manifest at version `1.3.0` and built time `2026-08-24T18:04:49Z`, then converges the governed evidence through the owners.
- **Order:**
  - the catalog owner runs first after admission (step 3b), because its validator changes (AD-1);
  - every owner and validator is byte-stable on a second pass;
  - a member byte change after the cut restarts at the cut;
  - an evidence-primary change restarts at step 3b.
- **New base.** The new `release_id` becomes the refresh base for WU-PR-04 and WU-PR-05, and `72fca4c3…` becomes historical.
- **Unchanged:** the 22-path label roster, the evidence-index updater and every frozen family.

**AD-6 — Canon trace is part of the deliverable.**
- **Plan and record.** The corrective plan and the unit's result record map each decision, and each route the unit touches, to the canon document, section and bullet relied on.
- **Enumeration test.** The route-enumeration test records every excluded pair's class and basis. A served pair with no recorded posture, or a record for a canon-retired path, fails continuous integration.

### Overlaid base clauses

For WU-PR-03 only. Every other word of each clause holds.

| Base clause | Becomes |
| :- | :- |
| Implementation Plan v1.1 §5 IF-6: the internal rows for `/ops/db/unavailable`, `/ops/probe/env` and `/ops/writer/diagnostic` | withdrawn (AD-1) |
| Audit EC-8 (instruction §4): "Catalog every registered route; remove none" | "Catalog every registered route that canon does not retire; remove none" |
| Instruction ID-1 binding reading and its exclusion classes (a) to (c) | classes (a) to (d) as AD-1 states |
| Instruction §9.2: "Normalize the value as `_dev_admin_gate` does (strip, lower), but serve only `dev`" | "Compare the raw value exactly; serve only `dev`" (AD-2) |
| Instruction §7: "No change to the `0.0.0.0` bind or to the production mount of the gated dev blueprint" | the bind is changed by AD-3; the production mount stays excluded (AD-4) |
| Build Notes 2.6 approved delta item 1 and its binding requirement that `scripts/dev_start_reader.sh` has an empty diff | the script changes in its banner's host text only (AD-3); `APP_ENV` propagation is unchanged |
| WU-PR-03 detailed plan v1.1 §6.2 and PD-5 (normalization), and §6.5 records 5 and 8 to 11 | superseded by AD-2 and AD-1 |

### Binding requirements

- **Catalog.** The catalog has 18 records with none for a canon-retired path. The validator refuses a canon-retired record. The enumeration test accounts for all served pairs: 18 catalogued plus 35 excluded equals 53 at `c98d41f`, or the then-current served count, with the arithmetic stated.
- **Exact gate:**
  - the served test admits exactly `dev`;
  - the refusal matrix includes unset, empty, ` dev`, `dev `, `Dev`, `DEV`, `test`, `local`, `prod`, `production`, `live` and an arbitrary value;
  - `docs/server/reader_v1.md` states "exactly `dev`".
- **Runner profile:**
  - the runner's run call carries `host="127.0.0.1"`, `debug=False`, `use_debugger=False` and `use_reloader=False`;
  - a test proves no `Access-Control-*` header on a dev-runner `GET /reader`, an `OPTIONS` preflight with `Origin` and `Access-Control-Request-Method`, and an error response;
  - `scripts/dev_start_reader.sh` and `docs/server/reader_v1.md` name host `127.0.0.1`;
  - the start-helper owner test and `VERIFY.sh` pass on the loopback bind.
- **Evidence and checks:**
  - the governed catalog family, the transport proofs and every evidence family the refresh regenerates are produced by their owners only;
  - frozen families keep their bytes;
  - the contract-inventory baseline still equals the discovered records;
  - the architecture snapshot test stays green;
  - the full `tests/` sweep passes under closed rails;
  - the two convergence passes are byte-identical;
  - the release attestation builds and verifies.
- **No skips.** No test is skipped, deselected, marked expected-failure or quarantined.

### Scope, exclusions and nonclaims

- **Changed:** catalog content (AD-1), one gate comparison (AD-2), the dev runner's run call and the start helper's banner (AD-3), two documents, tests, and the release refresh (AD-5).
- **Not changed:** no route added, removed, renamed or re-gated other than the `/reader` comparison. No public contract, payload, flag or transport change. No production factory change.
- **Out of WU-PR-03:** AD-4's four gaps.
- **Not edited:** no Specification edit, no permanent-canon edit, no admission-constant or version change.
- **Not established:** no QA verdict, acceptance, Ops, deployment, PF09 or PF30 status movement or closure follows from this addendum. #643's merge and this addendum do not establish acceptance of WU-PR-03.

### Affected surfaces

- **Requirements.** S10 (exact gate; local bind) and S15 (canon-read population) are corrected. S09's canonical runner meets the harness profile. S02, S07 and S18 are unchanged.
- **Tests.**
  - The enumeration test gains class (d), the retired-path pin and retargeted validator cases.
  - The transport gate test changes its served and refused values.
  - A CORS-absence test and runner-profile assertions are added.
- **Evidence.** The catalog family, its sidecars and path proofs, and every family the same-version refresh regenerates, with the Index and Mirror through the updater.
- **Ops and QA.** The S10 Live QA step proves the request-time refusal in the deployed target, as before. S15 stays a catalog-entries-only change. The dev runner is reachable only on loopback.
- **Downstream:**
  - WU-PR-04 and WU-PR-05 refresh from the new `release_id`;
  - WU-PR-05's S19 review receives AD-4's four gaps as named inputs;
  - WU-PR-08's port and bind statements (S17) describe the loopback bind;
  - the repository documentation unit states the start command and bind;
  - a later unit that changes the catalog validator runs its owner at step 3b.
- **Canon doc-delta candidates (not edited):**
  - HDE Schemas & Artifacts §8.8: the population rule, including canon-retired exclusion, `public_aux` and `aliases`;
  - HDE-CLI-API-Vendor-Ref §5.6 "Implementation and acceptance state";
  - HDE Mechanics Guide §34 "Current repository posture" (bind, flags, CORS, `APP_ENV` default), and its route table's `/api/reader` alias row;
  - HDE Architecture §3.4, which labels the health probes speculative, while HDE Mechanics Guide §32.3 requires them.

### Evidence

- **Served set at `c98d41f`:** 53 distinct pairs across the three factories. The catalog holds 23 records, five of them for the three canon-retired routes. The canon-retired pairs number nine.
- **Dev runner and gate at `c98d41f`:**
  - `adapter/http_reader.py` runs `create_app().run(host="0.0.0.0", port=…)` with no debugger or reloader arguments;
  - no module under `adapter/` or `engine/http/` emits a CORS header or imports a CORS extension;
  - the gate returns `raw.strip().lower() == "dev"`;
  - the start helper's banner prints `host=0.0.0.0`.
- **Env-gate proof.** The governed env-gate proof records `APP_ENV=prod` with `/reader_success_unreachable=true`.
- **PR-35 prototype.** It removed the five records, added class (d) and the retired pin, and regenerated the catalog family: validators exit 0, 253 tests passed. It also implemented the exact comparison with a re-cut: 28 tests passed. Its `release_id` value is not binding.

### Conflicts

- **CR-7** (CANON_RECONCILIATION): Specification S15 and the approved Plan's IF-6 and EC-8 catalogued three routes that HDE Architecture §3.5 excludes. Decided `APPROVED`, alternative (a): exclusion under canon, as AD-1 states.
- **CR-8** (CANON_RECONCILIATION): the instruction's normalizing gate conflicted with the explicit `APP_ENV=dev` passages. Decided `APPROVED`, alternative (a): exact comparison, as AD-2 states.
- **Carried:** CR-1 to CR-6 of HDE-CRD-0002, unchanged.

### Unresolved obligations and owners

- PF10 numbering and publication: the Product Owner.
- The corrective plan v2.0, the Product Owner's Proceed, implementation and the corrective pull request: the dedicated WU-PR-03 PR engineering session.
- The lineage review across #643 and the corrective pull request: the whole-change Implementation Agent, after that merge.
- AD-4's four gaps: S19 in WU-PR-05, through its instruction. Any gap S19 cannot reach returns to the Product Owner as a separate change candidate.
- A shared-environment bind need, if one appears: the Product Owner and infrastructure canon.
- The doc-delta candidates: the Product Owner.

### Status and consequences

- **Completed:** these decisions and their record.
- **Not yet done:** the corrective plan, Proceed, implementation, reviews, merge and lineage review.
- **Unproven:**
  - the full sweep and the two-pass convergence on the corrective branch;
  - loopback reachability in every shared environment the Product Owner uses.
- **Consequences when the corrective pull request lands:**
  - the Endpoint Catalog publishes only routes canon recognises;
  - the dev Reader route serves only for the exact value `dev` and only on loopback from the canonical runner;
  - the runner meets the canon harness profile;
  - the production exposure of every non-public route is settled once, under the security review.
