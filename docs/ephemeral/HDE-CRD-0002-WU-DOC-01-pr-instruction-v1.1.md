---
artifact_type: PR_INSTRUCTION
artifact_id: HDE-CRD-0002-WU-DOC-01-PR-INSTRUCTION
artifact_version: "1.1"
artifact_state: INSTRUCTION_READY
predecessor: docs/ephemeral/HDE-CRD-0002-WU-DOC-01-pr-instruction-v1.0.md (v1.0, INSTRUCTION_READY; blob c49ff720ffd2). Preserved unchanged; this version is its complete successor for plan cycle 3
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
DOCUMENTATION_UNIT_ID: WU-DOC-01
work_unit_title: "Final repository documentation (DOC; after WU-PR-08)"
plan_cycle: 3 (bounded corrective pass for DOC-20 findings DC-1 and DC-2)
AUTHORING_CONTEXT: APPROVED_BASE_WITH_OVERLAYS
immutable_approved_base: Specification v1.1 (approved) → Implementation Plan v1.1 + IA-30 review v1.1 (approved)
applicable_overlays: (1) Specification delta 01 (DELTA_APPROVE), PF10 addendum 2.20; (2) Implementation Plan delta 01 v1.1 (DELTA_APPROVE), PF10 addendum 2.19, whose P-8 sets this unit's bounded scope; (3) PF10 addendum 2.21, which routes the stale-document list to this unit; (4) PF10 addendum 2.17, which the writer nonclaim (DC-1) reads with the S21 ADR; (5) PF10 addendum 2.18 (no cost ceiling; the measure)
SPECIFICATION_REF: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (v1.1; blob c4802a5a7fa3), with Specification delta 01 docs/ephemeral/HDE-CRD-0002-specification-delta-v1.0.md
IMPLEMENTATION_PLAN_REF: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (v1.1; blob abffa2ccbd44) §7 WU-DOC-01, with Plan delta 01 docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-v1.1.md (v1.1) P-8
PLAN_REVIEW_REF: docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (IA-30 INITIAL_APPROVE; blob 0cc0276524b2), with docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-review-v1.1.md (IA-30 DELTA_APPROVE)
IMPLEMENTATION_AUDIT_REF: docs/ephemeral/HDE-CRD-0002-implementation-audit-v1.0.md (AUDIT_COMPLETE; blob b39ac9f276db)
business_case_ref: docs/ephemeral/HDE-CRD-0002-WU-DOC-01-po-disposition-business-case-v1.0.md §2 (measure: "Each statement WU-DOC-01 changes matches merged `main`, checked at DOC-20")
authorizing_decision: docs/ephemeral/HDE-CRD-0002-WU-DOC-01-po-disposition-doc20-correction-v1.0.md §2 (Product Owner, 2026-10-22: "authorize DOC-10 for instruction v1.1, give me the handoff"; landed by #697)
originating_finding: docs/ephemeral/HDE-CRD-0002-WU-DOC-01-documentation-completion-v1.0.md (DOC-20, INCOMPLETE; §6 DC-1 and DC-2; §8 decision returned)
accepted_lineage: docs/ephemeral/HDE-CRD-0002-WU-DOC-01-pr-work-unit-lineage-review-v2.0.md (PR-40 ACCEPT across #692 and #695; #696). Accepted-final; not reopened
prior_cycles: cycle 1 plan v1.0 → #692 (squash 4c9bbfc); cycle 2 plan v2.0 → #695 (squash cf8b759). Both PRs are landed history
ops_evidence: none (WU-OPS-01 follows; its business case is due before OPS-10)
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.7.4.md (433,368 bytes; sha256 8ac9723214bd90d12f8cf723e0a1f060ddaf73bc4f91c555447de7c6016d37ff)
pf10_addendum_created: none (DOC-10 is not an addendum producer)
issuer: the continuing whole-change Implementation Agent (IA) for HDE-CRD-0002 (this DOC-10 run: https://claude.ai/code/session_017Tz88x3eecWgXvRf3dudTQ; earlier IA work in session "HDE-CRD-0002-2", https://claude.ai/code/session_01U3QLYTkfUepeRbSGZNPj9N)
prompt: DOC-10 — Create Final Repository Documentation PR Instructions — 100926.1 (https://app.notion.com/p/3f44590a05eb81ce99b1d2ade30c572f; page state of 2026-10-12T02:29:24.131Z, read in full in this invocation)
prompt_release: GCFPE-20261009.1 / 100926.1
created_at: 2026-10-22T03:55:00Z
repository_baseline: origin/main f3cc29e6e7f3b8c1e0dc0386a8b6d484895fc881 (#697). Every fact in §5 and §6 was measured at this head
receiver: a new dedicated HDE-CRD-0002 WU-DOC-01 PR engineering session for plan cycle 3 (created by Nathan / Product Owner)
next_prompt: PR-20 — Create Detailed PR Implementation Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb819fbea5dcd966a750ba; page state of 2026-10-12T02:29:47.327Z; Inputs, Execute and Required result read in this invocation)
canon_conflict_register: CR-1 to CR-8 carried, all decided; no new entry (§15)
---

# HDE-CRD-0002 WU-DOC-01 — Final repository documentation PR instruction v1.1

## 1. Result and authority boundary

**INSTRUCTION_READY.** This is WU-DOC-01's PR instruction for plan cycle 3: one bounded corrective documentation pass that corrects the four sentences of DOC-20 findings DC-1 and DC-2, and nothing else.

- **The work:** four sentences in four Markdown documents (§6).
- **Closed:** every other statement of the ten documents, and the accepted lineage of #692 and #695 (review v2.0). Neither reopens.
- **What it does not do:** it changes no code, test, workflow, schema, canon, governed evidence or release member.
- **CI:** the four paths classify `documentation_only` (§5.3). The hosted `test` job starts, runs no lane and ends with `CI_APPLICABILITY_AND_EXACT_HEAD_OK`.

This instruction is not the documentation. It authorizes no implementation, publication, merge, QA, Ops, acceptance or closure.

## 2. Identity, lineage and what v1.1 changes

| Field | Value |
| :- | :- |
| Change | CRD HDE-CRD-0002 |
| Unit | WU-DOC-01, Plan v1.1 §7, scope as Plan delta 01 P-8 sets it |
| Authorizing decision | Product Owner disposition `…-po-disposition-doc20-correction-v1.0.md` §2: DOC-10 issues v1.1, the start of plan cycle 3, covering DC-1 and DC-2. Bounds: nothing else in the ten documents reopens; the accepted lineage stays accepted-final; v1.0 is preserved and v1.1 is a complete successor |
| Originating finding | DOC-20 record `…-documentation-completion-v1.0.md` §6 (DC-1, DC-2) and §8 |
| Business case | Unchanged. Beneficiary: agents and operators who take repository workflow from `AGENTS.md` and `README.md`. Measure: "Each statement WU-DOC-01 changes matches merged `main`, checked at DOC-20". No ceiling (addendum 2.18) |
| Acceptance (Plan v1.1 §7) | "Each statement traces to a merged unit; `tests/unit/test_check_agents_md_citations.py` passes; DOC-20 verifies completion." |
| Nonclaims (Plan v1.1 §7) | "Documentation completion establishes no QA, acceptance or closure." |

**What v1.1 changes from v1.0:**
- **Scope:** v1.0's 36 items (§6 of v1.0) are delivered and verified by DOC-20 (record §4), except the four sentences below. v1.1's items are DC-1a, DC-1b, DC-1c and DC-2 only.
- **Origin of the defects** (DOC-20 §6, "Origin"): v1.0's R-3 and A-1 asked for the writer's nonclaims "as the WU-PR-07 PR result record states them", and D-4 asked to "state what is read and by which app". The plan restated the nonclaim as existence, and checked `RELEASE_ID` only in `adapter/`. v1.0 is not defective (DOC-20 §8); v1.1 carries the controlling code so that PR-20 measures it directly.
- **Unchanged from v1.0:** the exclusions (§7), the security limits (§10), the PR lane (§11) and the canon-conflict register (§15).

## 3. Unit selection and dependency state

- **Stage:** DOC-20 returned INCOMPLETE with no lawful runnable receiver (DOC-20 §8). The Product Owner directed DOC-10 to issue v1.1 (decision §2), and DOC-10 hands off to PR-20.
- **Dependencies:** WU-DOC-01's dependency ("Ninth; after WU-PR-08 merges") and business case are met, as in v1.0 §3. The decision record (#697) is merged at `f3cc29e`.
- **Accepted-final:** #692 and #695 are landed history. Cycle 3 plans from the landed state, uses a new branch and a new PR, and never resumes, reuses or pushes to either (PR-20 "Re-plan entry"; PR-40 "Accepted-final lineage protection").
- **Order after this unit:** WU-OPS-01 (business case due before OPS-10), then QA-10, which waits for documentation `COMPLETE` and WU-OPS-01.

## 4. Requirement-to-documentation mapping (cycle 3)

| Req. | Delivered by (merged) | Delivered fact (observed at `f3cc29e`) | Documentation change (§6 item) |
| :- | :- | :- | :- |
| S21 | WU-PR-07 #668 | the v2 writer exists; no close pack, candidate source or close-run family has been produced with it, under v1 or v2 (§5.1) | DC-1a, DC-1b, DC-1c |
| S16, S17 (D-4 of v1.0, routed by addendum 2.21 as LR8-F2) | WU-PR-08 #687; WU-DOC-01 #692 | the HTTP adapter reads neither `ENGINE_TAG` nor `RELEASE_ID` from the environment; the vendor client reads `RELEASE_ID` from the environment when no release identity is passed (§5.2) | DC-2 |
| Every other requirement | as v1.0 §4 | verified complete by DOC-20 §5 | none (closed) |

## 5. Repository baseline (measured at `f3cc29e`)

Read with `git`, `grep`, `sed` and `python3` (3.13.16, the container's interpreter) under `env -i` closed rails (`SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC`). No code path outside `docs/ephemeral/` changed between `8187254` (DOC-20's head) and `f3cc29e` (`git diff --stat 8187254 f3cc29e -- . ':(exclude)docs/ephemeral'` is empty), so DOC-20's line numbers hold.

### 5.1 Close packs, candidate sources and close-run families (DC-1)

- **Close packs in `audit/`:** 16 Epics. `EPIC-008`, `EPIC-010`, `EPIC017`, `EPIC-018`, `EPIC-021` to `EPIC-030` have a `_close_report.md` and a `_MANIFEST.json`; `EPIC019` and `EPIC020` have a manifest only. README names the EPIC-027 pack itself (lines 118, 119 and 211, per DOC-20).
- **None was written by the writer.** No manifest has a top-level `schema_version` (all 16 read `None`). The writer's manifest schemas are `epic_close_candidate_manifest.v1` (`tools/qa/generate_epic_close_pack.py:43`) and `close_candidate_manifest.v2` (`:2190`). `git grep` for either manifest schema, or either source schema as a `"schema_version"` value, outside `tests/` and `docs/ephemeral/`: no hit.
- **No candidate source** file exists outside `schemas/`, `tests/` and docs.
- **No close-run family:** no `close/` directory under `audit/qa/`; no `audit/HDE-CRD-*` file.
- **`docs/EVIDENCE_INDEX.md:64`** says "no close-run family of any change exists yet". That is true, because only the updater writes a close-run family and none exists. DOC-20 rated it accurate. It is not in scope.
- **Source of the nonclaim:** WU-PR-07 result v1.0, lines 172-173: "No close pack, candidate source or close-run family of any change **is produced**" (DOC-20 §6). Read with addendum 2.17 "Scope boundaries and nonclaims" ("It produces no close pack for any change").

### 5.2 `RELEASE_ID` and `ENGINE_TAG` (DC-2)

- **HTTP adapter:** `adapter/wsgi.py:14-15` sets `ENGINE_TAG` (`Isis6`) and `RELEASE_ID` (`rel_dev`) with `app.config.setdefault`; lines 31-32 put them in `X-Engine-Tag` and `X-Release-Id`; `adapter/logging_filter.py:46,65` reads `app.config["RELEASE_ID"]` for log lines. No `adapter/` code reads either name from the environment.
- **Vendor client:** `HdApiClient.from_env` (`engine/bodygraph/vendor_client.py`) sets `source = env if env is not None else os.environ` (line 331) and `rid = (release_id or str(source.get("RELEASE_ID") or "")).strip().lower()` (line 344). An empty value becomes 64 zeros; a value that is not 64 lowercase hex characters is replaced by its SHA-256 (lines 345-348). It is sent as `User-Agent: GlowHDEngine/<release_id>` (line 482).
- **Production callers pass no `release_id`:**
  - `engine/bodygraph/resolver.py:471` passes `env=_client_config_env(database_env)`, and `:543` passes `env=vendor_env`;
  - `engine/bodygraph/ingest.py:172` passes `env=_client_config_env(env)`;
  - `_client_config_env` (`ingest.py:118-128`) and `_vendor_config_env` (`resolver.py:670-683`, the source of `vendor_env` at line 262) both start from `dict(os.environ)`.
  - So a `RELEASE_ID` set in the process environment reaches the vendor `User-Agent`.
- **`ENGINE_TAG`** is read from the environment nowhere (`grep` over `engine/` and `adapter/`; `engine/compat/identity.py` has only a constant).
- **Canon:** HDE-CLI-API-Vendor-Ref §7.2.2 "Canonical headers" requires `User-Agent: GlowHDEngine/<release_id>`, where `release_id` is lowercase 64-hex. Glow Infrastructure §8.1 "Shared keys" lists `RELEASE_ID` as OPEN/TBD, names only. Neither is changed or contradicted by DC-2: DC-2 describes the code.

### 5.3 The four documents and CI

| Document | Lines | Blob | Sentence (line) | Read by tests or tools for this sentence |
| :- | -: | :- | :- | :- |
| `README.md` | 254 | `1b63d4598be3` | 13 | none |
| `AGENTS.md` | 228 | `cd549f509900` | 143 | none; `ci/checks/check_agents_md_citations.py` checks the whole file |
| `CHANGELOG.md` | 543 | `e3c286d217fb` | 7 | none |
| `docs/ADAPTER_009.md` | 229 | `b80d00c1d1c1` | 48 | none |

- **"Read by":** `git grep` over `tests`, `ci`, `tools`, `scripts` and `.github` for "of any change exists", "not read from the environment" and "capability only": no hit. The document-reading tests of v1.0 §5.5 still apply, because they read these files as a whole.
- **Classification:** `classify_paths` on the four paths gives `reason='documentation_only'`, all seven lanes and `needs_python` false. None is a release member (v1.0 §5.3; unchanged).
- **Codex code review** excludes Markdown (`AGENTS.md` "Code review guidelines"), so no Codex finding is expected. Codex security review is deprecated (addendum 2.3).

## 6. Bounded items

Line numbers are at `f3cc29e`. **Required change** states what the text must say; PR-20 drafts the exact words.

| ID | Document:line | Current statement | Fact (§5) | Required change |
| :- | :- | :- | :- | :- |
| DC-1a | `README.md:13` | "the writer and the close-run family are capability only; no close pack, candidate source or close-run family of any change exists." | §5.1 | scope the clause to the writer: no close pack, candidate source or close-run family has been produced with this writer or under schema v2. The rest of the bullet (what the writer executes and what a close pack establishes) stays |
| DC-1b | `AGENTS.md:143` | "The writer and the CRD close-run family are capability only: no close pack, candidate source or close-run family of any change exists, and a close pack establishes no …" | §5.1 | the same scoping as DC-1a. The rest of the bullet stays |
| DC-1c | `CHANGELOG.md:7` | "Capability only: no close pack of any change exists." | §5.1 | the same scoping as DC-1a |
| DC-2 | `docs/ADAPTER_009.md:48` | "`ENGINE_TAG` and `RELEASE_ID` are not read from the environment: `adapter/wsgi.py` sets them as app configuration defaults …" | §5.2 | state that the HTTP adapter reads neither name from the environment, and that the vendor client reads `RELEASE_ID` from the environment for its `User-Agent` when no release identity is passed. One sentence. The line's first sentence (`ENGINE_SERVICE_TOKEN` and the others are read by no code) stays |

**Rules for the text:**
- **Legacy Epic close packs** stay unmentioned or stay true. If a sentence mentions them, it says only what §5.1 measures.
- **No new claim.** In particular, no statement that a close pack will be produced, or about `RELEASE_ID`'s value in any deployed service (§7).
- **DC-2's normalization detail** (zeros when empty; SHA-256 when not 64 hex) is optional. If stated, it states lines 345-348 exactly.

**Count:** 4 sentences in 2 findings: DC-1 (DC-1a to DC-1c) and DC-2.

## 7. Exclusions

- **Closed:** every statement of the ten documents other than the four in §6. A newly found stale statement is recorded and routed to the Product Owner, not edited. This includes a stale statement inside the four documents: v1.0 §9.3's "within an item's subject" allowance does not apply in cycle 3.
- **No canon edit.** Nothing in `docs/pfcanon/` changes.
- **Nothing generated or governed is edited by hand**, and no write-producing generator runs.
- **No code, test, fixture, workflow, schema, script or release member** changes. That includes `engine/bodygraph/vendor_client.py` and `adapter/wsgi.py`: DC-2 documents their behaviour and does not change it.
- **Not edited:** the S21 ADR (addendum 2.17), historical entries and posture records, and `docs/EVIDENCE_INDEX.md:64` (§5.1).
- **No Ops fact** about the live service (addendum 2.19).
- **No claims** of QA, acceptance, Ops, deployment, PF09 or PF30 movement, drainage or closure.

## 8. Interface contracts

| Contract | Counterpart | Content |
| :- | :- | :- |
| H-4 (WU-PR-07) | the close-pack writer | DC-1's nonclaim as the PR result record states it ("is produced"), read with the ADR and addendum 2.17 |
| D-4 (v1.0) / LR8-F2 | `docs/ADAPTER_009.md` "Env vars" | DC-2 states what is read and by which code |
| DOC-20 | completion verification | DOC-20 re-checks the measure on merged `main`, including the four corrected sentences |

## 9. Disposition rules for PR-20

- **Plan choices (PR-20's, recorded):** the wording of each sentence; whether DC-2 states the normalization detail; one PR (expected).
- **Baseline re-check:** PR-20 re-measures §5 and §6 at its own head and records each difference. A sentence already correct at its head is recorded as "no change".
- **Prototype:** PR-20 applies the full text in a throwaway copy and runs §10 items 2 to 4 there.
- **Measure:** the plan lists each changed sentence with the code or record that proves it. DOC-20 verifies that list.
- **Product Owner questions:** none expected. An `AGENTS.md` change beyond DC-1b goes to the Product Owner; the Proceed on a plan that names the exact DC-1b edit is the instruction for that edit.

## 10. Acceptance, tests and evidence

1. **Traceability:** each changed sentence names its fact in §5 (Plan v1.1 §7).
2. **`tests/unit/test_check_agents_md_citations.py` passes**, and `python ci/checks/check_agents_md_citations.py` prints `AGENTS_MD_CITATIONS_OK`. Both run locally, because CI selects no lane.
3. **The six document-reading test files** of v1.0 §5.5 pass on the PR head with CI's full install (`python -m pip install 'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e .`), in a throwaway copy or dedicated environment, under closed rails. Cycle 2's count was 1,248 passed (review v2.0 §5 row 2).
4. **`python tools/ci/prepush_check.py lanes membership build-notes`** on the PR head, with one `--path` per changed file for `membership`: `documentation_only`, no member, PF10 path and hash recorded.
5. **Hosted CI on the final head:** the `test` job succeeds with `CI_APPLICABILITY_AND_EXACT_HEAD_OK`.
6. **Paths:** `git diff --name-status` against the base lists only the four documents outside `docs/ephemeral/`.
7. **Evidence:** the PR result records under `docs/ephemeral/` hold the sentence-to-proof list, the test counts, the `lanes` output and the CI run identity. No evidence family and no QA artifact.

## 11. Security limits and lane

- **Security:** no secret, key or base URL in any document; environment names only. DC-2 names `RELEASE_ID` and the header; it records no value. Closed rails for every local run; no live vendor, production or database access.
- **PR-20** (new dedicated session) reads this instruction and its lineage, the four documents in full and §5's code at its head, re-checks the baseline, prototypes, writes one `PR_IMPLEMENTATION_PLAN` under `docs/ephemeral/` (version 3.0 by the cycle convention of v1.0 and v2.0), and returns `AWAITING_PO_PROCEED`.
- **PR-30** (after Nathan's Proceed for that exact plan): recovers existing work first; edits only the planned sentences; runs §10 items 2 to 4 and 6; commits coherently on a new branch; publishes `PR_CANDIDATE_PUBLISHED`; hands off to PR-35.
- **PR-35** (its own dedicated session): retrieves review threads; re-runs §10 items 2 and 3 on the final head; verifies item 5 and mergeability; returns `MERGE_PENDING` without merging.
- **PR description:** the `.github/pull_request_template.md` headings, filled under the `AGENTS.md` content rules.
- **Merge:** Nathan, manually.
- **PR-40:** this IA reviews the landed cycle-3 lineage, entered on `MERGE_OBSERVED` or, only where none was returned, on Nathan's merge assertion. #692 and #695 stay accepted-final.
- **DOC-20:** runs again and verifies the measure on merged `main`.

## 12. Recovery and rescope

- **Interruption:** resume from the phase's last saved artifact; inspect branches, PRs and `docs/ephemeral/` before creating anything.
- **Instruction defect:** returns to this IA through DOC-10; a corrected instruction is a new version.
- **Rescope** (material only): before Proceed, the PR-20 author owns it (RS-10; RS-30 for revisions) and this IA reviews it through RS-20. After Proceed, PR-30 or PR-35 records `PR_RETURN_PHASE`. An expected trigger: a correction that would need a code change. A wording choice is not a trigger.
- **Abort:** only Nathan's manual PR-50.

## 13. Unresolved items, carried observations and owners

| Item | Owner | State |
| :- | :- | :- |
| DC-1, DC-2 | this unit, cycle 3 | instructed here |
| DC-O1, DC-O2 (DOC-20 §6) | — / this IA | observations; no effect |
| RF-11; RF-1 to RF-10 | Product Owner | routed, unchanged |
| Carried items (plan v1.0 §17): DOC10-O1, the O-19 code, OBS-8, OBS-P3-13, PR35-C1, LR8-F1, the canon doc-deltas, the S21 ADR revision | as stated there | unchanged |
| WU-OPS-01's business case, before OPS-10 | Product Owner | due |
| QA-10 | Isis | waits for documentation `COMPLETE` and WU-OPS-01 |
| The §9 plan choices | PR-20 session | in the plan |

## 14. Semantic readiness comparison

| Source clause | Intended meaning | Instruction meaning | Acceptance | Stage |
| :- | :- | :- | :- | :- |
| Decision §2, DC-1 row | scope the nonclaim to the writer; legacy packs unmentioned or true | DC-1a to DC-1c; §6 rules | §10 (1) | PR-20; DOC-20 |
| Decision §2, DC-2 row | adapter reads neither name; vendor client reads `RELEASE_ID` for `User-Agent` when none is passed | DC-2 | §10 (1) | PR-20; DOC-20 |
| Decision §2, bounds | nothing else reopens; lineage stays final; v1.0 preserved | §1, §3, §7 | §10 (6) | all phases |
| Business case measure | each changed statement matches merged `main` | §9 measure list | — | DOC-20 |

**PR-20's input contract:** its sole substantive input is `PR_INSTRUCTION_ID`. This instruction carries the Specification, delta, Audit, Plan, delta and review lineage; PF10 and the overlays; the business case; the authorizing decision and finding; the baseline, items, exclusions, interfaces and dependencies; and acceptance, evidence, security, recovery, rescope, merge ownership and the return owner. Every fact in §5 and §6 was measured at `f3cc29e` by this IA.

## 15. Canon-conflict register

`CANON_CONFLICT_REGISTER` carried unchanged:

| ID | Status | Decision owner | Record |
| :- | :- | :- | :- |
| CR-1, CR-2, CR-3 (CANON_RECONCILIATION) | APPROVED_AS_CHANGED | Thoth | Specification v1.1 lineage |
| CR-4 | APPROVED | Product Owner | `docs/ephemeral/HDE-CRD-0002-WU-PR-01-po-disposition-cr-4-cr-5-v1.0.md` §2 |
| CR-5 | APPROVED_AS_CHANGED | Product Owner | same record §3 |
| CR-6 | APPROVED, alternative (a) | IA through RS-20 | WU-PR-01 rescope review v1.0 §12; addendum 2.6 |
| CR-7, CR-8 | APPROVED, alternative (a) each | Product Owner direction of 2026-10-14 | addendum 2.7 |

**No new conflict.** DC-1 and DC-2 are repository-documentation inaccuracies against code and records. Glow Infrastructure's OPEN/TBD entry for `RELEASE_ID` records the key name only, and DC-2 adds no infrastructure fact.

## 16. Return owner and next step

- **Next:** PR-20 — Create Detailed PR Implementation Plan — 100926.1, in a new dedicated top-level WU-DOC-01 PR engineering session for plan cycle 3, which Nathan creates. It returns `AWAITING_PO_PROCEED`.
- **Returns to this IA:** PR-40 after Nathan's merge, then DOC-20; RS-20 for a rescope; DOC-10 for an instruction defect.

## 17. TypeSafe reading for the receiving session (PR-20, WU-DOC-01 cycle 3)

Action sent (v8.2): "Write, in a new dedicated session, the third detailed PR implementation plan, not yet reviewed, for the final repository-documentation work unit of an approved change, after a completion verification found four inaccurate sentences on merged main: a close-pack nonclaim stated as a fact about the whole repository in three Markdown documents (README, CHANGELOG and the agent-instructions file) and one clause in an operator document that says an environment variable is not read when a vendor client does read it. A ready instruction lists each sentence's line, the controlling code and the bounded correction; the plan re-measures them at its head, drafts the exact replacement text, prototypes it in a throwaway copy with the local tests that read these documents, and keeps everything else in the unit closed. No code changes and no live run occur; a Product Owner Proceed, implementation, CI, a lineage review and a repeated completion verification follow."

- **TypeSafe v8.2: Opus 5.5 at high.** Effort score 1.76 (confidence 0.80); rung probabilities low 0.00, medium 0.27, high 0.70, extra high 0.03, max 0.00, ultracode 0.00. Model probabilities Fable 5.1 0.00, Opus 5.5 0.89, Sonnet 5.5 0.11, Haiku 5.5 0.00 (confidence 0.85). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.000, Fable 5.1 at high 0.000, Fable 5.1 at extra high 0.000, Fable 5.1 at max 0.000, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.000, Opus 5.5 at medium 0.240, Opus 5.5 at high 0.623, Opus 5.5 at extra high 0.027, Opus 5.5 at max 0.000, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.000, Sonnet 5.5 at medium 0.030, Sonnet 5.5 at high 0.077, Sonnet 5.5 at extra high 0.003, Sonnet 5.5 at max 0.000, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Sent 2026-10-22T03:53:27Z. Nathan picks the cell.
- **Detail:** v8.2 sent 2026-10-22T03:53:27Z; HTTP 200 in 0.59 s; 5527 input and 71 output tokens; jev-1.13.0. Rung by rule: high (nearest to the score, halves up); model by rule: Opus 5.5 (the most probable of the four options, a tie going to the higher-priced model). No flag printed.
- **Which request:** the installed TypeSafe scoring skill's request v8.2 and `score_v8.py`, run once with session kind `planning`, before this record was saved.
- **Records:**
  - The Notion row was not written.
  - Nathan's pick for PR-20 is not stated.
  - Nathan's pick for this DOC-10 session is not stated. Its reading is in the decision record §4.

**Surface advice:** run PR-20 as a new top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, with Notion read access for the prompt.
- **Environment:** CPython 3.12 with CI's full install in a throwaway copy, for the six document-reading test files (about 80 s) and the citation checker; git, bash and `ruby` for the pre-push check; closed rails through `env -i`.
- **Access:** no live vendor, production or database access.
- **Order:** this instruction's pull request should be merged first.

## 18. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / WU-DOC-01 / DOC-10 / instruction 2 (v1.1) |
| change / specification | CRD HDE-CRD-0002 / `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` v1.1, with Specification delta 01 |
| unit | WU-DOC-01 (S21 and S16/S17 documentation; DC-1, DC-2) |
| release | GCFPE-20261009.1 / 100926.1 |
| prompt | DOC-10 — Create Final Repository Documentation PR Instructions — 100926.1, https://app.notion.com/p/3f44590a05eb81ce99b1d2ade30c572f (page state of 2026-10-12T02:29:24.131Z). Receiver contract read: PR-20 — Create Detailed PR Implementation Plan — 100926.1, https://app.notion.com/p/3f44590a05eb819fbea5dcd966a750ba (page state of 2026-10-12T02:29:47.327Z) |
| role/stage | continuing whole-change IA / DOC-10 |
| capture time | 2026-10-22T03:55:00Z |
| execution identity | https://claude.ai/code/session_017Tz88x3eecWgXvRf3dudTQ |
| inherited usage | DOC-20 record §11; decision record (#697); instruction v1.0 §20 |
| repository persistence | recorded here only. `docs/changes/GCFPE_PROMPT_PROVENANCE.md` is absent on `main`; persistence is pending and non-gating |

## Canon relied on

Read on `main` at `f3cc29e`. `docs/pfcanon/` is unchanged from DOC-20's head; PF10 is v13.7.4 (path and hash in the front matter).

| Topic | Sources and sections |
| :- | :- |
| DOC-10 operation and routing | DOC-10 — Create Final Repository Documentation PR Instructions — 100926.1, read in full: "Execute" 1 to 6; "Required result"; "Result routing"; "Runtime artifacts, readback, and handoff"; "Native identity, source fidelity, and recovery" (a repeated invocation inspects the previous result and repairs only the defective portion) |
| Receiver contract | PR-20 — Create Detailed PR Implementation Plan — 100926.1: "Inputs" (including "Re-plan entry": a PR merged under an earlier plan cycle is landed history), "Execute" and "Required result", read in this invocation |
| Accepted lineage stays final | PR-40 — Review PR Work-Unit Lineage — 100926.1, "Accepted-final lineage protection", as the DOC-20 record and the decision record cite it |
| Unit scope; deploy facts excluded | PF10 addendum 2.19 (P-8; WU-DOC-01 and WU-OPS-01 consequences), read in full |
| Routed items (D-4, LR8-F2) | PF10 addendum 2.21, read in full |
| Writer nonclaim (DC-1) | PF10 addendum 2.17, read in full ("Deferred obligations": the usage note reads the ADR with this addendum; "Scope boundaries and nonclaims": "It produces no close pack for any change") |
| Measure; no ceiling | PF10 addendum 2.18, read in full (rules 1, 2 and 5; "Epic, task, and status effects") |
| `User-Agent` and `RELEASE_ID` | HDE-CLI-API-Vendor-Ref §7.2.2 "Canonical headers"; Glow Infrastructure §8.1 "Shared keys" (the conjunction identity keys, OPEN/TBD), read at those passages |
| Source fidelity | PF03-Reference-Technical-Writing-Best-Practices "Truth and source fidelity" (as v1.0 and the DOC-20 record read it) |
| QA entry ordering | PF19-Canon-Glow-QA-Guide §3.1 "Intent" (as v1.0 cites it) |
| Repository rules | `AGENTS.md`: canon-first rule; "Code review guidelines"; "Operating workflow" (closed rails; pytest readiness; pre-push check; PR descriptions; redaction) |

**Search:** `git grep -c -i -E 'DOC-10|WU-DOC-01|RELEASE_ID' origin/main -- docs/pfcanon/`, and case-sensitive `RELEASE_ID|User-Agent|GlowHDEngine/`. The governing hits are the PF10 addenda above, HDE-CLI-API-Vendor-Ref §7.2.2 and Glow Infrastructure §8.1. The other hits are acceptance-token names (`RELEASE_ID_RECOMPUTE_OK` and similar) and Epic history, not rules for this task.
