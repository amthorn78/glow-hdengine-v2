---
artifact_type: PROMPT_ECOSYSTEM_POSTFLIGHT_REPORT
artifact_version: "1.0"
created_date: 2026-09-21
author: independent post-flight auditor (fresh session; not PE35, not SFR-01)
round: 27
release: GCFPE-20260914.1 / 091426.1 / 55 — UNSELECTED_CANDIDATE
prompt: docs/ephemeral/gcfpe.round27/POSTFLIGHT-PROMPT-r27.md v1.1
verdict: PASS WITH WARNINGS
---

# Post-flight — GCFPE-20260914.1 / 091426.1 / 55

## Verdict

**PASS WITH WARNINGS.** No mandatory open finding. The Product Owner may prepare a promotion
decision packet.

**Nothing in the candidate release stops the flow.** Every check in scope ran and passed: all
55 bodies, all 831 registry assertions, all five installed gates, the graph against its proof
token, the `D15` terminal invariant, registry-versus-graph drift, the PF10 producer set, and
`PR-20`'s declared inputs. Zero findings are returned to any prompt owner.

The three warnings are against **the post-flight procedure and the shipped fixture runner's own
reporting** — not against the 55 prompts. Each offends the record; none stops the flow. They are
recorded because the next auditor will hit the first one and could mistake it for a defect, and
because the third one is the exact failure mode this round's prompt warns about, one level up.

## What was audited, and what reproduced

Every frozen identity in `FREEZE-SNAPSHOT-r27.md` was reproduced in this session before any
auditing began, using `docs/prompt_ecosystem_management/freeze.py` rooted at the skill directory.

| identity | frozen value | reproduced |
|---|---|---|
| installed `change-flow` | 21 files · `14981ba71e6fe400b4ae0d42410ce9bd9144e5b02bf73bfa53f2a823193240c2` | yes |
| installed `flowmaster-validate` | 29 files · `9c0ca6fe1811e444193daccf67c29a65d9f623fcf4d1e255095ae932a646a833` | yes |
| candidate contract | `1c3c7969b7b933569362a35acdff6f756e2ab8577054f5038e4a95ad3794e179` / 610549 bytes | yes, byte-identical in both bundled copies |
| graph proof token | 55 nodes · 227 edges · 55 state_routes · 569902 bytes · `1d0b72582df4735b3d22dd325687b0375a624bd9ab5760c9589171049cd715a7` | yes, rebuilt from the 56 committed parts |
| `CHANGE_FLOW_SPECIALIZATION_REVISION` | 3.2.8 | yes |
| `FLOWMASTER_VALIDATE_REVISION` | 3.2.14 | yes |
| `validator_revision` | 3.2.12 | yes |
| `SKILL_TREE_SHA256` | `6f682315a9437c1275688d568ee8b79baeccdd52f9c896b89fdd617a46863a93` | yes |

The four repository controls the freeze names also reproduced at their recorded digests and byte
counts. The synced skills directory was never written to: it holds zero `.pyc`.

One cross-check worth naming, because it closes the loop between two surfaces that could have
disagreed: the bundled candidate contract's own `frozen_graph_sha256` is
`1d0b72582df4735b3d22dd325687b0375a624bd9ab5760c9589171049cd715a7` with 55 nodes and 227 edges —
the same token the builder produced from `docs/graph/parts`. The contract and the committed parts
describe the same graph.

## The corpus-free checks (§3)

