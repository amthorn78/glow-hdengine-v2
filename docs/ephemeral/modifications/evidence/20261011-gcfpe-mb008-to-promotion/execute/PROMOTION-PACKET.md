# Promotion packet — GCFPE-20261009.1 / 100926.1

`MODIFICATION-20261011-gcfpe-mb008-to-promotion`, X14 (PLAN §3 PART-07, §7; DN-D). This is the exact snapshot
Nathan is asked to approve for promotion. Approving it authorizes PART-08 (X15–X22) as PLAN §7 and §8 state, with
amendment AM-2, and nothing else. Until then, nothing of PART-08 is done: no control binding, no new page, no
register change, no install, no archive move.

## 1. The promotion predicates (the register's own)

| # | Predicate | State | Evidence |
|---|---|---|---|
| 1 | Complete behaviour validation of the exact pinned snapshot | met | `execute/qualification-validators.json` (the 100926.1 profile over all 55 member bodies: 55 validated, none unevaluated, `ok`; flowmaster suite `FLOWMASTER_SUITE_PASS`; candidate and production contracts equal outside lifecycle fields and the graph digest); `execute/qualification-fixtures.json` (`fixture_suite_ok`, 54 of 54; 309 cases with bodies); `execute/x11-registry.json` (55 of 55 registry rows on fresh reads, every operation landed, 2,398 assertions, 665 injected regressions all reported) |
| 2 | Independent post-flight `PASS` or `PASS WITH WARNINGS`, no mandatory open finding | met | X13 first run `FAIL` on one finding (F-1/PFB-M1), corrected by AM-2; the focused post-flight of AM-2's operations: `PASS WITH WARNINGS` twice, 0 mandatory (`execute/REVIEW-POSTFLIGHT-A.md` … `-D.md`) |
| 3 | Nathan / Product Owner's separate approval of this snapshot | **open** | requested in §8 |

## 2. The snapshot

**Notion — the 55 members and PE, each at the revision X6 read** (`execute/x6-check.json`). The read-only sweep at
04:00Z and both focused post-flight reviewers' reads after 12:38Z found every control page at its pin; a fetch's
revision is the newest edit in its subtree, so none of these pages has moved since.

