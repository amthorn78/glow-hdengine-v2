---
artifact_type: QA_EVIDENCE_REVIEW
artifact_id: HDE-CRD-0002-QA110-QA-EVIDENCE-REVIEW
artifact_version: "1.2"
predecessor: docs/ephemeral/HDE-CRD-0002-QA110-qa-evidence-review-v1.1.md (ACCEPT of T13-RV1; run incomplete; selection SEL-110-1; blob b6968f8966e0; unchanged). Its predecessor v1.0 (T01 to T15; blob 0a797250aa81) is unchanged
state: ACCEPT
run_state: COMPLETE (every check of approved QA Plan v1.3 has a published primary and an accepted step decision)
change_class: CRD
change_id: HDE-CRD-0002
change_name: "Post-HDE-EPIC040 Repair: Carried Defects, Code Security Review, Pre-Push Check and Close-Pack Writer"
author: Kronos, the continuing QA authority for HDE-CRD-0002 (execution identity https://claude.ai/code/session_01PnD4YNbFZStRQWZ7TCM6jV, the session of reviews v1.0 and v1.1; not the session that executed T16 to T21)
session_disposition: continuing Kronos context, as the QA-100 handoff to QA-110 v1.3 routes it
invocation_binding: CRD / HDE-CRD-0002 / QA-110 / tasks T16 to T21 → QA-100 results v1.2 §3 and v1.3 §2 (QA Plan v1.3 checks 16 to 21, attempt 1 each)
context_conflict: NONE
execution_posture: MANUAL_PROMPT_EXECUTION
prompt: QA-110 — Review QA Evidence and Route the Next Action — 100926.1 (https://app.notion.com/p/3f44590a05eb81ee9a09e00af51f33cb; page state 2026-10-12T02:29:41.377Z; read in full at review v1.1 in this session, unchanged)
ecosystem_release: GCFPE-20261009.1 (100926.1)
approved_base: docs/ephemeral/HDE-CRD-0002-QA50-qa-plan-v1.3.md (QA_PLAN v1.3; blob 3aea6033e3c0; SHA-256 30f4a83cfa62276523c6bad5222f521cdf361eed8ebe59408387b24e8c2ec35a; immutable)
approving_review: docs/ephemeral/HDE-CRD-0002-QA70-qa-plan-review-v1.4.md (APPROVE by Isis, 2026-10-25T16:38:19Z)
qa_audit: docs/ephemeral/HDE-CRD-0002-QA50-qa-audit-v1.0.md (AUDIT_COMPLETE)
task_collections: docs/ephemeral/HDE-CRD-0002-QA90-qa-task-collection-v1.2.md (T16 to T20; blob 91beb2f75312; SHA-256 39d374bde3bb4d4d6ed2a6ac7b04fe293e28853d4ed38f2be9b3385831d77251) and docs/ephemeral/HDE-CRD-0002-QA90-qa-task-collection-v1.3.md (T21; blob a3e1daadfcb3; SHA-256 98f50573ee32eef64b23ed796c108cedc86a9a61f86b290f31e37aad6cdb441d); both on main through amthorn78/glow-hdengine-v2#743 (squash 44ce4ce), byte-equal to the pins QA-100 executed
execution_results: docs/ephemeral/HDE-CRD-0002-QA100-qa-execution-results-v1.2.md (blob 683d0c925dfa; 17,623 bytes) and docs/ephemeral/HDE-CRD-0002-QA100-qa-execution-results-v1.3.md (blob 1e5a343aff94; 10,272 bytes); on main through amthorn78/glow-hdengine-v2#744 (squash bb931733)
evidence_of_record: audit/qa/hde-crd-0002/ on main at bb931733035cb1d0d5d6f05169a6240c67a8fd18 (manifest 3,323 bytes, SHA-256 203b8ca18c061a918f9ca25df0e9f4596cd770a2134e305cb21f235c2aed9874; 21 checks)
tested_targets: the deployed production service glow-hdengine-v2 (checks 16 to 19, E-P; check 20, V-B in container 60f93a3e5923), release_id 77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e; the published family on the evidence branch built from main 463cbbef, a state-(b) commit (check 21)
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.8.md (SHA-256 439775924392a206ceffb70952b0af1975c24d4214fc73d4ed98fcf94220e13c; addenda 2.27 and 2.28 read in full in this session at QA-80; unchanged since)
observed_revision: bb931733035cb1d0d5d6f05169a6240c67a8fd18 (origin/main at review; amthorn78/glow-hdengine-v2#743 and amthorn78/glow-hdengine-v2#744 merged)
routing: QA-120 — Create Final QA Report and RCA — 100926.1, the continuing Kronos
PF10_ADDENDUM_OUTPUT: NOT_PRODUCED_BY_QA-110 (QA-110 is not an addendum producer)
created_at: 2026-10-26T00:25:00Z
---

# HDE-CRD-0002 — QA Evidence Review v1.2 (QA-110): checks 16 to 21

## 1. Result

| Task | `check_id` | Requirement(s) | QA-100 state | Step-log status | Decision |
| :- | :- | :- | :- | :- | :- |
| T16 | `qa-16-deployed-identity` | Step-0C (FND-031, FND-032) | `COMPLETE` | `PASS` | `ACCEPT`, with G-1 recorded (R-3) |
| T17 | `qa-17-deployed-not-found` | S02 | `COMPLETE` | `PASS` | `ACCEPT` |
| T18 | `qa-18-deployed-dev-surfaces` | S10, S19 | `COMPLETE` | `PASS` | `ACCEPT` |
| T19 | `qa-19-deployed-reader-input` | S19 | `COMPLETE` | `PASS` | `ACCEPT` |
| T20 | `qa-20-live-vendor-override` | S14, S19 | `COMPLETE` | `PASS` | `ACCEPT` |
| T21 | `qa-21-evidence-admission` | S22 | `COMPLETE` | `PASS` (after a Moon Loop rerun) | `ACCEPT`, with the Moon Loop accepted as a PASS-only deviation (R-4) |

- **Run state: complete.** With reviews v1.0 (T01 to T12, T14, T15) and v1.1 (T13-RV1), every check of Plan v1.3 now has an accepted step decision. All twenty-one manifest statuses are `PASS`.
- **Route:** QA-120 in the continuing Kronos session (QA-110 "ACCEPT" branch: the whole approved run is complete).
- **Incident I-1** (secret values printed into the executing session's transcript) is recorded and carried to QA-120's RCA (§6). It does not touch the evidence (§4).

Each `ACCEPT` is a step decision. It is not whole-change QA `PASS`, acceptance or closure; QA-120 decides the verdict against Plan §11.

## 2. Matching and identities (Execute rule 1)

| Item | Verified |
| :- | :- |
| Tasks to results | T16 to T20 (collection v1.2 §5) ↔ results v1.2 §3.1 to §3.5; T21 (collection v1.3 §3) ↔ results v1.3 §2. One member each, no duplicate, no unmatched member |
| Plan and checks | Plan v1.3 checks 16 to 21, blob `3aea6033e3c0`. Each task restates its check's actions, predicates and Outcomes unchanged, with the recorded normalizations NZ-01, NZ-06, NZ-08, NZ-20 to NZ-25 and NZ-30 to NZ-32 |
| Collections executed before merge | QA-100 executed v1.2 and v1.3 from the open amthorn78/glow-hdengine-v2#743 by Product Owner direction ("just proceed", PO-QA100-3). The bytes on `main` equal the executed pins: SHA-256 `39d374bde3bb4d4d6ed2a6ac7b04fe293e28853d4ed38f2be9b3385831d77251` and `98f50573ee32eef64b23ed796c108cedc86a9a61f86b290f31e37aad6cdb441d` recomputed here. Process deviation with no effect on content |
| Selection | SEL-110-1 (checks 16 to 21). The Product Owner narrowed the first execution to 16 to 20 (PO-QA100-1), then re-selected check 21 (PO-QA100-5) |
| Attempts | Attempt 1 each. T21 holds an in-session rerun inside attempt 1 (R-4) |
| Executor and initiator | Kronos as executor in a separate local CLI session on the Product Owner's workstation (5c9c7c47-41bd-437a-a9ee-63879dec618b), by the Product Owner's arrangement. That session also authored collections v1.2 and v1.3. This review runs in a different session. Check 20's V1 and V2 were typed and run by the Product Owner, attested verbatim: "I, Nathan, the Product Owner, typed and ran V1 and V2 myself" |
| Environments | E-P: the workstation shell, curl 8.18.0, Production binding recorded. V-B: `railway ssh` into service `glow-hdengine-v2`, container `60f93a3e5923` at P0 to A2, `/app/.venv/bin/python` (3.13.16), actor `root`. Check 21: evidence checkout and a `cp -a` test copy, CPython 3.12.15 with CI's install, default closed rails exported per command (NZ-30) |
| Deployed candidate | `release_id` `77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e` in check 16's body and in check 20's P1 `--version`. Release unchanged since state (a) (Plan §2) |

## 3. Predicates against captured output (Execute rule 2)

Every decisive value was read from the primaries' `=== COMMANDS ===` captures, not from their `=== PREDICATES ===` lines. Where practical, it was recomputed here.

**Check 16** (Plan check 16):
- Steps 1 to 4 `200 1.1`; four `HTTP/1.1 200 OK` status lines; `Cache-Control: no-store` and `Content-Type: application/json; charset=utf-8` in each; no `ETag` and no `Last-Modified` header (0 occurrences in the primary).
- HEAD `Content-Length: 347`, equal to step 1's body length. Step 5 `True True True True True 347`, both `cmp` silent.
- **Body recomputed:** the captured line plus one LF is 347 bytes with SHA-256 `c9302e7072138482c1363f66c58606b45faac476a07235772d06ca581bc0f06a`, as recorded. It has the six keys in the frozen order and canonical compact form, and `release_id` is the candidate.
- Step 6 `GET /internal/version False`, `HEAD /internal/version False`. Step 7 five `OK`, `classification PASS`, identity `MATCH`. The six consumed WU-OPS-01 digests equal collection v1.2's values (CR-9 interim (a)).
- Holds.

**Checks 17 to 19:** parsed request by request against the governed envelopes. Expected envelope bytes, each with one final LF:

| Envelope | Bytes | SHA-256 |
| :- | -: | :- |
| `ERR_NOT_FOUND` | 70 | `80c608ed33e9592b3e268e6ab8f66dd4444df3328ad379edae087530c77f6629` |
| `ERR_READER_FORBIDDEN` | 92 | `cbf3de126393c739e0f538498c2550504911a743dc4f6e9cc370120fae8e7c33` |
| `ERR_WRITER_FORBIDDEN` | 86 | `7d18dd2d18090514d4559ec66932cb52dc77f70549ad8f9c206658fe4d8a24c8` |
| `ERR_READER_INVALID_INPUT` | 94 | `c5eb83aec246444fe5d207f14e089b28d2cafc35c5d84ff49bc719b01c37b27a` |

| Check | Requests | Result |
| :- | :- | :- |
| 17 | r1, r3 to r7 `404` with the `ERR_NOT_FOUND` bytes; r2 (HEAD) `404`, body not observable with `curl -I` (recorded); r8 `405` with `Allow: GET, HEAD, OPTIONS` and the `ERR_NOT_FOUND` bytes | Each `HTTP/1.1`, `application/json; charset=utf-8`, `no-store`, no `ETag`, curl exit 0. Holds |
| 18 | d1 `403` `ERR_READER_FORBIDDEN`; d2 `403` (HEAD); d3 to d6 `403` `ERR_WRITER_FORBIDDEN`; d7 to d9 `404` `ERR_NOT_FOUND`. Observations o1 `OPTIONS` `200` and o2 `//reader?v=1` `403`, no predicate (LR5-O1) | As above. Holds |
| 19 | q1 (`v=1`, b1), q2 (`v=2`, b1), q3 (`v=1`, b2), each `422` with the `ERR_READER_INVALID_INPUT` bytes. Inputs recomputed: `[`×32,768 is 32,768 bytes, SHA-256 `a90ff70ad51360979071d268065d422fdea638d17ee71a1dd76d12f4e71578b1`; `{"a_id":`+`[`×20,000 is 20,008 bytes, `cdf9cd5993ce58f7834953703ae6cbaafab44980601489b357435db76c6874d0`. Both equal the recorded values, and the curl lines post those files to the named routes | Holds |

**The "final LF no" label** in the body headers of checks 16 to 19 is the assembler's display flag, not a fact about the response. The recorded lengths and SHA-256 values include exactly one final LF, as the recomputations show.

**Check 20** (Plan check 20; parsed from the captures):

| Item | Captured | Holds |
| :- | :- | :- |
| P1 | `P1_EXECUTABLE=OK`; `/app/engine/__init__.py`; `hdctl 0.0.0 (hdengine@prod;77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e)`; check 16 `PASS` at 23:18Z in the same session window | Yes |
| P2 | `HD_API_BASE_URL`, `HD_API_KEY`, `GEO_API_KEY` `SET`; `HDAPI_BASE_URL` `UNSET`; `APP_ENV=prod ENGINE_ENV=UNSET P2_ENGINE_ENV=OK` | Yes |
| P3 | exactly `SAFE_MODE=0`, `ALLOW_NETWORK=1`, `APP_ENV=prod`, `LC_ALL=C`, `LANG=C`, `TZ=UTC` | Yes |
| P4 | `ENGINE_ROOT=/app SINK=/root/.local/state/glow-hdengine/vendor_prod_override.jsonl ABSOLUTE_AS_CONFIGURED=True IN_REPOSITORY=False DIR_WRITABLE=True FILE_WRITABLE=True LINES=0`; directory `drwx------` (NZ-24) | Yes |
| P5 | `root` | Yes |
| V1 | exit 1; stdout (353 bytes, SHA-256 recomputed equal) `PROVIDER_PROD_OVERRIDE_REQUIRED`, `details.outbound_attempted` `false`; product stderr 0 bytes; one new sink line `refused`, `authorization_ref` `null`, `outbound_attempted` `false` | Yes |
| V2 | exit 0; stdout (2,022 bytes, SHA-256 recomputed equal) `status` `ok`; `route_family` `recommended_v2_chart`, `resource_path` `charts`; adapter `mapped`, `ChartResult`; `adapter_mapped_no_raw_vendor_payload`; `rows_written` 0; `Authorization: Bearer <redacted>` and `HD-Geocode-Key: <redacted>` present, no `HD-Api-Key`; product stderr 0 bytes | Yes |
| Sink | three new lines, each with the 16 keys of HDE CLI/API/Vendor Ref §7.1.11f; `refused` (own correlation ID), then `allowed` (`authorization_ref` the reference, `outbound_attempted` `false`, `route_family` `null`) and `completed` (`outbound_attempted` `true`, `recommended_v2_chart`, `charts`, `error_code` `null`), the last two sharing `5ef25d3a-79a0-43c5-885a-e4f879ea4607`; `actor_principal` `root` = P5; no user, birth, location, URL or header key and none of the synthetic input values | Yes |
| Container | `60f93a3e5923` at every read, V1, V2 and the after-reads (NZ-23) | Yes |
| Secret scan | A3 `NO_HIT` in the service against the service's values (4 names, 3,815 characters); local scan `NO_HIT` | Yes |
| Request limit | one allowed invocation (V2); no `--upsert`; no other vendor command | Yes |

V-A's `git status` is not applicable under V-B and is recorded with the reason. The stray `bash /tmp/` keystroke before V1 ran only locally and reached no service.

**Check 21** (Plan check 21; collection v1.3): see R-4 for the first run and the Moon Loop. The rerun's captures:
- Readiness (i) and (ii) silent, with `engine` inside the copy.
- `validate_crd_check_family` for HDE-CRD-0002 lists checks 1 to 20 with 20 of 20 statuses equal to their headers. Its only other entry is `qa-21-evidence-admission`'s own first publication (NZ-32, R-4).
- HDE-CRD-0001 validates with 10 checks. The five validators exit 0. Index read `21 21 []`.
- Step 2: `31 passed, 35 deselected`; `1 passed`; `81 passed, 86 deselected`; `1 passed`.
- Holds.

## 4. Evidence integrity and indexing

Verified read-only on `main` at `bb931733`, in a full-history scratch clone (git 2.43.0; CPython 3.12.3 with CI's install), under `env -i` with `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`. `git status --porcelain` was empty afterwards.

| Check | Result |
| :- | :- |
| `update_evidence_index.py --check`, `orientation_demo.py --check`, `validate_evidence_paths.py`, `check_mirror_schema.sh`, `check_lf_endings.py` | exit 0 each |
| `validate_crd_check_family`, HDE-CRD-0002 | 21 checks, all `PASS` |
| `validate_crd_check_family`, HDE-CRD-0001 | 10 checks |
| Index and Mirror | 22 of 22 keys (the manifest and 21 primaries) in `docs/evidence/INDEX.json`, 22 of 22 in `artifacts/evidence_index.jsonl` |
| Primaries 16 to 21 | each header `status` equals its manifest status, and each path proof's `size_bytes` and `sha256` equal the file: 16 `daad275072310b5aace1e726234d618f02c5cdaa26ebc2a732c129c08cacbdac`, 14,792 bytes; 17 `27258d4a7b1d1969dab693f1b257287f0ce1a023744021dfe9333b5ccf2db3eb`, 15,793; 18 `63fe7da715fc16c6f0e9d9246d56cfcda4581565d3cbddaecf2056f67a48856b`, 19,984; 19 `7c4cc490ccf4933851fd4a46efc0d98c2716955979eadb0e01a45e80d08b6412`, 8,929; 20 `5e96be9bd026172770b15a691fe18de415e13fb8907442dc09aaa99882bf1ed1`, 26,905; 21 `e5b7ca127fed0d22895b020fd3e19a3d23ec4a28881853d4f9b9e2f36b662502`, 20,604. All equal QA-100's records |
| Manifest | 3,323 bytes, SHA-256 `203b8ca18c061a918f9ca25df0e9f4596cd770a2134e305cb21f235c2aed9874`, equal to results v1.3 §3 |
| PR head against `main` | `git diff faea2922 bb931733 -- audit artifacts docs/evidence` is empty |
| Failure visibility | check 21's first run is blob `3e1562ea1175` at `d639772d` (20,530 bytes), preserved in history and recorded in the republished primary |
| Commit boundary (grant PO-QA100-2) | the evidence commits touch only `audit/qa/hde-crd-0002/**` and the updater-owned graph files; the records only `docs/ephemeral/` |
| Secret posture | the primaries record names `SET`/`UNSET` only. A pattern scan of the six new primaries and the QA-90/QA-100 records found no name-equals-value pair, no URL other than the production base, Notion, GitHub and tool-documentation links, and no DSN or key shape. This review holds no secret values, so value comparison relies on the executor's `NO_HIT` scans |

Missing required indexing: none. Plan §5.6's final receipt (results v1.3 §3) is present, and its values reproduce here.

**Hosted CI** (Plan §5.6: QA-110 reads it and QA-120 reports it; not a check predicate), at review:

| PR or push | Head | Run | State |
| :- | :- | :- | :- |
| amthorn78/glow-hdengine-v2#741 | `a905f246` | 40218259658 | success |
| `main` push | `86a75564` | 40218785186 | success |
| amthorn78/glow-hdengine-v2#744 | `2861558b` (checks 16 to 20) | 40245581199 | success |
| amthorn78/glow-hdengine-v2#744 | `66a1db8d`, `d639772d`, `7974e2c7` | 40245549332, 40246659316, 40247266229 | cancelled, superseded by later pushes (pull-request cancellation) |
| amthorn78/glow-hdengine-v2#744 | `faea2922` (head) | 40247385667 | in progress |
| `main` push | `bb931733` | 40247678102 | in progress |

QA-120 reads and reports the two runs still in progress. A red result is classified from its log before any re-run (FND-024, IR-7).

## 5. Rulings

**R-3 — G-1, check 16's header timestamp: accepted as a recorded assembly deviation; no republication.**
- Fact: the header's `timestamp_utc` is `2026-10-25T23:40:00Z`, a value typed during assembly. The requests ran 23:18:11Z to 23:18:12Z (body), and the primary was written at 23:23:10Z (its path proof's `mtime_utc`).
- Plan §5.4 asks for "the check's own finalization time". The header value is therefore wrong as metadata. No predicate reads it, the true times are preserved in the body and the path proof, and every validator accepts it.
- Republishing from the preserved body would be an assembly correction, not a rerun. It would also change the family after check 21 validated it and after §5.6's final receipt, so both would need repeating for no gain in proof.
- Decision: keep the primary as published. QA-120 states the true execution and finalization times and that the header value is a typed label. Basis: QA-110 "Required QA evidence indexing" ("do not rerun valid QA solely to index it"); Glow QA Guide §3.4.7 normalization (a metadata defect that changes no proof target); `AGENTS.md` "Evidence attribution" (record the actual tested state and time).

**R-4 — Check 21's first run and its Moon Loop: accepted as a PASS-only deviation.**
- **First run.** Readiness (i) printed `docs/prompt_ecosystem_management/authoritative-surfaces.md | 6 +++---`. The file changed on `main` in `63335e66` (amthorn78/glow-hdengine-v2#737, a Product Owner direction record and feedback-list note), after `da5735eb`. Plan §7 rule A maps a non-empty read to `TOOLING_BLOCKED`, and that is what was published (`d639772d`). Classification correct.
- **Cause: a planning defect in Plan v1.3 (this reviewer's own Plan).** §2's state (b) and rule A's guards exclude only `docs/ephemeral/` and `docs/pfcanon/`. `AGENTS.md` "Code review scope" names eight CI-exempt storage prefixes, `docs/prompt_ecosystem_management/` among them, which carry no runtime. A later change under any of the other six blocks the guard although no code changed. The failure is a Plan-versus-repository mismatch, not product behavior (Plan Templates "Bounded step-level rerun posture": classify as planning, harness or evidence-posture failure).
- **The correction.**
  - In the QA-created throwaway test copy only, the one file was restored to `22a3bc0`'s bytes (SHA-256 `9daecccc35005346e574b0055c27cd79f76ff4ec246d204d4bdf678f16e12b97`, equal to `git show 22a3bc0:` of the file), committed locally (`3b3cef3d`) and never pushed.
  - The copy then equals state (b) exactly as Plan §2 defines it.
  - No repository file, product code, test, generator, governed artifact, predicate or expected value changed.
  - The evidence checkout and `main` were untouched.
- **Why it is acceptable.**
  - Glow QA Guide §3.4.8 and Plan Templates "Moon Loop allowed (bounded)": the correction is minimal (one file, one surface), its root cause is clear, and it added no acceptance surface, feature, evidence family, token or public contract.
  - The evidence posture holds: the failure signature, a one-line remediation note naming the path and why, the hashes, and the rerun PASS are all in the same primary. The first run's bytes are also in history at `d639772d`.
  - The non-QA-root boundary (§3.4.8 "Non-QA-root remediation boundary") governs changes to the repository. This change was to a throwaway copy, and it restored rather than altered the Plan's defined target.
  - Plan Templates allows a review to accept such a Moon Loop as a PASS-only deviation when it "remains minimal, auditable, within approved check scope". This review states why, rather than hiding it under PASS.
  - **Independent check that the restored file did not bear on the result.** The four step 2 selectors were run here on an unmodified copy of `main` at `bb931733` (the final published family, with check 21 `PASS` and the file as amthorn78/glow-hdengine-v2#737 left it): `31 passed, 35 deselected in 273.65s`; `1 passed in 0.34s`; `81 passed, 86 deselected in 2.00s`; `1 passed in 9.33s`; each exit 0, `git status --porcelain` empty afterwards (2026-10-26T00:09:59Z to 00:14:47Z, git 2.43.0, CPython 3.12.3 with CI's install, closed rails). The same counts as the Plan and the rerun, without the restore. No Python, YAML or JSON file outside `docs/ephemeral/` names the file. The CI files that name its prefix (`ci.yml`, `classify_ci_changes.py`, `prepush_check.py`, `check_direct_db_contract.py`) name it as a documentation prefix, not as content.
  - Precedents: QA-110 v1.0 R-1 (a PASS-only Moon Loop deviation); HDE Build Notes 2.28.
- **NZ-32** (an execution-time normalization). Plan check 21's "exactly the twenty IDs of checks 1 to 20" was judged as: all twenty present with equal statuses, and no entry other than `qa-21-evidence-admission` itself, which the republication replaces by `check_id`. This preserves the predicate's objective, a coherent family of checks 1 to 20. The extra entry exists only because the first run published before the rerun. Accepted (Glow QA Guide §3.4.7).
- **Attempt accounting** (precedent QA-110 v1.0 R-2): the in-session rerun is a process deviation that consumes check 21's one ordinary rerun. No further attempt is needed, because the check is accepted.

**R-5 — I-1 is a security and process incident in the executing session, not a defect of the evidence or of any S-requirement.**
- Fact (results v1.2 §7): about 23:20Z, a malformed shell line in the executing session printed the workstation's values of `HD_API_KEY`, `GEO_API_KEY`, `HD_API_BASE_URL` and `DATABASE_URL` into that session's transcript.
- This contradicts Glow QA Guide §3.5.7 ("keep values off process argument lists and out of conversations, logs, files and commits") and the `AGENTS.md` redaction rule.
- No repository file, commit or published primary contains a value (the executor's `NO_HIT` scans; §4's pattern scan). The production service's values were not printed.
- The Product Owner decided not to rotate (PO-QA100-4) and directed prevention. A PreToolUse guard hook was installed on the workstation, outside the repository, and later narrowed after one false positive (results v1.3 §5).
- Decision: no check decision changes, because the evidence is untouched. I-1 goes to QA-120's RCA as an incident with its cause, the Product Owner's risk acceptance (owner: the Product Owner) and the prevention in place. Whether the transcript itself needs handling is the Product Owner's.

## 6. Observations (non-gating)

| ID | Observation | Owner |
| :- | :- | :- |
| O-9 | `build_commit` `9479d28` in the deployed identity is an older commit, not the deployed code's; recorded, never judged (Plan check 16; HDE Build Notes 2.19 judges by `release_id`) | Record only |
| O-10 | The "final LF no" label in the body headers of checks 16 to 19 is a display flag; the recorded bytes include one final LF (§3) | Record only |
| O-11 | Plan v1.3's state-(b) guards exclude two of `AGENTS.md`'s eight CI-exempt storage prefixes. That is R-4's planning defect. No Plan change is needed now, because every check has run | Kronos (Plan author), for QA-120's RCA |
| O-12 | Path-proof timestamps: every HDE-CRD-0002 proof carries `produced_at_utc` `2026-09-22T14:25:29Z` (O-2). On republication the writer keeps the earlier `mtime_utc` (O-5), for example check 21's proof `23:51:51Z` against its header `00:00:03Z`. The validators accept both, and `AGENTS.md` "Path-proof portability" treats `mtime_utc` as provenance, not correctness. Check 21 recorded them, as collection v1.3 asked | Kronos, for QA-120 (S22 context) |
| O-13 | On the service host, the sink holds three events until the container is replaced. On the workstation: Railway CLI 5.71.0, the `glow-workstation` key, the trusted host key and the guard hook; `/tmp/hde-crd-0002-evidence` and `/tmp/hde-crd-0002-qa` until this review is read; four leftover OPS03 directories (O-7) | Product Owner |

## 7. CANON_CONFLICT_REGISTER (carried)

Held in full in Plan v1.3 §13 and carried unchanged. QA-110 adds none: R-4's cause is a defect in this change's Plan under undisputed canon.

| ID | Status | Decision owner | Bearing here |
| :- | :- | :- | :- |
| CR-1 to CR-3 | `APPROVED_AS_CHANGED` | Thoth | None |
| CR-4 | `APPROVED` | Product Owner | None |
| CR-5 | `APPROVED_AS_CHANGED` | Product Owner | None |
| CR-6 | `APPROVED`, alternative (a) | Implementation Agent through RS-20 | None |
| CR-7, CR-8 | `APPROVED`, alternative (a) each | Product Owner | None |
| CR-9 | `PROPOSED`, unreviewed | Isis, IA-30 boundary | Applied by check 16 as interim (a): the six WU-OPS-01 paths consumed by reference |
| CR-10 | `APPROVED`, alternative (a) | Isis, ESC-40 | Publication (the `crd_id` key) |
| CR-11 | `APPROVED_AS_CHANGED`, alternative (a) | Isis, QA-70 review v1.0 | R-4's delta capture lives in the primary, not under `00_meta/` (Plan Templates "Moon Loop allowed (bounded)" names `00_meta/delta/`, which a CRD root cannot index) |
| CR-12 | `APPROVED`, alternative (a) | Product Owner, 2026-10-25 | None further |

## 8. Unresolved items and owners

| Item | Owner | State |
| :- | :- | :- |
| Final QA Report and RCA for the complete run (Plan §11 verdict criteria; R-3, R-4, R-5, O-9 to O-13; the hosted CI results still in progress) | Kronos, QA-120 | Next |
| I-1 risk acceptance (no rotation) and the transcript | Product Owner | Decided (PO-QA100-4); transcript handling open |
| CR-9 | Isis, IA-30 boundary | `PROPOSED` |
| O-1 (OPS03 `EXDEV`), O-A, D-1/LR6-O1, FND-028 | As review v1.1 §8 records them | Unchanged |
| G-1, the close representation of S01; PO-2 and PO-5 drainage; O-3, O-4 | As HDE Build Notes 2.28 records them | Unchanged |
| Cleanup of O-13's residual state | Product Owner | Open |

## 9. TypeSafe reading for the receiving session (QA-120)

Action sent (v8.2): "As the continuing QA authority, write the final QA report and a separate root-cause analysis for one change request whose whole approved QA plan of 21 checks has now run, with every step decision already recorded in three evidence reviews: reconcile all four task collections, results and reviews against the plan's 21 requirements and two tested source states, report coverage, evidence commits, environments, the one escalated failure and its merged remedy, deviations, incidents and unresolved risks, decide PASS or FAIL against the plan's written verdict criteria, and route to the closure retrospective. It is a Markdown record only; no code runs and no live call is repeated; an independent closure decision follows."

The reading as printed by the script:

- **TypeSafe v8.2: Opus 5.5 at extra high.** Effort score 3.30 (confidence 0.51); rung probabilities low 0.01, medium 0.03, high 0.10, extra high 0.40, max 0.45, ultracode 0.01. Model probabilities Fable 5.1 0.05, Opus 5.5 0.79, Sonnet 5.5 0.15, Haiku 5.5 0.01 (confidence 0.72). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.001, Fable 5.1 at medium 0.002, Fable 5.1 at high 0.005, Fable 5.1 at extra high 0.020, Fable 5.1 at max 0.023, Fable 5.1 at ultracode 0.001, Opus 5.5 at low 0.008, Opus 5.5 at medium 0.024, Opus 5.5 at high 0.079, Opus 5.5 at extra high 0.316, Opus 5.5 at max 0.356, Opus 5.5 at ultracode 0.008, Sonnet 5.5 at low 0.002, Sonnet 5.5 at medium 0.004, Sonnet 5.5 at high 0.015, Sonnet 5.5 at extra high 0.060, Sonnet 5.5 at max 0.068, Sonnet 5.5 at ultracode 0.002, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.001, Haiku 5.5 at extra high 0.004, Haiku 5.5 at max 0.005, Haiku 5.5 at ultracode 0.000. Flags: boundary between extra high and max. Sent 2026-10-26T00:13:34Z. Nathan picks the cell.
- **Detail (as printed):** v8.2 sent 2026-10-26T00:13:34Z; HTTP 200 in 0.55 s; 5476 input and 71 output tokens; jev-1.13.0. Rung by rule: extra high (nearest to the score, halves up); model by rule: Opus 5.5 (the most probable of the four options, a tie going to the higher-priced model). Flags: boundary between extra high and max.
- **Which request:** the installed TypeSafe scoring skill's request v8.2 and `score_v8.py`, run once with session kind `review` and label "QA-120 HDE-CRD-0002 final QA report and RCA (Plan v1.3, 21 checks)", before this review was saved.
- **Records:** the Notion row was not written.
- **Picks:** QA-120: Nathan's pick is not stated. This QA-110: Nathan's pick is not stated; its readings were not taken (QA-100 results v1.2 §10 and v1.3 §7: "TypeSafe: not read", HTTP 403 in the executor's local venue).

**Surface advice.**
- **Session.** QA-120 in the continuing Kronos session for HDE-CRD-0002 (https://claude.ai/code/session_01PnD4YNbFZStRQWZ7TCM6jV) on `amthorn78/glow-hdengine-v2`, with Notion read access for the QA-120 prompt and the CL-C-10 intake it names.
- **Reads.**
  - The three QA-110 reviews (v1.0 to v1.2), the four collections (v1.0 to v1.3), the four QA-100 result sets (v1.0 to v1.3) and the manifest on `main`.
  - Plan v1.3 §2, §10 and §11.
  - The Specification v1.1-approved with delta 01, the whole-change Implementation Plan and its lineage, and the QA-10 Reality Audit and Change Audit Triage, as QA-120's inputs list them.
- **GitHub read** for the two hosted runs still in progress at this review (§4).
- **No access needed:** production, Railway, the vendor or the database; no execution.
- **Writes:** only the QA Report, the RCA, a checkpoint and the handoff under `docs/ephemeral/`, by pull request.

## 10. Nonclaims

This review accepts six step results and records three rulings. It establishes no whole-change QA `PASS`, acceptance, Live QA sign-off beyond check 20's bounded call, closure, deployment, release activation, broad HumanDesignAPI v2 conformance, or PF09 or PF30 movement. It changes no product, test, generator, governed artifact or PF file. The pre-push tool's result and hosted CI are not QA verdicts.

## Canon relied on

Read on `main` at `bb931733`; `docs/pfcanon/` last changed by `21141b39` and unchanged since review v1.1. This branch edits no `docs/pfcanon/` file.

| Decision topic | Sources read | Applied in |
| :- | :- | :- |
| Review contract and routing | QA-110 — Review QA Evidence and Route the Next Action — 100926.1 (page state 2026-10-12T02:29:41.377Z; read in full at review v1.1 in this session): "Required QA evidence indexing", "Required Canon relied on block", Execute rules 1 to 6, "Required result and routing"; QA-120 — Create Final QA Report and RCA — 100926.1 (page state 2026-10-12T02:29:51.614Z), read in full at this invocation as the receiver's contract | §1, §5, handoff |
| Moon Loop and its boundaries | PF19-Canon-Glow-QA-Guide v3.0.6 §3.4.8, read in full at this invocation (Moon Loop; hard boundary; allowed actions; non-QA-root remediation boundary; evidence posture; stop condition); PF27-Canon-Plan-Templates v2.0.5 "Moon Loop allowed (bounded)" and "Bounded step-level rerun posture", read in full at this invocation | R-4 |
| Status classification | PF27 v2.0.5 "Exact status predicates" and "Causal precedence" (read at QA-110 v1.0 and QA-80 in this session; unchanged); Plan v1.3 §7 rules A and B and each check's Outcomes line | §3, R-4 |
| Normalization | QA-110 prompt "QA operation semantics and evidence"; PF19 §3.4.7 (as review v1.0 read it) | R-3, NZ-32 |
| Secrets and the incident | PF19 v3.0.6 §3.5.7, read in full at this invocation ("keep values off process argument lists and out of conversations, logs, files and commits"; presence `SET`/`UNSET` only); `AGENTS.md` redaction rule | R-5 |
| Live vendor call | Plan v1.3 check 20 (from HDE CLI/API/Vendor Ref §7.1.11b to §7.1.11f; Glow QA Guide §3.5.5 to §3.5.7, as the Plan cites them) | §3 check 20 |
| Deployed identity and probes | Plan v1.3 checks 16 to 19 (Glow QA Guide §3.5.2, §3.5.10; HDE-Mechanics Guide §14, as the Plan cites them); HDE Build Notes 2.19 (judged by `release_id`) | §3 |
| Evidence admission and indexing | Plan v1.3 check 21, §5.4 to §5.6; `AGENTS.md` "Path-proof portability" and "Code review scope" (the eight CI-exempt prefixes) | §4, R-4, O-11, O-12 |
| Precedents | HDE Build Notes v13.8 addendum 2.28 (QA-110 v1.0 R-1 and R-2) | R-4 |

In-flight documents read in full: QA-100 results v1.2 and v1.3; collection v1.3; collection v1.2 §1 to §5; the six primaries; Plan v1.3 checks 16 to 21 (this author's own). Read in part: QA-100 checkpoint and handoff v1.3; the manifest.

## Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | GCFPE-USE-HDE-CRD-0002-QA-110-20261026-03 |
| change | CRD HDE-CRD-0002 (Specification v1.1-approved with delta 01) |
| unit | QA Plan v1.3 checks 16 to 21 (Step-0C; S02, S10, S14, S19, S22); tasks T16 to T21, attempt 1 |
| prompt | QA-110 — Review QA Evidence and Route the Next Action — 100926.1, page state of 2026-10-12T02:29:41.377Z |
| release | GCFPE-20261009.1 / 100926.1 |
| role/stage | Kronos, QA-110 (`ACCEPT`; run complete; next QA-120) |
| capture time | 2026-10-26T00:25:00Z |
| execution identity | https://claude.ai/code/session_01PnD4YNbFZStRQWZ7TCM6jV (no worker subagents) |
| earlier uses | GCFPE-USE-HDE-CRD-0002-QA-110-20261025-01 and -02 (reviews v1.0 and v1.1); GCFPE-USE-HDE-CRD-0002-QA-90-20261025-03 and -05 (collections v1.2 and v1.3); GCFPE-USE-HDE-CRD-0002-QA-100-20261025-04 and -20261026-06 (results v1.2 and v1.3); each in its artifact |
| task/result/review mapping | T16 to T20 → results v1.2 §3.1 to §3.5 → this review §3 (`ACCEPT` each); T21 → results v1.3 §2 → this review §3 and R-4 (`ACCEPT`) |
| repository persistence | PENDING / NON_GATING (`docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent on `main`); owner: the authorized repository writer when the procedure is installed |