| check | result | evidence |
|---|---|---|
| **a.** graph rebuild vs. proof token | **PASS** | `build: 55 nodes, 227 edges, 55 state_routes / embedded JSON 569902 bytes sha256 1d0b7258… / validation PASS` |
| **b.** unresolved endpoints; prompt-originated inbound to `PR-50` | **PASS** | 0 edges and 0 `state_route` destinations resolve to an unknown endpoint. `PR-50` has exactly one inbound edge, from the boundary node `NATHAN_ABORT_INSTRUCTION` (`from_kind: boundary`). Zero prompt-originated. |
| **c.** `D15` terminal invariant | **PASS** | 280 `state_route` rows: 72 terminal, each `next_prompt_handoff_count: 0`; 208 nonterminal, each exactly `1`. Zero violations, measured on both the `state_routes` block and the edges' `route_branches`. |
| **d.** registry vs. graph drift | **PASS** | Zero residual drift on `outputs[].consumers` and on `required_interfaces`, row by row, once each row's own self-loop recovery branch is set aside. 11 rows carry such a branch — `CF-C-10`, `CF-E-10`, `CL-40`, `CL-E-20`, `DOC-10`, `IA-10`, `IA-20`, `PR-10`, `PR-20`, `PR-30`, `PR-35`. A prompt is not a consumer of its own output, so the graph routing `X → X` for recovery while the registry omits `X` from `X`'s consumers is agreement, not drift. |
| **e.** PF10 addendum producer set | **PASS** | `exact_producer_set` is `["CF-C-30", "CF-E-30", "ESC-40", "IA-30", "QA-70", "RS-20"]` in both the rebuilt graph and the bundled contract; both installed validators report the same six as `pf10_producers`. |
| **f.** `PR-20` inputs carry no QA Guide or QA Plan | **PASS** | `PR-20`'s registry `inputs` are exactly `["PR_INSTRUCTION_ID"]`. |
| **g.** five installed gates | **PASS** | below |
| **h.** selected release and Alpha | **PASS**, at repository scope | below |

### g. The five gates, each read by its own named flag

Run from a scratch copy of the installed skills with `PYTHONDONTWRITEBYTECODE=1`. The synced
directory was not written to.

| gate | its own top-level flag |
|---|---|
| `validate_gcfpe_20260914.py change-flow --contract <C>` | `ok: true`, `errors: []`, `contract_sha256: 1c3c7969…` |
| `run_gcfpe_20260914_fixtures.py change-flow --contract <C>` | `fixture_suite_ok: true`, `case_count: 155`, `section_13_passed: 33/33`, `section_13_variants_passed: 28/28`, `profile_errors: []` |
| `validate_flowmaster.py` | `suite_ok: true`, `verdict: FLOWMASTER_SUITE_PASS`, `finding_counts: {BLOCKER 0, ERROR 0, WARNING 0, ADVISORY 0}`; all six skills `PASS` |
| `validate_gcfpe_current.py change-flow` | `ok: true`, `errors: []`, `contract_status: SELECTED_PRODUCTION` |
| `change-flow/scripts/validate_gcfpe_20260914.py` | `PASS: change-flow GCFPE-20260914.1 contract and Markdown-only source policy` |

### h. The selected release and Alpha

`validate_gcfpe_current.py change-flow` returns `contract_status: SELECTED_PRODUCTION`,
`target_release: GCFPE-20260913.1`, `prompt_version: 091326.2`, `selected_member_count: 54`,
`ok: true`, `errors: []`. The candidate contract's own `selected_alias_during_staging` agrees
exactly: `{"member_count": 54, "prompt_version": "091326.2", "target_release": "GCFPE-20260913.1"}`.

**Stated plainly:** this proves the selected release unmutated **at contract and repository
scope**. It is not a live re-read of the 54 selected Notion pages, and §3 does not ask for one —
its opening line is *"All of this comes from the repository and the installed skills."* No
selected-release page was read in this pass.

Alpha: `PF10-HDE-Build-Notes-v13.2.9.md` §2.13 states *"`HDE-EPIC040-PR03` is **ACCEPTED_FINAL**.
… The next planned unit is PR04; its PR-10 instruction-authoring stage may now begin. This
acceptance does not authorize PR04 implementation, a Proceed, merge action, PF10 modification, or
any later lifecycle execution."* No `PR04` artifact exists anywhere in the repository; the single
`HDE-EPIC040-PR04` reference in PF10 is the `invocation_binding` line of the PR-10 handoff block
itself. PR04 / PR-10 is `NOT_STARTED`.

## The body pass (§4) — 55 of 55

Worked lane by lane. Each page was read from Notion, its body held in memory, piped to the shipped
validator on stdin, checked against its registry row, and discarded. No body was written to disk,
hashed, byte-compared, or carried into any artifact. This report contains no body content beyond
the quoted clauses a finding rests on.

