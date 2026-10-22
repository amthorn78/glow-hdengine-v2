---
artifact_type: PR_IMPLEMENTATION_PLAN
artifact_id: HDE-CRD-0002-WU-DOC-01-PR-IMPLEMENTATION-PLAN
artifact_version: "1.0"
artifact_state: AWAITING_PO_PROCEED
predecessor: none (first plan for WU-DOC-01)
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-DOC-01
work_unit_title: "Final repository documentation (DOC; after WU-PR-08)"
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-DOC-01-pr-instruction-v1.0.md (v1.0, INSTRUCTION_READY; blob c49ff720ffd2; landed by #690 as b7458aa)
IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (v1.1, approved; blob abffa2ccbd44) §7 WU-DOC-01, with Plan delta 01 docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-v1.1.md (v1.1, DELTA_APPROVE; blob 5103fe29d588), whose P-8 is this unit's bounded scope
SPECIFICATION_ID: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (v1.1, SPECIFICATION_APPROVED; blob c4802a5a7fa3), with Specification delta 01 docs/ephemeral/HDE-CRD-0002-specification-delta-v1.0.md (DELTA_APPROVE by docs/ephemeral/HDE-CRD-0002-specification-delta-review-v1.0.md)
PLAN_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (IA-30 INITIAL_APPROVE; blob 0cc0276524b2); the delta's approval docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-review-v1.1.md (IA-30 DELTA_APPROVE; blob 4801c7cc2c9d)
IMPLEMENTATION_AUDIT_ID: docs/ephemeral/HDE-CRD-0002-implementation-audit-v1.0.md (v1.0, AUDIT_COMPLETE; blob b39ac9f276db)
REMEDIATION_REVIEW_ID: none (no remediation lineage)
business_case_ref: docs/ephemeral/HDE-CRD-0002-WU-DOC-01-po-disposition-business-case-v1.0.md §2 (Product Owner adoption, 2026-10-22; blob 28b3deb24cb9; #689). No cost ceiling (addendum 2.18)
AUTHORING_CONTEXT: APPROVED_BASE_WITH_OVERLAYS
immutable_approved_base: Specification v1.1 (approved) → Implementation Plan v1.1 + IA-30 review v1.1 (approved)
effective_baseline: approved base + applicable PF10 overlays — Specification delta 01 (addendum 2.20), Plan delta 01 (addendum 2.19; P-8 sets the scope and drops the dedicated-environment install note), addendum 2.21 (routes the stale-document list to this unit), addendum 2.17 (read with the S21 ADR for the writer usage note), addendum 2.15 (the close-run family), addendum 2.12 (LR6-O5, LR6-O7, G-1), addenda 2.18, 2.11 (as 2.18 narrows it), 2.14 and 2.3
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.7.4.md (blob 1343ae09018e; 433,368 bytes; sha256 8ac9723214bd90d12f8cf723e0a1f060ddaf73bc4f91c555447de7c6016d37ff; the only PF10 file on main at b7458aa; addenda 2.1 to 2.21, 2.21 the last)
pf10_addendum_paths: docs/pfcanon/PF10-HDE-Build-Notes-v13.7.4.md §2.21, §2.20, §2.19, §2.18, §2.17, §2.15, §2.14, §2.12, §2.11, §2.3 (all inside that one file; read in full: 2.15, 2.17, 2.19, 2.21; read at the cited passages: 2.8, 2.10, 2.12, 2.16)
pf10_addendum_created: none (PR-20 is not a qualifying approval prompt)
companion_prototype_diff: docs/ephemeral/HDE-CRD-0002-WU-DOC-01-pr-implementation-plan-v1.0-prototype.diff (git diff b7458aa → prototype head 3d7b69ec; 10 files, +137/−57; 510 lines; 85,565 bytes; sha256 a334c348bf37187dab26a9051e9ee2f7a56692723fc1dd5f6838c8600e60ab63; `git apply --check` clean on b7458aa)
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
session_disposition: INITIAL_DEDICATED_ASSIGNMENT
role_session_ref: https://claude.ai/code/session_011Y6ExL6PGDrodZqKLRWCHK (the dedicated WU-DOC-01 PR engineering session that Nathan created; PR-20 now, PR-30 after the Proceed)
prompt: PR-20 — Create Detailed PR Implementation Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb819fbea5dcd966a750ba; page state as of 2026-10-12T02:29:47.327Z, fetched and read in full in this session)
repository_baseline: origin/main b7458aa448cf37357f8a9b9745ef2401d9d78a38 (#690). Outside docs/ephemeral/, every byte equals 6f2478f, the instruction's measured baseline (git diff --stat 6f2478f b7458aa outside docs/ephemeral/ is empty)
working_branch: claude/sharp-carson-5ttoho, from b7458aa (documents under docs/ephemeral/ only)
product_owner_decisions_in_this_session: Q-A6 "Keep, marked not current"; Q-AG "No AGENTS.md addition" (§5, 2026-10-22, answered through the session's question tool)
created_at: 2026-10-22T01:58:00Z
canon_conflict_register: CR-1 to CR-8 carried unchanged, all decided; no new entry (§18)
---

# HDE-CRD-0002 WU-DOC-01 — PR Implementation Plan v1.0

## 1. Result

**AWAITING_PO_PROCEED for v1.0.** This is the complete plan for WU-DOC-01 within P-8's bounded scope and addendum 2.21's routed items. It changes ten repository Markdown documents and nothing else.

- **The work:** 55 planned edits, all drafted to their exact text (§6). The companion diff carries them byte for byte, and PR-30 applies it with `git apply`.
- **No change:** `docs/server/reader_v1.md` (V-1) and README line 132 (R-8) stay as they are.
- **The prototype:** applied in a throwaway clone of `b7458aa`, it passed every check (§12):
  - the `AGENTS.md` citation checker;
  - the six document-reading test files: 1,248 passed, 0 failed, with CI's full install;
  - the pre-push `lanes` report (`documentation_only`) and `membership` report (no member changed);
  - only the ten planned paths changed.
- **Product Owner decisions:** the two questions the instruction reserved (§9.2) were asked in this session and answered (§5, PD-6 and PD-7).
- **Not done here:** no implementation, publication, merge, Ops, QA, acceptance or closure. This plan is pending the Product Owner's PR-30 Proceed for exactly v1.0.

## 2. Lineage and sources read in this session

| Source | Identity | How read |
| :- | :- | :- |
| PR instruction | `docs/ephemeral/HDE-CRD-0002-WU-DOC-01-pr-instruction-v1.0.md` (blob `c49ff720ffd2`) | in full |
| Business case | `docs/ephemeral/HDE-CRD-0002-WU-DOC-01-po-disposition-business-case-v1.0.md` | in full |
| Plan delta 01 P-8 | inside PF10 addendum 2.19 ("Approved delta, complete") | addendum 2.19 in full |
| Predecessor acceptance | `docs/ephemeral/HDE-CRD-0002-WU-PR-08-pr-work-unit-lineage-review-v1.0.md`, as PF10 addendum 2.21 records it (LR8-F2, LR8-O1) | addendum 2.21 in full |
| Writer usage note | PF10 addendum 2.17; `docs/adr/hde/close_pack_writer_adr.md` (blob `fcaa9da66fb7`) Decision, Stated limits, Nonclaims; addendum 2.15 | in full |
| Pre-push note | PF10 addendum 2.12, rows LR6-O5 and LR6-O7; WU-PR-06 instruction v1.0 contract G-1 | at those rows |
| Routed items | the eight lineage reviews' WU-DOC-01 rows; WU-PR-03 plan v2.0 §18; WU-PR-04 plan v1.0 §17; WU-PR-07 plan v1.1 §18 and result v1.0 §9; WU-PR-08 plan v1.0 F-2; the S19 record O-19 | searched and read at the rows (§7; a worker searched them and I checked the decisive rows) |
| The ten documents, `docs/server/reader_v1.md` and `docs/INDEX.md` | at `b7458aa` | in full where edited; at the cited lines elsewhere |
| Code and tools | `ci/checks/classify_ci_changes.py`, `ci/checks/check_agents_md_citations.py`, `ci/checks/check_direct_db_contract.py`, `tools/ci/prepush_check.py`, `tools/qa/generate_epic_close_pack.py`, `schemas/close_candidate_source.v2.json`, `tools/evidence/update_evidence_index.py`, `tools/evidence/generate_a7_transport_proofs.py`, `tools/evidence/build_release_attestation.py`, `adapter/wsgi.py`, `adapter/http_reader.py`, `adapter/factory.py`, `engine/bodygraph/resolver.py`, `engine/cli/main.py`, `scripts/make_release_pack.sh`, `scripts/hd_cli.py`, `Procfile` | at the lines cited in §6 |

## 3. Business case

Adopted by the Product Owner and carried unchanged (disposition record §2):
- **Beneficiary:** agents and operators who take repository workflow from `AGENTS.md` and `README.md`.
- **Benefit:** a session following them uses the delivered pre-push check and v2 close-pack source, not an outdated description.
- **Measure:** each statement WU-DOC-01 changes matches merged `main`, checked at DOC-20. §6 is the statement-to-proof list that DOC-20 verifies (instruction §9.5).
- **Ceiling:** none (addendum 2.18).

## 4. Baseline re-check (instruction §9.3)

All facts were re-measured at `b7458aa` under closed rails (`env -i`, `SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC`), CPython 3.12.3, in a throwaway clone. The venv held CI's full install, `'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e .`.

### 4.1 Confirmed as the instruction states

- Release `1.3.0`, built `2026-08-24T18:04:49Z`, 45 members.
  - `release_id` `77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e`, recomputed from `catalog/manifest.json`.
  - `scripts/release_id_recompute.py --check-manifest-only` exits 0; admission loads.
- No §6 document and not `docs/INDEX.md` changed between `1a4c8ab` and `b7458aa`.
- The tools and their facts:
  - `prepush_check.py --help` (exit 0);
  - `REPLAY_WORKFLOW_SHA256` `d02021f3…` equals the sha256 of `ci.yml`;
  - `generate_epic_close_pack.py` usage `--source SOURCE (--write | --check)`;
  - `ADMITTED_CRD_QA` at updater lines 51–54;
  - the A7 writer (`HDE_WRITE_A7_PROOFS=1` gate at line 176; `--check` passes; `PROOFS` at line 31);
  - `artifacts/release_id.txt` holds `8ca9ba71…`, written by `scripts/make_release_pack.sh` and read by `scripts/hd_cli.py`;
  - the `Procfile` line.
- The classifier and workflow facts behind A-3:
  - `docs/run/PROD_ENDPOINTS.json` and `docs/run/EPIC011_TEST_IDENTITIES.md` select `evidence`; they are the only Human Index rows under the eight prefixes;
  - every `.path_proof.txt` selects `evidence`, under a prefix or not (`classify_ci_changes.py:1732`);
  - the workflow filter re-includes `**.path_proof.txt` and those two files.
- S03 at the head: `prepush_check.py --no-run sweep` reports 215 tracked test files, `uncovered=0`.
- Pre-push reports on the eleven documents: `documentation_only`, no lanes, none a member of `1.3.0`, PF10 path and sha256 as in the front matter.

### 4.2 Differences from the instruction (each recorded; none changes scope)

| ID | Instruction statement | Measured at `b7458aa` | Effect |
| :- | :- | :- | :- |
| BR-1 | §5.5: five `hdctl` failures in the baseline | With CI's full install, the six test files pass: **1,248 passed, 0 failed**, about 76 s. The five failures came from the instruction's own environment, which lacked `-e .`, as it says (DOC10-F2) | none. §11 runs with the full install |
| BR-2 | §10 item 4: run `prepush_check.py lanes membership build-notes` | `membership` needs at least one `--path` ("FAILURE membership needs at least one --path"), so that command fails. Also, given `--path`, `lanes` switches to paths mode | §11 gives two commands: `lanes build-notes` in refs mode, and `membership` with one `--path` per changed file. The README and `AGENTS.md` usage text says the same (R-2, A-4) |
| BR-3 | A-6 fact: "an edit to them still fails classification with `CI_EVIDENCE_OWNER_TEST_MISSING`"; "their tests were retired (lines 44 and 49)" | Per generator, through `_evidence_generator_owner_targets`:<br>• `field_sufficiency`, `bg_resolve` and `parent_binding` raise `CI_EVIDENCE_OWNER_TEST_MISSING`;<br>• `v2_adapter` has its owner `tests/evidence/test_hde_epic037_v2_adapter.py`;<br>• `v2_to_compat` has its owner `tests/compat/test_hde_epic037_v2_adapter_to_compat.py`.<br>`classify_paths` alone selects `evidence` for all five. The retired evidence tests are `bg_resolve`, `field_sufficiency`, `pr05_parent_binding` and `v2_to_compat` (`tests/retired_tests.md` lines 48–51); `v2_adapter`'s test is not retired.<br>`--check`: `parent_binding` passes; the other four fail (three `STALE_…`, and `bg_resolve` `KeyError: 'adapter'`) | the A-6 text states the per-generator facts (§6.2) |
| BR-4 | §5.3 and D-4: `RELEASE_ID` "defaults to `rel_dev`"; `ENGINE_ENV` "read only as a fallback when `APP_ENV` is blank" | `RELEASE_ID` and `ENGINE_TAG` are Flask app-configuration defaults in `adapter/wsgi.py` (lines 14–15), not environment variables. `X-Engine-Tag` is `Isis6`, not the identity's `engine_tag`. `engine/config/provider_loader.py:51` reads `ENGINE_ENV` before `APP_ENV`. The resolver refuses when both are set and differ (`resolver.py:91`) | the D-4 and D-6 text scopes each statement to the code that reads it (§6.6) |
| BR-5 | not stated | `/internal/version` has **six** body keys, `engine_tag, build_commit, invocation_tag, invocation_sha256, emitter_sha256, release_id`, pinned by `tests/transport/test_internal_version_contract.py:134`. `docs/ADAPTER_009.md` lines 16 and 227–228 state five keys in another order | new item D-9, inside D-1's subject (§9.3) |
| BR-6 | D-6: the `X-Release-Id` line | The "Required headers (all responses)" set is applied only by `adapter.wsgi`. `adapter.factory`'s `/internal/version` response carries only `Cache-Control`, `Content-Length` and `Content-Type` | D-6 widened to the header block, which the instruction names ("and the header block") |
| BR-7 | D-1 to D-3 name lines 7–8, 20–21 and 44 | Lines 38–42, the "Auth (prod)" block (401 for a missing bearer), are also stale. They belong to LR8-F2's "Bearer statement" | D-3 covers lines 38–44 |
| BR-8 | not routed by the instruction | `docs/EVIDENCE_INDEX.md` lines 125–126 name the test as the A7 proof generator and list `encoding_invariance.txt`. `docs/RUN.md:82` says "APP_ENV=dev by default" | new items E-4 (subject of R-4 and P-1) and U-3 (subject of U-1) |
| BR-9 | L-1 "known delivered changes: S07, S08, S14 … line 78 already current" | S07, S08 and S14 are already stated. The final pass found 11 mismatches (§6.5) | L-1a to L-1k |
| BR-10 | routed item omitted | WU-PR-04 plan v1.0 §17 routes "`README.md`, `AGENTS.md` mentions of the override and the CLI … the shipped flag, the sink key and the band behavior" to WU-DOC-01 (carried by addendum 2.9). README lines 157 and 190 do not state them | new item R-9 in README. `AGENTS.md`: no addition, by the Product Owner's decision (PD-7) |
| BR-11 | dev `GET /reader` refusal | `APP_ENV` `test`, `local` and `prod` → 403 `ERR_READER_FORBIDDEN`; `dev` → 200 (test client) | R-5 states it |

## 5. Design decisions (instruction §9.1 and §9.2)

| ID | Decision | Reason |
| :- | :- | :- |
| PD-1 | **One PR.** | All edits are Markdown, `documentation_only`, with no member and no dependency between them (§10) |
| PD-2 | **R-2 gets its own README section**, "Pre-push check (HDE-CRD-0002)", after "Quickstart". | The note is long (reports, options, read-only rules, exit status, prerequisites, LR6-O7 limits, nonclaim); a section keeps Quickstart short. `AGENTS.md` A-4 points to it by heading |
| PD-3 | **R-3 is a new "What HDE-CRD-0002 adds to the close-pack writer (current)" block** at the top of README's Overview epic blocks, before HDE-EPIC040. | The HDE-EPIC039 line stays as that epic's record (instruction R-3). The README title ("HDE-EPIC040 current documentation") is left as it is: no item names it |
| PD-4 | **CHANGELOG grouping:** the existing "Added" / "Changed / Fixed" form, one bullet per delivered requirement group, each naming its requirement and merged PRs, then "Not delivered" (S01) and the nonclaims. | Matches every entry since HDE-EPIC034 |
| PD-5 | **A-3:** the factual sentence is corrected (two exceptions, and the workflow's re-includes). The review-scope rule's sentences, its bolded rule and the eight-prefix list stay byte-identical. | The rule exempts the eight prefixes, and still does; the correction names which paths under them CI runs. It does not change the set the 2026-09-21 rule exempts, so no Product Owner question was needed (§9.2). PR-35 and PR-40 can verify by diff that the bolded sentence is unchanged |
| PD-6 | **A-6 (Product Owner decision, 2026-10-22, "Keep, marked not current"):** `parent_binding --check` stays listed with the passing checks; the other four generators are named as not current validation entrypoints, with the measured reasons. | Asked under instruction §9.2. Nathan chose the recommended option |
| PD-7 | **No `AGENTS.md` change beyond A-1 to A-7 (Product Owner decision, 2026-10-22, "No AGENTS.md addition").** | Asked under instruction §9.2 for BR-10. The flag, sink key and band behaviour are stated in README (R-9) and `docs/CLI_commands.md` (lines 16–21), and `AGENTS.md` has no stale statement about them |
| PD-8 | **X-1:** of the 15 measured hits, only `docs/RUN.md:66` is a runnable command. It gains `APP_ENV=dev` and the recognized-value rule. The other 14 are descriptions or history and stay. `docs/INDEX.md` is not edited. | Classification table in §6.4 |
| PD-9 | **`docs/ADAPTER_009.md` history:** the epic-labelled sections "Internal Ops — HTTP Transport Evidence (EPIC-005)" (lines 185–217) and "EPIC-006 — posture" (lines 219–224) stay as history. | §7: historical entries stay. The two current "invariants (enforced)" blocks (lines 12–17 and 226–228) are corrected (D-9) |
| PD-10 | **D-7:** the section heading becomes "RUN — Production start (repository `Procfile`)". The text states the `Procfile` line and that it says nothing of the live service's settings. "Deploys come from commits on `main`" is not written. | §7 excludes deploy-trigger statements |
| PD-11 | **Wording discipline:** new `AGENTS.md` text names no PF document other than PF10, names PF10 only as "HDE Build Notes" with no locator, and uses no PF title. It avoids the word "bridge" in active guidance. | `check_agents_md_citations.py`; `check_direct_db_contract.py`. Both pass on the prototype |

## 6. Items, exact changes and proofs (the statement-to-proof list DOC-20 verifies)

The exact text of every change is in the companion diff. "Proof" names the code, help output or record that establishes the statement at `b7458aa`. Edit labels match the diff hunks.

### 6.1 `README.md` (+39/−7)

| Item | Change | Proof |
| :- | :- | :- |
| R-1 | Line 13: `release_id` `77204764…c51e`, "refreshed the manifest in place at `1.3.0`, with no version cut" | manifest recompute (§4.1); addendum 2.19 "Release identity"; manifest refreshes in #643, #646, #651, #656 |
| R-2 | New section "Pre-push check (HDE-CRD-0002)": two example commands; the five reports and `all`; the options and defaults; the read-only rules; exit status 0–4; prerequisites; the LR6-O7 limits and LR6-O5; the nonclaim | `prepush_check.py --help`; `EXIT_*` constants (lines 80–84) and `main` (lines 1690–1751); `SWEEP_TOOLS` (line 116); `REPLAY_WORKFLOW_SHA256` (line 122); addendum 2.12 LR6-O5 and LR6-O7; contract G-1 ("command, report names, arguments, environment prerequisites, exit rule and nonclaims"); BR-2 |
| R-3 | New Overview block: v2 source, schema and identities; output paths; close-run family pointer; the ADR read with HDE Build Notes; stated limits (review-trace-only posture; resolution A; resolution B; LR7-O15's presence registration); nonclaims; pointer to R-2 | `generate_epic_close_pack.py` lines 2182–2215, 2335–2339; schema `change_id` pattern; ADR "Decision" 1–3 and "Stated limits"; addendum 2.17 resolutions A and B; addendum 2.15; WU-PR-07 lineage review LR7-O15; WU-PR-07 result v1.0 §9 nonclaims |
| R-4 | Line 102: the A7 proof writer, its `HDE_WRITE_A7_PROOFS=1` gate and `--check`. Line 218 removed (retired test). New "CI coverage" bullet in "Testing (minimal)" | `generate_a7_transport_proofs.py` lines 31, 166–180; `tests/retired_tests.md` (the EPIC022 scaffold row); sweep `uncovered=0` (§4.1) |
| R-5 | Line 159: the start command, loopback bind, `PORT` default, `APP_ENV` exactly `dev`, 403 otherwise | `adapter/http_reader.py:1315–1325` and 383–389; BR-11 |
| R-6 | New "Release identity" bullet: `artifacts/release_id.txt` is not the release identity | `scripts/make_release_pack.sh` lines 6 and 28; `scripts/hd_cli.py:15`; O-19; LR8-O1 |
| R-7 | Line 135, one sentence: off-CI attestation under a distribution-patched setuptools, recorded as `build_backend_compat=distribution_install_layout` | `build_release_attestation.py` lines 341–418 and 464 |
| R-8 | **No change** (line 132's wheel limitation stays; no install note) | P-8; addendum 2.19 |
| R-9 | Line 157: `--band`, `--category` and `--perspective` with `--pair-file`. Line 190: recognized `APP_ENV`, `--allow-prod-vendor`, one read, `HDE_VENDOR_OVERRIDE_AUDIT_PATH` | `engine/cli/main.py:597–628`; `resolver.py:40–41`, 285–331; WU-PR-04 plan v1.0 §17; BR-10 |

### 6.2 `AGENTS.md` (operative passages only; +11/−5)

| Item | Change | Proof |
| :- | :- | :- |
| A-1 | New bullet after the generic closeout line: v2 schema, identities, output paths, the ADR deferring to HDE Build Notes (resolutions A and B in words), capability-only nonclaims. The HDE-EPIC039 lines stay | as R-3 |
| A-2 | Line 125: `release_id` and "refreshed … in place at that version, with no version cut". Line 130 unchanged | as R-1 |
| A-3 | Lines 69–70: the two exceptions and the workflow's re-includes. The rule's other sentences are byte-identical (PD-5) | `classify_ci_changes.py:1017–1047`, 1732, 1758, 1897–1899; `ci.yml` lines 4–17; §4.1 |
| A-4 | Line 55: CI's install and why `-e .` matters; readiness proof kept. New "Pre-push check" line (this is A-7, placed with A-4) | `ci.yml` lines 87–94; BR-1; as R-2 |
| A-5 | Line 45: start command, loopback bind, `APP_ENV` exactly `dev` | as R-5 |
| A-6 | Line 169: `parent_binding --check` with the passing checks; the four others named as not current, with BR-3's facts | BR-3; `--check` runs (§12.3); PD-6 |
| A-7 | See A-4 (one line in "Operating workflow") | as R-2 |

`AGENTS.md` is otherwise unchanged (PD-7; instruction §6.2). The Product Owner's Proceed on this exact plan is the instruction for these edits (instruction §9.2).

### 6.3 `CHANGELOG.md` (+25/−0)

| Item | Change | Proof |
| :- | :- | :- |
| CH-1 | New top entry "Unreleased — HDE-CRD-0002 …": Added (S20, S21, S22, S11–S13, S16, S19) and Changed / Fixed (S03–S05, S06, S02, S07, S08, S09 with S10, S14, S15, S18 with S17, the `1.3.0` refresh, this pass), each with its merged PRs; "Not delivered" S01; nonclaims. Historical entries, including the 2025-10-16 harness note, stay | instruction §4 mapping; merge commits `7136040` (#627), `bf7ad8c` (#630), `1d2c834` (#634), `b26f44f` (#637), `c98d41f` (#643), `2f3db0a` (#646), `5892538` (#651), `822ce15` (#656), `b963ed4` (#660), `8b73b57` (#668), `1a4c8ab` (#687); manifest history (#643, #646, #651, #656) |

### 6.4 `docs/EVIDENCE_INDEX.md`, `docs/qa_harness_pattern.md`, `docs/RUN.md`

| Item | Document | Change | Proof |
| :- | :- | :- | :- |
| E-1 | EVIDENCE_INDEX | New section: the `ADMITTED_CRD_QA` rows, refusal by both publishers, not discovery | updater lines 47–54, 5180–5186, 5240–5246 |
| E-2 | EVIDENCE_INDEX | The label text, regeneration-only labelling, frozen families unlisted, "not proof that an owner ran" | updater lines 56–88 (`CURRENT_RELEASE_CAPTURE_PATHS`, `_CURRENT_RELEASE_LABEL_RE`); OBS-W2-1 |
| E-3 | EVIDENCE_INDEX | Close-run family path, members, writer API, transaction, QA-family precondition, Index key, no Epic family, none exists | updater lines 4008–4042, 5222–5300; addendum 2.15; no `close/` directory under `audit/qa/` at `b7458aa` |
| E-4 | EVIDENCE_INDEX | Lines 125–126: `success_encoding_invariance.txt`; the writer, its gate and `--check` | as R-4; `tests/transport/test_a7_transport_proofs.py:141–142` |
| Q-1 | qa_harness_pattern | Line 79: admitted CRDs per the table. Line 83: keys use the admitted prefix. New paragraph: `publish_crd_close_run_family` | as E-1 and E-3 |
| U-1 | RUN | Line 5: binds `127.0.0.1` only | as R-5 |
| U-2 | RUN | Line 9: `tests/infra/test_sercanon_bytes.py` | `tests/retired_tests.md` (the `tests/test_sercanon.py` row); the file exists |
| U-3 | RUN | Line 82: the caller supplies `APP_ENV=dev`; the script never defaults it | `docs/server/reader_v1.md` line 19 (current state); `scripts/dev_start_reader.sh` |
| X-1 | RUN | Line 66: `APP_ENV=dev` prefix; the recognized-value rule | `resolver.py:39–41`, 73–100 |

X-1 classification (15 measured hits):
- **Runnable command:** `docs/RUN.md:66` → changed.
- **Descriptive or historical, unchanged:**
  - `AGENTS.md` 166, 173 and 181;
  - `CHANGELOG.md` 40, 51 and 67;
  - `README.md` 60 and 70;
  - `docs/CLI_commands.md` 51 and 52;
  - `docs/EVIDENCE_INDEX.md` 74;
  - `docs/INDEX.md` 32 and 35;
  - `docs/RUN.md` 65.
- **Count check:** 1 + 14 = 15.

### 6.5 `docs/CLI_commands.md` (L-1 final pass; +9/−7) and `docs/server/reader_v1.md`

Every line was compared with `hdctl --help` and each subcommand's help (all exit 0), and with the source. A worker made the comparison; I checked the decisive claims myself: aux-preview `main.py:597–662`; the stdout guard `main.py:570–575` with `CliError` default 64 against HDE CLI/API/Vendor Ref §4.1.4's exit 1; conjunction acquisition `resolver.py:915–927`; the audit events `resolver.py:285–331`. `tests/cli/test_cli_usage_and_errors.py` does not read the document; it only names it in a comment.

| Edit | Line | Change | Proof |
| :- | -: | :- | :- |
| L-1a | 3 | "Reader HTTP adapter (`adapter/http_reader.py`)" for the retired harness (S09). `hdctl` does not call `ensure_determinism_env`; the resolver's exact-value rails | no call under `engine/`; `resolver.py:133–145` |
| L-1b | 14 | aux-preview synopsis: `--category`, `--band` and `--perspective` optional with `--pair-file` | aux-preview help; `main.py:609–619` |
| L-1c | after 16 | defaults; the no-pair-file mode (`MISSING_AUX_INPUT`, exit 64) | `main.py:623–628` |
| L-1d | after 17 | `--source vendor` needs the birth tuple (`MISSING_VENDOR_INPUT`, exit 64); `db` and `auto` are the S8a stub | `main.py:263–267`; `resolver.py:215–224` |
| L-1e | 21 | recognized values; a conflict refuses | `resolver.py:39–41`, 91–92 |
| L-1f | 21 | audit events: one `refused` without the flag; `allowed` then a state event with it; `PROVIDER_AUDIT_UNAVAILABLE` only with the flag; in-repository sink refused; `--dry-run` without `--upsert` | `resolver.py:293–331`; `vendor_audit.py:86–105` |
| L-1g | 25 | computation-only only for complete charts; the DB lookup; a read-only vendor fallback that persists nothing | `main.py:468–491`, 729–736, 793–800; `resolver.py:915–927` |
| L-1h | 27 | the exit mismatch is now the `STDOUT_*` guards (64 against canon's 1); the guard is showcompat's; aux-preview prints text | `main.py:60–66`, 570–575, 801, 829; HDE CLI/API/Vendor Ref §4.1.4 |
| L-1i | 27 | the exceptions to "stderr code strings"; aux-preview stdout and `--admin-out` | `main.py:274–281`, 643–662 |
| L-1j | 64 | no `.sha256` beside `artifacts/cli/abba_sidecar.json` | `git ls-files artifacts/cli` |
| L-1k | 78 | `GET /reader` only for `APP_ENV` exactly `dev`; loopback bind | as R-5 |
| V-1 | — | `docs/server/reader_v1.md`: **no change**. No not-found limitation line exists; line 20 ("Unknown paths") states the delivered behaviour | file read at `b7458aa`; probes in §12.4 |

### 6.6 `docs/ADAPTER_009.md` (+27/−27), `docs/contracts/reader_v2_public_bytes.md`, `docs/acceptance/reader_a7_crib.md`

| Item | Lines | Change | Proof |
| :- | -: | :- | :- |
| D-1 | 7–8 | one `/internal/version` line: every app factory, no authorization check | test client: factory, http_reader and wsgi all 200 under `APP_ENV` `dev` and `prod`, with or without `Authorization` (§12.4) |
| D-2 | 20–21 | no authorization; `Authorization` ignored; no code reads `ENGINE_SERVICE_TOKEN`; `X-Identity-Override` → 400; local captures on `127.0.0.1:8000` | `adapter/http_reader.py:1175–1196`; grep over `adapter/` and `engine/` |
| D-3 | 38–44 | "Auth" block: no 401; the EPIC-005 note without its forward-looking sentence | as D-1; BR-7 |
| D-4 | 51–52 | `APP_ENV` selects; `ENGINE_ENV` fallback in `adapter/wsgi.py` and `adapter/env_guard.py`; the unread variables; `ENGINE_TAG` and `RELEASE_ID` are app configuration | `adapter/wsgi.py:14–15`, 36; `adapter/env_guard.py:35–46`; BR-4. `provider_loader.py`'s order is not described |
| D-5 | 121–127, 135 | `APP_ENV=dev` and the full closed-rails tuple; the bind statements stay | reader gate (BR-11); `AGENTS.md` closed rails |
| D-6 | 10, 24–29 | header set scoped to `adapter.wsgi`; `X-Engine-Tag` default `Isis6`; `X-Release-Id` default `rel_dev`, not the canonical `release_id` | `adapter/wsgi.py:27–39`; header probes (§12.4); BR-6 |
| D-7 | 139–147 | `Procfile` start line; no live-service claim | `Procfile`; PD-10 |
| D-8 | 112 | `tests/infra/test_sercanon_bytes.py` | as U-2 |
| D-9 | 16, 227–228 | six keys in their order, pinned by the test; `release_id` is canonical | `tests/transport/test_internal_version_contract.py:23–30`, 134; test-client body keys; body `release_id` = `77204764…` |
| K-1 | contract 19 | unknown paths: governed 404 from every factory | test client: `GET /api/reader/missing` → 404 `application/json; charset=utf-8`, `no-store`, no ETag, `ERR_NOT_FOUND`, all three factories |
| P-1 | crib 15–19 | the writer, its gate and `--check`; the current proof list | as R-4 |

### 6.7 Count

- **55 planned edits**, applied in this order: R-1, R-3, R-4a, R-6, R-7, R-5, R-2, R-4b, R-4c, A-5, A-4, A-3, A-2, A-1, A-6, A-6b, E-1..E-3, E-4, Q-1a–c, U-1, U-2, X-1, U-3, D-1, D-6a, D-9a, D-2, D-6b, D-6c, D-3, D-4, D-8, D-5a, D-5b, D-7, D-9b, K-1, P-1, L-1a–k, R-9a, R-9b, CH-1.
- **Against the instruction's 36 items:**
  - 33 changes are made. X-1 is one runnable command; L-1 is 11 mismatches; A-6 is five generators; E-3 has its membership rule stated.
  - The 2 no-change confirmations, R-8 and V-1, are confirmed.
  - The 1 routed exclusion, F-1, stays routed.
- **Added under §9.3** (stale statements inside the §6 documents and within an item's subject): D-9, E-4, U-3, R-9, and the widened D-3 and D-6.

## 7. Routed items and their coverage

| Routed item | Source | Covered by |
| :- | :- | :- |
| LR8-F2 (`docs/ADAPTER_009.md` statements) | addendum 2.21 | D-1 to D-9 |
| LR8-O1 / O-19 (documentation side) | addendum 2.21 | R-6 |
| H-4 writer usage note, read with addendum 2.17 | addendum 2.17 "Deferred obligations"; WU-PR-07 instruction H-4 | R-3, A-1 |
| G-1, LR6-O5, LR6-O7 | addendum 2.12 | R-2, A-4 (G-1's exit rule included) |
| LR7-O15 (CX7-11's stated limit) | WU-PR-07 lineage review | R-3 |
| Start command and bind; OBS-P3-12; OBS-P3-8 | addenda 2.8 and 2.10 | R-5, A-5, U-1, U-3, D-5, L-1k |
| LR3-O4 (README `release_id`) | addendum 2.8 | R-1 |
| WU-PR-04 plan §17 (README and `AGENTS.md` override, sink, band; runbook `APP_ENV`) | addendum 2.9 | R-9, X-1; `AGENTS.md` none (PD-7) |
| WU-PR-02 OBS-W2-1, OBS-W2-2 | WU-PR-02 plan v1.0 | E-2, R-7 |
| WU-PR-07 plan §18 documentation (`AGENTS.md`, README, `docs/qa_harness_pattern.md`) | WU-PR-07 result v1.0 §9 | A-1, R-3, Q-1 |
| F-3 (production route exposure, WU-PR-05) | addendum 2.10: "WU-DOC-01 receives F-3, O-19 …" | No §6 document needs a change. `docs/RUN.md` 71–73 (verified against `adapter/http_reader.py:904`), `AGENTS.md` 59, README 111 and `docs/server/reader_v1.md` 15–20 match the delivered behaviour. Two out-of-bound statements are routed (§16, RF-4 and RF-5) |
| OBS-P3-10 (`tests/retired_tests.md` line 54 calls `52be4558…` "current") | WU-PR-03 result v1.0 | Outside the §6 documents; routed (§16, RF-1) |

## 8. Files and requirement-to-change/test map

- **Files changed (10):**
  - `README.md`, `AGENTS.md`, `CHANGELOG.md`;
  - `docs/EVIDENCE_INDEX.md`, `docs/CLI_commands.md`, `docs/RUN.md`, `docs/ADAPTER_009.md`;
  - `docs/qa_harness_pattern.md`, `docs/contracts/reader_v2_public_bytes.md`, `docs/acceptance/reader_a7_crib.md`.
- **Files read but unchanged:** `docs/server/reader_v1.md` (V-1) and `docs/INDEX.md` (X-1).
- **Requirement map:** instruction §4 applies unchanged. Each requirement's documentation change is the §6 item it names, plus:
  - S14 and S08 → R-9;
  - S10 → U-3;
  - S21 → Q-1 and E-3.
- **Tests that read these documents** (instruction §5.2; each consumer's assertion confirmed):
  - `tests/unit/test_check_agents_md_citations.py::test_repository_agents_md_passes` runs the citation checker on `AGENTS.md`;
  - `ci/checks/check_direct_db_contract.py` scans tracked text for bridge guidance (`CHANGELOG.md` exempt);
  - `tests/cli/test_cli_usage_and_errors.py` names `docs/CLI_commands.md` only in a comment;
  - `tests/qa/test_generate_epic_close_pack.py` names `docs/ADAPTER_009.md` and the crib only in fixture literals;
  - the rails workflow test and the readiness test use README only as a path literal.

## 9. Implementation sequence for PR-30

1. **Recover first.** Inspect local roots, worktrees, branches and open PRs for WU-DOC-01, and `docs/ephemeral/HDE-CRD-0002-WU-DOC-01-*`. Resume the most advanced consistent state. Create nothing that already exists.
2. **Check the base.** `git fetch origin main`. Confirm that none of the ten files changed between `b7458aa` and `origin/main`: `git diff --stat b7458aa origin/main -- <the ten files>` must be empty.
   - If any changed, run `git apply --check` of the companion diff on `origin/main`.
   - If it does not apply, or a changed line touches an item's statement, stop and return to this PR-20 session through same-owner recovery. Do not hand-merge.
3. **Branch** from `origin/main` (the harness-designated branch for the PR-30 session).
4. **Apply** `git apply docs/ephemeral/HDE-CRD-0002-WU-DOC-01-pr-implementation-plan-v1.0-prototype.diff`, reading the companion from `main`. Then `git diff --name-status origin/main` must list exactly the ten files of §8, all `M`.
5. **Validate** as §11 items 1 to 5.
6. **Commit once**, `docs: bring repository documentation to HDE-CRD-0002's delivered state (WU-DOC-01)`, with the attribution lines the session requires.
7. **Write the PR-30 result record** under `docs/ephemeral/`. It holds:
   - the statement-to-proof list (§6, by reference);
   - the test counts, the `lanes` and `membership` output, and the applied-diff sha256.
8. **Push and open the PR.** The description uses the template headings under the `AGENTS.md` "PR descriptions" rules:
   - "What merging does" states what becomes current on `main`, and that merging does not establish QA, acceptance or closure.
9. **Return** `PR_CANDIDATE_PUBLISHED` with the PR-35 handoff.

## 10. PR split and merge dependencies

- **One PR.** No split: the edits are independent Markdown with no ordering constraint.
- **Merge dependency:** this plan's own PR (the record PR) should merge first, so PR-30 reads the companion diff from `main`. The merge is the Product Owner's manual act.
- **No other PR** is a prerequisite.
- **Downstream:** PR-40 (this unit's lineage review), then DOC-20, then WU-OPS-01's business case before OPS-10.

## 11. Validation PR-30 runs (PR-35 re-runs items 2 and 3 on the final head)

Run everything under closed rails (`env -i PATH=… HOME=… SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC`).

1. **Install:** CI's full install, `python -m pip install 'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e .`, into a venv bound to a throwaway copy or a dedicated environment. Then `python -m pytest --version`.
   - `*.egg-info/` is git-ignored (`.gitignore:34`), and the prototype clone stayed clean after `-e .`. A throwaway copy is still preferred.
2. **Citation check:** `python ci/checks/check_agents_md_citations.py` prints `AGENTS_MD_CITATIONS_OK`, and `tests/unit/test_check_agents_md_citations.py` passes (57).
3. **The six document-reading test files** (instruction §5.5) pass with zero failures. Prototype: **1,248 passed**.
4. **Pre-push reports**, on the committed head:
   - `python tools/ci/prepush_check.py --base origin/main --head HEAD lanes build-notes` → `reason=documentation_only;paths=10;lanes=none`, PF10 path and sha256 recorded;
   - `python tools/ci/prepush_check.py --head HEAD --path <each of the ten files> membership` → ten `not-member`, `release_id` unchanged.
5. **Changed paths:** `git diff --name-status origin/main...HEAD` lists the ten files only.
6. **Hosted CI (PR-35):**
   - the `test` job succeeds on the final head and prints `CI_APPLICABILITY_AND_EXACT_HEAD_OK`;
   - `CI_CHANGE_CLASSIFICATION` shows `reason=documentation_only`;
   - setup, install and pytest are skipped (`needs_python=false`). So items 2 and 3 are local-only evidence.

Codex code review excludes Markdown (`AGENTS.md` "Code review guidelines"), so no Codex finding is expected. A human or other review comment is dispositioned under addendum 2.11 rule 7 and addendum 2.14.

## 12. Prototype record

### 12.1 Construction

- **Clone:** a throwaway clone of `b7458aa`, branch `proto`.
- **Edits:** applied by a scratch script of 55 exact old→new replacements, each required to match exactly once. The script is not committed; the diff is the deliverable.
- **Commit:** one commit, prototype head `3d7b69ec804fc5d3f349169db9e9133f08a94714`.
- **Diff:** `git diff b7458aa 3d7b69ec` = the companion. 10 files, +137/−57; sha256 `a334c348bf37187dab26a9051e9ee2f7a56692723fc1dd5f6838c8600e60ab63`; `git apply --check` clean on `b7458aa`.
- **Line lengths:** README and `AGENTS.md` lines are long, so whole-line hunks make the diff 85,565 bytes. `git diff --word-diff` shows the changed words.

### 12.2 Results on the prototype head

| Check | Result |
| :- | :- |
| `check_agents_md_citations.py` | `AGENTS_MD_CITATIONS_OK` (exit 0) |
| `tests/unit/test_check_agents_md_citations.py` | 57 passed |
| §5.5 six files with the full install (`-e` of the prototype) | **1,248 passed** in 83.97 s; exit 0 |
| `prepush_check.py --base b7458aa --head HEAD lanes build-notes` | `reason=documentation_only;paths=10;lanes=none`; build-notes `PF10-HDE-Build-Notes-v13.7.4.md` sha256 `8ac97232…6d37ff`; PASS; repository unchanged |
| `prepush_check.py --head HEAD --path <ten files> membership` | ten `not-member`; `1.3.0`, 45, `release_id` `77204764…`; PASS |
| `git diff --name-status b7458aa HEAD` | the ten files, all `M` |
| Clone clean after the runs | yes |

### 12.3 Baseline runs at `b7458aa`, recorded for PR-40 and DOC-20

- **The six files with the full install:** 1,248 passed in 75.88 s.
- **The A7 writer:** `generate_a7_transport_proofs.py --check` → `a7 transport proofs check ok`.
- **The EPIC037 generators' `--check`:**

| Generator | Exit | Result |
| :- | -: | :- |
| `field_sufficiency` | 1 | `STALE_HDE_EPIC037_FIELD_SUFFICIENCY:…` |
| `v2_adapter` | 1 | `STALE_HDE_EPIC037_PR02_ADAPTER:…` |
| `bg_resolve` | 1 | `KeyError: 'adapter'` |
| `v2_to_compat` | 1 | `STALE_HDE_EPIC037_PR04_V2_TO_COMPAT:…` |
| `parent_binding` | 0 | `checked HDE-EPIC037 PR-05 parent-binding artifacts` |

- **The other entrypoints on that `AGENTS.md` line** all exit 0: `update_evidence_index.py --check`, `run_canonical_json_gate.py --check-only`, `orientation_demo.py --check`, `validate_evidence_paths.py`, `check_evidence_index_hash.sh`, `check_mirror_schema.sh` (run directly; it is a Python script) and `check_final_lf.sh`.
- **The pre-push sweep:** 215 tracked test files, `uncovered=0`.

### 12.4 Test-client probes at `b7458aa` (closed rails; Flask test client; no server, no network)

- **`/internal/version`** on `adapter.factory`, `adapter.http_reader` and `adapter.wsgi`, under `APP_ENV` `dev` and `prod`:
  - 200, `no-store`, no ETag;
  - with `Authorization: Bearer x`, 200;
  - with `X-Identity-Override`, 400;
  - body keys `engine_tag, build_commit, invocation_tag, invocation_sha256, emitter_sha256, release_id`;
  - `release_id` = `77204764…`.
- **Headers:** `adapter.factory` returns only `Cache-Control`, `Content-Length` and `Content-Type`. `adapter.wsgi` returns its full set, with `X-Engine-Tag: Isis6` and `X-Release-Id: rel_dev`.
- **`/internal/healthz`:** 200 on `adapter.wsgi` only; 404 on the other two.
- **`GET /api/reader/missing`:** 404 `application/json; charset=utf-8`, `no-store`, no ETag, `{"code":"ERR_NOT_FOUND",…}`, on all three factories.
- **Dev `GET /reader`:** `APP_ENV=dev` → 200; `test`, `local` and `prod` → 403 `ERR_READER_FORBIDDEN`.

## 13. Interface contracts (instruction §8)

| Contract | Met by |
| :- | :- |
| G-1 | R-2 states LR6-O5, every LR6-O7 limit, the exit rule and the nonclaim. Nothing in it goes beyond the tool's help, its exit constants, `SWEEP_TOOLS`, or addendum 2.12's rows |
| H-4 | R-3 and A-1: the v2 schema, both identities, the outputs, the nonclaims, the ADR read with addendum 2.17 (resolutions A and B) |
| IF-4, IF-5, IF-7 | E-1 to E-3 and Q-1 describe the updater at `b7458aa` |
| DOC-20 | §6 is the measure's statement list |
| WU-OPS-01 | no document states an Ops fact (PD-10) |

## 14. Security and migration

- **No secret:** no secret, token, key value or base URL in any edit. Environment variables appear by name only.
- **`/internal/version`:** D-1 to D-4 describe the measured behaviour and propose no authorization design. Its having no authorization check is recorded as RF-6 (§16) for the Product Owner; it is neither fixed nor decided here.
- **Runs:** closed rails for every run; no live vendor, production or database access occurred.
- **Migration:** none. No code, test, schema, workflow, governed artifact or release member changes. Rollback is a revert of the PR.

## 15. Risks and recovery

| ID | Risk | Treatment |
| :- | :- | :- |
| RK-1 | `main` moves a planned file before PR-30 | §9 step 2: `git apply --check`. A conflict returns to this PR-20 session; no hand merge |
| RK-2 | A reviewer reads the A-3 correction as changing the 2026-09-21 rule | PD-5: the rule's sentences are byte-identical, which the diff shows |
| RK-3 | A future edit to `AGENTS.md` trips the citation checker | the prototype passes it; PR-30 and PR-35 re-run it |
| RK-4 | A statement drifts after merge | DOC-20 re-checks §6 on merged `main` |
| RK-5 | The four EPIC037 generators are fixed later | the A-6 sentence then goes stale. Recorded for their owner (RF-3) |

- **Recovery:** resume from the last saved artifact; the prototype lives only in throwaway clones.
- **An instruction defect** returns to the IA through DOC-10.
- **Abort** is only Nathan's manual PR-50.

## 16. Findings outside this unit's bound (recorded and routed, not changed here)

| ID | Finding | Proposed owner |
| :- | :- | :- |
| RF-1 | `tests/retired_tests.md` line 54 calls `52be4558…` the current `release_id` (OBS-P3-10). It is a test-directory ledger, outside the §6 documents | the IA, for the ledger's next owner, or the Product Owner |
| RF-2 | Instruction §10 item 4's command fails `membership` without `--path` (BR-2) | the IA (DOC-10 lesson); applied here as two commands |
| RF-3 | Four EPIC037 generators fail `--check` on `main` (BR-3). That is evidence-generator drift, not documentation | the Product Owner, as a later-change candidate |
| RF-4 | `ARCHITECTURE.md` lines 29–30: the production app mounts the dev blueprint. True, but it omits that production now refuses those routes (S19-F03) | the Product Owner, with X-02 |
| RF-5 | `FLASK_AUTO_RUN_GUIDE.md:189` says the sampler exists "if `DEV_SAMPLER_URL` is set" | the Product Owner, with X-02 |
| RF-6 | `/internal/version` has no authorization check on any app factory; earlier documentation claimed a production Bearer requirement | the Product Owner, if it is a security concern (instruction §11) |
| RF-7 | `docs/hde_epic019_remediation.md:13` still says the runner binds `0.0.0.0` | the Product Owner, as a later documentation candidate |
| RF-8 | `artifacts/cli/help/hdctl_help.txt` (governed, frozen) holds the pre-S07 summary | its evidence owner; no hand edit |
| RF-9 | `scripts/qa/d6_live_vendor_qa.py` is tracked as mode 100644, unlike its siblings | the Product Owner, as a later candidate |
| RF-10 | The `STDOUT_*` guards exit 64, while HDE CLI/API/Vendor Ref §4.1.4 says 1 (stated in L-1h) | the Product Owner (code or canon doc-delta) |

## 17. Carried items (instruction §15), unchanged

| Item | Owner |
| :- | :- |
| DOC10-F1 | this unit (A-3) |
| DOC10-F2 | this unit (A-4) |
| DOC10-O1 (the prepush `lanes` note) | Product Owner, later change candidate. Not repeated in R-2 |
| O-19 code (`scripts/make_release_pack.sh`, `scripts/hd_cli.py`) | Product Owner; the documentation side is R-6 |
| OBS-8 orphaned fixtures (F-1) | Product Owner, later cleanup |
| OBS-P3-13 | the IA, as QA tool owner |
| PR35-C1 and LR8-F1 | Product Owner (addendum 2.21) |
| The canon doc-deltas of instruction §7 | Product Owner |
| The S21 ADR revision (addendum 2.17) | the Product Owner's instruction |
| WU-OPS-01's business case | Product Owner, before OPS-10 |

## 18. Canon-conflict register

`CANON_CONFLICT_REGISTER` is carried unchanged: CR-1 to CR-8, all decided.
- CR-1 to CR-3 are APPROVED_AS_CHANGED by Thoth.
- CR-4 is APPROVED and CR-5 APPROVED_AS_CHANGED, both by the Product Owner.
- CR-6 is APPROVED (a) by the IA through RS-20.
- CR-7 and CR-8 are APPROVED (a) each, by the Product Owner.

**No new conflict.** The corrected statements are repository documents following the delivered code. RF-10 (exit code 64 against canon's 1) is an existing code-versus-canon gap that the document now states accurately, as the document did before for a different gap. It is a doc-delta or code candidate, not a register entry this plan decides.

## 19. PR-30 and PR-35 obligations

- **PR-30** (this dedicated session, after Nathan's Proceed for exactly v1.0):
  - recover first;
  - apply only the companion diff;
  - run §11 items 1 to 5;
  - commit once;
  - write the result record;
  - publish the initial PR and return `PR_CANDIDATE_PUBLISHED` with a PR-35 handoff.
  
  PR-30 does not own review correction, current-head CI readiness or merge.
- **PR-35** (its own dedicated session):
  - retrieves every review thread and dispositions any finding (addendum 2.11 rule 7; addendum 2.14);
  - corrects in-scope defects with a coherent push;
  - re-runs §11 items 2 and 3 on the final head;
  - verifies item 6, the remote-head identity and mergeability;
  - returns `MERGE_PENDING` without merging.
  
  No `[skip ci]` without Nathan's direct instruction.
- **Merge:** Nathan merges manually.
- **After the merge:** PR-40 (the whole-change IA) reviews the landed lineage; then DOC-20.
- **Nonclaims:** every record keeps the nonclaims: no QA, acceptance, Ops, deployment, PF09 or PF30 movement, drainage or closure.

## 20. TypeSafe reading for the receiving session (PR-30, WU-DOC-01, plan v1.0)

Action sent (v8.2): "Implement, in a new dedicated session after a Product Owner Proceed, one already reviewed-once documentation work unit of an approved change: apply a planned, fully drafted set of about seventy statement corrections and additions across ten repository Markdown documents (README, CHANGELOG, the agent-instructions file's operative passages, an evidence-index guide, a CLI reference, a runbook, an operator document, a harness guide, a contract page and an acceptance crib), where the plan gives the exact replacement text and a prototype diff that already applies cleanly and passes; recover any existing work first, check the base has not moved, run the local tests that read these documents with the full CI install plus the pre-push lane and membership reports, commit once and publish the pull request. No code changes and no live provider run occur; a separate review-correction session, CI, a lineage review and a completion verification follow."

Note on the count: "about seventy statements" counts changed sentences and bullets. The 55 edits carry about that many, because CH-1 has 20 bullets and R-2 about 14.

- **TypeSafe v8.2: Opus 5.5 at medium.**
  - Effort score 1.46 (confidence 0.69). Rung probabilities: low 0.01, medium 0.56, high 0.38, extra high 0.04, max 0.00, ultracode 0.00.
  - Model probabilities: Fable 5.1 0.00, Opus 5.5 0.87, Sonnet 5.5 0.13, Haiku 5.5 0.00 (confidence 0.83).
  - Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.000, Fable 5.1 at high 0.000, Fable 5.1 at extra high 0.000, Fable 5.1 at max 0.000, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.009, Opus 5.5 at medium 0.487, Opus 5.5 at high 0.331, Opus 5.5 at extra high 0.035, Opus 5.5 at max 0.000, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.001, Sonnet 5.5 at medium 0.073, Sonnet 5.5 at high 0.049, Sonnet 5.5 at extra high 0.005, Sonnet 5.5 at max 0.000, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000.
  - Flags: boundary between high and medium.
  - Sent 2026-10-22T01:52:59Z. Nathan picks the cell.
- **Detail:** v8.2 sent 2026-10-22T01:52:59Z; HTTP 200 in 0.48 s; 5524 input and 71 output tokens; jev-1.13.0. Rung by rule: medium (nearest to the score, halves up). Model by rule: Opus 5.5 (the most probable of the four options, a tie going to the higher-priced model). Flags: boundary between high and medium.
- **Which request:** the installed TypeSafe scoring skill's request v8.2 and `score_v8.py`, run once with session kind `implementation`, before this record was saved.
- **Records:**
  - The Notion row was not written: this is a development-flow session, read-only toward Notion, as the earlier HDE-CRD-0002 records are.
  - Nathan's pick for PR-30 is not stated. Nathan's pick for this PR-20 session is not stated; the instruction §19 holds its reading.

**Surface advice:** run PR-30 in this same dedicated top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, entered by Nathan's Proceed.
- **Environment:**
  - Python 3.12 with CI's full install, in a venv bound to a throwaway copy or a dedicated environment;
  - git, bash, `curl` and `ruby` on `PATH` for the pre-push check;
  - closed rails.
- **Run times observed:**
  - the six test files: about 85 s;
  - each pre-push report: about 3 s.
- **Access:** no live vendor, production or database access.
- **Order:** this plan's pull request should be merged first, so the companion diff is on `main`.

## 21. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / WU-DOC-01 / PR-20 / plan 1 |
| change / specification | CRD HDE-CRD-0002 / `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` v1.1, with Specification delta 01 |
| unit | WU-DOC-01 |
| release | GCFPE-20261009.1 / 100926.1 |
| prompt | PR-20 — Create Detailed PR Implementation Plan — 100926.1, https://app.notion.com/p/3f44590a05eb819fbea5dcd966a750ba (page state as of 2026-10-12T02:29:47.327Z) |
| role/stage | dedicated WU-DOC-01 PR engineering session / PR-20 |
| capture time | 2026-10-22T01:58:00Z |
| execution identity | https://claude.ai/code/session_011Y6ExL6PGDrodZqKLRWCHK |
| inherited usage | the instruction §20 (DOC-10); the disposition record (business case) |
| repository persistence | recorded here only. `docs/changes/GCFPE_PROMPT_PROVENANCE.md` is absent on `main`; persistence is pending and non-gating |

## Canon relied on

Read on `main` at `b7458aa`. PF10 is v13.7.4 (path and hash in the front matter).

| Topic | Sources and sections |
| :- | :- |
| PR-20 operation | PR-20 — Create Detailed PR Implementation Plan — 100926.1, read in full: "Execute" 1 to 10; "Required result"; "Next step and recovery"; "Save and hand off"; "Mandatory single-block handoff" |
| Unit scope and routing | PF10 addenda 2.19 (P-8; "WU-DOC-01: drops the dedicated-environment install note"), 2.21 (the stale-document list; LR8-F2; LR8-O1) and 2.20, read in full or at their WU-DOC-01 passages; instruction §6 and §9 |
| Writer usage note | PF10 addendum 2.17 in full (resolutions A and B; "Deferred obligations"); addendum 2.15 in full (the close-run family); the S21 ADR "Decision", "Stated limits", "Nonclaims" |
| Pre-push note | PF10 addendum 2.12, rows LR6-O5 and LR6-O7; WU-PR-06 instruction v1.0 contract G-1 |
| Business case; no ceiling | disposition record §2; PF10 addendum 2.18 |
| Findings and dispositions | PF10 addendum 2.11 rule 7; addendum 2.14 |
| Reviewer chain | PF10 addendum 2.3; `AGENTS.md` "Code review guidelines" |
| CLI exit codes | PF05-Canon-HDE-CLI-API-Vendor-Ref §4.1.4 "Errors and exit codes (normative)", read in full |
| Source fidelity and citation form | PF03-Reference-Technical-Writing-Best-Practices "Truth and source fidelity" and "Canonical ownership", read in full |
| Doc-Delta discipline | PF04-Canon-HDE-Governance "Doc-Delta discipline": normative edits need a Doc-Delta; stylistic or non-functional rewording does not. This unit corrects repository documents to delivered code and makes no normative canon edit |
| QA entry ordering | PF19-Canon-Glow-QA-Guide §3.1 "Intent": the final repository-documentation PR precedes whole-change QA entry and is distinct from PF drainage |
| Repository rules | `AGENTS.md`: canon-first rule; "Code review guidelines"; "Operating workflow" (pytest readiness; redaction; docs-only PR posture; PR descriptions); "HDE-EPIC039 current workflow posture"; "HDE-EPIC040 current posture"; "Release identity" |
