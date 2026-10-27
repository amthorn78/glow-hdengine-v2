# Promotion packet — GCFPE-20261027.1 / 102726.1

`MODIFICATION-20261027-gcfpe-backlog-open-items`, X18 (PLAN §3 PART-24, §7; DN-1 D2). This is the exact snapshot Nathan is asked to approve for promotion. Approving it authorizes PART-25, X19 to X28, as PLAN §7 and §8 state, with the amendments AM-1 to AM-8 recorded in §E and AM-9 if you approve it (§6), and nothing else. Until then nothing of PART-25 is done: no control binding, no new page, no register change, no install, no archive move. Written by `execute/x18_packet_102726.py` from the receipts it names; `--check` reproduces it.

## 1. The promotion predicates (the register's own)

| # | Predicate | State | Evidence |
|---|---|---|---|
| 1 | Complete behaviour validation of the exact pinned snapshot | met | `docs/ephemeral/modifications/evidence/20261027-gcfpe-backlog-open-items/execute/x14r-bodies-102726.1.json`: the shipped 102726.1 validators over all 56 member bodies, none unevaluated, `ok` true; fixtures with the bodies 323 cases, without 297, none failed; the flowmaster suite with no finding from this change (C-21); text form `normalize_fetch.normalize (C-15)`; both D28 roots identical. `docs/ephemeral/modifications/evidence/20261027-gcfpe-backlog-open-items/execute/x15-registry-102726.1.json`: the candidate registry's assertions on fresh reads, 56 of 56 rows, every operation landed, 972 injected regressions all reported |
| 2 | Independent post-flight `PASS` or `PASS WITH WARNINGS`, no mandatory open finding | met | `execute/REVIEW-POSTFLIGHT-A.md`: PASS WITH WARNINGS — 0 mandatory open findings (4 other findings); `execute/REVIEW-POSTFLIGHT-B.md`: PASS WITH WARNINGS — 0 mandatory open findings (4 other findings) |
| 3 | Nathan / Product Owner's separate approval of this snapshot | **open** | requested in §8 |

## 2. The snapshot

**Notion — the 56 members and PE**, at the page ids of `execute/successor-pages-102726.1.json`, each at its X7 revision (`execute/landing-check-102726.1.json`). X14's fresh reads after 2026-10-27T20:14:34.643Z found no member moved since (`moved_since_landing_check` empty).

