---
artifact_type: PR_IMPLEMENTATION_PLAN
artifact_id: HDE-CRD-0002-WU-PR-03-PR-IMPLEMENTATION-PLAN
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-implementation-plan-v1.1.md
artifact_version: "1.1"
artifact_state: AWAITING_PO_PROCEED
hold_label: "ASK OK? — PR IMPLEMENTATION PLAN"
plan_cycle: 1 (first plan cycle for this work unit; v1.1 is the complete successor of the suspended v1.0 after the approved rescope)
predecessor: docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-implementation-plan-v1.0.md (v1.0, PENDING; blob 750c700cb325; 83,667 bytes; preserved unchanged; landed by amthorn78/glow-hdengine-v2#640 at 852370c)
companion: docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-implementation-plan-v1.0-prototype.diff (blob 35e118cd902a; 72,428 bytes; preserved unchanged; it already carries the approved design and applies cleanly to 150feab; no successor diff is issued; §4.4)
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-03
work_unit_title: "Public, dev and CLI surfaces (PR; Conjunction; S02, S07, S09, S10, S15, S18)"
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-instruction-v1.0.md (v1.0, INSTRUCTION_READY; blob 74e8f158b48d; 62,527 bytes; landed by amthorn78/glow-hdengine-v2#639 at 20f16d0; overlaid for the clauses review §7 names by addendum 2.6)
IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (v1.1; blob abffa2ccbd44; immutable)
PLAN_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (v1.1, IA-30 INITIAL_APPROVE, "ASK OK."; blob 0cc0276524b2)
SPECIFICATION_ID: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (v1.1, SPECIFICATION_APPROVED, "ASK OK."; blob c4802a5a7fa3)
IMPLEMENTATION_AUDIT_ID: docs/ephemeral/HDE-CRD-0002-implementation-audit-v1.0.md (v1.0, AUDIT_COMPLETE; blob b39ac9f276db) — lineage only
RESCOPE_REQUEST_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-03-rescope-request-v1.0.md (v1.0; blob 8fa8d85b6295; decided)
RESCOPE_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-03-rescope-review-v1.0.md (v1.0, RS-20, decision APPROVE, "ASK OK."; blob e3f50f162130; landed by amthorn78/glow-hdengine-v2#641 at 150feab)
REMEDIATION_REVIEW_ID: none
AUTHORING_CONTEXT: APPROVED_BASE_WITH_OVERLAYS
immutable_approved_base: Specification v1.1 (approved) → Implementation Plan v1.1 + review v1.1 (approved) → PR instruction v1.0 (issued by the IA under PR-10). None is rewritten
applicable_pf10_overlays: PF10 addendum 2.2, "Downstream work" item for WU-PR-03 with its "Binding requirements" for the contract-inventory generator (ID-4); addendum 2.3 (reviewer chain without the Codex security review); addendum 2.5 (carried LR-O1 to LR-O3); the new addendum record 2.6 (proposed number; docs/ephemeral/HDE-CRD-0002-WU-PR-03-PF10-build-notes-addendum-v1.0.md; blob 345985d7d9c8): RP-1 and RP-3 approved deltas, RP-2 in scope. Addendum 2.1 governs §20 only
effective_baseline: approved base + applicable PF10 overlays = the base above + addenda 2.2, 2.3 and 2.5 + addendum record 2.6, with the binding conditions B-1 to B-12 of the rescope review §7
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.6.md (v13.5.6, effective 2026.10.14; blob 9c5468fb69e4; 69,689 bytes; sha256 8663ab94289adae036dbb07af8b302d1b7f3b1d2a1b57dfb7bbd664a5b98bec0). Resolved afresh on main at 150feab: still the unique controlled PF10; unchanged since ad11821; addendum 2.6 is not yet published in it (its numbering and publication are the Product Owner's) and is applied from its docs/ephemeral/ record
pf10_addendum_paths: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.6.md §2.2 ("Approved delta", "Binding requirements", "Affected surfaces / Downstream work"), §2.3 (Rules 1–5), §2.5 (carried items); docs/ephemeral/HDE-CRD-0002-WU-PR-03-PF10-build-notes-addendum-v1.0.md (record 2.6); §2.1 for §20
pf10_addendum_created: none (PR-20 is not a qualifying approval prompt)
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
session_disposition: INITIAL_DEDICATED_ASSIGNMENT (the dedicated HDE-CRD-0002 WU-PR-03 PR engineering session, created by Nathan / Product Owner; resumed in its PR-20 planning context by the RS-20 return)
role_session_ref: NOT_YET_ASSIGNED (assignment owner Nathan / Product Owner); authoring session https://claude.ai/code/session_01GC6jqu4Lczzk7PR7QGXSTJ (v1.0 and v1.1)
author: dedicated HDE-CRD-0002 WU-PR-03 PR engineering session (PR-20)
return_owner: the continuing whole-change HDE-CRD-0002 Implementation Agent (PR-40 after the merge; RS-20 for any further rescope; PR-10 for an instruction defect)
prompt: PR-20 — Create Detailed PR Implementation Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb819fbea5dcd966a750ba; page state as of 2026-10-12T02:29:47Z; read in full)
prompt_release: GCFPE-20261009.1 / 100926.1
created_at: 2026-10-14T03:05:07Z
repository_baseline: origin/main 150feabeee3d0c9a4d9012198cf854db653177f4 (tree cc6f92f8a1ca; #641). git diff 20f16d0..150feab touches only docs/ephemeral/ (#640, #641), so every code, tool and evidence fact measured at 20f16d0 holds; the companion diff applies cleanly (git apply --check)
canon_conflict_register: CR-1, CR-2, CR-3 APPROVED_AS_CHANGED (Thoth); CR-4 APPROVED and CR-5 APPROVED_AS_CHANGED (Product Owner, docs/ephemeral/HDE-CRD-0002-WU-PR-01-po-disposition-cr-4-cr-5-v1.0.md); CR-6 APPROVED, alternative (a) (the IA through RS-20, rescope review v1.0 §12) (§16)
next_prompt: PR-30 — PR Implementation Proceed — 100926.1 (https://app.notion.com/p/3f44590a05eb8148a538f5c80588db14), on Nathan's Proceed for this exact plan
---

# HDE-CRD-0002 WU-PR-03 — Detailed PR Implementation Plan v1.1

## 1. State and authority

**AWAITING_PO_PROCEED.** Held at `ASK OK? — PR IMPLEMENTATION PLAN` (HDE Governance §9.1.1).

This is the complete, executable plan for WU-PR-03: S02, S07, S09, S10, S15 and S18, the ID-3 classifier registration, the ID-4 contract-inventory baseline refresh, the same-version release refresh with its governed-evidence convergence, and the approved rescope recorded by addendum 2.6. It is the complete successor of the suspended plan v1.0, which stays preserved.

What changed from v1.0. The RS-20 review (`docs/ephemeral/HDE-CRD-0002-WU-PR-03-rescope-review-v1.0.md`, decision APPROVE) decided both boundary findings and confirmed the third item:
- **RP-1 approved.** `scripts/dev_start_reader.sh` stays unchanged and keeps propagating `APP_ENV` exactly, as canon requires. IF-10's last clause, acceptance (2)'s last clause, contract E-6 and the instruction clauses that stated the default read as review §7.1 B-2 states. `VERIFY.sh` refuses without an explicit `APP_ENV=dev` (B-3). The runner item (§6.4) is no longer blocked.
- **RP-3 approved.** `tools/evidence/update_evidence_index.py` joins the bounded files for exactly one deleted roster line (B-7). The updater's own runs remove the purity-report row's stale label (B-8). LR-O2 applies (B-9). The convergence item (§6.10) is no longer blocked.
- **RP-2 confirmed in scope** (step 3b; PD-15).
- **CR-6 APPROVED,** alternative (a): canon governs.

§5A maps every binding condition B-1 to B-12 to the section of this plan that carries it. Nothing else in v1.0 changes: its design, prototype, rehearsals and final full sweep stand, and the review independently reproduced the decisive results (review §3.3, §4.2). The prototype diff already contains the approved design and applies cleanly to `150feab`.

Authority:
- Only Nathan's `PR Implementation Proceed` (PR-30) for exactly `docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-implementation-plan-v1.1.md` (v1.1) authorizes implementation. Only Nathan merges.
- This plan authorizes no implementation, merge, publication, Ops, QA, acceptance or closure. It changes no canon and creates no PF10 addendum.

## 2. Identity and lineage

| Item | Identity |
| :- | :- |
| Change | CRD HDE-CRD-0002 |
| Work unit | WU-PR-03 (Plan v1.1 §7 "WU-PR-03 — Public, dev and CLI surfaces (PR; Conjunction)") |
| Requirements | S02, S07, S09, S10, S15, S18; EC-2, EC-4, EC-6, EC-8; IF-6, IF-10, IF-11; the same-version refresh |
| Binding IA decisions | instruction §4 ID-1 (catalog population), ID-2 (harness retirement), ID-3 (classifier registration), ID-4 (contract-inventory baseline) |
| Approved rescope | rescope review v1.0 (RS-20, APPROVE; binding conditions B-1 to B-12) and addendum record 2.6: RP-1 (start helper propagates `APP_ENV`), RP-3 (one roster line), RP-2 (step 3b, in scope); CR-6 APPROVED |
| Upstream units | WU-PR-01 accepted (PF10 addendum 2.4); WU-PR-02 accepted (addendum 2.5) |
| Downstream | WU-PR-04 and WU-PR-05 refresh from this unit's `release_id`; WU-PR-05 (S19) reads the surfaces landed here; WU-PR-06 reads the ID-3 registrations; WU-PR-08 and WU-DOC-01 own the stale documents (§17); QA-10 needs S02 and S10 |
| Phase | Conjunction |
| Live QA class | S02, S07, S10 functional-feature; S15 catalog entries only; S09, S18 not production-affecting (Specification table; Plan §6) |

## 3. Sources read

Read completely by this session:
- PR-20 — Create Detailed PR Implementation Plan — 100926.1 (Notion, page state 2026-10-12T02:29:47Z) and PR-30 — PR Implementation Proceed — 100926.1 (page state 2026-10-12T02:30:08Z), for the receiver contract.
- PR instruction v1.0 (all 20 sections).
- For v1.1: the rescope review v1.0 (in full, including §7 B-1 to B-12, §8, §10, §11, §12), the addendum record 2.6 (in full), and this session's rescope request v1.0 and plan v1.0.
- Implementation Plan v1.1 §3, §4, §5, §7 (common paragraph; WU-PR-03 block), §10, §11, §12, §13, §14, §15.
- PF10 v13.5.6 addenda 2.2, 2.3, 2.5.
- HDE-CLI-API-Vendor-Ref (`docs/pfcanon/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.3.md`) §5.1.7, §5.2 item 1, §5.4 in full, §5.5 "Errors" and "Method and subpath handling", §5.6 in full; every `Allow` passage (admin bundle §5.10; §5.1.0 line 2071; §5.2 line 2327).
- HDE Schemas & Artifacts (`docs/pfcanon/PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.6.md`) §8.8 in full.
- HDE Governance (`docs/pfcanon/PF04-Canon-HDE-Governance-v2.8.7.md`) §9.1.1 (hold label; Proceed per detailed PR plan).
- Code and data: `adapter/factory.py`, `adapter/wsgi.py`, `adapter/app.py`, `adapter/http_reader.py` (blueprints, gates, helpers, `create_app`), `engine/http/compat_handler.py`, `engine/presenter/emitter.py`, `adapter/env_guard.py::_compute_env_mode`, `engine/cli/main.py` lines 74–82, `tools/evidence/generate_a7_transport_proofs.py`, `tools/evidence/generate_hdapi_v2_contract_inventory.py` (baseline and loci), `tools/evidence/hdapi_v2_boundary_analyzer.py` (record discovery and baseline comparison), `tools/evidence/update_evidence_index.py::_validate_epic038_pr02_semantics`, `ci/checks/classify_ci_changes.py` (registries, `_lanes_for_path`, `changed_test_targets`), `.github/workflows/ci.yml` (setup, changed-tests step, lanes), `scripts/dev_start_reader.sh`, `VERIFY.sh`, `dev/reader_harness/*`, `docs/ENDPOINTS_CATALOG.json`, `pytest.ini`, `.gitignore`, `Procfile`.
- Tests: `tests/http/test_endpoint_catalog.py`, `tests/http/test_reader_a7_transport.py`, `tests/adapter/test_gate_auth.py`, `tests/evidence/test_architecture_snapshot.py`, the coverage and registry pins of `tests/evidence/test_rails_ci_workflow_integration.py`, `tests/evidence/test_hdapi_v2_contract_inventory.py` (baseline fixtures).
- Documents in scope: `docs/acceptance/reader_a7_crib.md`, `docs/server/reader_v1.md`, `docs/ADAPTER_009.md` (lines 170–178), `ARCHITECTURE.md` (lines 1–40), `docs/CLI_commands.md` line 25.

## 4. Repository baseline (measured at `20f16d0`; re-verified at `150feab`)

`git diff 20f16d0..150feab` touches only `docs/ephemeral/` (#640: request, plan v1.0, prototype diff; #641: review, addendum record, checkpoint, handoff). Every code, tool, test and evidence fact below therefore holds at `150feab`, and `git apply --check` of the companion diff succeeds there. `docs/pfcanon/` is unchanged since `ad11821`.

### 4.1 Instruction facts re-verified

Every fact of instruction §5 that this plan relies on was re-read at `20f16d0`; none differs. In particular:
- **Served set.** The three factories serve 53 distinct `(path, method)` pairs; 10 are catalogued, 43 are not, 28 of them excluding OPTIONS (instruction §5.2 "28" confirmed). Table §5.2 of the instruction matches the `url_map` exactly.
- **`/reader` gate.** `adapter/http_reader.py` line 603: unset `APP_ENV` serves.
- **Contract-inventory baseline.** 21 records; `pprint.pformat(tuple(asdict(r) for r in records))` over `discover_route_registrations(ADAPTER_BOUNDARY_CANONICAL_ADAPTER_LOCI)`, filtered as the analyzer filters public supported non-constructor records, reproduces the tracked literal byte for byte (94,058 characters). The rebuild in ID-4 is therefore mechanical.
- **Classifier refusals.** `VERIFY.sh`, `dev/reader_harness/{app.py,__init__.py}` and `scripts/dev_start_reader.sh` refuse as instruction §5.8 states.

### 4.2 Facts this session established (not in the instruction)

| ID | Fact | Effect on the plan |
| :- | :- | :- |
| F-1 | `docs/ENDPOINTS_CATALOG.json` is a tracked **symlink** to `../artifacts/audit/ENDPOINTS_CATALOG.json` (mode 120000, 41-byte target). The A7 owner writes through it; only `artifacts/audit/ENDPOINTS_CATALOG.json` changes bytes; the docs path's blob is unchanged | "Catalog equals mirror byte for byte" holds by construction. PR-30 keeps the symlink (PD-16) |
| F-2 | `tools/evidence/update_evidence_index.py::_validate_epic038_pr02_semantics` calls the A7 owner's `validate_catalog` on the tracked catalog, and the config publisher runs the updater | With the new validator, every updater run refuses (`aux narrative catalog invalid`) until the A7 owner has rewritten the catalog. Plan v1.1 §10 runs the updater at step 5 and A7 at step 7, so its literal order fails for this unit (rehearsal 1, §4.3). PD-15 moves the A7 owner write before the gate |
| F-3 | `error_envelope("invalid_json")` emits `code: "ERR_COMPAT_INVALID_JSON"` (observed: compat GET with body → 400, `{"code":"ERR_COMPAT_INVALID_JSON",…}`, `no-store`, no ETag) | S18 text names both the alias and the emitted code (PD-18) |
| F-4 | Werkzeug 3.1.9 builds `MethodNotAllowed.valid_methods` from a set, so `Allow` order varies with the hash seed | The new 405 handler sorts the methods (PD-2). The factory's existing compat 405 `Allow` keeps Flask's order (byte-identity kept; OBS-P3-2) |
| F-5 | `adapter/http_reader.py::create_app`'s `after_request` reads `getattr(resp, "request", None)`; a Flask response has no `request`, so its `/internal/` ETag strip and its `/ops/writer/diagnostic` Content-Length rule never fire (probe: a test `/internal/` route's ETag survives in that factory and is stripped in `adapter/factory.py`) | Kept unchanged (instruction §9.1 "keep"); recorded as OBS-P3-1 for the IA and WU-PR-05 |
| F-6 | `.body200.json` and `.code304.txt` at the repository root are tracked, and the old `VERIFY.sh` overwrote them | The new `VERIFY.sh` writes only to a temporary directory (PD-8), so a run leaves the tree clean. The two files stay untouched (OBS-P3-6) |
| F-7 | The old `VERIFY.sh` exit test (lines 106–111) never sees the `_OK`/`_FAIL` tokens its Python blocks print, and reads standard input | PD-8 makes the exit status follow the tokens; recorded as a kept-and-repaired check |
| F-8 | `docs/contracts/reader_v2_public_bytes.md` line 19 states the HTML 404 limitation S02 removes | Outside §6 bounds; stale-document list (§17) |
| F-9 | After the refresh, `artifacts/core/purity/purity_report.json` is byte-stable (it binds engine-core source digests, not the release), so its Mirror row keeps `notes: "current-release capture: release 1.3.0, release_id 52be4558…"`. A full sweep then fails three tests of `tests/evidence/test_evidence_index_missing_state.py` (evidence lane), all on that row | RP-3, approved (addendum 2.6; review §7.2 B-7 to B-10): the one roster line leaves the updater; the updater unlabels the row |
| F-10 | `README.md` line 13 carries the current `release_id` | The stale-binding sweep reports it; WU-DOC-01 owns `README.md` (§17) |
| F-11 | Canon requires dev Reader start helpers to propagate `APP_ENV` exactly and never default it (HDE Architecture §3.8.1 "Repo-side start-helper posture"; HDE Mechanics Guide §5.6 "Dev Reader start helpers (APP_ENV propagation)" and §34; Glow Infrastructure §8.1; Conjunction checklist HDE-CONJ001.4; Glow QA Guide §13.9). The current `scripts/dev_start_reader.sh` conforms. EC-4's default would not; verified in scratch: with EC-4 an unset `APP_ENV` serves `/reader` 200 | RP-1, approved (addendum 2.6; review §7.1 B-1 to B-6): the script stays unchanged |
| F-13 | The boundary analyzer (`_adapter_routes_without_presenter`) rejects a factory error handler that returns the routing exception (`return err`) or calls a presenter helper defined in another module (`governed_not_found_response` imported from `adapter/http_reader.py`; `compat_error_response`). It accepts a helper nested in the same `create_app` that calls `emit_public` (the existing `_compat_error_response` pattern). Observed: the first prototype failed 19 tests of `tests/evidence/test_hdapi_v2_contract_inventory.py` with `ADAPTER_BOUNDARY_CHECK_FAILED:presenter_emitter_inspected,no_presenter_bypass`; the final design returns an empty finding list | §6.1 design (PD-1 revised): one nested presenter helper per factory |
| F-14 | Earlier tests in a full sweep reload the `adapter` package, after which `import adapter.factory` inside a test function leaves `adapter.factory` unset (191 `AttributeError` failures in the first sweep; none in an isolated run) | PD-23: new tests bind factory functions with `from adapter.factory import create_app as …` |
| F-12 | `VERIFY.sh` extracts the ETag with `awk 'BEGIN{IGNORECASE=1}/^etag:/…'`; `IGNORECASE` is gawk-only, so under the container's `/usr/bin/awk` the ETag is empty and `READER_304_STATUS`, `READER_304_EMPTY_BODY` and `ETAG_INVARIANCE` fail (observed once F-7 made the exit status real) | PD-20: `awk 'tolower($1)=="etag:"{print $2}'` |

### 4.3 Prototype (this session; scratch only, never pushed)

A detached worktree of `20f16d0` in the session scratchpad, CPython 3.12 with CI's install (`setuptools>=68`, `wheel`, `requirements.txt`, `requirements-dev.txt`, `-e .`), pytest 8.4.2, `ruby` at `/usr/local/bin/ruby`, closed rails (`LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`), vendor and database keys unset. The design of §6 was implemented there; its source, test and document diff is the companion file (§4.4).

Before the refresh (member bytes final, manifest not cut):
- A request matrix over 22 requests × 3 factories × `APP_ENV` in {`dev`, unset}, compared with `main`: every compat and `api_bp` response is byte-identical (31 keys per environment); unknown paths and unrouted methods change from Flask HTML to the governed envelope on `adapter/factory.py` and `adapter/http_reader.py`; `adapter/wsgi.py` unknown-path responses are unchanged; `GET`/`HEAD /reader` with `APP_ENV` unset change from 200 to 403. With member bytes changed and no cut, `/reader` answers 503 `ERR_M10_MANIFEST_MISMATCH` and `hdctl showcompat` answers `MANIFEST_MEMBER_HASH_MISMATCH` — the admission refusal the refresh removes.
- `ci/checks/check_cli_help.sh` exit 0; `hdctl --help` shows the new summary.
- ID-4: discovered 23 records, baseline 21; after the rebuild both 23 and equal in order (§6.8).
- Classifier on the prototype's changed paths (first design, 22 paths; final candidate, 82 paths with the regenerated evidence): reason `selected_lanes`, all seven lanes, 164 changed-test targets; the four ID-3 paths classify (§6.7).

The refresh (§6.10): the cut gave `1.3.0`, 45 members, rehearsal `release_id` `d041ee18dbd84834e4cf4e304b71322a5d2e0d1dc35ecd7d2b52bd838fc6d0c4`; `release_id_recompute.py --check-manifest-only` and the cutter `--check` exit 0; two manifest rows change (the two members). This value is a rehearsal value only: PR-30's own bytes fix the real one.

Rehearsal 1 (Plan v1.1 §10 order, steps 3–10, run twice): pass 1 steps 5 (updater and `--check`) and 6 (config family) exit 1 with `ValueError: aux narrative catalog invalid` (F-2); every later step passes once step 7 has rewritten the catalog; pass 2 passes every step. Because pass 1 skipped the config family, the two passes differ. This is the defect PD-15 corrects.

Rehearsal 2 (the order of §6.10, from the post-cut state, run twice): every step 3 to 10 exits 0 on both passes (64 of 64 runs); the second pass reproduces the first byte for byte (identical diff digest); sanity `summary:PASS` both times; goldens 8 of 8 `match`. The full sweep that followed found the three defects F-9, F-13 and F-14 (below).

Rehearsal 3 (the final design of this plan: the analyzer-accepted handlers of §6.1, the PD-23 test imports, the `VERIFY.sh` refusal (B-3), and the RP-3 roster line (B-7)):
- Reset to `20f16d0` and re-applied the source set.
- The cut gives rehearsal `release_id` `72fca4c341d871dc75a828140ee1494714b322a13656bac93f66164060ea390f` (45 members, `1.3.0`; recompute and cutter `--check` exit 0).
- Steps 3 to 10 run twice in §6.10 order: 64 of 64 runs exit 0; the two passes are byte-identical; sanity `summary:PASS` twice; goldens 8 of 8 `match`.
- The step-11 sweep finds only `README.md` and the frozen HDE-EPIC040 QA and Ops records; the purity-report row is unlabeled (RP-3).

Tests on the converged prototype: two full `tests/` sweeps, closed rails, `APP_ENV=dev`, `ruby` on `PATH`, run in the prototype worktree, each ending with an empty untracked and unstaged status.
- **First sweep** (after rehearsal 2, the first design): 213 failed, 4,531 passed, 3 skipped, 2 xfailed (904.7 s). Every failure is explained and fixed by the final design:
  - 191 in `tests/http/test_endpoint_catalog.py` (F-14; fixed by PD-23);
  - 19 in `tests/evidence/test_hdapi_v2_contract_inventory.py` (F-13; fixed by the §6.1 design);
  - 3 in `tests/evidence/test_evidence_index_missing_state.py` (F-9; fixed by RP-3's roster line).
- **Final sweep** (rehearsal 3 state, the final design): **4,747 passed, 3 skipped, 2 xfailed, 0 failed** (871.1 s). Collected counts:
  - `tests/scripts/test_dev_start_reader.py` 10;
  - `tests/http/test_endpoint_catalog.py` 201 (8 existing);
  - `tests/http/test_reader_a7_transport.py` 16;
  - `tests/cli/test_cli_usage_and_errors.py` 7;
  - `tests/evidence/test_hdapi_v2_contract_inventory.py` 300;
  - `tests/evidence/test_evidence_index_missing_state.py` 62;
  - `tests/evidence/test_http_reader_ci_ownership.py` 4;
  - `tests/evidence/test_rails_ci_workflow_integration.py` 138.
- **Other runs on the final state:**
  - `VERIFY.sh` with `APP_ENV=dev`: 12 tokens, all `_OK`;
  - `VERIFY.sh` with `APP_ENV` unset: `VERIFY_APP_ENV_NOT_DEV`, exit 2;
  - `ci/checks/check_cli_help.sh` exit 0; `generate_cli_conformance_artifacts.py --check` exit 0;
  - the classifier on the final 82 candidate paths: all seven lanes, 164 targets.

### 4.4 Prototype diff (companion file)

`docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-implementation-plan-v1.0-prototype.diff` (preserved, unchanged) is the prototype's diff from `20f16d0`, restricted to the 21 source, test and document files of §7.1 (the manifest and every regenerated governed artifact are excluded: PR-30 produces them with their owners). It carries the approved design:
- no `scripts/dev_start_reader.sh` hunk (B-1);
- the `VERIFY.sh` refusal (B-3);
- exactly one deleted line in `tools/evidence/update_evidence_index.py` (B-7).

`git apply --check` succeeds on `150feab`, and the review applied it at `852370c` and reproduced the decisive results. PR-30 may apply it as its starting point, but owns the implementation: it re-reads every hunk against this plan and re-runs §10 on the real branch. Where the diff and this plan differ, this plan governs and the difference is a defect PR-30 corrects. No successor diff is issued, because the design did not change.

## 5. Scope

In scope (instruction §6; Plan v1.1 §7 WU-PR-03 "Deliverables"):
- S02: app-level 404/405 handlers on `adapter/factory.py` and `adapter/http_reader.py::create_app` (IF-11).
- S10: the explicit-`dev` gate on `GET /reader` (IF-10); the start helper stays unchanged and propagates `APP_ENV` (addendum 2.6, B-1, B-2); the runner propagation test (B-4).
- S07: the `showcompat` help string; the `docs/CLI_commands.md` known-gap sentence (EC-6).
- S09: retire `dev/reader_harness/`; repoint `VERIFY.sh`, the crib and `docs/server/reader_v1.md`; two docstrings (EC-2; ID-2).
- S15: the 13 new catalog rows, the `CLASS` set and the validator in the A7 owner; the route-enumeration test (IF-6; EC-8; ID-1).
- S18: `docs/ADAPTER_009.md` line 174; `ARCHITECTURE.md` emitter and routing statements.
- ID-3: the classifier registration and one owner test. ID-4: the baseline data.
- RP-3: the one roster line in `tools/evidence/update_evidence_index.py` (addendum 2.6, B-7).
- The same-version refresh and every evidence family it regenerates, by owners only.
- The PR result record under `docs/ephemeral/`.

Out of scope (instruction §7): no route added or removed; no public contract, payload, flag or transport change; no change to compat shaping or the production Reader's governed 405; no version bump or admission-constant change; no canon edit or PF10 addendum; no hand edit of a governed artifact; no `AGENTS.md`, `README.md`, `CHANGELOG.md`, `.env.example` or S17 edit; no `adapter/wsgi.py`, `engine/http/compat_handler.py`, `engine/presenter/**`, `engine/config/registry_loader.py` or boundary-analyzer change; no updater change except the one RP-3 roster line (B-7); no `scripts/dev_start_reader.sh` change (B-1); no change to the `0.0.0.0` bind or the production mount of the dev blueprint (OBS-W3-1); no skipped, disabled, `xfail` or quarantined test; closed rails throughout.

## 5A. Applied rescope (addendum 2.6): binding-condition map

| Condition (review §7) | What it requires | Where this plan carries it |
| :- | :- | :- |
| B-1 Script | `scripts/dev_start_reader.sh` not changed; base-to-head diff empty | §5, §6.4, §7.1, §7.3, §8 step 8, §10 item 8 |
| B-2 Overlaid clauses | IF-10 last clause; EC-4 not implemented and its documentation clause restated; acceptance (2) last clause; the Deliverables item withdrawn; instruction §5.5 last sentence superseded; instruction §6 rows (script, documents, tests); E-6; §9 items 5 and 6; §10 S10 evidence row — each as review §7.1 B-2 words it | §5A.1 (verbatim), §6.4, §6.9, §9, §12 |
| B-3 `VERIFY.sh` | refuses unless the caller supplies exactly `APP_ENV=dev` (`VERIFY_APP_ENV_NOT_DEV`, effective value or `<UNSET>`, exit 2, before any runner starts); otherwise passes `APP_ENV` unchanged; no default anywhere in the script | §6.4, §7.1 |
| B-4 Owner test | `tests/scripts/test_dev_start_reader.py` stays the ID-3 owner; proves dev serves, unset refuses with `<UNSET>`, empty/`test`/`local`/`prod` kept and refused, `VERIFY.sh` passes with `dev` and refuses (unset, empty, `test`) with exit 2; needs `bash` and `curl` | §6.9, §10 |
| B-5 Documents | `docs/server/reader_v1.md` and `docs/acceptance/reader_a7_crib.md` state `APP_ENV=dev scripts/dev_start_reader.sh` and that the script never defaults `APP_ENV`; no other document changes for RP-1 | §6.4 |
| B-6 Unchanged | the `/reader` gate design, the catalog `env_gate`, acceptance (2)'s refusal set, IF-6, IF-11, the members | §6.2, §6.5 |
| B-7 Locus | one deleted line `"artifacts/core/purity/purity_report.json",` in `CURRENT_RELEASE_CAPTURE_PATHS` (22 paths remain); nothing else in the updater; instruction §5.7 (c) overlaid for this path only | §6.10, §7.1, §7.3, §8 step 8 |
| B-8 Publication by the updater | the label goes through the updater's own runs (step 5, then step 8); afterwards the purity rows have no `notes`, every other roster row carries the new label, step 11 finds no purity hit | §6.10, §12 |
| B-9 LR-O2 | the full `tests/` sweep under closed rails with `ruby`, ending with a clean tree; counts in the result record | §10 item 4, §12, §17 |
| B-10 Honest record | the result record states the roster change, its reason and the one row; nonclaim that the purity report is not a release-bound capture; cites the review; not a modification of WU-PR-02's accepted delivery | §12 |
| B-11 Unchanged obligations | everything else in instruction v1.0, the preserved v1.0 work and addenda 2.2, 2.3, 2.5 | throughout |
| B-12 New boundary | any further change outside the extended bounds is a new finding through the rescope lane | §14 RK-7 |

### 5A.1 Overlaid clauses as they now read for WU-PR-03 (review §7.1 B-2; verbatim)

- **IF-10, last clause** (Plan v1.1 §5; instruction §4): "`scripts/dev_start_reader.sh` propagates `APP_ENV` exactly as the caller supplies it, including unset and empty, and never defaults it; the canonical start command supplies `APP_ENV=dev`."
- **EC-4** (instruction §4): not implemented. Its documentation clause: `docs/server/reader_v1.md` states the start command `APP_ENV=dev scripts/dev_start_reader.sh` and that the script never defaults `APP_ENV`.
- **Acceptance (2), last clause** (Plan v1.1 §7; instruction §10): "`scripts/dev_start_reader.sh` with `APP_ENV=dev` starts a serving runner; with `APP_ENV` unset or empty it propagates that state and the runner refuses `GET /reader` (403 `ERR_READER_FORBIDDEN`)."
- **Deliverables item** "`scripts/dev_start_reader.sh` (default `APP_ENV=dev`)": withdrawn. The script is not a deliverable; its owner test is.
- **Instruction §5.5, last sentence:** superseded. After S10, an unset `APP_ENV` starts a runner whose `/reader` refuses; canon requires that, and the canonical start command supplies `APP_ENV=dev`.
- **Instruction §6:** the `scripts/dev_start_reader.sh` row reads "unchanged (canon: propagate exactly)"; in the documents row, "S10 gate and runner default" reads "S10 gate and the start command with `APP_ENV=dev`"; in the tests row, "the runner-default test" reads "the runner propagation test".
- **Contract E-6** (instruction §8): "`/reader` served only for `APP_ENV=dev`. The runner propagates `APP_ENV` exactly and the caller supplies `dev`. `VERIFY.sh` uses the canonical runner and requires `APP_ENV=dev`."
- **Instruction §9 item 5:** "defaulting `APP_ENV=dev`" reads "with the caller's `APP_ENV=dev`, refusing otherwise (B-3)". **Item 6's example** reads: a test that runs the script with `APP_ENV` unset and observes propagation and the refusal.
- **Instruction §10, S10 evidence row:** "the runner-default test" reads "the runner propagation test".
- **Instruction §5.7 (c),** for `artifacts/core/purity/purity_report.json` only: that path leaves the roster (B-7). For any other roster capture, a stale label after a refresh stays a finding to the IA, never a roster edit.

## 6. Design

### 6.1 S02 — governed not-found envelope (IF-11; E-2)

Each changed factory emits the envelope through a helper nested in its own `create_app` that calls `emit_public` directly. That is the shape the boundary analyzer accepts (F-13), as it already accepts `adapter/http_reader.py`'s `_compat_error_response`.

- **`adapter/http_reader.py::create_app`** (member):
  - a nested `_governed_error_response(err)` builds `emit_public(error_envelope("ERR_NOT_FOUND"))` with the routing status `err.code`, `Cache-Control: no-store` and `application/json; charset=utf-8`;
  - for a 405 with `err.valid_methods` it sets `Allow` to the sorted, comma-joined methods;
  - it pops `ETag` and `Content-Encoding` and sets `Content-Length`;
  - the two handlers are renamed `_governed_not_found` / `_governed_method_not_allowed`. The compat branch (`request.path.rstrip("/").startswith("/api/compat/v1")` → `_compat_error_response(status)`) is unchanged; `return err` becomes `return _governed_error_response(err)`;
  - `after_request` is unchanged; no module-level function is added.
- **`adapter/factory.py`**:
  - imports `Response`, `error_envelope` and `emit_public`;
  - a nested `_not_found_envelope_response(status, allow)` has the same body as `engine.http.compat_handler._writer_payload` for `ERR_NOT_FOUND`;
  - `@app.errorhandler(404)` `_governed_not_found` returns `_not_found_envelope_response(404, None)` for every path; a compat 404 is byte-identical to the former conversion, which never set `Allow` on a 404;
  - `@app.errorhandler(405)` `_governed_method_not_allowed` returns, on a compat path, `_not_found_envelope_response(405, err.get_response().headers.get("Allow"))` — Flask's own `Allow`, exactly what the `after_request` conversion read (HDE-CLI-API-Vendor-Ref §5.5 "Errors") — and elsewhere `_not_found_envelope_response(405, ", ".join(sorted(err.valid_methods or ())))`;
  - the existing `after_request` is unchanged. Its compat-conversion branch stays as written, although 404/405 no longer reach it as HTML.
- `adapter/wsgi.py` is not changed: it already answers unknown paths with the envelope (its 405 has no `Allow`; OBS-P3-3).
- HEAD on an unknown path carries no body (Werkzeug suppresses it) and keeps the headers; OPTIONS on an unknown path is 404.
- **Unchanged by construction:**
  - `api_bp` answers its own methods before routing fails (its views and `_refuse_unrouted_methods`);
  - unprefixed `POST /reader` has its view;
  - compat responses keep their bytes and headers.
- **Proof.** The request matrix on the final design: 31 compat and `api_bp` keys per environment identical to `main`, and every response identical to the first prototype's (§4.3).

### 6.2 S10 — explicit-`dev` gate (IF-10)

`adapter/http_reader.py` gains, beside `_select_reader_version`:

```python
def _reader_dev_env_explicit() -> bool:
    raw_app_env = os.environ.get("APP_ENV")
    return raw_app_env is not None and raw_app_env.strip().lower() == "dev"
```

and `reader_v1` replaces `if os.environ.get("APP_ENV", "dev") != "dev":` with `if not _reader_dev_env_explicit():`. Normalization follows `_dev_admin_gate` (strip, lower); only `dev` serves. The order is unchanged: `v` validation (400 `ERR_READER_INVALID_VERSION`) precedes the gate (403 `ERR_READER_FORBIDDEN`). HEAD runs the same view. `_dev_admin_gate` and the conjunction and sampler routes are not changed.

### 6.3 S07 — help text (EC-6)

`engine/cli/main.py` line 79 becomes `help="Emit the canonical magic10_compat_result.v1 document for a pair (stdin or files); Reader v1 bytes only via --dump-reader",`. The frozen `artifacts/cli/help/*` family and its `FROZEN_SHA256` stay byte-unchanged; the result record carries the nonclaim that it captures the earlier help text. `docs/CLI_commands.md` line 25 loses only the sentence beginning "Known gap:".

### 6.4 S09 — harness retirement, runner, `VERIFY.sh`, documents (EC-2, EC-4; ID-2)

- `git rm dev/reader_harness/app.py dev/reader_harness/__init__.py`. `dev/__init__.py` and `dev/.env.codex` stay.
- **`scripts/dev_start_reader.sh` — unchanged (B-1; PD-7).** It already exports `APP_ENV` only when the caller supplies it, displays `<UNSET>` otherwise, and runs `python -m adapter.http_reader`. With `APP_ENV=dev` the runner serves `/reader`; unset or empty is propagated and the runner refuses (403). Its base-to-head `git diff` is empty. EC-4 is not implemented.
- `VERIFY.sh` (PD-8):
  - `APP_ENV` (B-3): line 4 `export APP_ENV=${APP_ENV:-dev}` is replaced by a refusal before anything else runs: unless the caller supplies exactly `APP_ENV=dev`, it prints `VERIFY_APP_ENV_NOT_DEV: run with APP_ENV=dev (effective: …)` with the effective value or `<UNSET>` to standard error and exits 2, with no runner started and no standard output; otherwise it exports `APP_ENV` unchanged to the start helper. No default appears anywhere in the script;
  - keeps check 0 (serializer and emitter determinism) unchanged;
  - `PORT="${VERIFY_PORT:-5000}"`; frees that port as before; starts `PORT="$PORT" scripts/dev_start_reader.sh` in the background, writing its log to a `mktemp -d` work directory; polls `http://127.0.0.1:$PORT/reader?v=1&…` for up to 30 s instead of `sleep 1`;
  - probes `/reader` on `127.0.0.1` (HDE-CLI-API-Vendor-Ref §5.4 documented host) instead of the old harness's `/api/reader`;
  - keeps every check (`READER_200_HEADERS`, `READER_200_ETAG_PRESENT`, `READER_200_ETAG_MATCH`, `READER_304_STATUS`, `READER_304_EMPTY_BODY`, `READER_HEAD_CL_MATCH`, `ETAG_INVARIANCE`) and adds `READER_200_STATUS`;
  - writes every capture to the work directory, never to the repository (F-6), tees each token line to a token file, and exits 1 when any token ends `_FAIL` (F-7); a trap stops the runner and removes the work directory;
  - extracts the ETag portably with `awk 'tolower($1)=="etag:"{print $2}'` (F-12; PD-20).
- Documents (exact text in the companion diff):
  - `docs/acceptance/reader_a7_crib.md` lines 3–4: the start line becomes `APP_ENV=dev scripts/dev_start_reader.sh` (the caller supplies `APP_ENV`; the script propagates it unchanged), with the probe URL on `127.0.0.1:8000`.
  - `docs/server/reader_v1.md` line 17 (gate wording), line 19 (start command `APP_ENV=dev scripts/dev_start_reader.sh`; the script never defaults `APP_ENV`; `VERIFY.sh` starts the same runner; the former dev Reader harness "was removed in HDE-CRD-0002", without its path), line 20 (S02: unknown paths answer the envelope from every factory; `adapter/wsgi.py`'s 405 has no `Allow`) and line 24 (legacy notice names `APP_ENV=dev scripts/dev_start_reader.sh`).
  - No other document changes for RP-1 (B-5); `AGENTS.md` and `README.md` stay with WU-DOC-01 (OBS-P3-8).
  - `engine/emit_public.py` lines 20–22 and `tests/runtime/test_emit_public_legacy_helper.py` lines 3–6: docstrings only, no harness path.
- Active-reference result: after the change, `git grep reader_harness` outside the historical prefixes of instruction §5.4, `docs/pfcanon/` and `docs/ephemeral/` finds only the three classifier keys (ID-3 needs them to classify the deletion) and `CHANGELOG.md` line 333 (WU-DOC-01). PR-30 records both as the stated exceptions to acceptance (4).

### 6.5 S15 — catalog rows, validator and enumeration (IF-6; EC-8; ID-1)

**Rows.** Appended after the existing ten rows of `catalog_obj()` in `tools/evidence/generate_a7_transport_proofs.py`, in this order (existing rows keep their bytes and order). Every row has `a7_eligible: false`. Values are read from each view and its guard:

| # | method, path | blueprint_module | classification | internal | env_gate | rails_profile | extra |
| :- | :- | :- | :- | :- | :- | :- | :- |
| 1 | GET `/api/compat/v1` | `engine.http.compat_handler` | `internal_admin` | true | `APP_ENV!=prod` | `internal-admin writer no-store` | description "Compat ids-only probe (internal admin)" |
| 2 | HEAD `/api/compat/v1` | same | `internal_admin` | true | `APP_ENV!=prod` | same | "Compat HEAD (writer transport 405, Allow POST, OPTIONS; internal admin)" |
| 3 | OPTIONS `/api/compat/v1` | same | `internal_admin` | true | `APP_ENV!=prod` | same | "Compat OPTIONS (writer transport 204, Allow POST, OPTIONS; internal admin)" |
| 4 | GET `/aux/narrative` | `adapter.http_reader` | `public_aux` | false | `not_applicable_public` | `public-read-only; vendor-network-disabled` | `aliases: ["/api/aux/narrative"]` (HDE-CLI-API-Vendor-Ref §5.6 record) |
| 5 | GET `/ops/db/unavailable` | `adapter.http_reader` | `ops` | true | `operator-network-only` | `ops diagnostic no-io writer no-store` | |
| 6 | GET `/ops/rails/refusal` | same | `ops` | true | `operator-network-only` | same | |
| 7 | POST `/ops/rails/refusal` | same | `ops` | true | `operator-network-only` | same | |
| 8 | GET `/ops/probe/env` | same | `ops` | true | `operator-network-only` | `ops probe no-store` | |
| 9 | POST `/ops/writer/diagnostic` | same | `ops` | true | `operator-network-only` | `ops writer admin-scope no-store` | `route_id: "ops.writer.diagnostic.v1"` (the view's `_DIAGNOSTIC_ROUTE_ID`; PF12 §8.8 writer `route_id`) |
| 10 | HEAD `/ops/writer/diagnostic` | same | `ops` | true | `operator-network-only` | same | "writer transport 405, Allow POST, OPTIONS" |
| 11 | OPTIONS `/ops/writer/diagnostic` | same | `ops` | true | `operator-network-only` | same | "writer transport 204, Allow POST, OPTIONS" |
| 12 | GET `/internal/healthz` | `adapter.wsgi` | `ops` | true | `operator-network-only` | `ops-only no-store` | "(adapter.wsgi factory only)" |
| 13 | GET `/internal/readyz` | `adapter.wsgi` | `ops` | true | `operator-network-only` | `ops-only no-store` | same |

Readings recorded (PD-9): the compat rows share the POST row's gate, because `_compat_writer_transport_guard` answers 404 for a production env mode before any view. No `/ops/*` view and neither health route has a code-level environment gate; `operator-network-only` is the string the catalog already uses for the equally ungated `/internal/version`, so it is the observed gate in the catalog's own vocabulary, not a new claim (OBS-P3-4 routes the exposure question to WU-PR-05). The diagnostic writer additionally requires the admin bearer scope (`_require_admin_scope`), which `rails_profile` names. `HDE-CLI-API-Vendor-Ref §5.6`'s `/internal/admin/bundle/v1` gets no row (no factory mounts it; PF12 §8.8 "real mounted routes"). Result: 23 rows; `success_endpoints` stays `[{"method":"GET","path":"/reader"}]`; the `/reader` rows keep `APP_ENV=dev`; `generated_at_utc` stays the manifest's `built_at_utc` (unchanged by a same-version refresh).

**Validator** (`validate_catalog`; PD-10):
- `CLASS = {public_reader, public_compat, internal_identity, internal_admin, ops, dev_harness, public_aux}` — the PF12 §8.8 closed set plus the §5.6-projected `public_aux`, with a comment that `public_aux` and `aliases` are not yet registered by HDE Schemas & Artifacts and no conformance is claimed (Plan risk R-7).
- `aliases` joins the allowed key set. When present it must be a non-empty list of unique strings that start with `/`, contain no `?` and differ from `path`.
- Duplicate detection covers `(method, path)` and `(method, alias)` together, so an alias cannot collide with a catalogued pair.
- New pins: exactly one record has path `/aux/narrative`, and it is `GET`, `public_aux`, `aliases == ["/api/aux/narrative"]`, `internal: false`, `a7_eligible: false`, `env_gate: not_applicable_public`; `aliases` appears only on a `public_aux` record; `env_gate: not_applicable_public` never appears on an internal record. The Aux record is pinned by path, not by class uniqueness, so the existing `tests/transport/test_a7_transport_proofs.py::test_all_canon_valid_classifications_accepted` (which assigns every class in `CLASS` to the first row) stays unchanged and passing (PD-22).
- Every existing pin (key set, types, sampler row, production Reader row, success designation, `/internal/version` rejection) is unchanged.

**Enumeration test** (ID-1), in `tests/http/test_endpoint_catalog.py`: the union of `url_map` pairs from the three factories (built under `APP_ENV=dev`) must equal catalogued pairs ∪ the exclusion table; an uncatalogued, unexcluded pair fails; a stale exclusion fails; a catalogued pair no factory serves fails (PF12 §8.8 "real mounted routes"); the class-(b) exclusions equal the Aux record's `aliases`. The exclusion table (30 pairs, one reason each):

| Class | Pairs | Reason |
| :- | :- | :- |
| (a) governed refusal of a catalogued record | `/api/reader` DELETE, GET, HEAD, OPTIONS, PATCH, PUT (6); `/reader` POST (1) | HDE-CLI-API-Vendor-Ref §5.4 "Production mount"; PF12 §8.8 "The production route's other methods are refused…" |
| (b) alias spelling | `/api/aux/narrative` GET (1) | HDE-CLI-API-Vendor-Ref §5.6 `aliases` |
| (c) framework-implicit method | HEAD and OPTIONS of `/aux/narrative`, `/api/aux/narrative`, `/dev/reader/conjunction`, `/dev/sampler/conjunction`, `/dev/writer/conjunction`, `/internal/healthz`, `/internal/readyz`, `/ops/db/unavailable`, `/ops/probe/env`, `/ops/rails/refusal` (20); OPTIONS of `/reader` and `/internal/version` (2) | Flask adds them; neither §5.6 nor the view defines them. `HEAD /reader` and `HEAD /internal/version` stay catalogued because §5.6 defines them |

23 catalogued + 30 excluded = 53 served. No served pair fits none of (a) to (c), so no boundary finding arises.

### 6.6 S18 — documents

- `docs/ADAPTER_009.md` line 174 becomes: "`COMPAT_GET_BODY_400_OK` — Compat GET with body ⇒ 400 error_v1 envelope built from the `invalid_json` alias (emitted `code`: `ERR_COMPAT_INVALID_JSON`), `no-store`, no ETag." (F-3; PD-18). No other line of the file changes (S17's lines are WU-PR-08's).
- `ARCHITECTURE.md`:
  - line 9: `engine/presenter/emitter.py::emit_public(envelope, *, sort_keys=True) -> bytes`, with `emit_compact_json(envelope, *, sort_keys=True) -> tuple[bytes, dict]` named as the compatibility alias of `emit_public_with_envelope` (emitter lines 6, 16, 23);
  - line 24: the same signatures in the "Emitter/serializer discipline" list;
  - line 28: the heading "Routing (dev only)" becomes "Routing and mounts", with the three factories and their mounts (`adapter/factory.py` the Procfile app; `adapter/wsgi.py` adding the two health routes; `adapter/http_reader.py` the dev runner), and `docs/ENDPOINTS_CATALOG.json` named as the route inventory with its owner. The compat bullets that follow are unchanged.

### 6.7 ID-3 — classifier registration

In `ci/checks/classify_ci_changes.py`, exactly these four keys:
- `_WORKFLOW_CONTROL_PATH_LANES["VERIFY.sh"] = {"product"}`
- `_WORKFLOW_CONTROL_PATH_LANES["dev/reader_harness/__init__.py"] = {"product"}`
- `_WORKFLOW_CONTROL_PATH_LANES["dev/reader_harness/app.py"] = {"product"}`
- `_PRODUCT_TEST_OWNER_PATHS["scripts/dev_start_reader.sh"] = ("tests/scripts/test_dev_start_reader.py",)`

with a two-line comment naming HDE-CRD-0002 WU-PR-03 (S09). No function changes. Effects, measured on the prototype:
- `VERIFY.sh` and the two harness paths (edit or deletion) select `product` and need no owner target, so `CI_CHANGE_SURFACE_UNCLASSIFIED` and `CI_SOURCE_OWNER_TEST_MISSING` no longer fire; `scripts/dev_start_reader.sh` selects `product`, `release` and its owner test.
- The new owner test becomes a registered owner, so it is a full-validation target and satisfies the coverage pin `test_every_tracked_test_module_is_reached_by_a_lane_or_full_validation_target`.
- The classifier is a full-validation path, so this PR selects all seven lanes and runs every registered owner (164 targets on the prototype).
- Every pin of `tests/evidence/test_rails_ci_workflow_integration.py` stays true without edit (§4.3); none needs adding.

Why `product` for all three (PD-13): it is the smallest single-lane assignment (instruction §9.6); `scripts/` paths already select `product`; no lane runs `VERIFY.sh` itself. The owner test (§6.9) runs `VERIFY.sh` end to end, so `VERIFY.sh`'s behavior is proven whenever the runner script changes and on every full-validation run; a `VERIFY.sh`-only change selects `product` but not that test (OBS-P3-5 to the IA for WU-PR-06).

### 6.8 ID-4 — contract-inventory baseline

`ADAPTER_BOUNDARY_PUBLIC_ROUTE_BASELINE_RECORDS` is replaced, data only, by `pprint.pformat(tuple(asdict(r) for r in records))`, where `records` are the analyzer's own `discover_route_registrations(ADAPTER_BOUNDARY_CANONICAL_ADAPTER_LOCI)` filtered exactly as `_public_route_pass_state` filters (supported, public, not `blueprint_constructor`), computed at the PR head after every adapter edit (the test fixtures' signature path, §4.1). Diff (21 → 23 records):
- added: `adapter/factory.py` `app.errorhandler` 404 `_governed_not_found`; `adapter/factory.py` `app.errorhandler` 405 `_governed_method_not_allowed`;
- changed: `adapter/http_reader.py` `app.errorhandler` 404 `_compat_scoped_not_found` → `_governed_not_found`; 405 `_compat_scoped_method_not_allowed` → `_governed_method_not_allowed`;
- unchanged: every route, registration, `before_request` and `after_request` record, including `reader_post`, `reader_method_not_allowed` and `reader_post_not_allowed` at `/api`, and no `reader_v1_post` (addendum 2.2 item 1).

Review against HDE-CLI-API-Vendor-Ref §5.1.0 and §5.4: only error handlers change; no route, mount or method changes. The generator's outputs, schema, family, refusal codes, flags and write paths do not change; it gains no import symbol and is not run in write mode; `artifacts/vendor/hdapi_v2/` and `artifacts/architecture/` stay byte-unchanged. Re-run mechanism (addendum 2.2 binding requirement): `tests/evidence/test_hdapi_v2_contract_inventory.py` is an owner of `adapter/factory.py`, `adapter/wsgi.py` and `adapter/http_reader.py` (`_PRODUCT_TEST_OWNER_PATHS`, `_HTTP_READER_TEST_OWNERS`), so any later route change re-runs it. It needs `ruby` on `PATH`.

### 6.9 Tests (placement chosen so that no owner-guard or registry change beyond ID-3 is needed; PD-12)

| File | Added cases | Requirement |
| :- | :- | :- |
| `tests/http/test_endpoint_catalog.py` (owner of all three factories and `http_reader`) | enumeration with the exclusion table; the Aux record equals the §5.6 projection; validator rejects `aliases` off the Aux record, alias collisions and an unknown class; unknown-path matrix over 3 factories × 5 paths × GET, HEAD, POST, OPTIONS, PUT, DELETE × `APP_ENV` {dev, prod} (status, exact body, `Content-Type`, `no-store`, no ETag, HEAD empty); unrouted-method 405 with sorted `Allow` on `adapter/factory.py` and `adapter/http_reader.py`; compat descendant 404, compat PUT 405 (`Allow` kept on the production factory), compat HEAD 405 `Allow: POST, OPTIONS`, every non-POST `/api/reader` 405 `Allow: POST`, unprefixed `POST /reader` 405 `Allow: GET, HEAD` | S02, S15 |
| `tests/http/test_reader_a7_transport.py` (an `http_reader` owner; its seams avoid the admission dependency) | served for `dev`, ` DEV `, `Dev` (GET 200, HEAD 200 empty); refused for unset, empty, blank, `test`, `local`, `prod`, `production`, `live`, `staging`, `development`, `dev1` (403 `ERR_READER_FORBIDDEN`, `no-store`, JSON, no ETag, HEAD empty) and `v` still validated first | S10 |
| `tests/cli/test_cli_usage_and_errors.py` (owner of `engine/cli/main.py`; compat lane) | `cli(["--help"]) == 0`; output names `magic10_compat_result.v1` and `--dump-reader` and lacks the old phrase | S07 |
| `tests/scripts/test_dev_start_reader.py` (new; ID-3 owner; the runner propagation test, B-4) | With `APP_ENV=dev` the script's runner serves `GET /reader?v=1` 200 on a free loopback port; unset prints `[dev-start] APP_ENV=<UNSET>` and the runner refuses 403 `ERR_READER_FORBIDDEN`; `test`, `local`, `prod` and empty are kept and refused; `VERIFY.sh` with `APP_ENV=dev` and a free `VERIFY_PORT` exits 0 with every token `_OK` (including `READER_200_STATUS_OK`, `READER_304_STATUS_OK`); `VERIFY.sh` without an explicit `dev` (unset, empty, `test`) exits 2 with `VERIFY_APP_ENV_NOT_DEV`, empty standard output and no runner started. 10 cases. `python` on `PATH` is the test interpreter through an exec wrapper (a symlink loses a virtual environment); requires `bash` and `curl` | S09, S10 (runner), ID-3 |
| `tests/runtime/test_emit_public_legacy_helper.py` | docstring only | S09 |

No existing assertion changes. New cases never spell the module name `adapter.http_reader` as a string literal (parameter ids are `factory`, `http_reader`, `wsgi`; the Aux row's module is read from `create_app.__module__`), because `tests/evidence/test_http_reader_ci_ownership.py` counts such literals as unregistered literal-reference owners (PD-21; observed in the prototype). Tests that request `GET /reader` rely on `APP_ENV=dev`, which CI sets for every lane and the changed-tests step; PR-30 records any test that fails only with `APP_ENV` unset (§10 item 6).

### 6.10 Release refresh and convergence (Plan v1.1 §10 with PD-15 and instruction §5.7 (a)–(d))

All under closed rails, vendor and database keys unset, in a detached worktree for every write-capable run, each owner re-run once more to prove byte stability (steps 3b–10):

| Step | Command (owner) | Notes |
| :- | :- | :- |
| 1 | member bytes final: `adapter/http_reader.py`, `engine/cli/main.py` (one final LF) | no updater run from here to the cut (§5.7 (a)) |
| 2 | `python scripts/cut_release_manifest.py --version 1.3.0 --built-at-utc 2026-08-24T18:04:49Z --roster-from-admission`; `python scripts/release_id_recompute.py --check-manifest-only`; the cutter with `--check` | two manifest rows change; record the new `release_id` |
| 3 | `python -c "from engine.config.registry_loader import load_active_mechanics_bundle as l; b=l(); print(b.release_id, len(b.source_identities), b.manifest.version)"`; `python tools/config/generate_config_artifacts.py --compare-goldens . --report <outside the tree>/golden_report.json` | `1.3.0`, 45, the new `release_id`; exit 0 |
| **3b** | `HDE_WRITE_A7_PROOFS=1 python tools/evidence/generate_a7_transport_proofs.py`; then `--check` | **PD-15:** the catalog family (catalog, `.sha256` sidecars, snapshot) and the seven A7 proofs before any gate or updater run, because the updater validates the catalog with the new validator (F-2) |
| 4 | `python tools/evidence/run_canonical_json_gate.py`; `--check-only` | |
| 5 | `python tools/evidence/update_evidence_index.py`; `--check` | first updater run after the cut; labels the gate captures and the A7 family; with the RP-3 roster line removed it also drops the purity-report row's label (B-8) |
| 6 | `python tools/config/generate_config_artifacts.py --publish-family`; updater `--check` | |
| 7 | `HDE_WRITE_A7_PROOFS=1 python tools/evidence/generate_a7_transport_proofs.py` (byte-stable re-run; `--check`); `python tools/evidence/generate_determinism_gate_proofs.py`; `SAFE_MODE=0 ALLOW_NETWORK=1 python tools/evidence/generate_open_rails_abba_proof.py` (fixture mode, keys absent), then set `FROZEN_OPEN_ABBA_SHA256` in `tools/evidence/generate_open_rails_abba_proof.py` to `sha256sum audit/gates/determinism/open_rails_abba.json`; `python tools/evidence/generate_conjunction_writer_evidence.py`; `python tools/evidence/generate_engine_core_evidence.py` | |
| 8 | updater; `--check`; `orientation_demo.py --check`; `validate_evidence_paths.py`; `ci/checks/check_mirror_schema.sh`; `ci/checks/check_evidence_index_hash.sh`; `check_lf_endings.py`; `ci/checks/check_final_lf.sh`; `refresh_step_logs_manifest.py --check` | step-7 producers take the new label here (§5.7 (b)) |
| 9 | `python tools/evidence/run_sanity_pipeline.py --log-path <outside>/sanity.log` (must end `summary:PASS`); the canonical run; `python tools/evidence/run_sanity_pipeline_gate.py`; updater `--check` | |
| 10 | `generate_showcompat_artifacts.py --check`; `generate_cli_conformance_artifacts.py --check`; `generate_rails_gate_evidence.py --check`; `generate_env_matrix_snapshot.py --check` | frozen families unchanged |
| 11 | stale-binding sweep: `git grep` for the superseded `release_id` `52be4558…` and the superseded open-rails digest `c78740b3…` outside `docs/`, `.audit_src/`, `handoff/`, `manifest_pre.sha256`, `manifest_post.sha256` | expected hits, each classified: `README.md` (WU-DOC-01) and the HDE-EPIC040 QA and Ops records under `audit/qa/hde-epic040/` and `audit/ops/hde-epic040/` (frozen historical captures). The purity-report Mirror row is unlabeled and is not a hit (B-8). Anything else is a defect to fix before publication |
| 12 | §10 tests; the attestation build and verify | |

Restart rules: a member byte change after step 2 restarts at step 2; an evidence-primary change restarts at step 3b (it replaces Plan v1.1 §10's step 5 restart point for this unit, because the A7 owner now precedes the updater); steps 3b–10 must be byte-stable on a second run.

Families the rehearsal regenerated (expected set; PR-30 records its actual set): 29 primaries plus 30 path proofs, all by their owners:
- **Catalog family:** `artifacts/audit/ENDPOINTS_CATALOG.json` (through the `docs/` symlink), `artifacts/audit/ENDPOINTS_CATALOG.json.sha256`, `docs/ENDPOINTS_CATALOG.json.sha256`.
- **A7 proofs:** `artifacts/proofs/{reader_success_get_head_304.json,success_304.txt,success_encoding_invariance.txt,success_get.txt,success_head.txt}`. `endpoints_env_gate_proof.log`, `success_writers_errors.txt` and `artifacts/reader/endpoints_snapshot.json` are rewritten byte-identically.
- **Config family:** `artifacts/catalog/{catalog_schema_validation,domain_closure_report}.log`.
- **Engine core:** `artifacts/core/{abba/ab_ba_parity,json_compare/core_result_json_compare,two_run/identity}.json`. `purity/purity_report.json` is byte-stable (F-9).
- **F07 writer:** `artifacts/writer/{conjunction_write_readback.log,conjunction_writer_summary.json}`.
- **Canonical JSON gate:** `audit/gates/canonical_json/{json_canon_compare,json_canonical_check}.log`, `audit/gates/json_gate/canonical/{json_gate_check_log,json_gate_compare_log}.ndjson`.
- **Determinism:** `audit/gates/determinism/{abba.bytes,open_rails_abba.json,tworun_identity.sha256}`, `audit/gates/parity/reader_cli/{ab,ba,summary}.json`.
- **Index and Mirror:** `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, `artifacts/evidence_index.jsonl`, `artifacts/evidence_index.jsonl.sha256`.
- **Constant:** `FROZEN_OPEN_ABBA_SHA256` in `tools/evidence/generate_open_rails_abba_proof.py`.

The sanity log is rewritten byte-identically.

## 7. Change set

### 7.1 Files edited by hand (the companion diff)

| Path | Change | Requirement |
| :- | :- | :- |
| `adapter/http_reader.py` (member) | `_reader_dev_env_explicit`; the gate line; `governed_not_found_response`; the two renamed handlers' non-compat branch | S10, S02 |
| `adapter/factory.py` | import; two handlers | S02 |
| `engine/cli/main.py` (member) | the help string | S07 |
| `tools/evidence/generate_a7_transport_proofs.py` | `CLASS`, `AUX_PATH`, `AUX_ALIASES`; 13 rows; validator | S15 |
| `tools/evidence/generate_hdapi_v2_contract_inventory.py` | baseline data only (rebuilt, §6.8) | ID-4 |
| `ci/checks/classify_ci_changes.py` | four keys and a comment | ID-3 |
| `tools/evidence/update_evidence_index.py` | remove exactly the line `"artifacts/core/purity/purity_report.json",` from `CURRENT_RELEASE_CAPTURE_PATHS` (22 paths remain); nothing else (B-7) | RP-3 (addendum 2.6) |
| `scripts/dev_start_reader.sh` | **not edited** (B-1); listed only to record that its diff must be empty | RP-1 (addendum 2.6) |
| `VERIFY.sh` | canonical runner; temp work dir; token exit; portable ETag extraction; `APP_ENV` refusal (B-3) | S09; RP-1 |
| `dev/reader_harness/app.py`, `dev/reader_harness/__init__.py` | deleted | S09 |
| `docs/acceptance/reader_a7_crib.md`, `docs/server/reader_v1.md` | §6.4 | S09, S10, S02 |
| `docs/ADAPTER_009.md` (line 174), `ARCHITECTURE.md` | §6.6 | S18 |
| `docs/CLI_commands.md` | the known-gap sentence | S07 |
| `engine/emit_public.py`, `tests/runtime/test_emit_public_legacy_helper.py` | docstrings | S09 |
| `tests/http/test_endpoint_catalog.py`, `tests/http/test_reader_a7_transport.py`, `tests/cli/test_cli_usage_and_errors.py`, `tests/scripts/test_dev_start_reader.py` (new) | §6.9 | S02, S10, S07, S15, S09 |

### 7.2 Written only by owners

`catalog/manifest.json` (cutter); `FROZEN_OPEN_ABBA_SHA256` in `tools/evidence/generate_open_rails_abba_proof.py` (Plan v1.1 §10 step 7 refresh); every family in §6.10; the Index, Mirror, sentinels and path proofs (updater only). `docs/ENDPOINTS_CATALOG.json` stays a symlink (F-1).

### 7.3 Expected unchanged (a change is a finding, §14)

`adapter/wsgi.py`, `engine/http/compat_handler.py`, `engine/presenter/**`, `engine/config/registry_loader.py`, `scripts/dev_start_reader.sh` (B-1), `tools/evidence/update_evidence_index.py` (except the one B-7 line), `tools/evidence/hdapi_v2_boundary_analyzer.py`, `.github/workflows/ci.yml`, `pytest.ini`, `artifacts/vendor/hdapi_v2/**`, `artifacts/architecture/**`, `artifacts/cli/**`, `artifacts/identity/**`, `artifacts/math/**`, `audit/ops/**`, `artifacts/reader/endpoints_snapshot.json` (its content `GET /reader` is unchanged), `.body200.json`, `.code304.txt`.

## 8. Implementation sequence (PR-30)

1. Recover: inspect local roots, worktrees, branches, open PRs and `docs/ephemeral/HDE-CRD-0002-WU-PR-03-*` before creating anything (instruction §13).
2. Branch from current `main` (the session's designated branch); confirm `main` still carries `150feab`'s code (re-run the §4.1 checks and `git apply --check` of the companion diff if `main` moved outside `docs/ephemeral/`).
3. Set up Python 3.12 with CI's install, `ruby` on `PATH`, `bash` and `curl`; record versions.
4. Apply §7.1 (the companion diff as a starting point); re-read every hunk against §6.
5. Rebuild the ID-4 baseline from the edited adapters (§6.8); confirm discovered = baseline (23).
6. Run the changed-surface tests that do not need admission (`tests/http/test_reader_a7_transport.py`, `tests/cli/test_cli_usage_and_errors.py -k help`, `ci/checks/check_cli_help.sh`).
7. Freeze member bytes; run §6.10 steps 2–11; record each step, its exit code and the second-run byte stability.
8. Run §10 in a detached worktree of the candidate commit, including the B-1 and B-7 diff checks: `git diff <base> -- scripts/dev_start_reader.sh` is empty and `git diff <base> -- tools/evidence/update_evidence_index.py` is exactly the one deleted roster line.
9. Write the PR result record v1.0 (§12), commit coherently (code and evidence may be one commit, or a source commit followed by the convergence commit), push, open the PR with the template headings, record `PR_CANDIDATE_PUBLISHED`, and hand off to PR-35.

## 9. Requirement → change → test map

| Requirement / acceptance item | Change | Proof |
| :- | :- | :- |
| S02 / (1) | §6.1 | `test_unknown_paths_return_the_governed_not_found_envelope` (180 cases), `test_unrouted_methods_return_the_governed_405_with_allow`, `test_compat_and_production_reader_shaping_is_unchanged`; existing compat, Reader POST v1/v2 and transport tests |
| S10 / (2) (last clause as §5A.1) | §6.2; §6.4 runner unchanged (B-1) | `test_dev_reader_is_served_only_for_explicit_dev`, `test_dev_reader_refuses_every_other_environment`; `tests/scripts/test_dev_start_reader.py`; the A7 env-gate proof regenerated (`endpoints_env_gate_proof.log`, `APP_ENV=prod`) |
| S07 / (3) | §6.3 | `test_top_level_help_names_the_showcompat_stdout_contract`; `ci/checks/check_cli_help.sh`; `generate_cli_conformance_artifacts.py --check` |
| S09 / (4) | §6.4 | file absence; `VERIFY.sh` run (§10 item 5) and its owner test; the reference search (§6.4) |
| S15 / (5) | §6.5 | enumeration, Aux and validator tests; existing catalog tests; A7 `--check`; updater `--check`; catalog bytes = mirror bytes (symlink, F-1) |
| S18 / (6) | §6.6 | the corrected statements quoted in the result record |
| Refresh / (7) | §6.10 | admission line; second-run byte stability; recompute; seven lanes |
| ID-3 | §6.7 | classifier dry run on the PR's paths; `tests/evidence/test_rails_ci_workflow_integration.py` |
| ID-4 | §6.8 | `tests/evidence/test_hdapi_v2_contract_inventory.py` with `ruby` |
| RP-3 (S12 contract kept) | §6.10, §7.1 (B-7, B-8) | the three label tests of `tests/evidence/test_evidence_index_missing_state.py`; updater `--check`; the step-11 sweep; the full sweep (B-9) |

## 10. Validation plan (PR-30, local)

Every write-capable run happens in a detached worktree and ends with `git diff --exit-code` and empty `git status --short --untracked-files=all`:
1. Classifier dry run on the PR's changed paths: all seven lanes; record the target count.
2. The changed-tests step as CI runs it (the classifier's targets, in a detached worktree).
3. The seven lanes' commands as in `.github/workflows/ci.yml` (product, compat, db, rails, evidence, qa, release), the release lane including the attestation build and verify into an external empty directory with `--require-clean`.
4. **B-9 (LR-O2 applies: the updater changes):** every test file that imports or runs `tools/evidence/update_evidence_index.py` runs, satisfied by the full `tests/` sweep under closed rails with `ruby`, `bash` and `curl` available, in a detached worktree, ending with a clean tree; record pass, skip and xfail counts.
5. `VERIFY.sh` once from the repository root with `APP_ENV=dev` and a free `VERIFY_PORT`, and once without `APP_ENV`; record the tokens and both exit codes (0; 2 with `VERIFY_APP_ENV_NOT_DEV`).
6. Informative: the `http_reader` owner tests with `APP_ENV` unset, to name any test that depends on CI's `APP_ENV=dev`; a failure there is recorded, not fixed by changing an expectation.
7. Frozen families' `--check` modes (§6.10 step 10) and the A7, gate, updater, orientation, paths, mirror, index-hash, LF, final-LF and step-logs checks (§6.10 step 8).
8. The B-1 and B-7 diff checks (§8 step 8).

## 11. PR split, merge dependencies and pull request description

- One PR for the whole unit (Plan v1.1 §7; no split: the member edits, the refresh and the catalog regeneration must land together for admission and the updater to hold at every commit of `main`).
- Merge dependency: none open (WU-PR-01 and WU-PR-02 landed). WU-PR-04 and WU-PR-05 depend on this PR's `release_id` (E-3).
- PR description: `.github/pull_request_template.md` headings with the `AGENTS.md` content rules — Why (instruction §4; Specification rows), What changed (by path), Checks run (with counts), Not in this PR (§17 stale documents and observations with owners), What merging does (what becomes current on `main`; no QA, acceptance or closure).

## 12. Acceptance and evidence obligations (PR result record v1.0)

`docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-implementation-result-v1.0.md` names:
- the refreshed `release_id` and every regenerated family, with paths;
- the catalog diff (10 → 23 rows) and the ID-1 exclusion table;
- the nonclaim that `artifacts/cli/help/*` captures the earlier help text;
- each check actually run with counts; the S10 environment matrix result; the `VERIFY.sh` run;
- the ID-3 registry keys; the ID-4 baseline diff;
- every §6.10 step with exit code and second-run byte stability; the stale-binding sweep with each hit classified;
- the stale-document list (§17);
- **RP-3 (B-10):** the roster change, its reason (the purity report binds 12 engine-core, serializer, mechanics-catalog and schema sources, not the release) and the one row it unlabels; the nonclaim that the purity report is not a release-bound capture; a citation of the rescope review v1.0; no statement that WU-PR-02's accepted delivery is modified; the B-9 full-sweep counts;
- **RP-1:** the empty `scripts/dev_start_reader.sh` diff (B-1); acceptance (2) verified as §5A.1 words it; the `VERIFY.sh` refusal run;
- in-flight decisions (PR-30 contract), `NONE` when there are none.

## 13. Security and migration constraints

- Migration: none. Rollback: Nathan's revert of the squash commit, followed by a same-version manifest refresh (Plan v1.1 §7, §14).
- S02 and S10 only narrow exposure; no route opens. The `/reader` gate never serves an unset, empty or non-`dev` environment.
- Catalog fields are names-only (PF12 §8.8): no secrets, URLs, tokens or payload bytes.
- `VERIFY.sh` probes `127.0.0.1`; the runner's `0.0.0.0` bind is unchanged (OBS-W3-1).
- The test runner binds loopback only; closed rails; no secret, token or key value in tests, logs or records. The refresh opens no rail; the open-rails fixture proof runs in fixture mode with keys absent.

## 14. Risks and recovery

| ID | Risk | Treatment |
| :- | :- | :- |
| RK-1 | The updater refuses before the catalog is regenerated (F-2) | PD-15 order; restart point 3b |
| RK-2 | A member byte change after the cut | restart at step 2 (Plan v1.1 §10) |
| RK-3 | `Allow` order nondeterminism | sorted in the new handler (PD-2); tests compare the sorted string, and a set for the compat 405 |
| RK-4 | `ruby` absent on a runner | the contract-inventory test fails, never skips (addendum 2.2); PR-35 records the hosted version if the log shows it (O-6) |
| RK-5 | `curl` absent where the owner test runs | the test fails with "VERIFY.sh requires curl"; hosted `ubuntu-latest` provides it; recorded as a test dependency |
| RK-6 | OBS-17 qa-lane intermittent failure of `tests/qa/test_generate_epic_close_pack.py` | recorded as OBS-17 on this PR, never "fixed" here |
| RK-7 | A boundary trigger of instruction §14, or any change outside the bounds as extended by addendum 2.6 (B-12) (an unclassifiable served pair; a change outside §6; a classifier change beyond ID-3; a frozen-family `--check` failure; an architecture-snapshot failure) | stop the affected work; `RESCOPE_REQUEST` through RS-20 (PR-30 `PR_RETURN_PHASE`) |

Recovery: an interruption resumes in the same dedicated phase session from its last saved artifact; an ordinary defect in this plan returns to this PR-20 context as a new plan version; abort is only Nathan's manual PR-50.

## 15. Decisions taken in this plan (within approved scope)

| ID | Decision | Basis |
| :- | :- | :- |
| PD-1 | One nested presenter helper per factory (`_governed_error_response` in `adapter/http_reader.py::create_app`; `_not_found_envelope_response` in `adapter/factory.py::create_app`); no cross-module helper | IF-11 "as `adapter/wsgi.py` does"; the boundary analyzer's accepted shape (F-13); instruction ID-4 "The boundary analyzer accepts the new handlers, which must emit through the presenter" |
| PD-2 | **E-2: the 405 handlers keep `Allow`**, from the routing exception, sorted | RFC 9110 §15.5.6; every governed 405 in HDE-CLI-API-Vendor-Ref carries `Allow` (§5.1.0 line 2071, §5.2 line 2327, §5.10) and §5.5 requires it on the converted compat 405; F-4 |
| PD-3 | Compat paths keep their existing bytes and headers in both factories: in `adapter/factory.py` the nested helper reproduces the conversion exactly, with Flask's `Allow` on a compat 405 | instruction §9.1; HDE-CLI-API-Vendor-Ref §5.5 |
| PD-4 | Handler names `_governed_not_found`, `_governed_method_not_allowed` in both factories | the old names no longer describe the handlers; ID-4 records the rename |
| PD-5 | Gate helper `_reader_dev_env_explicit`; `v` validation stays first | instruction §9.2 |
| PD-6 | The S07 help text of §6.3 | instruction §9.4 |
| PD-7 | The start helper stays unchanged and propagates `APP_ENV` exactly | F-11; addendum 2.6; review §7.1 B-1 |
| PD-8 | `VERIFY.sh` per §6.4: canonical runner, `127.0.0.1`, readiness poll, temporary work directory, effective exit, `READER_200_STATUS` added; every earlier check kept | instruction §9.5; F-6, F-7 |
| PD-9 | The 13 rows of §6.5, including `operator-network-only` for ungated internal routes and the diagnostic writer's `route_id` | instruction §9.3; EC-8 "observed gates"; PF12 §8.8 |
| PD-10 | The validator extension of §6.5 | instruction §6 (S15 row); R-7 |
| PD-11 | The enumeration test and its 30-pair exclusion table | ID-1 |
| PD-12 | New tests go into existing registered owner files; one new file, the ID-3 owner | avoids owner-guard and registry changes beyond ID-3 (instruction ID-3 "No other classifier behavior changes") |
| PD-13 | `product` for `VERIFY.sh` and the harness paths; the four keys of §6.7 | instruction §9.6 |
| PD-14 | ID-4 rebuild method and diff of §6.8 | instruction §9.7; addendum 2.2 |
| PD-15 | **Convergence step 3b**: the A7 owner write before the gate and the first updater run; restart point 3b for an evidence-primary change | F-2; rehearsal 1 and 2 (§4.3). A sequencing correction inside Plan v1.1 §10's own method (the same commands, the same owners, step 7's A7 run kept and byte-stable), needed to deliver acceptance (7); not material (no acceptance intent, boundary, unit or dependency changes) |
| PD-16 | `docs/ENDPOINTS_CATALOG.json` stays a symlink | F-1 |
| PD-17 | Document texts of §6.4 and §6.6 | S09, S10, S02, S18 |
| PD-18 | S18 names the `invalid_json` alias and the emitted `ERR_COMPAT_INVALID_JSON` | F-3; Specification S18 acceptance intent |
| PD-19 | The rehearsal `release_id` is not binding; PR-30 records its own | §4.3 |
| PD-20 | `VERIFY.sh` ETag extraction made portable | F-12; instruction §9.5 "its checks stay meaningful" |
| PD-21 | New tests avoid the `adapter.http_reader` string literal | the http_reader ownership guard; instruction ID-3 "No other classifier behavior changes" |
| PD-22 | The Aux record is pinned by path, not class uniqueness | keeps `test_all_canon_valid_classifications_accepted` unchanged |
| PD-23 | New tests bind factory functions directly (`from adapter.factory import create_app as production_app`, `from adapter.wsgi import create_app as wsgi_app`) | F-14 |
| PD-24 | Remove the purity report from the updater's label roster, by the one line of B-7 | F-9; addendum 2.6; review §7.2 B-7 to B-10 |

## 16. Canon-conflict register

`CANON_CONFLICT_REGISTER` (CR-1 to CR-5 carried unchanged; CR-6 decided):

| ID | Status | Decision owner | Record |
| :- | :- | :- | :- |
| CR-1, CR-2, CR-3 (CANON_RECONCILIATION) | APPROVED_AS_CHANGED | Thoth | Specification v1.1 lineage |
| CR-4 | APPROVED | Product Owner | `docs/ephemeral/HDE-CRD-0002-WU-PR-01-po-disposition-cr-4-cr-5-v1.0.md` §2 |
| CR-5 | APPROVED_AS_CHANGED | Product Owner | same record §3 |

**Decided by the rescope review v1.0 §12:**

| ID | Classification | Statement | Decision |
| :- | :- | :- | :- |
| CR-6 | CANON_RECONCILIATION | Plan v1.1 IF-10 and WU-PR-03 acceptance (2) (from Audit EC-4; kept by Plan review v1.0 R1) required the dev Reader start helper to default `APP_ENV=dev`; HDE Architecture §3.8.1, HDE Mechanics Guide §5.6 and §34, Glow Infrastructure §8.1, Conjunction checklist HDE-CONJ001.4 and Glow QA Guide §13.9 require it to propagate `APP_ENV` exactly and never default it | **APPROVED**, alternative (a), canon governs, through addendum 2.6 (B-1 to B-6). Reviewer: the continuing whole-change IA through RS-20 (session https://claude.ai/code/session_01CCKsYD2yX5WgU3biWKb59j); reviewed artifact: rescope request v1.0 §5; decision time 2026-10-14T02:40:00Z. Proposed by the request 2026-10-14T02:01:29Z. No canon drainage. Alternative (b) (a Product Owner decision superseding canon) was not taken and is not foreclosed |

Coverage read for this plan: HDE-CLI-API-Vendor-Ref §5.1.7, §5.2 item 1, §5.4, §5.5, §5.6, §5.10 (`Allow`); HDE Schemas & Artifacts §8.8; HDE Governance §9.1.1; HDE Architecture §3.8.1; HDE Mechanics Guide §5.6 (start-helper paragraph) and §34; Glow Infrastructure §8.1 (`APP_ENV` note); Conjunction checklist HDE-CONJ001.4; Glow QA Guide §13.9; HDE Math Spec §12 dev-harness bullet; PF10 addenda 2.2, 2.3, 2.5. Otherwise:
- PD-2 follows canon.
- The S10 gate reading is the approved Plan's.
- `public_aux` and `aliases` follow HDE-CLI-API-Vendor-Ref §5.6 without a conformance claim (R-7, a drainage item).
- The S18 wording reports the emitted code beside the Specification's alias, which canon permits (HDE-CLI-API-Vendor-Ref §5.2 item 2, "legacy lowercase strings … retained as input aliases").

## 17. Stale documents, observations and carried items (not in this PR)

**Stale documents** (this unit makes them stale and may not change them; instruction §9.9):

| Document | Statement | Owner |
| :- | :- | :- |
| HDE-CLI-API-Vendor-Ref §5.1.7 "Known limits" and §5.1.0 line 2071's reference | unknown non-compat paths receive framework HTML 404 | Product Owner (canon doc-delta) |
| HDE-CLI-API-Vendor-Ref §5.6 "Implementation and acceptance state (informative)" | the catalog does not yet contain the Aux record | Product Owner (canon doc-delta) |
| HDE Architecture §3.8.1 "Current repository discrepancy"; HDE Math Spec §12 "Dev Reader harness" bullet | name `dev/reader_harness/` | Product Owner (canon doc-delta; ID-2) |
| HDE Mechanics Guide §34 "Current repository posture" | "The Reader handler treats missing `APP_ENV` as dev" (stale after S10; review §10) | Product Owner (canon doc-delta) |
| HDE Schemas & Artifacts §8.8 | `public_aux`, `aliases` and the ID-1 population rule are not registered (R-7) | Product Owner (canon doc-delta) |
| `docs/contracts/reader_v2_public_bytes.md` line 19 | the HTML 404 limitation (F-8) | WU-DOC-01 |
| `docs/acceptance/reader_a7_crib.md` line 13 | A7 proofs emitted by running a test; `encoding_invariance.txt` (the owner is the A7 generator; the file is `success_encoding_invariance.txt`) | WU-DOC-01 |
| `README.md` line 13 | the superseded `release_id` (F-10) | WU-DOC-01 |
| `CHANGELOG.md` line 333 | the dev runner at `dev/reader_harness/app.py` | WU-DOC-01 |
| `artifacts/cli/help/*`, `artifacts/audit/cli/help*.txt`, `artifacts/audit/cli_help_*.txt`, `audit/codex/epic011_r17c/cli/help.txt` | the earlier help text | frozen or historical captures; nonclaim only |

**Observations** (owner: the IA, who routes them):

| ID | Observation | Suggested route |
| :- | :- | :- |
| OBS-P3-1 | `adapter/http_reader.py::create_app`'s `after_request` never fires its `/internal/` ETag strip or diagnostic Content-Length rule (F-5) | WU-PR-05 (S19 reads these surfaces) or the Product Owner |
| OBS-P3-2 | The production factory's compat 405 `Allow` order depends on the hash seed (F-4); kept for byte identity | IA |
| OBS-P3-3 | `adapter/wsgi.py`'s 405 has no `Allow`, unlike E-2 | IA |
| OBS-P3-4 | The `/ops/*` probes and the health routes have no code-level environment gate and are mounted by the production app; `/ops/probe/env` returns the process id, start time and rails-state names | WU-PR-05 (S19); relates to OBS-W3-1 |
| OBS-P3-5 | A `VERIFY.sh`-only change selects `product` but not the owner test that runs it | WU-PR-06 (pre-push check) |
| OBS-P3-6 | Tracked root files `.body200.json`, `.code304.txt` are leftovers of the old `VERIFY.sh` | Product Owner |
| OBS-P3-7 | Plan v1.1 §10's step order needs step 3b whenever a unit changes the catalog validator (PD-15) | IA, for WU-PR-04, WU-PR-05 and WU-PR-08 (RP-2, confirmed in scope by the review §5) |
| OBS-P3-9 | The IF-7 roster entry for `artifacts/core/purity/purity_report.json` was a WU-PR-02 defect | Resolved in this unit by RP-3 (B-7); the IA carries the 22-path roster to WU-PR-04, WU-PR-05 and WU-PR-08 (review §10) |
| OBS-P3-8 | The `/reader` and runner documentation in `AGENTS.md` ("maintain the dev Reader helper (`scripts/dev_start_reader.sh`)") and `README.md` should state the start command with `APP_ENV=dev` now that RP-1 is decided | WU-DOC-01 |

**Carried** (instruction §15): OBS-W3-1 (Product Owner); LR-O1 and LR-O3 applied here (§6.10; EF-1); LR-O2 applies (B-9: the updater changes by one line; every consumer runs in the full sweep, §10 item 4); OBS-17 (RK-6); O-6 (RK-4); AQ-1 gates WU-PR-07 only.

## 18. PR-30 and PR-35 ownership

**PR-30** (after Nathan's Proceed for this exact plan), in the dedicated session:
- recovers existing work first (§8 step 1); implements only §7; produces governed evidence only through owners (§6.10, §7.2);
- tests locally (§10); makes one coherent commit or a coherent sequence (source, then convergence);
- writes and reads back the PR result record v1.0; opens the one PR; returns `PR_CANDIDATE_PUBLISHED` and hands off to PR-35 in its own dedicated session;
- does not own review correction, current-head CI readiness or merge.

**PR-35** (its own dedicated session, from PR-30's handoff):
- retrieves and resolves the Codex code review findings (addendum 2.3: no Codex security review);
- retests; pushes coherent corrections; any member change re-runs §6.10 from step 2, any evidence-primary change from step 3b;
- uses CI economically; verifies current-head CI (all seven lanes, `CI_APPLICABILITY_AND_EXACT_HEAD_OK`) and mergeability; records OBS-17 and O-6 if they occur;
- returns `MERGE_PENDING` without merging. Nathan merges manually; PR-40 by the IA follows the merge.

## 19. Session identity and recovery envelope

```yaml
change: HDE-CRD-0002 / WU-PR-03
phase: PR-20 complete; AWAITING_PO_PROCEED
plan: docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-implementation-plan-v1.1.md (v1.1)
predecessor: docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-implementation-plan-v1.0.md (v1.0, PENDING, preserved)
companion: docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-implementation-plan-v1.0-prototype.diff (unchanged)
rescope: request v1.0 → review v1.0 (APPROVE) → addendum record 2.6
instruction: docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-instruction-v1.0.md (v1.0, overlaid by addendum 2.6)
baseline: origin/main 150feabeee3d0c9a4d9012198cf854db653177f4
session_disposition: INITIAL_DEDICATED_ASSIGNMENT
role_session_ref: NOT_YET_ASSIGNED (Nathan / Product Owner)
authoring_session: https://claude.ai/code/session_01GC6jqu4Lczzk7PR7QGXSTJ
next: PR-30 on Nathan's Proceed for this exact plan
vehicle: none (no implementation branch, commit or PR exists for this unit's code)
resume_point: PR-30 §8 step 1
```

## 20. TypeSafe reading for the receiving session (PR-30, WU-PR-03, plan v1.1)

Action sent (v6): "Implement, in a new dedicated session after the Product Owner's Proceed, one work unit of an approved change from a detailed plan whose design was already prototyped, rehearsed and fully tested by the planning session and whose one bounded rescope is approved: about twenty-one hand-edited files (governed not-found handlers on two of three web app factories, an explicit-dev gate on a dev route, a CLI help string, removal of a broken dev harness, a verify script that now refuses without an explicit environment, an endpoint catalog grown from 10 to 23 rows with its generator, validator and route-enumeration test, three operator documents, a three-path CI classifier registration with one new owner test, a data-only contract-inventory baseline refresh, and one line removed from an evidence updater's label roster); two release members change, so a same-version release manifest refresh and a governed-evidence convergence of about a dozen owner-tool steps run in a fixed order, each proven byte-stable on a second run, followed by a full test sweep and an attestation build; then commit, open the pull request and hand off. No live vendor, production or database run; code review, review resolution and a lineage review follow."

- **TypeSafe v6: Opus 5.5, extra high.** Effort score 2.55 (confidence 0.65); rung probabilities low 0.00, medium 0.10, high 0.29, extra high 0.58, max 0.03, ultracode 0.00. Model probabilities Fable 5.1 0.06, Opus 5.5 0.94 (confidence 0.88). Twelve cells, computed from the two answers: Opus 5.5 at low 0.00, Opus 5.5 at medium 0.09, Opus 5.5 at high 0.27, Opus 5.5 at extra high 0.55, Opus 5.5 at max 0.03, Opus 5.5 at ultracode 0.00, Fable 5.1 at low 0.00, Fable 5.1 at medium 0.01, Fable 5.1 at high 0.02, Fable 5.1 at extra high 0.03, Fable 5.1 at max 0.00, Fable 5.1 at ultracode 0.00. Flags: boundary between high and extra high. Sent 2026-10-14T03:02:31Z. Nathan picks the cell.
- **Detail:** v6 sent 2026-10-14T03:02:31Z; HTTP 200 in 0.52 s; 4364 input and 54 output tokens; jev-1.13.0. Rung by rule: extra high (nearest to the score, halves up); model by rule: Opus 5.5 (P(most capable) 0.5 or more is Fable 5.1). Flags: boundary between high and extra high.
- **Notion row:** not written, as PR-20 directs. **Nathan's pick for PR-30:** not stated. **For this PR-20 session (plan v1.1):** not stated (reading in rescope review v1.0 §14).
- Earlier readings recorded in plan v1.0 §20 (PR-30 before RP-1; RS-20 with two and three items) are history and are not used for this plan.

**Surface advice:** run PR-30 as a new top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, with Notion read access for the prompt.
- **Environment.** A Python 3.12 environment with CI's install (package-index access for `pip install`), `ruby` on `PATH` for the contract-inventory test, and `bash` and `curl` for the runner propagation test and `VERIFY.sh`. All were present in this session's cloud container.
- **Run times observed in this lineage.** A full `tests/` sweep takes about 15 minutes; the two-pass convergence about 10; the evidence-lane tests about 13; an attestation build about 3.
- **Discipline.** The convergence rewrites governed files: run it in the working tree of the implementation branch only after the member edits are final, and run every check that can write tracked files in a detached worktree.
- **Access.** No live vendor, production or database access is needed.
- **Order.** This plan's pull request should be merged first.

## 21. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / WU-PR-03 / PR-20 / plan 1, version 1.1 (resumed after RS-20) |
| change / specification | CRD HDE-CRD-0002 / `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` v1.1 |
| work unit | WU-PR-03 (S02, S07, S09, S10, S15, S18) |
| release | GCFPE-20261009.1 / 100926.1 |
| prompt | PR-20 — Create Detailed PR Implementation Plan — 100926.1, https://app.notion.com/p/3f44590a05eb819fbea5dcd966a750ba (page state as of 2026-10-12T02:29:47Z) |
| role/stage | dedicated WU-PR-03 PR engineering session / PR-20 |
| capture time | 2026-10-14T03:05:07Z |
| execution identity | https://claude.ai/code/session_01GC6jqu4Lczzk7PR7QGXSTJ |
| inherited usage | PR-10 instruction 1 (instruction §20); PR-20 plan v1.0 and rescope request v1.0 (their own entries); RS-20 rescope review 1 (review §15) |
| repository persistence | recorded here only (installed writer `docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent; pending, non-gating; owner the Product Owner) |

## Canon precedence (Plan Templates, "Canon precedence for template use")

> Applicable, active, non-superseded PF10 addenda supersede conflicting PF-Canon only for the exact scope they address; otherwise follow PF-Canon. A formally approved bounded Product Owner rescope may supersede conflicting PF-Canon only for the exact decision it adjudicates.

## Canon relied on

Read on `main` at `20f16d0`, and for v1.1 re-resolved on `main` at `150feab` (`docs/pfcanon/` unchanged since `ad11821`).

| Topic | Sources and sections |
| :- | :- |
| Plan authority, hold and Proceed | PR-20 — Create Detailed PR Implementation Plan — 100926.1 (read in full); PR-30 — PR Implementation Proceed — 100926.1 (receiver contract); RS-20 — Review Bounded Work-Unit Rescope — 100926.1 (receiver contract of the rescope request); HDE Governance (`docs/pfcanon/PF04-Canon-HDE-Governance-v2.8.7.md`) §9.1.1 and §9.1.2; Plan Templates (`docs/pfcanon/PF27-Canon-Plan-Templates-v2.0.5.md`) "Canon precedence for template use" |
| Start-helper `APP_ENV` (RP-1; CR-6) | HDE Architecture (`docs/pfcanon/PF02-Canon-HDE-Architecture-v2.4.6.md`) §3.8.1 (read in full); HDE Mechanics Guide (`docs/pfcanon/PF14-Canon-HDE-Mechanics-Guide-v3.5.8.md`) §5.6 start-helper paragraph and §34; Glow Infrastructure (`docs/pfcanon/PF07-Canon-Glow-Infrastructure-v2.3.3.md`) §8.1 `APP_ENV` note; HDE Build Checklist — Conjunction (`docs/pfcanon/PF09.4-Canon-HDE-Build-Checklist-Conjunction-v1.3.1.md`) HDE-CONJ001.4; Glow QA Guide (`docs/pfcanon/PF19-Canon-Glow-QA-Guide-v3.0.6.md`) §13.9; HDE Math Spec (`docs/pfcanon/PF01-Canon-HDE-Math-Spec-v1.3.8.md`) §12 dev-harness bullet |
| Overlays and carried items | PF10-HDE-Build-Notes v13.5.6 (`docs/pfcanon/PF10-HDE-Build-Notes-v13.5.6.md`) addenda 2.2 ("Approved delta", "Binding requirements", "Affected surfaces"), 2.3 (Rules 1–5), 2.5 (carried items), 2.1 (§20); addendum record 2.6 (`docs/ephemeral/HDE-CRD-0002-WU-PR-03-PF10-build-notes-addendum-v1.0.md`, read in full) |
| Approved rescope | RS-20 rescope review v1.0 (`docs/ephemeral/HDE-CRD-0002-WU-PR-03-rescope-review-v1.0.md`, read in full: §1–§12, B-1 to B-12) |
| S02, PD-2 | HDE-CLI-API-Vendor-Ref (`docs/pfcanon/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.3.md`) §5.2 item 1 and item 2; §5.1.0 (line 2071); §5.1.7; §5.5 "Errors", "Method and subpath handling"; §5.10 (`Allow: POST`) |
| S10, S09, OBS-W3-1 | HDE-CLI-API-Vendor-Ref §5.4 (read in full); HDE Schemas & Artifacts (`docs/pfcanon/PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.6.md`) §8.8 "Reader surface routes and distinct contracts (normative)"; HDE Architecture §3.8.1 "Current repository discrepancy" and HDE Math Spec §12 dev-harness bullet (ID-2) |
| S15, ID-1 | HDE-CLI-API-Vendor-Ref §5.6 (read in full); HDE Schemas & Artifacts §8.8 (read in full) |
| Refresh | Implementation Plan v1.1 §10; `AGENTS.md` "Release identity" and "HDE-EPIC040 admission addition"; instruction §5.7 |
| In-flight documents | Specification v1.1 rows S02, S07, S09, S10, S15, S18; Plan v1.1 §3, §4, §5 (IF-6, IF-10, IF-11), §7, §10–§15; review v1.1 R1.1–R1.3 (as carried by the instruction); PR instruction v1.0 |
| Operative documentation | `AGENTS.md` (canon-first rule; closed rails; pytest readiness; sole Index/Mirror writer; no hand edits; endpoint catalog source of truth; PR descriptions) |

## Checks run by this session

All in the session scratchpad (detached worktrees of `20f16d0`; never pushed), CPython 3.12 with CI's install, pytest 8.4.2, `ruby` at `/usr/local/bin/ruby`, closed rails:

| Check | Result |
| :- | :- |
| `url_map` enumeration of the three factories | 53 pairs; 10 catalogued; 43 uncatalogued (28 excluding OPTIONS) |
| Contract-inventory baseline rebuild at `20f16d0` | byte-identical to the tracked literal (21 records) |
| Request matrix, 22 requests × 3 factories × 2 environments, `main` vs prototype | compat and `api_bp` 31 keys unchanged; changes as §4.3 |
| Boundary analyzer on the S02 designs | cross-module helper and `return err`: rejected; nested presenter helper: accepted (F-13) |
| Cut, recompute, cutter `--check`, admission (three times) | exit 0; `1.3.0`, 45 members |
| Rehearsal 1 (Plan v1.1 §10 order) | steps 5–6 exit 1 on pass 1 (F-2) |
| Rehearsal 2 and 3 (§6.10 order, two passes each) | 64 of 64 runs exit 0 each; passes byte-identical |
| EC-4 start-helper variant, `APP_ENV` unset | `/reader` 200 (F-11) |
| Roster-correction variant: seven evidence checks; 7 evidence and engine-core test files | all exit 0; 142 passed |
| Full `tests/` sweep, first design | 213 failed, 4,531 passed (explained in §4.3) |
| Full `tests/` sweep, final design | 4,747 passed, 3 skipped, 2 xfailed, 0 failed |
| `VERIFY.sh`, `check_cli_help.sh`, CLI conformance `--check` | as §4.3 |
| Stale-binding sweep (final) | `README.md` and frozen HDE-EPIC040 records only |
| Classifier on the final candidate paths | all seven lanes; 164 targets |

For v1.1, this session also ran, at `150feab`:
- `git diff --name-only 20f16d0 150feab` outside `docs/ephemeral/`: empty;
- `git apply --check` of the companion diff: succeeds (21 files; no `scripts/dev_start_reader.sh` hunk; one deleted roster line; the `VERIFY.sh` refusal present);
- PF10 resolution: `docs/pfcanon/PF10-HDE-Build-Notes-v13.5.6.md` is the unique controlled PF10.

The rescope review independently reproduced the decisive v1.0 results at `852370c` (review §3.3 and §4.2): the owner test 10 passed with the script byte-unchanged; the cut digest `72fca4c3…` equal to rehearsal 3; the stale label and its correction; the label and engine-core tests 74 passed. v1.1 relies on v1.0's rehearsals and final sweep, which the design change-free successor does not invalidate, and does not re-run them.

Not executed: the attestation build and verify (§6.10 step 12), the seven lanes' exact `ci.yml` commands as a set, and hosted CI. These are PR-30 and PR-35 obligations. No live vendor, production or database call was made.
