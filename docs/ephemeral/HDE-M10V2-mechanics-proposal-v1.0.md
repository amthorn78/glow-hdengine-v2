---
artifact_type: MECHANICS_PROPOSAL
artifact_version: "1.0"
logical_id: HDE-M10V2-MECHANICS-PROPOSAL
title: "Magic10 v2 mechanics proposal: relevant placement, center completion and aura-type pairing"
status: "PROPOSAL for independent review and Product Owner decision. Adopts nothing. Changes no canon, code, catalog, test or data."
brief: "docs/ephemeral/HDE-M10V2-hd-math-specialist-design-brief-v1.0.md (accepted by the Product Owner on 2026-11-01 by directing this run)"
role: "Human Design Math Specialist, as defined in the brief §2"
requested_by: "Nathan (Product Owner), 2026-11-01"
change_id: "None. The Product Owner assigns the change (CRD or Epic) that would carry an adopted design into canon and code."
repository_head_read: "amthorn78/glow-hdengine-v2 origin/main e2b7427f (HDE Build Notes v14.0.5; release 1.3.0, release_id 77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e); amthorn78/glow-docs edaa34c (docs/hd_refs, Human Design Reference Index v1.2.0)"
rails: "closed (LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev) for every engine run; no vendor call, no network to any product system, no database. Outside-source search for aura doctrine and mathematics only, as the brief §2.4 permits."
recorded: "2026-11-01T23:59Z"
producer: "Human Design Math Specialist session (https://claude.ai/code/session_01Q789tzD1cBKzL7p4Cec46s)"
---

# Magic10 v2 mechanics proposal (v1.0)

## 1. Summary

**What changes.** Magic10 v1 scores each category as the mean of channel-state responses over a fixed list of four to six channels. Because a random pair forms about 10 of the 36 channels, every channel it does not form counts 0, and scores pile up below 25. Magic10 v2 keeps the proven frame (two gate masks in, ten integer scores and bands out, deterministic, AB↔BA neutral, integer only) and changes what is measured:

1. **Relevant placement (D-1).** The relevance maps stay (each channel still feeds the categories it is relevant to), but the aggregation changes from a coverage mean to a **saturating accumulation**: a signal rises with what the pair does form and is no longer divided by what it does not. Where a connection lands is scored by a second feature, the centers.
2. **Center completion (D-2).** The composite's nine centers are classified as `open`, `shared`, `one_sided` (one person's definition conditions the other's openness) or `mutual` (defined only together). A **motor→Throat completion** feature is added. Each category reads a small weighted set of centers.
3. **Aura-type compatibility (D-3).** Each person's Type is **derived from the gate set** (Sacral definition, a motor reaching the Throat, any definition at all). Pairs of aura classes carry a bounded integer contribution per category. The contribution is at most 15 points of 100, measured at 0.4% to 7.6% of score variance.
4. **Relative bands (D-4).** Band lines are placed where pairs actually fall, **per category**, frozen into the release from a named reference population. Global lines were measured and rejected (§4.3).
5. **Reader v2 differentiates (D-5)** and **scores rank (D-6)**: no zero scores remain; 66 to 80 distinct score values per category; tie probability falls from 4% to 30% down to 2% to 3%.

**Why.** The Product Owner's direction (brief §3): relevant placement rather than "most channels connect", center completion, and aura-type compatibility; a multiband Reader v2 that works. Every Human Design rule below is cited and labelled; every number is populated; the whole formula was run on the validated 20,000-pair harness.

**Before and after** (same 2,000 synthetic people and 20,000 pairs as `HDE-EPIC041-POSTCLOSE-compat-score-range-v1.0.md`, seed `20261101`; v2 measured under the recommended per-category lines of §4):

| Measure (brief §4.3) | v1 (measured, reproduces the record) | v2 candidate |
| :- | :- | :- |
| Band mix, all 200,000 category results | Cool 78.5%, Open 21.0%, Warm 0.43%, Glow 0.0015% | Cool 29.8%, Open 34.9%, Warm 25.3%, Glow 10.0% |
| `harmony` band, what Reader v1 shows | Cool 81.6%, Open 18.2%, Warm 0.1%, Glow 0 | Cool 28.9%, Open 36.4%, Warm 25.6%, Glow 9.1% |
| Reader v2 pairs showing one band only | 19.3% | 0.1% |
| Reader v2 pairs showing exactly two bands | 76.9% (Cool and Open) | 7.4% |
| Reader v2 pairs showing three or more bands | 3.9% | 92.5% (three: 48.2%; all four: 44.3%) |
| Pairs with any Glow | 3 of 20,000 | 55.9% |
| Category score percentiles | all: p50 15, p90 30, p99 44 | per category: p50 39 to 59, p90 54 to 72, p99 62 to 81 |
| Scores of 0 | 2.5% to 8.0% per category; `balance` 41.8% | 0.0% in every category |
| Distinct score values per category | 8 (`balance`) to 60 | 66 to 80 |
| Tie probability (two random pairs share a category score) | 4.3% to 9.5%; `balance` 30.0% | 2.3% to 2.9% |
| Warm and Glow narrative templates reached (half the 360-template pack) | 0.43% of results | 35.3% of results |
| Live pair P1 (SYN-A with SYN-B) | 6 Cool, 4 Open | 4 Open, 4 Warm, 2 Glow |
| Live pair P2 | 9 Cool, 1 Open | 6 Cool, 2 Open, 2 Glow |
| AB↔BA identity, two-run identity | hold | hold (sha256 of all 200,000 scores identical across the forward run, the reversed run and the second run: `9ec56f0425e03eff6154501362921f6c89bb2cbe3501b503cc1d5516f699cb53`) |

**Rank agreement with v1.** Spearman correlation between v1 and v2 category scores is 0.82 to 0.91 for nine categories, so v2 keeps the ordering information v1 carried while spreading it. `balance` is 0.10: its v1 operations were 0 for most pairs and are redefined (§3.5).

## 2. Definitions and grounding

Every rule carries a claim status from the Human Design Reference Index §10: **source doctrine** (an admitted A2 or A3 source says it), **secondary interpretation** (an admitted A4 or A5 source says it; used only to corroborate), **outside source** (brief §2.4 route 1), or **analyst inference** (brief §2.4 route 2; Glow product synthesis, not Human Design doctrine). Product choices are marked **product choice**. The full citation register, with locators, is Appendix B.

### 2.1 Composite connection (D-1 grounding)

* **Doctrine.** "When you take the Body Graph of two individuals and you superimpose them over each other, where they connect, is revealed … How you connect and where you connect determines the nature of the relationship." (PF08, "The Rave Charts", Composite Rave passage; **source doctrine**.)
* **Doctrine.** "Imagine our example of Johannes. If there is a female in his life who connects his Solar Plexus Center, the basis of the relationship for Johannes will be emotional. How we connect determines the quality and feel of our relationships." (PF08, same passage; **source doctrine**.)
* **Doctrine.** A center is defined when "two centers are permanently connected by design from birth"; "Definition means the continual transfer of energy between two centers." (PF08, "Transfer to the Body Graph", Johannes analysis; **source doctrine**.)
* **Doctrine.** "What is defined in us is our foundation. What is not defined, what is receptive is how we connect to the world. It is what changes us." (PF08, same section; **source doctrine**.)
* **Product choice (retained from v1).** The five channel states and which channels are relevant to which category are v1's Glow-authored synthesis (HDE Math Spec §5.2.3, §5.2.4; "Human Design doctrine supports distinguishing the five states but does not supply these fractions"). v2 retains the 36-channel topology, the five states, the three response profiles and the 18 ordinary channel maps unchanged. Appendix A gives each channel's PF08 keynote beside the signals it feeds.
* **Product choice (new).** Aggregation by saturating accumulation. The mathematics is the hyperbolic saturation `x / (x + K)`, with `K` the half-saturation constant (outside source for mathematics, Appendix B, M-1). Doctrine does not supply `K`; it is a Glow value.

### 2.2 Center completion (D-2 grounding)