| prompt | disposition | page id | revision |
|---|---|---|---|
| CF-C-10 | SUCCESSOR | `4064590a05eb811e821bc064f56de3a3` | `2026-10-27T13:17:07.203Z` |
| CF-C-20 | SUCCESSOR | `4064590a05eb811f8305e12dc130b197` | `2026-10-27T13:11:25.235Z` |
| CF-C-30 | SUCCESSOR | `4064590a05eb81c1846df3512494d51d` | `2026-10-27T13:03:01.779Z` |
| CF-C-40 | SUCCESSOR | `4064590a05eb81c5851deb1cf765e49b` | `2026-10-27T13:11:03.196Z` |
| CF-E-10 | SUCCESSOR | `4064590a05eb81a0a3a8e043017dffbb` | `2026-10-27T13:22:24.392Z` |
| CF-E-20 | SUCCESSOR | `4064590a05eb8129a159df9439b4e922` | `2026-10-27T13:16:44.645Z` |
| CF-E-30 | SUCCESSOR | `4064590a05eb81a88f00d49a698027bb` | `2026-10-27T13:21:53.464Z` |
| CF-E-40 | SUCCESSOR | `4064590a05eb8113a64dda1a380c1b96` | `2026-10-27T13:17:15.163Z` |
| CF-PO-10 | SUCCESSOR | `4064590a05eb81809a74c181d50922eb` | `2026-10-27T13:22:27.779Z` |
| CL-05 | ADDED | `4064590a05eb814fba57ed387ee2cddd` | `2026-10-27T13:19:06.175Z` |
| CL-20 | SUCCESSOR | `4064590a05eb81c28ac8ff12b072826b` | `2026-10-27T13:15:06.100Z` |
| CL-30 | SUCCESSOR | `4064590a05eb81c1b64cfe813b3c0819` | `2026-10-27T13:20:49.487Z` |
| CL-40 | SUCCESSOR | `4064590a05eb81e18744cabb341b0113` | `2026-10-27T13:13:23.717Z` |
| CL-C-10 | SUCCESSOR | `4064590a05eb81119e59dd3b3b835f24` | `2026-10-27T13:14:18.752Z` |
| CL-E-10 | SUCCESSOR | `4064590a05eb813990f7d29936a6b205` | `2026-10-27T13:14:18.647Z` |
| CL-E-20 | SUCCESSOR | `4064590a05eb819f9a30f9d51249a91c` | `2026-10-27T13:21:34.064Z` |
| CL-E-30 | SUCCESSOR | `4064590a05eb81e58a4efd0845689472` | `2026-10-27T13:16:18.362Z` |
| CL-E-40 | SUCCESSOR | `4064590a05eb81a6a86ccb922e99db36` | `2026-10-27T13:10:18.917Z` |
| DOC-10 | SUCCESSOR | `4064590a05eb81b3a8b5dad3b0c20ed1` | `2026-10-27T13:19:44.974Z` |
| DOC-20 | SUCCESSOR | `4064590a05eb810a8895f107fe9e1679` | `2026-10-27T13:08:47.827Z` |
| ESC-10 | SUCCESSOR | `4064590a05eb819f949fd8f201e0a8b6` | `2026-10-27T13:11:05.410Z` |
| ESC-25 | SUCCESSOR | `4064590a05eb815ba64ef9ebfb75eb80` | `2026-10-27T13:09:50.459Z` |
| ESC-30 | SUCCESSOR | `4064590a05eb814284b9cd1450419bfb` | `2026-10-27T13:10:40.161Z` |
| ESC-40 | SUCCESSOR | `4064590a05eb81eb8d3ced2d01c3c108` | `2026-10-27T13:10:06.373Z` |
| GCFPE-MGMT-10 | KEPT | `3f74590a05eb81b69bd8c27106f7a59d` | `2026-10-12T02:30:05.584Z` |
| IA-10 | SUCCESSOR | `4064590a05eb813281cbc25f2f30db13` | `2026-10-27T13:16:07.631Z` |
| IA-20 | SUCCESSOR | `4064590a05eb81db9c6befccd5e520f1` | `2026-10-27T13:22:04.218Z` |
| IA-30 | SUCCESSOR | `4064590a05eb81ebb110fb0202874d8c` | `2026-10-27T13:21:07.780Z` |
| IA-40 | SUCCESSOR | `4064590a05eb81a5a137f6912fba26b9` | `2026-10-27T13:16:58.421Z` |
| IA-50 | SUCCESSOR | `4064590a05eb81d2b388fde42922edc7` | `2026-10-27T13:16:39.527Z` |
| IA-60 | SUCCESSOR | `4064590a05eb818498a9faf265f7129c` | `2026-10-27T13:22:09.622Z` |
| MGR-10 | SUCCESSOR | `4064590a05eb812cac4cfa7143f53d36` | `2026-10-27T13:15:48.337Z` |
| OPS-10 | SUCCESSOR | `4064590a05eb81fab31ef7c8921fc312` | `2026-10-27T13:12:27.044Z` |
| OPS-20 | SUCCESSOR | `4064590a05eb81c18158d838050befbc` | `2026-10-27T13:12:54.383Z` |
| OPS-30 | SUCCESSOR | `4064590a05eb813b8c9bdd5d92cd6cde` | `2026-10-27T13:07:41.085Z` |
| PR-10 | SUCCESSOR | `4064590a05eb81de9686f14e4693b315` | `2026-10-27T13:19:04.774Z` |
| PR-20 | SUCCESSOR | `4064590a05eb8141a25be9a48df6c2a9` | `2026-10-27T13:18:23.839Z` |
| PR-30 | SUCCESSOR | `4064590a05eb8157bcb9c79a43cefb08` | `2026-10-27T13:15:20.197Z` |
| PR-35 | SUCCESSOR | `4064590a05eb8108a9f5cececa4b3149` | `2026-10-27T13:13:39.046Z` |
| PR-40 | SUCCESSOR | `4064590a05eb81479a74fa542b90cadb` | `2026-10-27T13:18:21.343Z` |
| PR-50 | SUCCESSOR | `4064590a05eb81dcbf95e23b4112e43c` | `2026-10-27T13:01:37.364Z` |
| QA-10 | SUCCESSOR | `4064590a05eb8161b170fbb23f7aeb28` | `2026-10-27T13:07:31.843Z` |
| QA-100 | SUCCESSOR | `4064590a05eb8150bcfff1e25129b368` | `2026-10-27T13:21:17.380Z` |
| QA-110 | SUCCESSOR | `4064590a05eb81719360c698e54b260c` | `2026-10-27T13:09:31.094Z` |
| QA-120 | SUCCESSOR | `4064590a05eb810ea503f98b34fa85aa` | `2026-10-27T13:20:19.853Z` |
| QA-20 | SUCCESSOR | `4064590a05eb810ca861ff615ddb7e79` | `2026-10-27T13:14:52.288Z` |
| QA-50 | SUCCESSOR | `4064590a05eb81dbb28ed028d68b8816` | `2026-10-27T13:08:15.848Z` |
| QA-60 | SUCCESSOR | `4064590a05eb81c4b5fcde0e9e5a6fa9` | `2026-10-27T13:20:05.824Z` |
| QA-70 | SUCCESSOR | `4064590a05eb819ca94af85f1561b596` | `2026-10-27T13:19:35.915Z` |
| QA-80 | SUCCESSOR | `4064590a05eb81708849ef4ce804753b` | `2026-10-27T13:09:00.512Z` |
| QA-90 | SUCCESSOR | `4064590a05eb81929057e6667f7193c6` | `2026-10-27T13:15:43.099Z` |
| RS-10 | SUCCESSOR | `4064590a05eb81e3ab0de978fbd97b2f` | `2026-10-27T13:21:43.767Z` |
| RS-20 | SUCCESSOR | `4064590a05eb81e3bcdddac78d3027da` | `2026-10-27T13:20:37.196Z` |
| RS-30 | SUCCESSOR | `4064590a05eb813eb33ce2fdc351092b` | `2026-10-27T13:10:44.942Z` |
| RS-40 | SUCCESSOR | `4064590a05eb813b9234f34caeb67537` | `2026-10-27T13:08:26.035Z` |
| UTIL-10 | SUCCESSOR | `4064590a05eb8147b104c0998060ae6f` | `2026-10-27T13:11:38.789Z` |
| PE | SUCCESSOR | `4064590a05eb8173b2e7d37929e7fe4d` | `2026-10-27T13:09:24.084Z` |

