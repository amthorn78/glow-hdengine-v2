---
artifact_type: GCFPE_WORKFLOW_SKILL_FIT_REVIEW
artifact_version: "2.0"
created_date: 2026-09-20
release: GCFPE-20260914.1 / 091426.1 / 55
review_run: 10
reviewer: PE34 coordinating; isolated question agents under §7 verification isolation
verdict: SKILL_REPAIR_REQUIRED
findings: 3
corpus_findings: 2
finding_ids: [SF10-03, SF10-04, SF10-05, SF10-06, SF10-07]
carried_forward: [SF10-02, prompt_bodies_validated, SF-05]
frozen_snapshot_sha256: c321be051b90c346a24d26524e132e7b90732953c3cc289e3def511e5fcfbaeb
frozen_snapshot_files: 321
gate: post-flight remains blocked until this returns SKILL_FIT_CONFIRMED
supersedes: none — runs 7, 8 and 9 are dated records and are not edited; run 9 is recorded only on the Notion Round Tracking page
---

# GCFPE Workflow Skill-Fit Review — run 10

The tenth §10 run. Run against a frozen installed snapshot on 2026-09-20, after the D8
derivation guard (v11) cleared independent review and was installed. The nine previous runs
returned `SKILL_REPAIR_REQUIRED`. Their records are the round-7 artifact at
`gcfpe.workflow-skill-fit-review.md`, the round-8 artifact at
`gcfpe.workflow-skill-fit-review-round8.md`, and — for run 9 — the Notion page **GCFPE
Workflow Skill Repair — Round Tracking — 091426.1**, which has no repository counterpart. All
are dated records and none is modified.

## Verdict

`SKILL_REPAIR_REQUIRED`. Three skill findings, two corpus findings, one observation.

**This is the first run in which the D8/D15 guard is not among the findings.** v11 was
attacked independently and returned `GUARD_HOLDS`; it is installed and was exercised here. The
Round Tracking page records that the nine previous runs all judged a tree carrying a defeated
guard — round 8 as its Finding 1, "the D8/D15 guard (v5) is defeated", and run 9 as "the guard
defeated a sixth time". What blocks run 10 is a different class of defect: one check inside
`flowmaster-validate` that cannot read the rendering its own corpus uses, and two obsolete
bindings inside the installed skills.

The selected release `GCFPE-20260913.1 / 091326.2 / 54` was not touched. No skill was
installed, edited, or written during this run.

## Snapshot control

The tree was measured at the start of the review and again after the last tool run:

| | first measurement | closing measurement |
|---|---|---|
| files | 321 | 321 |
| digest excluding `manifest.json` | `c321be051b90c346a24d26524e132e7b90732953c3cc289e3def511e5fcfbaeb` | identical |
| `manifest.json` sha256 | `91dd6f62a5db3944d06a2672488583ba418019c25363517ab20a4a098b9bc468` | identical |
| `manifest.json` `lastUpdated` | `1789927024241` | identical |
| `*.pyc` | 0 | 0 |

**The whole tree is byte-identical across the review, `manifest.json` included.** Nothing moved
at all, so the qualification below is a statement about the baseline's portability, not about
this run.

The headline digest is reported with `manifest.json` excluded because that file carries
`lastUpdated`, a per-container sync epoch. It was directly observed moving earlier in this
session while every skill file stayed identical, which is why a manifest-inclusive digest is
not a portable baseline across containers. It did not move during this review.

The two most recent skill `updatedAt` values in the manifest are `flowmaster-validate`
17:53:52Z and `change-flow` 17:54:04Z — the v11 installation. No skill's `updatedAt` is later
than 17:54:04Z, and the review's first measurement was taken at 19:12Z. `SF-07` — the round-7
defect in which the snapshot moved mid-review — does not recur.

Every tool was run from a scratch copy of the whole tree with `PYTHONDONTWRITEBYTECODE=1`.
The installed directory was never written to. Zero `.pyc` files were produced.

### What was executed

The installed `flowmaster-validate` validator was run against the 55-body corpus:

- validator: `flowmaster-validate/scripts/validate_gcfpe_20260914.py`, sha256
  `535a3b161ef0996249540b46607b855c8d17d841fdd24ce3b615f97e6199bc2e`
- the `change-flow` copy of the same file: sha256
  `660d61fe619c9dd9aa2b5646a7344084af3c8c333fc044e2e91f51e941363c63`
- contract: `change-flow/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json`,
  sha256 `7f8d683e672dd4b14766fc2ec9c8ca7e5a964a11e4ddc4dea3fa4f8d7c9b5894`,
  status `UNSELECTED_CANDIDATE`, 55 members