**Shipped validator, `--bodies-stdin`:** all 55 ids appear in `prompt_bodies_validated` across the
lane runs; `errors: []` on every run; no run returned `prompt_bodies_validated: []` for bodies it
was given. `prompt_body_checks_not_evaluated` was read on every run, never `ok` alone.

**Registry `audit_assertions`:** **831** assertions across the 55 rows — 114 `required_literals`,
0 `forbidden_literals`, 167 `required_regex`, 550 `forbidden_regex`. Every one ran. **Zero rows
failed.**

**The three-body QA closure check, run once with `QA-120`, `CL-E-10` and `CL-C-10` supplied
together:** `ok: true`, `errors: []`, `prompt_bodies_validated: ["CL-C-10", "CL-E-10", "QA-120"]`,
and — the field that matters — **`prompt_body_checks_not_evaluated: []`**. Every other run in this
pass returned `["QA_PASS_CLASS_MAP_AND_INTAKES"]` there, because that check needs all three bodies
at once. This is the first time the class map **and** the six receiver literals have been
exercised against live pages. `validate_qa_closure_bodies` resolves each receiver by Notion page
id rather than by literal field text, compares the producer's class table against
`{EPIC: CL-E-10, CRD: CL-C-10}`, and checks the intake markers on both receivers. All of it
passed.

### Two fixture families that a corpus-free run leaves empty, exercised live

`run_gcfpe_20260914_fixtures.py` reports two counters that are zero in the §3g run because that
run supplies no bodies. Both were then run against live-read bodies, because both test §0 defect
classes directly and neither requires a corpus:

- **QA-closure source cases** — supplied `QA-120`, `CL-E-10`, `CL-C-10` (the same trio §4
  authorises). `qa_closure_source_case_count: 9`, all 9 passing. These are falsification cases:
  they mutate the producer's class table, retarget a destination, delete the CRD class cell,
  duplicate the CRD row, break each receiver's intake — and each expects a specific error. They
  prove the green result above is not vacuous.
- **Artifact-timing cases** — supplied the 18 bodies whose stage categories carry a timing rule
  (`CF-C-10`, `CF-C-20`, `CF-E-10`, `CF-E-20`, `CF-PO-10`, `IA-10`, `IA-20`, `IA-60`, `PR-10`,
  `PR-20`, `PR-30`, `PR-35`, `PR-40`, `PR-50`, `QA-10`, `QA-20`, `RS-10`, `RS-30`).
  `artifact_timing_case_count: 17`, of which `artifact_timing_actual_source_mutation_count: 13`,
  all passing, with `fixture_suite_ok: true` and `case_count: 172`. This family is precisely the
  check for *"an artifact required at a stage before anything produces it"*, and it had not run.

Both runs held their bodies in one process for one subprocess call and discarded them.

## Findings

**Against the candidate release: none.** No handoff names a receiver that does not exist or names
it wrongly. No artifact is required at a stage before something produces it. No terminal branch
emits a continuation and no nonterminal branch emits none. No two prompts disagree about who
decides. No route is declared by the graph and absent from a body, or the reverse.

Three warnings follow. Each is against a control, not a prompt.

### W1 — §3g's "a scratch copy of the installed skills" means the whole synced root, and a two-skill copy fails loudly

**Control:** `docs/prompt_ecosystem_management/postflight-procedure.md` and §3g of the post-flight
prompt.

**Defect:** the instruction *"Run, from a scratch copy of the installed skills"* reads naturally as
*the two skills under audit*. A scratch root holding only `change-flow` and `flowmaster-validate`
produces three errors that look exactly like release defects: `PRIMARY_FILE_IDENTITY`,
`SKILL_MISSING:glow-hde-pr-development`, `SKILL_MISSING:glow-merged-change-attribution-lock`.

**Evidence:** `validate_gcfpe_20260914.py:2550` and `validate_gcfpe_current.py:645` both resolve
sibling skills from the parent of the change-flow directory — `skills_root = change_skill_dir.parent`
— and then call `find_skill(skills_root, "glow-hde-pr-development")`,
`find_skill(skills_root, "flowmaster-primary")` and the attribution lock. Copying the entire synced
skills root (27 skills) makes all three errors vanish, while both freeze digests still reproduce
exactly — so the tree under audit is unchanged and only its neighbours were missing.