**The four skill packages** (`execute/x13r-packages-102726.1.json`; built by `execute/package_build_102726.py`, reproducible with `check`). The `.skill` files for installation are in `/tmp/claude-0/-home-user-glow-hdengine-v2/0940370d-6cc4-5605-b6f0-1f6824e675b3/scratchpad/review-d24`. They install together, at X22, after the register selects GCFPE-20261027.1.

| package | `.skill` sha256 | bytes | tree (`freeze.py`) |
|---|---|---|---|
| change-flow | `695c055a06517274d68d521055341f80fae31d066c9b676c003f434a5f699883` | 538,904 | `29 672f3cbb133092bee896d157c62deff8bb559dae446687ae1fd15ebbb07f74e0` |
| flowmaster-validate | `b334e067b0c72ecdbec45ed22b4813139b939aea90cff4a3706351b7116a73ee` | 721,634 | `45 72dbdbc673971d05d0b02bb05e57080e2a99368cde67cae51301303e3c2a85da` |
| glow-hde-pr-development | `8452f6e12dcd36e7094fdbb8c4e15be341e56098fac0834615e3f4e152b63456` | 26,085 | `4 af32b2f146d9395b37f82c7db6a14296b159311f2b810f17b8cc90366e7bcbee` |
| glow-graph-contract | `4364d082b447ada548a69e90191a7d867a731c58ca06dabf61e907bf8a6b37cd` | 58,987 | `9 b0d012108b673ea7279bd75088947e65efb8440274a1703c2579b74bbfdfb3b1` |

