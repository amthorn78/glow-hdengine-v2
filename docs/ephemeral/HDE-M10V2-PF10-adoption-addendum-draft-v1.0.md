---
artifact_type: PF10_ADDENDUM_DRAFT
artifact_id: HDE-M10V2-PF10-ADOPTION-ADDENDUM-DRAFT
artifact_version: "1.0"
subject: Draft HDE Build Notes addendum adopting the Magic10 v2 mechanics, for the next PF10 base version after v14.0.5, following addendum 2.1 (GATE:CORE-DET closed-rails evidence)
requested_by: Nathan / Product Owner, 2026-11-02 ("yes I will adopt. You can create a prompt that will go into the GTWPE flow for triage. it only needs the files you specified. The caveats and classifiers should be in source files, not prompt context")
author: Isis, Lead Developer (https://claude.ai/code/session_01Q789tyhUaytmY7x273kwes)
decision_owner: Product Owner
repository_head_read: origin/main 99f00c5c
numbering: 2.2 assumes addendum 2.1 (HDE-GTWPE-T05-ISIS-REVIEW v1.1) is the only addendum before it in the next base version; the publisher assigns the next continuous number if that differs
created_at: 2026-11-02T13:40:00Z
---

# Draft HDE Build Notes addendum: Magic10 v2 adoption

The text between the two rules below is the addendum, ready to paste into the next PF10 base version. It is self-contained. Its decision quotes are Nathan's words of 2026-11-02 in this session.

---

## 2.2 Magic10 v2 mechanics are adopted (relevant placement, center completion, pairwise aura-type compatibility, relative per-category bands), and every v2 statement drained before implementation carries [Required-When-Landed]

Timestamp: 110226 13:40 (UTC). Details:

* **What this records.** The Product Owner's adoption, on 2026-11-02, of the Magic10 v2 mechanics. The adopted design is the Magic10 v2 mechanics proposal v1.0, as amended by the Magic10 v2 open-questions resolution record v1.0. The decision also directs that permanent canon carry the adopted design now, marked as not yet implemented.
* **What this decides.**
  * R-1: the v2 formula.
  * R-2: the bands.
  * R-3: the values not yet set.
  * R-4: the status classifier for drained v2 content.
  * R-5: the contracts, retirements and single homes.
  * R-6: the implementing PF09 rows.
  * R-7: the disclosed effects and limits.

### Decision and approval status

* **Decision.**
  * Adoption: "yes I will adopt".
  * Canon now, marked unbuilt: "if we don't put this information in pfcanon now, it will be lost in the churn. Canon CAN describe unbuilt code … It just needs to be described as not yet implemented."
* **Status.** Proposed. R-1 to R-7 take effect as canon when this addendum is published in HDE Build Notes.
* **Implementation status.** Not started. No approved change owns the implementation, and no `config_id`, release or code exists for v2.
* **Relation to other canon.**
  * Magic10 v1 (`config_id` `m10-channel-state-v1.0.0`, `magic10_result.v1`, global inclusive maxima 24/49/74/100) remains the implemented, active mechanics until the v2 cutover release. This addendum does not change any v1 statement's status.
  * v2 replaces v1 only in that release. There is one active configuration, and rollback is the complete prior release.
  * The earlier exclusion of aura-diagnostic mechanics from Magic10 scoring does not apply to v2. Type enters v2 scoring, pairwise only (R-1).
  * Eligibility is unchanged: any Type combination remains eligible.

### R-1 — The v2 formula

**Inputs.**

* Exactly as v1: two eligible normalized gate masks. Nothing else from the stored chart is read, including the vendor `type`.
* Governed catalogs passed into Engine Core:
  * `catalog/gates_v1.json`, `catalog/channels_v1.json`, `catalog/magic10.json` and `catalog/magic10_caps.json`, unchanged;
  * a **centers catalog**: nine center IDs, each with a boolean `motor`. `sacral`, `solar_plexus`, `ego` and `root` are motors;
  * a **Type-pairing catalog**: the pair rules;
  * the **mechanics configuration v2**;
  * the **thresholds v2**.
* Complete-or-fail-closed closure, as in v1.

**Arithmetic.**

* All quantities are integers.
* `rhu(N, D) = floor((2N + D) / (2D))`, which is ROUND_HALF_UP for `N ≥ 0`, `D > 0`.
* Units:
  * signals and components are per-mille, `0..1000`;
  * responses are basis points, `0..10000`;
  * scores are points, `0..100`.
* No binary floating point anywhere.

**Evaluation order.**

1. Order the masks numerically as `member_lo`, `member_hi`.
2. Classify the 36 channels with the v1 five-state classifier: `none`, `companionship`, `dominance`, `compromise`, `electromagnetic`. `dominance` and `compromise` carry an owner.
3. For each member, compute:
   * its complete channels;
   * its defined centers, which are the centers of its complete channels;
   * its definition components;
   * `motor_to_throat`: a motor in the same component as `throat`, by any connected route;
   * its Type.
4. For the union mask, compute its defined centers and `motor_to_throat`.
5. Compute the center outcomes and the motor→Throat outcome.
6. Compute the twenty signals.
7. Compute the components `C_k`, `Z_k` and `T_k` for each category.
8. Compute the score. If `C_k = 0` and `Z_k = 0`, then `score_k = 0`. Otherwise `score_k = min(100, max(0, rhu(60·C_k + 25·Z_k + 15·T_k, 1000)))`.
9. Assign the band from that category's inclusive maxima (R-2).
10. Set `pair_key` under the v2 `config_id`.

**Type derivation, per member, from the gate set only.**

* No defined center → Reflector.
* `sacral` defined → Manifesting Generator if `motor_to_throat`, else Generator.
* Otherwise → Manifestor if `motor_to_throat`, else Projector.
* Aura classes: `generator` (Generator and Manifesting Generator), `projector`, `manifestor`, `reflector`.

**Center outcomes, per center `c`.** `D_lo` and `D_hi` are the members' defined centers, and `D_u` is the union's.

| Outcome | Condition |
| :- | :- |
| `open` | `c ∉ D_u` |
| `shared` | `c` is in both `D_lo` and `D_hi` |
| `one_sided` (owner `member_lo` or `member_hi`) | `c ∈ D_u`, and `c` is in exactly one of `D_lo`, `D_hi` |
| `mutual` | `c ∈ D_u`, and `c` is in neither `D_lo` nor `D_hi` |

* The motor→Throat outcome applies the same rule to the `motor_to_throat` predicate.
* `gives_lo` is the number of centers that are `one_sided(member_lo)` or `mutual`; `gives_hi` likewise.

**Signals.** The twenty signal IDs, their category pairs, the 18 ordinary channel maps and the response profiles are v1's.

* **Ordinary signals** use `saturating_state_sum_v2`.
  * `S = Σ w(c,s) · r(p_s, state_c)` in basis points.
  * `q_s = rhu(1000·S, S + 10000)`, and `0` when `S = 0`.
* **`equilibrium_score`** uses `bilateral_owner_mass_v2`, over all 36 channels with weight 1.
  * `m_lo` and `m_hi` count each member's owned `dominance` or `compromise` channels.
  * `q = rhu(1000 · 2·min(m_lo, m_hi), m_lo + m_hi)`, and `0` if both are `0`.
* **`counterweight_ratio`** uses `mutual_state_share_v2`, over all 36 channels with weight 1.
  * `F` is the number of channels not `none`, and `M` the number of `companionship` or `electromagnetic` channels.
  * `q = rhu(1000·M, F)`, and `0` if `F = 0`.

**Channel component.** `C_k = rhu(q_s1 + q_s2, 2)` over the category's two caps inputs.

**Center component.** The response profiles, in basis points:

| Profile | mutual | one_sided | shared | open |
| :- | -: | -: | -: | -: |
| `completion_bp_v2` | 10000 | 7500 | 2500 | 0 |
| `foundation_bp_v2` | 5000 | 7500 | 10000 | 0 |

The center map, where `motor_throat` reads the motor→Throat outcome:

| Category | Profile | Centers and weights |
| :- | :- | :- |
| harmony | completion | g 3, solar_plexus 2, spleen 1 |
| heat | completion | sacral 3, solar_plexus 2, ego 1, root 1, motor_throat 1 |
| communication | completion | throat 3, ajna 2, head 1 |
| alignment | foundation | g 3, ajna 1, ego 1 |
| comfort | completion | spleen 3, solar_plexus 2, g 1 |
| consistency | foundation | sacral 2, root 2, spleen 1 |
| expansion | completion | head 2, root 2, sacral 1 |
| creativity | completion | throat 2, head 2, g 1 |
| drive | completion | root 3, ego 2, sacral 1, motor_throat 2 |
| balance | `bilateral_completion_v2` | none |

* **Mapped categories:** `Z_k = rhu(1000·Σ weight·r(profile, outcome), 10000·Σ weight)`.
* **`balance`:** `Z = rhu(1000 · 2·min(gives_lo, gives_hi), gives_lo + gives_hi)`, and `0` if both are `0`.

**Type component, pairwise only.**

* `T_k = min(1000, max(0, 500 + Σ I_k[rule]))`, summed over the pair rules whose predicate holds.
* There is no per-person, per-class offset. Every rule depends on both members' classes.
* The six rules and their symmetric predicates:

| Rule | Predicate |
| :- | :- |
| `same_class` | both classes equal |
| `generator_with_nonsacral` | exactly one member is `generator` |
| `generator_manifestor` | the classes are {generator, manifestor} |
| `generator_projector` | the classes are {generator, projector} |
| `projector_manifestor` | the classes are {projector, manifestor} |
| `reflector_present` | a member is `reflector` |

* Their offsets are not yet set (R-3).
* Type moves a score by at most 15 points of 100.

**Determinism and neutrality.**

* AB↔BA: masks are ordered before every step, ownership is normalized, and every predicate is symmetric.
* Identity never enters, and the computation is integer only.
* Viewer preferences, presets and caller weights never enter `C`, `Z`, `T`, scores or bands; they remain sampler and ranker inputs.
* No hidden defaults: a missing center, class, weight, profile or line fails closed.

**Double counting.** `C` scores channel relevance and `Z` scores where the connection lands. On the synthetic reference population they correlate at 0.02 to 0.44, and `Z` changes 20% to 39% of bands. In `balance`, the two signals read owner mass and mutual share, and their correlation is −0.20. These are separate contributions, not one contribution counted twice.

### R-2 — Bands

* Bands are relative and per-category.
* Each category has its own inclusive maxima `[c1, c2, c3, 100]`, ascending and ending at 100. Each category set is the single band mapping for that category; it is not a preset.
* The target mix is 30 / 35 / 25 / 10 (Cool / Open / Warm / Glow).
* The maxima are cut from a governed synthetic reference population by a governed, repeatable tool that scores through `evaluate_pair` with the admitted release. The tool is Candidate CRD Items List item 13. Once cut, the maxima are frozen into the release as thresholds bytes.
* Changing them is a band change: new thresholds bytes, a new manifest cut and a new `release_id`. It is never a runtime adjustment.
* **Recalibration observation.**
  * What is measured: the realized band mix per category, over the stored real population, as aggregates only.
  * When it counts: once there are at least 400 stored real people.
  * The trigger: a band share in any category more than 5 points from the target is a recalibration case, decided by the Product Owner as a release.
* The v2.0 maxima are labelled "calibrated on the synthetic reference population".

### R-3 — Values not yet set

These are adopted as rules. Their values are not canon until set:

| Value | Rule that sets it | Set by |
| :- | :- | :- |
| Pair-rule offsets (R-1) | Each non-zero offset cites an admitted Human Design passage at its tier, and a rule with no admitted support has offset 0. The rejected alternatives are recorded | Magic10 v2 mechanics proposal v1.1 (HD Math Specialist) |
| Per-category inclusive maxima (R-2) | Target mix applied to the final formula on the governed reference population | The v2 release cut |
| Goldens M10-G001 to G008 (v2) | Computed from the final formula and maxima, and checked in both pair orders | The v2 change. M10-G001 (no channel, two Reflectors) is fixed now at 0 in every category, Cool |

### R-4 — Status classifier for drained v2 content

* **The tag.** Every v2 statement drained into permanent canon before the v2 cutover release carries `[Required-When-Landed]`. It means: adopted and binding as design; not yet implemented; it becomes `[Implemented]` only when its implementing PF09 row lands and the cutover release is admitted.
* **What the tag does not mean.** While a statement carries it, its absence from code is neither a defect nor a gap, and the statement is not evidence of implementation.
* **Implementing row.** Each tagged statement names its implementing PF09 row (R-6).
* **Tag definition in each target document.** A target document whose tagging convention lacks this tag gains its definition in that convention. This applies to HDE Math Spec §0.3, HDE Governance §0.3 and HDE CLI/API/Vendor Ref §0.3, and to the equivalent place in a target document that has no tagging convention.
* **v1 statements.** They keep their current status and text. v2 statements sit beside them and do not replace them before the cutover.
* **Why not the other tags.** v2 is not `[Speculative]`, because it is decided. It is not `[Required-Now]`, because that would make the implemented v1 a gap.

### R-5 — Contracts, retirements and single homes

All of these are `[Required-When-Landed]`, effective at the cutover release.

**Identities.**

* `config_id` `m10-relevance-centers-type-v2.0.0`.
* Schemas:
  * `magic10_mechanics_config.v2`;
  * `magic10_result.v2`;
  * `magic10_compat_result.v2`, where `q` widens from `0..200` to `0..1000`. This is an internal API contract change for `hdctl showcompat` stdout and `POST /api/compat/v1`.
* Cache key `magic10:v2:`.
* A new `release_id`, with manifest membership for every new member.

**Public Reader shapes are unchanged.** Reader v1 is one `{id, band}`, and Reader v2 is ten `{id, band}` in the governed order. Both are numeric-free.

**Configuration fields.**

* `signal_scale` 10.
* `response_scale` 10000.
* `rounding.signal` `round_half_up_to_per_mille`.
* `rounding.component` (new) `round_half_up_to_per_mille`.
* `rounding.category` `round_half_up_once`.
* The configuration adds `saturation_k_bp` 10000, `blend` 60/25/15, `center_profiles`, `center_map`, `sources.centers` and `sources.type_pairing`.

**Thresholds.** `math/thresholds.json` stays at its path, with `"version": "2"`, one maxima set per category, and a thresholds v2 schema.

**Loader rules.**

* Relaxed for v2:
  * no channel in both signals of one category;
  * one through six channels per Balance signal;
  * the `0..200` wire domain;
  * `edges == [24, 49, 74, 100]`.
* Added for v2:
  * center-map keys are the nine center IDs plus `motor_throat`, the one permitted non-center key;
  * weights are 1 to 3;
  * each profile has four outcome keys, with `open` 0;
  * the blend sums to 100;
  * `saturation_k_bp > 0`;
  * aura classes and pair-rule names are closed enums, and an unknown name fails closed;
  * each category's maxima are four ascending values ending at 100.

**Retirements and single homes.**

* **Motor→Throat.** The any-route `motor_to_throat` predicate is the only motor→Throat definition. The direct four-channel set (HDE Math Spec §5.4.2.1) and the §6.4 direct-MT flag are retired as governed inputs; neither has a scoring consumer.
* **Center tagging.** HDE Math Spec §6.3 center tagging is retired in favour of the four center outcomes. The owner of a `one_sided` outcome carries the actor indication.
* **Type.** The derived Type is the only scoring home for Type. The stored vendor `type` is non-scoring vendor metadata. Implementation QA compares derived and vendor Type on every vendor-backed chart, and any mismatch is a QA FAIL.
* **Evidence at the cut.**
  * Regenerated: the current evidence, namely the release-sanity stage 04 determinism outputs, the band-edge artifacts and the goldens.
  * Not regenerated: historical captures stay frozen.

### R-6 — Implementing PF09 rows

| Checklist | Row | Role |
| :- | :- | :- |
| HDE Build Checklist — Separation | A new task in the shape of HDE-SEPA005 | The v2 configuration contract: catalogs, schemas, fail-closed loader, identity |
| HDE Build Checklist — Conjunction | HDE-CONJ010.1 and .2 | Re-targeted from v1 to the v2 kernel and signal producers |
| HDE Build Checklist — Conjunction | HDE-CONJ010.5 | Unchanged in scope. The v2 Type component is derived from the gate set and never scores alone |
| HDE Build Checklist — Distillation | HDE-DIST008 and .1 to .3 | Re-targeted to v2 verification and the v2 release binding |
| HDE Build Checklist — Coagulation | HDE-COAG003.6 | The v1→v2 active-config cutover guard |
| HDE Build Checklist — Fermentation | A new deferred row | The R-2 recalibration observation |

### R-7 — Disclosed effects and limits

* **Reflector pairs.** Pairs containing a Reflector cannot reach Glow in `balance` or `consistency`, and almost never in `alignment`. These constructs score definition, and a Reflector defines no center. No Type-specific branch compensates for this. Reflectors are about 1.2% of the synthetic reference population.
* **Per-Type band effects** are re-measured on the final formula and recorded with the v2.0 maxima.
* **The pair rules are analyst inference** from admitted Human Design doctrine. No admitted source states a Type-pairing rule, matrix, valence or score.
* **Manifesting Generators** are paired as Generators. This is an inference: no admitted work names the Manifesting Generator aura.
* **Type never scores alone.** A category with no channel and no center contribution scores 0.
* **The maxima are calibrated on a synthetic population.** A real population will fall differently, and that is the R-2 recalibration case.
* **Bands describe composite Human Design mechanics** as Glow synthesizes them. They make no claim about relationship quality or outcomes.

### Scope, exclusions and nonclaims

* **Scope:** Magic10 v2 mechanics, bands, contracts, retirements, status classification and implementing rows.
* **Excluded:**
  * planetary activations as an input;
  * the public Reader shapes;
  * narrative keys and templates (the 360-row registry is unchanged);
  * conjunction mechanics;
  * implementing Candidate CRD Items List item 13, which stays a candidate.
* **Nonclaims.** This record:
  * implements nothing;
  * creates no release or `config_id`;
  * makes no QA verdict, acceptance, Ops result or PF09 movement;
  * drains no canon.

### Dependencies and unresolved obligations

* The offsets and maxima of R-3 depend on proposal v1.1 and the governed tool of R-2. *Type Sexual Signatures* (Ra Uru Hu, 2008) is to be acquired into the Human Design reference collection, and the pair rules are re-derived once it is admitted.
* No change is classified to implement v2.
* **Drainage targets.**
  * Permanent canon:
    * HDE Math Spec;
    * HDE Schemas & Artifacts;
    * HDE Governance;
    * HDE Mechanics Guide;
    * HDE CLI/API/Vendor Ref;
    * HDE Architecture;
    * Glow Infrastructure;
    * HDE Users Guide;
    * Glow QA Guide.
  * PF09 rows: HDE Build Checklist Separation, Conjunction, Distillation, Coagulation and Fermentation, for the R-6 rows.
  * The section map is in the resolution record, §5.

### Evidence

* `docs/ephemeral/HDE-M10V2-mechanics-proposal-v1.0.md` (SHA-256 `dc064a20…3c2a`): the formula, its measurements and the scripts.
* `docs/ephemeral/HDE-M10V2-mechanics-proposal-review-v1.0.md`: the independent review, ACCEPT WITH CHANGES, with every proposal number reproduced.
* `docs/ephemeral/HDE-M10V2-open-questions-resolution-and-drain-targets-v1.0.md` (SHA-256 `e51d14b2…dfbd5`): the amendments and the drain section map.
* `docs/ephemeral/HDE-M10V2-hd-math-specialist-design-brief-v1.0.md`: the design brief.

---