**Smallest correction:** in the procedure, say *a scratch copy of the entire synced skills
directory*. One word.

**Stops the flow?** No. It offends the record, and it will cost the next auditor a diagnosis.

### W2 — the assertion count in the tasking does not match the registry

**Control:** §4 step 3 of the post-flight prompt.

**Defect:** it says *"These are the 721 assertions the consolidated pass ran; they are per-row and
need only that one body."* The registry at `907e565eabe10bfe…` carries **831**, not 721.

**Evidence:** counted from `audit_assertions` across all 55 rows of
`docs/prompt_ecosystem_management/project-prompt-contract-registry.md`: 114 `required_literals` +
0 `forbidden_literals` + 167 `required_regex` + 550 `forbidden_regex` = 831. Neither 831 nor the
`required_literals + forbidden_regex` subtotal (664) is 721.

**Smallest correction:** restate the number from the registry, or drop it — the count is derivable
and pinning it in prose creates a second place to go stale. This pass ran all 831 and all passed,
so nothing is uncovered either way.

**Stops the flow?** No. It offends the record.

### W3 — `fixture_suite_ok: true` is not qualified by two families that evaluated zero cases

**Control:** `flowmaster-validate/scripts/run_gcfpe_20260914_fixtures.py`.

**Defect:** run without bodies — which is exactly how §3g runs it — the report says
`fixture_suite_ok: true` and `case_count: 155` alongside `qa_closure_source_case_count: 0` and
`artifact_timing_case_count: 0`. A reader taking the suite flag at face value would take both
families as covered. This is the hazard §4 names one level down — *"A run that validated nothing
returns ok true and is not a pass"* — reappearing at the suite flag.

**Evidence:** `run_gcfpe_20260914_fixtures.py:542` initialises `source_case_count = 0` and raises it
to 9 only inside the branch guarded by `if bodies and all(pid in bodies for pid in qa_trio)`; line
658 reads `timing_cases = run_artifact_timing_cases(bodies, source) if bodies else []`. The suite
flag is computed as `not profile_errors and all(case["passed"] for case in cases)` — vacuously true
over the cases that did not exist.

**Smallest correction:** have the runner name its empty families in its own top-level output, for
instance a `families_not_evaluated` list mirroring `prompt_body_checks_not_evaluated`. The
instrument already carries the right idea one layer down; it is not surfaced at the suite level.

**Stops the flow?** No. It offends the record — and in this pass the gap was closed rather than
assumed: both families were run against live bodies and both passed, as recorded above.

## §5 — the change-detection baseline

All 55 `page_last_edited_at` values, as returned by the Notion fetch. Page metadata, not content.

