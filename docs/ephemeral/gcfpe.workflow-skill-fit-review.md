---
artifact_type: GCFPE_WORKFLOW_SKILL_FIT_REVIEW
artifact_version: "1.0"
created_date: 2026-09-18
release: GCFPE-20260914.1 / 091426.1 / 55
reviewer: independent session, not the prompt author, per the plan's §10
verdict: SKILL_REPAIR_REQUIRED
findings: 11
quote_verification: 57 of 57 blockquotes located verbatim in a real source file; 0 fabricated
gate: post-flight is blocked until this returns SKILL_FIT_CONFIRMED
---

# GCFPE Workflow Skill-Fit Review

Release under review: `GCFPE-20260914.1 / 091426.1 / 55`
Reviewer posture: independent, read-only. No Notion write, no repository edit, no git action was performed. Every quotation below is copied byte-for-byte from the file named beside it.

## Sources actually read

- Installed skills root: `/root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502/` — `SKILL.md` read in full for `change-flow`, `glow-hde-pr-development`, `flowmaster-validate`, `amthor-workspace-governance-audit`, `glow-merged-change-attribution-lock`, `flowmaster-primary`, `flowmaster-propagate`, `skill-creator`, plus `glow-write-boundary`; `scripts/` read for the five skills that bundle them.
- The 55 prompt bodies at `/tmp/claude-0/-home-user-glow-hdengine-v2/5eb01919-e69e-571c-a806-0cabaacca134/scratchpad/pass/current/`.
- `/home/user/glow-hdengine-v2/docs/prompt_ecosystem_management/project-prompt-contract-registry.md` (55 rows, parsed).
- `/home/user/glow-hdengine-v2/docs/prompt_ecosystem_management/gcfpe.decision-record.md` (D1–D14).
- `/tmp/claude-0/-home-user-glow-hdengine-v2/5eb01919-e69e-571c-a806-0cabaacca134/scratchpad/pass/skill-index.json` — used only as a starting index; every claim taken from it was re-verified against the bodies.

`glow-hde-devops` is **not installed**: there is no such directory in the skills root and no entry for it in `manifest.json`. Its status is established in §B, question 8.

---

## A. Prompt-to-skill matrix

### A.0 How relationships are classified

The bodies use "primary skill" to mean the skill that carries the execution authority for *that prompt's own run*. The matrix therefore records, per prompt, the skills with an operative relationship in that prompt's run. Six relationships are uniform across the whole release and are stated once here rather than repeated 55 times:

| Skill | Relationship to all 55 prompts | Basis |
|---|---|---|
| `flowmaster-validate` | `VALIDATOR` | Validates the suite and the 55-member corpus against the pinned R1 oracle; `scripts/validate_gcfpe_20260914.py` reads every prompt body. Read-only by its own terms. |
| `amthor-workspace-governance-audit` | `VALIDATOR` | Audits declared prompt/workflow contracts and skill identity, read-only by its own terms. |
| `skill-creator` | `EDITING_TOOL` | Named by no prompt; edits skills, never executes a workflow row. `amthor-workspace-governance-audit/SKILL.md` line 26 forbids using it as a repair actor. |
| `flowmaster-primary` | `NONE` at prompt level | Upstream immutable core. Its core block is embedded byte-identically in `change-flow`; it is never loaded to run a GCFPE row. |
| `flowmaster-propagate` | `NONE` | No approved Primary-core change exists (§B question 9), so it is out of scope by the review brief's own condition. |
| `change-flow` | `NONE` at prompt level; `PRIMARY` at flow level | It selects, dispatches and keeps evidence for a whole Epic/CRD run; it never executes a prompt row itself. Treating it as a second per-prompt `PRIMARY` would manufacture the duplicate-authority defect question 1 asks about. |

Seventeen prompts restate the PR-lane invariant (`glow-hde-pr-development` is the sole primary skill for PR-30/PR-35) as a *fact they must preserve about another lane*. That is a cross-reference, not an operative relationship for their own run: none of them loads the skill. Those rows are `NONE` with the reference recorded, because classifying a preserved invariant as `SUPPORT` would assert an authority the bodies deny.

### A.1 The 55 rows

| # | Prompt | Skill | Class | Evidence (exact text in the body) |
|---|---|---|---|---|
| 1 | CF-C-10 | — | `NONE` | Names no skill. |
| 2 | CF-C-20 | — | `NONE` | Names no skill. |
| 3 | CF-C-30 | — | `NONE` | Names no skill. |
| 4 | CF-C-40 | — | `NONE` | Names no skill. |
| 5 | CF-E-10 | — | `NONE` | Names no skill. |
| 6 | CF-E-20 | — | `NONE` | Names no skill. |
| 7 | CF-E-30 | — | `NONE` | Names no skill. |
| 8 | CF-E-40 | — | `NONE` | Names no skill. |
| 9 | CF-PO-10 | — | `NONE` | Names no skill. |
| 10 | CL-20 | `glow-hde-pr-development`, `glow-merged-change-attribution-lock` | `NONE` (cross-reference only) | Line 34 preserves `one primary skill authority (\`glow-hde-pr-development\`)`; line 36 restates the attribution lock as PR-40-only. CL-20 loads neither. |
| 11 | CL-30 | same two, cross-reference | `NONE` | Lines 31 and 33 carry the identical invariant pair. |
| 12 | CL-40 | same two, cross-reference | `NONE` | Lines 20 and 22. |
| 13 | CL-C-10 | same two, cross-reference | `NONE` | Lines 38 and 40. |
| 14 | CL-E-10 | same two, cross-reference | `NONE` | Lines 37 and 39. |
| 15 | CL-E-20 | same two, cross-reference | `NONE` | Line 22. |
| 16 | CL-E-30 | same two, cross-reference | `NONE` | Line 22. |
| 17 | CL-E-40 | same two, cross-reference | `NONE` | Line 23. |
| 18 | DOC-10 | same two, cross-reference | `NONE` | Line 24. |
| 19 | DOC-20 | same two, cross-reference | `NONE` | Line 24. |
| 20 | ESC-10 | same two, cross-reference | `NONE` | Line 23. |
| 21 | ESC-25 | same two, cross-reference | `NONE` | Line 22. |
| 22 | ESC-30 | same two, cross-reference | `NONE` | Line 22. |
| 23 | ESC-40 | same two, cross-reference | `NONE` | Line 22. |
| 24 | GCFPE-MGMT-10 | — | `NONE` | Names no skill. Line 24 refers to "the dedicated workflow-skill review" as a process gate, not a skill. |
| 25 | IA-10 | — | `NONE` | Names no skill. |
| 26 | IA-20 | — | `NONE` | Names no skill. |
| 27 | IA-30 | — | `NONE` | Names no skill. |
| 28 | IA-40 | — | `NONE` | Names no skill. |
| 29 | IA-50 | — | `NONE` | Names no skill. |
| 30 | IA-60 | — | `NONE` | Names no skill. |
| 31 | MGR-10 | — | `NONE` | Names no skill. Coordination prompt; it determines the next native owner, it does not execute. |
| 32 | OPS-10 | — | `NONE` | Names no skill. Line 64 names an **actor** — "the authorized DevOps or target-environment operator" — not a skill. |
| 33 | OPS-20 | — | `NONE` | Names no skill. Line 9 names the same actor class. |
| 34 | OPS-30 | — | `NONE` | Names no skill. Line 84 names the same actor class. |
| 35 | PR-10 | — | `NONE` | Names no skill. PR planning is explicitly outside `glow-hde-pr-development`'s stated scope. |
| 36 | PR-20 | — | `NONE` | Names no skill. |
| 37 | **PR-30** | `glow-hde-pr-development` | **`PRIMARY`** | Line 59: assigns `glow-hde-pr-development` as the sole primary skill for this PR-30 phase; quoted in full in §B question 1. |
| 37b | PR-30 | `glow-merged-change-attribution-lock` | `PROHIBITED` | Same line 59, final sentence: the lock "is read-only and post-merge and is not used by PR-30". |
| 38 | **PR-35** | `glow-hde-pr-development` | **`PRIMARY`** | Line 10: assigns `glow-hde-pr-development` as the sole primary skill; quoted in full in §B question 1. |
| 38b | PR-35 | `glow-merged-change-attribution-lock` | `PROHIBITED` | Same line 10: "Do not use `glow-merged-change-attribution-lock` here". |
| 39 | PR-40 | `glow-merged-change-attribution-lock` | `SUPPORT` | Line 63: designates the lock as the read-only, post-merge evidence skill for this review; quoted in full in §B question 5. |
| 39b | PR-40 | `glow-hde-pr-development` | `PROHIBITED` | Same line 63: it "is not used to mutate the repository in PR-40". |
| 40 | PR-50 | — | `NONE` | Names no skill. Line 9 makes it unreachable from any skill. |
| 41 | QA-10 | — | `NONE` | Names no skill. |
| 42 | QA-20 | `glow-hde-pr-development` | `NONE` (cross-reference only) | Line 18 records "The primary skill authority is `glow-hde-pr-development`" as a PR-lane fact QA-20 must preserve. |
| 43 | QA-50 | — | `NONE` | Names no skill. |
| 44 | QA-60 | `glow-hde-pr-development` | `NONE` (cross-reference only) | Line 17 preserves "`glow-hde-pr-development` authority" for the PR lane. |
| 45 | QA-70 | `glow-hde-pr-development` | `NONE` (cross-reference only) | Line 24, same invariant. |
| 46 | QA-80 | — | `NONE` | Names no skill. |
| 47 | QA-90 | — | `NONE` | Names no skill. |
| 48 | QA-100 | generic support skill (unfilled) | `NONE` | Line 9: permits a support skill for a bounded environment/Railway/vendor/database/deployment/Ops/QA capability with no PR-workflow authority; quoted in full in §B question 2. No installed skill is designated to fill that slot; see question 4. Line 16 also cross-references the PR lane. |
| 49 | QA-110 | — | `NONE` | Names no skill. |
| 50 | QA-120 | — | `NONE` | Names no skill. |
| 51 | RS-10 | — | `NONE` | Names no skill. |
| 52 | RS-20 | — | `NONE` | Names no skill. |
| 53 | RS-30 | — | `NONE` | Names no skill. |
| 54 | **RS-40** | `glow-hde-pr-development` | **`PRIMARY`** | Line 10: assigns `glow-hde-pr-development` as the sole primary skill; quoted in full in §B question 1. |
| 55 | UTIL-10 | — | `NONE` | Names no skill. |

