---
artifact_type: RESCOPE_REQUEST
artifact_id: HDE-CRD-0002-WU-PR-03-PR35-RESCOPE-REQUEST
artifact_version: "1.0"
status: RESCOPE_REQUEST_PENDING_REVIEW
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-03
items: RP-4 (five endpoint-catalog rows publish three routes that HDE Architecture §3.5 marks RETIRED/NONCANONICAL and excludes from the Endpoint Catalog); RP-5 (the dev GET /reader gate trims and case-folds APP_ENV as instruction §9.2 directs, so " DEV " and "Dev" are served, where canon reads "explicit APP_ENV=dev")
originating_stage: PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1 (review correction after Proceed)
PR_RETURN_PHASE: PR-35
author: originating PR implementation author, the dedicated HDE-CRD-0002 WU-PR-03 PR-35 session, https://claude.ai/code/session_0136SjBtuTJwoEpceUd46T6C (session_disposition NEW_DEDICATED; top-level session Nathan created)
reviewer: the continuing whole-change Implementation Agent (IA) for HDE-CRD-0002 through RS-20 (the IA issued instruction v1.0 and rescope review v1.0 and did not author this request)
open_pull_request: amthorn78/glow-hdengine-v2#643 (open, not draft, base main)
proceed: Nathan / Product Owner's original PR-30 — PR Implementation Proceed — 100926.1 for exactly docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-implementation-plan-v1.1.md (result v1.0 front matter); no other Proceed exists or is requested
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-instruction-v1.0.md (v1.0, INSTRUCTION_READY; blob 74e8f158b48d)
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-implementation-plan-v1.1.md (v1.1, Proceeded; blob 1e18046e5bd4)
IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (v1.1; immutable; blob abffa2ccbd44)
PLAN_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (v1.1, IA-30 INITIAL_APPROVE; blob 0cc0276524b2)
SPECIFICATION_ID: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (v1.1, SPECIFICATION_APPROVED; blob c4802a5a7fa3)
prior_rescope_lineage: docs/ephemeral/HDE-CRD-0002-WU-PR-03-rescope-request-v1.0.md (RP-1 to RP-3; PR-20) decided by docs/ephemeral/HDE-CRD-0002-WU-PR-03-rescope-review-v1.0.md (RS-20 APPROVE, B-1 to B-12; blob e3f50f162130) with addendum record docs/ephemeral/HDE-CRD-0002-WU-PR-03-PF10-build-notes-addendum-v1.0.md (2.6; blob 345985d7d9c8). This request is new; it revises neither
phase_record: docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-implementation-result-v1.1.md (PR-35 checkpoint, RESCOPE_PENDING); predecessor docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-implementation-result-v1.0.md (PR-30, PR_CANDIDATE_PUBLISHED)
companion: docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr35-rescope-request-v1.0-prototype.diff (scratch prototypes of the recommended deltas; never applied to the pull request)
AUTHORING_CONTEXT: APPROVED_BASE_WITH_OVERLAYS
immutable_approved_base: Specification v1.1 → Implementation Plan v1.1 + review v1.1 → PR instruction v1.0
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.6.md on main (blob 9c5468fb69e4; sha256 8663ab94289adae0…; read in full, 501 lines to <eof>). Addenda 2.1 to 2.5; none addresses Endpoint Catalog population of retired routes or the dev Reader APP_ENV comparison (PF10 silence rule, "Precedence, versioning, and scope" §8). The pull request carries docs/pfcanon/PF10-HDE-Build-Notes-v13.5.7.md (Product Owner directed; unmerged; sha256 dfb4478c…), which adds only §2.6 (= addendum record 2.6), also silent on both topics
pf10_addendum_paths: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.6.md §2.2, §2.3, §2.5; §2.6 = docs/ephemeral/HDE-CRD-0002-WU-PR-03-PF10-build-notes-addendum-v1.0.md
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
repository_baseline: origin/main 1735d9449a02629566b6f4c618d6931f299d2e10
created_at: 2026-10-14T04:00:00Z
canon_conflict_register: CR-1 to CR-6 carried unchanged; CR-7 (RP-4) and CR-8 (RP-5) PROPOSED by this request (§7)
expected_output: one RESCOPE_REVIEW by the IA under docs/ephemeral/, one decision per the RS-20 matrix, and on APPROVE exactly one PF10_BUILD_NOTES_ADDENDUM
---

