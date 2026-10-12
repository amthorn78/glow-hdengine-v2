FAIL — 1 mandatory open finding

# Independent post-flight — REVIEWER-POSTFLIGHT-A

**Answer.** The release passes. All identities reproduce, every body-free check and gate passes, and all 55 bodies validate with no coverage gap (`prompt_bodies_validated` 55, `prompt_body_checks_not_evaluated` []). All 55 audit-assertion rows hold on my reads at the X6 revisions. Nothing found stops the flow. Nothing contradicts PF10 addendum 2.1, D27, PF06 §0.1A or the GCFPE-MGMT-10 three-mode contract.

The activation as specified does not pass. Three operations in `plan/activation-ops.json` (FI-B-SKILL, FI-PEV-2 and REG-SEL) would write, at X15 and X16, that `REVIEW-D24-A.md` and `REVIEW-D24-B.md` returned `SKILL_FIT_CONFIRMED` on the reviewed digests. `REVIEW-D24-A.md` returned `SKILL_REPAIR_REQUIRED`. Neither record reviewed the governance-audit digest that will be installed. That is a false statement on the operative Flow Index and register, so it is mandatory (F-1). It offends the record. It does not stop the flow. The selected-stage registry passes build, check and compare.

| | |
|---|---|
| Reviewer | `REVIEWER-POSTFLIGHT-A`, fresh context. Not an author of this release, not its D24 reviewer. |
| Brief | `execute/BRIEF-POSTFLIGHT.md`, committed at `99d14bc` |
| Branch | `claude/mb-008-modification-promotion-fdz2sn`, draft PR #605, not merged |
| HEAD read | `99d14bc`. At write time HEAD is `9568eec`. A names-only diff shows two additions, `execute/REVIEW-D24-D.md` and `execute/REVIEW-D24-C.md` (neither read), and a one-line change to the MODIFICATION record, which I did not read. `plan/` and `PLAN-20261011.md` are unchanged, and the §E X10 clause quoted in F-1 is still present (see *Disclosures*) |
| Date | 2026-10-12 (UTC) |
| Pre-fetch, members and PE | `2026-10-12T03:42:55.982Z` |
| Pre-fetch, the nine control pages | `2026-10-12T03:49:49.412Z` |
| Scratch | `/tmp/pfa`, outside the repository |
| Python | `PYTHONDONTWRITEBYTECODE=1` throughout |

## Findings

### F-1 — MANDATORY: the activation cites round-1 D24 records as confirming the installed packages

- **Control.** `plan/activation-ops.json`, three operations:
  - **FI-B-SKILL** (line 140): the Flow Index skill binding.
  - **FI-PEV-2** (line 194): the Flow Index promotion evidence.
  - **REG-SEL** (line 450): the register's new current-selection section.

  X15 writes the first two and X16 writes the third.
- **Defect.** All three hard-code the round-1 D24 records as having returned `SKILL_FIT_CONFIRMED` on the reviewed digests. The record contradicts this in two ways:
  - **A's verdict is not a confirmation.** `REVIEW-D24-A.md` line 1 reads "SKILL_REPAIR_REQUIRED — 2 REQUIRED findings." The record's §E X10 says the same: "REVIEW-D24-A: `SKILL_REPAIR_REQUIRED`, 2 required".
  - **Neither record covers the governance audit that will be installed.**
    - Round 1 (A and B) reviewed `amthor-workspace-governance-audit` at archive `8c68ab08…`, tree `15 43e76519…`. See `REVIEW-D24-A.md` line 24, `REVIEW-D24-B.md` line 14 and `execute/x9-packages.json`.
    - The X10 repair produced `.skill` `6199c76d…`, tree `15 f0f00820…` (`execute/x10-packages.json`). That is the package X17 installs.

  So B confirmed bytes that will not be installed. REG-SEL's sentence "the installed digests are compared with the reviewed ones at install" would compare against digests the cited records did not confirm for that package.

  The texts also misstate how D24 approves a package. D24 condition 5: "A package is approved only when both return `SKILL_FIT_CONFIRMED` against the same digests. Any `SKILL_REPAIR_REQUIRED` finding is repaired and re-reviewed by fresh reviewers on the new bytes." D24 condition 6: "A verdict covers exact bytes and does not carry." Under that ruling, A and B cannot be the approval of the packages X17 installs. Presenting them as that approval silently misstates a Product Owner ruling.

  The texts match PLAN §3's expected evidence, "two fresh reviewers, `SKILL_FIT_CONFIRMED` on the same digests; `execute/REVIEW-D24-A.md`, `execute/REVIEW-D24-B.md`". They were written before X10 ran, and X10's outcome made them false. Of M-1 to M-7, PIN-1-A, P-L1 to P-L9 and L1 to L6, none covers this, so it is not a restated accepted finding.
