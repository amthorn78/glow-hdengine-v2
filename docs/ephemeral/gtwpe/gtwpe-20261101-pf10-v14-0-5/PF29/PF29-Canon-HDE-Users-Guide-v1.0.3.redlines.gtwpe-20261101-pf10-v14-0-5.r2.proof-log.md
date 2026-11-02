# Proof log — PF29-Canon-HDE-Users-Guide v1.0.3 redlines, revision r2 — gtwpe-20261101-pf10-v14-0-5 (T-08)

## 1. Artifact and identity

| Field | Value |
| :---- | :---- |
| Artifact this log documents | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF29/PF29-Canon-HDE-Users-Guide-v1.0.3.redlines.gtwpe-20261101-pf10-v14-0-5.r2.md`: seventeen `REPLACE` redlines, RL-01 to RL-17, ending `END OF REDLINES` |
| Run identity | `gtwpe-20261101-pf10-v14-0-5/T-08/drain-r2`, the same in the redlines file |
| Supersedes | `drain-r1`: `PF29-Canon-HDE-Users-Guide-v1.0.3.redlines.gtwpe-20261101-pf10-v14-0-5.md` and its `.proof-log.md`, at commit `285bc728eb3c39de37e6d4842292ea36b421f256`. Both are kept unchanged as history. |
| Commit references | Updated after a rebase onto other sessions' commits, to the pushed hashes: r1 package `285bc728eb3c39de37e6d4842292ea36b421f256`, r1 application `550689fcbb40fb7c7eafa6f42fc9793078d6d5f7`, r2 package `e4506ee5fca18b0203fd81ee4698506aeb98ed4d`, r2 application `e37d0b5731762aaff783261631e3dc00b447e0fa`. The rebase changed no file content; the r2 redlines blob is still `c805c848b69067f06bfdec0e54d1b2034db35d59`. |
| Producing prompt | TW-DRAIN-10 — Prepare PF Document Redlines — 100926.1, Notion page `3f44590a05eb8172a314fe6b958bb9ff`, fetched live on 2026-11-02 ("Prompt Version: 100926.1") |
| Originating preparer | The Claude Code document session Nathan started for T-08, https://claude.ai/code/session_01Q789u3KLSaV6qHFgm3m8t4. It is the same session that prepared r1. No subagent, reviewer or other session took part. |
| Preparation date | 2026-11-02 |
| Preparation outcome | `READY` |
| Save outcome | `COMPLETE_PACKAGE`: the r2 redlines file and this proof log, both read back (§10) |
| Correction route | TW-APPLY-10 validates this package afresh in this session. An Apply diagnostic would return here, to `drain-r3`. |

## 2. Why r2 exists

The r1 package passed TW-APPLY-10 at commit `550689f`, which is kept in history. While I was recording the ledger row, the fetched ledger showed a correction dated 2026-11-02 and a new §8. Both cite GTWPE-D3 in `docs/prompt_ecosystem_management/gtwpe/gtwpe.decision-record.md`. That record has status `BINDING` and rests on Product Owner rulings from 2026-10-07. GTWPE-D3 states:

> all pf docs should be updated based on context and scope, not whether or not the addenda specify a drain target.

It also says: "No document is gated on a drain target or a specification, PF20 and PF30 aside. Every eligible document is updated on context and scope, PF27 among them." The ledger correction quotes Nathan's direction of 2026-11-02: "Just because there is not routing in a sections is NOT grounds for exclusion. You are supposed to analyze by context."

r1's canon search covered `docs/pfcanon/` and the ledger, but not this decision record. Its proof log §6 item 4 left these statements undrafted, with the reason that "neither D-1 nor D-3 names them":

- §7.5 and §9.2;
- the §17 `PROVIDER_CONFIG_INVALID` row;
- the compat lines in §1.1, §1.2 and §7.2.

GTWPE-D3 rejects that reason. r2 redoes the analysis on context and scope. It scans the whole of PF29 for every statement D-1, D-2 or D-3 bears on (§6), and it drains each one. Nathan's handoff authorizes the preparer to correct its own package in this session, after which Apply validates the corrected package afresh. This is that route.

r2 also changes one more r1 decision. r1 kept the §11.3 heading because of PF03 §3 and §8. Under context and scope, r2 retitles it (§7, item 2).

## 3. Sources and inputs

| Role | Identity | Read |
| :---- | :---- | :---- |
| Target (original) | `docs/pfcanon/PF29-Canon-HDE-Users-Guide-v1.0.3.md`, PF29-Canon-HDE-Users-Guide v1.0.3, Status Canon, effective 2026-10-26. Git blob `6730222d2f352221ddbe140a08c260380bbf5abc`; SHA-256 `2ef3b8a7bfabbc768bf0ae1799d29449fe3ecdc37b509a03dd7292f09f0c8301`; 76,613 bytes; 1,079 lines. Read at `e2b7427ff418ca8f08f05587c4a541308a76da56`; the same blob at `origin/main` `84d6d1cad95c67788336d174dc4b8922d9bb0cb2`. | Complete, lines 1–1079 |
| Change source | `docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md`, PF10-HDE-Build-Notes v14.0.5. Blob `9df074d90b59fe783c32f7cb3db25872d5dfe9d2`; SHA-256 `cea605d0475889bd9120a51947e23176ce7d2308eb5ab4503b040fd68ddf669d`. | Addendum 2.1 complete, lines 205–516: D-1 225–276, D-2 277–344, D-3 345–396, and the context 205–224 and 491–516 |
| Governing decision | `docs/prompt_ecosystem_management/gtwpe/gtwpe.decision-record.md` on `origin/main` `84d6d1c`, status `BINDING` | Front matter and GTWPE-D3 and GTWPE-D4 in full (lines 1–20, 114–226) |
| Ledger | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/LEDGER.md` at branch head `aef3266`, including the 2026-11-02 correction and §8. T-08 is unchanged there: rows C-01, C-02, C-03; supporting C-06; hold H-05. | Correction block, §5 and §8 read; T-08 rows compared with `142feb3` |
| Editorial standard | `docs/pfcanon/PF03-Reference-Technical-Writing-Best-Practices-v1.8.8.md`, blob `504712df548a02f3aa4e7b8c37027385e46a3878` | Complete |
| Repository code | Bounded read-only inspection at `e2b7427` under closed rails, with `git show` and `git grep`. The code is byte-identical at `84d6d1c`. | §5 |
| Supporting reading | None. PF05-Canon-HDE-CLI-API-Vendor-Ref and PF04-Canon-HDE-Governance are routed to by title and were not read. | — |