- frozen graph resolved: sha256 `1d0b72582df4735b3d22dd325687b0375a624bd9ab5760c9589171049cd715a7`,
  **55 nodes, 227 edges**
- bodies supplied: 55; `prompt_body_count: 55`

Result: `ok: false`, **12 error strings across exactly three check families**. No
`SKILL_MISSING`, no `BUNDLED_CONTRACT_UNREADABLE`, no `PROFILE_UNREADABLE`, no
`ROUTE_GRAPH`, no `PF10_*` error of any kind.

A first attempt at this measurement pointed the validator at the `SELECTED_PRODUCTION`
contract (54 members) from a partial tree copy and returned 138 errors including
`PROFILE_UNREADABLE`, `BUNDLED_GRAPH_UNREADABLE` and `SKILL_MISSING`. That run is a harness
failure, not a result, and is **not** credited anywhere in this review. It is recorded here
because a broken harness that still exits with a plausible-looking error list is the exact
failure the round-18 bench was rebuilt to prevent.

The D8 guard block is byte-identical across both installed validator copies: the four
contiguous functions `_addendum_paths`, `_ambiguous_addendum_keys`,
`pf10_addendum_contract_key_drift` and `addendum_list_value_drift`, 7355 characters,
md5 `46c69eaf8f00672e44f8502bbf43c721`.

## §A — Prompt-to-skill matrix

### A.0 How relationships are classified

The scan scope is **every skill installed in the frozen tree** — all 27 names in
`manifest.json`, plus every skill directory name — matched against all 55 bodies. That is an
exhaustive scan, not a chosen shortlist, so a `NONE` row cannot be an artefact of a scope that
omitted the skill in question.

**Exactly two installed skills are named by any prompt body:** `glow-hde-pr-development` in 22
prompts and `glow-merged-change-attribution-lock` in 17. No prompt body contains the name of
`change-flow`, `flowmaster-validate`, `flowmaster-primary`, `flowmaster-propagate`,
`amthor-workspace-governance-audit`, `tw-flowmaster`, `session-relay-flowmaster`,
`session-branch-flowmaster`, `skill-creator`, or any other installed skill.

- `PRIMARY` — the prompt binds the skill as the authority for its own execution.
- `SUPPORT` — the prompt binds the skill for a bounded capability without transferring authority.
- `PROHIBITED` — the prompt names the skill in order to exclude it from its own execution.
- `NONE` — the prompt binds no skill for its own execution. A prompt that names a skill only
  to restate the PR-lane authority as a contract fact is `NONE`, consistent with round 7.
  Naming an **actor** ("the authorized DevOps or target-environment operator") is not naming
  a skill.

A row reading "names no installed skill" means the exhaustive scan found none of the 27 names
in that body. It does not mean no skill acts on that prompt. Round 7's six uniform
relationships —
`flowmaster-validate` and `amthor-workspace-governance-audit` as `VALIDATOR` over the whole
corpus, `skill-creator` as `EDITING_TOOL`, `flowmaster-primary` and `flowmaster-propagate` as
`NONE` at prompt level, and `change-flow` as `PRIMARY` at flow level and `NONE` at prompt
level — are stated once there and are unchanged. This matrix records the per-prompt axis only,
so a prompt that does not name `flowmaster-validate` is `NONE` here and `VALIDATOR` there;
those are the same fact on two axes, not a contradiction.

55 prompts yield 58 relationship rows: 51 `NONE`, 3 `PRIMARY`, 1 `SUPPORT`, 3 `PROHIBITED`.
Four prompts carry a binding: PR-30, PR-35, PR-40, RS-40. The matrix was generated
mechanically from the 55 verified bodies; every basis quote in §B was matched byte-for-byte
against the file and line it names before acceptance.

**18 prompts** restate the PR-lane authority as a contract fact without binding a skill for
their own run: CL-20, CL-30, CL-40, CL-C-10, CL-E-10, CL-E-20, CL-E-30, CL-E-40, DOC-10,
DOC-20, ESC-10, ESC-25, ESC-30, ESC-40, QA-20, QA-60, QA-70, QA-100. Round 7 recorded
seventeen. The difference is one row, QA-60, whose line 17 preserves
"`glow-hde-pr-development` authority" as part of the PR work-unit invariant rather than naming
it as the sole primary skill. Round 7 is a dated record and is not edited; this run counts 18
by measurement and states the boundary case rather than reconciling the two counts silently.

### A.1 The 55 rows

