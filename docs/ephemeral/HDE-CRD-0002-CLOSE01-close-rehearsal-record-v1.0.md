---
artifact_type: CLOSE_REHEARSAL_RECORD
artifact_version: "1.0"
logical_id: HDE-CRD-0002-CLOSE01-CLOSE-REHEARSAL-RECORD
predecessor: none
change_id: HDE-CRD-0002
change_class: CRD
author: Isis (Isis-53), continuing Lead Developer and terminal closure authority for HDE-CRD-0002
session: https://claude.ai/code/session_01NxRhYei7RDGmMPYdKEkpok
requested_by: Nathan / Product Owner, 2026-10-26 ("create a task to create the close pack. The prompt should be created by you (Isis).")
purpose: prove, before the task prompt is issued, that its steps produce HDE-CRD-0002's close mutation set from the real records; scratch work only, nothing pushed from the rehearsal clones
finding: B-4 (§3), the closure finding that CL-C-10 v1.1 routes to ESC-30
captured_at_utc: 2026-10-26T02:05:59Z
repository_head_read: origin/main 58a27859495c21d16d8d5761be1104e502bd56d1, plus the CL-C-10 v1.0 record of pull request #747 (commit fb1ae131, docs/ephemeral only)
---

# HDE-CRD-0002 — Close rehearsal record (CLOSE01), v1.0

## 1. Result

- **The close mutation set cannot be produced with the writer on `main`.** Run r4 (the reference inputs, the writer as merged) stops at T2 with `EPIC_CLOSE_PACK_ERROR:SOURCE_SCHEMA_INVALID`. The cause is finding **B-4** (§3).
- **B-4 is the only blocker found.** Run r3 applies a narrow scratch exemption for B-4 and nothing else. With it, every step of Plan v1.1 WU-PR-07 T1 to T6 passes on the same inputs, and so do the hosted closeout job's seven checks under a requirements-only install, the writer's `--check` with `jsonschema` alone, and an idempotent re-run. The evidence-lane and qa-lane test selections also pass on r3's final commit (§4.4).
- **The reference inputs are the bytes r3 validated** (§5). The task prompt `docs/ephemeral/HDE-CRD-0002-CLOSE01-close-mutation-set-task-prompt-v1.0.md` uses them as a reference the close session re-verifies.

## 2. Method

| Item | Value |
| :- | :- |
| Clone | A fresh `git clone --no-hardlinks` of this repository per run, in the session scratch directory. Never pushed |
| Base | `58a27859`, then a merge of `fb1ae131` (the CL-C-10 v1.0 record of #747) as a stand-in for the Product Owner's merge. The driver asserts that the merge adds only that record |
| Rails | `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`, `GIT_CONFIG_GLOBAL=/dev/null`, `PYTHONPATH=<clone>` |
| Interpreters | CPython 3.12.3 with CI's full install (`requirements.txt`, `requirements-dev.txt`, `-e .`); a venv with `requirements.txt` only (the hosted closeout job's install); a venv with `jsonschema` only |
| Driver | `docs/ephemeral/HDE-CRD-0002-CLOSE01-rehearsal-driver-v1.0.py` (SHA-256 `db4a241ae8eed093ec1549ff9501bbf00ac4fd5020cb929ac2d8a0e2a8490ad3`), adapted from the WU-PR-07 lineage review's Appendix A driver (SHA-256 `1bec66df67d4ea7c3a61660309317d914eb62e982b90a8d7668721c507621b77`, verified byte for byte before adapting) to the real records |
| T1 inputs | `docs/ephemeral/HDE-CRD-0002-CLOSE01-reference-inputs-builder-v1.0.py` (SHA-256 `f39a97e7d867bc4f8a7c2973e93c7e4217dbfd848ae3a18f0f22038cfa692491`): writes the candidate source and the two ledgers and applies the RF-12 lines |
| Scratch prototype (r3 only) | `docs/ephemeral/HDE-CRD-0002-CLOSE01-rehearsal-scratch-prototype-v1.0.py` (SHA-256 `cfbf355d649bc50d6c94e4a6e492e31467f0224235103e625d604a4d37cd090d`). It is a diagnostic, not a proposed implementation (§3.5) |
| Capture time | The close-run family was published with the fixed rehearsal time `2026-10-26T00:00:00Z` |

