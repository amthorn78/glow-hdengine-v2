---
artifact_type: DOCUMENTATION_COMPLETION
artifact_id: HDE-CRD-0002-WU-DOC-01-DOCUMENTATION-COMPLETION
artifact_version: "1.0"
result: INCOMPLETE
routing: TERMINAL_PRODUCT_OWNER_RETURN (no lawful runnable receiver for the correction; §8)
predecessor: none (first DOC-20 for WU-DOC-01)
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
DOCUMENTATION_UNIT_ID: WU-DOC-01
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-DOC-01-pr-instruction-v1.0.md (v1.0; blob c49ff720ffd2)
PR_WORK_UNIT_LINEAGE_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-WU-DOC-01-pr-work-unit-lineage-review-v2.0.md (ACCEPT across #692 and #695; blob 0f138d9cdfdf; #696), with predecessor docs/ephemeral/HDE-CRD-0002-WU-DOC-01-pr-work-unit-lineage-review-v1.0.md (REJECT; blob e2329d66c645)
PR_IMPLEMENTATION_PLAN_IDS: docs/ephemeral/HDE-CRD-0002-WU-DOC-01-pr-implementation-plan-v1.0.md (§6, 55 edits); docs/ephemeral/HDE-CRD-0002-WU-DOC-01-pr-implementation-plan-v2.0.md (§6, C-1 and C-2)
PR_RESULT_IDS: v1.0, v1.1 (cycle 1, #692); v2.0, v2.1 (cycle 2, #695), all docs/ephemeral/HDE-CRD-0002-WU-DOC-01-pr-implementation-result-v<N>.md
PR_REFS: [amthorn78/glow-hdengine-v2#692 (squash 4c9bbfc), amthorn78/glow-hdengine-v2#695 (squash cf8b759)]
SPECIFICATION_ID: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (v1.1; blob c4802a5a7fa3), with Specification delta 01
IMPLEMENTATION_AUDIT_ID: docs/ephemeral/HDE-CRD-0002-implementation-audit-v1.0.md (blob b39ac9f276db)
IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (blob abffa2ccbd44) §7 WU-DOC-01, with Plan delta 01 v1.1 (P-8)
PLAN_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (IA-30 INITIAL_APPROVE; blob 0cc0276524b2)
business_case_ref: docs/ephemeral/HDE-CRD-0002-WU-DOC-01-po-disposition-business-case-v1.0.md §2 (measure: "Each statement WU-DOC-01 changes matches merged `main`, checked at DOC-20")
ops_evidence: none (WU-OPS-01 follows; not an input to documentation completion)
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
verifier: the continuing whole-change Implementation Agent for HDE-CRD-0002, session "HDE-CRD-0002-2" (https://claude.ai/code/session_01U3QLYTkfUepeRbSGZNPj9N); also the DOC-10 author and the PR-40 reviewer of this unit
prompt: DOC-20 — Verify Final Repository Documentation Completion — 100926.1 (https://app.notion.com/p/3f44590a05eb81d8a582eec0e93e6ee7; page state of 2026-10-12T02:29:19.255Z, read in full in this session)
prompt_release: GCFPE-20261009.1 / 100926.1
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.7.4.md (blob 1343ae09018e; sha256 8ac9723214bd90d12f8cf723e0a1f060ddaf73bc4f91c555447de7c6016d37ff)
pf10_addendum_created: none (DOC-20 is not an addendum producer)
repository_head_read: origin/main 8187254d2b9b8bfcf63bd1f7b18fd415f56d8ec8 (#696)
created_at: 2026-10-22T03:43:00Z
canon_conflict_register: CR-1 to CR-8 carried unchanged, all decided; no new entry (§9)
---

# HDE-CRD-0002 WU-DOC-01 — Documentation completion v1.0 (DOC-20)

## 1. Result

**INCOMPLETE.** WU-DOC-01 is merged and its lineage is accepted, and almost every statement it changed matches merged `main`. Two changed statements do not:

- **DC-1** — the close-pack nonclaim. Three documents say "no close pack … of any change exists": `README.md:13`, `AGENTS.md:143` and `CHANGELOG.md:7`.
  - On `main`, the close packs of 16 Epics exist in `audit/`, for example `audit/EPIC-027_close_report.md` and `_MANIFEST.json`. They were written by earlier tools; none carries the HDE-CRD-0002 writer's manifest schema.
  - The source of the nonclaim (WU-PR-07 result v1.0, lines 172-173) says "No close pack, candidate source or close-run family of any change **is produced**", meaning by this writer. The documents widened it into a false statement about the repository.
- **DC-2** — `RELEASE_ID` and the environment. `docs/ADAPTER_009.md:48` says "`ENGINE_TAG` and `RELEASE_ID` are not read from the environment".
  - `engine/bodygraph/vendor_client.py:344` reads `RELEASE_ID` from its environment mapping when no `release_id` is passed.
  - The production callers pass none: `engine/bodygraph/resolver.py:471` and `:543`, and `engine/bodygraph/ingest.py:172`. Their mapping starts from `os.environ`.
  - The value then becomes the vendor request's `User-Agent: GlowHDEngine/<release_id>` (`vendor_client.py:482`).

Both are inaccuracies in statements the unit changed, so the business-case measure is not met for them. Every other changed statement checked matches `main` (§4).

**Routing: terminal return to the Product Owner** (§8). Neither inaccuracy comes from a defective instruction. The unit's PR lineage is accepted, so new correction work needs an owner that the Product Owner names.

This record verifies documentation. It is not a second lineage verdict, and not QA, Ops, acceptance or closure.

## 2. Merge and acceptance evidence

- **#692**, squash `4c9bbfc` with parent `a85067c`: the ten documents, equal to plan v1.0's companion diff (sha256 `a334c348…0ab63`).
- **#695**, squash `cf8b759` with parent `0e2bd9e`: `docs/qa_harness_pattern.md` lines 14 and 97, equal to plan v2.0's companion diff (sha256 `40e19bd1…6e39c3`).
- **Accepted lineage:** review v2.0 (#696), ACCEPT across both PRs.
- **`main` at `8187254`:** only `docs/ephemeral/` changed after `cf8b759`.
- **The PR-35 `MERGE_PENDING` results** (v1.1 and v2.1) remain historical pre-merge evidence.

## 3. Method

- **Inputs read in full:** the instruction, plan v1.0 §6 and plan v2.0 §6, results v1.1 and v2.1, reviews v1.0 and v2.0, the business case, and DOC-20.
- **What was compared:** every line each document gained between `a85067c` and `8187254`, extracted with `git diff --word-diff`, against the code, tool help and records at `8187254`.
- **How:**
  - code reads with `grep` and `sed` at cited lines;
  - test-client probes and tool runs in a throwaway clone of `8187254`, with a CPython 3.12.3 venv holding CI's full install, under `env -i` closed rails.
- **Behaviour checks from reviews v1.0 §5 and v2.0 §5 are reused, not repeated:** no non-Markdown path changed from `4c9bbfc` to `8187254`. Those checks covered `/internal/version`, the unknown-path 404, the dev `/reader` gate, the EPIC037 `--check` runs, `release_id`, the CRD admission probe and the six document-reading test files (1,248 passed).

## 4. Statement verification by document

| Document | What was checked (plan items) | Evidence at `8187254` | State |
| :- | :- | :- | :- |
| `README.md` | R-1 `release_id`; R-2 pre-push section; R-3 close-pack writer block; R-4 A7 writer and CI coverage; R-5 dev Reader; R-6 `artifacts/release_id.txt`; R-7 off-CI attestation; R-9 aux-preview and vendor override | R-2: exit constants `prepush_check.py:80-84`; probes: `membership` without `--path` → 1, an unknown option → 2. Inherited keys at `:89`; `SWEEP_TOOLS` at `:116`; `REPLAY_WORKFLOW_SHA256` equals the sha256 of `ci.yml`. `sweep --no-run` → `uncovered=0`, PASS (once `ruby` was on `PATH`, as the prerequisites line says).<br>R-3: schema `change_id` `^HDE-(?:EPIC[0-9]{3}\|CRD-[0-9]{4,})$`, top-level `additionalProperties: false`; v2 output paths via `_derived_paths_v2`; ADR lines 47-58; presence registration at `_crd_close_pack_entries` (updater 4046-4084).<br>R-4: A7 writer `ALL` covers the catalog, the audit mirror and the snapshot.<br>R-6: `make_release_pack.sh:6,28-30`; `hd_cli.py` reads the file.<br>R-7: `build_release_attestation.py:344-347,464`.<br>R-9: `main.py:610-628`; `resolver.py:39-40`; `vendor_audit.py:23` | all accurate **except the R-3 nonclaim sentence (DC-1)** |
| `AGENTS.md` | A-1 to A-7 | review v1.0 §5 rows 4 to 8; this pass re-read A-1 against the writer and ADR | all accurate **except A-1's nonclaim clause (DC-1)** |
| `CHANGELOG.md` | CH-1 | every bullet's requirement matches its merge commit: S03 to S05 `7136040`/`bf7ad8c`; S06 and S11 to S13 `1d2c834`/`b26f44f`; S02, S07, S09, S10, S15 and S18 `c98d41f`/`2f3db0a`; S08 and S14 `5892538`; S19 `822ce15`; S20 `b963ed4`; S21 `8b73b57`; S16 and S17 `1a4c8ab`; S22 `1d2c834`/`b26f44f`. Manifest refreshes are exactly #643, #646, #651 and #656 (`git log -- catalog/manifest.json`) | accurate **except "Capability only: no close pack of any change exists" (DC-1)** |
| `docs/EVIDENCE_INDEX.md` | E-1 to E-4 | `ADMITTED_CRD_QA` lines 51-54; label text `update_evidence_index.py:3838` and regex `:86-87`; close-run key `:4011-4018`; no `close/` directory under `audit/qa/`; A7 writer lines 31 and 176 | accurate |
| `docs/qa_harness_pattern.md` | Q-1 (lines 79, 83, 87-93); C-1 (line 14); C-2 (line 97) | review v2.0 §5 rows 3 and 4 (admission probe; install command byte-identical to `AGENTS.md`); `publish_crd_close_run_family` signature at updater 5222 | accurate |
| `docs/CLI_commands.md` | L-1a to L-1k | no `ensure_determinism_env` under `engine/cli/`. Recognized environments `resolver.py:39-40`. `MISSING_VENDOR_INPUT` exit 64 at `main.py:267`. The S8a stub at `resolver.py:215-224`. Audit sink default `$XDG_STATE_HOME`, else `~/.local/state` (`vendor_audit.py:86-99`); in-repository sink refused (`:104`); `allowed` then a state event under one correlation ID (`resolver.py:304-330`). Resolver error envelopes exit 1 (`resolver.py:244-261`). `CliError` default 64 (`main.py:62-66`). No `.sha256` beside `artifacts/cli/abba_sidecar.json` | accurate |
| `docs/RUN.md` | U-1, U-2, U-3, X-1 | runner bind `127.0.0.1` (review v1.0 §5); `tests/infra/test_sercanon_bytes.py` exists; `scripts/dev_start_reader.sh:13-17` exports `APP_ENV` only when set, never defaulting it; recognized environment rule as in L-1e | accurate |
| `docs/ADAPTER_009.md` | D-1 to D-9 | probes from review v1.0 §5 rows 9 and 10. `Strict-Transport-Security` and the `ENGINE_ENV` fallback at `adapter/wsgi.py:36-38`. No source under `engine`, `adapter`, `presenter`, `math` or `catalog` reads `ENGINE_SERVICE_TOKEN`, `TOGGLES_SHA`, `BUILD_COMMIT_SHORT` or `BUILD_TIMESTAMP_UTC` | accurate **except D-4's "`ENGINE_TAG` and `RELEASE_ID` are not read from the environment" (DC-2)**. `ENGINE_TAG` is indeed not read from the environment |
| `docs/contracts/reader_v2_public_bytes.md` | K-1 | unknown-path probe on all three factories (review v1.0 §5 row 9) | accurate |
| `docs/acceptance/reader_a7_crib.md` | P-1 | A7 writer `PROOFS` and `ALL` lists; write gate; `--check` | accurate |
| `docs/server/reader_v1.md` | V-1 (no change) | line 20 states the delivered unknown-path behaviour | accurate (unchanged) |
| README line 132 | R-8 (no change) | the wheel still omits members; S01 was removed | accurate (unchanged) |

**Tally:** 57 planned edits (55 from plan v1.0, 2 from plan v2.0) and 2 no-change confirmations. Four changed sentences are inaccurate, in two findings:
- DC-1: three sentences;
- DC-2: one clause.

## 5. Requirement-by-requirement documentation state

| Requirement | Documentation on `main` | State |
| :- | :- | :- |
| S01 | removed; README states the wheel limitation | complete |
| S02 | contract page; `reader_v1.md` line 20; CHANGELOG | complete |
| S03, S04, S05 | README "CI coverage"; `docs/RUN.md` retained test; CHANGELOG | complete |
| S06 | README attestation sentence; CHANGELOG | complete |
| S07, S08, S14 | `docs/CLI_commands.md`; README R-9; CHANGELOG | complete |
| S09, S10 | README, `AGENTS.md`, CLI_commands, RUN, ADAPTER_009 capture environment, crib; CHANGELOG | complete |
| S11, S12, S13 | EVIDENCE_INDEX Mirror labels; CHANGELOG | complete |
| S15, S18 | CHANGELOG; ADAPTER_009 (S18, earlier unit) | complete |
| S16, S17 | ADAPTER_009 (WU-PR-08) and the D items; CHANGELOG | **incomplete: DC-2** (D-4, the operator variables of `docs/ADAPTER_009.md`) |
| S19 | CHANGELOG; README R-6 (O-19's documentation side) | complete |
| S20 | README pre-push section; `AGENTS.md` A-7; CHANGELOG | complete |
| S21 | README R-3; `AGENTS.md` A-1; EVIDENCE_INDEX E-3; qa_harness Q-1; CHANGELOG | **incomplete: DC-1** (the nonclaim sentence in README, `AGENTS.md` and CHANGELOG) |
| S22 | EVIDENCE_INDEX E-1; qa_harness lines 14 and 79; CHANGELOG | complete |
| Release refresh (delta 01) | README, `AGENTS.md`, CHANGELOG `release_id` `77204764…c51e` | complete |

**Security:** no secret in any document (review v1.0 §5 row 12). **Migration:** none. **Configuration:** `.env.example` (S16) and the variables in ADAPTER_009, with DC-2 open.

## 6. Findings

### DC-1 — the close-pack nonclaim is stated as a fact about the whole repository

| Field | Content |
| :- | :- |
| Text | `README.md:13` "no close pack, candidate source or close-run family of any change exists"; `AGENTS.md:143` the same clause; `CHANGELOG.md:7` "Capability only: no close pack of any change exists." |
| Fact | `audit/` holds the close packs of EPIC-008, EPIC-010, EPIC017, EPIC-018, EPIC019, EPIC020 and EPIC-021 to EPIC-030 (EPIC019 and EPIC020 have a manifest only). README itself names the EPIC-027 close pack (lines 118, 119 and 211). None carries `epic_close_candidate_manifest.v1` or `close_candidate_manifest.v2`, the writer's schemas (`generate_epic_close_pack.py:43`, `:2190`). No candidate source and no close-run family exists |
| Source of the obligation | instruction §6.1 R-3 and §6.2 A-1 (H-4: "the nonclaims, as the PR result record states them"). WU-PR-07 result v1.0 lines 172-173: "No close pack, candidate source or close-run family of any change **is produced**" |
| Origin | plan v1.0 §6 R-3 and A-1 restated the nonclaim as existence. PR-40 reviews v1.0 and v2.0 checked the paths and limits of these blocks, not the scope of this sentence |
| Real input | the three documents on `main`, read by every session (`AGENTS.md`) and by HDE-CRD-0002's own QA and close work, which will produce the first v2 close pack |
| Correction (bounded) | scope each clause to the writer: no close pack, candidate source or close-run family has been produced with this writer or under schema v2. Three sentences; no other text |

### DC-2 — `RELEASE_ID` is read from the environment by the vendor client

| Field | Content |
| :- | :- |
| Text | `docs/ADAPTER_009.md:48` "`ENGINE_TAG` and `RELEASE_ID` are not read from the environment: `adapter/wsgi.py` sets them as app configuration defaults …" |
| Fact | `HdApiClient.from_env` (`engine/bodygraph/vendor_client.py:331`, `:344`) uses `release_id`, else `source.get("RELEASE_ID")`, where `source` is the given mapping or `os.environ`. The production callers pass none: `resolver.py:471`, `resolver.py:543`, and `ingest.py:172` with `_client_config_env`, which starts from `dict(os.environ)` (`ingest.py:118-128`). The value is normalized to 64 hex characters and sent as `User-Agent: GlowHDEngine/<release_id>` (`vendor_client.py:345-348`, `:482`). `ENGINE_TAG` is not read from the environment anywhere |
| Source of the obligation | instruction §6.6 D-4 ("state what is read and by which app"); LR8-F2 |
| Origin | plan v1.0 BR-4 and D-4 checked `adapter/wsgi.py` and `adapter/env_guard.py` only. PR-40 reviews did not search `engine/` for `RELEASE_ID` |
| Real input | an operator shell or service with `RELEASE_ID` set; `docs/ADAPTER_009.md` is an operator document |
| Correction (bounded) | state that the HTTP adapter does not read either name from the environment, and that the vendor client reads `RELEASE_ID` from the environment for its `User-Agent` when no release identity is passed. One sentence |

### Observations (no effect on the result)

- **DC-O1.** README's pre-push "Prerequisites" line is accurate. A run without `/usr/local/bin` on `PATH` (where `ruby` is here) fails `sweep` with `TOOLING_FAILURE missing on PATH: ruby`, as the line implies.
- **DC-O2 (IA lesson).** As PR-40 reviewer, I spot-checked the changed statements rather than checking every one. Both findings were in text those reviews passed. This record is the first complete pass.

## 7. Measure (addendum 2.18 rule 5)

The business case's measure is "Each statement WU-DOC-01 changes matches merged `main`, checked at DOC-20". It is **not met**: four changed sentences, in two findings, do not match. Every other changed statement checked matches.

## 8. Routing and the decision returned

DOC-20's routes:
- **QA-10** needs `COMPLETE`.
- **DOC-10** is for a missing or defective instruction. The instruction is neither: R-3 asked for the nonclaims "as the PR result record states them", and D-4 asked for "what is read and by which app". The plan and the reviews fell short of those.
- **RS-10** is for a material delta. These are not material.
- **The native-owner branch** needs a known lawful receiver. None exists:
  - the PR-40 lineage is accepted, and "Accepted-final lineage protection" forbids rerunning or revising it;
  - new implementation after merge needs "the actual prospective work-unit owner".
- So this is a **terminal return to the Product Owner**.

**Decision returned to the Product Owner:** how DC-1 and DC-2 are corrected. They are four sentences in four documents.

**Recommendation:** direct one bounded corrective documentation pass for WU-DOC-01, a third plan cycle with the scope of §6's two "Correction" rows only. Name it as a new DOC-10 instruction version, v1.1, that adds DC-1 and DC-2. It then follows the usual lane: PR-20, Proceed, PR-30, PR-35, merge, PR-40, then DOC-20 again. Nothing else in the ten documents reopens.

**Resume point:** when the Product Owner directs it, this IA runs DOC-10 for the instruction v1.1. Once the corrective PR is merged and accepted, DOC-20 runs again.

## 9. Lineage, owners and nonclaims

| Item | Owner | State |
| :- | :- | :- |
| DC-1, DC-2 correction route | Product Owner | **decision returned** (§8) |
| RF-11 (`docs/qa_harness_pattern.md:120`'s §2.8 citation); RF-1 to RF-10 | Product Owner | routed, unchanged |
| Carried items (plan v1.0 §17): DOC10-O1, the O-19 code, OBS-8, OBS-P3-13, PR35-C1, LR8-F1, the canon doc-deltas, the S21 ADR revision | as stated there | unchanged |
| WU-OPS-01's business case, before OPS-10 | Product Owner | due |
| QA-10 | Isis | waits for documentation `COMPLETE` and WU-OPS-01 (Plan v1.1 §9 item 1) |

`CANON_CONFLICT_REGISTER` carried unchanged:
- CR-1, CR-2 and CR-3: APPROVED_AS_CHANGED by Thoth;
- CR-4: APPROVED, and CR-5: APPROVED_AS_CHANGED, both by the Product Owner;
- CR-6: APPROVED (a), by the IA through RS-20;
- CR-7 and CR-8: APPROVED (a) each, by the Product Owner.

No new conflict: DC-1 and DC-2 are repository-documentation inaccuracies against code and records.

**Not produced:** a corrective instruction, plan or PR; a QA, Ops or close artifact; a PF10 addendum.

**Not executed:** any repository change outside this record; a live probe; QA or Ops.

**Nonclaims:** this record establishes no QA verdict, acceptance, Ops, deployment, PF09 or PF30 movement, canon drainage or closure.

## 10. TypeSafe and surface

**TypeSafe: not read.** This is a terminal Product Owner return with no receiving session (DOC-20 "Runtime artifacts, readback, and handoff": a Product Owner decision return carries no continuation block). The reading is taken when the Product Owner's direction names the next session.

## 11. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / WU-DOC-01 / DOC-20 / completion 1 |
| change / specification | CRD HDE-CRD-0002 / `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` v1.1, with Specification delta 01 |
| unit | WU-DOC-01 |
| release | GCFPE-20261009.1 / 100926.1 |
| prompt | DOC-20 — Verify Final Repository Documentation Completion — 100926.1, https://app.notion.com/p/3f44590a05eb81d8a582eec0e93e6ee7 (page state of 2026-10-12T02:29:19.255Z) |
| role/stage | continuing whole-change IA / DOC-20 |
| capture time | 2026-10-22T03:43:00Z |
| execution identity | https://claude.ai/code/session_01U3QLYTkfUepeRbSGZNPj9N |
| inherited usage | review v2.0 §12; review v1.0 §13 |
| repository persistence | recorded here only. `docs/changes/GCFPE_PROMPT_PROVENANCE.md` is absent on `main`; persistence is pending and non-gating |

## Canon relied on

Read on `main` at `8187254`. `docs/pfcanon/` was last changed by `e56788c`; PF10 is v13.7.4.

| Decision topic | Sources and sections | How it governs |
| :- | :- | :- |
| DOC-20 operation, result and routing | DOC-20 — Verify Final Repository Documentation Completion — 100926.1, read in full: "Execute" 1 to 5; "Required result"; "Result routing"; "Runtime artifacts, readback, and handoff" | §1, §8: `COMPLETE` only when every obligation is accurate; terminal return when no lawful receiver exists |
| Accepted lineage cannot be reopened | PR-40 — Review PR Work-Unit Lineage — 100926.1, "Accepted-final lineage protection", read in full in this session | §8 |
| Measure; no ceiling | PF10 addendum 2.18, rules 1 and 5 and "Epic, task, and status effects", read in full in this session | §7 |
| Unit scope and routed items | PF10 addenda 2.19 (P-8) and 2.21; instruction §6; plans v1.0 and v2.0 §6 | §4 |
| Writer nonclaims (H-4) | PF10 addendum 2.17 ("WU-DOC-01's usage note for the writer … reads the ADR together with this addendum"); WU-PR-07 result v1.0 lines 172-173; ADR "Stated limits" | DC-1 |
| Real inputs | PF10 addendum 2.11 rule 4 | §6, each finding's "Real input" row |
| Documentation before QA; distinct states | PF19-Canon-Glow-QA-Guide §3.1 "Intent", read earlier in this session; PF04-Canon-HDE-Governance, the QA-10 paragraph ("After accepted PR/Ops delivery and final repository-documentation completion, continuing Isis executes QA-10") and the following paragraph ("Readiness, QA PASS, PR acceptance, documentation completion, repository landing and closure remain distinct states"), read in this invocation | §1, §9: QA-10 waits; this record is not a lineage verdict |
| Source fidelity | PF03-Reference-Technical-Writing-Best-Practices "Truth and source fidelity", read earlier in this session ("Unknown stays unknown. Do not invent … implementation … state") | §6: each finding cites the controlling code |
| Repository rules | `AGENTS.md` "Operating workflow" (closed rails; pytest readiness) | §3 |

**Search:** `git grep -c -i -E 'DOC-20|documentation completion|WU-DOC-01' origin/main -- docs/pfcanon/`. The hits:
- PF10 (42): addenda 2.18, 2.19 and 2.21 govern this verification;
- HDE Governance (2): the two paragraphs cited above;
- the Glow QA Guide (1), the Separation build checklist (1), HDE Phased Epics (5) and Reality Audits (3): HDE-EPIC040 DOC-20 history, not rules.
