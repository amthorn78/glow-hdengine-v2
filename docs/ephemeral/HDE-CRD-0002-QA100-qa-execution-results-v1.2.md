---
artifact_type: QA_EXECUTION_RESULTS
artifact_id: HDE-CRD-0002-QA100-QA-EXECUTION-RESULTS
artifact_version: "1.2"
predecessor: docs/ephemeral/HDE-CRD-0002-QA100-qa-execution-results-v1.1.md (task T13-RV1; reviewed by QA-110 v1.1; unchanged)
change_class: CRD
change_id: HDE-CRD-0002
change_name: "Post-HDE-EPIC040 Repair: Carried Defects, Code Security Review, Pre-Push Check and Close-Pack Writer"
stage: QA-100 — Execute Bounded QA Task — 100926.1
state: RESULTS_RETURNED_TO_QA110
author: Kronos as executor, by the Product Owner's arrangement (collection v1.2 §4.1); Claude Code CLI session on the Product Owner's workstation, local session 5c9c7c47-41bd-437a-a9ee-63879dec618b (no URL); the same session authored collection v1.2
invocation_binding: CRD / HDE-CRD-0002 / QA-100 / QA_PLAN v1.3 checks 16 to 20, tasks T16 to T20, attempt 1 each
context_conflict: "Collection v1.2 was executed before its pull request merged, by Product Owner direction in this session (\"just proceed\"); the executed text is the PR head blob pinned below"
execution_posture: MANUAL_PROMPT_EXECUTION
prompt: QA-100 — Execute Bounded QA Task — 100926.1 (https://app.notion.com/p/3f44590a05eb8182a201f0e177dad431; page state 2026-10-12T02:30:45.204Z; read in full at this invocation)
ecosystem_release: GCFPE-20261009.1 (100926.1)
task_collection: docs/ephemeral/HDE-CRD-0002-QA90-qa-task-collection-v1.2.md (TASK_READY; SHA-256 39d374bde3bb4d4d6ed2a6ac7b04fe293e28853d4ed38f2be9b3385831d77251; on branch docs/20261025-qa90-t16-t20, amthorn78/glow-hdengine-v2#743, open at execution)
approved_base: docs/ephemeral/HDE-CRD-0002-QA50-qa-plan-v1.3.md (blob 3aea6033e3c0; SHA-256 30f4a83cfa62276523c6bad5222f521cdf361eed8ebe59408387b24e8c2ec35a)
approving_review: docs/ephemeral/HDE-CRD-0002-QA70-qa-plan-review-v1.4.md (APPROVE)
qa_audit: docs/ephemeral/HDE-CRD-0002-QA50-qa-audit-v1.0.md (AUDIT_COMPLETE)
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.8.md (SHA-256 439775924392a206ceffb70952b0af1975c24d4214fc73d4ed98fcf94220e13c)
tested_target: the deployed production service glow-hdengine-v2 (release_id 77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e; container 60f93a3e5923 for check 20)
evidence_checkout: /tmp/hde-crd-0002-evidence at main 463cbbefd36c8fdfa92470156586d35931245cb6 (state (b) code), branch qa/hde-crd-0002-t16-t20-evidence
evidence_commits: ee7b8d9c (check 16), 7ede02ba (checks 17 to 19), c4c868ff (check 20); this record set in a following commit; pushed
routing: QA-110 — Review QA Evidence and Route the Next Action — 100926.1, Kronos
PF10_ADDENDUM_OUTPUT: NOT_PRODUCED_BY_QA-100
created_at: 2026-10-25T23:40:00Z
---

# HDE-CRD-0002 — QA-100 execution results v1.2: tasks T16 to T20 (QA Plan v1.3 checks 16 to 20)

## 1. Result

| Task | `check_id` | State | Published status | Attempt |
| :- | :- | :- | :- | :- |
| T16 | `qa-16-deployed-identity` | `COMPLETE` | `PASS` | 1 |
| T17 | `qa-17-deployed-not-found` | `COMPLETE` | `PASS` | 1 |
| T18 | `qa-18-deployed-dev-surfaces` | `COMPLETE` | `PASS` | 1 |
| T19 | `qa-19-deployed-reader-input` | `COMPLETE` | `PASS` | 1 |
| T20 | `qa-20-live-vendor-override` | `COMPLETE` | `PASS` | 1 (one allowed invocation used) |
| — | `qa-21-evidence-admission` | not in collection v1.2 | not published | — |

All five members of collection v1.2 ran and were published. No state is an acceptance or a QA PASS for the change. Two items need Kronos at QA-110: gap G-1 (check 16's header timestamp) and incident I-1 (§7).

## 2. Identity, venue and environment

- **Executor:** Kronos (this session), by the Product Owner's arrangement. **Initiator of check 20's V1 and V2:** the Product Owner, who typed both commands with the `!` prefix in this session. Attestation, verbatim: "I, Nathan, the Product Owner, typed and ran V1 and V2 myself".
- **E-P (checks 16 to 19):** the Product Owner's workstation shell; curl 8.18.0 at `/usr/bin/curl`, Python 3.12 (`python3`), git 2.53.0; Production binding `SAFE_MODE=0 ALLOW_NETWORK=1 APP_ENV=prod LC_ALL=C LANG=C TZ=UTC` exported in the shell. The readiness reads are in each primary.
- **E-V V-B (check 20):** the production service shell of `glow-hdengine-v2` (project `ample-illumination`, environment `production`) through Railway CLI 5.71.0 `railway ssh`, working directory `/app`, interpreter `/app/.venv/bin/python` (Python 3.13.16), actor `root`, container `60f93a3e5923` throughout.
- **Publication:** `/tmp/hde-crd-0002-evidence` under the default closed rails, venv `/tmp/hde-crd-0002-evid-venv` (CPython 3.12.15, CI's install; `engine` resolves inside the checkout); helper SHA-256 `8bfbde7cdddfa79cdcbc568096c1f4e8acff23e45c28ee665de12e8ba016b0ae`.

## 3. QA_EXECUTION_RESULTs

### 3.1 T16 `qa-16-deployed-identity` — COMPLETE, `PASS`

Executed 2026-10-25T23:18:11Z to 23:18:12Z. Steps 1 to 4: `200 1.1` each; every response `Cache-Control: no-store`, `Content-Type: application/json; charset=utf-8`, no `ETag`, no `Last-Modified`; HEAD `Content-Length` 347 equals step 1's body length. Step 5: `True True True True True 347`; `release_id` the candidate; both `cmp` silent. Step 6: `GET /internal/version False`, `HEAD /internal/version False`. Step 7: 5 of 5 `OK`, `classification PASS`, class `MATCH`. The six consumed WU-OPS-01 digests equal the collection's values (CR-9 interim (a)). `build_commit` `9479d28` recorded, not judged (O-9). 36 predicates, all PASS. Secret scan `NO_HIT` (4 names compared).

### 3.2 T17 `qa-17-deployed-not-found` — COMPLETE, `PASS`

r1 to r7 `404`, r8 (`DELETE /internal/version`) `405` with `Allow: GET, HEAD, OPTIONS`; all HTTP/1.1, `application/json; charset=utf-8`, `no-store`, no `ETag`; every body except HEAD's exactly the `ERR_NOT_FOUND` envelope plus LF; HEAD body not observable with `curl -I` (recorded, as in check 16). 48 predicates, all PASS. Secret scan `NO_HIT`.

### 3.3 T18 `qa-18-deployed-dev-surfaces` — COMPLETE, `PASS`

d1 `GET /reader?v=1` and d2 `HEAD` `403` (`ERR_READER_FORBIDDEN`); d3 to d6 `403` (`ERR_WRITER_FORBIDDEN`); d7 to d9 `404` (`ERR_NOT_FOUND`); all JSON, `no-store`, no `ETag`, HTTP/1.1. Observations, no predicate: o1 `OPTIONS /dev/sampler/conjunction` `200 text/html` with `Allow: HEAD, OPTIONS, GET` (the router's answer, LR5-O1); o2 `GET //reader?v=1` `403` `ERR_READER_FORBIDDEN`. 53 predicates, all PASS. Secret scan `NO_HIT`.

### 3.4 T19 `qa-19-deployed-reader-input` — COMPLETE, `PASS`

Bodies: `b1.json` 32,768 bytes (SHA-256 `a90ff70ad51360979071d268065d422fdea638d17ee71a1dd76d12f4e71578b1`), `b2.json` 20,008 bytes (`cdf9cd5993ce58f7834953703ae6cbaafab44980601489b357435db76c6874d0`). q1 (`v=1`, b1), q2 (`v=2`, b1), q3 (`v=1`, b2) each `422`, `ERR_READER_INVALID_INPUT` envelope plus LF, JSON, `no-store`, no `ETag`. 18 predicates, all PASS. Secret scan `NO_HIT`.

### 3.5 T20 `qa-20-live-vendor-override` — COMPLETE, `PASS`

- **Preflight (23:25:23Z to 23:25:34Z):** P1 `/app/engine/__init__.py` and `hdctl 0.0.0 (hdengine@prod;77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e)`; P2 the three vendor names `SET`, `HDAPI_BASE_URL` `UNSET`, `P2_ENGINE_ENV=OK`; P3 exactly the Production binding; P4 sink `/root/.local/state/glow-hdengine/vendor_prod_override.jsonl`, all four reads `True`/`False` as required, `LINES=0`, directory created `drwx------` (NZ-24); P5 `root`.
- **V1 (23:30:01Z, typed by the Product Owner):** exit 1; `status` `error`, `PROVIDER_PROD_OVERRIDE_REQUIRED`, `outbound_attempted` `false`; product stderr 0 bytes; one sink line `refused`, `authorization_ref` `null`. Gate A1 held; V2 allowed.
- **V2 (23:31:07Z, typed by the Product Owner):** exit 0; `status` `ok`; route family `recommended_v2_chart`, resource `charts`; adapter `mapped`, `ChartResult`; payload posture `adapter_mapped_no_raw_vendor_payload`; `rows_written` 0; header posture `Authorization: Bearer <redacted>`, `HD-Geocode-Key: <redacted>`, no `HD-Api-Key`; product stderr 0 bytes.
- **Sink:** three lines in all; the second and third share correlation ID `5ef25d3a-79a0-43c5-885a-e4f879ea4607` (`allowed`, then `completed` with `outbound_attempted` `true`); 16 keys each; actor `root`; no user key, birth data, location, URL or header text.
- **Secret scan in the service (A3):** `NO_HIT` (4 names, 3,815 characters). Local scan of the assembled body: `NO_HIT`.
- 32 predicates, all PASS. Script digests: `v1.sh` `b3c9f473e830aba5a27a3df3e8e223f5245fa8ab270db724bafa93774f3faf55`, `v2.sh` `90b7b6cc12ea92fc02d1f99dae11e6bf4e2ad4634e6f82a62a78994810e9c9ff`.

## 4. Normalizations applied

NZ-01, NZ-06 (all five); NZ-25 (T17 to T19); NZ-20 to NZ-24 (T20), as collection v1.2 §4.10 defines them. Each is recorded in its spec's `command_provenance` and its primary's notes.

## 5. Publication, indexing and receipt

| `check_id` | Primary bytes | Primary SHA-256 | Blob | Index key and Mirror row |
| :- | -: | :- | :- | :- |
| `qa-16-deployed-identity` | 14,792 | `daad275072310b5aace1e726234d618f02c5cdaa26ebc2a732c129c08cacbdac` | `e6b4b7f7c14d` | present, present |
| `qa-17-deployed-not-found` | 15,793 | `27258d4a7b1d1969dab693f1b257287f0ce1a023744021dfe9333b5ccf2db3eb` | `264b7c60ac95` | present, present |
| `qa-18-deployed-dev-surfaces` | 19,984 | `63fe7da715fc16c6f0e9d9246d56cfcda4581565d3cbddaecf2056f67a48856b` | `6862e9bef091` | present, present |
| `qa-19-deployed-reader-input` | 8,929 | `7c4cc490ccf4933851fd4a46efc0d98c2716955979eadb0e01a45e80d08b6412` | `5eb3a2cf00d0` | present, present |
| `qa-20-live-vendor-override` | 26,905 | `5e96be9bd026172770b15a691fe18de415e13fb8907442dc09aaa99882bf1ed1` | `eb8d8d8744f3` | present, present |

- Each call printed `PUBLISHED` with the primary and manifest paths. After each, the six read-only validators (`update_evidence_index.py --check`, `orientation_demo.py --check`, `validate_evidence_paths.py`, `check_mirror_schema.sh`, `check_lf_endings.py`, `validate_crd_check_family`) exited 0; the family grew 16, 17, 18, 19, 20.
- Final receipt after check 20: `validate_crd_check_family` lists 20 checks, `qa-01-preflight` to `qa-20-live-vendor-override`, every manifest status `PASS`. Manifest `audit/qa/hde-crd-0002/qa_step_logs_manifest.json` 3,161 bytes, SHA-256 `ec129099c6e45b2899c484babd4d6ace81278c1aa620728ad3dbda38b5c7d221`.
- Commit boundary (grant, collection §4.8): the three evidence commits touch only `audit/qa/hde-crd-0002/**` and the ten updater-owned graph files; this record set adds only `docs/ephemeral/` files. No other path, no merge, no force-push.

## 6. Product Owner decisions in this session

| ID | Decision | Effect |
| :- | :- | :- |
| PO-QA100-1 | "run checks 16-20"; "do not do 21, you won't be able to with open rails" | Selection narrowed to 16 to 20 |
| PO-QA100-2 | Check 20 at V-B with the Railway CLI ("install the railway CLI and do it properly"); initiator the Product Owner; evidence-only commit grant | Collection v1.2 §4.1, §4.8 |
| PO-QA100-3 | "just proceed" | Collection v1.2 executed before PR 743 merged |
| PO-QA100-4 | No credential rotation after I-1 ("Option 3"); "make sure this doesn't happen again, however you can" | I-1 recorded; guard installed (§7) |

## 7. Deviations, gaps and incidents for QA-110

- **G-1, check 16 header timestamp (assembly gap).** The T16 spec carried `captured_at_utc` `2026-10-25T23:40:00Z`, a value typed during assembly that is later than the check's actual finalization (requests ended 23:18:12Z; the primary was written at 23:23:10Z, its path proof's `mtime_utc`; evidence commit 23:23:23Z). The published header's `timestamp_utc` is therefore 23:40:00Z. Every validator accepts it; no predicate depends on it. The bodies of checks 17 to 20 cite it as a label. Kronos decides: keep with this record, or republish `qa-16-deployed-identity` by `check_id` from the preserved body (`/tmp/hde-crd-0002-qa/qa-16-deployed-identity/body.txt`) with the true time, an assembly correction rather than a rerun (Plan §5.4). Checks 17 to 20 carry their real finalization times.
- **I-1, secret values printed into this session's conversation (incident; not evidence).** At about 23:20Z, during T16's local secret scan, a malformed shell line (an `export $(<command>)` substitution that reduced to a bare `export`) printed the workstation environment, including the values of `HD_API_KEY`, `GEO_API_KEY`, `HD_API_BASE_URL` and `DATABASE_URL`, into the session transcript. It contradicts Glow QA Guide §3.5.7 ("keep values off process argument lists and out of conversations, logs, files and commits"). No repository file, commit or published primary contains a value: every primary scanned `NO_HIT`. The Product Owner decided not to rotate (PO-QA100-4). Remedy in place: a PreToolUse hook `~/.claude/hooks/block-env-dump.py`, registered in `~/.claude/settings.json`, denies bare `export`/`env`/`printenv`/`set`/`declare -x`, `export $(<command>)`, `/proc/*/environ` and `echo $<secret>` before they run; proven to fire. The workstation's values are not shown to be production's; the production service's values were never printed.
- **O-9 (carried from collection §2.4):** `build_commit` `9479d28` is an EPIC-005 commit, not the deployed code's commit; never judged.
- **Observation:** an initiator keystroke `bash /tmp/` ran before V1 against the local directory only; it reached no service and used no invocation.

## 8. Residual state, cleanup and resume point

- Deleted: `/tmp/hde-crd-0002-qa16` to `-qa19`; the container's `/tmp/hde-crd-0002-qa20`.
- Kept until QA-110 has read this record: `/tmp/hde-crd-0002-evidence`, `/tmp/hde-crd-0002-qa` (helper, specs, bodies, check 20 captures and scripts).
- On the service host: the sink file holds three events (append-only), until the container is replaced.
- On the workstation and the Product Owner's accounts: Railway CLI 5.71.0, the `glow-workstation` key, the trusted host key, the permission rule and the I-1 hook.
- Resume point: none within collection v1.2; all members ran. Next: QA-110.

## 9. Carried lineage and CANON_CONFLICT_REGISTER

Carried unchanged from Plan v1.3 §13 through collection v1.2 §6: CR-1 to CR-3 `APPROVED_AS_CHANGED` (Thoth); CR-4 `APPROVED`, CR-5 `APPROVED_AS_CHANGED`, CR-7 and CR-8 `APPROVED` (Product Owner); CR-6 `APPROVED` (RS-20); CR-9 `PROPOSED`, unreviewed (Isis, IA-30), applied by T16 as interim (a); CR-10 `APPROVED` (Isis, ESC-40); CR-11 `APPROVED_AS_CHANGED` (Isis), applied by T20 (primary only); CR-12 `APPROVED` (Product Owner). QA-100 adds none.

## 10. TypeSafe reading for the receiving session (QA-110)

Action sent (v8.2): "As the continuing QA authority, review the evidence returned for five already-executed bounded QA tasks of one change request: four read-only probe checks of the deployed production service and one mandatory live vendor call made under open rails in the production service shell, each published as one evidence log through the canonical writer. Verify each result against its written predicates, the evidence family's index and manifest registration and the read-only validators, record an accept or escalation decision per check in one Markdown review, and route the next stage; one selected final evidence-admission check remains unissued. No code runs and no live call is repeated; a later final QA report follows."

- **TypeSafe: not read.** As printed: "TypeSafe v8.2: not read (HTTP 403 after 2 attempt(s), sent 2026-10-25T23:34:00Z). Do not fill in a reading by hand."
- **Which request:** the installed skill's request v8.2 and `score_v8.py`, session kind `review`, label "QA-110 HDE-CRD-0002 review of T16 to T20 (QA Plan v1.3 checks 16 to 20)". Notion row not written.
- **Picks:** QA-110 and this QA-100: Nathan's pick is not stated.

**Surface advice.** QA-110 needs GitHub read of the evidence pull request and of PR 743 (the collection), and the repository; no production, Railway or vendor access. It can run in this workstation session or any Claude Code session on `amthorn78/glow-hdengine-v2`. Reads: this record; the five primaries; the manifest; collection v1.2 (PR 743 head); Plan v1.3 checks 16 to 20.

## 11. Nonclaims

These results establish no whole-change QA PASS, acceptance, Live QA completion beyond check 20's bounded call, deployment, release activation, broad HumanDesignAPI v2 conformance or closure. Check 21 is not run. Execution authority is not acceptance authority.

## Canon relied on

The QA-100 prompt (read in full); PF19-Canon-Glow-QA-Guide v3.0.6 §3.5.5, §3.5.6, §3.5.7, §3.5.10; PF05-Canon-HDE-CLI-API-Vendor-Ref v2.5.3 §7.1.11e and §7.1.11f; PF27-Canon-Plan-Templates v2.0.5 status predicates; HDE Build Notes v13.8 (2.11, 2.19, 2.27, 2.28). In-flight: approved Plan v1.3, the QA-70 reviews v1.4 and v1.2 (N-201), collection v1.2, the WU-OPS-01 Ops task §13.

## Provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | GCFPE-USE-HDE-CRD-0002-QA-100-20261025-04 |
| change | CRD HDE-CRD-0002 (Specification v1.1-approved with delta 01) |
| unit | Plan v1.3 checks 16 to 20; tasks T16 to T20, attempt 1 |
| prompt | QA-100 — Execute Bounded QA Task — 100926.1, page state 2026-10-12T02:30:45.204Z |
| release | GCFPE-20261009.1 / 100926.1 |
| role/stage | Kronos as executor, QA-100 |
| capture time | 2026-10-25T23:40:00Z |
| execution identity | Claude Code CLI session 5c9c7c47-41bd-437a-a9ee-63879dec618b (no URL; no subagents) |
| earlier uses | GCFPE-USE-HDE-CRD-0002-QA-90-20261025-03 (collection v1.2, this session) |
| task/result mapping | T16 to T20 → checks 16 to 20 → this record → QA-110 pending |
| repository persistence | PENDING / NON_GATING (`docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent on `main`) |
