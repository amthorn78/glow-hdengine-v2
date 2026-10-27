---
artifact_type: PR_WORK_UNIT_LINEAGE_REVIEW
artifact_id: HDE-CRD-0002-WU-PR-08-PR-WORK-UNIT-LINEAGE-REVIEW
artifact_version: "1.0"
decision: ACCEPT
progression: TERMINAL_PRODUCT_OWNER_RETURN (the next ordered unit, WU-DOC-01, needs its business case before DOC-10; §10)
predecessor: none (the first PR-40 review of WU-PR-08)
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-08
work_unit_title: "Environment template and operator documentation (PR; Coagulation; S16, S17)"
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-08-pr-instruction-v1.0.md (v1.0, INSTRUCTION_READY; blob e2c9f0ae1337; landed by #685)
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-08-pr-implementation-plan-v1.0.md (v1.0; the Product Owner's PR-30 Proceed for exactly v1.0; landed by #686 as 977a9c7), with its companion docs/ephemeral/HDE-CRD-0002-WU-PR-08-pr-implementation-plan-v1.0-prototype.diff (sha256 954a7881…)
PR_30_RESULT_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-08-pr-implementation-result-v1.0.md (PR_CANDIDATE_PUBLISHED)
PR_35_RESULT_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-08-pr-implementation-result-v1.2.md (final PR-35 checkpoint; its §5 success outcome occurred, so MERGE_PENDING holds for head d37090e as historical pre-merge evidence); v1.1 (MERGE_PENDING for bf32d20, withdrawn by v1.2) in the same lineage
PR_REFS: amthorn78/glow-hdengine-v2#687 (the unit's one PR)
entry_event: the Product Owner's fallback PR-40 handoff, pasted after he merged #687 by hand; no MERGE_OBSERVED result reached this session. The handoff's added context (the confirming run 39697136314 succeeded on d37090e; Codex reviewed that head with no findings) was verified independently (§3, §6, §7)
reviewer: the continuing whole-change HDE-CRD-0002 Implementation Agent, read-only PR-40 role, session "HDE-CRD-0002-2" (https://claude.ai/code/session_01U3QLYTkfUepeRbSGZNPj9N)
reviewer_independence: this session authored WU-PR-08's instruction v1.0 (PR-10) and no plan, code or result record of the unit
sessions_reviewed: PR-20/PR-30 https://claude.ai/code/session_01QezXHuju1GXwpubx7zDvTA; PR-35 https://claude.ai/code/session_01VASdh3cjEKqEVYa35EwCEn
return_owner: the whole-change IA for Plan progress; the Product Owner for the decision of §10
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
prompt: PR-40 — Review PR Work-Unit Lineage — 100926.1 (https://app.notion.com/p/3f44590a05eb81088487e918fd642a7f; page state of 2026-10-12T02:29:38.234Z, fetched and read in full in this invocation)
prompt_release: GCFPE-20261009.1 / 100926.1
repository_state_reviewed: origin/main 1a4c8abbd2acc34c6c80dd0e90df99295df3f630 (tree c2a11824cfcd), the merge commit itself; no later commit on main at review time
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.7.1.md (sha256 eab61385a819c859e1cf2743a204b70813feef23c902f647b3a5d7141454114d; unchanged since 7b763db)
pf10_addendum_created: none (PR-40 is not a qualifying approval prompt)
canon_conflict_register: CR-1 to CR-8 carried unchanged, all decided; no new entry (§11)
created_at: 2026-10-22T00:32:39Z
---

# HDE-CRD-0002 WU-PR-08 — PR work-unit lineage review v1.0 (PR-40)

## 1. Decision

**ACCEPT.** WU-PR-08 (requirements S16 and S17) is delivered with sufficient attributable evidence by pull request #687. It merged on 2026-10-22T00:26:03Z as squash commit `1a4c8ab`, whose tree equals the PR's final head `d37090e`.
- **Behaviour.** `.env.example` has `GEO_API_KEY`. Every readiness and port statement S17 corrects matches the code on `main`, re-checked by this review against the running apps (§5). `.env.example` is a classified CI surface.
- **Exactness.** The landed change outside `docs/ephemeral/` is the proceeded plan's prototype diff, byte for byte (§4).
- **Reviews.** Codex reviewed all three PR heads with no findings. There were no review threads, so no P1 was raised or declined (PF10 addendum 2.14; §6).
- **CI.** All seven lanes are green on the exact final head, ending `CI_APPLICABILITY_AND_EXACT_HEAD_OK` (run 39697136314; §7). One earlier run on identical code failed on a test outside the unit; its cause and fix are routed (§8, PR35-C1).
- **Measure** (business case, decision record §2): met (§5).

**Next stage: not runnable yet.** The next ordered unit is WU-DOC-01, through DOC-10. Its business case is due before DOC-10 (addendum 2.18), and none is on record. The decision returns to the Product Owner (§10). This is a terminal return, with no continuation block.

ACCEPT is this review's lineage result only. It is not QA, acceptance of the change, Ops, deployment or closure.

## 2. Identity and lineage

| Item | Identity |
| :- | :- |
| Specification | `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` v1.1, with Specification delta 01 (`docs/ephemeral/HDE-CRD-0002-specification-delta-v1.0.md`, DELTA_APPROVE) |
| Implementation Audit | `docs/ephemeral/HDE-CRD-0002-implementation-audit-v1.0.md`, §6 S16 and S17 |
| Implementation Plan | `docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md` (review v1.1, INITIAL_APPROVE), with Plan delta 01 v1.1 (`docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-v1.1.md`, DELTA_APPROVE by review v1.1 of the delta; addendum record 2.19). P-7 is this unit's block |
| Business case | `docs/ephemeral/HDE-CRD-0002-WU-PR-08-po-disposition-scope-v1.0.md` §2, with no cost ceiling (addendum 2.18) |
| Instruction, plan, results | as the header names them |
| Proceed | the Product Owner's PR-30 Proceed for exactly plan v1.0 (result v1.0 front matter); no second Proceed |
| Product Owner direction in PR-35 | PO-35-1: push the result record to the PR's branch (result v1.1 §7) |

## 3. Merge state and landed lineage

| Item | Evidence |
| :- | :- |
| PR #687 | `merged: true`, `merged_by: amthorn78`, `merged_at: 2026-10-22T00:26:03Z`; base `main` `977a9c7`; head `claude/awesome-einstein-ig69r1` at `d37090e` |
| Merge commit | `1a4c8abbd2acc34c6c80dd0e90df99295df3f630`, a squash with one parent, `977a9c7`; author `amthorn78`, 2026-10-22T00:26:03Z |
| PR commits, in order | `9b93cf0` (implementation, PR-30), `bf32d20` (result v1.0), `e1cb6d1` (result v1.1), `d37090e` (result v1.2) |
| Tree identity | `1a4c8ab^{tree}` = `d37090e^{tree}` = `c2a11824cfcd`; `git diff d37090e 1a4c8ab` is empty |
| `main` after the merge | `1a4c8ab` is `main`'s head at review time; no divergence |

## 4. Attribution

- **All of `977a9c7..1a4c8ab` is attributable to #687:** six files, +526/−10.
  - **Unit files:** `.env.example` (+1), `ci/checks/classify_ci_changes.py` (+3) and `docs/ADAPTER_009.md` (+7/−10).
  - **Records:** result v1.0, v1.1 and v1.2 under `docs/ephemeral/`.
- **Exactly the proceeded plan.** `git diff 977a9c7 1a4c8ab -- . ':(exclude)docs/ephemeral'` has sha256 `954a7881fbdcf688826bdf41f4da593fc7ea9430529709c1e37cfa3024745acb`. That equals the plan's companion prototype diff (`docs/ephemeral/HDE-CRD-0002-WU-PR-08-pr-implementation-plan-v1.0-prototype.diff`), byte for byte.
- **No change after PR-30's commit.** `9b93cf0` is the only commit touching the unit files. The three later commits add only `docs/ephemeral/` records, so PR-35 made no correction.
- **Since the instruction's baseline:** `67adb68..1a4c8ab` outside `docs/ephemeral/` changes exactly the three unit files.
- **Not attributable to this unit:** nothing landed outside the PR.

## 5. Requirement coverage on `main` (`1a4c8ab`), checked by this review

Checks ran in a throwaway clone at `1a4c8ab`, closed rails (`env -i`; `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 PYTHONDONTWRITEBYTECODE=1`; `APP_ENV` as stated), on CPython 3.12.3 with CI's requirements installed. The clone ended clean (`git status --short` empty).

| Acceptance (P-7) | Check | Result |
| :- | :- | :- |
| (1) `.env.example` has a `GEO_API_KEY` entry and nothing else changed | `git diff 977a9c7 1a4c8ab -- .env.example` | one added line, `GEO_API_KEY=changeme`; lines 1 to 3 unchanged. **Met** |
| (2) readiness statements as implemented, naming the app; port statements match the runner and `Procfile` | the statement map below, against the code and the test client | **Met** |
| (3) admission `1.3.0`, 45 members, the base's `release_id` | `load_active_mechanics_bundle()`; `ADMITTED_RELEASE_VERSION`; `ADMITTED_RELEASE_ROSTER`; `identity._manifest_release_id()`; `scripts/release_id_recompute.py --check-manifest-only` | admission ok; `1.3.0`; 45; `77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e`; recompute exit 0. **Met** |
| (4) `.env.example` alone classifies | `classify_paths(['.env.example'])` | `documentation_only`, no lanes, no `CI_CHANGE_SURFACE_UNCLASSIFIED`. **Met**. The classifier itself still selects all seven lanes |
| (5) all seven lanes green on the exact PR head with `CI_APPLICABILITY_AND_EXACT_HEAD_OK` | run 39697136314 on `d37090e` (§7) | **Met** |

**Statement map** (plan v1.0 §6), each re-checked against `main`:

| # | Corrected statement on `main` | Evidence on `1a4c8ab` |
| :- | :- | :- |
| R-1 (line 6) | readyz "always 200 `{"ok":true,"schema":"v1"}`; no dependency check, no smoke" | `adapter/wsgi.py` lines 47–51; test client: `adapter.wsgi` 200 with that body, under `APP_ENV=dev` and `prod` |
| R-2 (line 22) | "/internal/readyz performs no override check; config/runtime_overrides.json does not change its response" | test client, `APP_ENV=prod`, with `config/runtime_overrides.json` present: 200, same body |
| R-3 (line 33) | "/internal/readyz adds no header of its own (no X-Toggles-SHA)" | the prod response's headers are `Cache-Control`, `Content-Length`, `Content-Type`, `Referrer-Policy`, `Strict-Transport-Security`, `X-Adapter-Version`, `X-Content-Type-Options`, `X-Correlation-Id`, `X-Engine-Tag`, `X-Frame-Options`, `X-Release-Id`. No `X-Toggles-SHA` |
| R-4 (lines 46–48) | registered only by `adapter.wsgi:create_app()`, exposed as `adapter.app:app`; the production app and the dev Reader answer 404; unconditional 200 | test client: `adapter.factory` 404 and `adapter.http_reader` 404, under dev and prod; `adapter/app.py` exposes `create_app()`; `Procfile` runs `adapter.factory:create_app()` |
| P-1 (line 119), P-2 (line 135) | `http://127.0.0.1:8000`; loopback on `$PORT` when set (default 8000) | `adapter/http_reader.py` lines 1320–1321 (`host="127.0.0.1"`, `port=int(os.environ.get("PORT", "8000"))`); `scripts/dev_start_reader.sh` line 10 (`PORT:=8000`) |
| Line 146, unchanged | production `--bind 0.0.0.0:$PORT` | `Procfile` |

**Live probes.** PR-30 (`9b93cf0`) and PR-35 (`bf32d20`) ran live probes from the operator's shell on code identical to `main` (result v1.0 §3; result v1.1 §4). This review relied on the test client and the source rather than repeating them.

**Measure** (decision record §2: "`.env.example` has a `GEO_API_KEY` entry …, and each statement S17 corrects matches the code on the merged head"): **met**, by acceptance (1) and the statement map. Addendum 2.18 rule 5 asks PR-40 to record this.

**Other obligations.**
- *Interfaces:* no route, payload or behaviour changed (`/internal/readyz` unchanged); contract F-3 holds.
- *Tests:* none added, as plan PD-2 decided (no test enumerates the changed registry).
- *Documentation:* `docs/ADAPTER_009.md` only, within S17's bound.
- *Dependencies:* after WU-PR-07, as P-7 orders.
- *Security:* a placeholder value only; no secret in any record.
- *Recovery:* PR-30 recovered before creating (result v1.0 §2).

## 6. Reviews and the addendum 2.14 check

- **Codex code review:** the summary comment (6328780869) records the latest review, of `d37090e`. It completed 2026-10-22T00:02:50Z, trigger "New commits", `has_any_findings: false`, `has_unresolved_findings: false`.
  - The earlier rounds are recorded in the PR-35 records: `9b93cf0` (no findings, result v1.1 §2) and `e1cb6d1` (no findings, result v1.2 §4).
  - The code reviewed is the same in all three rounds.
- **Review threads:** 0. **Formal reviews:** 0. **Issue comments:** the Codex summary and PR-35's one standing-down comment on the failed run (6329297225).
- **Addendum 2.14:** no P1 was raised, so none was declined. **Addendum 2.11 rules 7 and 8:** no finding needed a disposition, and no repeated class arose.
- **Codex security review:** not in the chain (addendum 2.3). Its empty row is no gap.

## 7. Hosted CI

| Run | Head | Result |
| :- | :- | :- |
| 39693139601 | `bf32d20` | success, seven lanes (result v1.1 §5) |
| 39695867041 | `e1cb6d1` | failure in the changed-tests step: 1 failed, 4,520 passed, 2 skipped. The test was `tests/tools/test_prepush_check.py::test_build_notes_requires_exactly_one_file[names2-False]`, outside the unit (result v1.2 §2; §8 PR35-C1) |
| **39697136314** | **`d37090e`** (final head) | **success**, read by this review below |
| 39699657729 (push to `main`) | `1a4c8ab` | in progress at 00:30:30Z, when this review was written. Its tree is the one 39697136314 tested; the review does not depend on it |

**Run 39697136314**, job 119557151090:
- `event: pull_request`; `HEAD_SHA` `d37090ed0aebb3241e7bc75c19eecb50fcd74bde`; `BASE_SHA` `977a9c7…`.
- Image `ubuntu-26.04` 20261018.168.1; git 2.55.0. It ran 00:01:40Z to 00:22:17Z.
- The whole job log was retrieved (920 of 920 lines) and scanned in full. The classification, the counts and the final step were read directly:
  - `CI_CHANGE_CLASSIFICATION:event=pull_request;reason=selected_lanes;paths=6;lanes=product,compat,db,rails,evidence,qa,release`;
  - changed tests: 4,521 passed, 2 skipped;
  - product 77; compat 119 passed, 3 skipped, 2 xfailed; db 269; rails 120, 113, 155 and 138; evidence 134; qa 488; release 79;
  - every final-step outcome `success`; the step printed `CI_APPLICABILITY_AND_EXACT_HEAD_OK`.

## 8. Findings, observations and owners

No finding against the landed work.

| ID | Item | Owner |
| :- | :- | :- |
| PR35-C1 | **A test-fixture race in WU-PR-06's `tests/tools/test_prepush_check.py`.** Its `IDENTITY` (line 33) does not disable git auto-maintenance. On the runner's git 2.55.0, a detached maintenance child can change `.git/objects` during the test's read-only snapshot (result v1.2 §3, a probable cause from the log and git's documentation). It failed once on hosted CI, a real input under addendum 2.11 rule 4(b). WU-PR-06 is accepted-final and is not reopened. The proposed patch, untested, adds `"-c", "maintenance.auto=false"` to `IDENTITY` | Product Owner, as a later-change candidate |
| LR8-F1 | **Plan F-1: the override guard sees `app.config`, not the environment.** `adapter/wsgi.py` line 20 calls `validate_or_fail(app)`. `_as_mapping` (`adapter/env_guard.py` lines 82–95) returns `app.config` for a Flask app, so the prod refusal never sees the process environment. `adapter.factory` does not call the guard. Confirmed by reading the code. The document makes no claim about the guard (plan PD-4) | Product Owner, as a later-change candidate |
| LR8-F2 | **Plan F-2 and instruction ID-8: stale statements in `docs/ADAPTER_009.md` outside S17's bound.** Lines 7 and 8 list `/internal/version` twice; line 20 says "localhost"; the `ENGINE_ENV` line (now 51); the start line with an install prefix (now 143 to 147); the capture environment without `APP_ENV=dev`; `TOGGLES_SHA`; `X-Release-Id`'s default; and the Bearer statement | WU-DOC-01, through its DOC-10 instruction |
| LR8-O1 | O-19 (`scripts/make_release_pack.sh` writes a non-canonical `artifacts/release_id.txt`): its documentation side | WU-DOC-01; any code change, the Product Owner |
| LR8-O2 | The carried hazards OBS-P4-5 and OBS-P4-7 did not occur on #687 | carried as before |

## 9. Carried items (instruction ID-7)

- **Loopback bind statements:** met (P-1, P-2).
- **OBS-P4-5:** a hazard only; no such test was added.
- **O-19:** LR8-O1.
- **F-3:** holds; no route changed.
- **Not carried, as decided:** addendum 2.10's `1.4.0` cut and addendum 2.6's purity-report regeneration (Plan delta 01, K-1 and K-2).

## 10. Next stage and the decision returned to the Product Owner

- **The next ordered unit is WU-DOC-01** (Plan v1.1 §7, as Plan delta 01 P-8 amends its scope): "Final repository documentation (DOC; after WU-PR-08)". Its block says "Dependencies and order. Ninth; after WU-PR-08 merges", which is met. It is a final documentation unit without instructions, so its stage is **DOC-10** (PR-40, "Resolve the next approved Plan stage").
- **Why it cannot start.** Addendum 2.18, "Epic, task, and status effects", says WU-DOC-01's business case is due before DOC-10. It states beneficiary, evidence, benefit and measure. No such record exists on `main`. The next stage after it, WU-OPS-01, has the same prerequisite, before OPS-10.
- **Decision returned to the Product Owner:** WU-DOC-01's business case. To support it, the documentation gaps measured on `main` at `1a4c8ab`:
  - `README.md` does not mention `tools/ci/prepush_check.py`, the pre-push check WU-PR-06 delivered;
  - `AGENTS.md` names only `schemas/epic_close_candidate_source.v1.json`, while WU-PR-07 delivered `schemas/close_candidate_source.v2.json`, which accepts CRD identities;
  - `docs/EVIDENCE_INDEX.md` has no HDE-CRD-0002 entry;
  - `CHANGELOG.md` has no HDE-CRD-0002 entry;
  - the items routed to WU-DOC-01 (LR8-F2, LR8-O1, and the items earlier lineage reviews carried: the H-4 usage note, the start command and bind, OBS-P3-12, LR3-O4, F-3, O-19).
- **A draft for the Product Owner to adopt, change or reject.** It is not decided here:
  - *Beneficiary:* agents and operators who take repository workflow from `AGENTS.md` and `README.md`. Every later PR session reads `AGENTS.md`.
  - *Evidence:* the four gaps above.
  - *Benefit:* a session following `AGENTS.md` and `README.md` uses the tools HDE-CRD-0002 delivered, the pre-push check and the v2 close-pack source, rather than an outdated description.
  - *Measure:* each statement WU-DOC-01 changes matches merged `main`, checked at DOC-20.

  Whether this meets addendum 2.11 rule 2 is the Product Owner's call: a document gap is a business case only where someone would act wrongly on it.
- **Resume point:** when the business case is recorded, the next stage is DOC-10 for WU-DOC-01, run by this IA.

## 11. Canon-conflict register

`CANON_CONFLICT_REGISTER` is carried unchanged:
- CR-1, CR-2 and CR-3: APPROVED_AS_CHANGED (Thoth).
- CR-4: APPROVED, and CR-5: APPROVED_AS_CHANGED (Product Owner).
- CR-6: APPROVED (a) (this IA through RS-20).
- CR-7 and CR-8: APPROVED (a) each (Product Owner).

No new conflict. Plan v1.0 §19 records why HDE Architecture §3.4's speculative readiness concept is consistent with the corrected document.

## 12. NOT PRODUCED and NOT EXECUTED

- **NOT PRODUCED:** a QA artifact, an Ops record, a close pack, a PF10 addendum, a WU-DOC-01 instruction or business case.
- **NOT EXECUTED:**
  - a live probe from the operator's shell (PR-30 and PR-35 ran them on identical code);
  - the full local replay (the hosted run on the final head was read instead);
  - the test suites (the hosted run covers them).
- **Pending at writing:** the `main` push run 39699657729.

## 13. TypeSafe reading

**TypeSafe: not read.** The result is a terminal return to the Product Owner with no receiving session to score. A reading belongs to the record that hands off DOC-10, once it is runnable. Nathan's pick for this PR-40 session is not stated; its reading is result v1.2 §8.

## 14. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / WU-PR-08 / PR-40 / lineage review 1 |
| change / specification | CRD HDE-CRD-0002 / `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` v1.1, with Specification delta 01 |
| work unit | WU-PR-08 (S16, S17) |
| release | GCFPE-20261009.1 / 100926.1 |
| prompt | PR-40 — Review PR Work-Unit Lineage — 100926.1, https://app.notion.com/p/3f44590a05eb81088487e918fd642a7f (page state of 2026-10-12T02:29:38.234Z) |
| role/stage | continuing whole-change IA / PR-40 |
| capture time | 2026-10-22T00:32:39Z |
| execution identity | https://claude.ai/code/session_01U3QLYTkfUepeRbSGZNPj9N |
| inherited usage | results v1.0 to v1.2 (sessions 01QezXHuju1GXwpubx7zDvTA and 01VASdh3cjEKqEVYa35EwCEn); plan v1.0; instruction v1.0 |
| repository persistence | recorded here only (`docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent on `main`; pending, non-gating) |

## Canon relied on

Read on `main` at `1a4c8ab`. `docs/pfcanon/` was last changed by `7b763db` (PF10 v13.7.1).

| Decision topic | Sources and sections |
| :- | :- |
| Review operation, decision, next stage, terminal return | PR-40 — Review PR Work-Unit Lineage — 100926.1, read in full: "Resolve the next approved Plan stage"; "Execute" 1 to 10; "Required result"; "Terminal operator return"; "Accepted-final lineage protection" |
| Unit scope and acceptance | Plan delta 01 v1.1 P-7 and P-8, and its addendum record (2.19), read in full for PR-10 in this session; instruction v1.0 (this session's own) |
| Measure; no ceiling; the WU-DOC-01 business case due before DOC-10 | PF10-HDE-Build-Notes v13.7.1 addendum 2.18: rule 5 and "Epic, task, and status effects", read in full in this session; addendum 2.11 rules 1 to 8, read in full in this session (rule 2 for the draft business case; rule 4(b) for PR35-C1) |
| P1 check; finding disposition | addendum 2.14 rules 1 to 6; addendum 2.11 rules 7 and 8, read in full in this session |
| Review chain | addendum 2.3, read in full in this session |
| Accepted-final WU-PR-06 not reopened (PR35-C1) | PR-40 "Accepted-final lineage protection" |
| CI shape and marker | `AGENTS.md` "HDE-EPIC039 current workflow posture" |
| Release identity unchanged | `AGENTS.md` "Release identity" and "HDE-EPIC040 current posture" |
| Dev access address | PF06-Canon-Change-Process-Guide v2.5.4 §0.6.1, the access-address bullets, read in full in this session |

**In-flight documents read in full for this review:** results v1.0, v1.1 and v1.2; plan v1.0; the instruction v1.0.

**Repository read at `1a4c8ab`:**
- the three unit files and their diff;
- `adapter/wsgi.py`, `adapter/app.py`, `adapter/env_guard.py` lines 79–105 and `adapter/http_reader.py` lines 1316–1324;
- `scripts/dev_start_reader.sh` and `Procfile`;
- `tests/tools/test_prepush_check.py` line 33 and its `git log`;
- the gaps of §10 in `README.md`, `AGENTS.md`, `docs/EVIDENCE_INDEX.md` and `CHANGELOG.md`.

**GitHub read:**
- #687: details, commits, check runs, reviews, review threads and issue comments;
- run 39697136314 and its full job log;
- the `main` push run 39699657729.