| prompt | page id | revision (X6) |
|---|---|---|
| CF-C-10 | `3f44590a05eb810f83d4d539e5b0e588` | `2026-10-12T02:29:03.544Z` |
| CF-C-20 | `3f44590a05eb81a7a944f19bd9a2e3de` | `2026-10-12T02:29:09.414Z` |
| CF-C-30 | `3f44590a05eb8121af3bf2249c6d6ca8` | `2026-10-12T02:29:05.619Z` |
| CF-C-40 | `3f44590a05eb81458686cc39d8d98b2a` | `2026-10-12T02:29:18.974Z` |
| CF-E-10 | `3f44590a05eb81129b09cddebcc18458` | `2026-10-12T02:29:06.412Z` |
| CF-E-20 | `3f44590a05eb813cb9cbc61c225b88e2` | `2026-10-12T02:29:12.283Z` |
| CF-E-30 | `3f44590a05eb8104824fe084354a0ef8` | `2026-10-12T02:29:08.639Z` |
| CF-E-40 | `3f44590a05eb81f1994df5f6ab3a7f32` | `2026-10-12T02:29:22.102Z` |
| CF-PO-10 | `3f44590a05eb81f9bf84f4585d9f7a2c` | `2026-10-12T02:29:09.502Z` |
| CL-20 | `3f44590a05eb81739b57da57c285f45d` | `2026-10-12T02:29:16.766Z` |
| CL-30 | `3f44590a05eb816ea12febba885940e8` | `2026-10-12T02:29:13.172Z` |
| CL-40 | `3f44590a05eb8155934dd1c4c2b5d1eb` | `2026-10-12T02:29:26.600Z` |
| CL-C-10 | `3f44590a05eb819b8022f2a4cdd3b022` | `2026-10-12T02:29:13.994Z` |
| CL-E-10 | `3f44590a05eb81248741f4679b050262` | `2026-10-12T02:29:21.313Z` |
| CL-E-20 | `3f44590a05eb8186913fcb9f6b2a2f32` | `2026-10-12T02:29:16.227Z` |
| CL-E-30 | `3f44590a05eb81be834efe3faf7abb6f` | `2026-10-12T02:29:29.629Z` |
| CL-E-40 | `3f44590a05eb8101a264f9fa702b8a6e` | `2026-10-12T02:29:17.029Z` |
| DOC-10 | `3f44590a05eb81ce99b1d2ade30c572f` | `2026-10-12T02:29:24.131Z` |
| DOC-20 | `3f44590a05eb81d8a582eec0e93e6ee7` | `2026-10-12T02:29:19.255Z` |
| ESC-10 | `3f44590a05eb81f2af47fff48995f272` | `2026-10-12T02:29:32.722Z` |
| ESC-25 | `3f44590a05eb81949370e6d1b222b40b` | `2026-10-12T02:29:20.067Z` |
| ESC-30 | `3f44590a05eb81e385dbd4fe337ad9d9` | `2026-10-12T02:29:51.552Z` |
| ESC-40 | `3f44590a05eb8173905cc6d17a40457b` | `2026-10-12T02:29:22.274Z` |
| IA-10 | `3f44590a05eb813aa0ccd709ebd134d0` | `2026-10-12T02:29:35.733Z` |
| IA-20 | `3f44590a05eb81a8bf39f4b16cc61a5f` | `2026-10-12T02:29:23.010Z` |
| IA-30 | `3f44590a05eb811db88dece791f1f60c` | `2026-10-12T02:29:54.641Z` |
| IA-40 | `3f44590a05eb81ca83ecdac0960a6f16` | `2026-10-12T02:29:25.413Z` |
| IA-50 | `3f44590a05eb810aa299fbb05a34dece` | `2026-10-12T02:29:38.746Z` |
| IA-60 | `3f44590a05eb81cdab15c7e7f7094a64` | `2026-10-12T02:30:00.331Z` |
| MGR-10 | `3f44590a05eb813ea53ac959e7a4e597` | `2026-10-12T02:29:57.710Z` |
| OPS-10 | `3f44590a05eb81509957c43992c03625` | `2026-10-12T02:29:29.013Z` |
| OPS-20 | `3f44590a05eb8155aebacd56f469643e` | `2026-10-12T02:29:42.649Z` |
| OPS-30 | `3f44590a05eb81ec8da3effc3b28cf97` | `2026-10-12T02:30:04.097Z` |
| PE | `3f44590a05eb81f98b76c83465dc1960` | `2026-10-12T02:30:10.895Z` |
| PR-10 | `3f44590a05eb815d97d5f3930c7d3e8a` | `2026-10-12T02:29:33.739Z` |
| PR-20 | `3f44590a05eb819fbea5dcd966a750ba` | `2026-10-12T02:29:47.327Z` |
| PR-30 | `3f44590a05eb8148a538f5c80588db14` | `2026-10-12T02:30:08.672Z` |
| PR-35 | `3f44590a05eb811ebf72e949b7b1572e` | `2026-10-12T02:30:15.569Z` |
| PR-40 | `3f44590a05eb81088487e918fd642a7f` | `2026-10-12T02:29:38.234Z` |
| PR-50 | `3f44590a05eb81d29748eb21df73b02c` | `2026-10-12T02:29:48.607Z` |
| QA-10 | `3f44590a05eb8134af92e7c85a48e67c` | `2026-10-12T02:30:12.398Z` |
| QA-100 | `3f44590a05eb8182a201f0e177dad431` | `2026-10-12T02:30:45.204Z` |
| QA-110 | `3f44590a05eb81ee9a09e00af51f33cb` | `2026-10-12T02:29:41.377Z` |
| QA-120 | `3f44590a05eb81a4a3fbc0fae65d153e` | `2026-10-12T02:29:51.614Z` |
| QA-20 | `3f44590a05eb81289c7be77f66bac909` | `2026-10-12T02:30:15.395Z` |
| QA-50 | `3f44590a05eb815d89d3e602973d83ad` | `2026-10-12T02:30:48.299Z` |
| QA-60 | `3f44590a05eb81489053f72637577807` | `2026-10-12T02:29:44.410Z` |
| QA-70 | `3f44590a05eb81209128ea7c82938faf` | `2026-10-12T02:29:54.691Z` |
| QA-80 | `3f44590a05eb818789e9ff3ffa9e06d8` | `2026-10-12T02:30:18.516Z` |
| QA-90 | `3f44590a05eb81bea720f004a7e1a6d8` | `2026-10-12T02:30:51.327Z` |
| RS-10 | `3f44590a05eb81a588c9c82aa8a2d3f2` | `2026-10-12T02:29:47.386Z` |
| RS-20 | `3f44590a05eb81be9566cd6397c9424c` | `2026-10-12T02:29:57.795Z` |
| RS-30 | `3f44590a05eb8131bc61e346a46840e9` | `2026-10-12T02:30:23.555Z` |
| RS-40 | `3f44590a05eb813993beccaaf88523d4` | `2026-10-12T02:30:54.130Z` |
| UTIL-10 | `3f44590a05eb81d997d1fd2b8d1b5042` | `2026-10-12T02:29:50.321Z` |
| GCFPE-MGMT-10 | `3f74590a05eb81b69bd8c27106f7a59d` | `2026-10-12T02:30:05.584Z` |