PF10 search outside 2.1, by term only (unchanged from r1): no later addendum amends D-1 to D-3 or adds a PF29 rule for these surfaces.

Canon and rules relied on:

- PF29-Canon-HDE-Users-Guide §0.2 "Scope" (the currency rule), §0.4, §0.5 (`\[Current gap\]`) and §1.1's provenance sentence.
- PF03-Reference-Technical-Writing-Best-Practices §3, §4, §5, §6, §7, §8, §12 "Runnable guides and usage documentation" and §14.
- PF10-HDE-Build-Notes v14.0.5 addendum 2.1.
- GTWPE-D3, which is binding.
- `AGENTS.md`: canon-first search, PF canon read-only, no PF10 section citations inside other PF documents, closed rails.

## 4. Preflight

- The task, scope, identities and branch are unchanged from r1. Branch `claude/gtwpe-triage-authoring-j94ewf`; draft amthorn78/glow-hdengine-v2#826 is open.
- The target and source have not drifted.
- r2's output names carry `.r2` before `.md`, so neither collides with the r1 files, which stay.

## 5. The availability decision

This is unchanged from r1 §4, re-verified at `e2b7427`. None of D-1, D-2 or D-3 is delivered in checked-in code.

| Decision | Checked-in behavior at `e2b7427` |
| :---- | :---- |
| D-1 | `engine/cli/main.py` (blob `77b88602`): lines 52–59, 231–256 and 293–296 accept `--allow-prod-vendor` only on `bg:resolve` and refuse it on every other command with exit 64. Showcompat vendor parties use `source_policy="vendor"` (lines 748–755); conjunction uses `"local" if source in ("db", "auto") else "vendor"` (line 799). `engine/bodygraph/resolver.py` (blob `5f238b9a`): `classify_vendor_environment` (line 73) has one caller, `_resolve_vendor` (line 270), the `bg:resolve` path. Compat acquisition, `resolve_compat_chart` (line 1083) → `_acquire_dry_run` (lines 915–1032), does not classify the environment, apply the override or write an audit event. In compat acquisition, `APP_ENV` is read only by the production-write refusal (lines 523–531), which does not engage on a dry run. In the CLI, `APP_ENV` is read only for the resolver passthrough (line 208) and the dev:sampler gate (lines 833–836, 929). |
| D-2 | `engine/bodygraph/vendor_client.py` (blob `ac980757`): `_configured_base_version` (lines 102–109) case-folds every path segment and picks `v2` if any segment is `v2`, else `v1`. `classify_bg_resolve_route_policy` (lines 124–153) sends every non-`v2` base to `bodygraphs` as `explicit_legacy_fallback`, `supported: True`. The only base check is the HTTPS scheme (lines 296–297, `PROVIDER_CONFIG_MISSING`); the other `urlparse` uses (lines 103, 636) do not validate host, userinfo, query or fragment. `resolver.py` line 704 feeds `bg:resolve` (line 409) and compat acquisition (line 940, then legacy ingest at line 1008). `PROVIDER_ROUTE_UNSUPPORTED` occurs nowhere in runtime code under `engine/` or `adapter/`. |
| D-3 | `engine/http/compat_handler.py` (blob `df9a6e03`) lines 108–120: the route returns 404 only when `_compute_env_mode(os.environ) == "prod"`. `adapter/env_guard.py` (blob `ba0cb043`) lines 31–51 strip and case-fold, pass `staging` and unknown values through, and return `dev` when both variables are unset. The exact-match `_dev_admin_gate` (`adapter/http_reader.py` lines 901–907) is not applied to the compat blueprint (line 1260; also `adapter/factory.py`, `adapter/wsgi.py`). |

