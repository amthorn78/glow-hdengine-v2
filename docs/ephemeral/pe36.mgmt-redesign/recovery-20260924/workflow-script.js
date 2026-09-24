export const meta = {
  name: 'recovery-evidence-20260924',
  description: 'Bounded forensic evidence for the prompt-ecosystem recovery analysis: live changes, known defects, PLAN salvage and convergence, process and model configuration; then refute-by-default checks',
  phases: [
    { title: 'Evidence', detail: 'four read-only readers over recorded evidence; no new prompt audit' },
    { title: 'Verify', detail: 'refute-by-default checks of the load-bearing claims' },
  ],
}

const CONTEXT = `CONTEXT (established; do not re-derive it):
You are a read-only evidence worker in a bounded RECOVERY ANALYSIS of the Glow GCFPE prompt ecosystem, requested by Nathan (Product Owner) on 2026-09-24.
Repository: /home/user/glow-hdengine-v2. Its working tree is at origin/main c2fbf3c (detached HEAD). Refs you can read: origin/main; origin/pr/474 (head 84c1a03), origin/pr/476, origin/pr/477 (head d6b31be), origin/pr/478 (head d609c45, the full commit history of the closeout-residuals run, 15b900a..d609c45).

What happened:
- 2026-09-23 02:02Z to 17:27Z: one maintenance session, acting as GCFPE-MGMT-10 in its proposed three-mode form, ran MODIFICATION-20260923-alpha-feedback-open-entries (the "AF Modification") through INTAKE, ANALYZE, PLAN, Amendment 1, EXECUTE (E1 to E6) and close-out. It changed the LIVE ecosystem: all 55 live 091426.1 prompt bodies were edited in place in Notion (E6 step 4), six skill packages were installed by Nathan after review rounds a1 to a5, Notion control pages were edited, and graph parts, the registry and an R1 oracle successor changed. PRs #474, #476, #477, all merged.
- 2026-09-23 17:45Z to 2026-09-24 08:28Z: the same session ran the follow-up MODIFICATION-20260923-closeout-residuals (40 items, 17 parts). ANALYZE was approved at 21:05Z. PLAN then ran 8 review rounds and 7 repair rounds without producing an approval request, and Nathan stopped it. Nothing was executed. PR #478 was merged at 09:29Z to preserve the record; a merge approves nothing.
- That session's own RCA: docs/ephemeral/modifications/evidence/closeout-residuals/RCA-20260924-closeout-residuals.md, with its evidence in the rca-20260924/ folder beside it.

Nathan's recovery brief governs this analysis. Its rules for you:
- Do NOT perform a new semantic review of prompts or skills, and do not hunt for new defects. Start from recorded defects and records. Something new is in scope only if it has a concrete execution consequence that you can show from evidence.
- Judge by functional behaviour, not semantic tidiness: a finding matters because it has a credible impact on execution.
- Never treat raw finding counts as progress or regress; weigh severity.
- Preserve work: the default for any change already made is to keep it, unless evidence shows it is harmful.

Hard constraints:
- READ ONLY. Do not write, create, edit or delete any file in the repository, in Notion or in any skill directory. Do not commit, push, fetch, checkout, switch or reset anything in git: other workers share this working tree. Use git show <ref>:<path>, git diff, git log and plain reads only. If you need scratch files, put them under /tmp/claude-0/recovery-scratch/<your-label>/ .
- Do NOT fetch any GCFPE prompt body from Notion: not the 55 live bodies, the PE Metaprompt, the GCFPE-MGMT-10 proposed body or the triage prompt. Use the repository's recorded evidence about bodies instead (it quotes clauses of at most 15 words). Notion operational pages (registers, the Modification Backlog, tracking pages) may be read if you need them.
- Installed skills are readable under /root/.claude/skills/synced/*/<skill-name>/ . Never write there.
- Large files: navigate by headings and grep; do not read a 400 KB spec whole.
- Cite evidence as path:line, commit, or file plus heading. Mark anything you inferred as (inferred).
- Be exact and concise. Your final answer is structured data for the orchestrator, not a report to a human.`