- **Evidence (quoted clauses).**
  - FI-B-SKILL: "`…/execute/REVIEW-D24-A.md` and `REVIEW-D24-B.md` in `amthorn78/glow-hdengine-v2` — `SKILL_FIT_CONFIRMED` on the reviewed digests."
  - FI-PEV-2: "`…/execute/REVIEW-D24-A.md` and `REVIEW-D24-B.md` — `SKILL_FIT_CONFIRMED`, scoped to the reviewed digests"
  - REG-SEL: "The D24 independent skill review returned `SKILL_FIT_CONFIRMED` for the six reviewed packages (`…/execute/REVIEW-D24-A.md`, `REVIEW-D24-B.md`); the installed digests are compared with the reviewed ones at install."
- **Smallest correction.**
  1. In the three texts, replace the two hard-coded record names with a marker, for example `@D24_RECORDS`, defined in the file's marker table.
  2. X14 fills it in the promotion packet with the D24 records whose verdict is `SKILL_FIT_CONFIRMED` on the exact digests X17 installs. Alternatively, the texts can name every D24 record with its actual verdict and the digests it covered.
  3. Re-run `activation_render.py plan` and `control_check.py` on the changed texts.

  The change edits text that the plan approval (PIN-1-A) approved, so it returns to Nathan.
- **Stops the flow or offends the record.** It offends the record. GCFPE routing, members and gates are unaffected. It is mandatory under the brief's rule because the activation as specified would write a false statement into two operative controls and would misstate D24's approval rule.

### Non-mandatory notes (no correction needed for this verdict)

- **N-1. A refinement of accepted M-4 (L6), not a new finding.**
  - FI-B-GRAPH and REG-SEL's machine-contract row bind `docs/graph/parts/` to `@PRODUCTION_TOKEN` (235 edges, `43f84f29…`). The per-prompt contracts row names `GCFPE-PCR-20261009.1`.
  - I built `docs/graph/parts/` both on `main` and on this branch. Both give 55 nodes · 229 edges · 55 state_routes · 575,074 bytes · sha256 `ae2bd159…`.
  - So from X16 until X21 replaces the parts on the branch (PLAN §5 X21), even the PR branch does not carry the bound token. M-4's "describe the PR branch" holds from X21 on.
  - The consequence is the same as M-4's, which was accepted as "transient until a merge Nathan controls; low".
- **N-2. REG-SEL predicate 1 cites imprecisely.** It cites `execute/candidate-registry.md` for "the candidate registry's assertions on fresh reads". The assertion results are recorded in `execute/x11-registry.json` (`assertions`), not in the three files cited. The claim is supported by evidence in the same directory; only the citation is off.
- **N-3. The briefed command does not render the two new pages.** The activation command in the brief passes `--pages`, and `activation_render.py` renders the new pages only `if not check_mode and not a.pages:` (line 240).
  - I made one extra `plan --emit` run without `--pages` to review them. In that run the X6a inventory page showed `NO_FETCH`, as expected, because it was not among my reads.
  - The catalog had 0 findings and 55 rows, with each binding equal to the validated member page id. The register entry had no markers left and every step pending.
  - The X15 command from M-3 also passes `--pages`, so X15(a)'s new-page content has to come from a run without it. That is procedural and does not stop the flow.
- **N-4. MGMT-10: a branch-modelling difference.** The successor's body says of `PRODUCT_OWNER_ACTION_PENDING`: "Not terminal." The graph marks that branch `terminal_for_invocation: true` with 0 handoffs. Both return to Nathan with no handoff, and the body also says "This prompt hands off to no other prompt." D15 holds and no route is missing, so this is an observation only.
- **Accepted and not findings.** The stand-in marker values (L3). PE's three P-L8 passages (L5). M-2, M-5 and M-6.