Six runtime-code citations in 2.1 still hold at the same lines: `main.py` 799, `resolver.py` 704, `vendor_client.py` 102–109, `compat_handler.py` 112, `env_guard.py` 31–51 and `http_reader.py` 901–907. The test and workflow citations were not re-read.

Decision, as in r1: drain with `\[Current gap\]` qualifiers. Each statement gives the decided rule as canon and the checked-in behavior as the gap. No future date, plan or owner is invented. Static inspection proves checked-in bytes only.

## 6. Contextual scan of PF29 (GTWPE-D3)

PF29 was searched in full for the terms D-1 to D-3 govern:

- `showcompat`, `--source vendor` and `conjunction`;
- `legacy`, `fallback`, `non-v2`, `bodygraphs`, `/v1` and `/v2`;
- `/api/compat/v1`, `ERR_WRITER_FORBIDDEN` and `dev/admin`;
- `--allow-prod-vendor`, `PROVIDER_` and `HD_API_BASE_URL`.

Each search was run in both raw and escaped spellings. Every hit line was read and decided.

| PF29 lines (original) | Bearing | Disposition |
| :---- | :---- | :---- |
| 81 | Provenance of availability claims | RL-01 |
| 86, 217–223, 451, 530, 911 | "Source-tree fallback" means the `scripts/hdctl.py` launcher, a different subject from D-2 | No change |
| 87, 90 | Summary rows: showcompat "depending on flags and rails"; conjunction | No change. The rows stay accurate as summaries, and the detail is drained at §7.5, §9.2 and §13.3. |
| 92 | `bg:resolve` row restates the non-v2 fallback (D-2) | RL-02 |
| 100 | `POST /api/compat/v1` availability row (D-3) | RL-03 |
| 102, 593–629, 965 | Dev HTTP conjunction routes | No change. D-1 covers CLI paths only (PF10 l.229), and D-3 covers the compat namespace. D-2's route selection reaches these routes' resolver acquisition through RL-08's general statement. The §9.3 example is already a closed-rails refusal exercise. |
| 122 | Production-public compat row (D-3, wider exposure) | RL-04 |
| 152, 184, 317, 380, 637, 984, 987, 996, 1007, 1008 | Mention a hit term but no rule D-1 to D-3 decides (closed-rails list, key presence, `DEV_ADMIN_ONLY`, Reader, Aux, legacy CLI stub, QA record, v2 adapter and write rows) | No change |
| 407, 430, 433 | §7.2 route line, curl example, "remains blocked in production" | No change. These lines stay true, and the example runs on the §4.1 harness, which sets `APP_ENV=dev`. |
| 417 | §7.2 method posture: 404 only (D-3) | RL-05 |
| 481–485 | §7.5 showcompat vendor recipe with no `APP_ENV` (D-1 classification; D-2 selection) | RL-06. `APP_ENV=dev` is added to the example. In checked-in code this changes no behavior (§5); under canon it is required. |
| 487 | "Birth-based vendor fallback is prohibited" (`--source auto`) | No change: a different subject from D-2 |
| 566–581, 587, 1046–1048 | File and stdin conjunction; DB conjunction | No change: no vendor acquisition |
| 589 | §9.2 conjunction vendor acquisition (D-1, D-2) | RL-07 |
| 702–708, 1054–1056, 941–947 | `bg:resolve` vendor dry-run, §11.2, Recipe F and §18 | No change. The delivered `bg:resolve` gate is accurate. "Configured v2 base" now takes its meaning from §11.3. |
| 710–714 | §11.3 heading and body (D-2 supersedes the section) | RL-08 |
| 716–734, 949–957, 1058–1064 | v2 mapped-cache persistence | No change: configured-v2 only |
| 742–761 | §12.1 keys; §12.2 legacy v1 route table | No change. The legacy v1 table is consistent with terminal-v1 selection. |
| 771 | §12.2 "configured HD\_API\_BASE\_URL owns any vendor API version prefix" (D-2 base boundary) | RL-09 |
| 820–834 | §13.2 production compat posture (D-3) | Already represented. Lines 824–832 limit production compat to internal, CLI or "future explicit production contract after canon and implementation change", and "PF29 does not create that production public endpoint". That is equivalent to D-3's wider-exposure rule for the production posture, and its 404 statement stays true. |
| 838 | §13.3 non-v2 fallback sentence (D-2) | RL-10 |
| 840–846 | §13.3 v2 persistence and the delivered `bg:resolve` override | No change: accurate |
| 848 | §13.3 last paragraph (D-1 placement; D-2 sentence) | RL-11 |
| 963 | §16 compat nonclaim (D-3) | RL-12 |
| 969 | §16 non-v2 fallback nonclaim (D-2) | RL-13 |
| 985 | §16 override limit (D-1) | RL-14 |
| 986 | §16 dev-route gates | No change. The compat route is handled at line 963 (RL-12). |
| 998 | §17 compat 404 row (D-3) | RL-15 |
| 1002–1004 | `PROVIDER_REFUSED`, `PROVIDER_NETWORK_BLOCKED`, `PROVIDER_CONFIG_MISSING` rows | No change. D-2 names no code for boundary violations beyond route shapes; PF05 owns that, and the HTTPS row stays true. |
| 1005 | §17 `PROVIDER_CONFIG_INVALID` row (D-1 classification) | RL-16 |
| 1006 | §17 override row (D-1) | RL-17 |
| 1044, 1079 | §18 compat curl; closing note | No change |
| No line | A troubleshooting row for `PROVIDER_ROUTE_UNSUPPORTED` | Not added. Checked-in runtime never emits the code, so operators can meet no such symptom today. RL-08 documents the code and its gap where the route rule lives. |

