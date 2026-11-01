---
artifact_type: REVIEW_PROMPT
artifact_version: "1.0"
logical_id: HDE-M10V2-MECHANICS-PROPOSAL-REVIEW-PROMPT
title: "Independent review of the Magic10 v2 mechanics proposal: correctness, engineering feasibility and scope, and alchemical fidelity"
requested_by: "Nathan (Product Owner), 2026-11-01: 'create a prompt for an independent session that reviews it for correctness, engineering feasibility and scope, AND alchemical fidelity'"
reviewed_artifact: "docs/ephemeral/HDE-M10V2-mechanics-proposal-v1.0.md on amthorn78/glow-hdengine-v2 main 0bf99656 (merged by #824); SHA-256 dc064a2780042a98ebefa2b3dc3f326a8674c4185ac950881b5845503a3f3c2a; git blob 7b6ab7638e7d62fd38a063eeb816a2af25b78a63; 3,243 lines"
brief_step: "docs/ephemeral/HDE-M10V2-hd-math-specialist-design-brief-v1.0.md §9 step 3 (independent review)"
recorded: "2026-11-01T23:47Z"
producer: "Isis (session https://claude.ai/code/session_01Q789tyhUaytmY7x273kwes), who wrote the design brief but not the proposal"
---

# Independent review of the Magic10 v2 mechanics proposal (prompt v1.0)

**Model and reasoning setting**

- **TypeSafe v8.2: Fable 5.1 at max.** Effort score 3.89 (confidence 0.92); rung probabilities low 0.00, medium 0.00, high 0.02, extra high 0.07, max 0.90, ultracode 0.01. Model probabilities Fable 5.1 0.66, Opus 5.5 0.33, Sonnet 5.5 0.01, Haiku 5.5 0.00 (confidence 0.55). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.000, Fable 5.1 at high 0.013, Fable 5.1 at extra high 0.046, Fable 5.1 at max 0.594, Fable 5.1 at ultracode 0.007, Opus 5.5 at low 0.000, Opus 5.5 at medium 0.000, Opus 5.5 at high 0.007, Opus 5.5 at extra high 0.023, Opus 5.5 at max 0.297, Opus 5.5 at ultracode 0.003, Sonnet 5.5 at low 0.000, Sonnet 5.5 at medium 0.000, Sonnet 5.5 at high 0.000, Sonnet 5.5 at extra high 0.001, Sonnet 5.5 at max 0.009, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Sent 2026-11-01T23:49:03Z. Nathan picks the cell.

Paste everything below the line into a new session with **both** repositories attached: `amthorn78/glow-hdengine-v2` and `amthorn78/glow-docs`.

---

## 1. Your task

You are the **independent reviewer** of the Magic10 v2 mechanics proposal.
* The proposal designs a new compat scoring formula for the Glow HD Engine: relevant placement, center completion, aura-type pairing, and relative per-category bands.
* The Product Owner will decide whether to adopt it, and will use your review to decide.

Review it on four dimensions, and give a verdict on each:
1. **Correctness:** the mathematics, the measurements, and the Human Design doctrine.
2. **Engineering feasibility:** whether it can be built as stated, and at what cost.
3. **Scope:** whether it does what the brief asked, within canon, and nothing more.
4. **Alchemical fidelity:** whether it keeps to Glow's own method, as defined in §5.4 from canon.

**The artifact under review.**
* `docs/ephemeral/HDE-M10V2-mechanics-proposal-v1.0.md`, on `main` at `0bf99656`.
* SHA-256 `dc064a2780042a98ebefa2b3dc3f326a8674c4185ac950881b5845503a3f3c2a`.
* Confirm both values before you start. If they differ, stop and report.

## 2. Independence

* **You are not the proposal's author** (session `01Q789tzD1cBKzL7p4Cec46s`), **nor the brief's author** (session `01Q789tyhUaytmY7x273kwes`). Do not contact either session, and do not rely on their transcripts.
* **Judge the work itself.** The proposal's own summaries, and §8 of this prompt, are claims to test, not facts to accept.
* **Do your own full review first.** Turn to §8 only after you have formed your own findings on every dimension.
* **Record your session ID** in your review.

## 3. What you may and may not do