| # | prompt | lane | `page_last_edited_at` |
|---:|---|---|---|
| 1 | `CF-C-10` | CF-C | `2026-09-18T03:05:53.656Z` |
| 2 | `CF-C-20` | CF-C | `2026-09-18T03:06:03.404Z` |
| 3 | `CF-C-30` | CF-C | `2026-09-18T03:06:15.793Z` |
| 4 | `CF-C-40` | CF-C | `2026-09-18T03:06:22.627Z` |
| 5 | `CF-E-10` | CF-E | `2026-09-18T03:06:08.080Z` |
| 6 | `CF-E-20` | CF-E | `2026-09-18T03:06:01.447Z` |
| 7 | `CF-E-30` | CF-E | `2026-09-18T03:06:23.721Z` |
| 8 | `CF-E-40` | CF-E | `2026-09-18T03:06:06.095Z` |
| 9 | `CF-PO-10` | CF-PO | `2026-09-18T03:06:10.597Z` |
| 10 | `IA-10` | IA | `2026-09-18T12:09:09.005Z` |
| 11 | `IA-20` | IA | `2026-09-18T14:44:19.150Z` |
| 12 | `IA-30` | IA | `2026-09-19T01:30:12.392Z` |
| 13 | `IA-40` | IA | `2026-09-18T12:04:25.571Z` |
| 14 | `IA-50` | IA | `2026-09-18T14:46:09.666Z` |
| 15 | `IA-60` | IA | `2026-09-18T14:27:28.534Z` |
| 16 | `PR-10` | PR | `2026-09-18T12:10:49.095Z` |
| 17 | `PR-20` | PR | `2026-09-18T12:09:30.980Z` |
| 18 | `PR-30` | PR | `2026-09-19T01:30:19.437Z` |
| 19 | `PR-35` | PR | `2026-09-19T01:30:21.248Z` |
| 20 | `PR-40` | PR | `2026-09-18T12:10:12.747Z` |
| 21 | `PR-50` | PR | `2026-09-18T12:10:36.583Z` |
| 22 | `RS-10` | RS | `2026-09-18T12:11:17.483Z` |
| 23 | `RS-20` | RS | `2026-09-19T01:30:09.239Z` |
| 24 | `RS-30` | RS | `2026-09-18T12:12:04.048Z` |
| 25 | `RS-40` | RS | `2026-09-19T01:30:13.976Z` |
| 26 | `QA-10` | QA | `2026-09-18T15:38:47.263Z` |
| 27 | `QA-20` | QA | `2026-09-18T12:11:02.004Z` |
| 28 | `QA-50` | QA | `2026-09-18T12:10:26.736Z` |
| 29 | `QA-60` | QA | `2026-09-18T12:11:24.126Z` |
| 30 | `QA-70` | QA | `2026-09-19T01:30:10.709Z` |
| 31 | `QA-80` | QA | `2026-09-18T12:04:56.327Z` |
| 32 | `QA-90` | QA | `2026-09-18T12:10:48.444Z` |
| 33 | `QA-100` | QA | `2026-09-19T01:30:18.092Z` |
| 34 | `QA-110` | QA | `2026-09-18T12:11:29.318Z` |
| 35 | `QA-120` | QA | `2026-09-18T12:04:41.951Z` |
| 36 | `ESC-10` | ESC | `2026-09-19T01:29:52.204Z` |
| 37 | `ESC-25` | ESC | `2026-09-19T01:29:55.707Z` |
| 38 | `ESC-30` | ESC | `2026-09-19T01:29:57.603Z` |
| 39 | `ESC-40` | ESC | `2026-09-19T01:29:59.689Z` |
| 40 | `OPS-10` | OPS | `2026-09-18T12:11:39.435Z` |
| 41 | `OPS-20` | OPS | `2026-09-18T15:42:44.524Z` |
| 42 | `OPS-30` | OPS | `2026-09-18T12:09:11.981Z` |
| 43 | `DOC-10` | DOC | `2026-09-19T01:29:49.085Z` |
| 44 | `DOC-20` | DOC | `2026-09-19T01:29:51.124Z` |
| 45 | `CL-20` | CL | `2026-09-19T01:29:25.162Z` |
| 46 | `CL-30` | CL | `2026-09-19T01:29:27.005Z` |
| 47 | `CL-40` | CL | `2026-09-19T01:29:36.843Z` |
| 48 | `CL-C-10` | CL-C | `2026-09-19T01:29:29.008Z` |
| 49 | `CL-E-10` | CL-E | `2026-09-19T01:29:30.748Z` |
| 50 | `CL-E-20` | CL-E | `2026-09-19T01:29:38.283Z` |
| 51 | `CL-E-30` | CL-E | `2026-09-19T01:29:39.729Z` |
| 52 | `CL-E-40` | CL-E | `2026-09-19T01:29:47.888Z` |
| 53 | `MGR-10` | MGR | `2026-09-18T03:07:05.332Z` |
| 54 | `UTIL-10` | UTIL | `2026-09-18T12:03:57.553Z` |
| 55 | `GCFPE-MGMT-10` | GCFPE-MGMT | `2026-09-18T03:06:36.425Z` |

### Was any page edited after 2026-09-19?

**No.** The most recent edit in the set is `PR-35` at `2026-09-19T01:30:21.248Z`. Nothing is later.

**21 of the 55 were edited on 2026-09-19**, all inside 56 seconds, between `01:29:25.162Z` and
`01:30:21.248Z`: `CL-20`, `CL-30`, `CL-40`, `CL-C-10`, `CL-E-10`, `CL-E-20`, `CL-E-30`, `CL-E-40`,
`DOC-10`, `DOC-20`, `ESC-10`, `ESC-25`, `ESC-30`, `ESC-40`, `IA-30`, `PR-30`, `PR-35`, `QA-70`,
`QA-100`, `RS-20`, `RS-40`. The other 34 were edited on 2026-09-18.

