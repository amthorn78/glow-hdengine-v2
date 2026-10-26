# T-PF29 — preparation proof log for `redlines-PF29-from-v1.0.2.md`

This is the processing report for the redlines file beside it, `redlines-PF29-from-v1.0.2.md` in `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/pf29/`. Both files carry run `gtwpe-20261026-pf10-v13-8-8/T-PF29`, preparation revision `P1`.

## Outcome

- Preparation outcome: **READY**. Fifteen `REPLACE` operations. Every change identified in the selected units is accounted for below, and no blocking dependency remains.
- Save completeness: see "Save verification" at the end. It is recorded only after both files were read back.
- Next step: TW-APPLY-10 100926.1 (https://app.notion.com/p/3f44590a05eb81eebff6e3afa3d9aa5b) in the same Nathan-started document session, as the handoff authorizes.

## Identity

| Item | Value |
| --- | --- |
| Task | T-PF29, ledger `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/LEDGER.md` at `13b64dddea4cfe0bb35e56c1833fbcd03af238c7` (blob `74944b261c0ebb2f80a416fb004b9a913da592d1`; byte-identical on `main` `0838ba08`). On the shared branch the T-PF29 row was unchanged and `PENDING` when this preparation started |
| Assigned rows | A10 with X06 (§1.1: the retired-route table and the production posture after S19-F03); S-APR with X05 (the §16 `--allow-prod-vendor` bullet; the §10.1 band override after S08; Recipe F: APP_ENV after S14); A08 with X04 (§4.1: the helper binds 127.0.0.1, not 0.0.0.0). None of the held items H-01 to H-06 is routed to this task, and none is touched |
| Prompt | TW-DRAIN-10 — Prepare PF Document Redlines — 100926.1, https://app.notion.com/p/3f44590a05eb8172a314fe6b958bb9ff, fetched live on 2026-10-26 (Notion page state 2026-10-09T11:05:22Z) |
| Originating preparer | TW-DRAIN-10 in the Nathan-started T-PF29 document session: Claude Code cloud session https://claude.ai/code/session_016STkEGvGYVWWaqSxnj76eo. One session, no subagent, no reviewer |
| Target | `PF29-Canon-HDE-Users-Guide` v1.0.2, Status Canon, Effective date 2026-10-09; `docs/pfcanon/PF29-Canon-HDE-Users-Guide-v1.0.2.md` |
| Target baseline | `origin/main` `0838ba08254eaefc888019df49a06aa2ae99cc6c` (2026-10-26T21:18:50Z), which differs from the ledger baseline `9dda63dd3f05f496c3ff67e95da78550d3950c5a` only by the ledger file. Git blob `6a0d4725a710bfe1289282729156e15cc8acfcce`; 72,066 bytes; 1,072 lines; LF line endings, no CR; ends with one LF; raw UTF-8 SHA-256 `36c3b1bdce884f902dce56650065bdbd26aa3dcb1da8954f62f2c38f83fd5601`. Last changed by `2ff696b4` (2026-10-24T01:18:47Z). `main` carries no newer PF29 |
| Change source 1 | PF10-HDE-Build-Notes v13.8.8, `docs/pfcanon/PF10-HDE-Build-Notes-v13.8.8.md`, blob `680b0accb0bdf260b0489d1a7385f90bb120cd99`, 729,539 bytes, 3,955 lines, SHA-256 `f5e13efb5ab1354bda2f578ca69f41bed773160784602a896927bc091a254c2f`, effective 2026.10.26. It is the sole unlettered logical representation on `main` |
| Change source 2 | HDE-CRD-0002 Specification v1.1 (SPECIFICATION_APPROVED), `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md`, blob `c4802a5a7fa33db38d42d8a7f64679cd18b50480`, 43,151 bytes, 308 lines, SHA-256 `fb412f178fa0ecae527704b16ced4be2c28e42a84e663ccbebdbdb669b7382df`; overlaid by delta 01, `docs/ephemeral/HDE-CRD-0002-specification-delta-v1.0.md`, blob `9408d6ed091bcba3d751fcb17ae392a1ceca8bbb`, 21,046 bytes, 162 lines, SHA-256 `59ef9a776c6b5615333cfe68ba4d8145a3d1fe1fdd194b12bb24cf71a233b636` |
| Selected units, read in full | PF10 front matter, lines 1–223 (application rules §1–§9, cross-references, template, Addendum Index); 2.8, lines 890–1002; 2.10, lines 1102–1204. Specification lines 147–193 ("Specification approval", "Phase blocks", "Canon, QA & Build Notes posture"); delta 01 §2 rows C-8 to C-12 (lines 61–65) |
| Supporting cross-references | X04: `docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-implementation-plan-v2.0.md`, blob `1d6a92a483e238ea4a8144d44461bbbc81704e17`, §18, lines 753–792. X05: `docs/ephemeral/HDE-CRD-0002-WU-PR-04-pr-implementation-plan-v1.0.md`, blob `6baead456619af1e73e15ace1079380f5797ca85`, §17, lines 701–739. X06: `docs/ephemeral/HDE-CRD-0002-WU-PR-05-pr-implementation-result-v1.0.md`, blob `20b170490447a530feb56682ab412503e2ae6717`, §10, lines 156–165. Each was read in full at that boundary as supporting reading, not as a change source |
| Closure and approval evidence (identities checked on `main`) | X10 Specification review v1.1 (blob `c48f77a0c220`; INITIAL_APPROVE by Thoth, 2026-10-12T19:39:51Z); SR4 delta review v1.0 (blob `5a6cecc86f60`; DELTA_APPROVE by Thoth, 2026-10-21T18:36:00Z); X11 CL-C-10 closure decision v1.2 (blob `2260eae17974`; CLOSE, CHANGE_CLOSED by Isis, 2026-10-26T16:40:00Z); X12 CL-20 post-closure record v1.0 (blob `ac60f368f6d9`); X13 QA-120 QA Report v1.0 (blob `d6cceaf3a019`; PASS, 21 checks); X14 `audit/HDE-CRD-0002_close_report.md` (blob `0bbc8050d3c1`). As the handoff and the ledger record them; used only to establish that no assigned change is held on closure grounds |
| Output | `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/pf29/redlines-PF29-from-v1.0.2.md` and this proof log, on branch `docs/20261026-gtwpe-pf10-v13-8-8-documents` (shared draft PR #761, https://github.com/amthorn78/glow-hdengine-v2/pull/761) |

Every source was read from `origin/main`. No native Google Doc, Drive copy, Library copy or memory was used.

## Coverage

- **Target.** The complete PF29 v1.0.2, lines 1–1072, was read, including every table and code block.
- **Selected sources.** Each selected unit was read in full, heading to next heading of the same level. No unselected PF10 addendum was read for this task.
- **Editorial standard.** `PF03-Reference-Technical-Writing-Best-Practices` v1.8.8 (blob `504712df548a`, 43,953 bytes, 633 lines) was read in full.
- **Supporting reading, read to establish meaning or ownership only:**
  - HDE CLI/API/Vendor Ref (`docs/pfcanon/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.3.md`) §7.1.11 to §7.1.11f, lines 3498–3597: the override's flag, environment classification, rail and flag matrix, evaluation order, error carrier, authorized initiator and audit contract. This is the owner RL-006, RL-007 and RL-011 route to by title.
  - `docs/ephemeral/HDE-CRD-0002-WU-PR-05-pr-implementation-plan-v1.0.md` (blob `54809ffbaf34`) §19, lines 717–739, and its S19-F01 to S19-F09 rows in §5. X06 §10 defers the stale-passage detail to that plan's §19, which states the PF29 §1.1 change: "add that a production-like application answers them as unknown paths".
  - Specification v1.1 S08 and S14 requirement rows (lines 87 and 93), for their acceptance intent.
  - Repository documents on `main`, read-only, for consistency with the delivered wording only: `docs/CLI_commands.md` lines 16–23 and `README.md` line 223.
  - The T-PF07 package on the shared branch, for this run's native redline and proof-log structure only.
- **Repository inspection** (PF29 §0.2), all read-only at `origin/main` `0838ba08`. The application code is identical at `9dda63dd`, since the only change between them is the ledger. Nothing was installed or executed; `hdctl --help` was read from the parser code:
  - `scripts/dev_start_reader.sh` (whole file);
  - `adapter/http_reader.py`: `_reader_dev_env_explicit`, `reader_v1`, `_PRODUCTION_DEV_WRITER_ROUTES`, `_PRODUCTION_RETIRED`, `_production_posture`, `_mount_for_production`, `_dev_admin_gate`, `create_app`'s 404 and 405 handlers, and `__main__`;
  - `adapter/env_guard.py` `_compute_env_mode`;
  - `adapter/factory.py` (whole `create_app`) and `adapter/wsgi.py`'s 404 and 405 handlers;
  - `engine/cli/main.py`: `_build_parser` (the `showcompat`, `aux-preview` and `bg:resolve` parsers), `_allow_prod_vendor_usage_error`, `bg_resolve`, `_resolver_env` and `aux_preview`;
  - `engine/bodygraph/resolver.py`: `classify_vendor_environment`, `resolve_bodygraph`, `_resolve_vendor`, the production write guard in `_resolve_vendor_route`, `_vendor_config_env` and `_acquire_dry_run`;
  - `scripts/hd_cli.py`, where line 52 still emits `open_leader`.
- **Canon-first search.** `git grep` on `main` over the target and the selected sources, for `allow-prod-vendor`, `0.0.0.0`, `127.0.0.1`, `--band`, `APP_ENV`, `ENGINE_ENV`, `ERR_NOT_FOUND`, `HTML`, `/ops/`, `magic10_compat_result`, `PROVIDER_CONFIG_INVALID`, `VERIFY`, `reader_harness`, `catalog` and the marker terms listed under "Marker and hygiene classification".

## Precedence, supersession and closure

- **Closure.** HDE-CRD-0002 is closed, by CL-C-10 v1.2 (CLOSE, CHANGE_CLOSED, Isis, 2026-10-26T16:40:00Z; X11), after the QA-120 PASS (X13). No assigned change is held back on closure grounds.
- **The Specification in force** is the approved base v1.1 plus approved delta 01 (PF10 2.20; ledger "Precedence and closure controls"). S01 is removed and the release stays at 1.3.0. Delta rows C-8 and C-9 change the Conjunction and Fermentation Dependencies cells to "a same-version manifest refresh". C-10 rewrites the Coagulation row to S16 and S17. C-11 drops the re-cut from the ordering line, and C-12 deletes the S01 row of the Live QA table. None of them changes the text this package relies on: the Fermentation row still names S08 and S14, and the S14 drainage bullet (line 178) is untouched by the delta.
- **Supersession** (PF10 front matter §5), applied as the handoff states:
  - 2.18 withdraws the cost-ceiling passages of 2.11 to 2.16.
  - 2.14 narrows 2.11 rules 7 and 8 for P1 findings.
  - 2.17 amends 2.15.
  - 2.11's misnumbered cross-references are read by the rule their text describes.
  - None of these bears on 2.8 or 2.10 or on any PF29 passage.
  - Per the ledger, 2.19 and 2.20 take 2.10's "WU-PR-08 (S17) cuts `1.4.0`" out of force. It is not drafted, and PF29 keeps release 1.3.0 with 45 members (v1.0.2 lines 493 and 976).
- **PF10 silence** (front matter §8). No selected unit states replacement wording for PF29. The wording below is drafted within PF29's own conventions and each claim was checked against `main`.
- **Citation rule** (`AGENTS.md`; PF03 §3 "Canonical ownership"). No payload cites HDE Build Notes by addendum, section or version, and no payload names HDE Build Notes at all. Other PF documents are routed by their exact in-document title, as PF29 already does.

## Change and disposition ledger

Every change identified in the selected units is listed with its disposition. "Elsewhere" means the triage ledger routes it to another task or owner; no PF29 edit is made for it. The ledger's assigned rows name the target sections the sources name; the ledger also states that "each document session determines the actual edits". Rows marked **(full-target read)** are PF29 passages that the same selected units make stale but that the ledger row does not name. They were found by the complete target read and the canon-first search.

### 2.8 (A08) with X04

| Item | Disposition |
| --- | --- |
| AD-3 (S09/S10): the canonical runner binds loopback with the debugger and reloader off; X04 §18: HDE Users Guide §4.1 "binds the process through `python -m adapter.http_reader` to host `0.0.0.0` on `PORT`" is stale | **RL-003** (§4.1). The client-address exception clause, which only reconciled the old bind, goes with it |
| S10 / (2), last clause: the start helper propagates APP_ENV and sets no default | **RL-003** (§4.1) |
| S10 / (2): GET/HEAD `/reader` only for APP_ENV exactly `dev` (CR-8, AD-2) | **RL-004** (§6.1 "Current repository discrepancy \[Current gap\]") and **RL-012** (§16 dev GET `/reader` bullet) **(full-target read)**. §6.1's rule bullet "APP\_ENV=dev is required." (line 331) and §17's `ERR_READER_FORBIDDEN` row (line 993) were already accurate and are unchanged |
| S02 / (1): unknown paths on the factories answer the governed envelope | **RL-009** (§16 unknown-path bullet) **(full-target read)** |
| S07 / (3): `hdctl --help` names `magic10_compat_result.v1` | **RL-010** (§16 CLI help sentence) **(full-target read)** |
| S09 / (4): `dev/reader_harness/` removed; `VERIFY.sh` runs against the canonical runner | No change. PF29 names neither, and §4.1 already documents only the canonical helper (no occurrence of `VERIFY` or `reader_harness` in the target) |
| S15 / (5), AD-1, CR-7: Endpoint Catalog classes and the canon-retired exclusion | Elsewhere: HDE Schemas & Artifacts §8.8 and HDE CLI/API/Vendor Ref §5.6 (T-PF12, T-PF05). PF29 documents no catalog content |
| S18 / (6): repository documents | Not PF canon (repository documents) |
| (7): admission 1.3.0, 45 members, refreshed `release_id` | Already represented: PF29 v1.0.2 lines 493 and 976 state 1.3.0 with 45 members; PF29 states no `release_id` |
| AD-4's four gaps, carried to WU-PR-05 | Delivered under 2.10; see S19-F02 and S19-F03 below |
| Required canon drainage: CR-7 targets; 2.7 candidates; plan v2.0 §18 rows other than PF29 §4.1 (HDE Mechanics Guide §34, HDE Schemas & Artifacts §8.8, HDE CLI/API/Vendor Ref §5.6, HDE Architecture §3.4, `docs/RUN.md`, the healthcheck comment, `AGENTS.md`/`README.md`) | Elsewhere: T-PF14, T-PF12, T-PF05, T-PF02, and the Product Owner for the repository documents |
| X04 OBS-P3-16 (HDE-CONJ001.1 `no-store`) | Elsewhere: T-PF09.4 |
| Observations LR3-O1 to LR3-O5; carried observations; canon-conflict register CR-1 to CR-8; TypeSafe and receiving-session advice | Not PF29 content (PF10 publication facts, Implementation Agent lessons, history) |

### 2.10 (A10) with X06

| Item | Disposition |
| --- | --- |
| S19-F03 and the production-posture probes: in a production posture the three canon-retired `/ops` routes answer `ERR_NOT_FOUND` 404, the same answer as an unknown path, before any handler runs; the dev runner keeps the full mount. X06 §10 names HDE Users Guide §1.1 as stale; plan §19 states the change | **RL-002** (§1.1 retired-route block) |
| S19-F03, dev-harness half: in a production posture the dev-harness routes answer their canonical forbidden errors | Already represented: the \[Dev or QA only\] rows of the §1.1 table for these routes (lines 95, 96 and 102), the §0.5 legend (line 69) and §16 lines 959 and 961 present them as dev/QA-only, never production-public. Router-level `OPTIONS` and redirect answers on these paths are LR5-O1, **held (H-03)**; no wording about them is drafted |
| S19-F02: exact dev/admin HTTP gate (and the exact CLI gate, plan row S19-F02) | **RL-012** (§16) **(full-target read)**. §5.1 "APP\_ENV must be dev, test, or local." (line 273), §5.2 (line 317) and the §17 `DEV_ADMIN_ONLY` and 403 rows (lines 990–991) were already accurate and are unchanged |
| S19-F05: strict rails (`SAFE_MODE` open only for exactly `0`, network only for exactly `1`) | Already represented: PF29's open-rails prefixes are exactly `SAFE_MODE=0 ALLOW_NETWORK=1` (§2.2, line 168) and no passage relies on a lenient reading |
| S19-F09: `--report` refusal with a symlinked candidate root | Already represented: §7.6 (line 501) states that `--report` writes only outside both candidate and repository roots; the fix makes that hold for the symlink case |
| S19-F01, S19-F04, S19-F06, S19-F07, S19-F08; CX5-1 | No PF29 passage depends on them: Reader body nesting depth, the writer helper's chunked-body read, ingest log paths, the CLI catch-all's stderr token, manifest path characters, the ingest runner's logs |
| Same-version release refresh at 1.3.0 (`release_id` `77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e`, 45 members) | Already represented, as under 2.8 (7) |
| LR5-O1 (router-level `OPTIONS` and redirect answers) | **Held (H-03)**, Product Owner. Not drafted. RL-002 states only what holds for every method on the three retired paths |
| Required canon drainage: HDE Architecture §3.3, §3.5, §3.8.1; HDE Mechanics Guide §34; the "never fires" wording of 2.7 AD-4 item 4 | Elsewhere: T-PF02, T-PF14; the PF10 wording is a Product Owner publication fact |
| "WU-PR-08 (S17) cuts `1.4.0`" | Out of force (2.19, 2.20); not drafted |
| Routed findings S19-R01 to S19-R07 and X-02; LR5-O2 to LR5-O5; carried observations | Product Owner or Implementation Agent, undecided; not drafted. S19-R02 names HDE Users Guide §11.3's legacy-fallback posture among what a fix would reverse; it is undecided, so §11.3 stays as it is |

### S-APR (Specification v1.1 lines 147–193, as overlaid by delta 01 C-8 to C-12) with X05

| Item | Disposition |
| --- | --- |
| Canon impact, S14 status drainage: "the `--allow-prod-vendor` bullet of HDE Users Guide §16 become[s] stale once S14 lands; their owners update them" (X05 §17 row "HDE Users Guide §16") | **RL-011** (§16 bullet) and its pointer **RL-015** (§18 closing paragraph, "unsupported flag") |
| Phase blocks, Fermentation: S14 holds on `main`; X05 §17 Recipe F row: "the open-rails dry-run command supplies no `APP_ENV`; after S14 an unset value refuses `PROVIDER_CONFIG_INVALID`, and a production-like one needs the flag" | **RL-008** (Recipe F). The same command, byte for byte, also appears in §11.2 and §18: **RL-006** and **RL-014** **(full-target read)**. The production-like case is **RL-007** (§13.3) **(full-target read)**. The error codes are **RL-013** (§17) **(full-target read)** |
| Phase blocks, Fermentation: S08 holds on `main`; X05 §17 row for HDE Users Guide §10.1 ("The band comes from that row; --band does not override it", stale after S08) | **RL-005** (§10.1) |
| Phase blocks, Conjunction (S02, S07, S09, S10, S15, S18) and Distillation (S19) | Delivered as 2.8 and 2.10 record them; dispositions above |
| Phase blocks, Coagulation as overlaid by C-10 (S16, S17; S01 removed) | No PF29 change. PF29 §3.1 (line 213) and §16 (line 976) already state that packaged-wheel admission remains a gap, which delta C-6's "Not delivered" confirms |
| Canon impact, S21 and S22; operative documentation (`AGENTS.md`); ADR; QA requirement; Live QA minimum (C-12) | Elsewhere: T-PF06, T-PF12, T-PF19, the Product Owner and the QA lane. "Any live `--allow-prod-vendor` step is initiated as the Override initiator constraint states" is reflected in RL-007 and RL-011's human-initiator sentence |
| Specification approval block; Implementation Plan approval status; independent QA Plan reference; Material HDE Build Notes references | History and record content: T-PF30.1 |
| X05 rows outside PF29: HDE CLI/API/Vendor Ref §7.1.11 and §7.2.0; the Glow Infrastructure key `HDE_VENDOR_OVERRIDE_AUDIT_PATH`; §7.1.11f "governed clock boundary"; `README.md`, `AGENTS.md`, `docs/RUN.md` | Elsewhere: T-PF05; T-PF07; **held (H-04)**; the repository documents (WU-DOC-01 delivered them, as `docs/CLI_commands.md` on `main` shows) |
| X05 OBS-P4-1 to OBS-P4-7 | Not PF29 content |

### Consistency redline RL-001

RL-002 to RL-014 add or correct repository-dependent statements verified at `0838ba08`, while §1.1's opening paragraph attributes all availability to `e7265a09`. **RL-001** keeps `e7265a09` for every unchanged statement. It names `0838ba08` and the exact statements checked against it (PF03 §4 step 5: one identified snapshot per repository-dependent claim). Its recipe-execution nonclaim stays unchanged and still holds: no recipe was executed.

## Redline summary

| ID | Operation | Section | Original lines | Change type | Source rows |
| --- | --- | --- | --- | --- | --- |
| RL-001 | `REPLACE` | §1.1 opening paragraph | 81 | CONSISTENCY | A08, A10, S-APR |
| RL-002 | `REPLACE` | §1.1 retired-route block | 113 | CANON_UPDATE | A10 with X06 |
| RL-003 | `REPLACE` | §4.1 bind paragraph | 245 | CANON_UPDATE | A08 with X04 |
| RL-004 | `REPLACE` | §6.1 discrepancy paragraph | 341 | CANON_UPDATE | A08 |
| RL-005 | `REPLACE` | §10.1 pair-file paragraph | 637 | CANON_UPDATE | S-APR with X05 |
| RL-006 | `REPLACE` | §11.2 precondition and command | 700–702 | CONSISTENCY | S-APR with X05 |
| RL-007 | `REPLACE` | §13.3 production command | 840 | CONSISTENCY | S-APR with X05 |
| RL-008 | `REPLACE` | §15 Recipe F body | 937–941 | CANON_UPDATE | S-APR with X05 |
| RL-009 | `REPLACE` | §16 unknown-path bullet | 977 | CANON_UPDATE | A08 |
| RL-010 | `REPLACE` | §16 `--dump-reader` and CLI help bullet | 978 | CANON_UPDATE | A08 |
| RL-011 | `REPLACE` | §16 `--allow-prod-vendor` bullet | 979 | CANON_UPDATE | S-APR with X05 |
| RL-012 | `REPLACE` | §16 dev GET `/reader` bullet | 980 | CANON_UPDATE | A08, A10 |
| RL-013 | `REPLACE` | §17 `PROVIDER_CONFIG_INVALID` row, plus one row for the override codes | 999 | CANON_UPDATE | S-APR with X05 |
| RL-014 | `REPLACE` | §18 dry-run lead-in and command | 1047–1049 | CONSISTENCY | S-APR with X05 |
| RL-015 | `REPLACE` | §18 closing paragraph | 1072 | CONSISTENCY | S-APR (consequent on RL-011) |

The redlines file gives each operation's exact OLD and NEW payloads, its controlling basis and its rationale.

## Constraints and interpretations

- **Scope beyond the named sections.** RL-004, RL-006, RL-007, RL-009, RL-010, RL-012, RL-013 and RL-014 edit passages that the ledger row does not name. Each rests on a change the selected units record (2.8 S02, S07, S10; 2.10 S19-F02; S-APR S14), on PF29 §0.2's rule that every described command and availability claim be checked against current repository reality, and on direct inspection of `main`. RL-006 and RL-014 repeat RL-008's fix on the byte-identical command, so the guide does not keep, in two places, a command that S14 makes refuse. RL-007 does the same for the production-like case X05 names ("a production-like one needs the flag").
- **Owner routing.** HDE CLI/API/Vendor Ref owns the override contract, the recognized environment values and the evaluation order. The payloads give only the operator-facing consequences (what to set, which refusal to expect, who may supply the flag) and route the contract to that document by exact title (PF03 §5, §12 "Runnable guides").
- **The production example (RL-007).** The §13.3 command keeps its user placeholder and adds `APP_ENV=prod` and `--allow-prod-vendor <AUTHORIZATION_REF>` as placeholders, with the instruction to set APP_ENV to the environment the process actually runs in. It is labelled \[Operator-authorized only\] by its existing heading. It authorizes nothing, and it carries no reference or credential value.
- **Directed agents.** PF29 §2.2's directed-agent rule is left unchanged. HDE CLI/API/Vendor Ref §7.1.11e makes the override's initiator an authenticated human and states that an AI agent cannot self-authorize by supplying the flag. RL-007 and RL-011 state that limit where the flag is described.
- **Held item H-03.** RL-002 states the retired paths' answer "for every method", which 2.10 and the code establish (the hook checks retired endpoints before the automatic-`OPTIONS` pass-through). It says nothing about the dev-harness paths' router-level `OPTIONS` or redirect answers.
- **Delta 01.** It is read and applied by overlay. It changes none of the relied-on text, so it justified no change.

## Header and metadata provenance for TW-APPLY-10

- **Baseline header** (§0.1 "Header", lines 5–15), in order:
  - Title: `PF29-Canon-HDE-Users-Guide`
  - Version: `v1.0.2`, an unambiguous dotted numeric version with a `v` prefix
  - Status: `Canon`
  - Effective date: `2026-10-09`, format `YYYY-MM-DD`
  - Last Update Gate: `BN 13.5; HDE-EPIC040-specification-v1.1-approved.md; HDE-EPIC040-CL-E-10-closure-decision-v1.2.md`, entries separated by `; `
  - Invocation tag: `INV-f2ac55d77ce9aacc`
- **Sources that justified this update, in source order:**
  1. PF10-HDE-Build-Notes v13.8.8 (`docs/pfcanon/PF10-HDE-Build-Notes-v13.8.8.md`), gate token `BN 13.8.8`. It justifies RL-001 to RL-004, RL-009, RL-010 and RL-012.
  2. `HDE-CRD-0002-specification-v1.1-approved.md`. It justifies RL-001, RL-005 to RL-008, RL-011 and RL-013 to RL-015.
- **Not gate sources:**
  - Delta 01 justified no change.
  - X04, X05 and X06 are supporting cross-references under the ledger, not change sources in their own right.
  - PF03 and PF05 are PF documents read in support.
  - The ledger is never a Last Update Gate.
- **No change-history redline.** PF29 has no change log, revision history or Doc-Delta section, and no rule requiring one.
- **No other restatement.** The target restates its own version and date nowhere outside §0.1; the title carries no version.
- **No status change.** Status `Canon` is not stale.
- **Reserved for Apply.** No redline touches the header.

## Marker and hygiene classification (TW-DRAIN-10 document-control rule)

The complete target was scanned for draft-status language, placeholders, TODO, TBD, FIXME, unresolved drafting notes, editorial comments, instructions to a future writer, ASCII or Unicode ellipses, and restatements of the document's own version or date. No marker requiring removal was found, so this package has no hygiene redline.

| Hit or class | Classification | Disposition |
| --- | --- | --- |
| Command placeholders: `\<user\_a\>`, `\<fixture-chart-a\>`, `YYYY-MM-DD`, `HH:MM`, `"Place"`, `\<production-hde-base-url\>`, `\<same arguments\>`, `approved-user-or-test-id` | Operator input placeholders in examples; PF03 §13 requires obvious placeholders | Kept |
| The "Confirm" and "confirm" operator steps in Recipe F, Recipe G and §17 | Operator steps, not drafting notes | Kept |
| \[Planned, not implemented\] and \[Current gap\] labels | Canon-required availability labels (§0.2, §0.5) | Kept. RL-004 removes the one \[Current gap\] label whose gap S10 closed |
| "no recipe was executed for this revision" (line 81); "not fresh results of this revision" (line 978) | Claim boundaries | Kept; both still hold |

## Validation

Producer validation ran twice:

- **Batch build.** A builder took every OLD block byte-exact from the unchanged original by inclusive line range, and checked each operation and the whole batch.
- **Saved-file revalidation.** A separate parser read only the saved redlines file and the original, extracted every OLD and NEW payload from the fences, and repeated every check.

Both runs agree.

| ID | Original lines | Expected count | Observed (non-overlapping / overlapping) | Complete lines | Heading path unique | Inside section | NEW present and different | Valid |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RL-001 | 81 | 1 | 1 / 1 | yes | yes (2 headings) | yes | yes | yes |
| RL-002 | 113 | 1 | 1 / 1 | yes | yes (2) | yes | yes | yes |
| RL-003 | 245 | 1 | 1 / 1 | yes | yes (2) | yes | yes | yes |
| RL-004 | 341 | 1 | 1 / 1 | yes | yes (2) | yes | yes | yes |
| RL-005 | 637 | 1 | 1 / 1 | yes | yes (2) | yes | yes | yes |
| RL-006 | 700–702 | 1 | 1 / 1 | yes | yes (2) | yes | yes | yes |
| RL-007 | 840 | 1 | 1 / 1 | yes | yes (2) | yes | yes | yes |
| RL-008 | 937–941 | 1 | 1 / 1 | yes | yes (2) | yes | yes | yes |
| RL-009 | 977 | 1 | 1 / 1 | yes | yes (1) | yes | yes | yes |
| RL-010 | 978 | 1 | 1 / 1 | yes | yes (1) | yes | yes | yes |
| RL-011 | 979 | 1 | 1 / 1 | yes | yes (1) | yes | yes | yes |
| RL-012 | 980 | 1 | 1 / 1 | yes | yes (1) | yes | yes | yes |
| RL-013 | 999 | 1 | 1 / 1 | yes | yes (1) | yes | yes | yes |
| RL-014 | 1047–1049 | 1 | 1 / 1 | yes | yes (1) | yes | yes | yes |
| RL-015 | 1072 | 1 | 1 / 1 | yes | yes (1) | yes | yes | yes |

- **Dialect.** All fifteen are `REPLACE` with expected count 1. No `FIND_AND_REPLACE` is used, so RL-045 does not arise.
- **Conflicts.** No two spans intersect. RL-009, RL-010, RL-011 and RL-012 sit on consecutive original lines; each pair is separated by one untouched LF, so they are compatible, and no insertion sits at any of their boundaries.
- **One-pass simulation.** The operations were applied at their original offsets in descending order, without rematching. The result equals the reconstruction from untouched original intervals and payloads: 76,656 bytes, SHA-256 `27659df884b9744842551425fe8eb57422c8d7e5e4aadfba15433bb0f3332eaf`. This is content only; header metadata is Apply's. The parser's application of the saved file gives the same bytes.
- **Payload hygiene.**
  - No NEW payload contains an ellipsis or a trailing space.
  - The longest backtick run in any payload is 1, so the four-backtick fences are safe.
  - No payload contains a secret, a credential, an authorization reference value or production data.
- **Corrections during preparation.** Before the first save, two wordings were refined: RL-013's cause cell, and RL-007's "dry-run included", which became "even for a dry-run". The whole batch was rebuilt and revalidated after the change. After the first save, and before any commit, two "Findings or source items" lines (RL-004 and RL-013) that abbreviated a source quotation with an ellipsis were rewritten in full. No payload changed, and the saved file was rebuilt and revalidated with the same content result. No committed package was revised.
- **Not executed.** No test, recipe, `hdctl` invocation, server, vendor, database or production access. These are text checks, not product QA.

## Unresolved items, limits and observations

- **Blocking items.** None.
- **Held items.** H-03 (LR5-O1) and H-04 (OBS-W4-4) are named by the selected units and left undrafted. H-01, H-02, H-05 and H-06 do not reach PF29's assigned scope. H-02's candidate home includes HDE Users Guide §3.1, which is not touched.
- **Observations for the Product Owner** (not drafted, outside the selected scope or not established):
  - §16 line 978 keeps "the recorded unselected test baseline remain out-of-lane". HDE-CRD-0002 S03 (WU-PR-01, addendum 2.4, not selected for T-PF29) brought previously unselected tests into CI lanes. Whether this clause is stale is not established here.
  - The §1.1 `hdctl bg:resolve` row (line 92) and the §1.2 configured-v2 dry-run row (line 123) summarize without the APP_ENV requirement or the override. They route to §11 and are not false, so they are unchanged.
  - §12.1 lists no audit-sink key. HDE CLI/API/Vendor Ref owns the sink contract and Glow Infrastructure owns key names. On `main`, Glow Infrastructure does not yet list `HDE_VENDOR_OVERRIDE_AUDIT_PATH` (T-PF07 has drafted it); PF29 does not name it.
  - Every availability statement this package does not change still rests on snapshot `e7265a09`, as RL-001 states. A full re-inspection of PF29 is outside this task.

## Correction route

A TW-APPLY-10 diagnostic on this package returns to this preparer, TW-DRAIN-10 in session https://claude.ai/code/session_016STkEGvGYVWWaqSxnj76eo, under run `gtwpe-20261026-pf10-v13-8-8/T-PF29`. A corrected package would carry revision `P2`.

## Save verification

Recorded after both files were read back in full from the working tree of branch `docs/20261026-gtwpe-pf10-v13-8-8-documents`.

- `redlines-PF29-from-v1.0.2.md`: 36,774 bytes, 426 lines, SHA-256 `0a421b03b5654a4d5e0222c00a2d22690e9e365feae2f913afce56bdf8436ea1`. It contains 15 `## RL-` blocks and ends with `END OF REDLINES` and one LF. The independent parser revalidated it.
- This proof log was read back in full after this entry was written. It names its redlines file, run and revision.
- Save completeness: **COMPLETE_PACKAGE**. The commit that holds both files is given in the final response and in the T-PF29 ledger row.
