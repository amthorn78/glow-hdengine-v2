---
artifact_type: SKILL_REVIEWER_PROMPT_DRAFT
template: docs/prompt_ecosystem_management/reviewer-prompt-template.md v1.1
modification: MODIFICATION-20260923-closeout-residuals
written_at: PLAN, repair round 6 (P-100)
filled_by: EV/skills/fill_brief.py at X4.4; the filled brief is REVIEWER-PROMPT-cr{{K}}.md
---

# Reviewer prompt draft, rounds cr<k> (PLAN-time draft; X4.4 fills it)

This is the canonical reviewer template with §2 to §9 written at PLAN (P-100). Its fenced block is the template's
fenced block with every slot filled except six tokens, which `EV/skills/fill_brief.py` fills at X4.4 from
`EX/packages.json`, the branch and the round number, and nothing else:

| token | filled with |
|---|---|
| `{{K}}` | the round number: 1 + the number of `REVIEWER-PROMPT-cr*.md` files under `docs/ephemeral/modifications/evidence/closeout-residuals/` and its `attempt-*/` directories on the branch |
| `{{ARCHIVES}}` | one line per package from `EX/packages.json`: `NAME.skill, N files, N bytes, sha256 H; extracted freeze F D` |
| `{{OUT_DIR}}` | the absolute path of `$SCRATCH/skills-out`, where the seven archives are |
| `{{HEAD}}` | `git rev-parse HEAD` at X4.4 before the brief is committed: X4.3's commit, which carries `EX/packages.json` |
| `{{PRIOR}}` | §2's text: the first variant below when no earlier round exists, the second when the earlier round was on this attempt's packages (a re-cut), the third when a PLAN session wrote it for a plan change |
| `{{REREVIEW}}` | §10's re-review line: `NONE, first review.` for the first variant, otherwise the variant's sentence |