| # | Prompt | Skill named | Relationship | Basis |
|---|---|---|---|---|
| 1 | CF-C-10 | — | `NONE` | names no installed skill |
| 2 | CF-C-20 | — | `NONE` | names no installed skill |
| 3 | CF-C-30 | — | `NONE` | names no installed skill |
| 4 | CF-C-40 | — | `NONE` | names no installed skill |
| 5 | CF-E-10 | — | `NONE` | names no installed skill |
| 6 | CF-E-20 | — | `NONE` | names no installed skill |
| 7 | CF-E-30 | — | `NONE` | names no installed skill |
| 8 | CF-E-40 | — | `NONE` | names no installed skill |
| 9 | CF-PO-10 | — | `NONE` | names no installed skill |
| 10 | CL-20 | `glow-hde-pr-development`, `glow-merged-change-attribution-lock` | `NONE` | `CL-20.md:34` — restates the PR-lane authority as a contract fact; binds no skill for its own execution |
| 11 | CL-30 | `glow-hde-pr-development`, `glow-merged-change-attribution-lock` | `NONE` | `CL-30.md:31` — restates the PR-lane authority as a contract fact; binds no skill for its own execution |
| 12 | CL-40 | `glow-hde-pr-development`, `glow-merged-change-attribution-lock` | `NONE` | `CL-40.md:20` — restates the PR-lane authority as a contract fact; binds no skill for its own execution |
| 13 | CL-C-10 | `glow-hde-pr-development`, `glow-merged-change-attribution-lock` | `NONE` | `CL-C-10.md:38` — restates the PR-lane authority as a contract fact; binds no skill for its own execution |
| 14 | CL-E-10 | `glow-hde-pr-development`, `glow-merged-change-attribution-lock` | `NONE` | `CL-E-10.md:37` — restates the PR-lane authority as a contract fact; binds no skill for its own execution |
| 15 | CL-E-20 | `glow-hde-pr-development`, `glow-merged-change-attribution-lock` | `NONE` | `CL-E-20.md:22` — restates the PR-lane authority as a contract fact; binds no skill for its own execution |
| 16 | CL-E-30 | `glow-hde-pr-development`, `glow-merged-change-attribution-lock` | `NONE` | `CL-E-30.md:22` — restates the PR-lane authority as a contract fact; binds no skill for its own execution |
| 17 | CL-E-40 | `glow-hde-pr-development`, `glow-merged-change-attribution-lock` | `NONE` | `CL-E-40.md:23` — restates the PR-lane authority as a contract fact; binds no skill for its own execution |
| 18 | DOC-10 | `glow-hde-pr-development`, `glow-merged-change-attribution-lock` | `NONE` | `DOC-10.md:24` — restates the PR-lane authority as a contract fact; binds no skill for its own execution |
| 19 | DOC-20 | `glow-hde-pr-development`, `glow-merged-change-attribution-lock` | `NONE` | `DOC-20.md:24` — restates the PR-lane authority as a contract fact; binds no skill for its own execution |
| 20 | ESC-10 | `glow-hde-pr-development`, `glow-merged-change-attribution-lock` | `NONE` | `ESC-10.md:23` — restates the PR-lane authority as a contract fact; binds no skill for its own execution |
| 21 | ESC-25 | `glow-hde-pr-development`, `glow-merged-change-attribution-lock` | `NONE` | `ESC-25.md:22` — restates the PR-lane authority as a contract fact; binds no skill for its own execution |
| 22 | ESC-30 | `glow-hde-pr-development`, `glow-merged-change-attribution-lock` | `NONE` | `ESC-30.md:22` — restates the PR-lane authority as a contract fact; binds no skill for its own execution |
| 23 | ESC-40 | `glow-hde-pr-development`, `glow-merged-change-attribution-lock` | `NONE` | `ESC-40.md:22` — restates the PR-lane authority as a contract fact; binds no skill for its own execution |
| 24 | GCFPE-MGMT-10 | — | `NONE` | names no installed skill |
| 25 | IA-10 | — | `NONE` | names no installed skill |
| 26 | IA-20 | — | `NONE` | names no installed skill |
| 27 | IA-30 | — | `NONE` | names no installed skill |
| 28 | IA-40 | — | `NONE` | names no installed skill |
| 29 | IA-50 | — | `NONE` | names no installed skill |
| 30 | IA-60 | — | `NONE` | names no installed skill |
| 31 | MGR-10 | — | `NONE` | names no installed skill |
| 32 | OPS-10 | — | `NONE` | names no installed skill |
| 33 | OPS-20 | — | `NONE` | names no installed skill |
| 34 | OPS-30 | — | `NONE` | names no installed skill |
| 35 | PR-10 | — | `NONE` | names no installed skill |
| 36 | PR-20 | — | `NONE` | names no installed skill |
| 37 | **PR-30** | `glow-hde-pr-development` | **PRIMARY** | `PR-30.md:59` — Use `glow-hde-pr-development` as the sole primary skill for this PR-30 phase. |
| 37 | **PR-30** | `glow-merged-change-attribution-lock` | **PROHIBITED** | `PR-30.md:59` — `glow-merged-change-attribution-lock` is read-only and post-merge and is not used by PR-30. |
| 38 | **PR-35** | `glow-hde-pr-development` | **PRIMARY** | `PR-35.md:10` — Use `glow-hde-pr-development` as the sole primary skill. |
| 38 | **PR-35** | `glow-merged-change-attribution-lock` | **PROHIBITED** | `PR-35.md:10` — Do not use `glow-merged-change-attribution-lock` here; that skill is read-only post-merge evidence for PR-40. |
| 39 | **PR-40** | `glow-merged-change-attribution-lock` | **SUPPORT** | `PR-40.md:63` — the read-only, post-merge skill for resolving landed attribution during this review |
| 39 | **PR-40** | `glow-hde-pr-development` | **PROHIBITED** | `PR-40.md:63` — is not used to mutate the repository in PR-40 |
| 40 | PR-50 | — | `NONE` | names no installed skill |
| 41 | QA-10 | — | `NONE` | names no installed skill |
| 42 | QA-100 | `glow-hde-pr-development` | `NONE` | `QA-100.md:16` — restates the PR-lane authority as a contract fact; binds no skill for its own execution |
| 43 | QA-110 | — | `NONE` | names no installed skill |
| 44 | QA-120 | — | `NONE` | names no installed skill |
| 45 | QA-20 | `glow-hde-pr-development` | `NONE` | `QA-20.md:18` — restates the PR-lane authority as a contract fact; binds no skill for its own execution |
| 46 | QA-50 | — | `NONE` | names no installed skill |
| 47 | QA-60 | `glow-hde-pr-development` | `NONE` | `QA-60.md:17` — restates the PR-lane authority as a contract fact; binds no skill for its own execution |
| 48 | QA-70 | `glow-hde-pr-development` | `NONE` | `QA-70.md:24` — restates the PR-lane authority as a contract fact; binds no skill for its own execution |
| 49 | QA-80 | — | `NONE` | names no installed skill |
| 50 | QA-90 | — | `NONE` | names no installed skill |
| 51 | RS-10 | — | `NONE` | names no installed skill |
| 52 | RS-20 | — | `NONE` | names no installed skill |
| 53 | RS-30 | — | `NONE` | names no installed skill |
| 54 | **RS-40** | `glow-hde-pr-development` | **PRIMARY** | `RS-40.md:10` — Use `glow-hde-pr-development` as the sole primary skill. |
| 55 | UTIL-10 | — | `NONE` | names no installed skill |

