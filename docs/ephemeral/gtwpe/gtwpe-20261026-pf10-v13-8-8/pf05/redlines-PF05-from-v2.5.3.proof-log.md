# Proof log — redlines-PF05-from-v2.5.3.md (T-PF05 preparation)

This is the processing report for the redlines file `redlines-PF05-from-v2.5.3.md` in this directory. It records how the file was made, from which sources, what was verified and what is left. It establishes no PF change, canon adoption, QA verdict, acceptance or closure.

## 1. Artifact, outcome and identity

| Field | Value |
| :---- | :---- |
| Artifact | `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/pf05/redlines-PF05-from-v2.5.3.md`, package revision 2; 23,808 bytes; SHA-256 `f5224bb704bd94bdf7df496a6ee35df3e31d8f6bc13acd1cac6ffc354ae24b9e` |
| Preparation outcome | `READY` |
| Save completeness | `COMPLETE_PACKAGE` (receipt in §12) |
| Operations | 8: RL-01 to RL-04 and RL-06 to RL-08 `REPLACE`, RL-05 `INSERT`; terminated by `END OF REDLINES` |
| Prompt | TW-DRAIN-10 — Prepare PF Document Redlines — 100926.1, https://app.notion.com/p/3f44590a05eb8172a314fe6b958bb9ff; body fetched live on 2026-10-26 (page last edited 2026-10-09T11:05:22.094Z); version line `Prompt Version: 100926.1` |
| Authorization | Nathan's handoff "GTWPE 100926.1 T-PF05 document session (TW-DRAIN-10 then TW-APPLY-10)", sent 2026-10-26T21:08:28Z, which authorizes this preparation and then TW-APPLY-10 in this session. For revision 2: Nathan's direction in this session on 2026-10-26, "Don't run a whole new drain, just fix them in the current one", referring to the stale sentences in §4.1.6, §5.1.0 and §5.1.7 |
| Run identity | `gtwpe-20261026-pf10-v13-8-8 / T-PF05 / TW-DRAIN-10 / run 1`, package revision 2 (first run; no earlier T-PF05 output existed) |
| Revision history | Revision 1: 5 operations, redlines SHA-256 `bcc4c6061c07a292c777016f6a4a659c9f4824d03d04d28f42e8a1db2d853c15`, committed at `431661b` and applied at `e24e05f`. Revision 2 replaces it in place against the same baseline: RL-01 to RL-04 are unchanged byte for byte, RL-05's entry is widened, and RL-06 to RL-08 are added. Git history keeps revision 1 |
| Originating preparer | Claude Code cloud session https://claude.ai/code/session_01D49VTgmgq8kpkcN9WLDdAW; one session, no subagents and no reviewers, as the handoff directs |
| Ledger | `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/LEDGER.md`, task T-PF05, rows A07, A08, A09 (with X05) and S-APR |
| Preparation date | 2026-10-26 |

## 2. Turn preflight

1. **Task.** TW-DRAIN-10 preparation for one general PF, PF05, followed in this session by TW-APPLY-10. PF05 is not a PF09 volume, so TW-DRAIN-20 does not apply.
2. **Identities and access.** The target, PF10 and the HDE-CRD-0002 records were read from `origin/main` (§3). The prompt bodies were fetched live from Notion. No Google Drive, ChatGPT Library or memory copy was used.
3. **Selected scope.** PF10 v13.8.8 front matter (lines 1–223) and addenda 2.7, 2.8 and 2.9 in full; the Specification's approval block, phase blocks and "Canon, QA & Build Notes posture" (lines 147–193) with delta 01 C-8 to C-12; X05 (plan v1.0 §17, lines 701–739). Each was read to its boundary.
4. **Target reading.** PF05 read in full, lines 1–4439 (§4).
5. **Baseline currency.** At the start, `origin/main` was `0838ba08254eaefc888019df49a06aa2ae99cc6c`, the merge of #760 at 2026-10-26T21:18:51Z. `git diff --name-status 9dda63d 0838ba0` lists one added path, the ledger. PF05 and PF10 have the same blobs at both commits, so `main` carries no newer target version and the ledger baseline holds.
6. **Destination.** #760 had merged, so the handoff's continuation applies: `docs/20261026-gtwpe-pf10-v13-8-8-documents`. It did not exist at this session's first check. The T-PF07 document session then created it at `28184eab1a8ba36e6c4cec5d073acbb9d3db6e38` and opened shared draft PR #761 (2026-10-26T21:39:03Z). This session reuses that branch and PR and does not open another. That session has since recorded #761 on the ledger's continuation line; this session writes only the T-PF05 Completion cell.
7. **Posture.** Closed rails (`SAFE_MODE=1`, `ALLOW_NETWORK=0`). No vendor, production, database, Railway, TypeSafe or Drive access. No write to `docs/pfcanon/`.
8. **Revision 2.** Nathan directed the stale sentences reported as O-1 to be fixed in this run. While verifying them, the preparer found that the same sentences also carry a third stale claim: the legacy CLI proof failure, which S03 resolved by retiring the test. The editable scope therefore grows by three passages: §4.1.6 line 837, §5.1.0 line 2071 and §5.1.7 line 2253. The baseline, the target identity, the ledger rows and the held items are unchanged. `origin/main` was re-checked at `0838ba08254eaefc888019df49a06aa2ae99cc6c`.

## 3. Sources and inputs

Every repository file was read at `origin/main` `0838ba08254eaefc888019df49a06aa2ae99cc6c`.