* **Doctrine, composite defines centers.** Johannes and Renate: "Alone, she had mental activity without [relevance], and he, mental activity without clarity; together, in each other's aura … this system is complete and defined." (PF08, "Head–Ajna Complementarity (with Johannes)"; **source doctrine**.) This is the `mutual` outcome: a center neither person defines alone, defined together.
* **Doctrine, one-sided completion.** "Most important for Johannes, together he has an emotional base. Together they connect and define the Heart to the Solar Plexus center." (PF08, same section; **source doctrine**.) Renate's defined Heart (21-45) meets Johannes's open emotional center through 37-40. This is the `one_sided` outcome: one person's definition conditions the other's openness.
* **Doctrine, the caution.** "If this type of design connects with a defined Splenic center, the immediate result is that this person is going to make them feel better. It is possible in this situation that the feeling better is the only beneficial connection." (PF08, Composite Rave passage; **source doctrine**.) v2 treats completion as salient, not as a verdict, and makes no relationship-quality claim.
* **Doctrine, undefined centers are where connection happens.** "An undefined center is always vulnerable. It is where our life changes." (PF08, "RAVE — Channel and Definition Analysis Graph"; **source doctrine**.) "Think about your own design and understand what you do to other people, what you do when you step into their aura, what you fill up what they may have open." (Complete Guide, Part Seven, printed p. 111; **source doctrine**.)
* **Doctrine, center keynotes** used to decide which centers are relevant to which category: Head "Inspiration, initiation"; Ajna "Knowing, intuition and understanding"; Throat "Action, metamorphosis"; Heart "Ego, zeal and passion"; Spleen "Balance, judgment and cleansing"; Sacral "Maturation, reproduction and sexuality"; Solar Plexus "Aspiration, sensitivity and emotion"; Root "Assertion, energy and evolution"; G "Spirituality, gravity, attraction and love" (PF08, "The Centers"; **source doctrine**). The Complete Guide adds: the Spleen "gives us a sense of security in this life … makes us feel good" (Part Seven, p. 106); the open G Center is "desperate for … love, direction" (p. 102); the Throat has "11 ways that we speak" (p. 101); the Heart Center carries "this deep desperateness to try to prove yourself" (p. 102) (**source doctrine**).
* **Doctrine, motors and the Throat.** "The Solar Plexus is a motor … The Spleen is not a motor. The Ajna is not a motor." (Complete Guide, Part Seven, p. 108.) "The Root Center is a pressure center like the Head Center." (p. 105.) "The Generator is a prime motor" (Generators' Course, segment 1); "the 45th Gate … points directly down to the 21st Gate, to the Ego Center, to a Motor" (segment 76). The Root as a power source that, bridged to the Throat, "would immediately turn this Projector into a Manifestor" (Complete Guide, Part Fifteen, p. 232). (All **source doctrine**.) The four motors are therefore Sacral, Solar Plexus, Heart/Ego and Root; the A5 secondary source lists exactly these four ("The Four Motors", Winn, *Understanding the Centers*; **secondary interpretation**, corroborating).
* **Doctrine, manifesting.** "If you're looking at the 35 - 36, direct connection of the Throat to the Solar Plexus, this is a Gate that has direct access to manifesting. If you're looking at the 12th, going down to the 22, again, you've got a Gate directly connected to a Motor … direct manifesting potential." (Generators' Course, segment 76; **source doctrine**.) The canon-governed Direct Motor→Throat set `12-22`, `20-34`, `21-45`, `35-36` (HDE Math Spec §5.4.2.1) is the direct case of this.
* **Product choice.** Which centers feed which category, their weights, the two center response profiles, and the completion ordering `mutual > one_sided > shared` for connection categories and `shared > one_sided > mutual` for foundation categories (§3.6). The ordering follows the doctrine above (PF08: definition is foundation and consistency; openness is where connection and change happen) but the numbers are Glow's.

### 2.3 Type derivation (D-3 grounding)

* **Doctrine.** "The moment you see an undefined Sacral Center right away you know that you're dealing with either a Manifestor or Projector or a Reflector." (Complete Guide, Part Fifteen, "The Undefined Sacral Center: A Projector", p. 229; **source doctrine**.) "Manifestors and Projectors and Reflectors are non-Sacral beings; three types that are non-Sacral beings." (Part Seven, p. 103.) "Only Generators have a defined Sacral Center." (Generators' Course, segment 1.)
* **Doctrine, Manifesting Generator is a Generator.** "I was told that there were only four kinds of beings, and there are only four kinds of beings. There are two kinds of Generators. But Generators are Generators are Generators. The reality is that anyone who has a defined Sacral Center, that their Strategy is the same." (Generators' Course, segment 15, "MANIFESTING GENERATOR: MORE EASILY SEDUCED TO MANIFEST"; **source doctrine**.) "One third of humanity are Manifesting Generators." (same.)
* **Doctrine, a motor reaching the Throat.** A definition bridging a power source to the Throat "would immediately turn this Projector into a Manifestor … The bridge is something—a gate or a channel—that will bring the two areas of definition together." (Complete Guide, Part Fifteen, p. 232; **source doctrine**.) The bridge in that example runs Root → Spleen → G → Throat, so the route is any connected definition, not only a direct channel. Winn's A5 table states the same mechanics for all five Types ("Have a defined Sacral Center and a motor to the throat" for Manifesting Generator; "an open Sacral Center and a motor to the throat" for Manifestor; "an open Sacral Center and no motor to the throat" for Projector; "no centers defined" for Reflector; *Understanding Your Clients*, segments 58 to 59; **secondary interpretation**, corroborating). Reflectors are "deeply, deeply, deeply open" (Complete Guide, Part Eight, p. 122; **source doctrine**).
* **Validation of the derivation (§3.4).** Every vendor-backed chart in the repository that carries a Type matches: three HumanDesignAPI v2 payloads (`fixtures/hdapi/normalized/`, a Projector with single definition, a Projector with split definition, a Manifestor with triple split) match on Type, on the full set of defined centers and on the number of definition components; the two vendor-shaped charts in `fixtures/charts/alice.json` and `tests/fixtures/bodygraph/source_invariance/` match (both Manifesting Generator). Over the 2,000 synthetic people the derived shares are Generator 38.7%, Manifesting Generator 33.0%, Projector 19.8%, Manifestor 7.3%, Reflector 1.2%, Solar Plexus defined 51.0%; doctrine gives two-thirds Generators (71.7% here), one third Manifesting Generators (33.0%), 1.4% Reflectors (Complete Guide p. 122) and 51% emotional (p. 108). Under a direct-only motor→Throat rule, 214 of the 2,000 people would change Type (187 Manifesting Generator → Generator, 27 Manifestor → Projector) and the shares would leave doctrine, so v2 uses any connected route.

### 2.4 Aura-type pairing (D-3 grounding, the gap, and the route taken)

* **Doctrine, each Type's aura.** "I happen to be a Manifestor, I have a closed aura. It makes it very, very difficult for people to approach me. As a matter of fact, it has a pushing off quality … there seems to be a barrier between them and others. The majority of humanity, Generators … They have an enveloping aura. They take everything into their aura. It's an open aura and brings everything inward. When you come to the Projector the Projector has a focused aura. They focus directly on the other. It is a very penetrating aura. Projectors come into the world with a gift of being able to recognize and the yearning to be recognized." (Complete Guide, Part Fifteen, p. 230; **source doctrine**.) "Whether you're a Manifestor like me with a closed aura, or you're a Generator with this huge enveloping aura … whether you're a Reflector sampling or whether you're a Projector focused" (Holistic Analysis Fundamentals, segment 117; **source doctrine**). "The Projector aura is a deeply penetrating aura. And the Projector came into the world to guide us" (same, segment 28).
* **Doctrine, how a Sacral meets an open Sacral.** "Think about that Projector with that open Sacral Center being conditioned by the Generator. And remember what happens when you meet them in the aura, you're taking that energy into that center; this is an amplification of that energy. That juiced up Projector now does not know when enough is enough." (Complete Guide, Part Seven, p. 104; **source doctrine**.) "Most Projectors would rather be a Generator; it's a natural relationship between the two." (Part Fifteen, p. 235.) The Projector "is a non-energy type and is going to be very dependent" (p. 229).
* **Doctrine, Generators under Manifestor conditioning.** "The Manifesting Generators have been the most deeply conditioned by Manifestor propaganda." (Generators' Course, segment 15.) "All other types are not born to work - they are born to find life." (segment 1.)
* **The gap.** No admitted source states a rule for how two Types combine in a relationship. The Reference Index records this: "Relationship/composite teaching is partial: PF08 examples and advanced Design Resonance do not establish a general compatibility score" (§9). Body-to-other resonance (HD-SYN-02, route M15) "establishes no app compatibility score" and is not used.
* **Route 1, outside sources (searched 2026-11-01, Appendix B, O-1 to O-3).** A web search for Ra Uru Hu, IHDS or Jovian Archive material on Type pairings found: a Jovian Archive product page for Ra Uru Hu's lecture *Type Sexual Signatures* (Ibiza, 2008), which describes "honoring our Aura Type" as the key to correct interaction but publishes no passage; and a 2025 blog series ("Human Design Academy by Ra Uru Hu", *Understanding Our Design in Relationships*) that says it is "based on" a 1998 recording, is not a transcript, and cannot be verified as Ra's text. Under the brief §2.4 an outside source needs title, author, publisher, edition and the exact passage relied on; the blog cannot supply that provenance, so **no outside source is relied on for any rule**. Its statements are recorded in Appendix B for the reviewer and are consistent with, but not the basis of, the inferences below. **Recommendation (Q-3):** acquire *Type Sexual Signatures* (Jovian Archive, Ra Uru Hu, 2008) into `docs/hd_refs/` as a direct source on Type in relationship; it is the one primary work the search surfaced.
* **Route 2, analyst inference.** The pairing contribution is built from the cited aura mechanics by six stated principles (§3.7). Each is **analyst inference**, Glow product synthesis, labelled as such, bounded to at most 15 points of 100, and listed together in §2.6 for review.

### 2.5 Bands (D-4 grounding)

* **Product canon.** Bands are "the user-visible signal"; narratives are chosen by "category + band + perspective" and are "the primary outcome users read"; admins "tune numbers → bands without rewriting copy" (Glow Story). Scores rank candidates. These are **product choices**, not doctrine; Human Design supplies no band.
* **Mathematics (outside source, M-2).** Placing lines at population quantiles is sample-quantile calibration; the integer-score tie handling in §4.2 follows the rounding family of definitions in Hyndman and Fan (1996).

### 2.6 Consolidated list of rules that are not admitted doctrine

For the independent review and the Product Owner (brief §7.2). Everything else in §2 is cited admitted doctrine or a retained v1 product choice.

| ID | Rule | Status |
| :- | :- | :- |
| I-1 | Saturating accumulation `x/(x+K)` with `K = 10000` basis points (one full-response channel-equivalent) replaces the coverage mean | product choice; mathematics from outside source M-1 |
| I-2 | Center response profiles: `completion_bp_v2` (mutual 10000, one_sided 7500, shared 2500, open 0) and `foundation_bp_v2` (shared 10000, one_sided 7500, mutual 5000, open 0) | product choice ordered by PF08 doctrine (§2.2) |
| I-3 | Center-to-category map and weights (§3.6) | product choice from PF08 and Complete Guide keynotes (§2.2) |
| I-4 | Motor→Throat completion feeds `heat` (weight 1) and `drive` (weight 2) | product choice from Generators' Course segment 76 |
| I-5 | Type is derived with any connected definition route from a motor to the Throat | source doctrine (Complete Guide p. 232) corroborated by A5; validated §2.3 |
| I-6 | Manifesting Generator shares the Generator aura class for pairing | source doctrine (Generators' Course segment 15: "two kinds of Generators"); Complete Guide p. 230 describes one Generator aura |
| I-7 | Per-Type category offsets `A` (§3.7, Table 7a) | analyst inference from the aura and energy doctrine in §2.4 |
| I-8 | Pair interaction rules `I` (§3.7, Table 7b) | analyst inference from §2.4 |
| I-9 | Blend 60 / 25 / 15 (channel / center / Type) | product choice; Type bounded to 15 points |
| I-10 | `balance` operations over all 36 channels and the bilateral-completion operation | product choice; doctrine basis is PF08's "how we connect" in both directions |
| I-11 | Relative, per-category band lines at target shares 30 / 35 / 25 / 10 from the named reference population | product choice; mathematics from outside source M-2 |

## 3. The complete formula

### 3.1 Inputs and closure

* **Inputs.** Exactly as v1: two eligible normalized gate masks (HDE Math Spec §5.2.1). Nothing else from the stored chart is read; the vendor `type` field is not an input.
* **Governed catalogs** (all passed into Engine Core as normalized inputs; HDE Schemas & Artifacts owns paths and schemas, §7 names what is needed):
  * `catalog/gates_v1.json` and `catalog/channels_v1.json`, unchanged;
  * **centers catalog** (new): the nine center IDs with one boolean `motor`; `sacral`, `solar_plexus`, `ego`, `root` are `true`, the other five `false`;
  * **mechanics configuration v2** (new `config_id = "m10-relevance-centers-type-v2.0.0"`, schema `magic10_mechanics_config.v2`): profiles, 20 signal rows, category input weights, saturation constant, center profiles, center map, blend;
  * **Type pairing catalog** (new): the `A` table and the `I` rules of §3.7;
  * `catalog/magic10.json` and `catalog/magic10_caps.json`, unchanged (ten categories, twenty signal IDs, bounds 0 to 100);
  * **thresholds v2**: inclusive maxima per category (§4).
* **Closure.** Complete-or-fail-closed exactly as §5.2.1 and §5.2.7: every gate resolves once, every channel once, every center once, every Type class once, every category has three populated components.

### 3.2 Integer arithmetic

All quantities are integers. `rhu(N, D) = floor((2N + D) / (2D))` is `ROUND_HALF_UP(N / D)` for `N ≥ 0`, `D > 0`. Signals and components are in **per-mille units** (`0..1000`); responses are in **basis points** (`0..10000`); scores are in points (`0..100`). No binary floating point anywhere.

### 3.3 Evaluation order (one declared order)

1. Order the two masks numerically as `member_lo`, `member_hi`. Equal masks remain two equal members.
2. Classify the 36 channels with the §6.1 five-state classifier (unchanged): `none`, `companionship`, `dominance`, `compromise`, `electromagnetic`, with the owner for `dominance` and `compromise`.
3. For each member alone: its complete channels (both gates present), its defined centers (centers of its complete channels), its definition components (centers joined by its complete channels), `motor_to_throat` (a motor center in the same component as `throat`), and its Type (§3.4).
4. For the union mask (both gate sets together): its defined centers and `motor_to_throat`.
5. Center outcomes and the motor→Throat outcome (§3.5).
6. Twenty signals in per-mille (§3.5).
7. Per category: channel component `C_k`, center component `Z_k`, Type component `T_k` (§3.6, §3.7).
8. Per category: `score_k = min(100, max(0, rhu(60·C_k + 25·Z_k + 15·T_k, 1000)))`.
9. Per category: band from that category's inclusive maxima (§4), monotone, no score mutation.
10. `pair_key` as §5.2.2 with the new `config_id`; result schema `magic10_result.v2` (same shape as v1 plus nothing public).

### 3.4 Type derivation (per member, from the gate set only)

```text
defined   = centers touched by the member's complete channels
if defined is empty:                      Type = Reflector
elif sacral in defined:
    Type = Manifesting Generator if motor_to_throat else Generator
else:
    Type = Manifestor if motor_to_throat else Projector

motor_to_throat = some definition component contains throat and at least one of
                  {sacral, solar_plexus, ego, root}
aura_class      = generator (Generator, Manifesting Generator) | projector | manifestor | reflector
```

### 3.5 Pair features

**Center outcomes.** For each center `c`, with `D_lo`, `D_hi` the members' defined centers and `D_u` the union's:

| Outcome | Condition | Meaning |
| :- | :- | :- |
| `open` | `c ∉ D_u` | undefined in the composite |
| `shared` | `c ∈ D_lo` and `c ∈ D_hi` | both define it alone |
| `one_sided` (owner `member_lo` or `member_hi`) | `c ∈ D_u`, in exactly one of `D_lo`, `D_hi` | one person's definition conditions the other's openness |
| `mutual` | `c ∈ D_u`, in neither | defined only together (electromagnetic completion) |

**Motor→Throat outcome.** `open`, `shared`, `one_sided`, `mutual` by the same rule applied to the `motor_to_throat` predicate of `member_lo`, `member_hi` and the union.

**Completions given.** `gives_lo` = number of centers that are `one_sided(member_lo)` or `mutual`; `gives_hi` likewise for `member_hi`.

**Signals.** The twenty signal IDs, their category pairs and the 18 ordinary channel maps and profiles are exactly v1's (HDE Math Spec §5.2.4; reproduced in Appendix A). Only the operations change.

* Ordinary signal `s` (`weighted_state_sum_v1` map, v2 operation `saturating_state_sum_v2`): `S = Σ w(c,s) · r(p_s, state_c)` over its channels, in basis points; `q_s = rhu(1000·S, S + K)` with `K = 10000`; `q_s = 0` when `S = 0`. One full-response channel gives 500; two give 667; three give 750; five give 833. All `none` gives 0.
* `equilibrium_score` (v2 operation `bilateral_owner_mass_v2`, over all 36 channels, weights 1): `m_lo`, `m_hi` = count of `dominance` or `compromise` channels owned by each member; `W = m_lo + m_hi`; `q = rhu(1000 · 2·min(m_lo, m_hi), W)`, `0` if `W = 0`.
* `counterweight_ratio` (v2 operation `mutual_state_share_v2`, over all 36 channels, weights 1): `F` = count of channels not `none`; `M` = count of `companionship` or `electromagnetic`; `q = rhu(1000·M, F)`, `0` if `F = 0`.

Response profiles (unchanged values, HDE Math Spec §5.2.3): `coherence_bp_v1` none 0, companionship 10000, dominance 5000, compromise 2500, electromagnetic 7500; `activation_bp_v1` 0, 5000, 7500, 2500, 10000; `expression_bp_v1` 0, 7500, 5000, 2500, 10000.

### 3.6 Channel and center components

**Channel component.** For category `k` with caps inputs `(s1, s2)` and input weights `(b1, b2) = (1, 1)`: `C_k = rhu(b1·q_s1 + b2·q_s2, b1 + b2)`.

**Center component.** Response profiles in basis points:

| Profile | mutual | one_sided | shared | open |
| :- | -: | -: | -: | -: |
| `completion_bp_v2` | 10000 | 7500 | 2500 | 0 |
| `foundation_bp_v2` | 5000 | 7500 | 10000 | 0 |

Center map (`motor_throat` is read from the motor→Throat outcome):

| Category | Profile | Centers and weights | Grounding (§2.2) |
| :- | :- | :- | :- |
| harmony | completion | g 3, solar_plexus 2, spleen 1 | G: attraction, love; Solar Plexus: emotion; Spleen: "make you feel better" |
| heat | completion | sacral 3, solar_plexus 2, ego 1, root 1, motor_throat 1 | Sacral: sexuality; Solar Plexus: emotion; Heart: zeal, passion; Root: energy; manifesting |
| communication | completion | throat 3, ajna 2, head 1 | Throat: "11 ways that we speak"; Ajna: understanding; Head: inspiration |
| alignment | foundation | g 3, ajna 1, ego 1 | G: direction; Ajna: understanding; Heart: will |
| comfort | completion | spleen 3, solar_plexus 2, g 1 | Spleen: security, "feel good"; Solar Plexus: sensitivity; G: love |
| consistency | foundation | sacral 2, root 2, spleen 1 | Sacral: sustained motor; Root: energy; Spleen: judgment |
| expansion | completion | head 2, root 2, sacral 1 | Head: inspiration; Root: evolution; Sacral: maturation |
| creativity | completion | throat 2, head 2, g 1 | Throat: metamorphosis; Head: inspiration; G: identity |
| drive | completion | root 3, ego 2, sacral 1, motor_throat 2 | Root: assertion, energy; Heart: ego; Sacral: motor; manifesting |
| balance | `bilateral_completion_v2` | none | both directions of "how we connect" |

For a mapped category: `W = Σ weights`; `N = Σ weight · r(profile, outcome)`; `Z_k = rhu(1000·N, 10000·W)`. For `balance`: `Z = rhu(1000 · 2·min(gives_lo, gives_hi), gives_lo + gives_hi)`, `0` if both are `0`.

### 3.7 Type component

`T_k = min(1000, max(0, 500 + A_k[class_lo] + A_k[class_hi] + Σ I_k[rule]))` over the rules whose predicate holds.

**Table 7a, per-class offsets `A` (per mille).** Analyst inference, each row tied to §2.4.

| Class | harmony | heat | communication | alignment | comfort | consistency | expansion | creativity | drive | balance | Basis |
| :- | -: | -: | -: | -: | -: | -: | -: | -: | -: | -: | :- |
| generator | +50 | +50 | 0 | 0 | +50 | +200 | −50 | 0 | +150 | +50 | enveloping, open aura that takes in; the sustained Sacral motor; responds rather than initiates |
| projector | +50 | −150 | +200 | +150 | 0 | −150 | −50 | +50 | −200 | +50 | focused, penetrating aura; recognizes and guides; non-energy, dependent on connection |
| manifestor | −200 | +150 | −150 | −50 | −200 | −50 | +200 | +100 | +250 | −100 | closed aura with a pushing-off quality, a barrier; a motor to the Throat; initiates |
| reflector | 0 | −200 | 0 | −50 | 0 | −200 | −100 | −50 | −250 | +100 | sampling aura, deeply open; no fixed definition; mirrors |

**Table 7b, pair interaction rules `I` (per mille).**

| Rule | Predicate | Offsets | Basis |
| :- | :- | :- | :- |
| same_class | both classes equal | alignment +50 | like auras meet alike |
| generator_with_nonsacral | exactly one member is generator | heat +100, comfort −50 | Sacral energy amplified in the open Sacral: "never knowing when enough is enough" (Complete Guide p. 104) |
| generator_manifestor | classes are {generator, manifestor} | harmony −50, drive +50 | Generators "most deeply conditioned by Manifestor propaganda" (Generators' Course seg. 15); Manifestor initiates, Generator responds |
| generator_projector | classes are {generator, projector} | alignment +100, communication +50 | "a natural relationship between the two" (Complete Guide p. 235); the Projector recognizes, the Generator supplies energy |
| projector_manifestor | classes are {projector, manifestor} | harmony −50, alignment −50 | focused aura meets a closed, repelling one; recognition meets the barrier |
| reflector_present | a member is reflector | balance +50 | the sampling aura reflects the other |

**Limits of Type (Q-4).** `T` spans the full 0 to 1000 only in `drive`; the other categories realise ranges from 400 to 700 (creativity) up to 100 to 900 (consistency), and the largest possible score swing is `0.015 × (max − min)`: 4.5 points (creativity) to 15.0 points (drive). Measured share of score variance explained by `T`: 0.4% to 7.6% (consistency 6.4%, drive 7.6%, all others at or below 3.2%); the channel component explains 40% to 82% and the center component 9% to 31%. Type never drowns out the chart-specific mechanics.

### 3.8 Determinism and neutrality

* AB↔BA: masks are ordered numerically before every step; ownership is normalized to `member_lo`/`member_hi`; `A` is symmetric by construction and every `I` predicate is symmetric. Verified on 20,000 pairs reversed (§5.6).
* Identity never enters: nothing but the two masks and the governed catalogs is read.
* Equal masks: all channels `companionship` or `none`; all centers `shared` or `open`; `gives_lo = gives_hi = 0`; both Types equal.
* Integer only, `ROUND_HALF_UP` at the declared stages (signal, channel component, center component, score), one defensive clamp.
* No hidden defaults: a missing center, class, weight, profile or line fails closed.

## 4. Band design

### 4.1 Absolute or relative (Q-5)

**Recommendation: relative, frozen.** v1's absolute lines on v2 scores still do not use the four bands: under 24/49/74 the v2 mix would be Cool 1% to 11%, Open 24% to 73%, Warm 19% to 70%, Glow 0% to 5% by category (§5.3). Any usable line set has to be chosen from where pairs fall; choosing it once from a named population and freezing it into the release is that, done honestly. A pair's band still depends only on its two charts, the lines are governed catalog bytes, so determinism, AB↔BA identity and the numeric-free covenant are unchanged.

### 4.2 Method

* **Reference population.** The 2,000 synthetic people of the score-range record (seed `20261101`, births uniform over 1950-01-01 to 2005-12-31 UTC, charts by the validated `hdchart.py` with the mean node) and its 20,000 distinct random pairs.
* **Target mix.** For each category the three inclusive maxima are the integer scores whose cumulative shares are closest to the target cumulative shares (30%, 65%, 90% for the recommended mix), chosen in increasing order; the fourth maximum is 100. Integer scores tie, so realised shares deviate by up to about one point.
* **Recalibration rule.** The lines are governed bytes in the thresholds artifact; changing them is a band change under HDE Math Spec §5.2.8 and §5.3.5: new thresholds bytes, new manifest cut, new `release_id`, review of the public contract. Recalibrating on a real population is a Product Owner decision taken as a release, never a runtime adjustment.

### 4.3 Global or per-category (Q-5)

**Recommendation: per-category.** With one global set fitted to the pooled v2 scores for the recommended target (maxima 37, 49, 61), the realised category mixes diverge: `balance` would be Glow 41.9% and Cool 7.7%; `consistency` Glow 18.5%; `harmony` Glow 1.2%; `comfort` Glow 1.1%; `expansion` Cool 44.5%. That recreates v1's problem (categories stuck in one or two bands) in a new place. Per-category lines give every category 29% to 31% Cool, 34% to 37% Open, 23% to 27% Warm and 9% to 11% Glow.

### 4.4 The recommended lines (target 30 / 35 / 25 / 10)

| Category | Cool ≤ | Open ≤ | Warm ≤ | Glow ≤ | Realised mix (Cool / Open / Warm / Glow) |
| :- | -: | -: | -: | -: | :- |
| harmony | 35 | 45 | 54 | 100 | 28.9 / 36.4 / 25.6 / 9.1 |
| heat | 36 | 46 | 56 | 100 | 30.1 / 33.6 / 26.8 / 9.5 |
| communication | 36 | 48 | 58 | 100 | 28.9 / 35.5 / 25.3 / 10.3 |
| alignment | 39 | 49 | 58 | 100 | 29.1 / 34.2 / 26.6 / 10.0 |
| comfort | 34 | 45 | 53 | 100 | 29.1 / 36.6 / 23.4 / 10.9 |
| consistency | 44 | 55 | 65 | 100 | 30.6 / 34.2 / 25.4 / 9.8 |
| expansion | 32 | 43 | 53 | 100 | 29.5 / 34.4 / 25.1 / 10.9 |
| creativity | 34 | 44 | 54 | 100 | 30.5 / 33.9 / 25.9 / 9.7 |
| drive | 42 | 54 | 63 | 100 | 30.2 / 36.0 / 24.8 / 9.1 |
| balance | 52 | 63 | 71 | 100 | 30.9 / 34.3 / 24.5 / 10.3 |

**Alternative mixes measured** (all per-category; Reader v2 figures are pairs by distinct bands shown, then pairs with any Glow):

| Target Cool / Open / Warm / Glow | 1 band | 2 bands | 3 bands | 4 bands | Any Glow | Warm or Glow results |
| :- | -: | -: | -: | -: | -: | -: |
| **A: 30 / 35 / 25 / 10 (recommended)** | 0.1% | 7.4% | 48.2% | 44.3% | 55.9% | 35.3% |
| B: 25 / 35 / 30 / 10 | 0.1% | 6.9% | 51.0% | 42.0% | 55.9% | 39.3% |
| C: 40 / 30 / 20 / 10 | 0.5% | 9.8% | 44.4% | 45.3% | 55.9% | 30.3% |
| D: 30 / 40 / 25 / 5 | 0.2% | 12.5% | 60.0% | 27.3% | 34.7% | 30.3% |
| E: 35 / 35 / 22 / 8 | 0.3% | 10.2% | 50.2% | 39.4% | 48.4% | 30.3% |

A is recommended because it is the only mix in which all four bands are a meaningful share of every category and 44% of pairs see all four bands. D is the alternative if the Product Owner wants Glow rarer (one pair in three shows a Glow somewhere); its lines are in `v2_measure.json` (Appendix D).

### 4.5 Canon affected

HDE Math Spec §5.3 (one global set becomes ten per-category sets), §5.4.2 (`bands.thresholds` shape), §5.2.8; HDE Governance §4.1.5 and `BAND_EDGE_GOLDENS_OK` (edges pinned at 24, 49, 74); `math/thresholds.json` shape; `engine/core/core.py` and `engine/magic10/calculators.py` (the hard-coded 24/49/74 band rule). Detail in §7.

## 5. Measurements

Harness: the brief §8 scripts from `HDE-EPIC041-POSTCLOSE-compat-score-range-v1.0.md` Appendices A to F, extracted and hash-verified; a fresh clone of `main` at `e2b7427f`; closed rails; PyEphem 4.2.1 in an analysis-only virtual environment. The v1 baseline was rerun first through `distribution.py` and reproduced the record exactly (Cool 78.5%, Open 21.0%, Warm 0.4%, Glow 0.0%; all-Cool pairs 19.3%). v1 per-pair scores for the comparison came from the real `evaluate_pair` (`v1_perpair.py`). The v2 candidate is a pure function of two masks (`m10v2.py`); `measure.py`, `sensitivity.py` and `goldens.py` produce every number below. Scripts and output digests: Appendices C and D.

### 5.1 Band mix, overall and per category

Overall, under the recommended lines: Cool 29.8%, Open 34.9%, Warm 25.3%, Glow 10.0% (v1: 78.5 / 21.0 / 0.43 / 0.0015). Per category: §4.4.

### 5.2 Scores per category

| Category | v1 mean | v1 p50 / p90 / p99 | v1 zero | v2 mean | v2 p10 / p50 / p90 / p99 | v2 min / max | v2 zero | v2 distinct values |
| :- | -: | :- | -: | -: | :- | :- | -: | -: |
| harmony | 15.5 | 16 / 28 / 38 | 5.2% | 41.0 | 28 / 42 / 54 / 62 | 5 / 72 | 0.0% | 66 |
| heat | 18.1 | 16 / 35 / 50 | 7.8% | 41.9 | 26 / 42 / 56 / 64 | 3 / 73 | 0.0% | 71 |
| communication | 16.2 | 15 / 30 / 43 | 3.5% | 43.2 | 27 / 44 / 59 / 68 | 6 / 79 | 0.0% | 67 |
| alignment | 15.2 | 16 / 28 / 41 | 7.1% | 45.0 | 30 / 46 / 59 / 66 | 7 / 74 | 0.0% | 67 |
| comfort | 15.7 | 16 / 28 / 41 | 5.4% | 40.5 | 26 / 41 / 54 / 62 | 3 / 72 | 0.0% | 66 |
| consistency | 14.4 | 14 / 26 / 38 | 6.4% | 49.9 | 33 / 51 / 65 / 73 | 2 / 81 | 0.0% | 80 |
| expansion | 18.6 | 16 / 35 / 50 | 8.0% | 38.9 | 23 / 39 / 54 / 64 | 6 / 76 | 0.0% | 69 |
| creativity | 16.4 | 15 / 30 / 44 | 6.2% | 40.1 | 26 / 40 / 54 / 63 | 7 / 73 | 0.0% | 67 |
| drive | 19.4 | 18 / 33 / 48 | 2.5% | 48.4 | 33 / 49 / 63 / 70 | 2 / 78 | 0.0% | 77 |
| balance | 8.4 | 8 / 25 / 34 | 41.8% | 57.4 | 40 / 59 / 72 / 81 | 11 / 89 | 0.0% | 78 |

Component means (per mille): channel `C` 303 to 529 (zero for 0.0% to 8.0% of pairs); center `Z` 485 to 801 (zero for 0.0% to 8.2%); Type `T` 435 to 716. The v2 raw scale is not fully used (maximum 72 to 89); with relative lines that is immaterial, and the ceiling case is the companionship fixture of §6.

### 5.3 v2 under v1's absolute lines (for the Q-5 argument)

| Category | Cool | Open | Warm | Glow |
| :- | -: | -: | -: | -: |
| harmony | 6.2 | 72.6 | 21.2 | 0.0 |
| heat | 7.7 | 64.6 | 27.7 | 0.0 |
| communication | 8.0 | 59.5 | 32.5 | 0.1 |
| alignment | 3.3 | 60.0 | 36.6 | 0.0 |
| comfort | 7.2 | 71.2 | 21.5 | 0.0 |
| consistency | 2.9 | 42.7 | 53.9 | 0.5 |
| expansion | 11.1 | 69.7 | 19.2 | 0.0 |
| creativity | 8.1 | 71.5 | 20.4 | 0.0 |
| drive | 3.1 | 47.6 | 49.2 | 0.1 |
| balance | 1.1 | 23.6 | 70.1 | 5.1 |

### 5.4 Reader v2 distribution of distinct bands per pair (D-5)

| Distinct bands shown in one pair's ten | v1 | v2 (lines of §4.4) |
| :- | -: | -: |
| 1 | 19.3% | 0.1% |
| 2 | 76.9% | 7.4% |
| 3 | 3.9% | 48.2% |
| 4 | 0.0% | 44.3% |

No category is stuck: the least-used band of any category is 9.1% (`harmony` and `drive` Glow). The most common v2 ten-band profiles are each 2% to 2.4% of pairs, against v1's five profiles covering 88%.

### 5.5 Zeros and ties (D-6)

Zero scores: v1 2.5% to 8.0% per category and 41.8% for `balance`; v2 0.0% for every category (minimum scores 2 to 11). Tie probability (chance that two random pairs share a category score): v1 4.3% to 9.5%, `balance` 30.0%; v2 2.3% to 2.9%. Distinct values: v1 8 to 60; v2 66 to 80. Mean inter-category correlation is unchanged (v1 0.150, v2 0.153), so the ten categories stay as independent of each other as before.

### 5.6 AB↔BA and two-run checks

All 20,000 pairs were scored forward, scored reversed, and scored a second time; the sha256 of the 200,000 scores is `9ec56f0425e03eff6154501362921f6c89bb2cbe3501b503cc1d5516f699cb53` in all three runs, and the reversed run's signal vectors equal the forward run's. The eight golden pairs of §6 were each checked in both orders.

### 5.7 Sensitivity (each knob moved by ±20%, lines frozen at §4.4)

| Knob | Direction | Mean abs. score change | Max | Category results changing band | Min Spearman vs base |
| :- | :- | -: | -: | -: | -: |
| saturation `K` | −20% / +20% | 2.04 / 1.67 | 4 / 3 | 18.1% / 14.7% | 0.996 / 0.998 |
| blend, channel share (others rescaled) | −20% (48/32/20) / +20% (72/18/10) | 3.05 / 3.10 | 11 / 12 | 24.4% / 21.4% | 0.966 / 0.978 |
| blend, center share | −20% (64/20/16) / +20% (56/30/14) | 1.30 / 1.28 | 5 / 5 | 10.0% / 10.1% | 0.991 / 0.991 |
| blend, Type share | −20% (62/26/12) / +20% (58/24/18) | 0.60 / 0.55 | 3 / 3 | 4.0% / 3.9% | 0.997 / 0.997 |
| center profile responses (mutual, one_sided, shared) | −20% / +20% | 2.60 / 1.87 | 5 / 4 | 21.6% / 15.4% | 0.994 / 0.992 |
| signal profile responses (four non-zero states) | −20% / +20% | 2.02 / 1.28 | 4 / 3 | 17.9% / 11.4% | 0.997 / 0.996 |
| each category's largest center weight | −20% / +20% | 0.44 / 0.30 | 3 / 2 | 3.6% / 2.3% | 0.994 / 0.997 |
| Type `A` offsets | −20% / +20% | 0.39 / 0.35 | 2 / 2 | 3.1% / 2.8% | 0.998 / 0.998 |
| Type `I` offsets | −20% / +20% | 0.04 / 0.03 | 1 / 1 | 0.3% / 0.2% | 0.999 / 0.999 |

Reading: ranking is robust everywhere (Spearman ≥ 0.966); band membership moves most with the overall level knobs (`K`, blend, profiles) because the lines are frozen, which is the expected behaviour of relative bands and the reason the lines are recalibrated only by release. The Type tables are the least sensitive knobs.

## 6. Goldens (expected v2 results at the lines of §4.4)

Full vectors (channel states, center outcomes, all twenty signals, `C`, `Z`, `T`) are in Appendix D (`v2_goldens.json`). AB and BA were checked for each.

**Live pairs** (gate sets from `hdchart.py`, mean node, validated 60 of 60 against the live vendor run in the score-range record; SYN-A and SYN-B have the same birth data as P1's two people, so SYN-A with SYN-B is P1):

| Category | P1 / SYN-A with SYN-B: v1 score, band → v2 score, band | P2: v1 → v2 |
| :- | :- | :- |
| harmony | 10 Cool → 42 Open | 32 Open → 58 Glow |
| heat | 22 Cool → 44 Open | 13 Cool → 36 Cool |
| communication | 10 Cool → 38 Open | 20 Cool → 40 Open |
| alignment | 32 Open → 53 Warm | 0 Cool → 23 Cool |
| comfort | 10 Cool → 44 Open | 22 Cool → 55 Glow |
| consistency | 27 Open → 65 Warm | 3 Cool → 40 Cool |
| expansion | 25 Open → 45 Warm | 0 Cool → 15 Cool |
| creativity | 20 Cool → 47 Warm | 0 Cool → 21 Cool |
| drive | 40 Open → 72 Glow | 10 Cool → 46 Open |
| balance | 0 Cool → 72 Glow | 8 Cool → 51 Cool |

P1: both Generators (A: `root`, `sacral`, `solar_plexus` defined, single definition; B: `g`-`sacral` and `ajna`-`throat`, split); 11 channels formed (6 electromagnetic, 4 dominance, 1 compromise); centers: `ego` and `spleen` mutual, `sacral` shared, `head` open, five one-sided; motor→Throat mutual. P2: both Generators; 7 channels (3 electromagnetic, 2 dominance, 2 compromise); `spleen` and `throat` mutual; `ajna`, `head` open.

**Adapted v1 golden set** (HDE Math Spec §9.5):

| Golden | v2 fixture | Expected v2 behaviour |
| :- | :- | :- |
| M10-G001, no relationship channels | gates `{1}` and `{2}` | every channel `none`; both Reflectors; every center `open`; all twenty signals 0; `C = Z = 0`; scores are the Type floor only: harmony 8, heat 2, communication 8, alignment 7, comfort 8, consistency 2, expansion 5, creativity 6, drive 0, balance 11; all Cool |
| M10-G002, homogeneous companionship | both masks all 64 gates | every channel `companionship`; both Manifesting Generators; every center `shared`; signals 667 to 833, `equilibrium_score` 0, `counterweight_ratio` 1000; scores harmony 63 Glow, heat 55 Warm, communication 61 Glow, alignment 81 Glow, comfort 63 Glow, consistency 88 Glow, expansion 52 Warm, creativity 57 Glow, drive 61 Warm, balance 39 Cool. Balance is Cool because two identical charts complete nothing for each other and carry no one-owner mass. Kernel fixture, not a lawful chart |
| M10-G003, owner mass split | A full on `02-14`, `07-31`, `21-45`; B full on `26-44`, `32-54`, `37-40` | six dominance channels, three per owner; `equilibrium_score = 1000`, `counterweight_ratio = 0`; `gives_lo = 3`, `gives_hi = 3`, balance `Z = 1000`; balance score 64 Warm |
| M10-G003, one-sided owner mass | A as above; B gate `{3}` | three dominance channels owned by A; `equilibrium_score = 0`; `gives_hi = 4`, `gives_lo = 0`, balance `Z = 0`; balance score 11 Cool |
| M10-G004, sparse sets | A `{5,19,20,34,43,49}`, B `{9,12,15,22,23,52}` | states as v1 (`05-15`, `23-43` electromagnetic; `09-52`, `12-22` dominance B; `19-49`, `20-34` dominance A); both Manifesting Generators; `ajna`, `g` mutual; `root`, `sacral`, `solar_plexus`, `throat` shared; scores harmony 50 Warm, heat 27 Cool, communication 44 Open, alignment 28 Cool, comfort 43 Open, consistency 50 Open, expansion 10 Cool, creativity 40 Open, drive 35 Cool, balance 74 Glow |
| M10-G005, identity independence | unchanged | nothing but masks enters; `pair_key` under the new `config_id` |
| M10-G006, category boundary matrix | per category, scores at each inclusive maximum and the next integer | for every category: `c1` Cool, `c1+1` Open, `c2` Open, `c2+1` Warm, `c3` Warm, `c3+1` Glow, `100` Glow, with `c1, c2, c3` from §4.4 (asserted for all ten) |
| M10-G007, valid self-pair | unchanged | ineligible before Engine Core; `categories: []`; Reader preimage hash unchanged |
| M10-G008, distinct people, equal masks `{1}` | unchanged inputs | both Reflectors; same scores as G001; all Cool; Reader v1 one Cool item, Reader v2 ten Cool items; `pair_key` under the new `config_id` |

## 7. Canon delta list (nothing edited here)

**HDE Math Spec (PF01).**
* §5.2 scope, §5.2.1: add the centers catalog, the Type pairing catalog and the v2 configuration to inputs; new `config_id`; result schema `magic10_result.v2`.
* §5.2.3: unchanged state and profile values; add the two center response profiles.
* §5.2.4: operations `saturating_state_sum_v2`, `bilateral_owner_mass_v2`, `mutual_state_share_v2`; the Balance maps become all 36 channels; retain the 18 ordinary maps.
* §5.2.5: the three-component reduction, blend 60/25/15, one `ROUND_HALF_UP`, clamp; the per-category band handoff.
* new §5.2.x: Type derivation, aura classes, center outcomes, motor→Throat outcome, Type component with the `A` and `I` tables, the 15-point limit.
* §5.2.8: v2 knob table (`K`, blend, center weights 1..3, center profiles, Type offsets, lines) and what counts as structural.
* §5.3: per-category inclusive maxima; the method, reference population and recalibration rule of §4; boundary behaviour per category.
* §5.4.1, §5.4.2, §5.4.4: new governed inputs; `bands.thresholds` becomes a per-category object; §5.4.2.1 unchanged (the direct set remains governed; v2's predicate is the any-route connected definition and is stated as such).
* §6.3 center tagging: promote from `[Speculative]` to the four-outcome contract of §3.5, or retire in favour of it; §6.4 direct-MT flag: state its relationship to the motor→Throat outcome.
* §9.5: replace the v1 goldens with §6; §9.1 boundary proofs per category.
* §4.1 eligibility: unchanged ("any Type combination" remains eligible; Type now enters scoring, not eligibility).

**HDE Governance (PF04).** §12.1 `GATE:CORE-MATCH`: "band thresholds are inclusive maxima" stays true; add "per category". §4.1.5 and `BAND_EDGE_GOLDENS_OK`: edges no longer 24/49/74/100; proof goldens become the ten per-category sets. `GATE:CORE-DET`: unchanged.

**HDE Schemas & Artifacts (PF12).** §2.1: a centers catalog path and schema (nine rows, `id`, `motor`). §2.6: `math/thresholds.json` carries per-category edges. §2.9: `magic10_mechanics_config.v2` shape (adds `saturation_k_bp`, `blend`, `center_profiles`, `center_map`, `sources.centers`, `sources.type_pairing`), new loader closure rules (every center in the map exists; weights 1..3; profiles have four outcome keys with `open = 0`; blend sums to 100; `K > 0`), result schema `magic10_result_v2` (same shape), compat result schema v2. New Type pairing catalog path and schema. Manifest membership for all new members; new `release_id`. §2.10 public Reader schemas: unchanged.

**HDE Architecture (PF02).** No new component. Engine Core receives two more normalized catalogs; the Type derivation is pure and lives in Engine Core, not in the adapter. Note that the stored `type` field is not consumed.

**HDE Narratives Guide (PF17).** None expected. Keys stay `(category, band, perspective, slot)`; the 360-row registry is unchanged. Warm and Glow rows become reachable.

**HDE Users Guide (PF29).** §7 compat workflows: the admin/CLI result shows the same signal and score fields; the example `compat_score 50, band Open` in §5.1 would no longer hold under per-category lines; refresh examples after implementation.

**HDE Build Notes (PF10).** An adoption addendum recording the Product Owner's decision (brief §9 step 4), superseding `M10-CANON-001`'s "aura-diagnostic mechanics out of scope" for Type.

## 8. Implementation impact (nothing implemented)

* **Code areas.** `engine/magic10/composite.py` (center outcomes and Type derivation beside the classifier), `engine/magic10/signals.py` (three new operations), `engine/magic10/calculators.py` (three-component reduction, per-category band rule), `engine/core/core.py` (bundle validation for the new catalogs and schema v2; the hard-coded 24/49/74 check becomes per-category), `engine/config/registry_loader.py` (two new catalogs, roster, admitted release constants), `engine/compat/compute.py` (result schema v2 identity), schemas, goldens and the owner tests of HDE Build Notes 2.16 R-1.
* **Catalogs.** New: centers catalog, Type pairing catalog, mechanics configuration v2. Changed: `math/thresholds.json` shape. Unchanged: gates, channels, `magic10.json`, `magic10_caps.json`, narratives pack.
* **Data change.** None. v2 reads the same stored gate set. Planetary activations are not an input (Q-2).
* **Release cut.** One release carrying all new members; `ADMITTED_RELEASE_ROSTER` grows; new `release_id`. v2 replaces v1 in that release (Q-6).
* **Stale cached results.** Every intrinsic cache entry carries `config_id` and `release_id`; both change, so every v1 entry is a miss and is recomputed (HDE Math Spec §5.2.2). No migration.
* **Reader shapes.** Unchanged: v1 one `{id, band}`; v2 ten `{id, band}` in the governed order; numeric-free.
* **QA.** Live compat test (HDE Build Notes 2.15) with SYN-A and SYN-B; §6 gives their expected v2 bands.

## 9. Decisions for the Product Owner (with recommendations)

| Q | Decision | Recommendation |
| :- | :- | :- |
| Q-1 | Meaning of "relevant placement" | Adopt (a) quality over coverage and (b) center relevance together, as §3 does. Defer (c) planetary placement. |
| Q-2 | Planetary activations as an input | Not in v2.0. It is a data change: the vendor adapter must keep per-planet activations, the stored chart schema changes, every stored person (SYN-A, SYN-B and all production rows) must be re-acquired with vendor calls, and the harness's `hdchart.py` would need the activation list it already computes. Nothing in D-1 to D-6 needed it. |
| Q-3a | Do the admitted references support a Type pairing model and the composite rules? | Composite rules: yes (§2.1, §2.2). Type derivation and each Type's aura: yes (§2.3, §2.4). A Type pairing rule: no; the gap is recorded. |
| Q-3b | Which route was used, and adopt the resulting rules? | Route 1 found no citable primary passage; route 2, analyst inference, produced Tables 7a and 7b. Recommend adoption as Glow product synthesis, bounded to 15 points, reviewed by the independent step. Recommend acquiring Ra Uru Hu's *Type Sexual Signatures* (Jovian Archive, 2008) into `docs/hd_refs/`. |
| Q-3c | Is Manifesting Generator its own Type? | Derive it (it is validated and reported), but pair it as a Generator: doctrine says there are "two kinds of Generators" with one aura. |
| Q-4 | How much may Type move a score? | 15 points of 100 at most, measured 0.4% to 7.6% of variance. Keep the blend 60/25/15. |
| Q-5 | Bands | Relative, per-category, target 30/35/25/10 (A); D (Glow 5%) if Glow should be rarer. Reference population as §4.2; recalibration only by release. |
| Q-6 | Cutover | Confirm: v2 replaces v1 in the adopting release; one active configuration; rollback is the complete prior release. |
| Q-7 (new) | Motor→Throat route | Any connected definition (validated against vendor Types and population shares), with the §5.4.2.1 direct set retained as a governed subset. The alternative, direct-only, changes 10.7% of Types and leaves doctrine. |
| Q-8 (new) | `balance` redefinition | The two Balance signals run over all 36 channels and the center component is bilateral completion. v1's `balance` was 0 for 41.8% of pairs; the construct name and position stay. |

## 10. Limits, nonclaims, canon relied on

### 10.1 Limits

* The reference population is synthetic, with births uniform over 1950 to 2005 and random pairs. A real user pool will fall differently; the frozen lines would then give a different realised mix, and that is the recalibration case of §4.2.
* Type derivation is validated against the only vendor charts in the repository that carry a Type (three HumanDesignAPI v2 payloads and two vendor-shaped fixtures) and against doctrine's population shares. The vendor Types of P1, P2, SYN-A and SYN-B are not in the repository evidence (OPS01 stored compat outputs only), so that check belongs to implementation QA. No fixture exercises an indirect motor→Throat route.
* A Reflector defines nothing and so completes nothing for a partner; pairs with a Reflector score low on `balance` by construction (mean 36 against 58 overall). This is a mechanical consequence of the definition, stated here, not a claim about Reflectors.
* The Type tables are inference. They are bounded, measured, and the least sensitive knobs in §5.7; they are not doctrine and are labelled so.
* The `hdchart.py` chart calculation is validated on four people (60 of 60 numbers); the v1 reproduction here cross-checks the whole population at the band level.
* Outside-source search was bounded to the pages listed in Appendix B.

### 10.2 Nonclaims

This proposal:
* changes no canon, code, catalog, test, schema, data or Notion page;
* creates no change, CRD candidate, release or `config_id` in any system;
* adopts no formula; the role proposes and the Product Owner decides;
* makes no QA verdict, acceptance, Ops result or closure claim;
* makes no claim about relationship quality or outcomes, and no medical, psychological, sexual, safety or destiny claim; bands and scores describe composite Human Design mechanics as Glow synthesises them.

### 10.3 Canon relied on

Read on `main` at `e2b7427f` (`amthorn78/glow-hdengine-v2`) and `edaa34c` (`amthorn78/glow-docs`).

* **HDE Math Spec v1.3.8:** §2.5; §4.1 to §4.7; §5.1; §5.2 in full; §5.3 in full; §5.4.1 to §5.4.4 including §5.4.2.1; §5.5; §5.6; §6.1; §6.3; §6.4; §6.7; §7.2, §7.3; §8.2, §8.3; §9.1, §9.5.
* **HDE Governance v2.8.8:** §4.1.5; §12.1 (`GATE:CORE-DET`, `GATE:CORE-MATCH`); §12.2 band entries.
* **HDE Schemas & Artifacts v2.9.7:** §2.1, §2.6, §2.9, §2.10.
* **HDE Architecture v2.4.7:** §2.1 components (routing only).
* **HDE Narratives Guide v1.5.4:** §2.3 candidate registry.
* **HDE Users Guide v1.0.3:** §5.1, §6.4, §7.
* **HDE Build Notes v14.0.5:** current-version rule; addenda 2.15 and 2.16.
* **Glow Story:** in full.
* **PF08 Human Design System:** "The Centers"; "Channels" (keynote list); "The Rave Charts" (Composite Rave passage, Johannes analysis, "RAVE — Channel and Definition Analysis Graph", "Composite with Renate").
* **History only, not authority:** `M10-CANON-001` (v1 adoption, superseded base version at `e6578b53`).
* **Records:** `docs/ephemeral/HDE-EPIC041-POSTCLOSE-compat-score-range-v1.0.md` (harness, population, v1 figures); `docs/ephemeral/HDE-EPIC041-POSTCLOSE-OPS01-ops-execution-result-v1.0.md` and `audit/ops/hde-epic041/postclose-ops01/` (live pairs); `docs/ephemeral/HDE-M10V2-hd-math-specialist-design-brief-v1.0.md` (the brief).
* **Human Design references (`glow-docs/docs/hd_refs/`):** Human Design Reference Index v1.2.0 (§1, §3, §4, §5, §9, §10); *The Complete Guide to the Human Design System* (PDF, text layer via `pdftotext -layout`, printed page numbers from the page footers); Generators' Course (HD-TYPE-01); Holistic Analysis Fundamentals (HD-SYN-01, aura descriptors only); Winn, *Understanding Your Clients* and *Understanding the Centers* (HD-SECONDARY-01/02, A5, corroboration only). Not used: HD-SYN-02 (no compatibility score, per the index), PF11 (gate meanings were not needed beyond the retained v1 maps).

## Appendix A — Channel keynotes (PF08) and the retained v1 signal maps

Each of the 36 channels, its two centers from `catalog/channels_v1.json`, its PF08 keynote ("Channels: The Channels and their keynotes"), and the ordinary signals it feeds. The maps are v1's and unchanged (HDE Math Spec §5.2.4). In v2 the two Balance signals read all 36 channels.

| Channel | Centers | PF08 keynote (source doctrine) | Ordinary signals fed (v1 map, retained) |
| :- | :- | :- | :- |
| `01-08` | g, throat | Inspiration: the creative role model | `novelty_factor` |
| `02-14` | g, sacral | The Beat: a design of being the keeper of keys | `vector_cohesion`, `willpower_current` |
| `03-60` | root, sacral | Mutation: energy which fluctuates and initiates, pulse | `momentum_flux`, `variance_stability`, `growth_tendency`, `novelty_factor` |
| `04-63` | ajna, head | Logic: a design of mental ease mixed with doubt | `signal_clarity` |
| `05-15` | g, sacral | Rhythm: a design of being in the flow | `resonance_strength`, `buffer_resilience`, `pattern_integrity` |
| `06-59` | sacral, solar_plexus | Mating: a design focused on reproduction | `resonance_strength`, `spark_intensity`, `soothe_index` |
| `07-31` | g, throat | The Alpha: for good or bad, a design of leadership | `vector_cohesion` |
| `09-52` | root, sacral | Concentration: a design of determination, focused | `pattern_integrity`, `focus_pressure` |
| `10-20` | g, throat | Awakening: a design of commitment to higher principles | `vector_cohesion`, `expression_flow` |
| `10-34` | g, sacral | Exploration: a design of following one's convictions | `vector_cohesion` |
| `10-57` | g, spleen | Perfected Form: a design of survival | `buffer_resilience` |
| `11-56` | ajna, throat | Curiosity: a design of a searcher | `exchange_density`, `horizon_reach`, `expression_flow` |
| `12-22` | solar_plexus, throat | Openness: a design of a social being | `resonance_strength`, `exchange_density`, `soothe_index`, `expression_flow` |
| `13-33` | g, throat | The Prodigal: the design of the witness | `resonance_strength`, `exchange_density` |
| `16-48` | spleen, throat | The Wave Length: a design of talent | `pattern_integrity`, `expression_flow` |
| `17-62` | ajna, throat | Acceptance: a design of an organizational being | `signal_clarity`, `pattern_integrity` |
| `18-58` | root, spleen | Judgment: a design of insatiability | `pattern_integrity`, `growth_tendency`, `focus_pressure` |
| `19-49` | root, solar_plexus | Synthesis: a design of being sensitive | `rapport_delta`, `axis_agreement`, `soothe_index` |
| `20-34` | sacral, throat | Charisma: a design where thoughts must become deeds | `momentum_flux`, `focus_pressure` |
| `20-57` | spleen, throat | The Brain Wave: a design of penetrating awareness | `exchange_density` |
| `21-45` | ego, throat | Money: a design of a materialist | `willpower_current` |
| `23-43` | ajna, throat | Structuring: a design of individuality | `signal_clarity`, `novelty_factor` |
| `24-61` | ajna, head | Awareness: a design of a thinker | `signal_clarity` |
| `25-51` | ego, g | Initiation: a design of needing to be first | `spark_intensity`, `novelty_factor`, `willpower_current` |
| `26-44` | ego, spleen | Surrender: a design of a transmitter | `rapport_delta`, `exchange_density`, `willpower_current` |
| `27-50` | sacral, spleen | Preservation: a design of custodianship | `rapport_delta`, `axis_agreement`, `buffer_resilience` |
| `28-38` | root, spleen | Struggle: a design of stubbornness | `axis_agreement`, `horizon_reach`, `focus_pressure` |
| `29-46` | g, sacral | Discovery: a design of succeeding where others fail | `momentum_flux`, `variance_stability`, `horizon_reach` |
| `30-41` | root, solar_plexus | Recognition: a design of focused energy | `spark_intensity` |
| `32-54` | root, spleen | Transformation: a design of being driven | `axis_agreement`, `variance_stability`, `growth_tendency`, `willpower_current` |
| `34-57` | sacral, spleen | Power: a design of an archetype | `buffer_resilience` |
| `35-36` | solar_plexus, throat | Transitoriness: a design of a 'Jack of all Trades' | `momentum_flux`, `horizon_reach`, `expression_flow` |
| `37-40` | ego, solar_plexus | Community: a design of being a part, seeking a whole | `rapport_delta`, `soothe_index` |
| `39-55` | root, solar_plexus | Emoting: a design of moodiness | `spark_intensity` |
| `42-53` | root, sacral | Maturation: a design of balanced development, cyclical | `variance_stability`, `growth_tendency`, `focus_pressure` |
| `47-64` | ajna, head | Abstraction: a design of mental activity and clarity | `signal_clarity` |

## Appendix B — Citation register

Format follows the Human Design Reference Index §10: source ID; title; locator; claim; status. Complete Guide locators are printed page numbers read from the page footers of the PDF text layer (`pdftotext -layout`); the physical PDF page is the printed page plus 12. Markdown locators are the `## Source segment N` markers of the `docs/hd_refs` companions.

| Ref | Source (ID, tier) | Locator | Claim relied on | Status |
| :- | :- | :- | :- | :- |
| D-01 | PF08 Human Design System (A2) | "The Rave Charts", Composite Rave passage beginning "When you take the Body Graph of two individuals" | superimposition reveals where two charts connect; "How you connect and where you connect determines the nature of the relationship" | source doctrine |
| D-02 | PF08 (A2) | same passage, "Imagine our example of Johannes" | a partner who connects an open center makes that center the basis of the relationship | source doctrine |
| D-03 | PF08 (A2) | same passage, "A feel of a connection can be misleading" | a defined Spleen meeting an undefined one "is going to make them feel better"; may be "the only beneficial connection" | source doctrine |
| D-04 | PF08 (A2) | "Transfer to the Body Graph", Johannes analysis ("Definition: when two centers are permanently connected…") | definition of a defined center; "continual transfer of energy between two centers" | source doctrine |
| D-05 | PF08 (A2) | same section ("What is defined in us is our foundation…") | definition is foundation; receptivity (openness) is how we connect | source doctrine |
| D-06 | PF08 (A2) | "RAVE — Channel and Definition Analysis Graph" | "An undefined center is always vulnerable. It is where our life changes." | source doctrine |
| D-07 | PF08 (A2) | "Composite with Renate", "Head–Ajna Complementarity (with Johannes)" | two hanging gates complete a channel together: "this system is complete and defined" (mutual completion) | source doctrine |
| D-08 | PF08 (A2) | same, "Emotional Channels Opened" and "Most important for Johannes, together he has an emotional base" | one person's definition conditions the other's open center (one-sided completion) | source doctrine |
| D-09 | PF08 (A2) | "The Centers" | the nine center keynotes | source doctrine |
| D-10 | PF08 (A2) | "Channels: The Channels and their keynotes" | the 36 channel keynotes (Appendix A) | source doctrine |
| D-11 | HD-FND-01 Complete Guide (A2) | Part Fifteen, "The Undefined Sacral Center: A Projector", p. 229 | an undefined Sacral means Manifestor, Projector or Reflector; the Projector "is a non-energy type and is going to be very dependent" | source doctrine |
| D-12 | HD-FND-01 (A2) | Part Fifteen, p. 230 (aura paragraph) | Manifestor closed aura, "pushing off quality", "a barrier"; Generators "enveloping aura … open aura and brings everything inward"; Projector "focused aura … very penetrating aura", "recognize and the yearning to be recognized" | source doctrine |
| D-13 | HD-FND-01 (A2) | Part Fifteen, "Split Definition: The 31/7 and the 54/32", p. 232 | a bridge gate or channel joining a power source (Root) to the Throat "would immediately turn this Projector into a Manifestor" | source doctrine |
| D-14 | HD-FND-01 (A2) | Part Fifteen, "The Undefined Sacral Center", p. 235 | "Most Projectors would rather be a Generator; it's a natural relationship between the two" | source doctrine |
| D-15 | HD-FND-01 (A2) | Part Seven, "The Sacral Center", p. 103 | "Manifestors and Projectors and Reflectors are non-Sacral beings"; two-thirds of humanity are Generators | source doctrine |
| D-16 | HD-FND-01 (A2) | Part Seven, p. 104 | Projector conditioned by Generator: "an amplification of that energy … does not know when enough is enough" | source doctrine |
| D-17 | HD-FND-01 (A2) | Part Seven, "The Root Center", p. 105 | "The Root Center is a pressure center like the Head Center" | source doctrine |
| D-18 | HD-FND-01 (A2) | Part Seven, "The Splenic Center and the Solar Plexus Center", p. 106 | Spleen is an awareness center, "makes us feel good", "sense of security" | source doctrine |
| D-19 | HD-FND-01 (A2) | Part Seven, "The Solar Plexus Center", p. 108 | "The Solar Plexus is a motor … The Spleen is not a motor. The Ajna is not a motor."; 51% of humanity emotionally defined | source doctrine |
| D-20 | HD-FND-01 (A2) | Part Seven, pp. 100 to 102 (Head, Throat, G, Heart) | per-center keynotes used in §3.6 ("11 ways that we speak"; open G "desperate for … love, direction"; Heart "to prove yourself") | source doctrine |
| D-21 | HD-FND-01 (A2) | Part Seven, "Watch Your Not-Self", p. 111 | "what you do when you step into their aura, what you fill up what they may have open" | source doctrine |
| D-22 | HD-FND-01 (A2) | Part Eight, "The Sleep State is Our Deepest Conditioning Process", p. 122 | 1.4% of waking raves are Reflectors; Reflectors "deeply, deeply, deeply open" | source doctrine |
| D-23 | HD-FND-01 (A2) | Part Eight, "The Aura", "The Aura Has a Prana", pp. 113 to 114 | the aura is an energy field about two arm-lengths; auras interpenetrate | source doctrine |
| D-24 | HD-TYPE-01 Generators' Course (A3) | segment 1 | "only Generators have a defined Sacral Center"; "the Generator is a prime motor"; other types "are born to find life" | source doctrine |
| D-25 | HD-TYPE-01 (A3) | segment 15, "MANIFESTING GENERATOR: MORE EASILY SEDUCED TO MANIFEST" | "only four kinds of beings … two kinds of Generators"; same Strategy for any defined Sacral; one third of humanity are Manifesting Generators; "most deeply conditioned by Manifestor propaganda" | source doctrine |
| D-26 | HD-TYPE-01 (A3) | segment 76 | 35-36 and 12-22: Throat gate "directly connected to a Motor … direct manifesting potential"; 45 "points directly down to the 21st Gate, to the Ego Center, to a Motor" | source doctrine |
| D-27 | HD-SYN-01 Holistic Analysis Fundamentals (A3) | segment 117 | "Manifestor … closed aura … Generator with this huge enveloping aura … a Reflector sampling … a Projector focused" | source doctrine |
| D-28 | HD-SYN-01 (A3) | segment 28 | "The Projector aura is a deeply penetrating aura. And the Projector came into the world to guide us" | source doctrine |
| S-01 | HD-SECONDARY-02 Winn, *Understanding Your Clients* (A5) | segments 58 to 59, "Quick Review Types and Strategies" | mechanical definitions of the five Types by Sacral definition and motor to the Throat; Reflectors "Have no centers defined" | secondary interpretation (corroborates D-11, D-13, D-15, D-25, D-26) |
| S-02 | HD-SECONDARY-02 (A5) | segment 48 ("Whenever the Sacral Center is defined, the person's Type is automatically a Generator or Manifesting Generator") | Manifesting Generators are "first and foremost Generators" | secondary interpretation (corroborates D-25) |
| S-03 | HD-SECONDARY-02 (A5) | segments 55 to 56 | "closed and repelling aura" (Manifestor); "focused aura" (Projector) | secondary interpretation (corroborates D-12) |
| S-04 | HD-SECONDARY-01 Winn, *Understanding the Centers* (A5) | segment 64, "The Four Motors" | the four motors are Sacral, Root, Emotional Solar Plexus, Will | secondary interpretation (corroborates D-19, D-24, D-26, D-13) |
| G-01 | Human Design Reference Index v1.2.0 | §9 "Open source gaps" | "Relationship/composite teaching is partial … do not establish a general compatibility score" | index record of the gap |
| G-02 | Human Design Reference Index v1.2.0 | §4 M15 | HD-SYN-02 "establishes no app compatibility score"; not used | routing |
| O-01 | Jovian Archive, product page *Type Sexual Signatures* (Ra Uru Hu, Ibiza 2008, audio and illustrated eBook transcript) | https://jovianarchive.com/products/type-sexual-signatures , accessed 2026-11-01 | page says "honoring our Aura Type is the key to avoiding negative interaction"; no passage published | outside source, located but not relied on (no passage available); recommended for acquisition |
| O-02 | "Human Design Academy by Ra Uru Hu", blog *Understanding Our Design in Relationships*, Part 2, dated 2025-04-16, "based on" a 1998 recording | https://understandingourdesigninrelationships.blogspot.com/2025/04/UnderstandingOurDesigninRelationships-1998-CD1-Track02.html , accessed 2026-11-01 | states aura descriptors (closed and repelling; open and enveloping; focused and penetrating; sampling and resistant) and pair remarks (Generator–Projector "deeply satisfying connections when the Generator responds to the Projector's guidance"; Manifestor–Projector "tension, as the Manifestor seeks freedom while the Projector seeks recognition"; Reflectors "sample and mirror"; "no perfect combination") | outside source, not relied on: not a transcript; author, publisher and edition unverifiable; consistent with D-12, D-14, D-27 and with the inferences of §3.7 |
| O-03 | same blog, Part 9 "The Four Types in Relationship", dated 2025-04-17 | https://understandingourdesigninrelationships.blogspot.com/2025/04/UnderstandingOurDesigninRelationships-1998-CD1-Track09.html , accessed 2026-11-01 | "Projector guides the Generator's energy"; "Manifestor initiates, Generator responds. Can be powerful — or chaotic"; "You cannot matchmake by Type. Compatibility is not a formula." | outside source, not relied on (same provenance limit) |
| M-01 | Mathematics: hyperbolic saturation (Michaelis–Menten form of the Hill equation), `y = y_max · x / (x + K)`, `K` the half-saturation constant | https://www.physiologyweb.com/calculators/hill_equation_interactive_graph.html ; https://arxiv.org/pdf/1305.5533 (Half-Saturation Constants in Functional Responses); both accessed 2026-11-01 | the saturating accumulation of §3.5 and the meaning of `K` | outside source (mathematics only) |
| M-02 | Mathematics: Hyndman, R. J. and Fan, Y. (1996), "Sample Quantiles in Statistical Packages", *The American Statistician* 50(4), 361–365, DOI 10.1080/00031305.1996.10473566 | https://doi.org/10.1080/00031305.1996.10473566 , accessed 2026-11-01 | quantile-based placement of band lines; the rounding family for discrete scores (§4.2) | outside source (mathematics only) |

Conflicts: none found between admitted sources on the claims used. The outside pages agree with the admitted descriptors; where O-02 adds "resistant" (Reflector) and "absorbing" (Projector), v2 relies only on the admitted words "sampling" and "focused, penetrating".

## Appendix C — Analysis scripts (verbatim, with SHA-256)

Analysis only; not product code. Run from a fresh clone of `main` under closed rails with PyEphem 4.2.1 installed in a separate virtual environment, after extracting `hdchart.py` (Appendix A of the score-range record, SHA-256 `5969513b1177b9b9086dc7abb2a38e0a7eca5f365d7ad3472bb6e25285d3b159`) and `distribution.py` (its Appendix C). `hdmech.py` reads the topology catalogs from the clone at the absolute path in its `REPO` constant; set it to the clone's path. Order: `gen_people.py`, then `v1_perpair.py <clone>` (and `distribution.py <clone> <out.json> 2000 20000 cache` for the baseline), then `measure.py`, `sensitivity.py`, `goldens.py`.

### C.1 `gen_people.py` (SHA-256 `488dafeada3c645b939b70b126ff3818961947314dcfdc9cbf3999e41afda7ec`)

Replicates the record's seeded population and pair list and dumps them to JSON.

```python
"""Replicate distribution.py's seeded population and pair list; dump to JSON (analysis only)."""
import datetime as dt, json, pathlib, random, sys, uuid
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "harness"))
from hdchart import gates_utc
SEED = 20261101; N_PEOPLE = 2000; N_PAIRS = 20000
rng = random.Random(SEED)
start, span = dt.datetime(1950, 1, 1), (dt.datetime(2006, 1, 1) - dt.datetime(1950, 1, 1)).total_seconds()
people = []
for i in range(N_PEOPLE):
    when = start + dt.timedelta(seconds=rng.random() * span)
    uid = str(uuid.uuid5(uuid.NAMESPACE_URL, f"scorerange-synthetic-{SEED}-{i}"))
    people.append({"uid": uid, "when_utc": when.isoformat(), "gates": gates_utc(when, true_node=False)})
pairs, seen = [], set()
while len(pairs) < N_PAIRS:
    a, b = rng.sample(range(N_PEOPLE), 2)
    key = (min(a, b), max(a, b))
    if key not in seen:
        seen.add(key); pairs.append([a, b])
(HERE / "out" / "people.json").write_text(json.dumps({"seed": SEED, "people": people, "pairs": pairs}))
print("people", len(people), "pairs", len(pairs))
```

### C.2 `v1_perpair.py` (SHA-256 `6df1e78f3520152564f930cd2d0fccf8df8844510b6e7b589005035f852e7b73`)

v1 per-pair scores through the real `evaluate_pair` (closed rails, admitted release of the clone).

```python
"""Per-pair v1 results through the real evaluate_pair (analysis only). Saves scores and signals."""
import json, pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent
REPO = pathlib.Path(sys.argv[1]); sys.path.insert(0, str(REPO))
from engine.bodygraph.resolver import ResolvedCompatChart
from engine.compat.compute import evaluate_pair, evaluation_party
from engine.config.registry_loader import load_active_mechanics_bundle
from tests.support.pr04_fixtures import complete_chart
B = load_active_mechanics_bundle()
P = json.loads((HERE / "out/people.json").read_text())
parties = [evaluation_party(ResolvedCompatChart(p["uid"], complete_chart(p["uid"], p["gates"]), "resolved", None, None, None, None)) for p in P["people"]]
out = []
for a, b in P["pairs"]:
    r = evaluate_pair(parties[a], parties[b], bundle_provider=lambda: B)
    out.append({"scores": [c["score"] for c in r["categories"]], "signals": [s["q"] for s in r["signals"]]})
order = [c["category_id"] for c in r["categories"]]
(HERE / "out/v1_perpair.json").write_text(json.dumps({"order": order, "release_id": B.release_id, "config_id": B.mechanics["config_id"], "results": out}))
print("saved", len(out), "pairs; order", order, "release", B.release_id[:12])
```

### C.3 `hdmech.py` (SHA-256 `d5165bbac4ab30c0ad0922c46917309083eff5ec87614de59dde30e210848f05`)

Pure Human Design mechanics over gate masks: complete channels, defined centers, definition components, motor→Throat, Type, the §6.1 classifier, composite outcomes.

```python
"""Pure Human Design mechanics over gate masks (analysis prototype; not product code).

Everything here is a function of a 64-bit gate mask and the governed topology catalogs
(catalog/gates_v1.json, catalog/channels_v1.json read from a checkout of main).
"""
from __future__ import annotations
import json, pathlib

REPO = pathlib.Path("/tmp/claude-0/-home-user/5d854c62-60a7-548f-87fb-0d88643ee7eb/scratchpad/hde/repo")
GATES = {r["gate"]: r["center"] for r in json.loads((REPO / "catalog/gates_v1.json").read_text())["gates"]}
CHANNELS = {r["id"]: r for r in json.loads((REPO / "catalog/channels_v1.json").read_text())["channels"]}
CENTERS = ("ajna", "ego", "g", "head", "root", "sacral", "solar_plexus", "spleen", "throat")
MOTORS = frozenset({"sacral", "solar_plexus", "ego", "root"})   # doctrine: four motors
STATES = ("none", "companionship", "dominance", "compromise", "electromagnetic")


def bit(g: int) -> int:
    return 1 << (g - 1)


def mask_of(gates) -> int:
    return sum(bit(g) for g in gates)


def complete_channels(mask: int) -> list[str]:
    """Channels whose two gates are both in the mask (ASCII order of channel id)."""
    return [cid for cid, row in CHANNELS.items() if mask & bit(row["gates"][0]) and mask & bit(row["gates"][1])]


def defined_centers(mask: int) -> frozenset[str]:
    out = set()
    for cid in complete_channels(mask):
        out.update(CHANNELS[cid]["centers"])
    return frozenset(out)


def definition_components(mask: int) -> list[frozenset[str]]:
    """Connected components of defined centers, joined by the mask's complete channels."""
    parent = {c: c for c in CENTERS}
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]; x = parent[x]
        return x
    touched = set()
    for cid in complete_channels(mask):
        a, b = sorted(CHANNELS[cid]["centers"])
        touched.update((a, b))
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra
    comps = {}
    for c in touched:
        comps.setdefault(find(c), set()).add(c)
    return [frozenset(v) for v in comps.values()]


def motor_to_throat(mask: int) -> bool:
    """A motor center lies in the same definition component as the Throat."""
    for comp in definition_components(mask):
        if "throat" in comp and comp & MOTORS:
            return True
    return False


def derive_type(mask: int) -> str:
    defined = defined_centers(mask)
    if not defined:
        return "Reflector"
    sacral = "sacral" in defined
    mt = motor_to_throat(mask)
    if sacral:
        return "Manifesting Generator" if mt else "Generator"
    return "Manifestor" if mt else "Projector"


def aura_class(hd_type: str) -> str:
    return {"Generator": "generator", "Manifesting Generator": "generator",
            "Manifestor": "manifestor", "Projector": "projector", "Reflector": "reflector"}[hd_type]


def classify_channel(cid: str, mask_lo: int, mask_hi: int):
    """PF01 §6.1 five-state classifier (same as engine/magic10/composite.py)."""
    x, y = (bit(g) for g in CHANNELS[cid]["gates"])
    lo = bool(mask_lo & x) + bool(mask_lo & y)
    hi = bool(mask_hi & x) + bool(mask_hi & y)
    owner = None
    if lo == hi == 2:
        state = "companionship"
    elif lo == 2 or hi == 2:
        state = "compromise" if min(lo, hi) == 1 else "dominance"
        owner = "member_lo" if lo == 2 else "member_hi"
    elif lo == hi == 1 and bool(mask_lo & x) != bool(mask_hi & x):
        state = "electromagnetic"
    else:
        state = "none"
    return state, owner


def composite(mask_a: int, mask_b: int) -> dict:
    """Pair-level mechanics: channel states, composite centers, center outcomes, motor->throat."""
    lo, hi = sorted((mask_a, mask_b))
    states = {cid: classify_channel(cid, lo, hi) for cid in CHANNELS}
    union = lo | hi
    def_lo, def_hi = defined_centers(lo), defined_centers(hi)
    def_union = defined_centers(union)   # any channel complete across both gate sets
    outcomes = {}
    for c in CENTERS:
        if c not in def_union:
            outcomes[c] = "open"                 # undefined in the composite
        elif c in def_lo and c in def_hi:
            outcomes[c] = "shared"               # defined in both individually
        elif c in def_lo or c in def_hi:
            outcomes[c] = "one_sided"            # one person's definition conditions the other's openness
        else:
            outcomes[c] = "mutual"               # undefined in both; defined only together (EM)
    mt_lo, mt_hi, mt_union = motor_to_throat(lo), motor_to_throat(hi), motor_to_throat(union)
    if not mt_union:
        mt = "open"
    elif mt_lo and mt_hi:
        mt = "shared"
    elif mt_lo or mt_hi:
        mt = "one_sided"
    else:
        mt = "mutual"
    return {"states": states, "centers": outcomes, "motor_throat": mt,
            "types": (derive_type(lo), derive_type(hi))}
```

### C.4 `m10v2.py` (SHA-256 `507c6e67ea29ba0bbab039f17e576d4bf7420ecdfddcf9e982e3024844482b54`)

The v2 candidate formula and its configuration (all values of §3).

```python
"""Magic10 v2 candidate: pure integer function of two gate masks and a configuration (analysis prototype).

Evaluation order (all integer; ROUND_HALF_UP = (2N + D) // (2D) for N, D >= 0):
  1. order masks numerically (lo, hi); classify the 36 channels (PF01 §6.1 classifier);
  2. per person: defined centers, definition components, motor->throat, Type (aura class);
  3. composite center outcomes (open / shared / one_sided+owner / mutual) and motor->throat outcome;
  4. 18 ordinary signals: saturating accumulation q = rhu(1000*S/(S+K)), S = sum w*r(state) in bp;
     2 Balance signals over all 36 channels (bilateral owner mass; mutual-state share);
  5. channel component C_k = rhu(weighted mean of the category's two signals) (per mille);
  6. center component Z_k = rhu(weighted mean of center-outcome responses) (per mille); balance uses the
     bilateral completion operation;
  7. Type component T_k = clamp(500 + A_k[lo] + A_k[hi] + I_k[pair], 0, 1000);
  8. score_k = clamp(rhu((a*C_k + b*Z_k + c*T_k) / 1000), 0, 100) with a+b+c = 100;
  9. band_k from the category's inclusive maxima.
"""
from __future__ import annotations
import copy, json, pathlib
import hdmech as m

REPO = m.REPO
MECH_V1 = json.loads((REPO / "catalog/magic10_mechanics_v1.json").read_text())
CAPS = json.loads((REPO / "catalog/magic10_caps.json").read_text())
ORDER = json.loads((REPO / "catalog/magic10.json").read_text())["order"]


def rhu(n: int, d: int) -> int:
    """round_half_up(n/d) for n >= 0, d > 0, in integers."""
    return (2 * n + d) // (2 * d)


CENTER_PROFILES = {
    "completion_bp_v2": {"mutual": 10000, "one_sided": 7500, "shared": 2500, "open": 0},
    "foundation_bp_v2": {"shared": 10000, "one_sided": 7500, "mutual": 5000, "open": 0},
}
# center -> category map: {category: (profile, {center_or_motor_throat: weight})}
CENTER_MAP = {
    "harmony":       ("completion_bp_v2", {"g": 3, "solar_plexus": 2, "spleen": 1}),
    "heat":          ("completion_bp_v2", {"sacral": 3, "solar_plexus": 2, "ego": 1, "root": 1, "motor_throat": 1}),
    "communication": ("completion_bp_v2", {"throat": 3, "ajna": 2, "head": 1}),
    "alignment":     ("foundation_bp_v2", {"g": 3, "ajna": 1, "ego": 1}),
    "comfort":       ("completion_bp_v2", {"spleen": 3, "solar_plexus": 2, "g": 1}),
    "consistency":   ("foundation_bp_v2", {"sacral": 2, "root": 2, "spleen": 1}),
    "expansion":     ("completion_bp_v2", {"head": 2, "root": 2, "sacral": 1}),
    "creativity":    ("completion_bp_v2", {"throat": 2, "head": 2, "g": 1}),
    "drive":         ("completion_bp_v2", {"root": 3, "ego": 2, "sacral": 1, "motor_throat": 2}),
    "balance":       ("bilateral_completion_v2", {}),
}
# Type (aura class) contributions per category, per mille offsets from 500
TYPE_A = {
    #                 harm  heat  comm  alig  comf  cons  expa  crea  driv  bala
    "generator":  dict(zip(ORDER, [  50,   50,    0,    0,   50,  200,  -50,    0,  150,   50])),
    "projector":  dict(zip(ORDER, [  50, -150,  200,  150,    0, -150,  -50,   50, -200,   50])),
    "manifestor": dict(zip(ORDER, [-200,  150, -150,  -50, -200,  -50,  200,  100,  250, -100])),
    "reflector":  dict(zip(ORDER, [   0, -200,    0,  -50,    0, -200, -100,  -50, -250,  100])),
}
# pair interaction rules: (predicate name, {category: offset})
TYPE_I = [
    ("same_class",            {"alignment": 50}),
    ("generator_with_nonsacral", {"heat": 100, "comfort": -50}),
    ("generator_manifestor",  {"harmony": -50, "drive": 50}),
    ("generator_projector",   {"alignment": 100, "communication": 50}),
    ("projector_manifestor",  {"harmony": -50, "alignment": -50}),
    ("reflector_present",     {"balance": 50}),
]

CONFIG = {
    "config_id": "m10-relevance-centers-type-v2.0.0-candidate",
    "saturation_k_bp": 10000,
    "blend": {"channel": 60, "center": 25, "type": 15},
    "profiles": {row["profile_id"]: dict(row["responses"]) for row in MECH_V1["profiles"]},
    "signals": {row["signal_id"]: {"operation": row["operation"], "profile_id": row.get("profile_id"),
                                   "channels": [(c["channel_id"], c["weight"]) for c in row["channels"]]}
                for row in MECH_V1["signals"]},
    "category_weights": {row["category_id"]: list(row["weights"]) for row in MECH_V1["category_weights"]},
    "center_profiles": CENTER_PROFILES, "center_map": CENTER_MAP,
    "type_a": TYPE_A, "type_i": TYPE_I,
    # bands: {category: [c1, c2, c3, 100]} inclusive maxima; filled by calibration
    "bands": {k: [24, 49, 74, 100] for k in ORDER},
}
# Balance signals in v2 run over all 36 channels (membership list unused)
CONFIG["signals"]["equilibrium_score"]["channels"] = [(cid, 1) for cid in m.CHANNELS]
CONFIG["signals"]["counterweight_ratio"]["channels"] = [(cid, 1) for cid in m.CHANNELS]


def pair_predicates(cls_lo: str, cls_hi: str) -> set[str]:
    s = {cls_lo, cls_hi}
    out = set()
    if cls_lo == cls_hi: out.add("same_class")
    if "generator" in s and s != {"generator"}: out.add("generator_with_nonsacral")
    if s == {"generator", "manifestor"}: out.add("generator_manifestor")
    if s == {"generator", "projector"}: out.add("generator_projector")
    if s == {"projector", "manifestor"}: out.add("projector_manifestor")
    if "reflector" in s: out.add("reflector_present")
    return out


def signal_q(sig: dict, states: dict, cfg: dict) -> int:
    op = sig["operation"]
    if op == "weighted_state_sum_v1":          # v2 reading: saturating accumulation
        resp = cfg["profiles"][sig["profile_id"]]
        S = sum(w * resp[states[cid][0]] for cid, w in sig["channels"])
        K = cfg["saturation_k_bp"]
        return rhu(1000 * S, S + K) if S else 0
    if op == "twice_min_owner_mass_v1":         # over all mapped channels: 2*min(m_lo,m_hi)/(m_lo+m_hi)
        m_lo = sum(w for cid, w in sig["channels"] if states[cid][1] == "member_lo")
        m_hi = sum(w for cid, w in sig["channels"] if states[cid][1] == "member_hi")
        W = m_lo + m_hi
        return rhu(1000 * 2 * min(m_lo, m_hi), W) if W else 0
    if op == "companionship_em_mass_v1":        # mutual-state share of formed channels
        formed = sum(w for cid, w in sig["channels"] if states[cid][0] != "none")
        M = sum(w for cid, w in sig["channels"] if states[cid][0] in ("companionship", "electromagnetic"))
        return rhu(1000 * M, formed) if formed else 0
    raise ValueError(op)


def center_outcomes(lo: int, hi: int) -> tuple[dict, str, dict]:
    """Per-center outcome with owner for one_sided; motor->throat outcome; completion counts by giver."""
    union = lo | hi
    d_lo, d_hi, d_u = m.defined_centers(lo), m.defined_centers(hi), m.defined_centers(union)
    out = {}
    for c in m.CENTERS:
        if c not in d_u: out[c] = ("open", None)
        elif c in d_lo and c in d_hi: out[c] = ("shared", None)
        elif c in d_lo: out[c] = ("one_sided", "member_lo")
        elif c in d_hi: out[c] = ("one_sided", "member_hi")
        else: out[c] = ("mutual", None)
    mt_lo, mt_hi, mt_u = m.motor_to_throat(lo), m.motor_to_throat(hi), m.motor_to_throat(union)
    mt = "open" if not mt_u else "shared" if (mt_lo and mt_hi) else "one_sided" if (mt_lo or mt_hi) else "mutual"
    return out, mt, {"lo_gives": sum(1 for v in out.values() if v == ("one_sided", "member_lo") or v[0] == "mutual"),
                     "hi_gives": sum(1 for v in out.values() if v == ("one_sided", "member_hi") or v[0] == "mutual")}


def center_component(cat: str, outcomes: dict, mt: str, gives: dict, cfg: dict) -> int:
    profile, cmap = cfg["center_map"][cat]
    if profile == "bilateral_completion_v2":
        a, b = gives["lo_gives"], gives["hi_gives"]
        return rhu(1000 * 2 * min(a, b), a + b) if a + b else 0
    resp = cfg["center_profiles"][profile]
    W = sum(cmap.values())
    N = sum(w * resp[(mt if key == "motor_throat" else outcomes[key][0])] for key, w in cmap.items())
    return rhu(1000 * N, 10000 * W)


def type_component(cat: str, cls_lo: str, cls_hi: str, cfg: dict) -> int:
    t = 500 + cfg["type_a"][cls_lo][cat] + cfg["type_a"][cls_hi][cat]
    preds = pair_predicates(cls_lo, cls_hi)
    for name, offsets in cfg["type_i"]:
        if name in preds: t += offsets.get(cat, 0)
    return min(1000, max(0, t))


def band_of(score: int, maxima: list[int]) -> str:
    for edge, band in zip(maxima, ("Cool", "Open", "Warm", "Glow")):
        if score <= edge: return band
    return "Glow"


def score_pair(mask_a: int, mask_b: int, cfg: dict = CONFIG) -> dict:
    lo, hi = sorted((mask_a, mask_b))
    states = {cid: m.classify_channel(cid, lo, hi) for cid in m.CHANNELS}
    outcomes, mt, gives = center_outcomes(lo, hi)
    types = (m.derive_type(lo), m.derive_type(hi))
    cls = (m.aura_class(types[0]), m.aura_class(types[1]))
    q = {sid: signal_q(sig, states, cfg) for sid, sig in cfg["signals"].items()}
    a, b, c = cfg["blend"]["channel"], cfg["blend"]["center"], cfg["blend"]["type"]
    result = {"types": types, "classes": cls, "states": states, "centers": outcomes, "motor_throat": mt,
              "signals": q, "C": {}, "Z": {}, "T": {}, "scores": {}, "bands": {}}
    for cat in ORDER:
        s1, s2 = CAPS[cat]["inputs"]; b1, b2 = cfg["category_weights"][cat]
        C = rhu(b1 * q[s1] + b2 * q[s2], b1 + b2)
        Z = center_component(cat, outcomes, mt, gives, cfg)
        T = type_component(cat, cls[0], cls[1], cfg)
        N = a * C + b * Z + c * T                 # per-mille blend * 100
        score = min(100, max(0, rhu(N, 1000)))
        result["C"][cat], result["Z"][cat], result["T"][cat] = C, Z, T
        result["scores"][cat] = score
        result["bands"][cat] = band_of(score, cfg["bands"][cat])
    return result
```

### C.5 `measure.py` (SHA-256 `5663dede9bd6a0e9badcdd1e7b68b89a44304d06784dd62b43632526a2dfcbc8`)

Distribution, calibration, Reader v2 statistics, zeros and ties, AB↔BA and two-run checks, v1 comparison.

```python
"""Measure the Magic10 v2 candidate on the seeded reference population (analysis only)."""
from __future__ import annotations
import collections, copy, hashlib, json, pathlib, statistics, sys, time
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE.parent / "harness"))
import hdmech as m, m10v2 as v2
from hdchart import gates_local

OUT = HERE.parent / "out"
P = json.loads((OUT / "people.json").read_text())
masks = [m.mask_of(p["gates"]) for p in P["people"]]
pairs = P["pairs"]; N = len(pairs); ORDER = v2.ORDER; BANDS = ("Cool", "Open", "Warm", "Glow")


def run_all(cfg):
    t0 = time.time()
    res = [v2.score_pair(masks[a], masks[b], cfg) for a, b in pairs]
    return res, time.time() - t0


def canon(res):
    return hashlib.sha256(json.dumps([[r["scores"][k] for k in ORDER] for r in res]).encode()).hexdigest()


def calibrate(scores_by_cat, target):
    """Inclusive maxima per category closest to the target cumulative shares (Cool, Cool+Open, Cool+Open+Warm)."""
    cum = [target[0], target[0] + target[1], target[0] + target[1] + target[2]]
    lines = {}
    for cat, v in scores_by_cat.items():
        v = sorted(v); n = len(v)
        counts = collections.Counter(v); cdf = {}; acc = 0
        for s in range(0, 101):
            acc += counts.get(s, 0); cdf[s] = acc / n
        maxima = []
        prev = -1
        for c in cum:
            best = min(range(prev + 1, 100), key=lambda s: abs(cdf[s] - c))
            maxima.append(best); prev = best
        lines[cat] = maxima + [100]
    return lines


def mix(scores, maxima):
    n = len(scores); out = collections.Counter(v2.band_of(s, maxima) for s in scores)
    return {b: round(out[b] / n * 100, 1) for b in BANDS}


def reader_stats(res, lines):
    distinct = collections.Counter(); any_glow = 0; all_one = 0; warmglow = 0; profiles = collections.Counter()
    for r in res:
        bands = [v2.band_of(r["scores"][k], lines[k]) for k in ORDER]
        d = len(set(bands)); distinct[d] += 1; any_glow += "Glow" in bands; all_one += d == 1
        warmglow += sum(b in ("Warm", "Glow") for b in bands)
        profiles[tuple(bands.count(b) for b in BANDS)] += 1
    return {"distinct": {k: round(distinct[k] / N * 100, 1) for k in sorted(distinct)},
            "pairs_any_glow_pct": round(any_glow / N * 100, 1), "pairs_single_band_pct": round(all_one / N * 100, 1),
            "warm_or_glow_results_pct": round(warmglow / (10 * N) * 100, 1),
            "top_profiles": [(p, round(c / N * 100, 1)) for p, c in profiles.most_common(5)]}


def pct(v, p):
    v = sorted(v); return v[min(len(v) - 1, int(p / 100 * len(v)))]


def tie_rate(v):
    n = len(v); c = collections.Counter(v); return sum(x * x for x in c.values()) / (n * n)


def summarize(res, label):
    by = {k: [r["scores"][k] for r in res] for k in ORDER}
    rows = {}
    for k in ORDER:
        v = by[k]
        rows[k] = {"mean": round(statistics.mean(v), 1), "p10": pct(v, 10), "p50": pct(v, 50), "p90": pct(v, 90),
                   "p99": pct(v, 99), "min": min(v), "max": max(v), "zero_pct": round(v.count(0) / N * 100, 2),
                   "distinct_values": len(set(v)), "tie_rate_pct": round(tie_rate(v) * 100, 2)}
    return by, rows


if __name__ == "__main__":
    cfg = copy.deepcopy(v2.CONFIG)
    res, secs = run_all(cfg)
    h1 = canon(res)
    # two-run identity and AB<->BA identity
    res2, _ = run_all(cfg); h2 = canon(res2)
    rev = [v2.score_pair(masks[b], masks[a], cfg) for a, b in pairs]; h3 = canon(rev)
    assert h1 == h2 == h3, (h1, h2, h3)
    by, rows = summarize(res, "v2")
    report = {"pairs": N, "seconds": round(secs, 1), "two_run_sha256": h1, "abba_identical": h1 == h3,
              "config_id": cfg["config_id"], "v2_scores": rows}
    # component stats
    comp = {}
    for k in ORDER:
        comp[k] = {c: {"mean": round(statistics.mean(r[c][k] for r in res), 0), "zero_pct": round(sum(r[c][k] == 0 for r in res) / N * 100, 1),
                       "min": min(r[c][k] for r in res), "max": max(r[c][k] for r in res)} for c in ("C", "Z", "T")}
    report["components"] = comp
    # type pair distribution
    tp = collections.Counter(tuple(sorted(r["classes"])) for r in res)
    report["class_pairs_pct"] = {"+".join(k): round(v / N * 100, 1) for k, v in tp.most_common()}
    # calibration
    targets = {"A_30_35_25_10": (30, 35, 25, 10), "B_25_35_30_10": (25, 35, 30, 10), "C_40_30_20_10": (40, 30, 20, 10)}
    report["calibration"] = {}
    pooled = [s for k in ORDER for s in by[k]]
    for name, t in targets.items():
        per = calibrate(by, [x / 100 for x in t])
        glob = calibrate({"all": pooled}, [x / 100 for x in t])["all"]
        glines = {k: glob for k in ORDER}
        report["calibration"][name] = {
            "per_category_lines": per,
            "per_category_mix": {k: mix(by[k], per[k]) for k in ORDER},
            "per_category_reader": reader_stats(res, per),
            "global_lines": glob,
            "global_mix_by_category": {k: mix(by[k], glob) for k in ORDER},
            "global_reader": reader_stats(res, glines),
        }
    # v1 absolute lines applied to v2 scores, for reference
    report["v2_under_v1_lines"] = {k: mix(by[k], [24, 49, 74, 100]) for k in ORDER}
    # v1 comparison if available
    v1p = OUT / "v1_perpair.json"
    if v1p.exists():
        V1 = json.loads(v1p.read_text()); assert V1["order"] == ORDER
        v1by = {k: [r["scores"][i] for r in V1["results"]] for i, k in enumerate(ORDER)}
        report["v1_scores"] = {k: {"mean": round(statistics.mean(v), 1), "p50": pct(v, 50), "p90": pct(v, 90), "p99": pct(v, 99), "max": max(v),
                                   "zero_pct": round(v.count(0) / N * 100, 2), "distinct_values": len(set(v)), "tie_rate_pct": round(tie_rate(v) * 100, 2)} for k, v in v1by.items()}
        # rank agreement: Spearman between v1 and v2 per category
        def spearman(x, y):
            def ranks(v):
                order = sorted(range(len(v)), key=lambda i: v[i]); r = [0.0] * len(v); i = 0
                while i < len(v):
                    j = i
                    while j + 1 < len(v) and v[order[j + 1]] == v[order[i]]: j += 1
                    for k2 in range(i, j + 1): r[order[k2]] = (i + j) / 2 + 1
                    i = j + 1
                return r
            rx, ry = ranks(x), ranks(y); mx, my = statistics.mean(rx), statistics.mean(ry)
            num = sum((a - mx) * (b - my) for a, b in zip(rx, ry)); den = (sum((a - mx) ** 2 for a in rx) * sum((b - my) ** 2 for b in ry)) ** 0.5
            return round(num / den, 3)
        report["v1_v2_spearman"] = {k: spearman(v1by[k], by[k]) for k in ORDER}
    (OUT / "v2_measure.json").write_text(json.dumps(report, indent=1))
    print(json.dumps({k: report[k] for k in ("pairs", "seconds", "abba_identical", "two_run_sha256")}))
    print("v2 scores:"); [print(f"  {k:14}", rows[k]) for k in ORDER]
    print("components:"); [print(f"  {k:14}", comp[k]) for k in ORDER]
    print("class pairs:", report["class_pairs_pct"])
    for name in targets:
        c = report["calibration"][name]
        print(f"--- target {name}: per-category lines", c["per_category_lines"])
        print("    per-category reader:", c["per_category_reader"])
        print("    global lines", c["global_lines"], "global mix by category:", c["global_mix_by_category"])
        print("    global reader:", c["global_reader"])
    print("v2 under v1 lines:", report["v2_under_v1_lines"])
    if "v1_v2_spearman" in report: print("spearman v1 vs v2:", report["v1_v2_spearman"])
```

### C.6 `sensitivity.py` (SHA-256 `6c5f0e0b757033ec0ac6b6eb5e98a760f40c86b7c1081b9d936e6eda9ab1fcb7`)

±20% knob sensitivity with lines frozen.

```python
"""Sensitivity of the v2 candidate: move each knob by +/-20%, lines frozen at the base calibration."""
from __future__ import annotations
import copy, json, pathlib, statistics, sys
HERE = pathlib.Path(__file__).resolve().parent; sys.path.insert(0, str(HERE))
import hdmech as m, m10v2 as v2
OUT = HERE.parent / "out"
P = json.loads((OUT / "people.json").read_text()); masks = [m.mask_of(p["gates"]) for p in P["people"]]; pairs = P["pairs"]
ORDER = v2.ORDER
report = json.loads((OUT / "v2_measure.json").read_text())
LINES = report["calibration"]["A_30_35_25_10"]["per_category_lines"]
base_cfg = copy.deepcopy(v2.CONFIG); base_cfg["bands"] = LINES
base = [v2.score_pair(masks[a], masks[b], base_cfg) for a, b in pairs]
N = len(pairs)


def spearman(x, y):
    def ranks(v):
        order = sorted(range(len(v)), key=lambda i: v[i]); r = [0.0] * len(v); i = 0
        while i < len(v):
            j = i
            while j + 1 < len(v) and v[order[j + 1]] == v[order[i]]: j += 1
            for k in range(i, j + 1): r[order[k]] = (i + j) / 2 + 1
            i = j + 1
        return r
    rx, ry = ranks(x), ranks(y); mx, my = statistics.mean(rx), statistics.mean(ry)
    num = sum((a - mx) * (b - my) for a, b in zip(rx, ry)); den = (sum((a - mx) ** 2 for a in rx) * sum((b - my) ** 2 for b in ry)) ** 0.5
    return num / den


def compare(res):
    dscore = []; band_changes = 0; rho = []
    for k in ORDER:
        x = [r["scores"][k] for r in base]; y = [r["scores"][k] for r in res]
        dscore += [abs(a - b) for a, b in zip(x, y)]
        band_changes += sum(v2.band_of(a, LINES[k]) != v2.band_of(b, LINES[k]) for a, b in zip(x, y))
        rho.append(spearman(x, y))
    return {"mean_abs_dscore": round(statistics.mean(dscore), 2), "max_abs_dscore": max(dscore),
            "band_change_pct": round(band_changes / (10 * N) * 100, 1), "min_spearman": round(min(rho), 3)}


def scaled(v, f, cap=None):
    x = int(round(v * f)); return min(cap, x) if cap else x


knobs = {}
for f in (0.8, 1.2):
    tag = f"{int(round((f-1)*100)):+d}%"
    c = copy.deepcopy(base_cfg); c["saturation_k_bp"] = scaled(10000, f); knobs[f"saturation_K {tag}"] = c
    for part in ("channel", "center", "type"):
        c = copy.deepcopy(base_cfg); w = dict(c["blend"]); w[part] = scaled(w[part], f)
        tot = sum(w.values()); c["blend"] = {k: w[k] for k in w}
        # renormalise to 100 by adjusting the other two proportionally
        others = [k for k in w if k != part]; rest = 100 - w[part]; s = sum(w[k] for k in others)
        c["blend"][others[0]] = int(round(w[others[0]] / s * rest)); c["blend"][others[1]] = rest - c["blend"][others[0]]
        knobs[f"blend_{part} {tag} -> {c['blend']}"] = c
    c = copy.deepcopy(base_cfg)
    for p in c["center_profiles"].values():
        for st in ("one_sided", "shared", "mutual"): p[st] = scaled(p[st], f, 10000)
    knobs[f"center_profile_responses {tag}"] = c
    c = copy.deepcopy(base_cfg)
    for cls in c["type_a"]: c["type_a"][cls] = {k: scaled(v, f) for k, v in c["type_a"][cls].items()}
    knobs[f"type_A_offsets {tag}"] = c
    c = copy.deepcopy(base_cfg); c["type_i"] = [(n, {k: scaled(v, f) for k, v in d.items()}) for n, d in c["type_i"]]
    knobs[f"type_I_offsets {tag}"] = c
    c = copy.deepcopy(base_cfg)
    for p in c["profiles"].values():
        for st in ("companionship", "dominance", "compromise", "electromagnetic"): p[st] = scaled(p[st], f, 10000)
    knobs[f"signal_profile_responses {tag}"] = c
    # center weights: perturb each category's largest-weight center only (a scaled uniform change is a no-op)
    c = copy.deepcopy(base_cfg)
    for cat, (prof, cmap) in c["center_map"].items():
        if cmap:
            top = max(cmap, key=cmap.get); cmap[top] = max(1, scaled(cmap[top], f))
    knobs[f"center_top_weight {tag}"] = c
out = {}
for name, c in knobs.items():
    res = [v2.score_pair(masks[a], masks[b], c) for a, b in pairs]
    out[name] = compare(res); print(f"{name:60} {out[name]}")
(OUT / "v2_sensitivity.json").write_text(json.dumps(out, indent=1))
```

### C.7 `goldens.py` (SHA-256 `8f3186974d0a7b36baf6e6c37f2a7af80576544061dbad2cbf08570369d3f663`)

Live pairs and the adapted golden set.

```python
"""Expected v2 results for the live pairs and the adapted M10 golden set (analysis only)."""
from __future__ import annotations
import copy, json, pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE.parent / "harness"))
import hdmech as m, m10v2 as v2
from hdchart import gates_local
OUT = HERE.parent / "out"; ORDER = v2.ORDER
LINES = json.loads((OUT / "v2_measure.json").read_text())["calibration"]["A_30_35_25_10"]["per_category_lines"]
cfg = copy.deepcopy(v2.CONFIG); cfg["bands"] = LINES
PEOPLE = {"P1A/SYN-A": ("1990-01-01", "12:00", "Europe/Amsterdam"), "P1B/SYN-B": ("1985-07-15", "08:30", "Europe/London"),
          "P2A": ("1992-03-21", "18:45", "America/New_York"), "P2B": ("1978-11-02", "04:10", "Australia/Sydney")}
gates = {k: gates_local(*v, False) for k, v in PEOPLE.items()}
out = {"lines": LINES, "people": {}}
for k, g in gates.items():
    mk = m.mask_of(g)
    out["people"][k] = {"gates": g, "type": m.derive_type(mk), "defined_centers": sorted(m.defined_centers(mk)),
                        "motor_to_throat": m.motor_to_throat(mk), "components": [sorted(c) for c in m.definition_components(mk)]}
    print(k, out["people"][k])


def show(name, ma, mb, note=""):
    r = v2.score_pair(ma, mb, cfg); rb = v2.score_pair(mb, ma, cfg)
    assert r["scores"] == rb["scores"] and r["signals"] == rb["signals"]
    formed = {c: s for c, (s, o) in r["states"].items() if s != "none"}
    out[name] = {"note": note, "types": r["types"], "classes": r["classes"], "channels": formed,
                 "centers": {c: v[0] + ("" if v[1] is None else f"({v[1]})") for c, v in r["centers"].items()}, "motor_throat": r["motor_throat"],
                 "signals": r["signals"], "C": r["C"], "Z": r["Z"], "T": r["T"], "scores": r["scores"], "bands": r["bands"]}
    print(f"\n== {name} {note}\n types {r['types']} mt {r['motor_throat']}\n channels {formed}\n centers {out[name]['centers']}")
    print(" signals", r["signals"]); print(" C", r["C"]); print(" Z", r["Z"]); print(" T", r["T"])
    print(" scores", r["scores"]); print(" bands", r["bands"])
    return r

show("P1 (= SYN-A with SYN-B)", m.mask_of(gates["P1A/SYN-A"]), m.mask_of(gates["P1B/SYN-B"]), "live pair; same birth data as SYN-A/SYN-B")
show("P2", m.mask_of(gates["P2A"]), m.mask_of(gates["P2B"]), "live pair")
show("M10-G001 adapted: no relationship channels", m.mask_of({1}), m.mask_of({2}), "gates {1} and {2}: every channel none, both Reflectors")
show("M10-G002 adapted: homogeneous companionship", (1 << 64) - 1, (1 << 64) - 1, "both all 64 gates: every channel companionship, all centers shared")
# G003 adapted: balance ownership. lo owns three full channels hi lacks entirely; hi owns three others.
A = m.mask_of({2, 14, 7, 31, 21, 45}); B = m.mask_of({26, 44, 32, 54, 37, 40})
show("M10-G003 adapted: owner mass split 3/3", A, B, "A full on 02-14,07-31,21-45; B full on 26-44,32-54,37-40 -> dominance x6, split 3/3")
show("M10-G003 adapted: one-sided owner mass", A, m.mask_of({3}), "A full on three channels, B has gate 3 only -> all one-owner mass on A")
show("M10-G004 adapted: sparse sets", m.mask_of({5, 19, 20, 34, 43, 49}), m.mask_of({9, 12, 15, 22, 23, 52}), "Math Spec §9.5 member sets")
show("M10-G008 adapted: equal masks {1}", m.mask_of({1}), m.mask_of({1}), "distinct people, equal gate masks")
# G006 adapted: band boundaries per category at the frozen lines
out["M10-G006 adapted"] = {k: {"maxima": LINES[k], "boundary_cases": [(LINES[k][0], "Cool"), (LINES[k][0] + 1, "Open"), (LINES[k][1], "Open"), (LINES[k][1] + 1, "Warm"), (LINES[k][2], "Warm"), (LINES[k][2] + 1, "Glow"), (100, "Glow")]} for k in ORDER}
for k in ORDER:
    for s, b in out["M10-G006 adapted"][k]["boundary_cases"]: assert v2.band_of(s, LINES[k]) == b
print("\nG006 boundary assertions hold for all ten categories at the frozen lines")
(OUT / "v2_goldens.json").write_text(json.dumps(out, indent=1))
```

## Appendix D — Measurement outputs

SHA-256 of the analysis outputs as produced (kept in the analysis workspace, not committed; the figures in §§1, 4, 5 and 6 are transcribed from them):

* `people.json`: `bb7e336d2a3efe9b596f98d9df8467b97a0ef79b75c970842c72445fd24d4b19`
* `v1_distribution.json`: `61947a217df45faaa80da0d68f4d7e6d6319c802b2a5ce926b86cd01e34fd301`
* `v1_perpair.json`: `eba6413e74a58eff120a14ea9df6ce3feffba879a3cddb5fb85799bcb9e67b32`
* `v2_measure.json`: `e09becc8feae0cd0515923f0c53010d1296427b5296fac9e14b855f32b6b82dd`
* `v2_goldens.json`: `2bd75e39a64fee9e5a9d3ea3f05bb0a649ef618e1fae0baaeeabde5cccd76b91`
* `v2_sensitivity.json`: `ce648a855d8a6e71995760f746df2548e2eff82b498c182f7d9c6b4fda1f73cb`

### D.1 Calibrated inclusive maxima for every target mix measured (per category, `[Cool ≤, Open ≤, Warm ≤, 100]`)

```json
{
 "A_30_35_25_10": {
  "harmony": [
   35,
   45,
   54,
   100
  ],
  "heat": [
   36,
   46,
   56,
   100
  ],
  "communication": [
   36,
   48,
   58,
   100
  ],
  "alignment": [
   39,
   49,
   58,
   100
  ],
  "comfort": [
   34,
   45,
   53,
   100
  ],
  "consistency": [
   44,
   55,
   65,
   100
  ],
  "expansion": [
   32,
   43,
   53,
   100
  ],
  "creativity": [
   34,
   44,
   54,
   100
  ],
  "drive": [
   42,
   54,
   63,
   100
  ],
  "balance": [
   52,
   63,
   71,
   100
  ]
 },
 "B_25_35_30_10": {
  "harmony": [
   34,
   44,
   54,
   100
  ],
  "heat": [
   34,
   45,
   56,
   100
  ],
  "communication": [
   34,
   47,
   58,
   100
  ],
  "alignment": [
   37,
   48,
   58,
   100
  ],
  "comfort": [
   33,
   43,
   53,
   100
  ],
  "consistency": [
   41,
   54,
   65,
   100
  ],
  "expansion": [
   30,
   42,
   53,
   100
  ],
  "creativity": [
   32,
   43,
   54,
   100
  ],
  "drive": [
   40,
   52,
   63,
   100
  ],
  "balance": [
   49,
   62,
   71,
   100
  ]
 },
 "C_40_30_20_10": {
  "harmony": [
   38,
   46,
   54,
   100
  ],
  "heat": [
   39,
   48,
   56,
   100
  ],
  "communication": [
   40,
   50,
   58,
   100
  ],
  "alignment": [
   42,
   51,
   58,
   100
  ],
  "comfort": [
   38,
   46,
   53,
   100
  ],
  "consistency": [
   47,
   57,
   65,
   100
  ],
  "expansion": [
   35,
   45,
   53,
   100
  ],
  "creativity": [
   37,
   46,
   54,
   100
  ],
  "drive": [
   45,
   55,
   63,
   100
  ],
  "balance": [
   55,
   64,
   71,
   100
  ]
 },
 "D_30_40_25_5": {
  "harmony": [
   35,
   46,
   57,
   100
  ],
  "heat": [
   36,
   48,
   59,
   100
  ],
  "communication": [
   36,
   50,
   62,
   100
  ],
  "alignment": [
   39,
   51,
   61,
   100
  ],
  "comfort": [
   34,
   46,
   56,
   100
  ],
  "consistency": [
   44,
   57,
   68,
   100
  ],
  "expansion": [
   32,
   45,
   57,
   100
  ],
  "creativity": [
   34,
   46,
   57,
   100
  ],
  "drive": [
   42,
   55,
   65,
   100
  ],
  "balance": [
   52,
   64,
   74,
   100
  ]
 },
 "E_35_35_22_8": {
  "harmony": [
   37,
   46,
   55,
   100
  ],
  "heat": [
   37,
   48,
   57,
   100
  ],
  "communication": [
   38,
   50,
   59,
   100
  ],
  "alignment": [
   41,
   51,
   59,
   100
  ],
  "comfort": [
   36,
   46,
   54,
   100
  ],
  "consistency": [
   45,
   57,
   66,
   100
  ],
  "expansion": [
   34,
   45,
   55,
   100
  ],
  "creativity": [
   35,
   46,
   55,
   100
  ],
  "drive": [
   44,
   55,
   64,
   100
  ],
  "balance": [
   54,
   64,
   72,
   100
  ]
 }
}
```

### D.2 Global lines fitted to the pooled v2 scores (rejected in §4.3)

```json
{"A_30_35_25_10": [37, 49, 61, 100], "B_25_35_30_10": [35, 48, 61, 100], "C_40_30_20_10": [41, 51, 61, 100]}
```

### D.3 Sensitivity results (`v2_sensitivity.json`)

```json
{
 "saturation_K -20%": {
  "mean_abs_dscore": 2.04,
  "max_abs_dscore": 4,
  "band_change_pct": 18.1,
  "min_spearman": 0.996
 },
 "blend_channel -20% -> {'channel': 48, 'center': 32, 'type': 20}": {
  "mean_abs_dscore": 3.05,
  "max_abs_dscore": 11,
  "band_change_pct": 24.4,
  "min_spearman": 0.966
 },
 "blend_center -20% -> {'channel': 64, 'center': 20, 'type': 16}": {
  "mean_abs_dscore": 1.3,
  "max_abs_dscore": 5,
  "band_change_pct": 10.0,
  "min_spearman": 0.991
 },
 "blend_type -20% -> {'channel': 62, 'center': 26, 'type': 12}": {
  "mean_abs_dscore": 0.6,
  "max_abs_dscore": 3,
  "band_change_pct": 4.0,
  "min_spearman": 0.997
 },
 "center_profile_responses -20%": {
  "mean_abs_dscore": 2.6,
  "max_abs_dscore": 5,
  "band_change_pct": 21.6,
  "min_spearman": 0.994
 },
 "type_A_offsets -20%": {
  "mean_abs_dscore": 0.39,
  "max_abs_dscore": 2,
  "band_change_pct": 3.1,
  "min_spearman": 0.998
 },
 "type_I_offsets -20%": {
  "mean_abs_dscore": 0.04,
  "max_abs_dscore": 1,
  "band_change_pct": 0.3,
  "min_spearman": 0.999
 },
 "signal_profile_responses -20%": {
  "mean_abs_dscore": 2.02,
  "max_abs_dscore": 4,
  "band_change_pct": 17.9,
  "min_spearman": 0.997
 },
 "center_top_weight -20%": {
  "mean_abs_dscore": 0.44,
  "max_abs_dscore": 3,
  "band_change_pct": 3.6,
  "min_spearman": 0.994
 },
 "saturation_K +20%": {
  "mean_abs_dscore": 1.67,
  "max_abs_dscore": 3,
  "band_change_pct": 14.7,
  "min_spearman": 0.998
 },
 "blend_channel +20% -> {'channel': 72, 'center': 18, 'type': 10}": {
  "mean_abs_dscore": 3.1,
  "max_abs_dscore": 12,
  "band_change_pct": 21.4,
  "min_spearman": 0.978
 },
 "blend_center +20% -> {'channel': 56, 'center': 30, 'type': 14}": {
  "mean_abs_dscore": 1.28,
  "max_abs_dscore": 5,
  "band_change_pct": 10.1,
  "min_spearman": 0.991
 },
 "blend_type +20% -> {'channel': 58, 'center': 24, 'type': 18}": {
  "mean_abs_dscore": 0.55,
  "max_abs_dscore": 3,
  "band_change_pct": 3.9,
  "min_spearman": 0.997
 },
 "center_profile_responses +20%": {
  "mean_abs_dscore": 1.87,
  "max_abs_dscore": 4,
  "band_change_pct": 15.4,
  "min_spearman": 0.992
 },
 "type_A_offsets +20%": {
  "mean_abs_dscore": 0.35,
  "max_abs_dscore": 2,
  "band_change_pct": 2.8,
  "min_spearman": 0.998
 },
 "type_I_offsets +20%": {
  "mean_abs_dscore": 0.03,
  "max_abs_dscore": 1,
  "band_change_pct": 0.2,
  "min_spearman": 0.999
 },
 "signal_profile_responses +20%": {
  "mean_abs_dscore": 1.28,
  "max_abs_dscore": 3,
  "band_change_pct": 11.4,
  "min_spearman": 0.996
 },
 "center_top_weight +20%": {
  "mean_abs_dscore": 0.3,
  "max_abs_dscore": 2,
  "band_change_pct": 2.3,
  "min_spearman": 0.997
 }
}
```

### D.4 Goldens, full vectors (`v2_goldens.json`)

Channel states omit `none`; `centers` carry the one-sided owner; signals, `C`, `Z`, `T` are per mille; scores are points; bands use the lines of §4.4.

```json
{
 "lines": {
  "harmony": [
   35,
   45,
   54,
   100
  ],
  "heat": [
   36,
   46,
   56,
   100
  ],
  "communication": [
   36,
   48,
   58,
   100
  ],
  "alignment": [
   39,
   49,
   58,
   100
  ],
  "comfort": [
   34,
   45,
   53,
   100
  ],
  "consistency": [
   44,
   55,
   65,
   100
  ],
  "expansion": [
   32,
   43,
   53,
   100
  ],
  "creativity": [
   34,
   44,
   54,
   100
  ],
  "drive": [
   42,
   54,
   63,
   100
  ],
  "balance": [
   52,
   63,
   71,
   100
  ]
 },
 "people": {
  "P1A/SYN-A": {
   "gates": [
    1,
    4,
    6,
    7,
    9,
    10,
    13,
    14,
    21,
    26,
    38,
    39,
    41,
    48,
    49,
    52,
    54,
    55,
    58,
    61
   ],
   "type": "Generator",
   "defined_centers": [
    "root",
    "sacral",
    "solar_plexus"
   ],
   "motor_to_throat": false,
   "components": [
    [
     "root",
     "sacral",
     "solar_plexus"
    ]
   ]
  },
  "P1B/SYN-B": {
   "gates": [
    1,
    2,
    4,
    5,
    10,
    13,
    14,
    16,
    17,
    19,
    23,
    26,
    28,
    30,
    32,
    42,
    43,
    45,
    50,
    61,
    62
   ],
   "type": "Generator",
   "defined_centers": [
    "ajna",
    "g",
    "sacral",
    "throat"
   ],
   "motor_to_throat": false,
   "components": [
    [
     "g",
     "sacral"
    ],
    [
     "ajna",
     "throat"
    ]
   ]
  },
  "P2A": {
   "gates": [
    1,
    5,
    10,
    13,
    15,
    21,
    25,
    26,
    30,
    37,
    38,
    39,
    40,
    41,
    43,
    46,
    52,
    54,
    58,
    59,
    64
   ],
   "type": "Generator",
   "defined_centers": [
    "ego",
    "g",
    "root",
    "sacral",
    "solar_plexus"
   ],
   "motor_to_throat": false,
   "components": [
    [
     "ego",
     "root",
     "solar_plexus"
    ],
    [
     "g",
     "sacral"
    ]
   ]
  },
  "P2B": {
   "gates": [
    1,
    5,
    6,
    14,
    19,
    24,
    25,
    31,
    33,
    36,
    43,
    44,
    46,
    48,
    57,
    59,
    62,
    64
   ],
   "type": "Generator",
   "defined_centers": [
    "sacral",
    "solar_plexus"
   ],
   "motor_to_throat": false,
   "components": [
    [
     "sacral",
     "solar_plexus"
    ]
   ]
  }
 },
 "P1 (= SYN-A with SYN-B)": {
  "note": "live pair; same birth data as SYN-A/SYN-B",
  "types": [
   "Generator",
   "Generator"
  ],
  "classes": [
   "generator",
   "generator"
  ],
  "channels": {
   "02-14": "compromise",
   "09-52": "dominance",
   "16-48": "electromagnetic",
   "17-62": "dominance",
   "19-49": "electromagnetic",
   "21-45": "electromagnetic",
   "23-43": "dominance",
   "28-38": "electromagnetic",
   "30-41": "electromagnetic",
   "32-54": "electromagnetic",
   "39-55": "dominance"
  },
  "centers": {
   "ajna": "one_sided(member_hi)",
   "ego": "mutual",
   "g": "one_sided(member_hi)",
   "head": "open",
   "root": "one_sided(member_lo)",
   "sacral": "shared",
   "solar_plexus": "one_sided(member_lo)",
   "spleen": "mutual",
   "throat": "one_sided(member_hi)"
  },
  "motor_throat": "mutual",
  "signals": {
   "rapport_delta": 429,
   "resonance_strength": 0,
   "spark_intensity": 636,
   "momentum_flux": 0,
   "signal_clarity": 500,
   "exchange_density": 0,
   "vector_cohesion": 200,
   "axis_agreement": 692,
   "soothe_index": 429,
   "buffer_resilience": 0,
   "pattern_integrity": 636,
   "variance_stability": 429,
   "growth_tendency": 500,
   "horizon_reach": 500,
   "novelty_factor": 429,
   "expression_flow": 500,
   "willpower_current": 692,
   "focus_pressure": 636,
   "equilibrium_score": 800,
   "counterweight_ratio": 545
  },
  "C": {
   "harmony": 215,
   "heat": 318,
   "communication": 250,
   "alignment": 446,
   "comfort": 215,
   "consistency": 533,
   "expansion": 500,
   "creativity": 465,
   "drive": 664,
   "balance": 673
  },
  "Z": {
   "harmony": 792,
   "heat": 625,
   "communication": 625,
   "alignment": 700,
   "comfort": 875,
   "consistency": 800,
   "expansion": 350,
   "creativity": 450,
   "drive": 813,
   "balance": 889
  },
  "T": {
   "harmony": 600,
   "heat": 600,
   "communication": 500,
   "alignment": 550,
   "comfort": 600,
   "consistency": 900,
   "expansion": 400,
   "creativity": 500,
   "drive": 800,
   "balance": 600
  },
  "scores": {
   "harmony": 42,
   "heat": 44,
   "communication": 38,
   "alignment": 53,
   "comfort": 44,
   "consistency": 65,
   "expansion": 45,
   "creativity": 47,
   "drive": 72,
   "balance": 72
  },
  "bands": {
   "harmony": "Open",
   "heat": "Open",
   "communication": "Open",
   "alignment": "Warm",
   "comfort": "Open",
   "consistency": "Warm",
   "expansion": "Warm",
   "creativity": "Warm",
   "drive": "Glow",
   "balance": "Glow"
  }
 },
 "P2": {
  "note": "live pair",
  "types": [
   "Generator",
   "Generator"
  ],
  "classes": [
   "generator",
   "generator"
  ],
  "channels": {
   "05-15": "compromise",
   "06-59": "compromise",
   "10-57": "electromagnetic",
   "13-33": "electromagnetic",
   "26-44": "electromagnetic",
   "30-41": "dominance",
   "37-40": "dominance"
  },
  "centers": {
   "ajna": "open",
   "ego": "one_sided(member_lo)",
   "g": "one_sided(member_lo)",
   "head": "open",
   "root": "one_sided(member_lo)",
   "sacral": "shared",
   "solar_plexus": "shared",
   "spleen": "mutual",
   "throat": "mutual"
  },
  "motor_throat": "mutual",
  "signals": {
   "rapport_delta": 556,
   "resonance_strength": 556,
   "spark_intensity": 500,
   "momentum_flux": 0,
   "signal_clarity": 0,
   "exchange_density": 667,
   "vector_cohesion": 0,
   "axis_agreement": 0,
   "soothe_index": 429,
   "buffer_resilience": 500,
   "pattern_integrity": 200,
   "variance_stability": 0,
   "growth_tendency": 0,
   "horizon_reach": 0,
   "novelty_factor": 0,
   "expression_flow": 0,
   "willpower_current": 500,
   "focus_pressure": 0,
   "equilibrium_score": 500,
   "counterweight_ratio": 429
  },
  "C": {
   "harmony": 556,
   "heat": 250,
   "communication": 334,
   "alignment": 0,
   "comfort": 465,
   "consistency": 100,
   "expansion": 0,
   "creativity": 0,
   "drive": 250,
   "balance": 465
  },
  "Z": {
   "harmony": 625,
   "heat": 469,
   "communication": 500,
   "alignment": 600,
   "comfort": 708,
   "consistency": 800,
   "expansion": 350,
   "creativity": 550,
   "drive": 750,
   "balance": 571
  },
  "T": {
   "harmony": 600,
   "heat": 600,
   "communication": 500,
   "alignment": 550,
   "comfort": 600,
   "consistency": 900,
   "expansion": 400,
   "creativity": 500,
   "drive": 800,
   "balance": 600
  },
  "scores": {
   "harmony": 58,
   "heat": 36,
   "communication": 40,
   "alignment": 23,
   "comfort": 55,
   "consistency": 40,
   "expansion": 15,
   "creativity": 21,
   "drive": 46,
   "balance": 51
  },
  "bands": {
   "harmony": "Glow",
   "heat": "Cool",
   "communication": "Open",
   "alignment": "Cool",
   "comfort": "Glow",
   "consistency": "Cool",
   "expansion": "Cool",
   "creativity": "Cool",
   "drive": "Open",
   "balance": "Cool"
  }
 },
 "M10-G001 adapted: no relationship channels": {
  "note": "gates {1} and {2}: every channel none, both Reflectors",
  "types": [
   "Reflector",
   "Reflector"
  ],
  "classes": [
   "reflector",
   "reflector"
  ],
  "channels": {},
  "centers": {
   "ajna": "open",
   "ego": "open",
   "g": "open",
   "head": "open",
   "root": "open",
   "sacral": "open",
   "solar_plexus": "open",
   "spleen": "open",
   "throat": "open"
  },
  "motor_throat": "open",
  "signals": {
   "rapport_delta": 0,
   "resonance_strength": 0,
   "spark_intensity": 0,
   "momentum_flux": 0,
   "signal_clarity": 0,
   "exchange_density": 0,
   "vector_cohesion": 0,
   "axis_agreement": 0,
   "soothe_index": 0,
   "buffer_resilience": 0,
   "pattern_integrity": 0,
   "variance_stability": 0,
   "growth_tendency": 0,
   "horizon_reach": 0,
   "novelty_factor": 0,
   "expression_flow": 0,
   "willpower_current": 0,
   "focus_pressure": 0,
   "equilibrium_score": 0,
   "counterweight_ratio": 0
  },
  "C": {
   "harmony": 0,
   "heat": 0,
   "communication": 0,
   "alignment": 0,
   "comfort": 0,
   "consistency": 0,
   "expansion": 0,
   "creativity": 0,
   "drive": 0,
   "balance": 0
  },
  "Z": {
   "harmony": 0,
   "heat": 0,
   "communication": 0,
   "alignment": 0,
   "comfort": 0,
   "consistency": 0,
   "expansion": 0,
   "creativity": 0,
   "drive": 0,
   "balance": 0
  },
  "T": {
   "harmony": 500,
   "heat": 100,
   "communication": 500,
   "alignment": 450,
   "comfort": 500,
   "consistency": 100,
   "expansion": 300,
   "creativity": 400,
   "drive": 0,
   "balance": 750
  },
  "scores": {
   "harmony": 8,
   "heat": 2,
   "communication": 8,
   "alignment": 7,
   "comfort": 8,
   "consistency": 2,
   "expansion": 5,
   "creativity": 6,
   "drive": 0,
   "balance": 11
  },
  "bands": {
   "harmony": "Cool",
   "heat": "Cool",
   "communication": "Cool",
   "alignment": "Cool",
   "comfort": "Cool",
   "consistency": "Cool",
   "expansion": "Cool",
   "creativity": "Cool",
   "drive": "Cool",
   "balance": "Cool"
  }
 },
 "M10-G002 adapted: homogeneous companionship": {
  "note": "both all 64 gates: every channel companionship, all centers shared",
  "types": [
   "Manifesting Generator",
   "Manifesting Generator"
  ],
  "classes": [
   "generator",
   "generator"
  ],
  "channels": {
   "01-08": "companionship",
   "02-14": "companionship",
   "03-60": "companionship",
   "04-63": "companionship",
   "05-15": "companionship",
   "06-59": "companionship",
   "07-31": "companionship",
   "09-52": "companionship",
   "10-20": "companionship",
   "10-34": "companionship",
   "10-57": "companionship",
   "11-56": "companionship",
   "12-22": "companionship",
   "13-33": "companionship",
   "16-48": "companionship",
   "17-62": "companionship",
   "18-58": "companionship",
   "19-49": "companionship",
   "20-34": "companionship",
   "20-57": "companionship",
   "21-45": "companionship",
   "23-43": "companionship",
   "24-61": "companionship",
   "25-51": "companionship",
   "26-44": "companionship",
   "27-50": "companionship",
   "28-38": "companionship",
   "29-46": "companionship",
   "30-41": "companionship",
   "32-54": "companionship",
   "34-57": "companionship",
   "35-36": "companionship",
   "37-40": "companionship",
   "39-55": "companionship",
   "42-53": "companionship",
   "47-64": "companionship"
  },
  "centers": {
   "ajna": "shared",
   "ego": "shared",
   "g": "shared",
   "head": "shared",
   "root": "shared",
   "sacral": "shared",
   "solar_plexus": "shared",
   "spleen": "shared",
   "throat": "shared"
  },
  "motor_throat": "shared",
  "signals": {
   "rapport_delta": 800,
   "resonance_strength": 800,
   "spark_intensity": 667,
   "momentum_flux": 667,
   "signal_clarity": 789,
   "exchange_density": 789,
   "vector_cohesion": 800,
   "axis_agreement": 800,
   "soothe_index": 800,
   "buffer_resilience": 800,
   "pattern_integrity": 833,
   "variance_stability": 800,
   "growth_tendency": 667,
   "horizon_reach": 667,
   "novelty_factor": 667,
   "expression_flow": 789,
   "willpower_current": 714,
   "focus_pressure": 714,
   "equilibrium_score": 0,
   "counterweight_ratio": 1000
  },
  "C": {
   "harmony": 800,
   "heat": 667,
   "communication": 789,
   "alignment": 800,
   "comfort": 800,
   "consistency": 817,
   "expansion": 667,
   "creativity": 728,
   "drive": 714,
   "balance": 500
  },
  "Z": {
   "harmony": 250,
   "heat": 250,
   "communication": 250,
   "alignment": 1000,
   "comfort": 250,
   "consistency": 1000,
   "expansion": 250,
   "creativity": 250,
   "drive": 250,
   "balance": 0
  },
  "T": {
   "harmony": 600,
   "heat": 600,
   "communication": 500,
   "alignment": 550,
   "comfort": 600,
   "consistency": 900,
   "expansion": 400,
   "creativity": 500,
   "drive": 800,
   "balance": 600
  },
  "scores": {
   "harmony": 63,
   "heat": 55,
   "communication": 61,
   "alignment": 81,
   "comfort": 63,
   "consistency": 88,
   "expansion": 52,
   "creativity": 57,
   "drive": 61,
   "balance": 39
  },
  "bands": {
   "harmony": "Glow",
   "heat": "Warm",
   "communication": "Glow",
   "alignment": "Glow",
   "comfort": "Glow",
   "consistency": "Glow",
   "expansion": "Warm",
   "creativity": "Glow",
   "drive": "Warm",
   "balance": "Cool"
  }
 },
 "M10-G003 adapted: owner mass split 3/3": {
  "note": "A full on 02-14,07-31,21-45; B full on 26-44,32-54,37-40 -> dominance x6, split 3/3",
  "types": [
   "Manifesting Generator",
   "Projector"
  ],
  "classes": [
   "generator",
   "projector"
  ],
  "channels": {
   "02-14": "dominance",
   "07-31": "dominance",
   "21-45": "dominance",
   "26-44": "dominance",
   "32-54": "dominance",
   "37-40": "dominance"
  },
  "centers": {
   "ajna": "open",
   "ego": "shared",
   "g": "one_sided(member_lo)",
   "head": "open",
   "root": "one_sided(member_hi)",
   "sacral": "one_sided(member_lo)",
   "solar_plexus": "one_sided(member_hi)",
   "spleen": "one_sided(member_hi)",
   "throat": "one_sided(member_lo)"
  },
  "motor_throat": "one_sided",
  "signals": {
   "rapport_delta": 500,
   "resonance_strength": 0,
   "spark_intensity": 0,
   "momentum_flux": 0,
   "signal_clarity": 0,
   "exchange_density": 333,
   "vector_cohesion": 500,
   "axis_agreement": 333,
   "soothe_index": 333,
   "buffer_resilience": 0,
   "pattern_integrity": 0,
   "variance_stability": 333,
   "growth_tendency": 429,
   "horizon_reach": 0,
   "novelty_factor": 0,
   "expression_flow": 0,
   "willpower_current": 750,
   "focus_pressure": 0,
   "equilibrium_score": 1000,
   "counterweight_ratio": 0
  },
  "C": {
   "harmony": 250,
   "heat": 0,
   "communication": 167,
   "alignment": 417,
   "comfort": 167,
   "consistency": 167,
   "expansion": 215,
   "creativity": 0,
   "drive": 375,
   "balance": 500
  },
  "Z": {
   "harmony": 750,
   "heat": 688,
   "communication": 375,
   "alignment": 650,
   "comfort": 750,
   "consistency": 750,
   "expansion": 450,
   "creativity": 450,
   "drive": 625,
   "balance": 1000
  },
  "T": {
   "harmony": 600,
   "heat": 500,
   "communication": 750,
   "alignment": 750,
   "comfort": 500,
   "consistency": 550,
   "expansion": 400,
   "creativity": 550,
   "drive": 450,
   "balance": 600
  },
  "scores": {
   "harmony": 43,
   "heat": 25,
   "communication": 31,
   "alignment": 53,
   "comfort": 36,
   "consistency": 37,
   "expansion": 30,
   "creativity": 20,
   "drive": 45,
   "balance": 64
  },
  "bands": {
   "harmony": "Open",
   "heat": "Cool",
   "communication": "Cool",
   "alignment": "Warm",
   "comfort": "Open",
   "consistency": "Cool",
   "expansion": "Cool",
   "creativity": "Cool",
   "drive": "Open",
   "balance": "Warm"
  }
 },
 "M10-G003 adapted: one-sided owner mass": {
  "note": "A full on three channels, B has gate 3 only -> all one-owner mass on A",
  "types": [
   "Reflector",
   "Manifesting Generator"
  ],
  "classes": [
   "reflector",
   "generator"
  ],
  "channels": {
   "02-14": "dominance",
   "07-31": "dominance",
   "21-45": "dominance"
  },
  "centers": {
   "ajna": "open",
   "ego": "one_sided(member_hi)",
   "g": "one_sided(member_hi)",
   "head": "open",
   "root": "open",
   "sacral": "one_sided(member_hi)",
   "solar_plexus": "open",
   "spleen": "open",
   "throat": "one_sided(member_hi)"
  },
  "motor_throat": "one_sided",
  "signals": {
   "rapport_delta": 0,
   "resonance_strength": 0,
   "spark_intensity": 0,
   "momentum_flux": 0,
   "signal_clarity": 0,
   "exchange_density": 0,
   "vector_cohesion": 500,
   "axis_agreement": 0,
   "soothe_index": 0,
   "buffer_resilience": 0,
   "pattern_integrity": 0,
   "variance_stability": 0,
   "growth_tendency": 0,
   "horizon_reach": 0,
   "novelty_factor": 0,
   "expression_flow": 0,
   "willpower_current": 600,
   "focus_pressure": 0,
   "equilibrium_score": 0,
   "counterweight_ratio": 0
  },
  "C": {
   "harmony": 0,
   "heat": 0,
   "communication": 0,
   "alignment": 250,
   "comfort": 0,
   "consistency": 0,
   "expansion": 0,
   "creativity": 0,
   "drive": 300,
   "balance": 0
  },
  "Z": {
   "harmony": 375,
   "heat": 469,
   "communication": 375,
   "alignment": 600,
   "comfort": 125,
   "consistency": 300,
   "expansion": 150,
   "creativity": 450,
   "drive": 469,
   "balance": 0
  },
  "T": {
   "harmony": 550,
   "heat": 450,
   "communication": 500,
   "alignment": 450,
   "comfort": 500,
   "consistency": 500,
   "expansion": 350,
   "creativity": 450,
   "drive": 400,
   "balance": 700
  },
  "scores": {
   "harmony": 18,
   "heat": 18,
   "communication": 17,
   "alignment": 37,
   "comfort": 11,
   "consistency": 15,
   "expansion": 9,
   "creativity": 18,
   "drive": 36,
   "balance": 11
  },
  "bands": {
   "harmony": "Cool",
   "heat": "Cool",
   "communication": "Cool",
   "alignment": "Cool",
   "comfort": "Cool",
   "consistency": "Cool",
   "expansion": "Cool",
   "creativity": "Cool",
   "drive": "Cool",
   "balance": "Cool"
  }
 },
 "M10-G004 adapted: sparse sets": {
  "note": "Math Spec \u00a79.5 member sets",
  "types": [
   "Manifesting Generator",
   "Manifesting Generator"
  ],
  "classes": [
   "generator",
   "generator"
  ],
  "channels": {
   "05-15": "electromagnetic",
   "09-52": "dominance",
   "12-22": "dominance",
   "19-49": "dominance",
   "20-34": "dominance",
   "23-43": "electromagnetic"
  },
  "centers": {
   "ajna": "mutual",
   "ego": "open",
   "g": "mutual",
   "head": "open",
   "root": "shared",
   "sacral": "shared",
   "solar_plexus": "shared",
   "spleen": "open",
   "throat": "shared"
  },
  "motor_throat": "shared",
  "signals": {
   "rapport_delta": 333,
   "resonance_strength": 556,
   "spark_intensity": 0,
   "momentum_flux": 429,
   "signal_clarity": 500,
   "exchange_density": 333,
   "vector_cohesion": 0,
   "axis_agreement": 333,
   "soothe_index": 500,
   "buffer_resilience": 429,
   "pattern_integrity": 556,
   "variance_stability": 0,
   "growth_tendency": 0,
   "horizon_reach": 0,
   "novelty_factor": 500,
   "expression_flow": 333,
   "willpower_current": 0,
   "focus_pressure": 600,
   "equilibrium_score": 1000,
   "counterweight_ratio": 333
  },
  "C": {
   "harmony": 445,
   "heat": 215,
   "communication": 417,
   "alignment": 167,
   "comfort": 465,
   "consistency": 278,
   "expansion": 0,
   "creativity": 417,
   "drive": 300,
   "balance": 667
  },
  "Z": {
   "harmony": 583,
   "heat": 219,
   "communication": 458,
   "alignment": 400,
   "comfort": 250,
   "consistency": 800,
   "expansion": 150,
   "creativity": 300,
   "drive": 188,
   "balance": 1000
  },
  "T": {
   "harmony": 600,
   "heat": 600,
   "communication": 500,
   "alignment": 550,
   "comfort": 600,
   "consistency": 900,
   "expansion": 400,
   "creativity": 500,
   "drive": 800,
   "balance": 600
  },
  "scores": {
   "harmony": 50,
   "heat": 27,
   "communication": 44,
   "alignment": 28,
   "comfort": 43,
   "consistency": 50,
   "expansion": 10,
   "creativity": 40,
   "drive": 35,
   "balance": 74
  },
  "bands": {
   "harmony": "Warm",
   "heat": "Cool",
   "communication": "Open",
   "alignment": "Cool",
   "comfort": "Open",
   "consistency": "Open",
   "expansion": "Cool",
   "creativity": "Open",
   "drive": "Cool",
   "balance": "Glow"
  }
 },
 "M10-G008 adapted: equal masks {1}": {
  "note": "distinct people, equal gate masks",
  "types": [
   "Reflector",
   "Reflector"
  ],
  "classes": [
   "reflector",
   "reflector"
  ],
  "channels": {},
  "centers": {
   "ajna": "open",
   "ego": "open",
   "g": "open",
   "head": "open",
   "root": "open",
   "sacral": "open",
   "solar_plexus": "open",
   "spleen": "open",
   "throat": "open"
  },
  "motor_throat": "open",
  "signals": {
   "rapport_delta": 0,
   "resonance_strength": 0,
   "spark_intensity": 0,
   "momentum_flux": 0,
   "signal_clarity": 0,
   "exchange_density": 0,
   "vector_cohesion": 0,
   "axis_agreement": 0,
   "soothe_index": 0,
   "buffer_resilience": 0,
   "pattern_integrity": 0,
   "variance_stability": 0,
   "growth_tendency": 0,
   "horizon_reach": 0,
   "novelty_factor": 0,
   "expression_flow": 0,
   "willpower_current": 0,
   "focus_pressure": 0,
   "equilibrium_score": 0,
   "counterweight_ratio": 0
  },
  "C": {
   "harmony": 0,
   "heat": 0,
   "communication": 0,
   "alignment": 0,
   "comfort": 0,
   "consistency": 0,
   "expansion": 0,
   "creativity": 0,
   "drive": 0,
   "balance": 0
  },
  "Z": {
   "harmony": 0,
   "heat": 0,
   "communication": 0,
   "alignment": 0,
   "comfort": 0,
   "consistency": 0,
   "expansion": 0,
   "creativity": 0,
   "drive": 0,
   "balance": 0
  },
  "T": {
   "harmony": 500,
   "heat": 100,
   "communication": 500,
   "alignment": 450,
   "comfort": 500,
   "consistency": 100,
   "expansion": 300,
   "creativity": 400,
   "drive": 0,
   "balance": 750
  },
  "scores": {
   "harmony": 8,
   "heat": 2,
   "communication": 8,
   "alignment": 7,
   "comfort": 8,
   "consistency": 2,
   "expansion": 5,
   "creativity": 6,
   "drive": 0,
   "balance": 11
  },
  "bands": {
   "harmony": "Cool",
   "heat": "Cool",
   "communication": "Cool",
   "alignment": "Cool",
   "comfort": "Cool",
   "consistency": "Cool",
   "expansion": "Cool",
   "creativity": "Cool",
   "drive": "Cool",
   "balance": "Cool"
  }
 },
 "M10-G006 adapted": {
  "harmony": {
   "maxima": [
    35,
    45,
    54,
    100
   ],
   "boundary_cases": [
    [
     35,
     "Cool"
    ],
    [
     36,
     "Open"
    ],
    [
     45,
     "Open"
    ],
    [
     46,
     "Warm"
    ],
    [
     54,
     "Warm"
    ],
    [
     55,
     "Glow"
    ],
    [
     100,
     "Glow"
    ]
   ]
  },
  "heat": {
   "maxima": [
    36,
    46,
    56,
    100
   ],
   "boundary_cases": [
    [
     36,
     "Cool"
    ],
    [
     37,
     "Open"
    ],
    [
     46,
     "Open"
    ],
    [
     47,
     "Warm"
    ],
    [
     56,
     "Warm"
    ],
    [
     57,
     "Glow"
    ],
    [
     100,
     "Glow"
    ]
   ]
  },
  "communication": {
   "maxima": [
    36,
    48,
    58,
    100
   ],
   "boundary_cases": [
    [
     36,
     "Cool"
    ],
    [
     37,
     "Open"
    ],
    [
     48,
     "Open"
    ],
    [
     49,
     "Warm"
    ],
    [
     58,
     "Warm"
    ],
    [
     59,
     "Glow"
    ],
    [
     100,
     "Glow"
    ]
   ]
  },
  "alignment": {
   "maxima": [
    39,
    49,
    58,
    100
   ],
   "boundary_cases": [
    [
     39,
     "Cool"
    ],
    [
     40,
     "Open"
    ],
    [
     49,
     "Open"
    ],
    [
     50,
     "Warm"
    ],
    [
     58,
     "Warm"
    ],
    [
     59,
     "Glow"
    ],
    [
     100,
     "Glow"
    ]
   ]
  },
  "comfort": {
   "maxima": [
    34,
    45,
    53,
    100
   ],
   "boundary_cases": [
    [
     34,
     "Cool"
    ],
    [
     35,
     "Open"
    ],
    [
     45,
     "Open"
    ],
    [
     46,
     "Warm"
    ],
    [
     53,
     "Warm"
    ],
    [
     54,
     "Glow"
    ],
    [
     100,
     "Glow"
    ]
   ]
  },
  "consistency": {
   "maxima": [
    44,
    55,
    65,
    100
   ],
   "boundary_cases": [
    [
     44,
     "Cool"
    ],
    [
     45,
     "Open"
    ],
    [
     55,
     "Open"
    ],
    [
     56,
     "Warm"
    ],
    [
     65,
     "Warm"
    ],
    [
     66,
     "Glow"
    ],
    [
     100,
     "Glow"
    ]
   ]
  },
  "expansion": {
   "maxima": [
    32,
    43,
    53,
    100
   ],
   "boundary_cases": [
    [
     32,
     "Cool"
    ],
    [
     33,
     "Open"
    ],
    [
     43,
     "Open"
    ],
    [
     44,
     "Warm"
    ],
    [
     53,
     "Warm"
    ],
    [
     54,
     "Glow"
    ],
    [
     100,
     "Glow"
    ]
   ]
  },
  "creativity": {
   "maxima": [
    34,
    44,
    54,
    100
   ],
   "boundary_cases": [
    [
     34,
     "Cool"
    ],
    [
     35,
     "Open"
    ],
    [
     44,
     "Open"
    ],
    [
     45,
     "Warm"
    ],
    [
     54,
     "Warm"
    ],
    [
     55,
     "Glow"
    ],
    [
     100,
     "Glow"
    ]
   ]
  },
  "drive": {
   "maxima": [
    42,
    54,
    63,
    100
   ],
   "boundary_cases": [
    [
     42,
     "Cool"
    ],
    [
     43,
     "Open"
    ],
    [
     54,
     "Open"
    ],
    [
     55,
     "Warm"
    ],
    [
     63,
     "Warm"
    ],
    [
     64,
     "Glow"
    ],
    [
     100,
     "Glow"
    ]
   ]
  },
  "balance": {
   "maxima": [
    52,
    63,
    71,
    100
   ],
   "boundary_cases": [
    [
     52,
     "Cool"
    ],
    [
     53,
     "Open"
    ],
    [
     63,
     "Open"
    ],
    [
     64,
     "Warm"
    ],
    [
     71,
     "Warm"
    ],
    [
     72,
     "Glow"
    ],
    [
     100,
     "Glow"
    ]
   ]
  }
 }
}
```