const R1 = `${CONTEXT}

TASK: the live-change ledger and the freeze point.

Nathan's brief assumes the review rounds rewrote a working ecosystem. Establish from evidence what actually changed in the LIVE ecosystem on 2026-09-23/24, when, and how it was checked.

1. For the AF Modification, build a ledger of every change that reached a live surface, grouped by the unit that caused it: the D23 rulings (D23-A results live in artifacts; D23-B short handoffs; D23-C implementor latitude; D23-D PR-35 in its own session; D23-E MERGE_OBSERVED dispatch; D23-F PR-40 reject re-plans through PR-20; D23-G no release header line and version bump instead of sibling pages), the C-TOP rule (no main-ecosystem prompt runs as a subagent; nothing creates a session), D22 (transient body files), D24 (reviewer subagents), AF-004's governance-line scan, AF-006's Notion read-only message, and any other unit you find. For each unit give:
   - surfaces changed: which prompt bodies (a count; name them when there are fewer than about ten, otherwise the rule that selected them), which installed skills, registry rows or guards, graph parts, the R1 oracle, which Notion control pages;
   - the verification that ran, and what it did NOT test (for example, a check that the new wording is present that never checked that contradicting old wording was removed);
   - the residuals recorded afterwards that trace to this unit (close-out section 4, the E6 report's residuals, closeout-residuals items);
   - where the BEFORE state can be recovered for a selective revert: the pre-E2 contract in docs/ephemeral/modifications/evidence/pre-e2-contract/, git history of docs/graph and of the registry, earlier skill packages or reviewed digests in the repository, Notion page history for bodies. Say which of these exist and which do not.
   Sources: docs/ephemeral/modifications/MODIFICATION-20260923-alpha-feedback-open-entries.md (its sections A, P including Amendment 1, and E); MODIFICATION-20260923-pr40-reject-replans.md; docs/ephemeral/modifications/specs/EXECUTION-SPEC-20260923-alpha-feedback-open-entries-v2.md (large: grep its headings and its canonical texts C-*); evidence/e6/E6-report.md; evidence/e6/CLOSE-OUT-20260923.md; docs/prompt_ecosystem_management/gcfpe.decision-record.md D22 to D24 and their successors; git show --stat and diffs of d848942, aeb256e, 77d98dd for docs/graph and docs/prompt_ecosystem_management; evidence/e2, e3 and repair-a1 to repair-a3 as needed.
2. The PLAN window. List every live write (Notion page, prompt body, skill install, registry or graph change landing on main) made after the close-out (2026-09-23 17:27Z) up to now. The RCA's section 6 says the only Notion writes were the Modification Backlog page, a link on the Alpha feedback list and one Backlog update. Confirm or correct this from the git history of origin/pr/478 and origin/main and the records. Also say whether anything on main changed a live-governing document after 17:27Z (for example notion-write-boundary.md, authoritative-surfaces.md, modification-template.md, the decision record) and what.
3. The freeze point for recovery: the repository commit; the last time any live body was written and by which step; whether E6's freeze (step 8, "Nathan lifts the freeze") has been lifted and where that is recorded; the installed skill digests now expected.
4. The previous promoted state: what it was (release identifier, members, skill digests), and what evidence of its BEHAVIOUR survives, given that the 091426.1 bodies were edited in place (D23-G, Amendment 1 A1-3).
5. A short summary of the AF Modification's own process: predicted against actual interaction cost, its review and repair rounds with their outcomes (the EXECUTE preflight, skill review rounds a1 to a5), and its amendments.`

