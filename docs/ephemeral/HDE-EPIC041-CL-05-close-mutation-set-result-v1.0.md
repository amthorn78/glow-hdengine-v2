---
artifact_type: CLOSE_MUTATION_SET_RESULT
artifact_version: "1.0"
logical_id: HDE-EPIC041-CL-05-CLOSE-MUTATION-SET-RESULT
predecessor: none (first CL-05 output for HDE-EPIC041)
CHANGE_CLASS: EPIC
CHANGE_ID: HDE-EPIC041
epic_name: Separation Pass 4
CLOSE_MUTATION_SET_RESULT: CLOSE_PR_READY
entry: "(a) final QA Report docs/ephemeral/HDE-EPIC041-QA120-final-qa-report-v1.0.md (HDE-EPIC041-QA120-QA-REPORT v1.0, verdict PASS; SHA-256 41a43a887ef1d30db2c50b6d37a4ba17577276c6887abc50cfeece15ad7bcb1b)"
authorization: "the Product Owner's invocation of CL-05 for HDE-EPIC041 in this session (2026-11-01), the Proceed for its close mutation set and close-tooling repair"
tooling_pull_request: "amthorn78/glow-hdengine-v2#811 (base 9f13d9f8, reviewed head 4b3cd3de709055f23a5cabacaffc32605f55419e; merged by the Product Owner 2026-11-01T15:29Z as 7178df65f395f5b5c1cfd827ef3f8c9cd82b2a70)"
close_pull_request: "amthorn78/glow-hdengine-v2#812 (base 7178df65, head ac62c120de2423b10ed3ce7b4a64714353d2b0fe; open, not merged at writing)"
close_commits: "C1 ad5236744dd6f7a7d553bd005063f24a568b9adb; C2 f58c7360602ea0b48add8ec325ad46c57bd198b3; C3 ac62c120de2423b10ed3ce7b4a64714353d2b0fe"
producer: the Close Implementer for HDE-EPIC041 (this CL-05 session; platform identity not directly known and not invented)
closure_authority: Isis, at CL-E-10, after the Product Owner merges #812
prompt: CL-05 — Prepare and Publish the Close Mutation Set — 102726.1 (https://app.notion.com/p/4064590a05eb814fba57ed387ee2cddd; page state 2026-10-27T13:19:06.175Z; read in full)
ecosystem_release: GCFPE-20261027.1 / 102726.1
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.9.7.md (current on main throughout)
authored_at: 2026-11-01 (UTC)
GCFPE_PROMPT_USES:
  - usage_id: HDE-EPIC041-CL05-20261101
    change: HDE-EPIC041 (EPIC)
    specification: docs/ephemeral/HDE-EPIC041-epic-specification-v1.1.md (v1.1)
    work_unit: HDE-EPIC041-CL-05
    ecosystem_release: GCFPE-20261027.1 / 102726.1
    prompt: CL-05 — 102726.1 (https://app.notion.com/p/4064590a05eb814fba57ed387ee2cddd), revision as of 2026-10-27T13:19:06.175Z
    role_stage: Close Implementer / CL-05
    captured_at: 2026-11-01
    runtime_identity: not directly known (D27)
    outcome: CLOSE_PR_READY
    result_references: this record; #811; #812
    repository_persistence: PENDING (no docs/changes/GCFPE_PROMPT_PROVENANCE.md on main; owner GCFPE management; non-gating)
---

# HDE-EPIC041 — CL-05 Close Mutation Set Result v1.0: CLOSE_PR_READY

## 1. Result

`CLOSE_MUTATION_SET_RESULT: CLOSE_PR_READY`.

The close pull request amthorn78/glow-hdengine-v2#812 is open. On its exact head `ac62c120`, the hosted `test` job and the closeout workflow have both passed (§7). It awaits the Product Owner's merge, after which Isis decides closure at CL-E-10.

The close report's decision is `SATISFIED`, with posture review-trace-only. That is the close pack's record of its bound inputs. It is not the closure decision, which Isis makes at CL-E-10.

## 2. Record fields (Plan Templates §3B)

| Field | Value |
| :- | :- |
| Change identity | HDE-EPIC041, Separation Pass 4 (EPIC) |
| Entry | (a): the final QA Report v1.0, `verdict: PASS` (front matter) |
| Authorization | The Product Owner's invocation of CL-05 for HDE-EPIC041 (front matter), plus the decisions of §3 |
| Close mutation set | §5, each item by exact path; all written by the canonical writers |
| Close rehearsal | §4: rehearsal 1 found four close-tooling defects and one input error; rehearsal 2, after the repair, passed with no defect |
| Close-tooling repair | §6: B-1 to B-4 in #811, with owner tests, a close-pack ADR amendment, and the regeneration of HDE-CRD-0002's close pack |
| Close pull request | #812; the Product Owner's merge is pending (§7) |
| Exit | CL-E-10 — Perform Epic Retrospective and Decide Closure, Isis |
| Nonclaims | §11 |

## 3. Product Owner decisions in this session (2026-11-01)

Each decision was given through the session's question tool, with its options and consequences stated.

1. **CCR-5, close-pack ordering.** The ruling is "(B) now, bounded": for HDE-EPIC041 only, CL-05 writes the close pack after QA PASS and before CL-E-10. The correcting HDE Build Notes addendum stays the Product Owner's. Basis: HDE Build Notes 2.2 R-3 governs as written unless the Product Owner rules otherwise (HDE Build Notes 2.5, "Epic, task, and status effects", and 2.7, "CL-05 stops … if the CCR-5 ordering is unresolved"). The ruling is the bounded Product Owner decision AGENTS.md "Canon-first rule" allows for the exact decision it adjudicates.
2. **Epic close-run home.** The ruling is "Admit via tooling PR": an explicit admission of HDE-EPIC041's close run. Close-pack ADR "Stated limits": "an Epic close run needs its own explicit admission". Change Process Guide §3.5.2.1: "an Epic close run needs its own explicit admission". This turned CL-05 step 3c's Epic stop into close-tooling repair (step 4).
3. **ADR binding.** The ruling is "Regenerate CRD-0002 pack". HDE-CRD-0002's committed close pack binds the close-pack ADR and the v2 source schema by SHA-256, so the repair would fail its check. Its close report and manifest were regenerated from the unchanged candidate source by the canonical writer, and republished by the canonical updater, in #811.

## 4. Rehearsals (throwaway clones; never pushed)

**Environment.** All runs used:

- full-history clones (`git rev-parse --is-shallow-repository` printed `false`);
- CPython 3.12.3 with CI's install (`setuptools>=68 wheel -r requirements.txt -r requirements-dev.txt -e .`, `pytest 8.4.2`);
- a `requirements.txt`-only interpreter;
- a `jsonschema`-only interpreter;
- every repository tool run through `env -i` with `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1 GIT_CONFIG_GLOBAL=/dev/null`, with output and exit status captured to files without a truncating pipe.

**Rehearsal 1, on `main` `9f13d9f8`:**

| Step | Command | Exit | Output | Classification |
| :- | :- | :- | :- | :- |
| R1-1 | `python tools/qa/generate_epic_close_pack.py --source audit/EPIC-041_close_candidate_source.json --write` | 1 | `EPIC_CLOSE_PACK_ERROR:SOURCE_SCHEMA_INVALID` (`jsonschema` names `tracked_issues[0..6].id`: `'ISSUE-EPIC041-TI-01' does not match '^TI-[0-9]{3,}$'`) | Close-tooling defect B-1 |
| R1-2 | same, with the candidate B-1 fix | 1 | `EPIC_CLOSE_PACK_ERROR:POINTER_UNRESOLVED` | Close-tooling defect B-2 |
| R1-3 | same, with the candidate B-2 fix | 1 | `EPIC_CLOSE_PACK_ERROR:DEFERRAL_POINTER_UNBOUND` | Input error: the PF09.3 heading's literal text carries `**` markers; corrected in the source |
| R1-4 | same, corrected input | 0 | `EPIC_CLOSE_PACK_WRITE_OK:audit/EPIC-041_close_report.md:audit/EPIC-041_MANIFEST.json` | — |
| R1-5 | `python tools/evidence/update_evidence_index.py` | 0 | No Index row and no path proof for `audit/EPIC-041_*` (0 rows) | Close-tooling defect B-3 |
| R1-6 | The seven checks on clean C2 | 0 × 7 | All pass; the close pack is unregistered | — |
| R1-7 | `publish_crd_close_run_family(HarnessConfig("HDE-EPIC041"), [CheckResult(…)])` | 1 | `ValueError: governed CRD close-run publication admits only HDE-CRD-0001, HDE-CRD-0002; refused None` | Close-tooling defect B-4 |

**Rehearsal 1 operator slips** (no effect on any evidence):

- One invocation of the writer ran in the primary checkout instead of the rehearsal clone. It was refused before any write with `EPIC_CLOSE_PACK_ERROR:INPUT_UNTRACKED`, and `git status` was clean afterwards.
- One check-runner helper had a log-name bug. It was fixed and the checks rerun.
- R1-7's first attempt passed a list as the command and was refused by `CheckResult`; it was rerun with a tuple.

**Pre-rehearsal on the tooling head `4b3cd3de`, before the merge.** Every step passed:

- the writer `--write`;
- the updater, which registered `epic041.close_report` and `epic041.manifest`;
- the seven checks;
- `publish_epic_close_run_family` with nine primaries, leaving the QA manifest and `checks/` byte-identical;
- the seven checks again;
- the writer `--check` with the `jsonschema`-only interpreter, for both HDE-EPIC041 and HDE-CRD-0002.

**Rehearsal 2, on `main` `7178df65`, after #811 merged:**

- **First attempt.** It stopped at checkout: a local clone of the primary checkout did not carry `7178df65` as a branch. Later commands in the same shell line ran on that clone's default branch without the selected interpreter, and wrote nothing. The attempt was discarded.
- **Second attempt.** A fresh GitHub clone checked out `7178df65` and ran the scripted close sequence under `set -euo pipefail`. Every step exited 0:
  - C1, C2 and C3;
  - the seven checks on C2 and again on C3;
  - QA family unchanged;
  - the writer `--check` with `jsonschema` only;
  - `prepush_check.py lanes build-notes`: lanes `evidence` and `release`; `qa` not selected; 0 changed-test targets.

  The rehearsal found no defect.

## 5. The close mutation set (#812, produced on `close/hde-epic041-close-pack` from `main` `7178df65`)

**T1, C1 `ad523674`:**

| Path | What it holds |
| :- | :- |
| `audit/EPIC-041_close_candidate_source.json` (SHA-256 `ba3470e2…a1e3cb`) | The v2 candidate source, `json.dumps(indent=2, sort_keys=True)` plus LF, valid against `schemas/close_candidate_source.v2.json` |
| `audit/docdeltas/hde-epic041_drain_targets.md` (SHA-256 `418473ba…0c6b`) | Names every deferral and tracked-issue ID |
| `README.md`, `AGENTS.md`, `CHANGELOG.md` | One line each, the "only close pack produced with this writer" nonclaim, which the close makes untrue |

**T2 and T3, C2 `f58c7360`:**

| Path | What it holds |
| :- | :- |
| `audit/EPIC-041_close_report.md` (24,729 bytes; SHA-256 `93179f6e…035ea`) and `audit/EPIC-041_MANIFEST.json` (4,671 bytes; SHA-256 `9c30b4bc…7661`) | Writer output |
| Human Index, sentinel, Machine Mirror and checksum, orientation output, path proofs | Updater output |

**T5, C3 `ac62c120`:**

| Path | What it holds |
| :- | :- |
| `audit/qa/hde-epic041/close/<check_id>/primary.log` with its path proof | Nine primaries: `close-pack-write`, `evidence-index-write`, `close-pack-check`, `evidence-index-check`, `orientation-check`, `mirror-schema`, `evidence-index-hash`, `evidence-paths`, `final-lf`. Each is `PASS` with exit 0 |

The T5 primaries:

- Each was rendered from one captured step's command, exit status and output, by `publish_epic_close_run_family`.
- The steps ran 2026-11-01T15:33:13Z to 15:33:27Z. Every primary carries `timestamp_utc` `2026-11-01T15:33:27Z`, the publication's single `captured_at_utc`.
- The Index went from 667 to 678 rows: two close-pack rows and nine close-run rows, each with `epic_id: HDE-EPIC041`.

**Source content:**

- **Records:** the four planning records, by identity and SHA-256.
- **Requirements:** nine requirement IDs, `R-01` to `R-04` and `AC-01` to `AC-05`.
- **QA checks:** the seven QA Plan checks with QA Plan §18's criteria maps.
- **Acceptance:** nine rows, all `MET`, each bound to the manifest and the primaries whose mapping names it, with limitations IR-01, IR-02, N-06, BE-03 and BE-04.
- **Deliverables:** D1 to D5, allocated to WU-PR-01, WU-PR-02, WU-PR-03 and WU-CL-05.
- **Deferrals:** 13. One is in register form: HDE-SEPA006, pointing at HDE Build Checklist Separation's Task heading. The other twelve are in ADR-status form: DELTA-001 to -003, CCR-1, CCR-5, CCR-6, IR-01, IR-02, QR-07, FND-005 to -007.
- **Tracked issues:** ISSUE-EPIC041-TI-01 to -07, as ADR-status lines.
- **Later-drain statements:** four.
- **ADR block:** four decisions: D-1 retire; landing route A; close-pack ordering; Epic close-run admission.
- **Follow-ups:** empty.
- **QA RCA:** 11 summary lines.
- **Excluded binding:** the source does not bind the close-pack ADR (§6).

**T4 and T6.** The seven checks exited 0 on clean C2 and again on clean C3, leaving the tree clean, and the writer `--check` with `jsonschema` only exited 0. Also on clean C3:

- `prepush_check.py lanes build-notes`: PASS. 37 paths; lanes `evidence` and `release`; HDE Build Notes v13.9.7, SHA-256 `413f3e44…5578`.
- `prepush_check.py membership`: PASS, with one `--path` for each of the 37 paths; none is a release member.

**Scope proof.** All 37 changed paths fall within CL-05's allowed changes. Between C2 and C3, and against `main`:

- the diff on `audit/qa/hde-epic041/qa_step_logs_manifest.json` and `checks/` is empty;
- `audit/docdeltas/hde-epic041_doc_deltas.md` is unchanged.

## 6. Close-tooling repair (#811)

| ID | Defect and proven cause | Fix | Owner tests |
| :- | :- | :- | :- |
| B-1 | The v2 `ti_id` pattern `^TI-[0-9]{3,}$` refuses the Epic's own tracked-issue IDs `ISSUE-EPIC041-TI-01` to `-07` (Plan Templates "Tracked Issues"; Specification §11) | `ti_id` also admits `ISSUE-EPIC<NNN>-TI-<nn>`. The writer refuses one naming another Epic (`TRACKED_ISSUE_UNBOUND`) | `test_b1_*`, 4 tests |
| B-2 | Only a CRD may point to its close-run directory before the close run writes it | The change's own close-run directory may be a pointer. A CRD must still point to it; any other absent pointer stays `POINTER_UNRESOLVED` | `test_b2_*`, 5 tests |
| B-3 | The updater admits writer close-pack Index rows for CRDs only | `ADMITTED_EPIC_CLOSE` (HDE-EPIC041 only); absent-tolerant `epic041.close_report` and `epic041.manifest` rows with `epic_id` | `test_epic_close_pack_*`, 2 tests |
| B-4 | No Epic close-run family or publication entrypoint | `publish_epic_close_run_family` and Epic close-run discovery. It renders each primary through the QA harness's renderer, requires the recorded QA family, writes no QA file, and refuses on any change to the QA family | `test_epic_close_run_*`, 4 tests |

**Owner tests.**

- On `main`'s tools, the new writer tests gave 5 failed and 4 passed; the 4 that passed pin the preserved refusals. The updater tests gave 6 failed.
- On the repair:
  - 9 and 6 passed;
  - the full owner files `tests/qa/test_generate_epic_close_pack.py` and `tests/evidence/test_evidence_index_missing_state.py`: 973 passed;
  - the classifier-selected changed tests: 1228 passed.

**ADR amendment.** `docs/adr/hde/close_pack_writer_adr.md` gained a 2026-11-01 amendment recording B-1 to B-4. Decisions 7 and 8 and the stated limits are updated. The Product Owner's merge of #811 adopted it.

**Narrowed rule.** One rule recorded in the ADR was narrowed: "No Epic close-run family is admitted" now admits HDE-EPIC041 only. The basis is the Product Owner's explicit admission (§3, item 2), which the ADR's own limit required. That rule refused the change's own same-run close evidence of record (CL-05 step 4.5; Change Process Guide §3.5.1, "Close-tooling repair").

**Brittle binding found.** HDE-CRD-0002's committed close pack binds the close-pack ADR and the v2 source schema by SHA-256. So both B-1 and the ADR amendment failed its check, with `MANIFEST_BINDING_MISMATCH` (reproduced). It was regenerated in #811 (§3, item 3); only its two source-binding digests changed, and its close-run family is unchanged. HDE-EPIC041's source does not bind the ADR, so it does not repeat the problem.

**Hosted results for #811, on head `4b3cd3de`:**

- `test` job, run 41313876273: success. It selected lanes product, compat, evidence, qa and release, and ended `CI_APPLICABILITY_AND_EXACT_HEAD_OK`.
- Closeout workflow, run 41313876303: success. It ran in tooling mode with `Closeout candidate: audit/HDE-CRD-0002_close_candidate_source.json` and `EPIC_CLOSE_PACK_CHECK_OK`.
- Codex code review: no findings. Review threads: none.

## 7. Close pull request #812: hosted results

Exact head `ac62c120de2423b10ed3ce7b4a64714353d2b0fe`, base `7178df65`:

- **Hosted `test` job,** run 41321934313: success, 15:34:50Z to 15:41:37Z. It selected lanes `evidence` and `release`, both with outcome success; `qa` was skipped. It ended `CI_APPLICABILITY_AND_EXACT_HEAD_OK`.
- **Closeout workflow,** run 41321934297: success. The repository event that started it was the `pull_request` opening of #812, which changes `audit/EPIC-041_*`; there was no dispatch. It printed `Closeout candidate: audit/EPIC-041_close_candidate_source.json` and `EPIC_CLOSE_PACK_CHECK_OK:audit/EPIC-041_close_report.md:audit/EPIC-041_MANIFEST.json`. The six retained read-only checks and the clean-tree check passed.
- **Codex code review** of `ac62c12`: completed with no findings. Review threads: none.
- **Merge:** pending, the Product Owner's.

## 8. Measures named by the change's records, as observed

- **QA evidence of record:** unchanged. The diff on the QA manifest and `checks/` is empty from C2 to C3 and against `main`. The 14 QA Index rows are unchanged.
- **Release:** no release member is touched (37 of 37 not members; release 1.3.0, 45 members). No `catalog/manifest.json` or `ADMITTED_RELEASE_*` change.
- **Product code:** not touched by #811 or #812.
- **PF-Canon and HDE Build Notes:** not touched.

## 9. Deviations and limitations

- **Bounded Product Owner ruling on CCR-5.** For HDE-EPIC041 only, the close-pack write precedes the closure decision, contrary to HDE Build Notes 2.2 R-3 as written. The correcting addendum is not yet published.
- **Acceptance map.** The approved Specification §10 lists an acceptance map and its viability log (Ruling R-A; TI-07; CCR-1). CL-05's allowed changes do not include one, and no canonical writer for a tokenless acceptance map exists. None is written. The close report's exact-source acceptance section binds each criterion, and CCR-1 is deferred to the Product Owner. Isis judges this at CL-E-10.
- **Single publication timestamp.** The nine close-run primaries carry the publication's single `captured_at_utc`, 15:33:27Z, not each step's own time (15:33:13Z to 15:33:27Z). The publication API takes one timestamp, as for HDE-CRD-0002.
- **Owner test scope.** The full owner-file run (973 passed) ran on #811's first commit. The second commit changed only the ADR wording and the regenerated HDE-CRD-0002 bytes, and the hosted `test` job passed on the final head.
- **Execution venue:** not claimed.

## 10. TypeSafe reading and surface advice for CL-E-10

- **Method.** The installed TypeSafe scoring skill, request v8.2. The script ran once with session kind `review` and label "HDE-EPIC041 CL-E-10 retrospective and closure decision". No Notion row was written.
- **Action sent (v8.2).** "As the continuing closure authority, perform the retrospective of one already-reviewed Epic and decide CLOSE or DO_NOT_CLOSE: read its merged close pull request (one close report, one manifest, two ledgers, nine close-run primaries and their index rows, about 37 files), its final QA report and RCA and about ten earlier records, check them against a written stage procedure and canon, and record one closure decision; no code is changed, no live run against a provider occurs, and the Product Owner's post-closure updates follow."
- **Reading, as printed.** `TypeSafe v8.2: Opus 5.5 at extra high.` Effort score 2.81 (confidence 0.61); rung probabilities low 0.01, medium 0.08, high 0.20, extra high 0.52, max 0.19, ultracode 0.00. Model probabilities Fable 5.1 0.02, Opus 5.5 0.95, Sonnet 5.5 0.03, Haiku 5.5 0.00 (confidence 0.93). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.002, Fable 5.1 at high 0.004, Fable 5.1 at extra high 0.010, Fable 5.1 at max 0.004, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.009, Opus 5.5 at medium 0.076, Opus 5.5 at high 0.190, Opus 5.5 at extra high 0.494, Opus 5.5 at max 0.180, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.000, Sonnet 5.5 at medium 0.002, Sonnet 5.5 at high 0.006, Sonnet 5.5 at extra high 0.016, Sonnet 5.5 at max 0.006, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Flags: none. Sent 2026-11-01T15:35:02Z. Nathan picks the cell.
- **Picks.** Nathan stated no model or setting for this session or for CL-E-10; none is recorded.
- **Surface advice (CL-E-10).**
  - A standalone top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, entered with the handoff after Nathan merges #812.
  - Read access to `main` and to GitHub for #811 and #812.
  - A full-history clone with a `requirements.txt`-only interpreter, if the closure review re-runs the read-only checks or the writer `--check`.
  - No vendor, database, Railway, deployment or open-rails access.

## 11. Nonclaims

- **What this record is.** This record and the close mutation set do not reopen implementation, QA or the closure decision.
- **What it changes.** They change no approved QA evidence, product code, PF-Canon, HDE Build Notes, PF09, PF30 or board state.
- **What it does not establish.** They establish no closure, acceptance, QA verdict beyond QA-120's, canon drainage, Ops, deployment or release.
- **Merging.** Merging this record preserves it and approves nothing (D21-C).

## 12. Prompt defects reported to the GCFPE-MGMT-10 maintenance owner

| ID | Prompt identity | Expected behaviour | Actual behaviour | Evidence |
| :- | :- | :- | :- | :- |
| PD-1 | CL-05 — 102726.1, "Execute" step 3c | Step 3c says "An Epic close stops here after its rehearsal". The expected route was close-tooling repair once the Product Owner admits the Epic's close run | The step reads as an unconditional stop, although step 4 and Change Process Guide §3.5.1 cover a missing admission as close-tooling repair | §3, item 2 |
| PD-2 | CL-05, "Allowed changes" | Allowed changes should cover another change's close pack that a close-tooling repair invalidates, because it binds the ADR or schema by digest | Not listed; it needed a Product Owner decision | §3, item 3; §6 |
| PD-3 | CL-05, "Inputs" | The approved Specification lists an acceptance map; the expected route was to write it or to defer it | No writer or allowed path exists for it | §9 |

## Canon relied on

Resolved from `docs/pfcanon/` on `main`. Each identity resolved to one controlled Markdown file. The search used `grep -n -i` over `docs/pfcanon/*.md` and `docs/ephemeral/HDE-EPIC041-*`, with these terms: close mutation set, close-run, close pack, CCR-5, acceptance map, tracked issue, Epic close run.

| Title (file) | Sections read | Used for |
| :- | :- | :- |
| Change Process Guide (`PF06-Canon-Change-Process-Guide-v2.5.5.md`) | §3.5.1 "Requirement", including "Close-mutation-set stage" and "Close-tooling repair"; §3.5.2.1 "Close-pack files"; §3.5.2.2; §3.5.2.3; §3.5.2.4 "Repo-docs and evidence updates (same PR)"; §1.0.6 "QA and closeout"; §3.5.4 "ADR block in the close-pack (all epics)"; §0.4.1.2 by its RCA contents, as QA-120 applied them | Stage authority, repair route, Epic close-run admission, close PR contents, crib notes and Doc-Delta note, ADR block |
| Plan Templates (`PF27-Canon-Plan-Templates-v2.0.6.md`) | §3B "Close Mutation Set Task Record (Template)", whole; "Tracked Issues" | This record's fields; the tracked-issue ID form (B-1) |
| Glow QA Guide (`PF19-Canon-Glow-QA-Guide-v3.0.7.md`) | §3.1.3 "Permanent drainage and post-closure administration"; "Close report requirements (validator-bound; mechanical)"; the close-run row of the evidence layout table under "Close-pack truthfulness and same-run execution" | Ordering, close report pointers, close-run family |
| HDE Schemas and Artifacts (`PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.7.md`) | §8.17 "Live QA evidence layout", change-container identity | QA root and close-run home |
| HDE Governance (`PF04-Canon-HDE-Governance-v2.8.8.md`) | The closeout-record list: coverage ledger, accepted-deviation accounting, deviation notes, the tracked-issue `ADR status line:` form | Coverage and deviation accounting; tracked-issue rendering |
| HDE Build Checklist Separation (`PF09.3-Canon-HDE-Build-Checklist-Separation-v1.1.8.md`) | Task HDE-SEPA006 headings | Deferral register heading |
| HDE Build Notes (`PF10-HDE-Build-Notes-v13.9.7.md`) | "Precedence, versioning, and scope" §1; the Addendum Index; 2.2 (R-1 to R-3) in full; 2.5 PF09 row-closure record, "Required canon drainage" and "Deferred obligations"; 2.7 by its CCR-5 and CL-05 lines | R-3 and CCR-5; no planning-document or versioned-PF input; open items |
| Close-pack ADR (`docs/adr/hde/close_pack_writer_adr.md`) | Whole, read with HDE Build Notes | Writer rules; the stated limits repaired |
| AGENTS.md | "Canon-first rule"; "Governed evidence rules"; "Evidence attribution, currentness and distinct decisions"; "Pre-push check"; "PR descriptions" | Procedure, PR bodies, distinct facts |

> Applicable, active, non-superseded PF10 addenda supersede conflicting PF-Canon only for the exact scope they address; otherwise follow PF-Canon. A formally approved bounded Product Owner rescope may supersede conflicting PF-Canon only for the exact decision it adjudicates.

In-flight inputs, each at its highest version and read for the facts the source records:

- the Specification v1.1;
- the Implementation Plan v1.1;
- the QA Plan v1.0, §14, §15, §18 to §21 and the check mapping lines;
- the QA-10 change audit triage v1.0, §6 CCR-5;
- the Specification review v1.0, Ruling R-A;
- the QA-120 Report v1.0 and RCA v1.0.

No closure decision exists, since this is entry (a).