Totals: 55 prompt rows. Three `PRIMARY` relationships (PR-30, PR-35, RS-40 — all to the same skill). One `SUPPORT` (PR-40 ↔ attribution lock). Four `PROHIBITED`. 17 cross-reference-only rows. The rest `NONE`. Plus the six uniform release-level relationships in §A.0.

---

## B. The ten questions

### 1. Does every prompt that needs a primary skill have exactly one appropriate primary skill?

**Yes.** Exactly three prompts assert a primary skill for their own execution, and all three name the same one.

PR-30, line 59:
> Use `glow-hde-pr-development` as the sole primary skill for this PR-30 phase. Use a support skill only for a specifically needed bounded environment, Railway, vendor, database, deployment, Ops, or QA capability; it is support-only and supplies no PR-workflow authority. `glow-merged-change-attribution-lock` is read-only and post-merge and is not used by PR-30.

PR-35, line 10:
> Use `glow-hde-pr-development` as the sole primary skill. Use a support skill only for a specifically required bounded environment, Railway, vendor, database, deployment, Ops, or QA capability; it receives no PR-workflow authority. Do not use `glow-merged-change-attribution-lock` here; that skill is read-only post-merge evidence for PR-40.

RS-40, line 10:
> Use `glow-hde-pr-development` as the sole primary skill. A support skill is support-only for a specifically needed environment, Railway, vendor, database, deployment, Ops, or QA capability and gains no PR-workflow authority. Across PR-30, PR-35, interrupted recovery, and this eligible RS-40 continuation, preserve exactly one of every item in this canonical list: `WORK_UNIT_ID`; original Product Owner Proceed; dedicated PR-development session; workspace/worktree; branch; pull request; PR instruction; detailed PR plan; primary skill authority; continuous recovery/artifact lineage.

The installed skill's own description matches that assignment exactly — `glow-hde-pr-development/SKILL.md` frontmatter:
> description: Execute one Product Owner-proceeded Glow HDE PR work unit in its single dedicated development session across GCFPE PR-30 implementation/publication, PR-35 review correction/merge readiness, interrupted recovery, and eligible RS-40 continuation. Do not use for PR planning, Product Owner merge, PR-40 lineage review, QA/Ops execution, deployment, or Change Flow orchestration.

No prompt names two primary skills, and no second installed skill claims the PR-30/PR-35/RS-40 lane. The other 52 prompts declare no primary skill because their work is a role's authoring, review or decision act, not a tooled repository operation — PR-10 and PR-20 (PR planning), PR-40 (read-only lineage review), PR-50 (Product-Owner-only manual abort) and the OPS rows are each explicitly excluded from `glow-hde-pr-development`'s scope by its own frontmatter, quoted above.

### 2. Are support skills prevented from assuming workflow authority?

**Yes, in the prompt layer and in the two support-classed skills' own text.**

The generic support clause appears in the same words in every prompt that carries it. PR-35, line 10:
> Use `glow-hde-pr-development` as the sole primary skill. Use a support skill only for a specifically required bounded environment, Railway, vendor, database, deployment, Ops, or QA capability; it receives no PR-workflow authority. Do not use `glow-merged-change-attribution-lock` here; that skill is read-only post-merge evidence for PR-40.

RS-40, line 10 states the same limit and adds the continuity list. QA-100, line 9:
> You are the authorized environment or DevOps operator, not Kronos acting as the executor. Execute **Execute Bounded QA Task** for the exact supplied change. R1 coverage: GCF-23. A support skill may supply only the specifically required environment, Railway, vendor, database, deployment, Ops, or QA capability; it receives no PR-workflow, approval, review, or merge authority.

`glow-merged-change-attribution-lock` disclaims workflow authority in its own frontmatter:
> description: Resolve and validate the landed repository attribution of one merged PR or an ordered merged-PR lineage as temporary, read-only evidence for an active PR review. Separate attributable changes from later divergence without mutating the repository or making QA, PF, Ops, acceptance, repair, drainage, or closure decisions. Use when a Glow PR reviewer needs an in-flight attribution bundle. Do not use for implementation, planning, PR merge, repository repair, QA execution, Ops, or Change Flow orchestration.

and in its compatibility section:
> This skill supplements, but never replaces, native PR-review evidence and guards. It does not create a prompt field, runtime requirement, or prompt-local skill dependency. It does not edit migrated prompts.

`glow-hde-pr-development` states the reciprocal boundary at line 176:
> - Use Change Flow controls for workflow selection and orchestration, not repository implementation.

The one qualification: the support slot the prompts describe is currently **unfilled** — no installed skill is designated for bounded environment/Railway/vendor/database/deployment/Ops capability (see question 4). An unfilled slot cannot assume authority, so the answer stands, but the slot is worth recording.

### 3. Does `glow-hde-pr-development` fully and narrowly own PR-30, PR-35, interrupted PR recovery, and eligible RS-40 continuation?