## §B — The ten questions

| # | Question | Answer |
|---|---|---|
| 1 | Does every prompt that needs a primary skill have exactly one appropriate primary skill? | **YES** |
| 2 | Are support skills prevented from assuming workflow authority? | **YES** |
| 3 | Does `glow-hde-pr-development` fully and narrowly own PR-30, PR-35, interrupted PR recovery, and eligible RS-40 continuation? | **YES** |
| 4 | Is a support skill limited to specific environment, Railway, vendor, database, deployment or bounded Ops capabilities, with no PR-lane authority? | **NO_SUBJECT** |
| 5 | Is `glow-merged-change-attribution-lock` limited to optional read-only landed-attribution support for PR-40? | **YES** |
| 6 | Does `change-flow` orchestrate the selected workflow without performing repository implementation? | **YES** |
| 7 | Do `flowmaster-validate` and `amthor-workspace-governance-audit` validate rather than author, approve, promote, or execute runtime work? | **YES** |
| 8 | Do any prompt contracts require a capability that no installed skill safely supplies? | **NO** |
| 9 | Do any installed skills overlap, contradict, overreach, or carry obsolete prompt/version bindings? | **YES — two obsolete bindings** |
| 10 | Is a new specialized skill actually required, or can the existing specialized PR-development skill be corrected without duplicating authority? | **NO new skill required** |

### 1 — exactly one appropriate primary skill: YES

Three prompts bind a primary, all the same one. PR-30 line 59: "Use
`glow-hde-pr-development` as the sole primary skill for this PR-30 phase." PR-35 line 10 and
RS-40's continuation carry the identical sentence. No prompt binds two primaries, and no
prompt that executes PR work leaves the primary unnamed. The 51 `NONE` prompts do not need a
primary: they are authored, reviewed, planned, QA'd or operated natively by their named human
or agent role. The decision record states the general case at line 824 — "primary skill has
exactly one, and no prompt contract requires a capability no installed skill" — and at line
825 gives the worked example: "safely supplies — are answered: OPS-20 needs no primary skill."

