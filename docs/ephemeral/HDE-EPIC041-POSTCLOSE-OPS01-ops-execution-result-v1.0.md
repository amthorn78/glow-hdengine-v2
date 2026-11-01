---
artifact_type: OPS_EXECUTION_RESULT
artifact_id: HDE-EPIC041-POSTCLOSE-OPS01-OPS-EXECUTION-RESULT
artifact_version: "1.0"
result_state: "COMPLETE. Attempt 1 PASS, with one Product Owner-authorized override of step S's literal outcome (section 7). Evidence published in the pull request that carries this result."
CHANGE_CLASS: EPIC
CHANGE_ID: HDE-EPIC041
OPS_UNIT_ID: HDE-EPIC041-POSTCLOSE-OPS01
OPS_TASK_ID: "HDE-EPIC041-POSTCLOSE-OPS01 v1.1 (docs/ephemeral/HDE-EPIC041-POSTCLOSE-OPS01-compat-open-rails-v1.1.md, sha256 f7a5bce6c056232e2258ee7d002b17a2e718051a7425f5878897b4fba03d97fc, read from main at 9de411bf)"
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
authorizing_principal: Nathan (Product Owner)
executor: "PO-delegated agent: Claude Code, Opus 5.5 (claude-opus-5-5) at max effort, local session on the Product Owner's Linux machine"
delegation_ref: "claude-code session 4db3135f-52ec-4bb5-beec-352094b804c0 (local session; no URL exists)"
evidence_root: audit/ops/hde-epic041/postclose-ops01/
run_window_utc: "2026-11-01T20:11:18Z to 2026-11-01T20:14:07Z"
created_at: 2026-11-01T20:24Z
---

# HDE-EPIC041-POSTCLOSE-OPS01: full compat test under open rails, execution result v1.0

## 1. Result

**PASS.** Every predicate of the task held on the first attempt, with one exception. Step S's secret scan printed `secret_scan=LEAK` because its header-text check matched the engine's own redacted header names. No secret value, or any fragment of one, appears in the evidence. Under the Product Owner's standing instruction for this run ("override any nits with authority") and HDE Governance §3.4, the executor classified the match as not secret-bearing and kept the files (section 7). Read literally, the task would have given `FAIL_TOOLING` and deleted the only record of the two production writes.

What the run showed:

* **Part V, live vendor compat through `hdctl`.** Five `showcompat --source vendor` runs produced well-formed compat results and Reader v1 bytes from live HumanDesignAPI v2 charts. Two runs of the same pair gave identical bytes, AB and BA gave identical bytes, and the two pairs gave different results.
* **Part W, two synthetic stored people.** SYN-A and SYN-B were missing from production. Each was stored with one row through the engine's write path, and its read-back matched.
* **Part D, the deployed service.** Production serves the release on `main` and gives a two-person compat answer for SYN-A and SYN-B in v1 and v2, identical in both orders. That answer matches the CLI's answer for the same birth data in all ten categories. The v1 bytes are identical, including the idempotence hash. Both governed error answers returned their codes.
* **Part C, closed rails.** The vendor command refused before any I/O.

## 2. Task, authority and timing

* **Task.** HDE-EPIC041-POSTCLOSE-OPS01 v1.1, an Ops task prompt, run as written from `docs/ephemeral/HDE-EPIC041-POSTCLOSE-OPS01-compat-open-rails-v1.1.md` on `main` at `9de411bf` (sha256 `f7a5bce6…7fd97fc`). HDE-EPIC041 stays closed; this is the separate full compat test the Product Owner directed on 2026-11-01.
* **Authorization.** The prompt asks for two exact lines in the Product Owner's message. He could not paste text into this surface, so he gave the sign-off as follows:
  * at 2026-11-01T20:07:23Z, he answered a question that stated "picking an option counts as both sign-off lines", choosing "Run it, with writes (Recommended)";
  * at 20:07:19Z, he wrote "I can't paste anything here. just run with writes. override any nits with authority".
  * The executor treats these as both lines: `Authorized: HDE-EPIC041-POSTCLOSE-OPS01 v1.1` and `Authorized writes: HDE-EPIC041-POSTCLOSE-OPS01 v1.1 Part W, SYN-A and SYN-B only`.