**Scope: yes. Fully: no — one of the four is broken by a stale internal gate.**

The scope is exactly right. Frontmatter (quoted in question 1) names the four surfaces and excludes PR planning, Product Owner merge, PR-40 lineage review, QA/Ops execution, deployment and Change Flow orchestration. The body carries the recovery duty (the "Recover before creating work" section, lines 37–49), both phases, and the ten-field GCF-17 continuity list that PR-30, PR-35, RS-40, QA-20 and QA-70 all restate identically.

The break is RS-40. The skill still gates the continuation on the drainage lifecycle that D6 retired. `glow-hde-pr-development/SKILL.md` line 57:
> The PR-30 result vocabulary is exactly `PR_CANDIDATE_PUBLISHED`, `RESCOPE_PENDING`, `RECOVERY_PENDING`, or `PRODUCT_OWNER_DECISION_REQUIRED`. The PR-35 result vocabulary is exactly `MERGE_PENDING`, `RESCOPE_PENDING`, `RECOVERY_PENDING`, `REMOTE_EVIDENCE_PENDING`, or `PRODUCT_OWNER_DECISION_REQUIRED`. RS-40 continues the exact recorded PR-30 or PR-35 phase and returns only that phase's lawful result after the four-state drain gate. Do not invent another result, downgrade an external-evidence wait into completion, or treat a postpublication PR-30 rescope as if PR-35 had already begun.

and line 148:
> For an approved rescope with `PR_RETURN_PHASE` of `PR-30_POSTPUBLICATION` or `PR-35`, require the same IA's actual `RESCOPE_REVIEW`, the existing open PR, and fresh `DRAIN_VERIFIED` evidence binding its one approved addendum to the independently resolved current PF10 Markdown. Only those open-PR branches use selected `RS-40 — Approved Rescope — Resume PR Implementation`. Resume the recorded phase in the same dedicated PR session, workspace/worktree, branch, open PR, current evidence and original Product Owner Proceed. The approved delta overlays the immutable base only for its explicit scope; do not reauthor the base Plan, create a duplicate work surface, restart the PR, or obtain another Proceed. An accepted-final PR remains final and must never be rerun.

The RS-40 prompt supplies no such evidence and forbids the comparison that would produce it. `RS-40.md` line 16:
> If unique current controlled PF10 Markdown cannot be resolved and read, return `SOURCE_RESOLUTION_ERROR`, stop terminally, and preserve evidence. Otherwise work from the current PF10 as read. Record the PF10 version actually read as provenance; it is evidence of what was read, never a gate on later work. Do not compare current PF10 against the addendum, and never stop, wait, or route on whether the approved delta is yet present, absent, or worded differently.

This is Finding F1. Everything else in the four-surface ownership is intact.

### 4. Is a support skill limited to specific environment, Railway, vendor, database, deployment or bounded Ops capabilities, with no PR-lane authority?

**The limit is stated correctly everywhere it appears, and no installed skill currently occupies the slot.**

Eighteen prompt bodies carry the support clause in one of two identical forms (PR-30/PR-35/RS-40/QA-100 and the CL/DOC/ESC family). All of them bound it to "environment, Railway, vendor, database, deployment, Ops, or QA capability" and deny PR-workflow authority.

The skill that historically filled the slot, `glow-hde-devops`, is not installed and is named by no prompt — the approved registry actively forbids its name in every body (question 8). `glow-hde-pr-development` absorbs the capability into its own authority instead, at line 175:
> - Handle a genuinely needed environment, Railway, vendor, database, deployment, or bounded operational capability inside this skill's own authority. Such work supports PR-30 and PR-35; it never governs them or transfers authority to another skill.

That is a lawful resolution: the prompts say a support skill *may* be used ("Use a support skill only for..."), never that one must exist. Nothing in a real run stalls for want of it.

### 5. Is `glow-merged-change-attribution-lock` limited to optional read-only landed-attribution support for PR-40?

**Yes, on both sides, and it is the cleanest skill in scope.**

PR-40, line 63:
> `glow-merged-change-attribution-lock` is the read-only, post-merge skill for resolving landed attribution during this review. It supplies evidence only and has no implementation, correction, rescope, QA, Ops, acceptance, merge, or closure authority. `glow-hde-pr-development` remains the PR-30/PR-35 implementation authority and is not used to mutate the repository in PR-40.

PR-30 (line 59) and PR-35 (line 10) each exclude it by name. Seventeen other bodies restate "read-only post-merge evidence for PR-40 only".

The skill agrees. Frontmatter is quoted in question 2. Its read-only invariant is enforced mechanically, not just asserted — `glow-merged-change-attribution-lock/SKILL.md` line 49 lists the forbidden Git operations, the artifact filename at line 106 lives inside a task-owned temporary directory, and line 112 forbids promoting it to any durable store. Its optionality is explicit at line 120:
> After validation, provide the reviewer the complete artifact bytes within the active task. If the reviewer runs in the same environment, use the task-local file. If an already-active relay can transfer a task-scoped attachment, it may do so without becoming a dependency of this skill. Do not place a filesystem path into an ID-only prompt field. If complete transient delivery is unavailable, omit the bundle and let the reviewer run natively.

Its bundled fixture suite passes in this environment: `python3 scripts/run_fixture_tests.py` returns `"suite_ok": true`, exit 0.

### 6. Does `change-flow` orchestrate the selected workflow without performing repository implementation?

**Yes.**

`change-flow/SKILL.md` line 248:
> Coordinate exactly one complete Epic or CRD change from Product Owner class selection through the canonical runtime endpoint. The endpoint includes an Isis closure decision, the required manual post-closure ceremony, actually selected optional maintenance and a final shared CL-40 scan for missing PF09 rows and CRD candidates. The scan is the last managed prompt and does not decide or reopen closure.

Its embedded Primary core, line 33:
> - Act as the controller and evidence keeper, not as a substitute for the worker sessions being orchestrated.

Its PR row delegates rather than implements — line 446:
> - GCF-17 — The same dedicated PR session implements only that work unit across selected PR-30 and PR-35, validates it, and creates exactly one active branch and pull request. Any ordered lineage wording refers only to read-only historical landed-attribution evidence after manual merge, never multiple active work vehicles. PR-30 ends at coherent initial publication; PR-35 owns review correction and genuine current-head merge readiness. In-scope repair remains there. Out-of-scope work stops.

and its runtime entry gate, line 268, requires the delegation policy as an input:
> - The policy for one dedicated PR-development session per planned PR work unit, using `glow-hde-pr-development` as the sole primary skill across PR-30 implementation/publication, same-session PR-35 review/readiness, interrupted recovery, and eligible RS-40 continuation.

There is no implementation instruction anywhere in the specialization: no commit, push, test-run or branch-creation directive addressed to itself. The reciprocal boundary is stated in `glow-hde-pr-development/SKILL.md` line 176.

`change-flow` also refuses to run this release until the register selects it — line 269 states `never treat reservation or publication as selection`, and line 274 rejects an "unselected candidate". Every prompt body carries `UNSELECTED_CANDIDATE` or `Lifecycle: \`UNSELECTED_CANDIDATE\``. That refusal is correct governance, not a defect.

Two stale bindings inside `change-flow` are Findings F10 and F11.

### 7. Do `flowmaster-validate` and `amthor-workspace-governance-audit` validate rather than author, approve, promote, or execute runtime work?

**Their declared posture is correct. Their executable behaviour is not currently usable, and what they assert about the corpus is stale.**

Posture, `flowmaster-validate/SKILL.md` line 21:
> This skill is a deterministic read-only validator. It never repairs a skill, propagates a core, invokes Change Flow, calls live Notion workflow components, mutates a registry, or converts a finding into an accepted deviation.