## Activation review (§4)

The briefed run had all nine control pages fetched after `2026-10-12T03:49:49.412Z`, with the briefed `--set` and `--pin` values. Overall `ok: true`.

| Page | Pin matches | Applied | Refused | batch_safe | findings_after |
|---|---|---|---|---|---|
| Flow Index `3db4590a05eb81de9736ea69bac61016` | true | 152 | 0 | true | 0 |
| CF hub `3db4590a05eb81d59059eb6b95ed5fcf` | true | 47 | 0 | true | 0 |
| IA hub `3db4590a05eb8195a2ccf7c0959a8b6e` | true | 53 | 0 | true | 0 |
| QA hub `3db4590a05eb814d96d3dcfa8835f96d` | true | 31 | 0 | true | 0 |
| ESC hub `3db4590a05eb81cd938de84cfffead9c` | true | 19 | 0 | true | 0 |
| TW hub `3db4590a05eb811b9c14f2ae89c28df7` | true | 14 | 0 | true | 0 |
| Alpha checklist `3db4590a05eb812f87caed515836687f` | true | 11 | 0 | true | 0 |
| PE `3f44590a05eb81f98b76c83465dc1960` | true | 5 | 0 | true | 0 |
| Register `3d24590a05eb81ce942ad994cfca9fa1` | true | 6 | 0 | true | 0 |

I read every rendered operation as text. F-1 is the only sentence I found false at some moment of X15–X22 or after it. The N-1 and N-3 cases above are accepted or procedural. Specifically:

- The sentences about indexes and hubs read "operative only while the register selects" 100926.1.
- The predecessor disposition reads `SUPERSEDED` until X19.
- The register entry is created with every step pending.
- Dated sections get a `Historical — ` heading with their text kept.
- The Alpha checklist operations historicize a subsection and its heading and do not change Alpha state.
- I found no unstated in-place release-bound value.

**Selected-stage registry.**

| Step | Result |
|---|---|
| Build | 535,408 bytes, 55 rows, read back equal |
| Check | `ok`: 0 errors, 0 warnings, no deriver drift, 55 `ACTIVE`, `header_values_ok` true, no markers left |
| Compare with `execute/candidate-registry.md` | `ok`; differs only at `approved_at`, `approved_by`, `authority_sources.1.pending`, `authority_sources.1.url` and `status`, plus preamble lines 3–5 |

The values are:
- `status: APPROVED`
- `approved_by: Nathan / Product Owner`
- `approved_at: '2026-10-13'` (stand-in)
- `registry_id: GCFPE-PCR-20261009.1`
- the catalog URL (stand-in)
- lane parent titles at 100926.1

No finding.

## Timestamp baseline (page_last_edited_at as read)

Every member value equals its fetch `as_of` and its revision in `execute/x6-check.json`. All times are 2026-10-12 UTC.

