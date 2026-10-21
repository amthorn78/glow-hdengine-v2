---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-04-PR-IMPLEMENTATION-RESULT
artifact_version: "1.0"
result_state: PR_CANDIDATE_PUBLISHED
phase: PR-30
plan_cycle: 1 (the first plan for this work unit)
predecessor: none
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-04
work_unit_title: "Provider gate and Aux preview (PR; Fermentation; S08, S14)"
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-04-pr-instruction-v1.0.md (v1.0, INSTRUCTION_READY; landed by #649 at 9c82b62; unchanged)
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-04-pr-implementation-plan-v1.0.md (v1.0; blob 6baead45; 92,216 bytes; landed by #650 as 6b5b3f3); companion docs/ephemeral/HDE-CRD-0002-WU-PR-04-pr-implementation-plan-v1.0-prototype.diff (blob e0917239; 75,580 bytes)
IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (v1.1; immutable)
PLAN_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (v1.1, IA-30 INITIAL_APPROVE)
SPECIFICATION_ID: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (v1.1, SPECIFICATION_APPROVED; not edited)
IMPLEMENTATION_AUDIT_ID: docs/ephemeral/HDE-CRD-0002-implementation-audit-v1.0.md (v1.0, AUDIT_COMPLETE) — lineage only
REMEDIATION_REVIEW_ID: none
effective_baseline: approved base (Specification v1.1 → Implementation Plan v1.1 + review v1.1 → PR instruction v1.0) + PF10 addenda 2.3, 2.5, 2.6, 2.7 (AD-5 and its downstream items) and 2.8, as instruction v1.0 and plan v1.0 apply them
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.9.md (v13.5.9; blob a125fd4eefbf; unchanged on origin/main 6b5b3f3 since b9edb0c; the unique controlled PF10). Provenance, not a gate
pf10_addendum_paths: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.9.md §2.3, §2.5, §2.6, §2.7, §2.8; §2.1 for §18
pf10_addendum_created: none (PR-30 is not a qualifying approval prompt)
proceed: Nathan / Product Owner, by pasting in this session on 2026-10-18 the PR-30 invocation that names exactly docs/ephemeral/HDE-CRD-0002-WU-PR-04-pr-implementation-plan-v1.0.md (v1.0, state AWAITING_PO_PROCEED), with the prerequisite that #650 is merged (it is: 6b5b3f3 on main). The one Proceed for plan cycle 1
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
session: the dedicated HDE-CRD-0002 WU-PR-04 PR engineering session, PR-30 phase, https://claude.ai/code/session_01JNmEgwAw93afByBxnV6JS8 (the session that ran PR-20; Nathan pasted the PR-30 handoff in it)
prompt: PR-30 — PR Implementation Proceed — 100926.1 (https://app.notion.com/p/3f44590a05eb8148a538f5c80588db14; page state as of 2026-10-12T02:30:08Z; read in full); primary skill glow-hde-pr-development 1.4.0
repository: amthorn78/glow-hdengine-v2; authorized local root /home/user/glow-hdengine-v2 (cloud container)
repository_baseline: origin/main 6b5b3f30c008c4c95b575ac508a9e594894eb9bc (#650 over #649; §2)
branch: claude/dreamy-hawking-yz6hnr (the designated branch; restarted at origin/main 6b5b3f3 after #650 merged; only this cycle's commits)
pull_request: amthorn78/glow-hdengine-v2#651 (https://github.com/amthorn78/glow-hdengine-v2/pull/651; open, base main, not draft)
commits: a00cb8b (hand-edited source, plan §7.1, with the in-flight decisions of §13); 2336a0c (owner-produced re-cut and convergence; the tested code and evidence head); the record commit that adds this file (docs/ephemeral/ only)
release_id: 2f18a5ebbf1908ae1425ec546677d6618746f27c2e1ddc9e5087a81b0aaceb76 (1.3.0, 45 members; supersedes d84d99e1…)
canon_conflict_register: CR-1 to CR-8 carried, all decided; no new entry (§16)
created_at: 2026-10-18T12:57:07Z
next_phase: PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1 (https://app.notion.com/p/3f44590a05eb811ebf72e949b7b1572e), in its own dedicated session (session_disposition NEW_DEDICATED)
---

# HDE-CRD-0002 WU-PR-04 — PR Implementation Result v1.0 (PR-30)

## 1. Result

**PR_CANDIDATE_PUBLISHED.** Plan v1.0 is implemented, converged by the owners, locally validated (§10) and published as [amthorn78/glow-hdengine-v2#651](https://github.com/amthorn78/glow-hdengine-v2/pull/651):
- **S14:** `hdctl bg:resolve --source vendor --allow-prod-vendor <AUTHORIZATION_REF>`, the seven-step order and eight-row matrix of HDE-CLI-API-Vendor-Ref §7.1.11a–f, the `ENGINE_ENV` alias, the 16-field audit record in an owner-only local sink outside the checkout, and the read-only production override (§5, §6).
- **S08:** `aux-preview --pair-file … --band B` uses band B for the selected category (§7).
- **ID-8, ID-10 and the documents line:** as plan §6.9, §6.11 and §6.12 (§8).
- **Refresh:** one same-version re-cut at `1.3.0` (`release_id` `2f18a5eb…`) and two byte-identical convergence passes; 54 owner-produced paths (§9).

PR-35 owns review retrieval and correction, hosted current-head CI and merge readiness. Nothing here is merged. Nothing here claims merge readiness, QA, acceptance or closure.

## 2. Recovery and base

| Check | Observation |
| :- | :- |
| Prerequisite | #650 merged: `6b5b3f3` on `origin/main` |
| Open pull requests | none (GitHub listing, state open, before any remote write of this phase) |
| Local root, worktrees, branches | one worktree, `/home/user/glow-hdengine-v2`, on `claude/dreamy-hawking-yz6hnr`; the branch held only #650's merged history, so it was restarted at `origin/main` `6b5b3f3` (12:15:27Z) before any change |
| Remote branches | `claude/friendly-galileo-y1vx5h` (TypeSafe ladder records under `docs/ephemeral/`; unrelated), `claude/nifty-cray-w86vmp`, `claude/wizardly-edison-x05uwc`, `codex/exclude-markdown-code-review`, `docs/20261012-crd0002-specification`, `main`. `claude/dreamy-hawking-yz6hnr` is absent on the remote. None carries WU-PR-04 code |
| WU-PR-04 artifacts on `main` | instruction v1.0, plan v1.0 and its companion diff; no `HDE-CRD-0002-WU-PR-04-pr-implementation-result-*`, no WU-PR-04 code commit or pull request |
| Plan §8 step 2 | `git diff --name-only 9c82b62 6b5b3f3` lists only the plan and its companion diff (`docs/ephemeral/`); no member, manifest or other path moved, so §4.1's checks needed no re-run. `git apply --check` of the companion diff on `6b5b3f3`: exit 0 |
| PF10 | `docs/pfcanon/PF10-HDE-Build-Notes-v13.5.9.md`, blob `a125fd4eefbf` on `6b5b3f3`, the only PF10 file; unchanged since `b9edb0c` |
| Environment (plan §8 step 3) | CPython 3.12.3 venv with CI's install (`setuptools>=68`, `wheel`, `requirements.txt`, `requirements-dev.txt`, `-e .`); `python -m pytest --version` → pytest 8.4.2; `ruby` 3.3.6 at `/usr/local/bin/ruby`; `bash`, `curl`. Closed rails `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`; unset by name `DATABASE_URL`, `GEO_API_KEY`, `HD_API_KEY`, `HDAPI_BASE_URL`, `HD_API_BASE_URL`, `HDAPI_KEY`, `HD_GEOCODE_KEY`, `GH_TOKEN`, `GITHUB_TOKEN`, `ENGINE_ENV` |

## 3. Authority, Proceed and lineage

- **Proceed.** Nathan's PR Implementation Proceed for exactly plan v1.0 (front matter). It authorizes this unit's implementation, local validation and initial publication, and PR-35's review correction under the same Proceed. It authorizes no merge.
- **Scope.** Plan v1.0 §5 and §7.1; the effective baseline in the front matter. Nothing outside §7.1 was hand-edited; owner-produced paths came only from their owners (§9).
- **Lineage.** Specification v1.1 → Implementation Plan v1.1 + IA-30 review v1.1 → PR instruction v1.0 (PR-10) → plan v1.0 (PR-20) → this result (PR-30). None is rewritten.

## 4. Implementation (commit `a00cb8b`)

`a00cb8b` = the companion diff applied to `6b5b3f3` plus the two in-flight decisions of §13 (11 paths, +1,286 / −19):

| Path | Change |
| :- | :- |
| `engine/cli/main.py` (member) | the `--allow-prod-vendor` option (metavar `AUTHORIZATION_REF`, `bg:resolve` only); the four usage lines; `_allow_prod_vendor_usage_error(argv)` called in `cli()` before argparse, including D-1's `--` rule; step 2 in `bg_resolve`; the hand-over `authorization_ref=args.allow_prod_vendor`; the S08 band override |
| `engine/bodygraph/resolver.py` (member) | `AUTHORIZATION_REF_PATTERN`, `is_valid_authorization_ref`, `VendorEnvironment`, `classify_vendor_environment`, `_OverrideGate`, `_AttemptTrackingClient`, `_override_refusal`; the `authorization_ref` keyword on `resolve_bodygraph` and `_resolve_vendor`; steps 4 to 6; `_resolve_vendor_route` with the gate hooks; `_append_flag_absent_event`, `_append_state_event`; `override_gate` on `_resolve_vendor_v2_chart`; the legacy production write refusal |
| `engine/bodygraph/vendor_audit.py` (new, 178 lines; not a member) | plan §6.7 |
| `tests/bodygraph/test_vendor_prod_override.py` (new, 96 cases) | M-1 to M-8, O-1 to O-7, the audit record and seams |
| `tests/cli/test_bg_resolve.py` (6 → 37 cases) | plan §7.1's 35 plus D-1's two `--` cases |
| `tests/cli/test_aux_preview.py` (2 → 9 cases) | S08; D-2's import placement |
| `tests/bodygraph/test_resolver_vendor.py` (4 → 24 cases) | classification (11) and refusals (5); ID-3 legacy (3); unchanged non-production legacy write (1); `APP_ENV` in two mappings (F-3); the `ENGINE_ENV` fixture (F-13) |
| `tests/bodygraph/test_bg_resolve_v2_mapped_cache.py` (28 cases, count unchanged) | the `production_override` helper; the two production-like tests; the `ENGINE_ENV` fixture |
| `tools/evidence/generate_v2_mapped_cache_evidence.py` | the `production` scenario only (plan §6.9) |
| `ci/checks/classify_ci_changes.py` | the two ID-10 entries |
| `docs/CLI_commands.md` | plan §6.12 |

Member bytes were frozen at this commit; no member changed afterwards (the restart rule did not trigger).

## 5. S14 — order and matrix, with results

All rows run under the I/O guards of plan §9 (`HdApiClient` construction, `DBAccess`, `urllib.request.Request`/`urlopen`, `socket.getaddrinfo`, `socket.socket` fail the test). Every case passed in the pre-cut runs, the hermeticity runs and the full sweep (§10).

**Order** (plan §6.2):

| Step | Refusal | Exit | Event | Tests (cases) |
| :- | :- | :- | :- | :- |
| O-1 parse | usage `COMMAND`, `DUPLICATE`, `VALUE` | 64 | none | `test_o1_parse_errors_precede_rails_and_resolver` (2); `tests/cli/test_bg_resolve.py`: `…_duplicate_is_usage` (3), `…_invalid_value_is_usage` (14), `…_outside_bg_resolve_is_usage` (5) |
| O-2 source | usage `SOURCE` | 64 | none | `test_o2_non_vendor_source_is_usage_before_rails` (3); `…_with_non_vendor_source_is_usage` (3) |
| O-3 rails | existing `PROVIDER_REFUSED`, `PROVIDER_NETWORK_BLOCKED` | 1 | none | `test_o3_rails_precede_environment_classification` (1); M-1, M-2 |
| O-4 environment | `PROVIDER_CONFIG_INVALID` | 1 | none | `test_o4_environment_is_classified_before_the_matrix` (14), `test_o4_engine_env_alias_applies_when_app_env_is_blank` (3), `test_o4_process_production_environment_is_never_downgraded` (1); `test_environment_classification` (11), `…_refuses_absent_unknown_or_conflicting` (5) |
| O-5 matrix | `PROVIDER_PROD_OVERRIDE_REQUIRED`, `PROVIDER_PROD_OVERRIDE_INVALID` | 1 | M-3 only | `test_o5_matrix_precedes_actor_and_event` (1) |
| O-6 actor and event | `PROVIDER_AUDIT_UNAVAILABLE` | 1 | `allowed`, durable, before step 7 | `test_o6_durable_event_precedes_step_seven` (1), `test_o6_event_failure_blocks_step_seven` (1) |
| O-7 existing gates | step-7 codes; ID-3 `PROVIDER_WRITE_UNSUPPORTED` | 1 or 0 | one state event | `test_o7_production_override_is_read_only_on_both_write_paths` (6), `test_o7_state_event_failure_changes_nothing` (1), `test_o7_vendor_failure_after_an_attempt_is_recorded_as_failed` (1); `test_production_override_refuses_legacy_writes_before_ingest` (3) |

**Matrix** (plan §6.4):

| Row | Environment / rails / flag | Code | Exit | Events | Tests (cases) |
| :- | :- | :- | :- | :- | :- |
| M-1 | any recognized / `SAFE_MODE` closed / absent or valid | existing `PROVIDER_REFUSED`, existing bytes | 1 | none | `test_m1_safe_mode_closed_refuses_with_existing_bytes` (10) |
| M-2 | any recognized / network closed / absent or valid | existing `PROVIDER_NETWORK_BLOCKED`, existing bytes | 1 | none | `test_m2_network_closed_refuses_with_existing_bytes` (8) |
| M-3 | `prod`, `production`, `live` / open / absent | `PROVIDER_PROD_OVERRIDE_REQUIRED` | 1 | one `refused` when actor and sink are available | `test_m3_production_flag_absent_requires_override_and_records_refusal` (10), `test_m3_flag_absent_result_stands_when_its_event_cannot_persist` (1), `test_production_dry_run_without_flag_refuses` (1); CLI `test_production_like_cli_without_flag_emits_the_override_refusal` (1, two-run identity) |
| M-4 | production-like / open / malformed or duplicated | CLI usage (O-1) | 64 | none | the O-1 CLI usage tests |
| M-5 | production-like / open / valid; actor or sink unavailable | `PROVIDER_AUDIT_UNAVAILABLE` | 1 | none | `test_m5_valid_flag_with_unavailable_actor_refuses_before_io` (1), `test_m5_valid_flag_with_unavailable_sink_refuses_before_io` (1), `test_unwritable_sink_is_unavailable` (2) |
| M-6 | production-like / open / valid and auditable | step 7 decides | 0 or 1 | `allowed`, then the state event | `test_m6_valid_auditable_flag_allows_one_bounded_read` (2: v2 and legacy; exactly one fake fetch) |
| M-7 | recognized non-production / open / absent | current behavior | as today | none | `test_m7_non_production_without_flag_keeps_current_policy` (6) |
| M-8 | recognized non-production / open / present | `PROVIDER_PROD_OVERRIDE_INVALID` | 1 | none | `test_m8_non_production_with_flag_is_invalid` (5) |

Library reference (PD-4): `test_library_reference_must_be_valid_and_applicable` (7). CLI hand-over: `test_allow_prod_vendor_valid_value_reaches_the_resolver_once` (4); `MISSING_VENDOR_INPUT` kept: `test_allow_prod_vendor_keeps_missing_vendor_input_usage` (1).

## 6. Override contract (instruction §8, contract F-2)

For WU-PR-05 (S19 review of the override code), WU-PR-08 and the QA Plan:

- **Command form:** `hdctl bg:resolve --source vendor --allow-prod-vendor <AUTHORIZATION_REF> …`. One value of 1 to 128 characters matching `^[A-Za-z0-9][A-Za-z0-9._:/-]{0,127}$`; given once; accepted only by `bg:resolve` with `--source vendor`; never after `--`; no short spelling, alias, negation, environment form or default. Library: `resolve_bodygraph(..., authorization_ref=<str | None>)`.
- **Usage errors** (exit 64, stderr one line, stdout empty, value never echoed): `hdctl: --allow-prod-vendor is accepted only by bg:resolve --source vendor`; `hdctl bg:resolve: --allow-prod-vendor may be given only once`; `hdctl bg:resolve: --allow-prod-vendor requires one AUTHORIZATION_REF of 1 to 128 characters matching ^[A-Za-z0-9][A-Za-z0-9._:/-]{0,127}$`; `hdctl bg:resolve: --allow-prod-vendor is accepted only with --source vendor`.
- **Environment:** `APP_ENV`, else `ENGINE_ENV` when `APP_ENV` is blank; trimmed and lowercased; nonblank values must agree; production-like `{prod, production, live}`, non-production `{dev, test, local, stage, staging}`; anything else refuses. A production-like process value is never downgraded by a caller's mapping (PD-5).
- **Refusal codes** (exit 1, envelope on stdout, empty stderr; `error.details.outbound_attempted: false` at exactly that place, PD-15):

| Code | Message |
| :- | :- |
| `PROVIDER_CONFIG_INVALID` (step 4) | `vendor environment classification requires APP_ENV or ENGINE_ENV to name one recognized environment` |
| `PROVIDER_PROD_OVERRIDE_REQUIRED` | `production-like vendor access requires --allow-prod-vendor` |
| `PROVIDER_PROD_OVERRIDE_INVALID` (non-production) | `production vendor override is not accepted in a non-production environment` |
| `PROVIDER_PROD_OVERRIDE_INVALID` (library: malformed reference or non-vendor source) | `production vendor override reference is malformed or inapplicable` |
| `PROVIDER_AUDIT_UNAVAILABLE` | `production vendor override audit is unavailable` |

  Step-7 refusals keep their existing bytes; the override's write refusals are `PROVIDER_WRITE_UNSUPPORTED` "mapped-cache persistence is refused in production-like environments" (v2) and "BodyGraph persistence is refused in production-like environments" (legacy), with no `details`.
- **Read-only:** with an allowed production override, `--upsert` (with or without `--dry-run`) and every write refuse before database construction and before vendor I/O (PD-10).
- **Actor rule:** `pwd.getpwuid(os.geteuid()).pw_name`; never `USER`, `LOGNAME`, `LNAME`, `USERNAME`, a CLI option or the reference. A failed lookup, a name that sanitizes to empty, or a UID without an account name refuses `PROVIDER_AUDIT_UNAVAILABLE` (PD-6).
- **Sink:** key `HDE_VENDOR_OVERRIDE_AUDIT_PATH` (read from the merged vendor view); else `$XDG_STATE_HOME/glow-hdengine/vendor_prod_override.jsonl` when `XDG_STATE_HOME` is nonblank and absolute; else `~/.local/state/glow-hdengine/vendor_prod_override.jsonl`. Must be absolute after `realpath`, and not equal to or inside the repository checkout. Parents created `0700`; the file opened `O_WRONLY|O_APPEND|O_CREAT|O_CLOEXEC` `0600`, must be regular; existing permissions are not changed; any `OSError` is unavailable.
- **Record:** schema `vendor_prod_override.v1`, event `vendor_prod_override`; one `sercanon` line per event (UTF-8, sorted keys, compact, one LF), written in full, then `fsync`. Exactly 16 fields: `actor_principal`, `authorization_ref`, `command` (`bg:resolve`), `correlation_id` (UUID4), `environment`, `error_code`, `event`, `network_open`, `occurred_at` (`%Y-%m-%dT%H:%M:%S.%fZ`), `outbound_attempted`, `outcome`, `resource_path`, `route_family`, `safe_mode_open`, `schema_version`, `source` (`vendor`). Strings keep printable ASCII only; every other character becomes `?`.
- **Events and outcomes:** M-3 writes one best-effort `refused` (reference null, `PROVIDER_PROD_OVERRIDE_REQUIRED`, `outbound_attempted` false, route fields null); its failure changes nothing. M-6 writes `allowed` before step 7 (route fields and `error_code` null, `outbound_attempted` false); its failure is `PROVIDER_AUDIT_UNAVAILABLE`. After step 7, one state event with the same `correlation_id`: `completed` (true), `failed` after the fetch was entered (true), `refused` before the fetch (false); route fields carry the classified labels or null; an unexpected exception appends `failed` or `refused` with `error_code` null and propagates; a state-event failure changes nothing. No event for steps 1 to 4, closed rails or any non-production invocation.
- **Never on stdout, stderr, exceptions or logs:** the reference, actor, correlation ID, sink path, timestamp, override state. Never in the sink: subject, birth fields, location, URL, header, key, database identifier, raw provider message.

## 7. S08 — Aux preview band

In `_resolve_from_pair_file`, after the file's category and band are read and validated, `if args.band: band = args.band`. Category selection, perspective, the file's `release_id`, emission only with `--show-narrative`, the `--admin-out` sidecar (naming the flagged band's key) and the non-pair-file path are unchanged. Tests: `test_aux_preview_pair_file_band_flag_selects_the_flagged_band` (4 bands, sidecar key), `…_without_band_flag_uses_the_file_band` (1), `…_keeps_category_refusals` (1: `MISSING_COMPAT_CATEGORY`, empty categories, `INVALID_COMPAT_INPUT`), `…_without_show_narrative_emits_nothing` (1); all pass.

## 8. Bounded changes

- **ID-8** (plan §6.9), exactly: the `production_override` helper and its use in `test_production_like_refuses_before_vendor_and_db` (3) and `test_process_production_environment_cannot_be_overridden_for_database_write`, assertions unchanged; the `production` scenario of `generate_v2_mapped_cache_evidence.py` (temporary sink, patched actor `fixture-operator`, `authorization_ref="HDE-CRD-0002-FIXTURE"`), output bytes and `PREDICATE_KEYS` unchanged; `"APP_ENV": "test"` in two mappings of `tests/bodygraph/test_resolver_vendor.py` (F-3); the autouse `ENGINE_ENV` removal in that file and in the mapped-cache file (F-13, PD-19). No expected code weakened, no assertion removed, no test skipped, deselected or marked.
- **ID-10:** `_PRODUCT_TEST_OWNER_PATHS["engine/bodygraph/vendor_audit.py"] = ("tests/bodygraph/test_vendor_prod_override.py",)` and `_EVIDENCE_GENERATOR_TEST_OWNERS["tools/evidence/generate_v2_mapped_cache_evidence.py"] = ("tests/evidence/test_v2_mapped_cache_evidence.py",)`, each with a one-line comment; no function changed.
- **Documents:** `docs/CLI_commands.md` only (plan §6.12). The stale documents are listed in §12.
- **Expected unchanged (plan §7.3):** `git diff --name-only 6b5b3f3 2336a0c` touches none of them (checked by path pattern), nor `adapter/**`, `engine/http/**`, `engine/compat/**` or `docs/pfcanon/**`.

## 9. Release refresh and convergence (commit `2336a0c`)

Run in the branch's working tree after `a00cb8b`, under closed rails with vendor and database keys unset; plan §6.13 steps 2 to 10 (pass 1, 37 runs) and steps 3 to 10 (pass 2, 34 runs). Every run exited 0.

| Step | Result |
| :- | :- |
| 2 | `cut_release_manifest.py --version 1.3.0 --built-at-utc 2026-08-24T18:04:49Z --roster-from-admission`; recompute `--check-manifest-only`; cutter `--check`: exit 0. Two manifest rows changed (`engine/bodygraph/resolver.py`, `engine/cli/main.py`) |
| 3 | admission: `2f18a5ebbf1908ae1425ec546677d6618746f27c2e1ddc9e5087a81b0aaceb76`, 45 members, `1.3.0`; `--compare-goldens .` with the report outside the tree: exit 0 |
| 3b | A7 write then `--check`: exit 0 |
| 4–6 | canonical JSON gate and `--check-only`; updater and `--check`; `--publish-family` and updater `--check`: exit 0 |
| 7 | A7 write and `--check`; determinism gate proofs; open-rails ABBA proof (fixture mode, keys absent); `FROZEN_OPEN_ABBA_SHA256` set by one anchored replacement to `9949ddf5fe7e5d329a6d9a49bea916a9ff369ba6dd058de18b7cf7df9556098f` (supersedes `06611525…`); conjunction writer and engine core evidence: exit 0 |
| 8 | updater, `--check`, `orientation_demo.py --check`, `validate_evidence_paths.py`, `ci/checks/check_mirror_schema.sh`, `ci/checks/check_evidence_index_hash.sh`, `check_lf_endings.py`, `ci/checks/check_final_lf.sh`, `refresh_step_logs_manifest.py --check`: exit 0 |
| 9 | sanity pipeline with the log outside the tree: `summary:PASS` (both passes); canonical run; `run_sanity_pipeline_gate.py`; updater `--check`: exit 0 |
| 10 | showcompat, CLI conformance, rails gate and env matrix `--check`: exit 0 (frozen families unchanged) |
| 11 | `git grep -l -E 'd84d99e1\|06611525'` outside `docs/`, `.audit_src/`, `handoff/`, `manifest_pre.sha256`, `manifest_post.sha256`: no hit. Mirror: 620 rows; 27 carry the new `release_id`; none carries `d84d99e1`; the purity-report row has no `notes` |

**Byte stability.** Each pass left 54 changed paths and no untracked file; the two `git diff HEAD` patches are byte-identical (SHA-256 `63685bd99c566b23096c53d9b3008d3e2f5267e747608f9de63292be835d0b4e`), and `git diff a00cb8b 2336a0c` has the same digest.

**Changed set** (54 paths, equal to plan §6.13's expected set):
- `catalog/manifest.json`; `tools/evidence/generate_open_rails_abba_proof.py` (`FROZEN_OPEN_ABBA_SHA256` only);
- 26 evidence primaries and their 26 path proofs: `artifacts/proofs/{reader_success_get_head_304.json,success_304.txt,success_encoding_invariance.txt,success_get.txt,success_head.txt}`; `artifacts/catalog/{catalog_schema_validation,domain_closure_report}.log`; `artifacts/core/{abba/ab_ba_parity,json_compare/core_result_json_compare,two_run/identity}.json`; `artifacts/writer/{conjunction_write_readback.log,conjunction_writer_summary.json}`; `audit/gates/canonical_json/{json_canon_compare,json_canonical_check}.log`; `audit/gates/json_gate/canonical/{json_gate_check_log,json_gate_compare_log}.ndjson`; `audit/gates/determinism/{abba.bytes,open_rails_abba.json,tworun_identity.sha256}`; `audit/gates/parity/reader_cli/{ab,ba,summary}.json`; `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, `artifacts/evidence_index.jsonl`, `artifacts/evidence_index.jsonl.sha256`.

The families plan §6.13 lists as rewritten byte-identically (the catalog family, `endpoints_env_gate_proof.log`, `success_writers_errors.txt`, `artifacts/reader/endpoints_snapshot.json`, `artifacts/core/purity/purity_report.json`, the canonical sanity log) are not in the diff.

## 10. Local validation (plan §10)

Every run that can write tracked files ran in a detached worktree of `2336a0c` and ended with `git diff --exit-code` and an empty `git status --short --untracked-files=all` (all clean). Profile as §2.

| # | Check | Result |
| :- | :- | :- |
| 1 | Classifier, base `6b5b3f3…` → head `2336a0c…`, event `pull_request` | `reason=selected_lanes`; 65 paths; all seven lanes; `needs_python=true`, `changed_tests=true`; 166 changed-test targets (the same 166 as the plan's rehearsal) |
| 2 | Changed-tests step as `ci.yml` runs it | the 166 targets in a detached worktree with `-p no:cacheprovider`: 3,679 passed (676.7 s), exit 0; clean tree. Two more than the rehearsal's 3,677: D-1's cases |
| 3 | Seven lanes as `ci.yml` writes them | product 77 passed; compat (`check_cli_help.sh`, serializer guard, emitter proof, tests) 103 passed, 3 skipped, 2 xfailed; db (direct-DB contract check, tests) 249 passed; rails (the three job definitions: 24, 113 and 59 passed; then the pin file: 138 passed); evidence (seven checks, tests) 130 passed (784.1 s); qa 488 passed; release (recompute, tests) 79 passed; every lane exit 0; clean tree |
| 3 | Attestation build and verify into the external empty directory, `--require-clean` | recompute exit 0; build exit 0; verify exit 0; `release_admission` `PR06R_B_FINAL_PASS`, `validation_result` `PASS`, `release_id` and `manifest_sha256` `2f18a5eb…`, `source_commit` `2336a0ca6d87…` with `source_commit_exact` true; tree clean |
| 4 | Full `tests/` sweep (`ruby`, `bash`, `curl` on `PATH`) | **4,915 passed, 3 skipped, 2 xfailed, 0 failed** (1,560.8 s; 12:29:44Z to 12:55:47Z), exit 0, then `git diff --exit-code` and an empty status. The baseline's 4,761 plus 154 new cases (96 + 31 + 7 + 20), with the same skips and xfails; the 5 warnings are the pre-existing `datetime.utcnow()` deprecation in `engine/ops/http_log.py` |
| 5 | `generate_v2_mapped_cache_evidence.py --check`; `generate_bodygraph_policy_proofs.py --check` | exit 0 (`V2_MAPPED_CACHE_EVIDENCE_OK`); exit 0 |
| 6 | `ci/checks/check_cli_help.sh`; `tests/cli/test_serializer_guards.py`; `serializer_grep_guard.py`; `emitter_symbol_proof.py` | exit 0; 3 passed; exit 0; output byte-identical to `artifacts/cli/guards/emitter_symbol_proof.txt` (SHA-256 `6120d745…`) |
| 7 | EPIC037 equivalence: `build_outputs()` on `6b5b3f3` and on `2336a0c`, `inspected_internal_loci` and `input_references` set aside | four files; every body equal (the closed-rails envelope included); loci equal in two files and differing in the other two only at `engine/bodygraph/resolver.py` and `engine/cli/main.py`; `main`'s output equals the plan's rehearsal baseline. The pre-existing `--check`s (F-5): `generate_hde_epic037_bg_resolve.py --check` and `generate_hde_epic036_bg_resolve_route_policy.py --check` exit 1 on `6b5b3f3` and on `2336a0c` with the same stale-file lists; neither was run in write mode |
| 8 | Convergence checks of §6.13 steps 2 to 10 in `--check` form, and step 11, on `2336a0c` | 18 runs, all exit 0; admission `2f18a5eb…` 45 `1.3.0`; stale-binding hits 0; tree clean |
| 9 | Negative controls on the source with one hunk disabled (scratch copy; restored after each) | NC-1 step 5: 42 failed, 115 passed; NC-2 the pre-I/O event write: 14 failed, 143 passed; NC-3 ID-3's legacy write refusal: 6 failed, 151 passed (these three on the new file, `test_resolver_vendor.py` and `test_bg_resolve.py`, 157 cases); NC-4 the S08 override: 3 failed, 6 passed (`test_aux_preview.py`); NC-5 the CLI pre-scan: 22 failed, 111 passed (`test_bg_resolve.py` and the new file, 133 cases); NC-6 D-1's `--` rule: 2 failed, 35 passed (`test_bg_resolve.py`). Every one fails as intended |
| 10 | Hermeticity: the four changed test files, the mapped-cache file and `tests/evidence/test_v2_mapped_cache_evidence.py` | `APP_ENV=dev`: 212 passed; `APP_ENV` unset: 212 passed; with `tests/adapter/test_jsonschema.py` first in one process: 215 passed, 2 xfailed (also run pre-cut with the same counts). F-4, informative: `tests/bodygraph/test_bg_resolve_route_policy.py` 12 passed with `APP_ENV=dev`; with it unset 6 failed, 6 passed on `2336a0c` and 12 passed on `6b5b3f3`, the six plan F-4 names |

Pre-cut (plan §8 step 5, on the source before the cut): the six files 212 passed; with `APP_ENV` unset 212 passed; with `test_jsonschema.py` first 215 passed, 2 xfailed.

**Not run:** hosted CI (PR-35's); any live vendor, production or database call.

## 11. Requirement → proof (plan §9)

| Item | Proof (this phase) |
| :- | :- |
| S14 flag, order, matrix, carrier | §5 tables; usage tests; classification tests; the CLI two-run identity |
| S14 initiator and audit | `test_record_has_exactly_the_if2_fields_and_canonical_lines`, `test_fields_are_sanitized_against_cr_lf_and_control_bytes`, `test_record_and_streams_carry_no_subject_url_or_secret`, `test_actor_comes_from_the_effective_uid_not_the_environment`, `test_sink_path_rule`, `test_sink_is_created_owner_only_and_appended`, `test_unknown_outcome_is_rejected`, `test_unwritable_sink_is_unavailable`; M-3, M-5, M-6, O-6, O-7 |
| S14 rails first, no public path, read-only | M-1, M-2, O-3; `test_o7_production_override_is_read_only_on_both_write_paths` (6); `test_production_override_refuses_legacy_writes_before_ingest` (3); no `adapter/**`, `engine/http/**` or `engine/compat/**` path in the diff; `tests/bodygraph/test_resolve_compat_chart.py` passes in the sweep |
| S14 live behavior | not this unit (QA Plan) |
| S08 | §7 |
| Refresh | §9; lanes; attestation |
| ID-8 | the two mapped-cache tests; `generate_v2_mapped_cache_evidence.py --check`; sanity `summary:PASS`; the attestation |
| ID-10 | classifier dry run (§10 #1); `tests/evidence/test_rails_ci_workflow_integration.py` in the rails lane |
| ID-7 | M-1/M-2 byte assertions; `emitter_symbol_proof.py` byte equality; the EPIC037 equivalence |

## 12. Stale documents, observations and carried items (not in this pull request)

Unchanged from plan v1.0 §17, which holds the full text and owners:
- **Stale documents:** HDE-CLI-API-Vendor-Ref §7.1.11 "Required-Now implementation gap (DD-04; held)" and §7.2.0; HDE Users Guide §16, §10.1 and Recipe F; Glow Infrastructure §8 (the key `HDE_VENDOR_OVERRIDE_AUDIT_PATH`); the §7.1.11f "governed clock boundary" (Product Owner, canon doc-delta); `README.md`, `AGENTS.md` and runbooks with `bg:resolve --source vendor` commands, for example `docs/RUN.md` lines 65–66 (WU-DOC-01). The DD-04 rows in `audit/docdeltas/hde-epic040_doc_deltas.md`, `audit/qa/hde-epic040/00_meta/doc_deltas.md` and HDE Phased Epics stay as they are.
- **Observations** OBS-P4-1 to OBS-P4-7 (owner: the IA, who routes them). OBS-P4-1 holds as described: the classifier dry run selects all lanes here only because this pull request touches full-validation paths. No new observation arose in this phase.
- **Carried:** OBS-W4-1 and OBS-W4-3 to WU-PR-05 (S19); OBS-W4-2 and OBS-W4-4 to the Product Owner; LR-O1 and LR-O3 applied (§9); LR-O2 not triggered, its consumers run in the sweep; OBS-17 (RK-5) and O-6 (RK-6) for PR-35 if they occur; AD-4's gaps, OBS-P3-3, OBS-P3-14, OBS-P3-17 and LR3-O2's wording to the WU-PR-05 instruction; LR3-O1, LR3-O4, LR3-O5 with their owners; AQ-1 gates WU-PR-07 only.

## 13. In-flight decisions

| ID | What changed | Why it was necessary | Tested by (outcome) |
| :- | :- | :- | :- |
| D-1 | `_allow_prod_vendor_usage_error` treats an occurrence after the `--` separator as the `COMMAND` usage error (`engine/cli/main.py`, 7 lines); two cases added to `test_allow_prod_vendor_outside_bg_resolve_is_usage` (`… -- --allow-prod-vendor REF` and `… -- --allow-prod-vendor=REF`) | Found in PR-30's re-read of the companion hunks against plan §6.1. With a valid value after `--`, the pre-scan passed and argparse then reported "unrecognized arguments: --allow-prod-vendor <value>", echoing the reference on stderr. ID-1 and §6.1 require that no usage path echoes the value, and §7.1.11a accepts the option only on `bg:resolve --source vendor`. The fix applies the plan's own rule to the one path the companion diff missed; it adds no behavior outside §6.1 | the two new cases pass (stdout empty, exit 64, the `COMMAND` line, value absent from both streams); NC-6 (the rule disabled): 2 failed, 35 passed; `tests/cli/test_bg_resolve.py` 37 passed; full sweep (§10 #4) |
| D-2 | `tests/cli/test_aux_preview.py`: the two function-local `import json` moved to one module-level import | Repository style (module-level imports, as `test_resolver_vendor.py` in this unit); no behavior change | `tests/cli/test_aux_preview.py` 9 passed; NC-4 unchanged (3 failed, 6 passed) |
| D-3 | Publication order. Plan §8 step 9 lists "write and read back the record, commit, push and open the PR". The two code commits were pushed and the pull request opened first; this record, which names the pull request and the post-publication read-back, was then committed and pushed | The PR-30 prompt requires the record to hold the PR reference and allows PR and commit references only after they exist; the handoff may not carry the only copy of a fact. Same precedent as WU-PR-03 result v2.0 D-1. Cost: the first hosted run is superseded by the record push (pull-request concurrency cancels it) | this record read back after the push (§14) |

## 14. PR_REMOTE_ACTION_LEDGER

| Time (UTC, 2026-10-18) | Action | Evidence |
| :- | :- | :- |
| 12:15:27 | branch `claude/dreamy-hawking-yz6hnr` restarted at `origin/main` `6b5b3f3` (local only; it held only #650's merged history) | reflog |
| 12:18:13, 12:26:59 | local commits `a00cb8b` (source) and `2336a0c` (convergence) | §4, §9 |
| 12:28–12:55:47 | local validation (§10) | all pass |
| before any remote write | open-PR listing; remote branch listing | none open; `claude/dreamy-hawking-yz6hnr` absent on the remote |
| 12:56:14 | before the push: `origin/main` `6b5b3f3` (fetched), branch `claude/dreamy-hawking-yz6hnr`, clean tree, outgoing `a00cb8b`, `2336a0c`; `git push -u origin claude/dreamy-hawking-yz6hnr` (new branch) | `* [new branch]`; `git ls-remote` → `2336a0ca6d87cc470bb5f745b48c6228dfd858a0` |
| 12:56:50 | created amthorn78/glow-hdengine-v2#651 (base `main`, head `claude/dreamy-hawking-yz6hnr`, not draft), description with the template headings | https://github.com/amthorn78/glow-hdengine-v2/pull/651; read back: open, not draft, not merged, head `2336a0ca6d87…`, base `6b5b3f30c008…`, 2 commits, 65 files (+1,391/−124), `mergeable_state: unstable` (hosted checks starting). The server replaced the description's closing attribution lines with its own footer |
| after this record is written | record commit and push (`docs/ephemeral/` only) | read back by PR-30 after the push; the pushed head is verified by PR-35 at entry |
| — | Reviews read | none (PR-35's) |
| — | Hosted CI | not observed (PR-35's). The run started for `2336a0c` is superseded by the record push; the workflow's pull-request concurrency cancels it (D-3). The record push still selects all seven lanes, because the classifier compares base to head |
| — | Mergeability | `unstable` at 12:56:50 for `2336a0c` (checks not complete); PR-35 re-reads it on the current head |
| — | Remaining useful local action | none for PR-30 |
| — | Next evidence action | PR-35: subscribe to the pull request; read the Codex code review and the CI on the current head |

## 15. Constraints, unresolved items and owners

| Item | Owner | State |
| :- | :- | :- |
| Codex code review findings on the pull request (addendum 2.3: no Codex security review) | PR-35 | pending |
| Hosted CI on the current head: all seven lanes, the changed-tests step, the release lane's attestation, `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; OBS-17 and O-6 if they occur | PR-35 | pending |
| Mergeability and readiness (`MERGE_PENDING`) | PR-35 | pending |
| Restart rules for any correction | PR-35 | a member change re-runs plan §6.13 from step 2; an evidence-primary change from step 3b; steps 3 to 10 byte-stable on a second pass; the attestation again |
| Merge | Nathan only | — |
| Lineage review and WU-PR-04 acceptance | the whole-change IA (PR-40) | after the merge |
| Live `--allow-prod-vendor` call | QA Plan | not this unit |
| Stale documents, OBS-P4-1 to OBS-P4-7, carried items | §12 owners | recorded |
| Downstream: WU-PR-05 refreshes from `release_id` `2f18a5eb…` and reviews the override code (S19); WU-PR-06 reads the ID-10 registrations; WU-PR-08 cuts `1.4.0` | the IA, through their instructions | contract F-1 and F-2 (§6, front matter) |
| Persistence of prompt-use provenance | Product Owner (installed writer `docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent on `main`) | pending, non-gating |

Constraints preserved throughout: closed rails; no live vendor, production or database call; no secret in any log or record; no audit sink in the repository (tests and tools used temporary sinks); no hand edit of a governed artifact; no skipped, deselected, `xfail`-marked or quarantined test; no canon, Specification or instruction edit; no PF10 addendum; no public route, Reader, payload or transport change; no admission-constant or version change.

## 16. Canon-conflict register

`CANON_CONFLICT_REGISTER`, carried unchanged:

| ID | Classification | Status | Decision owner | Record |
| :- | :- | :- | :- | :- |
| CR-1, CR-2, CR-3 | CANON_RECONCILIATION | APPROVED_AS_CHANGED | Thoth | Specification v1.1 lineage |
| CR-4 | CANON_RECONCILIATION | APPROVED | Product Owner | `docs/ephemeral/HDE-CRD-0002-WU-PR-01-po-disposition-cr-4-cr-5-v1.0.md` §2 |
| CR-5 | CANON_RECONCILIATION | APPROVED_AS_CHANGED | Product Owner | same record §3 |
| CR-6 | CANON_RECONCILIATION | APPROVED, alternative (a) | the IA through RS-20 | rescope review v1.0 §12; addendum 2.6 |
| CR-7, CR-8 | CANON_RECONCILIATION | APPROVED, alternative (a) each | Product Owner direction of 2026-10-14 | decision record §6; addendum 2.7 |

No new conflict was found during implementation. D-1 applies §7.1.11a and ID-1 as written.

## 17. Nonclaims

- The `--allow-prod-vendor` flag was not exercised live; no production environment was contacted.
- No QA verdict, acceptance, Ops, deployment, PF09 movement or closure. No QA artifact was created; `audit/qa/hde-crd-0002/` is untouched. Local CI-equivalent passes are not QA.
- No conformance claim beyond HDE-CLI-API-Vendor-Ref §7.1.11's implementation; no complete BodyGraph-resolution, broad HumanDesignAPI v2, live route or public Reader claim (plan §18).
- The DD-04 canon paragraph and every other stale passage of §12 are not edited.
- The EPIC036 and EPIC037 frozen captures stay stale as on `main` (F-5).
- WU-PR-04 is not accepted by this record or by a merge; PR-40 decides.

## 18. TypeSafe reading and surface advice for the receiving session (PR-35, WU-PR-04)

PF10 addendum 2.1 governs. Run once, before this record was saved, with the step label "PR-35 — Resolve PR Reviews and Reach Merge Readiness (HDE-CRD-0002 WU-PR-04)" and session kind `review`.

**Action sent (v8.2):** "Resolve, in a new dedicated session following an existing task list, the automated code review of one newly published and not yet reviewed pull request for one work unit of an approved change: about 65 changed paths, of which 11 are hand-edited files with about 1,300 added lines (a production vendor-override flag on one CLI command, a seven-step pre-I/O order and eight-row environment matrix in the resolver, a new audit module of about 180 lines, one new and four extended test files) and 54 are evidence paths regenerated by owner tools in a same-version release refresh. Read every review finding and thread, fix the in-scope findings locally with tests, and push coherent corrections; any change to the two release members re-runs the fixed refresh of about twelve owner-tool steps with a byte-stable second pass, a full test sweep of about 4,900 tests and an attestation build. Then verify current-head CI across seven lanes and mergeability and return readiness without merging. No live vendor, production or database call; a lineage review follows the Product Owner's merge."

**The reading, as the skill printed it:**
- **TypeSafe v8.2: Opus 5.5 at extra high.** Effort score 2.83 (confidence 0.65); rung probabilities low 0.00, medium 0.01, high 0.33, extra high 0.49, max 0.17, ultracode 0.00. Model probabilities Fable 5.1 0.06, Opus 5.5 0.94, Sonnet 5.5 0.00, Haiku 5.5 0.00 (confidence 0.92). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.001, Fable 5.1 at high 0.020, Fable 5.1 at extra high 0.029, Fable 5.1 at max 0.010, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.000, Opus 5.5 at medium 0.009, Opus 5.5 at high 0.310, Opus 5.5 at extra high 0.461, Opus 5.5 at max 0.160, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.000, Sonnet 5.5 at medium 0.000, Sonnet 5.5 at high 0.000, Sonnet 5.5 at extra high 0.000, Sonnet 5.5 at max 0.000, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Flags: boundary between high and extra high. Sent 2026-10-18T12:35:50Z. Nathan picks the cell.
- **Detail:** v8.2 sent 2026-10-18T12:35:50Z; HTTP 200 in 0.61 s; 5575 input and 71 output tokens; jev-1.13.0. Rung by rule: extra high (nearest to the score, halves up); model by rule: Opus 5.5 (the most probable of the four options, a tie going to the higher-priced model). Flags: boundary between high and extra high.

**Records:** the Notion row was not written, as PR-30 directs. Nathan's pick for PR-35: not stated. Nathan's pick for this PR-30 session: not stated (the reading for PR-30 is in plan v1.0 §21).

**Surface advice for PR-35** (execution surface only):
- **Session.** A new top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, with Notion read access for the prompt and GitHub access to the pull request; at entry it subscribes to the pull request's activity.
- **Environment, if a correction needs local re-runs.** Python 3.12 with CI's install (package-index access for `pip install`); `ruby`, `bash` and `curl` on `PATH`. All were present in this session's container. The container sets several vendor, database and GitHub keys (§2 lists the names); unset them for every local run.
- **Run times observed in this phase** (the sweep, the lanes and the changed-tests step ran concurrently on four CPUs, so each is slower than alone): full `tests/` sweep about 26 minutes; changed-tests step about 11; evidence-lane tests about 13; one refresh pass about 4 minutes; attestation build and verify about 3 minutes (12:30:38Z to 12:33:35Z).
- **Discipline.** Run any re-convergence in the branch's working tree only after member edits are committed; run every other check that can write tracked files in a detached worktree; invoke `ci/checks/*.sh` by path (F-2); run the attestation before any push that changes a member or an evidence primary (F-3).
- **Access.** No live vendor, production or database access is needed.

## 19. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / WU-PR-04 / PR-30 / result 1 (plan cycle 1), version 1.0 |
| change / specification | CRD HDE-CRD-0002 / `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` v1.1 |
| work unit | WU-PR-04 (S08, S14) |
| release | GCFPE-20261009.1 / 100926.1 |
| prompt | PR-30 — PR Implementation Proceed — 100926.1, https://app.notion.com/p/3f44590a05eb8148a538f5c80588db14 (page state as of 2026-10-12T02:30:08Z). Receiver contract read: PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1, https://app.notion.com/p/3f44590a05eb811ebf72e949b7b1572e (page state as of 2026-10-12T02:30:15Z) |
| role/stage | dedicated WU-PR-04 PR engineering session / PR-30 |
| capture time | 2026-10-18T12:57:07Z |
| execution identity | https://claude.ai/code/session_01JNmEgwAw93afByBxnV6JS8 |
| inherited usage | PR-10 instruction 1 (instruction §20); PR-20 plan 1 (plan v1.0 §22) |
| pull request and commits | amthorn78/glow-hdengine-v2#651 (https://github.com/amthorn78/glow-hdengine-v2/pull/651; open, base main, not draft); `a00cb8b`, `2336a0c`, and this record's commit |
| repository persistence | recorded here only (`docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent on `main`; pending, non-gating; owner the Product Owner) |

## 20. Next phase

PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1 (https://app.notion.com/p/3f44590a05eb811ebf72e949b7b1572e).
- **Session.** Its own new dedicated session (`session_disposition: NEW_DEDICATED`), entered from this phase's handoff, which Nathan pastes.
- **Continuity.** It continues amthorn78/glow-hdengine-v2#651 (https://github.com/amthorn78/glow-hdengine-v2/pull/651; open, base main, not draft) under the original Proceed for plan v1.0; it shares this phase's work unit, workspace, branch, pull request, instruction, plan, primary skill and recovery lineage.
- **Inputs:** this record; plan v1.0 and its companion diff; instruction v1.0; the immutable Specification v1.1, Implementation Plan v1.1 and review v1.1; PF10 as resolved at entry (addenda 2.3, 2.5 to 2.8).
- **Branch and head.** PR-35 verifies both at entry from the pull request.

## Canon relied on

Read on `main` (`docs/pfcanon/` unchanged since `b9edb0c`; this phase read canon at `6b5b3f3`, where it equals `9c82b62`).

| Topic | Sources and sections |
| :- | :- |
| Phase authority, result and handoff | PR-30 — PR Implementation Proceed — 100926.1 (read in full); PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1 (receiver contract, read in full); HDE Governance (`docs/pfcanon/PF04-Canon-HDE-Governance-v2.8.7.md`) §9.1.1 (Proceed per detailed PR plan; merges are Product Owner actions) and §9.1.2 (canon precedence over in-flight documents) |
| S14 | HDE-CLI-API-Vendor-Ref (`docs/pfcanon/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.3.md`) §7.1.11 preamble and §7.1.11a to §7.1.11f (mapped in §5 and §6; D-1 applies §7.1.11a); §3.1.1 carriers; §3.3 usage and typed errors, determinism pins; §3.4 exit codes; §4.6 (`--upsert` in prod; PD-10) |
| S08 | HDE-CLI-API-Vendor-Ref §4.5; HDE Users Guide (`docs/pfcanon/PF29-Canon-HDE-Users-Guide-v1.0.2.md`) §10.1 |
| Sink key | Glow Infrastructure (`docs/pfcanon/PF07-Canon-Glow-Infrastructure-v2.3.3.md`) §8.1 |
| Stale passages | HDE-CLI-API-Vendor-Ref §7.1.11, §7.2.0; HDE Users Guide §10.1, Recipe F, §16 |
| Overlays and carried items | PF10-HDE-Build-Notes v13.5.9 (`docs/pfcanon/PF10-HDE-Build-Notes-v13.5.9.md`): addendum 2.8; 2.3 (Rules 1–5; no Codex security review); 2.5 (LR-O1 to LR-O3, OBS-17, O-6); 2.6 (RP-2, the 22-path roster, the label-timing and stale-label rules, the step-3b order and restart point); 2.7 (AD-5 "Order" and "New base"); 2.1 (§18) |
| Route-policy statement | Plan Templates (`docs/pfcanon/PF27-Canon-Plan-Templates-v2.0.5.md`) "`bg:resolve --source vendor` route-policy posture" (plan §18, unchanged) |
| Refresh | Implementation Plan v1.1 §10; plan v1.0 §6.13; `AGENTS.md` "Release identity" and "HDE-EPIC040 admission addition" |
| In-flight documents | Specification v1.1 rows S08 and S14 and constraints; Plan v1.1 §5 (IF-1, IF-2), §7; PR instruction v1.0 (ID-1 to ID-10, contracts F-1 and F-2); plan v1.0 (all sections applied) |
| Operative documentation | `AGENTS.md` (canon-first rule; closed rails and redaction; sole Index/Mirror writer; no hand edits; pytest readiness; PR descriptions; truncation guardrail; QA output placement) |