and line 51:
> This validator remains read-only. It does not repair prompts, mutate skills, publish/archive pages, run workers, drain PF10, merge, resume Alpha, or activate automation.

Posture, `amthor-workspace-governance-audit/SKILL.md` line 18:
> - Remain read-only in every mode. Do not edit, install, publish, archive, retire, move, approve, or execute anything.

and line 26:
> - Do not invoke `skill-creator`, Flowmaster propagation, or any manager/writer to fix findings. Recommend the correct pathway only.

Neither authors, approves, promotes or executes. I found no instruction in either that mutates a governed surface, and `amthor`'s bundled fixture suite passes (29 tests, exit 0).

But three things break when either is actually run against this release:

- `flowmaster-validate`'s documented entry point does not execute at all (Finding F6).
- Its prompt-corpus check requires the retired drainage tokens and so fails a compliant corpus (Finding F5), and hard-codes a single header schema that 11 of the 55 compliant prompts do not use (Finding F7).
- `amthor` asserts the retired drainage contract and a Drive-link handoff requirement as audit invariants (Finding F8), and its registry validator cannot read the approved registry (Finding F9).

So: they validate rather than author — but against the wrong expected state.

### 8. Do any prompt contracts require a capability that no installed skill safely supplies?

**No.**

The approved registry declares **no skill requirement at all**. `required_interfaces` on all 55 rows contains only other prompt IDs (verified by parsing: 50 distinct values, every one a prompt key). The registry mentions no skill name anywhere except in a prohibition. Skill authority is declared in the prompt bodies, and every capability those bodies name is supplied:

- PR-30/PR-35/RS-40 need one PR-execution skill → `glow-hde-pr-development`, installed.
- PR-40 optionally needs landed-attribution evidence → `glow-merged-change-attribution-lock`, installed, optional, degrades gracefully.
- The bounded environment/Ops capability → absorbed into `glow-hde-pr-development`'s own authority (question 4).
- Everything else is a role's authoring/review/decision act needing no skill.

**`glow-hde-devops`, established for myself from the inputs.** It is not installed: no directory in the skills root, no entry in `manifest.json`, and the path the observational registry records for it (`/root/.codex/skills/remote-skills`) does not exist in this environment. It is named by **no** prompt body. That is not an accident of drafting — the approved registry forbids the name in every one of the 55 rows. From `project-prompt-contract-registry.md` line 208, repeated identically on all 55 rows under `forbidden_regex`:
>     - value: (?<![.\w/-])glow-hde-devops(?![\w-])

I verified all 55 bodies against every assertion in their registry rows — required literals, required regexes and forbidden regexes — and found **zero violations**. So `glow-hde-devops` was deliberately de-named from the prompt layer and its capability folded into `glow-hde-pr-development`. Its absence is a completed decision, not a gap. The only residue is that `docs/ephemeral/GCFPE-20260914.1-Observed-Workspace-Skill-Registry.md` (status `DRAFT`) still lists it `lifecycle: ACTIVE` — stale inventory evidence with no runtime consumer, so not a finding.

### 9. Do any installed skills overlap, contradict, overreach, or carry obsolete prompt/version bindings?

**No overlap and no overreach. Extensive obsolete bindings, and one direct contradiction of an approved ruling.**

*Overlap:* none. Each in-scope skill owns a disjoint surface, and the two candidate collision points are resolved by name in the bodies (PR-30/PR-35 exclude the attribution lock; PR-40 excludes the PR-development skill).

*Overreach:* none found. Each skill's own text denies the authorities adjacent to it, and I could not find a clause where one reaches into another's lane.

*Primary-core drift:* none. The marked core block is byte-identical across `flowmaster-primary`, `change-flow`, `tw-flowmaster`, `session-branch-flowmaster` and `session-relay-flowmaster` (SHA-256 `22e6fb73df9d57e66d2a0320c3f303b3aff22790e975597ad0696603506ca68b`, 18175 bytes each), and all five declare `FLOWMASTER_CORE_REVISION: 1.0.3`. There is therefore **no approved Primary-core change**, so `flowmaster-propagate` has nothing to do and is out of scope by the brief's own condition.

*Obsolete bindings:* this is where the release is actually broken. D6 retired the PF10 drainage lifecycle from prompt behaviour entirely, and D7 removed Drive as a storage authority. Both were applied to the prompt corpus — I verified the 55 bodies contain **none** of the retired tokens. Four installed skills were not repaired with them:

| Skill | Retired-token lines | Drive-as-authority lines |
|---|---|---|
| `glow-hde-pr-development` | 8 | 10 |
| `amthor-workspace-governance-audit` | 3 | 5 |
| `change-flow` | 2 | 9 |
| `flowmaster-validate` | 2 | 4 |

These produce Findings F1, F2, F5, F8, F10, F11. The sharpest form is a validator that *requires* what an approved registry *forbids*: `flowmaster-validate/scripts/validate_gcfpe_20260914.py` line 1258 demands `READY_FOR_MANUAL_DRAIN`, `NON_CANONICAL_PENDING_MANUAL_DRAIN` and `drain_owner` in six prompt bodies, while `project-prompt-contract-registry.md` lists those same tokens under `forbidden_regex` on every row.

*Version bindings:* `change-flow` line 268 and `flowmaster-validate` line 27 both describe `GCFPE-20260914.1 / 091426.1 / 55` as a staged candidate behind the still-selected `GCFPE-20260913.1 / 091326.2 / 54`. That agrees with the prompt headers and the register model, so it is current, not obsolete.

### 10. Is a new specialized skill actually required, or can the existing specialized PR-development skill be corrected without duplicating authority?

**No new skill is required. Correct the existing one.**

Every defect I found in `glow-hde-pr-development` is a stale binding to two retired rulings, not a missing capability: the RS-40 drain gate (F1), Drive-shaped intake and storage (F2), a second-branch artifact rule (F3), and a one-string validator drift (F4). None needs behaviour the skill does not already describe; each is removal or substitution inside the existing text.

A new skill would also be actively harmful here. Twenty-two prompt bodies name `glow-hde-pr-development` as the **sole** primary skill authority, and the ten-field GCF-17 continuity list makes `primary skill authority` a field that PR-30, PR-35, interrupted recovery and RS-40 must share exactly one value for — asserted identically in PR-30 line 10, PR-35 line 11, RS-40 line 10, QA-20 line 18, QA-70 line 24 and `glow-hde-pr-development/SKILL.md` line 55. A second PR-lane skill would give that field two values and break the invariant that three separate validators check.

---

## C. Findings

Eleven findings. All are in installed skills; the 55 prompt bodies and the approved registry are internally consistent and consistent with each other.

### F1 — `glow-hde-pr-development` gates RS-40 on the drainage lifecycle D6 retired

**What is wrong.** The skill requires `DRAIN_VERIFIED` before resuming an approved open-PR rescope, and describes RS-40 as returning its result "after the four-state drain gate".

**Evidence.** `/root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502/glow-hde-pr-development/SKILL.md`, line 57:
> The PR-30 result vocabulary is exactly `PR_CANDIDATE_PUBLISHED`, `RESCOPE_PENDING`, `RECOVERY_PENDING`, or `PRODUCT_OWNER_DECISION_REQUIRED`. The PR-35 result vocabulary is exactly `MERGE_PENDING`, `RESCOPE_PENDING`, `RECOVERY_PENDING`, `REMOTE_EVIDENCE_PENDING`, or `PRODUCT_OWNER_DECISION_REQUIRED`. RS-40 continues the exact recorded PR-30 or PR-35 phase and returns only that phase's lawful result after the four-state drain gate. Do not invent another result, downgrade an external-evidence wait into completion, or treat a postpublication PR-30 rescope as if PR-35 had already begun.

