SKILL_FIT_CONFIRMED — 0 REQUIRED findings (2 LISTED).

# REVIEW-D24-C — D24 skill review, round 2, of the six MB-008 packages, MODIFICATION-20261011-gcfpe-mb008-to-promotion (X10)

**Reviewer:** REVIEWER-D24-C. I started with a fresh context. I did not author this change, and I was not a round-1 reviewer. I have not read reviewer D's record. It was committed while I was writing this one, and my findings do not depend on it.

**Brief:** `execute/BRIEF-D24-R2.md`, committed at `e45c573`, 27,658 B, sha256 `711ccfa6…`. It was my only brief. Slots: `<REVIEWER_ID>` = REVIEWER-D24-C, `<RECORD_FILE>` = REVIEW-D24-C.md.

**Branch:** `claude/mb-008-modification-promotion-fdz2sn`. HEAD was `99d14bc` when I started and `983588e` when I finished.
- `99d14bc` follows `e45c573` and only adds `execute/BRIEF-POSTFLIGHT.md`.
- `983588e` only adds `execute/REVIEW-D24-D.md`.
- Neither commit touches the packages, `package_build.py`, the plan artifacts, the contracts or the PLAN. So the frozen subject did not move, and the review is not void.

**Canon:** `main` at `9312add`. **Date:** 2026-10-12 (UTC). **Scratch:** `/tmp/d24c`.

## Answer

**Verdict: `SKILL_FIT_CONFIRMED`.** It covers only the six archives below, identified by these exact bytes. It is void for any other bytes, including a repackaging of the same trees.

| Package | Files | Bytes | sha256 | Extracted freeze digest |
|---|---|---|---|---|
| change-flow.skill | 25 | 390,333 | `eea8dd2068fdce1e0b80c0c84f658745544ac3673663831e4bd9663602204bfd` | `25 c9b0927f327c31328c4b64a0408a946619c985a492702a70a2cd88e216cf22c2` |
| flowmaster-validate.skill | 37 | 507,685 | `1e8d413234cc4d388cb1d3ff7486de182639314bfbcb331889a4dfa0498d4e7c` | `37 02a69b8a99181e79e554299a51dcc31e8b6b629d4974d05c96b191cf948fa200` |
| glow-hde-pr-development.skill | 4 | 23,332 | `1aad2cf4f9ff0ad54dd8612aa78d1bedce7c45be5759163262effa5e847d2409` | `4 f0880ceb6c5d8104a79fb37260ce2cdd90cac110878eaabc2a12106f8b6bbaf0` |
| glow-graph-contract.skill | 9 | 58,371 | `2b6cc39637dc374d2ca3bfb4d2de1cccb90d30fcc1dc8ef46baa7589a5f3131e` | `9 d00c8d1705e3aa181b22c151f103edc9a0f9eccdcfe593fd3a92b90cb0fec6b9` |
| session-relay-flowmaster.skill | 5 | 56,563 | `6028346473f984519d78284efa8d295d257019c83f984ebacd3596427a13c1c4` | `5 33d8b9be98288b1ba698a403964409fb65f5cc53d81cbd94a348ff5b3ce4b52c` |
| amthor-workspace-governance-audit.skill | 15 | 57,190 | `6199c76d1cd607284d7760ec2f121cd665dc7eb152c9e53a3704899cd479fd96` | `15 f0f00820a1df24d20974dd3ad1a58bc4cb8d358d6e7b9a77ccd9ec26329e45f8` |

**Round-1 findings:**
- **R-1: fixed.** The retired F05 sentence is gone from both places it was stated. The new text matches PF06 §0.1A and the F05 wording in change-flow and the PR skill.
- **R-2: fixed.** The pre-D27 rule is gone from all three places it was stated. The new text uses the same D27 wording as change-flow and flowmaster-validate.
- **The repair adds no defect.** Its guard does what it is meant to do, but it is narrower than its comment says (L-C1, LISTED).

**Trend (D26-A rule 5).** Distinct REQUIRED defects went from 2 to 0.

**What I measured.** I took every value in this record from the bytes I was given.
- The baseline reproduces.
- Every §8 gate passes from the extracted contents.
- `package_build.py --check` rebuilds all 95 files exactly.
- The round-1 build script, rerun, reproduces the round-1 trees. The repaired audit differs from them in exactly the four files C11 names, and in exactly the lines of `execute/d24-repair.patch`.
- Every hash pin agrees with the artifact it pins.

**Findings.** Two are new, and both are LISTED:

| ID | Class | Artifact | Defect |
|---|---|---|---|
| L-C1 | LISTED | audit `scripts/run_fixture_suite.py:357–364` (DR-GUARD) and how the record describes it | The guard matches three exact sentences, case-sensitively. A reworded retired rule passes. The record and the code comment say more than the test checks. |
| L-C2 | LISTED | change-flow `SKILL.md:284` (unchanged from baseline `:280`) | The runtime entry gate still requires "The exact authorized environment execution route for bounded Ops and QA work". D27 says no particular QA venue is required. |