* **Read:**
  * both repositories, on `main`;
  * canon in `glow-hdengine-v2/docs/pfcanon/`;
  * the Human Design collection in `glow-docs/docs/hd_refs/`, through its `Human Design Reference Index.md` (v1.2.0).
* **Run** the proposal's analysis scripts, and any checks of your own, offline under closed rails (`LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev`). The scripts need PyEphem 4.2.1, installed for the analysis only.
* **Write** exactly one file, `docs/ephemeral/HDE-M10V2-mechanics-proposal-review-v1.0.md`, through one pull request to `amthorn78/glow-hdengine-v2`. Write nothing else: no canon, code, catalog, test, data, Notion page, or anything in `glow-docs`.
* **Make no vendor calls,** and touch no production system or database.
* **Sources.**
  * For mathematics, outside sources are allowed.
  * For Human Design doctrine, use the admitted collection. The proposal used the brief's §2.4 routes for aura and composite doctrine: authoritative outside sources, or labelled inference. You may check outside sources to test that use, and must record what you consulted.
* **Approve nothing.** You give verdicts and recommendations; the Product Owner decides.

## 4. Read first

1. **The proposal,** all of it, including Appendices A to D.
2. **The brief:** `docs/ephemeral/HDE-M10V2-hd-math-specialist-design-brief-v1.0.md`. It is the specification the proposal answers: §3 direction, §5 D-1 to D-7, §6 constraints, §7 deliverables, §12 decisions.
3. **The evidence:**
   * `docs/ephemeral/HDE-EPIC041-POSTCLOSE-compat-score-range-v1.0.md`: the v1 harness and its population, Appendices A to F;
   * `docs/ephemeral/HDE-EPIC041-POSTCLOSE-OPS01-ops-execution-result-v1.0.md` and `audit/ops/hde-epic041/postclose-ops01/`: the live pairs.
4. **Canon:**
   * **HDE Math Spec:** §2.5, §4.1, §5.2 to §5.6, §6.1 to §6.7, §7, §8, §9.
   * **HDE Governance:** §4.1.5 and §12.1.
   * **HDE Schemas & Artifacts:** §2.
   * **HDE Narratives Guide:** the candidate registry.
   * **Glow Story.**
   * **HDE Build Notes (current version):** 2.15 and 2.16.
   * **For alchemical fidelity:**
     * the 7 Phases of Alchemical Engineering reference (PF21) in full;
     * the Glow Development Philosophy (PF13), §B, §C, §D and §I;
     * the HDE Build Checklists for Separation (Task HDE-SEPA005), Conjunction (Task HDE-CONJ010) and Distillation (Task HDE-DIST008).
5. **The Human Design references the proposal cites:**
   * the Reference Index;
   * *The Complete Guide to the Human Design System* (PDF);
   * PF08;
   * the Generators' Course;
   * Holistic Analysis Fundamentals;
   * Winn, which the index ranks A5, for corroboration only.

## 5. The review

For each check: state what you did, what you found, and your evidence (a locator, or a command and its output).

### 5.1 Correctness

1. **Reproduce the measurements.**
   * Extract the seven Appendix C scripts and verify their SHA-256 values.
   * Rerun the v1 baseline, the v2 measurement, the goldens and the sensitivity runs.
   * Confirm or refute every number in §1, §4.4, §5 and §6, including AB↔BA and two-run identity.
2. **Formula integrity.**
   * Integer-only arithmetic, and the `rhu` definition.
   * One complete evaluation order.
   * Every value populated, and no hidden default.
   * Fail-closed closure, and symmetric `A` and `I` tables.
   * One clamp.
   * The edge cases: equal masks, `W = 0` and `F = 0`, a pair of Reflectors, and the M10-G001 to G008 adaptations.
3. **Type derivation.** Check the §3.4 rule against the Complete Guide (printed pages 229 to 232) and the Generators' Course.
   * Check the any-route motor-to-Throat predicate. A direct-only rule would change 10.7% of Types; is any-route the correct doctrine?
   * Check whether treating Manifesting Generator as a Generator aura class is correct.
   * Check the "5 of 5 vendor charts match" claim against the actual fixtures.
4. **Doctrine citations.**
   * Verify every quoted passage at its stated locator.
   * Check that each claim-status label is right.
   * Check that §2.6 lists every rule that is not admitted doctrine. Flag any rule presented as doctrine that is really inference or product choice.