## 7. Change ledger by source item

All r1 dispositions stand, except those r2 changes below. r2 adds the following drains, on context and scope:

- D-1 (C-01): RL-06 (§7.5), RL-07 (§9.2) and RL-16 (§17, `PROVIDER_CONFIG_INVALID`). The operator-facing consequence at PF10 l.272 ("Open-rails showcompat tests with an absent or unrecognized environment now refuse with PROVIDER\_CONFIG\_INVALID") drains into all three, besides RL-11.
- D-2 (C-02): RL-06 and RL-07 (compat acquisition route selection, l.281–283), and RL-09 (§12.2 configured-base boundary, l.285–287). The boundary is routed to PF05-Canon-HDE-CLI-API-Vendor-Ref, with the gap stated: only the HTTPS scheme is checked.
- D-3 (C-03): RL-03 (§1.1 row), RL-04 (§1.2 wider exposure, l.359–361) and RL-05 (§7.2 refusal, l.350–354). §13.2 is already represented (§6).

Unchanged from r1:

- the D-1 audit command-field values (l.241) are PF05-owned;
- v1 retirement (l.288, l.343) is left undecided;
- the residual-risk record (l.362–364) is governance;
- test and evidence consequences belong to the implementing change;
- canon superseded in PF04, PF05, PF14 and PF27 belongs to T-01, T-02, T-05 and T-07;
- the PF05 §7.2.0 gap is H-09, and item 9 is H-10.