I re-classify no round-1 LISTED finding (see *Round-1 LISTED findings*).

## 1. Identity, reproduced before review

- **Archives.** I copied the six read-only `.skill` files to `/tmp/d24c/pkg`.
  - All six match §1 in sha256, byte size and entry count: 25, 37, 4, 9, 5 and 15 entries.
  - Every entry is a regular file under its own skill root. There are no directory entries, absolute paths, `..` segments, backslashes, symlinks or duplicate names.
- **Baseline.** I copied the installed directory to `/tmp/d24c/inst`. With `freeze.py`, the copies and the live directory (read-only) both give the six §3 digests: 22, 31, 4, 9, 5 and 15 files. Since the baseline reproduced, the review went ahead.
- **Extracted trees.** All six freeze digests match §1.
  - `name:` is unchanged in every SKILL.md. In fact the whole frontmatter block is byte-identical to the baseline in all six.
  - From a copy of skill-creator, `quick_validate` returns `Skill is valid!` for all six.
- **§8 c, installed against extracted (`diff -rq`).** Exactly the 26 paths in §8 c differ, and nothing else.
  - No installed file is missing.
  - `fixtures/gcfpe-20261009.1-100926.1/` holds only `scenarios.json`.

## 2. Gates I ran, from the extracted contents

R is `/tmp/d24c/R`: the six extracted skills plus copies of the seven L3 siblings. Every command ran with `PYTHONDONTWRITEBYTECODE=1`. I read each top-level flag by its own name, and took each exit code from a capture that keeps the producer's own status.

| # | Gate | Result |
|---|---|---|
| 1 | `validate_flowmaster.py --skills-root R` | Exit 0. `verdict` FLOWMASTER_SUITE_PASS, `suite_ok` true, findings 0/0/0/0, `self_identity` OK, six skills PASS. Current overlay: profile `GCFPE-20261009.1-100926.1-VALIDATION`, `ok` true, `SELECTED_PRODUCTION`, 235 edges. Current fixtures: `fixture_suite_ok` true, 54/54, variants 55/55, all 283 cases passed, all 13 `dependency-*` cases passed. `rows_exact` and `interfaces_closed` are true. Change-flow fixtures: 34/34 (14 positive, 20 negative). |
| 2 | The same, with the explicit 100926.1 contract and candidate root `X` | Exit 0, FLOWMASTER_SUITE_PASS, 0 findings. The explicit entry ran the 100926.1 profile with `ok` true, and its fixtures passed 283 cases. |
| 3 | flowmaster `validate_gcfpe_20261009.py R/change-flow --contract …100926.1…` | Exit 0, `ok` true, `errors` []. |
| 4 | `run_gcfpe_20261009_fixtures.py` (same contract) | Exit 0. `fixture_suite_ok` true; 54/54, 55/55 variants, 283 cases. |
| 5 | `run_change_flow_fixtures.py` | Exit 0; 34/34, `fixture_suite_ok` true. |
| 6 | change-flow `validate_gcfpe_20261009.py` | Exit 0, `PASS: change-flow GCFPE-20261009.1 contract and Markdown-only source policy`. Its 091426.1 sibling: exit 1, `FAIL: specialization revision`, by design (L4). |
| 7 | `validate_glow_hde_pr_development.py` | Exit 0, PASS. |
| 8 | audit `run_fixture_suite.py` | Exit 0; 38 tests, OK, including `test_retired_mb008_role_and_numbering_rules_absent`. |
| 9 | `validate_relay_manifest.py --self-test` | Exit 0, `status` PASS. |
| 10 | Regenerator, run from the repository root, with `<G>`/`<F>` extracted and `<I>` my verified copy of the installed directory | Built from `docs/graph/parts`: 55 nodes, 229 edges, 575,074 B, `ae2bd159…`; recipe output 613,326 B `dbae180b…`, **2 EQUAL**. Candidate parts: 235 edges, 593,625 B `a58666e5…`; contract 634,423 B `90593603…`, **byte-equal** to `execute/contracts`. Production parts: 593,569 B `43f84f29…`; contract 631,061 B `cd291f17…`, **byte-equal**. |
| 11 | `package_build.py /tmp/d24c/inst /tmp/d24c/ext … --graph <my production embedded JSON> --check` | Exit 0; `equal` true; `differing` []; 95 files. The graph argument is the text between the first ```` ```json ```` line and the last ```` ``` ```` line, plus its final LF: 593,569 B `43f84f29…`, byte-equal to both bundled graph copies. |
| 12 | `plan/package_apply.py /tmp/d24c/ext --check` | Exit 1, as the record states. 44 `LANDED`. AU-REV and AU-REV-FX are `CONFLICT`, because DR-REV and DR-REV-FX supersede them; 1.14.1 is in both files. |

**Beyond the brief:**