### 2 — support skills cannot assume workflow authority: YES

Stated per-prompt and per-skill. CL-E-20 line 22: "`glow-hde-pr-development` is the sole
primary skill authority. A support skill is used only for a specifically required
environment, Railway, vendor, database, deployment, or Ops capability.
`glow-merged-change-attribution-lock` is read-only post-merge evidence for PR-40 only."
PR-30 line 59 adds that a support skill "is support-only and supplies no PR-workflow
authority". The skill agrees from its own side:
`glow-merged-change-attribution-lock` SKILL.md line 128 — "This skill supplements, but never
replaces, native PR-review evidence and guards. It does not create a prompt field, runtime
requirement, or prompt-local skill dependency."

### 3 — `glow-hde-pr-development` owns its four phases fully and narrowly: YES

Its own trigger, SKILL.md line 3: "Execute one Product Owner-proceeded Glow HDE PR work unit
in its single dedicated development session across GCFPE PR-30 implementation/publication,
PR-35 review correction/merge readiness, interrupted recovery, and eligible RS-40
continuation". Narrowness is stated in the same line — "Do not use for PR planning, Product
Owner merge, PR-40 lineage review, QA execution, standalone Ops or deployment work outside a
PR work unit, or Change Flow orchestration" — and again at line 171. Continuity across the
phase boundary is pinned at line 55 as an exact ordered ten-field list in which "PR-30 and
PR-35 share exactly one value for each field; the phase boundary may not duplicate, replace,
omit, or transfer any field." RS-40 line 10 carries the matching corpus-side statement.

### 4 — support-skill limits: NO_SUBJECT

The question's subject was `glow-hde-devops`. **D16** removes it. Decision record line 805:
"## D16 — No DevOps skill exists, and the Ops lane needs none"; line 811: "**The ruling: 'we
do not need any devops skill period.'**"; line 813: "`glow-hde-devops` is retired. None is
installed, none is required, and none is to be created." Line 822 records how the Ops lane
runs instead: "natively, by their named human or agent operator, with no skill binding".

The Ops prompts name an actor, not a skill — OPS-20 line 9: "You are the authorized DevOps or
target-environment operator for the exact bounded operation supplied in OPS_TASK_ID." That is
a role, and the round-7 reading of it is unchanged.

The question was not re-litigated. The *residue* of the retired skill inside the installed
tree is a separate matter and is finding 3 below.

### 5 — the attribution lock stays read-only and PR-40-only: YES

Four independent statements agree. PR-40 line 63: "`glow-merged-change-attribution-lock` is
the read-only, post-merge skill for resolving landed attribution during this review. It
supplies evidence only and has no implementation, correction, rescope, QA, Ops, acceptance,
merge, or closure authority." PR-35 line 10 excludes it — "Do not use
`glow-merged-change-attribution-lock` here; that skill is read-only post-merge evidence for
PR-40" — and PR-30 line 59 likewise. The skill's own trigger, SKILL.md line 3, scopes itself
to "one merged PR or an ordered merged-PR lineage as temporary, read-only evidence for an
active PR review", and line 16 refuses durability: "The bundle is temporary evidence for the
active PR-review task. It is not a durable project record, new infrastructure, or downstream
authority." Line 120 makes it optional in fact as well as in wording: "If complete transient
delivery is unavailable, omit the bundle and let the reviewer run natively."

### 6 — `change-flow` orchestrates without implementing: YES

SKILL.md line 33: "Act as the controller and evidence keeper, not as a substitute for the
worker sessions being orchestrated." Line 256 enumerates what it never substitutes for,
including "a dedicated PR session, an authorized environment operator". Line 443 (GCF-14)
keeps implementation out of the orchestrator's own hands: "Create one dedicated PR session for
one planned PR work unit. That session validates the repository and creates the per-PR
Implementation Plan. It performs no implementation before Proceed." The PR skill states the
same boundary from the other side, line 169: "Use Change Flow controls for workflow selection
and orchestration, not repository implementation."

### 7 — the two validators validate rather than act: YES

`flowmaster-validate` SKILL.md line 21: "This skill is a deterministic read-only validator. It
never repairs a skill, propagates a core, invokes Change Flow, calls live Notion workflow
components, mutates a registry, or converts a finding into an accepted deviation."
`amthor-workspace-governance-audit` SKILL.md line 18: "Remain read-only in every mode. Do not
edit, install, publish, archive, retire, move, approve, or execute anything." Line 26 keeps it
from routing around itself: "Do not invoke `skill-creator`, Flowmaster propagation, or any
manager/writer to fix findings. Recommend the correct pathway only." Its script enforces the
posture rather than asserting it — `audit_workspace_governance.py` line 733 emits
`"authorization": "NONE — PROPOSAL ONLY"` and line 741
`"required_approval": "EXACT PRODUCT OWNER APPROVAL BEFORE MUTATION"`.