const R2 = `${CONTEXT}

TASK: the known-defect inventory, with each defect's origin and operational significance.

Build one row for every KNOWN open defect in the live ecosystem, from these sources only:
- the 40 items of docs/ephemeral/modifications/MODIFICATION-20260923-closeout-residuals.md (the frontmatter items and section A, including any items whose premise the verification refuted);
- its ANALYZE evidence in docs/ephemeral/modifications/evidence/closeout-residuals/: ANALYZE-body-evidence.md, ANALYZE-anchor-census.md, ANALYZE-skill-evidence.md, ANALYZE-closure.md;
- docs/ephemeral/modifications/evidence/e6/CLOSE-OUT-20260923.md sections 4 and 6, and evidence/e6/E6-report.md's residuals;
- the GCFPE Modification Backlog, Notion page 3e54590a05eb81eb818fd0f42045167a (an operational page; read it), entries MB-*;
- the round-a5 non-blocking findings in docs/ephemeral/modifications/evidence/SECTION-10-REVIEW-a5-*.md;
- D22's unguarded status in docs/prompt_ecosystem_management/gcfpe.decision-record.md.
Leave out the closeout-residuals PLAN's own defects: they concern a plan that never ran. Group body-level findings where one fix covers them (for example the 123 HANDOFF_RESTATES_CONTENT findings are one row per item, not 123 rows), but keep genuinely different mechanisms apart.

For each row decide, with evidence:
(a) origin. PRE_EXISTING: the text or behaviour was there before 2026-09-23 and the AF Modification did not change it. AF_PARTIAL_APPLICATION: the AF Modification added a new rule or text but left older text that now contradicts it. AF_INTRODUCED: the AF Modification's own new text or edit is itself defective. RECORD_ONLY: a document, register or record disagrees with reality, but no session behaves differently. UNKNOWN. Use the ANALYZE evidence (it distinguishes old clauses from placed canonical texts), git history for repository surfaces, the E3/E4/E6 records, and skill history where it exists.
(b) operational significance, in the brief's categories. MATERIAL: has caused an observed failure; or creates a strong likelihood of incorrect behaviour; or makes an important instruction impossible or contradictory; or breaks a handoff, state transition, output requirement or execution boundary. CREDIBLE_RISK: a realistic mechanism, not yet observed. LOW_IMPACT: harmless redundancy, stylistic inconsistency, imprecise wording that is read correctly anyway, an unreachable edge case, minor overlap. NO_RUNTIME_EFFECT: affects records, audits or documentation only.
   State the mechanism concretely ("a session running PR-35 would ...", "change-flow would stop at ... because ..."). Where an old and a new instruction are both present, say which behaviour a session is likely to produce and whether either outcome is harmful. Remember that the old behaviour was working before 2026-09-23.
   Specific checks you must make: ITEM-08 (do change-flow or session-relay-flowmaster pin GCFPE stage prompts by body content hash; after the in-place body edits, would a run now stop, or be told to hash bodies against D22?) by reading the installed skills; ITEM-29, ITEM-30 and ITEM-31 (PR-35 and RS-40 closed result lists against MERGE_OBSERVED; PR-40 reject routing); ITEM-34 (QA-110: can a failing run be accepted?) and ITEM-35 (QA-80), including whether each existed before 2026-09-23 (compare the pre-E2 contract in docs/ephemeral/modifications/evidence/pre-e2-contract/ and the git history of docs/graph); ITEM-22 (registry parent IDs: does anything other than the governance audit read them?); ITEM-11 (the NameError in flowmaster-validate's validate_gcfpe_current.py: which invocation reaches it, and does any routine run use that invocation?).
(c) vs_before_0923: is behaviour now WORSE, SAME or BETTER than before the AF Modification, or UNKNOWN?
(d) the smallest fix (a narrow patch, a selective revert of one change, or none), and a recommendation: FIX_NOW only for MATERIAL, or for CREDIBLE_RISK with a cheap and safe fix; DEFER for the rest; SELECTIVE_REVERT only where a patch is not safe; NONE where nothing should change.
Finish with counts by origin and significance.`