| # | Probe | Result |
|---|---|---|
| 13 | Round-1 reconstruction: `package_build.py` from `894966c` (no step A2), copied to scratch with `plan/` linked read-only | Rebuilds the audit at `15 43e76519…`, the round-1 digest, and the other five at the §1 digests. Round-1 tree against round-2 tree: exactly four audit files differ (`SKILL.md`, `references/interoperability-contracts.md`, `references/project-prompt-registry-schema.md`, `scripts/run_fixture_suite.py`). Their 16 changed lines are identical to `execute/d24-repair.patch`. The `plan/` artifacts and the contracts are unchanged since `894966c`. |
| 14 | `plan/registry_assemble.py check --stage candidate --registry execute/candidate-registry.md --audit-root <round-2 extracted audit> …` | Exit 0, `ok` true, 0 validator errors and 0 warnings, 55 of 55 rows `ACTIVE`, no drift. X11's registry result holds with the repaired audit. |
| 15 | Guard probes on scratch copies of the audit (L-C1) | Each retired sentence put back alone fails the new test: `SKILL.md` R-2, `interoperability-contracts.md` R-1, registry schema R-2. Each run is 38 tests with 1 failure, exit 1. A reworded rule passes: 38 tests OK, exit 0. |
| 16 | Explicit-contract dispatch | 091426.1 contract: its own profile runs and fails loudly on `CHANGE_FLOW_SPECIALIZATION_REVISION: 3.3.1` and `GLOW_HDE_PR_DEVELOPMENT_SKILL_REVISION: 1.3.1`. The 091326.2 alias: the 100926.1 profile runs and fails loudly with `target_release` `GCFPE-20260913.1`. This reproduces round 1's L-6. |
| 17 | The 17 MB-008 fixtures, projected against the 091426.1 contract and the installed change-flow text | CONT-POS-02, TS-POS-01, TS-POS-02, REM-POS-02 and REM-POS-03 still pass on the baseline. This reproduces L-B2 defect 2. |

**Bundled copies (C2).** Both `…100926.1-direct-handoff-contract.json` copies are byte-equal to `execute/contracts/…-production-contract.json` and to my regenerated production contract (631,061 B `cd291f17…`). Both graph copies are byte-equal to my production build's embedded JSON (593,569 B `43f84f29…`).

## 3. Counts and pins (§8 d to f)

**§8 d.**
- **The profile's pins match the bundled files:**
  - `candidate_contract`: `cd291f17…`, 631,061 B.
  - `frozen_graph`: `43f84f29…`, 593,569 B, 55 nodes, 235 edges.
  - `fixtures`: `e24c881d…`, count 54. The file is 26,868 B.
- **The fixture document:**
  - 54 scenarios: 31 positive, 23 negative, 55 variants. Rows 38 to 54 are the 17 MB-008 cases, 11 positive and 6 negative.
  - `required_fixture_ids` is in row order.
  - `negative_rule_attribution` equals the runner's `EXPECTED_NEGATIVE_RULES`, and its keys are exactly the 23 negatives.
- **Parents.** change-flow's `EXPECTED_PARENT_BY_LANE` has 16 lanes. It equals the `staged_parent_id` of all 55 members, with no mismatch.
- **Members and edges.** The contract has 55 members, the same set as the graph's 55 nodes. The graph has 235 edges.

**§8 e.** I recomputed each pin from its artifact:

| Pin | Value | Consumers that agree |
|---|---|---|
| Frozen graph | `43f84f29…`, 593,569 B | flowmaster `EXPECTED_FROZEN_GRAPH_SHA256`/`BYTES`; change-flow `EXPECTED_GRAPH_SHA`; the profile; the contract's `source_snapshot.frozen_candidate_graph` |
| Contract | `cd291f17…`, 631,061 B | `EXPECTED_CANDIDATE_CONTRACT_SHA256`/`BYTES`; the profile |
| Fixtures | `e24c881d…` | `EXPECTED_FIXTURE_SHA256`; the profile |
| Routing surface | `d3a08833964a2610f88bd754b7e7510d`, 290 rows | Computed on the bundled contract by each validator's own `routing_surface()`; equal to both validators' `EXPECTED_ROUTING_SURFACE`/`_ROWS` |
| Governing plan | `4de47784…`, 50,156 B | `PLAN-20261011.md` at HEAD; flowmaster's plan literal; change-flow's `EXPECTED_PLAN_SHA`/`BYTES`/`PATH`; the contract's `governing_plan` |
| Predecessor | `dbae180b…`, 613,326 B | The bundled 091426.1 contract; change-flow's `EXPECTED_PREDECESSOR_CONTRACT_SHA`; flowmaster's `PREDECESSOR_CONTRACT_PIN`; the contract's own pin |
| `SKILL_TREE_SHA256` | `429eda21…` | Recomputed with the validator's `skill_tree_digest`; `validate_self_identity` returns [] |

**§8 f. Revision sites.**
- **change-flow 3.4.0.** Live at:
  - change-flow `SKILL.md:8` and its own validator;
  - flowmaster `validate_flowmaster.py:146` and `:1357`;
  - flowmaster `validate_gcfpe_current.py:647–648`.

  Older values survive only as history or mapping: 3.3.1 in change-flow's 091426.1 validator (history), 2.0.0 in the two R1 oracle files and the oracle mapping at `validate_flowmaster.py:1356`, and 3.2.8 in flowmaster's narrative.