Other items:

1. Mapping from r1 to r2 IDs. r1 RL-01→RL-01, RL-02→RL-02, RL-03→RL-08, RL-04→RL-10, RL-05→RL-11, RL-06→RL-12, RL-07→RL-13, RL-08→RL-14, RL-09→RL-15, RL-10→RL-17. RL-03 to RL-07, RL-09 and RL-16 are new. Every carried-over payload is byte-identical to r1, except:
   - RL-01, whose provenance list now names every section with a new gap statement;
   - RL-08, which r1's RL-03 (lines 712–714) widened to lines 710–714 to include the heading.
2. The §11.3 heading becomes "Terminal-v1 legacy BodyGraph route \[Implemented\] \[Operator-authorized only\]". PF03 §8 keeps headings "unless the requested change explicitly authorizes otherwise". D-2 supersedes "HDE Users Guide §11.3" as a section (l.314), with no quoted sentence, unlike its §13.3 and §16 entries. Under GTWPE-D3 that supersession is read on context and scope, and the old title "Non-v2 legacy fallback" states the superseded rule. These stay as they were: the number, level, order and boundaries, and the availability labels. The terminal-v1 route is implemented. No canon file cites the old title (searched with `git grep` in `docs/pfcanon/` on `origin/main`). Nathan can reject the retitle in review without affecting any other redline.
3. The PF10 section labels "§16" for the troubleshooting rows resolve to PF29 §17, as in r1.
4. Handoff destinations. The handoff names §11.3, §13.3, §16 and the two rows. GTWPE-D3 treats named targets as a floor, not a gate, so RL-01 to RL-07, RL-09 and RL-16 are in scope.

## 8. Held and outside dependencies

| ID | Item | Waits for |
| :---- | :---- | :---- |
| H-05 | AGENTS.md edits under D-1 ("Showcompat Live QA posture"; PF10 l.266) and D-2 ("EPIC036 docs posture" and the EPIC038 posture lines; l.324). Not a PF target. | The Product Owner's explicit instruction to edit AGENTS.md (PF10 l.507; ledger §5 H-05). Not drafted. |

Nothing else blocks the package. When item 9 (H-10) is delivered, the `\[Current gap\]` statements become stale; that is a later drain, not a blocker.

## 9. Producer validation

The batch was validated against the unchanged original from the r2 specification. It was validated again by an independent parse of the saved r2 file. The two runs agree.