const R3 = `${CONTEXT}

TASK: what the eight PLAN rounds produced that is worth keeping, and whether the loop was converging.

The closeout-residuals PLAN is recorded in: docs/ephemeral/modifications/MODIFICATION-20260923-closeout-residuals.md (section P); docs/ephemeral/modifications/specs/EXECUTION-SPEC-20260923-closeout-residuals.md (425 KB: navigate by headings and grep); docs/ephemeral/modifications/evidence/closeout-residuals/plan/ (its README.md indexes DECISIONS.md, engine/, registry/, skills/, texts/, notion/, dryrun/pass1 to pass7); and the RCA with rca-20260924/ (defects-by-round.csv, defects-r4-r8-path-consequence.csv, round8-review-results.json, process-review.json). The plan's history is on origin/pr/478: 2ef89b6 (first PLAN), then the repair commits 4e62587, 4c8fd00, 0d98ecf, 6b29ce9, de3d3d5, 8a905f3, 46ecce0, 0e24b01.

1. Content against machinery. Split the plan into CONTENT, the edits that deliver the 40 items (body edits: spec section 3, engine/locals.json and closeout_rules.py; skill diffs under skills/diffs/; the registry diff and guards; graph edits; repository texts under texts/; Notion control edits in notion/edits.json), and MACHINERY, everything that exists to handle failure, stop, lift, resume in a new session, route after merge, and the leases, journals and sent lists that serve those. Give sizes (bytes, lines, decision counts) for each side, and list the decisions (P-numbers) that are content.
2. Stability. Check the RCA's claim that spec section 3 (the 51 prompt-body edits) has not changed since 8a905f3, by diffing that section across the commits yourself. Say when each content component last changed.
3. Salvage. For each content component, say whether it could be executed as it stands, what evidence shows it works (dry-run passes 4 to 7: plan and readback on fresh fetches; the skill suite gate's results; the registry guard tests), and what it would still need. The AF Modification's E6 landed 55 bodies with a simpler engine, docs/ephemeral/modifications/evidence/e6/land.py: could the closeout content land the same way, and what did E6 do when something failed?
4. Minimal execution design. Describe the smallest execution that lands the content safely (compare the RCA's corrective action 9). Say which of round 8's four open defects (RCA section 8) disappear if the machinery is cut, and which remain.
5. Convergence, judged by severity and not raw count. The brief: "A process that goes from five serious defects to fifteen cosmetic findings may be converging. A process that repeatedly replaces one serious defect with another is not." From defects-by-round.csv and defects-r4-r8-path-consequence.csv, give per review round: material defects in the 40 items' CONTENT (a wrong edit, or a certain failure on the normal path); defects in MACHINERY split by consequence (silent wrong edit, mis-record or ruling breach, against a loud stop); and how many were regressions that a repair introduced. Then choose one verdict from LEGITIMATE_CONVERGENCE, DIMINISHING_RETURNS, REVIEW_INDUCED_REGRESSION, INAPPROPRIATE_REVIEW_MODEL, MIXED, separately for content and for machinery if they differ, with the numbers that decide it.`

const R4 = `${CONTEXT}

TASK: which governing rules and review practices drove the day's loops; the model-configuration question; stopping-rule candidates.

1. Governing rules. For each rule that contributed to the PLAN loop or to the other loops of the day, say where it lives, who authored it (check git log for each file: the PE36 main session designed D20, D21, docs/prompt_ecosystem_management/modification-template.md v2.0 and modification_validate.py on 2026-09-22/23; the Modification session added D22 to D24 and successors), how it contributed, and a recovery class: KEEP, KEEP_PATCH (with the smallest patch), SELECTIVE_REVERT, DEFER or UNKNOWN. Examine at least: template rule 3 ("Scope freezes at ANALYZE approval ... This is what bounds the review loops"); rule 6 ("A part lands whole or not at all") and its interaction with D22 (no body copies, so no rollback journal); section P's standard ("A plan is complete when it could be executed mechanically with no interpretation"); rules 4 and 5; D20 and D21 (one run carries the whole process; delegate by workload); D24's condition 5 ("Any SKILL_REPAIR_REQUIRED finding is repaired and re-reviewed by fresh reviewers": does anything cap it?); ecosystem-change-management.md DISP-001 and any "no open findings" rule; session-working-rules.md; reviewer-prompt-template.md; execution-and-delegation-model.md; and the redesign analysis docs/ephemeral/pe36.mgmt-redesign/GCFPE-MGMT-REDESIGN-ANALYSIS-v1.0.md, stages 4 and 5 ("pilot on one real, small, already-known change"). Start from the RCA's sections 4 and 7; confirm or correct them rather than repeating them.
2. Every review loop of 2026-09-23/24, in order: the AF Modification's EXECUTE preflight (121, then 198 findings); its skill review rounds a1 to a5, including the "hardening round a3" made after both a3 reviewers returned SKILL_FIT_CONFIRMED (docs/ephemeral/modifications/evidence/SECTION-10-REVIEW-*, REVIEWER-PROMPT-a*, repair-a*); the closeout-residuals ANALYZE (three review rounds, plus the five-sweeper, six-verifier sweep of all 55 bodies); and the PLAN's eight rounds. For each: rounds; what it found that mattered (material against cosmetic); whether it continued after a clean or nearly clean result; whether its value justified its cost.
3. Model configuration. Nathan ran with the highest reasoning setting and the harness's "ultracode" multi-agent mode. From the evidence (RCA RC8, process-review.json, the transcript facts the RCA cites, the contrast between ANALYZE and PLAN under the same mode, which defects only deep full reviews found, such as R3-01 and R4-06, and whether a cheaper dry run could have found them), answer: did the deep configuration find operationally significant defects a standard configuration would likely have missed; did it mainly widen the review surface; did it encourage broad rewrites; should it be the default for routine maintenance; what evidence should trigger escalation to it. Mark inference as inference.
4. Stopping-rule candidates: two or three concrete, checkable rules, each with the evidence that it would have stopped this day's loops at a good point, and its risk.`