5. **The aura-pairing gap.**
   * Confirm, by your own search of the admitted collection, that no admitted source states a Type-pair rule.
   * Assess the outside-source search record in Appendix B, and the recommendation to acquire *Type Sexual Signatures*.
6. **Inference quality.** For Tables 7a and 7b:
   * Does each row follow from the cited aura doctrine?
   * Are the signs and sizes defensible?
   * What alternatives exist?
7. **Statistical validity.**
   * **Circularity.** The per-category lines are fitted to the same population they are measured on, so the 30/35/25/10 mix holds by construction. Say which results are informative.
   * **Out of sample.** Test the frozen lines on populations you generate yourself: different seeds and birth eras.
   * **How much of the "no zero scores" result is constant offset?** For example, the Type component's 500 baseline at 15% weight, or foundation profiles. How much is relational signal?
   * **What Glow means now.** Under these lines, 55.9% of pairs show at least one Glow. Does Glow still mean something?

### 5.2 Engineering feasibility and scope

1. **Implementation impact.** Is §8 complete?
   * code areas;
   * catalogs and schemas;
   * the admission constants in `engine/config/registry_loader.py`;
   * the release cut, cache invalidation, performance and Reader shapes.
2. **Pure Engine Core.** Can the formula run as pure Engine Core computation with catalogs injected, and with fail-closed validation (HDE Math Spec §7.2 item 7, §7.3)?
3. **Open PF09 work.**
   * HDE-DIST008, "Full-domain Magic10 verification", is Partial, and is written around v1's mechanics.
   * What happens to it, and to HDE-SEPA005 and HDE-CONJ010, if v2 is adopted?
   * Does the proposal account for this?
4. **Gates and tests.** What the HDE Build Notes 2.16 owner tests, the goldens, and the live compat test (2.15) need.
   * Whether the score-distribution command-line utility, Candidate CRD Items List item 13, should be part of the same change.
5. **Reproducibility.** Can someone other than the author run the scripts as published?
6. **Brief compliance.**
   * Is every requirement D-1 to D-7 met?
   * Is every deliverable in brief §7, items 1 to 10, present?
   * Are the brief §12 decisions answered, with recommendations?
7. **Canon constraints** (brief §6):
   * input closure and determinism;
   * the promotion prerequisites (HDE Math Spec §7.2 and §8.2, items 1 to 8) and invariants (§7.3, §8.3);
   * the public covenants and eligibility;
   * the out-of-scope list, including "no relationship verdicts" and keeping viewer preferences outside intrinsic scores.
8. **Canon delta list (§7).** Does every cited section exist, and is any needed change missing?
9. **Overreach.** Anything changed or claimed beyond the brief's scope.
10. **Product effects of Type.** Measure whether some Types systematically score lower across all their partners, overall and per category. That matters for both bands and ranking.
    * Is the effect justified by doctrine, disclosed, and within the "no relationship verdicts" boundary?
    * Which Product Owner decision does it need?

### 5.3 Alchemical fidelity — the criteria, from canon

Score the proposal against each of these. Cite the canon passage you apply.

1. **Phase placement and mode discipline.** PF21 says "The power is in not mixing modes."
   * Name the phase this work is in, and check that the proposal stays in it: no implementation, and no premature solidifying.
   * In particular: is freezing band lines from a synthetic population a Coagulation step taken before Fermentation, when the product meets real users? Is recalibration routed to the right later phase?