* **Accepted risk.** With the write line, the Product Owner accepts the risk the prompt states and leaves unverified: no check was made that no production consumer lists stored HD Engine people to users. It is still unverified.
* **Model and reasoning setting.** The prompt's TypeSafe v8.2 reading was Fable 5.1 at max, with a model near tie with Opus 5.5. The Product Owner ran the task on Opus 5.5 at max effort.
* **Timing.** Preflight ran from 20:06Z to 20:10Z (section 4). The run started at 20:11:18Z and was sealed at 20:14:07Z.
* **Evidence publication.** The prompt leaves the landing of the evidence to the Product Owner.
  * At 20:18:54Z he asked for this report: "give me a fill report as an md file in docs/ephemeral".
  * At 20:19:29Z he directed "you can also commit all other evidence as you suggested". The suggestion was `audit/ops/hde-epic041/postclose-ops01/`, through a pull request, and this is that pull request.

## 3. Tested state

| Identity | Value |
| :- | :- |
| `main_sha` (fresh clone) | `9de411bf699fe84dc8b492781380761652ed27d4` |
| `local_release_id` | `77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e` (release 1.3.0, the value the prompt expected) |
| `deployed_release_id` | `77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e`, equal to `main` |
| `deployed_build_commit` | `9479d28`, a static constant and not the deployed commit (finding F-5) |
| `hdctl_version` | `hdctl 0.0.0 (hdengine@prod;77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e)` |
| Deployed `/internal/version` | `engine_tag` `hdengine@prod`; `invocation_tag` `INV-f2ac55d77ce9aacc`; `invocation_sha256` `3f119e72…2c6e69`; `emitter_sha256` `c828effe…09bc19` |
| Interpreter | CPython 3.12.15, the version CI uses, in a fresh venv |

The CLI ran `main` at `9de411bf`. The deployed service's own commit is unknown, because `/internal/version` carries no build identity beyond the static constant. Its release identity equals `main`'s.

## 4. Environment

* **Venue.** The Product Owner's Linux machine (kernel 7.0.0-38-generic), running `bash`, `git`, `curl` and Python 3.12.15. The prompt allows "any Linux shell meeting the environment contract in section 4"; this was not Codespaces.
* **Credentials.** All credential names were present: `HD_API_BASE_URL`, `HD_API_KEY`, `GEO_API_KEY` and `DATABASE_URL` were `SET`, and `HDAPI_BASE_URL` was `UNSET`.
  * The vendor base ends in `v2`.
  * `DATABASE_URL` is a PostgreSQL connection string whose host is on Railway's public proxy. That is the external connection string the prompt requires, not the Railway-internal host.
  * Only presence and these classifications were recorded; no value was printed or stored.
* **Profile and rails.** The machine's environment profile was `open`. Step 0 exported `LC_ALL=C LANG=C TZ=UTC APP_ENV=dev SAFE_MODE=1 ALLOW_NETWORK=0 PYTHONDONTWRITEBYTECODE=1` in the run shell. Rails were then opened only by prefix on each vendor command, and never exported open.
* **Network preflight, added by the executor.** Before step 0, plain TCP connections opened to the vendor host, `glow-hdengine-v2-production.up.railway.app:443`, the database host and `github.com:443`, and all four succeeded. The executor checked this because the task forbids retries. No request was sent, so this is not a vendor acquisition or a production request.
* **One shell session.** The agent's shell does not keep state between commands, so the run used one persistent `bash` process. It read each block's file name from a named pipe and sourced the block, so variables, functions, the working directory and the venv carried over as in one terminal. Commands in a block read stdin from `/dev/null`.

## 5. Steps and predicates

| Step | Exit or HTTP | Predicate | Outcome |
| :- | :- | :- | :- |
| 0.1 presence | none | three vendor names `SET`, `HDAPI_BASE_URL` `UNSET`, base ends in `v2` | PASS |
| 0.2 clone, install, identity | `pip_exit=0`, `release_check_exit=0` | both 0, tree clean | PASS (`tree_clean=yes`) |
| C closed rails (`c0`) | 1 | exit 1, 0 stdout bytes, stderr exactly `PROVIDER_REFUSED` | PASS |
| V `p1_ab_1` | 0 | exit 0, empty stderr | PASS |
| V `p1_ab_2` | 0 | exit 0, empty stderr | PASS |
| V `p1_ba` | 0 | exit 0, empty stderr | PASS |
| V `p2_ab` | 0 | exit 0, empty stderr | PASS |
| V `p2_ba` | 0 | exit 0, empty stderr; `V-run complete` | PASS |
| E1 bad location (`e1`) | 1 | not 0, empty stdout, one uppercase token | PASS (`PROVIDER_ERROR`) |
| V-check | `check_exit=0` | `CHECK_FAILS=0` | PASS |
| W.1 probe SYN-A | 404 | 200 and ineligible (present), or 404 `ERR_M10_PERSON_UNRESOLVED` (missing) | missing |
| W.1 probe SYN-B | 404 | same | missing |
| W.2 store SYN-A | 0 | `ok`, `mapped`, UUID, `rows_after=1`, `rows_written` 1 or 0, `read_back_match=True` | PASS (`rows_written=1`) |
| W.2 store SYN-B | 0 | same | PASS (`rows_written=1`) |
| D1 `/internal/version` | 200 | 200 | PASS |
| D2 Reader v1, SYN-A then SYN-B | 200 | 200 | PASS |
| D3 Reader v1, SYN-B then SYN-A | 200 | 200 | PASS |
| D4 Reader v2, SYN-A then SYN-B | 200 | 200 | PASS |
| D5 Reader v2, SYN-B then SYN-A | 200 | 200 | PASS |
| D6 `?v=3` | 400 | 400, `ERR_READER_INVALID_VERSION` | PASS |
| D7 `{"a_id":"not-a-uuid"}` | 422 | 422, `ERR_READER_INVALID_INPUT` | PASS |
| Check D | `check_d_exit=0` | `CHECK_D_FAILS=0` | PASS |
| S secret scan and seal | none | `secret_scan=CLEAN` | printed `LEAK` from header text only; not secret-bearing (section 7) |