| r2 ID | r1 ID | Section | Lines | Byte span | Expected | Observed | OLD SHA-256 | NEW SHA-256 |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| RL-01 | RL-01 | §1.1 | 81–81 | 4703–5484 | 1 | 1 | `f7d1b43b0a92152161bc7655658f2fade7a31aa0334e61c907feb162d3f0577a` | `ce79e5a9fb2dd786a593ff0139118411c7bffee4af7f4fcf552ac897934b498b` |
| RL-02 | RL-02 | §1.1 | 92–92 | 6366–6937 | 1 | 1 | `e6c74c061f99e99fefd4c665b5b44865679e186cb8644feaca1db33cd417749b` | `08aa5f21f890730387085b4600ac4be37a3868a03048b44ddfc4c10287b317f4` |
| RL-03 | new | §1.1 | 100–100 | 8014–8128 | 1 | 1 | `01504ae390787c91d81a6dfe0088598b069632acf6608bd3d01404f3b8e014f9` | `c3118430cb2012171b78936c255152edc7f32736f7e65a496002428249cda855` |
| RL-04 | new | §1.2 | 122–122 | 10409–10637 | 1 | 1 | `db466f247453e104692900089c670c6b6325caa8aabb74920dc281bb844e36c6` | `c588317c6ab33d017840dff40dc561fb81ba838847fb796f4ecede5d8787f2c9` |
| RL-05 | new | §7.2 | 417–417 | 26485–26655 | 1 | 1 | `b690426e23cf356b308a867dbe7fbffef3e8f90d8f5e84350287cbf446d806f4` | `320e329797a3c3783fd40c390206b7bb40f2205408a75b04c682a933b251493a` |
| RL-06 | new | §7.5 | 483–485 | 30665–31175 | 1 | 1 | `49eeebb9b4656565c6fa9dd5bab6d264d791921e8bf967da19e8fb2f3492f466` | `5bc7d8fdbf53b57d0fc86742a2e47c767e57dee43b151abfd1327bd49e409749` |
| RL-07 | new | §9.2 | 589–589 | 38496–39001 | 1 | 1 | `5fc61b9c4dff85cc46fc5d911d0d1f17b06c20e4e0c4431f040166d02f414518` | `23028d6450603ff0c55e7861fed9dad95e8b71cdb565765708c3ed9901b4a45c` |
| RL-08 | RL-03 | §11.3 | 710–714 | 45075–45552 | 1 | 1 | `f54594bc0c7d738ba0ad7cd80a1ddb3f4c9aedf1560d66a06b3705049b0ea201` | `9492ca7e2d3b660f8e6d5e6174a9087a1357e6996f6d93179dcfa4b39416e0f6` |
| RL-09 | new | §12.2 | 771–771 | 49464–49651 | 1 | 1 | `3e472add32fd4cf2c72e8b2428cded926c9f54e9763b01b13cf5496601c8bb96` | `4c37357620d7e4c1487db579aaa4607e4cd46e07e4cd96637aa75e651d7c5c9f` |
| RL-10 | RL-04 | §13.3 | 838–838 | 51927–52296 | 1 | 1 | `3471cf41575a62d6058f2e155c1a751a89e92f6b17bb5cc0fc741d2a007aec4c` | `1571d7733e81754901426c51a0b2bca517fdd329859fe258966b23ec7a8f5a8b` |
| RL-11 | RL-05 | §13.3 | 848–848 | 54032–54153 | 1 | 1 | `7679268e2411da0ba69abf26fd0f53ad9350fab58fd4060d4f9daad168e9ee2c` | `9586e5aba82fe5090b75f2eaf86ccfd4445ba408cd3d21daa8b19a0211065117` |
| RL-12 | RL-06 | §16 | 963–963 | 62304–62506 | 1 | 1 | `ae508d574029fa5ab2a41a18b2d298f3967f692440f4a60146beec75203543e4` | `8ba7ed3293917dee1e25c6c0df5cc0a32d87a80a8886874b73ae2ace2d7cd45d` |
| RL-13 | RL-07 | §16 | 969–969 | 62691–62916 | 1 | 1 | `f39d3d56b1eea1f06c4371b498699337b6b86bff9385f8c9d9c9ec11ed1e0cd0` | `9d8025d8ea2efe77c695552775478e7933fe5e8a588a1fceee275d260c9c3aea` |
| RL-14 | RL-08 | §16 | 985–985 | 65513–66146 | 1 | 1 | `101362406db21e77b55803095ea7ab5cc40217910907232685a2ec1e919f5080` | `d3f92993fbab037e5f8fb573900bdeb48133fdd5b7424157f06a860994e8d920` |
| RL-15 | RL-09 | §17 | 998–998 | 67682–67849 | 1 | 1 | `cf1ff9c0fe98003092ff44235d25d13273aad19621fe88e0a023142ef598a537` | `e127634725fdcf40ee6d4dce9fd529f619ce063233fdd8060be266d0634c0c55` |
| RL-16 | new | §17 | 1005–1005 | 68913–69327 | 1 | 1 | `a253c3037e3e2fe2320e5378364bb4243a44a24bcdc3d88a3a24c5028909254a` | `99d339c4d7ea8058450e4e5f85c260afe1ad4c615b66b60db29049ec7055eeda` |
| RL-17 | RL-10 | §17 | 1006–1006 | 69328–69846 | 1 | 1 | `15a9aa873e6dfe546be9837b0c5d8d72aaf765d8e68de6fb2068c20e335f6ef3` | `4bd7b5d64ca19dcb190289dee18c589b58358a674706011eb5bb2c2c32914998` |