| Page | page_last_edited_at |
|---|---|
| CF-C-10 | 02:29:03.544Z |
| CF-C-20 | 02:29:09.414Z |
| CF-C-30 | 02:29:05.619Z |
| CF-C-40 | 02:29:18.974Z |
| CF-E-10 | 02:29:06.412Z |
| CF-E-20 | 02:29:12.283Z |
| CF-E-30 | 02:29:08.639Z |
| CF-E-40 | 02:29:22.102Z |
| CF-PO-10 | 02:29:09.502Z |
| CL-20 | 02:29:16.766Z |
| CL-30 | 02:29:13.172Z |
| CL-40 | 02:29:26.600Z |
| CL-C-10 | 02:29:13.994Z |
| CL-E-10 | 02:29:21.313Z |
| CL-E-20 | 02:29:16.227Z |
| CL-E-30 | 02:29:29.629Z |
| CL-E-40 | 02:29:17.029Z |
| DOC-10 | 02:29:24.131Z |
| DOC-20 | 02:29:19.255Z |
| ESC-10 | 02:29:32.722Z |
| ESC-25 | 02:29:20.067Z |
| ESC-30 | 02:29:51.552Z |
| ESC-40 | 02:29:22.274Z |
| IA-10 | 02:29:35.733Z |
| IA-20 | 02:29:23.010Z |
| IA-30 | 02:29:54.641Z |
| IA-40 | 02:29:25.413Z |
| IA-50 | 02:29:38.746Z |
| IA-60 | 02:30:00.331Z |
| MGR-10 | 02:29:57.710Z |
| OPS-10 | 02:29:29.013Z |
| OPS-20 | 02:29:42.649Z |
| OPS-30 | 02:30:04.097Z |
| PR-10 | 02:29:33.739Z |
| PR-20 | 02:29:47.327Z |
| PR-30 | 02:30:08.672Z |
| PR-35 | 02:30:15.569Z |
| PR-40 | 02:29:38.234Z |
| PR-50 | 02:29:48.607Z |
| QA-10 | 02:30:12.398Z |
| QA-20 | 02:30:15.395Z |
| QA-50 | 02:30:48.299Z |
| QA-60 | 02:29:44.410Z |
| QA-70 | 02:29:54.691Z |
| QA-80 | 02:30:18.516Z |
| QA-90 | 02:30:51.327Z |
| QA-100 | 02:30:45.204Z |
| QA-110 | 02:29:41.377Z |
| QA-120 | 02:29:51.614Z |
| RS-10 | 02:29:47.386Z |
| RS-20 | 02:29:57.795Z |
| RS-30 | 02:30:23.555Z |
| RS-40 | 02:30:54.130Z |
| UTIL-10 | 02:29:50.321Z |
| GCFPE-MGMT-10 successor `3f74590a05eb81b69bd8c27106f7a59d` | 02:30:05.584Z |
| PE Metaprompt 100926.1 `3f44590a05eb81f98b76c83465dc1960` | 02:30:10.895Z (equal on both reads) |

The control pages, as read for §4:

| Control page | Fetch `as_of` | page_last_edited_at |
|---|---|---|
| Flow Index | 2026-10-12T02:34:11.699Z | 2026-10-11T20:10:23.284Z |
| CF hub | 2026-10-12T02:29:57.710Z | 2026-10-09T20:19:06.953Z |
| IA hub | 2026-10-12T02:30:54.130Z | 2026-10-09T20:19:03.530Z |
| QA hub | 2026-10-12T02:30:51.327Z | 2026-10-09T20:19:05.496Z |
| ESC hub | 2026-10-12T02:29:51.552Z | 2026-10-09T20:19:08.504Z |
| TW hub | 2026-10-12T02:30:10.895Z | 2026-10-09T20:19:09.916Z |
| Alpha checklist | 2026-09-23T17:43:43.526Z | 2026-09-23T17:43:43.526Z |
| Register | 2026-10-09T20:19:11.175Z | not recorded |

## Checks run

### 1. Identities: all reproduced

- **The six packages.** Each `.skill` sha256 equals `execute/x10-packages.json`. Each freeze digest equals its recorded value:

  | Package | Freeze digest |
  |---|---|
  | change-flow | 25 `c9b0927f…` |
  | flowmaster-validate | 37 `02a69b8a…` |
  | glow-hde-pr-development | 4 `f0880ceb…` |
  | glow-graph-contract | 9 `d00c8d17…` |
  | session-relay-flowmaster | 5 `33d8b9be…` |
  | amthor-workspace-governance-audit | 15 `f0f00820…` |

- **Graph builds.**
  - Candidate parts build 55 / 235 / 55, 593,625 bytes, `a58666e5…`, PASS.
  - Production parts build 593,569 bytes, `43f84f29…`, PASS.
- **Contracts.**
  - Candidate `90593603…` (634,423 bytes).
  - Production `cd291f17…` (631,061 bytes), equal to the copies bundled in change-flow and flowmaster-validate.
