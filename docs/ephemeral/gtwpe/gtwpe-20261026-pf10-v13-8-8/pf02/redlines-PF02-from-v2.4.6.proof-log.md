# Proof log — redlines-PF02-from-v2.4.6.md

## 1. Artifact and outcome

- Artifact: `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/pf02/redlines-PF02-from-v2.4.6.md`, five `REPLACE` redlines RL-01 to RL-05, terminated by `END OF REDLINES`.
- This proof log: `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/pf02/redlines-PF02-from-v2.4.6.proof-log.md`, in the same directory.
- Run identity: `gtwpe-20261026-pf10-v13-8-8/T-PF02/TW-DRAIN-10/r1`. This is the first preparation run for T-PF02; no earlier output exists under these names.
- Preparation outcome: `READY`. Save completeness: see §12.
- Actual originating preparer: TW-DRAIN-10 — Prepare PF Document Redlines — 100926.1, page https://app.notion.com/p/3f44590a05eb8172a314fe6b958bb9ff (fetched live on 2026-10-26; page state as of 2026-10-09T11:05:22.139Z), run in Claude Code session https://claude.ai/code/session_01M9PsXYe8yx3bTeqJUj1sTL, which Nathan started for T-PF02.
- Authorized next step: TW-APPLY-10 — Apply Validated Redlines — 100926.1 (https://app.notion.com/p/3f44590a05eb81eebff6e3afa3d9aa5b), in the same session, as Nathan's handoff authorizes. The preparer applies nothing.

## 2. Handoff, ledger and destination

- Handoff: "GTWPE 100926.1 T-PF02 document session (TW-DRAIN-10 then TW-APPLY-10)", from Nathan, 2026-10-26. It names the target, the assigned rows, the selected addenda with line ranges, the supporting cross-references, the closure evidence, the output paths and the destination rules.
- Ledger: `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/LEDGER.md`, blob `74944b261c0ebb2f80a416fb004b9a913da592d1`. It is the same blob at the handoff's commit `13b64dddea4cfe0bb35e56c1833fbcd03af238c7` and on `origin/main` `0838ba08254eaefc888019df49a06aa2ae99cc6c`. Its "Precedence and closure controls" and "Held and deferred items" sections were read before work started. Task row T-PF02 agrees with the handoff on the target, rows and route.
- Assigned rows: A07 (§3.4 against HDE Mechanics Guide §32.3); A08 with X04 (the §3.4 row); A10 with X06 (§3.3, §3.5 and §3.8.1 stale: the production mount of the dev-harness routes and the retired `/ops` routes, settled by S19-F03; the root helpers); A06 as context (the §3.8.1 start-helper posture stands).
- Destination: #760 was merged at 2026-10-26T21:18:51Z (head `13b64dd`, landed as `0838ba0`), so the handoff's continuation applies. `git ls-remote --heads origin` showed no branch matching `gtwpe` and no pull request was open, so this session created `docs/20261026-gtwpe-pf10-v13-8-8-documents` from `origin/main` `0838ba08254eaefc888019df49a06aa2ae99cc6c`.

## 3. Target identity

- Path: `docs/pfcanon/PF02-Canon-HDE-Architecture-v2.4.6.md`; title `PF02-Canon-HDE-Architecture`; version `v2.4.6`; status `Canon`; effective date `2026-10-09`; Last Update Gate `BN 13.5; HDE-EPIC040-specification-v1.1-approved.md; HDE-EPIC040-CL-E-10-closure-decision-v1.2.md`; invocation tag `INV-f2ac55d77ce9aacc`.
- Blob `b0bf3d66965d0de91044b519a29bc30b1cc2d040` at both `9dda63dd3f05f496c3ff67e95da78550d3950c5a` (the ledger baseline, 2026-10-26T20:36:17Z) and `0838ba08254eaefc888019df49a06aa2ae99cc6c` (`main` when work started, 2026-10-26T21:18:50Z). `main` moved between them only by the ledger file; no newer PF02 exists in `docs/pfcanon/`.
- Raw bytes: 140,533 bytes, 1,617 lines, LF only, no BOM, no final LF; SHA-256 `4bfa53ad9775f6b69432b28ae11048b6458461249186c9bb9161e51e5ecb28db`.
- Coverage: read in full, lines 1–1617, including the front matter, every table and list, and §1 to §8.

## 4. Change source and selected units

PF10 HDE Build Notes v13.8.8 is the only change source.

| Unit | Lines | Read | Role |
| :- | :- | :- | :- |
| `docs/pfcanon/PF10-HDE-Build-Notes-v13.8.8.md`, blob `680b0accb0bdf260b0489d1a7385f90bb120cd99`, 729,539 bytes, SHA-256 `f5e13efb5ab1354bda2f578ca69f41bed773160784602a896927bc091a254c2f` | 1–3955 | identity checked | the single unlettered v13.8.8 representation on `main` |
| F00 front matter: precedence §1 to §9, cross-references, template, Addendum Index | 1–223 | full | application rules |
| A06, addendum 2.6 | 531–687 | full | context only |
| A07, addendum 2.7 | 688–889 | full | change-bearing for §3.4 |
| A08, addendum 2.8 | 890–1002 | full | change-bearing for §3.4, with X04 |
| A10, addendum 2.10 | 1102–1204 | full | change-bearing for §3.3, §3.5, §3.8.1, with X06 |

Supersession (front matter §5) was checked for the overlaps this target touches:
- 2.18 withdraws the cost-ceiling passages of 2.11 to 2.16; 2.14 narrows 2.11 rules 7 and 8; 2.17 amends 2.15. None of these touches 2.6, 2.7, 2.8 or 2.10.
- 2.19 and 2.20 take 2.10's "1.4.0 cut" for WU-PR-08 out of force. That passage has no PF02 target, and nothing drafted here relies on it.
- A bounded search of the later addenda (after line 1204) for `run_flask`, "root helper", `OBS-P3-17`, `X-02`, `_mount_for_production`, `reader_harness` and "HDE Architecture" found no addendum that changes the facts drafted here. 2.33 (line 3612) defers X-02, and 2.35 item 9 (lines 3768–3778) lists X-02 as an undecided finding for a later CRD, noting it is unreachable in production after S19-F03.
- 2.11's misnumbered cross-references are not used by any change here.

## 5. Supporting reading

These were read only to check meaning, ownership or current state. None is a change source, and none widens the edit scope.

- X04: `docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-implementation-plan-v2.0.md` §18, lines 753–792, blob `1d6a92a483e2`. Line 763 is the §3.4 row. Line 778 (OBS-P3-17) is the root-helper observation.
- X06: `docs/ephemeral/HDE-CRD-0002-WU-PR-05-pr-implementation-result-v1.0.md` §10, lines 156–165, blob `20b170490447`.
- X06 cites "plan §19", so its source was read: `docs/ephemeral/HDE-CRD-0002-WU-PR-05-pr-implementation-plan-v1.0.md` (blob `54809ffbaf34`) §19, lines 717–739, which names the exact stale statement in each PF02 section; and §7.3, lines 399–419, the D-1 design of S19-F03.
- `docs/ephemeral/HDE-CRD-0002-S19-code-security-review-v1.0.md` (blob `016e74e557ee`): the §4 rows for S19-F02 and S19-F03, the §5 rows for gaps 1 to 3 and OBS-P3-17, and the §8 row for X-02.
- HDE Mechanics Guide (`PF14-Canon-HDE-Mechanics-Guide-v3.5.8.md`, blob `3360a9eb1a50`): §32, lines 4762–4855, including §32.3; and the §34 lines that name the canonical dev runner and start command (lines 4898, 4933 and 4946).
- HDE-CLI-API-Vendor-Ref (`PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.3.md`, blob `8b136def4c22`): §5.5's production-posture resolution sentence (in the §5.5 block from line 2476).
- `PF03-Reference-Technical-Writing-Best-Practices-v1.8.8.md` (blob `504712df548a`, SHA-256 `df685f3a66aa18fdcacb697b340263cb59fc682564fa59c50b3d9b9ca735c462`), read in full as the editorial standard. Its §8 default against fenced paste text yields to TW-DRAIN-10's exact-redline contract, which is the operator-supplied format.
- `AGENTS.md` (blob `7e358b4601d3`): the canon-first, canon read-only, write-boundary and truncation rules.
- A canon-wide search: `git grep -i -E 'healthz|readyz' origin/main -- docs/pfcanon/`.

## 6. Closure and approval evidence

HDE-CRD-0002 is closed, so no change here is held on closure grounds. Each file was confirmed present at the stated blob on `main`.

- X10 `docs/ephemeral/HDE-CRD-0002-specification-review-v1.1.md` (`c48f77a0c220`): Specification INITIAL_APPROVE by Thoth, 2026-10-12T19:39:51Z.
- SR4 `docs/ephemeral/HDE-CRD-0002-specification-delta-review-v1.0.md` (`5a6cecc86f60`): delta 01 DELTA_APPROVE by Thoth, 2026-10-21T18:36:00Z.
- X11 `docs/ephemeral/HDE-CRD-0002-CL-C-10-closure-decision-v1.2.md` (`2260eae17974`): CLOSE, CHANGE_CLOSED by Isis, 2026-10-26T16:40:00Z.
- X12 `docs/ephemeral/HDE-CRD-0002-CL-20-post-closure-record-v1.0.md` (`ac60f368f6d9`): M-0 (this drainage) to M-3.
- X13 `docs/ephemeral/HDE-CRD-0002-QA120-qa-report-v1.0.md` (`d6cceaf3a019`): final QA Report, PASS, 21 checks.
- X14 `audit/HDE-CRD-0002_close_report.md` (`0bbc8050d3c1`): the close report and its deferrals.

## 7. Repository inspection

Every current-repository statement in a NEW literal was checked by direct read-only inspection of `origin/main` `0838ba08254eaefc888019df49a06aa2ae99cc6c`. Its code tree equals that of `9dda63dd`. The history was deepened to confirm that no commit after the S19 merge (`822ce15`) changes any inspected file.

| Path | Blob | Fact used |
| :- | :- | :- |
| `adapter/factory.py` | `618a624dc4d4` | Registers `bp` at `/`, `api_bp` at `/api` and `compat_blueprint`; defines no `/internal/healthz` or `/internal/readyz` |
| `adapter/http_reader.py` | `ffba6c4e1794` | Lines 559–625: `_PRODUCTION_DEV_WRITER_ROUTES`, `_PRODUCTION_RETIRED`, `_production_posture` (through `_compute_env_mode`) and `_mount_for_production`, which installs `_refuse_in_production` only in a production posture. The hook answers retired endpoints, and a method no rule names on their paths, with the app's not-found answer. It leaves Flask's automatic `OPTIONS` alone, gives the dev `GET /reader` endpoint its refusal, and gives the four dev/admin endpoints their writer refusal. It reads no request-time environment value. Line 1155 `bp.record(_mount_for_production)`. `_dev_admin_gate` is exact (`dev`, `test`, `local`), and the four dev routes call it. Lines 1248–1260: `create_app` registers `bp`, `api_bp` under `/api` and `compat_blueprint`. Lines 1315–1325: the module runner |
| `adapter/wsgi.py` | `52fd4aedf1a9` | Registers the same three blueprints; defines `/internal/healthz` and `/internal/readyz` |
| `adapter/env_guard.py` | `ba0cb043c469` | `_compute_env_mode`: a non-empty `APP_ENV`, trimmed and lower-cased, else `ENGINE_ENV`; `prod`, `production` or `live` gives `prod` |
| `engine/http/compat_handler.py` | `df9a6e033e29` | Uses `_compute_env_mode`, the same resolution as the hook |
| `scripts/dev_start_reader.sh` | `6ddaa5dbb505` | Exports `APP_ENV` only when the caller set it (`<UNSET>` displayed otherwise); `exec python -m adapter.http_reader`; banner `host=127.0.0.1` |
| `run_flask.py` | `61493b36fb16` | Imports `adapter.factory.create_app`; `app.run(host, port, debug=debug, use_reloader=True, use_debugger=debug)`, where `debug` defaults to true |
| `run_flask_dev.sh` | `197dd0980f89` | Exports `FLASK_DEBUG=1` and `FLASK_APP=adapter.factory:create_app`; runs `python run_flask.py` |
| `dev/reader_harness/` | none | `git ls-files` lists no path beginning `dev/reader_harness/`. The only matches are the historical audit-source copies `.audit_src/dev/reader_harness/__init__.py` and `.audit_src/dev/reader_harness/app.py` |
| `artifacts/audit/ENDPOINTS_CATALOG.json` (`docs/ENDPOINTS_CATALOG.json` is a symlink to it) | `97f201f1472f` | 18 records. The four dev routes are `dev_harness` and not A7-eligible. There is no record for `/ops/db/unavailable`, `/ops/probe/env` or `/ops/writer/diagnostic`. `/internal/healthz` and `/internal/readyz` are `ops`, "adapter.wsgi factory only" |
| `Procfile` | `e9ab44a0aea6` | Read only to confirm which factory production starts (`adapter.factory:create_app()`); not restated in PF02 |

The app was not started and pytest was not run, as the handoff allows. Runtime answers are not claimed beyond the code read. Addendum 2.10 records the S19 lineage review's Flask test-client probes on `822ce15`. Those probes cover the same bytes for every inspected file, and they agree with the code read: in a production posture the dev routes are refused and the retired routes answer 404; the rules and pairs are the same in both postures; on the dev runner `/ops/probe/env` and the sampler answer 200.

## 8. Change and disposition ledger

| Source item | Disposition | Target location and evidence |
| :- | :- | :- |
| A07: "HDE Architecture §3.4, which labels the health probes speculative, while HDE Mechanics Guide §32.3 requires them" | Actionable: RL-02 | §3.4 label, line 914. HDE Mechanics Guide §32 is `[Required-Now]` and owns health/ready behavior; §32.3 requires both probes |
| A08 with X04, line 763 (the same §3.4 item) | Same change as A07: RL-02 | One redline covers both rows |
| A10 with X06: §3.3 stale ("without an environment-specific unmount"; plan §19) | Actionable: RL-01 | §3.3 discrepancy, lines 896–897, becomes the production-posture behavior and a static-inspection limit |
| A10 with X06: §3.5 stale (the retired routes' "continued presence"; plan §19) | Actionable: RL-03 | §3.5 discrepancy, lines 955–956. Drift classification and nonclaims retained; production-like answer added |
| A10 with X06: §3.8.1 stale ("exposes the same Reader and internal/dev sampler routes as the production adapter"; plan §19) | Actionable: RL-04 | §3.8.1 bullet, line 1089 |
| A10 with X06: §3.8.1, the root helpers (X-02, OBS-P3-17); with A07 and A08 for the delivered S09 harness retirement | Actionable: RL-05 | §3.8.1 discrepancy, lines 1093–1094. The `dev/reader_harness/app.py` sentence no longer describes `main`. The root-helper fact stays true and its classification is retained. X-02 itself is not decided |
| A06: the §3.8.1 "Repo-side start-helper posture" bullet stands (CR-6) | Already represented; no change | Line 1083 unchanged. `scripts/dev_start_reader.sh` conforms on `main` (§7) |
| A06: HDE Architecture §3.8.1 among the six passages that need no change | Already represented; no change | Line 1083 |
| A06, A07, A10: HDE Mechanics Guide §5.6 and §34, Glow Infrastructure §8.1, HDE-CONJ001.4, Glow QA Guide §13.9, HDE Schemas & Artifacts §8.8, HDE CLI/API/Vendor Ref §5.6, HDE Users Guide §1.1 and §4.1 | Outside this target | Routed by the ledger to T-PF14, T-PF12, T-PF05 and T-PF29. A06's other passages need no change |
| A07 AD-1 to AD-6 (catalog population, exact gate, runner profile, AD-4 gaps, refresh, canon trace) | No PF02 change beyond RL-01 to RL-05 | AD-4's gaps were settled by S19 (A10), which RL-01, RL-03, RL-04 and RL-05 reflect. The rest is owned elsewhere or is history |
| A08 LR3-O1; A10 "never fires" wording of 2.7 AD-4 item 4 | Not a PF02 change | PF10 publication facts (ledger "Precedence and closure controls") |
| A10 LR5-O1 (router-level `OPTIONS` and redirects) | Held: H-03; not drafted | No NEW literal claims the dev or retired routes are "not available" at router level, or decides the question. RL-01, RL-03 and RL-04 state handler-level facts only |
| A10 S19-R01 to S19-R07, X-01, X-03, X-04 | Not a PF02 change | Product Owner (2.10; 2.35 item 9) |
| A10 "cuts 1.4.0" | Out of force (2.19, 2.20); no PF02 target | none |
| A08 OBS-P3-16 (X04 line 777) | Outside this target | T-PF09.4 |
| X06 line 159: repository documents describing the production route set or the root helpers | Not PF canon | WU-DOC-01 and PF10 2.34's repository-documentation deltas |

## 9. Observations reported, not drafted

1. Probe route names. HDE Mechanics Guide §32.3 and HDE Build Checklist — Coagulation name the probes `/healthz` and `/readyz`. PF02 §3.4, the Endpoint Catalog and `adapter/wsgi.py` use `/internal/healthz` and `/internal/readyz`. No assigned source resolves the split. RL-02 keeps PF02's existing names and adds none.
2. Probe factory. PF02 §3.4's unchanged current-behavior paragraph, verified on `main`, says the probes are defined only in `adapter/wsgi.py`, not in the selected factory. Whether that conflicts with HDE Mechanics Guide §32.1A and §32.3 is a question for that guide's owner and the Product Owner. It is not drafted here.
3. §3.5 keeps its nonclaim "No repository removal, test migration, deployment convergence, or catalog mutation is claimed", as written. The catalog itself was changed by #643 and #646 (2.7 AD-1, 2.8). That catalog content belongs to HDE Schemas & Artifacts and HDE-CLI-API-Vendor-Ref, not to PF02.
4. The pinned current-behavior paragraphs of §3.3 (line 856), §3.4 (line 928) and §3.5 (line 953) are still true at `0838ba0`. They keep their `cc754cfb` commit pin, because no source directs a change.

## 10. Held items

No held item was touched. H-03 (LR5-O1) is the only held item that relates to this target, and it is not drafted. H-01, H-02, H-04, H-05 and H-06 do not bear on PF02.

## 11. Producer validation

The saved redlines file was parsed by a local validator in the session scratchpad. The validator extracts each OLD and NEW literal by the file's stated fence convention and checks it against the unchanged original bytes. It ran before READY was declared:

| ID | Operation | Scope | Expected | Observed | Original byte span | Original lines | OLD bytes | NEW bytes |
| :- | :- | :- | :- | :- | :- | :- | :- | :- |
| RL-01 | REPLACE | whole PF | 1 | 1 | 70330–70645 | 896–897 | 315 | 1128 |
| RL-02 | REPLACE | whole PF | 1 | 1 | 71544–71580 | 914 | 36 | 211 |
| RL-03 | REPLACE | whole PF | 1 | 1 | 73970–74464 | 955–956 | 494 | 917 |
| RL-04 | REPLACE | whole PF | 1 | 1 | 83165–83695 | 1089 | 530 | 722 |
| RL-05 | REPLACE | whole PF | 1 | 1 | 84449–84977 | 1093–1094 | 528 | 924 |

- Conflicts: none. The gaps between consecutive spans are 899, 2,390, 8,701 and 754 bytes. No two spans intersect, no edit touches another's boundary, and no NEW literal is another redline's locator.
- Dialect: only `REPLACE`. No `FIND AND REPLACE` or `FIND_AND_REPLACE` is used, so RL-045 does not arise.
- Payloads: every NEW differs from its OLD. No NEW contains an ASCII three-period ellipsis or U+2026. The trailing double spaces of label lines and of the RL-04 bullet are present in the saved literals.
- One-pass simulation, applied in descending offset order on the original-bound plan: 142,532 bytes, SHA-256 `9f5bc90c5e5a16be49a9a2cd52a201adc88c0aad7b3858a69e0308c94b9bff84`. Every untouched interval is byte-identical. LF only; no final LF, as in the original. The header is untouched, because document-control fields are Apply's.
- PF03 checks on the NEW text: claim states are separated (`[Implemented]` current facts carry a commit pin; requirements stay requirements); titles are cited without versions; no headers, payloads, status codes or error tokens; HDE Build Notes is not cited.

## 12. Save and completion

Recorded only after both files were read back; see the receipt below.

Receipt (2026-10-26, this session):
- `redlines-PF02-from-v2.4.6.md`: read back complete; 16,358 bytes, 172 lines, LF only, last line `END OF REDLINES`; SHA-256 `783e9f23824e6cc9388fe47e70ee58ecac43296c3fee5dc12d6790fd06f5d5ea`. Re-validated from the saved bytes with the same result as §11; its simulation was byte-identical to the first.
- This proof log: read back complete before this receipt was added (sections 1 to 12 present, LF only, no ellipsis). It does not carry its own hash.
- Save completeness: `COMPLETE_PACKAGE`. Preparation outcome: `READY`. The package is ready for TW-APPLY-10 with the original `docs/pfcanon/PF02-Canon-HDE-Architecture-v2.4.6.md` (blob `b0bf3d66965d0de91044b519a29bc30b1cc2d040`), ledger rows A06, A07, A08 with X04 and A10 with X06, branch `docs/20261026-gtwpe-pf10-v13-8-8-documents`, the final outputs `PF02-from-v2.4.6.md` and `PF02-from-v2.4.6.proof-log.md`, and the diagnostic path `apply-diagnostic-PF02-from-v2.4.6.md`, all in this directory.
