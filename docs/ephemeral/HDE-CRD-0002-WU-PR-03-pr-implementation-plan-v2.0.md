---
artifact_type: PR_IMPLEMENTATION_PLAN
artifact_id: HDE-CRD-0002-WU-PR-03-PR-IMPLEMENTATION-PLAN
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-implementation-plan-v2.0.md
artifact_version: "2.0"
artifact_state: AWAITING_PO_PROCEED
hold_label: "ASK OK? — PR IMPLEMENTATION PLAN"
plan_cycle: 2, the corrective cycle the Product Owner directed on 2026-10-14 for the merged, not-yet-accepted WU-PR-03 (#643). Entry is the corrective architecture decision record and PF10 addendum 2.7, not a PR-40 REJECT; no separate PR-40 review of #643 alone runs first (decision record §5)
predecessor: docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-implementation-plan-v1.1.md (v1.1; blob 1e18046e5bd4; 91,547 bytes; the plan of cycle 1, Proceeded once and spent; landed as amthorn78/glow-hdengine-v2#643, squash c98d41f). Plan v1.0, its prototype diff and v1.1 are preserved unchanged. This v2.0 plans only the corrective delta; cycle 1's delivered scope is landed history and stands
companion: docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-implementation-plan-v2.0-prototype.diff (new; the 7 hand-edited files of §7.1 as prototyped against 79eac95; §4.5)
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-03
work_unit_title: "Public, dev and CLI surfaces (PR; Conjunction; S02, S07, S09, S10, S15, S18)"
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-instruction-v1.0.md (v1.0, INSTRUCTION_READY; blob 74e8f158b48d; unchanged; overlaid by PF10 addenda 2.6 and 2.7 for the clauses they name)
IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (v1.1; blob abffa2ccbd44; immutable)
PLAN_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (v1.1, IA-30 INITIAL_APPROVE, "ASK OK."; blob 0cc0276524b2)
SPECIFICATION_ID: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (v1.1, SPECIFICATION_APPROVED, "ASK OK."; blob c4802a5a7fa3; not edited)
IMPLEMENTATION_AUDIT_ID: docs/ephemeral/HDE-CRD-0002-implementation-audit-v1.0.md (v1.0, AUDIT_COMPLETE; blob b39ac9f276db) — lineage only
CORRECTIVE_DECISION_RECORD_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-03-corrective-architecture-decisions-v1.0.md (v1.0, COMPLETE; blob e35ec2cc4858; Product Owner-directed decisions AD-1 to AD-6; CR-7 and CR-8 APPROVED, alternative (a))
cycle_1_records: PR-30 result docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-implementation-result-v1.0.md (v1.0, PR_CANDIDATE_PUBLISHED; blob fdc2f792315f); PR-35 result docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-implementation-result-v1.1.md (v1.1, RESCOPE_PENDING; historical; blob b72e57020353); PR-35 rescope request docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr35-rescope-request-v1.0.md (blob 471368c500ca) and its prototype diff (blob 90729930fa62); PR-35 rescope review docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr35-rescope-review-v1.0.md (RS-20, SPECIFICATION_CHANGE_REQUIRED; blob 36af6af0cadb)
RESCOPE_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-03-rescope-review-v1.0.md (v1.0, RS-20, APPROVE, B-1 to B-12; blob e3f50f162130; cycle 1, carried through addendum 2.6)
REMEDIATION_REVIEW_ID: none
AUTHORING_CONTEXT: APPROVED_BASE_WITH_OVERLAYS
immutable_approved_base: Specification v1.1 (approved) → Implementation Plan v1.1 + review v1.1 (approved) → PR instruction v1.0 (issued by the IA under PR-10). None is rewritten
applicable_pf10_overlays: PF10 addendum 2.2 (its WU-PR-03 downstream item and binding requirements for the contract-inventory generator, ID-4); 2.3 (reviewer chain without the Codex security review); 2.5 (carried LR-O1 to LR-O3); 2.6 (start-helper propagation, 22-path label roster, step 3b), superseded by 2.7 only where 2.7's "Overlaid base clauses" says so; 2.7 (AD-1 to AD-6, the overlaid clauses and the binding requirements of this corrective cycle). Addendum 2.1 governs §21 only. Addendum 2.4 is a WU-PR-01 record
effective_baseline: approved base + applicable PF10 overlays = the base above + addenda 2.2, 2.3, 2.5, 2.6 and 2.7 (§5A)
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.8.md (v13.5.8, effective 2026.10.14; blob 3c13456a576c; 103,474 bytes; sha256 94573d06200935fdd29c71b04bafd2035c69b9d0537d1e4f69d9e7f02fe27eb6; one unlettered document; addenda 2.1 to 2.7; resolved afresh on main 79eac95 and read in full: front matter §§1–9, cross-references, template, index, addenda 2.1 to 2.7). Addendum 2.7 is published there, so it governs over its docs/ephemeral/ record (handoff instruction); the published text and the record agree item by item (§3)
pf10_addendum_paths: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.8.md §2.2, §2.3, §2.5, §2.6, §2.7 (records docs/ephemeral/HDE-CRD-0002-WU-PR-03-PF10-build-notes-addendum-v1.0.md for 2.6 and docs/ephemeral/HDE-CRD-0002-WU-PR-03-corrective-PF10-build-notes-addendum-v1.0.md for 2.7); §2.1 for §21
pf10_addendum_created: none (PR-20 is not a qualifying approval prompt)
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
session_disposition: INITIAL_DEDICATED_ASSIGNMENT (a new top-level dedicated WU-PR-03 PR engineering session for plan cycle 2, created by Nathan / Product Owner; the last known WU-PR-03 planning session https://claude.ai/code/session_01GC6jqu4Lczzk7PR7QGXSTJ was not reused)
role_session_ref: NOT_YET_ASSIGNED (assignment owner Nathan / Product Owner); authoring session https://claude.ai/code/session_0186RTKAbX7HsgFuEgBB1fE8
author: dedicated HDE-CRD-0002 WU-PR-03 PR engineering session (PR-20, plan cycle 2)
return_owner: the continuing whole-change HDE-CRD-0002 Implementation Agent (PR-40 across #643 and the corrective pull request, after the merge; RS-20 for any rescope; PR-10 for an instruction defect)
prompt: PR-20 — Create Detailed PR Implementation Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb819fbea5dcd966a750ba; page state as of 2026-10-12T02:29:47Z; read in full)
prompt_release: GCFPE-20261009.1 / 100926.1
created_at: 2026-10-14T06:35:55Z
repository_baseline: origin/main 79eac952edbed9e31c3c6ab98528196b81ae69a8 (tree e6e17c0717c4; Product Owner commit "PF10 update" over #644 at 41069c2). git diff c98d41f..79eac95 touches only docs/ephemeral/ (five records of #644) and docs/pfcanon/ (PF10 v13.5.7 → v13.5.8), so every code, tool, test and evidence fact of #643's merge holds here
vehicle_state: amthorn78/glow-hdengine-v2#643 merged 2026-10-14T04:41:15Z as squash c98d41f (head dc45a35); Codex P1 threads PRRT_kwDOP103ks6sJ4Y8 (RP-5) and PRRT_kwDOP103ks6sJ4Y_ (RP-4) open, P2 thread PRRT_kwDOP103ks6sJ2D_ resolved; #644 merged 2026-10-14T05:08:51Z as 41069c2. No open pull request in the repository at authoring time (GitHub listing, state open: none). No Proceed, branch or pull request exists for the corrective work; PR_RETURN_PHASE does not apply
canon_conflict_register: CR-1, CR-2, CR-3 APPROVED_AS_CHANGED (Thoth); CR-4 APPROVED and CR-5 APPROVED_AS_CHANGED (Product Owner); CR-6 APPROVED (the IA, rescope review v1.0 §12); CR-7 and CR-8 APPROVED, alternative (a) each (Product Owner direction of 2026-10-14; decision record §6; addendum 2.7) (§16)
next_prompt: PR-30 — PR Implementation Proceed — 100926.1 (https://app.notion.com/p/3f44590a05eb8148a538f5c80588db14), on Nathan's Proceed for this exact plan
---

# HDE-CRD-0002 WU-PR-03 — Detailed PR Implementation Plan v2.0 (corrective, plan cycle 2)

Canon precedence rule for this derived artifact (Plan Templates, "Canon precedence for template use"): Applicable, active, non-superseded PF10 addenda supersede conflicting PF-Canon only for the exact scope they address; otherwise follow PF-Canon. A formally approved bounded Product Owner rescope may supersede conflicting PF-Canon only for the exact decision it adjudicates.

## 1. State and authority

**AWAITING_PO_PROCEED.** Held at `ASK OK? — PR IMPLEMENTATION PLAN` (HDE Governance §9.1.1).

This is the complete, executable corrective plan for WU-PR-03. It plans only the delta from `main` that PF10 addendum 2.7 decides:
- **AD-1.** The Endpoint Catalog drops the five records of the three canon-retired routes (23 → 18). The catalog owner's validator refuses them, fail-closed. The route-enumeration test gains exclusion class (d).
- **AD-2.** The dev `GET`/`HEAD /reader` gate compares `APP_ENV` exactly with `dev`.
- **AD-3.** The canonical dev runner binds `127.0.0.1` with the debugger and reloader off and emits no CORS header, proved by tests; the start helper's banner names the host.
- **AD-5.** One same-version re-cut, because AD-2 and AD-3 change the release member `adapter/http_reader.py`, and the convergence through the owners.
- **AD-6.** The canon trace is a deliverable: this plan carries it (§17), the result record repeats it, and the enumeration test records each exclusion's class and basis.

AD-4 is out of WU-PR-03 by decision (§18).

**What #643 delivered stands** (§4.1): S02, S07, S09, S18, ID-3, ID-4, the RP-1 start-helper propagation, the RP-3 22-path label roster, and every other part of S10 and S15. The corrective pull request changes them only where a decision above says so.

**Prototype.** The whole delta was built and run in a scratch clone of `79eac95` (§4.4):
- the cut and two convergence passes, byte-identical;
- the classifier-selected lanes, the attestation, `VERIFY.sh` and the full `tests/` sweep;
- red controls proving that the new tests fail on the old code.

The companion diff carries the hand-edited part (§4.5).

Authority:
- Only Nathan's `PR Implementation Proceed` (PR-30) for exactly `docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-implementation-plan-v2.0.md` (v2.0) authorizes implementation. It is a new Proceed for plan cycle 2; cycle 1's Proceed (plan v1.1) is spent.
- Only Nathan merges. #643 is merged history and is not resumed, reused or pushed to.
- This plan authorizes no implementation, merge, publication, Ops, QA, acceptance or closure. It changes no canon, no Specification, and creates no PF10 addendum.

## 2. Identity and lineage

| Item | Identity |
| :- | :- |
| Change | CRD HDE-CRD-0002 |
| Work unit | WU-PR-03 (Plan v1.1 §7 "WU-PR-03 — Public, dev and CLI surfaces (PR; Conjunction)") |
| Requirements corrected | S10 (exact gate; loopback runner), S15 (canon-read population); S09's canonical runner meets the harness profile. S02, S07, S18 unchanged (addendum 2.7 "Affected surfaces") |
| Decisions applied | AD-1, AD-2, AD-3, AD-5, AD-6 (addendum 2.7; decision record §3, §4). AD-4 outside the unit |
| Cycle 1 | plan v1.1 (spent) → #643 (squash `c98d41f`) → result v1.0 (`PR_CANDIDATE_PUBLISHED`) → result v1.1 (`RESCOPE_PENDING`, historical) → PR-35 rescope request v1.0 → PR-35 rescope review v1.0 (`SPECIFICATION_CHANGE_REQUIRED`) → Product Owner direction → decision record v1.0 and addendum 2.7 (published in PF10 v13.5.8) |
| Cycle 2 | this plan v2.0 → Proceed → PR-30 (result v2.0) → PR-35 (results v2.1 onward) → Nathan's merge → PR-40 by the IA across #643 then the corrective pull request |
| Upstream units | WU-PR-01 accepted (addendum 2.4); WU-PR-02 accepted (addendum 2.5) |
| Downstream | WU-PR-04 and WU-PR-05 refresh from this cycle's `release_id`; WU-PR-05 (S19) receives AD-4's four gaps; WU-PR-08 (S17) describes the loopback bind; WU-DOC-01 states the start command and bind (decision record §7). They wait on PR-40's decision across both pull requests |
| Phase | Conjunction |
| Live QA class | S02, S07, S10 functional-feature; S15 catalog entries only (no route removed); S09, S18 not production-affecting (Specification table; Plan §6; unchanged by 2.7) |

## 3. Sources read

Read completely by this session, on `main` at `79eac95`:
- PR-20 — Create Detailed PR Implementation Plan — 100926.1 (Notion, page state 2026-10-12T02:29:47Z).
- PF10 v13.5.8 in full. Addendum 2.7 as published was compared with its `docs/ephemeral/` record: the same sections, decisions, overlaid clauses, binding requirements and evidence, with formatting differences only (PF10 renders `#643` as a link and strips code spans). The record's front matter adds provenance only.
- The corrective decision record v1.0, the addendum record 2.7 and the handoff file.
- The PR-35 rescope request v1.0 and its prototype diff; the PR-35 rescope review v1.0.
- Plan v1.1; results v1.0 and v1.1; instruction v1.0 (all 20 sections); rescope review v1.0 (B-1 to B-12).
- Implementation Plan v1.1 (in full); its review v1.1; Specification v1.1 (approved representation, in full).
- Canon sections, each in full, as listed in "Canon relied on".
- Code and data at `79eac95`:
  - `adapter/http_reader.py` (the gate, `get_reader_bp`, `create_app`, the `__main__` block), `adapter/factory.py` and `adapter/wsgi.py` (`url_map`);
  - `tools/evidence/generate_a7_transport_proofs.py` (`catalog_obj`, `validate_catalog`);
  - `tools/evidence/hdapi_v2_boundary_analyzer.py` (`discover_route_registrations`, `_public_route_pass_state`) and the generator's baseline;
  - `ci/checks/classify_ci_changes.py` (`_HTTP_READER_TEST_OWNERS`, `_WORKFLOW_CONTROL_PATH_LANES`, `_PRODUCT_TEST_OWNER_PATHS`) and `.github/workflows/ci.yml` (every lane step);
  - `scripts/dev_start_reader.sh`, `VERIFY.sh`, `scripts/qa/dev_sampler_healthcheck.py`, `docs/server/reader_v1.md`, `docs/acceptance/reader_a7_crib.md`, `docs/RUN.md`, `ARCHITECTURE.md` "Routing and mounts", `pytest.ini`, `requirements*.txt`;
  - Flask 2.3.3 `Flask.run` (installed source).
- Tests at `79eac95`: `tests/http/test_endpoint_catalog.py`, `tests/http/test_reader_a7_transport.py`, `tests/scripts/test_dev_start_reader.py`, `tests/scripts/test_dev_sampler_healthcheck.py`.
- GitHub: #643's three review threads (states above); the open and recent pull-request listings.

Consulted in part: WU-PR-02 plan v2.0 (front matter and §8 to §20, as the structure precedent for a corrective cycle); `run_flask.py`, `run_flask_dev.sh` and `FLASK_AUTO_RUN_GUIDE.md` (F-28).

## 4. Repository baseline (verified at `79eac95`)

### 4.1 What #643 landed and still holds

Per addendum 2.7 "Base and what landed" and result v1.0 §4 to §8, verified on `main`:
- S02: the governed not-found envelope on all three factories;
- S07: the help text;
- S09: the harness retirement and the `VERIFY.sh` repoint;
- S10: the request-time `/reader` gate;
- S15: a 23-record catalog with the Aux record and its validator;
- S18: the document corrections;
- ID-3: the classifier registrations; ID-4: the contract-inventory baseline;
- the start-helper propagation (RP-1) and the 22-path label roster (RP-3);
- the refresh with `release_id` `72fca4c341d871dc75a828140ee1494714b322a13656bac93f66164060ea390f`.

`git diff c98d41f 79eac95` outside `docs/ephemeral/` and `docs/pfcanon/` is empty.

### 4.2 The corrective targets, re-measured at `79eac95`

| ID | Fact | Decision |
| :- | :- | :- |
| F-15 | The three factories serve 53 distinct `(path, method)` pairs. The catalog holds 23 records, no catalogued pair is unserved, and `success_endpoints` is `[GET /reader]`. Nine served pairs belong to canon-retired routes: `GET`, `HEAD`, `OPTIONS` of `/ops/db/unavailable` and `/ops/probe/env`, and `POST`, `HEAD`, `OPTIONS` of `/ops/writer/diagnostic`. Five of them are catalogued: `GET /ops/db/unavailable`, `GET /ops/probe/env`, `POST`, `HEAD` and `OPTIONS /ops/writer/diagnostic`. The test's exclusion table holds 30 pairs, four of them retired-route `HEAD`/`OPTIONS` pairs in class (c) | AD-1 |
| F-16 | `adapter/http_reader.py::_reader_dev_env_explicit` (lines 378–384) returns `raw_app_env is not None and raw_app_env.strip().lower() == "dev"`. `reader_v1` validates `v` first (lines 609–611), then gates (line 612) | AD-2 |
| F-17 | The `__main__` block (lines 1239–1242) runs `create_app().run(host="0.0.0.0", port=int(os.environ.get("PORT","8000")))`, with no `debug`, `use_debugger` or `use_reloader` argument. No module under `adapter/` or `engine/http/` names CORS or an `Access-Control-*` header. `scripts/dev_start_reader.sh` line 23 prints `(host=0.0.0.0)` | AD-3 |
| F-18 | Flask 2.3.3 `Flask.run`: an explicit `debug` argument overrides `FLASK_DEBUG`; `use_reloader` and `use_debugger` default to the app's debug state; `load_dotenv` defaults to true and is a no-op unless `python-dotenv` is installed. `python-dotenv` is absent from CI's install and from `requirements*.txt`, and no `.env` or `.flaskenv` is tracked | AD-3 (why the flags are explicit); OBS-P3-14 |
| F-19 | `scripts/qa/dev_sampler_healthcheck.py` also starts `python -m adapter.http_reader` and waits on the host of `DEV_SAMPLER_URL`. Its test (`tests/scripts/test_dev_sampler_healthcheck.py`) uses `127.0.0.1`, so the loopback bind keeps it working. Its line-129 comment ("Reader runner binds to 0.0.0.0") becomes stale. `.devcontainer/devcontainer.json` already uses `127.0.0.1` (HDE Mechanics Guide §34) | AD-3; OBS-P3-13 |
| F-20 | `docs/RUN.md` line 5 states that the runner "binds `0.0.0.0`". It is outside the decided documents and becomes stale | OBS-P3-12 |
| F-21 | The env-gate proof `artifacts/proofs/endpoints_env_gate_proof.log` records `APP_ENV=prod` with `/reader_success_unreachable=true`; AD-2 does not change it | AD-2, AD-4 |
| F-22 | The contract-inventory baseline (ID-4) records route and app-handler registrations only. The `__main__` run call and the gate body are neither, so the baseline stays equal to the discovered records | ID-4 unchanged |
| F-28 | Two tracked root helpers, `run_flask.py` and `run_flask_dev.sh` (documented by `FLASK_AUTO_RUN_GUIDE.md`), run the production factory `adapter.factory:create_app` with `FLASK_DEBUG=1`, the debugger on and `use_reloader=True`, bound by default to `127.0.0.1` (`FLASK_RUN_HOST` overrides it). HDE Architecture §3.8.1 "Current repository discrepancy" says these helpers do not satisfy the dedicated-harness contract. They are not the canonical runner, which is the one AD-3 binds | OBS-P3-17; not changed |

### 4.3 Facts this session established in the prototype

| ID | Fact | Effect |
| :- | :- | :- |
| F-23 | With the corrective design, discovered public route records = 23 = the tracked baseline, `pprint.pformat` byte-equal | `tools/evidence/generate_hdapi_v2_contract_inventory.py` stays unchanged (decision record §4) |
| F-24 | The classifier on the 68 prototype paths (7 hand-edited, 61 owner-produced) selects `product`, `compat`, `db`, `evidence`, `release`, with `changed_tests=true` and 20 targets. It does not select `rails` or `qa`, because the classifier itself does not change in this cycle | §10, §11 CI cost |
| F-25 | `ci/checks/check_mirror_schema.sh` is a Python script (`#!/usr/bin/env python3`). Run with `bash`, it fails with exit 2 and writes nothing. `ci.yml` invokes it by path. This session's first convergence pass made that harness error once; the direct run then exited 0 on the same state, and pass 2 invoked it by path | §6.5 note (the same lesson as WU-PR-02 P-8) |
| F-26 | `adapter/http_reader.py::create_app`'s after-request hook runs on every response; its two branches never match, because a Flask response has no `request` attribute (cycle 1 F-5). The red control in §4.4 injected a second after-request hook into `create_app`, and it fired on every response. Addendum 2.7 AD-4 item 4 and decision record §7 say the hook "never fires" | Precision note for the WU-PR-05 instruction (OBS-P3-15); no change here |
| F-27 | `runpy.run_module(<module>, run_name="__main__")`, with `flask.Flask.run` monkeypatched to record its arguments, executes the real `__main__` block in-process without serving. Python warns once when the module is already imported; the test filters exactly that warning | §6.4 runner-profile test |

### 4.4 Prototype (this session; scratch only, never pushed)

**Environment.**
- A separate scratch clone of `79eac95` in the session scratchpad, not a worktree of the session's repository.
- CPython 3.12.3 venv with CI's install (`setuptools>=68`, `wheel`, `requirements.txt`, `requirements-dev.txt`, `-e .`). Readiness: `python -m pytest --version` → `pytest 8.4.2`.
- `ruby` 3.3.6 at `/usr/local/bin/ruby`, `bash`, `curl`.
- Closed rails: `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`; vendor, geocode, database and `GH_TOKEN` variables unset.

**Hand edits** (§7.1; the companion diff): 7 files, 111 insertions and 29 deletions.

**Before the cut** (member bytes final, manifest not cut): `tests/http/test_reader_a7_transport.py` gave 27 passed. Its seams avoid the admission dependency.

**Red controls:**
- RC-1: with `adapter/http_reader.py` restored to `79eac95` and the new tests kept, 7 failed:
  - the refusal cases ` dev`, `dev `, ` DEV `, `Dev`, `DEV` (served by the normalizing gate);
  - both runner-profile cases (`host="0.0.0.0"` and no flags).
- RC-2: with an after-request hook that sets `Access-Control-Allow-Origin: *` injected into `create_app`, all 6 CORS-absence cases failed.
- In both cases the file was restored and the diff re-checked.

**Re-cut and convergence** (§6.5 order; the script ran steps 2 and 3 once, then steps 3 to 10 in each pass):
- Cut: `release_id` `d84d99e1f2ffd1f97157097302e6480a4abfc04ae70c3b54dfd9283d8eae68c7` (`1.3.0`, 45 members). One manifest row changes, `adapter/http_reader.py`. The recompute and the cutter `--check` exit 0.
- Pass 1 (with the cut): 35 of 36 runs exit 0. The exception is the F-25 harness error. A direct run of `check_mirror_schema.sh` on the pass-1 state then exits 0.
- Pass 2: 33 of 33 runs exit 0.
- Both passes leave 61 changed paths with the same `git diff HEAD` digest, `a6fd148b7beba528ba0e38b0801f4212715e292209c06008f1847b5f4ac608b5`.
- Sanity: `summary:PASS` in both passes.
- The open-rails fixture digest becomes `06611525045515c29b7dc4dee50b9906dce8053726a642a5de9050ce5d01613c` in both passes.
- These two values are rehearsal values. PR-30's bytes fix the real ones. If PR-30 applies the companion diff's `adapter/http_reader.py` hunks unchanged, the cut reproduces `d84d99e1…`.

**After convergence:**
- the catalog has 18 records, `cmp` equal to its mirror, and the docs path is still a symlink (mode 120000);
- the 27 labelled Mirror rows (the 22 roster paths) all carry `d84d99e1…`;
- the purity-report row has no `notes`;
- the step-11 sweep finds no hit for `72fca4c3` or `64553c25` outside the excluded prefixes.

**Validation:** §10, results in "Checks run by this session".

### 4.5 Prototype diff (companion file)

`docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-implementation-plan-v2.0-prototype.diff` is the prototype's diff from `79eac95`, restricted to the 7 hand-edited files of §7.1. The manifest, the constant and every regenerated governed artifact are excluded: PR-30 produces them with their owners. `git apply --check` succeeds on `79eac95`.

PR-30 may apply it as its starting point, but it owns the implementation:
- it re-reads every hunk against §6;
- it re-runs §10 on the real branch;
- where the diff and this plan differ, this plan governs and the difference is a defect PR-30 corrects and records.

## 5. Scope (the corrective delta only)

In scope (addendum 2.7 "Scope, exclusions and nonclaims", "Changed"; decision record §4):
- **AD-1:** in `tools/evidence/generate_a7_transport_proofs.py`, the five records out, the canon-retired path set and the validator pin in. In `tests/http/test_endpoint_catalog.py`, exclusion class (d) with nine pairs and its basis, the retargeted validator case and the retired-pin case.
- **AD-2:** in `adapter/http_reader.py` (member), the exact comparison. In `tests/http/test_reader_a7_transport.py`, served `dev` only and the extended refusal matrix.
- **AD-3:**
  - `adapter/http_reader.py`'s run call;
  - `scripts/dev_start_reader.sh`'s banner host text;
  - the runner-profile and CORS-absence tests in `tests/http/test_reader_a7_transport.py`;
  - one banner assertion in `tests/scripts/test_dev_start_reader.py`.
- **AD-2 and AD-3 documents:** `docs/server/reader_v1.md` lines 17 and 19.
- **AD-5:** the same-version re-cut of `catalog/manifest.json` by the cutter, and every evidence family the refresh regenerates, by its owner.
- **AD-6:** the canon trace in this plan (§17) and in the result record; the class-and-basis record in the enumeration test.
- The PR result records under `docs/ephemeral/`.

Out of scope:
- **AD-4's four gaps** (WU-PR-05, S19), and every route or factory change. No route is added, removed, renamed or re-gated other than the `/reader` comparison.
- No public contract, payload, flag or transport change.
- No production factory change, no `Procfile` change.
- No Specification edit, no canon edit, no PF10 addendum.
- No admission-constant or version change.
- No change to `adapter/factory.py`, `adapter/wsgi.py`, `engine/http/compat_handler.py`, `engine/presenter/**` or `engine/cli/main.py`.
- No change to `engine/config/registry_loader.py`, `tools/evidence/update_evidence_index.py`, `tools/evidence/hdapi_v2_boundary_analyzer.py`, `tools/evidence/generate_hdapi_v2_contract_inventory.py` or `ci/checks/classify_ci_changes.py`.
- No change to `VERIFY.sh`, `.github/workflows/ci.yml`, `docs/acceptance/reader_a7_crib.md`, `docs/RUN.md`, `ARCHITECTURE.md`, `AGENTS.md`, `README.md` or `CHANGELOG.md`.
- No frozen family, no `artifacts/architecture/**`.
- No hand edit of any governed artifact.
- No skipped, deselected, `xfail`-marked or quarantined test. Closed rails throughout.
- Anything already delivered by #643 and not named by a decision above.

## 5A. Applied overlay (addendum 2.7): binding requirements and overlaid clauses

### 5A.1 Binding-requirement map

| Binding requirement (addendum 2.7) | Where this plan carries it |
| :- | :- |
| Catalog: 18 records, none for a canon-retired path | §6.1; §9 (5); §12 |
| The validator refuses a canon-retired record | §6.1 (pin); §6.2 (retired-pin test) |
| The enumeration test accounts for all served pairs, 18 + 35 = 53 (or the then-current count), with the arithmetic stated | §6.2; §12 states the arithmetic at the PR head |
| Exact gate: the served test admits exactly `dev` | §6.3 |
| The refusal matrix includes unset, empty, ` dev`, `dev `, `Dev`, `DEV`, `test`, `local`, `prod`, `production`, `live` and an arbitrary value | §6.3 (16 values, a superset) |
| `docs/server/reader_v1.md` states "exactly `dev`" | §6.6 |
| The run call carries `host="127.0.0.1"`, `debug=False`, `use_debugger=False`, `use_reloader=False` | §6.4; the runner-profile test |
| A test proves no `Access-Control-*` header on a dev-runner `GET /reader`, an `OPTIONS` preflight with `Origin` and `Access-Control-Request-Method`, and an error response | §6.4 (6 cases, including three errors) |
| `scripts/dev_start_reader.sh` and `docs/server/reader_v1.md` name host `127.0.0.1` | §6.4, §6.6 |
| The start-helper owner test and `VERIFY.sh` pass on the loopback bind | §10 items 2, 9 and 11 |
| Governed families produced by their owners only; frozen families keep their bytes | §6.5; §7.2; §10 item 7 |
| The contract-inventory baseline still equals the discovered records | §6.7 (F-23); §10 item 2 |
| The architecture snapshot test stays green | §10 item 3 (product lane) |
| The full `tests/` sweep passes under closed rails | §10 item 11 |
| The two convergence passes are byte-identical | §6.5; §12 |
| The release attestation builds and verifies | §10 item 8 |
| No test is skipped, deselected, marked expected-failure or quarantined | §5; §10 |
| AD-6: the plan and result record map each decision and each touched route to canon | §17; §12 |

### 5A.2 Overlaid base clauses as they now read for WU-PR-03 (addendum 2.7, verbatim; every other word of each clause holds)

| Base clause | Now reads |
| :- | :- |
| Implementation Plan v1.1 §5 IF-6: the internal rows for `/ops/db/unavailable`, `/ops/probe/env` and `/ops/writer/diagnostic` | withdrawn (AD-1) |
| Audit EC-8 (instruction §4): "Catalog every registered route; remove none" | "Catalog every registered route that canon does not retire; remove none" |
| Instruction ID-1 binding reading and its exclusion classes (a) to (c) | classes (a) to (d) as AD-1 states |
| Instruction §9.2: "Normalize the value as `_dev_admin_gate` does (strip, lower), but serve only `dev`" | "Compare the raw value exactly; serve only `dev`" (AD-2) |
| Instruction §7: "No change to the `0.0.0.0` bind or to the production mount of the gated dev blueprint" | the bind is changed by AD-3; the production mount stays excluded (AD-4) |
| Build Notes 2.6 approved delta item 1 and its binding requirement that `scripts/dev_start_reader.sh` has an empty diff | the script changes in its banner's host text only (AD-3); `APP_ENV` propagation is unchanged |
| WU-PR-03 detailed plan v1.1 §6.2 and PD-5 (normalization), and §6.5 records 5 and 8 to 11 | superseded by AD-2 and AD-1 |

**Readings carried from addendum 2.6** (not overlaid by 2.7):
- B-2's clauses (IF-10's last clause, acceptance (2)'s last clause, E-6) stand.
- So does the `VERIFY.sh` refusal (B-3), and B-7's one-line roster deletion is already landed.
- The 2.6 binding requirement "git diff from base to head is empty for `scripts/dev_start_reader.sh`" is replaced, for this cycle, by "exactly the one banner line" (§10 item 12).

**Acceptance (5)** reads under ID-1 classes (a) to (d): "Every `(method, path)` rule of the three factories has a catalog row" means a row, or exactly one reasoned exclusion in classes (a) to (d) (2.7 "S15 reading").

## 6. Design

### 6.1 AD-1 — the catalog owner (`tools/evidence/generate_a7_transport_proofs.py`)

**The canon-retired path set.** After the `AUX_PATH` line, add:

```python
# PF02 §3.5 "Current repository discrepancy" and PF29 §1.1: checked-in routes canon marks
# RETIRED/NONCANONICAL and excludes from the Endpoint Catalog (HDE-CRD-0002 AD-1).
CANON_RETIRED_PATHS={'/ops/db/unavailable','/ops/probe/env','/ops/writer/diagnostic'}
```

It is a module constant, so the enumeration test imports it (PD-25). The canon-retired set therefore has one home, the catalog owner. HDE Architecture's Endpoint Catalog routing note forbids derived inventories from hard-coding a second inventory.

**Records.** Remove exactly the five records of `catalog_obj()` whose `path` is in that set:
- `GET /ops/db/unavailable`;
- `GET /ops/probe/env`;
- `POST /ops/writer/diagnostic` (with `route_id`);
- `HEAD` and `OPTIONS /ops/writer/diagnostic`.

The other 18 records keep their bytes and order:
- `/ops/rails/refusal` `GET` and `POST`, an adopted route (HDE Architecture §3.5);
- `/internal/healthz` and `/internal/readyz`, which no canon retires (2.7 AD-1 "Unchanged").

`success_endpoints` stays `[GET /reader]`. `generated_at_utc` stays the manifest's `built_at_utc`.

**Validator pin.** After the "aliases only on the aux record" check, add:

```python
 if any(p in CANON_RETIRED_PATHS for e in cat['endpoints'] for p in [e['path'],*e.get('aliases',[])]): raise ValueError('canon-retired route must not be cataloged')
```

It refuses a canon-retired path as a record path or as an alias (PD-25). Every other check is unchanged, including `CLASS`, the Aux pin, the sampler pin, the production Reader pin and the success designation.

**Routes.** No route changes. The three retired routes stay mounted and behave as before. Their production exposure is AD-4's, in WU-PR-05.

### 6.2 AD-1 and AD-6 — the enumeration and validator tests (`tests/http/test_endpoint_catalog.py`)

**Import.** `from tools.evidence.generate_a7_transport_proofs import CANON_RETIRED_PATHS, catalog_obj, validate_catalog`.

**Class and basis as data (AD-6).** The comment that described classes (a) to (c) becomes data the test checks (PD-26):

```python
_GOVERNED_REFUSAL = "a"
_ALIAS = "b"
_FRAMEWORK_IMPLICIT = "c"
_CANON_RETIRED = "d"
_EXCLUSION_BASIS = {
    _GOVERNED_REFUSAL: 'governed refusal of a catalogued record: PF05 §5.4 "Production mount"; '
    'PF12 §8.8 "Reader surface routes and distinct contracts"',
    _ALIAS: 'alias spelling of a canonical record, carried by its aliases: PF05 §5.6',
    _FRAMEWORK_IMPLICIT: "a method Flask adds automatically (HEAD for a GET view; OPTIONS) "
    "whose behavior neither PF05 §5.6 nor the route's own view defines",
    _CANON_RETIRED: 'canon-retired route, excluded from the Endpoint Catalog: PF02 §3.5 '
    '"Current repository discrepancy"; PF29 §1.1 "Checked-in retired/noncanonical route drift"',
}
```

**Exclusion table.**
- In class (c), the `HEAD`/`OPTIONS` pairs of `/ops/db/unavailable` and `/ops/probe/env` leave.
- Class (d) gets nine pairs:
  - `GET`, `HEAD`, `OPTIONS` of `/ops/db/unavailable` and of `/ops/probe/env`;
  - `HEAD`, `OPTIONS`, `POST` of `/ops/writer/diagnostic`.
- Classes (a) and (b) are unchanged.
- The table holds 35 pairs: (a) 7, (b) 1, (c) 18, (d) 9.

**Enumeration test.** `test_every_served_pair_has_one_catalog_row_or_a_reasoned_exclusion` keeps its four assertions and the Aux alias check. It adds (PD-27):
- `len(served) == len(catalogued) + len(excluded)`: the arithmetic, 18 + 35 = 53 at the prototype head;
- every excluded pair's class has a non-empty basis: "a served pair with no recorded posture … fails";
- the class-(d) pairs equal exactly the served pairs whose path is in `CANON_RETIRED_PATHS`. A retired pair can be neither catalogued nor left in another class, and a class-(d) pair cannot name an adopted route;
- no catalogued path is in `CANON_RETIRED_PATHS`: "a record for a canon-retired path … fails". The tracked-catalog validation in `test_endpoint_catalog_schema_is_strict_and_valid` proves it again.

**Validator tests** (PD-28):
- In `test_validator_rejects_aliases_off_the_aux_record_and_alias_collisions`, the case that reclassified the `/ops/probe/env` record now edits `/internal/healthz`, a record that stays. The other three cases are unchanged.
- A new `test_validator_refuses_a_record_for_a_canon_retired_route`, parametrized over the three paths:
  - it asserts that `catalog_obj()` holds none of them;
  - it appends a copy of the adopted `/ops/rails/refusal` record re-pathed to the retired path;
  - it expects `ValueError` matching `canon-retired`, so that this pin, and no other check, refuses it.

**Unchanged.** `test_unrouted_methods_return_the_governed_405_with_allow` still exercises `/ops/writer/diagnostic`'s 405. That case tests the route, which stays, not the catalog.

### 6.3 AD-2 — the exact gate (`adapter/http_reader.py`, member)

```python
def _reader_dev_env_explicit() -> bool:
    """Dev ``GET /reader`` gate (PF05 §5.4 and §5.6; PF12 §8.8): served only when
    ``APP_ENV`` is exactly ``dev``, with no trimming or case-folding.  Unset,
    empty, ``test``, ``local`` and every other value refuse; an unset
    environment is not development."""

    return os.environ.get("APP_ENV") == "dev"
```

Unchanged:
- the helper's name and call site (line 612);
- the order (`v` validation, 400 `ERR_READER_INVALID_VERSION`, before the gate, 403 `ERR_READER_FORBIDDEN`);
- `HEAD` through the same view;
- `_dev_admin_gate` and the sampler and conjunction gates (AD-4 item 3 is WU-PR-05's);
- the catalog `env_gate` `APP_ENV=dev`, `VERIFY.sh` and the start helper's propagation (PD-29).

Tests in `tests/http/test_reader_a7_transport.py` (PD-30):
- `test_dev_reader_is_served_only_for_explicit_dev`: parameters `["dev"]` only.
- `test_dev_reader_refuses_every_other_environment`: unset, `""`, `"  "`, `" dev"`, `"dev "`, `" DEV "`, `"Dev"`, `"DEV"`, `"test"`, `"local"`, `"prod"`, `"production"`, `"live"`, `"staging"`, `"development"`, `"dev1"`. That is 16 values, a superset of 2.7's list; `staging`, `development` and `dev1` are the arbitrary values.
- Each case asserts:
  - 403 `ERR_READER_FORBIDDEN`, `no-store`, JSON, no ETag;
  - `HEAD` 403 with no body;
  - `v=2` still answering 400 first.

### 6.4 AD-3 — the canonical dev runner

**Run call** (`adapter/http_reader.py` `__main__`; PD-31):

```python
if __name__ == "__main__":
    # dev runner (Railway uses gunicorn via Procfile): loopback only, debugger and
    # reloader off (PF05 §5.4 "Gate"; PF14 §34 "Required local capture profile")
    import os
    create_app().run(
        host="127.0.0.1",
        port=int(os.environ.get("PORT", "8000")),
        debug=False,
        use_debugger=False,
        use_reloader=False,
    )
```

The run call has no host override. The port stays `8000` by default, with the explicit `PORT` override (HDE Mechanics Guide §34). The explicit flags matter: Flask would otherwise take `debug` from `FLASK_DEBUG` and default the reloader and debugger to it (F-18). The module-level `app = create_app()` is unchanged.

**CORS.** No code is added. The runner emits no CORS header today (F-17), and a test makes that a test-backed declaration (HDE Mechanics Guide §34 "Current repository posture": "no … test-backed disabled-CORS declaration").

**Banner** (`scripts/dev_start_reader.sh` line 23, the only changed line): `[dev-start] Binding port ${PORT} via python -m adapter.http_reader (host=127.0.0.1)`. `APP_ENV` propagation and every other line are unchanged.

**Tests** (PD-32). They are placed in existing registered owners, so no classifier registration is needed:
- **`tests/http/test_reader_a7_transport.py`** (a direct `_HTTP_READER_TEST_OWNERS` entry):
  - `test_dev_runner_binds_loopback_with_debugger_and_reloader_off`, parametrized over `PORT` unset (expects 8000) and `PORT=8123`:
    - it monkeypatches `flask.Flask.run` to record its arguments;
    - it runs `runpy.run_module(http_reader.__name__, run_name="__main__")` (F-27), using the module's `__name__` rather than the literal module path (cycle 1 PD-21: the ownership guard counts that literal);
    - it asserts exactly one call with `{"host": "127.0.0.1", "port": <port>, "debug": False, "use_debugger": False, "use_reloader": False}` on an app that serves `/reader`.
  - `test_dev_runner_emits_no_cors_headers`, six requests carrying `Origin: https://cross-origin.invalid` to `http_reader.create_app()` (the app the runner serves):
    - `GET` and `HEAD /reader` under `APP_ENV=dev` (200);
    - a preflight `OPTIONS /reader` with `Access-Control-Request-Method: GET` (200);
    - `GET /reader` under `APP_ENV=prod` (403), with `v=2` (400), and an unknown path (404).
    - Each asserts the status and that no response header name starts with `access-control-`.
- **`tests/scripts/test_dev_start_reader.py`** (the ID-3 owner of the script): `test_runner_with_explicit_dev_serves_reader` adds `assert "(host=127.0.0.1)" in banner`. Its runner is reached on `127.0.0.1`, as before, so the owner test proves that the start helper still serves on the loopback bind.

**Shared environments.** An environment that needs another bind uses its infrastructure-provided start command (HDE Mechanics Guide §34 "Shared environments"), not this runner. No such environment is known to this plan. The `.devcontainer` value is `127.0.0.1` (F-19).

### 6.5 AD-5 — the corrective release refresh and convergence

The order is Plan v1.1 §10 with step 3b (addendum 2.6 RP-2; 2.7 AD-5), as cycle 1 ran it (result v1.0 §5). It runs:
- under closed rails, with vendor, geocode, database and `GH_TOKEN` variables unset;
- in the implementation branch's working tree, after the member bytes are final and committed;
- steps 2 and 3 once, then steps 3b to 10 a second time to prove byte stability.

| Step | Command (owner) | Notes |
| :- | :- | :- |
| 1 | member bytes final: `adapter/http_reader.py` (one final LF) | no updater run from here to the cut (LR-O3 (a)) |
| 2 | `python scripts/cut_release_manifest.py --version 1.3.0 --built-at-utc 2026-08-24T18:04:49Z --roster-from-admission`; `python scripts/release_id_recompute.py --check-manifest-only`; the cutter with `--check` | one manifest row changes (`adapter/http_reader.py`); record the new `release_id` |
| 3 | `python -c "from engine.config.registry_loader import load_active_mechanics_bundle as l; b=l(); print(b.release_id, len(b.source_identities), b.manifest.version)"`; `python tools/config/generate_config_artifacts.py --compare-goldens . --report <outside the tree>/golden_report.json` | `<release_id> 45 1.3.0`; exit 0 |
| **3b** | `HDE_WRITE_A7_PROOFS=1 python tools/evidence/generate_a7_transport_proofs.py`; then `--check` | the catalog owner first, because the updater validates the catalog with this cycle's validator (AD-5; RP-2) |
| 4 | `python tools/evidence/run_canonical_json_gate.py`; `--check-only` | |
| 5 | `python tools/evidence/update_evidence_index.py`; `--check` | first updater run after the cut |
| 6 | `python tools/config/generate_config_artifacts.py --publish-family`; updater `--check` | |
| 7 | the A7 owner write and `--check` (byte-stable re-run); `python tools/evidence/generate_determinism_gate_proofs.py`; `SAFE_MODE=0 ALLOW_NETWORK=1 python tools/evidence/generate_open_rails_abba_proof.py` (fixture mode, keys absent), then set `FROZEN_OPEN_ABBA_SHA256` in that file to `sha256sum audit/gates/determinism/open_rails_abba.json`; `python tools/evidence/generate_conjunction_writer_evidence.py`; `python tools/evidence/generate_engine_core_evidence.py` | |
| 8 | updater; `--check`; `python tools/evidence/orientation_demo.py --check`; `python tools/evidence/validate_evidence_paths.py`; `ci/checks/check_mirror_schema.sh`; `ci/checks/check_evidence_index_hash.sh`; `python tools/evidence/check_lf_endings.py`; `ci/checks/check_final_lf.sh`; `python tools/evidence/refresh_step_logs_manifest.py --check` | step-7 producers take the new label here (LR-O3 (b)). Invoke the `ci/checks/*.sh` files by path, as `ci.yml` does; `check_mirror_schema.sh` is a Python script (F-25) |
| 9 | `python tools/evidence/run_sanity_pipeline.py --log-path <outside>/sanity.log` (must end `summary:PASS`); then `python tools/evidence/run_sanity_pipeline.py` (the canonical run); `python tools/evidence/run_sanity_pipeline_gate.py`; updater `--check` | |
| 10 | `python tools/cli/generate_showcompat_artifacts.py --check`; `python tools/cli/generate_cli_conformance_artifacts.py --check`; `python tools/evidence/generate_rails_gate_evidence.py --check`; `python tools/evidence/generate_env_matrix_snapshot.py --check` | frozen families unchanged |
| 11 | stale-binding sweep: `git grep -l` for the superseded `release_id` `72fca4c341d871dc75a828140ee1494714b322a13656bac93f66164060ea390f` (and prefix `72fca4c3`) and the superseded open-rails digest `64553c25ada7a04c89dd5c1a2651463a5e907a4b77ccb37bd40ed9a0167135d9` (and prefix `64553c25`), outside `docs/`, `.audit_src/`, `handoff/`, `manifest_pre.sha256` and `manifest_post.sha256` | expected: no hit (prototype). Any hit is classified in the result record; a binding hit is a defect to fix before publication |
| 12 | §10 tests; the attestation build and verify | |

**Restart rules** (2.7 AD-5):
- a member byte change after step 2 restarts at step 2;
- an evidence-primary change restarts at step 3b;
- steps 3b to 10 must be byte-stable on a second run.

**Expected changed set: 61 owner-produced paths** (prototype; PR-30 records its actual set). That is 29 evidence primaries, each with its path proof (29 proofs), plus `docs/ENDPOINTS_CATALOG.json.path_proof.txt`, plus `catalog/manifest.json` and the constant file. The families:
- **Catalog:** `artifacts/audit/ENDPOINTS_CATALOG.json` (through the `docs/` symlink, which stays mode 120000), `artifacts/audit/ENDPOINTS_CATALOG.json.sha256`, `docs/ENDPOINTS_CATALOG.json.sha256`.
- **A7 success proofs:** `artifacts/proofs/{reader_success_get_head_304.json,success_304.txt,success_encoding_invariance.txt,success_get.txt,success_head.txt}`.
- **Config:** `artifacts/catalog/{catalog_schema_validation,domain_closure_report}.log`.
- **Engine core:** `artifacts/core/{abba/ab_ba_parity,json_compare/core_result_json_compare,two_run/identity}.json`.
- **F07 writer:** `artifacts/writer/{conjunction_write_readback.log,conjunction_writer_summary.json}`.
- **Canonical JSON gate:** `audit/gates/canonical_json/{json_canon_compare,json_canonical_check}.log`, `audit/gates/json_gate/canonical/{json_gate_check_log,json_gate_compare_log}.ndjson`.
- **Determinism and parity:** `audit/gates/determinism/{abba.bytes,open_rails_abba.json,tworun_identity.sha256}`, `audit/gates/parity/reader_cli/{ab,ba,summary}.json`.
- **Index and Mirror:** `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, `artifacts/evidence_index.jsonl`, `artifacts/evidence_index.jsonl.sha256`.
- **Constant:** `FROZEN_OPEN_ABBA_SHA256` in `tools/evidence/generate_open_rails_abba_proof.py`.

The same family set as cycle 1's refresh (result v1.0 §5).

**Rewritten byte-identically:**
- `artifacts/proofs/endpoints_env_gate_proof.log` (F-21) and `artifacts/proofs/success_writers_errors.txt`;
- `artifacts/reader/endpoints_snapshot.json`;
- `artifacts/core/purity/purity_report.json` (unlabelled, RP-3);
- the canonical sanity log.

**New base.** The new `release_id` becomes the refresh base for WU-PR-04 and WU-PR-05 (contract E-3). `72fca4c3…` becomes historical. The 22-path roster, the updater and every frozen family are unchanged.

### 6.6 Documents (`docs/server/reader_v1.md`)

- Line 17: "It is served only when `APP_ENV` is exactly `dev` (no trimming or case-folding); unset, empty and every other value, including ` dev`, `Dev`, `DEV`, `test` and `local`, return 403 `ERR_READER_FORBIDDEN`."
- Line 19: "… and runs `python -m adapter.http_reader`, which binds `127.0.0.1` only (loopback; debugger and reloader off; no CORS headers) on `PORT` (default `8000`)."

No other line changes (PD-33). The crib already probes `127.0.0.1:8000` and needs no change.

### 6.7 Unchanged by construction, and verified

- **Contract-inventory baseline (ID-4):** discovered = baseline (F-23). `tests/evidence/test_hdapi_v2_contract_inventory.py` passes with `ruby` in the changed-test step (§10 item 2), as addendum 2.2 requires.
- **Classifier (ID-3):** no registration is needed. The new tests live in registered owners; the changed paths classify (F-24).
- **Architecture snapshot:** `tests/evidence/test_architecture_snapshot.py` passes in the product lane (§10 item 3).
- **`VERIFY.sh`:** unchanged. It probes `127.0.0.1` and passes on the loopback bind (§10 item 9).
- **Production factory and routes:** unchanged. The request-time refusal stays the S10 control in production (AD-4; F-21).

## 7. Change set

### 7.1 Files edited by hand (the companion diff)

| Path | Change | Decision |
| :- | :- | :- |
| `tools/evidence/generate_a7_transport_proofs.py` | `CANON_RETIRED_PATHS`; five records removed; the validator pin | AD-1 |
| `tests/http/test_endpoint_catalog.py` | the import; `_CANON_RETIRED` and `_EXCLUSION_BASIS`; class (d) with nine pairs (four leave class (c)); four enumeration assertions; the retargeted validator case; the retired-pin test | AD-1, AD-6 |
| `adapter/http_reader.py` (member) | `_reader_dev_env_explicit` exact comparison and docstring; the `__main__` run call | AD-2, AD-3 |
| `tests/http/test_reader_a7_transport.py` | the served and refused parameters; the runner-profile test; the CORS-absence test; imports `runpy`, `warnings`, `flask` | AD-2, AD-3 |
| `scripts/dev_start_reader.sh` | line 23, the banner's host text only | AD-3 |
| `tests/scripts/test_dev_start_reader.py` | one assertion that the banner names `127.0.0.1` | AD-3 |
| `docs/server/reader_v1.md` | lines 17 and 19 | AD-2, AD-3 |

### 7.2 Written only by owners

- `catalog/manifest.json` (the cutter).
- `FROZEN_OPEN_ABBA_SHA256` in `tools/evidence/generate_open_rails_abba_proof.py`, set from the regenerated proof's SHA-256 (Plan v1.1 §10 step 7).
- Every family in §6.5.
- The Index, Mirror, sentinels and path proofs (the updater only).

`docs/ENDPOINTS_CATALOG.json` stays a symlink.

### 7.3 Expected unchanged (a change is a finding, §14 RK-7)

- **Adapters and engine:** `adapter/factory.py`, `adapter/wsgi.py`, `engine/http/compat_handler.py`, `engine/presenter/**`, `engine/cli/main.py`, `engine/config/registry_loader.py`.
- **Tools and CI:**
  - `tools/evidence/update_evidence_index.py`, `tools/evidence/hdapi_v2_boundary_analyzer.py`, `tools/evidence/generate_hdapi_v2_contract_inventory.py`;
  - `ci/checks/classify_ci_changes.py`, `.github/workflows/ci.yml`, `pytest.ini`.
- **Scripts:** `VERIFY.sh`, `scripts/qa/dev_sampler_healthcheck.py`, and every line of `scripts/dev_start_reader.sh` but line 23.
- **Documents:** `docs/acceptance/reader_a7_crib.md`, `docs/RUN.md`, `ARCHITECTURE.md`, `AGENTS.md`, `README.md`, `CHANGELOG.md`, `Procfile`.
- **Governed and frozen artifacts:**
  - `artifacts/vendor/hdapi_v2/**`, `artifacts/architecture/**`, `artifacts/cli/**`, `artifacts/identity/**`, `artifacts/math/**`, `audit/ops/**`;
  - `artifacts/reader/endpoints_snapshot.json`, `artifacts/proofs/endpoints_env_gate_proof.log`, `artifacts/proofs/success_writers_errors.txt`, `artifacts/core/purity/purity_report.json`;
  - `.body200.json`, `.code304.txt`.
- **`docs/pfcanon/`.**

## 8. Implementation sequence (PR-30)

PR-30 executes this after Nathan's Proceed for exactly this plan (v2.0).

1. **Recover before creating anything** (PR-30; instruction §13).
   - Inspect local roots, worktrees, branches, open pull requests and `docs/ephemeral/HDE-CRD-0002-WU-PR-03-*` for cycle-2 work: `*-pr-implementation-result-v2*`, or a branch or pull request carrying §7.1. Resume the most advanced consistent state.
   - Never reuse #643, its branch `claude/nifty-cray-w86vmp`, or the cycle-1 Proceed. Publish from a branch whose only commits are this cycle's, on top of the current `main`.
2. **Base check.** Fetch `main` and record the base SHA. If `main` has moved past `79eac95`, run `git diff 79eac95 <base> -- adapter/ tools/evidence/generate_a7_transport_proofs.py tests/http/test_endpoint_catalog.py tests/http/test_reader_a7_transport.py tests/scripts/test_dev_start_reader.py scripts/dev_start_reader.sh docs/server/reader_v1.md catalog/manifest.json ci/checks/classify_ci_changes.py tools/evidence/update_evidence_index.py`.
   - If it is not empty, re-measure F-15 to F-17 and F-23 and re-run `git apply --check` of the companion diff before continuing.
   - A changed served set (a pair fitting none of the classes (a) to (d)) is a finding (§14).
3. **Environment.**
   - Python 3.12 with CI's install. Pytest readiness: `python -m pip install -r requirements-dev.txt`, then `python -m pytest --version` (`AGENTS.md`).
   - `ruby` on `PATH`, with `ruby --version` recorded, for the contract-inventory test (addendum 2.2). `bash` and `curl` for the start-helper owner test and `VERIFY.sh`.
   - Closed rails; vendor, geocode, database and `GH_TOKEN` variables unset.
4. **Apply §7.1.** Use the companion diff as a starting point. Re-read every hunk against §6.
5. **Before and after, without admission.**
   - At the base, with only the new tests applied, `tests/http/test_reader_a7_transport.py` must fail exactly the RC-1 set (7 cases). Record it.
   - With §7.1 applied, the file must pass (27).
   - Optionally, repeat RC-2 (an injected CORS header fails 6 of 6) in a scratch worktree, never in the branch.
6. **Commit the source** (member bytes final). No updater run happens before the cut.
7. **Convergence.** Run §6.5 steps 2 to 11. Record each step, its exit code, the second pass's byte stability (identical `git diff` digest), the new `release_id`, the open-rails digest, and the step-11 sweep with each hit classified.
8. **Commit the convergence** (owner-produced files only).
9. **Validate** (§10) on the candidate commit's tree, in detached worktrees.
10. **Publish.**
    - Write the result record v2.0 (§12), commit it, push, and open the pull request with the template headings (§11).
    - Read the record back.
    - Return `PR_CANDIDATE_PUBLISHED` with the PR-35 handoff.

**Restart rules:**
- any member change after step 6 restarts at step 6;
- any evidence-primary change after step 7 restarts at §6.5 step 3b;
- any change after step 9 repeats step 9.

## 9. Requirement → change → test map

| Requirement / acceptance item (as overlaid) | Change | Proof (local, PR-30) | Proof (hosted, PR-35) |
| :- | :- | :- | :- |
| S15 / (5), read under classes (a)–(d) (2.7 AD-1; EC-8 as overlaid) | §6.1, §6.2 | the enumeration test (18 + 35 = 53); the retired-pin test (3); the validator case; A7 `--check`; updater `--check`; `cmp` catalog = mirror; `success_endpoints` unchanged | changed-test step; evidence lane |
| S10 / (2): exact `dev` (2.7 AD-2; IF-10 first part) | §6.3 | the served test (1) and refusal matrix (16); before/after RC-1 | changed-test step |
| S10 / (2), last clause as 2.6 B-2 (the runner propagates; unset refuses) | unchanged | `tests/scripts/test_dev_start_reader.py` (10) | changed-test step |
| S09 / S10: the canonical runner meets the local capture profile (2.7 AD-3) | §6.4 | the runner-profile test (2); the CORS-absence test (6); the banner assertion; RC-1 and RC-2; `VERIFY.sh` with `APP_ENV=dev` exit 0 | changed-test step |
| AD-5 / acceptance (7): admission `1.3.0`, 45 members, new `release_id`; byte-stable passes; recompute; lanes green | §6.5 | admission line; two-pass digest; `release_id_recompute.py --check-manifest-only`; the selected lanes; the attestation | product, compat, db, evidence and release lanes; `CI_APPLICABILITY_AND_EXACT_HEAD_OK` |
| AD-6: the canon trace and the recorded class basis | §6.2, §17 | the basis assertion in the enumeration test; §17 repeated in the result record | changed-test step |
| ID-4 (addendum 2.2): the baseline equals the discovered records | none (F-23) | `tests/evidence/test_hdapi_v2_contract_inventory.py` with `ruby` | changed-test step |
| S02, S07, S18, ID-3, RP-1, RP-3 (delivered by #643) | none | the full sweep; `check_cli_help.sh`; the CLI conformance `--check`; `VERIFY.sh` | the lanes |

## 10. Validation plan (PR-30, local)

Every check runs on the candidate commit's tree under §8 step 3's environment, in a detached worktree with `PYTHONPATH` set to it. Each ends with `git diff --exit-code` and an empty `git status --short --untracked-files=all`. A failure is a finding to fix, never to skip, deselect, mark `xfail` or quarantine.

1. **Classifier dry run.** `python ci/checks/classify_ci_changes.py --base <base SHA> --head <candidate SHA> --event-name pull_request --github-output <outside> --changed-tests-output <outside>`, with full SHAs. Expect exit 0, lanes `product,compat,db,evidence,release`, `changed_tests=true`, and the prototype's 20 targets (F-24); record any difference.
2. **The changed-test step** as `ci.yml` runs it: one `python -m pytest -q -p no:cacheprovider -- <targets>` process. Prototype: 854 passed.
3. **Product lane:** `generate_ordering_artifacts.py --check` and its four test paths, including `tests/evidence/test_architecture_snapshot.py`. Prototype: 77 passed.
4. **Compat lane:** `ci/checks/check_cli_help.sh`, the serializer grep guard and the emitter symbol proof (outputs outside the tree), and its ten test files. Prototype: 103 passed, 3 skipped, 2 xfailed.
5. **DB lane:** `check_direct_db_contract.py` and its seven test paths. Prototype: 249 passed.
6. **Evidence lane:** the updater `--check`, `orientation_demo.py --check`, `refresh_step_logs_manifest.py --check`, `ci/checks/check_evidence_index_hash.sh`, `validate_evidence_paths.py`, `ci/checks/check_mirror_schema.sh` and `ci/checks/check_final_lf.sh`, with the `.sh` files invoked by path; then its six test files. Prototype: every check exit 0; 130 passed (572 s).
7. **Release-lane tests:** `release_id_recompute.py --check-manifest-only` and the four release-lane test files. Prototype: recompute exit 0; 79 passed. Frozen families: §6.5 step 10 in both passes.
8. **Attestation:** `python tools/evidence/build_release_attestation.py --output <external empty dir> --require-clean`, then `--verify`, both exit 0. Record `validation_result`, `release_admission`, `release_id`, `manifest_sha256`, `source_commit` and `source_commit_exact`. Prototype: both exit 0; `validation_result: PASS`, `release_admission: PR06R_B_FINAL_PASS`, `release_id` = `manifest_sha256` = `d84d99e1…`, `source_commit` the scratch convergence commit, `source_commit_exact: true` (about 3 minutes).
9. **`VERIFY.sh`** from the worktree root, with `APP_ENV=dev` and a free `VERIFY_PORT`: exit 0, every token `_OK`, against the loopback runner. Prototype: exit 0; 12 of 12 tokens `_OK` (`SERIALIZER_ONE_LF`, `PREIMAGE`, `TWO_RUN_IDENTITY`, `AB_BA`, `READER_200_STATUS`, `READER_200_HEADERS`, `READER_200_ETAG_PRESENT`, `READER_200_ETAG_MATCH`, `READER_304_STATUS`, `READER_304_EMPTY_BODY`, `READER_HEAD_CL_MATCH`, `ETAG_INVARIANCE`), probing the loopback runner.
10. **`VERIFY.sh` without `APP_ENV`:** exit 2, `VERIFY_APP_ENV_NOT_DEV` on standard error, empty standard output. Prototype: exit 2; `VERIFY_APP_ENV_NOT_DEV: run with APP_ENV=dev (effective: <UNSET>)`. Informative: the 24 `_HTTP_READER_TEST_OWNERS` files plus `tests/scripts/test_dev_start_reader.py` and `tests/scripts/test_dev_sampler_healthcheck.py`, run with `APP_ENV` unset, to name any test that depends on CI's `APP_ENV=dev`. A failure there is recorded, not fixed by changing an expectation. Prototype: 804 passed; no test depends on CI's `APP_ENV=dev`.
11. **Full sweep:** `python -m pytest -q -p no:cacheprovider tests` with `ruby`, `bash` and `curl` on `PATH`. Expect 0 failed and a clean tree. Prototype: 4,761 passed, 3 skipped, 2 xfailed, 0 failed (1,107 s), clean tree. The 3 skips (`tests/cli/test_showcompat_parity_and_identity.py`, open-rails vendor cases) and 2 xfails (`tests/adapter/test_jsonschema.py`, `/internal/version` cases) are pre-existing, in files this delta does not touch. Cycle 1 had 4,747 passed with the same skips and xfails; the 14 added are this delta's new and changed parametrizations. The updater does not change, so LR-O2 is not triggered. The refresh rewrites the Index and Mirror, though, so every updater consumer must run (instruction §10), and the sweep covers them.
12. **Diff checks** against the base:
    - `git diff <base> <candidate> --name-only`, outside `docs/ephemeral/`, lists exactly the 7 files of §7.1 and the 61 of §6.5;
    - `git diff <base> <candidate> -- scripts/dev_start_reader.sh` is exactly the line-23 change;
    - `git diff <base> <candidate> -- <§7.3 paths>` is empty;
    - `git diff --check` exits 0.

The rails and qa lanes are not selected (F-24). Their test files run in the full sweep. PR-30 records the qa-lane file `tests/qa/test_generate_epic_close_pack.py` result from the sweep (OBS-17).

## 11. PR split, merge dependencies and pull request description

- **One pull request.** It comes from a branch whose only commits are this cycle's: the source commit, the convergence commit, result v2.0, and the PR-35 records. It is new. #643 is not reopened, reused or pushed to.
- **No split.** The member edit, the re-cut and the regenerated families must land together, so that admission and the updater hold at every commit of `main` (cycle-1 plan §11).
- **Upstream merge dependency.** This plan's own pull request merges to `main` first, so that PR-30 reads it from `main`. #644 is merged.
- **Downstream.**
  - PR-40 by the IA reviews the WU-PR-03 lineage across #643 and this corrective pull request after Nathan merges it, and decides acceptance (decision record §5).
  - WU-PR-04's instruction follows only on ACCEPT. Its refresh base is this cycle's `release_id`.
- **CI cost:** the product, compat, db, evidence and release lanes and a 20-target changed-test step (F-24). The classifier's own rules select them for these paths; no lane is added (Plan Templates, "CI lane classification and automated budget-control discipline"). The record commits under `docs/ephemeral/` select no lane.
- **Pull request description** (`.github/pull_request_template.md` headings; `AGENTS.md` "PR descriptions"):
  - **Why:**
    - the Product Owner direction of 2026-10-14, quoted from the decision record;
    - PF10 addendum 2.7 (AD-1, AD-2, AD-3, AD-5, AD-6), with CR-7 and CR-8 `APPROVED`;
    - #643's open Codex threads, resolved by this pull request: `PRRT_kwDOP103ks6sJ4Y_` (catalogued retired routes) by AD-1, `PRRT_kwDOP103ks6sJ4Y8` (normalizing gate) by AD-2. The threads stay on #643 as merged evidence; nothing is posted there.
  - **What changed:** grouped by path, as §7.1 and §6.5.
  - **Checks run:** each check with its counts, including the before/after and the red controls, the two-pass digest and the sweep.
  - **Not in this PR:**
    - AD-4's four gaps (WU-PR-05, S19), with OBS-P3-3;
    - the doc-delta candidates (Product Owner);
    - the stale documents (§18), with owners;
    - PR-40's acceptance decision.
  - **What merging does:** the 18-record catalog, the exact gate and the loopback runner become current on `main`, with the new `release_id`. For the records under `docs/ephemeral/`: "Merging preserves the record and approves nothing (D21-C)". It establishes no QA, acceptance or closure. Merge-order dependency: before WU-PR-04's instruction.
  - It must not restate #643's claims as its own, and it states that #643's description is unchanged.

## 12. Acceptance and evidence obligations (result record v2.0)

`docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-implementation-result-v2.0.md` contains:
- the recovery performed and the base SHA; the commits, with the tree of the tested commit;
- **the canon trace (AD-6):** §17's decision and route tables, restated against the landed code, with any difference explained;
- **AD-1:** the catalog diff (23 → 18 records; the five removed records named); the exclusion table by class with counts; the arithmetic at the head ("18 catalogued + 35 excluded = 53 served", or the then-current values); the validator pin and its test;
- **AD-2:** the served value and the refusal matrix result; RC-1 before and after;
- **AD-3:** the run-call arguments as the test observed them; the CORS-absence cases; the banner line; the `VERIFY.sh` and owner-test runs on the loopback bind;
- **AD-5:**
  - the new `release_id` (superseding `72fca4c3…`), the open-rails digest and the changed set with paths;
  - every §6.5 step with its exit code; the second-pass digest; the stale-binding sweep with each hit classified;
  - the statement that the new `release_id` is the refresh base for WU-PR-04 and WU-PR-05;
- every §10 check actually run, with counts, the `ruby` version and the environment;
- `CANON_CONFLICT_REGISTER` as §16 states it;
- in-flight decisions (PR-30 contract), or `NONE`;
- **nonclaims:**
  - CI green is not QA;
  - no QA artifact;
  - no route, production-factory or public-contract change;
  - the three canon-retired routes stay mounted, their exposure being AD-4's;
  - WU-PR-03 is not accepted by this record or by the merge; PR-40 decides across #643 and this pull request.

QA evidence and `audit/qa/hde-crd-0002/` are out of scope (instruction §7). No new evidence family is produced.

## 13. Security and migration constraints

- **Migration:** none (no data or schema change). Rollback is Nathan's revert of the corrective squash commit followed by a same-version manifest refresh, because a member changes (Plan v1.1 §7, §14). That would restore the 23-record catalog and the normalizing gate.
- **Security:** every change narrows exposure or makes a declaration test-backed.
  - AD-2 refuses padded and case-variant values that served before.
  - AD-3 removes the all-interfaces bind of the dev runner, pins the debugger and reloader off, and proves the absence of CORS.
  - AD-1 removes canon-retired routes from the governed inventory; their exposure in production is unchanged and belongs to WU-PR-05 (AD-4).
  - No route opens. The production factory is unchanged.
- **Names only.** Catalog fields carry no secrets, URLs, tokens or payload bytes (HDE Schemas & Artifacts §8.8). The CORS test uses the reserved `.invalid` origin.
- **Rails and secrets.** The refresh opens no rail. The open-rails fixture proof runs in fixture mode with keys absent. No secret, token or key value appears in tests, logs or records.
- **Reviewer chain (addendum 2.3):** the Codex code review is read and resolved by PR-35. No Codex security review is requested or waited on, and its absence is not a gap.

## 14. Risks and recovery

| ID | Risk | Treatment |
| :- | :- | :- |
| RK-1 | The updater refuses before the catalog owner has run with the new validator | step 3b order (AD-5); restart point 3b |
| RK-2 | A member byte change after the cut | restart at step 2 |
| RK-3 | `check_mirror_schema.sh` run through `bash` | invoke by path (F-25) |
| RK-4 | `ruby` absent on a runner | the contract-inventory test fails, never skips (addendum 2.2); PR-35 records the hosted version if the log shows it (O-6) |
| RK-5 | `curl` absent where the owner test runs | the test fails with "VERIFY.sh requires curl"; hosted `ubuntu-latest` provides it |
| RK-6 | `runpy` re-execution has side effects | prototype: none (27 passed; the full sweep passed with it). The test filters only the one `RuntimeWarning` about re-execution (F-27) |
| RK-7 | A boundary: a served pair fitting none of (a) to (d); a change needed outside §7.1 and §6.5 (in particular to a §7.3 path); a classifier change; an architecture-snapshot or frozen-family `--check` failure; a contract-inventory baseline change; any route or production-factory change | stop the affected work; `RESCOPE_REQUEST` through RS-20 with `PR_RETURN_PHASE` recorded. AD-4's gaps are never pulled into this unit |
| RK-8 | A reviewer asks to unmount the dev routes in production or to gate the retired routes | outside the unit by decision (AD-4). PR-35 replies with AD-4 and leaves it to WU-PR-05 |
| RK-9 | A shared environment needs a non-loopback bind | 2.7 AD-3 "Shared environments": the infrastructure-provided start command, not this runner; the Product Owner and infrastructure canon own it |
| RK-10 | OBS-17: intermittent failure of `tests/qa/test_generate_epic_close_pack.py` | the qa lane is not selected; locally it runs in the sweep; a failure is recorded as OBS-17, never fixed here |

Recovery:
- an interruption resumes in the same phase session from its last saved artifact;
- an ordinary defect in this plan returns to this PR-20 context, and the correction is a complete successor version (v2.1);
- a boundary found in PR-30 or PR-35 goes through RS-20 with `PR_RETURN_PHASE`;
- abort is only Nathan's manual PR-50 instruction.

## 15. Decisions taken in this plan (within approved scope)

Numbered after plan v1.1's PD-1 to PD-24 so that no identifier is reused.

| ID | Decision | Basis |
| :- | :- | :- |
| PD-25 | `CANON_RETIRED_PATHS` lives in the catalog owner, and the enumeration test imports it. The pin refuses a retired path as a record path or an alias, with the message `canon-retired route must not be cataloged` | HDE Architecture §0 "Endpoint Catalog (single home; routing note)": derived inventories must not hard-code a second inventory; 2.7 AD-1 "fail-closed" |
| PD-26 | `_EXCLUSION_BASIS` records each class's canon basis as data, which the test asserts for every excluded pair; it replaces the class comment | 2.7 AD-6 "records every excluded pair's class and basis" |
| PD-27 | Four added enumeration assertions: the arithmetic; a basis for every exclusion; class (d) = the served retired pairs exactly; no catalogued retired path | 2.7 binding requirements (catalog; AD-6) |
| PD-28 | The `/ops/probe/env` validator case retargets to `/internal/healthz`; a parametrized retired-pin test per path, matching `canon-retired` | decision record §4; keeps the classification check covered |
| PD-29 | The gate is `os.environ.get("APP_ENV") == "dev"`; the helper's name and call site are kept | 2.7 AD-2 |
| PD-30 | Served `["dev"]`; a 16-value refusal matrix | 2.7 binding requirements (a superset of the listed values) |
| PD-31 | The run call as §6.4: keyword arguments, no host override, `PORT` default `8000` | 2.7 AD-3; HDE Mechanics Guide §34 |
| PD-32 | AD-3 tests: the runner-profile test via `runpy` with `Flask.run` recorded, and the six-request CORS-absence test, both in `tests/http/test_reader_a7_transport.py`; the banner assertion in `tests/scripts/test_dev_start_reader.py`. No classifier registration | decision record §4 ("inside existing owner registrations"); cycle-1 PD-21; F-24, F-27 |
| PD-33 | The text of `docs/server/reader_v1.md` lines 17 and 19 (§6.6); no other document changes | 2.7 AD-2, AD-3 binding requirements; the decided documents only (F-20 → OBS-P3-12) |
| PD-34 | Version the cycle-2 plan and records as v2.x: plan v2.0, result v2.0, PR-35 results v2.1 onward | WU-PR-01 and WU-PR-02 cycle-2 precedent (WU-PR-02 plan v2.0 PD-14) |
| PD-35 | The convergence is cycle 1's order with step 3b, run once from the cut and once more from step 3; the sweep patterns are this cycle's superseded values | 2.7 AD-5; result v1.0 §5 |
| PD-36 | Local validation runs the five selected lanes, the attestation, `VERIFY.sh` and the full sweep | instruction §10; 2.7 binding requirements |

## 16. Canon-conflict register

`CANON_CONFLICT_REGISTER`:

| ID | Classification | Status | Decision owner | Effect on this plan |
| :- | :- | :- | :- | :- |
| CR-1, CR-2, CR-3 | CANON_RECONCILIATION | `APPROVED_AS_CHANGED` | Thoth | none |
| CR-4 | CANON_RECONCILIATION | `APPROVED` | Product Owner (`docs/ephemeral/HDE-CRD-0002-WU-PR-01-po-disposition-cr-4-cr-5-v1.0.md` §2) | none |
| CR-5 | CANON_RECONCILIATION | `APPROVED_AS_CHANGED` | Product Owner (same record §3) | this pull request carries no canon change |
| CR-6 | CANON_RECONCILIATION | `APPROVED`, alternative (a) | the IA through RS-20 (rescope review v1.0 §12) | the start helper's propagation stands; only its banner text changes (2.7 overlays 2.6 item 1 for that line) |
| CR-7 | CANON_RECONCILIATION (Specification S15 and Plan IF-6/EC-8 versus HDE Architecture §3.5) | **`APPROVED`**, alternative (a): exclusion under canon | the Product Owner's direction of 2026-10-14; decisions drafted by the IA (decision record §6; addendum 2.7) | applied by §6.1 and §6.2 |
| CR-8 | CANON_RECONCILIATION (instruction §9.2 versus the explicit `APP_ENV=dev` passages) | **`APPROVED`**, alternative (a): exact comparison | same | applied by §6.3 |

CR-7 history: PROPOSED 2026-10-14T04:00Z (PR-35 rescope request §7); reviewed and escalated 05:05Z (PR-35 rescope review §7); APPROVED 05:10Z (decision record §6). Drainage: HDE Schemas & Artifacts §8.8 population rule and HDE-CLI-API-Vendor-Ref §5.6 "Implementation and acceptance state" (Product Owner). CR-8: the same times; no drainage.

**No new conflict.** This plan applies decided canon readings and creates no reading of its own. Searched on `main` for this plan:
- `git grep` of `docs/pfcanon/` for `RETIRED/NONCANONICAL`, `/ops/probe/env`, `/ops/db/unavailable`, `/ops/writer/diagnostic`, `Endpoint Catalog`, `127.0.0.1`, `0.0.0.0`, `use_reloader`, `use_debugger`, `CORS`, `Access-Control`, `APP_ENV=dev`, `exactly` and `dev harness`;
- the change's `docs/ephemeral/HDE-CRD-0002-*` records for the same terms.

Every governing hit is read and mapped in §17. One canon inconsistency outside this unit's decisions surfaced and is recorded, not resolved (OBS-P3-16): HDE Build Checklist — Conjunction HDE-CONJ001.1 says harness responses use `no-store` "on all" responses, while HDE-CLI-API-Vendor-Ref §5.4 sets `Cache-Control: private, max-age=0, must-revalidate` on the dev Reader's 200. Neither the corrective change nor cycle 1 changes any header, so no change requirement is affected. It is a doc-delta observation for the Product Owner, not a register entry.

## 17. Canon trace (AD-6)

Every source below was read in full on `main` at `79eac95` (see "Canon relied on").

### 17.1 Decisions

| Decision | Canon document, section and bullet relied on | How this plan applies it |
| :- | :- | :- |
| AD-1 | HDE Architecture §3.5 "Internal-ops identity and refusal (route-only)": "Current repository discrepancy" ("The checked-in `/ops/db/unavailable`, `/ops/probe/env`, and `/ops/writer/diagnostic` routes are `RETIRED/NONCANONICAL` as architecture and excluded from the Endpoint Catalog"; "No repository removal … or catalog mutation is claimed"), and "Adopted routes" (`/internal/version`; `/ops/rails/refusal`) | §6.1: five records out; the routes stay mounted; `/ops/rails/refusal` stays catalogued |
| AD-1 | HDE Users Guide §1.1 "Checked-in retired/noncanonical route drift (unsupported)" (the three rows; "do not define route bytes, promise removal, create a deprecation window, or imply compatibility support") | §6.2 class (d) basis; no route removal |
| AD-1 | HDE Architecture §0 "Intent & scope", "Endpoint Catalog (single home; routing note)" ("the single home for the canon set of client-callable endpoints"; derived inventories "MUST NOT independently hard-code a second endpoint inventory") | PD-25: the retired set lives in the owner; the test imports it |
| AD-1 | HDE Schemas & Artifacts §8.8 "Authoritative Endpoint Catalog file" ("a machine-readable inventory of HTTP endpoints (public surfaces and key internal/ops/dev endpoints)"; "select only from Catalog entries that correspond to real mounted routes"; the closed class set and the minimum fields) | §6.1: no new class, no field change; the `catalogued − served` assertion is kept |
| AD-1 | HDE-CLI-API-Vendor-Ref §5.6 "Endpoint Catalog (JSON success)" (the transport-facts table lists none of the three routes; "Catalog membership never by itself proves reachability"; the Aux record and `aliases`) | the Aux record, `public_aux` and `aliases` unchanged |
| AD-1 | HDE Governance §9.1.2 "Canon precedence and persistent sources" (canon over in-flight documents; "Follow the governing PF position immediately"); HDE Build Notes 2.7 AD-1 ("S15 reading") | S15 read under canon; IF-6/EC-8 overlaid (§5A.2) |
| AD-2 | HDE-CLI-API-Vendor-Ref §5.4 "Route and gate (must)", bullet "Gate." ("The route must be gated by `APP_ENV=dev` …") | §6.3: the exact comparison |
| AD-2 | HDE-CLI-API-Vendor-Ref §5.6 transport-facts table, `/reader` row ("explicit `APP_ENV=dev`") | §6.3 |
| AD-2 | HDE Schemas & Artifacts §8.8 "Reader surface routes and distinct contracts (normative)" ("explicitly gated by `APP_ENV=dev`") | §6.3; the catalog `env_gate` `APP_ENV=dev` unchanged |
| AD-2 | HDE Mechanics Guide §34 route table, `/reader?v=1` row ("It requires explicit `APP_ENV=dev`"), and "Required local capture profile" ("Require the caller to supply `APP_ENV=dev`. Do not document a missing value as equivalent to dev") | §6.3; §6.6 |
| AD-2 (contrast) | HDE-CLI-API-Vendor-Ref §5.5 "Validation and environment gating" (trimming and case-folding only to resolve the compat production posture, which widens refusal); HDE Governance "Dev/admin APP_ENV gating (dev/test/local only)" ("exactly `{"dev","test","local"}`"; "MUST NOT assume a default") | why normalization is not applied to this gate; `_dev_admin_gate` is AD-4's |
| AD-3 | HDE-CLI-API-Vendor-Ref §5.4 "Gate." ("… bound only to a local interface (for example, `127.0.0.1`) …"), "Documented local-style access (clarification)" (`127.0.0.1` as the documented client host), "Rails closed." | §6.4 run call; §6.6 document text |
| AD-3 | HDE Mechanics Guide §34 "Required local capture profile": bind `127.0.0.1`; port `8000` with a `PORT` override; caller-supplied `APP_ENV=dev`; closed rails; `LC_ALL`/`LANG`/`TZ` pins; "Disable CORS. No cross-origin allow-list, wildcard, credentials, or CORS response headers"; "Set Flask `debug=False`, `use_debugger=False`, and `use_reloader=False` explicitly" | §6.4: every bullet the runner owns |
| AD-3 | HDE Mechanics Guide §34 "Shared environments" and "Current repository posture" (the `0.0.0.0` bind, the absent flags, no "test-backed disabled-CORS declaration") | §6.4 shared-environment note; the CORS test as the test-backed declaration |
| AD-3 | HDE Build Checklist — Conjunction, Subtask HDE-CONJ001.1 "Harness behavior & non-production posture", "Dev-only posture" ("Bound only to loopback (for example `127.0.0.1`)"; "CORS disabled for harness routes"; "debug reloader is OFF during evidence runs") | supporting canon for AD-3; found by this plan's search; not cited by the decision record |
| AD-3 (scope) | Glow Infrastructure §2.2 "Documented client access vs service identity (names-only)", bullet "Client access, service identity, and server bind are separate facts" ("Services may still bind to `0.0.0.0` … when that is the correct runtime posture"), and Plan Templates line 1026 ("`127.0.0.1` in these templates is not … a server bind requirement") | they govern services and templates generally; HDE Mechanics Guide §34 governs this dev runner specifically. No conflict; the production `Procfile` and `scripts/start_web.sh` binds are untouched |
| AD-3 (unchanged) | HDE Architecture §3.8.1 "Dev/QA Reader availability", bullet "Repo-side start-helper posture (names-only)"; HDE Mechanics Guide §5.6, paragraph "Dev Reader start helpers (APP_ENV propagation)" | the banner changes; propagation does not (2.6 RP-1; CR-6) |
| AD-4 | HDE Architecture §3.2 "A7 proof surface" ("Non-prod entries must be unreachable in production"); §3.3 "Gating & posture" ("Harness is dev-only; never mounted in production") and "Current repository discrepancy"; §1.3 "Separation of surfaces"; HDE-CLI-API-Vendor-Ref §5.4 "Gate." ("must not be mounted in production builds or non-dev deploys"); HDE Governance dev/admin gating; Specification S19 | §5 out of scope; §18 carried to WU-PR-05 |
| AD-5 | Implementation Plan v1.1 §10; HDE Build Notes 2.6 (step 3b; the 22-path roster) and 2.7 AD-5; `AGENTS.md` "Release identity" and "HDE-EPIC040 admission addition"; HDE Governance §9.1.2 | §6.5 |
| AD-6 | `AGENTS.md` canon-first rule; HDE Governance §9.1.2 ("Record the actual PF titles and sections relied on and claim conformance only to material read"); Plan Templates "Canon precedence for template use" | this section; PD-26; §12 |

### 17.2 Routes the unit touches

| Route and methods | Posture after the corrective pull request | Canon |
| :- | :- | :- |
| `GET /reader`, `HEAD /reader` | served only for `APP_ENV` exactly `dev`; catalogued (`dev_harness`, `env_gate: APP_ENV=dev`, A7-eligible, the success designation) | HDE-CLI-API-Vendor-Ref §5.4 "Gate.", §5.6 `/reader` row; HDE Schemas & Artifacts §8.8 "Reader surface routes and distinct contracts" and "Governed Reader success-proof designation"; HDE Mechanics Guide §34 route table |
| `OPTIONS /reader` | unchanged; framework-implicit (class (c)); no CORS headers (tested) | HDE Mechanics Guide §34 "Disable CORS"; ID-1 class (c) |
| `POST /reader` | unchanged; governed refusal (class (a)) | HDE-CLI-API-Vendor-Ref §5.4 "Production mount" |
| `GET`, `HEAD`, `OPTIONS /ops/db/unavailable`; `GET`, `HEAD`, `OPTIONS /ops/probe/env`; `POST`, `HEAD`, `OPTIONS /ops/writer/diagnostic` | mounted and unchanged; not catalogued; class (d), canon-retired; the validator refuses a record for them | HDE Architecture §3.5 "Current repository discrepancy"; HDE Users Guide §1.1 "Checked-in retired/noncanonical route drift" |
| `GET`, `POST /ops/rails/refusal` | unchanged; catalogued | HDE Architecture §3.5 "Adopted routes" |
| the dev runner (`python -m adapter.http_reader`, started by `scripts/dev_start_reader.sh`) | binds `127.0.0.1` only; debugger and reloader off; no CORS headers | HDE-CLI-API-Vendor-Ref §5.4 "Gate."; HDE Mechanics Guide §34 "Required local capture profile"; HDE Build Checklist — Conjunction HDE-CONJ001.1 |
| every other served pair (the remaining 14 catalogued records and the other 24 class (a)–(c) exclusions) | unchanged | the class bases of §6.2; cycle 1's per-record readings (plan v1.1 §6.5, PD-9) |

Tally at the prototype head: 53 served = 18 catalogued + 35 excluded (7 (a), 1 (b), 18 (c), 9 (d)).

## 18. Stale documents, observations and carried items (not in this pull request)

**Stale documents** (made stale or left stale by this cycle; not changed here):

| Document | Statement | Owner |
| :- | :- | :- |
| HDE Mechanics Guide §34 "Current repository posture" | the `0.0.0.0` bind, the absent flags, no test-backed disabled-CORS declaration, and "The Reader handler treats missing `APP_ENV` as dev"; also its route table's `/api/reader?v=1` alias row | Product Owner (canon doc-delta; 2.7) |
| **HDE Users Guide §4.1 "Start the local Reader/dev harness"** (new) | "The helper binds the process through `python -m adapter.http_reader` to host `0.0.0.0` on `PORT` …" | Product Owner (canon doc-delta; found by this plan's search; not in 2.7's list) |
| HDE Schemas & Artifacts §8.8 | the population rule, including the canon-retired exclusion, `public_aux` and `aliases` | Product Owner (canon doc-delta; CR-7 drainage) |
| HDE-CLI-API-Vendor-Ref §5.6 "Implementation and acceptance state (informative)" | the catalog state | Product Owner (canon doc-delta; CR-7 drainage) |
| HDE Architecture §3.4 | the health probes are labelled speculative, while HDE Mechanics Guide §32.3 requires them (as 2.7 records it) | Product Owner (2.7 doc-delta) |
| **`docs/RUN.md` line 5** (new, OBS-P3-12) | "binds `0.0.0.0` on `PORT`" | WU-DOC-01, through the IA |
| **`scripts/qa/dev_sampler_healthcheck.py` line 129** (new, OBS-P3-13) | the comment "Reader runner binds to 0.0.0.0"; its behavior is unaffected (F-19) | the IA (QA tool owner) |
| `AGENTS.md`, `README.md` | the start command with `APP_ENV=dev` and the loopback bind | WU-DOC-01 (decision record §7) |
| cycle 1's stale-document list (result v1.0 §9) | unchanged | as named there |

**Observations** (owner: the whole-change IA, who routes them):

| ID | Observation | Suggested route |
| :- | :- | :- |
| OBS-P3-12 | `docs/RUN.md` line 5 states the `0.0.0.0` bind (F-20) | WU-DOC-01 |
| OBS-P3-13 | `scripts/qa/dev_sampler_healthcheck.py` line 129 comment (F-19) | IA |
| OBS-P3-14 | `Flask.run` would read `.env`/`.flaskenv` through `python-dotenv` if that were installed. It is not in `requirements*.txt` or CI's install, and no such file is tracked (F-18). With it installed, an operator's local `.env` could supply `APP_ENV` to the runner. Not changed here, because 2.7 binds the run-call arguments exactly | WU-PR-05 (S19) or the Product Owner |
| OBS-P3-15 | Precision: `create_app`'s after-request hook does run; its two branches never match (F-26). Addendum 2.7 AD-4 item 4 says it "never fires" | the WU-PR-05 instruction's wording of AD-4 item 4 |
| OBS-P3-16 | HDE Build Checklist — Conjunction HDE-CONJ001.1 says harness responses use `no-store` "on all" responses; HDE-CLI-API-Vendor-Ref §5.4 sets `private, max-age=0, must-revalidate` on the dev Reader's 200. Not affected by either cycle | Product Owner (doc-delta) |
| OBS-P3-17 | The root helpers `run_flask.py` and `run_flask_dev.sh` (with `FLASK_AUTO_RUN_GUIDE.md`) run the production factory, which mounts the dev routes, with the interactive debugger and reloader on (F-28). HDE Architecture §3.8.1 records them as not satisfying the dedicated-harness contract. AD-3 binds the canonical runner only | WU-PR-05 (S19, with AD-4's gaps) or the Product Owner |

**Carried** (decision record §7; addendum 2.7 "Unresolved obligations and owners"; cycle 1):
- **AD-4's four gaps**, to WU-PR-05 (S19) as named inputs:
  - the production mount of the dev-harness routes and the `POST /reader` stub;
  - the retired `/ops` routes ungated in production (OBS-P3-4);
  - `_dev_admin_gate` normalization (OBS-RS2-1);
  - the after-request hook (OBS-P3-1, with OBS-P3-15).
  
  OBS-P3-3 (`adapter/wsgi.py`'s 405 has no `Allow`) goes with them.
- WU-PR-08 (S17): the port and bind statements describe the loopback bind.
- WU-PR-04, WU-PR-05 and WU-PR-08: the refresh base is this cycle's `release_id`; the 22-path roster stays; step 3b applies when a unit changes the catalog validator.
- WU-DOC-01: `AGENTS.md` and `README.md` state the start command with `APP_ENV=dev` and the loopback bind; OBS-P3-12.
- From cycle 1, unchanged: OBS-P3-2, OBS-P3-5 to OBS-P3-11 with their owners (result v1.0 §9); OBS-W3-1, now addressed for the bind by AD-3 and for the production mount by AD-4; LR-O1 and LR-O3, applied in §6.5; LR-O2, not triggered (the updater does not change), with every consumer run by the sweep; OBS-17 (RK-10); O-6 (RK-4); AQ-1 (WU-PR-07 only).

## 19. PR-30 and PR-35 ownership

**PR-30** (after Nathan's Proceed for exactly this v2.0, in a dedicated session):
- recovers before creating any vehicle (§8 step 1);
- implements only §7.1 and produces governed evidence only through the owners (§6.5, §7.2);
- records the RC-1 before/after and tests locally under §10;
- makes coherent commits (source, then convergence) and publishes the initial candidate on a new pull request;
- writes, pushes and reads back result v2.0;
- returns `PR_CANDIDATE_PUBLISHED` with a handoff to PR-35 in PR-35's own dedicated session.

PR-30 owns neither review correction nor current-head CI readiness nor merge.

**PR-35** (its own dedicated session):
- retrieves and resolves the Codex code review findings (addendum 2.3), retests locally and pushes coherent corrections within §5;
  - a member change re-runs §6.5 from step 2;
  - an evidence-primary change re-runs it from step 3b;
- uses CI economically: known findings first; no `[skip ci]` without Nathan's direct authorization;
- verifies current-head CI (the five classified lanes and the changed-test step, `CI_APPLICABILITY_AND_EXACT_HEAD_OK`), remote-head identity and mergeability;
- records each run on its heads with its actual conclusion, and the hosted `ruby` version if the log shows it (O-6);
- writes its records as results v2.1 onward;
- returns `MERGE_PENDING — Ready to merge` without merging.

No CI waiver exists for HDE-CRD-0002.

**Merge and lineage.** Nathan merges manually. PR-40 by the whole-change IA then reviews the WU-PR-03 lineage across #643 and the corrective pull request.

## 20. Session identity and recovery envelope

```yaml
change: HDE-CRD-0002 / WU-PR-03
phase: PR-20 plan cycle 2 complete; AWAITING_PO_PROCEED
plan: docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-implementation-plan-v2.0.md (v2.0)
companion: docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-implementation-plan-v2.0-prototype.diff
predecessor: docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-implementation-plan-v1.1.md (v1.1, spent by #643; preserved)
entry: Product Owner direction of 2026-10-14 → docs/ephemeral/HDE-CRD-0002-WU-PR-03-corrective-architecture-decisions-v1.0.md → PF10 addendum 2.7 (published in v13.5.8)
instruction: docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-instruction-v1.0.md (v1.0; overlaid by addenda 2.6 and 2.7)
baseline: origin/main 79eac952edbed9e31c3c6ab98528196b81ae69a8
session_disposition: INITIAL_DEDICATED_ASSIGNMENT
role_session_ref: NOT_YET_ASSIGNED (Nathan / Product Owner)
authoring_session: https://claude.ai/code/session_0186RTKAbX7HsgFuEgBB1fE8
earlier_sessions: plan v1.0/v1.1 and PR-30 https://claude.ai/code/session_01GC6jqu4Lczzk7PR7QGXSTJ; cycle-1 PR-35 https://claude.ai/code/session_0136SjBtuTJwoEpceUd46T6C (provenance only)
pending_decision: Nathan's PR Implementation Proceed for exactly this plan (v2.0)
vehicle: none for cycle 2 (no implementation branch, commit or pull request exists); #643 is merged history
resume_point: PR-30 §8 step 1
scratch_state: TRANSIENT_SCRATCH only (scratch clone with prototype commits, worktrees and venv in this session's scratchpad); this plan and its companion diff are self-sufficient without them
```

## 21. TypeSafe reading for the receiving session (PR-30, WU-PR-03 plan cycle 2)

PF10 addendum 2.1 governs. The reading is reported as the skill printed it. No agent recommendation of model, reasoning level or effort is given beside it.

Action sent (v6): "Implement, in a new dedicated session after the Product Owner's Proceed, a corrective detailed plan, not yet reviewed, for one work unit of an approved change whose first pull request already merged: seven hand-edited files following a complete task list and a ready prototype diff (remove five endpoint-catalog records for canon-retired routes and add a fail-closed validator pin and a fourth reasoned exclusion class to the route-enumeration test; make a dev route's environment gate an exact comparison; pin the dev runner to a loopback bind with debugger and reloader off and add run-call and no-CORS tests; change one start-script banner line and one document), then, because one release member changes, run a same-version release manifest re-cut and a governed-evidence convergence of about thirty-five owner-tool runs in a fixed order, proven byte-identical on a second pass, followed by five CI-lane replications, an attestation build, a verify script and a full sweep of about 4,800 tests taking about 20 minutes, all already rehearsed green by the planning session; then commit, open a new pull request, write the result record and hand off. No live provider call occurs; code review, a review-and-CI phase, the Product Owner's manual merge and an independent lineage review follow."

- **TypeSafe v6: Opus 5.5, high.** Effort score 2.28 (confidence 0.69); rung probabilities low 0.00, medium 0.10, high 0.54, extra high 0.34, max 0.01, ultracode 0.00. Model probabilities Fable 5.1 0.03, Opus 5.5 0.97 (confidence 0.94). Twelve cells, computed from the two answers: Opus 5.5 at low 0.00, Opus 5.5 at medium 0.10, Opus 5.5 at high 0.52, Opus 5.5 at extra high 0.33, Opus 5.5 at max 0.01, Opus 5.5 at ultracode 0.00, Fable 5.1 at low 0.00, Fable 5.1 at medium 0.00, Fable 5.1 at high 0.02, Fable 5.1 at extra high 0.01, Fable 5.1 at max 0.00, Fable 5.1 at ultracode 0.00. Sent 2026-10-14T06:35:17Z. Nathan picks the cell.
- **Detail:** v6 sent 2026-10-14T06:35:17Z; HTTP 200 in 0.74 s; 4387 input and 54 output tokens; jev-1.13.0. Rung by rule: high (nearest to the score, halves up); model by rule: Opus 5.5 (P(most capable) 0.5 or more is Fable 5.1). Flags: none printed.
- **One send:** taken once, before this plan was saved, with the step label "PR-30 HDE-CRD-0002 WU-PR-03 corrective (plan v2.0)".
- **Records:**
  - the Notion row was not written, as PR-20 directs;
  - Nathan's pick for PR-30 is not stated;
  - Nathan's pick for this PR-20 session is not stated (the reading for it is in the decision record §8: Opus 5.5, high).

**Surface advice for PR-30** (execution surface only):
- **Session.** Run PR-30 as a new top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, with Notion read access for the prompt and GitHub access to open the pull request.
- **Environment.** Python 3.12 with CI's install (package-index access for `pip install`); `ruby` on `PATH` for the contract-inventory test; `bash` and `curl` for the start-helper owner test and `VERIFY.sh`. All were present in this session's cloud container.
- **Run times observed in this session:**
  - the full `tests/` sweep, about 18.5 minutes;
  - the evidence lane, about 9.5;
  - the changed-test step, about 2.5;
  - the two convergence passes, about 6 together;
  - the attestation build and verify, about 3;
  - the `APP_ENV`-unset owner set, about 2.5.
- **Discipline.**
  - Run the convergence in the branch's working tree only after the member edit is committed.
  - Run every other check that can write tracked files in a detached worktree.
  - Invoke `ci/checks/*.sh` by path (F-25).
- **Access.** No live vendor, production or database access is needed.
- **Order.** This plan's pull request is merged first.

## 22. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / WU-PR-03 / PR-20 / plan 2 (corrective cycle), version 2.0 |
| change / specification | CRD HDE-CRD-0002 / `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` v1.1 |
| work unit | WU-PR-03 (S02, S07, S09, S10, S15, S18); corrective decisions AD-1 to AD-6 |
| release | GCFPE-20261009.1 / 100926.1 |
| prompt | PR-20 — Create Detailed PR Implementation Plan — 100926.1, https://app.notion.com/p/3f44590a05eb819fbea5dcd966a750ba (page state as of 2026-10-12T02:29:47Z) |
| role/stage | dedicated WU-PR-03 PR engineering session / PR-20, plan cycle 2 |
| capture time | 2026-10-14T06:35:55Z |
| execution identity | https://claude.ai/code/session_0186RTKAbX7HsgFuEgBB1fE8 |
| inherited usage | PR-10 instruction 1 (instruction §20); PR-20 plan v1.0, request v1.0 and plan v1.1; RS-20 rescope review 1 (review §15); PR-30 result 1 (result v1.0 §16); PR-35 result 1.1 and rescope request 2; RS-20 rescope review 2 (PR-35 rescope review §11); the Product Owner-directed decision record (record §9) |
| repository persistence | recorded here only (installed writer `docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent on `main`; pending, non-gating; owner the Product Owner) |

## Canon precedence (Plan Templates, "Canon precedence for template use")

> Applicable, active, non-superseded PF10 addenda supersede conflicting PF-Canon only for the exact scope they address; otherwise follow PF-Canon. A formally approved bounded Product Owner rescope may supersede conflicting PF-Canon only for the exact decision it adjudicates.

Here, HDE Build Notes 2.7 is the applicable addendum for the scope it addresses (AD-1 to AD-6 and its overlaid clauses). Permanent canon governs everything else, and it agrees with 2.7's decisions (§17).

The corrective decisions are Product Owner-directed, so this plan also states what Plan Templates requires of an artifact that relies on a Product Owner decision:
- the exact decisions: AD-1 to AD-6 (§1; addendum 2.7);
- the work transferred: AD-4's gaps to WU-PR-05, the bind statements to WU-PR-08, the documentation to WU-DOC-01 (§18);
- the preserved boundaries and nonclaims: §5 and §12;
- the PF drain candidates: §18 "Stale documents".

## Canon relied on

Read on `main` at `79eac95`. `docs/pfcanon/` changed since cycle 1 only by PF10 (v13.5.6 → v13.5.7 → v13.5.8).

| Topic | Sources and sections |
| :- | :- |
| Plan authority, hold, Proceed, receiver contract | PR-20 — Create Detailed PR Implementation Plan — 100926.1 (read in full); HDE Governance (`docs/pfcanon/PF04-Canon-HDE-Governance-v2.8.7.md`) §9.1.1 and §9.1.2 (read in full); Plan Templates (`docs/pfcanon/PF27-Canon-Plan-Templates-v2.0.5.md`) "Canon precedence for template use" (read in full) |
| Overlays | PF10-HDE-Build-Notes v13.5.8 (`docs/pfcanon/PF10-HDE-Build-Notes-v13.5.8.md`): front matter §§1–9, cross-references, template, index, addenda 2.1 to 2.7 (read in full). Addendum records 2.6 (`docs/ephemeral/HDE-CRD-0002-WU-PR-03-PF10-build-notes-addendum-v1.0.md`) and 2.7 (`docs/ephemeral/HDE-CRD-0002-WU-PR-03-corrective-PF10-build-notes-addendum-v1.0.md`), read in full |
| AD-1 | HDE Architecture (`docs/pfcanon/PF02-Canon-HDE-Architecture-v2.4.6.md`) §0 "Intent & scope" ("Endpoint Catalog (single home; routing note)"), §1.3 in full, §3.2 to §3.5 in full; HDE Users Guide (`docs/pfcanon/PF29-Canon-HDE-Users-Guide-v1.0.2.md`) §1.1 in full; HDE Schemas & Artifacts (`docs/pfcanon/PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.6.md`) §8.8 in full; HDE-CLI-API-Vendor-Ref (`docs/pfcanon/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.3.md`) §5.6 in full |
| AD-2 | HDE-CLI-API-Vendor-Ref §5.4 and §5.5 in full; HDE Schemas & Artifacts §8.8 "Reader surface routes and distinct contracts (normative)"; HDE Mechanics Guide (`docs/pfcanon/PF14-Canon-HDE-Mechanics-Guide-v3.5.8.md`) §34 in full; HDE Governance "Dev/admin APP_ENV gating (dev/test/local only)" (both passages) |
| AD-3 | HDE-CLI-API-Vendor-Ref §5.4; HDE Mechanics Guide §34; HDE Build Checklist — Conjunction (`docs/pfcanon/PF09.4-Canon-HDE-Build-Checklist-Conjunction-v1.3.1.md`) Subtask HDE-CONJ001.1; Glow Infrastructure (`docs/pfcanon/PF07-Canon-Glow-Infrastructure-v2.3.3.md`) §2.2 "Documented client access vs service identity (names-only)" (read in full); Plan Templates line 1026 (the `127.0.0.1` template note); HDE Users Guide §4.1 (stale bind statement) |
| AD-4 | as the decision record's "Canon relied on" maps it; HDE Architecture §1.3, §3.2, §3.3 and §3.5 re-read in full here |
| AD-5 | Implementation Plan v1.1 §10; addendum 2.6 (RP-2, RP-3) and 2.7 AD-5; `AGENTS.md` "Release identity" and "HDE-EPIC040 admission addition" |
| AD-6 | `AGENTS.md` canon-first rule; HDE Governance §9.1.2 |
| Start-helper propagation (unchanged; CR-6) | HDE Architecture §3.8.1 in full (including "Current repository discrepancy"); HDE Mechanics Guide §5.6, paragraph "Dev Reader start helpers (APP_ENV propagation)" |
| Other search hits, classified | HDE Reality Audits (`docs/pfcanon/PF23-Canon-Reality-Audits-v1.2.2.md`) §5 "Adapter / HTTP Surfaces", lines 100–111: a dated reality-audit inventory, historical evidence and not a population rule; HDE Build Checklist — Separation (`docs/pfcanon/PF09.3-Canon-HDE-Build-Checklist-Separation-v1.1.7.md`) line 422: historical evidence that a test calls `/ops/writer/diagnostic`, which still passes because the route stays |
| In-flight documents | Specification v1.1 (in full); Implementation Plan v1.1 (in full) and review v1.1 (in full); instruction v1.0 (in full); plan v1.1 (in full); results v1.0 and v1.1 (in full); rescope review v1.0 (in full); PR-35 rescope request v1.0 and its prototype diff (in full); PR-35 rescope review v1.0 (in full); corrective decision record v1.0 and its handoff (in full) |
| Operative documentation | `AGENTS.md` (canon-first rule; closed rails; pytest readiness; sole Index/Mirror writer; no hand edits; endpoint catalog source of truth; PR descriptions; evidence attribution; truncation guardrail) |

## Checks run by this session

All in this session's scratchpad (a separate scratch clone of `79eac95`, never pushed), with the §4.4 environment:

| Check | Result |
| :- | :- |
| `url_map` enumeration of the three factories at `79eac95` | 53 pairs; catalog 23; 9 retired pairs, 5 of them catalogued (F-15) |
| Gate, run call, banner, CORS search, Flask `run` source, `python-dotenv` presence | F-16 to F-18 |
| Canon search (§16) | hits classified in §17 and "Canon relied on" |
| `tests/http/test_reader_a7_transport.py` before the cut | 27 passed |
| RC-1 (old `adapter/http_reader.py`, new tests) | 7 failed, 20 passed (as designed) |
| RC-2 (injected CORS header) | 6 of 6 CORS cases failed (as designed) |
| Cut, recompute, cutter `--check`, admission | exit 0; `d84d99e1… 45 1.3.0` |
| Convergence pass 1 (steps 2–10) | 35 of 36 exit 0; the exception is the F-25 harness error (`check_mirror_schema.sh` run through `bash`, exit 2, no write); the direct re-run exit 0 |
| Convergence pass 2 (steps 3–10) | 33 of 33 exit 0; diff digest identical to pass 1 (`a6fd148b…`); 61 paths; `summary:PASS` |
| Stale-binding sweep | no hit for `72fca4c3` or `64553c25` outside the excluded prefixes |
| Catalog and Mirror after convergence | 18 records; catalog = mirror; symlink kept; 27 labelled rows carry `d84d99e1…`; purity row unlabelled |
| Contract-inventory baseline | discovered 23 = baseline 23, byte-equal (F-23) |
| Classifier dry run (`79eac95` → prototype head) | exit 0; 68 paths; product, compat, db, evidence, release; 20 targets (F-24) |
| `python3 ci/checks/check_agents_md_citations.py`; `ci/checks/check_env_pins.sh` | exit 0 |
| Changed-test step (the 20 targets, one process) | 854 passed (147 s); clean tree |
| Product lane (ordering `--check`; four test paths incl. the architecture snapshot) | 77 passed; clean tree |
| Compat lane (`check_cli_help.sh`, serializer guard, emitter proof, ten test files) | 103 passed, 3 skipped, 2 xfailed; clean tree |
| DB lane (`check_direct_db_contract.py`; seven test paths) | 249 passed; clean tree |
| Evidence lane (seven read-only checks, `.sh` by path; six test files) | every check exit 0; 130 passed (572 s); clean tree |
| Release-lane tests (recompute; four test files) | 79 passed; clean tree |
| Attestation build and verify (`--require-clean`, external directory) | exit 0; `PASS`; `PR06R_B_FINAL_PASS`; `d84d99e1…`; `source_commit_exact: true` |
| `VERIFY.sh` with `APP_ENV=dev` (loopback runner) | exit 0; 12 of 12 tokens `_OK` |
| `VERIFY.sh` with `APP_ENV` unset | exit 2; `VERIFY_APP_ENV_NOT_DEV` |
| The 24 `_HTTP_READER_TEST_OWNERS` files plus the two script tests, `APP_ENV` unset | 804 passed; clean tree |
| Full `tests/` sweep (detached worktree) | 4,761 passed, 3 skipped, 2 xfailed, 0 failed (1,107 s); clean tree |
| TypeSafe scoring script (§21) | one send; HTTP 200 |
| `git apply --check` of the companion diff on `79eac95` | succeeds (7 files) |

Not executed: hosted CI and the Codex code review (PR-35's); the rails and qa lane commands (not selected; their tests ran in the sweep); a second attestation build. No live vendor, production or database call was made.