The overall classification follows the prompt's section 7. Every listed predicate is met, with S classified as described, so the result is PASS.

## 6. Compat results

The two `bands:` lines from `check.txt` and the two deployed lines from `check_d.txt`, verbatim:

```text
p1_ab_1 bands: harmony=Cool heat=Cool communication=Cool alignment=Open comfort=Cool consistency=Open expansion=Open creativity=Cool drive=Open balance=Cool
p2_ab bands: harmony=Open heat=Cool communication=Cool alignment=Cool comfort=Cool consistency=Cool expansion=Cool creativity=Cool drive=Cool balance=Cool
deployed_v2 bands: heat=Cool harmony=Cool communication=Cool alignment=Open comfort=Cool consistency=Open expansion=Open creativity=Cool drive=Open balance=Cool
reader_cli_parity=MATCH
```

The table also gives the scores from the CLI compat results. These are internal compat output, not the public Reader, which carries bands only:

| Category | P1 (CLI) score and band | P2 (CLI) score and band | Deployed v2, SYN-A and SYN-B |
| :- | :- | :- | :- |
| harmony | 10 Cool | 32 Open | Cool |
| heat | 22 Cool | 13 Cool | Cool |
| communication | 10 Cool | 20 Cool | Cool |
| alignment | 32 Open | 0 Cool | Open |
| comfort | 10 Cool | 22 Cool | Cool |
| consistency | 27 Open | 3 Cool | Open |
| expansion | 25 Open | 0 Cool | Open |
| creativity | 20 Cool | 0 Cool | Cool |
| drive | 40 Open | 10 Cool | Open |
| balance | 0 Cool | 8 Cool | Cool |

* **Result identity.** Schema `magic10_compat_result.v1`, `config_id` `m10-channel-state-v1.0.0`. The pair key is `8ade82e2…974d161` for P1 and `85709b17…635cbfa6` for P2.
* **Reader v1.** The CLI's P1 Reader v1 bytes (`p1_ab_1.reader.json`) and the deployed v1 bodies for SYN-A and SYN-B in both orders (`d2_v1_ab.body`, `d3_v1_ba.body`) share sha256 `6dc0de34…061f57e`. The idempotence hash `5aa45444…8114b8` and the invocation tag are identical. P2's Reader v1 bytes have sha256 `83944ffc…4989daa`.
* **Reader v2.** The deployed v2 bodies are identical in both orders: sha256 `08796881…68137651`, idempotence hash `900724a0…8eee1398`.

## 7. The secret scan and the step S override

* **What step S printed.** `HEADER_TEXT_FOUND` and `secret_scan=LEAK`. No `SECRET_FOUND` line was printed for `HD_API_KEY`, `GEO_API_KEY`, `HD_API_BASE_URL` or `DATABASE_URL`, so no full value is present.
* **What matched.** Only `w_store_a.out` and `w_store_b.out`, the JSON `hdctl bg:resolve` printed, with seven matches each. Every match is in the engine's redacted request-posture fields: `header_posture` (`Authorization: Bearer <redacted>`, `HD-Geocode-Key: <redacted>`) and `route_auth_posture` (`Authorization: Bearer <redacted>`). The base URL is also `<redacted>`, and every header value is the literal `<redacted>`.
* **Fragment check.** After step S, the executor scanned all 36 evidence files, the console log and the pip log for pieces of each secret, recording counts only. There were zero hits for any of these:
  * the `DATABASE_URL` value, password, user name and host;
  * the `HD_API_BASE_URL` value and host;
  * the full value, first 12 characters and last 12 characters of `HD_API_KEY` and `GEO_API_KEY`.