- **PR skill 1.4.0.** Live in its `SKILL.md:8`, its validator, flowmaster `validate_gcfpe_20261009.py:2729` and `validate_gcfpe_current.py:664`. 1.3.1 survives only in the 091426.1 validator.
- **Relay 3.3.0.** Live in its `SKILL.md:8` and `validate_flowmaster.py:186`.
- **`FLOWMASTER_VALIDATE_REVISION` 3.4.0.** Live at `SKILL.md:8`. The values 3.2.13 to 3.2.16 appear only in dated narrative.
- **`validator_revision` 3.4.0.** Live at every 100926.1 site: the profile, the runner, the suite and the validator. 3.3.2 survives only in the 091426.1 files.
- **`WORKSPACE_GOVERNANCE_AUDITOR_REVISION` 1.14.1.** It appears in `SKILL.md:10` and `run_fixture_suite.py:344`, and nowhere else in the packages. In the repository, 1.14.1 occurs only in this change's own records, so it is unspent.
- **091426.1 and 100926.1 references.** Every 091426.1 reference in `*.py` and `*.md` sits in a history file, a commented allowlist, explicit-only dispatch, or glow-graph-contract's regenerator and documentation. Every default points at 100926.1.

## 4. The repair (A0)

### R-1: fixed

- **Was** (round-1 text): "The producer does not edit PF10, allocate canon numbering, or claim adoption."
- **Now**, `SKILL.md:48`: "The producer does not edit PF10 or claim adoption; it numbers the addendum at creation from the current controlled PF10 Markdown (`PF06-Canon-Change-Process-Guide` §0.1A)."
- **Now**, `references/interoperability-contracts.md:42`: the same rule, with "the producer" as subject.
- **Against PF06 §0.1A.** PF06 says: "Resolve the current continuous addendum number and format before authoring. Each addendum has one H2 with the next number…" The new text agrees.
- **Against the other packages:**
  - The PR skill says "the responsible producer numbers it at creation from the current controlled PF10 Markdown". Its validator pins that phrase.
  - change-flow `:327` says "Before authoring, it resolves the next continuous addendum number from the current controlled PF10 Markdown".
  - The contract has `producer_allocates_pf10_number: true`, and its `number_carrier` is the H2 heading.
- **Nothing contradicts it.** The neighbouring `interoperability-contracts.md:38` ("The governance auditor never edits, numbers, publishes…") binds the auditor, not the producers. No line in the audit still says that a producer does not number.

### R-2: fixed

- **`SKILL.md:59`:** "DevOps owns bounded Ops execution, not PR-development workflow control; QA execution follows the arrangement the Product Owner chooses (`D27`)."
- **`interoperability-contracts.md:29`:** "DevOps executes bounded Ops instructions; QA execution follows the arrangement the Product Owner chooses (`D27`)."
- **`project-prompt-registry-schema.md:80`:** "DevOps executes bounded Ops tasks; QA execution follows the arrangement the Product Owner chooses (`D27`);"
- **Against the other packages.** These lines use the exact phrase of change-flow `SKILL.md:10` and flowmaster-validate `SKILL.md:299`. They sit beside the already-redlined `SKILL.md:42` and `interoperability-contracts.md:30`.
- **Against D27.** D27 says: "Kronos authors the steps/tasks. The Product Owner has wide latitude about execution; an executor/session identity or particular venue is not required." The new lines agree.
- **What is left.** Nothing in the audit gives QA execution to DevOps.
  - `interoperability-contracts.md:27` still lists Kronos's duties without execution ("create QA tasks, analyze committed QA evidence, and issue QA acceptance review"). That matches D27's "Kronos authors", and line `:29` now covers execution. It is round-1 L-B1, LISTED, and not new.

### The guard (DR-GUARD)

- **It fires on each retired sentence.** I put each one back, alone, into a scratch copy, and each run fails the new test (probe 15).
- **It is narrow.** It checks three literal, case-sensitive sentences, and a reworded rule passes (L-C1). That limit does not touch these bytes: my broad match finds no reworded rule anywhere in the audit.

### The revision, 1.14.0 → 1.14.1 (DR-REV, DR-REV-FX)

- **Required.** `skill-identity-and-freeze.md` (*Advertised identity must be unspent*) says: "A spent identity is one already bound to a published §10 verdict … Corrected bytes never reuse one." The round-1 verdicts are bound to 1.14.0.
- **Unspent.** 1.14.1 occurs only in this change's records.
- **A deviation from the PLAN, disclosed.** The approved PLAN says "revision 1.14.0" (§3 PART-01). The MODIFICATION record's §E *Disclosed deviations (EXECUTE)* discloses the change, and X10's rollback ("repair and re-review on new bytes") covers it.
- **Nothing left behind.** No later plan step writes 1.14.0: the only repository occurrences are `plan/package-redlines.json` and `plan/patches/amthor-workspace-governance-audit-mb008.patch`, and neither feeds anything after X10.