Checks run and their results:

- Operation dialect: all seventeen are `REPLACE`, with expected and observed occurrence 1. No repeated-replacement operation is used, so RL-045 is not engaged.
- Line bounds: every OLD block is line-bounded, and its resolved lines match the stated location.
- Overlap: spans are strictly disjoint. RL-16 ends at byte 69,327 and RL-17 starts at 69,328; the original line feed between them is untouched.
- Payloads: non-empty, different from OLD, no backtick-fence line, no ASCII or Unicode ellipsis.
- Heading-path lines: each occurs exactly once in the original.
- One-pass simulation:
  - each NEW block occurs exactly once;
  - these superseded literals occur zero times: "Non-v2 configured bases preserve explicit legacy BodyGraph fallback", "explicit legacy BodyGraph fallback is preserved", "With a non-v2 configured base, explicit legacy fallback may proceed", "For non-v2 legacy fallback", "any supported non-v2 legacy fallback", "Non-v2 legacy fallback", and the §7.5 command without `APP_ENV`;
  - the body before the header change has SHA-256 `785e0ec09d177672edf11d5d53e675cc2b8af137b06e8165523767c2c33f59da`, 83,897 bytes, 1,087 lines.
- Corrections inside r2 before saving: RL-03's wording now covers an unset `APP_ENV`, and RL-07's gap marker gained its section cross-references. The whole batch was revalidated after each.

These checks establish the package's editorial and mechanical condition only. They are not CI, QA or governed evidence.

## 10. Save verification

| File | Bytes | SHA-256 | Read back |
| :---- | :---- | :---- | :---- |
| `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF29/PF29-Canon-HDE-Users-Guide-v1.0.3.redlines.gtwpe-20261101-pf10-v14-0-5.r2.md` | 33,181 | `bf546c175417fc12fd4c78cadf23a5363a27174634da9d8eb230685903f01197` | Complete, 464 lines ending `END OF REDLINES`. Parsed whole and revalidated; identity, metadata and payload fields reviewed. |
| This proof log | — | — | Complete, after writing. No self-referential hash. |

## 11. Next step

TW-APPLY-10 100926.1 (page `3f44590a05eb81eebff6e3afa3d9aa5b`) runs next in this session, on this r2 package against the unchanged original at `e2b7427`. Its final output stays `PF29-Canon-HDE-Users-Guide-v1.0.4.md`, with its `.proof-log` beside it. It supersedes the r1 application output at commit `550689f`, which is kept in git history.
