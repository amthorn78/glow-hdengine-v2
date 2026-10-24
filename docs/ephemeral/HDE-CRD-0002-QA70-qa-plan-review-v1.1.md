---
artifact_type: QA_PLAN_REVIEW
artifact_id: HDE-CRD-0002-QA70-QA-PLAN-REVIEW
artifact_version: "1.1"
predecessor: docs/ephemeral/HDE-CRD-0002-QA70-qa-plan-review-v1.0.md (DENY of QA Plan v1.0; blob b083486fc768; SHA-256 abc0a18311fe4132b0690d9a8a3e1ae8ce97309edf46899a975321e0dfe47fa6; unchanged)
REVIEW_MODE: INITIAL_QA_PLAN_REVIEW
AUTHORING_CONTEXT: INITIAL_OR_PREAPPROVAL_AUTHORING
prompt_mode: REVIEW
decision: DENY
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
change_name: "Post-HDE-EPIC040 Repair: Carried Defects, Code Security Review, Pre-Push Check and Close-Pack Writer"
reviewer: Isis (Isis-53), continuing Lead Developer and QA Plan decision owner for HDE-CRD-0002 (execution identity https://claude.ai/code/session_01NxRhYei7RDGmMPYdKEkpok, the session of review v1.0)
session_disposition: continuing Isis context, as the QA-80 handoff routed it
context_conflict: none
prompt: QA-70 — Review Whole-Change QA Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb81209128ea7c82938faf; page state 2026-10-12T02:29:54.691Z, unchanged since review v1.0; read in full at this invocation)
prompt_release: GCFPE-20261009.1 / 100926.1
QA_PLAN_ID: docs/ephemeral/HDE-CRD-0002-QA50-qa-plan-v1.1.md (QA_PLAN v1.1, PLAN_PENDING_REVISED; blob b1131351570a; SHA-256 fc830f58b4e7248ad90462555568bdc58fd9448e93f7db29a05f2aef09a55dc2; 103,443 bytes, 724 lines; read in full)
QA_PLAN_PREDECESSOR: docs/ephemeral/HDE-CRD-0002-QA50-qa-plan-v1.0.md (v1.0, denied by review v1.0; blob bd49f7c232cd; unchanged)
REDLINE_APPLICATION_REPORT_ID: docs/ephemeral/HDE-CRD-0002-QA80-redline-application-report-v1.0.md (blob 1722268d6eda; SHA-256 313710521602d25ca7d4af1f7831db5907cf25b8e868d9bd55ace7cca184aa8d; read in full)
QA80_CHECKPOINT_ID: docs/ephemeral/HDE-CRD-0002-QA80-checkpoint-v1.0.md (blob 37a413296ac8; read in full)
QA_AUDIT_ID: docs/ephemeral/HDE-CRD-0002-QA50-qa-audit-v1.0.md (QA_AUDIT v1.0, AUDIT_COMPLETE; blob eed40533c7b4; unchanged; read in full at review v1.0, §5 re-read here)
author: Kronos, the QA authority for HDE-CRD-0002 (execution identity https://claude.ai/code/session_01PnD4YNbFZStRQWZ7TCM6jV)
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.7.8.md (519,440 bytes; SHA-256 42459e54e4a14eb89a1cd3be80eae8458a5b1c2c50e1fca1b1ce9882b05e6f9b; byte-identical to the version review v1.0 read)
repository_head_read: origin/main f75733db8286160f044724004b6865d3349ed813 (amthorn78/glow-hdengine-v2#722, committed 2026-10-24T04:54:27Z); code outside docs/ephemeral/ and docs/pfcanon/ identical to 0b15328d
PF10_ADDENDUM_OUTPUT: NONE (an initial-mode DENY produces no addendum)
canon_conflict_register: CR-1 to CR-11 carried unchanged, as Plan v1.1 §13 records them; no new conflict (§5)
decision_time_utc: 2026-10-24T05:06:56Z
next_prompt: QA-80 — Revise Whole-Change QA Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb818789e9ff3ffa9e06d8), the same Kronos author
handoff: docs/ephemeral/HDE-CRD-0002-QA70-handoff-to-qa80-v1.1.md
---

# HDE-CRD-0002 — QA Plan Review v1.1 (QA-70, re-review of Plan v1.1)

## 1. Decision

**`DENY`.** QA Plan v1.1 applies all fourteen redlines of review v1.0, each once, and changes nothing outside their regions and QA-80's bookkeeping (§3). Nine of the eleven earlier findings are fully corrected; FND-001 and FND-003 are corrected except where FND-101 and FND-102 arise. One new Blocker remains, introduced by the revision's own text:

- **FND-101 (Blocker).** Common rule A applies the E-L readiness reads to check 21's test copy: HEAD equals the tested commit, the clone is not shallow, and `git status --porcelain` is empty. That copy must hold the published evidence family. If the family is uncommitted, the status is not empty; if it is committed, HEAD is not the tested commit. So check 21 is `TOOLING_BLOCKED` in every run, S22 can never pass, and §11's `verdict: PASS` is unreachable.

It meets the blocker test of HDE-Governance §9.8.3: as written, the operator cannot execute check 21 in any target environment. Its root is partly this reviewer's: review v1.0's RL-05 required "the clone is at check 1's recorded tested source" for every executable check without declaring the coupled constraint for check 21's copy (Plan Templates "Coupled-constraint rule"). Under Plan Templates' "Non-author penalty rule" it is not author churn.

One Caveat (FND-102) is corrected in the same revision: check 20's P4 reports any configured sink path as absolute, because it resolves the path before testing it.

The Plan returns to the same Kronos author through QA-80 with three redlines on three regions (§6). Everything else in v1.1 is kept as written.

**What is verified and kept** (observed at `f75733d`, §2):
- The provenance block, the full-history E-L class and check 1's history reads; check 15's outcomes.
- V-B's interpreter and check 20's P1, P2 (it matches HDE CLI/API/Vendor Ref §7.1.11b) and its classification rules.
- Common rule B, whose order is Plan Templates' causal precedence.
- Check 13's race placement; check 16's full `/internal/version` checklist and HTTP/1.1 protocol rule, whose commands run as printed.
- §9's rerun authority and attempt-1 preservation; the CR-11 record.
- The 21 checks and their mappings, unchanged from v1.0 as the close writer parses them.

This review produces no PF10 addendum. It is not task selection, execution, a QA result, a merge or a closure decision.

## 2. Review method and independent checks

All rows are planning validation by the reviewer, **observed** at `f75733d`. None is QA evidence; nothing from them was committed or published. No production, vendor, Railway or database access was used.

**Environment.**
- A throwaway full-history clone of `main`, detached at `f75733d`, outside the repository.
- A CPython 3.12.3 venv with CI's full install (`python -m pip install 'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e .`; exit 0; `pytest 8.4.2`).
- Commands ran under `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1` with every vendor and database name unset and `XDG_STATE_HOME` an empty scratch directory, unless a row says otherwise.

| # | Object | What ran | Result (observed) |
| :- | :- | :- | :- |
| 1 | Region discipline | `git diff --no-index -U0` of Plan v1.0 and v1.1 | 38 hunks (141 lines added, 70 removed), each inside an RL-01 to RL-14 region or QA-80's bookkeeping (front matter, title, §0 revision row, §15, Canon relied on, provenance), as the application report §6 states |
| 2 | Close-writer parsing | `_requirement_ids`, `_qa_plan_checks` and `_qa_plan_mapping` from `tools/qa/generate_epic_close_pack.py` on v1.0 and v1.1 | 22 requirements; 21 checks each, equal; mappings equal; all 22 requirements mapped |
| 3 | Plan lint (HDE-Governance §9.8.3; Glow QA Guide §3.4.10) | Byte scan of v1.1 | No U+2026, no three consecutive full stops, no fenced block, no CR; one final LF |
| 4 | Full-history reads (checks 1 and 15) | `git rev-parse --is-shallow-repository`; `git cat-file -e '7136040^{commit}'`; check 1 step 1's diff; check 15 step 3 | `false`; exit 0 (`7136040` is the #627 merge, as HDE Build Notes 2.4 records); empty diff against `0b15328d`; `git log --oneline 7136040^..HEAD -- pyproject.toml` prints nothing |
| 5 | Rule A E-L reads | Rule A's first bullet, in the clone | HEAD `f75733d`; `false`; empty status; Python 3.12.3; pytest 8.4.2; `engine` inside the clone. (`ruby` is absent from this reviewer container; that is the reviewer's venue, not a Plan defect) |
| 6 | Check 1 step 6 | Its `git ls-files`, `ls -l` and `test -e` reads; `hdctl --version` | The three documents listed; both doc-delta surfaces absent (`git ls-files` prints nothing; `ls -l` exits 2, N-101); the five entrypoints present; the pinned version line |
| 7 | Check 16 steps 1 to 6 as printed | Extracted from v1.1 lines 463 to 468. Two substitutions: the base URL became a local threaded Werkzeug server running `adapter.factory.create_app()` under `APP_ENV=prod`, and the scratch directory was moved (§7 allows another, recorded) | Steps 1 to 4 each print `200 1.1`. All four captures carry `Content-Type: application/json; charset=utf-8`, `Cache-Control: no-store` and `Content-Length: 347`, with no ETag and no Last-Modified. Step 5 prints `True True True True True 347`; both `cmp` runs are silent. Step 6 prints `GET /internal/version False` and `HEAD /internal/version False`. The same requests against Werkzeug's single-threaded HTTP/1.0 server print `200 1`, which falls under check 16's first outcome (`TOOLING_BLOCKED`), not a behaviour failure |
| 8 | Check 20 P1 (V-B form) | `python -m engine.cli --version` in the clone | The pinned line with the candidate `release_id` |
| 9 | Check 20 P2 as printed | Line 529's command with stand-in environments, `APP_ENV=prod` | `P2_ENGINE_ENV=OK` for `ENGINE_ENV` unset, blank, `prod` and ` Prod `; `CONFLICT` for `production` and `live`; the same rule as HDE CLI/API/Vendor Ref §7.1.11b and `engine/bodygraph/resolver.py` (`strip(_ASCII_WHITESPACE).lower()`) |
| 10 | Check 20 P4 as printed, against the code | Line 531's command and `resolve_sink_path` of `engine/bodygraph/vendor_audit.py` (lines 85 to 106; Audit §5) on the same inputs | With `XDG_STATE_HOME` set: the same sink path. With `HDE_VENDOR_OVERRIDE_AUDIT_PATH=rel/sink.jsonl`: P4 prints the cwd-resolved path, `ABSOLUTE=True DIR_WRITABLE=True FILE_WRITABLE=True LINES=0`, and creates `rel/` under the working directory. The code raises `AuditUnavailable` (lines 101 to 102: a configured path is judged absolute before `realpath`). The flag-absent event is then silently not written (`_append_flag_absent_event` returns) (FND-102) |
| 11 | Check 21's test copy against rule A | A clone at `f75733d` on a branch, with one stand-in file under `audit/qa/hde-crd-0002/checks/`, read uncommitted and then committed | Uncommitted: HEAD equals the tested commit, `git status --porcelain` one line. Committed: HEAD differs from the tested commit, status empty. Code outside `docs/ephemeral/`, `docs/pfcanon/` and the QA root identical in both (FND-101) |
| 12 | Canon facts the revision cites | Reads listed in Canon relied on | HDE-Mechanics Guide §14.2 (frozen key order) and §14.3 to §14.4 with its checklist (HEAD with no body and `Content-Length` equal to the GET body length; conditionals never 304; compact UTF-8, one LF, keys not re-sorted). Glow Infrastructure §10.1: `Procfile` `web: /app/.venv/bin/python -m gunicorn` as a checked-in declaration. HDE Build Notes 2.21: PR35-C1, the auto-maintenance race in `tests/tools/test_prepush_check.py`. Glow QA Guide §10.6: "invalid Plan" and the ESC-10 route. Each statement in v1.1 matches its source |

## 3. Redline verification (review v1.0 §6)

| ID | Applied in v1.1 (lines) | Result |
| :- | :- | :- |
| RL-01 | 36 to 41 | Applied. The overclaim is gone; each class of locus and value names its actual basis |
| RL-02 | 111 | Applied. E-L is a full-history clone; a shallow clone is not E-L |
| RL-03 | 114 | Applied. `/app/.venv/bin/python` with its Glow Infrastructure §10.1 basis; P1 establishes it |
| RL-04 | 130 | Applied |
| RL-05 | 205 to 220 | Applied. Rule B is correct. Rule A is correct for checks 2 to 15, check 21's evidence-checkout reads, E-P and E-V. Its first bullet is not satisfiable for check 21's test copy (FND-101) |
| RL-06 | 227 to 243 | Applied: (a) history reads and their outcome; (b) CR-11's condition and the Covers line; (c) the three documents' discovery |
| RL-07 | 423 | Applied |
| RL-08 | 452 | Applied |
| RL-09 | 460 to 483 | Applied: (a) every invariant of Glow QA Guide §3.5.2, with HDE-Mechanics Guide §14's exact forms, each extra request once and unauthenticated; HEAD's body stated as not observable with the offline observation cited (N-102); (b) one protocol version required and recorded, and §3.5.10's tooling test |
| RL-10 | 528 to 552 | Applied: (a), (b) and (d) as required. (c) P4 establishes the directory and writability without writing an event, but its absoluteness read cannot fail (FND-102) |
| RL-11 | 580 to 583 | Applied: attempt 2 only on Kronos's actual QA-110 decision; attempt 1's primary committed before republication, or stated unavailable |
| RL-12 | 637 to 654 | Applied. The record matches review v1.0 §5 field for field and keeps the original proposal |
| RL-13 | 27 | Applied |
| RL-14 | 660 to 661 | Applied |

**Earlier findings after this revision.**
- FND-002, FND-004 to FND-011: corrected.
- FND-001: corrected for every environment except check 21's test copy (FND-101).
- FND-003: corrected for P2 and the classification. FND-102 reopens the same failure class for one configuration (a relative or in-repository sink path).

## 4. Findings

**Blocker test.** As review v1.0 §3 applied it:
- HDE-Governance §9.8.3: "A Blocker is only an issue that prevents the operator from executing the plan in the target environment or prevents reviewers from determining pass/fail for the in-scope behavior with confidence". Its conflict note makes that test govern Live QA plan approval.
- §9.7.7 ("Live QA Plan approval blockers are operational only") agrees.
- Each Caveat states its deviation and the basis for not blocking on it (§9.7.4, "No silent relaxation").

**Provenance.**
- Both findings are **Introduced by current revision** (Plan Templates "Review stability and no-moving-target discipline"): each sits in text that v1.1 added. No finding is raised on unchanged text, and nothing here is Review Drift.
- Each finding's triggering input is real under HDE Build Notes 2.11 rule 4, as 2.18 leaves it.

### FND-101 — Blocker — Rule A cannot be met by check 21's test copy

- **Region:** §7 common rule A, first bullet (v1.1 line 208); coupled to CHECK 21's Rails/Env line (line 560).
- **Defect (O).**
  - Rule A's first bullet applies to "checks 2 to 15, and check 21's test copy". It requires, from the clone root:
    - "`git rev-parse HEAD` equals the tested commit check 1 recorded";
    - "`git rev-parse --is-shallow-repository` prints `false`";
    - "`git status --porcelain` is empty".
  - A failed read makes the check `TOOLING_BLOCKED` (line 212).
  - Check 21 step 2 runs in "a throwaway copy of the evidence checkout with its published files", and its PASS predicate needs "the real root present".
  - The evidence checkout is "a clean clone of `main` at or after the tested source (code identical), on one evidence branch" (§5.4), with no history requirement.
  - So the copy either holds the published family uncommitted (status not empty) or committed on the evidence branch (HEAD is not the tested commit). A copy of a shallow evidence checkout is also shallow.
- **Evidence (O).** §2 row 11 shows both states. Plan §10 maps S22 to check 21 alone.
- **Canon (C).**
  - HDE-Governance §9.8.2 "Dependency posture is required per step": the step-local check establishes dependency readiness before "the main behavior command". Rule A's reads for the copy instead test two properties the copy cannot have, by its own definition: HEAD at the tested commit, and an empty status (I).
  - Plan Templates "Exact status predicates": `TOOLING_BLOCKED` permits no product-behaviour verdict.
  - Plan Templates "Coupled-constraint rule": a review requiring more explicitness must declare the coupled constraints; review v1.0's RL-05 did not.
- **Why it blocks (§9.8.3; §9.7.7: required QA step coverage, explicit PASS or FAIL verdictability).** In every run, check 21 stops at readiness. S22 is left unproven. §11 then forbids `verdict: PASS` for the whole change ("all twenty-one checks are `PASS`"). The cause is a planning defect, not an environment fault.
- **Real input.** The copy is the environment the Plan itself prescribes for every execution.

### FND-102 — Caveat — Check 20's P4 does not apply the delivered code's sink refusals

- **Region:** CHECK 20 P4 (v1.1 line 531).
- **Defect (O).**
  - P4 resolves the path with `os.path.realpath` before it prints `ABSOLUTE=`, so that read is always `True`.
  - The delivered sink rule (Audit §5: "a sink inside the repository refuses (vendor_audit.py:85-106)") refuses two configurations: a configured `HDE_VENDOR_OVERRIDE_AUDIT_PATH` that is not absolute as configured, and a sink inside the repository that holds the running `engine` package.
  - P4 tests the repository rule only under V-A. Its `mkdir` also runs before any test passes.
- **Evidence (O).** §2 row 10: a relative configured path passes P4 and fails in the code.
- **Effect.**
  - V1 still refuses with `PROVIDER_PROD_OVERRIDE_REQUIRED`, but its best-effort event is not written.
  - The Outcomes then apply "V1's event missing although P4 established a writable sink" → `FAIL_BEHAVIOR`. That is a false S14 behaviour failure from configuration: the class FND-003 removed.
  - V2 would answer `PROVIDER_AUDIT_UNAVAILABLE`, which v1.1 rightly classes `TOOLING_BLOCKED`.
- **Canon (C).**
  - HDE CLI/API/Vendor Ref §7.1.11f: every production-like evaluation creates a "locally durable" event before I/O.
  - Glow QA Guide §3.5.7: classify before acting.
  - Plan Templates "Exact status predicates": `FAIL_BEHAVIOR` is not for configuration.
- **Real input.** `HDE_VENDOR_OVERRIDE_AUDIT_PATH` is an operator-settable name the CLI reads (HDE Build Notes 2.11 rule 4(c)), and P2 records its presence.
- **Classification.** Caveat under HDE-Governance §9.8.3. The fault needs an operator to configure a relative or in-repository sink path, and the Plan's environments and examples set neither. With the variable unset, or set to an absolute path outside the repository, P4 and the code agree (§2 row 10). Kronos reviews any `FAIL_BEHAVIOR` at QA-110. The correction is due in this revision.

### Non-gating notes (no correction required)

- **N-101 (check 1 step 6).** `ls -l` of an absent doc-delta surface exits 2 (§2 row 6), and absence is the expected state. Check 1 is not among §5.2's non-zero-exit checks (6, 9, 11 and 20). The executor asserts that status inside the `bash -c` wrapper of §5.2, or reads existence another way, as in-flight normalization (HDE-Governance §9.7.7). The check's `exit_code` is step 7's.
- **N-102 (check 16, HEAD body).** HDE-Mechanics Guide §14's checklist requires HEAD with no body. v1.1 states that `curl -I` cannot observe a body and cites the offline observation. An HTTP/1.1 client reads no body on a HEAD response, so the stated limit is the truthful form of this invariant for a deployed probe.

## 5. CANON_CONFLICT_REGISTER

- **Carried unchanged** as Plan v1.1 §13 records them: CR-1 to CR-8 and CR-10.
- **CR-9:** stays `PROPOSED` (Isis, IA-30 boundary). The Plan's treatment rests on Glow QA Guide §11.1 (review v1.0 §5).
- **CR-11:** `APPROVED_AS_CHANGED`, alternative (a), as decided in review v1.0 §5. Plan v1.1 §13 records it field for field, and check 1 step 6 applies its condition (RL-06(b), RL-12).
- **New conflicts:** none. FND-101 and FND-102 are Plan defects under undisputed canon.

## 6. Redlines for QA-80

One-pass bundle (Plan Templates "Redline bundle construction discipline"):
- Anchors are line ranges of the unchanged Plan v1.1, and no two regions overlap.
- Kronos chooses the wording, commands and evidence design, within loci the Audit, canon, HDE Build Notes or the Plan already establish. No new locus is supplied here.
- QA-80's bookkeeping (front matter, §14's review row, §15, Canon relied on, provenance) follows its prompt.

| ID | Base region (Plan v1.1) | Required outcome | Finding |
| :- | :- | :- | :- |
| RL-15 | Line 208 (§7 rule A, first bullet) | Keep the reads for checks 2 to 15 as written. For check 21's test copy, require only readiness that such a copy can satisfy: (i) its code equals the tested source's under §2's guard, with no difference outside `docs/ephemeral/`, `docs/pfcanon/` and the paths §2's evidence-only commit permission names; (ii) the interpreter, pytest and `engine`-inside-the-copy reads. Do not require HEAD to equal the tested commit, an empty status, or full history for that copy. A failed read stays `TOOLING_BLOCKED`. If the chosen comparison reads the tested commit, state the history the copy needs. §5.4's evidence-checkout definition (line 150) may be amended for that purpose only | FND-101 |
| RL-16 | Line 531 (CHECK 20, P4) | P4 judges the sink by the delivered rule (Audit §5, `vendor_audit.py:85-106`), including its two refusals. First, a configured `HDE_VENDOR_OVERRIDE_AUDIT_PATH` that is not absolute as configured, judged before any path resolution. Second, a sink inside the repository that holds the `engine` package P1 resolved (V-A: the clone; V-B: the deployed package's repository). Either fails P4 → `TOOLING_BLOCKED`, and V1 does not run. P4 creates no directory until both reads pass | FND-102 |
| RL-17 | Line 560 (CHECK 21, Rails/Env line) | Name the test environment for what it is: a throwaway copy of the evidence checkout holding the published family. It uses E-L's interpreter and install, and its code equals the tested source (RL-15). It is not an E-L clone (§3.2: "detached at the tested source, never the evidence checkout") | FND-101 |

## 7. Coverage after correction

Unchanged: S02 to S22 keep their checks (Plan §10), S01 keeps check 15, the Live QA minimum stays checks 17 to 19 plus check 20, and no check is added, removed, parked or rescoped. After RL-15 and RL-17, check 21 can reach its decisive point, so S22 becomes provable.

## 8. Unresolved items and owners

| Item | Owner | State |
| :- | :- | :- |
| QA Plan revision per §6, with an item-by-item application report | Kronos, QA-80 | Next |
| Re-review of the revision | Isis, QA-70 | After QA-80 |
| CR-11 permanent drainage (Plan Templates Step-0B for CRDs; HDE-Mechanics Guide §1.6.3) | Product Owner | Not a condition of the run |
| CR-9 | Isis, IA-30 boundary | `PROPOSED`, unchanged |
| Executor arrangement; check 20 venue and human initiator; evidence-only commit grant | Product Owner, recorded at QA-90 | Not stated |
| N-5 of review v1.0: helper readiness for the exact `publish_crd_check_family` invocation | Kronos, QA-90 | Carried |
| G-1, the close representation of S01 | Close mutation set and Isis; Product Owner if a route beyond the writer is needed | Open |
| N-6 of review v1.0, documentation delta | Product Owner | Candidate |
| QA50-F03 pinning test; FND-012, FND-022, FND-023, FND-028, FND-029, FND-034, FND-037, FND-038; documentation deltas FND-017 to FND-021 and FND-040 | Product Owner | As Plan v1.1 §14 records them |

## 9. TypeSafe reading for the receiving session (QA-80)

Action sent (v8.2): "As its original author, revise one whole-change QA plan of 21 separately verifiable checks (about 720 lines) that an independent reviewer has denied twice, applying exactly three required redlines on three lines: two for one blocking finding (make the step-local readiness rule satisfiable for the one check whose tests run in a copy of the evidence checkout holding the published files, and name that copy's environment truthfully) and one further correction (make the live vendor check's audit-sink precondition apply the delivered code's own refusal rules), and record an item-by-item application report, changing nothing else. It is a Markdown record only: no task list exists yet, no live run against a provider occurs, and an independent re-review, task creation, execution and evidence review follow."

The reading as printed by the script:

- **TypeSafe v8.2: Opus 5.5 at high.** Effort score 2.13 (confidence 0.81); rung probabilities low 0.00, medium 0.08, high 0.72, extra high 0.19, max 0.01, ultracode 0.00. Model probabilities Fable 5.1 0.02, Opus 5.5 0.93, Sonnet 5.5 0.04, Haiku 5.5 0.00 (confidence 0.91). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.002, Fable 5.1 at high 0.014, Fable 5.1 at extra high 0.004, Fable 5.1 at max 0.000, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.000, Opus 5.5 at medium 0.074, Opus 5.5 at high 0.670, Opus 5.5 at extra high 0.177, Opus 5.5 at max 0.009, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.000, Sonnet 5.5 at medium 0.003, Sonnet 5.5 at high 0.029, Sonnet 5.5 at extra high 0.008, Sonnet 5.5 at max 0.000, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Sent 2026-10-24T05:06:09Z. Nathan picks the cell.
- **Detail (as printed):** v8.2 sent 2026-10-24T05:06:09Z; HTTP 200 in 0.55 s; 5505 input and 71 output tokens; jev-1.13.0. Rung by rule: high (nearest to the score, halves up); model by rule: Opus 5.5 (the most probable of the four options, a tie going to the higher-priced model). Flags: none printed.
- **Which request:** the installed TypeSafe scoring skill's request v8.2 and `score_v8.py`, run once with session kind `review` and label "QA-80 HDE-CRD-0002 QA Plan revision after QA-70 re-review DENY", before this review was saved.
- **Records:** the Notion row was not written.
- **Picks:**
  - QA-80: Nathan's pick is not stated.
  - This QA-70 re-review: Nathan's pick is not stated. Its reading is in Plan v1.1 §15 (Opus 5.5 at extra high, score 2.64).

**Surface advice.**
- **Session.** Run QA-80 in the same Kronos author session for HDE-CRD-0002 (https://claude.ai/code/session_01PnD4YNbFZStRQWZ7TCM6jV), as the QA-70 contract routes an initial `DENY`, on `amthorn78/glow-hdengine-v2`. If that session cannot be continued, Nathan creates a top-level Claude Code cloud session for the Kronos role on the same repository, and the revision records that.
- **Reads.**
  - Notion read access for the QA-80 prompt.
  - This review; Plan v1.1 and its application report; review v1.0; Audit v1.0 §5.
  - From `docs/pfcanon/` on `main`:
    - HDE-Governance §9.8.2 and §9.8.3;
    - Plan Templates "Exact status predicates" and "Review stability and no-moving-target discipline";
    - HDE CLI/API/Vendor Ref §7.1.11f;
    - Glow QA Guide §3.5.7.
- **Optional re-checks.**
  - RL-15: a stand-in file in a clone shows both copy states in seconds.
  - RL-16: P4's command can be compared with `vendor_audit.py:85-106` offline, with stand-in environments (a relative configured path, and a path inside the clone).
- **No access needed:** production, the vendor, Railway or the database; no publication through the evidence writer.
- **Writes:** only the revised Plan, its application report and the handoff, under `docs/ephemeral/`, by pull request.
- **Order:** this review's pull request is merged first, so QA-80 reads it from `main`.

## Canon relied on

Read on `main` at `f75733d`; this branch edits no `docs/pfcanon/` file. Review v1.0's "Canon relied on" stays the basis for every topic not listed here. It was read at `55465c2`, and `docs/pfcanon/` is byte-identical between the two commits.

Searches (`grep -n -i -E` over `docs/pfcanon/`):
- "7136040"
- "PR35-C1"
- "app/\.venv|Procfile"
- "ESC-10"
- "14\.[1-4]|Internal version proof surface checklist|engine_tag"
- "7\.1\.11b"
- "7\.1\.11f" with "absolute|relative|sink|XDG|durable"
- "a7_eligible"
- "Causal precedence|Exact status predicates"
- "Review stability and no-moving-target"

HDE Build Notes v13.7.8 is silent on the readiness of check 21's copy and on P4's form, so permanent canon governs both.

| Decision topic | Sources read (title, version, sections) | Applied in |
| :- | :- | :- |
| Review mode, criteria, outputs, routing | QA-70 — Review Whole-Change QA Plan — 100926.1 (page state 2026-10-12T02:29:54.691Z), read in full at this invocation | §1, §6, §9, handoff |
| Blocker test and caveat classification | PF04-Canon-HDE-Governance v2.8.7 §9.8.3 and §9.7.4, §9.7.7 (each read in full at review v1.0; unchanged) | §4; both classifications; N-101 |
| Revision-round review rules | PF27-Canon-Plan-Templates v2.0.5 "Review stability and no-moving-target discipline", read in full here: full-gate first pass, gate freeze, "Coupled-constraint rule", "Unchanged-text blocker rule", "Non-author penalty rule", provenance classes | §1; §4 provenance; FND-101 |
| Readiness per step (FND-101) | PF04 §9.8.2 "Dependency posture is required per step" (read in full at review v1.0); PF27 "Exact status predicates" and "Causal precedence", read in full here | FND-101; RL-15, RL-17; rule B in §1 |
| `/internal/version` (RL-09) | PF14-Canon-HDE-Mechanics-Guide v3.5.8 §14.1 to §14.4 and "Internal version proof surface checklist", read in full here; the invariant checklist of PF19-Canon-Glow-QA-Guide v3.0.6 §3.5.2, read in full here (§3.5.2 read at review v1.0); PF12-Canon-HDE-Schemas-and-Artifacts v2.9.6 (the catalog's `endpoints` key, searched) | §2 rows 7, 12; §3 RL-09; N-102 |
| The live vendor check (RL-10; FND-102) | PF05-Canon-HDE-CLI-API-Vendor-Ref v2.5.3 §7.1.11b (read in full here) and §7.1.11f (read in full at review v1.0; its event and sink lines re-read here); PF19 §3.5.7 (read at review v1.0) | §2 rows 9, 10; FND-102; RL-16 |
| V-B interpreter (RL-03) | PF07-Canon-Glow-Infrastructure v2.3.3 §10.1 "Checked-in declarations", read in full here | §2 row 12; §3 RL-03 |
| Rerun authority (RL-11) | PF19 §10.6, the "Ordinary QA execution/evidence faults" paragraph re-read here; §11.1 (read at review v1.0) | §3 RL-11 |
| History and race records (RL-02, RL-07) | HDE Build Notes v13.7.8 2.4 (the #627 lineage record naming `7136040`) and 2.21 (the PR35-C1 row), read at those records | §2 rows 4, 12; §3 RL-07 |
| Real inputs | HDE Build Notes 2.11 rules 4 to 7, as 2.18 leaves them (read at review v1.0) | Both findings |
| TypeSafe reading | HDE Build Notes 2.1; the installed TypeSafe scoring skill | §9 |

**HDE Build Notes.** `docs/pfcanon/PF10-HDE-Build-Notes-v13.7.8.md` (SHA-256 above) is the version in force. It was read in full in this session at QA-20, and it is byte-unchanged.

**In-flight documents.**
- **Under review, read in full:** Plan v1.1, the application report v1.0 and the QA-80 checkpoint v1.0.
- **Also read:** the QA-80 handoff v1.0 (it binds this invocation); Plan v1.0 (the predecessor, compared by diff); the QA Audit v1.0 (§5 re-read for the sink rule).
- **My own earlier records:** review v1.0 and its handoff, authored in this session.
- **Precedent, not authority:** `docs/ephemeral/HDE-EPIC040-QA70-qa-plan-review-v1.2.md` to `v1.4.md` (structure and numbering of a re-review).
- **Repository rules:** `AGENTS.md` (canon-first rule, closed rails, pytest readiness rule, real-input rule, truncation guardrail).

## Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | GCFPE-USE-HDE-CRD-0002-QA-70-20261024-02 |
| change | CRD HDE-CRD-0002 (Specification v1.1-approved with delta 01) |
| unit | whole change; QA Plan v1.1, checks 1 to 21 (S01 removed; S02 to S22); re-review of RL-01 to RL-14 |
| prompt | QA-70 — Review Whole-Change QA Plan — 100926.1, page state of 2026-10-12T02:29:54.691Z |
| release | GCFPE-20261009.1 / 100926.1 |
| role/stage | Isis, QA-70, `INITIAL_QA_PLAN_REVIEW` (revised pending version) |
| capture time | 2026-10-24T05:06:56Z |
| execution identity | https://claude.ai/code/session_01NxRhYei7RDGmMPYdKEkpok (no worker subagents) |
| earlier uses | GCFPE-USE-HDE-CRD-0002-QA-10-20261023-01 and GCFPE-USE-HDE-CRD-0002-QA-10-20261024-02 (QA-10); GCFPE-USE-HDE-CRD-0002-QA-20-20261024-01 (QA-20); GCFPE-USE-HDE-CRD-0002-QA-50-20261024-01 (QA-50, Kronos); GCFPE-USE-HDE-CRD-0002-QA-70-20261024-01 (QA-70, review v1.0); GCFPE-USE-HDE-CRD-0002-QA-80-20261024-01 (QA-80, Kronos) |
| repository persistence | PENDING / NON_GATING (`docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent on `main`); owner: the authorized repository writer when the procedure is installed |