**This answer is about the authority boundary, and it is YES.** Findings 1 and the two corpus
findings below are about *correctness* — whether a check reads its corpus as the corpus is
actually written. Both can be true at once: a validator can stay strictly inside its authority
and still contain a check that is wrong. Conflating the two is how a correctness defect gets
argued away as an authority question.

### 8 — a required capability no installed skill supplies: NO

No prompt contract requires one. The PR lane's capability question resolves inside the PR
skill's own authority rather than by reaching for another skill — SKILL.md line 168: "Handle a
genuinely needed environment, Railway, vendor, database, deployment, or bounded operational
capability inside this skill's own authority. Such work supports PR-30 and PR-35; it never
governs them or transfers authority to another skill." The decision record line 824 records the
general finding, and line 813 confirms that the one skill a contract might have reached for is
retired and "none is required".

### 9 — overlap, contradiction, overreach, or obsolete bindings: YES — two obsolete bindings

Findings 2 and 3. No overlap, contradiction or overreach was found: the primary/support
boundary is stated consistently on both sides in every case examined, and
`flowmaster-primary` SKILL.md line 3 explicitly yields to specialization — "Do not use in
place of an installed domain specialization such as tw-flowmaster or change-flow when that
specialization applies."

### 10 — a new specialized skill: NO

Not required. Every finding in this review is a bounded correction inside an existing
installed skill: one check function in `flowmaster-validate`, one unreachable root in
`flowmaster-propagate`, and stale bundled reference data in `change-flow`. None of them is a
capability gap, and none of them would be addressed by adding a skill. The plan's own default
stands: "Do not add one by default."

## §C — Findings

### Finding 1 — `SF10-03` — `flowmaster-validate` cannot read the rendering its own corpus uses

`QA_PASS_BODY_CLASS_MAP`. `validate_qa_closure_bodies` reads QA-120's `PASS` class map with a
Markdown-pipe regex and then compares the captured URL to the contract's `notion_url` as a
literal string:

