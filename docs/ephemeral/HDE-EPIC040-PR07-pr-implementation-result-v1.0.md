---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-EPIC040-PR07-PR-IMPLEMENTATION-RESULT
artifact_version: "1.0"
artifact_state: PR_CANDIDATE_PUBLISHED
phase: PR-30
change_class: EPIC
change_id: HDE-EPIC040
work_unit_id: HDE-EPIC040-PR07
pr_implementation_plan_id: HDE-EPIC040-PR07-PR-IMPLEMENTATION-PLAN v1.0
pr_instruction_id: HDE-EPIC040-PR07-PR-INSTRUCTION v1.0
authoring_context: APPROVED_BASE_WITH_OVERLAYS
execution_posture: MANUAL_PROMPT_EXECUTION
base_main: 5a2b6a6431a44d06750abb6a7cc1354fcc9589cf
documentation_commit: 757103c2ee1eaa2c916aa15739dc0dec9a3acf3a
working_branch: claude/sleepy-clarke-igh9e7
capture_utc: 2026-09-26T20:17Z
next_stage: PR-35 (its own dedicated session)
---

# HDE-EPIC040-PR07 — PR Implementation Result v1.0 (PR-30)

## 1. Identity, state and authority boundary

| Field | Value |
| --- | --- |
| artifact_type | `PR_IMPLEMENTATION_RESULT` (PR-30 phase record) |
| artifact_id / version | `HDE-EPIC040-PR07-PR-IMPLEMENTATION-RESULT` v1.0 — first issue; no predecessor result exists for this unit |
| repository_path | `docs/ephemeral/HDE-EPIC040-PR07-pr-implementation-result-v1.0.md` |
| State | `PR_CANDIDATE_PUBLISHED`. This record is the records commit of the one initial publication (plan §9 C5). It is pushed together with the documentation commit in a single push that creates the working branch on the remote, and the one pull request is opened from that branch. The pull-request number, the pushed remote head and the first check state come into existence after these bytes are fixed. Under PR-30 ("Populate result artifact, PR and commit references only after they actually exist"), the pull request itself and the PR-30 return record them, and PR-35 advances this checkpoint with them at entry. If the push or the pull-request creation does not complete, this state does not hold and the PR-30 return says so |
| CHANGE_CLASS / CHANGE_ID | `EPIC` / `HDE-EPIC040` — Separation Pass 3 |
| WORK_UNIT_ID | `HDE-EPIC040-PR07` — final repository documentation through DOC-10; documentation only |
| PR_IMPLEMENTATION_PLAN | `HDE-EPIC040-PR07-PR-IMPLEMENTATION-PLAN` v1.0, `docs/ephemeral/HDE-EPIC040-PR07-pr-implementation-plan-v1.0.md`, SHA-256 `7fd735aa1a9352e36c6a3c999e47a32d20608df5d25d8d7fe0fff5e2888664d5`, 126,982 bytes, blob `9e8b2a470c5b230f3b40cc769913cc1477f3ae31`; on `main` since planning PR [#517](https://github.com/amthorn78/glow-hdengine-v2/pull/517) merged as `5a2b6a6` (2026-09-26T19:56:16Z); read from `main` (plan §9 C0) |
| PR_INSTRUCTION | `HDE-EPIC040-PR07-PR-INSTRUCTION` v1.0, `INSTRUCTION_READY`, `docs/ephemeral/HDE-EPIC040-PR07-pr-instruction-v1.0.md`, SHA-256 `3113b4e85ff50c10ab569e0f27eb882225abb333aaaa8db2bd8e712db0cd1c7b`, 9,404 bytes, blob `a6b3ff574f72aa3ebe480c03d811773130fe23c9` |
| Original Product Owner Proceed | Nathan's PR-30 invocation in this session: "invoking this prompt with this block is Nathan's PR-30 Proceed for exactly HDE-EPIC040-PR07-PR-IMPLEMENTATION-PLAN v1.0 and HDE-EPIC040-PR07-PR-INSTRUCTION v1.0". It is the one Proceed for this plan; PR-35 continues under it and never requests another |
| Immutable bases and accepted predecessors | As plan v1.0 §§1 and 2.1, unchanged and not rewritten: Specification v1.1, Implementation Audit v2.0, Implementation Plan v2.1 (`docs/ephemeral/HDE-EPIC040-implementation-plan-v2.1.md`, SHA-256 `10732f9338b209e3ce19e81936119e47c9551ea912298a27c731c9e60e2a61be`; §6.7 is this unit), Plan Review v2.1 (Isis-50 `APPROVE`); PR01 to PR06, PR06a and PR06b `ACCEPTED_FINAL` and not reopened |
| Effective baseline | approved base + PF10 overlays §2.23 (`docs/ephemeral/HDE-EPIC040-PR06a-PF10-build-notes-addendum-v1.0.md`, SHA-256 `a69e2205de410bf6332bb558f3ee0110e3524b7143a84591bbed18ff476528e9`) and §2.25 (`docs/ephemeral/HDE-EPIC040-PR06b-PF10-build-notes-addendum-v1.0.md`, SHA-256 `63d0bdcee8d4295738bb6a05a5a93c72951a871532e12d53b7e3a449fcca14a3`), with §§2.5, 2.7, 2.9, 2.10 and 2.12 as plan §2.3 records. No `REMEDIATION_REVIEW` applies |
| Current controlled PF10 | `docs/pfcanon/PF10-HDE-Build-Notes-v13.3.7.md`, SHA-256 `af292883d5d4f27bd5cc510117e29b044ec2ac0b0f522df48fd0022010c6855c`, 286,355 bytes, the only PF10 file on `main` at `5a2b6a6`, byte-identical to the version the plan read. Recorded as provenance, not as a gate |
| producer_role | Dedicated PR-development session for exactly HDE-EPIC040-PR07, PR-30 phase |
| session_disposition | `RETAIN_EXISTING` (the same dedicated PR07 session that ran PR-20) |
| role_session_ref | `NOT_YET_ASSIGNED` — no reference was assigned; no platform ID is invented. Known runtime identity: `https://claude.ai/code/session_01UrEaEb4uQkqq2zHD7VTYyc` |
| invocation_binding | `HDE-EPIC040` / `HDE-EPIC040-PR07` / `PR-30` |
| context_conflict | `NONE` |
| execution_posture | `MANUAL_PROMPT_EXECUTION` |
| Primary skill authority | `glow-hde-pr-development` (sole primary skill for PR-30 and PR-35) |
| Authority boundary | Implementation of plan §6 and its local proof only. No merge, auto-merge, QA, OPS01, acceptance, activation, deployment, PF-Canon edit (including C040-06/07/08 drainage), PF09 movement or Epic closure. Nathan alone merges |

### 1.1 GCF-17 continuity fields (shared unchanged by PR-30 and PR-35)

| # | Field | Value |
| --- | --- | --- |
| 1 | `WORK_UNIT_ID` | `HDE-EPIC040-PR07` |
| 2 | Original Product Owner Proceed | the PR-30 invocation quoted in §1 |
| 3 | Workspace / worktree | repository checkout `/home/user/glow-hdengine-v2` of `amthorn78/glow-hdengine-v2` in this session's container. The proof worktree (a detached worktree under the session scratchpad, outside the repository) is transient scratch and is removed after publication |
| 4 | Branch | `claude/sleepy-clarke-igh9e7` (see IFD-03: restarted from `main` at `5a2b6a6`; the merged planning PR #517 used the same branch name and is landed history) |
| 5 | Pull request | the one pull request opened from this branch at publication; its number postdates this record (§1 State). It is not #517 |
| 6 | PR instruction | `docs/ephemeral/HDE-EPIC040-PR07-pr-instruction-v1.0.md` v1.0 |
| 7 | Detailed PR plan | `docs/ephemeral/HDE-EPIC040-PR07-pr-implementation-plan-v1.0.md` v1.0 |
| 8 | Primary skill authority | `glow-hde-pr-development` |
| 9 | Recovery / artifact lineage | instruction v1.0 → plan v1.0 (PR-20, #517) → this result v1.0 (PR-30) |

## 2. Sources read in PR-30

- Prompt: PR-30 — PR Implementation Proceed — 091426.1, `https://app.notion.com/p/3db4590a05eb8123afb8caeeaa83a294?pvs=204` (page as of 2026-09-24T15:47:45.499Z), read completely. Destination verified: PR-35 — Resolve PR Reviews and Reach Merge Readiness — 091426.1, `https://app.notion.com/p/3db4590a05eb8120b443ed2cb08b723c?pvs=204` (page as of 2026-09-24T15:48:24.405Z), read completely; both pages sit under `AI Prompts / HDE IA — GCFPE-20260914.1 — 091426.1`. Notion was read only; no Notion write was made.
- Release selection: GCFPE-20260914.1 / 091426.1 / 55 members as plan §2.4 records it; the register was not re-read in PR-30.
- Repository: the plan v1.0 and instruction v1.0 completely; `AGENTS.md`; `.github/pull_request_template.md`; `.github/workflows/ci.yml` triggers; the fifteen documentation files at base and head.
- PF sources of plan §2.2: unchanged at `5a2b6a6` (the only change since the planning baseline `48b0559` is the plan file itself, §3), so the planning reads stand; nothing under `docs/pfcanon/` was edited.

## 3. C0 — Recovery and preconditions

| Check | Evidence | Outcome |
| --- | --- | --- |
| Proceed for this exact plan | the PR-30 invocation (§1) | present |
| Plan on `main` | `git ls-tree origin/main docs/ephemeral/` lists the plan; #517 merged as `5a2b6a6` | plan read from `main`, not from a PR head |
| `main` movement since planning | `git diff --name-only 48b0559 origin/main` → `docs/ephemeral/HDE-EPIC040-PR07-pr-implementation-plan-v1.0.md` only; `origin/main` still `5a2b6a6431a44d06750abb6a7cc1354fcc9589cf` at 20:10Z | no documented surface moved; the F-facts stand, and every fact the new text relies on was re-verified at the head anyway (§§6.2, 6.3) |
| Existing PR07 implementation vehicle | open PRs: only [#516](https://github.com/amthorn78/glow-hdengine-v2/pull/516) (`chore(claude)` settings, unrelated); PR07 records on `main`: the instruction and the plan only (no result, rescope or checkpoint); remote `claude/sleepy-clarke-igh9e7`: absent (`git ls-remote --heads` returns nothing; deleted when #517 merged); worktrees: the checkout and this session's scratch worktrees only | none exists; one documentation commit created on the restarted branch (IFD-03) |
| Unrelated user work | checkout clean at entry | nothing to preserve |

## 4. C1 — Local validation environment

| Item | Value |
| --- | --- |
| Interpreter | Python 3.11.15 (virtualenv under the session scratchpad); pytest 8.4.2 (readiness proof `python -m pytest --version`); pip 24.0 |
| Installation | the virtualenv built in the PR-20 run holding `requirements.txt` and `requirements-dev.txt` (plan §3.3), with setuptools 79.0.1 and wheel 0.48.0 present; its editable install was re-pointed at the candidate worktree for PR-30 (2026-09-26T20:02:11Z; `pip show glow-hdengine` reports the candidate worktree as the editable project location) |
| Candidate worktree | detached at `757103c2ee1eaa2c916aa15739dc0dec9a3acf3a`, outside the repository; `git status --short --untracked-files=all` empty after every proof group |
| Rails | `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 PYTHONDONTWRITEBYTECODE=1`; `HD_API_BASE_URL`, `HDAPI_BASE_URL`, `HD_API_KEY`, `GEO_API_KEY`, `DATABASE_URL`, `DEV_SAMPLER_URL`, `GH_TOKEN` and `PYTHONPATH` UNSET for every proof process. `APP_ENV=dev` only for the P-14 Reader probes, with the prescribed `APP_ENV=prod` and unset probes. One deliberate refusal probe with `SAFE_MODE=0` (P-03e), which refused before any I/O |
| Network | no vendor, geocoding or database I/O by any proof; the only socket a proof opened was the local helper on `127.0.0.1:8000` (P-14(d)). `pip wheel` (P-14(g)) printed pip's upgrade notice; pip's own version check may consult the package index, which is packaging tooling, not application I/O. Package installation for the virtualenv (PR-20 run) used the package index |
| CI parity | this PR's CI classifies as `documentation_only` and runs no Python (P-09), so the local Python version does not bear on CI (plan R-12) |

## 5. C2 — Implementation

- Method: every edit was taken mechanically from the plan's own §6 blocks. The per-section block counts were asserted, and every anchor had to match exactly once before any file was written, so no text was retyped. Order as C2: contract pages, server page, README, command and configuration pages, INDEX, transport pages, additional homes, AGENTS, CHANGELOG.
- Reproduction proof (plan §11.1 "no other line changed"): re-applying §6 onto a fresh detached worktree of `5a2b6a6` reproduces all fifteen files byte-identically to `757103c` (15 compared, 0 differing).
- Generated companions: none (plan D-09; F-22). No code, schema, golden, catalog, manifest, evidence or PF-Canon byte changed (P-11).
- Documentation commit: `757103c2ee1eaa2c916aa15739dc0dec9a3acf3a`, "docs: HDE-EPIC040-PR07 final repository documentation (DOC-10)", 2026-09-26T20:01:23Z, parent `5a2b6a6`; 15 files, +203 / −27.

| Path | Plan § | Added / deleted lines |
| --- | --- | --- |
| `docs/contracts/reader_v2_public_bytes.md` (new) | 6.1 | 66 / 0 |
| `docs/contracts/reader_v1_public_bytes.md` | 6.2 | 26 / 3 |
| `docs/server/reader_v1.md` | 6.3 | 14 / 2 |
| `README.md` | 6.4 | 22 / 9 |
| `CHANGELOG.md` | 6.5 | 12 / 0 |
| `docs/CLI_commands.md` | 6.6 | 16 / 1 |
| `docs/RUN.md` | 6.7 | 9 / 3 |
| `docs/config_and_bundles.md` | 6.8 | 8 / 1 |
| `docs/INDEX.md` | 6.9 | 11 / 3 |
| `docs/acceptance/http_transport_evidence.md` | 6.10 | 2 / 0 |
| `docs/ADAPTER_009.md` | 6.11 | 3 / 1 |
| `AGENTS.md` | 6.12 | 9 / 0 (additive only) |
| `docs/architecture/emitters.md` | 6.13 | 1 / 1 |
| `FLASK_AUTO_RUN_GUIDE.md` | 6.14 | 3 / 2 |
| `ARCHITECTURE.md` | 6.15 | 1 / 1 |

The `docs/RUN.md` curl line (§6.7) is kept: P-14(d) executed it against a live local helper, so the §6.7 fallback was not needed.

## 6. Proofs on the committed head (C3 and C4; plan §8)

All proofs ran on `757103c` in the detached candidate worktree under the §4 rails. Exit statuses come from captures that carry the producer's own status (`"$@" > out 2> err; rc=$?`, or a plain capture of the producer). Times are UTC on 2026-09-26.

| ID | Command or check | Exit | Result |
| --- | --- | --- | --- |
| P-01 | every backticked repository path in added lines exists at the head | 0 | PASS — 73 distinct paths, none missing |
| P-02 | symbol and constant existence by reading | 0 | PASS — 20 symbols found; `_admission_execution_provenance` covers exactly eight modules: `engine/config/registry_loader.py`, `engine/serializer/canon.py`, `engine/stable/sercanon.py`, `engine/categories/registry.py`, `engine/core/core.py`, `engine/magic10/composite.py`, `engine/magic10/signals.py`, `engine/magic10/calculators.py` |
| P-03a | `python tools/config/generate_config_artifacts.py --check` | 0 | PASS |
| P-03b | `python tools/config/generate_config_artifacts.py --compare-goldens . --report <scratch>/golden_report.json` | 0 | PASS — `ok: true`, schema `magic10_golden_comparison.v1`, 8 cases `M10-G001` to `M10-G008`, every `outcome` `match`, `mismatches` empty, `candidate_release_id` equal to the manifest digest; report SHA-256 `bea29970107fe750394e0f78c1047de93ebd9193565cd82a8e6e92e7b515dca8` (identical to the planning-time report) |
| P-03c | `python tools/bodygraph/check_magic10_gate_readiness.py --help` | 0 | PASS |
| P-03d | `python tools/bodygraph/check_magic10_gate_readiness.py` | 5 | PASS — stderr `READINESS_EMPTY_SELECTION` |
| P-03e | `SAFE_MODE=0 python tools/bodygraph/check_magic10_gate_readiness.py --user-id 00000000-0000-4000-8000-000000000000` | 5 | PASS — stderr `RAILS_CLOSED_REQUIRED:[('SAFE_MODE', '1')]`; refused before any I/O |
| P-03f | `python tools/generate_registry_report.py --help` | 0 | PASS — usage `[-h] [--allow-aliases]`; no `--check` |
| P-03g | `python scripts/release_id_recompute.py --check-manifest-only` | 0 | PASS |
| P-03h | `python scripts/cut_release_manifest.py --version 1.3.0 --built-at-utc 2026-08-24T18:04:49Z --check` | 0 | PASS |
| P-03i | the same with `--roster-from-admission` | 0 | PASS |
| P-03j | admission one-liner (`load_active_mechanics_bundle()` and `identity_meta()`) | 0 | PASS — prints `AdmittedMechanicsBundle 1.3.0 45 52be45584acbaa327da2d1cac724857dcdc999ca8c7a8f65108427942a4afe96 True` (release_id equals the manifest digest and `identity_meta()["release_id"]`); tree clean afterwards |
| P-04 | the five golden-named examples on the two contract pages | 0 | PASS — v1 `g03_harmony_open`, v1 `g06_error_invalid_input`, v2 `g03_eligible_ten_in_order`, v2 `g01_ineligible`, v2 `g04_error_invalid_version`: each equals its golden minus the trailing LF, each validates (Draft 2020-12) against the schema of its directory, and the `idempotence_hash` of the three success examples recomputes from `engine.presenter.emitter.emit_public`. The historical EPIC-004 `compat` example is excluded and stays labelled historical |
| P-05 | Markdown links in added lines | 0 | PASS — the added lines contain no Markdown links (paths are backticked and covered by P-01) |
| P-06 | claims audit of added lines | 0 | PASS — see §6.1 |
| P-07 | secret and private-data scan of added lines | 0 | PASS — no credential URL, `Bearer ` value, key assignment, birth data or fixture content; no UUID in added lines; five distinct 64-hex values, all expected: the admitted `release_id` `52be45584acbaa327da2d1cac724857dcdc999ca8c7a8f65108427942a4afe96`, the synthetic 64-`a` `release_id` of the goldens, and the golden `idempotence_hash` values of v1 `g03`, v2 `g03` and v2 `g01` |
| P-08 | `python ci/checks/check_direct_db_contract.py` | 0 | PASS — `DIRECT_DB_CONTRACT_OK` |
| P-09 | `python ci/checks/classify_ci_changes.py --base 5a2b6a6431a44d06750abb6a7cc1354fcc9589cf --head 757103c2ee1eaa2c916aa15739dc0dec9a3acf3a --event-name pull_request --github-output <scratch>/gh_out.txt --changed-tests-output <scratch>/changed_tests.txt` | 0 | PASS — `product=false compat=false db=false rails=false evidence=false qa=false release=false needs_python=false changed_tests=false reason=documentation_only path_count=15`; stdout `CI_CHANGE_CLASSIFICATION:event=pull_request;reason=documentation_only;paths=15;lanes=none`; no `CI_CHANGE_SURFACE_UNCLASSIFIED` |
| P-10a | `python tools/evidence/update_evidence_index.py --check` | 0 | PASS |
| P-10b | `python tools/evidence/orientation_demo.py --check` | 0 | PASS |
| P-10c | `python tools/evidence/refresh_step_logs_manifest.py --check` | 0 | PASS |
| P-10d | `python tools/evidence/validate_evidence_paths.py` | 0 | PASS |
| P-10e | `ci/checks/check_mirror_schema.sh` | 0 | PASS |
| P-10f | `ci/checks/check_evidence_index_hash.sh` | 0 | PASS |
| P-10g | `ci/checks/check_final_lf.sh` | 0 | PASS |
| P-10h | `python tools/evidence/run_canonical_json_gate.py --check-only` | 0 | PASS; `git status` clean |
| P-11 | `git diff --name-only` over the three-dot (merge-base) range from `origin/main` to `HEAD`, against the fifteen §3.4 paths | 0 | PASS at `757103c` — exactly the fifteen paths; nothing under the forbidden prefixes; no existing `docs/ephemeral/` file touched. At the records commit the list gains exactly this record (verified before the push; §9) |
| P-12 | formatting | 0 | PASS — `git diff --check` clean; no CR; no ellipsis in added lines; fences balanced; twelve files end with exactly one LF and three keep their pre-existing ending unchanged (IFD-01) |
| P-13 | the fifteen-file pytest roster of plan §8 (`python -m pytest -q -p no:cacheprovider` over those files) | 0 | PASS — 716 passed in 62.66 s; `tests/reader_v1/test_cli_proof.py` not in the roster (pre-existing failure O-P06a-03) |
| P-14 | documented invocations | 0 | PASS — see §6.2 |
| P-15 | content-map completeness | 0 | PASS — 34 content rows, see §6.3 |

The doc-level proofs (P-01, P-02, P-04 to P-07, P-11, P-12, P-15) completed at 20:04:41Z and again at 20:10:52Z with byte-identical output. The command proofs' output files carry times from 20:06:57Z (P-03a) to 20:10:03Z (P-14(g)).

### 6.1 P-06 claims audit (reviewer-checked)

Hard checks: no PF version number in added lines; no link into `docs/ephemeral/`; no drainage statement without "as of HDE-EPIC040-PR07"; no enumeration of the governed error pairs; no copy of the 36-row table. All empty. Claim-word hits, each reviewed:

| File | Hit in context | Disposition |
| --- | --- | --- |
| `AGENTS.md` | "`engine/config/registry_loader.py` and fails closed otherwise" | failure mode, not a closure claim |
| `AGENTS.md` | "both refuse outside closed rails" | rails posture, not a closure claim |
| `CHANGELOG.md` | "with their non-mutation and closed-rails constraints" | rails posture |
| `README.md` | "PR01 through PR06, PR06a and PR06b are accepted final" | the permitted accepted-final status of PR units |
| `README.md` | "admission fails closed unless every member is present" | failure mode |
| `docs/CLI_commands.md` | "refuse outside the closed rails" | rails posture |
| `docs/contracts/reader_v2_public_bytes.md` | "as of HDE-EPIC040-PR07, C040-07 has not been drained" | negative, time-bound drainage status |

No QA, acceptance, deployment, production-readiness, activation, PF09 or closure claim is made.

### 6.2 P-14 execution summary

| Step | Invocation | Outcome |
| --- | --- | --- |
| (a1) | `hdctl showcompat --a-file fixtures/charts/alice.json --b-file fixtures/charts/bob.json` | exit 0; 3,298 bytes, SHA-256 `6b0a923c4b79d7217666b5d7a4f9211f2ab71c58d72de122ed1cabd7ef2e27cb`; keys `categories`, `config_id`, `pair_key`, `release_id`, `schema`, `signals`; `schema` `magic10_compat_result.v1`. Written to a scratch pair file outside the repository in place of the README's `/tmp/pair.json` (as P-14(a) prescribes) |
| (a2) | `hdctl aux-preview --pair-file <scratch pair> --category harmony --band Cool --perspective shared --show-narrative` | exit 0; "Together you feel calm and even. The pace is kind and unforced." |
| (b) | the same with `--band Hot` | exit 64; argparse `invalid choice: 'Hot' (choose from 'Cool', 'Open', 'Warm', 'Glow')` — the band set is sealed |
| (c) | `hdctl showcompat --a-file fixtures/charts/alice.json --b-file fixtures/charts/bob.json --dump-reader <scratch>/dump_reader.json` | exit 0; sidecar 330 bytes, LF-terminated, SHA-256 `103df389283c7e577ebd78d377eb49fe6b7d014b732389577ea9efbbe1de32d0` |
| (d) | from the worktree root: `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PORT=8000 scripts/dev_start_reader.sh` in the background, then the `docs/RUN.md` command `curl -s 'http://127.0.0.1:8000/reader?v=1&a=fixtures/charts/alice.json&b=fixtures/charts/bob.json&a_tz=UTC&b_tz=UTC'` (with connection retries while the helper bound), then the helper stopped | port 8000 was free and used; helper logged `Binding port 8000 via python -m adapter.http_reader (host=0.0.0.0)`; curl exit 0, HTTP 200, `Content-Type: application/json; charset=utf-8`, `Cache-Control: private, max-age=0, must-revalidate`, `Vary: Authorization, Accept-Encoding`, `ETag` present; body byte-identical to (c) (330 bytes, same SHA-256); port released at stop (20:09:29Z) |
| (e) | Flask test-client probes on `adapter.factory`, `adapter.wsgi` and `adapter.http_reader` | 60 of 60 checks OK. Each factory: `POST /api/reader?v=1` and `?v=2` without a database → 503 `ERR_M10_RESOLVER_UNAVAILABLE`; `?v=3`, no `v`, `v=1&v=2` and `v=` → 400 `ERR_READER_INVALID_VERSION`; body `{}` → 422 `ERR_READER_INVALID_INPUT`; a 32,770-byte body → 422 `ERR_READER_INVALID_INPUT`; `GET`, `PUT`, `PATCH`, `DELETE` on `/api/reader` → 405 `ERR_NOT_FOUND` with `Allow: POST`; `POST /reader` → 405 with `Allow: GET, HEAD`; dev `GET /reader` → 200, bytes equal to (c), headers as (d); dev `?v=2` → 400; bare `a=alice.json` → 400 `ERR_READER_INVALID_PATH`; `APP_ENV=prod` → 403 `ERR_READER_FORBIDDEN`; `APP_ENV` unset → 200 (O-P07-04). Every error body is valid against `schemas/reader.v1.schema.json`, `Cache-Control: no-store`, no ETag. Unknown path `/api/reader/missing`: HTML 404 from `adapter.factory` and `adapter.http_reader`, JSON 404 `no-store` from `adapter.wsgi` (O-P06a-22) |
| (f) | `APP_ENV=dev python -c "import dev.reader_harness.app"` | exit 1; `AttributeError: 'Flask' object has no attribute 'getattr'` (O-P07-03) |
| (g) | `python -m pip wheel --no-deps --no-build-isolation -w <scratch>/wheel2 <candidate worktree>` | exit 0; `glow_hdengine-0.0.0-py3-none-any.whl`, SHA-256 `fef88273d09852a672ccf5d7fc7711349eea8b9bafbf09ba82b3e880bc6af879`; 16 of the 45 manifest members absent: `adapter/schemas/error_v1.schema.json`, `catalog/narratives/keys.json`, `catalog/narratives/manifest.json`, `catalog/narratives/palettes.json`, `catalog/narratives/suppression_map.json`, `catalog/narratives/templates.json`, `errors/token_map/token_map.json`, `migrations/005_identity.sql`, `schemas/channels_v1.schema.json`, `schemas/gates_v1.schema.json`, `schemas/magic10_compat_result_v1.schema.json`, `schemas/magic10_mechanics_v1.schema.json`, `schemas/magic10_result_v1.schema.json`, `schemas/reader.v1.schema.json`, `schemas/reader.v2.schema.json`, `tools/bodygraph/check_magic10_gate_readiness.py` (matches F-21 / O-12). The build directories it writes are gitignored; the worktree stayed clean |

Additional re-verification at the head for facts the new text relies on (inference support for P-15): `hdctl --help` still reads "Emit canonical Reader v1 bytes from vendor JSON" for `showcompat` (F-16, O-P07-01). `--band Glow` against the `Cool` harmony pair exits 0 with the `Cool` narrative (F-17, O-P07-02). `catalog/channels_v1.json` has 36 rows with `circuit_primary` counts individual 15, collective 14, tribal 7; its `integration` rows are exactly `10-20`, `10-57`, `20-34`, `34-57`; `10-34` is `individual`/`centering` and `20-57` is `individual`/`knowing`; every row carries `primary_domain`, `domains` and `flags` (F-19). `EXPECTED_TARGET_PATHS` 26 and `EXPECTED_SET_RULES` 6; `keys.json` and `templates.json` 360 each (F-23). `config/bands_4B60_v1.json` and `config/toggles_v1.json` exist, with no reader in `engine/`, `adapter/`, `presenter/`, `scripts/` or `tools/` (F-07). `catalog/magic10_mechanics_v1.json`: `magic10_mechanics_config.v1`, `m10-channel-state-v1.0.0`, `magic10_result.v1`, 20 signals, four `sources` rows each with a 64-hex SHA-256 (F-02). `COMPAT_RESULT_SCHEMA` and `PURE_RESULT_SCHEMA` at `engine/compat/compute.py:42–43`. Both bundles are `config_bundle.fe.v1` / `config_bundle.be.v1` at the head and at the HDE-EPIC040 base `9065e6f`. `schemas/reader.v1.schema.json` has no line containing `_leader` or `"prompt"` at the head, against 4 and 1 such lines at `9065e6f`; no file under `goldens/reader/` contains `_leader`; `scripts/hd_cli.py` still does. `schemas/reader.v2.schema.json` declares no `number` or `integer` type. The readiness tool mentions `UPDATE`, `INSERT` and `DELETE` only in its docstring's negation, and its selection-file reader skips blank and `#` lines. The generator help describes `--publish-family` as "Publish the scoped config, catalog logs, bundles and required evidence companions from this checkout". The `/api` mount is at `adapter/factory.py:12`, `adapter/wsgi.py:24` and `adapter/http_reader.py:1172`. The PF10 v13.3.7 headings "HDE-EPIC040 — Record the approved source-backed Channel taxonomy and existing-state conformance" (§2.5, line 461) and "HDE-EPIC040-PR06b — Reader v1 error-envelope schema conformance (C040-08)" (§2.25, line 2568) exist as cited.

### 6.3 P-15 content map — quotations from the head (`757103c`)

Each quotation is copied from the named line at the head; the F-facts it relies on were re-verified at the head by the proofs named.

- **Supported four-argument core** — `README.md:11`; F-01, F-02; P-02, P-13, P-03j
  > the supported Magic-10 core is the four-argument `engine/core/core.py::compute_core(member_a, member_b, mechanics_bundle, release_id)`, which returns one complete intrinsic `magic10_result.v1`; eligibility belongs to the caller.
- **Core (INDEX)** — `docs/INDEX.md:88`; F-01; P-02
  > Engine Core compute: `engine/core/core.py::compute_core` (four arguments: `member_a`, `member_b`, `mechanics_bundle`, `release_id`; eligibility belongs to the caller, `engine/compat/compute.py::evaluate_pair`)
- **Core (AGENTS)** — `AGENTS.md:98`; F-01; P-02
  > Supported core: `engine/core/core.py::compute_core(member_a, member_b, mechanics_bundle, release_id)`; eligibility belongs to the caller. The Reader and `hdctl showcompat` reach it through `engine/compat/compute.py::evaluate_pair`.
- **Strict config/result schemas** — `docs/config_and_bundles.md:4`; F-02; P-01, P-03a, head read (§6.2)
  > Mechanics configuration: `catalog/magic10_mechanics_v1.json` (`magic10_mechanics_config.v1`, `config_id` `m10-channel-state-v1.0.0`, `result_schema` `magic10_result.v1`), validated against `schemas/magic10_mechanics_v1.schema.json`. Its `sources` bind `catalog/magic10_caps.json`, `catalog/magic10.json`, `catalog/channels_v1.json` and `math/thresholds.json` by SHA-256.
- **Canonical writers** — `docs/config_and_bundles.md:6`; F-06; P-01, P-03a, generator help (§6.2)
  > Writers (canonical owners; never hand-edit their outputs): `tools/config/generate_config_artifacts.py` writes `artifacts/registry/registry_report.json`, `artifacts/thresholds/magic10_config.json` and `artifacts/thresholds/band_edges.json`
- **Writer usage (RUN)** — `docs/RUN.md:10`; F-06; P-03a, P-03f
  > `python tools/generate_registry_report.py` has no check mode; it writes the registry report.
- **Complete versus candidate release** — `README.md:134`; F-03, F-04; P-02, P-03g to P-03j
  > Complete versus candidate release (HDE-EPIC040): admission accepts only the complete release pinned in `engine/config/registry_loader.py` by `ADMITTED_RELEASE_VERSION`, `ADMITTED_RELEASE_BUILT_AT_UTC` and the 45-path `ADMITTED_RELEASE_ROSTER`, with every member's bytes, hash and size matching the manifest and the executing mechanics modules equal to their admitted members.
  > A candidate root is only validated or compared (for example with `--compare-goldens`); it is never activated.
- **Release cut and admission constants (RUN)** — `docs/RUN.md:12`; F-03, F-04; P-02, P-03h, P-03i
  > A new release version also changes `ADMITTED_RELEASE_VERSION` (and, where they change, `ADMITTED_RELEASE_BUILT_AT_UTC` and `ADMITTED_RELEASE_ROSTER`) in `engine/config/registry_loader.py` before the cut, because admission compares the manifest with those constants and that file is itself a release member.
- **Admission addition (AGENTS)** — `AGENTS.md:117`; F-03, F-04; P-02, P-03i
  > HDE-EPIC040 admission addition: the cutter still writes only `catalog/manifest.json`, but admission compares the manifest with `ADMITTED_RELEASE_VERSION`, `ADMITTED_RELEASE_BUILT_AT_UTC` and `ADMITTED_RELEASE_ROSTER` in `engine/config/registry_loader.py`, which is itself a release member.
- **Unchanged FE/BE promise** — `docs/config_and_bundles.md:7`; F-06; bundle identities at head and at `9065e6f` (§6.2)
  > FE/BE promise: the bundle schema identities `config_bundle.fe.v1` and `config_bundle.be.v1` are unchanged by HDE-EPIC040, and the Channel fields `primary_domain`, `domains` and `flags` remain non-scoring Product metadata (`PF12-Canon-HDE-Schemas-and-Artifacts` §2.1).
- **Numeric-free Reader promise** — `docs/contracts/reader_v2_public_bytes.md:23`; F-13; P-04, P-13, schema read (§6.2)
  > Exactly six keys: `categories`, `eligible`, `idempotence_hash`, `meta`, `reader_version` and `release_id`. `reader_version` is always `"v2"`. No field is numeric.
- **Comparator command** — `docs/CLI_commands.md:36`; F-08; P-03b
  > Golden comparison: `python tools/config/generate_config_artifacts.py --compare-goldens <candidate-root> [--goldens <path>] [--report <path>]`
- **Readiness command** — `docs/CLI_commands.md:40`; F-09; P-03c to P-03e, P-02, P-13
  > Gate readiness: `python tools/bodygraph/check_magic10_gate_readiness.py --user-id <uuid> [--user-id <uuid>]` or `--selection-file <path>` (one canonical UUID per line; blank lines and `#` comments ignored; a regular, non-symlinked file of at most 1,048,576 bytes).
- **Non-mutation and security constraints** — `docs/CLI_commands.md:43`; F-09; head read (§6.2), P-13
  > It issues no `UPDATE`, `INSERT` or `DELETE` and performs no acquisition, repair, backfill or vendor call. It reads through the database configured by `DATABASE_URL`; never print or commit that value.
- **Admission limits** — `README.md:134`; F-03, F-05; P-02 (eight modules); PF10 §§2.9, 2.10, 2.12 unchanged
  > Limits: the executing-module check proves executable-code equivalence for eight first-party modules, not the historical bytes the interpreter read or resistance to arbitrary in-process tampering; admission provides no process-death atomicity, multi-file atomic visibility or cross-process locking.
- **Writer recovery limits** — `docs/config_and_bundles.md:8`; F-05; PF10 §2.6 unchanged
  > They do not promise crash atomicity, multi-file atomic visibility or cross-process locking.
- **Authoritative 36-row evidence/decision (C040-06)** — `README.md:16`; F-19, F-20, plan §5.3; PF10 heading (§6.2)
  > The decided record, with the complete 36-row table and its evidence, is the `PF10-HDE-Build-Notes` addendum "HDE-EPIC040 — Record the approved source-backed Channel taxonomy and existing-state conformance"; it names the original ADR `HDE-EPIC040-C040-06-HD-MECHANICS-ADR` v1.0, which keeps the full source ledger.
- **Why Integration uses the broad grouping** — `README.md:16`; F-19; head re-execution (§6.2)
  > Official broad-group exposition places Integration in Individual, so the four Integration Channels (`10-20`, `10-57`, `20-34`, `34-57`) are `individual` with substream `integration`, while Integration's separate formal structure is preserved; Channel-specific evidence keeps `10-34` as `individual`/`centering` and `20-57` as `individual`/`knowing`.
- **Reader v2** — `docs/contracts/reader_v2_public_bytes.md:3`; F-10, F-13; P-04, P-13, P-14(e)
  > Reader v2 exposes the full Magic-10 set as bands only. HDE-EPIC040-PR06a delivered it. Reader v1 is unchanged and stays available on the same route; see `docs/contracts/reader_v1_public_bytes.md`.
- **`/api/reader` route and version selection** — `docs/contracts/reader_v2_public_bytes.md:15`; F-10; P-14(e), P-13
  > Version selection: the query carries exactly one `v`, with the value `1` or `2`. A missing, empty, repeated or other value returns 400 `ERR_READER_INVALID_VERSION` before the body is read.
- **Route note (transport evidence)** — `docs/acceptance/http_transport_evidence.md:20`; F-10; P-14(e), P-13
  > The production Reader is `POST /api/reader?v=1` or `?v=2`: a success is 200, non-conditional and carries no ETag; its errors are `no-store` without ETag; every other method on `/api/reader` returns 405 with `Allow: POST`.
- **Route note and parity (ADAPTER_009)** — `docs/ADAPTER_009.md:176` and `:180`; F-10, F-15; P-14(c) to P-14(e)
  > `HTTP_POST_METHOD_POSTURE_OK` keeps its original meaning, which now holds for the unprefixed `POST /reader`: it returns the governed 405 (`ERR_NOT_FOUND`, `Allow: GET, HEAD`, `no-store`, no ETag).
  > Bytes are LF-terminated; Reader↔CLI parity is defined via the CLI `--dump-reader` sidecar (not `showcompat` stdout), as in `docs/acceptance/http_transport_evidence.md`.
- **Conformed Reader v1 schema, error branch** — `docs/contracts/reader_v1_public_bytes.md:19–21`; F-13; P-04 (`g06`), P-14(e)
  > Reader v1 errors have exactly four keys: `code`, `error`, `ok` (`false`) and `schema` (`"v1"`).
- **Error envelope (ARCHITECTURE)** — `ARCHITECTURE.md:11`; F-24, F-13; P-01, P-02, P-14(e)
  > Errors: `engine/compat/errors.py::error_envelope` builds the governed `error_v1` envelope with keys `schema` (`"v1"`), `ok` (`false`), `code` and `error`, adding `details` only when a caller passes one (the Reader routes never do)
- **Retired `*_leader` identities as history** — `docs/contracts/reader_v1_public_bytes.md:31–33`; F-13, F-14; head and `9065e6f` reads (§6.2)
  > Before HDE-EPIC040-PR06a, the published schema and goldens used the category identities `open_leader`, `warm_leader`, `cool_leader` and `glow_leader`, and the schema permitted a `prompt` field. PR06a retired them from the contract, and no Reader route emits them.
- **Current release `1.3.0`, 45 members** — `README.md:13`; §3.1 admitted-release fact; P-03j
  > Release: the admitted release is `catalog/manifest.json` version `1.3.0` with 45 members (`release_id` `52be45584acbaa327da2d1cac724857dcdc999ca8c7a8f65108427942a4afe96`).
- **Current release (AGENTS)** — `AGENTS.md:97`; P-03j
  > Current release: `catalog/manifest.json` version `1.3.0`, 45 members.
- **`docs/server/reader_v1.md:42` correction** — `docs/server/reader_v1.md:54`; F-10, F-11, F-15; P-14(c) to P-14(e)
  > The production Reader is `POST /api/reader?v=1|2` (see "Current state (HDE-EPIC040)" above); `GET /api/reader` returns 405.
- **Dev `APP_ENV` behaviour stated truthfully** — `docs/server/reader_v1.md:17`; F-11; P-14(e)
  > When `APP_ENV` is set to a value other than `dev`, it returns 403 `ERR_READER_FORBIDDEN`; an unset `APP_ENV` is treated as `dev`.
- **C040-07 status** — `docs/contracts/reader_v2_public_bytes.md:8`; F-20; `docs/pfcanon/` unchanged since planning (§3)
  > Drainage: as of HDE-EPIC040-PR07, C040-07 has not been drained into `PF01-Canon-HDE-Math-Spec`, `PF04-Canon-HDE-Governance`, `PF05-Canon-HDE-CLI-API-Vendor-Ref` or `PF12-Canon-HDE-Schemas-and-Artifacts`, nor into the consequential statements of `PF14-Canon-HDE-Mechanics-Guide` and `PF29-Canon-HDE-Users-Guide`.
- **C040-08 status** — `docs/contracts/reader_v1_public_bytes.md:23`; F-20; as above
  > As of HDE-EPIC040-PR07, drainage of C040-08 into `PF01-Canon-HDE-Math-Spec` §2.3 and `PF04-Canon-HDE-Governance` §8.1.2, which still describe the envelope without `schema`, is pending with their maintainers.
- **C040-06 status** — `docs/INDEX.md:8`; F-20; as above
  > Drainage into `PF12-Canon-HDE-Schemas-and-Artifacts` §2.1 and `PF01-Canon-HDE-Math-Spec` §§6.1–6.2 is pending as of HDE-EPIC040-PR07.
- **CHANGELOG entry** — `CHANGELOG.md:3`; P-11
  > Unreleased — HDE-EPIC040: Separation Pass 3 final repository documentation (README/CHANGELOG/AGENTS/docs/)
- **Public surfaces (emitters)** — `docs/architecture/emitters.md:16`; F-10; P-14(e)
  > Public surfaces: the Reader endpoints (Reader v1, and since HDE-EPIC040 Reader v2, on `POST /api/reader`; the dev `GET /reader` is Reader v1) and `hdctl showcompat` share the presenter/emitter and remain the only public APIs.
- **Flask guide mount** — `FLASK_AUTO_RUN_GUIDE.md:136`; F-10; `adapter/factory.py:12`
  > app.register_blueprint(api_bp, url_prefix="/api")  # production Reader: POST /api/reader
- **Carried observations described, not fixed** — O-P06a-22 at `docs/contracts/reader_v2_public_bytes.md:19` and `docs/server/reader_v1.md:20`; O-12 at `README.md:132`; O-P06a-03 in the retired-identities note (`docs/contracts/reader_v1_public_bytes.md:33`); P-14(e), P-14(g)
  > Known limitation: a wheel built from this tree omits 16 of the 45 release members (for example the files under `schemas/` and `catalog/narratives/`), and admission fails closed unless every member is present with its recorded bytes, so run admission-dependent commands from a source checkout.

No second Canon catalog is created, and no Plan or Audit text is copied (P-06: no enumeration of the governed pairs, no 36-row copy).

## 7. Plan §11 checklist — PR-30 self-check

This is the PR session's own check against the plan. It does not replace the Codex code and security reviews that PR-35 reads on the pull request.

| Item | Evidence | Outcome |
| --- | --- | --- |
| Every edited line is one §6 names; no other line changed | re-application of §6 onto a fresh base reproduces all fifteen files byte-identically (§5); P-11 | holds |
| Every stated fact traces to a re-verified F-fact; every command executed as written | P-15 (§6.3), P-03, P-14, §6.2 re-verification | holds |
| Examples byte-equal to goldens and schema-valid; none presented as current release output | P-04; the examples are labelled synthetic and carry the synthetic 64-`a` `release_id` | holds |
| History labelled, not rewritten; corrected lines exactly §6's; `AGENTS.md` rules untouched | `docs/server/reader_v1.md` current-state block labels everything below it as retained history; `AGENTS.md` diff has zero deleted lines | holds |
| PF cited by exact title; addenda by heading and register ID; no PF version; no `docs/ephemeral/` link; no second canon | P-06 | holds |
| Drainage pending and time-bound; no QA, acceptance, deployment, activation, PF09 or closure claim | P-06 (§6.1) | holds |
| PR description follows the template and states §15's "What merging does" | written at publication, after this record; PR-35 verifies it on the pull request | pending at write time |
| No secret, credential or unredacted value; keys by name only | P-07 | holds |
| No real chart or personal data; fixture paths only as command arguments | P-07; examples are synthetic goldens | holds |
| No control weakened: closed rails default kept, refusals stated, governed 405s and `no-store` errors kept | P-03e, P-14(e); text of §6.3 quotations | holds |
| Dev `APP_ENV` behaviour stated truthfully | `docs/server/reader_v1.md:17`; P-14(e) | holds |
| No protection claimed that the implementation lacks | admission limits and writer non-atomicity stated (§6.3) | holds |
| No live vendor or database action | readiness tool run only in refusal modes; Reader probes by test client and a local helper without a database | holds |

## 8. In-flight decisions

| ID | What changed | Why it was necessary to deliver the approved scope | What was tested (test identity → outcome) |
| --- | --- | --- | --- |
| IFD-01 | P-12's "ends with exactly one LF" was applied as "ending unchanged from base" for `ARCHITECTURE.md`, `docs/ADAPTER_009.md` and `docs/server/reader_v1.md`. These three already end with a trailing blank line at `5a2b6a6`, and their endings were not edited | Plan §5.2 rule 7 forbids editing lines §6 does not name; normalizing those endings would edit an unnamed line in three files. P-12's purpose, that PR07 adds no formatting defect, is kept | P-12 → PASS (no CR, no ellipsis, fences balanced, the other twelve files end with exactly one LF, the three endings byte-equal to base); `git diff --check` → clean; P-10g `ci/checks/check_final_lf.sh` → exit 0 |
| IFD-02 | C3 (proofs on the working tree) and C4 (proofs on the committed head) ran as one pass on the committed head in a fresh detached worktree | The fifteen files were committed as the single documentation commit directly after C2, so the working tree equalled the commit and a separate working-tree pass would have proved identical bytes. Every proof passed on its first valid run, so no correction or amendment was needed | P-01 to P-15 on `757103c` → all PASS; doc proofs re-run → identical output; §6 re-application from base → 15 of 15 files byte-identical |
| IFD-03 | The working branch is this session's designated branch `claude/sleepy-clarke-igh9e7`, restarted locally from `main` at `5a2b6a6` under the same name. That name had carried planning PR #517, which merged as `5a2b6a6` and whose remote branch was deleted. The implementation pull request is a new pull request, not #517 | The session may push only to this branch, and a merged pull request is landed history that cannot carry the implementation. Restarting from `main` keeps exactly this plan cycle's new commits on the branch | `git log origin/main..HEAD` → the documentation commit only (then the records commit); P-11 → exact path set; `git ls-remote --heads origin claude/sleepy-clarke-igh9e7` → no remote branch before the publication push |

No decision changes the approved scope, a documented surface beyond §6, or any code, evidence or canon byte. None is material; no rescope is raised.

## 9. `PR_REMOTE_ACTION_LEDGER` and checkpoint

| Time (UTC, 2026-09-26; proof times are output-file times) | Action | Evidence / identity | Status |
| --- | --- | --- | --- |
| after 19:56:16Z | PR-30 entry and C0 recovery | §3; `main` `5a2b6a6` (#517 merged); no PR07 vehicle | done; entry time not captured more precisely |
| before 20:01:23Z | local branch `claude/sleepy-clarke-igh9e7` restarted from `origin/main` (IFD-03); C2 edits applied | 15 files | done (local) |
| 20:01:23Z | documentation commit | `757103c2ee1eaa2c916aa15739dc0dec9a3acf3a` | done (local) |
| 20:02:11Z | editable install re-pointed at the candidate worktree | `pip show` | done |
| 20:04:41Z | doc-level proofs | §6 | PASS |
| between 20:04:41Z and 20:06:57Z | first command-proof run | a scratch-runner defect put a nonexistent interpreter directory on `PATH`, so the rows ran under the system interpreter and failed for missing modules; not a documentation defect; the runner was corrected and every row re-run | discarded; not evidence |
| 20:06:57Z to 20:08:17Z | command proofs P-03, P-08, P-09, P-10, P-13, P-14(a to c, e, f) | §6 | PASS, worktree clean |
| 20:09:29Z | P-14(d) live helper and curl | §6.2 | PASS; helper stopped |
| 20:10:03Z | P-14(g) wheel | §6.2 | PASS |
| 20:10:52Z | doc-level proofs re-run | byte-identical output | PASS |
| after 20:10:52Z | §6 re-application from base; supplementary head reads | §5, §6.2 | PASS |
| after 20:17Z | records commit carrying this record | its identity cannot be written into its own bytes | local; published by the next action |
| next | P-11/P-12 on the records commit; one push creating the remote branch; one pull request opened against `main` | provider evidence postdates this record | recorded by the PR-30 return and PR-35's entry checkpoint |

| Ledger field | Value at write time |
| --- | --- |
| Local checks | §6, all PASS on `757103c` |
| Commits | documentation `757103c`; records commit (this file) |
| Pushes | none yet; exactly one planned (both commits) |
| PR creation / reuse | none yet; one new pull request planned; #517 is landed history and is not reused |
| Review reads and finding dispositions | none (PR-35) |
| CI runs | none yet. `ci.yml` runs on `pull_request` (paths under `docs/ephemeral/`, `docs/pfcanon/`, `docs/graph/` and `docs/prompt_ecosystem_management/` ignored) and on push to `main`; opening the pull request starts the single `test` job, expected `documentation_only` (P-09); cancellation of superseded runs is pull-request-only |
| Stale / cancelled runs | none |
| Remote head | none (remote branch absent) |
| Mergeability | not yet observable |
| Remaining useful local action | none after publication |
| Next evidence action | PR-35: subscribe, read Codex code and security reviews, current-head CI, mergeability |

## 10. Not executed and not established

| Item | Reason / owner |
| --- | --- |
| Pull-request number, pushed remote head, first check state | postdate this record (§1); recorded by the PR-30 return; PR-35 advances this checkpoint |
| Codex code review and security review; review-thread resolution | PR-35 |
| Current-head CI and mergeability | PR-35 |
| `tests/reader_v1/test_cli_proof.py` | not run; pre-existing failure O-P06a-03, excluded from the P-13 roster by the plan |
| Readiness tool against a database | never run; only its refusal modes (P-03d, P-03e) |
| Production `POST /api/reader` success over HTTP | not exercised; it needs a database. The success path is covered by the P-13 roster through the tests' injected seams |
| QA verdict, acceptance, OPS01 attestation, deployment, activation, PF09 movement, C040-06/07/08 drainage, Epic closure | outside PR07; not executed and not established |

## 11. Carried register, observations and IA routing

### 11.1 `CANON_CONFLICT_REGISTER`

Carried unchanged from plan v1.0 §13.1, which carries Plan v2.1 §11, Plan Review v2.1 §6, PF10 §§2.2 to 2.5, 2.23, 2.25, 2.26 and the instruction §11: C040-01 to C040-04 `CANON_RECONCILIATION` / `APPROVED` (Thoth-17, 2026-09-08T13:23:24Z); C040-05 `CANON_RECONCILIATION` / `APPROVED`, alternative A (Isis-49, 2026-09-09T03:57:16Z); C040-06 `NEW_CANON` / `APPROVED`, alternative A (Isis-50, 2026-09-09T11:48:08Z); C040-07 `NEW_CANON` / `APPROVED` by the Product Owner, 2026-09-26 (PF10 §2.23); C040-08 `CANON_RECONCILIATION` / `APPROVED`, alternative A (the retained whole-change IA by Product Owner direction, 2026-09-26; PF10 §2.25). No entry is reopened, relabelled, omitted or newly decided; no new entry is proposed. PR07 documents C040-06, C040-07 and C040-08 by pointer, with drainage pending as of HDE-EPIC040-PR07 (§6.3); drainage stays with the PF maintainers.

### 11.2 Code and design defects routed to the whole-change IA (non-gating)

As the Product Owner directed at PR-20 ("Code or design defects found go to the whole-change IA and return to this session"), these stay routed to the retained whole-change HDE-EPIC040 IA through the plan (§14.2), this result and the PR-40 lineage review. PR-30 re-observed each at the head (§6.2) and fixed none:

| ID | Observation | Re-observed at `757103c` | Owner route |
| --- | --- | --- | --- |
| O-P07-01 | `hdctl --help` says `showcompat` emits Reader v1 bytes; stdout is `magic10_compat_result.v1` | yes | whole-change IA; CLI / PF05 owner. Labelled at the point of use in `docs/CLI_commands.md` |
| O-P07-02 | `aux-preview --band` is not applied when the pair file carries the band | yes (`--band Glow` → `Cool` narrative, exit 0) | whole-change IA; CLI / narratives owner |
| O-P07-03 | `dev/reader_harness/app.py` raises `AttributeError` at import | yes (P-14(f)) | whole-change IA; PF02 / dev-harness owner. Labelled "not a start path" |
| O-P07-04 | dev `GET /reader` treats an unset `APP_ENV` as `dev` | yes (P-14(e)) | whole-change IA; HTTP transport / PF05 owner. Stated truthfully |

O-P07-05 to O-P07-09 (plan §13.2) are carried unchanged with their owners. The accepted-unit observations O-P06a-22, O-12 and O-P06a-03 are described where a documented surface meets them (§6.3); O-P06a-23 and O-P06b-17 are not documentation surfaces and are recorded here only. None is fixed by PR07.

## 12. Constraints and unresolved items

| Item | Owner |
| --- | --- |
| Review, CI and merge readiness of the published candidate | PR-35 (its own dedicated session) |
| Merge | Nathan / Product Owner, manually |
| Landed-lineage review after the merge | PR-40 |
| O-P07-01 to O-P07-04 decisions; any decision that changes a documented surface before PR07 merges returns to this dedicated PR07 lineage for a successor plan | whole-change HDE-EPIC040 IA |
| C040-06, C040-07, C040-08 drainage into PF01, PF04, PF05, PF12 (and consequential PF14, PF29) | the PF maintainers |
| O-P07-08 (PF10 v13.3.7 index omits §2.26; §2.11 line 1373 stored truncated) and O-P07-09 (`AGENTS.md` PF10 section-number citations) | Nathan |
| OPS01 on the clean final candidate after PR07 merges | OPS01 owner (Plan §6.8; PF10 §2.25) |
| Prompt-use provenance repository persistence | authorized repository writer once a procedure is installed (§13) |

## 13. Prompt-use provenance

`GCFPE_PROMPT_USES`: `GCFPE-USE-HDE-EPIC040-PR-30-20260926-PR07-01`. Prior entries carried by reference: `GCFPE-USE-HDE-EPIC040-PR-20-20260926-PR07-01` (plan §16), `GCFPE-USE-HDE-EPIC040-PR-10-20260926-PR07-01` (instruction §12), `GCFPE-USE-HDE-EPIC040-PR-40-20260926-PR06b-01`, `GCFPE-USE-HDE-EPIC040-PR-40-20260926-PR06a-01`.

- Prompt: PR-30 — PR Implementation Proceed — 091426.1, `https://app.notion.com/p/3db4590a05eb8123afb8caeeaa83a294?pvs=204` (page as of 2026-09-24T15:47:45.499Z; Notion read only).
- Release: GCFPE-20260914.1 / 091426.1 / 55 members.
- Change / unit: HDE-EPIC040 / HDE-EPIC040-PR07; Specification v1.1; instruction v1.0; plan v1.0.
- Role / stage: dedicated PR07 PR-development session / PR-30.
- Captured: 2026-09-26T20:17Z.
- Execution identity: harness session `https://claude.ai/code/session_01UrEaEb4uQkqq2zHD7VTYyc`.
- PF10 read: v13.3.7 (`af292883d5d4f27bd5cc510117e29b044ec2ac0b0f522df48fd0022010c6855c`).
- Result, commit and PR references: the documentation commit `757103c` exists and is recorded; the records commit and the pull request postdate these bytes (§1).
- Repository persistence: `docs/changes/GCFPE_PROMPT_PROVENANCE.md` is absent at `5a2b6a6` (the directory holds only `AUDIT_RESULTS.json` and `AUDIT_SUMMARY.md`); `PENDING / NON_GATING`; owner: the authorized repository writer once a procedure is installed.

## 14. PR-35 continuation

- Receiver: PR-35 — Resolve PR Reviews and Reach Merge Readiness — 091426.1, `https://app.notion.com/p/3db4590a05eb8120b443ed2cb08b723c?pvs=204`, in its own dedicated top-level session (`session_disposition: NEW_DEDICATED`), entered from the PR-30 handoff that Nathan pastes.
- Inputs by repository path: this record; `docs/ephemeral/HDE-EPIC040-PR07-pr-implementation-plan-v1.0.md`; `docs/ephemeral/HDE-EPIC040-PR07-pr-instruction-v1.0.md`; `docs/ephemeral/HDE-EPIC040-implementation-plan-v2.1.md` (§6.7); `docs/ephemeral/HDE-EPIC040-PR06a-PF10-build-notes-addendum-v1.0.md` (PF10 §2.23); `docs/ephemeral/HDE-EPIC040-PR06b-PF10-build-notes-addendum-v1.0.md` (PF10 §2.25); `docs/pfcanon/PF10-HDE-Build-Notes-v13.3.7.md`; the pull request opened from `claude/sleepy-clarke-igh9e7` at publication.
- Obligations carried from plan §17.1: review retrieval and correction; local re-proof of any corrected line (the affected P-rows of §6); coherent corrective pushes; CI economy (this PR's CI is `documentation_only`); current-head identity; required checks or a valid waiver; mergeability; a security review on the corrected head where a correction lands; code-fix requests routed to the whole-change IA (plan R-08), not pushed; the pull-request number and remote head recorded in PR-35's entry checkpoint; no merge.

## 15. State summary

| Item | State |
| --- | --- |
| This record | `PR_CANDIDATE_PUBLISHED` (§1) |
| Documentation commit | `757103c2ee1eaa2c916aa15739dc0dec9a3acf3a` on `claude/sleepy-clarke-igh9e7`, parent `5a2b6a6` |
| Local proofs P-01 to P-15 | PASS on `757103c` |
| In-flight decisions | IFD-01 to IFD-03 (§8); none material |
| Boundary finding / rescope | none; `PR_RETURN_PHASE` not applicable |
| Code/design defects O-P07-01 to O-P07-04 | routed to the whole-change IA; non-gating |
| Codex reviews, current-head CI, mergeability, merge readiness | `NOT YET EVALUATED` (PR-35) |
| Merge | Nathan's manual action; not performed |
| QA, OPS01, acceptance, activation, deployment, PF09, C040 drainage, closure | `NOT EXECUTED` / `NOT ESTABLISHED` |
| Provenance persistence | `PENDING / NON_GATING` |