# HDE-CRD-0002 WU-PR-03 — PR-35 rescope request v1.0

## 1. Request

The WU-PR-03 PR-35 session asks the whole-change IA for one RS-20 decision on two items raised by the Codex code review of [amthorn78/glow-hdengine-v2#643](https://github.com/amthorn78/glow-hdengine-v2/pull/643). Both touch text the IA bound: instruction ID-1 and §9.2, and rescope review v1.0 B-6 ("The `/reader` gate design (IF-10's first part), the catalog `env_gate` (`APP_ENV=dev`), acceptance (2)'s refusal set, IF-6, IF-11 and the members are unchanged"). B-12 routes any further change of that kind here.

| Item | Codex thread | Boundary | Requested decision | Recommended |
| :- | :- | :- | :- | :- |
| RP-4 | `PRRT_kwDOP103ks6sJ4Y_` (P1, comment 4266550069, `tools/evidence/generate_a7_transport_proofs.py` L54, commit `b178f03`) "Keep retired diagnostic routes out of the catalog" | IF-6 and EC-8 (Implementation Plan v1.1 §5), instruction ID-1 (binding reading and exclusion classes (a)–(c)), acceptance (5)'s reading, plan v1.1 §6.5 rows 5 and 8–11, B-6. Instruction ID-1 names this exact case as a boundary finding: "If PR-20 finds a served pair that fits none of (a) to (c) and has no defensible row, that is a boundary finding for RS-10/RS-20 (§14)"; §14 lists it as the first expected trigger | Decide whether the five rows leave the catalog and how the enumeration test accounts for the routes | Alternative (a), §3.3 |
| RP-5 | `PRRT_kwDOP103ks6sJ4Y8` (P1, comment 4266550065, `adapter/http_reader.py` L383–384, commit `b178f03`) "Require the exact `dev` environment value" | instruction §9.2 ("Normalize the value as `_dev_admin_gate` does (strip, lower), but serve only `dev`"), plan v1.1 §6.2 and PD-5, B-6. A protected security boundary (S10 is the fail-closed dev gate); the PR session cannot amend the IA's disposition rule | Decide whether the gate compares the raw value exactly | Alternative (a), §4.3 |

The third Codex thread on #643 (`PRRT_kwDOP103ks6sJ2D_`, P2, aliases off the Aux record) is an ordinary in-scope correction. PR-35 fixed it in commit `3a1b0a7` (result v1.1, in-flight decision D-4). It is not part of this request.

## 2. Canon searched and read for both items

Canon was searched on `main` (`git grep` on `origin/main -- docs/pfcanon/` for `/ops/probe/env`, `/ops/db/unavailable`, `/ops/writer/diagnostic`, `RETIRED/NONCANONICAL`, `Endpoint Catalog`, `ENDPOINTS_CATALOG`, `APP_ENV`, `explicit`, `exactly`). The governing sections found were read in full: HDE Architecture §3.5; HDE Users Guide §1.1 "Checked-in retired/noncanonical route drift (unsupported)"; HDE-CLI-API-Vendor-Ref §5.4 and §5.6 (and §5.5, §5.11 for contrast); HDE Schemas & Artifacts §8.8; HDE Mechanics Guide §34 route table and "Current repository posture"; HDE Governance §4.1.4 "Dev/admin APP_ENV gating (dev/test/local only)"; PF10 v13.5.6 in full. No HDE-CRD-0002 document under `docs/ephemeral/` cites HDE Architecture §3.5 or the term `RETIRED/NONCANONICAL` (searched); the instruction's ID-1 "No conflict" analysis read HDE Schemas & Artifacts §8.8 and HDE-CLI-API-Vendor-Ref §5.6 only.

## 3. RP-4: retired diagnostic routes in the Endpoint Catalog

### 3.1 Evidence

**Canon on `main`:**
- HDE Architecture §3.5 "Internal-ops identity and refusal (route-only)", *Current repository discrepancy*: "The checked-in `/ops/db/unavailable`, `/ops/probe/env`, and `/ops/writer/diagnostic` routes are `RETIRED/NONCANONICAL` as architecture and excluded from the Endpoint Catalog. Their continued presence in the selected blueprint is repository drift; this document does not describe them as supported ops, admin, diagnostic, evidence, product, or public interfaces. No repository removal, test migration, deployment convergence, or catalog mutation is claimed." The adopted routes are `/internal/version` and `/ops/rails/refusal`.
- HDE Users Guide §1.1 lists the same three routes as `RETIRED/NONCANONICAL`, "Unsupported … Do not use as an operator workflow", and states the rows "do not define route bytes, promise removal, create a deprecation window, or imply compatibility support".
- HDE-CLI-API-Vendor-Ref §5.6's transport-facts table does not list the three routes (nor `/ops/rails/refusal` or the two health routes).
- HDE Schemas & Artifacts §8.8 calls the Catalog "a machine-readable inventory of HTTP endpoints (public surfaces and key internal/ops/dev endpoints)" and requires selection from "real mounted routes". It does not require every mounted route to be catalogued and does not override §3.5's exclusion.
- PF10 is silent (front matter), so permanent canon governs (AGENTS.md canon-first rule; HDE Governance §9.1.2).

**Approved-base text that conflicts:**
- Implementation Plan v1.1 §5 IF-6: "internal rows for `/ops/db/unavailable`, `/ops/rails/refusal`, `/ops/probe/env`, `/ops/writer/diagnostic` (`adapter.http_reader`) and `/internal/healthz`, `/internal/readyz` (`adapter.wsgi`)".
- EC-8 (instruction §4): "Catalog every registered route; remove none … the ops probes and the two `adapter.wsgi` health routes get internal rows with their observed gates."
- Specification v1.1 S15 acceptance intent: "Every registered route has a catalog entry, or the route is removed; the audit mirror is produced by its owner."
- Instruction ID-1 binding reading: "Every `(method, path)` that a factory serves as endpoint behavior has exactly one catalog row", with exclusion classes (a) governed refusal, (b) alias, (c) framework-implicit only.
- Plan v1.1 §6.5 rows 5, 8, 9, 10, 11 and PD-9; rescope review v1.0 B-6 ("IF-6 … unchanged").

**State on the pull request** (`b178f03`, unchanged at `3a1b0a7`): `docs/ENDPOINTS_CATALOG.json` (symlink to `artifacts/audit/ENDPOINTS_CATALOG.json`) carries 23 rows, of which five publish the retired routes as supported `ops` records: `GET /ops/db/unavailable`; `GET /ops/probe/env`; `POST`, `HEAD`, `OPTIONS /ops/writer/diagnostic` (the POST row with `route_id: "ops.writer.diagnostic.v1"`). The routes themselves are unchanged and still mounted (`adapter/http_reader.py` lines 756, 806, 1123, 1144, 1156) and exercised by `tests/adapter/test_diagnostic_writer.py`, `tests/transport/test_ops_rails_refusal.py` and `tests/transport/test_writers_errors_headers.py`.

### 3.2 Why this is not an in-scope repair

Removing the rows changes IF-6 (an immutable Implementation Plan interface), EC-8, the IA's binding ID-1 reading and its closed exclusion classes, and therefore how acceptance (5) is read. It also bears on the Specification's S15 acceptance wording ("or the route is removed"). The instruction itself routes this case to RS-20 (ID-1; §14 first trigger), and B-6 and B-12 hold IF-6 unchanged absent a new decision. Keeping the rows instead would publish, through the governed catalog and its audit mirror, routes canon excludes from it. Neither direction is a PR-session decision.

### 3.3 Alternatives

| | Delta | Effect on S15 | Size | Assessment |
| :- | :- | :- | :- | :- |
| **(a) Canon governs: catalog-only exclusion (recommended)** | Remove the five rows (catalog 23 → 18). Add `RETIRED_PATHS` and a fail-closed validator pin ("retired route must not be cataloged"), on the precedent of the existing "GET internal dev sampler must not be cataloged" pin. Add ID-1 exclusion class (d) "canon-retired route (HDE Architecture §3.5; HDE Users Guide §1.1)" holding the nine served pairs of the three routes (GET, HEAD, OPTIONS of `/ops/db/unavailable` and `/ops/probe/env`; POST, HEAD, OPTIONS of `/ops/writer/diagnostic`), moving four framework-implicit pairs out of (c) (exclusions 30 → 35; 18 + 35 = 53 served). Retarget the existing validator-test line that edits the `/ops/probe/env` row. No route, member, test of the routes, or `success_endpoints` change | The three routes are neither catalogued nor removed. The requester reads S15 under canon (canon governs the in-flight wording; HDE Governance §9.1.2) with the exclusion stated and reasoned in the enumeration test, and the removal question left to its owner. Whether that reading is within Specification intent, or is `SPECIFICATION_CHANGE_REQUIRED`, is the IA's decision | 2 hand-edited files (`tools/evidence/generate_a7_transport_proofs.py`, `tests/http/test_endpoint_catalog.py`); 11 owner-produced files (§3.4) | Smallest canon-conforming delta; keeps WU-PR-03 "catalog entries only (no route removed)" (instruction §2 Live QA class) |
| (b) Remove the three routes | Delete the views from the blueprint and the tests, captures and documents that exercise them | Meets S15's "or the route is removed" literally | `adapter/http_reader.py` (member: re-cut and full convergence from plan §6.10 step 2); `tests/adapter/test_diagnostic_writer.py`, `tests/transport/test_ops_rails_refusal.py`, `tests/transport/test_writers_errors_headers.py`; `artifacts/proofs/writers_no_304.txt`; the ID-4 contract-inventory baseline and the architecture snapshot; S15 becomes production-affecting (Specification Live QA table: "S15 where it removes a registered route") | Contradicts EC-8 "remove none" and instruction §14's "a route that must be removed" trigger; HDE Architecture §3.5 and the Users Guide promise no removal; overlaps WU-PR-05 (S19, OBS-P3-4) |
| (c) Keep the rows | No code change; a Product Owner scoped override of HDE Architecture §3.5 for the catalog | Unchanged | none here | Needs a Product Owner decision and a PF10 overlay; publishes routes canon calls unsupported |

### 3.4 Prototype of alternative (a) (scratch worktree of `3a1b0a7`; never pushed)

- Diff: the RP-4 part of the companion file.
- Before regeneration, five tests fail as expected (the tracked catalog no longer matches the owner and the validator refuses it).
- After `HDE_WRITE_A7_PROOFS=1 python tools/evidence/generate_a7_transport_proofs.py` (plan §6.10 step 3b), then `run_canonical_json_gate.py` and `--check-only`, then `update_evidence_index.py` and `--check`, `orientation_demo.py --check`, `validate_evidence_paths.py`, `ci/checks/check_mirror_schema.sh`, `ci/checks/check_evidence_index_hash.sh`, `check_lf_endings.py`, `ci/checks/check_final_lf.sh`, `refresh_step_logs_manifest.py --check`: all exit 0.
- `tests/http/test_endpoint_catalog.py`, `tests/transport/test_a7_transport_proofs.py`, `tests/adapter/test_diagnostic_writer.py`, `tests/transport/test_ops_rails_refusal.py`, `tests/transport/test_writers_errors_headers.py`: 253 passed.
- Owner-produced changes (11): `artifacts/audit/ENDPOINTS_CATALOG.json`, `artifacts/audit/ENDPOINTS_CATALOG.json.sha256`, `docs/ENDPOINTS_CATALOG.json.sha256`; path proofs `artifacts/audit/ENDPOINTS_CATALOG.json.path_proof.txt`, `artifacts/audit/ENDPOINTS_CATALOG.json.sha256.path_proof.txt`, `docs/ENDPOINTS_CATALOG.json.path_proof.txt`, `docs/ENDPOINTS_CATALOG.json.sha256.path_proof.txt`; Mirror `artifacts/evidence_index.jsonl`, its `.sha256` and their two path proofs. `docs/evidence/INDEX.json`, the canonical JSON gate logs, the manifest and `release_id` (`72fca4c3…`) are unchanged.
- Not run in the prototype: plan §6.10 steps 6 to 10 and their second byte-stability pass, the lanes and the full sweep. RS-40 / PR-35 runs them from restart point 3b.

## 4. RP-5: the dev `GET /reader` gate's comparison

### 4.1 Evidence

**Canon on `main`:**
- HDE-CLI-API-Vendor-Ref §5.4 *Route and gate (must)*: "The route **must** be gated by `APP_ENV=dev` and bound only to a local interface … or disabled entirely."
- HDE-CLI-API-Vendor-Ref §5.6 table, `/reader`: "explicit `APP_ENV=dev`".
- HDE Schemas & Artifacts §8.8 *Reader surface routes and distinct contracts (normative)*: "explicitly gated by `APP_ENV=dev`".
- HDE Mechanics Guide §34 route table: "It requires explicit `APP_ENV=dev`".
- HDE Governance §4.1.4 *Dev/admin APP_ENV gating*: "Allowed `APP_ENV` values for these dev/admin surfaces are exactly `{"dev","test","local"}`. If `APP_ENV` is missing, empty, or any other value (including `"prod"` or any unrecognized string) … **MUST** fail closed".
- Contrast: HDE-CLI-API-Vendor-Ref §5.5 states trimming and case-folding expressly, for the compat production-posture resolution only; §5.11 says "When `APP_ENV` is exactly one of `dev`, `test`, or `local`" for the sampler, whose code (`_dev_admin_gate`) nevertheless trims and case-folds.
- PF10 is silent (front matter).

**Approved-base text:**
- Implementation Plan v1.1 §5 IF-10: "`GET /reader` … served only when `APP_ENV` is explicitly `dev`; unset, empty and every other value, including `test` and `local`, refuse with `ERR_READER_FORBIDDEN` 403".
- Instruction §9.2 (the IA's disposition rule): "Normalize the value as `_dev_admin_gate` does (strip, lower), but serve only `dev`."
- Plan v1.1 §6.2 and PD-5 follow §9.2; rescope review v1.0 B-6 keeps "The `/reader` gate design (IF-10's first part)" unchanged.

**State on the pull request:** `adapter/http_reader.py::_reader_dev_env_explicit` returns `raw_app_env is not None and raw_app_env.strip().lower() == "dev"`. `tests/http/test_reader_a7_transport.py::test_dev_reader_is_served_only_for_explicit_dev` serves `dev`, ` DEV ` and `Dev`. `docs/server/reader_v1.md` line 17 states "(surrounding whitespace and letter case ignored)".

### 4.2 Why this is routed rather than repaired

Codex's reading (exact comparison) agrees with the canon wording above and with IF-10's "every other value". The current behavior follows the IA's explicit §9.2 rule, which B-6 confirmed. Replacing a binding IA disposition on a protected security gate is not the PR session's decision. If the IA finds IF-10 and canon already require the exact comparison, `IN_SCOPE_REPAIR` returns it to PR-35 with no addendum.

### 4.3 Alternatives

| | Delta | Size | Assessment |
| :- | :- | :- | :- |
| **(a) Exact comparison (recommended)** | `_reader_dev_env_explicit` returns `os.environ.get("APP_ENV") == "dev"`. `test_dev_reader_is_served_only_for_explicit_dev` keeps `dev` only; the refusal matrix adds ` dev`, `dev `, `Dev`, `DEV`. `docs/server/reader_v1.md` line 17 reads "exactly `dev`". `_dev_admin_gate`, the sampler and conjunction routes, `VERIFY.sh` (already exact), the start helper (B-1) and the catalog `env_gate` stay unchanged | `adapter/http_reader.py` is a release member: same-version re-cut and full convergence from plan §6.10 step 2 with a second byte-stable pass; new `release_id` (prototype value `99e40e185a279da6301c94700d39d862619f62750ef7a0ad27ffc9a7cd1ec7d4`, not binding), which becomes the refresh base for WU-PR-04 and WU-PR-05 (contract E-3). Prototype after the cut: `tests/http/test_reader_a7_transport.py` and `tests/scripts/test_dev_start_reader.py` 28 passed | Fail-closed on case or whitespace misconfiguration; matches canon wording |
| (b) Keep normalization (`REJECT`) | none; PR-35 answers the Codex thread with the IA's reading and resolves it | none | Keeps a gate that serves `Dev` and ` DEV `; canon wording does not state normalization for this route |

Acceptance (2)'s refusal set and IF-10's first part are satisfied by both alternatives as written; (a) also refuses case and whitespace variants.

## 5. Impact

| Surface | RP-4 (a) | RP-5 (a) |
| :- | :- | :- |
| Requirements | S15 (catalog 18 rows; ID-1 class (d)); acceptance (5) read with class (d). S02, S07, S09, S10, S18 unaffected | S10 / IF-10 (exact `dev`); acceptance (2) unaffected in wording |
| Dependencies | none upstream; WU-PR-05 (S19; OBS-P3-4) keeps the route-exposure and removal question for the three routes | release refresh base for WU-PR-04 and WU-PR-05 changes (E-3) |
| Tests | `tests/http/test_endpoint_catalog.py` (exclusion table, one validator case retargeted, one added) | `tests/http/test_reader_a7_transport.py` (served and refused parameters) |
| Evidence | catalog family, path proofs, Mirror (11 files) via restart point 3b | full convergence from step 2 (plan §6.10; result v1.0 §5 lists the family set) |
| Ops / QA | none; S15 stays "catalog entries only (no route removed)" | none; S10 stays functional-feature for later Live QA |
| Documentation | no repository document lists the catalog rows; canon doc-delta candidates: HDE-CLI-API-Vendor-Ref §5.6 "Implementation and acceptance state", HDE Schemas & Artifacts §8.8 (population rule incl. retired routes; R-7) | `docs/server/reader_v1.md` line 17 |
| Downstream | WU-PR-04, WU-PR-05, WU-PR-08 carry the 18-row catalog and the class-(d) rule; OBS-P3-7 (step 3b after a validator change) applies | none beyond E-3 |

If both are approved, one convergence from step 2 covers both (the catalog owner runs at step 3b).

## 6. Completed valid work (preserved)

- PR-30 candidate on #643 (`7811f43`, `7f6da26`, `2d914e9`, `2d26e2b`, `b178f03`) as result v1.0 records, including the full sweep (4,747 passed) and all seven local lanes on `7f6da26`.
- PR-35 commit `3a1b0a7` (Codex P2 aliases fix; D-4 in result v1.1) with its local validation (result v1.1 §5).
- Codex code review of `2d26e2b` and `b178f03` read; three threads classified (result v1.1 §3).
- Nothing in RP-4 or RP-5 invalidates the S02, S07, S09, S18, ID-3, ID-4, RP-1 or RP-3 work.

## 7. Canon-conflict register entries (proposed)

| ID | Classification | Sources | Conflict | Affected | Alternatives / recommended | Interim | Drainage | Status |
| :- | :- | :- | :- | :- | :- | :- | :- | :- |
| CR-7 | CANON_RECONCILIATION | HDE Architecture §3.5 *Current repository discrepancy*; HDE Users Guide §1.1; vs Implementation Plan v1.1 IF-6, EC-8; instruction ID-1; plan v1.1 §6.5 rows 5, 8–11 | The in-flight documents catalogue three routes canon marks `RETIRED/NONCANONICAL` and excludes from the Endpoint Catalog | S15, acceptance (5) | (a) canon governs, catalog-only exclusion (recommended); (b) route removal; (c) Product Owner override | rows stay on the PR head until decided; the PR is not presented as merge-ready | HDE Schemas & Artifacts §8.8 population rule; HDE-CLI-API-Vendor-Ref §5.6 implementation state (Product Owner) | PROPOSED; unreviewed |
| CR-8 | CANON_RECONCILIATION | HDE-CLI-API-Vendor-Ref §5.4, §5.6; HDE Schemas & Artifacts §8.8; HDE Mechanics Guide §34; HDE Governance §4.1.4 *Dev/admin APP_ENV gating*; vs instruction §9.2, plan v1.1 §6.2, PD-5 | The instruction normalizes `APP_ENV` before comparing; canon states `APP_ENV=dev` explicitly | S10, IF-10 | (a) exact comparison (recommended); (b) keep normalization | normalization stays on the PR head until decided | none if (a); if (b), canon wording that permits normalization (Product Owner) | PROPOSED; unreviewed |

CR-1 to CR-6 are carried unchanged (CR-1 to CR-3 APPROVED_AS_CHANGED, Thoth; CR-4 APPROVED and CR-5 APPROVED_AS_CHANGED, Product Owner; CR-6 APPROVED, the IA through rescope review v1.0 §12).

## 8. Risks, exclusions, unresolved facts

- **Risk.** RP-5 (a) changes the `release_id` again; any document that recorded `72fca4c3…` as WU-PR-03's refresh base (result v1.0 §8, the pull request description) becomes historical and is superseded by the next PR-35 record.
- **Risk.** Under RP-4 (a) the three routes stay mounted by the production factory with no code-level gate (OBS-P3-4); the catalog exclusion does not change exposure.
- **Exclusions.** No route removal, member change other than RP-5 (a), updater, classifier, presenter, boundary-analyzer or frozen-family change is requested. No canon edit.
- **Unresolved.** Whether S15's wording admits the canon-retired exclusion (the IA's decision; §3.3). Hosted CI on the PR-35 push (result v1.1 ledger).

## 9. Return

`PR_RETURN_PHASE: PR-35`. On `APPROVE` for either item, RS-40 — Approved Rescope — Resume PR Implementation — 100926.1 resumes PR-35 on #643 under the original Proceed. `IN_SCOPE_REPAIR` or `REJECT` returns to PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1 under unchanged authority, with no addendum. `REVISION_REQUIRED` returns to this author through RS-30. `SPECIFICATION_CHANGE_REQUIRED` returns to Nathan. A split outcome (one decision per item) is the IA's to state; PR-35 applies whatever it decides in one coherent push.

## Canon precedence (Plan Templates, "Canon precedence for template use")

Applicable, active, non-superseded PF10 addenda supersede conflicting PF-Canon only for the exact scope they address; otherwise PF-Canon governs. A formally approved bounded Product Owner rescope may supersede conflicting PF-Canon only for the exact decision it adjudicates. Neither exists for RP-4 or RP-5.

## Canon relied on

Read on `main` at `1735d94` (`docs/pfcanon/` unchanged since `ad11821`).

| Topic | Sources and sections |
| :- | :- |
| RP-4 | HDE Architecture (`docs/pfcanon/PF02-Canon-HDE-Architecture-v2.4.6.md`, blob b0bf3d66965d) §3.5 in full; HDE Users Guide (`docs/pfcanon/PF29-Canon-HDE-Users-Guide-v1.0.2.md`, blob 6a0d4725a710) §1.1 route tables; HDE-CLI-API-Vendor-Ref (`docs/pfcanon/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.3.md`, blob 8b136def4c22) §5.6 in full; HDE Schemas & Artifacts (`docs/pfcanon/PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.6.md`, blob 1542a8f78846) §8.8 in full |
| RP-5 | HDE-CLI-API-Vendor-Ref §5.4 in full, §5.5 (production posture sentence), §5.6, §5.11 (APP_ENV gate bullets); HDE Schemas & Artifacts §8.8 *Reader surface routes and distinct contracts*; HDE Mechanics Guide (`docs/pfcanon/PF14-Canon-HDE-Mechanics-Guide-v3.5.8.md`, blob 3360a9eb1a50) §34 route table and *Current repository posture*; HDE Governance (`docs/pfcanon/PF04-Canon-HDE-Governance-v2.8.7.md`, blob 86cf613ce7f9) §4.1.4 *Dev/admin APP_ENV gating (dev/test/local only)* |
| Precedence and routing | HDE Governance §9.1.2 (canon over in-flight documents), as cited by instruction v1.0; PF10 HDE Build Notes v13.5.6 in full (precedence §1–§9; addenda 2.1–2.5); addendum record 2.6; AGENTS.md canon-first rule |
| Workflow | PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1 (https://app.notion.com/p/3f44590a05eb811ebf72e949b7b1572e; page state 2026-10-12T02:30:15Z; read in full): *Material rescope boundary*; RS-20 — Review Bounded Work-Unit Rescope — 100926.1 (https://app.notion.com/p/3f44590a05eb81be9566cd6397c9424c; page state 2026-10-12T02:29:57Z; read in full): *Required inputs*; skill `glow-hde-pr-development` 1.4.0 |
| In-flight documents | Specification v1.1 rows S10, S15 and the Live QA table; Implementation Plan v1.1 §5 IF-6, IF-10; instruction v1.0 §2, §4 (EC-8, ID-1), §9.2, §13, §14; plan v1.1 §6.2, §6.5, §6.10, §14, §15; rescope review v1.0 §7 (B-6, B-12) |

## Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / WU-PR-03 / PR-35 / rescope request 2 (PR-35), version 1.0 |
| change / specification | CRD HDE-CRD-0002 / `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` v1.1 |
| work unit | WU-PR-03 (S02, S07, S09, S10, S15, S18) |
| release | GCFPE-20261009.1 / 100926.1 |
| prompt | PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1 (page state 2026-10-12T02:30:15Z) |
| role/stage | dedicated WU-PR-03 PR-35 session / review correction |
| capture time | 2026-10-14T04:00:00Z |
| execution identity | https://claude.ai/code/session_0136SjBtuTJwoEpceUd46T6C |
| repository persistence | recorded here only (`docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent; pending, non-gating; owner the Product Owner) |