| Ref | Role | Path | Blob | Bytes | SHA-256 | Read |
| :-- | :-- | :-- | :-- | --: | :-- | :-- |
| Target | PF05 v2.5.3, the original | `docs/pfcanon/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.3.md` | `8b136def4c22f8308169a1b0315086b3e90ead1d` | 323,966 | `65a9ad6e9d4e75cf50c4e0ae5ac6b3cbabce35bea759de9a6ef4c77549dd6352` | lines 1–4439, in full |
| SR1 | Change source: PF10 v13.8.8, effective 2026.10.26 | `docs/pfcanon/PF10-HDE-Build-Notes-v13.8.8.md` | `680b0accb0bdf260b0489d1a7385f90bb120cd99` | 729,539 | `f5e13efb5ab1354bda2f578ca69f41bed773160784602a896927bc091a254c2f` | 1–223 (front matter, precedence §1–§9, index); 688–889 (2.7); 890–1002 (2.8, including S02 met at line 933 and S07 met at line 937); 1003–1101 (2.9). Supporting for revision 2: 2.2 lines 266–272, 295 and 309–311 (the S03 base and its retirements) and 2.4 line 423 (S03 met) |
| RTL | Supporting for revision 2: the retired-test ledger | `tests/retired_tests.md` | `ea44b46262168fd5240451fe1e9da069c76e6a5e` | 19,110 | (repository evidence) | lines 1–12 (header: "HDE-CRD-0002 WU-PR-01 (S03)") and 60–66, including line 65 (`tests/reader_v1/test_cli_proof.py`, reason O-P06a-03, retired 2026-10-13, with replacing coverage) |
| SR2 | Change source: Specification v1.1, approved base | `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` | `c4802a5a7fa33db38d42d8a7f64679cd18b50480` | 43,151 | `fb412f178fa0ecae527704b16ced4be2c28e42a84e663ccbebdbdb669b7382df` | 140–200, covering S-APR (147–193) |
| SR3 | Overlay: Specification delta 01 | `docs/ephemeral/HDE-CRD-0002-specification-delta-v1.0.md` | `9408d6ed091bcba3d751fcb17ae392a1ceca8bbb` | 21,046 | `59ef9a776c6b5615333cfe68ba4d8145a3d1fe1fdd194b12bb24cf71a233b636` | 1–162, in full |
| SR4 | Delta approval | `docs/ephemeral/HDE-CRD-0002-specification-delta-review-v1.0.md` | `5a6cecc86f604a17aaa3e6c89b17183d2d0f9ffa` | 14,586 | `ee5b07d2fe1ee69e23fb0b78b489fde4885696eb7c1135e80a5a887e207ac169` | decision lines 8, 20, 32 (`DELTA_APPROVE`, 2026-10-21T18:36:00Z) |
| X05 | Supporting: WU-PR-04 plan v1.0 §17 | `docs/ephemeral/HDE-CRD-0002-WU-PR-04-pr-implementation-plan-v1.0.md` | `6baead456619af1e73e15ace1079380f5797ca85` | 92,216 | `229771af915ac7586273fe5adce6f6ea51355ed77e79240ea774ded0c2041101` | 695–745, covering 701–739 |
| X04 | Supporting: WU-PR-03 plan v2.0 §18, which 2.8 carries | `docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-implementation-plan-v2.0.md` | `1d6a92a483e238ea4a8144d44461bbbc81704e17` | 100,705 | `eb6ec79ac808a034be4dde2541b82c42eef56a3eb6da67bc56301cab180a75bc` | 750–795, covering §18 (753–792) and the §17 tally on line 751 |
| X01 | Supporting: drain-targets ledger | `audit/docdeltas/hde-crd-0002_drain_targets.md` | `ee5057acb06e852fd0cd3e83a4e98e23220141d4` | 3,589 | `61282f685a700893edc6e28fb9977b43627a9da0917f1dd37b3014a6dbc435a9` | lines 10 (CR-7 to §5.6), 14 (DD-04 to §7.1.11), 29–30 (FND-029, FND-012) |
| X10 | Specification approval | `docs/ephemeral/HDE-CRD-0002-specification-review-v1.1.md` | `c48f77a0c220d65455f50e3c550a283d0b332a0c` | 14,195 | `883e9bc88c85e7d83f706dc13966c0e194101b0f67fb50f7762c6e258ab9b871` | lines 8, 19, 31 (`INITIAL_APPROVE` by Thoth, 2026-10-12T19:39:51Z) |
| X11 | Closure decision | `docs/ephemeral/HDE-CRD-0002-CL-C-10-closure-decision-v1.2.md` | `2260eae17974336c0ff267b3b45fce71e3f1b1e1` | 31,910 | `03ff5cb718669766465ae3e78be5fbd01eee5da3c430909e3f4bf071e54d6ca5` | lines 18–20, 41–42 (`CLOSE`, `CHANGE_CLOSED`, 2026-10-26T16:40:00Z) |
| X12 | Post-closure record | `docs/ephemeral/HDE-CRD-0002-CL-20-post-closure-record-v1.0.md` | `ac60f368f6d928c0e87467ca93d826401b4d39cb` | 15,904 | `35c02b9aaf470f30f0ad92799c2e155162de35ae3858e06d4c3ca4a09aa659bb` | lines 74–77 (M-0 to M-3; M-0 is this drainage, pending) |
| X13 | Final QA Report | `docs/ephemeral/HDE-CRD-0002-QA120-qa-report-v1.0.md` | `d6cceaf3a019779e935eb2306300686beb3bf259` | 41,391 | `f31e2e077300ead2a7b89a84dda31fc235f3c28ae2d90f8c9b886f4f0fb09973` | lines 6, 41–46, 62, 96, 107, 127, 140, 249 (verdict `PASS`; checks 9 and 20 for S14; IR-1 actor `root`; IR-2 no showcompat vendor step) |
| X14 | Close report; content source for the limits in RL-03 | `audit/HDE-CRD-0002_close_report.md` | `0bbc8050d3c197bc2fef6371cdb7064739d4c507` | 40,914 | `47d29b5c6da63df5b67fa90a8b3eb42933fd1df357908053eca92f10f4e412ee` | line 37 (S14 met and its limitation); Deferrals section, 34 entries, including lines 116 (`CR-7`), 125 (`DD-04`) and 128 (`FND-012`) |
| PF03 | Editorial standard, Reference v1.8.8 | `docs/pfcanon/PF03-Reference-Technical-Writing-Best-Practices-v1.8.8.md` | `504712df548a02f3aa4e7b8c37027385e46a3878` | 43,953 | `df685f3a66aa18fdcacb697b340263cb59fc682564fa59c50b3d9b9ca735c462` | lines 1–633, in full |
| PF02 | Supporting: retired-route canon | `docs/pfcanon/PF02-Canon-HDE-Architecture-v2.4.6.md` | `b0bf3d66965d0de91044b519a29bc30b1cc2d040` | 140,533 | `4bfa53ad9775f6b69432b28ae11048b6458461249186c9bb9161e51e5ecb28db` | lines 953–956; title line |
| PF29 | Supporting: retired-route canon | `docs/pfcanon/PF29-Canon-HDE-Users-Guide-v1.0.2.md` | `6a0d4725a710bfe1289282729156e15cc8acfcce` | 72,066 | `36c3b1bdce884f902dce56650065bdbd26aa3dcb1da8954f62f2c38f83fd5601` | lines 105–111; title line |
| WI4 | Supporting: WU-PR-04 instruction, OBS-W4-1 to OBS-W4-4 | `docs/ephemeral/HDE-CRD-0002-WU-PR-04-pr-instruction-v1.0.md` | `51371eeae9d9c206866d386eee485ad94dbc3e78` | 73,805 | `60220ff7abe4d92934313e402482bb34d343e040f0cfff769b43b13dd1121ffc` | lines 540–548 |
| GS | Supporting: CL-40 gap scan | `docs/ephemeral/HDE-CRD-0002-CL-40-cycle-gap-scan-v1.0.md` | `d7c94739547f0aeb433d32adea4bf850313bbc9b` | 26,635 | `06d3ac4bc4d4b943857297d74008f558ebd93e3a662ca7eee67ae03005fb3927` | line 168 (OBS-W4-2 and OBS-W4-4 are canon points for the Product Owner) |
| Ledger | Routing only | `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/LEDGER.md` | `74944b261c0ebb2f80a416fb004b9a913da592d1` (equal at `13b64dddea4cfe0bb35e56c1833fbcd03af238c7` and on `main`) | 40,440 | `88e73039cfd4415a0de4d2cc83fda4893d5420cd188bde63f385c91b3c19e234` | in full, including "Precedence and closure controls" and "Held and deferred items" |
| SR5 | Repository controls | `AGENTS.md` | `7e358b4601d3f412b331d4b46184d3f3b24b7d04` | 61,057 | `1c802b8f767cd693805c25dd014ae81c36472242ab3e01c54f2d2073a4457f1b` | as session context; canon-first and canon read-only rules |