* **Classification.** The match is not secret-bearing:
  * HDE Governance §3.4 permits open-rails evidence to record "key names, redacted values, header names, redacted header-shape posture". It makes the result `FAIL_TOOLING` when "secret-bearing output is persisted", which did not happen.
  * Hard rule 5 ("never save request or response headers from the vendor") is not breached. These fields are the engine's redacted posture summary, not vendor headers.
* **The override.** The Product Owner authorized overriding procedural mismatches for this run, so step S's literal `LEAK` outcome was overridden. Nothing was deleted, edited or resealed.
  * `S_CLASSIFICATION_NOTE.txt`, written by the executor at 20:16Z, records this classification beside the evidence. It is not run output and is not listed in `SHA256SUMS`.
* **Without the override.** The prompt's literal rule gives `FAIL_TOOLING`, withholds the evidence and deletes the two `w_store_*.out` files.

## 8. Findings

* **F-1. Release identity.** There is no mismatch: the deployed `release_id` equals `main`'s, so production serves the release on `main`.
* **F-2. Reader and CLI parity.** `reader_cli_parity=MATCH` in all ten categories.
  * The stored pair binds UUIDs, while the CLI derives identities from birth data. Even so, the Reader v1 bytes are identical, including the idempotence hash (section 6).
* **F-3. E1 token.** `PROVIDER_ERROR`. An unresolvable location came back as the generic typed provider error, with no location-specific code. The predicate requires only a single uppercase token, so this is an observation, not a failure.
* **F-4. Synthetic people.** Neither SYN-A nor SYN-B was stored before the run. W.2 stored both, each with `status=ok`, `rows_before=0`, `rows_after=1`, `rows_written=1` and `read_back_match=True`:

  | Person | UUID | Adapter | Payload posture | Route | `canonical_sha256` |
  | :- | :- | :- | :- | :- | :- |
  | SYN-A | `9cff60ae-6eb6-5618-aec5-8acaa4f290d2` | `ADAPTER_MAPPED`, `ChartResult`, `mapped` | `adapter_mapped_no_raw_vendor_payload` | `adapter_backed_v2_chart`, resource `charts`, family `recommended_v2_chart` | `99c5c02ab5d666dfe99b6f94d22fea90a86d70dbb44aa6553807ab4ff33e627c` |
  | SYN-B | `57f0c055-ff09-5fdb-aedb-def880437e6f` | `ADAPTER_MAPPED`, `ChartResult`, `mapped` | `adapter_mapped_no_raw_vendor_payload` | `adapter_backed_v2_chart`, resource `charts`, family `recommended_v2_chart` | `489bfaa66e28e14f6097d78c1393b17c60c458978cd5d95cef3dc03f55e7e1b5` |

  The database provider was `psycopg` and the vendor HumanDesignAPI v2. The rows are permanent QA fixtures; the prompt says not to delete them.
