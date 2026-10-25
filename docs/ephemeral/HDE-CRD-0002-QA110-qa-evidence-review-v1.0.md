---
artifact_type: QA_EVIDENCE_REVIEW
artifact_id: HDE-CRD-0002-QA110-QA-EVIDENCE-REVIEW
artifact_version: "1.0"
predecessor: none (the first QA-110 review for HDE-CRD-0002)
state: ESCALATION_REQUIRED
change_class: CRD
change_id: HDE-CRD-0002
change_name: "Post-HDE-EPIC040 Repair: Carried Defects, Code Security Review, Pre-Push Check and Close-Pack Writer"
author: Kronos, the continuing QA authority for HDE-CRD-0002 (execution identity https://claude.ai/code/session_01PnD4YNbFZStRQWZ7TCM6jV, the session that wrote QA Plan v1.0 to v1.2 and the QA-90 collection v1.0)
session_disposition: continuing Kronos context, as the QA-100 handoff to QA-110 v1.0 routes it
invocation_binding: CRD / HDE-CRD-0002 / QA-110 / QA-90 collection v1.0 tasks T01 to T15 against the QA-100 execution results v1.0
context_conflict: NONE
execution_posture: MANUAL_PROMPT_EXECUTION
prompt: QA-110 — Review QA Evidence and Route the Next Action — 100926.1 (https://app.notion.com/p/3f44590a05eb81ee9a09e00af51f33cb; page state 2026-10-12T02:29:41.377Z; read in full at this invocation)
ecosystem_release: GCFPE-20261009.1 (100926.1)
approved_base: docs/ephemeral/HDE-CRD-0002-QA50-qa-plan-v1.2.md (QA_PLAN v1.2; blob 66f6016cc75bd1ab4ff9730ea89e5e25c7ec629c; SHA-256 8068ea350a9239c83e692a552bac8d5561a914d8694835faf4d38e0ab69f64e9; immutable)
approving_review: docs/ephemeral/HDE-CRD-0002-QA70-qa-plan-review-v1.2.md (APPROVE by Isis (Isis-53); SHA-256 b33d38a25defc48348189b9846a4e8d4f476b72d566882c67414c9af323037ef)
qa_audit: docs/ephemeral/HDE-CRD-0002-QA50-qa-audit-v1.0.md (AUDIT_COMPLETE; SHA-256 d4f886b7b2272a1fb4c2e8b251d0f6e3d731cbbe18e2b7234cac179948080dad)
task_collection: docs/ephemeral/HDE-CRD-0002-QA90-qa-task-collection-v1.0.md (TASK_READY; SHA-256 fd1eb20d2cfd3a1da9b776980eaa9fcd705273f8eba537d0472ec02e96a328ca)
execution_results: docs/ephemeral/HDE-CRD-0002-QA100-qa-execution-results-v1.0.md (RESULTS_RETURNED_TO_QA110; SHA-256 7f87b1c211ebf96a419fbdb6494c9a736d3f9f9a66dbc71fa4f624004e3034b8)
evidence_of_record: audit/qa/hde-crd-0002/ on main at faa2246799901ef8e708bcf7ee8d0e57cd55f3ec (squash merge of amthorn78/glow-hdengine-v2#726; tree f56b5ca20fc2 equals the pull request head b0830c15's tree; the evidence bytes equal evidence commit 3d8080472473ed20b306da6a83228e16c11f82cb)
tested_source: 2e03a2686af87ab0607c6cfb9afb4ad79bcdb171 (code outside docs/ephemeral/ and docs/pfcanon/ identical to 0b15328d, check 1)
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.7.8.md (SHA-256 42459e54e4a14eb89a1cd3be80eae8458a5b1c2c50e1fca1b1ce9882b05e6f9b; the single PF10 file on main)
observed_revision: aae20472a51c7827f07f1853e82d85f0b157bd0b (origin/main at review; amthorn78/glow-hdengine-v2#726 and amthorn78/glow-hdengine-v2#727 merged)
routing: ESC-10 — Create QA Escalation Report — 100926.1, in this continuing Kronos session, for check 13 (S20)
PF10_ADDENDUM_OUTPUT: NOT_PRODUCED_BY_QA-110 (QA-110 is not an addendum producer)
created_at: 2026-10-25T01:26:00Z
---

# HDE-CRD-0002 — QA Evidence Review v1.0 (QA-110): tasks T01 to T15 of QA Plan v1.2

## 1. Result

| Field | Value |
| --- | --- |
| Members reviewed | T01 to T15 (Plan v1.2 checks 1 to 15), matched one to one with the fifteen `QA_EXECUTION_RESULT` records of the QA-100 results v1.0 §3 and §4 |
| Decision per member | 14 × `ACCEPT` (T01 to T12, T14, T15); 1 × `ESCALATION_REQUIRED` (T13) (§4) |
| Step-log status upheld | 14 × `PASS`; `qa-13-prepush-check` `FAIL_BEHAVIOR`. Every decisive predicate was re-read against the captured command output, not against the primaries' own PREDICATES lines (§4) |
| Finding | QA110-F01: the delivered pre-push tool (S20) exits 4, `PREPUSH_CHECK_READ_ONLY_VIOLATION`, with all five reports `status=PASS`. It is a product behavior defect on a delivered surface, verified independently (§6) |
| Moon Loops | Check 3: accepted as a PASS-only Moon Loop deviation (ruling R-1, §5). Check 13: accepted as an execution deviation that removed a venue cause. The failure it left is QA110-F01 (§6.3) |
| Attempt lineage | In-session reruns ran on checks 3 and 13 without the QA-110 decision Plan §9 requires. They are recorded as a process deviation, and each check's one ordinary rerun is consumed (ruling R-2, §7) |
| Evidence and indexing | Complete for the fifteen checks. Five read-only validators and `validate_crd_check_family` pass on `main` at `aae2047`. Every primary matches its path proof, its Index key and its Mirror row. Hosted CI is green on amthorn78/glow-hdengine-v2#726's head and on the `main` push (§3) |
| Run state | Incomplete. Plan checks 16 to 21 are unissued and have no Product Owner selection. No authored task is waiting (§10) |
| Next stage | ESC-10 — Create QA Escalation Report — 100926.1, in this continuing Kronos session, for QA110-F01 (§10) |
| Not established | Whole-change QA PASS, acceptance, closure, the QA-120 Report, the final receipt of Plan §5.6, or any claim for checks 16 to 21 (§15) |

## 2. Inputs and matches

| Item | Identity | Match |
| :- | :- | :- |
| Approved base | Plan v1.2, SHA-256 `8068ea350a9239c83e692a552bac8d5561a914d8694835faf4d38e0ab69f64e9`, blob `66f6016cc75b` | Equal to the pins in the collection and in the QA-100 results. Check 1 read the blob in the E-L clone |
| Approving review | QA-70 review v1.2, SHA-256 `b33d38a25defc48348189b9846a4e8d4f476b72d566882c67414c9af323037ef` | Equal to the QA-100 pin |
| Audit | QA Audit v1.0, SHA-256 `d4f886b7b2272a1fb4c2e8b251d0f6e3d731cbbe18e2b7234cac179948080dad` | Equal to the QA-100 pin |
| Task collection | v1.0, SHA-256 `fd1eb20d2cfd3a1da9b776980eaa9fcd705273f8eba537d0472ec02e96a328ca` | Equal to the QA-90 checkpoint pin and the QA-100 pin |
| Execution results | QA-100 results v1.0, 32,825 bytes, SHA-256 `7f87b1c211ebf96a419fbdb6494c9a736d3f9f9a66dbc71fa4f624004e3034b8` | On `main` through amthorn78/glow-hdengine-v2#726 |
| Selection | Product Owner "Steps: Checks 1 through 15" | Each T-ID maps to exactly one Plan check and one `check_id` (collection §3); no duplicate, no missing member |
| Attempts | Every task is attempt 1 | Checks 3 and 13 carry in-session reruns inside attempt 1 (§7) |
| Tested source | `2e03a268`, tree `af5293473238` | Each primary's readiness block records it |
| Environment | E-L on the Product Owner's workstation (Ubuntu 26.04.1, git 2.53.0, CPython 3.12.15 uv build). E-D through the check 3 Moon Loop | Results §2 |
| PF10 | v13.7.8, SHA-256 `42459e54e4a14eb89a1cd3be80eae8458a5b1c2c50e1fca1b1ce9882b05e6f9b` | Unchanged since the Plan approval |

## 3. Evidence integrity and indexing (verified here)

All of the following was run read-only by Kronos on 2026-10-25, in a fresh full-history clone of `main` at `aae2047`, under `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0` with vendor and database names unset. That checkout's status was empty before and after.

| Check | Result |
| :- | :- |
| `python tools/evidence/update_evidence_index.py --check` | exit 0 |
| `python tools/evidence/orientation_demo.py --check` | exit 0 |
| `python tools/evidence/validate_evidence_paths.py` | exit 0 |
| `ci/checks/check_mirror_schema.sh`, run directly (it is a Python script) | exit 0. A first invocation through `bash` was my invocation error, a syntax error before any check ran. It is not a repository result |
| `python tools/evidence/check_lf_endings.py` | exit 0 |
| `validate_crd_check_family(HarnessConfig(crd_id="HDE-CRD-0002"))` | 15 checks: fourteen `PASS`, `qa-13-prepush-check` `FAIL_BEHAVIOR` |
| Primary bytes | All fifteen sizes and SHA-256 values equal QA-100 results §3, and each equals its `.path_proof.txt` |
| Header fields | Each `check_name`, `pf_refs` and `evidence_artifacts` equals the collection's Spec line for its task. Each `captured_env` holds only the six admitted names; both token arrays are empty; schema `pf27.step_log_header.v2` |
| Index and Mirror | Each primary has its Human Index key and one Machine Mirror row with a matching SHA-256. The manifest (2,339 bytes, SHA-256 `ae34abc336da8b2323f756ffbe2202fe2a8f78615bfa781075e17460e3e064e9`) has its Mirror row |
| amthorn78/glow-hdengine-v2#726 changed paths | 46 files: 32 under `audit/qa/hde-crd-0002/`, the ten updater-owned graph files, and the four QA-100 records under `docs/ephemeral/`. That is exactly Plan §2's evidence-only commit scope plus the executor's own records |
| `main` versus the evidence commit | `git diff 3d808047 faa2246 -- audit artifacts docs/evidence` is empty |
| Hosted CI, amthorn78/glow-hdengine-v2#726 head `b0830c15` | Run 40149195209, job 121036980535: `success`. Lanes `evidence` and `release` selected and `success`, the others `skipped`; `CI_APPLICABILITY_AND_EXACT_HEAD_OK`. This is the selection Plan §5.6 expected. The named risks FND-024 and IR-7 did not appear |
| Hosted CI, `main` push `faa2246` | Run 40149378863, job 121037477924: `success`. The evidence lane, the release attestation and the applicability step are `success` |
| Code review on amthorn78/glow-hdengine-v2#726 | The Codex summary on `b0830c15` reads completed, `has_any_findings: false` |

Missing required indexing: none. Index coverage is complete for this selection. Plan §5.6's final receipt follows check 21 and is not due.

## 4. Member decisions

Every decisive value below was read from the command records (`--- command:` with exit code and stdout) of the primary on `main`. Normalizations are those of collection §4.10 and are syntax- or location-level only (Glow QA Guide §3.4.7).

| Task | `check_id` | Decision | Status | Decisive evidence re-read |
| :- | :- | :- | :- | :- |
| T01 | `qa-01-preflight` | `ACCEPT` | `PASS` | HEAD `2e03a268`, shallow `false`, `7136040` resolves, guard diff empty. Manifest SHA-256 `77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e`, `1.3.0 2026-08-24T18:04:49Z 45`, exact `hdctl --version`. Python 3.12.15, pytest 8.4.2, ruby, bash, curl and git present. Nine names `UNSET`. Six validators exit 0. Step-0B: all twenty selectors at their Audit counts; five entrypoints; three documents tracked; PF10 v13.7.8; Plan blob `66f6016c`; both doc-delta surfaces absent (`ls -l` exit 2 asserted); no BLOCKER or CAVEAT. Final status empty |
| T02 | `qa-02-ci-coverage` | `ACCEPT` | `PASS` | "3 passed"; "2 passed, 136 deselected"; "66 rows", no `BAD`; tracked count `0`. Step 4 cited, not decisive |
| T03 | `qa-03-attestation-debian` | `ACCEPT` (R-1) | `PASS` | Rerun 2: `78.1.1 /usr/lib/python3/dist-packages/setuptools/__init__.py None`. Build and verify exit 0. `attestation.json` 28,163 bytes with `release_id` `77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e`, `PASS`, `PR06R_B_FINAL_PASS`; compat line count `1`; "11 passed"; build clone status empty |
| T04 | `qa-04-showcompat-help` | `ACCEPT` | `PASS` | Both help commands exit 0 with 0-byte stderr; `cmp` exit 0 (797 and 797 bytes); sentence count `1`; `check_cli_help.sh` exit 0; "2 passed" |
| T05 | `qa-05-aux-preview-band` | `ACCEPT` | `PASS` | `harmony` `Cool`. Eight `aux-preview` exits 0 with empty stderr. The file and flag forms are equal for Open, Warm and Glow; `file-none` equals `flag-Cool`; each band output differs from `file-none` (asserting script exit 0); "7 passed" |
| T06 | `qa-06-dev-harness-retired` | `ACCEPT` | `PASS` | `git ls-files dev/reader_harness` empty; `test ! -e` exit 0; `VERIFY.sh:0`, `docs/acceptance/reader_a7_crib.md:0` (grep exit 1 asserted); "4 passed" |
| T07 | `qa-07-dev-reader-gate` | `ACCEPT` | `PASS` | "33 passed"; one match, `389:    return os.environ.get("APP_ENV") == "dev"` |
| T08 | `qa-08-release-evidence-tooling` | `ACCEPT` | `PASS` | "2 passed", "6 passed", "4 passed"; supporting count 27 |
| T09 | `qa-09-override-matrix` | `ACCEPT` | `PASS` | "256 passed". (a) and (b) exit 1 with `"status":"error"` and `PROVIDER_REFUSED`, stderr 0 bytes. (c), (d) and (e) exit 64, stdout empty, one stderr line without the flag value. `XDG_STATE_HOME` and status empty |
| T10 | `qa-10-endpoint-catalog` | `ACCEPT` | `PASS` | "247 passed"; generator `--check` exit 0 ("a7 transport proofs check ok"); `cmp` silent; `18` |
| T11 | `qa-11-template-and-documents` | `ACCEPT` | `PASS` | Fourteen "contains" counts of 1 or more; the "no" counts are `adapter/factory.py:0` and `adapter/http_reader.py:0` (exit 1 asserted); `documentation_only`; `emit_public(...) -> bytes`; the three factory names in `## Routing and mounts` |
| T12 | `qa-12-security-review` | `ACCEPT` | `PASS` | `per-file rows 49`; `fixed rows 9 without disposition 0`; `routed rows 7 without disposition 0`; "268 passed, 648 deselected" |
| T13 | `qa-13-prepush-check` | `ESCALATION_REQUIRED` | `FAIL_BEHAVIOR` | Decisive rerun: step 1 exit 4, stderr `PREPUSH_CHECK_READ_ONLY_VIOLATION: the repository's tree, ignored files, directories, HEAD or git metadata changed`. All five reports `status=PASS`, replay steps 01 to 16 `SUCCESS`, and the `PREPUSH_CHECK_RESULT` line is absent. Step 2 as predicated, exit 0; step 3 "137 passed"; step 4 empty. Plan check 13 Outcomes: "Exit 4 (repository changed) → `FAIL_BEHAVIOR`" (§6) |
| T14 | `qa-14-close-pack-writer` | `ACCEPT` | `PASS` | "905 passed"; "4 passed, 62 deselected"; ADR line 3 begins as predicated and ends with the review reference; `test -f` exit 0 |
| T15 | `qa-15-s01-removal` | `ACCEPT` | `PASS` | Five counts of `1`, plus the manifest version `1.3.0`; `git log --oneline 7136040^..HEAD -- pyproject.toml` empty in a full-history clone; the Procfile serves `adapter.factory:create_app()` |

An `ACCEPT` is a step decision. It is not whole-change PASS, acceptance or closure, and it does not cover checks 16 to 21.

## 5. Ruling R-1: check 3's Moon Loop is accepted as a PASS-only deviation

| Item | Fact |
| :- | :- |
| Attempt-1 receipt | `TOOLING_BLOCKED`: "No interpreter meets step 1 in this venue: /usr/bin/python3 (3.14.4) makes _distutils_system_mod importable; /usr/bin/python3.13, 3.12 and 3.11 are absent". Preserved byte for byte at `docs/ephemeral/HDE-CRD-0002-QA100-t03-attempt1-primary-v1.0.log` (12,380 bytes, SHA-256 `f67c2274cb9288f464616b5db503846b36dacd6f245b03521af9b2e4872961e3`, verified here). Its failure signature is also in the governed primary's NOTES |
| Direction | Product Owner, in the execution session, before the rerun: "We need to just run a moon loop and pass T03. I am not going to be blocked on a python version as long as the product functions" (PO-1) |
| What changed | Only QA environment wiring outside every repository: an E-D venv from uv CPython 3.13.17 with a `.pth` entry for `/usr/lib/python3/dist-packages`, then `pip install --ignore-installed` after rerun 1's `rpds.rpds` import error. No repository file, predicate or expected value changed |
| Proof target | Unchanged. Step 1's two defining properties of E-D hold literally (Plan §3.2). The builder's own probe judged the patched backend present (`build_backend_compat=distribution_install_layout`, count 1). That is the WU-PR-02 F-1 causal condition S06 is about |
| Departures | The Plan's literal construction (`/usr/bin/python3 -m venv --system-site-packages`) and NZ-02's system-interpreter list; `setuptools` 78.1.1 rather than 68.1.2; `wheel` 0.46.3 rather than 0.42.0. None is a predicate of check 3 |
| Bounds | About ten minutes (attempt 1 published 23:46:03Z; decisive primary 23:56:15Z); one subsystem (the QA venv); no new evidence family, surface or token. Glow QA Guide §3.4.3: the republication updated the stable check directory |

**Ruling.** Accepted as a PASS-only Moon Loop deviation under Plan Templates "Bounded step-level rerun posture": "If an executed Moon Loop is broader than a narrow plan example but still remains minimal, auditable, within approved check scope, and does not add new acceptance surfaces, feature work, evidence family, token, or public contract, the review may accept it as a caveat or PASS-only deviation".

It stays acceptable because:
- the correction is environment wiring, which the Glow QA Guide §3.4.8 preflight rule names as what is repaired ("repair the plan and/or environment wiring");
- the venue's tools are the Product Owner's choice (QA-110 "Product Owner execution choice");
- every decisive predicate is met on unchanged code.

The evidence posture of Glow QA Guide §3.4.8 is met: the failure signature, the one-line remediation note naming what changed and why, and the PASS rerun are in the same primary. §10.6's rule that the original failure stays visible is met by the preserved attempt-1 file.

**Caveat carried to QA-120.** S06 is proven under Ubuntu 26.04's patched `setuptools` 78.1.1, wired as recorded. It is not proven under the Plan's literal E-D construction, and not for other distributions or versions (the primary's own nonclaim). PO-2's direction on tool versions (§9) bears on whether that matters; it is not canon yet.

## 6. Finding QA110-F01 (check 13; S20): the read-only guard trips although every report passes

### 6.1 Expected and observed

| | |
| :- | :- |
| Requirement | S20 (Specification v1.1): "One read-only command reports CI lanes and release membership for given paths, the current Build Notes path and hash, the uncovered-test sweep run in a throwaway copy, and a `ci.yml` replay in a throwaway worktree, writing nothing to the repository" |
| Expected (Plan check 13 step 1) | Exit 0, all five reports `status=PASS`, and a final `PREPUSH_CHECK_RESULT: PASS` line reporting the repository unchanged |
| Observed, decisive rerun (after attempt 1 ended at 2026-10-25T00:16:57Z; primary finalized 00:56:35Z) | Exit 4 (`EXIT_READ_ONLY_VIOLATION`); every report `status=PASS`; replay steps 01 to 16 `SUCCESS` (step 08 "4521 passed, 2 skipped"; `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; "copy after replay: clean"); stderr `PREPUSH_CHECK_READ_ONLY_VIOLATION: the repository's tree, ignored files, directories, HEAD or git metadata changed`; no `PREPUSH_CHECK_RESULT` line |
| Observed, attempt 1 (00:02:22Z to 00:16:57Z) | Exit 4 with the same stderr line, and replay `status=FAIL` at step 08: 2 failed in `tests/ops/test_hde_epic038_ops03.py` (`OSError: [Errno 18] Invalid cross-device link` between `/tmp` on tmpfs and `TMPDIR` on ext4); steps 09 to 15 `SKIPPED` |
| Other steps | Step 2 as predicated; step 3 "137 passed" both times; step 4 empty both times. The PR35-C1 signature does not apply: no test in `tests/tools/test_prepush_check.py` failed |
| Classification | `FAIL_BEHAVIOR` (Plan Templates "Exact status predicates" and "Causal precedence"). Readiness held and the QA tooling is trustworthy. The delivered surface under test (Plan §7 rule B names `tools/ci/prepush_check.py` for S20) contradicts an explicit predicate. Plan check 13's own Outcomes line maps exit 4 to `FAIL_BEHAVIOR` |

### 6.2 Independent verification (Kronos, scratch repositories only; no check was rerun)

1. **The git mechanism.** In throwaway repositories under git 2.43.0: a source repository with its objects packed, and a `git clone --shared --no-checkout` copy checked out detached. After clone and checkout, the source pack's mtime and ctime are unchanged. After `git hash-object -w` of a blob the source pack already holds, run from inside the copy, both move (1792891042 to 1792891045). Writing a new blob leaves them where they are.
2. **The delivered guard sees it.** The tool's own functions were imported from `tools/ci/prepush_check.py` at `aae2047`, with code equal to the tested source. `repository_state(src)` before and after `make_copy(src, head, copy)` is equal. After one write in the copy of an object already in the source pack, it differs, in the `metadata` field only.
3. **What follows from the code.** `make_copy` clones every throwaway copy with `--shared`. `_metadata_digest` digests the lstat identity (mode, size, mtime, ctime) of every file under `.git`, `objects/` included, and `main` returns `EXIT_READ_ONLY_VIOLATION` when the state differs. So any replayed or reporting step that writes, inside a copy, an object the source already packs changes the guarded state of the source, with no content change. This agrees with the executor's diagnostic under git 2.53.0 (results §5.2).

These establish that the mechanism exists in the delivered design. They do not establish which `.git` file changed during step 1 of the QA-100 run, or which step wrote. The guard's message names no file, and the executor's mtime inspection followed step 3, which overwrote any step-1 change (results §5.2).

### 6.3 Check 13's Moon Loop

The Product Owner directed it: "That means this environment needs a fix, so resolve it as a moon loop" (PO-3). It changed only the check shell (`TMPDIR` unset, as on hosted CI) and removed two leftover directories under `/tmp/hde-epic038-ops03`. It removed attempt 1's venue cause: the replay passed.

It is accepted as an execution deviation that sharpened the receipt. It did not resolve the check, and no Moon Loop could: the remaining failure is in delivered product code. That is non-QA-root remediation, and Glow QA Guide §3.4.8 and Plan §9 route it through PR work.

### 6.4 Venue dependence (fact, not diagnosis)

| Run | Venue | Result |
| :- | :- | :- |
| PR-40 lineage review of WU-PR-06 on `fc51620` (HDE Build Notes addendum 2.12) | The reviewing session's scratch clones (`--no-hardlinks`); git 2.43.0, CPython 3.12.3 | `replay --full` exit 0 with a `PREPUSH_CHECK_RESULT: PASS` line reporting the repository unchanged |
| QA Audit §7 item 9 on `0b15328d` | Throwaway clones in this Kronos session's scratchpad; CPython 3.12.3; git version not recorded by the Audit (this session's container reports git 2.43.0 at this review) | Plan check 13's step 1 exit 0, every line as predicated |
| QA-100, two runs on `2e03a268` (code identical to `0b15328d`) | Product Owner workstation; Ubuntu 26.04.1; git 2.53.0; source the E-L clone used by checks 1 to 12, 14 and 15 first | Exit 4 both times |

The code under test is the same in all three. Why the guard held in the first two venues is not established here. It is a fact for diagnosis, not for this review to resolve. The workstation is a real operating environment for the tool (`AGENTS.md`, "Report a finding only when its triggering input is real": "the operator's shell"), and the Plan does not restrict check 13's venue by git version.

### 6.5 Why this is escalation, not a bounded rerun

- QA-110 Execute rule 3 allows `BOUNDED_RERUN_REQUIRED` only when "the sole defect is an execution/evidence fault". Here the defect is in the delivered tool's design (§6.2), and a venue cause was already removed without changing the result (§6.3).
- Plan §9: "a second failure of the same check, any `FAIL_BEHAVIOR`, an invalid Plan, or a needed change of scope, target, rails, evidence or predicate goes to Kronos at QA-110, then through the ESC-10 remediation route". Glow QA Guide §10.6: "A second failure, behavior defect, invalid Plan, or scope/authority/code/Ops issue takes the ESC-10 remediation route".
- The repair changes `tools/ci/prepush_check.py` or its tests, product code outside the QA root.
- Check 13's one ordinary rerun is in any case consumed (R-2).
- QA-110 Execute rule 4 applies because the whole approved run is not complete (§10).

### 6.6 Second observed failure in the same check (O-1; for diagnosis, not decided here)

Attempt 1's replay failed two tests in `tests/ops/test_hde_epic038_ops03.py`. The OPS03 tool's fixed `RUN_ROOT` `/tmp/hde-epic038-ops03` (tmpfs) and pytest's `tmp_path` under `TMPDIR` (ext4) are on different filesystems, so a link or rename between them fails with `EXDEV`.

- That is a repository-test portability failure in a real venue, a developer shell with `TMPDIR` set.
- S20's replay reported it truthfully. It is not an S20 defect, and no CRD-0002 requirement names OPS03.
- Under Glow QA Guide §3.4.8 ("An independent or opportunistic defect requires separate Product Owner disposition"), Thoth or the Product Owner decides whether it is in scope.

It does not change T13's decision.

### 6.7 What stays valid

- Steps 2 to 4 of check 13 passed.
- The lanes, membership, build-notes and sweep reports passed with their predicated values.
- The replay passed every step once the venue cause was removed.
- Checks 1 to 12, 14 and 15 are accepted (§4) and are not reopened by this finding.
- WU-PR-06's accepted-final PR lineage (addendum 2.12) is not reopened by QA. Any repair is a new routed work item under Glow QA Guide §10.6.

## 7. Ruling R-2: attempt lineage

Plan §9 states that "The executor does not rerun on its own" and that "only Kronos's actual QA-110 decision allows attempt 2". Two checks ran a second execution inside attempt 1 without that decision, each at the Product Owner's in-session direction:
- check 3: two Moon Loop reruns;
- check 13: one rerun.

**Ruling** (precedent: HDE-EPIC040 QA-110 review v1.0, ruling LR-01):
- Each is recorded as a process deviation, and each check's one ordinary rerun is consumed. No attempt 2 remains for check 3 or check 13.
- Check 3's earlier attempt-1 bytes are preserved verbatim outside the governed root, because they were never committed (Plan §9's alternative for an uncommitted attempt 1, under which "the missing bytes are never reconstructed"). Here they were not lost.
- Check 13 preserves both executions in one primary.
- A later execution of check 13 after a repair is the remediation route's verification and return (Glow QA Guide §10.6 step 5). It is not an ordinary attempt 2, and it does not reset attempts.

The Product Owner's directions are honored as execution arrangements. They did not, and could not, decide acceptance; that decision is made here.

## 8. QA-100 deviations D-01 to D-08

| ID | Disposition |
| :- | :- |
| D-01 | Accepted. NZ-01: scratch locations under the session scratchpad, recorded in each primary |
| D-02 | Accepted. T01 ran steps 2 to 5 before the NZ-05 script, so the status read stays last. Every command is read-only; `command` records the real order |
| D-03 | Accepted. T05's `cmp` comparisons ran in one asserting script, applying Plan §5.2's expected-non-zero rule. Normalization only (Glow QA Guide §3.4.7) |
| D-04 | Accepted. T10's extra status read is supporting. T13's `exit_code` is step 1's status, the decisive child for the failed predicate |
| D-05 | Accepted. T11's factory names were resolved and counted within `## Routing and mounts`, as the collection directs |
| D-06 | Accepted. QA-glue corrections were made before publication, and none changed an observed value |
| D-07 | Accepted. Check 3's setup records had lone CR bytes converted to LF and noted (Plan §5.3 rule 1) |
| D-08 | Accepted. Specs were scanned for secrets as well as bodies: `NO_HIT` |

## 9. Product Owner decisions carried (PO-1 to PO-5)

| ID | Effect in this review |
| :- | :- |
| PO-1 | The check 3 Moon Loop (R-1) |
| PO-2 | "Do not pin tool versions", `PENDING_DRAINAGE`. Context for R-1's caveat. It changes no predicate of the approved Plan v1.2. Drainage owner: the Product Owner (direction record §5) |
| PO-3 | The check 13 Moon Loop (§6.3) |
| PO-4 | Evidence persisted in the repository. Accepted as Plan §2's evidence-only commit grant: amthorn78/glow-hdengine-v2#726's paths stay within §2's scope (§3), and the Product Owner merged it. Its prompt-defect report on QA-100 Execute step 4, addressed to the GCFPE-MGMT-10 maintenance owner, is carried unchanged |
| PO-5 | Drain the evidence-persistence rule to the Glow QA Guide §3.4.3; owner the Product Owner. No canon was edited. QA-110 records it and does not drain it |

## 10. Run state and routing

- **Whole approved run:** Plan v1.2 has twenty-one checks, and the Product Owner selected checks 1 to 15 ("Steps: Checks 1 through 15").
  - Checks 16 to 21 have no task and no selection. They are not authored dependency-waiting tasks, so no QA-100 branch exists for them.
  - Check 21 depends on checks 1 to 20 being published (Plan §8). The run is therefore incomplete (precedent: HDE-EPIC040 QA-110 review v1.0, "Run state: Incomplete" with checks unissued).
- **Branch:** a substantive behavior defect before the whole approved run is complete is `ESCALATION_REQUIRED` (QA-110 Execute rule 4). The destination is ESC-10 — Create QA Escalation Report — 100926.1, in this continuing Kronos session, with complete failure evidence. ESC-10 creates the report and hands it to Thoth (ESC-30); QA-110 chooses no remedy.
- **Not routed now:** checks 16 to 21. They need the Product Owner's selection at a later QA-90, which the remediation route does not block. The 1 to 15 results above are preserved for that run.
- **Thoth binding** for the escalation: the continuing Thoth session for HDE-CRD-0002 (https://claude.ai/code/session_01QDA4Gim8zTtX2KqAEWnaum), as the FND-001 remediation records name it.

## 11. Observations carried (not decided here)

| ID | Observation | Owner |
| :- | :- | :- |
| O-1 | §6.6: the OPS03 tests fail when `TMPDIR` and `/tmp` are on different filesystems | Thoth at ESC-30; the Product Owner if out of scope |
| O-2 | The canonical writer stamps `produced_at_utc: 2026-09-22T14:25:29Z` in every HDE-CRD-0002 path proof, a value also found in `audit/gates/sanity_pipeline/sanity_pipeline.log.path_proof.txt`; `mtime_utc` carries the capture time. The validators accept it | Kronos, at check 21's review (S22, the first real publication) |
| O-3 | Left outside the repository on the Product Owner's workstation (results §9): uv CPython 3.13.17, and two OPS03 test directories under `/tmp/hde-epic038-ops03/`. The QA-100 evidence checkout and working files may now be removed: this review has read the evidence from `main` | Product Owner |
| O-4 | Collection self-review (Kronos, QA-90 author). NZ-02 listed only system interpreters, so a venue without them reached `TOOLING_BLOCKED`. §4.8's default, "without the grant the Product Owner commits", led to PO-4. Neither touched a proof target | Kronos, for later HDE-CRD-0002 QA-90 tasks |

## 12. CANON_CONFLICT_REGISTER (carried)

Carried unchanged from Plan v1.2 §13, collection §6 and results §10. The full entries are in Plan v1.2 §13. QA-110 adds none: the finding is a behavior defect, not a canon conflict.

| Entry | Status | Reviewer / artifact |
| :- | :- | :- |
| CR-1 to CR-3 | `APPROVED_AS_CHANGED` | As Plan v1.2 §13 records |
| CR-4 | `APPROVED` | As Plan v1.2 §13 records |
| CR-5 | `APPROVED_AS_CHANGED` | As Plan v1.2 §13 records |
| CR-6 to CR-8 | `APPROVED`, alternative (a) | As Plan v1.2 §13 records |
| CR-9 | `PROPOSED` | Isis, IA-30 boundary; unreviewed |
| CR-10 | `APPROVED`, alternative (a) | HDE Build Notes addendum 2.24 |
| CR-11 | `APPROVED_AS_CHANGED`, alternative (a) | QA-70 review v1.0; applied in check 1, which found no deltas |

PO-2 and PO-4 meet canon that is silent on their subjects (each direction record §3 or §5), so they are not conflicts.

## 13. Constraints, unresolved items and owners

| Item | Owner | State |
| :- | :- | :- |
| QA110-F01 remedy | Thoth (ESC-30), then IA and Isis (Glow QA Guide §10.6) | Open; the ESC-10 report comes first |
| Which `.git` file changed in step 1, and which step wrote it | Thoth (diagnosis) | Not observed (§6.2) |
| Why the guard held at `fc51620` (git 2.43.0) and at `0b15328d` (git version not recorded) | Thoth (diagnosis) | Not established (§6.4) |
| O-1 | Thoth; Product Owner if independent | Open |
| Selection of checks 16 to 21, check 20's venue and initiator | Product Owner | Not selected |
| Re-verification of check 13 after a repair | Kronos, on the remediation route's return | Not due |
| PO-2 and PO-5 drainage | Product Owner | `PENDING_DRAINAGE` |
| G-1, the close representation of S01 | Close mutation set and Isis; Product Owner if needed | Open; T15's evidence is in |
| CR-9 | Isis, IA-30 boundary | `PROPOSED` |
| QA-100 prompt defect (PO-4 record §6) | GCFPE-MGMT-10 maintenance owner | Reported by QA-100; carried |

## 14. TypeSafe reading for the receiving session (ESC-10)

Action sent (v8.2): "Write a new QA escalation report, a single document of a few hundred lines, for one change request from an already-completed QA evidence review: one failed check of a delivered developer tool (a read-only pre-push command whose repository-unchanged guard reports a violation in one venue but not in two earlier ones), stating expected versus observed behavior, the attempts and evidence, hypotheses kept separate from evidence, affected requirements and preserved valid results, and the exact facts the remediation owner must resolve, without choosing a remedy. No task list exists; no live run against a provider occurs; a later independent diagnosis and remediation review follows; the work is one unit, not many independent units."

The reading as printed by the script:

- **TypeSafe v8.2: Sonnet 5.5 at high.** Effort score 1.68 (confidence 0.71); rung probabilities low 0.01, medium 0.36, high 0.58, extra high 0.04, max 0.01, ultracode 0.00. Model probabilities Fable 5.1 0.02, Opus 5.5 0.34, Sonnet 5.5 0.64, Haiku 5.5 0.00 (confidence 0.52). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.007, Fable 5.1 at high 0.012, Fable 5.1 at extra high 0.001, Fable 5.1 at max 0.000, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.003, Opus 5.5 at medium 0.122, Opus 5.5 at high 0.197, Opus 5.5 at extra high 0.014, Opus 5.5 at max 0.003, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.006, Sonnet 5.5 at medium 0.230, Sonnet 5.5 at high 0.371, Sonnet 5.5 at extra high 0.026, Sonnet 5.5 at max 0.006, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Sent 2026-10-25T01:25:12Z. Nathan picks the cell.
- **Detail (as printed):** v8.2 sent 2026-10-25T01:25:12Z; HTTP 200 in 0.62 s; 5478 input and 69 output tokens; jev-1.13.0. Rung by rule: high (nearest to the score, halves up); model by rule: Sonnet 5.5 (the most probable of the four options, a tie going to the higher-priced model). Flags: none printed.
- **Which request:** the installed TypeSafe scoring skill's request v8.2 and `score_v8.py`, run once with session kind `review` and label "ESC-10 HDE-CRD-0002 check 13 escalation report", before this review was saved.
- **Records:** the Notion row was not written.
- **Picks:**
  - ESC-10: Nathan's pick is not stated.
  - This QA-110: Nathan's pick is not stated. Its reading was not taken: the QA-100 record §11 states "TypeSafe: not read" (HTTP 403 in that venue).

**Surface advice for ESC-10.**
- **Session:** this continuing Kronos session for HDE-CRD-0002 (https://claude.ai/code/session_01PnD4YNbFZStRQWZ7TCM6jV), on `amthorn78/glow-hdengine-v2`, which ESC-10 names as its own role.
- **Reads:**
  - this review;
  - the check 13 primary on `main`;
  - the QA-100 results §5.2;
  - Plan v1.2 check 13, §7 rule B and §9;
  - the Specification v1.1 S20 row;
  - WU-PR-06's instruction, plan, lineage review and postmortem v1.1;
  - HDE Build Notes addendum 2.12;
  - Glow QA Guide §3.4.8 and §10.6.
- **Optional re-check:** §6.2's reproduction runs in under a minute, with scratch git repositories and the tool's own functions.
- **Access:** GitHub read only. There is no production, vendor, Railway or database access, and the 24-minute replay is not rerun (ESC-10 executes no QA).
- **Writes:** only its report, checkpoint and handoff under `docs/ephemeral/`, by pull request.

## 15. Nonclaims

This review accepts fourteen step results and escalates one. It does not establish:
- whole-change QA PASS, acceptance or closure, or any S-requirement as a whole-change verdict;
- deployment, release activation, or PF09 or PF30 movement;
- the QA-120 Report.

It chooses no remedy for QA110-F01 and changes no product, test, generator, governed artifact or PF file. The pre-push tool's result is not CI's result. Hosted CI's green on amthorn78/glow-hdengine-v2#726 is not QA.

## Canon relied on

Read from `docs/pfcanon/` on `main` at `aae2047`; this branch edits no `docs/pfcanon/` file.

| Decision topic | Governing source read |
| :- | :- |
| The review's own rules: member states, routing, indexing proof, the whole-run condition | QA-110 — Review QA Evidence and Route the Next Action — 100926.1 (page state 2026-10-12T02:29:41.377Z), read in full: "Required QA evidence indexing", "QA authorship and Product Owner execution choice", "Execute and decision rules" 1 to 6, "Required result and routing" |
| ESC-10 receiver contract | ESC-10 — Create QA Escalation Report — 100926.1 (page state 2026-10-12T02:29:32.722Z), read in full: "Required inputs", "Execute", "Result routing" |
| Moon Loop scope and evidence posture (R-1, §6.3) | PF19-Canon-Glow-QA-Guide v3.0.6 §3.4.8, read in full: Moon Loop, "Entrypoint existence preflight", "Execution-critical helper readiness", the hard boundary, "Allowed remediation actions", "Non-QA-root remediation boundary", "Evidence posture for in-session remediation", the stop condition, "PO-approved Extended Moon Loop remediation" |
| Accepting a broader Moon Loop as PASS-only; rerun posture (R-1, R-2) | PF27-Canon-Plan-Templates v2.0.5, the Step-0B "Moon Loop allowed (bounded)" clause and "Bounded step-level rerun posture", each read in full |
| Status classification of T13 | PF27-Canon-Plan-Templates v2.0.5 "Exact status predicates" and "Causal precedence", read in full |
| Escalation route and attempt limit (§6.5, R-2) | PF19-Canon-Glow-QA-Guide v3.0.6 §10.6, read from "Artifact and owner boundaries" through "Evidence-package caveats and failure history" |
| Republication into the stable check directory; PO-5's drainage target | PF19-Canon-Glow-QA-Guide v3.0.6 §3.4.3 (read from its opening through the path-grammar table's first row) |
| S20's delivery lineage and prior passing venue (§6.4, §6.7) | HDE Build Notes v13.7.8 (`docs/pfcanon/PF10-HDE-Build-Notes-v13.7.8.md`): addendum 2.12 "Approval and source record" and "Retained decisions and requirements", read. The whole file was searched for `prepush`, `pre-push`, `READ_ONLY_VIOLATION`, `freshen`, `--shared`, `PR35-C1`, `Moon Loop`, `QA-110`, `ESC-10` and `whole approved run`. The hits are in 2.12, the 2.21 PR35-C1 record (read at QA-100's citation) and the CRD-0002 records 2.24 to 2.26. No addendum sets a rule for evidence review, Moon Loop acceptance or the pre-push guard, so the Glow QA Guide and Plan Templates govern |
| Real-input rule for the venue (§6.4) | `AGENTS.md` "Code review guidelines", "Report a finding only when its triggering input is real" (repository rule, read) |
| In-flight documents | QA Plan v1.2 (§2, §3.2, §5.6, §6, §7 rules A and B, checks 1 to 15, §9, §10), read in full for those parts. QA-70 review v1.2 (§7). QA-90 collection v1.0 (§3 and §5, read in full). QA-100 results v1.0, checkpoint and handoff (read in full). The T03 attempt-1 record. The two Product Owner direction records (read in full). Specification v1.1-approved (S20 row and change map). WU-PR-06 instruction (header). The HDE-EPIC040 QA-110 review v1.0 (its LR-01 ruling and run-state row, as precedent) |

## Provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | GCFPE-USE-HDE-CRD-0002-QA-110-20261025-01 |
| change | CRD HDE-CRD-0002 (Specification v1.1-approved with delta 01) |
| unit | QA Plan v1.2 checks 1 to 15; tasks T01 to T15, attempt 1 each; requirements S01 (removal), S03 to S21 as mapped |
| prompt | QA-110 — Review QA Evidence and Route the Next Action — 100926.1, page state of 2026-10-12T02:29:41.377Z |
| release | GCFPE-20261009.1 / 100926.1 |
| role/stage | Kronos, QA-110 (`ESCALATION_REQUIRED`) |
| capture time | 2026-10-25T01:26:00Z |
| execution identity | https://claude.ai/code/session_01PnD4YNbFZStRQWZ7TCM6jV (no worker subagents) |
| earlier uses | GCFPE-USE-HDE-CRD-0002-QA-100-20261024-01 and those it lists, each in its artifact |
| task/result/review mapping | T01 to T15 → `qa-01-preflight` to `qa-15-s01-removal` → QA-100 results §3 → §4 here (14 `ACCEPT`, T13 `ESCALATION_REQUIRED`) |
| repository persistence | PENDING / NON_GATING (`docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent on `main`); owner: the authorized repository writer when the procedure is installed |