**Source roles.** SR1 and SR2 carry the changes; SR3 is read as the overlay of SR2, and none of its C-8 to C-12 changes touches the S14 drainage sentence (SR2 lines 172–176). X14 supplies the two recorded limits in RL-03. X01, X04, X05, WI4, GS, PF02 and PF29 are supporting reading only. X10 to X13 are approval and closure evidence. HDE-CRD-0002 is `CHANGE_CLOSED` (X11), so none of its changes is held on closure grounds. The ledger routes work and is not a change source.

**Supersession inside PF10 (front matter §5).** 2.18 withdraws the cost-ceiling passages of 2.11 to 2.16; 2.14 narrows 2.11 rules 7 and 8; 2.17 amends 2.15. None of 2.7, 2.8 or 2.9 is superseded, and none of their passages used here is a cost-ceiling passage. 2.11's misnumbered cross-references are not used. 2.8 records LR3-O1, the lost code spans for `dev` and `dev ` in 2.7, as a PF10 publication fact; it does not affect PF05.

## 4. Coverage

- **Target.** PF05 was read in seven contiguous ranges: 1–468, 469–1310, 1311–2132, 2133–2736, 2737–3524, 3525–4221, 4222–4439. Every range returned complete text, the last ending at the final rule and blank line. No truncation occurred.
- **Selected sources.** Each unit in §3 marked "in full" or by a boundary was read to that boundary, including its tables.
- **Canon-first search.** `git grep` on `origin/main` across `docs/pfcanon/` for `DD-04`, `allow-prod-vendor`, `HDE_VENDOR_OVERRIDE_AUDIT_PATH`, `canon-retired`, `PROVIDER_PROD_OVERRIDE`, `vendor_prod_override` and `governed clock boundary` found, outside PF05 and PF10, only HDE Users Guide line 979 (the stale §16 bullet; T-PF29's task), HDE Phased Epics line 11430 (the historical DD-04 row; X05 keeps it as history) and two unrelated live-deferral lines in the Separation checklist and the Glow QA Guide. A search of PF05 itself located every statement of the DD-04 status and the Catalog state: lines 125, 2577, 3500, 3605 and the historical v2.5.3 Change Log entry at line 4126. For revision 2, a search of PF05 for `HTML 404`, `stale showcompat help`, `describes Reader v1 bytes` and `test_cli_proof` found lines 837, 2071 and 2253 only.

## 5. Repository inspection (read-only, at `main@0838ba08254eaefc888019df49a06aa2ae99cc6c`)

**Endpoint Catalog (RL-02).**
- `docs/ENDPOINTS_CATALOG.json` is a symlink to `artifacts/audit/ENDPOINTS_CATALOG.json` (5,618 bytes; SHA-256 `85453d93f619e19cbc85984fec480a52ef0fbb13cc053ef834d6129333c22885`); `cmp` shows them equal.
- The file has top-level keys `endpoints` (18 records), `generated_at_utc` and `success_endpoints` (`[{"method":"GET","path":"/reader"}]`).
- The `GET /aux/narrative` record has `classification` `public_aux`, `internal` false, `env_gate` `not_applicable_public`, `a7_eligible` false and `aliases` `["/api/aux/narrative"]`.
- No record path matches `/ops/db/unavailable`, `/ops/probe/env` or `/ops/writer/diagnostic` (grep count 0). No record exists for `/internal/admin/bundle/v1`, and `grep` of `adapter/` and `engine/` finds no such route and no `admin-bundle` CLI command.
- `tools/evidence/generate_a7_transport_proofs.py` line 38 defines `CANON_RETIRED_PATHS` for the three paths, and line 87 raises `canon-retired route must not be cataloged` for a matching path or alias.
- `tests/http/test_endpoint_catalog.py` lines 100–164 assert one record or one reasoned exclusion per served pair. Its exclusion table holds 35 pairs, (a) 7, (b) 1, (c) 18 and (d) 9; with the 18 records that is 53 served pairs, the tally of X04 line 751. The three retired paths stay registered in `adapter/http_reader.py`.

**Production vendor override (RL-03).**
- `engine/cli/main.py` lines 52–59 and 231–293 hold the `--allow-prod-vendor` flag, its pre-scan and its usage messages.
- `engine/bodygraph/resolver.py` lines 73–103 hold `classify_vendor_environment`, and `_resolve_vendor` (lines 227–330) holds the rails, then classification (step 4), the matrix (step 5), actor and pre-I/O audit event (step 6) and route (step 7). The refusal codes are `PROVIDER_PROD_OVERRIDE_INVALID`, `PROVIDER_PROD_OVERRIDE_REQUIRED` and `PROVIDER_AUDIT_UNAVAILABLE`.
- `engine/bodygraph/vendor_audit.py` holds the 16 `AUDIT_FIELDS` and the sink key `HDE_VENDOR_OVERRIDE_AUDIT_PATH`. The default subpath is `glow-hdengine/vendor_prod_override.jsonl` under an absolute `XDG_STATE_HOME`, else `~/.local/state`. A relative path or one inside the repository is refused. The actor is `pwd.getpwuid(os.geteuid()).pw_name`. Each event is appended as one canonical JSON line (`sercanon`) to a file created with mode `0600`, which is then fsynced, followed by its directory and every directory the call created.
- `grep` finds `authorization_ref` and `classify_vendor_environment` only in `engine/cli/main.py` and these two modules. `resolve_compat_chart` reaches vendor acquisition through `_acquire_dry_run` (resolver lines 915–940 and 1049–1072), which checks the generic rails only. `engine/cli/main.py` line 396 and `engine/compat/compute.py` lines 457–458 call it. This is the gap that X14 records as `FND-012`.

**§7.2.0 gaps (RL-04).**
- `engine/bodygraph/vendor_client.py` lines 90–96 hold the five route contracts, and `build_contract_route_request` (lines 396–473) builds any of them.
- `classify_bg_resolve_route_policy` (lines 124–153) sends every non-`v2` base, including an unversioned one, to legacy `bodygraphs`, against §7.1.10's `PROVIDER_ROUTE_UNSUPPORTED`.
- `PINNED_MAX_ATTEMPTS` is `{0, 1, 2, 3}` (line 49), against §7.3.3's `{1,2,3}`, and the backoff profiles are checked apart from `max_attempts` (lines 57–65 and 162–175), against §7.3.4's complete tuples.

**Resolved limits (RL-06 to RL-08, revision 2).**
- **S02.** `adapter/factory.py` (blob `618a624dc4d4`) line 30, `adapter/http_reader.py` (blob `ffba6c4e1794`) line 1287 and `adapter/wsgi.py` (blob `52fd4aedf1a9`) line 53 each register a 404 handler that emits `error_envelope("ERR_NOT_FOUND")`. The `http_reader` handler says "never framework HTML"; under `/api/compat/v1` it uses the compat envelope of §5.5.
- **S07.** `engine/cli/main.py` (blob `77b886026c10`) line 94 gives the `showcompat` help: "Emit the canonical magic10_compat_result.v1 document for a pair (stdin or files); Reader v1 bytes only via --dump-reader".
- **S03.** `tests/reader_v1/test_cli_proof.py` is absent, and `tests/retired_tests.md` line 65 records its retirement on 2026-10-13. The reason is O-P06a-03: the legacy `scripts/hd_cli.py` stub refuses `--admin-out` without `--admin`, and the stub is no Reader surface and no proof. The replacing coverage is `tests/reader_v1/test_emitter.py` and `tests/cli/test_cli_canonical_bytes.py::test_reader_dump_and_admin_sidecars_are_canonical`. `scripts/hd_cli.py` stays as the retained legacy stub that §5.1.6 names.
- **Probe (a local check, not CI and not QA).** With the same scratch install, closed rails and `APP_ENV=dev`, a Flask test client on each of the three factories requested `GET`, `POST`, `HEAD` and `OPTIONS` on `/nope`, and `GET` and `POST` on `/api/reader/x`. All 18 requests returned `404` with `application/json; charset=utf-8`. The 15 body-bearing ones carried `code` `ERR_NOT_FOUND` in 70 bytes, and `HEAD` returned no body. The worktree was clean afterwards. The PF05 text states only the checked-in handlers.

**Tests run (implementation checks, not CI and not QA).** In a detached scratch worktree of `0838ba0`, with CI's install (`setuptools>=68`, `wheel`, `requirements.txt`, `requirements-dev.txt`, `-e .`) in a scratch virtual environment:
- **Environment.** pytest 8.4.2; `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`; vendor, database and override keys unset; `XDG_STATE_HOME` pointed at an empty scratch directory.
- **Commands and results.** `python -m pytest -q -p no:cacheprovider tests/http/test_endpoint_catalog.py`: 247 passed, exit 0. The same for `tests/bodygraph/test_vendor_prod_override.py`: 99 passed, exit 0.
- **Clean afterwards.** The worktree's `git status --short --untracked-files=all` was empty and the scratch state directory stayed empty.

The PF05 text claims none of these results; it states only checked-in facts.

## 6. Change and disposition ledger

Dispositions: **RL** an actionable redline; **EQ** already represented, with its location; **OUT** owned by another document or task; **HELD** not drafted, by the ledger; **NC** not a PF05 change (history, evidence, process or a PF10 publication fact).

| Row | Item | Disposition and evidence |
| :-- | :-- | :-- |
| A07 | AD-1 and CR-7: canon-retired routes excluded from the Endpoint Catalog; catalog 23 to 18; validator refuses a retired record | RL-02 (§5.6 state). The population rule and exclusion classes: OUT, to HDE Schemas & Artifacts §8.8 (T-PF12) |
| A07 | AD-1 S15 reading: a registered route that canon retires is accounted for by its exclusion; removal stays with its canon owner | RL-02, stated as the recorded decision behind the state, not as a new PF05 rule |
| A07 | AD-2 and CR-8: dev Reader gate compares `APP_ENV` exactly | EQ: §5.4 "Gate." bullet (line 2430, "gated by `APP_ENV=dev`"), §5.6 table `/reader` row (line 2543, "explicit `APP_ENV=dev`"), §10.3 (line 4048). AD-2 itself names these passages as its basis |
| A07 | AD-3: canonical dev runner binds loopback, debugger and reloader off, no CORS | EQ: §5.4 "Gate." ("bound only to a local interface (for example, `127.0.0.1`)"). The runner profile: OUT, to HDE Mechanics Guide §34 (T-PF14) |
| A07 | AD-4: production exposure of non-public routes | NC for this task: decided under S19 (2.10, not a T-PF05 row). PF05 §5.4 and §5.12 already state the canon; no PF05 wording is named |
| A07 | AD-5 release refresh; AD-6 canon trace | NC: release identity and process; no PF05 content |
| A07 | Doc-delta candidates: §5.6 state | RL-02 |
| A07 | Doc-delta candidates: HDE Schemas & Artifacts §8.8, HDE Mechanics Guide §34 and its alias row, HDE Architecture §3.4 | OUT: T-PF12, T-PF14, T-PF02 |
| A08 | "Required canon drainage": CR-7 into §5.6 | RL-02 |
| A08 | "Required canon drainage": CR-7 into HDE Schemas & Artifacts §8.8 | OUT: T-PF12 |
| A08 | X04 §18 row for HDE-CLI-API-Vendor-Ref §5.6 "Implementation and acceptance state (informative)": "the catalog state" | RL-02 |
| A08 | X04 §18 rows for HDE Mechanics Guide §34, HDE Users Guide §4.1, HDE Schemas & Artifacts §8.8, HDE Architecture §3.4, repository documents | OUT: T-PF14, T-PF29, T-PF12, T-PF02; the repository documents belong to WU-DOC-01 and the Product Owner |
| A08 | OBS-P3-16 (Conjunction checklist `no-store` against PF05 §5.4) | OUT: T-PF09.4. PF05 §5.4 is the reference and does not change |
| A08 | LR3-O1 (PF10 rendering), LR3-O2 to LR3-O5, carried observations, lineage, CI and review facts | NC: PF10 publication fact, owners named, or history |
| A09 | X05 row "§7.1.11 'Required-Now implementation gap (DD-04; held)': the flag is not an available facility" | RL-03 |
| A09 | X05 row for §7.2.0 "Contract and implementation posture": it "lists 'no production-vendor override flag or audit gate' among the material gaps" | RL-04 |
| A09 | X05 row "§7.1.11f 'governed clock boundary' undefined (OBS-W4-4)" | HELD: H-04. Not drafted; §7.1.11f is untouched |
| A09 | X05 rows for HDE Users Guide §16, §10.1 and Recipe F; Glow Infrastructure §8 key `HDE_VENDOR_OVERRIDE_AUDIT_PATH`; `README.md`, `AGENTS.md` and runbooks | OUT: T-PF29, T-PF07, WU-DOC-01. RL-03 names the key as an implementation fact; its owner stays Glow Infrastructure |
| A09 | LR4-O2: the actor is an account name, not necessarily a person | RL-03 records it as a limit. Who may initiate stays with §7.1.11e; the venue question stays with its owner |
| A09 | OBS-W4-1 (carried): showcompat and conjunction vendor acquisition carry no production-override gate | RL-03 records the verified limit and X14's `FND-012` deferral. Whether those commands must meet the gate is not decided by any source, so no rule is drafted |
| A09 | OBS-W4-2: CLI refusal channel (§3.4 and §4.6 stderr-only, against the stdout resolver envelope that §7.1.11e names) | EQ for the fact: §1 line 89 ("failure-stream behavior does not conform to §§3.3-3.4") and §4.7 line 996 ("failure streams diverge"). The canon decision stays with the Product Owner (GS line 168); not drafted |
| A09 | OBS-W4-3: every non-`v2` base takes the legacy route | EQ: §7.2.0 "broad non-v2 legacy selection", kept and re-verified in RL-04 |
| A09 | LR4-O1, LR4-O3, LR4-O4, OBS-P4-1 to OBS-P4-7, readings PD-4, PD-5 and PD-10 ("stay within canon") | NC: owners named; no PF05 change |
| A09 | Required canon drainage: "the canon doc-delta candidates of plan v1.0 §17 and the standing CR-7 targets" | RL-02, RL-03, RL-04 for PF05; the rest OUT as above |
| S-APR | "Canon impact": S14 implements §7.1.11 without changing it | Preserved: §7.1.11a to §7.1.11f are unchanged |
| S-APR | "S14 (status drainage after implementation)": the §7.1.11 DD-04 paragraph becomes stale | RL-03; and RL-01 for the same status restated in §1 |
| S-APR | S14: the HDE Users Guide §16 bullet | OUT: T-PF29 |
| S-APR | S21 close-pack targets; operative `AGENTS.md` passages | OUT: T-PF06, T-PF12, T-PF19; the Product Owner |
| S-APR | Approval block, phase blocks, QA posture and Live QA table, overlaid by delta C-8 to C-12 | NC: record history and QA posture; no PF05 content. C-8 to C-12 reword the release re-cut and delete the S01 row; neither touches PF05 |
| A08 | Requirement coverage: S02 met (unknown paths answer the governed envelope, line 933) | Revision 2, at Nathan's direction: RL-07 (§5.1.0) and RL-08 (§5.1.7). Revision 1 had reported it as O-1 |
| A08 | Requirement coverage: S07 met (`hdctl --help` names `magic10_compat_result.v1`, line 937) | Revision 2, at Nathan's direction: RL-06 (§4.1.6) and RL-08 (§5.1.7). Revision 1 had reported it as O-1 |
| 2.2 and 2.4 (supporting) | S03 met; `tests/reader_v1/test_cli_proof.py` retired with its recorded reason | Revision 2, at Nathan's direction: RL-06 and RL-08. Found while verifying O-1; revision 1 had not identified it |
| PF05 rule | §0.4 and §11.1: log a normative delta | RL-05 (Change Log entry for v2.5.4, widened in revision 2 to name §§4.1.6, 5.1.0 and 5.1.7) |

**Classification of RL-05.** §11.1 logs "normative deltas only" and lets editorial moves go unlogged. RL-03 removes the directive "do not invoke or describe the flag as operational", which governs how canon readers treat the flag, so this revision is a normative delta and the entry is required. The v2.5.3 entry logged the same DD-04 status ("retain held DD-04").

## 7. Redlines, basis and rationale

| ID | Op | Location (original) | Basis | Rationale |
| :-- | :-- | :-- | :-- | :-- |
| RL-01 | REPLACE | §1 "Vendor ingest (HDAPI)", line 125, second sentence of the "Live HTTP gated by SAFE rails" bullet | S-APR; A09 with X05 | The bullet restates the DD-04 status; S14's delivery makes "unimplemented" stale |
| RL-02 | REPLACE | §5.6, line 2577 | A07 (AD-1, CR-7); A08 drainage; X04 §18 | The paragraph describes the Catalog at `aa58e93` before S15 and CR-7. The new state is verified at `0838ba0` (§5) |
| RL-03 | REPLACE | §7.1.11, line 3500 | S-APR; A09 with X05; LR4-O2; OBS-W4-1 with X14 `FND-012`; X14 line 37 | S14 delivered the flag and gate (#651, squash `5892538`, accepted by 2.9), so the held-gap paragraph is stale. The contract is unchanged; the new text gives the bounded implementation state and its recorded limits |
| RL-04 | REPLACE | §7.2.0, line 3605 | A09 with X05 | The delivered gap leaves the list; the other two gaps are re-verified and the inspection is pinned |
| RL-05 | INSERT | §11.1, between lines 4126 and 4127 | PF05 §0.4 and §11.1 | Required change-history entry naming every changed section; version v2.5.4, no date in the format |
| RL-06 | REPLACE | §4.1.6, line 837, the "Remaining CLI limitations:" bullet | Nathan's direction; A08 S07; supporting 2.2, 2.4 and `tests/retired_tests.md` for S03 | The bullet says the parser still describes Reader v1 bytes and the legacy CLI proof failure stands; both are resolved. Its other limitations stay |
| RL-07 | REPLACE | §5.1.0, line 2071, the last sentence of the method-contract paragraph | Nathan's direction; A08 S02 | The sentence retains an HTML 404 limitation that S02 removed; unknown descendant paths take the governed §5.2 error |
| RL-08 | REPLACE | §5.1.7, line 2253, the "Known limits remain:" paragraph | Nathan's direction; A08 S02 and S07; supporting S03 | The HTML 404, stale showcompat help and legacy CLI proof limits are resolved. The wheel-install limit, the carried findings and the nonclaim sentence stay |

**Editorial standard applied (PF03).**
- §3 "Truth and source fidelity" and "Claim-state separation": static inspection proves checked-in bytes only, and a negative statement names its snapshot and search scope.
- §4 step 5: one repository snapshot, `0838ba0`, for every repository claim.
- §5 and §6: routing by title. HDE Build Notes is named by title only, with no addendum number or other locator; other documents use PF05's existing short titles (**HDE-Architecture**, **HDE-Users-Guide**, **HDE-Schemas & Artifacts**).
- §3 "Structure and language": no ellipsis in any payload.
- §7 retention: still-valid text is kept, notably the remaining §7.2.0 gaps and the unchanged §7.1.11 contract.

## 8. Document-control inputs for TW-APPLY-10

- **Header (lines 3–10).** H2 `## **0.1 Header**`, then:
  - `**Title:** PF05-Canon-HDE-CLI-API-Vendor-Ref  ` (line 5);
  - `**Version:** v2.5.3  ` (line 6);
  - `**Status:** Canon  ` (line 7);
  - `**Effective date:** 2026-10-09  ` (line 8);
  - `**Last Update Gate:** BN 13.5; HDE-EPIC040-specification-v1.1-approved.md; HDE-EPIC040-CL-E-10-closure-decision-v1.2.md   ` (line 9, ending in three spaces);
  - `**Invocation tag:** INV-f2ac55d77ce9aacc` (line 10).
- **Formats.**
  - The version is native dotted numeric, `v` plus three components, so one bump gives `v2.5.4`.
  - The date is `YYYY-MM-DD`.
  - The gate lists sources separated by `; `, writing PF10 as `BN <version>` and any other source as its filename.
- **Sources that justified this update, in recorded order:**
  1. PF10 file `PF10-HDE-Build-Notes-v13.8.8.md`, v13.8.8 (RL-01 to RL-04 and RL-06 to RL-08), giving `BN 13.8.8`;
  2. `HDE-CRD-0002-specification-v1.1-approved.md` (S-APR; RL-01, RL-03);
  3. `HDE-CRD-0002_close_report.md` (the RL-03 limits).
- **Not gate sources.** No PF document other than PF10 is a source. The delta (SR3) justifies no change. X01, X04, X05, WI4 and GS are supporting reading.
- **Internal restatements.** The title carries no version. Line 835's "inspected read-only on 2026-10-09" and the Change Log's v2.5.3 entry are history and are not restatements of the header.
- **Status.** `Canon`; not stale.
- **Change-history agreement.** RL-05 names `v2.5.4`, the version Apply derives. The entry format records no date.

## 9. Producer validation

The batch was validated twice:
- **Before saving.** `pf05_redlines.py` built each operation from the baseline bytes and asserted each count, the absence of overlap and the absence of ellipses.
- **After saving.** An independent parser, `check_package.py`, read only the saved file and extracted every fenced payload by its stated convention. It verified each stated byte length and SHA-256, re-resolved every locator against the original, checked conflicts and simulated one-pass application. Both scripts are in the session scratchpad and are not committed.

| ID | Operation and dialect | Scope | Expected | Observed | Original span or gap (byte offsets) | Payload checks |
| :-- | :-- | :-- | --: | --: | :-- | :-- |
| RL-01 | `REPLACE` | whole PF | 1 | 1 | [18262, 18377) | OLD 115 bytes `9a4ba5f0480d254636d6e7457093ff0d26ed1b9dc41025249c9733f5b9905d3d`; NEW 96 bytes `4ee12aeb4c521f6709a6a7bdad24b388404fafa224fe9d41c94d57167f64631b` |
| RL-02 | `REPLACE` | whole PF | 1 | 1 | [199202, 199654) | OLD 452 bytes `244434aa139c28e77d2de6febbe27701f677427bb8599405abae1621e95e609c`; NEW 1,669 bytes `3d7e22165edf2a9d6e3be073ea082d513425527917598f09fcc512d029cfb3ff` |
| RL-03 | `REPLACE` | whole PF | 1 | 1 | [259142, 259836) | OLD 694 bytes `f1561d111595e852fcb8bc72398995432c164c1c647b138372ce7ca5cbcd4a46`; NEW 1,986 bytes `140bb0df3b787874be8c4f94d577b6621f5f8ad3e57f64a48706cbec8fa9a42a` |
| RL-04 | `REPLACE` | whole PF | 1 | 1 | [267539, 268073) | OLD 534 bytes `c92c423362b1ccd682cd6df639ce709862c86c5e291e58b9f302fc1770222ead`; NEW 631 bytes `4827e9ec774c76b70c23301588df2b258f75055d09a9f4c7376ffa5ef7b9f7ec` |
| RL-05 | `INSERT` | whole PF | 1 | 1 | gap at 307197 | BEFORE 445 bytes `e5c18567bd896f69d90742aad08e8dcd1c764f7cb2923053da7ce0729979f302` (count 1); AFTER 417 bytes `adafe4dbe84db32b463a0a5826518a11e8d7954a9ebc1f86d2c196215b139f73` (count 1); TEXT 363 bytes `b04f1143914eb9d36d3a85d85a088c246c4f6edc6f1202397c9fe1e80e7abf23` (revision 1: 252 bytes) |
| RL-06 | `REPLACE` | whole PF | 1 | 1 | [76816, 77298) | OLD 482 bytes `96920064dba80c2f2e2534c5266d38117024520edba0f78427fbddf3694b02d3`; NEW 728 bytes `367e316da87bb797b311fe8fdefa8cb01f97cd28a71a0b4bcba7a6d757838e5e` |
| RL-07 | `REPLACE` | whole PF | 1 | 1 | [153354, 153495) | OLD 141 bytes `54f8c25aeae7dc316e3fc80c00ae5fde84641e6a354d31d215b5962a3eca8875`; NEW 178 bytes `93ff3dea56972a8bf8fa3b7f945c4b3e560a6c6bb79e752353af6c657a6f40de` |
| RL-08 | `REPLACE` | whole PF | 1 | 1 | [166307, 166948) | OLD 641 bytes `4ba93d030fa547df15b03a0fa43d1bb4a4955faaea01270a43c15808ccaf6d9c`; NEW 797 bytes `fadf0f1ca9c989edc6df8cc12dfb5b67358fed98ce7b499972fb3dd0c4a33d93` |

- **Conflicts.** None. The eight spans are disjoint and in order, and the RL-05 gap lies outside every replaced span.
- **RL-045.** No `FIND AND REPLACE` or `FIND_AND_REPLACE` operation is used; every single-occurrence edit is `REPLACE`.
- **Payload hygiene.** No payload contains a CR, a trailing space, a fence or an ellipsis. Every OLD block is absent after simulated application and every NEW block and the inserted text are present.
- **Simulation (revision 2).** One pass in descending offset order from the original (323,966 bytes) gives 327,355 bytes, 4,461 lines, SHA-256 `c157925a8cb796023ca2ac07dc19bedb0e518f6b6c1bb7c5e8d8b1cacc7c1915`, content operations only, before the header plan. A stream rebuilt from the nine untouched intervals and the payloads equals it, and the in-memory plan gives the same bytes. `diff` shows exactly the eight intended changes. (Revision 1's simulation was 326,805 bytes, SHA-256 `13cb56bca5913c0599261fd2a2992d77f031ee78fb233381f83e2892f749bad2`.)
- **Hygiene scan (TW-DRAIN-10).** No `Draft` status language about the document, TODO, TBD, FIXME or drafting note is present. The `[OPEN]` markers (lines 251, 255, 866, 1031) record open contract decisions. "JSON Schema Draft 2020-12" names a specification. Line 1738's "the draft's" is rationale history. The angle-bracket placeholders, such as `<path>`, sit in examples and templates. None needs a hygiene redline.

## 10. Held items, observations and limits

**Held, not drafted.** H-03 (LR5-O1: §5.12 and §5.11.2) and H-04 (OBS-W4-4: §7.1.11f "governed clock boundary"). No redline touches either section.

**O-1. Resolved in revision 2.**
- **Revision 1.** It reported the stale S02 and S07 sentences at §4.1.6 line 837, §5.1.0 line 2071 and §5.1.7 line 2253 as out of scope for routing.
- **Revision 2.** Nathan directed them to be fixed in this run, and RL-06 to RL-08 do so. They also fix a third stale claim in the same sentences that revision 1 had not identified: the legacy `scripts/hd_cli.py` / `tests/reader_v1/test_cli_proof.py` failure, resolved by S03's retirement of the test.
- **What stays.** In those sentences, the stdin/user flag spellings and file gates, `--dump-reader` without Reader v2, the §4.1.7 gap, the wheel-install limitation and the carried findings stay. No source shows them resolved.

**O-2.** §3.7 and §4.6 list `bg:resolve --source=vendor --dry-run` under open rails as allowed in pre-Glow production. In a production-like environment that call now also needs the §7.1.11 flag (§7.1.11d: "A production dry run that contacts the vendor still requires the flag"). §7.1.11 already governs, no source names these passages, and they stay unchanged.

**O-3.** PF05 already contains ellipses (for example lines 279, 2117, 2188 and 2495), which PF03 forbids. No source authorizes their cleanup; this batch adds none.

**O-4.** The §5.6 transport-facts table does not list `/ops/rails/refusal`, `/internal/healthz` or `/internal/readyz`, which the Catalog records. No source names the table; it stays unchanged.

**Limits.** Every repository statement in the redlines is static inspection at one commit. The tests in §5 were run locally to check this documentation, not as CI or QA, and are not cited in PF05. This package edits no PF and establishes no canon drainage, QA, acceptance or closure.

## 11. Next step

READY with `COMPLETE_PACKAGE` (revision 2). Nathan's handoff authorizes TW-APPLY-10 — Apply Validated Redlines — 100926.1 (https://app.notion.com/p/3f44590a05eb81eebff6e3afa3d9aa5b) in this session, and the revision 2 direction asks for the revised PF to be remade from this package. Its inputs are:
- the original `docs/pfcanon/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.3.md` at blob `8b136def4c22f8308169a1b0315086b3e90ead1d`;
- this redlines file and this proof log;
- ledger rows A07, A08, A09 (with X05) and S-APR, with the source boundaries in §3;
- branch `docs/20261026-gtwpe-pf10-v13-8-8-documents`;
- outputs `PF05-from-v2.5.3.md` and `PF05-from-v2.5.3.proof-log.md` in this directory, or `apply-diagnostic-PF05-from-v2.5.3.md` on failure.

## 12. Save verification receipt

Both files of this package (revision 2) were read back from the working tree after saving. The redlines file matched its recorded size and SHA-256 (§1). Re-parsing the saved redlines file with `check_package.py` returned no failure and exit 0. This receipt is written after those checks; this proof log does not carry its own hash.