Usage: `python <driver> <repo> 58a27859495c21d16d8d5761be1104e502bd56d1 <empty-workdir> <label> <full-venv-python> <jsonschema-only-python> <requirements-only-python> origin/docs/hde-crd-0002-cl-c-10-closure-decision <builder> [<prototype>]`.

## 3. Finding B-4 — the v2 writer refuses HDE-CRD-0002's own QA evidence for S06

### 3.1 Observed

Run r4, step T2: `python tools/qa/generate_epic_close_pack.py --source audit/HDE-CRD-0002_close_candidate_source.json --write` exits non-zero with `EPIC_CLOSE_PACK_ERROR:SOURCE_SCHEMA_INVALID`. Validating the same source against `schemas/close_candidate_source.v2.json` with `jsonschema` gives exactly one error:

`['evidence_inputs', 14, 'path'] 'audit/qa/hde-crd-0002/checks/qa-03-attestation-debian/primary.log' should not be valid under {'$ref': '#/$defs/feedback_dependency'}`

### 3.2 Cause (proven)

1. The schema types every `evidence_inputs[].path` as `causal_repository_path`, which is `repository_path` and "not `feedback_dependency`" (`schemas/close_candidate_source.v2.json` lines 27 to 29 and 472 to 480; blob `b3b774233ad2`). The writer applies the same pattern again to every causal string (`_require_feedback_free_values_v2`, `tools/qa/generate_epic_close_pack.py` lines 2400 to 2410; blob `c1ef3fca9221`). Both landed with WU-PR-07 (#668).
2. The pattern rejects the word "attestation" between non-alphanumeric characters. QA check 3's ID is `qa-03-attestation-debian`, so its primary's path is refused.
3. The writer requires each `MET` criterion to bind the primary of a `PASS` check whose QA plan mapping names it (PO-35-21; ADR "Stated limits"; `ACCEPTANCE_EVIDENCE_UNBOUND`). In approved QA Plan v1.3 (blob `3aea6033e3c0`), only check 3's "Surface / D-goal mapping:" line names S06 (§6 and §10).
4. `SATISFIED` needs every requirement ID to have a `MET` row (`REQUIREMENT_COVERAGE_INCOMPLETE`, `DECISION_CONTRADICTION`).

So no source can give HDE-CRD-0002 a `SATISFIED` close pack with the writer as merged. A `NOT SATISFIED` pack would state a follow-up for a requirement QA proved, which is untrue.

### 3.3 What it is and is not

- **It is a defect of delivered S21 capability, found at closure.** S21's acceptance intent is that "the writer produces a canon-conforming close report and manifest from tracked inputs for an Epic or a CRD". Its stated first use is this change's own Close Gate: Plan v1.1 §9 item 5, and the Audit's "S21 completes before HDE-CRD-0002 enters its ordinary Close Gate". For that use it fails.
- **The refusal's intent is not wrong.** It keeps hosted results, receipts and attestations out of a close pack's causes. Here it matches a word inside the change's own QA check ID, a QA-governed primary that the bound step-logs manifest lists. That is a false positive of a string rule.
- **Why no earlier stage caught it.** QA check 14 ran the writer's tests and states "no close pack or candidate source is produced; the business-case measure is the real close (after QA-120)" (QA Plan v1.3 check 14 Nonclaims). The WU-PR-07 lineage review's rehearsal used stand-in check IDs. The QA Plan's check IDs were written after the writer merged, and no review compared them with the writer's refusal. My five QA-70 reviews and my CL-C-10 v1.0 did not either.
- **Other words.** No other HDE-CRD-0002 check ID or bound path contains a refused word. The source's free text avoids them by design. S06 and S11 row text is bound by reference, never copied (ADR decision 6).

### 3.4 Constraints any remedy meets (from the records)

- PO-35-21 binding rule: a `MET` criterion binds a mapped `PASS` primary.
- ADR decision 6: "The v1 feedback-dependency refusal applies unchanged to every v2 causal value". A remedy that narrows it changes an approved ADR decision. The ADR and its amendments are the Product Owner's (AQ-1; HDE Build Notes 2.15, 2.17).
- The v1 path, its refusals and output bytes stay unchanged (ADR decision 1).
- QA check 14's PASS predicate pins "905 passed" for `tests/qa/test_generate_epic_close_pack.py`. A remedy that adds tests changes that count, so S21's tested state changes after the QA verdict. Whether and how it is re-verified is for ESC-40 to decide (AGENTS.md, "Evidence attribution, currentness and distinct decisions").
- The approved QA evidence is not edited. Renaming check 3 would reopen an approved QA manifest (CC-2).

### 3.5 The scratch prototype (diagnostic only)

The prototype adds a second accepted form for `evidence_inputs[].path`: `audit/qa/<change-dir>/checks/<check_id>/primary.log`. It also skips the writer's refusal for values that fully match that form. It proves only that nothing else blocks the close.

It is not a proposed implementation. It exempts the path form for any change directory and any check, whether or not the bound QA step-logs manifest lists it, and it adds no test. ESC-30 owns the remedy proposal.

## 4. Runs and outcomes

### 4.1 Run r4: reference inputs, writer as merged

| Step | Outcome |
| :- | :- |
| Base and stand-in merge | `6988f2eb` (stand-in), adds only the CL-C-10 v1.0 record |
| T1, commit C1 | `28099612` |
| T2 writer `--write` | **Refused**, `EPIC_CLOSE_PACK_ERROR:SOURCE_SCHEMA_INVALID` (B-4) |

### 4.2 Run r3: reference inputs, plus the scratch prototype

| Step | Outcome |
| :- | :- |
| Stand-in merge `P` | `14f8e6ec` |
| Prototype commit | `6c51dfa0` |
| T1, C1 | `55897628`: candidate source, both ledgers, the RF-12 lines in `README.md`, `AGENTS.md` and `CHANGELOG.md` |
| T2 writer `--write` | Exit 0 |
| T3 updater | Exit 0. C2 is `30e81259` |
| T4: writer `--check`, `update_evidence_index.py --check`, `orientation_demo.py --check`, `check_mirror_schema.sh`, `check_evidence_index_hash.sh`, `validate_evidence_paths.py`, `check_final_lf.sh` | All exit 0 on clean C2. The tree stayed clean |
| T5 `publish_crd_close_run_family` | Nine close-run primaries (the two T2 and T3 writes and the seven T4 checks) with path proofs under `audit/qa/hde-crd-0002/close/`. C3 is `dfd7bd66`, tree `b0073be2` |
| QA evidence untouched | `qa_step_logs_manifest.json` and `checks/` unchanged between C2 and C3 |
| T6, the T4 set again on clean C3 | All exit 0 |
| Hosted closeout job's seven checks, `requirements.txt`-only interpreter, job environment, no `PYTHONPATH` | All exit 0. The writer printed `EPIC_CLOSE_PACK_CHECK_OK:audit/HDE-CRD-0002_close_report.md:audit/HDE-CRD-0002_MANIFEST.json` |
| Writer `--check` with `jsonschema` only | Exit 0, the same line |
| Tree after those checks | Clean |
| Idempotence: T2, T3 and T5 again on clean C3 with the same captures | No byte changed |
| Close files | 20 tracked: the close report and manifest and 18 close-run files (9 primaries and 9 path proofs) |
| Report decision lines | `- Closure decision: SATISFIED`; `- Decision posture: review-trace-only` |
| Commands | 61, none non-zero |

Close-only diff, from the prototype commit to C3: 38 paths. `tools/ci/prepush_check.py --base 6c51dfa0 --head dfd7bd66 lanes` reports `lanes=evidence,release`, `changed_tests=false` and no changed-test targets. Membership: none of the T1 paths is a release member (`membership: not-member` for each; roster 45, `1.3.0`).

The 38 paths are:
- the three RF-12 files;
- the Index, sentinel, Mirror, Mirror checksum and orientation output, each with its path proof;
- the close report and manifest with path proofs;
- the candidate source and the two ledgers;
- the 18 close-run files.

### 4.3 Run r2

Run r2 matched r3, with an earlier wording of one deferral. r3 supersedes it.

### 4.4 Lane proxies on r3's C3 (FND-001 remedy measure (2))

| Selection (as `.github/workflows/ci.yml` names it) | Outcome |
| :- | :- |
| Evidence lane: `refresh_step_logs_manifest.py --check`, then the six-file pytest selection | Exit 0; 134 passed in 1,110 s |
| qa lane: the seven-file pytest selection | 488 passed in 22.6 s |
| Tree before and after | Clean |

These are local proxies, not CI's result. The three files measure (2) protects (`tests/evidence/test_evidence_index_missing_state.py`, `tests/evidence/test_evidence_skeleton.py`, `tools/qa/qa_harness.py`) are unchanged.

## 5. Reference inputs (validated bytes)

| File | SHA-256 | Bytes |
| :- | :- | :- |
| `docs/ephemeral/HDE-CRD-0002-CLOSE01-reference-close-candidate-source-v1.0.json` (committed as `audit/HDE-CRD-0002_close_candidate_source.json`) | `8cc61a4bac5b93e634d96d16fbb1fbe60712e71276dfb6b2a9cfb6a35dcd8992` | 25,520 |
| `docs/ephemeral/HDE-CRD-0002-CLOSE01-reference-doc-deltas-v1.0.md` (as `audit/docdeltas/hde-crd-0002_doc_deltas.md`) | `97935031d989845d0cc5767393d40d86907135a59606dc7976dd5c92e298ffd0` | 1,502 |
| `docs/ephemeral/HDE-CRD-0002-CLOSE01-reference-drain-targets-v1.0.md` (as `audit/docdeltas/hde-crd-0002_drain_targets.md`) | `ea98432dd143843007a6f0be0b7371c94aa2eeb7410eec046afb91411ce79714` | 2,382 |

Generated in r3, for comparison only (not committed): close report SHA-256 `a71d80e1e39925f8abadd2ce7d61606bb32bcb38e0e4624170d73acfa5dabbec`, manifest `fdb36ab125d9732a5bd43102811bc99c750c0763b6a12f9410615a483f731b93`. They will differ in the real close, because the remedy changes the writer and schema.

## 6. Rules the rehearsal established for the source text

| ID | Rule | Basis |
| :- | :- | :- |
| RH-1 | No source string may name check 3 by its ID. Refer to it as "check 3". The same refusal applies to any text containing "attestation", "receipt", "release identity", "release_id", "run ID", "CI result", "commit SHA", "source commit" or "later commit" (the `feedback_dependency` pattern) | Schema `$defs/feedback_dependency` |
| RH-2 | `follow_ups` is empty. `SATISFIED` refuses any follow-up, so open items are deferrals. This corrects CL-C-10 v1.0 §8 R-1, which listed "the follow-ups" | Writer `DECISION_CONTRADICTION` |
| RH-3 | Every deferral takes the ADR-status form: HDE-CRD-0002 has no PF30 record (CR-1), and its drain-target pointers would bind a PF30 heading | ADR "Stated limits" |
| RH-4 | The QA RCA is embedded as `summary_lines`. The QA-120 RCA lives in `docs/ephemeral/`, and the binding form accepts only `audit/HDE-CRD-0002_QA_RCA.md` | Writer `QA_RCA_UNBOUND` |
| RH-5 | The doc-deltas ledger lists items with `- `. A table is not a list | Writer `DOC_DELTAS_INVALID` |
| RH-6 | Ops records whose file names contain "receipt" cannot be bound. None is needed | RH-1 |
| RH-7 | The approved Specification, QA plan and QA report bound must be each family's highest tracked version, and `plan_path` the highest Implementation Plan version | Writer `*_NOT_CURRENT` |
| RH-8 | PF titles are the writer's file-name titles, for example "HDE Schemas and Artifacts", "HDE CLI API Vendor Ref", "Plan Templates" | Writer `PF_TITLE_UNKNOWN` |

## 7. Nonclaims

- This record produces no close pack and no governed evidence. Nothing from the rehearsal clones was pushed.
- It changes no code and proposes no implementation; the prototype is diagnostic.
- It is not QA, not CI's result, and not a closure decision.
- Its lane proxies are local runs.

## Canon relied on

Read on `main` at `58a27859`:

- PF06-Canon-Change-Process-Guide v2.5.4: §3.5.1; §3.5.2.1 to §3.5.2.4, read in full (close PR contents, exact-source acceptance, binary decision, Index and Mirror trio, same-run execution evidence); §3.5.4 (ADR block, closure override, "No posture-only PASS"), read in full.
- PF04-Canon-HDE-Governance v2.8.7: the closeout-record list (deferrals, coverage ledger, accepted-deviation accounting, no over-claim), at lines 900 to 920.
- HDE Build Notes v13.8.2: 2.15 and 2.17 (the writer and its rules); 2.24 (FND-001 measure (2)).
- `docs/adr/hde/close_pack_writer_adr.md` (blob `fcaa9da66fb7`): Decision 1 to 9 and "Stated limits", read in full; "Affected canon and drainage consequences".
- Approved QA Plan v1.3 §6, §10 and check 14.
- `AGENTS.md`: "Evidence attribution, currentness and distinct decisions"; closed rails.