**That is the gap this pass closes.** The consolidated pass ran its assertions on 2026-09-18, so it
provably covered 34 of the 55 pages in their current state and did not cover the other 21. All 21
have now been read and checked in their current state, and all 21 pass. Every timestamp above was
re-confirmed unchanged when those pages were read a second time for the fixture-family runs.

## Method, stated plainly

Under the **Prompt Corpus Storage and Fidelity Policy**
(`docs/prompt_ecosystem_management/prompt-corpus-policy.md`), which governs how this audit was
conducted and not only what it concluded:

- No prompt body was written to disk, individually or in bulk, temporarily or otherwise.
- Nothing was exported, mirrored, snapshotted or cached. No corpus exists anywhere as a result of
  this pass.
- No body was hashed or compared byte-for-byte against anything.
- This report contains no body content and no body digest.
- No complete local corpus was required or assembled. Bodies were held in memory, one lane at a
  time, and discarded.

**No procedural conflict arose.** §4's prescribed method and
`docs/prompt_ecosystem_management/prompt-validation-procedure.md` are the same procedure, and
neither conflicts with §2. The §2 stop condition — *"If a procedure you are told to follow
conflicts with this, the procedure is defective — report it and stop"* — was not triggered.

Three method notes, for the record:

1. **The prompt was run at v1.1.** The copy supplied to this session was v1.0; `origin/main` carries
   v1.1, whose amendment repoints `freeze.py`, the corpus policy and the post-flight procedure at
   their repository homes. `docs/prompt_ecosystem_management/freeze.py` is byte-identical to the
   round-23 file the v1.0 text named, so the digest recipe used is the one both versions specify.
   The amendment's own words — *"no finding or verdict is affected"* — hold.
2. **Where a page's body was read twice, it was streamed from this session's own Notion reads
   rather than re-fetched into context.** The fixture-family runs needed 18 and 3 bodies
   respectively, and every one had already been read from Notion in the body pass. Streaming them
   keeps the corpus out of the auditor's context entirely, which serves §4's *"so no single context
   holds the corpus"* better than re-reading would. `page_last_edited_at` was re-confirmed identical
   for all 21 in the process. The harness's own oversized-result files that this required were
   deleted immediately after the run, per the policy's accumulation clause.
3. **The largest set held in one process was 18 of 55**, for the artifact-timing family, which
   cannot run on fewer. That is not a corpus, it was never on disk, and it is gone.

### Checks that ran, and checks that did not

**Ran, and passed:** §1 identity reproduction (8 identities plus 4 repository controls); §3a–§3h;
the five installed gates; the 55-body validator pass; 831 registry assertions; the three-body QA
closure check; 9 QA-closure falsification cases; 17 artifact-timing cases.

**Did not run, and why:**

- **A live re-read of the 54 selected-release Notion pages.** Not asked for — §3 is explicitly a
  repository-and-skills check — and out of scope besides. §3h is proven at contract and repository
  scope only, and this report does not claim more.
- **Everything §6 strikes:** manual-drain handshake (retired by `D6`), Drive artifact routing
  (retired by `D7`), required/optional input classification (unfalsifiable, dispositioned
  2026-09-21), byte-for-byte body identity (prohibited). Their absence is not reported as a finding.
- **Nothing else was skipped.** Where a check could only be run at a narrower scope, the scope is
  named above rather than inferred.

## Standing

Read-only throughout. Nothing was repaired, no prompt body was edited in Notion, `docs/pfcanon/`
was not written, no skill was installed, packaged or modified, the synced skills directory was not
written to, nothing was merged and no auto-merge was enabled, nothing was promoted, archived,
drained or resumed. This report is a new dated record; no existing dated record was corrected in
place (`AUTH-001`).

The three warnings return to the owners of `postflight-procedure.md`, of the round-27 post-flight
prompt, and of `flowmaster-validate`. None is mandatory, and none blocks a promotion decision
packet.

**DECISION NEEDED** — the promotion of `GCFPE-20260914.1 / 091426.1 / 55` is a Product Owner
decision, and this post-flight permits the packet to be prepared. It does not promote anything.