const verifyHead = `${CONTEXT}

You are an ADVERSARIAL VERIFIER. Another worker produced the output below. Try to REFUTE its load-bearing claims from primary evidence. Default to REFUTED or UNVERIFIABLE when the evidence does not support a claim; use CORRECTED, with the right value, where a claim is partly wrong; CONFIRMED only when you checked it yourself. Do not add new defects unless evidence shows a concrete execution consequence; put those, if any, under "missed".`

const V1 = out => `${verifyHead}

Checks you must make:
- For EVERY row rated MATERIAL or CREDIBLE_RISK, and every row recommended FIX_NOW or SELECTIVE_REVERT: try to refute (a) its origin and (b) its significance. Find the evidence it cites and check that the mechanism would really occur for a session running that prompt or skill. Downgrade when the mechanism is not demonstrated.
- Then sample at least eight LOW_IMPACT or NO_RUNTIME_EFFECT rows, choosing those most likely to hide a routing, result-list, gate or hash-pinning consequence, and say whether any is in fact material.
- Check the counts.

THE OUTPUT TO VERIFY:
${JSON.stringify(out)}`

const V2 = out => `${verifyHead}

Checks you must make:
1. The claim about live writes in the PLAN window (after 2026-09-23 17:27Z): whether any prompt body, skill install, Notion control page, registry or graph change landed; and whether any live-governing document on main changed after 17:27Z.
2. The surfaces listed for each unit, especially body counts and skill lists.
3. Every "did not test" statement about a verification.
4. The freeze-point facts, including E6 step 8.
5. The availability claims for before-state references: does the pre-E2 contract really regenerate the shipped 091426.1 contract; do earlier skill packages or digests exist in the repository; is Notion page history the only record of earlier bodies?
Add under "missed" only a live change or residual the worker missed that you can show from evidence.

THE OUTPUT TO VERIFY:
${JSON.stringify(out)}`

const V3 = out => `${verifyHead}

Checks you must make:
1. Spec section 3's stability since 8a905f3: run the git diffs yourself.
2. The content/machinery split and the list of content decisions.
3. The salvage claims: do the dry-run pass reports really show plan and readback passing for all 51 bodies; do the skill suite gate results pass; are the registry guard tests recorded as passing?
4. The minimal-execution design's claim about which round-8 defects disappear.
5. The convergence verdict: recompute the per-round numbers from the CSVs and say whether the verdict follows.

THE OUTPUT TO VERIFY:
${JSON.stringify(out)}`