**The six skill packages** (`execute/x10-packages.json`; built by `execute/package_build.py`, reproducible with
`--check`). They install together, at X17, after the register selects GCFPE-20261009.1.

| package | `.skill` sha256 | bytes | tree (`freeze.py`) |
|---|---|---|---|
| change-flow | `eea8dd2068fdce1e0b80c0c84f658745544ac3673663831e4bd9663602204bfd` | 390,333 | `25 c9b0927f327c31328c4b64a0408a946619c985a492702a70a2cd88e216cf22c2` |
| flowmaster-validate | `1e8d413234cc4d388cb1d3ff7486de182639314bfbcb331889a4dfa0498d4e7c` | 507,685 | `37 02a69b8a99181e79e554299a51dcc31e8b6b629d4974d05c96b191cf948fa200` |
| glow-hde-pr-development | `1aad2cf4f9ff0ad54dd8612aa78d1bedce7c45be5759163262effa5e847d2409` | 23,332 | `4 f0880ceb6c5d8104a79fb37260ce2cdd90cac110878eaabc2a12106f8b6bbaf0` |
| glow-graph-contract | `2b6cc39637dc374d2ca3bfb4d2de1cccb90d30fcc1dc8ef46baa7589a5f3131e` | 58,371 | `9 d00c8d1705e3aa181b22c151f103edc9a0f9eccdcfe593fd3a92b90cb0fec6b9` |
| session-relay-flowmaster | `6028346473f984519d78284efa8d295d257019c83f984ebacd3596427a13c1c4` | 56,563 | `5 33d8b9be98288b1ba698a403964409fb65f5cc53d81cbd94a348ff5b3ce4b52c` |
| amthor-workspace-governance-audit | `6199c76d1cd607284d7760ec2f121cd665dc7eb152c9e53a3704899cd479fd96` | 57,190 | `15 f0f00820a1df24d20974dd3ad1a58bc4cb8d358d6e7b9a77ccd9ec26329e45f8` |


Advertised revisions: change-flow 3.4.0, flowmaster-validate 3.4.0 (`SKILL_TREE_SHA256` `429eda21…`),
glow-hde-pr-development 1.4.0, session-relay-flowmaster 3.3.0, amthor-workspace-governance-audit 1.14.1;
glow-graph-contract advertises none.

**Contracts and graph**

| artifact | identity |
|---|---|
| production contract (bundled in change-flow and flowmaster-validate) | `execute/contracts/gcfpe-20261009.1-100926.1-production-contract.json`, 631,061 B, sha256 `cd291f17ac832cc0aad62b5cc7e554bd6d524e18de7aea7f2f4fec5a1651317f`, `SELECTED_PRODUCTION` |
| candidate contract | `execute/contracts/gcfpe-20261009.1-100926.1-candidate-contract.json`, 634,423 B, sha256 `90593603e14f69ea96b16eb13614e689a479af1b19b6cfc32dae7213a5e1377c` |
| candidate graph (`execute/candidate-graph-parts/`) | 55 nodes · 235 edges · 55 state_routes · 593,625 bytes · sha256 `a58666e5722edd220a07e1bd88bb0e9daef29511449f099783a5da2bc1780e72` |
| production graph (`execute/production-graph-parts/`, written to `docs/graph/parts/` at X21) | 55 nodes · 235 edges · 55 state_routes · 593,569 bytes · sha256 `43f84f29b9921c21f63ffbe21dd36a14bd846a89ae697ba3cf38746c2f887eb1` |
| governing plan (pinned by both contracts) | `PLAN-20261011.md`, 50,156 B, sha256 `4de47784d63a895fe002283965032844409a247f7c8d0c4632c97c8b9dcd4d5b` |