### Did the repair add a defect?

No. The four changed files are exactly what C11 says. The audit's other scripts (the registry engine X11 used) are byte-identical to round 1, and none of them reads the changed reference files. X11's `check` passes with the repaired audit (probe 14). The audit fixture suite passes.

### My broad match for the retired rules (D26-E)

**Patterns,** case-insensitive, over all six extracted trees in `*.md`, `*.py` and `*.json`. The 091426.1-and-earlier bundled contracts and glow-graph-contract's batch reports were excluded.
- For F05: `numbering`, `does not number`, `not number`, `numbers the`, `allocat… (the|canon|pf10)`, `pastes and`, `final pf10`, `never number`, `owner numbers`, `nathan numbers`, `assigns … number`, `final … number`, `choose … number`.
- For F02: `devops … qa`, `qa … execut… … (devops|operator|environment)`, `environment operator`, `executes qa`, `qa executor`, `kronos never`, `never executes`, `KRONOS_NEVER`, `kronos … (may not|cannot|must not|does not) execute`, `authorized qa lane and its operator`, `qa execution remains`, `ops and qa`, `qa/ops`.

**Every hit is accounted for:**
- **Guards, fixtures and the oracle.**
  - The forbidden-phrase lists in change-flow's validator, the PR skill's validator and the audit's new guard.
  - The fixture keys `pf10_numbering` and `product_owner_numbers`.
  - The immutable R1 oracle and runtime maps (the GCF-23 actor). These were accepted at PLAN as L-A11 and listed in round 1 as L-12.
- **Text that is consistent.**
  - change-flow `:477`, where QA-10 has no numbering authority. QA-10 is not a producer.
  - The audit's `interoperability-contracts.md:38`, about the auditor.
  - The Ops-only operator receiving roles in the contract.
  - Relay's "Relay does not execute QA".
- **Round-1 L-1.** The contract's `support_skill_policy` still reads "QA execution remains with the authorized QA lane and its operator". It is deferred and not re-classified. C11's phrase "no surviving active text" holds only with this listed exception.
- **Inert history.**
  - change-flow `references/pre-guide-audit-correction.json:91`: "addendum preparation does not authorize live-ledger inspection or final numbering." This is the 20260906.1 QA-15-era correction. It is byte-identical to the baseline, and no SKILL.md references it. Its validator, `validate_pre_guide_correction.py`, has no caller in any package. Unlike the other history files, change-flow's history paragraph (`:570`) does not name it; that is cosmetic.
  - The audit's `epic-reengineering-interoperability.md:45`: "Never mutate PF10 or choose final numbering". It sits under the MB-003 *Historical and non-operative* banner.
- **New, LISTED.** change-flow `SKILL.md:284` (L-C2).

## 5. Findings

Both are LISTED under D26-A rule 3. Neither has a silent outcome on the normal path, and neither changes what these bytes do on the promotion path. Under D26-A rule 4, each goes into the promotion packet as an accepted risk or onto the backlog.

### L-C1 — the new guard matches exact sentences, not the rules

- **Artifact.** amthor-workspace-governance-audit `scripts/run_fixture_suite.py:357–364`. Also the descriptions of it:
  - its own comment: "must not survive anywhere in this skill's text";
  - brief §2: "fails if either retired rule returns anywhere in the audit's *.md";
  - the MODIFICATION record's X10 row: "fails if either retired rule returns".
- **Defect.** `assertNotIn` checks three literal, case-sensitive sentences. A reworded rule, or a sentence that only differs in case, passes. The neighbouring `test_retired_d22_phrases_absent` lower-cases its input; this test does not. So it guards against the exact sentences coming back, not against the rules coming back, which is what the descriptions say.
- **Evidence.** Probe 15:
  - Each of the three retired sentences, put back alone: 38 tests, 1 failure, exit 1.
  - Appending "The producer does not number the addendum; Nathan numbers it. DevOps executes QA." to `references/rule-catalog.md`: 38 tests, OK, exit 0.
- **Path, likelihood, consequence.**
  - The path is only a future edit to the audit that restates a retired rule in new words.
  - The likelihood is low.
  - The consequence is that this guard stays green; D26-E's broad match and a review would still have to catch it. The shipped bytes are correct.
- **Smallest correction.** At the next audit maintenance:
  - describe the guard as "fails if any of three retired sentences returns verbatim";
  - optionally lower-case the text, as the D22 test does;
  - optionally add two loose patterns, such as `DevOps[^.]{0,60}\bQA\b` and `allocat\w*[^.]{0,30}number`.

  No repair round is needed.

### L-C2 — change-flow's entry gate still requires an exact QA execution route

