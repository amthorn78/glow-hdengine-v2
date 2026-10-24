---
artifact_type: QA_PLAN_REVIEW
artifact_id: HDE-CRD-0002-QA70-QA-PLAN-REVIEW
artifact_version: "1.0"
predecessor: none (the first QA-70 review of HDE-CRD-0002)
REVIEW_MODE: INITIAL_QA_PLAN_REVIEW
AUTHORING_CONTEXT: INITIAL_OR_PREAPPROVAL_AUTHORING
prompt_mode: REVIEW
decision: DENY
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
change_name: "Post-HDE-EPIC040 Repair: Carried Defects, Code Security Review, Pre-Push Check and Close-Pack Writer"
reviewer: Isis (Isis-53), continuing Lead Developer and QA Plan decision owner for HDE-CRD-0002 (execution identity https://claude.ai/code/session_01NxRhYei7RDGmMPYdKEkpok, the session of QA-10 v1.0 and v1.1 and the QA-20 Guide)
session_disposition: continuing Isis context, as the QA-50 handoff routed it
context_conflict: none
prompt: QA-70 — Review Whole-Change QA Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb81209128ea7c82938faf; page state 2026-10-12T02:29:54.691Z; read in full)
prompt_release: GCFPE-20261009.1 / 100926.1
QA_PLAN_ID: docs/ephemeral/HDE-CRD-0002-QA50-qa-plan-v1.0.md (QA_PLAN v1.0, PLAN_PENDING; blob bd49f7c232cd; SHA-256 081a51080a292519c32778b62120ddd41892ba9112d4336d431396f5c6e9272f; 81,719 bytes, 653 lines; read in full)
QA_AUDIT_ID: docs/ephemeral/HDE-CRD-0002-QA50-qa-audit-v1.0.md (QA_AUDIT v1.0, AUDIT_COMPLETE; blob eed40533c7b4; SHA-256 d4f886b7b2272a1fb4c2e8b251d0f6e3d731cbbe18e2b7234cac179948080dad; 36,342 bytes; read in full)
author: Kronos, the QA authority for HDE-CRD-0002 (execution identity https://claude.ai/code/session_01PnD4YNbFZStRQWZ7TCM6jV)
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.7.8.md (519,440 bytes; SHA-256 42459e54e4a14eb89a1cd3be80eae8458a5b1c2c50e1fca1b1ce9882b05e6f9b; addenda 2.1 to 2.26)
repository_head_read: origin/main 55465c2269e15cfdf06c14049e7c6f84707ce02a (#720 merged 2026-10-24T03:16:59Z); code outside docs/ephemeral/ and docs/pfcanon/ identical to 0b15328d and 3a5d846
PF10_ADDENDUM_OUTPUT: NONE (an initial-mode DENY produces no addendum)
canon_conflict_register: CR-1 to CR-10 carried unchanged; CR-11 APPROVED_AS_CHANGED, alternative (a) (§5)
decision_time_utc: 2026-10-24T03:57:24Z
next_prompt: QA-80 — Revise Whole-Change QA Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb818789e9ff3ffa9e06d8), the same Kronos author
handoff: docs/ephemeral/HDE-CRD-0002-QA70-handoff-to-qa80-v1.0.md
---

# HDE-CRD-0002 — QA Plan Review v1.0 (QA-70)

## 1. Decision

**`DENY`.** QA Plan v1.0 is not approvable as written. Three blockers survive faithful syntax normalization (FND-001 to FND-003). Each meets the blocker test of HDE-Governance §9.8.3: as written, the Plan either cannot be executed correctly in a real target environment or does not let reviewers determine pass or fail for in-scope behaviour with confidence. Each also contradicts canon whose governing passages I have read; Canon relied on lists each section and how much of it was read. The Plan returns to the same Kronos author through QA-80 with the one-pass redline bundle of §6. Eight caveats (FND-004 to FND-011) are corrected in the same revision, because the Plan is being revised and they touch the same regions or failure classes. They do not by themselves decide this outcome.

**What is sound and is kept.**
- The candidate definition and the code-identity guard.
- The four environment classes and the per-check rails table: closed default with `APP_ENV=dev`, the Production binding only for checks 16 to 20, never a mixed pair.
- The KISS evidence layout, the step-log header contract, and the evidence-assembly rules QA50-F01 and QA50-F02.
- The publication procedure, the per-check registration map and the final receipt, which meet the QA-70 prompt's "Required QA evidence indexing" in full.
- The evidence-only commit request, framed as a Product Owner grant at task execution (Glow QA Guide §3.4.9; N-9).
- The coverage of S01 (removal) and S02 to S22.
- The Live QA minimum: checks 17 to 19 against the deployed service, and check 20's live vendor call.
- Check 20's human-initiator rule, synthetic inputs, request limit, stop checks and nonclaims.
- The exclusions, the nonclaims, and CR-11's recommended alternative.

**Verified as executable.**
- Every one of the Plan's 20 pytest selectors collects at exactly the Audit's count.
- Every selector of checks 2 to 14 passes at exactly the count its predicate names, with no failure and no skip, in a throwaway clone of `main` under the default rails (§2).
- The command predicates of checks 2, 4, 5, 6, 7, 9, 10, 11, 12, 14 and 15, check 16's consumed-Ops step, and the expected responses of checks 16 to 19 also reproduce.

The defects below concern environment, classification and authority, not the selected tests.

This review produces no PF10 addendum. It is not task selection, execution, a QA result, a merge or a closure decision. Approval of a later revision is not a QA PASS.

## 2. Review method and independent checks

All rows are planning validation by the reviewer, labelled **observed** at `55465c2`. None is QA evidence; nothing from them was committed, pushed or published through the evidence writer. No production, vendor, Railway or database access was used.

**Environment.**
- A throwaway clone of this checkout, detached at `55465c2` with full history, outside the repository.
- A CPython 3.12.3 venv with CI's full install (`python -m pip install 'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e .`; exit 0; `pytest 8.4.2`).
- Every command ran under `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`, with `HD_API_KEY`, `GEO_API_KEY`, `HD_API_BASE_URL`, `HDAPI_BASE_URL`, `DATABASE_URL`, `HDE_VENDOR_OVERRIDE_AUDIT_PATH` and `ENGINE_ENV` unset, and `XDG_STATE_HOME` an empty scratch directory, unless a row says otherwise.
- After every row the clone's `git status --porcelain` was empty, and no file appeared under the scratch state directory.

| # | Check or object | What ran | Result (observed) |
| :- | :- | :- | :- |
| 1 | All 20 selectors of checks 2 to 14 and 21 | `python -m pytest -p no:cacheprovider --collect-only -q` per selector | Exit 0 each. 3; 2; 11; 2; 7; 4; 33; 2, 6, 4; 256; 247; 268; 137; 905, 4; 31, 1, 81, 1. Equal to the Audit §7 item 2 counts; check 21's fourth selector, absent from that list, collects 1, as item 8's run shows |
| 2 | Selectors of checks 2 to 14 | `python -m pytest -q -p no:cacheprovider` per selector, as the Plan names them | Exit 0 each. 3 passed; 2 passed; 11 passed; 2 passed; 7 passed; 4 passed; 33 passed; 2, 6, 4 passed; 256 passed; 247 passed; 268 passed; 137 passed (135.7 s); 905 passed (136.3 s), 4 passed. No failure, no skip. Check 21's selectors were not run here (the Audit §7 item 8 ran them against a stand-in root) |
| 3 | Check 2 step 3 | The Plan's `awk` and `git ls-files` lines on `tests/retired_tests.md` | `66 rows`, no `BAD` line; 0 ledger paths tracked |
| 4 | Check 4 step 1 | `hdctl --help`; `python -m engine.cli --help` (stdout captured to files) | Both exit 0, stderr empty, stdouts byte-identical. With whitespace collapsed, the full S07 sentence occurs once. See N-1 |
| 5 | Check 5 steps 1 to 3 | The Plan's showcompat and aux-preview forms | For each of `Open`, `Warm` and `Glow`, the pair-file form equals the flag form and differs from the no-band output; the no-band output equals the `Cool` flag form |
| 6 | Checks 6, 7, 11 | The Plan's `git ls-files`, `test`, `grep -c` and classifier lines | Check 6: nothing tracked, `app.py` absent, counts 0 and 0 (grep exit 1). Check 7: one match (`adapter/http_reader.py`, line 389). Check 11: every "contains" count 1 or more, every "no" count 0, classifier `documentation_only` |
| 7 | Checks 8, 10, 12, 14, 15 (static parts) | Counts and reads the predicates name | Check 8 step 4: 27 Mirror rows. Check 10: `generate_a7_transport_proofs.py --check` exit 0, catalogs equal, 18 records. Check 12 step 1: 49 per-file rows, 9 fixed rows (S19-F01 to F09), 7 routed rows (S19-R01 to R07). Check 14 step 3: line 3 as predicated; schema present. Check 15: the five greps count 1 |
| 8 | Check 15 step 3 | `git log --oneline 7136040^..HEAD -- pyproject.toml` | Full history: prints nothing. In this session's own checkout of `main`, a shallow clone (`git rev-parse --is-shallow-repository`: true; boundary `142e56f`), it prints `142e56f docs(ephemeral): HDE-CRD-0002 WU-PR-02 PR work-unit lineage review v2.0 (PR-40, ACCEPT) (#638)`: the boundary commit, shown as adding `pyproject.toml` (FND-002) |
| 9 | Check 9 step 2 | Probes (a) to (e) with `hdctl` | (a), (b): exit 1, `PROVIDER_REFUSED` envelope, stderr empty. (c), (d), (e): exit 64, stdout empty, one stderr line that does not contain the value. No sink file |
| 10 | Check 16 step 3 | `sha256sum -c SHA256SUMS.attempt1` in `audit/ops/hde-crd-0002/wu-ops-01/`; reads | 5 of 5 OK; `classification PASS`; `identity_reads MATCH (reads=1)` with the candidate `release_id` |
| 11 | Checks 16 to 19 expected responses | Flask test client on `adapter.factory.create_app()` with `APP_ENV=prod` at registration | Every response of Audit §6 reproduces, including check 19's second body (20,008 bytes): 422 `ERR_READER_INVALID_INPUT`, `no-store`, no ETag. `/internal/version`: GET and HEAD 200; `If-None-Match` and `If-Modified-Since` GETs 200; `application/json; charset=utf-8`; `no-store`; no ETag; no Last-Modified; body ends with one LF; six keys. The catalog's two `/internal/version` records carry `a7_eligible: false` (FND-005) |
| 12 | Check 20 environment classification | `classify_vendor_environment(view, process={})` called directly (no CLI, rails closed, no I/O) | `APP_ENV=prod` alone, or with `ENGINE_ENV=prod` or `" PROD "`: production-like. With `ENGINE_ENV=production` or `live`: `PROVIDER_CONFIG_INVALID`, `outbound_attempted: false` (FND-003) |
| 13 | Check 20 predicates against the code | Read `engine/bodygraph/resolver.py` and `engine/bodygraph/vendor_audit.py` | The 16 audit fields; the flag-absent `refused` event (best-effort); the pre-I/O `allowed` event and the post-I/O state event under one `correlation_id` with route fields; V2's dry-run stdout fields (`adapter.status` `mapped`, `payload_family` `ChartResult`, `cache.payload_posture` `adapter_mapped_no_raw_vendor_payload`, `ingest.rows_written` 0, the redacted header posture). Each matches the Plan's predicate |
| 14 | Locus provenance | Every path-like string in the Plan's code spans (124) checked against the Audit, HDE Build Notes and PF canon | 16 repo-resident loci appear verbatim in none of them; check 1's discovery covers 13 (FND-011) |
| 15 | Check 4 wrapping | `textwrap.wrap` of the S07 help text at widths 40 to 240 | Whitespace collapse recovers the sentence at the default 80 columns. It fails at 40 to 49, 51, 59, 60, 83 to 86 and 140 to 145, where the wrap breaks `--dump-reader` at its hyphen (N-1) |
| 16 | Prohibited characters and blocks (HDE-Governance §9.8.3; Glow QA Guide §3.4.10) | Searched the Plan for fenced code blocks, U+2026 and triple full stops | None |

## 3. Findings

**Blocker test.** HDE-Governance §9.8.3, "Review gate (blocking)": "A Blocker is only an issue that prevents the operator from executing the plan in the target environment or prevents reviewers from determining pass/fail for the in-scope behavior with confidence". Its "Conflict note (explicit override)" makes that test govern Live QA plan approval. HDE-Governance §9.7.7 agrees ("Live QA Plan approval blockers are operational only"), and each Blocker below names the §9.7.7 class it affects. Plan Templates "Live QA Plan approval materiality discipline" and "Materiality-based blocker discipline" also agree. Every other finding is a Caveat. Each Caveat states its deviation and the basis for not blocking on it (HDE-Governance §9.7.4, "No silent relaxation"). No Caveat is accepted: each is a required correction in this revision.

**Provenance and basis.**
- Every finding is **Introduced by current revision**: v1.0 is the first revision reviewed, and this is the full-gate first pass of Plan Templates "Review stability and no-moving-target discipline".
- Basis labels follow Plan Templates "Proof classification": canon requirement (C), observed repository reality (O), inference (I).
- Each finding's triggering input is real under HDE Build Notes 2.11 rule 4, as 2.18 leaves it.

### FND-001 — Blocker — No step-local readiness check in checks 2 to 15 and 21

- **Region:** §7 opening paragraph (line 196); §8 (lines 527 to 530); §3.2 hazards (line 107).
- **Defect (O).** The only environment preflight is check 1: candidate guard, interpreter and tools, `engine` resolving inside the clone. No later executable check reruns a readiness check before its main commands. §2 and §8 let QA-90 split the checks into separate tasks, executors and venues. The hazard line (107) assigns the guard against OBS-W5-5 ("an editable install mapped to another checkout runs the wrong code") to check 1 alone.
- **Canon (C).**
  - HDE-Governance §9.8.2, "Dependency posture is required per step": "A shared bootstrap step does not remove per-step responsibility. Each later step MUST either include its own dependency preflight or explicitly depend on the bootstrap and rerun a short step-local readiness check before the main behavior command". Also: "Behavior verdicts MUST NOT be issued before dependency readiness is established".
  - Plan Templates CHECK template, "Dependency posture (required for executable checks)", "Per-step enforcement".
  - Glow QA Guide §3.4.8, "Entrypoint existence preflight".
- **Why it blocks (§9.8.3; §9.7.7: proof target identity, evidence trust).** A check run in a later task, session or venv can exercise another checkout's code or another interpreter. The §5.2 context block records the clone's commit and the interpreter, but not where `engine` resolves. Reviewers therefore cannot determine with confidence that a recorded PASS or FAIL concerns the candidate.
- **Precedent (not authority).** The approved HDE-EPIC040 QA Plan v1.2 carried this line in every check (`docs/ephemeral/HDE-EPIC040-QA50-qa-plan-v1.2.md`, line 441).

### FND-002 — Blocker — History-dependent predicates assume a full clone that E-L does not require

- **Region:** §3.2 E-L (line 102); CHECK 1 step 1 (line 205); CHECK 15 step 3 and predicate (lines 421, 424).
- **Defect (O).**
  - Check 15 step 3 expects `git log --oneline 7136040^..HEAD -- pyproject.toml` to print nothing, and check 1 step 1 diffs against `0b15328d`.
  - E-L is defined as "A throwaway clone of `amthorn78/glow-hdengine-v2` detached at the tested source, never the evidence checkout". It does not require complete history, and check 1 does not record it.
  - Check 15 states no FAIL or BLOCKED outcome.
- **Evidence (O).** §2 row 8: in this session's shallow checkout of `main`, which is the default state of a cloud-session checkout, step 3 prints the shallow-boundary commit `142e56f` as adding `pyproject.toml`. With full history it prints nothing. A clone made from a shallow checkout is itself shallow.
- **Canon (C).**
  - HDE-Governance §9.8.2: the dependency set and preflight per step.
  - Plan Templates CHECK template, "Dependency posture".
  - Glow QA Guide §3.4.1: each check identifies its PASS, FAIL and BLOCKED outcomes.
  - Plan Templates "Exact status predicates": an unavailable required environment fact is `TOOLING_BLOCKED`, never `FAIL_BEHAVIOR`.
- **Why it blocks (§9.8.3; §9.7.7: explicit PASS or FAIL verdictability, evidence trust).** In a real target environment (HDE Build Notes 2.11 rule 4(b), the operator's shell), check 15 cannot be executed correctly. The S01-removal evidence, which the close relies on (G-1), would show a false record that this change altered packaging. Neither the shallowness nor an outcome rule would let a reviewer see that it is an environment fault.

### FND-003 — Blocker — Check 20 admits a configuration canon refuses, then calls the refusal a behaviour failure

- **Region:** CHECK 20 P2 (line 483), P4 (line 485), Outcomes (lines 501 to 506).
- **Defect (O, C).**
  - P2 accepts `ENGINE_ENV` "`UNSET` or a production-like value", while P3 fixes `APP_ENV=prod`.
  - HDE CLI/API/Vendor Ref §7.1.11b: "If both names are nonblank, their normalized values must be equal; a conflict is `PROVIDER_CONFIG_INVALID`."
  - So `ENGINE_ENV=production` or `live` passes P2, and V1 then returns `PROVIDER_CONFIG_INVALID` (exit 1, no sink event) instead of `PROVIDER_PROD_OVERRIDE_REQUIRED`.
  - The Outcomes map "V1 deviates → `FAIL_BEHAVIOR`; V2 is not run".
  - The same rule turns a correct V1 refusal into `FAIL_BEHAVIOR` when its best-effort event could not be written. P4 does not establish that the sink can be written.
- **Evidence (O).**
  - §2 row 12 reproduces the classification.
  - The flag-absent event is best-effort ("the refusal stands whether or not its event persists", `_append_flag_absent_event`).
  - HDE Build Notes 2.9 records the same rule in WU-PR-04's black-box probes ("`APP_ENV=dev` with `ENGINE_ENV=prod` exit 1, `PROVIDER_CONFIG_INVALID`").
- **Canon (C).**
  - HDE CLI/API/Vendor Ref §7.1.11b and §7.1.11c.
  - Glow QA Guide §3.5.7: "An open-rails failure is not automatically a product behavior failure. QA MUST classify the failure before acting." Also: "Do not collapse those categories into a single `FAIL_BEHAVIOR` result without proof." Conflicting configuration fails closed "as configuration ambiguity, not product behavior failure".
  - Plan Templates "Exact status predicates": `FAIL_BEHAVIOR` is not used for missing tools, credentials, open-rails authorization or configuration.
- **Real input.** `ENGINE_ENV` is an operator-settable name the CLI reads (HDE Build Notes 2.11 rule 4(c)), and P2 itself permits a production-like value.
- **Why it blocks (§9.8.3; §9.7.7: explicit PASS or FAIL verdictability, required QA step coverage).** On the change's only mandatory live vendor check, a configuration fault would be recorded as an S14 behaviour failure and V2 would not run. Reviewers would hold a false verdict for S14, and the live vendor call would be lost (Glow QA Guide §3.5.5; Change Process Guide §1.1.5A).

### FND-004 — Caveat — The executor reruns a check before Kronos decides

- **Region:** §9 bullets 1 to 3 (lines 534 to 536). CHECK 13's Outcomes (line 396) and check 20's rerun rule (line 535) inherit it.
- **Defect (O).**
  - §9 grants "one bounded ordinary-lane rerun per check" for an execution or evidence fault, and says "QA-100 records both attempts".
  - It sends a check to Kronos at QA-110 only after "a second failure of the same check".
  - The first rerun is therefore decided and run by the executor before any QA-110 decision. For check 20 it can be a second outbound vendor request.
- **Canon (C).**
  - Glow QA Guide §10.6: "Ordinary QA execution/evidence faults retain their existing limit: a first eligible fault requires Kronos's actual QA-110 decision before QA-90 attempt 2".
  - Glow QA Guide §11.1: Kronos "makes actual bounded-rerun/escalation decisions".
  - QA-50, Execute phase 2 item 4, and the QA-70 prompt: "QA-110 retains evidence review, existing bounded retry/missing-evidence handling and escalation".
- **Classification.** Caveat under HDE-Governance §9.8.3. The rule moves the attempt-2 decision from Kronos to the executor, but it neither prevents execution nor stops a reviewer from judging either attempt's evidence. Check 20's limit of two invocations still bounds the vendor requests. The correction is due in this revision.

### FND-005 — Caveat — Check 16 produces `/internal/version` evidence without the canon's invariant checklist

- **Region:** CHECK 16 Actions and PASS predicate (lines 432 to 437).
- **Defect (O).** Check 16 records `/internal/version` GET and HEAD captures in its governed primary. It verifies status 200, `Cache-Control: no-store`, no ETag, "application/json" and the six keys. It omits:
  - conditional requests (`If-None-Match`, `If-Modified-Since`) answering 200, never 304;
  - `Last-Modified` absent;
  - the exact `Content-Type: application/json; charset=utf-8`;
  - HEAD parity;
  - the LF-terminated canonical body;
  - the catalog entry for `/internal/version` with `a7_eligible: false`.
- **Canon (C).** Glow QA Guide §3.5.2: "Internal version proof surface uses an explicit invariant checklist (required). Any remediation guide, QA step, or probe tool that produces /internal/version governed evidence MUST explicitly enumerate and verify the canon-critical invariants below. It is not acceptable to imply these checks by referencing PF sections only." HDE Build Notes is silent on this.
- **Evidence (O).** §2 row 11: every listed invariant holds in the application. The fix adds read-only probes that are expected to pass. The live service may differ only in router behaviour (IR-3).
- **Classification.** Caveat under HDE-Governance §9.8.3. Check 16's in-scope purpose (readiness and the deployed `release_id`) can still be judged. But its governed `/internal/version` evidence would not meet the canon checklist. The correction is due in this revision.

### FND-006 — Caveat — Seven checks state no FAIL or BLOCKED outcome

- **Region:** CHECK 6, 7, 8, 10, 12, 14 and 19 blocks. CHECK 15 is FND-002; CHECK 19 says only "A 500 or `text/html` fails".
- **Canon (C).** Glow QA Guide §3.4.1 (PASS, FAIL and BLOCKED outcomes per check); HDE-Governance §9.8.2 (explicit PASS and FAIL predicates); Plan Templates CHECK template "Expected result".
- **Risk and safe default.** Each of these checks states an explicit, checkable PASS predicate, so FAIL is its negation and a verdict stays determinable. Plan Templates' exact status predicates and causal precedence supply the failure class. The risk: rerun eligibility turns on `FAIL_TOOLING` versus `FAIL_BEHAVIOR`, which the executor would then classify from those general predicates alone, with no check-specific signature.

### FND-007 — Caveat — Check 13 names the wrong step for the FND-024 race

- **Region:** CHECK 13 Outcomes (line 396).
- **Defect (O).** The race (change audit triage v1.1, FND-024; PR35-C1) is in `tests/tools/test_prepush_check.py`, which step 3 runs (and step 1's `replay` where it runs that file). Step 2 runs only the `lanes` report and cannot carry that signature. As written, a real race falls under "any other failure → `FAIL_BEHAVIOR`".
- **Canon (C).** Plan Templates "Bounded step-level rerun posture" (the exact trigger condition).
- **Classification.** Caveat. The intended target is unambiguous from FND-024's definition, and Plan Templates Step-0B ("Doc-delta surfaces") treats a "wording-only" mismatch inside one check whose "intended target remains unambiguous" as a CAVEAT, not a BLOCKER.

### FND-008 — Caveat — "Not HTTP/1.x" would block valid HTTP/2 answers

- **Region:** CHECK 16 Outcomes (line 438).
- **Defect (O, I).** `curl` negotiates HTTP/2 when the server offers it; `curl` 8.5.0 in this container is built with `nghttp2`. WU-OPS-01's identity read did not record the protocol.
- **Canon (C).** Glow QA Guide §3.5.10 names two tooling failures: a target that cannot be reached, and a response with no status line or headers whose handler was never exercised. A valid HTTP/2 response is neither.
- **Safe default.** No false PASS results. But if the operator's `curl` negotiates HTTP/2, the literal rule blocks checks 17 to 19 (and check 20 under V-B) for a protocol reason unrelated to the product.

### FND-009 — Caveat — V-B's interpreter is not the one canon records

- **Region:** §3.2 E-V (line 105); CHECK 20 P1 and V1 (lines 482, 489).
- **Defect (O, C).** V-B runs `python -m engine.cli` in the service shell. Glow Infrastructure records the production process's interpreter as `/app/.venv/bin/python` (the `Procfile` record), so an unqualified `python` in that shell is not established. Glow Infrastructure §2.7 does establish the service shell as a valid console: "Any shell (local terminal, CI shell, or other remote environment) that can reach the production Railway base URL and/or connect to `ample-illumination/production/postgres` with the appropriate environment configuration is a valid console for the canonical HD Engine CLI."
- **Safe default.** P1 fails with zero vendor I/O and the check is `TOOLING_BLOCKED`. The cost is a lost live window.
- **Classification.** Caveat. HDE-Governance §9.7.7 ("Live QA Plan review burden") limits an objection that only prefers another interpreter to an execution note. This finding rests on a separate fact: the Plan assumes, without an allowed source, that `python` in that shell imports the deployed `engine`, and that decides whether check 20 can run at all.

### FND-010 — Caveat — The first attempt's primary is not preserved as §9 claims

- **Region:** §9 bullet 1 (line 534).
- **Defect (O).** §9 says the first attempt's published primary "remains in git history". Nothing requires a commit before attempt 2 republishes the same `check_id` in place; the family is current-state.
- **Canon (C).**
  - Plan Templates "Bounded step-level rerun posture": preserve the earlier failed or blocked state, and state an overwritten initial artifact as unavailable rather than reconstruct it.
  - HDE-Mechanics Guide §1.6.3: canonical current state and historical attempts are distinct.
- **Safe default.** The rerun's notes carry the failure signature.

### FND-011 — Caveat — Locus provenance is overstated, and three document loci have none

- **Region:** §0 opening paragraph (line 32); CHECK 1 step 6 (line 210).
- **Defect (O).** Line 32 says the Audit's §5 to §7 "back every path, test node and expected value named here". They do not:
  - 16 repo-resident loci appear verbatim in no allowed provenance source: not in the Audit, not in HDE Build Notes, not in PF canon (§2 row 14).
  - Several expected values are not in the Audit: 66 ledger rows, 27 Mirror rows, the 49, 9 and 7 S19 counts, 18 catalog records, the ADR's third line.
- **What is covered.** Check 1's Step-0B discovery (collect-only of every selector; `test -e` of five entrypoints) covers 13 of the 16 loci. Three document loci remain uncovered: `tests/retired_tests.md`, `docs/acceptance/reader_a7_crib.md`, `docs/adr/hde/close_pack_writer_adr.md`.
- **Canon (C).**
  - HDE-Governance §9.8.2, "QA planning reality posture" and "Discovery-first posture": verbatim provenance from HDE Build Notes, PF canon or the initial QA Audit, or a discovery step. Otherwise the plan "MUST be returned for revision".
  - Plan Templates "Path provenance and locus provenance lock".
- **Classification.** Caveat, by an explicit downgrade (HDE-Governance §9.7.4, "Downgrades" and "No silent relaxation").
  - Several rules treat this defect as blocking. HDE-Governance §9.7.4 lists "a required repo locus asserted without allowed proof or discovery-first posture" among Stage A plan-approval blockers; §9.7.7 repeats it among its "Valid blocker classes"; §9.7.9 makes "any unvalidated asserted path" a "mechanical planning-review blocker"; and §9.8.2's "Blocking posture" returns such a plan for revision.
  - For a Live QA Plan, two rules narrow them. §9.7.7 admits a blocker only where the issue affects "repo-locus truth where the plan requires an existing locus". §9.8.3 rejects "unproven repo file paths (not present in repo; see §9.7.9)", and its conflict note makes §9.8.3 govern Live QA plan approval wherever other language would treat a non-execution issue as a Blocker.
  - Basis: every locus and value here exists and matches at `55465c2` (§2). Repo-locus truth holds, no invented locus or false value results, and neither execution nor a verdict depends on the missing provenance.
  - Claim limit: the Plan's provenance for these loci stays unproven until RL-01 and RL-06(c) apply. The Plan is returned on FND-001 to FND-003, and this correction is due in the same revision. N-6 records a related canon tension over which sources count as provenance.

## 4. Per-check summary

| # | check_id | Verified here (observed) | Affected by |
| :- | :- | :- | :- |
| 1 | `qa-01-preflight` | `hdctl --version` prints the pinned line; all selectors and entrypoints resolve | FND-002, FND-011, CR-11 condition |
| 2 | `qa-02-ci-coverage` | 3 and 2 passed; ledger predicates hold | FND-001, FND-011 |
| 3 | `qa-03-attestation-debian` | 11 passed. `--output`, `--verify`, `--require-clean`, `build.log`'s compat line and the attestation fields exist in `tools/evidence/build_release_attestation.py`. The Debian condition is the Audit's (§7 item 7). Build not run here | FND-001 |
| 4 | `qa-04-showcompat-help` | §2 row 4; 2 passed | FND-001; N-1 |
| 5 | `qa-05-aux-preview-band` | §2 row 5; 7 passed | FND-001 |
| 6 | `qa-06-dev-harness-retired` | §2 row 6; 4 passed | FND-001, FND-006, FND-011 |
| 7 | `qa-07-dev-reader-gate` | 33 passed; one grep match | FND-001, FND-006 |
| 8 | `qa-08-release-evidence-tooling` | 2, 6, 4 passed; 27 rows | FND-001, FND-006 |
| 9 | `qa-09-override-matrix` | 256 passed; §2 row 9 | FND-001 |
| 10 | `qa-10-endpoint-catalog` | 247 passed; §2 row 7 | FND-001, FND-006 |
| 11 | `qa-11-template-and-documents` | §2 row 6 | FND-001 |
| 12 | `qa-12-security-review` | 268 passed; 49, 9, 7 | FND-001, FND-006; N-4 |
| 13 | `qa-13-prepush-check` | 137 passed; the tool's output is the Audit's (§7 item 9) | FND-001, FND-004, FND-007 |
| 14 | `qa-14-close-pack-writer` | 905 and 4 passed; ADR line and schema | FND-001, FND-006, FND-011 |
| 15 | `qa-15-s01-removal` | §2 rows 7, 8 | FND-001, FND-002 |
| 16 | `qa-16-deployed-identity` | §2 rows 10, 11 | FND-005, FND-008 |
| 17 | `qa-17-deployed-not-found` | §2 row 11 | none |
| 18 | `qa-18-deployed-dev-surfaces` | §2 row 11 | none |
| 19 | `qa-19-deployed-reader-input` | §2 row 11 | FND-006 |
| 20 | `qa-20-live-vendor-override` | §2 rows 12, 13 | FND-003, FND-004, FND-009 |
| 21 | `qa-21-evidence-admission` | selectors collect; the Audit's stand-in run (§7 item 8) | FND-001 |

## 5. CANON_CONFLICT_REGISTER decisions

**Carried unchanged** (full fields in their records, as Plan v1.0 §13 cites them):
- CR-1 to CR-3: `APPROVED_AS_CHANGED` (Thoth).
- CR-4: `APPROVED`; CR-5: `APPROVED_AS_CHANGED` (Product Owner).
- CR-6: `APPROVED`, alternative (a) (Implementation Agent through RS-20; HDE Build Notes 2.6).
- CR-7 and CR-8: `APPROVED`, alternative (a) each (Product Owner; 2.7).
- CR-10: `APPROVED`, alternative (a) (Isis, ESC-40, 2026-10-23T20:15:00Z; 2.24).

**CR-9: not decided here.** It stays `PROPOSED` (Isis, IA-30 boundary), unchanged. The Plan's treatment rests independently on Glow QA Guide §11.1: check 16's primary and its path proof point to the WU-OPS-01 files without re-homing them. §11.1 reads: "When QA consumes it, the QA check's governed `audit/qa/<change-id>/checks/<check_id>/primary.log` and required sibling path proof point to that evidence rather than re-homing it." No QA-70 decision on CR-9 is needed for this Plan.

**CR-11 — decided.**

| Field | Value |
| :- | :- |
| ID; classification | CR-11; CANON_RECONCILIATION |
| Sources and clauses (verified) | **Plan Templates v2.0.5:** "Mandatory Step-0 artifacts", Step-0B, "Doc-delta surfaces (required; two-surface pair)", "MUST be generated by commands", and the "no deltas" determination rule. **Plan Templates §2A**, "Existing-template reuse and substitution": templates are reused "when substitution preserves their contract", and "PF27 MUST NOT invent a CRD path". **HDE-Mechanics Guide v3.5.8 §1.6.3:** CRD publication "neither repairs unrelated historical evidence implicitly nor permits arbitrary additional-file or index-metadata injection"; CRD `additional_files` "do not automatically become indexed evidence"; auxiliary verification output "does not become a primary or indexed family merely by being present". **Glow QA Guide v3.0.6 §3.4.3** (KISS outputs; `00_meta/` only for an exact owning-canon path) and §3.5.7. **Implementation Plan v1.1 §7 WU-PR-07** "Terminal-state reachability" (a) and T1: the close mutation set authors `audit/docdeltas/hde-crd-0002_doc_deltas.md` as a tracked causal input, "each stating when empty" |
| Statement | As proposed: for a CRD, Step-0B's `00_meta` capture cannot be indexed by the governed writer, and its draft surface is a close-stage causal input another owner authors |
| Affected requirements | None of S01 to S22 directly; the QA run's Step-0B obligation and the close's doc-delta ledger |
| Original proposal | Kronos, Plan v1.0 §13, 2026-10-24T02:36:06Z. Alternatives: (a) Step-0B in check 1's indexed primary, reported in QA-120, ledger left to T1; (b) an unindexed `00_meta/doc_deltas.md` (rejected); (c) a writer extension (code outside QA). Recommended (a) |
| Decision | **`APPROVED_AS_CHANGED`, alternative (a).** The change: check 1's Step-0B capture applies Step-0B's own rules in full: stable IDs, BLOCKERS and CAVEATS separated, generated by commands, plan-versus-execution drift recorded, "no deltas" only when empty. Before emitting "no deltas", it records whether either doc-delta surface exists: the draft ledger `audit/docdeltas/hde-crd-0002_doc_deltas.md`, and the `00_meta/doc_deltas.md` capture surface CR-11 names. It preserves, and never overwrites, any proof-bearing content it finds |
| Rationale | (a) keeps Step-0B's substance in governed, indexed evidence through the only canonical CRD writer, without inventing a path or a writer change. (b) would leave present-but-unindexed evidence that HDE-Mechanics Guide §1.6.3 excludes. (c) changes code outside QA. The ledger is already a close-stage input under the approved Implementation Plan. The change makes explicit a Step-0B rule that the Plan's check 1 omits |
| Interim treatment; unresolved risk | (a) as changed is the treatment for this run; none for this run |
| Drainage target and owner | Plan Templates Step-0B (CRD applicability) and HDE-Mechanics Guide §1.6.3; the Product Owner. Not a condition of this run |
| Reviewer and session; reviewed artifact | Isis (Isis-53), https://claude.ai/code/session_01NxRhYei7RDGmMPYdKEkpok, QA-70; `docs/ephemeral/HDE-CRD-0002-QA50-qa-plan-v1.0.md` (v1.0) |
| Decision time; status history | 2026-10-24T03:57:24Z; `PROPOSED` (Kronos, Plan v1.0) → `APPROVED_AS_CHANGED` (Isis, this review) |
| HDE Build Notes recording | Not produced (QA-70 in initial mode produces no addendum). The Product Owner may record it |

No new canon conflict needs a decision. N-6 records one documentation-delta candidate that this review resolves by applying the stricter rule.

## 6. Redlines for QA-80

One-pass bundle (Plan Templates "Redline bundle construction discipline"):
- Every anchor is a line range of the unchanged Plan v1.0.
- No two regions overlap, and no redline lies inside another's region.
- Each redline states the required outcome and its source. Kronos chooses the wording, commands and evidence design, within loci that canon, HDE Build Notes, the Audit or the Plan already establish. No new locus is supplied here.
- QA-80's own bookkeeping (front matter fields, the §15 TypeSafe reading, Canon relied on, prompt-use provenance) follows its prompt. RL-13 and RL-14 only fix the CR-11 and review-state facts there.

| ID | Base region (Plan v1.0) | Required outcome | Finding |
| :- | :- | :- | :- |
| RL-01 | Line 32 (§0 opening paragraph) | State provenance truthfully. Do not claim the Audit backs every path, test node and expected value. Name the actual basis: Audit §5 to §7, canon, check 1's discovery, or a per-check discovery record | FND-011 |
| RL-02 | Line 102 (§3.2, E-L row) | E-L clones hold the full history of `main` that checks 1 and 15 read. A shallow clone is not E-L | FND-002 |
| RL-03 | Line 105 (§3.2, E-V row) | V-B uses the interpreter Glow Infrastructure records for the service process (`/app/.venv/bin/python`), or the Plan states how P1 establishes the shell's interpreter before any step | FND-009 |
| RL-04 | Line 121 (§5.1, second bullet) | Replace "(CR-11, interim)" with CR-11's decided status | CR-11 |
| RL-05 | Line 196 (§7 opening paragraph) | Add two common rules for every check block that does not state its own. (a) **Step-local readiness:** before its main commands, each executable check reruns a short readiness check of the environment class it uses. At minimum: the clone is at check 1's recorded tested source; the class's interpreter and tools resolve; `engine` resolves inside that clone (check 1 step 3's own reads). The result is recorded under `=== CONTEXT ===`; if it fails, the check is `TOOLING_BLOCKED`, never `FAIL_BEHAVIOR`. (b) **Default outcome map:** a block without an Outcomes line uses a stated default that follows Plan Templates' exact status predicates and causal precedence (Glow QA Guide §3.4.1) | FND-001, FND-006 |
| RL-06 | Lines 198 to 216 (CHECK 1 block, consolidated) | (a) Record that the E-L clone is not shallow; `TOOLING_BLOCKED` if it is (RL-02). (b) Apply CR-11's condition (§5), and update the "Covers" line to the decided status. (c) Bring `tests/retired_tests.md`, `docs/acceptance/reader_a7_crib.md` and `docs/adr/hde/close_pack_writer_adr.md` under Step-0B's discovery (existence recorded verbatim before use; a BLOCKER if absent), or cite an allowed provenance source for them | FND-002, FND-011, CR-11 |
| RL-07 | Line 396 (CHECK 13, Outcomes) | Name the steps that can carry the FND-024 race signature: step 3, which runs `tests/tools/test_prepush_check.py`, and step 1's `replay` where it runs that file. Not step 2. Rerun eligibility follows RL-11 | FND-007 |
| RL-08 | Line 424 (CHECK 15, PASS predicate) | Add outcomes. Unavailable history (a shallow clone, or `7136040` unresolvable) → `TOOLING_BLOCKED`. `FAIL_BEHAVIOR` only when a full-history clone shows a commit touching `pyproject.toml` in that range, or a count other than 1 | FND-002 |
| RL-09 | Lines 432 to 438 (CHECK 16, Actions to Outcomes, consolidated) | (a) Enumerate and verify every canon-critical `/internal/version` invariant of Glow QA Guide §3.5.2: GET 200; HEAD 200 with parity; conditional requests (`If-None-Match`, `If-Modified-Since`) answering 200, never 304; `Cache-Control: no-store`; `Content-Type: application/json; charset=utf-8`; no ETag; no Last-Modified; exactly the six keys; the LF-terminated canonical body; the `docs/ENDPOINTS_CATALOG.json` entry with `a7_eligible: false`. Each extra request is sent once, with no auth header. (b) Replace "not HTTP/1.x" with Glow QA Guide §3.5.10's test: unreachable, or no valid response with a status line and headers. Record the negotiated protocol version, or require one version for every deployed probe and record it | FND-005, FND-008 |
| RL-10 | Lines 482 to 506 (CHECK 20, P1 to Outcomes, consolidated) | (a) P1 and V1 under V-B use RL-03's interpreter. (b) P2: `ENGINE_ENV` `UNSET`, or nonblank and equal to `APP_ENV` after HDE CLI/API/Vendor Ref §7.1.11b normalization. Any other value fails P2 → `TOOLING_BLOCKED`, no V1. (c) P4 establishes, without writing an event, that the sink's directory exists or can be created and is writable by the actor. (d) Classify every V1 and V2 deviation under Glow QA Guide §3.5.7 before acting. `PROVIDER_CONFIG_INVALID`, or a missing V1 event with an unwritable sink, is configuration or tooling (`TOOLING_BLOCKED`). `FAIL_BEHAVIOR` only when P1 to P5 hold and the output or events contradict HDE CLI/API/Vendor Ref §7.1.11c to §7.1.11f | FND-003, FND-009 |
| RL-11 | Lines 534 to 536 (§9, bullets 1 to 3, consolidated) | (a) The one bounded ordinary-lane rerun runs only after Kronos's QA-110 decision on the first eligible fault, as a QA-90 attempt 2 (Glow QA Guide §10.6, §11.1). The executor does not rerun on its own, and for check 20 that decision precedes any second V2. (b) Attempt 1's published primary is committed on the evidence branch before attempt 2 republishes the same `check_id`. Otherwise attempt 2's notes state that attempt 1's primary is unavailable and carry its failure signature (Plan Templates "Bounded step-level rerun posture") | FND-004, FND-010 |
| RL-12 | Lines 590 to 603 (§13, CR-11) | Record CR-11's decision as §5 of this review states it (status, reviewer and session, reviewed artifact and version, decision time, rationale, the change, history), keeping the original proposal | CR-11 |
| RL-13 | Lines 2 to 27 (front matter) | `canon_conflict_register` shows CR-11's decided status; the revision's own fields follow QA-80 | CR-11 |
| RL-14 | Lines 609 to 610 (§14, the first two rows) | The review row reflects this DENY and the revision's next review; the CR-11 row shows its decided status | CR-11 |

## 7. Non-gating notes (no correction required)

- **N-1 (check 4).** argparse wraps the S07 help text by terminal width, and at some widths breaks `--dump-reader` at its hyphen (§2 row 15). At the default 80 columns of a non-terminal capture, the collapse holds; `COLUMNS` is not exported in this venue. If an executor's shell exports it, recording its value in `=== CONTEXT ===` explains a mismatch.
- **N-2.** The class label "1/2" for checks 17 to 19 is none of Glow QA Guide §3.5.6's three classes. The Product Owner subset (check 20 only) is unambiguous.
- **N-3.** §11 does not name Plan Templates' "QA RCA & Doc Delta summary" with its Coverage versus QA Plan accounting. Canon binds QA-120 to it regardless.
- **N-4 (check 12 step 1).** A naive pattern miscounts the S19 rows: §10 repeats the S19-F IDs, and two S19-R IDs carry suffixes. The executor records the counting command actually used.
- **N-5 (carried to QA-90).** The exact `publish_crd_check_family` invocation is authored at QA-90 (§5.4). It is execution-critical, so Glow QA Guide §3.4.8 "Execution-critical helper readiness" applies to it before its first governed use.
- **N-6 (documentation-delta candidate; Product Owner).** Glow QA Guide §3.4.1 counts "bounded direct inspection of the actual repository" as locus provenance. HDE-Governance §9.8.2 and Plan Templates limit it to HDE Build Notes, PF canon and the initial QA Audit, or a discovery step. This review applies the stricter rule, which satisfies both.
- **N-7.** §1's "hosted CI ran it on the tested code" compresses two runs: the full matrix on `1a4c8ab`, and the change-selected `evidence` and `qa` lanes on `3a5d846`, which is the tested code (HDE Build Notes 2.25). Between them, 19 files changed outside `docs/ephemeral/` and `docs/pfcanon/` (observed): WU-DOC-01's documents (among them `AGENTS.md`, `README.md` and `CHANGELOG.md`), WU-OPS-01's six evidence files, and WU-REM-01's two evidence-lane test files and `tools/qa/qa_harness.py`. Stated precisely, the claim is that pair of runs.
- **N-8.** When a check is `TOOLING_BLOCKED`, HDE-Governance §9.8.2 "Blocked-step minimum fields" applies to its primary: the blocking precondition, why it cannot be satisfied, whether it blocks closeout, and the required follow-up. The §5.2 body layout can carry them under `=== NOTES ===`. Canon binds the step record regardless.
- **N-9.** No check proposes VCS workflow as a QA step (HDE-Governance §9.8.3). The evidence-only commit permission (§2) is a request the Product Owner grants or withholds at task execution; without it, the Product Owner commits (Glow QA Guide §3.4.9). §5.4's "on one evidence branch" sits inside that grant.

## 8. Coverage after correction

Unchanged in substance:
- S02 to S22 each keep their checks (Plan §10).
- S01 keeps check 15 as removal evidence, with its outcomes made explicit.
- The Live QA minimum stays checks 17 to 19 plus check 20.
- No check is added, removed, parked or rescoped.

## 9. Unresolved items and owners

| Item | Owner | State |
| :- | :- | :- |
| QA Plan revision per §6, with an item-by-item application report | Kronos, QA-80 | Next |
| Re-review of the revision | Isis, QA-70 | After QA-80 |
| CR-11 permanent drainage (Plan Templates Step-0B for CRDs; HDE-Mechanics Guide §1.6.3) | Product Owner | Not a condition of the run |
| CR-9 | Isis, IA-30 boundary | `PROPOSED`, unchanged |
| Executor arrangement; check 20 venue and human initiator; evidence-only commit grant | Product Owner, recorded at QA-90 | Not stated |
| N-5 helper readiness | Kronos, QA-90 | Carried |
| G-1, the close representation of S01 | Close mutation set and Isis; Product Owner if a route beyond the writer is needed | Open |
| N-6 documentation delta | Product Owner | Candidate |
| QA50-F03 pinning test; FND-012, FND-022, FND-023, FND-028, FND-029, FND-034, FND-037, FND-038; documentation deltas FND-017 to FND-021 and FND-040 | Product Owner | As Plan v1.0 §14 records them |

## 10. TypeSafe reading for the receiving session (QA-80)

Action sent (v8.2): "As its original author, revise one whole-change QA plan of 21 separately verifiable checks (about 650 lines) that an independent reviewer has denied once, applying exactly five required blocking redlines and seven further required corrections across most of its checks (a step-local readiness check in every executable check, full-history clones for history-dependent checks, the canon's full identity-endpoint invariant list on one deployed probe, the live vendor check's environment precondition and failure classification, rerun authority routed to the evidence reviewer, explicit failure outcomes, locus provenance and one decided canon-conflict condition), and record an item-by-item application report, changing nothing else. It is a Markdown record only: no task list exists yet, no live run against a provider occurs, and an independent re-review, task creation, execution and evidence review follow."

**Count note.** The action text counts five blocking and seven further corrections. Before issue, this review applied HDE-Governance §9.8.3's blocker test and reclassified two of the five as caveats: three blocking and nine further. The receiving work is unchanged: the same twelve corrections, in the same fourteen redlines. The QA-70 prompt runs the script once, so the reading was not retaken. Nathan may have it retaken on a corrected text.

The reading as printed by the script:

- **TypeSafe v8.2: Opus 5.5 at extra high.** Effort score 2.54 (confidence 0.67); rung probabilities low 0.00, medium 0.02, high 0.44, extra high 0.52, max 0.02, ultracode 0.00. Model probabilities Fable 5.1 0.04, Opus 5.5 0.93, Sonnet 5.5 0.03, Haiku 5.5 0.00 (confidence 0.91). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.001, Fable 5.1 at high 0.018, Fable 5.1 at extra high 0.021, Fable 5.1 at max 0.001, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.000, Opus 5.5 at medium 0.019, Opus 5.5 at high 0.409, Opus 5.5 at extra high 0.484, Opus 5.5 at max 0.019, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.000, Sonnet 5.5 at medium 0.001, Sonnet 5.5 at high 0.013, Sonnet 5.5 at extra high 0.016, Sonnet 5.5 at max 0.001, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Flags: boundary between high and extra high. Sent 2026-10-24T03:51:01Z. Nathan picks the cell.
- **Detail (as printed):** v8.2 sent 2026-10-24T03:51:01Z; HTTP 200 in 0.56 s; 5512 input and 71 output tokens; jev-1.13.0. Rung by rule: extra high (nearest to the score, halves up); model by rule: Opus 5.5 (the most probable of the four options, a tie going to the higher-priced model). Flags: boundary between high and extra high.
- **Which request:** the installed TypeSafe scoring skill's request v8.2 and `score_v8.py`, run once with session kind `review` and label "QA-80 HDE-CRD-0002 QA Plan revision after QA-70 DENY", before this review was first saved.
- **Records:** the Notion row was not written.
- **Picks:** Nathan's pick for QA-80 is not stated. Nathan's pick for this QA-70 session is not stated; its reading is in Plan v1.0 §15 (Fable 5.1 at max, score 3.58).

**Surface advice.**
- **Session.** Run QA-80 in the same Kronos author session for HDE-CRD-0002 (https://claude.ai/code/session_01PnD4YNbFZStRQWZ7TCM6jV), as the QA-70 contract routes an initial `DENY`, on `amthorn78/glow-hdengine-v2`. If that session cannot be continued, Nathan creates a top-level Claude Code cloud session for the Kronos role on the same repository, and the revision records that.
- **Reads.**
  - Notion read access for the QA-80 prompt.
  - This review; Plan v1.0 and Audit v1.0; the Live QA Guide v1.0.
  - `docs/pfcanon/` on `main`:
    - Glow QA Guide §3.4.1, §3.5.2, §3.5.7, §3.5.10, §10.6 and §11.1;
    - Plan Templates §A.1 and "Review guardrails";
    - HDE-Governance §9.8.2 and §9.8.3;
    - HDE CLI/API/Vendor Ref §7.1.11b to §7.1.11f;
    - Glow Infrastructure §2.7 and its `Procfile` record;
    - HDE Build Notes v13.7.8.
- **Optional re-checks.**
  - Use a throwaway clone with full history. Fetch the full history of `main` first if the session's checkout is shallow.
  - Install CI's dependencies on Python 3.12 under closed rails.
  - Collecting all selectors takes seconds. Running the selectors of checks 2 to 14 took about 6 minutes here; check 14's 905 tests and check 13's 137 tests took about 2.3 minutes each.
  - The Flask test client confirms check 16's added invariants offline.
- **No access needed:** production, the vendor, Railway or the database; no publication through the evidence writer.
- **Writes:** only the revised Plan, its redline application report and the handoff, under `docs/ephemeral/`, by pull request.
- **Order:** this review's pull request is merged first, so QA-80 reads it from `main`.

## Canon relied on

Read on `main` at `55465c2`; this branch edits no `docs/pfcanon/` file.

Searches (`git grep -n -i -E` over `docs/pfcanon/`):
- "HTTP/1|HTTP/2|--http"
- "VCS mutation|evidence branch|commit and push|evidence pull request"
- "Step-0B|doc_deltas|docdeltas"
- "If-None-Match|Last-Modified|invariant checklist"
- "QA-110 decision|attempt 2|bounded rerun|ordinary-lane"
- "allowed provenance|repo-locus|locus lock|initial QA Audit|bounded direct inspection"
- "ENGINE_ENV"
- "ssh|service shell|console"
- "HDE_VENDOR_OVERRIDE_AUDIT_PATH"
- "QA planning reality posture|Discovery-first|IP Approved|CA vetted"
- "wording-level|wording level" and "CAVEATS?" (Plan Templates)

HDE Build Notes is silent on four topics: Step-0B for CRDs, the `/internal/version` invariant checklist, the rerun decision, and locus provenance. Permanent canon governs those.

| Decision topic | Sources read (title, version, sections) | Applied in |
| :- | :- | :- |
| Review mode, decision criteria, outputs, routing | QA-70 — Review Whole-Change QA Plan — 100926.1 (page state 2026-10-12T02:29:54.691Z), read in full | §1, §6, §10, handoff |
| Blocker definition for Live QA plan approval | PF04-Canon-HDE-Governance v2.8.7 §9.8.3 "Review gate (blocking)", read in full, including its rejection list, "Formatting is not an approval gate", "Conflict note (explicit override)" and the prompt-family separation rule; PF04 §9.7.4 "Blocking status and downgrades" and §9.7.7 "Plan approval gate", each read in full | §3 blocker test and every classification in §3; §2 row 16; N-9 |
| Materiality, syntax latitude, redline bundle, review stability, prompt mode | PF27-Canon-Plan-Templates v2.0.5 "Review guardrails", lines 1002 to 1359, read in full: "Source-bound review authority and exact-fix limits", "Hard blockers for plan approval/execution", "Live QA Plan approval materiality discipline", "Plan command, syntax, and example-literalness approval rule", "Explicit non-blockers", "Materiality-based blocker discipline for planning and review artifacts" and "QA planning QoS guardrails". Also PF19-Canon-Glow-QA-Guide v3.0.6 §3.4.10, read in full | Every classification in §3; §6 |
| Template structure, CHECK fields, dependency posture, path provenance, Step-0, close-out | PF27 §A.1 Live QA Plan, lines 301 to 1001, read in full; PF04 §9.8.1 and §9.8.2 (lines 3242 to 3484, read in full) and §9.8.4 (read) | FND-001, FND-002, FND-006, FND-007, FND-011; N-3, N-8 |
| Per-check outcomes and status classes | PF19 §3.4.1 and §3.4.2 (read); PF27 "Exact status predicates" and "Causal precedence"; PF04 §9.8.2 | FND-002, FND-003, FND-006, FND-007 |
| Rails, venue and consoles | PF19 §3.3, §3.4.8, §3.5.5 and §3.5.6 (each read in full); PF07-Canon-Glow-Infrastructure v2.3.3 §2.7 (read in full) and its `Procfile` record (read); PF27 "Rails posture (explicit)" | §1 kept items; FND-009 |
| The mandatory live vendor call and the S14 contract | PF27 "Open-Rails Live QA Requirement for production-affecting epics"; PF19 §3.5.5 to §3.5.7; PF06-Canon-Change-Process-Guide v2.5.4 §1.1.5A (read); PF05-Canon-HDE-CLI-API-Vendor-Ref v2.5.3 §7.1.11 to §7.1.11f (read in full). For this change, HDE Build Notes 2.9 overtakes §7.1.11's preamble on the held implementation gap: it records that the delivered flag was accepted under §7.1.11a to §7.1.11f | FND-003; check 20 kept items |
| HTTP readiness | PF19 §3.5.10, read in full | FND-008 |
| `/internal/version` | PF19 §3.5.2 (read); PF27 Step-0C | FND-005 |
| Rerun and escalation authority | PF19 §10.6 (read from its opening through "Evidence-package caveats and failure history"); PF19 §11.1 (read in full); QA-50 — Create Whole-Change QA Audit and Plan — 100926.1, Execute phase 2 item 4 (page state 2026-10-12T02:30:48.299Z, read in full); PF27 "Bounded step-level rerun posture" | FND-004, FND-010 |
| Evidence layout, writer, indexing, consumed Ops evidence | PF19 §3.4.3 to §3.4.6 (read in full) and §11.1; PF14-Canon-HDE-Mechanics-Guide v3.5.8 §1.6.3 (lines 894 to 944, read); QA-70 "Required QA evidence indexing" | §1 kept items; CR-9 note |
| Step-0B for a CRD (CR-11) | PF27 Step-0B and §2A (lines 1866 to 1946, read in full); PF14 §1.6.3; PF19 §3.4.3; Implementation Plan v1.1 §7 WU-PR-07 "Terminal-state reachability" (read) | §5 |
| VCS boundary and source attribution | PF19 §3.4.9 and §10.8 (each read in full); PF27 "VCS mutation and exact-source identity boundary (hard)" and the hard blocker on preplanned-commit equality; PF04 §9.8.2 "Branch/commit workflow is out of scope" and §9.8.3 | §1 kept items (the evidence-only commit request; the code-identity guard); N-9 |
| Locus provenance | PF04 §9.8.2 "QA planning reality posture" and "Discovery-first posture", including its "Blocking posture"; PF04 §9.7.9 "Plan locus validation" (read); PF27 "Path provenance and locus provenance lock"; PF19 §3.4.1, §3.4.2, §3.4.14 and §11.3 (read in full) | FND-011, N-6 |
| Real inputs | HDE Build Notes 2.11 rules 4 to 7 (read), as 2.18 leaves them (read) | Every finding |
| Report and RCA | PF19 §3.1.2 (read); PF27 "Close-out deliverables" | N-3 |
| TypeSafe reading | HDE Build Notes 2.1; the installed TypeSafe scoring skill | §10 |

**HDE Build Notes.** `docs/pfcanon/PF10-HDE-Build-Notes-v13.7.8.md` was read in full in this session at QA-20 and is byte-unchanged since (SHA-256 above).
- Re-read for this review: 2.9 (S14 delivery and its black-box probes; LR4-O2), 2.11 rules 4 to 7, 2.18 rules, and 2.25 (measures (1) and (2)).
- Addenda that bear on the Plan: 2.1, 2.9, 2.10, 2.11, 2.15 to 2.20, and 2.23 to 2.26.

**In-flight documents** (paths and versions; read as stated):

- **Under review, read in full:** `docs/ephemeral/HDE-CRD-0002-QA50-qa-plan-v1.0.md` and `docs/ephemeral/HDE-CRD-0002-QA50-qa-audit-v1.0.md`.
- **My own earlier records** (authored in this session):
  - `docs/ephemeral/HDE-CRD-0002-QA20-live-qa-guide-v1.0.md`, with §12 re-read here;
  - `docs/ephemeral/HDE-CRD-0002-QA10-qa-readiness-v1.1.md`, `docs/ephemeral/HDE-CRD-0002-QA10-reality-audit-v1.1.md` and `docs/ephemeral/HDE-CRD-0002-QA10-change-audit-triage-v1.1.md`, with the triage's FND-024 row re-read here.
- **Read in full at QA-10:**
  - `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` (the S18 row re-read here) with `docs/ephemeral/HDE-CRD-0002-specification-delta-v1.0.md`;
  - `docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md` (WU-PR-07 re-read here) with `docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-v1.1.md`;
  - `docs/ephemeral/HDE-CRD-0002-WU-OPS-01-ops-task-receipt-v1.0.md`;
  - `docs/ephemeral/HDE-CRD-0002-WU-REM-01-pr-work-unit-lineage-review-v1.0.md` and `docs/ephemeral/HDE-CRD-0002-WU-DOC-01-documentation-completion-v1.1.md`, both at the QA-10 reassessment.
- **Re-read here in part:** `docs/ephemeral/HDE-CRD-0002-S19-code-security-review-v1.0.md` (§4 and §6) and the WU-OPS-01 evidence files.
- **Precedent, not authority:**
  - `docs/ephemeral/HDE-EPIC040-QA70-qa-plan-review-v1.1.md` (structure);
  - `docs/ephemeral/HDE-EPIC040-QA70-planning-failure-rca-v1.1.md` (§2 to §7, read);
  - `docs/ephemeral/HDE-EPIC040-QA50-qa-plan-v1.2.md` (line 441).
- **Repository rules:** `AGENTS.md`: canon-first rule, closed rails, redaction rule, pytest readiness rule, evidence attribution, truncation guardrail.

## Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | GCFPE-USE-HDE-CRD-0002-QA-70-20261024-01 |
| change | CRD HDE-CRD-0002 (Specification v1.1-approved with delta 01) |
| unit | whole change; QA Plan v1.0, checks 1 to 21 (S01 removed; S02 to S22) |
| prompt | QA-70 — Review Whole-Change QA Plan — 100926.1, page state of 2026-10-12T02:29:54.691Z |
| release | GCFPE-20261009.1 / 100926.1 |
| role/stage | Isis, QA-70, `INITIAL_QA_PLAN_REVIEW` |
| capture time | 2026-10-24T03:57:24Z |
| execution identity | https://claude.ai/code/session_01NxRhYei7RDGmMPYdKEkpok (no worker subagents) |
| earlier uses | GCFPE-USE-HDE-CRD-0002-QA-10-20261023-01 and GCFPE-USE-HDE-CRD-0002-QA-10-20261024-02 (QA-10); GCFPE-USE-HDE-CRD-0002-QA-20-20261024-01 (QA-20); GCFPE-USE-HDE-CRD-0002-QA-50-20261024-01 (QA-50, Kronos) |
| repository persistence | PENDING / NON_GATING (`docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent on `main`); owner: the authorized repository writer when the procedure is installed |