**Registry.** Candidate stage `execute/candidate-registry.md`, 535,417 B, sha256
`cb44a371a8b4ee1faa100084be5965895d723681f995d360ca731bce646d59cf`. X21 writes the selected stage with
`registry_assemble.py build --stage selected`, which differs from the candidate only at status, approval, the
catalog row's url and pending keys and the preamble's status lines (`compare`).

**The activation.** `plan/activation-ops.json` sha256 `902586dccabed31e5d511e811caebdcdb445bcabb972cbe82709d0d344300c16`, `plan/activation_render.py` sha256 `7b83b857d3145e075ae921f04adc237b60d5955913813f11de2c5ed33549071b`,
`plan/control_check.py` sha256 `4d1c0b7f606474793446414c64ce164f46e3a092b8090f146d7219709d17274b` — with PIN-1-A and AM-2 (the file's `amendment` key; record §E, *Nathan's
decisions after X13*).

## 3. The reviews

| review | brief | records and verdicts |
|---|---|---|
| D24, round 1 (X10) | `execute/BRIEF-D24.md` (`894966c`) | `REVIEW-D24-A.md` `SKILL_REPAIR_REQUIRED` (2 required: R-1, R-2), `REVIEW-D24-B.md` `SKILL_FIT_CONFIRMED`; R-1 and R-2 repaired (`execute/d24-repair-redlines.json`) |
| D24, round 2 (X10) | `execute/BRIEF-D24-R2.md` (`e45c573`) | `REVIEW-D24-C.md` `SKILL_FIT_CONFIRMED`; `REVIEW-D24-D.md` `SKILL_REPAIR_REQUIRED` (1 required: D-1, accepted by Nathan as a listed risk, no third round) |
| post-flight (X13) | `execute/BRIEF-POSTFLIGHT.md` (`99d14bc`) | `REVIEW-POSTFLIGHT-A.md` `FAIL` (F-1), `REVIEW-POSTFLIGHT-B.md` `FAIL` (PFB-M1, the same finding) |
| focused post-flight of AM-2 (X13) | `execute/BRIEF-POSTFLIGHT-R2.md` (`d51ee87`) | `REVIEW-POSTFLIGHT-C.md` `PASS WITH WARNINGS`, `REVIEW-POSTFLIGHT-D.md` `PASS WITH WARNINGS`; 0 mandatory |

## 4. Activation markers

| marker | value |
|---|---|
| `@MGMT10_PAGE_ID` | `3f74590a05eb81b69bd8c27106f7a59d` (X1) |
| `@PRODUCTION_TOKEN` | `55 nodes · 235 edges · 55 state_routes · 593,569 bytes · sha256 43f84f29…` (X7) |
| `@D24_RECORDS` | `docs/ephemeral/modifications/evidence/20261011-gcfpe-mb008-to-promotion/execute/REVIEW-D24-C.md` (`SKILL_FIT_CONFIRMED`) and `REVIEW-D24-D.md` (`SKILL_REPAIR_REQUIRED`; its one required finding, D-1, accepted by Nathan / Product Owner as a listed risk on 2026-10-12), on the six round-2 packages |
| `@POSTFLIGHT_VERDICT` | `docs/ephemeral/modifications/evidence/20261011-gcfpe-mb008-to-promotion/execute/REVIEW-POSTFLIGHT-A.md` and `REVIEW-POSTFLIGHT-B.md`: `FAIL`, each on one mandatory finding, which amendment AM-2 corrected; `REVIEW-POSTFLIGHT-C.md`: `PASS WITH WARNINGS` and `REVIEW-POSTFLIGHT-D.md`: `PASS WITH WARNINGS`, on AM-2's operations |
| `@PROMOTION_APPROVED_AT` | **remaining**: the UTC date of Nathan's approval, quoted in §E |
| `@ACTIVATION_DATE` | **remaining**: the UTC date X15 starts |
| `@CATALOG_PAGE_ID` | **remaining**: the page X15(a) creates |
| `@REGISTER_ENTRY_PAGE_ID` | **remaining**: the page X15(f) creates |

**Pins** (PLAN §7, PIN-1-A): PE `2026-10-12T02:30:10.895Z`; hubs CF `2026-10-12T02:29:57.710Z`, IA
`2026-10-12T02:30:54.130Z`, QA `2026-10-12T02:30:51.327Z`, Escalation `2026-10-12T02:29:51.552Z`, TW
`2026-10-12T02:30:10.895Z` (`execute/x13-pins.json`); the Alpha checklist `2026-09-23T17:43:43.526Z`; the Flow
Index, its revision read right after X15(a); the register, its revision read right after X15(f).