* **F-5. `build_commit` does not identify the deployed code.**
  * `/internal/version` returns `build_commit` `9479d28`. That value is the static constant `"build_commit": "9479d28"` in `_STATIC_IDENTITY` in `engine/runtime/identity.py`, in place since HDE-EPIC038 PR-01 (#346, 2026-07-12).
  * Commit `9479d28` itself is "EPIC-005: add resilient start_web.sh for Railway" (2025-10-25), 1,362 commits behind `main`.
  * The CLI built from `main` carries the same constant. The field therefore cannot show which commit production runs, and this run compared deployed identity by `release_id` only.
  * This is reported, not classified as a defect; the owner of the runtime identity contract can decide whether it needs a change.
* **F-6. Step S scan.** This is the header-text match and override described in section 7.

## 9. Counts

| Count | Value | Limit |
| :- | :- | :- |
| Vendor acquisitions (upper bound) | 14: 10 in V, 2 in E1, 2 in W.2 | 14 |
| Production HTTP requests | 9: 2 in W.1, 7 in D | 10 |
| Retries | 0 | 0 |
| `hdctl` commands with `DATABASE_URL` set | 2 W.2 writes, plus `hdctl --version` in step 0.2, which returns before any I/O (prompt finding P-3) | the W.2 writes only |

E1 is counted as two acquisitions, as the prompt's counter does. The vendor may have served fewer, because party B's location could not be resolved.

## 10. Writes and side effects

* **Before.** `hde.body_graphs` had no row for SYN-A or SYN-B: both W.1 probes returned 404, and W.2 reported `rows_before=0`.
* **After.** Each has one row, written through the engine's write path. The production Reader now answers for the pair: D2 to D5 returned 200 and eligible.
* **Not changed.**
  * The database apart from those two rows: no other write and no delete.
  * The repository, until the pull request that carries this result.
  * PF canon, Notion and the board.
  * The Railway service's configuration and deployment.
* **Rails.** Exported closed at step 0 and opened only by per-command prefix.
* **Residue on the Product Owner's machine.**
  * The run directory, kept: `/home/nathan/hde-compat-ops01-20261101T201118Z`. It holds the clone at `main`, its venv, `pip.log`, `ev/`, `SHA256SUMS`, the classification note, and the two checker scripts the prompt writes.
  * The executor's driver files in its session scratchpad.

## 11. Evidence

* **Where.** `audit/ops/hde-epic041/postclose-ops01/` holds 38 files: the 36 files the run wrote to `ev/`, the run's `SHA256SUMS`, and `S_CLASSIFICATION_NOTE.txt`.
* **Copy check.** Each file was copied unedited, and `cmp` shows all 38 identical to the run directory.
* **Not landed.** The checker scripts `check.py` and `check_d.py` are not in the evidence; they are verbatim in the prompt (block 6 and block 9). `pip.log` is not landed either.
* **Seal.**
  * `SHA256SUMS` has digest `910f965ced2fdf5a6fc5caaa562741e891fdfd0f791168e78f4d4787ec8f8293`, and 35 of its 36 entries verify in the repository path.
  * The exception is `run.log`. Step S computes `SHA256SUMS` and then appends two lines to `run.log`: the digest and the finish time.
  * `run.log` without its last two lines matches the sealed entry `e632184c9b97c89e29736d630bb02acaf17b72d98c13dc31da19c2ad038b724a`. Its final bytes have the sha256 in the table below. Nothing changed after the seal except those two lines, which the prompt itself writes (prompt finding P-2).
* **Path proofs and index.** None, and no Evidence Index or Mirror row, following the earlier Ops evidence landing in #704 (section 15).

Inventory of the landed bytes:

| File | Bytes | sha256 |
| :- | -: | :- |
| `SHA256SUMS` | 2849 | `910f965ced2fdf5a6fc5caaa562741e891fdfd0f791168e78f4d4787ec8f8293` |
| `S_CLASSIFICATION_NOTE.txt` | 1353 | `60d896dbb70fd9e92dabba062f3b23cbbb09d6f55869dcc6e41a9ef00943b31e` |
| `c0.err` | 17 | `b8737c9a84643ae05848cbcb176e4298e6d0f56f1e3246e9fea9fee5c99bec57` |
| `c0.out` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `check.txt` | 326 | `500284ee2359f0838cc2fe14795d308a4a0bb925a6a1675b3a062c8fbe5efd02` |
| `check_d.txt` | 316 | `7f971bfb0aa831df3f70ff9895d9b77bf369957b89ea56776cbe627844ecd47a` |
| `d1_version.body` | 347 | `c9302e7072138482c1363f66c58606b45faac476a07235772d06ca581bc0f06a` |
| `d2_v1_ab.body` | 330 | `6dc0de34576262f093e4a1aeb1b7f0512fa1062021b8cd5b0e2e4527e061f57e` |
| `d3_v1_ba.body` | 330 | `6dc0de34576262f093e4a1aeb1b7f0512fa1062021b8cd5b0e2e4527e061f57e` |
| `d4_v2_ab.body` | 621 | `08796881417c7b46e77f060f045cca24203ee12d770fa2faa79edd6e68137651` |
| `d5_v2_ba.body` | 621 | `08796881417c7b46e77f060f045cca24203ee12d770fa2faa79edd6e68137651` |
| `d6_bad_version.body` | 100 | `0e6e1929248ac37bdb5b0bbc1ad1fb655b5737030d24d886b9b643036da41fd5` |
| `d7_bad_body.body` | 94 | `c5eb83aec246444fe5d207f14e089b28d2cafc35c5d84ff49bc719b01c37b27a` |
| `e1.err` | 15 | `f5718842ffc0c550ca25be48fc5d32a8c39883cf862018575739c6798f889987` |
| `e1.out` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `p1_ab_1.err` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `p1_ab_1.out` | 3302 | `1b08d323bc52696d8376c46079921b640793a89af00cdb4f5204bf664f46ff10` |
| `p1_ab_1.reader.json` | 330 | `6dc0de34576262f093e4a1aeb1b7f0512fa1062021b8cd5b0e2e4527e061f57e` |
| `p1_ab_2.err` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `p1_ab_2.out` | 3302 | `1b08d323bc52696d8376c46079921b640793a89af00cdb4f5204bf664f46ff10` |
| `p1_ab_2.reader.json` | 330 | `6dc0de34576262f093e4a1aeb1b7f0512fa1062021b8cd5b0e2e4527e061f57e` |
| `p1_ba.err` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `p1_ba.out` | 3302 | `1b08d323bc52696d8376c46079921b640793a89af00cdb4f5204bf664f46ff10` |
| `p1_ba.reader.json` | 330 | `6dc0de34576262f093e4a1aeb1b7f0512fa1062021b8cd5b0e2e4527e061f57e` |
| `p2_ab.err` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `p2_ab.out` | 3292 | `87a361f9aa994c63577e07d0d9cb59358bc36822fa597f4f65733ca465b6edac` |
| `p2_ab.reader.json` | 330 | `83944ffcc5db810e9c5db9b21374f1bd44e85ac3664bfcff0ebd29fbc4989daa` |
| `p2_ba.err` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `p2_ba.out` | 3292 | `87a361f9aa994c63577e07d0d9cb59358bc36822fa597f4f65733ca465b6edac` |
| `p2_ba.reader.json` | 330 | `83944ffcc5db810e9c5db9b21374f1bd44e85ac3664bfcff0ebd29fbc4989daa` |
| `release_check.txt` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `run.log` | 4487 | `ff114df4088a467f146966089138d70f9a64bf08dba81182e4dd45215731d925` |
| `w_probe_a.body` | 92 | `8ad84a2a8259e71662100669c44502ac01699508a0729ee1a33b105c3e58847c` |
| `w_probe_b.body` | 92 | `8ad84a2a8259e71662100669c44502ac01699508a0729ee1a33b105c3e58847c` |
| `w_store_a.err` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `w_store_a.out` | 1574 | `534b9fbcd57fa21a8be63f5828e79e5c72cd3c2f5246d308292e5ddf0a1908ef` |
| `w_store_b.err` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `w_store_b.out` | 1574 | `7e66478346790fcb23208dba89a640a1fd92d28709edb21ce226895bf6fc3c64` |

The ten empty files are part of the record. Each `.err` file of a successful command is empty, as are `c0.out` and `e1.out`, the empty stdout the predicates require, and `release_check.txt`, because the release check printed nothing.

## 12. Command ledger

The ten bash blocks of prompt v1.1 were extracted by their fences, from the file as read from `main`, and sourced unchanged:

| Block | Step | Prompt lines | sha256 |
| :- | :- | :- | :- |
| b01 | 0.1 | 129 to 138 | `f45ca661bfca95246e2ee7192daeadfe3d87f70135262623962ae6b0776cd950` |
| b02 | 0.2 | 149 to 157 | `0084ecb760fa3804ac67a2d4a67797f329b8e4b31fea1e9fdc10bffaabdaeab0` |
| b03 | C | 169 to 172 | `feb8bb36a3cd6a6a07b7cd8734b0ad2971d83e8005b42a83ba89e6228e017939` |
| b04 | V-run | 180 to 200 | `c235c04c175bbed3e27de3040c05ac6d583dca348178a258d9e9174b0f774722` |
| b05 | E1 | 208 to 210 | `afd8fa9c84fe003def08447b1a38877f93b84d5bc3f766fc6d3789dd3841ae60` |
| b06 | V-check | 221 to 276 | `aa0340490dffb17c2211c9792f4a62af39a878df5caafa489eefa914b2db6ab5` |
| b07 | W.1 | 288 to 301 | `e36061f3095ae78b47424c644ec1bf423f35852c0099d534114d9145e35bcd30` |
| b08 | W.2, as written (lines commented out) | 314 to 324 | `df4c3741d74a96de73980edca0d023b0ebe97cd20a00f3749c630f1383d4d2de` |
| b08a | W.2, the function and the SYN-A line uncommented | from b08 | `9b97ce9240af010c0e94e633402d18a940fa5932b7848c093c76c2a90d7a4497` |
| b08b | W.2, the SYN-B line uncommented | from b08 | `2eaff5d316f9700178a603c7949864f24afcf4c740a4ab2b00bd7f3a1ec4f63e` |
| b09 | D | 347 to 396 | `c503386843af470f3c1b43c530b687d3352dd5f777e1f31a5752c0ce7e5afc9f` |
| b10 | S | 414 to 421 | `4c8e649b79a31c5b36edfc1e3e7c41be2ff85f28cb21dccea1ab76b8367e1223` |

W.2 differs from the block as written only in the step the prompt asks for: "uncomment only the lines you need". Both probes showed 404, so both lines were needed. They ran as two blocks, SYN-A and then SYN-B, so a failure on SYN-A would have stopped the run before SYN-B.

The commands as executed, expanded:

```bash
# C (b03)
env -u DATABASE_URL SAFE_MODE=1 ALLOW_NETWORK=0 hdctl showcompat --source vendor \
  --birthdate-a 1990-01-01 --birthtime-a 12:00 --location-a "Amsterdam, Netherlands" \
  --birthdate-b 1985-07-15 --birthtime-b 08:30 --location-b "London, United Kingdom"
# V (b04) and E1 (b05): each through the prompt's v() function as
env -u DATABASE_URL SAFE_MODE=0 ALLOW_NETWORK=1 hdctl showcompat --source vendor <party flags> \
  --dump-reader "$EV/<name>.reader.json"
#   p1_ab_1, p1_ab_2: A=1990-01-01 12:00 Amsterdam, Netherlands; B=1985-07-15 08:30 London, United Kingdom
#   p1_ba:            A=1985-07-15 08:30 London, United Kingdom; B=1990-01-01 12:00 Amsterdam, Netherlands
#   p2_ab:            A=1992-03-21 18:45 New York, United States; B=1978-11-02 04:10 Sydney, Australia
#   p2_ba:            A=1978-11-02 04:10 Sydney, Australia; B=1992-03-21 18:45 New York, United States
#   e1:               A=1990-01-01 12:00 Amsterdam, Netherlands; B=1985-07-15 08:30 Zzqx Synthetic Nowhere 000
# W.2 (b08a, b08b): with DATABASE_URL set, through the prompt's w() function
SAFE_MODE=0 ALLOW_NETWORK=1 hdctl bg:resolve --user 9cff60ae-6eb6-5618-aec5-8acaa4f290d2 --source vendor \
  --birthdate 1990-01-01 --birthtime 12:00 --location "Amsterdam, Netherlands" --upsert
SAFE_MODE=0 ALLOW_NETWORK=1 hdctl bg:resolve --user 57f0c055-ff09-5fdb-aedb-def880437e6f --source vendor \
  --birthdate 1985-07-15 --birthtime 08:30 --location "London, United Kingdom" --upsert
# W.1 (b07) and D (b09): through the prompt's h() and post() functions, base https://glow-hdengine-v2-production.up.railway.app
curl -sS --max-time 30 -o "$EV/<name>.body" -w '%{http_code}' -X POST -H 'Content-Type: application/json' \
  --data '{"a_id":"<uuid>","b_id":"<uuid>"}' "$BASE/api/reader?v=<1|2|3>"
#   w_probe_a: SYN-A, SYN-A, v=1   w_probe_b: SYN-B, SYN-B, v=1
#   d2: SYN-A, SYN-B, v=1   d3: SYN-B, SYN-A, v=1   d4: SYN-A, SYN-B, v=2   d5: SYN-B, SYN-A, v=2   d6: SYN-A, SYN-B, v=3
curl -sS --max-time 30 -o "$EV/d1_version.body" -w '%{http_code}' "$BASE/internal/version"
curl -sS --max-time 30 -o "$EV/d7_bad_body.body" -w '%{http_code}' -X POST -H 'Content-Type: application/json' \
  --data '{"a_id":"not-a-uuid"}' "$BASE/api/reader?v=1"
```

## 13. Deviations and limitations

Deviations. Each is procedural and none changes a command's arguments, inputs or a predicate's test:

* **DV-1. Venue.** The Product Owner's local shell, not Codespaces. The prompt allows this.
* **DV-2. Interpreter.** `python3` was pointed at CPython 3.12.15, the version CI uses, because the machine's default `python3` is 3.14.4. Both meet the prompt's "3.11 or later". The prompt's commands are unchanged.
* **DV-3. One persistent shell.** The blocks were sourced into one persistent shell through a named pipe, with stdin from `/dev/null` (section 4).
* **DV-4. Sign-off.** The authorization came as a question answer and a message instead of pasted lines (section 2).
* **DV-5. Preflight.** TCP-only reachability checks and credential classification were added before step 0 (section 4).
* **DV-6. W.2 in two blocks.** The needed lines were uncommented and run one person at a time (section 12).
* **DV-7. Step S.** Its literal outcome was overridden, and a classification note was added beside the evidence (section 7).

Limitations:

* **L-1. Scope.** The run proves only what it exercised (section 16).
* **L-2. Deployed commit.** The deployed service's commit is unknown (F-5).
* **L-3. Acquisition count.** The vendor acquisition count is an upper bound (section 9).
* **L-4. Consumer risk.** The risk the Product Owner accepted with the write line is still unverified (section 2).

## 14. Prompt findings, for any later version of this task

Each was observed in this run and applies only to the prompt's text:

* **P-1. The secret scan matches redacted fields.** Step S's header pattern (`bearer |hd-api-key:|hd-geocode-key:|authorization:`) also matches the engine's redacted `header_posture` and `route_auth_posture` fields in `bg:resolve` output. Any run that executes W.2 therefore prints `LEAK` with no secret present. A version that ignores matches followed by `<redacted>`, or scans for secret values only, would avoid this.
* **P-2. `run.log` never verifies.** Step S writes `SHA256SUMS` and then appends two lines to `run.log`. Sealing last, or sealing `run.log` separately, would fix this.
* **P-3. Step 0.2 contradicts hard rule 2.** It runs `hdctl --version` with `DATABASE_URL` set, while the rule says every `hdctl` command other than W.2 runs with it unset. This is harmless: `cli()` in `engine/cli/main.py` returns on `--version` before any other work.
* **P-4. The sign-off gate assumes paste.** The prompt expects the Product Owner to paste exact lines into the execution surface. In this Claude Code surface he could not.
* **P-5. One shell session.** "Run the blocks in order, in one shell session" assumes an interactive terminal. An agent shell needs a persistent process to keep state between blocks.
* **P-6. `deployed_build_commit` is not a deployed identity.** The prompt reports it as one, but it is a static constant (F-5).

## 15. Not in this result

* Evidence Index and Mirror rows, and path proofs, for this Ops root. HDE Governance §3.4 asks for records-only Machine Mirror entries for the closed-rails refusal proof and for open-rails conformance runs, with their redaction checks. Registering them needs a roster change in the canonical updater (`tools/evidence/update_evidence_index.py`) and its owner tests, as IDX-01 did for HDE-EPIC041's QA evidence. That is a separate change for the Product Owner to direct. The earlier Ops landing in #704 also carried none.
* **Conjunction** (`hdctl showcompat --conjunction`) and the compat-determinism generator. Both are out of scope by the prompt's section 8.
* Any decision on F-5 (the static `build_commit`) or on the prompt findings P-1 to P-6.

## 16. Nonclaims

* **Scope.** This result proves only the behavior it exercised: live vendor compat through `hdctl` at `main` `9de411bf`, the storage of the two synthetic people, and the deployed Reader's answers for them.
* **What it does not establish.** No QA verdict, acceptance, PF09 movement, deployment, release activation or closure. It also establishes no full HumanDesignAPI v2 conformance, no conjunction behavior and no public Reader change.
* **Evidence class.** This is Ops evidence (HDE Governance §3.4), and HDE-EPIC041 stays closed.
* **CLI-local runs.** The CLI-local vendor runs are not deployed-service validation (Glow QA Guide §3.5.5). Part D checked the deployed service without vendor traffic.
* **Merging.** Merging this result preserves the record and approves nothing.

## 17. Canon relied on

Read on `main` at `9de411bf`; `docs/pfcanon/` was unchanged since `5a046cb2`, where the prompt's author read it.

* **HDE Governance §3.4, "Open rails (controlled)".** The executor relied on these parts:
  * "HDAPI v2 open-rails vendor proof posture", including the evidence bundle and `FAIL_TOOLING` conditions;
  * "Production-functional epic live-proof requirement";
  * "Route-family proof is not workflow proof";
  * the secret-safety paragraph, which permits redacted header-shape posture;
  * "Controlled vendor-backed no-user validation", including "Preflight and execution classification" and "Evidence-output posture".
* **Glow QA Guide §3.5.5, "PO Live QA sessions (vendor-first rails)".** A CLI-local vendor smoke is not deployed-service validation.
* **Glow Infrastructure §2.7.** The production target names, "CLI-local vendor smoke target distinction" and "Any-shell terminal access".
* **HDE Build Notes, addendum 2.1, D-1.** The production vendor override is decided to cover `showcompat`. It does not gate this run's `APP_ENV=dev` shell.
* **AGENTS.md.** Closed-rails defaults, the redaction rule, QA output placement, and "Evidence attribution, currentness and distinct decisions".
* **Code read for findings.**
  * `engine/runtime/identity.py`, for F-5;
  * `engine/cli/main.py` (`cli()`, the `--version` path), for P-3;
  * `engine/bodygraph/ingest.py` (`SYNTHETIC_USER_ID_MAP`), for the two registered UUIDs.