- **Candidate registry.** `cb44a371…` (535,417 bytes).
- **The seven siblings** copied from synced match their digests:

  | Sibling | Freeze digest |
  |---|---|
  | flowmaster-primary | 2 `2d41da26…` |
  | glow-merged-change-attribution-lock | 10 `c518ccb0…` |
  | glow-po-reporting | 1 `7e04368a…` |
  | session-branch-flowmaster | 2 `17b5800b…` |
  | skill-creator | 18 `e4fee9c9…` |
  | tw-flowmaster | 2 `0581205b…` |
  | typesafe-scoring | 3 `088c77f3…` |

  No `__pycache__` appeared in any extracted tree.

### 2. Checks that need no body: all pass

- **D15, on both part sets.** 290 branches. 0 terminal branches with a handoff, 0 nonterminal branches without one, 0 unknown endpoints, every result state routed.
- **Registry against the graph.** `registry_assemble.py check --stage candidate`: `ok`, 0 errors, 0 warnings, no drift, 55 `ACTIVE`.
- **PF10 producer set.** Exactly CF-C-30, CF-E-30, ESC-40, IA-30, QA-70 and RS-20, with `producer_allocates_pf10_number` true and `producer_edits_pf10` false.
- **PR-20's declared inputs.** `accepted_inputs` equals its in-edges: PR-10 and DOC-10 `PR_INSTRUCTION`, PR-40 `REJECT`, and three from RS-20.
- **Installed gates.**
  - `validate_flowmaster.py --strict-warnings` over the 13-skill root: `FLOWMASTER_SUITE_PASS`, 0 findings. The current overlay is the 100926.1 profile, `ok`. 283 fixture cases, 54/54, 55/55.
  - change-flow fixtures 34/34.
  - Governance-audit suite 38 OK.
  - Relay self-test PASS.
  - PR skill validator PASS.
  - change-flow `validate_gcfpe_20261009` PASS.
  - `run_gcfpe_20261009_fixtures` 283 OK.

### 3. Bodies, lane by lane

The lanes were CF (9), CL plus DOC (10), ESC (4), IA plus MGR (7), OPS (3), PR (6), QA (10), and RS plus UTIL plus MGMT-10 (6).

- **Lanes.** Every lane's profile was `ok`, and every lane's `assertions --landed` rows held. In the lane runs `QA_PASS_CLASS_MAP_AND_INTAKES` is reported not evaluated because it is set-scoped.
- **Full run.** The full 55-body run returned `ok`, `prompt_bodies_validated` 55, `prompt_body_checks_not_evaluated` [], 0 errors.
- **Fixtures with bodies.** 309 cases, `fixture_suite_ok`, 54/54, 55/55, `qa_closure` 9, `artifact_timing` 17.
- **Assertions.** `registry_assemble.py assertions --landed`, with the brief's `--page` and `--shared`: 55/55 rows `ok`, 0 not landed, 0 `NO_FETCH`.
- **body_check.** `body_check check`: 56 pages `ok`, 87/87 operations landed, 273/273 guard rows pass.
- **Revisions.** Every `as_of` equals X6's.

### 4. Semantic audit of the bodies against the four rulings: no finding

**PF10 addendum 2.1.** TypeSafe readings are kept, no agent gives its own model advice, and surface advice is kept. Examples:
- PR-10, PR-20, PR-30 and PR-40: "do not prescribe a runtime setting or give their own assessment of one … the TypeSafe reading and surface advice … inform Nathan's choice and prescribe nothing".
- PR-35: "Do not give your own recommendation, assessment or ranking of model, reasoning level or effort".

**PF06 §0.1A.** The six producers resolve their addendum's number. Examples:
- ESC-40: "resolve the current continuous addendum number from the current controlled PF10 Markdown".
- CL-*: "it resolves the addendum's number from the current controlled PF10 at creation".

Nonproducers' "Never … allocate PF10 numbering" is about themselves.

**D27.**
- OPS-10: "Ops execution belongs to the authorized environment session, not Kronos."
- QA-50 and QA-60: "Kronos is not categorically barred from execution if the Product Owner chooses it … execution authority does not become acceptance authority."
- QA-100: "The Product Owner chooses the execution arrangement; no particular session type or identity is required."

**The MGMT-10 three-mode contract.** The successor has the three modes ANALYZE, PLAN and EXECUTE, carries "This prompt hands off to no other prompt.", and has the TypeSafe section. ESC-40 decides "exactly `APPROVE`, `APPROVE_AS_CHANGED`, or `DENY`". IA-40 uses "exactly one `AUTHORING_MODE`".