2. **Ψ / Λ / Σ coherence** (PF21's Hermetic overlay: vision, model, body).
   * Does the change move all three consistently?
     * **Vision (Glow Story):** bands as the user signal, narratives chosen by band, ranking, the "#1 category" band.
     * **Model:** the HDE Math Spec and HDE Governance.
     * **Body:** catalogs and code.
   * Is any layer left contradicting another, for example the HDE Users Guide's examples?
3. **PF13's four elements and its definition of done** (PF13 §C, §I):
   * **FIRE:** a one-sentence outcome and a success signal;
   * **WATER:** no second surface. That means one formula, one active configuration, and unchanged public Reader shapes;
   * **AIR:** contracts named and versioned (`config_id`, result schema, thresholds shape), with evolution reversible;
   * **EARTH:** it fails safely, is legible to a future reader, and captures what was learned.
4. **PF13's tenets** (§B):
   * **Single home per concept.** For example, a derived Type alongside the vendor's `type` field, or the governed direct motor-to-Throat set alongside the any-route predicate.
   * **Phase discipline and verification before scale.** Is there a verify step and success signal before release?
5. **Fit with the phase-named build checklists.** Where would v2's tasks belong: the Separation configuration contract, Conjunction integration, Distillation verification? Does the proposal place its impact there?

## 6. Findings and verdicts

**Each finding gives:**
* an ID (`R-01` onward);
* its dimension;
* its severity: **Blocker** (adoption would be wrong or unsafe), **Major** (must change before adoption), **Minor** (should change), or **Observation**;
* the evidence;
* a recommended fix;
* the Product Owner decision it bears on.

**Verdicts.**
* Per dimension: `SOUND`, `SOUND WITH CHANGES` or `UNSOUND`.
* Overall: `ACCEPT`, `ACCEPT WITH CHANGES` or `REJECT`, as a recommendation to the Product Owner, never an approval.

## 7. Deliverable

`docs/ephemeral/HDE-M10V2-mechanics-proposal-review-v1.0.md`, in one pull request, containing:
1. a summary, with the four verdicts and the overall verdict in the first lines;
2. the identity of what was reviewed (path, commit, SHA-256) and your session ID;
3. sections for correctness, feasibility and scope, and alchemical fidelity, as in §5, each with its checks and findings;
4. the findings table (§6);
5. your independent re-measurements, with the scripts and seeds you used, so they can be rerun;
6. the effect on each Product Owner decision in proposal §9;
7. limits, nonclaims, and a "Canon relied on" section.

## 8. Points raised before this review: test them, don't assume them

The brief's author read the proposal before writing this prompt and raised the points below. Do your own review first; then confirm or refute each, with evidence. They may be wrong.

1. **Reproducibility.** `hdmech.py` (Appendix C.3) hard-codes `REPO` to the author's own scratch path (`/tmp/claude-0/-home-user/5d854c62-…/scratchpad/hde/repo`), so the scripts do not run elsewhere as published.
2. **Circularity.** The 30/35/25/10 headline mix holds by construction on the fitting population. Only per-pair results, out-of-sample results and live pairs are informative.
3. **Constant offsets.** The Type component's 500 baseline at 15% weight adds about 7.5 points to every score. Some of "no zero scores" may come from constants rather than relational signal.
4. **Type fairness.** In the brief author's own rerun on the reference population:
   * pairs containing a Manifestor reached Glow on `harmony` 2.6% of the time, against 9.3% for Generators and 10.5% for Projectors;
   * Reflector person-pairs averaged 402 total points across the ten categories, against 446 overall.
   * `harmony` is the band Reader v1 shows.
5. **Population shift.** On the brief author's rerun, the frozen lines held on younger populations: births 1985 to 2005 gave 30.3 / 34.6 / 25.2 / 9.9, and 1995 to 2004 gave 30.6 / 34.5 / 25.2 / 9.7. This one is in the proposal's favour.
6. **Reproduction.** The same rerun reproduced the reference mix (29.8 / 34.9 / 25.4 / 10.0; the proposal states Warm 25.3) and the distinct-band distribution (0.1 / 7.4 / 48.2 / 44.3).
7. **Open PF09 work.** HDE-DIST008 (Partial) is a v1-specific verification task, and adopting v2 changes its target. The proposal's §7 and §8 do not mention it.
8. **Citations.** HDE Math Spec §5.2.7 and HDE Governance §4.1.5, both cited by the proposal, exist.

## Canon relied on (for this prompt)

Read on `main` at `0bf99656`:
* **HDE Math Spec:** §5.2.7 and §9.5 headings.
* **HDE Governance:** §4.1.5.
* **7 Phases of Alchemical Engineering (PF21):** overlay and all seven phases.
* **Glow Development Philosophy (PF13):** §B, §C, §D, §I.
* **HDE Build Checklist — Distillation:** Task HDE-DIST008 and Subtask HDE-DIST008.1.
* **HDE Build Checklists for Separation (HDE-SEPA005) and Conjunction (HDE-CONJ010):** by heading.
* **The design brief:** in full.
* **The proposal:** §1 to §10 in full, with Appendix C scripts extracted and hash-checked.

## Nonclaims

This prompt reviews nothing itself. It adopts nothing, and creates no change, CRD or release.