```python
rows = re.findall(
    r"(?m)^\| `PASS` \| `(EPIC|CRD)` \| `(CL-[EC]-10) — [^`]+` at (https://[^ |]+) \|$",
    producer,
)
if len(rows) != 2 or {r[0]: r[1] for r in rows} != expected:
    errors.append("QA_PASS_BODY_CLASS_MAP")
for cls, destination, url in rows:
    if url != (contract.get("member_registry") or {}).get(expected[cls], {}).get("notion_url"):
        errors.append("QA_PASS_BODY_CLASS_MAP")
```

QA-120's body does not render that mapping as a Markdown table. It has **zero** lines
beginning with `|`. The map is an HTML table, and each destination is a page mention, not a
bare URL — line 42:

```
<td>`CL-E-10 — Perform Epic Retrospective and Decide Closure — 091426.1` at <mention-page url="https://app.notion.com/p/3db4590a05eb811a8578d75885c16cac"/></td>
```

So the regex matches nothing, `len(rows) != 2`, and the check fails. It would still fail if the
table were converted to pipes, because the second half compares against
`https://app.notion.com/p/3db4590a05eb811a8578d75885c16cac?pvs=204` while the mention's `url`
attribute carries no query.

**This is the same defect round 8 recorded as `SF10-01`, at a second site, unfixed.** The fix
exists in the same file. `notion_page_identity` was added for exactly this, and its docstring
names the problem:

> A prompt body renders its own binding as a page mention, and the mention's `url` attribute
> never carries the `?pvs=204` query that the contract's `notion_url` does. An earlier version
> compared the whole header line as a literal, so the check failed on all 55 members at once
> -- information about the check, not the bodies. Identity is the page id; the rendering and
> the query string are not identity.

That reasoning was applied to the identity-header check, which now passes 55 of 55, and was not
carried to `validate_qa_closure_bodies`. One conversion was made where two were needed.

**Proposed bounded repair:** in `validate_qa_closure_bodies`, accept both renderings of the
class-map row and compare destinations with `notion_page_identity` instead of string equality.
No new check, no relaxed predicate: the same two rows, the same two destinations, the same two
pages, read through the normalizer the file already defines.

### Finding 2 — `SF10-04` — `flowmaster-propagate` cannot run by either route

Its default root does not exist and the fallback is unavailable. `scripts/propagate_core.py`
line 28:

```python
DEFAULT_ROOT = Path("/mnt/skills/user")  # Claude port: see flowmaster-validate for the same change
```

`/mnt/skills/user` is absent in this environment. The alternative route is a git checkout, and
the installed skills root is not one — `git rev-parse --show-toplevel` from the tree root
returns `fatal: not a git repository (or any of the parent directories): .git`, which reaches
line 151:

```python
raise PropagationError("skills root is not inside a readable git checkout")
```

The skill is therefore unrunnable as installed, by either route. It is not on the promotion
path, so this does not block §11 by itself; it is an obsolete binding to an environment that no
longer exists, and it is why question 9 answers YES.

**Proposed bounded repair:** none proposed inside this review. Propagation is a build-time
maintenance operation — SKILL.md line 8: "This is a build-time maintenance operation, not
runtime skill invocation or inheritance." Whether it is repointed or retired is a Product Owner
decision about the skill-authoring pipeline, not a repair this review is authorized to specify.

### Finding 3 — `SF10-05` — `change-flow` bundles contracts that bind a retired skill and collide on identity

Two distinct problems in `change-flow/references/`.

**(a) A retired skill is still bound.** Three bundled contracts bind `glow-hde-devops` as a
support skill at revision 1.5.0, which D16 retires:

| file | line | status |
|---|---|---|
| `gcfpe-20260913.1-091326.2-direct-handoff-contract.json` | 180 | `CANDIDATE_VALIDATED` |
| `gcfpe-20260913.1-direct-handoff-contract.json` | 167 | `CANDIDATE_VALIDATED` |
| `gcfpe-20260912.2-direct-handoff-contract.json` | 87 | `CANDIDATE_UNTIL_SELECTED_IN_NOTION_REGISTER` |

Each carries `"support_skill": "glow-hde-devops"` with `"support_only": true` and
`"support_skill_revision": "1.5.0"`.

**The live `SELECTED_PRODUCTION` contract does not.** `gcfpe-current-direct-handoff-contract.json`
contains no occurrence of `glow-hde-devops`; its `pr_development_contract` names only
`"primary_skill": "glow-hde-pr-development"` at revision 1.2.0. That correction was made in the
production copy and not in the candidate copies.

**(b) Three files share one `contract_id` and disagree.** `GCFPE-PF10-INTEGRITY-20260913.1` is
the `contract_id` of `gcfpe-current-direct-handoff-contract.json` (`SELECTED_PRODUCTION`),
`gcfpe-20260913.1-091326.2-direct-handoff-contract.json` (`CANDIDATE_VALIDATED`), and
`gcfpe-20260913.1-direct-handoff-contract.json` (`CANDIDATE_VALIDATED`). The first two are not
byte-identical: they have the same top-level key set and differ in exactly two values —
`status`, and `pr_development_contract`, which is where the retired binding lives. So one
`contract_id` resolves to files that disagree about whether a retired skill is bound.

`change-flow` SKILL.md line 554 disclaims stale references, but only a different set of them:

> The older integrated-readiness, final-scan, Alpha-feedback, assessment-middleware,
> Epic-alpha, and Epic-reengineering reference files remain immutable historical provenance.
> They are not executed as current routing overlays.

The direct-handoff contracts above are not in that list and carry no equivalent disclaimer.

**Proposed bounded repair:** disclaim the superseded direct-handoff contracts in the same terms
SKILL.md line 554 already uses for the correction files, so `contract_id` resolution has one
current answer. Do **not** edit the contract bytes: under `AUTH-001` these are dated records,
and the selected release is never touched. The fix is the authority relationship, not the
easier-to-edit fact.

## §C.2 — Corpus findings (not skill repairs)

These two surfaced from the same validator run. Neither is a skill defect, and neither is
repaired by changing a skill. Both are recorded because §11 must validate all 55 bodies and
both would fail it.

### C1 — `SF10-06` — GCFPE-MGMT-10 is the one body missing a token its own state routes require

`PROMPT_HANDOFF_CONTRACT:GCFPE-MGMT-10`. When a prompt has any public result state that is not
terminal for the invocation, the check requires the literal `NEXT_PROMPT_HANDOFF` in its body.
**54 of 55 prompts have such a state; 53 of those 54 bodies carry the literal.** GCFPE-MGMT-10
is the only one that does not. PR-50 is the one prompt whose public states are all terminal; it
is not required to carry it and does not.

GCFPE-MGMT-10 has two non-terminal public states — `ECOSYSTEM_CHANGE_COMPLETE` and
`READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION`, both `next_prompt_handoff_count: 1` — and
its body carries the obligation in prose (line 34: "It may contain exactly one saved/read-back
manual-use handoff to **PR-10 — Create PR Work-Unit Instructions — 091426.1**") without the
token.

A check that fails on every member of a set is information about the check; a check that passes
on 53 of 54 is information about the one. This is a body gap, and the correction is a Notion
body edit in place, by the prompt's owner. It is **not** grounds for a skill change.

### C2 — `SF10-07` — four CF Specification prompts contradict the plan-writer contract they are declared under

`PROMPT_WRITER` × 10 error strings across four prompts: CF-C-20, CF-C-40, CF-E-20, CF-E-40.

The contract declares them plan writers itself. `plan_writer_contract.evaluated_prompt_ids`
lists all fourteen writers including these four, with
`"authoring_context_required": true` and `"current_pf10_markdown_required": true`. The
validator's roster matches the contract's exactly — `PLAN_WRITER_SET` did not fire.

None of the four bodies contains `AUTHORING_CONTEXT`, "active addend", or "current controlled
PF10" — zero occurrences of each, in all four. The ten writers that pass carry the obligation
explicitly; IA-10 line 26 is representative: "Before writing the Audit or Plan, resolve and
read the unique current controlled PF10 Markdown and every applicable active addendum by its
repository path."

Two of the four do not merely omit it — they assert the opposite. CF-C-20 line 12 and CF-E-20
line 12: "Initial authoring does not make PF10 a universal prerequisite." Both also state at
line 8 that the prompt "does not ... edit PF10, or create a PF10 addendum."

So the contract and the four bodies disagree about whether these prompts owe a PF10-resolution
obligation, and the validator is faithful to the contract. **This review cannot resolve that
disagreement**, and does not attempt to: it is a Specification-authoring question owned by its
prompt owners and the Product Owner. Either the four bodies acquire the obligation, or the
contract's `plan_writer_contract` roster drops them. Both are outside a skill repair.

## Verified clean

- **The D8/D15 guard.** v11 was attacked by an independent reviewer that could not see the
  repair and returned `GUARD_HOLDS`. It is installed, its guard block is byte-identical across
  both installed validator copies, and it was exercised in this run: no `PF10_ADDENDUM_*` error of any kind fired against
  the candidate contract. Recorded in `gcfpe.round19.d8-v11-cleared-and-installed.md`.
- **`SF10-01` at the identity-header site is closed.** All 55 bodies pass
  `prompt_identity_header_valid` in candidate mode — 55/55, zero `PROMPT_BODY_IDENTITY`
  errors — where round 8 measured a check that failed on all 55. Two negative controls were run
  and both returned `False`: mangling the prompt id in the header, and dropping the header
  block. The pass is therefore a property of the bodies, not of a check that cannot fail.
- **The graph closes.** 55 nodes, 227 edges, frozen graph sha256 `1d0b7258…`. No
  `ROUTE_GRAPH`, `STATE_ROUTE_MEMBER_SET`, or `UNRESOLVED_GRAPH_PREDICATES` error.
- **Required skills are present.** No `SKILL_MISSING` for `glow-hde-pr-development` or
  `glow-merged-change-attribution-lock`.
- **Eight of the ten questions answer as intended.** Question 4 has no subject under D16 and
  was not re-litigated. Question 9 answers **YES** — the answer a defect produces — and carries
  findings 2 and 3. The other eight are clean.

### `SF10-02` is carried forward, still present and still not violated

Round 9 recorded `SF10-02`: the prompt-body marker check pins a skill literal in the PR-40 body
but pins none in PR-30 or PR-35, so a body-versus-contract drift on the primary-skill binding
would go undetected. That is still true of the installed validator — its `exact_markers` table
gives `"PR-40"` the marker `"glow-merged-change-attribution-lock"` while `"PR-30"` and
`"PR-35"` get only state and phase tokens — and it is still not violated: PR-30 line 59 and
PR-35 line 10 both carry the correct sentence, verified in §A of this run. A false negative
cannot fire, so this run could not have detected it independently; it is recorded as carried,
unchanged, non-blocking.

### Observation — `prompt_bodies_validated` is a presence flag

Line 2260 of the validator:

```python
"prompt_bodies_validated": prompt_dir is not None,
```

It reports whether a prompt directory was supplied, not whether any body passed. It read `true`
in this run because a directory was supplied, and it would read `true` for an empty one. It is
not a verdict and must not be cited as one. Carried forward, unchanged, not blocking.

## What this run does not claim

No skill was installed, edited, or written. No prompt body was edited. No prompt page in Notion
was changed; the Round Tracking page records this run, as it records every round. The selected
release `GCFPE-20260913.1 / 091326.2 / 54` was not touched. This review
is not QA, not acceptance, not promotion, and not post-flight. Per §10, post-flight remains
blocked: **the three skill findings and the two corpus findings are presented to Nathan for
separate approval before any repair is attempted.**