**Routes.** Graph routes match the bodies for every lane I traced, including ESC-40, RS-20, DOC-10 and DOC-20.

### 5. Activation and selected stage

As reported above.

## Checks not run, limits and deviations

- **Excluded by the brief.** I did not read `execute/REVIEW-D24-C.md` or `-D.md`. I did not review package code quality (L4), wording, prose drift, presentation or byte fidelity.
- **Rendered operations, not final bytes (L1).** I reviewed the activation as rendered operations on my reads, not as final bytes. The Flow Index pin is a stand-in. Per L2, I read the rendered text itself and did not rely on `control_check.py`'s 100-character excuse window.
- **Deviation: `-B -s` instead of `-I`.** I ran the validators with `python3 -B -s` from `/tmp/pfa`, not with `-I`. Under `-I` they fail on their sibling imports with `ModuleNotFoundError: No module named 'validate_gcfpe_current'`. Bytecode writing was off throughout.
- **Deviation: an extra activation run.** I made one extra activation `plan --emit` run without `--pages` to see the two new pages (N-3).
- **Assertions may read another session's fetch.** `body_check.latest_fetch`, which the `assertions` command uses, reads the newest fetch after `--fetched-after` from every record in this session, including fetches by concurrent subagents. I confirmed that each row's `as_of` equals `execute/x6-check.json`, so the revision read is the pinned one whoever fetched it.
- **Two pre-fetch times.** The nine control pages used a second pre-fetch time, `2026-10-12T03:49:49.412Z`.

## Disclosures

**Prompt bodies (D22).**
- I fetched all 55 member bodies and PE (twice) into context with the Notion fetch tool. Lane bodies went to `--bodies-stdin` through a subprocess pipe; I wrote no body file myself.
- Because of the fetch results' size, the harness saved eight body reads and one control-page read to the session store `tool-results/`: OPS-10, OPS-30, PR-10, PR-20, PR-40, QA-10, PE twice, and the register.
- Each was used only for the check in hand. None was hashed, byte-compared or cited as the body. All nine were deleted at the end of the task and verified absent.
- The scratch outputs in `/tmp/pfa` that could hold body or control text were deleted: the activation emits, the body_check output and the assertion output. The rest of `/tmp/pfa` (package extractions, graph builds, the selected-stage registry build and my scripts) holds no body and is deleted at the end of the task.
- The fetched text also sits in the harness's own session transcript, which this session does not control. It is left to the harness's teardown.
- This record carries only quoted clauses.

**Incidental exposure.** To confirm that no input had moved, I ran `git log` and saw commit `983588e`, whose subject states a verdict for `REVIEW-D24-D.md`. I did not open `REVIEW-D24-C.md` or `-D.md`. F-1 and its correction do not depend on round 2's outcome.

**Writes.** None in Notion. None in the repository except this file. No commit or push. Nothing under `/root/.claude/skills/synced/`.

**Canon relied on:**
- PF-Canon on `main` at `9312add2`:
  - PF10-HDE-Build-Notes v13.5.2, searched in full, with addendum 2.1 read.
  - PF04-Canon-HDE-Governance v2.8.7 §9.1.1–§9.1.6.
  - PF06-Canon-Change-Process-Guide v2.5.4 §0.1A.
- Repository controls:
  - AGENTS.md.
  - `docs/prompt_ecosystem_management/postflight-procedure.md`.
  - `prompt-corpus-policy.md`, including the D22 amendment.
  - `gcfpe.decision-record.md` D15, D17, D18, D20, D22, D24 and D27.
  - `skill-identity-and-freeze.md`.
  - `PLAN-20261011.md` §3, §5, §7, §8 and §10.
  - `MODIFICATION-20261011-gcfpe-mb008-to-promotion.md` §E and §P, including M-1 to M-7 and PIN-1-A.
  - `REVIEW-PLAN-DIFF-2.md` M-4.

DECISION NEEDED: F-1 returns to its owner. The correction changes plan-approved activation text, so Nathan must decide on it before a promotion packet goes to him.