## 5. What approval authorizes, in order (PLAN §7, §8)

X15: the catalog and the register entry created, then PE, the Flow Index, the five hubs and the Alpha checklist,
each by one write from `activation_render.py plan --emit` at its pin, re-fetched and checked. X16: the register,
last. X17: **you install the six packages**; `freeze.py` on each installed tree must equal §2's tree digest, or the
review is void. X18: production validation on the activated state. X19: the 57 predecessor pages archived by move.
X20: the literal sweep (never a selected member body). X21: the repository's selected surfaces on this branch
(PR #606). X22: after you merge PR #606, verification from `main`, the backlog rows, and the record pull request.
Stop rule: the first failed or ambiguous write stops the run and returns to you; no blind retry, no archival after a
failed step.

## 6. Accepted risks — every listed finding

None of these stops the flow. Each stays listed (D26-A rule 4) and is carried to the backlog at X22 unless you opt
in to a repair.

- **D24 round 1, A** (`REVIEW-D24-A.md`): L-1 the 100926.1 contract carries the 091426.1 template's F02 sentence;
  L-2 the F07 fixture rule reads nothing F07 changed; L-3 the new rules pass cases outside the facts they model;
  L-4 six invariants have no dependency case; L-5 the retired Kronos token is allowed inside change-flow's
  prohibition block; L-6 an explicit non-091426.1 contract always runs the 100926.1 profile, and coverage keys keep
  old names; L-7 the governing plan is called a file "on `main`" before it is; L-8 dead staging code in the profile
  validator; L-9 a wrong edge-count comment in change-flow's check; L-10 D-GG-1 overstates what the graph derives;
  L-11 the alpha record is not "unchanged"; L-12 the GCF-23 actor, a possible canon tension; L-13 older stale audit
  text (a 20260914.1 current-release line; the IA-40 sentence); L-14 section-13 naming in the 100926.1 fixtures;
  L-15 the member-URL check compares the contract only with its own graph.
- **D24 round 1, B** (`REVIEW-D24-B.md`): L-B1 the audit's stale F02/F04/F05 lines (F02 and F05 repaired by R-1/R-2;
  the IA-40 line stays); L-B2 the fixture method is overstated; L-B3 "repository file on `main`" is false through
  the install window; L-B4 glow-graph-contract's paragraphs around D-GG-1 go stale at X21; L-B5 misleading
  comments and data that change no behaviour.
- **D24 round 2**: **D-1, accepted by you** — flowmaster-validate `SKILL.md:170` still says "Producers never
  edit/number PF10 or claim adoption."; L-C1 and L-D2 the audit guard matches exact sentences only; L-C2 change-flow
  `SKILL.md:284` still makes an authorized Ops-and-QA execution route an entry prerequisite; L-D1 "37-case" at
  flowmaster-validate `SKILL.md:176`.
- **Post-flight, first run**: N-1 the branch carries the 229-edge parts until X21 (M-4); N-2 and PFB-L3 REG-SEL's
  evidence citation (repaired by AM-2); N-3 and PFB-L2 no single command renders the two new pages with a passing
  report; N-4 MGMT-10's "Not terminal." against the graph's terminal branch; PFB-L1 FI-BIND-P briefly false inside
  X15 (PIN-1-A text); PFB-L4 one marker for two verdicts (repaired by AM-2); PFB-L5 IA-30's `return_point` against
  the contract's `return_phase`.
- **Focused post-flight**: PFC-L1 and W-1 — the catalog's `validation_evidence` says "the register states their
  verdicts and records", which is untrue from X15(a) until X16 writes the register (one line: "once it selects
  GCFPE-20261009.1"); D's N-4 `plan/dry_run.py` has no stand-in for `@D24_RECORDS` (not on the X15–X22 path).

## 7. Your actions

| action | when | verified by |
|---|---|---|
| approve this snapshot, in your own words | now | your words quoted in §E |
| install the six packages | at X17, when asked, not before | `freeze.py` on each installed tree equals §2 |
| merge PR #606 | after X21 | X22 detects it by files on `main` |
| merge X22's record pull request | after X22 | it preserves the record and approves nothing (D21-C) |

## 8. The approval requested

A suggested form, to change as you wish: *"Nathan approves promotion of GCFPE-20261009.1 / 100926.1 as the snapshot
in execute/PROMOTION-PACKET.md at <commit>, accepting the listed risks in its §6. Go on to PART-08."*