- **Artifact.** change-flow `SKILL.md:284`, in the runtime entry gate's input list: "The exact authorized environment execution route for bounded Ops and QA work." The line is unchanged from the baseline (`:280`). Round 1 did not raise it.
- **Defect.**
  - It makes an exact QA execution route an entry prerequisite of every run, and `:293` rejects a missing input.
  - D27 (*QA authorship and execution*) says: "The Product Owner has wide latitude about execution; an executor/session identity or particular venue is not required." The same SKILL.md states D27 at `:377` and `:391`.
  - The line is in the F02 domain of a package this change edits for F02. Its wording ("Ops and QA work") matched none of the record's D26-E patterns.
- **Why it is not a canon breach.** PF04-Canon-HDE-Governance §9.1.1 gives QA task execution to an "Authorized environment/DevOps path". A route the Product Owner chooses and authorizes can be read as that path.
- **Path, likelihood, consequence.**
  - The path is the entry gate of every FRESH or RESUME run.
  - The likelihood of harm is low, because the operator can name the Product Owner's chosen arrangement as the route.
  - At worst the gate refuses loudly at entry, or asks for a QA venue that D27 says need not be fixed. Neither outcome is silent.
- **Smallest correction.** At the next change-flow maintenance, replace the line with: "The exact authorized environment execution route for bounded Ops work, and the QA execution arrangement the Product Owner chooses (`D27`); no executor, session identity or venue is fixed at entry."

## 6. The claims

| Claim | Disposition |
|---|---|
| C1 | **Confirmed, read together with C11.** `diff -rq` shows exactly the §8 c list. `package_build.py --check` reproduces all 95 files. Two parts of C1 are not literal: AU-REV and AU-REV-FX's value 1.14.0 is superseded, and eight repair operations were added. C11 and §E disclose both. `package-redlines.json`, `package_apply.py` and the patches are unchanged since `91add4b`; only PIN-1-A's three files changed after it. |
| C2 | **Confirmed** (§2, bundled copies). |
| C3 | **Confirmed.** The default run uses the 100926.1 profile. The 091426.1 profile runs only when its own contract is passed. Any other explicit contract goes to the 100926.1 profile, which fails loudly for a third release (probe 16, round-1 L-6). |
| C4 | **Confirmed** by the gates and the lines I read. V1: `KRONOS_NEVER_EXECUTES_OPS.` at `:389` and `QA_EXECUTION_ARRANGEMENT = PRODUCT_OWNER_CHOICE` at `:391`; the retired token is forbidden in both validators; both R1 oracle files are unchanged (`diff -rq`). V2 and V7: §3. V3, V4 and V6: confirmed through gates 1 to 6 and `validate_flowmaster.py:1792`. I did not re-derive V3's link list line by line. |
| C5 | **Counts confirmed:** 37 + 17, of which 11 are positive and 6 negative. **The method statement is overstated:** round-1 L-4 and L-B2, reproduced by probe 17. |
| C6 | **Confirmed** as a description of the code. I read the required and forbidden clause lists and the parent, manifest and URL checks. |
| C7 | **Confirmed.** The validator passes. Its required phrases (`:26–31`) and forbidden phrases (`:131–132`) are as stated. |
| C8 | **Confirmed** (gate 10). |
| C9 | **Confirmed, with the round-2 value.** The audit now advertises 1.14.1, not the 1.14.0 that C9 states. §2 of the brief records the change. |
| C10 | **Confirmed and disclosed.** Each addition is a named, count-checked substitution, reproduced by `--check`. |
| C11 | **Confirmed.** Only the audit differs from round 1, in exactly the four files named (probe 13). Its other scripts are byte-identical, and X11's check still passes (probe 14). No active SKILL.md or audit text states a retired rule. The accounted exceptions are in §4. |

## 7. Answers to the §6 questions

- **A0 — the repair.**
  - R-1 and R-2 are each fixed in every place their rule was stated. The new text matches PF06 §0.1A, D27, and the other packages' wording (§4).
  - The guard tests the three retired sentences, not rewordings of them (L-C1).
  - The repair added no defect.
  - My broad match finds no surviving active statement of either rule beyond round-1 L-1, the inert history above and L-C2.
- **A1 — the 17 fixtures and six rules.**
  - On the facts they model, the rules match their rulings:
    - F01 matches D27 *Continuity*.
    - F02 matches D27 *QA authorship and execution*, and its arrangement and Kronos tokens.
    - F05 matches PF06 §0.1A and PF27's numbered-H2 form, with no standalone number field.
    - F07 matches PF10 addendum 2.1 rules 2 to 4 and PF04 §9.1.3's surface advice.
    - F08 matches ESC-40's three verdicts and ESC-25/ESC-30's proposal or legacy id.
    - F09 matches `receiver_compatibility.PR-20`'s RS-20 return, only from the recorded planning origin before Proceed.
  - The rules accept forbidden cases only on facts they do not model: round-1 L-3, and L-B2's F02 Ops branch.
  - The F07 rule and CONT-POS-02 are near-tautological as regression evidence. Probe 17 shows five positives still pass on the baseline contract and text.
  - Reading change-flow's text is sound for F01's recovery sentence and F02's tokens, because the contract has no field for either.
  - For F08 the stated reason does not hold: the contract does carry ESC-40's `result_states` (L-B2).
  - The 13 dependency cases each prove a dependency on what they remove, and all pass. Six invariants are never removed (L-4). All of this is round 1's, and stays LISTED.
