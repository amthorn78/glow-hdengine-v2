---
artifact_type: PR_WORK_UNIT_LINEAGE_REVIEW
artifact_id: HDE-CRD-0002-WU-PR-04-PR-WORK-UNIT-LINEAGE-REVIEW
artifact_version: "1.0"
decision: ACCEPT
predecessor: none (the first PR-40 review of WU-PR-04)
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-04
work_unit_title: "Provider gate and Aux preview (PR; Fermentation; S08, S14)"
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-04-pr-instruction-v1.0.md (v1.0, INSTRUCTION_READY; blob 51371eeae9d9; landed by #649 as 9c82b62)
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-04-pr-implementation-plan-v1.0.md (v1.0; Proceeded; spent; blob 6baead456619; landed by #650 as 6b5b3f3) with companion docs/ephemeral/HDE-CRD-0002-WU-PR-04-pr-implementation-plan-v1.0-prototype.diff (blob e09172397364)
PR_30_RESULT_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-04-pr-implementation-result-v1.0.md (PR_CANDIDATE_PUBLISHED; blob 80a40a279291)
PR_35_RESULT_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-04-pr-implementation-result-v1.2.md (MERGE_PENDING; historical pre-merge evidence; blob 905e752f8b11), with its checkpoint docs/ephemeral/HDE-CRD-0002-WU-PR-04-pr-implementation-result-v1.1.md (blob c5c4a4b65c04)
PR_REFS: amthorn78/glow-hdengine-v2#651 (the only pull request of this work unit; merged as 5892538)
entry_event: MERGE_OBSERVED for #651 (merged 2026-10-18T14:12:25Z as 5892538), delivered by the PR-35 session in the pasted handoff; no saved MERGE_OBSERVED artifact exists (NOT PRODUCED); the merge was verified independently (§3). The conditional PR-40 block issued with MERGE_PENDING is void
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
reviewer: the continuing whole-change HDE-CRD-0002 Implementation Agent, read-only PR-40 role; session https://claude.ai/code/session_01CCKsYD2yX5WgU3biWKb59j (author of the WU-PR-04 instruction; not an author of the plan, code or results reviewed here)
pr_sessions: PR-20 and PR-30 https://claude.ai/code/session_01JNmEgwAw93afByBxnV6JS8; PR-35 https://claude.ai/code/session_01L3975UmX1MJFVcHhQqKv5F
approved_lineage: Specification docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (v1.1); Implementation Audit docs/ephemeral/HDE-CRD-0002-implementation-audit-v1.0.md (v1.0); Implementation Plan docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (v1.1); Plan review docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (v1.1, IA-30 INITIAL_APPROVE)
overlays: PF10 addenda 2.3 (review chain), 2.5 (LR-O1 to LR-O3), 2.6 (22-path roster; step 3b), 2.7 AD-5 (refresh base and restart rules), 2.8 (WU-PR-03 acceptance and its carried items); none created for this unit
return_owner: the same continuing whole-change HDE-CRD-0002 Implementation Agent
prompt: PR-40 — Review PR Work-Unit Lineage — 100926.1 (https://app.notion.com/p/3f44590a05eb81088487e918fd642a7f; page state as of 2026-10-12T02:29:38.234Z; read in full in this invocation)
prompt_release: GCFPE-20261009.1 / 100926.1
created_at: 2026-10-18T14:43:28Z
repository_state_reviewed: origin/main 5892538 (tree ccb58403a4a2); no commit after it at review time
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.9.md (v13.5.9; blob a125fd4eefbf; 135,146 bytes; sha256 361274ddcb0e04e1d8986e2bfff4529912b5bba06a9c57820b8bc12a1adbff1e; docs/pfcanon/ unchanged since b9edb0c). Read in full by this IA session at PR-10 for this unit: the v13.5.8→v13.5.9 diff, addenda 2.6, 2.7 and 2.8, and 2.3; 2.5's retained decisions. The file is byte-unchanged since (same blob), so this review relies on that reading
pf10_addendum_created: none (PR-40 is not a qualifying approval prompt)
canon_conflict_register: CR-1 to CR-8 carried; no new entry (§9)
next_prompt: PR-10 — Create PR Work-Unit Instructions — 100926.1 (https://app.notion.com/p/3f44590a05eb815d97d5f3930c7d3e8a), for WU-PR-05
---

# HDE-CRD-0002 WU-PR-04 — PR work-unit lineage review v1.0 (PR-40, #651)

## 1. Decision

**ACCEPT.** WU-PR-04 is delivered with sufficient attributable evidence by its one pull request, #651.
- **S14.** `hdctl bg:resolve --source vendor --allow-prod-vendor <AUTHORIZATION_REF>` implements HDE-CLI-API-Vendor-Ref §7.1.11a to §7.1.11f:
  - the CLI pre-scan and usage carrier;
  - environment classification;
  - the eight-row matrix and the seven-step pre-I/O order;
  - the actor rule and the 16-key audit record, durable (file and directory entries) before vendor I/O;
  - the read-only production override.
- **S08.** `aux-preview --pair-file … --band B` uses band B.
- **Instruction decisions.** ID-1 to ID-10 hold as bound. The plan's PD-1 to PD-19 and PR-30's D-1 to D-3 stay inside them.
- **Review.** The one Codex finding (CX-1, P1, audit directory durability) was corrected before the merge and re-reviewed clean.
- **CI and checks.** Hosted CI passed on the final head across all seven lanes. This review's own runs on merged `main` confirm the landed state (§5).

ACCEPT is this review's lineage result only. It is not QA, acceptance of HDE-CRD-0002, Ops, deployment, release activation, PF09 or PF30 movement, or closure. The `--allow-prod-vendor` live call belongs to the QA Plan.

## 2. Inputs read

- **In full, in this invocation:**
  - the PR-40 prompt;
  - plan v1.0 (all 22 sections, its "Canon relied on" and "Checks run");
  - results v1.0, v1.1 and v1.2.
- **Authored by this IA and re-read for the decisions that depend on it:** instruction v1.0 (§4 ID-1 to ID-10, §6, §7, §10, §15).
- **Companion diff.** Applied to `6b5b3f3` in a scratch worktree and compared file by file with the landed source commit (§3).
- **Approved lineage, re-read where a decision depends on it:**
  - Specification v1.1: rows S08 and S14; constraints "Release members", "Vendor override", "Override initiator", "Live QA"; Exclusions;
  - Implementation Plan v1.1: §7 WU-PR-04 and WU-PR-05 blocks, §10;
  - Plan review v1.1 (N4 carry);
  - Audit §6 S08 and S14, §7.1 EC-7.
- **GitHub, read directly:**
  - #651 metadata, its six commits and its single check run;
  - the final head's job log, read whole by a programmatic scan (906 lines, 72,968 bytes, SHA-256 `1e239a00…`; it begins with the runner start and ends with "Cleaning up orphan processes"; not truncated);
  - the one review thread, both formal reviews and the three issue comments.
- **Code on `main`, read in full:**
  - `engine/bodygraph/vendor_audit.py`;
  - the landed diffs of `engine/bodygraph/resolver.py`, `engine/cli/main.py`, `ci/checks/classify_ci_changes.py` and `tools/evidence/generate_v2_mapped_cache_evidence.py`;
  - the removed and replaced lines of the four extended test files.

## 3. Merge state and landed lineage

| Item | Fact |
| :- | :- |
| Pull request | #651, merged=true, merged by amthorn78 at 2026-10-18T14:12:25Z; base `main` `6b5b3f30c008`; head `claude/dreamy-hawking-yz6hnr` `484ce6e160a7`; 6 commits; 68 files (+2,175/−124) |
| Commits, in order | `a00cb8b` source, 11 hand-edited paths (PR-30); `2336a0c` owner-produced re-cut and convergence, 54 paths (PR-30); `c6df96f` result v1.0; `90ec0ca` CX-1 correction, 2 paths (PR-35); `685b67e` result v1.1; `484ce6e` result v1.2. Each has one parent, the previous commit; `a00cb8b`'s parent is `6b5b3f3` |
| Squash | `5892538`, one parent `6b5b3f3` (the pull request's base). `5892538^{tree}` equals `484ce6e^{tree}` equals `ccb58403a4a2`. `git diff 6b5b3f3 484ce6e` and `git diff 6b5b3f3 5892538` have the same SHA-256 (`a22a2a28…`) |
| Changed set | 68 paths: 5 added (`engine/bodygraph/vendor_audit.py`, `tests/bodygraph/test_vendor_prod_override.py`, results v1.0 to v1.2), 63 modified. Outside `docs/ephemeral/`: the 11 paths of plan §7.1 and the 54 owner-produced paths of plan §6.13, exactly: the manifest, the file holding `FROZEN_OPEN_ABBA_SHA256`, 26 evidence primaries (the Index and Mirror files included) and their 26 path proofs |
| Source versus the plan's companion diff | the same 11 files; equal except three, each matching a recorded in-flight decision: `engine/cli/main.py` (D-1, the `--` separator rule), `tests/cli/test_bg_resolve.py` (D-1's two cases), `tests/cli/test_aux_preview.py` (D-2, module-level import) |
| `FROZEN_OPEN_ABBA_SHA256` | one line, `06611525…` → `9949ddf5…` |
| Plan §7.3 expected-unchanged paths | empty diff over all of them, `adapter/**`, `engine/http/**`, `engine/compat/**`, `docs/pfcanon/**`, `schemas/**`, `audit/qa/**` and the frozen families included |
| Interstage commits since the WU-PR-03 review (`39afdc6`) | `b9edb0c` (PF10 v13.5.8 → v13.5.9, Product Owner commit), `9c82b62` (#649, this unit's instruction), `6b5b3f3` (#650, its plan and companion diff): `docs/pfcanon/` and `docs/ephemeral/` only, none attributable to the code delivery |
| Later divergence | none: `origin/main` is `5892538` at review time |

**Attribution.** The landed delta is exactly #651's direct delta: single-parent squash on the pull request's base, equal trees, equal diff digests. The glow-merged-change-attribution-lock collector was not run (NOT EXECUTED); native attribution meets its EXACT condition for a squash. No item is unproven.

## 4. Reviews, checks and corrected-change coverage

| Item | Fact |
| :- | :- |
| Codex code review, `2336a0c` ("PR opened") | failed on the usage limit (comment 6250183766). Product Owner decision PO-1: request a review (result v1.1 §6) |
| Codex code review, `c6df96f` ("Manual request") | review 5563130407: one P1 finding, CX-1, thread `PRRT_kwDOP103ks6tqvyR` (`engine/bodygraph/vendor_audit.py`). "Persist the audit directory entry before vendor I/O": `fsync` on the file does not persist the entries created by `mkdir` and `O_CREAT`, against §7.1.11f "locally durable … before I/O" |
| CX-1 disposition | corrected by `90ec0ca` (directory fsyncs after the file; any failure is `PROVIDER_AUDIT_UNAVAILABLE` before step 7; three new tests); answered before the push (r4307219438); thread resolved. The module is not a release member and binds no evidence, so no re-cut |
| Codex code review, `685b67e` and `484ce6e` ("New commits") | completed with no findings; summary comment 6250183424 records the last as "Completed 2026-10-18T13:54:41Z — `484ce6e`", `has_any_findings: false`. No thread is open |
| Codex security review | not part of the chain (PF10 addendum 2.3); not a gap |
| Human reviews | none requested or present; the second formal review (5563196869) is the container of PR-35's thread reply |
| Hosted CI, final head `484ce6e` | run 39133403313, job 117692978297, check `test`: success, 13:51:40Z to 14:07:48Z. Checkout `HEAD is now at 484ce6e1`; `CI_CHANGE_CLASSIFICATION:event=pull_request;reason=selected_lanes;paths=68;lanes=product,compat,db,rails,evidence,qa,release`; changed-test step 3,682 passed; product 77; compat 103 passed, 3 skipped, 2 xfailed; db 249; rails 24, 113 and 59, then the pin file 138; evidence 130; qa 488; release 79, then the attestation built and verified; every lane flag `true` with outcome `success`; `CI_APPLICABILITY_AND_EXACT_HEAD_OK` printed; no `##[error]` line. Runner ubuntu-24.04 image 20261012.334.1, Python 3.12.15 |
| Earlier hosted runs | 39129417131 (`2336a0c`) cancelled by concurrency; 39129482681 (`c6df96f`) success, stale after CX-1; 39132120009 (`685b67e`) success with the same counts (result v1.2 §2). None is a gate |
| Corrected-change coverage | the reviewed and CI-tested head `484ce6e` is the merged tree. `685b67e` and `484ce6e` add records under `docs/ephemeral/` only. The code tree PR-35 validated locally (`90ec0ca`, result v1.1 §5) equals the merged code tree |
| Waivers | none exists or was used for HDE-CRD-0002 |
| OBS-17 and O-6 | OBS-17 did not occur: the close-pack test passed in the changed-test step and the qa lane. O-6: `ruby` is present on the hosted runner, because the contract-inventory test passed; its version is still unprinted |

## 5. This review's independent checks on the merged `main` (`5892538`)

Environment: two detached worktrees of `5892538` in a scratch clone. CPython 3.12.3 with CI's install, pytest 8.4.2, `ruby` at `/usr/local/bin/ruby`, `bash` and `curl`. Closed rails: `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`. Unset: `DATABASE_URL`, `GEO_API_KEY`, `HD_API_KEY`, `HDAPI_BASE_URL`, `HD_API_BASE_URL`, `HDAPI_KEY`, `HD_GEOCODE_KEY`, `GH_TOKEN`, `GITHUB_TOKEN`, `HDE_VENDOR_OVERRIDE_AUDIT_PATH` and (outside the sweep) `ENGINE_ENV`. `XDG_STATE_HOME` pointed at an empty scratch directory, so a stray default-sink write would be visible. Every worktree ended with an empty `git status --short --untracked-files=all`.

1. **Admission:** `2f18a5ebbf1908ae1425ec546677d6618746f27c2e1ddc9e5087a81b0aaceb76 45 1.3.0`; manifest SHA-256 equal.
2. **Read-only evidence and release checks**, 13 × exit 0:
   - `release_id_recompute.py --check-manifest-only`;
   - `update_evidence_index.py --check`;
   - `orientation_demo.py --check`;
   - `validate_evidence_paths.py`;
   - `ci/checks/check_mirror_schema.sh`, `ci/checks/check_evidence_index_hash.sh` (by path);
   - `check_lf_endings.py`;
   - `ci/checks/check_final_lf.sh`;
   - `refresh_step_logs_manifest.py --check`;
   - `run_canonical_json_gate.py --check-only`;
   - `generate_a7_transport_proofs.py --check`;
   - `generate_v2_mapped_cache_evidence.py --check` (`V2_MAPPED_CACHE_EVIDENCE_OK`);
   - `generate_bodygraph_policy_proofs.py --check`.
3. **Frozen families and CLI help,** 5 × exit 0: `generate_showcompat_artifacts.py --check`, `generate_cli_conformance_artifacts.py --check`, `generate_rails_gate_evidence.py --check`, `generate_env_matrix_snapshot.py --check`, `ci/checks/check_cli_help.sh`.
4. **Stale-binding sweep and labels.**
   - `git grep -l -E 'd84d99e1|06611525'` outside `docs/`, `.audit_src/`, `handoff/` and `manifest_*.sha256`: no hit. In `docs/` outside `docs/ephemeral/` and `docs/pfcanon/`: no hit.
   - Mirror: 620 rows; 27 labelled rows, all carrying `2f18a5eb…` and none `d84d99e1…`; the purity-report rows carry no `notes`.
   - No audit sink file is tracked.
5. **Pre-existing EPIC036 and EPIC037 checks** (plan F-5). `generate_hde_epic037_bg_resolve.py --check` and `generate_hde_epic036_bg_resolve_route_policy.py --check` exit 1 on `5892538` and on `39afdc6` with the same stale-file lists. They were not caused by this unit, and neither was run in write mode.
6. **Targeted tests:**
   - the unit's six test files (`test_vendor_prod_override.py`, `test_resolver_vendor.py`, `test_bg_resolve.py`, `test_aux_preview.py`, `test_bg_resolve_v2_mapped_cache.py`, `tests/evidence/test_v2_mapped_cache_evidence.py`): 215 passed, which is result v1.0's 212 plus CX-1's 3;
   - the same with `APP_ENV` unset: 215 passed;
   - with `tests/adapter/test_jsonschema.py` first in the same process: 218 passed, 2 xfailed (plan F-13 holds);
   - route-policy, compat-chart, serializer-guard, CLI usage, showcompat-sources and classifier-pin files: 215 passed;
   - `tests/bodygraph/test_bg_resolve_route_policy.py` with `APP_ENV` unset: 6 failed, 6 passed. These are the six plan F-4 names (OBS-P4-2), which pass wherever `APP_ENV` is set, as in every CI lane.
7. **Negative controls** on the merged source, each with one guard disabled in a scratch worktree, then restored:

   | ID | Guard disabled | Result |
   | :- | :- | :- |
   | NC-A | CX-1's directory fsyncs | 3 failed, 96 passed |
   | NC-B | the step-5 flag-required refusal | 17 failed, 119 passed |
   | NC-C | ID-3's legacy production write refusal | 6 failed, 117 passed |
   | NC-D | the S08 band override | 3 failed, 6 passed |
   | NC-E | the process no-downgrade rule (PD-5) | 2 failed, 125 passed |
   | NC-F | an actor taken from `USER` before the user database | 1 failed, 98 passed |

   Every one fails as intended.
8. **Black-box CLI probes.**
   - **Setup:** `python -m engine.cli bg:resolve` with `HD_API_BASE_URL=https://127.0.0.1:9/v2` and fake key values, so any connection could only reach the local discard port; a scratch sink.
   - **Results:**

     | Probe | Exit | Outcome | Events |
     | :- | :- | :- | :- |
     | closed rails, `APP_ENV=prod` | 1 | the `PROVIDER_REFUSED` envelope, with no `details` (byte equality with the earlier envelope is asserted by the M-1 and M-2 tests, not by this probe) | none |
     | open rails, `APP_ENV=prod`, no flag | 1 | `PROVIDER_PROD_OVERRIDE_REQUIRED`, `error.details.outbound_attempted: false`, stderr empty | one `refused` line with the 16 keys, `authorization_ref` null, `actor_principal` `root` |
     | open rails, `APP_ENV=dev` with the flag | 1 | `PROVIDER_PROD_OVERRIDE_INVALID` | none |
     | `APP_ENV` blank | 1 | `PROVIDER_CONFIG_INVALID` | none |
     | `APP_ENV=dev` with `ENGINE_ENV=prod` | 1 | `PROVIDER_CONFIG_INVALID` | none |
     | valid flag, sink inside the checkout | 1 | `PROVIDER_AUDIT_UNAVAILABLE` | no file created |
     | duplicate flag (both spellings) | 64 | one stderr line, stdout empty, the value not echoed | — |
     | malformed value | 64 | as above | — |
     | `--source db` | 64 | as above | — |
     | the option after `--` | 64 | as above | — |
     | the option on `showcompat` | 64 | as above | — |

   - **Leak search:** the reference appears on no stdout or stderr. No sink line contains the user, the location, the URL or a key value.
   - **An unintended run, recorded as it happened.** One probe meant to put the sink inside the checkout was misconfigured: the scratch sink variable overrode it. That invocation took the allowed path (`APP_ENV=prod`, a valid flag, an auditable sink) and reached step 7. It attempted HTTP to `127.0.0.1:9`, which refused the connection: `PROVIDER_NETWORK_ERROR`, exit 1. No vendor or external host was contacted. It wrote the two events M-6 specifies:
     - an `allowed` event before I/O (`outbound_attempted` false, route fields null);
     - then a `failed` state event under the same `correlation_id` (`outbound_attempted` true, `route_family` `recommended_v2_chart`, `resource_path` `charts`, `error_code` `PROVIDER_NETWORK_ERROR`).

     The corrected probe gave `PROVIDER_AUDIT_UNAVAILABLE` and created no file in the checkout.
9. **Full `tests/` sweep** (`python -m pytest -q -p no:cacheprovider tests/`, with `XDG_STATE_HOME` pointed at an empty scratch directory): **4,918 passed, 3 skipped, 2 xfailed, 0 failed** (1,707 s; 14:14:37Z to 14:43:09Z); pytest exit 0; afterwards `git status` and `git diff` empty, and no file under the scratch `XDG_STATE_HOME`. The count equals PR-35's on `90ec0ca` (result v1.1 §5 #7). The skips and xfails are the pre-existing ones; the 5 warnings are the pre-existing `datetime.utcnow()` deprecation in `engine/ops/http_log.py`. Every updater consumer, the rails- and qa-lane test files and `tests/adapter/test_jsonschema.py` (with its `ENGINE_ENV` leak, plan F-13) ran in it.
10. **Not re-run here** (NOT EXECUTED): the release attestation (CI built and verified it on `484ce6e`, whose tree equals `5892538`; PR-35 built and verified it on `90ec0ca`); a re-convergence (the `--check` modes in items 2 and 3 verify the converged state); a separate classifier dry run (the CI log's classification on the identical tree is the record); the attribution-lock collector (§3).

## 6. Requirement coverage across the work unit

| Requirement and acceptance (Plan v1.1 §7 WU-PR-04) | State | Evidence |
| :- | :- | :- |
| S14 / (1): table-driven tests over the eight matrix rows and seven steps with zero outbound attempts; exit 1 and `outbound_attempted` false for policy refusals, exit 64 for usage; `ENGINE_ENV` alias and conflict; production dry run without the flag refuses `PROVIDER_PROD_OVERRIDE_REQUIRED` | MET | result v1.0 §5 (M-1 to M-8, O-1 to O-7 with case counts); §5 items 6 to 8 here; NC-B; hosted CI |
| S14 / (2): exactly the IF-2 fields, CR/LF-sanitized, no subject or secret data; unwritable sink → `PROVIDER_AUDIT_UNAVAILABLE` before I/O | MET | `vendor_audit.py` read in full (16 keys, printable-ASCII sanitization, exclusions); the probe events in §5 item 8; leak search; result v1.0 §6; CX-1's durability tests and NC-A |
| S14 / (3): closed rails refuse first; no Reader or Aux route gains a vendor path | MET | M-1, M-2 and the closed-rails probe with existing bytes; the empty diff over `adapter/**`, `engine/http/**`, `engine/compat/**`, `engine/narratives/**` (§3); `_acquire_dry_run` unchanged (instruction ID-1; OBS-W4-1 recorded) |
| S14 "authorized initiator" | MET for the implementation: the actor comes from the effective UID through the user database, never from the environment, a CLI option or the reference; a UID with no account name refuses (PD-6; NC-F). Whether a venue yields a stable authenticated human principal is the QA Plan's (N4, R-3; LR4-O2) | code; tests; probes |
| S14 read-only override (instruction ID-3; §7.1.11d) | MET: with an allowed override, `--upsert` and every write refuse `PROVIDER_WRITE_UNSUPPORTED` on both paths before database construction and vendor I/O | `test_o7_production_override_is_read_only_on_both_write_paths` (6), `test_production_override_refuses_legacy_writes_before_ingest` (3); NC-C |
| S08 / (4): `aux-preview --pair-file … --band B` emits band B; without the flag, the file's band | MET | the landed override (three lines); tests (9); NC-D |
| (5): admission and convergence as WU-PR-03 (7); all lanes green | MET | admission `2f18a5eb… 45 1.3.0` (§5 item 1); result v1.0 §9 (two byte-identical passes, digest `63685bd9…`, 54 paths); the `--check` modes here; hosted CI all seven lanes on the final head |
| Instruction ID-1 to ID-10 | MET as bound | §3 (changed set; companion comparison); result v1.0 §4 to §8; the plan's decisions PD-1 to PD-19 lie inside them |
| ID-7 output bytes | MET: existing envelopes unchanged (M-1/M-2 byte assertions; EPIC037 body equivalence in result v1.0 §10 #7); the new refusals carry `error.details.outbound_attempted` only; the emitter proof is byte-identical | results; §5 item 8 |
| ID-8 bounded changes | MET: only the environment setup of the existing tests changed, no assertion was removed or weakened (removed lines read here), no skip or `xfail` was added; the generator changed only its `production` invocation, `--check` passes | §2; §5 items 2 and 6 |
| ID-10 classifier | MET: two registry entries, no function change; all seven lanes ran | the classifier diff; CI classification |
| Evidence obligations (Plan; instruction §10) | MET: the result record names every check with counts, the refreshed `release_id` and every family, the tables, the sink key and default, the actor rule, the ID-8 list, the classifier keys, the stale-document list and the nonclaims; no live call; no sink in the repository | results v1.0 to v1.2; §5 item 4 |
| Security (instruction §11) | MET | the gate only narrows; nothing on stdout or stderr carries the reference, actor or sink path (§5 item 8); the sink is owner-only and outside the checkout |
| Migration and recovery | none needed; no recovery item open | — |
| PR description | MET: the template headings with checks and counts; updated after CX-1 (IF-35-4) | #651 body |

## 7. Findings

**No finding against the landed work.** CX-1 was found and closed before the merge (§4).

Observations (not defects of the unit), with owners:

| ID | Observation | Owner |
| :- | :- | :- |
| LR4-O1 | `append_event` creates the sink's parent with `Path.mkdir(mode=0o700, parents=True)`. Python applies `mode` only to the last directory; intermediate directories it creates (for example a missing `~/.local/state`) get the default mode. The sink's own directory (`0700`) and file (`0600`) are owner-only, so the record stays protected. Plan PD-9 reads "create missing parents owner-only (`0700`)" | IA, as an optional hardening input for a later unit; no security effect on the record |
| LR4-O2 | In this cloud container the actor resolves to `root`. A shell that runs as a shared or root account yields an account name, not a person; whether a venue's principal is a stable authenticated human remains the QA Plan's question (Plan R-3; review v1.0 N4), as the instruction bound | QA Plan (Kronos), through the IA |
| LR4-O3 | Lesson for this IA: instruction v1.0 §10 listed `generate_hde_epic037_bg_resolve.py --check` as a validation without running it at the baseline, where it already failed (plan F-5, OBS-P4-3). The plan replaced it with an equivalence check; no correction is needed for this unit | IA (lesson; later instructions run every check they list) |
| LR4-O4 | Instruction v1.0 §3 says WU-PR-05 "reviews the override code under S19". S19's bound is what #467, #492, #501 and #508 merged, read on `main` (Specification; Plan §7). `engine/bodygraph/resolver.py` and `engine/cli/main.py` are among the 48 paths, so their review on `main` includes the override code in them. `engine/bodygraph/vendor_audit.py` is not among them. The WU-PR-05 instruction states S19's coverage of it precisely | IA (WU-PR-05 instruction) |
| OBS-P4-1 to OBS-P4-7 | as plan v1.0 §17 states: the classifier gap (P4-1); six route-policy tests that depend on an ambient `APP_ENV` (P4-2); the EPIC036/037 `--check`s stale on `main` (P4-3); `scripts/ops/admin_vendor_qa.py` (P4-4); the attestation's child environment without `APP_ENV` (P4-5); no band reaches a suppressed key through `aux-preview` (P4-6); `tests/adapter/test_jsonschema.py`'s `ENGINE_ENV` leak (P4-7) | P4-1 WU-PR-06 or a later classifier unit; P4-2 and P4-7 a later unit through the IA; P4-3 and P4-4 Product Owner; P4-5 the WU-PR-05 and WU-PR-08 instructions; P4-6 observation only |

Carried observations, unchanged:
- OBS-W4-1 and OBS-W4-3: named S19 inputs for WU-PR-05;
- OBS-W4-2 and OBS-W4-4: Product Owner;
- AD-4's four gaps, OBS-P3-3, OBS-P3-14, OBS-P3-17 and LR3-O2's wording: WU-PR-05 instruction;
- LR3-O1, LR3-O4, LR3-O5: their owners;
- OBS-17: did not occur on #651;
- O-6: `ruby` present, version unprinted;
- LR-O1 to LR-O3: applied in this unit's refresh;
- AQ-1: WU-PR-07 only;
- the canon doc-delta candidates of plan v1.0 §17: Product Owner.

## 8. Next approved Plan stage

**WU-PR-05 — Code security review of the HDE-EPIC040 PR04 to PR06a code (PR; Distillation), through PR-10 — Create PR Work-Unit Instructions — 100926.1, by the whole-change Implementation Agent.**
- **Basis:**
  - Implementation Plan v1.1 §7 orders WU-PR-01 → … → WU-PR-04 → WU-PR-05 → …;
  - WU-PR-05's block states "Dependencies and order. Fifth; after WU-PR-03 and WU-PR-04 so that fixes are judged against the surfaces' final shape and precede the version bump";
  - WU-PR-03 is accepted (addendum 2.8); WU-PR-04 is accepted by this review;
  - WU-PR-05 is an ordinary PR unit, so PR-10 is the destination;
  - no `HDE-CRD-0002-WU-PR-05-*` file exists on `main`.
- **Carried into the WU-PR-05 instruction by its author:**
  - the refresh base `release_id` `2f18a5ebbf1908ae1425ec546677d6618746f27c2e1ddc9e5087a81b0aaceb76`, should a fix change a member, with the 22-path roster, step 3b and LR-O1 to LR-O3;
  - AD-4's four gaps with OBS-P3-3, OBS-P3-14, OBS-P3-17 and LR3-O2's wording;
  - OBS-W4-1 and OBS-W4-3;
  - LR4-O4 (S19's coverage of the override code) and LR4-O1;
  - OBS-P4-5 (the attestation's child environment has no `APP_ENV`) and OBS-P4-7 (the `ENGINE_ENV` leak) as test-environment hazards;
  - OBS-17 as a qa-lane risk; O-6.
- **Carried for later instructions:** WU-PR-08 (S17) receives the loopback bind statements and OBS-P4-5; WU-DOC-01 receives the start command and bind, OBS-P3-12, LR3-O4 and plan v1.0 §17's repository documents (`README.md`, `AGENTS.md`, runbooks such as `docs/RUN.md` lines 65–66).

## 9. CANON_CONFLICT_REGISTER

| ID | Status | Decision owner | Record |
| :- | :- | :- | :- |
| CR-1, CR-2, CR-3 (CANON_RECONCILIATION) | APPROVED_AS_CHANGED | Thoth | Specification v1.1 lineage |
| CR-4 | APPROVED | Product Owner | `docs/ephemeral/HDE-CRD-0002-WU-PR-01-po-disposition-cr-4-cr-5-v1.0.md` §2 |
| CR-5 | APPROVED_AS_CHANGED | Product Owner | same record §3 |
| CR-6 | APPROVED, alternative (a) | this IA through RS-20 | rescope review v1.0 §12; addendum 2.6 |
| CR-7, CR-8 | APPROVED, alternative (a) each | Product Owner direction of 2026-10-14 | decision record §6; addendum 2.7 |

No new conflict. The unit applies HDE-CLI-API-Vendor-Ref §7.1.11 as written. Its readings (the matrix and step order read together; PD-4's use of an existing code; PD-5's two-view rule; PD-10's read-only `--upsert`) are recorded in plan v1.0 §15 and §16 and stay within canon. Drainage stays with the Product Owner, unperformed.

## 10. NOT PRODUCED, NOT EXECUTED and pending values

- **NOT PRODUCED:** a saved `MERGE_OBSERVED` artifact for #651; any QA, Ops, acceptance or closure artifact; a PF10 addendum by this review.
- **NOT EXECUTED by this review:** the attribution-lock collector; a release attestation build; a re-convergence; a separate classifier dry run; any live vendor, production or database call. One local connection attempt to `127.0.0.1:9` occurred through a misconfigured probe (§5 item 8); no external host was contacted.
- **Pending:** none for WU-PR-04.

## 11. TypeSafe reading and surface advice for the receiving session (PR-10, WU-PR-05)

Action sent (v8.2): "Write, as the continuing whole-change implementation agent, a new PR work-unit instruction, not yet reviewed, for the fifth unit of an approved change: a one-time recorded code security review of about 48 source and configuration files that four earlier pull requests merged, read on the current main with a per-file review line and a findings table, where each confirmed finding is fixed with a regression test or routed with an owner, and a same-version release re-cut only if a fix changes a release member. It must re-measure the current repository baseline, map the governing canon to the review's threat checklist, and carry about fifteen named inputs and observations from three accepted units (four architecture gaps on non-public routes, the new production vendor-override code, two vendor-path observations, a release refresh base and test-environment hazards). A task list exists (the approved plan's unit block); no code is written and no live provider call occurs; a detailed plan, a Product Owner Proceed, implementation and independent reviews follow."

- **TypeSafe v8.2: Opus 5.5 at extra high.** Effort score 2.96 (confidence 0.29); rung probabilities low 0.02, medium 0.05, high 0.28, extra high 0.26, max 0.37, ultracode 0.02. Model probabilities Fable 5.1 0.18, Opus 5.5 0.81, Sonnet 5.5 0.01, Haiku 5.5 0.00 (confidence 0.75). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.004, Fable 5.1 at medium 0.009, Fable 5.1 at high 0.050, Fable 5.1 at extra high 0.047, Fable 5.1 at max 0.067, Fable 5.1 at ultracode 0.004, Opus 5.5 at low 0.016, Opus 5.5 at medium 0.041, Opus 5.5 at high 0.227, Opus 5.5 at extra high 0.211, Opus 5.5 at max 0.300, Opus 5.5 at ultracode 0.016, Sonnet 5.5 at low 0.000, Sonnet 5.5 at medium 0.001, Sonnet 5.5 at high 0.003, Sonnet 5.5 at extra high 0.003, Sonnet 5.5 at max 0.004, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Flags: boundary between high and max. Sent 2026-10-18T14:26:22Z. Nathan picks the cell.
- **Detail:** v8.2 sent 2026-10-18T14:26:22Z; HTTP 200 in 0.55 s; 5546 input and 71 output tokens; jev-1.13.0. Rung by rule: extra high (nearest to the score, halves up); model by rule: Opus 5.5 (the most probable of the four options, a tie going to the higher-priced model). Flags: boundary between high and max.
- **Which request.** The installed skill's request v8.2 (`request-v8.2.json`, sha256 `62486fcc…`). The skill states it passed its pre-registered gates on 2026-10-18; on `main` the ladder directory still holds the v8 pre-registration (#647) only.
- **Records.** No Notion row was written, as PR-40 directs. Nathan's pick for PR-10 (WU-PR-05) is not stated. Nathan's pick for this PR-40 session is not stated; its reading is result v1.2 §8.

**Surface advice:**
- **Session:** the whole-change Implementation Agent's top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, with Notion read access for the prompt.
- **What it reads:**
  - `docs/pfcanon/` on `main`;
  - the HDE-CRD-0002 records, with Audit §6 S19 and Appendix B (the 48 paths);
  - the 48 files and the WU-PR-03 and WU-PR-04 records named in §8;
  - GitHub read access for #467, #492, #501 and #508 if the instruction cites their merge facts.
- **Environment:** re-measuring the baseline needs Python 3.12 with CI's install, plus `ruby`, `bash` and `curl`, under closed rails in a scratch worktree. Unset the vendor, database and GitHub keys the container sets.
- **Access:** no live vendor, production or database access is needed.
- **Writes:** only the instruction, under `docs/ephemeral/`. This review's pull request should be merged first.

## 12. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / WU-PR-04 / PR-40 / lineage review 1 |
| change / specification | CRD HDE-CRD-0002 / `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` v1.1 |
| work unit | WU-PR-04 (S08, S14) |
| release | GCFPE-20261009.1 / 100926.1 |
| prompt | PR-40 — Review PR Work-Unit Lineage — 100926.1, https://app.notion.com/p/3f44590a05eb81088487e918fd642a7f (page state as of 2026-10-12T02:29:38.234Z). Receiver contract read: PR-10 — Create PR Work-Unit Instructions — 100926.1, https://app.notion.com/p/3f44590a05eb815d97d5f3930c7d3e8a (page state as of 2026-10-12T02:29:33.739Z) |
| role/stage | continuing whole-change IA, read-only PR-40 role |
| capture time | 2026-10-18T14:43:28Z |
| execution identity | https://claude.ai/code/session_01CCKsYD2yX5WgU3biWKb59j |
| inherited usage | instruction v1.0 (§20); plan v1.0 (§22); results v1.0 (§19), v1.1 and v1.2 (§10) |
| pull request | amthorn78/glow-hdengine-v2#651 (`5892538`) |
| repository persistence | PENDING / NON_GATING (`docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent on `main`); recorded here only |

## Canon relied on

Read on `main` at `5892538` (`docs/pfcanon/` unchanged since `b9edb0c`).

| Decision topic | Sources and sections |
| :- | :- |
| Review authority, entry and result | PR-40 — Review PR Work-Unit Lineage — 100926.1 (read in full: "Inputs", "Product Owner merge action", "Read-only review boundary", "Execute", "Required result", "Resolve the next approved Plan stage"); PR-10 — Create PR Work-Unit Instructions — 100926.1 (receiver contract); HDE Governance (`docs/pfcanon/PF04-Canon-HDE-Governance-v2.8.7.md`) §9.1.1 (Proceed per detailed PR plan; merges are Product Owner actions) and §9.1.2 (canon on `main`; in-flight documents govern within their scope) |
| S14 coverage | HDE-CLI-API-Vendor-Ref (`docs/pfcanon/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.3.md`) §7.1.11 preamble and §7.1.11a to §7.1.11f (each clause checked against the landed code: the flag and pattern; classification; the matrix; the order; the carriers; the initiator; the 15-row field table, the exclusions, sanitization and "locally durable … before I/O"); §7.1.10 (route selection unchanged; OBS-W4-3); §3.3 and §3.4 (usage carrier exit 64); §4.6 (`--upsert` not in prod; PD-10). HDE Governance §3.1 "Public traffic (Reader/Aux)" and "Admin ops windows (vendor override)" |
| S08 coverage | HDE-CLI-API-Vendor-Ref §4.5 |
| Review chain | PF10-HDE-Build-Notes v13.5.9 (`docs/pfcanon/PF10-HDE-Build-Notes-v13.5.9.md`) addendum 2.3 (Rules 1–5: the Codex code review read and resolved; no security review) |
| Refresh and labels | Implementation Plan v1.1 §10; addenda 2.6 (RP-2 step 3b; RP-3 22-path roster), 2.7 AD-5 (new base, restart rules), 2.5 (LR-O1 to LR-O3); `AGENTS.md` "Release identity" and "HDE-EPIC040 admission addition" |
| Carried items and next stage | addendum 2.8 ("Carried into the WU-PR-04 instruction"; "Carried for later instructions"); Implementation Plan v1.1 §7 (WU-PR-04 and WU-PR-05 blocks); Specification v1.1 S19 |
| TypeSafe reading | addendum 2.1; the typesafe-scoring skill (request v8.2) |
| In-flight documents | Specification v1.1 rows S08 and S14, constraints and Exclusions; Plan v1.1 §5 (IF-1, IF-2), §7; review v1.1 (N4 carry); Audit §6 S08, S14, §7.1 EC-7; instruction v1.0; plan v1.0; results v1.0 to v1.2 |
| Operative documentation | `AGENTS.md` (canon-first rule; closed rails and redaction; sole Index/Mirror writer; no hand edits; pytest readiness; "Evidence attribution, currentness and distinct decisions"; truncation guardrail and its exit-status corollary, applied in §5 item 5) |

Silence: no canon section defines a lineage-review predicate beyond the PR-40 prompt and HDE Governance §9.1.