Same file, line 148:
> For an approved rescope with `PR_RETURN_PHASE` of `PR-30_POSTPUBLICATION` or `PR-35`, require the same IA's actual `RESCOPE_REVIEW`, the existing open PR, and fresh `DRAIN_VERIFIED` evidence binding its one approved addendum to the independently resolved current PF10 Markdown. Only those open-PR branches use selected `RS-40 — Approved Rescope — Resume PR Implementation`. Resume the recorded phase in the same dedicated PR session, workspace/worktree, branch, open PR, current evidence and original Product Owner Proceed. The approved delta overlays the immutable base only for its explicit scope; do not reauthor the base Plan, create a duplicate work surface, restart the PR, or obtain another Proceed. An accepted-final PR remains final and must never be rerun.

Same file, lines 139–144 define the four states, including:
> - `MANUAL_DRAIN_REQUIRED`: current PF10 was resolved and read, and the exact stable anchor is absent.

The prompt that drives this surface forbids exactly that comparison. `/tmp/claude-0/-home-user-glow-hdengine-v2/5eb01919-e69e-571c-a806-0cabaacca134/scratchpad/pass/current/RS-40.md`, line 20:
> If unique current controlled PF10 Markdown cannot be resolved and read, return `SOURCE_RESOLUTION_ERROR`, stop terminally, and preserve evidence. Otherwise work from the current PF10 as read. Record the PF10 version actually read as provenance; it is evidence of what was read, never a gate on later work. Do not compare current PF10 against the addendum, and never stop, wait, or route on whether the approved delta is yet present, absent, or worded differently.

The ruling, `/home/user/glow-hdengine-v2/docs/prompt_ecosystem_management/gcfpe.decision-record.md` lines 126–127:
> - RS-40 loses its `DRAIN_VERIFIED` gate and keeps its resumption and routing
>   responsibility. If current Canon says implementation may resume, it resumes.

**What breaks in a real run.** An approved postpublication rescope returns to RS-40. The prompt hands the session a `RESCOPE_REVIEW`, one addendum, and `FRESH_CURRENT_PF10_RESOLUTION_REQUIRED: true` — and no drain evidence, because no prompt produces any. The skill's gate is unsatisfiable. Its own escalation rule (line 158) then classifies a non-verified drain check as a nested reason under terminal `PRODUCT_OWNER_DECISION_REQUIRED` with **no continuation handoff**. The PR work unit stops dead and returns to Nathan for evidence that no longer exists. This is precisely the originating failure D6 was written to eliminate: "a prompt refusing to continue after the PF10 update had already happened, because it was still looking for an intermediate condition that no longer mattered."

**Smallest bounded change.** In `glow-hde-pr-development/SKILL.md`: delete the four-state verification block (lines 139–144) and the `PRE_DRAIN_BASELINE_EVIDENCE` sentence at line 146; strike "after the four-state drain gate" from line 57; in lines 148 and 150, replace the `DRAIN_VERIFIED` predicate with RS-40's actual contract — independently resolve and completely read current controlled PF10 from `docs/pfcanon/`, record the version read as provenance, and resume. Keep approved-base immutability and the routing behaviour, which D6 explicitly preserves.

### F2 — `glow-hde-pr-development` requires Drive as intake and storage authority, contrary to D7 and to every prompt it serves

**What is wrong.** Required inputs are specified as Drive links, the rescope artifact is written to a Drive folder, and a Drive readback is mandated.

**Evidence.** Same file, line 17:
> - the complete IA-issued PR instruction and detailed PR implementation Plan covered by the original Proceed, with versions and actual Drive links;

Line 20:
> - the immutable approved base, unique current PF10 Markdown direct Drive link, every applicable active PF10 addendum direct Drive link, and explicit effective overlay scope;

Line 131:
> 2. save a precise recovery/result artifact in the approved Drive folder;

Line 167:
> Keep repository-controlled outputs at their exact governed paths. Keep reusable prompt bodies in Notion. Do not use provider-internal file IDs as runtime artifact references. After each Drive write, read back the saved file and retain its actual title, version, Drive link, and digest when available.

What the prompts actually supply — `RS-40.md` line 12 requires "the complete RS-20 `RESCOPE_REVIEW` and its repository path; exactly one read-back `PF10_BUILD_NOTES_ADDENDUM` and its repository path", and line 35:
> Write checkpoints, implementation results, action ledger, tests, reviews, CI evidence indexes, and handoffs as complete machine-readable Markdown at paths under `docs/ephemeral/` in the repository, committed and pushed on the working branch, while repository code/evidence remains at explicitly authorized paths. Preserve versions, read every write back completely, and return their repository paths. Google Drive is used only where Nathan directs a specific file there.

`PR-30.md` contains the string "Drive" zero times. The ruling, `gcfpe.decision-record.md` lines 145–147:
> **The repository is the persistent storage and versioning authority for this prompt
> ecosystem. Notion is the operational and indexing layer. Google Drive is not a storage
> authority at all** — not a default, not a fallback, not a place canon is resolved from.

**What breaks in a real run.** PR-30's intake gate. The skill says "Require the complete selected invocation ... including ... actual Drive links". A compliant PR-30 invocation carries repository paths and no Drive links at all, so a session obeying the skill either blocks a valid invocation as incomplete or invents a Drive link to satisfy it. Line 131 sends the rescope artifact to a Drive folder that the prompts, the registry (`forbidden_regex: drive\.google\.com`) and `glow-write-boundary` all exclude as a destination.

**Smallest bounded change.** Substitute "repository path under `docs/ephemeral/`" for each Drive link/folder/readback in lines 17, 20, 131 and 167, matching the wording the 54 prompts already use, and keep the one surviving conditional sentence D7 preserves.

### F3 — `glow-hde-pr-development` mandates a second branch and a second pull request, breaking the GCF-17 continuity the same skill enforces

**What is wrong.** The artifact-storage rule tells the PR session to commit its artifacts on a separate dated branch and open a second pull request.

**Evidence.** Same file, line 165:
> Commit them on a `docs/<yyyymmdd>-<short-slug>` branch and open one pull request; the Product Owner merges.

The continuity contract in the same file, line 55:
> The exact ordered ten-field GCF-17 continuity list is: `WORK_UNIT_ID`; original Product Owner Proceed; dedicated PR-development session; workspace/worktree; branch; pull request; PR instruction; detailed PR plan; primary skill authority; continuous recovery/artifact lineage. PR-30 and PR-35 share exactly one value for each field; the phase boundary may not duplicate, replace, omit, or transfer any field.

What the prompts say — `RS-40.md` line 35 is quoted in F2; `PR-35.md` line 85:
> Write review matrices, action ledgers, checkpoints, rescope requests, and handoff artifacts as complete efficient machine-readable Markdown at a path under `docs/ephemeral/` in the repository, committed and pushed on the working branch. Read every saved artifact back completely and verify identity, body, version, state, repository path, and consumer. Repository paths outside `docs/ephemeral/` and `docs/graph/` are not written, and `docs/pfcanon/` is read-only. Google Drive is used only where Nathan directs a specific file there. Repository-controlled code/tests remain in the exact authorized checkout and PR. Never use an opaque provider or Library identifier as continuity.

Fifty-four of the 55 bodies contain "on the working branch"; none contains `docs/<yyyymmdd>-<short-slug>`.