`{{PRIOR}}`, first variant (no `REVIEWER-PROMPT-cr*.md` exists):
> NONE for these bytes: this is the first review of this Modification's packages. The installed baseline (§3) was
> confirmed in round a5 (docs/ephemeral/modifications/evidence/SECTION-10-REVIEW-a5-SFR-A5-1.md and -2.md, and
> Nathan's install); that confirmation covers the baseline only and nothing carries to these bytes.

`{{PRIOR}}`, second variant (the earlier round `cr<k-1>` reviewed this attempt's packages, and the session that held
its archives ended before delivery, so X4.3 re-cut them; P-100):
> Round cr<k-1> (REVIEWER-PROMPT-cr<k-1>.md and any verdict files SECTION-10-REVIEW-cr<k-1>-*.md beside it) reviewed
> archives with other sha256 values and the same extracted freeze digests as §1. Its archives were not delivered and
> no longer exist. Every archive sha256 has changed, so nothing carries: not a confirmation, not a measurement. Read
> its verdict files, if any, for their findings; each one is carried forward here by ID and must be re-judged.

The third variant is written by the PLAN session that makes a plan change (P-84 revised): it names the prior round,
its verdicts and digests, what the plan change altered, and the disposition of every prior finding by ID.

`{{REREVIEW}}`: the first variant gives `NONE, first review.`; the second gives `Give the disposition of every finding
in round cr<k-1>'s verdict files, if any.`; the third is written with its `{{PRIOR}}`.

The same brief goes to both reviewers; only the reviewer id and the record path differ. Both are fresh subagents
with no context from the authoring session:
- **SFR-CR{{K}}-1** writes `docs/ephemeral/modifications/evidence/closeout-residuals/SECTION-10-REVIEW-cr{{K}}-SFR-CR{{K}}-1.md`
- **SFR-CR{{K}}-2** writes `docs/ephemeral/modifications/evidence/closeout-residuals/SECTION-10-REVIEW-cr{{K}}-SFR-CR{{K}}-2.md`

```plain text
You are <REVIEWER_ID>, performing independent validation of one skill change. You did not author it.
Nothing is installed and nothing may be installed until you rule. No skill may be installed while
you are reviewing; if the tree moves under you, the review is void — say so and stop.

=== 1. WHAT THIS VERDICT IS SCOPED TO ===
Seven packages, in {{OUT_DIR}}/:
{{ARCHIVES}}
They install together, in one sitting: flowmaster-validate 3.3.1 passes only with change-flow 3.3.1,
session-relay-flowmaster 3.2.0, glow-hde-pr-development 1.3.1 and the dbae180b contract in both bundled
copies. Each line gives the archive's own digest and the freeze digest of the tree it extracts to
(docs/prompt_ecosystem_management/freeze.py <extracted skill dir>). Both are what this verdict is
scoped to.

=== 2. THE PRIOR VERDICT, AND WHAT DOES NOT CARRY ===
{{PRIOR}}

=== 3. BASELINE, SO IDENTITY REPRODUCES BEFORE ANYTHING ELSE ===
Baseline the diff was taken against: the installed synced tree
/root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502,
by the recipe docs/prompt_ecosystem_management/freeze.py <dir>:
  flowmaster-validate 31 a79401deaabe35ce1393d91e8d333e86c26a71500b3c5abd89ff5fdbaa7f8f48
  change-flow 22 ee546df57f3d5f0f0dc29c514376e64ca0fa830fe03e64ff7acd8645648bcb73
  glow-graph-contract 6 4e671ddc935b629f7285baeb42b93c9848b19fdeb1be39ebfcaa35c2d171f1b8
  session-relay-flowmaster 5 15aef9890ebfa286bf56272e64cc9880d6dc57701d4e8b45e15fa6f45c3f2121
  glow-hde-pr-development 4 68077fa6620992997c8bb3949b1135ba47b1c5bd275610eb49c3b7d8d04ecf22
  amthor-workspace-governance-audit 15 819915e4a57184fd3af0c783f13e102892eb7182d0c951727869655d11ae078d
  glow-po-reporting 1 3221ae8de6f6500d27154ed0e77c0241e1679999ce42a953a9f6fad4515a0464
Repaired trees, once extracted (the freeze digests in §1; EV/skills/expected_after_patch.txt):
  flowmaster-validate 31 0ca2a74d…, change-flow 22 9a551af3…, glow-graph-contract 9 e241bb9a…,
  session-relay-flowmaster 5 c8a5b224…, glow-hde-pr-development 4 265f9170…,
  amthor-workspace-governance-audit 15 c214e874…, glow-po-reporting 1 7e04368a….
Reproduce the baseline first. If it does not reproduce, stop and say so before reviewing anything.
The whole synced root's digest also covers 19 skills this change does not touch, which may sync at any
time; it is not an identity of this change (P-79). Do not chase it.

=== 4. WHERE THE REPOSITORY EVIDENCE IS ===
Repository amthorn78/glow-hdengine-v2, local clone /home/user/glow-hdengine-v2. Branch
claude/epic-tesla-17406z — read its HEAD ({{HEAD}} when this brief was committed). NOT MERGED: the
execution pull request is opened only after the Notion landing passes (spec §9 X6.4), so main has none
of this attempt's commits.
**If that branch does not exist when you look, it merged and was deleted.** Read the same paths on
main; the execution pull request would then be the merged one from claude/epic-tesla-17406z.
- The record: docs/ephemeral/modifications/MODIFICATION-20260923-closeout-residuals.md (§A, which Nathan
  approved; §P, which he approved; §E so far).
- The execution specification: docs/ephemeral/modifications/specs/EXECUTION-SPEC-20260923-closeout-residuals.md.
  §5 lists the packages and every edit; §1 lists every PLAN decision (P-01 onward).
- The PLAN evidence: docs/ephemeral/modifications/evidence/closeout-residuals/plan/ (EV). The seven diffs
  are EV/skills/diffs/<skill>.diff; the suite gate is EV/skills/run_gate.py; the recorded suite and
  regression results are EV/skills/results/; the manifest is EV/skills/manifest.json.
- This attempt's evidence so far: docs/ephemeral/modifications/evidence/closeout-residuals/execute/ (EX):
  gate_pre.json, gate_pkg.json and packages.json.
- The rulings: docs/prompt_ecosystem_management/gcfpe.decision-record.md: D22, D23 with its successor
  notes, D24, and D25 (added by this attempt's first commit).
Read AGENTS.md first. It governs.

=== 5. WHAT THE CHANGE CLAIMS, AS CLAIMS ===
C1. Each package is its installed baseline (§3) with exactly EV/skills/diffs/<skill>.diff applied, and
    nothing else: 27 files changed and 3 added (glow-graph-contract's scripts contract_recipe.py,
    regenerate_contract.py and registry_deriver.py), as spec §5.1 counts them.
C2. The item claims, each tested by the suites or a regression:
    ITEM-01 the RS-20 package glow-hde-pr-development describes carries no lineage or evidence the named
      artifacts already hold (D23-B); ITEM-02 session-relay-flowmaster no longer tells a handoff to carry
      advice and identity the named artifacts hold; ITEM-03 flowmaster-validate no longer describes a
      Selection status header its own validator rejects; ITEM-04 its guidance and profile staging_rule no
      longer presume a local copy of the prompt corpus (D22); ITEM-05 and ITEM-06 the governance audit and
      the relay no longer snapshot or hash prompt bodies (D22); ITEM-07 the audit's behavioral fixture no
      longer rejects the cross-session PR-30 to PR-35 route (D23-D); ITEM-08 stage prompts are pinned by
      stable ID, version and direct Notion page, by one GCFPE override sentence outside the byte-identical
      protected core, in change-flow and the relay; ITEM-09 glow-graph-contract states the post-D23 graph
      counts; ITEM-10 change-flow no longer calls 091426.1 the collision-checked reserved successor;
      ITEM-11 validate_gcfpe_current.py fails closed with a named result, not a NameError, for
      --bodies-stdin with the historical alias contract; ITEM-12 the graph builder rejects edge_indices
      bookkeeping that does not match the edges, and reindex repairs it; ITEM-13 the contract regenerator
      and the registry deriver are maintained scripts of glow-graph-contract, and the kept pre-E2 contract
      regenerates the shipped 091426.1 contract byte for byte; ITEM-14 the relay no longer names Drive as
      the artifact plane (text, ARTIFACT_PLANE enum with REPOSITORY, validator, self-test, examples);
      ITEM-15 the five round-a5 non-blocking findings are repaired; ITEM-16 the D22 guards fire on
      regression; ITEM-24 glow-po-reporting places the named state immediately before a NEXT_PROMPT_HANDOFF
      block; ITEM-25 glow-graph-contract says bundled graph copies are validator fixtures built from
      docs/graph/parts; ITEM-36 the release-line check reads the whole body; ITEM-39 no packaged skill
      states the retired D18 Alpha state as current.
C3. The contract goes 4.1.0 -> 4.1.1 (6902924a… -> dbae180b…) in both bundled copies, differing only in
    .contract_revision and .pr_development_contract.primary_skill_revision (1.3.0 -> 1.3.1).
    SKILL_TREE_SHA256 is re-declared last (ed52208f…); validator_revision is 3.3.1 at all four sites.
C4. The suite gate passes on the branch's reindexed graph parts: run_gate.py --set pkg, 34 of 34 rows ok
    (EX/gate_pkg.json).
C5. No main-ecosystem skill text instructs creating, launching or scheduling a session, or running a
    main-ecosystem prompt as a subagent; workers inside a task are allowed, and GCFPE-MGMT-10 and the
    triage prompt are excepted (D23).
Authority: Nathan's approval of ANALYZE (2026-09-23) and of this PLAN (the record's plan_approved_by and
plan_approved_date), and the rulings D22, D23 and D25 as the decision record states them.

=== 6. WHAT TO ATTACK, IN PRIORITY ORDER ===
A1. The D22 guards (ITEM-16): can a body-copying, body-hashing or corpus-snapshot instruction survive
    in any of the seven packages, in text or in a script, and pass every suite? Try a paraphrase.
A2. ITEM-08's override sentence: is the protected core still byte-identical in change-flow and the
    relay, and does the sentence sit outside it at every site the contract names?
A3. ITEM-12 and ITEM-13: the stricter builder and reindex (graph_parts.py), contract_recipe.py and
    registry_deriver.py. Does the builder reject every bookkeeping error it should and accept the
    reindexed parts? Does the recipe reproduce dbae180b… from the kept template, and fail when it should?
A4. ITEM-36: does the whole-body release-line check reject a label line anywhere, and does it
    wrongly reject any legitimate line?
A5. ITEM-14: does any consumer, fixture or example still expect a Drive artifact plane?
A6. ITEM-11: is the named fail-closed result reached on every path that raised NameError?
A7. The revision sites: every version string, validator_revision site and hash pin, recounted
    independently of the author's list.
A8. The author's recorded regressions (§8): which of them test the author's own construction, and
    what they do not reach.
Question, not a finding: is anything in these packages outside the items above, PART-01 and
RULING-5-Q3-A as spec §5.2 lists them?

=== 7. KNOWN LIMITS, VOLUNTEERED ===
L1. The prompt bodies live in Notion and are not part of this review: they are edited and checked by
    the landing gate after this review (spec §9 X4.5 to X6.1). Do not fetch or copy any body (D22).
L2. Nothing is installed; the post-install check (X7.4) comes after the Notion landing and the merge.
L3. The installed tree's manifest.json mtime changes on the host's periodic sync; that is not a
    content change. The whole root's digest may change for the same reason (§3).
L4. The must-fail regressions in EV/skills/results/regress_final_*.json were run at PLAN by scripts
    kept in the PLAN session's scratchpad, not in the repository: their recorded outcomes are there,
    but they cannot be re-run from the repository. Write your own probes (§8g).

=== 8. WHAT TO EXECUTE ===
Work from a scratch copy. Never write to the synced skills directory. Run everything with
PYTHONDONTWRITEBYTECODE=1.
  a. Extract each archive. Confirm the file counts, byte sizes and sha256 in §1 from the bytes you
     were given. Confirm every entry sits under its skill root, with no traversal sequences and no
     entry outside it. Confirm `name:` in each SKILL.md frontmatter is unchanged.
  b. Extract into a clean tree, restore the untouched sibling skills the tooling needs, and run the
     gates FROM THE EXTRACTED CONTENTS, not from any working copy:
       R=/tmp/claude-0/review-<REVIEWER_ID>; mkdir -p "$R/ext" "$R/tmp"
       for s in flowmaster-validate change-flow glow-graph-contract session-relay-flowmaster glow-hde-pr-development amthor-workspace-governance-audit glow-po-reporting; do mkdir -p "$R/ext/$s" && (cd "$R/ext/$s" && unzip -q {{OUT_DIR}}/$s.skill); done
       cp -r /root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502 "$R/root"
       for s in flowmaster-validate change-flow glow-graph-contract session-relay-flowmaster glow-hde-pr-development amthor-workspace-governance-audit glow-po-reporting; do rm -rf "${R:?}/root/${s:?}" && cp -r "$R/ext/$s/$s" "$R/root/$s"; done
       for s in flowmaster-validate change-flow glow-graph-contract session-relay-flowmaster glow-hde-pr-development amthor-workspace-governance-audit glow-po-reporting; do printf '%s ' $s; python3 docs/prompt_ecosystem_management/freeze.py "$R/ext/$s/$s"; done
       cd /home/user/glow-hdengine-v2 && TMPDIR="$R/tmp" python3 docs/ephemeral/modifications/evidence/closeout-residuals/plan/skills/run_gate.py --set pkg --pkg-root "$R/root" --out "$R/gate"
     The freeze lines must equal EV/skills/expected_after_patch.txt. run_gate.py exits 0 only when every
     row equals its embedded expectation; read its `ok` per row and its exit code, not a count alone.
     It writes only under --out, and refuses an --out inside the repository or a skill tree.
     Read each tool's own top-level flag by name. A green section count beside a false suite flag
     means the suite failed.
  c. Confirm the extracted trees differ from the installed tree only in the files listed here, and
     that the list accounts for every difference (diff -rq -x __pycache__ <installed>/<skill>
     "$R/ext/<skill>/<skill>"; derived at PLAN by that command against the patched trees):
       flowmaster-validate: SKILL.md; references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json;
         references/gcfpe-20260914.1-091426.1-validation-profile.json; scripts/run_gcfpe_20260914_fixtures.py;
         scripts/run_gcfpe_current_fixtures.py; scripts/validate_flowmaster.py;
         scripts/validate_gcfpe_20260914.py; scripts/validate_gcfpe_current.py
       change-flow: SKILL.md; references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json;
         scripts/validate_gcfpe_20260914.py
       glow-graph-contract: SKILL.md; scripts/graph_parts.py; added scripts/contract_recipe.py,
         scripts/regenerate_contract.py, scripts/registry_deriver.py
       session-relay-flowmaster: SKILL.md; references/manifest-v2-examples.md; scripts/validate_relay_manifest.py
       glow-hde-pr-development: SKILL.md; scripts/validate_glow_hde_pr_development.py
       amthor-workspace-governance-audit: SKILL.md; references/behavioral-fixtures.md;
         references/epic-reengineering-interoperability.md; references/interoperability-contracts.md;
         references/report-contracts.md; references/rule-catalog.md; scripts/audit_workspace_governance.py;
         scripts/run_fixture_suite.py
       glow-po-reporting: SKILL.md
  d. The contract: both bundled copies are byte-identical and hash to dbae180b…; `diff` against the
     4.1.0 contract (6902924a…, regenerated by contract_recipe.py with --contract-revision 4.1.0
     --primary-skill-revision 1.3.0; spec §5.4 execute.4 gives both commands) shows exactly the two
     revision lines. The graph built from the branch's docs/graph/parts has 55 nodes and 229 edges, and
     its embedded JSON is 575 074 B, sha256 ae2bd159….
  e. Recompute every hash pin from its artifact and confirm each consumer agrees with it:
     SKILL_TREE_SHA256 (flowmaster-validate/SKILL.md), the contract digests the validators pin, and the
     graph digest the candidate root carries.
  f. Recount every versioned site by grep, independently of the author's list: 3.3.1 for
     flowmaster-validate and change-flow, 3.2.0 for the relay, 1.3.1 for the PR skill, 1.13.0 for the
     audit, validator_revision 3.3.1 at four sites.
  g. Write must-fail probes of your own against A1 to A6, and report each result.
Derive every digest from the artifact in front of you. Never transcribe one from the report.

The author's measurements, for you to contradict rather than confirm:
  run_gate.py --set pkg: exit 0, 34 of 34 rows ok (EX/gate_pkg.json at {{HEAD}}); the seven freeze
  lines equal EV/skills/expected_after_patch.txt; the recorded regressions are exact: regress_plan
  36/36, function-level 20/20, the four-package set 33/33, change-flow's own 11/11
  (EV/skills/results/regress_final_*.json); the reindex rewrites 27 files and a second reindex 0.

=== 9. WHAT NOT TO DO ===
Do not install any skill. Do not write to the synced skills directory. Do not merge and do not
enable auto-merge. Do not treat a prior confirmation as carrying to these bytes. Do not edit anything
in the repository: not docs/pfcanon, not the registry, not the graph parts, not the record; your only
write in the repository is your own verdict file. Do not read, fetch, copy or hash any Notion prompt
body, and make no Notion write. Do not push, and do not run git commands that change the branch.

=== 10. THE DELIVERABLE ===
One verdict, using exactly this vocabulary: SKILL_FIT_CONFIRMED or SKILL_REPAIR_REQUIRED. Bind it
explicitly to the digests in §1 and state that it is void for any other bytes. For each finding give
the artifact, the exact defect, the evidence, and the smallest correction. Answer every §6 question
explicitly; a question is not a finding.
State which gates you actually ran and which you could not, plainly, rather than inferring a result.
Write a successor record; do not correct an earlier dated record in place (AUTH-001).
{{REREVIEW}}
Put your answer first and close with DECISION NEEDED, NOTHING NEEDED, or IN FLIGHT.
```
