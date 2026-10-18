---
artifact_type: S19_CODE_SECURITY_REVIEW_RECORD
artifact_id: HDE-CRD-0002-S19-CODE-SECURITY-REVIEW
artifact_version: "1.0"
artifact_state: RECORDED
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-05
requirement: S19 (Specification v1.1; source 6(b), RA-09)
work_unit_title: "Code security review of the HDE-EPIC040 PR04 to PR06a code (PR; Distillation; S19)"
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-05-pr-instruction-v1.0.md (v1.0, INSTRUCTION_READY)
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-05-pr-implementation-plan-v1.0.md (v1.0; §5 holds the review this record transcribes)
SPECIFICATION_ID: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (v1.1, SPECIFICATION_APPROVED)
IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (v1.1)
IMPLEMENTATION_AUDIT_ID: docs/ephemeral/HDE-CRD-0002-implementation-audit-v1.0.md (v1.0; §6 S19 and Appendix B bind the review)
reviewed_head: 1e97ba9b0c9f274192385068f0b71a0e7a904fa8 (main; instruction ID-2)
head_confirmation: at the implementation base 8170cd8eb36b5e35adfab1fae9231bcd317d951c (main; #655), the 49 blob IDs equal §6, row for row (programmatic comparison); git diff 1e97ba9 8170cd8 changes only the plan and its companion diff under docs/ephemeral/
reviewer: the dedicated HDE-CRD-0002 WU-PR-05 PR engineering session, PR-20 phase (read-only review on main, with four read-only worker sessions inside it; §1 "Method")
recorded_by: the same dedicated session, PR-30 phase, from plan v1.0 §5 (instruction ID-2; plan §14)
fix_commits: d0f25b6 (source, plan §8.1); 176de33 (owner-produced same-version refresh and convergence, plan §9); on the WU-PR-05 pull request, whose result record names it
release_id_after_unit: 77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e (1.3.0, 45 members; supersedes 2f18a5eb…)
canon_conflict_register: CR-1 to CR-8 carried, all decided; no new entry
created_at: 2026-10-18T20:34:36Z
---

# HDE-CRD-0002 — S19 Code Security Review Record v1.0

This record is the S19 code security review of the HDE-EPIC040 PR04 to PR06a code: the 49 paths of Audit Appendix B, read at current bytes on `main`. It satisfies Plan v1.1 §7 WU-PR-05 deliverable "the S19 record" and instruction §10 acceptance (1) and (2).

Sections 1 to 9 are transcribed without change from plan v1.0 §5.1 to §5.9, which hold the review as PR-20 performed it. Inside them, references of the form §n, P-n, PD-n, NC-n, RK-n, D-1 and O-n or X-n point into plan v1.0. The findings tables of §4 add the Confirmed and Disposition columns. Section 10 adds what exists only after implementation: the fix commits, the regression tests, the negative controls and the run results.
## 1. Scope, reviewed head and method

- **Paths.** The 49 paths Audit Appendix B names (its prose says 48; three sidecars are written as suffixes; ID-1, OBS-W5-1). Each has a per-file line (§5.6).
- **Bytes.** Current bytes on `main` at the reviewed head `1e97ba9b0c9f274192385068f0b71a0e7a904fa8`, including what PR06b, the four CI commits of 2026-09-27 and WU-PR-01 to WU-PR-04 changed in them (§5.6 "Later changes"; instruction §5.2). The blob of each path is in §5.6.
- **Context reads.** Tests, callers and callees outside the 49 are read as proof or context and get no per-file line (ID-1).
- **What counts.** A finding is a defect located in, or reached through, code of the 49 paths; its fix may change a path outside them (ID-1). `engine/bodygraph/vendor_audit.py` is context only (LR4-O4).
- **Method.** Manual review with repository tooling only: reading, `git`, `grep`, the Python standard library and the repository's own tests and tools, under closed rails, with probes in scratch copies (Flask test client; no live vendor, production or database call). No scanner, linter or analyzer was run, installed or added (Exclusions bullet 6; addendum 2.3 Rule 3).
  - This session read 18 of the 49 paths itself (§3).
  - Four read-only worker sessions, run inside this session under one written brief (the eight-item checklist, the confirmation rule of ID-4, read-only rules, own throwaway worktrees, no write-mode generator, never the EPIC030 generator), read the other 31 in full and reported per-file results with line citations. Every worktree they used ended with an empty `git status --short --untracked-files=all` and was removed.
  - This session re-read the cited lines of every candidate it classifies and ran its own probes for every finding fixed here.
- **Limits.** Static reading plus closed-rails probes: no deployed-service, live-vendor or database behavior is observed. Platform behavior outside the repository (GitHub path-filter limits, Railway configuration, branch protection) is not observable. Race conditions were reasoned from code, not run.

## 2. Severity scale (instruction ID-4)

| Level | Criterion |
| :- | :- |
| High | Exploitable now by an unauthenticated network client against the production application, with a secret, PII, write or vendor-call consequence |
| Medium | Reachable now on the production application by an unauthenticated client and violating a canon security or error-contract requirement, without a secret, PII, write or vendor consequence; or a production-mounted surface whose only control against such a consequence is a check that does not meet canon |
| Low | Reachable only by an operator, a CI job or a local user (CLI, tools, dev, test or local deployments), or only after a further misconfiguration; consequence limited to integrity of local or governed evidence, refusal-code accuracy or defence in depth |
| Informational | No reachable exposure found; a latent pattern, or a deviation from canon wording without effect |

## 3. Threat checklist

The eight items of Audit §6 S19, mapped to canon exactly as instruction §4.1 maps them: T1 input bounds and body limits; T2 path and file handling; T3 environment gating and rails; T4 secret and keys-only logging; T5 error disclosure; T6 injection into audit or log lines; T7 concurrency and atomic publication for the evidence writers; T8 dependency and subprocess use. Where canon is silent the line states the observed behavior and judges the risk; silence is not a finding by itself. For T7 canon names no general atomic-replace rule for evidence writers, so each writer's actual behavior is stated.

Canon map (instruction §4.1, as instruction §16 records it read):

| # | Checklist item | Governing canon on `main` (read for this instruction) |
| :- | :- | :- |
| T1 | Input bounds and body limits | HDE-CLI-API-Vendor-Ref §5.5 "Validation and environment gating" (reject invalid or empty ids before resolution; exact compat namespace); §5.11.3 (sampler body validated by the writer JSON helpers; typed errors); §7.1.11a (the authorization reference's bounds); §7.1.10 "Configured-base boundary" (absolute HTTPS, host, no userinfo, query or fragment) |
| T2 | Path and file handling | HDE Schemas & Artifacts §6.2.1 (the attestation builder refuses a symlinked output root, an output inside the repository, a non-directory or non-empty destination, or an overwrite); HDE Mechanics Guide §27.1 (manifest entries use safe repository-relative POSIX paths, no parent traversal, no unsafe symlink source) and §27.3 (the builder refuses an output inside the repository and leaves the checkout byte-stable); Glow QA Guide §9.2.4, the `EVIDENCE_PATHS_VALIDATED_OK` QA definition (Index and Mirror records reference only safe, in-repository paths); HDE Users Guide §6.1 ("a and b must point to safe, complete mapped chart files under fixtures/charts"; the dev `GET /reader` query parameters, read by `_safe_load_chart`) |
| T3 | Environment gating and rails | HDE Governance §2.0.10 `ENV_RAILS_POLICY_OK`, including "Dev/admin APP_ENV gating" (exactly `{"dev","test","local"}`; missing, empty or other values fail closed without default) and the same rule in §4.1.4 "Dev/admin APP_ENV gating (dev/test/local only)"; §3.1 "SAFE rails default ON", "Public traffic (Reader/Aux)", "Admin ops windows (vendor override)"; HDE Architecture §1.3 "Separation of surfaces", §3.2 "A7 proof surface" ("Non-prod entries must be unreachable in production"), §3.3 "Gating & posture" ("Harness is dev-only; never mounted in production") and "Current repository discrepancy", §3.5 "Adopted routes" and "Current repository discrepancy"; HDE-CLI-API-Vendor-Ref §5.4 "Gate" ("must not be mounted in production builds or non-dev deploys"), §5.5, §5.6 transport table, §5.11.2 ("exactly one of `dev`, `test`, or `local`"), §7.1.1 to §7.1.11; HDE Mechanics Guide §22 and §34; Glow Infrastructure §2.4 "Production — Railway" (production `SAFE_MODE=0`, `ALLOW_NETWORK=1`, `APP_ENV=prod`) |
| T4 | Secret and keys-only logging | HDE Governance §7.1 "Keys-only logging" and §8.2 "No PII or secrets in logs"; HDE-CLI-API-Vendor-Ref §5.4 "Hygiene and logs" and §7.1.11f exclusions; `AGENTS.md` redaction rule |
| T5 | Error disclosure | HDE-CLI-API-Vendor-Ref §8.1 ("HTTP error envelopes must not echo payloads, secrets, stack traces, or vendor bodies") and §5.2 by reference; HDE Governance §8.1.2 "Typed errors" and §6.3.2 (diagnostics keys-only; no stack traces); HDE Architecture §1.3 "No leakage across boundaries" |
| T6 | Injection into audit or log lines | HDE Governance §7.1.4 "Determinism and formatting" and §8.2.3 "Structured log shape tests"; HDE-CLI-API-Vendor-Ref §7.1.11f (CR/LF and delimiter sanitization) and §3.3 CRLF guards on stdout |
| T7 | Concurrency and atomic publication for the evidence writers | `AGENTS.md` "Evidence harness" (the updater is the sole Index/Mirror writer, one convergent transaction) and "never hand-edit governed artifacts"; HDE Schemas & Artifacts §8.3 "Field order and write discipline (merge-blocking)" and §8.6.1; §6.2.1 and HDE Mechanics Guide §27.3 (attestation). Canon names no general atomic-replace rule for evidence writers; the review states each writer's actual behavior. Runtime concurrency fact: the production command runs `gunicorn` with `--workers 2 --threads 4` (`Procfile`) |
| T8 | Dependency and subprocess use | HDE Mechanics Guide §27.3 (no raw subprocess output retained in attestation content); HDE Schemas & Artifacts §8.11 SBOM (optional); Specification Exclusions bullet 6 and Plan acceptance (3) (no new tooling or dependency) |

## 4. Findings

**Confirmed, fixed here** (instruction ID-5 (a) to (f) hold for each):

| ID | File and line at `1e97ba9` | Description | Item | Severity | Confirmed | Canon or requirement | Evidence | Disposition | Live QA class (surface) |
| :- | :- | :- | :- | :- | :- | :- | :- | :- | :- |
| S19-F01 | `adapter/http_reader.py` 485–491 (`_parse_reader_post_body`), 175–178 (`_read_writer_json`); `engine/http/compat_handler.py` 132 (`post_json`) | A JSON body nested past the parser's recursion limit raises `RecursionError`, which no handler catches: the production `POST /api/reader` (unauthenticated) answers 500 `text/html` with no `no-store` and a logged traceback; the writer helper and compat `POST` do the same on their surfaces | T1, T5 | Medium | Confirmed | HDE-CLI-API-Vendor-Ref §5.2 item 1 (every governed HTTP error emits `error_v1`), §5.2.3 table (invalid JSON → `ERR_READER_INVALID_INPUT` 422), §8.1 | P-1; NC-01 to NC-03 | Fixed here: source commit `d0f25b6` (design: plan §7); regression tests `test_s19_*` in `tests/http/test_reader_post_v1.py`, `tests/http/test_reader_post_v2.py`, `tests/transport/test_writers_errors_headers.py`, `tests/http/test_compat_endpoint_contract.py`; negative controls NC-01, NC-02, NC-03 (each fails with the fix disabled) | Functional-feature: the production application that serves Reader v1 and v2 |
| S19-F02 | `adapter/http_reader.py` 826–832 (`_dev_admin_gate`); `engine/cli/main.py` 832–835 (`_ensure_dev_admin_env`) | The dev/admin `APP_ENV` gates normalize: the HTTP gate trims and case-folds (admits ` dev`, `DEV`, `TEST `), the CLI gate case-folds (admits `DEV`, `Dev`, `TEST`). Named input gap 3 | T3 | Low | Confirmed | HDE Governance §2.0.10 `ENV_RAILS_POLICY_OK` and "Dev/admin APP_ENV gating" ("exactly"); HDE-CLI-API-Vendor-Ref §5.11.2 ("exactly one of dev, test, or local"), §5.12 | P-4, P-5; NC-04, NC-05 | Fixed here: source commit `d0f25b6` (design: plan §7); regression tests `test_s19_*` in `tests/http/test_dev_conjunction_http.py`, `tests/cli/test_cli_usage_and_errors.py`; negative controls NC-04, NC-05 (each fails with the fix disabled) | Functional-feature: the production application (the routes are mounted there) and the operator CLI surface |
| S19-F03 | `adapter/factory.py` 13; `adapter/http_reader.py` 1176 and the routes at 606–678, 756–820, 987–1078, 1123–1168; `adapter/wsgi.py` 23 | The production application mounts the dev harness (`GET`/`HEAD /reader`, `POST /internal/dev/sampler`, the three `/dev/*/conjunction` routes) and the three canon-retired `/ops` routes. Today, unauthenticated: `/ops/probe/env` returns the process id, its start time, the `SAFE_MODE`, `ALLOW_NETWORK` and `APP_ENV` values and whether a probe token exists; the harness code (fixture reads, Engine evaluation, vendor acquisition under the production open rails, idempotence writes) is reachable code behind one request-time check that S19-F02 shows does not meet canon; the retired writer checks bearers against test-token environment values. Named inputs gaps 1 and 2 | T3, T5 | Medium | Confirmed | HDE Architecture §3.2 "A7 proof surface" ("Non-prod entries must be unreachable in production"), §3.3 "Gating & posture" ("Harness is dev-only; never mounted in production") and "Current repository discrepancy", §3.5 "Current repository discrepancy" (`RETIRED/NONCANONICAL`), §1.3 "No leakage across boundaries"; HDE-CLI-API-Vendor-Ref §5.4 "Gate" ("must not be mounted in production builds"), §5.12 ("MUST NOT be available in production"); HDE Users Guide §1.1 ("Do not use as an operator workflow"); HDE Governance `BG_VENDOR_CALLS_DISABLED_IN_PROD_OK`; addendum 2.7 AD-4 | P-4, P-10, P-14; NC-06, NC-17, NC-18 | Fixed here: source commit `d0f25b6` (design: plan §7); regression tests `test_s19_*` in `tests/http/test_endpoint_catalog.py`; negative controls NC-06, NC-17, NC-18 (each fails with the fix disabled) | Functional-feature: the production application |
| S19-F04 | `adapter/http_reader.py` 155 | The writer JSON helper reads the whole body before its 32 KiB check when `Content-Length` is absent (a chunked request; werkzeug returns the raw stream when `wsgi.input_terminated` is set, as gunicorn sets it). Reached by the dev sampler after its gate and the retired writer after authentication; after S19-F03 neither handler is reachable in production | T1 | Low | Confirmed | the writer limit (`ERR_WRITER_REQUEST_TOO_LARGE`, "request body exceeds 32 KiB"; HDE-CLI-API-Vendor-Ref §5.11.3 "writer JSON helpers") | test with a counting stream; NC-07 | Fixed here: source commit `d0f25b6` (design: plan §7); regression tests `test_s19_*` in `tests/transport/test_writers_errors_headers.py`; negative controls NC-07 (each fails with the fix disabled) | Functional-feature: the production application module |
| S19-F05 | `engine/bodygraph/resolver.py` 126–133, 174–175, 923–925; `engine/bodygraph/ingest.py` 56–61, 144–145 | The resolver and the ingest read the rails leniently: `SAFE_MODE` closes only for `1`/`true`/`yes`/`on` (unset, empty, `2`, `false` count as open) and `ALLOW_NETWORK` opens for `true`/`yes`/`on`. The production-override matrix, its audit events and credential projection then run under rails canon treats as closed; only the socket layer's exact check prevents I/O | T3 | Low | Confirmed | HDE-CLI-API-Vendor-Ref §7.1.2 (two-gate rule: exactly `SAFE_MODE=0` and `ALLOW_NETWORK=1`), §7.1.3, §7.1.11d (rails first); HDE Governance §3.1 "SAFE rails default ON" | P-2; NC-08, NC-09 | Fixed here: source commit `d0f25b6` (design: plan §7); regression tests `test_s19_*` in `tests/bodygraph/test_resolver_vendor.py`, `tests/bodygraph/test_ingest.py`; negative controls NC-08, NC-09 (each fails with the fix disabled) | Functional-feature with the mandatory live vendor call: vendor ingest through `hdctl bg:resolve --source vendor` (the S14 class) |
| S19-F06 | `engine/bodygraph/ingest.py` 50–52, 138–139; `engine/bodygraph/resolver.py` 446–451, 461 | Vendor runs append to the tracked governed files `artifacts/ingest/retry_trace.log` and `artifacts/ingest/ingest_success.log`, resolved against the working directory: the non-production legacy call uses the ingest defaults, the production-override path passes `log_path=RETRY_LOG` | T7, T2 | Low | Confirmed | `AGENTS.md` (governed evidence produced only by its owners; no hand edits); the repository's own posture (`tests/evidence/test_open_rails_abba_proof.py` treats them as governed logs a live run must not change); HDE Engine Epics Map lists them as EPIC-011 evidence | P-3; NC-10, NC-11 | Fixed here: source commit `d0f25b6` (design: plan §7); regression tests `test_s19_*` in `tests/bodygraph/test_resolver_vendor.py`, `tests/bodygraph/test_ingest.py`; negative controls NC-10, NC-11 (each fails with the fix disabled) | Functional-feature with the mandatory live vendor call (vendor ingest) |
| S19-F07 | `engine/cli/main.py` 324–326 (catch-all), 220–223, 331–334, 883–886, 949–952 | An unexpected CLI failure writes `CLI_UNEXPECTED:<exception text>` to stderr; JSON nested past the recursion limit (stdin, pair file, party files, candidates, viewer preferences) and undecodable input reach it | T5, T1 | Low | Confirmed | HDE-CLI-API-Vendor-Ref §3.3 and §8.2 (one LF-terminated code token on stderr) | P-6; NC-12, NC-13 | Fixed here: source commit `d0f25b6` (design: plan §7); regression tests `test_s19_*` in `tests/cli/test_cli_usage_and_errors.py`, `tests/cli/test_cli_file_inputs.py`; negative controls NC-12, NC-13 (each fails with the fix disabled) | Functional-feature: the operator CLI surface |
| S19-F08 | `engine/config/registry_loader.py` 1076–1079 (rule), 1083–1087 (messages); `scripts/cut_release_manifest.py` 61–71 (rule), 146, 168 (messages) | The manifest path rules admit control characters, NUL included, and a refused path can be echoed raw into a message or stderr line (line injection). Admission's exact roster check refuses such a path before any file is opened; `load_manifest` (used by `scripts/release_id_recompute.py`) and the cutter accept it | T2, T6 | Low | Confirmed | HDE Math Spec §5.4.3 ("no … NUL"); HDE Governance §7.1.4 (log-line determinism) | worker probe (in-memory `_parse_manifest`; cutter `--check` on a crafted manifest printed a forged line); NC-14, NC-15 | Fixed here: source commit `d0f25b6` (design: plan §7); regression tests `test_s19_*` in `tests/config/test_manifest_schema.py`, `tests/scripts/test_cut_release_manifest.py`; negative controls NC-14, NC-15 (each fails with the fix disabled) | Loader: functional-feature (release admission in the production application); cutter: not production-affecting (release tooling) |
| S19-F09 | `tools/config/generate_config_artifacts.py` 322 vs `tools/config/artifacts.py` 471 | The golden-comparison `--report` refusal compares the report with the candidate root resolved through symlinks, while admission uses the lexical absolute path; a `<symlink>/..` candidate argument lets the report land inside the admitted root | T2 | Low | Confirmed | HDE Mechanics Guide §25.6 and HDE Users Guide §7.6 ("`--report` writes only … outside both repository and candidate root"); `AGENTS.md` "HDE-EPIC040 current posture" | worker probe at the validator; NC-16 | Fixed here: source commit `d0f25b6` (design: plan §7); regression tests `test_s19_*` in `tests/config/test_config_artifacts.py`; negative controls NC-16 (each fails with the fix disabled) | Not production-affecting (read-only repository tooling) |

**Confirmed, routed** (instruction ID-5: at least one of (a) to (d) fails, or the item lies in a frozen family; the owner decides):

| ID | File and line | Description | Item | Severity | Confirmed | Disposition | Reason |
| :- | :- | :- | :- | :- | :- | :- | :- |
| S19-R01 (OBS-W4-1) | `engine/cli/main.py` 747–753, 788–799; `engine/bodygraph/resolver.py` 905–1021 | `hdctl showcompat --source vendor`, and conjunction mode with any source but `db` or `auto`, acquire from the vendor under open rails with no production override, audit event or production gate. Production rails are open by default (Glow Infrastructure §2.4), so any production shell reaches it | T3 | Low | Confirmed | Routed to Product Owner (owner of HDE-CLI-API-Vendor-Ref) | ID-5 (a) and ID-7: §7.1.11a scopes the override to `bg:resolve`; `BG_VENDOR_CALLS_DISABLED_IN_PROD_OK` admits CLI runs under explicit open-rails profiles; a gate would set policy canon does not state. Decision needed: whether production showcompat and conjunction acquisition must meet a production gate |
| S19-R02 (OBS-W4-3) | `engine/bodygraph/resolver.py` 676–694 → `engine/bodygraph/vendor_client.py` 100–153 | Route selection reads any path segment, case-insensitively, as the version: a nonterminal `v2` selects `charts` with the Bearer key; an unversioned or `v3` base selects legacy `bodygraphs` with the `HD-Api-Key` credential projected; userinfo, query and fragment are not refused | T1, T3 | Low | Confirmed | Routed to Product Owner | ID-7: a §7.1.10 fix reverses the posture that tests pin (`tests/bodygraph/test_hde_epic038_mapped_cache_smoke.py` line 118 asserts the legacy fallback for an unversioned and a `v3` base; `tests/bodygraph/test_bg_resolve_route_policy.py` line 86; `tests/bodygraph/test_bg_resolve_v2_mapped_cache.py` line 237), that the governed EPIC038 evidence predicate `explicit_legacy_fallback` records (`tools/evidence/generate_v2_mapped_cache_evidence.py` line 275) and that `AGENTS.md` "EPIC036 docs posture", HDE Mechanics Guide §1.1 and HDE Users Guide §11.3 state; the frozen EPIC036 and EPIC037 captures would contradict it. The fix needs the Product Owner's decision on retiring that posture, with evidence and test owners |
| S19-R03 | `engine/http/compat_handler.py` 130–173 | `POST /api/compat/v1` returns the internal numeric result with no authentication; canon describes the success body as "after the production-excluding environment gate and internal authentication". Production answers 404 through the compat guard; a reachable non-production deployment (Glow Infrastructure §2.2 Staging/QA) would serve stored-UID results unauthenticated | T3 | Low | Confirmed | Routed to Product Owner | ID-5 (a): canon names no compat authentication mechanism (credential, scope or registry), so a fix would set policy |
| S19-R04 | `tools/errors/generate_error_artifacts.py` 319–320; `tools/evidence/generate_epic030_pr05_category_framework_evidence.py` 243; `tools/evidence/run_sanity_pipeline_gate.py` 106 | Governed owner tools without argument parsing act on any invocation, `--help` included: the error-artifact generator rewrites tracked files, the release member `errors/token_map/token_map.json` among them, with truncate-then-write; the EPIC030 generator rewrites three frozen logs with wall-clock times and a different category order (OBS-W5-3); the sanity gate runs the canonical write pipeline | T7 | Low | Confirmed | Routed to Product Owner | ID-5 (a) and (d): each fix changes an owner tool's invocation contract, which no canon rule sets; the EPIC030 family is frozen and its regeneration belongs to its owner. Operator and CI-runner reach only |
| S19-R05 | `tools/evidence/run_sanity_pipeline.py` 333, 347; `tools/evidence/build_release_attestation.py` 178–191, 603–617, 907–912 | Unrestricted or non-exclusive write targets: `--log-path` follows symlinks and can overwrite a governed file; the attestation builder accepts any existing empty output root, follows symlinks on later writes and, on failure, removes `evidence/` and bundle files it did not create (a concurrent run's bundle was destroyed in the worker's probe) | T2, T7 | Low | Confirmed | Routed to Product Owner (owner of HDE Schemas & Artifacts §6.2.1 and HDE Mechanics Guide §27.3) | ID-5 (a): canon accepts an empty existing destination; exclusivity and ownership rules for the output root are an owner contract decision. Operator only; CI uses a fresh `$RUNNER_TEMP` path |
| S19-R06 | `tools/cli/generate_showcompat_artifacts.py` 104–109 | The frozen-family generator runs the relative `scripts/hdctl.py` with no `cwd`: run from another directory, it executes that directory's file with the full environment | T8 | Low | Confirmed | Routed to Product Owner (owner of the frozen `artifacts/cli/**` family) | ID-5 (d): the tool belongs to a frozen family (instruction §6); its governed callers pass `cwd=ROOT` |
| S19-R07 | `tools/evidence/run_canonical_json_gate.py` 1205 | A failing target validation records `validation_error:<type>:<exception text>` in the governed check rows, absolute local paths included, and write mode publishes them | T5 | Low | Confirmed | Routed to Product Owner (owner of HDE Governance §6.3.2 diagnostics rules) | ID-5 (a): the content rule for gate diagnostics is the owner's; reached only by a failing operator or CI run |

Every confirmed finding has a disposition: fixed here, with a regression test and a recorded negative control, or routed with an owner and a reason. Not-confirmed items are in §6 and §8 (instruction ID-4).

## 5. Named inputs (instruction ID-6 and ID-7)

| Input | Canon basis | Evidence | Classification (ID-4) | Disposition (ID-5) |
| :- | :- | :- | :- | :- |
| Gap 1 — production mount of the dev harness and the `POST /reader` stub | HDE Architecture §3.2, §3.3 and its "Current repository discrepancy"; HDE-CLI-API-Vendor-Ref §5.4 "Gate", §5.12 | P-4; instruction §5.3 | Confirmed, part of S19-F03 | Fixed here (D-1). The stub stays: HDE-CLI-API-Vendor-Ref §5.4 "Production mount" and HDE Users Guide §6.4 state it as the production refusal (PD-2) |
| Gap 2 — the three canon-retired `/ops` routes, mounted and ungated in production | HDE Architecture §3.5 "Current repository discrepancy"; HDE Users Guide §1.1 | P-4 (`/ops/probe/env` 200 with process and rails state) | Confirmed, part of S19-F03 | Fixed here: in a production-like posture answered as an unknown path (the governed 404) before any handler; code kept (removal stays with its canon owner) |
| Gap 3 — `_dev_admin_gate` normalizes | HDE Governance "Dev/admin APP_ENV gating"; HDE-CLI-API-Vendor-Ref §5.11.2 | P-4 | Confirmed, S19-F02 (with the CLI gate) | Fixed here: exact comparison; refusal matrix of instruction ID-6 |
| Gap 4 — `adapter/http_reader.py::create_app`'s after-request hook never matches (`getattr(resp, "request", None)` is `None`) | none (no canon names the hook) | P-7: no `/internal/` ETag and the diagnostic 204/405 already carry `Content-Length: 0` | Not confirmed as a security finding (no observable effect). Non-security defect: dead code | Observation O-01 (§5.7); not fixed here (ID-4) |
| OBS-P3-3 — `adapter/wsgi.py`'s 405 emits no `Allow` | none in canon for this factory (RFC 9110 requires `Allow` on a 405) | P-8 | Not confirmed: `adapter/wsgi.py` is not the production factory; no exposure | Observation O-02 |
| OBS-P3-14 — `python-dotenv` would let `Flask.run` read a local `.env` | addendum 2.7 AD-3 (the runner's run-call arguments) | absent from `requirements*.txt` and CI's install; no `.env` or `.flaskenv` tracked; present only in this container's system Python, not in the CI-equivalent venv | Not confirmed | none |
| OBS-P3-17 — root helpers run the production factory with the debugger and reloader | HDE Architecture §3.8.1 "Current repository discrepancy" | `run_flask.py`, `run_flask_dev.sh` (outside the 49) | The part reached through `adapter/factory.py` is gap 1, fixed by D-1 (under a production-like `APP_ENV` no harness handler is reachable there either); the helpers' own settings are out of scope | Out-of-scope observation X-02 (§5.8) |
| OBS-W4-1 | HDE-CLI-API-Vendor-Ref §7.1.11a; HDE Governance `BG_VENDOR_CALLS_DISABLED_IN_PROD_OK` | §5.4 R01 | Confirmed (realistic exposure path under T3) | Routed: S19-R01 |
| OBS-W4-3 | HDE-CLI-API-Vendor-Ref §7.1.10 and §7.2.0 | §5.4 R02 | Confirmed (violates §7.1.10) | Routed: S19-R02 |

## 6. Per-file lines (49)

Columns: attribution (merged by; later changes as instruction §5.1 lists them); member of the release (M); items that apply; what was read; result. "n/a" items are stated in the line.

| # | Path (blob at `1e97ba9`) | Attribution; M | Items | Read | Result |
| :- | :- | :- | :- | :- | :- |
| 1 | `.github/workflows/ci.yml` (`3836bad11c39`) | #467; 398276b, 735af8a, #627; no | T6, T8; T2 ($RUNNER_TEMP paths only); T4 (no secret referenced); T1, T5, T7 n/a (orchestration) | whole file; the classifier; the pin test | No finding. `pull_request` (not `_target`); `contents: read`; `persist-credentials: false`; the only `${{ }}` inside `run:` is `github.event_name`; no cache; changed paths reach the shell only through a quoted array. Not confirmed: CI1 (GitHub path-filter limits), CI3 (actions pinned by tag; `setuptools`/`wheel` unpinned) — observations O-11, O-12 |
| 2 | `adapter/factory.py` (`618a624dc4d4`) | #508; #643; no | T3, T5; T1, T2, T4, T6–T8 n/a (registration and error handlers only) | whole file | S19-F03 (line 13, the mount; the fix lives in the blueprint and this file is unchanged). Error handlers emit the governed envelope (S02) |
| 3 | `adapter/http_reader.py` (`a26feb9b48f4`) | #467, #508; #643, #646; M | T1–T6; T7, T8 n/a (no evidence writer, no subprocess) | whole file | S19-F01 (485–491, 175–178), S19-F02 (826–832), S19-F03, S19-F04 (155). Not confirmed: `_safe_load_chart` (resolve then prefix check; both refusals map to `ERR_READER_INVALID_PATH`, no existence oracle; the `is_symlink()` after `resolve` is dead, O-03); `_require_admin_scope` compares test tokens with `==` (dev-only after S19-F03; O-04); conjunction errors echo `provider_details` such as `str(URLError)` (dev-only after S19-F03; no secret content; X-04); the aux route reflects no query value (P-9). Gap 4 hook (O-01) |
| 4 | `adapter/schemas/error_v1.schema.json` (`720aa6738466`) | #501; M | T1, T5; others n/a (static contract) | whole file; its consumers | No finding. `details: {}` accepts any object (SC1); no leak found through it; observation O-13 |
| 5 | `adapter/wsgi.py` (`52fd4aedf1a9`) | #508; no | T3, T5 | whole file | S19-F03 (line 23, same mount; file unchanged). OBS-P3-3 (O-02). HSTS header decision normalizes `APP_ENV`, which only widens a header; no finding |
| 6 | `catalog/manifest.json` (`80364154c776`) | #467, #501, #508; #513, #643, #646, #651; identity source | T2 | whole file; `git ls-files -s` modes | No finding. Canonical bytes; 45 safe repository-relative POSIX paths, all mode `100644`, hashes and sizes equal to disk |
| 7 | `ci/checks/classify_ci_changes.py` (`3be620cbac91`) | all four; e1bff8d, 398276b, 2876fa0, 735af8a, #627, #643, #651; no | T1, T2, T6, T8; T3–T5, T7 n/a | 1–340, 960–1140, 1522–2055 read; registry tables skimmed | No finding. `git diff -z` with list argv; strict UTF-8; NUL/CR/LF, absolute and `..` paths refused; unknown surfaces fail closed (exit 2); `$GITHUB_OUTPUT` gets fixed keys only. CI2 (workflow filter's governed exceptions hard-coded): observation O-14 |
| 8 | `ci/checks/run_rails_job_definitions.py` (`ce25809df3e7`) | #467; no | T4, T6, T8; T3 (exact rails values) | whole file; `ci/jobs/*.yml` | No finding. List argv matched against an allowlist; credential-bearing arguments refused. Not confirmed: RR1, children inherit names outside its 8-name strip list under open rails (no path to I/O or output found; CI sets none; O-15); RR2 `python` from `PATH` |
| 9 | `ci/jobs/rails_open_conformance.yml` (`b1d3f056b3e4`) | #467; no | T3, T8 | whole file | No finding. Open rails for two allowlisted commands; no credential keys |
| 10 | `engine/bodygraph/ingest.py` (`68fb7b4a7d0a`) | #467; no | T2, T3, T4, T6, T7 | whole file | S19-F05 (56–61, 144–145), S19-F06 (50–52, 138–139). Log lines are `json.dumps` (no injection); content keys-only (`user_id` is a UUID or a UUID5) |
| 11 | `engine/bodygraph/mapped_cache.py` (`8741137ba14a`) | #467; M | T1, T5; T3, T4 | whole file | No finding. Parameterized SQL with fixed table names; value-free typed errors; read-back parity |
| 12 | `engine/bodygraph/projection.py` (`e28c47d8ee02`) | #467; M | T1, T5 | validators and `project_bodygraph` | No finding. Exact key sets, typed refusals; recursion depth bounded by its callers' JSON parse (S19-F01 covers the parse) |
| 13 | `engine/bodygraph/resolver.py` (`c3550c066094`) | #467; #651; M | T1–T6 | `resolve_bodygraph`, `_resolve_vendor`, `_resolve_vendor_route`, `_resolve_vendor_v2_chart`, `_vendor_config_env`, `_classify_env_route_policy`, `_acquire_dry_run`, `_resolve_stored` (lines 126–490, 617–735, 905–1072); the WU-PR-04 override steps 4 to 7 and event calls (LR4-O4) | S19-F05, S19-F06; R01 (905–1021), R02 (676–694). The override code: no further finding (the WU-PR-04 chain reviewed `vendor_audit.py`; LR4-O4) |
| 14 | `engine/bodygraph/v2_adapter.py` (`447243305d5e`) | #467; M | T1, T4, T5 | `adapt_v2_chart_payload` and validators | No finding. Pure mapping; no raw payload retained; typed refusals |
| 15 | `engine/cli/main.py` (`7761834a6100`) | #467; #643, #651; M | T1–T6 | `cli`, the pre-scan (WU-PR-04), `bg_resolve`, showcompat sources, file loaders, `_ensure_dev_admin_env`, dev sampler | S19-F02 (832–835), S19-F07; R01. `--dump-reader` and `--dump-admin-dir` write operator-chosen paths (operator surface; no finding) |
| 16 | `engine/compat/compute.py` (`77e311800838`) | #467; M | T1, T3, T5 | header, `evaluate_pair`, conjunction carriers (1–68, 300–470) | No finding. Its `source_policy="vendor"` default is reached by R01's paths; admission per evaluation costs about 0.3 s (worker measure; availability observation O-16) |
| 17 | `engine/compat/error_tokens.py` (`32f013d484e6`) | #467; M | T5 | whole file | No finding. Static messages; value-free boundary errors. The alias `forbidden` maps to two tokens (O-05) |
| 18 | `engine/config/__init__.py` (`aef7a0206c09`) | #467; no | all n/a (re-exports; lazy import by fixed names) | whole file | No finding |
| 19 | `engine/config/registry_loader.py` (`d7e9496d96d0`) | #508; #513; M | T1, T2, T5, T6, T7 | whole file (worker); 1030–1110 (this session) | S19-F08 (1076–1087). Not confirmed: unbounded manifest read before its size check for an operator-chosen candidate root (RL3), schema recursion (RL2). No TOCTOU between hash and parse; no-follow descriptors; thread-safe (no shared mutable state) |
| 20 | `engine/emit_public.py` (`4fdcd8d94517`) | #467; #643; no | T5 | whole file | No finding |
| 21 | `engine/http/compat_handler.py` (`42d0e7f9bfc6`) | #467; M | T1, T3, T5 | whole file | S19-F01 (132); R03. The production guard follows HDE-CLI-API-Vendor-Ref §5.5 exactly (exact namespace; trimmed, case-folded production posture); no body limit on the dev-only route (not confirmed: no canon bound, loopback runner) |
| 22 | `engine/runtime/public.py` (`df33eab7d8f4`) | #467, #508; M | T5 | whole file | No finding. Bands-only projection with closed key sets |
| 23 | `errors/token_map/token_map.json` (`7a5b2df0125f`) | #467, #501; M | T5 | whole file; its producer | No finding. 30 static messages |
| 24 | `errors/token_map/token_map.json.path_proof.txt` (`30822f401b73`) | #467, #501; no | T7 (binding) | whole file; the updater's proof writer | No finding. Binds path, size 2,982 and sha256 `a218f515…`, both equal; written by the updater |
| 25 | `presenter/reader_v1/emitter.py` (`4a9f1bacbd72`) | #508; M | T5 | whole file | No finding. Exactly `{id, band}` items; duplicates refused |
| 26 | `schemas/reader.v1.schema.json` (`a91843f13c20`) | #501, #508; #513; M | T1, T5 | whole file | No finding. Closed objects; constant codes |
| 27 | `schemas/reader.v1.schema.json.sha256` (`e8ef6ca434c2`) | #501, #508; #513; no | T7 (binding) | whole file | No finding. Matches the schema bytes; validated by `tests/reader_v1/test_schema.py` |
| 28 | `schemas/reader.v2.schema.json` (`7803e9a63009`) | #508; M | T1, T5 | whole file | No finding. Exactly ten ordered items |
| 29 | `schemas/reader.v2.schema.json.sha256` (`0a39e26325c2`) | #508; no | T7 (binding) | whole file | No finding. Matches |
| 30 | `scripts/cut_release_manifest.py` (`f87ef35c396d`) | #501; no | T2, T3, T6, T7 | whole file | S19-F08 (61–71, 146, 168). Closed rails required; resolved paths stay inside the repository; standalone write is non-atomic (the coordinating owner publishes atomically; O-17) |
| 31 | `scripts/make_reader_v1_goldens.py` (`9bb05d6dc503`) | #508; #513; no | T2, T7 | whole file | No finding. Writes at import time to fixed paths (O-18) |
| 32 | `scripts/make_release_pack.sh` (`6ea1acf4ffc1`) | #508; no | T2, T6, T7 | whole file | No finding. Quoted heredoc. Its `artifacts/release_id.txt` (`8ca9ba71…`) is not the canonical `release_id` and `scripts/hd_cli.py` reads it (naming drift; O-19) |
| 33 | `tools/bodygraph/check_magic10_gate_readiness.py` (`50fbc78f77e0`) | #492; M | T1–T5, T7 | whole file | No finding. Refuses outside closed rails before any provider; writes nothing (no `--report` option); one fixed parameterized `SELECT`; selection file bounded to 1 MiB, symlink and FIFO refused. Not confirmed: it connects to `DATABASE_URL` under closed rails (by design, HDE Mechanics Guide §25.6), not in a read-only session (O-20) |
| 34 | `tools/cli/generate_cli_conformance_artifacts.py` (`54db49d57b0a`) | #467; no | T3, T4, T7, T8 | whole file | No finding. Children inherit the environment (closed rails, `APP_ENV=test`); captured outputs are tokens and help text; not confirmed as exposure (GCC1; O-15). `--check` read-only |
| 35 | `tools/cli/generate_showcompat_artifacts.py` (`9ef2f0b818e9`) | #467; no | T3, T4, T7, T8 | whole file | R06 (104–109). `--check` read-only |
| 36 | `tools/config/artifacts.py` (`c8b702fefaee`) | #492, #501; no | T1, T2, T3, T5, T7 | whole file | No finding of its own (S19-F09's admitted root is at 471). Goldens read bounded to 1 MiB with no-follow; the report's exception text could carry a host path (ART1, not confirmed; O-21) |
| 37 | `tools/config/generate_config_artifacts.py` (`402c60206398`) | #492, #501; no | T1, T2, T3, T5, T7 | whole file | S19-F09 (322). Not confirmed: re-check before the report write (GCA2), linked-worktree reading of "repository" (GCA3), case-insensitive file systems (GCA4); no-argument run writes three governed artifacts, as HDE Users Guide warns |
| 38 | `tools/errors/generate_error_artifacts.py` (`ea1e1110578e`) | #501; no | T3, T4, T7, T8 | whole file | R04 (319–320). Children inherit the environment under forced closed rails with the database forced unavailable (GEA2, not confirmed; O-15) |
| 39 | `tools/evidence/build_release_attestation.py` (`edcdd517aa87`) | #467; #634; no | T2, T4, T5, T7, T8 | whole file | R05. Holds as canon states: refusals before writes (symlinked root, inside the source, non-directory, non-empty); child environment allowlist (`PATH`, `TMPDIR`, closed rails, `HDE_*`); no shell; no raw subprocess output retained. Not confirmed: skip-worktree defeats the clean check (BRA3; deliberate operator act; O-22); `--source` other than the running checkout lets a failure receipt land in the running checkout (BRA2; O-22) |
| 40 | `tools/evidence/generate_a7_transport_proofs.py` (`b5f71b9c704d`) | #467, #508; #643, #646; no | T2, T3, T7 | whole file | No finding. `APP_ENV` restored in `finally`; write gated by `HDE_WRITE_A7_PROOFS=1`. The env-gate proof is fixed text from one `prod` probe (A7-1; evidence strength, O-23); twelve sequential writes, one through the tracked symlink `docs/ENDPOINTS_CATALOG.json` (by design) |
| 41 | `tools/evidence/generate_conjunction_writer_evidence.py` (`ad8d812ed29d`) | #508; no | T2, T3, T4, T7 | whole file | No finding. Refuses unless exactly closed rails; `DATABASE_URL` popped and restored; the lookup seam is app config only. `os.environ.setdefault("APP_ENV", "dev")` is not restored for a library caller (CONJ-1; O-24) |
| 42 | `tools/evidence/generate_determinism_gate_proofs.py` (`31df358af63a`) | #467; no | T3, T4, T7, T8 | whole file | No finding. Children forced to closed rails; outputs are hashes. Environment inheritance (DET-1, not confirmed; O-15) |
| 43 | `tools/evidence/generate_epic030_pr05_category_framework_evidence.py` (`c2d199883a9e`) | #467; no | T2, T7, T8 | whole file (read only; never run) | R04 (243). Also: wall-clock `produced_at`; its binding log checks key presence, not hashes (OBS-W5-3) |
| 44 | `tools/evidence/generate_hde_epic037_v2_to_compat.py` (`b76746a132fa`) | #467; no | T2, T3, T4, T7 | whole file | No finding. Closed rails enforced before work; synthetic fixtures only. Its `--check` fails on `main` from code drift, not security (OBS-W5-4) |
| 45 | `tools/evidence/generate_open_rails_abba_proof.py` (`d5097d28e679`) | #467, #501, #508; #513, #643, #646, #651; no | T2, T3, T4, T7, T8 | whole file | No finding. Live mode needs `--live`, exact rails, `APP_ENV=dev`, the canonical base, a confirmed authorization and an unused receipt; fixture-mode children have vendor keys stripped and run local-only showcompat; outputs carry presence booleans and redacted bases. Not confirmed: exact-name environment denylist (ORA-2; O-15); `--check-current`, which CI's rails job runs, does not byte-compare the committed proof while the release is admitted (ORA-1; the updater's `--check` binds its bytes; evidence-currency observation O-25) |
| 46 | `tools/evidence/regenerate_identity_closure.py` (`c1a06abee562`) | #467; #634; no | T2, T3, T8 | whole file | No finding. The source-tree refusal rests on `HDE_ISOLATED_RELEASE_BUILD=1` plus a hidden flag (RIC1; defeatable only by a deliberate operator act; O-22) |
| 47 | `tools/evidence/run_canonical_json_gate.py` (`652029563561`) | #467, #501; no | T2, T5, T7 | whole file | R07 (1205). Primaries published atomically per file; rows are `json.dumps` |
| 48 | `tools/evidence/run_sanity_pipeline.py` (`853566a0e4f7`) | #467; no | T2, T7, T8 | whole file | R05 (333, 347). Pins enforced; child output captured, never printed; log lines built from constants |
| 49 | `tools/evidence/run_sanity_pipeline_gate.py` (`62fbf8f87b1f`) | #467; no | T2, T5, T8 | whole file | R04 (106). Re-prints the pipeline's own output on failure (RSG2; not confirmed) |

## 7. Not-confirmed items and non-security observations

Recorded, not fixed here (ID-4); owner the IA unless stated, who routes them:

| ID | Observation | Owner |
| :- | :- | :- |
| O-01 | Gap 4: `adapter/http_reader.py::create_app`'s after-request hook is dead (`resp.request` does not exist); no observable effect (P-7). Addendum 2.7 and the decision record say it "never fires"; the precise statement is that it runs and never matches | IA (a later unit; doc wording) |
| O-02 | OBS-P3-3: `adapter/wsgi.py`'s 405 has no `Allow` header (P-8) | IA |
| O-03 | `_safe_load_chart`'s `rp.is_symlink()` after `resolve(strict=True)` is always false | IA |
| O-04 | `_require_admin_scope` compares bearer tokens with `==`; after S19-F03 the route answers the governed 404 in production before its handler | IA |
| O-05 | The alias `forbidden` maps to both `ERR_READER_FORBIDDEN` and `ERR_WRITER_FORBIDDEN` | IA |
| O-11 to O-13 | CI1 (GitHub path-filter limits, platform behavior); CI3 (tag-pinned actions, unpinned `setuptools` and `wheel`, no hashes); SC1 (`error_v1.details` unconstrained) | Product Owner (CI and dependency policy; schema owner) |
| O-14 | CI2: the workflow's path filter hard-codes the governed exceptions under exempt prefixes; they agree with the Index today, with no test tying them | WU-PR-06 or a later CI unit |
| O-15 | Environment inheritance into child processes (RR1, DET-1, ORA-2, GCC1, GEA2, RIC2): no path from an inherited value to I/O or output was found | IA (defence-in-depth candidate) |
| O-16 | Admission runs on every evaluation (about 0.3 s, CPU-bound) under 2 workers × 4 threads | Product Owner (performance) |
| O-17, O-18 | Non-atomic standalone writes of the cutter and of the goldens script (import-time writes) | IA |
| O-19 | `scripts/make_release_pack.sh` writes a non-canonical `artifacts/release_id.txt` that `scripts/hd_cli.py` reads as a release identity | WU-PR-08 / WU-DOC-01 through the IA |
| O-20 | The gate-readiness tool's `SELECT` runs in an ordinary (not read-only) transaction | IA |
| O-21 | `tools/config/artifacts.py` puts exception text into its report | IA |
| O-22 | Attestation and closure guards defeatable only by deliberate operator acts (BRA2, BRA3, RIC1) | IA |
| O-23 | The env-gate proof is fixed text from one `prod` probe; the exact gate itself is proven by `tests/http/test_reader_a7_transport.py` | IA / QA Plan |
| O-24 | `generate_conjunction_writer_evidence.py` leaves `APP_ENV=dev` set in a library caller's process | IA |
| O-25 | ORA-1: CI's `--check-current` does not compare the committed open-rails proof with a rebuild while the release is admitted | IA |

## 8. Out-of-scope observations (instruction ID-8)

| ID | Observation | Owner |
| :- | :- | :- |
| X-01 | LR4-O1: `vendor_audit.append_event` creates missing intermediate directories with the default mode; the sink directory and file stay owner-only | IA (routes it at the WU-PR-05 PR-40 review) |
| X-02 | OBS-P3-17: `run_flask.py` and `run_flask_dev.sh` start the production factory with the debugger and reloader on (HDE Architecture §3.8.1 discrepancy). After D-1 no harness handler is reachable there under a production-like `APP_ENV` | Product Owner |
| X-03 | The same lenient rails reading as S19-F05 outside the 49: `engine/providers/vendor_http.py` (`_is_truthy` on `ALLOW_NETWORK`) and `scripts/bodygraph/run_refresh_worker.py` (`_truthy` on both rails) | IA (later change candidate) |
| X-04 | `engine/bodygraph/vendor_client.py` puts `str(exc)` of a network error into `PROVIDER_NETWORK_ERROR` details, which the dev conjunction routes echo; after S19-F03 their handlers are not reachable in production | IA |

## 9. Route-policy statement (Plan Templates "`bg:resolve --source vendor` route-policy posture")

The route policy is unchanged by this unit (S19-R02 is routed, not fixed):
- configured `v2` bases are v2 chart-backed (`charts`, the deterministic `ChartResult` adapter);
- every other base takes the explicit legacy BodyGraph fallback (`bodygraphs`), including the unversioned, nonterminal and `v3` bases of S19-R02.

S19-F05 changes only which rail values count as open; the route selected for open rails is the same. This unit claims no BodyGraph-resolution conformance beyond existing evidence, no broad HumanDesignAPI v2 platform conformance, no live route availability and no public Reader change.

## 10. Fixes, regression tests and evidence after implementation

**Commits.** `d0f25b6` carries the hand-edited fixes and tests. Its diff from `8170cd8` equals plan v1.0's companion diff byte for byte, so the fixes are exactly plan §7. `176de33` carries the owner-produced refresh: 56 paths, `release_id` `77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e`.

**Regression tests.** 267 cases, all named `test_s19_*`, in the 13 existing modules that own each fixed source (plan §8.1, PD-13):

| Finding | Host modules (cases) | Negative controls (result of 267 with the fix disabled) |
| :- | :- | :- |
| S19-F01 | `tests/http/test_reader_post_v1.py` (6), `tests/http/test_reader_post_v2.py` (6), `tests/transport/test_writers_errors_headers.py` (writer case), `tests/http/test_compat_endpoint_contract.py` (1) | NC-01 12 failed; NC-02 1 failed; NC-03 1 failed |
| S19-F02 | `tests/http/test_dev_conjunction_http.py` (60), `tests/cli/test_cli_usage_and_errors.py` (13 gate cases) | NC-04 24 failed; NC-05 4 failed |
| S19-F03 | `tests/http/test_endpoint_catalog.py` (43) | NC-06 18 failed; NC-17 3 failed; NC-18 3 failed |
| S19-F04 | `tests/transport/test_writers_errors_headers.py` (bounded-read case) | NC-07 1 failed |
| S19-F05 | `tests/bodygraph/test_resolver_vendor.py`, `tests/bodygraph/test_ingest.py` | NC-08 30 failed; NC-09 9 failed |
| S19-F06 | `tests/bodygraph/test_resolver_vendor.py`, `tests/bodygraph/test_ingest.py` | NC-10 3 failed; NC-11 1 failed |
| S19-F07 | `tests/cli/test_cli_usage_and_errors.py` (2), `tests/cli/test_cli_file_inputs.py` (5) | NC-12 2 failed; NC-13 2 failed |
| S19-F08 | `tests/config/test_manifest_schema.py` (7), `tests/scripts/test_cut_release_manifest.py` (6) | NC-14 6 failed; NC-15 6 failed |
| S19-F09 | `tests/config/test_config_artifacts.py` (1) | NC-16 1 failed |

Each negative control ran once in a scratch copy before the cut and once in a detached worktree of `176de33`, with the same result both times. Every other case passed, and the file was restored byte for byte.

**Runs on `176de33`** (detached worktrees; closed rails, with vendor, database and GitHub keys unset). Each run ended with an empty `git status --short --untracked-files=all`.

| Check | Result |
| :- | :- |
| Full `tests/` sweep | 5,185 passed, 3 skipped, 2 xfailed, 0 failed (1,031.6 s), exit 0 |
| The CI lanes as `.github/workflows/ci.yml` writes them | All exit 0: classifier (77 paths; product, compat, db, rails, evidence, release; qa false; 39 changed-test targets); changed tests 1,874 passed; product 77 passed; compat 119 passed, 3 skipped, 2 xfailed; db 268 passed; rails `RAILS_JOB_DEFINITIONS_OK` and 138 passed; evidence 130 passed. Release: recompute and 79 passed, then the attestation build and verify (`release_admission` `PR06R_B_FINAL_PASS`, `validation_result` `PASS`, `source_commit_exact` true) |
| Instruction §5.6 read-only checks | 27 × exit 0; sanity `summary:PASS`, `first_failed_stage:NONE`. The three pre-existing failures (`generate_hde_epic037_v2_to_compat.py --check`, `generate_hde_epic037_bg_resolve.py --check`, `generate_hde_epic036_bg_resolve_route_policy.py --check`) exit 1 with output byte-identical to `1e97ba9` |
| Production-factory probe (instruction §5.3), `APP_ENV=prod` | `GET`/`HEAD /reader?v=1` 403 `ERR_READER_FORBIDDEN`. `POST /reader` 405 `Allow: GET, HEAD`. The sampler and the three conjunction routes 403 `ERR_WRITER_FORBIDDEN`, also with request-time `APP_ENV=dev`. `/ops/probe/env`, `/ops/db/unavailable` and `POST /ops/writer/diagnostic` 404 `ERR_NOT_FOUND`. `/ops/rails/refusal` 503 and `/internal/version` 200 unchanged |
| Served set, every pair under `APP_ENV=prod` | rules and pairs unchanged in all three factories (21 and 49; `adapter.wsgi` 23 and 55). The nine canon-retired pairs change their answer, and `/internal/version`'s body carries the new `release_id`. Nothing else changes |
| Canonical runner `adapter.http_reader.create_app`, `APP_ENV=dev` | full mount; the handlers answer as at `1e97ba9` |
| Gate matrix (`POST /internal/dev/sampler`) | served only for exactly `dev`, `test`, `local`; `DEV`, ` dev`, `Dev`, `TEST `, `prod` and empty refused |

**Nonclaims.**
- This review is implementation-side assurance, not QA and not acceptance (Plan v1.1).
- No fixed surface was run live; each fix's Live QA class (§4) is for the QA Plan.
- No QA verdict, acceptance, Ops, deployment, PF09 movement or closure is claimed.
- No conformance is claimed beyond the fixes made.
- No canon was edited. The routed findings (S19-R01 to S19-R07) are not decided by this unit; their owners decide them.
- No scanner, linter, analyzer or dependency was run, installed or added (Exclusions bullet 6; PF10 HDE Build Notes 2.3 Rule 3).

## Canon relied on

The review relied on the canon plan v1.0 "Canon relied on" lists, read on `main` at `1e97ba9` (`docs/pfcanon/` unchanged at `8170cd8`):
- HDE Architecture §1.3, §3.2, §3.3, §3.5 and §3.8.1;
- HDE-CLI-API-Vendor-Ref §3.3, §5.2, §5.4, §5.5, §5.11, §5.12, §7.1.1 to §7.1.11 and §8.1 to §8.4;
- HDE Governance §2.0.10, "Dev/admin APP_ENV gating", §3.1, §7.1, §8.1 and §8.2;
- HDE Users Guide §1.1, §6.4 and §7.6;
- HDE Math Spec §5.4.3;
- HDE Mechanics Guide §25.6 and §27;
- HDE Schemas & Artifacts §6.2.1 and §8;
- Glow Infrastructure §2;
- Plan Templates "`bg:resolve --source vendor` route-policy posture";
- PF10 HDE Build Notes v13.6 addenda 2.3, 2.5 to 2.9;
- the instruction §4.1 checklist map (§3).