const S = { type: 'string' }
const R1_SCHEMA = {
  type: 'object',
  properties: {
    live_changes: { type: 'array', items: { type: 'object', properties: {
      unit: S, motivating_entry: S, surfaces: S, verification_run: S, not_tested: S,
      known_residuals: S, before_state_reference: S, evidence: S,
    }, required: ['unit', 'surfaces', 'verification_run', 'not_tested', 'known_residuals', 'before_state_reference', 'evidence'] } },
    plan_window_live_writes: S,
    governing_docs_changed_after_closeout: S,
    freeze_point: S,
    pre_change_baseline: S,
    af_process_summary: S,
    notes: S,
  },
  required: ['live_changes', 'plan_window_live_writes', 'freeze_point', 'pre_change_baseline', 'af_process_summary'],
}
const R2_SCHEMA = {
  type: 'object',
  properties: {
    defects: { type: 'array', items: { type: 'object', properties: {
      id: S, summary: S, surface: S,
      origin: { type: 'string', enum: ['PRE_EXISTING', 'AF_PARTIAL_APPLICATION', 'AF_INTRODUCED', 'RECORD_ONLY', 'UNKNOWN'] },
      origin_evidence: S,
      significance: { type: 'string', enum: ['MATERIAL', 'CREDIBLE_RISK', 'LOW_IMPACT', 'NO_RUNTIME_EFFECT'] },
      mechanism: S,
      vs_before_0923: { type: 'string', enum: ['WORSE', 'SAME', 'BETTER', 'UNKNOWN'] },
      smallest_fix: S,
      recommendation: { type: 'string', enum: ['FIX_NOW', 'DEFER', 'SELECTIVE_REVERT', 'NONE'] },
    }, required: ['id', 'summary', 'surface', 'origin', 'origin_evidence', 'significance', 'mechanism', 'vs_before_0923', 'smallest_fix', 'recommendation'] } },
    counts: S,
    notes: S,
  },
  required: ['defects', 'counts'],
}
const R3_SCHEMA = {
  type: 'object',
  properties: {
    content_vs_machinery: S,
    content_decisions: S,
    section3_stability: S,
    salvage: { type: 'array', items: { type: 'object', properties: {
      component: S, executable_as_is: S, evidence_it_works: S, still_needs: S,
    }, required: ['component', 'executable_as_is', 'evidence_it_works', 'still_needs'] } },
    minimal_execution_design: S,
    round8_defects_if_machinery_cut: S,
    convergence_per_round: S,
    convergence_verdict_content: { type: 'string', enum: ['LEGITIMATE_CONVERGENCE', 'DIMINISHING_RETURNS', 'REVIEW_INDUCED_REGRESSION', 'INAPPROPRIATE_REVIEW_MODEL', 'MIXED'] },
    convergence_verdict_machinery: { type: 'string', enum: ['LEGITIMATE_CONVERGENCE', 'DIMINISHING_RETURNS', 'REVIEW_INDUCED_REGRESSION', 'INAPPROPRIATE_REVIEW_MODEL', 'MIXED'] },
    convergence_reasoning: S,
    notes: S,
  },
  required: ['content_vs_machinery', 'section3_stability', 'salvage', 'minimal_execution_design', 'round8_defects_if_machinery_cut', 'convergence_per_round', 'convergence_verdict_content', 'convergence_verdict_machinery', 'convergence_reasoning'],
}
const R4_SCHEMA = {
  type: 'object',
  properties: {
    governing_rules: { type: 'array', items: { type: 'object', properties: {
      rule: S, where: S, authored_by: S, how_it_contributed: S, evidence: S,
      recovery_class: { type: 'string', enum: ['KEEP', 'KEEP_PATCH', 'SELECTIVE_REVERT', 'DEFER', 'UNKNOWN'] },
      smallest_patch: S,
    }, required: ['rule', 'where', 'authored_by', 'how_it_contributed', 'evidence', 'recovery_class', 'smallest_patch'] } },
    review_loops: { type: 'array', items: { type: 'object', properties: {
      loop: S, rounds: S, material_findings: S, cosmetic_findings: S, continued_after_clean: S, value_vs_cost: S,
    }, required: ['loop', 'rounds', 'material_findings', 'continued_after_clean', 'value_vs_cost'] } },
    model_configuration: S,
    escalation_triggers: S,
    stopping_rule_candidates: S,
    notes: S,
  },
  required: ['governing_rules', 'review_loops', 'model_configuration', 'escalation_triggers', 'stopping_rule_candidates'],
}
const VERDICT_SCHEMA = {
  type: 'object',
  properties: {
    checks: { type: 'array', items: { type: 'object', properties: {
      claim: S,
      verdict: { type: 'string', enum: ['CONFIRMED', 'REFUTED', 'CORRECTED', 'UNVERIFIABLE'] },
      correction: S,
      evidence: S,
    }, required: ['claim', 'verdict', 'evidence'] } },
    missed: S,
    summary: S,
  },
  required: ['checks', 'summary'],
}

const READERS = [
  { key: 'live', prompt: R1, schema: R1_SCHEMA, verify: V2 },
  { key: 'defects', prompt: R2, schema: R2_SCHEMA, verify: V1 },
  { key: 'plan', prompt: R3, schema: R3_SCHEMA, verify: V3 },
  { key: 'process', prompt: R4, schema: R4_SCHEMA, verify: null },
]

const results = await pipeline(
  READERS,
  r => agent(r.prompt, { label: `read:${r.key}`, phase: 'Evidence', schema: r.schema, effort: 'high' }),
  (out, r) => {
    if (!out) { log(`reader ${r.key} returned nothing`); return { key: r.key, out: null, verdict: null } }
    if (!r.verify) return { key: r.key, out, verdict: null }
    return agent(r.verify(out), { label: `verify:${r.key}`, phase: 'Verify', schema: VERDICT_SCHEMA, effort: 'high' })
      .then(v => ({ key: r.key, out, verdict: v }))
  },
)
return results