**What breaks in a real run.** A PR-30 session saving its publication checkpoint obeys line 165, cuts a `docs/...` branch and opens a second PR. The work unit now has two branches and two pull requests, so the `branch` and `pull request` fields of the ten-field list hold two values each — violating the invariant asserted by this same skill (line 58), by PR-30 line 10, PR-35 line 11, RS-40 line 10, QA-20 line 18, QA-70 line 24, and checked by `flowmaster-validate` and `amthor`. It also multiplies the remote actions the skill's own "Control remote-action cost" section exists to minimise.

**Smallest bounded change.** Replace line 165 with the prompts' own rule: commit the artifacts under `docs/ephemeral/` on the work unit's existing working branch and reference them by repository path. `flowmaster-validate/SKILL.md` line 33 carries the same stale assertion and would need the same substitution (see F5's fix scope).

### F4 — `glow-hde-pr-development`'s own bundled validator fails on its own `SKILL.md`

**What is wrong.** The skill's documented post-change check fails because the body was edited without updating the string the validator matches.

**Evidence.** Running the command the skill documents at line 188 (`python3 scripts/validate_glow_hde_pr_development.py`) from the skill directory prints `FAIL: missing Markdown-only PFCanon contract` and exits 1. The validator expects, at `scripts/validate_glow_hde_pr_development.py` line 73:
>         "Markdown-only PFCanon": "Never open, fetch, inspect, compare, cite as authority, or use a Google Doc, DOC, or DOCX PFCanon item",

The body now reads, at `SKILL.md` line 25 (the whole line is shown; the relevant sentence is the third):
> Resolve the currently selected prompt for the actual phase by its exact Notion name, version, and page identity. Do not infer currentness from title similarity or search order. Treat reusable prompts as workflow instructions; treat the supplied approved artifacts as the substantive scope. Resolve PFCanon authority only from controlled Markdown at repository path `docs/pfcanon` on the current head of the default branch, verifying the chosen Markdown item's direct parent. Never open, fetch, inspect, compare, cite as authority, or use a Google Doc, DOC, DOCX, or Drive-copy PFCanon item; Drive holds only the Product Owner's human reference copies and there is no fallback. PFCanon is read-only to every agent. Failure to resolve and completely read one unique controlled Markdown authority is `SOURCE_RESOLUTION_ERROR`, never evidence that a manual drain did or did not occur.

The substring the validator looks for was broken by the insertion of `, or Drive-copy` before `PFCanon item`.

**What breaks in a real run.** The skill's own stated maintenance gate ("Run after changes") cannot pass, so any future authorized repair of this skill either reports a false failure or is done with the gate disabled. It is the guard D14 requires for a ruling, and it is currently dead.

**Smallest bounded change.** Update the expected string on line 73 of the validator to the sentence now in the body. (If F2's Drive repair also touches that sentence, make both edits in one pass.)

### F5 — `flowmaster-validate` requires, in the prompt bodies, the exact tokens the approved registry forbids

**What is wrong.** The bundled release validator asserts the retired drainage lifecycle as a corpus requirement.

**Evidence.** `/root/.claude/skills/synced/.../flowmaster-validate/SKILL.md` line 40:
> - The exact semantic addendum producers remain CF-C-30, CF-E-30, IA-30, QA-70, RS-20, and ESC-40. One qualifying approval creates exactly one standalone `PF10_BUILD_NOTES_ADDENDUM` with `READY_FOR_MANUAL_DRAIN`, `NON_CANONICAL_PENDING_MANUAL_DRAIN`, `drain_owner: Nathan / Product Owner`, the complete required schema, and a stable anchor. Nonqualifying outcomes create none. Producers never edit/number PF10 or claim adoption.

Line 41:
> - Post-drain results are exhaustively `SOURCE_RESOLUTION_ERROR`, `MANUAL_DRAIN_REQUIRED`, `MANUAL_DRAIN_MISMATCH`, or `DRAIN_VERIFIED`. Pre-drain PF10 is `PRE_DRAIN_BASELINE_EVIDENCE`; the receiver independently resolves current controlled Markdown and verifies the exact anchor, normalized delta, and absence of a later conflicting overlay. A source failure never proves that Nathan did not drain.

The check is executable, at `flowmaster-validate/scripts/validate_gcfpe_20260914.py` line 1257–1258:
>             for marker in ("PF10_BUILD_NOTES_ADDENDUM", "READY_FOR_MANUAL_DRAIN", "NON_CANONICAL_PENDING_MANUAL_DRAIN", "drain_owner"):

and line 1293:
>         "RS-40": tuple(EXPECTED_DRAIN_RESULTS + EXPECTED_RETURN_PHASES),

with `EXPECTED_DRAIN_RESULTS` at line 51–53 and `EXPECTED_PRODUCERS` at line 47.

The approved registry forbids those same tokens on every row — `project-prompt-contract-registry.md` line 205:
>     - value: DRAIN_VERIFIED|MANUAL_DRAIN_REQUIRED|MANUAL_DRAIN_MISMATCH|READY_FOR_MANUAL_DRAIN|NON_CANONICAL_PENDING_MANUAL_DRAIN|drain_owner|drain_verification_anchor|PRE_DRAIN_BASELINE_EVIDENCE|pf10_reference_visibility_check|PF10_REFERENCE_VISIBILITY|NATHAN_MANUAL_PF10_DRAIN|pf10_addendum_role|POST_CLOSURE_DRAINAGE_STATUS

**What breaks in a real run.** I ran the check. Calling `validate_prompt_bodies` on the live 55-body corpus (with only the `Prompt ID:` header normalised so the corpus reaches the semantic checks — see F7) produces 21 failures that are purely the retired machinery: `PROMPT_PRODUCER:{CF-C-30,CF-E-30,ESC-40,IA-30,QA-70,RS-20}:{READY_FOR_MANUAL_DRAIN,NON_CANONICAL_PENDING_MANUAL_DRAIN,drain_owner}` (18) and `PROMPT_ROUTE_SEMANTICS:RS-40:{DRAIN_VERIFIED,MANUAL_DRAIN_REQUIRED,MANUAL_DRAIN_MISMATCH}` (3). A correctly repaired release fails its own release gate, and a session trusting the validator would "repair" the prompts back to the state D6 retired — the exact hazard D7 records for the deleted committed graph copy.

**Smallest bounded change.** Remove the three drain markers from the `EXPECTED_PRODUCERS` loop at line 1258, leaving `PF10_BUILD_NOTES_ADDENDUM`; change the `RS-40` entry at line 1293 from `EXPECTED_DRAIN_RESULTS + EXPECTED_RETURN_PHASES` to `["SOURCE_RESOLUTION_ERROR"] + EXPECTED_RETURN_PHASES`, which is what RS-40 actually declares; and strike the two corresponding assertions from `SKILL.md` lines 40–41. Line 33's `docs/<yyyymmdd>-<short-slug>` assertion is the F3 counterpart and belongs in the same pass.

### F6 — `flowmaster-validate`'s documented entry point cannot run in this environment

**What is wrong.** Two hard-coded paths from a different skill layout make the suite abort before any check executes.

**Evidence.** Running the command at `flowmaster-validate/SKILL.md` line 60 (`python3 scripts/validate_flowmaster.py`) from the skill directory returns:

    {
      "fatal_error": "skills root does not exist: /mnt/skills/user"
    }

exit 2. Supplying the real root (`--skills-root /root/.claude/skills/synced/b25b7d44-.../`) returns:

    {
      "fatal_error": "[Errno 2] No such file or directory: '/root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502/skill-6a8f973972a88191ae25426f5a818169/fixtures/gcfpe-20260913.1-091326.2/scenarios.json'"
    }

exit 2. The second path is hard-coded at `flowmaster-validate/scripts/run_gcfpe_current_fixtures.py` line 111:
>         change_skill_dir.parent / "skill-6a8f973972a88191ae25426f5a818169"

That is the codex `remote-skills` package directory name; in the installed tree the sibling directory is `flowmaster-validate`. The selected alias contract is `gcfpe-direct-handoff-contract/3.1`, so the legacy branch containing that path is the one taken.

**What breaks in a real run.** The skill's whole purpose — "Use after editing Primary or a specialization, before or after propagation, or when auditing suite currency" — is unavailable. Any repair of any Flowmaster skill currently has no working suite gate. The targeted validator (`validate_gcfpe_20260914.py`) does run, but it reports `SKILL_MISSING:glow-hde-pr-development` and `SKILL_MISSING:glow-merged-change-attribution-lock` for the same layout reason, plus `PRIMARY_FILE_IDENTITY`.

**Smallest bounded change.** Resolve the fixture path from the script's own location (`Path(__file__).resolve().parents[1] / "fixtures" / ...`, which is where `fixtures/gcfpe-20260913.1-091326.2/scenarios.json` actually sits) instead of a sibling package name, and default the skills root to the parent of the skill directory rather than `/mnt/skills/user`. Both are one-line changes; neither alters a single check.

### F7 — `flowmaster-validate` hard-codes one prompt header schema; 11 of 55 compliant prompts use the other

**What is wrong.** The corpus check requires an unbackticked `Prompt ID:` line and a fixed second line, and aborts the entire corpus validation when a body uses the backticked variant.

**Evidence.** `flowmaster-validate/scripts/validate_gcfpe_20260914.py` line 1213:
>         match = re.search(r"(?m)^Prompt ID:\s*([A-Z0-9-]+)\s*$", prefix)

and `prompt_identity_header_valid`, line 193:
>         and f"Prompt ID: {prompt_id}" in nonblank[:8]

Eleven live bodies use the backticked schema. `CF-C-10.md` lines 1–5:
> Prompt ID: `CF-C-10`
> Prompt version: `091426.1`
> Ecosystem release: `GCFPE-20260914.1`
> Lifecycle: `UNSELECTED_CANDIDATE`

The other 44 use `Prompt Version: 091426.1` / `Prompt ID: RS-40` / `Selection status: UNSELECTED_CANDIDATE`. The approved registry **tolerates both** — its per-row required regex is:
>     - value: 'Prompt [Vv]ersion: `?091426\.1`?'

**What breaks in a real run.** Running `validate_prompt_bodies` on the live corpus returns `PROMPT_BODY_MEMBER_SET` plus eleven `PROMPT_BODY_MISSING_ID` errors and then **returns early**, so no semantic check runs at all. The release gate reports an unusable result on a corpus that satisfies its own approved registry with zero violations. The authoritative side here is the registry, whose regex was written to accept both schemas.

**Smallest bounded change.** Make the ID regex at line 1215 tolerate optional backticks, and relax `prompt_identity_header_valid` to accept the registry's own shapes — `Prompt [Vv]ersion: \`?091426\.1\`?` in the first eight non-blank lines rather than an exact line 2, and `Lifecycle:` as an accepted alias for `Selection status:`. Do not change the 11 prompt bodies: they satisfy the approved registry as written.

*Unestablished, deliberately not counted as a finding:* with headers normalised, `prompt_identity_header_valid` still fails for all 55, because it expects a plain `Candidate Notion URL: <url>?pvs=204` line while the captures render the link as `<mention-page url="...">Title</mention-page>` without `?pvs=204`. I cannot tell from these inputs whether that is a live-body difference or an artifact of how the pages were captured, so I record it and make no claim.

### F8 — `amthor-workspace-governance-audit` audits against the retired drainage contract and a Drive-link handoff requirement

**What is wrong.** Two of its GCFPE audit invariants encode state that D6 and D7 removed, so a compliant corpus fails the audit.

**Evidence.** `amthor-workspace-governance-audit/SKILL.md` line 46:
> - Every addendum states `status: READY_FOR_MANUAL_DRAIN`, `canonicality: NON_CANONICAL_PENDING_MANUAL_DRAIN`, and `drain_owner: Nathan / Product Owner`; carries the exact base, approval, overlay, affected requirements/dependencies/tests/Ops/docs/downstream work, exclusions, conflicts, unresolved items, return point, and stable `drain_verification_anchor`; and remains separate from the decision/handoff. The producer does not edit PF10, allocate canon numbering, or claim adoption. The approved base remains immutable. A pre-drain PF10 link is `PRE_DRAIN_BASELINE_EVIDENCE`. Nathan's manual drain is the canonicalization boundary, and the receiver freshly resolves/read current controlled PF10 before reliance.

Line 47:
> - Post-drain audit results are exhaustively `SOURCE_RESOLUTION_ERROR`, `MANUAL_DRAIN_REQUIRED`, `MANUAL_DRAIN_MISMATCH`, or `DRAIN_VERIFIED`; source failure makes no assertion about drainage. A PR rescope records exactly `PR-30_PREPUBLICATION`, `PR-30_POSTPUBLICATION`, or `PR-35`. After qualifying approval and manual drain, a prepublication branch resumes PR-30 directly with no open PR/RS-40; an open-PR branch uses RS-40 to resume the recorded PR-30 or PR-35 phase in the same session/workspace/worktree/branch/open PR/original Proceed. `REJECT`/`IN_SCOPE_REPAIR` return to the existing repair owner; `REVISION_REQUIRED` uses RS-30; `SPECIFICATION_CHANGE_REQUIRED` returns terminally to Nathan.

Line 45 requires the addendum itself to be a Drive artifact:
> - Exactly the selected approval surfaces that themselves record a qualifying approved rescope, escalation/remediation, material approved-Plan or QA-Plan delta, or in-flight Specification delta emit exactly one separate Drive `PF10_BUILD_NOTES_ADDENDUM`. The six surfaces are exactly CF-C-30, CF-E-30, IA-30, QA-70, RS-20, and ESC-40. Initial approval, rejection/denial, `REVISION_REQUIRED`, pending, unchanged, editorial, and `IN_SCOPE_REPAIR` emit no empty addendum.

Line 38 makes Drive links a handoff requirement:
> - Every nonterminal final response contains exactly one fenced `text` `NEXT_PROMPT_HANDOFF` block that is itself a complete prompt the operator can paste into the receiving session. It begins by directing the receiver to the exact selected destination prompt by name, version, and direct Notion URL; names the receiving role/session and work identifiers; provides direct Drive artifact links; carries status, decisions, constraints, unresolved items, next action, and expected output; and contains no blanks, menus, or alternative destinations. Terminal results identify completion and the native Product Owner return.

The prompts produce the addendum as repository Markdown — `PR-30.md` line 30 states every qualifying addendum "is complete Markdown written at a path under `docs/ephemeral/` in the repository", and contains no drain fields.

**What breaks in a real run.** A governance audit of this release reports the six addendum producers as non-compliant for lacking `READY_FOR_MANUAL_DRAIN`, `NON_CANONICAL_PENDING_MANUAL_DRAIN` and `drain_owner`, reports every handoff as non-compliant for carrying repository paths instead of Drive links, and reports the addendum storage location as wrong. Because the skill is explicitly a preflight/postflight gate for repair batches and "final workflow validation", those false defects become the input to the next repair — re-introducing exactly what was retired.

**Smallest bounded change.** Delete lines 46 and 47's drainage content, keeping the parts D6 preserves (one addendum per qualifying approval, exact base/approval/overlay content, approved-base immutability, the `PR_RETURN_PHASE` triple, and the RS-40 / direct-PR-30 routing); strike "Drive" from line 45 and "provides direct Drive artifact links" from line 38, substituting the repository-path wording the prompts use.

### F9 — `amthor`'s registry validator cannot read the approved registry in its governed form

**What is wrong.** The bundled script parses the whole file as YAML; the approved registry is Markdown with one fenced YAML block, which is the form D7 requires for `docs/prompt_ecosystem_management/`.

**Evidence.** Running the skill's own script:

    python3 scripts/validate_project_prompt_registry.py /home/user/glow-hdengine-v2/docs/prompt_ecosystem_management/project-prompt-contract-registry.md

raises an unhandled `yaml.parser` traceback from `audit_workspace_governance.py` line 55 (`return yaml.safe_load(handle)`) and never reaches a check. The registry's first line is `# Project Prompt Contract Registry — GCFPE-20260914.1 / 091426.1`, and its content begins after a ```` ```yaml ```` fence.

The content itself is valid: extracting the fenced block and calling the skill's own `validate_project_registry` on it returns **0 problems**.

**What breaks in a real run.** The audit's registry-validation step cannot be performed on the registry it is meant to validate. A session either reports the crash as a registry defect (it is not — the registry is schema-clean) or skips the check.

**Smallest bounded change.** In `scripts/audit_workspace_governance.py`'s `load_data`, when the path ends in `.md`, extract the first ```` ```yaml ```` fenced block and parse that; otherwise parse the file as now. One function, no schema change.

### F10 — `change-flow` gates affected delivery on "verified manual drainage"

**What is wrong.** Three passages keep drainage as a blocking condition, and the frontmatter advertises it as part of the flow's scope.

**Evidence.** `change-flow/SKILL.md` line 478:
> - One ESC-40 record supplies the exact remediation decision only when it identifies the immutable approved IMPLEMENTATION_PLAN_REF, explicit bounded delta and required evidence. On approval it emits exactly one PF10 addendum overlay. Affected delivery waits for verified manual drainage, then returns to the native delivery owner and originating verification owner. It does not approve or create a replacement Plan, and no duplicate IA-30 review of the same delta is added. Ordinary IA-30 initial/pending Plan review remains separate.

Line 482:
> - A product objective or exclusion change uses the existing rescope proposal and PO decision plus a standalone Specification delta reviewed by the native Thoth prompt; approval emits one PF10 addendum without rewriting the approved Specification, and no affected continuation relies on the delta before verified manual drainage. The same drain-before-reliance rule governs material Implementation Plan and QA Plan deltas. Early findings may supply approved baseline and source evidence without a nonexistent PR Instruction. PR-originated rescope preserves its same-IA decision and one-addendum/manual-drain contract; after fresh verification, prepublication PR-30 resumes directly while an open-PR PR-30/PR-35 phase uses RS-40. Remediation cannot redefine success to erase a shortfall.

Line 320:
> For PR-30, PR-35, or RS-40, an unrecoverable invocation or missing required source, owner or verified drainage evidence ends terminally at Nathan for that invocation with no continuation handoff. Preserve the work and exact missing evidence; this is neither PR abort nor change closure. Recoverable local defects remain work for the existing session.

Frontmatter, line 3, ends the scope list with "post-closure drainage" — a lifecycle D6's consequences list removes along with `POST_CLOSURE_DRAINAGE_STATUS`, under which CL-20 was renamed to its current title, `CL-20 — Prepare Closure Memo and Post-Closure Record — 091426.1`.

**What breaks in a real run.** After an ESC-40 or RS-20 approval, the orchestrator holds the affected delivery waiting for drainage evidence that no prompt produces and no actor is asked for. The run parks at a gate with no owner. Line 320 additionally makes "missing ... verified drainage evidence" a terminal no-handoff return for PR-30/PR-35/RS-40 — the orchestrator-level twin of F1.

**Smallest bounded change.** In lines 478, 482 and 320, replace the drainage predicate with the current rule: the approved delta is in force from the turn after the addendum is created, and the receiving prompt resolves current PF10 as part of its normal work. Delete "and post-closure drainage" from the frontmatter description. Leave GCF-26's Product Owner ceremony, which D6 preserves as a ceremony rather than a gate, and leave approved-base immutability untouched.

### F11 — The bundled direct-handoff contract carries `pf10_addendum_role` on all 55 members and Drive-URL addendum fields

**What is wrong.** The pinned candidate contract shipped inside both `change-flow` and `flowmaster-validate` still models two fields the decision record deleted.

**Evidence.** `change-flow/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json` and the byte-identical copy at `flowmaster-validate/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json` each contain `pf10_addendum_role` **55 times** — once per member registry row (for example, `RS-40` carries `"pf10_addendum_role": "NON_PRODUCER"`) — and `direct_drive_url` twice.

`D4` deletes the addendum-role token; the registry lists `pf10_addendum_role` among the `forbidden_regex` values quoted in F5. `D1` is titled "No Drive URL in the PF10 addendum contract", and the validator still requires those fields — `validate_gcfpe_20260914.py` lines 70–79 include `approval_decision.direct_drive_url` and `immutable_base.direct_drive_url` in `EXPECTED_ADDENDUM_FIELDS`.

**What breaks in a real run.** The contract is what `flowmaster-validate` compares the graph and the prompt corpus against, and what `change-flow` resolves member identity from. Any repair driven from it re-introduces a deleted field and a Drive URL requirement into the addendum schema. It is a smaller, slower version of the same hazard D7 records when it removed the committed graph copy that "had drifted from its source and still carried the retired drainage machinery".

**Smallest bounded change.** Regenerate the contract from the current graph parts with `pf10_addendum_role` dropped from the member schema and the two `direct_drive_url` addendum fields replaced by repository-path fields; drop the same four entries from `EXPECTED_ADDENDUM_FIELDS` and the `graph_pf10.get("drain_owner")` comparison at line 377. This is a derived artifact, so it should be rebuilt rather than hand-edited — `glow-graph-contract` exists for exactly that.

### Noted, not findings

- `GCFPE-MGMT-10.md` line 24 still says "Do not run the dedicated workflow-skill review or independent post-flight before Batch 6", and D12 retired Batches 3–6. The sentence sits under "## Batch method", which applies only "When the authorization names one repair batch". A release-wide gate is not a batch, so I cannot establish anything that breaks in a real run, and I do not raise it.
- `docs/ephemeral/GCFPE-20260914.1-Observed-Workspace-Skill-Registry.md` (status `DRAFT`) lists `glow-hde-devops` as `lifecycle: ACTIVE` though it is not installed. Stale inventory evidence with no runtime consumer.
- The 11/44 header-schema split is a structural difference. It has exactly one consumer that cares, and that consumer is wrong about it (F7).

---

## D. Verdict

The prompt corpus and the approved registry are consistent with each other and with D1–D14: all 55 bodies satisfy every required literal, required regex and forbidden regex in their registry rows, with zero violations. The assignment of skills is correct — one primary skill, correctly scoped, for the three prompts that need one; one optional read-only support skill for PR-40; support skills held to support; validators holding a read-only posture; `skill-creator` nowhere near a runtime lane; no core drift and therefore no propagation due. No new skill is required and no product-owner decision is outstanding: D6, D7, D4 and D12 already settle the direction of every repair proposed above.

What is wrong is that four installed skills — `glow-hde-pr-development`, `flowmaster-validate`, `amthor-workspace-governance-audit` and `change-flow` — plus the direct-handoff contract two of them share, were left bound to state that two approved rulings retired. Four of the eleven findings stop a real run outright (F1 the RS-40 continuation, F6 the validation suite, F9 the registry check, F10 the orchestrator's delivery gate), two make a compliant corpus fail its own gates (F5, F7), and the rest re-introduce retired state into whatever is repaired next. All eleven are bounded, in-place corrections to existing skills.

SKILL_REPAIR_REQUIRED