- **A2 — change-flow's `validate_gcfpe_20261009.py`.** Removing the URL-map and topology checks dropped nothing 100926.1 has.
  - It still pins staged parents per lane: 16 lanes, equal to all 55 members (§3).
  - It still checks manifest parent parity, and the URL format, against the graph.
  - The member-URL check proves only that the contract matches the graph it was derived from (L-15). Independent evidence of the live bindings comes from X1, X4, X6 and X12.
  - Every remaining pin is measured from the right artifact (§3 e).
- **A3 — the X8 additions.** M-A1, M-A2, C20 and C21 are needed, disclosed in §E and reproduced by `--check`. The disclosed dry-run gap is real and accurately stated: the dry run measured N6 before N8 moved the PR revision. No finding.
- **A4 — does anything still treat 091426.1 as current?** No caller, default or document in the six packages does (probe 16). The `gcfpe_20260914_candidate*` coverage keys mislead a human reader but are harmless to a machine, because every entry carries `profile` and `target_release`. Not a finding.
- **A5 — the Kronos substring.** The old token cannot survive anywhere it would be read as active.
  - change-flow's own validator forbids it anywhere in SKILL.md, case-insensitively (`validate_gcfpe_20261009.py:1065`).
  - The suite forbids it outside the marked prohibition block. A copy inside the block passes the suite and fails gate 6 loudly (round-1 L-5).
  - It remains only in the immutable R1 oracle, mapped by `maintenance_metadata`, and in the validators' own lists.
- **A6 — the approved redline texts as landed.**
  - F01, F02, F04, F05, F07, F08 and MB-003 agree with D27 and the canon I read.
  - F05 agrees with PF06 §0.1A and PF27. F07 agrees with PF10 addendum 2.1 and PF04 §9.1.3.
  - **Canon note on F02.** PF10 is silent on QA execution. PF04 §9.1.1 gives QA task execution to an "Authorized environment/DevOps path", and "Kronos independently reviews actual evidence". I read the Product Owner's chosen arrangement as that authorized path, so the D27 wording, including the repaired audit lines, does not breach it.
  - The remaining tension, that Kronos would review its own execution when the Product Owner chooses Kronos, comes from the approved change-flow and flowmaster text, not from the repair. It is round-1 L-12, accepted.
  - SR-F07-1's "run" is as approved.
  - New: L-C2.
- **A7 — the docs.**
  - D-FV-1's "repository file on `main`" is not yet true. The plan is absent from `origin/main` (round-1 L-7, L-B3).
  - D-FV-8's "each by its own release's profile" is overstated (probe 16, L-6).
  - D-GG-1 overstates what is derived, and the text around it goes stale at X21 (L-10, L-B4). I did not re-derive D-GG-1 beyond gate 10.
  - The other D-FV items agree with the code I ran.
- **A8 — fit with the 100926.1 candidate.**
  - The contract's 55 members are the graph's 55 nodes, and the graph has 235 edges.
  - All 55 staged parents equal their lane's pinned parent.
  - Receiving roles and bodies are X12's to check. No prompt body was read here.

**Q1 — is anything in the packages false between their build and X16?**
- **True only after X16.** These are consumed by nothing before the X17 install:
  - the contract's `SELECTED_PRODUCTION` selection fields;
  - change-flow's statement that 100926.1 is the current overlay, and that 091426.1 is a superseded predecessor.
- **Stale after X16 (minor).** flowmaster `SKILL.md:155` names "the selected 091426.1 contract" as the predecessor.
- **Still false after install.** `REPOSITORY_FILE_ON_MAIN` stays false until PR #605 merges (L-7, L-B3).
- **The repair is not affected.** It adds nothing release-dated, and no later step writes the audit's revision anywhere.

**Q2 — should the 091426.1 change-flow check say in its own text that it is history?**
- Yes. Its docstring still reads "Deterministic checks for the GCFPE-20260914.1 Change Flow successor". It prints a bare `FAIL: specialization revision` (gate 6). change-flow's SKILL.md does not name it.
- The cheapest fix is a one-line historical docstring, plus a mention in change-flow's history paragraph at `:570`.
- It is not needed for these bytes: no document names it as a current gate, and flowmaster's `REQUIRED_SCRIPTS` comments it as history.

## 8. Round-1 LISTED findings