Advertised revisions: change-flow 3.5.0, flowmaster-validate 3.5.0 (`SKILL_TREE_SHA256` `e5723d286cecc4768050e76d64e03a4f59dd67ca1900c2aa5c18da348bb19779`), glow-hde-pr-development 1.5.0; glow-graph-contract advertises none.

**The five unchanged skills** (installed; X13r's trees, `freeze.py`, D28 name-line form). P0 and P3 compare all nine digests, these and the four above.

| skill | tree |
|---|---|
| amthor-workspace-governance-audit | `15 f0f00820a1df24d20974dd3ad1a58bc4cb8d358d6e7b9a77ccd9ec26329e45f8` |
| session-relay-flowmaster | `5 33d8b9be98288b1ba698a403964409fb65f5cc53d81cbd94a348ff5b3ce4b52c` |
| glow-write-boundary | `1 662f9647ccfd996aa72e3d80ac70edc3d06a4310805ef14207b1340c69e93fc4` |
| typesafe-scoring | `3 8e26b0554e3ff37c0ae6ae0fa4d5242d5823fc6fd1f7514ebe10137d27d25523` |
| glow-merged-change-attribution-lock | `10 c518ccb0076b042859de4d2e136ef682bb127b6524133d2a575d433490eaf48f` |

**The successor map** `execute/successor-pages-102726.1.json`: 27,601 B, sha256 `f45a880de8b6fe597b69419a6f33ad92776693dad779877fc0c2eda186d6b1b8` (written once at X3; P0 compares it).

**Contracts and graph**

| artifact | identity |
|---|---|
| production contract (bundled in change-flow and flowmaster-validate) | 646,249 B, sha256 `f5dfa63f3f0b1c0dc3a55e647dffeee8da70f7500e46df40242b80c09c4c0b5d`, `SELECTED_PRODUCTION`; regenerated byte for byte by the patched regenerator (X13r G5) |
| candidate contract | 649,674 B, sha256 `3527775d675733ff0e6163505b6ea283d76998a3a1ecf44d997fef0387026b1e` |
| candidate graph | 56 nodes · 240 edges · 56 state_routes · 608,051 bytes · sha256 `e17d4e6ad78f7c925a4207f764a941da6dd2c75690c38fdfa35b6c5baeb91b5a` |
| production graph (written to `docs/graph/parts/` at X26) | 56 nodes · 240 edges · 56 state_routes · 607,994 bytes · sha256 `2342744dc1d9de9d8bfad34bdc3d5edd244afbc7f428c8706cae3d56e90e1d41` |
| governing plan (pinned by both contracts) | `PLAN-20261027.md`, 84,106 B, sha256 `a3b11f4668b166c462158bdca836a0856b87b7e09adff4380e3a9b46320023e2` |

**Registry.** Candidate stage `execute/candidate-registry.md`, 1,419,546 B, sha256 `137a911eda1e782b3de4a1d76eaa7463d940a43b38bdaf8824e52b1c4b100e52`, 56 rows. X26 writes the selected stage with `registry_assemble_102726.py build --stage selected`, which differs from the candidate only at approved_at, approved_by, status (`compare`).

**The activation.** `plan/activation-ops.json` sha256 `ccc2d9e54c081950d5ffec79722de8ba288ccd247f8d9c87567b6b87f361ea6c`, `plan/activation_render_102726.py` sha256 `752a5aa5887437062e12f7c7af3964cd9f7cb34404700ae26908326180ca2495`, `plan/control_check_102726.py` sha256 `6622a2befea2b4eef922de7caf899f9d7e156d3f467d954dc0a5c47f70bc0a89`, with AM-3 to AM-7 (record §E). The operating procedure it binds at P2: `docs/ephemeral/GCFPE-Direct-Handoff-and-Runtime-Artifact-Operating-Procedure-v5.1.0-20261027.md` on `main` (5,376 B, sha256 `0abe16d23d251e37061cfe82d7540eece19096c0c440afa45ba49ac0bfe066e9`), landed by pull request #770 (`5b3ccdcc`); `reviewer-prompt-template.md` at 1.3; the note after D30 present (`execute/x18-controls-main-102726.1.json`).

## 3. The reviews

| review | brief | records and verdicts |
|---|---|---|
| D24 (X16) | `execute/BRIEF-D24.md` (`267d806d`) | `REVIEW-D24-A.md`: SKILL_FIT_CONFIRMED — 0 REQUIRED findings (1 LISTED); `REVIEW-D24-B.md`: SKILL_FIT_CONFIRMED — 0 REQUIRED findings (2 LISTED) |
| post-flight (X17) | `execute/BRIEF-POSTFLIGHT.md` (`2e398691`) | `REVIEW-POSTFLIGHT-A.md`: PASS WITH WARNINGS — 0 mandatory open findings (4 other findings); `REVIEW-POSTFLIGHT-B.md`: PASS WITH WARNINGS — 0 mandatory open findings (4 other findings) |

## 4. Activation markers and pins

| marker | value |
|---|---|
| `@PUBLICATION_DATE` | `2026-10-27` (X9, C3) |
| `@CONTROLS_PR` | `770` (X1, `execute/controls-pr-102726.1.json`) |
| `@CATALOG_PAGE_ID` | `4064590a05eb8113ae7de73041631c00` (X9, C-CAT, `execute/notion-controls-102726.1.json`) |
| `@PE_PAGE_ID` | `4064590a05eb8173b2e7d37929e7fe4d` (the successor map) |
| `@PRODUCTION_TOKEN` | `56 nodes · 240 edges · 56 state_routes · 607,994 bytes · sha256 2342744dc1d9de9d8bfad34bdc3d5edd244afbc7f428c8706cae3d56e90e1d41` (X11) |
| `@PROMOTION_D` | `D31` (RE-W7-11) |
| `@PROCEDURE_PR` | `770` (v5.1.0 landed by it; `execute/x18-controls-main-102726.1.json`) |
| `@PACKET_PATH` | `docs/ephemeral/modifications/evidence/20261027-gcfpe-backlog-open-items/execute/PROMOTION-PACKET.md` |
| `@QUAL_VALIDATORS_PATH` | `docs/ephemeral/modifications/evidence/20261027-gcfpe-backlog-open-items/execute/x14r-bodies-102726.1.json` |
| `@QUAL_FIXTURES_PATH` | `docs/ephemeral/modifications/evidence/20261027-gcfpe-backlog-open-items/execute/x14r-bodies-102726.1.json` |
| `@QUAL_RECEIPT_PATHS` | `<code>docs/ephemeral/modifications/evidence/20261027-gcfpe-backlog-open-items/execute/x14r-bodies-102726.1.json</code> (the shipped validators and fixtures over the 56 bodies) and <code>docs/ephemeral/modifications/evidence/20261027-gcfpe-backlog-open-items/execute/x15-registry-102726.1.json</code> (the registry's assertions)` |
| `@D24_RECORDS` | `<code>docs/ephemeral/modifications/evidence/20261027-gcfpe-backlog-open-items/execute/REVIEW-D24-A.md</code> and <code>docs/ephemeral/modifications/evidence/20261027-gcfpe-backlog-open-items/execute/REVIEW-D24-B.md</code>: both <code>SKILL_FIT_CONFIRMED</code>, 0 required findings, on the four packages' digests; their listed findings are in the promotion packet` |
| `@POSTFLIGHT_VERDICT` | `<code>docs/ephemeral/modifications/evidence/20261027-gcfpe-backlog-open-items/execute/REVIEW-POSTFLIGHT-A.md</code> (<code>PASS WITH WARNINGS</code>) and <code>docs/ephemeral/modifications/evidence/20261027-gcfpe-backlog-open-items/execute/REVIEW-POSTFLIGHT-B.md</code> (<code>PASS WITH WARNINGS</code>)` |
| `@PROMOTION_APPROVED_AT` | **remaining**: the UTC date of your approval, quoted in §E |
| `@ACTIVATION_DATE` | **remaining**: the UTC date P1 starts |
| `@REGISTER_ENTRY_PAGE_ID` | **remaining**: the page P1(a) creates |
| `@REGISTER_SELECTED_AT` | **remaining**: the register's revision after P2 |
| `@ARCHIVAL_DATE` | **remaining**: the UTC date P5 completes |
| `@INSTALL_RECEIPT` | **remaining**: X22's receipt |
| `@PRODVAL_RECEIPT` | **remaining**: X23's receipt |
| `@ARCHIVAL_RECEIPT` | **remaining**: X24's receipt |

**Pins** (each control page's revision as read at X18 after C-FI-REV, `execute/x18-check-102726.1.json`):

| page | id | revision |
|---|---|---|
| HDE Change Flow Overview | `3c74590a05eb811d8433e7022629e213` | `2026-10-12T17:34:33.909Z` |
| Glow Operations Hub | `3ce4590a05eb814f8892f88ff8539308` | `2026-10-27T14:22:01.528Z` |
| register | `3d24590a05eb81ce942ad994cfca9fa1` | `2026-10-27T15:35:32.914Z` |
| hub HDE TW | `3db4590a05eb811b9c14f2ae89c28df7` | `2026-10-27T15:35:23.456Z` |
| Alpha checklist | `3db4590a05eb812f87caed515836687f` | `2026-10-12T13:37:58.821Z` |
| hub HDE QA | `3db4590a05eb814d96d3dcfa8835f96d` | `2026-10-27T15:35:17.895Z` |
| hub HDE IA | `3db4590a05eb8195a2ccf7c0959a8b6e` | `2026-10-27T15:35:15.062Z` |
| hub Escalation | `3db4590a05eb81cd938de84cfffead9c` | `2026-10-27T15:35:20.690Z` |
| hub HDE Change Flow | `3db4590a05eb81d59059eb6b95ed5fcf` | `2026-10-27T15:35:12.051Z` |
| Flow Index | `3db4590a05eb81de9736ea69bac61016` | `2026-10-27T22:40:18.010Z` |
| catalog 100926.1 (read only) | `3f74590a05eb812db385c2544d7570f7` | `2026-10-12T13:28:07.573Z` |
| catalog 102726.1 | `4064590a05eb8113ae7de73041631c00` | `2026-10-27T15:33:12.290Z` |
| PE Metaprompt 102726.1 | `4064590a05eb8173b2e7d37929e7fe4d` | `2026-10-27T13:09:24.084Z` |

**C4.** C-FI-REV, sent once at X18, is on the Flow Index exactly as written: the page read after the write equals the plan's model, the read before it with C-FI-REV applied, line for line (`execute/x18-landed-probe-102726.1.json`: `after_equals_model` true, 0 lines differing). `control_check_102726.py --phase candidate` on the controls, the catalog and PE: ok, 0 findings. **But `activation_render_102726.py check --phase review` reports C-FI-REV not landed** (`execute/x18-check-102726.1.json`): a false negative of the plan's own counting rule, which expects an anchor once per replacement up to the phase, so an operation anchored inside an earlier one's text is expected twice. The same rule misjudges six P1 operations: `P1d-FI-CAND-H`, `P1e-HUB-CF-CAND`, `P1e-HUB-ESC-CAND`, `P1e-HUB-IA-CAND`, `P1e-HUB-QA-CAND`, `P1e-HUB-TW-CAND`. Uncorrected, P1(d) would stop on the Flow Index after P1(a) to (c) are written. The proposed **AM-9** (§6, first) counts the anchor only in the replacements still on the page whole; measured in memory (`execute/am9-experiment-102726.1.json`): the self-test 49 of 49 on the real map and 49 of 49 on the stand-in map; the review check `ok`; no false negative from review through sweep; a missing replacement, a leftover anchor and an unapplied operation still read not landed.

## 5. What approval authorizes, in order (PLAN §7, §8)

In the order of PLAN §7 (D17): the transaction is coordinated, not atomic, and the order is its safety property.

- **X19, P0.** The register still selects 100926.1 / 55; every control page's revision equals its pin in §4; the successor map's and the nine skills' digests and v5.1.0's sha256 equal §2's. Otherwise stop.
- **X20, P1, bindings.** P1(a) creates the register entry under the register; then one write per page from `activation_render_102726.py plan --phase activation --emit` at its pin: (b) the catalog, (c) PE 102726.1's frontmatter, (d) the Flow Index with its title, (e) the five hubs and their titles, (f) the Alpha checklist and its title; each re-fetched and checked.
- **X21, P2, the register, last.** *Current selection* names GCFPE-20261027.1 / 102726.1 / 56, binds the catalog, and the procedure binding moves to v5.1.0.
- **X22, P3. You install the four packages** when asked, not before. `freeze.py` on each installed tree must equal §2's digest, and the five unchanged skills theirs, or the review is void.
- **X23, P4.** Production validation on the activated state: fresh reads of all 56; 56 bodies validated, none unevaluated; every registry row passes.
- **X24, P5.** The 57 superseded pages (the 54 member predecessors, PE 100926.1, the 100926.1 catalog and the CL-05 candidate) moved to the archive page `3c94590a05eb811cb145cd010e3b3fcf`, intact.
- **X25, P6.** The sweep by literal: the Glow Operations Hub and the HDE Change Flow Overview, then a search for current 100926.1 / 55 statements; a selected member body is never edited.
- **X26, P7 and R1 to R5.** On a branch: `docs/graph/parts/` replaced by the production parts; the selected registry with your approval date; `authoritative-surfaces.md`, `notion-write-boundary.md` and the D31 promotion entry; the promotion pull request.
- **X27, R7.** After you merge it, verification from `main`.
- **X28.** The backlog's 28 taken entries get their dispositions; the record pull request; `ECOSYSTEM_CHANGE_COMPLETE`.

Stop rule: the first failed or ambiguous write stops the run and returns to you; no blind retry, no automatic rollback, no archival after a failed step. The 30-hour limit of your rule 4 still applies: the run ends at 2026-10-28T17:20Z, at the next safe point before a promotion write.

## 6. Accepted risks — every listed finding

**First, a prerequisite of promotion: proposed amendment AM-9 (your decision).** `activation_render_102726.py`'s `landed()` counts a start anchor's expected occurrences over every replacement the page carries up to the phase. An operation anchored inside an earlier operation's text is then expected twice where the page holds it once, and reads not landed. It did so for C-FI-REV at X18 (the page is exactly the model, §4) and would for P1d-FI-CAND-H and the five P1e-*-CAND operations at P1, so P1(d) would stop on the Flow Index after P1(a) to (c) are written. AM-9 counts the anchor only inside the replacements still on the page whole, and in the operation's own; the content of every write is unchanged. Measured in memory, the plan file unchanged (`execute/am9-experiment-102726.1.json`): the self-test 49 of 49 on both maps, the review check `ok`, no false negative from review through sweep, and a missing replacement, a leftover anchor and an unapplied operation each still not landed. It is not a storage-form fix (rule 2 does not reach it), so it is put to you; it would count toward rule 4 only if you say so. On your word it is committed with a self-test case each way before P0, and C4's check is run again.

**Then the listed findings.** None of them stops the flow. Each stays listed (D26-A rule 4) and goes to the backlog at X28 unless you opt in to its correction. The four marked **opt-in** have a one-line correction ready; taking one changes approved text, so it needs your words, and it is then written with the transaction's operations and checked like them.

**From the D24 review (X16)**

- **D24-A F1 = D24-B LISTED-1.** The D24 brief's expected result for `package_apply.py --check` on the extracted trees was wrong: it reports 104 `LANDED` and `SR-W7-CF-04` `UNTOUCHED`, because R-P1's `RP1-CF-02` extends the note that operation inserts. The author's error in the brief, disclosed in §E. No package byte is affected; `package_build_102726.py check` is equal over 87 files.
- **D24-B LISTED-2: your decision.** No package gate checks what CL-05's handoff to the closure receiver (Isis) carries. If it ever omitted the QA Report or the RCA, CL-E-10 or CL-C-10 would stop at intake (`STOP_CLOSURE_EVIDENCE_INCOMPLETE`), a loud stop. Post-flight B read CL-05's body: its exit handoff names the result record, the QA-120 Report and the RCA by repository path. A new check is a new design element; by default it goes to the backlog.

**From the post-flight (X17)**

- **PF-A F-1 = PF-B W-1, opt-in.** From P1, P2 and P6 until you merge the promotion pull request, control text names repository surfaces that `main` does not yet hold: `docs/graph/parts/` with the 102726.1 token, `GCFPE-PCR-20261027.1`, and D31 (P1d-FI-B-TOKEN; P2-REG-SEL's *machine contract* and *per-prompt contracts* rows; P6-HUB-SEL and P6-OV-SEL). It is the order D17 adopted, the pattern of 100926.1's promotion (D29), and X27 verifies it. Correction: add "(on `main` from the promotion pull request)" to those rows.
- **PF-A F-2, opt-in.** The Flow Index's and the QA hub's new navigation lines (P1d-FI-FLOW-QA, P1e-HUB-QA-PASS) say CL-05 hands a verified `EPIC` to CL-E-10, without the condition that P-L18 accepts: until canon admits an Epic close-run family, an Epic close stops `BLOCKED` after its rehearsal. CL-05's body and the graph carry the condition. Correction: append "for an Epic whose close-run family canon admits; otherwise CL-05 returns `BLOCKED` after its rehearsal".
- **PF-A F-3 = PF-B W-2.** `activation_render_102726.py plan --chain` ignores `--emit`, so the post-flight brief's statement that the author ran its step (a) with `--emit` shows counts only (disclosed in §E). Both reviewers read all 238 operations another way. The transaction writes from the non-chain `plan --phase PH --emit`, which emits. A tool fix goes to the backlog.
- **PF-A F-4, opt-in.** P6-HUB-SEL carries over "Sections on this page headed \"Historical … — 091426.1\" were written for the predecessor"; the predecessor is now 100926.1, and X25's literal sweep will not catch it. Correction: "Sections on this page headed \"Historical …\" were written for earlier releases and are kept as written; where they differ from the selected 102726.1 prompts or the register, those govern."
- **PF-B W-3.** PE Metaprompt's page carries release and selection state (`status`, `candidate_release`, `promotion_authorized`, `validation_status`, a `Prompt Version` line), as PE 100926.1 did; `prompt-body-content-policy.md` has no ruling on whether PE's head is a control head or a prompt body. To the backlog for a ruling.
- **PF-B W-4, opt-in.** C-FI-REV, written at X18 as approved, appends the review line but leaves the candidate record's "<b>Recovery-stage status:</b> qualification pending: the graph build, the registry, the validators over every member, the D24 package review and the independent post-flight." standing. P1(d) retitles that section historical, so the clause would then stand in the historical record for good (and indefinitely as current text if promotion is declined). Correction: "qualification pending:" to "qualification complete:" in that sentence, written at P1(d) with the Flow Index's other operations.

**Carried**

- EXECUTE's amendments AM-1 to AM-8 and its disclosed deviations (record §E, *Disclosed deviations (EXECUTE)*), among them: the chain's coverage gap from the review phase (covered by a second command), the X15 revisions file's form, the installed `xlsx` update at 20:05Z, and X17's two false starts.
- The open findings accepted at plan approval: PLAN §10 P-L1 to P-L28 and the reviewers' L-1 to L-D8 (record §P). Restating one is not a new finding.

## 7. Your actions

| action | when | verified by |
|---|---|---|
| approve this snapshot, in your own words | now | your words quoted in §E |
| install the four packages | at X22, when asked, not before | `freeze.py` on each installed tree equals §2 |
| merge the promotion pull request | after X26 | X27 detects it by files on `main` |
| merge X28's record pull request | after X28 | it preserves the record and approves nothing (D21-C) |

## 8. The approval requested

A suggested form, to change as you wish:

*"AM-9 as proposed, outside rule 4's count. Nathan approves promotion of GCFPE-20261027.1 / 102726.1 as the snapshot in execute/PROMOTION-PACKET.md at <commit>, accepting the listed risks in its §6, with the opt-in corrections <none / any of PF-A F-1, PF-A F-2, PF-A F-4, PF-B W-4>; D24-B LISTED-2 goes to the backlog. Go on to PART-25."*

An opt-in correction is written with the transaction's operations: PF-B W-4 on the Flow Index at P1(d), the others in the operations they amend, each rendered, written once and checked like them. Without AM-9, P1 cannot pass its own check.