- **Nothing re-classified.** I re-classify none of L-1 to L-15 or L-B1 to L-B5.
- **Reproduced:** L-6 (probe 16), L-B2 defect 2 (probe 17) and L-7/L-B3 (the plan is absent from `main`).
- **The IA-40 sentence stays LISTED.** This is L-13, and the third sentence of L-B1, in `project-prompt-registry-schema.md:80`: "IA-40 revises only an initial, not-yet-approved Implementation Plan". The repair edited the same line for R-2 and left this sentence. I agree that it stays LISTED:
  - **Not on the enforced path.** `SKILL.md:146` points enforcement at `interoperability-contracts.md`. There, IA-40's rule (`:26`) and `SKILL.md:61` limit only "exact-redline successors" to unapproved artifacts, and send approved deltas through the addendum overlay. That is compatible with IA-40's separate pending `MATERIAL_PLAN_DELTA` mode.
  - **Its failure would be loud.** At worst it causes a false finding that reaches a human reviewer.
  - **The real behaviour is checked elsewhere.** IA-40's `PLAN_DELTA_PENDING` is pinned by the contract hash and checked at X12.
  - **It predates this change.** The sentence was already wrong in 091426.1.

## 9. What I ran, what I could not, and disclosures

- **Ran:**
  - §8 a, b (all ten gates, the regenerator in three forms, and the reproduction), c, d, e and f, as recorded above;
  - probes 12 to 17;
  - `quick_validate`.
- **Did not run, or could not:**
  - No body-level check. Under L1 and D22, no prompt body was read, copied, hashed or compared, and no transient body file was made.
  - No live Notion state (L5).
  - I did not run `package_skill`, because the archives do not reproduce by repackaging (L2); §8 b reproduces the trees instead.
  - I did not run the author's `x8_gates.py`; I reran its gates myself.
- **Disclosures:**
  - For gate 10 I used my verified copy of the installed directory as `<I>`. Its freeze digests equal the live directory's.
  - Several probes imported modules from the extracted trees without `-I`, because the runner needs its sibling imports. These are the packages under review. Every run had `PYTHONDONTWRITEBYTECODE=1`. A final `find` shows no `__pycache__` anywhere in `/tmp/d24c/R` or `/tmp/d24c/ext`, and the six extracted digests are unchanged.
  - To reconstruct round 1, I copied `package_build.py` from `894966c` into scratch and linked `plan/` read-only. It wrote only to `/tmp/d24c/r1out`.
- **Repository writes.** Nothing outside this record. `git status` was clean before I wrote it. I made no commit and no push, and wrote nothing to Notion, `docs/pfcanon/` or the synced skills directory.

**Freeze.** Nothing moved during the review. No skill was installed.
- At the end, all 13 installed skills give the same digests on the live directory and on my copies:
  - the six of §3;
  - `flowmaster-primary 2 2d41da26…`, `glow-merged-change-attribution-lock 10 c518ccb0…`, `glow-po-reporting 1 7e04368a…`, `session-branch-flowmaster 2 17b5800b…`, `skill-creator 18 e4fee9c9…`, `tw-flowmaster 2 0581205b…` and `typesafe-scoring 3 088c77f3…`.
- The six source archives in the scratchpad still hash to §1.

**Canon relied on:** read on `origin/main` `9312add`.
- **`AGENTS.md`.**
- **PF06-Canon-Change-Process-Guide v2.5.4 §0.1A**, read in full.
- **PF10-HDE-Build-Notes v13.5.2**, read in full: precedence rules 1 to 9 and addendum 2.1. It is silent on QA execution and on addendum numbering, so permanent canon governs those.
- **PF04-Canon-HDE-Governance v2.8.7 §9.1.1 to §9.1.6**, read in full.
- **PF27-Canon-Plan-Templates v2.0.5**, *Canon precedence for template use*, read in full:
  > Applicable, active, non-superseded PF10 addenda supersede conflicting PF-Canon only for the exact scope they address; otherwise follow PF-Canon. A formally approved bounded Product Owner rescope may supersede conflicting PF-Canon only for the exact decision it adjudicates.
- **PF03-Reference-Technical-Writing-Best-Practices v1.8.8**, line 346 on the addendum form: a search hit read in context; no complete read is claimed.
- **Controls:**
  - `gcfpe.decision-record.md` D22, D24, D26 and D27, in full;
  - `skill-identity-and-freeze.md` and `skill-packaging-and-delivery.md`, in full;
  - `freeze.py`.
- **In-flight records:**
  - `MODIFICATION-20261011-gcfpe-mb008-to-promotion`: §A.2, §A.6, §P (accepted risks, the returns to Nathan, and the approval to enter EXECUTE), §E rows X7 to X12, and *Disclosed deviations (EXECUTE)*.
  - `PLAN-20261011.md`: §3 PART-01 at line 68, the §5 X8 to X13 rows, and the §7 X16 and X17 rows. No complete read is claimed.
  - The parent `MODIFICATION-20261009-gcfpe-latest-alpha-analysis`: the Q3 decision at lines 292 and 303.
  - `execute/d24-repair-redlines.json`, `d24-repair.patch`, `x10-packages.json` and `x10-repair-gates.json`.
  - `execute/package_build.py`: its header, `build` and `main`.
  - `execute/REVIEW-D24-A.md` and `REVIEW-D24-B.md`, in full.

NOTHING NEEDED
