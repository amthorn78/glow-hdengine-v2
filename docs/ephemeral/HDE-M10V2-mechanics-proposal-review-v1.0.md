---
artifact_type: MECHANICS_PROPOSAL_REVIEW
artifact_version: "1.0"
logical_id: HDE-M10V2-MECHANICS-PROPOSAL-REVIEW
title: "Independent review of the Magic10 v2 mechanics proposal v1.0: correctness, engineering feasibility, scope and alchemical fidelity"
status: "REVIEW for Product Owner decision. Recommends ACCEPT WITH CHANGES; approves nothing. Changes no canon, code, catalog, test, schema, data or Notion page."
verdicts: "correctness SOUND WITH CHANGES; engineering feasibility SOUND WITH CHANGES; scope SOUND WITH CHANGES; alchemical fidelity SOUND WITH CHANGES; overall recommendation ACCEPT WITH CHANGES (no Blocker; four Major, sixteen Minor, five Observations)"
reviewed: "docs/ephemeral/HDE-M10V2-mechanics-proposal-v1.0.md on main at 0bf99656, SHA-256 dc064a2780042a98ebefa2b3dc3f326a8674c4185ac950881b5845503a3f3c2a; both values confirmed before any review work (the file is byte-identical on main at 84d6d1ca)"
review_prompt: "docs/ephemeral/HDE-M10V2-mechanics-proposal-review-prompt-v1.0.md (main at 84d6d1ca, #825)"
brief: "docs/ephemeral/HDE-M10V2-hd-math-specialist-design-brief-v1.0.md"
repository_head_read: "amthorn78/glow-hdengine-v2 origin/main 84d6d1ca (catalog/, math/, engine/ and tests/ unchanged between e2b7427f, the head the proposal read, 0bf99656 and 84d6d1ca); amthorn78/glow-docs edaa34c (docs/hd_refs, Human Design Reference Index v1.2.0)"
rails: "closed (LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev) for every script run, in a scratch clone of main at 0bf99656 with PyEphem 4.2.1 in an analysis-only virtual environment; no vendor call, no production system, no database, no Notion write; no outside web page fetched"
recorded: "2026-11-02T04:05Z"
producer: "Independent reviewer session (https://claude.ai/code/session_01Q789u1t8bov1DNsykHZ6vY). Not the proposal's author (session 01Q789tzD1cBKzL7p4Cec46s) and not the brief's author (session 01Q789tyhUaytmY7x273kwes); neither was contacted and no transcript was read."
---

# Independent review of the Magic10 v2 mechanics proposal (v1.0)

## 1. Summary and verdicts

| Dimension | Verdict |
| :- | :- |
| Correctness (mathematics, measurements, doctrine) | **SOUND WITH CHANGES** |
| Engineering feasibility | **SOUND WITH CHANGES** |
| Scope | **SOUND WITH CHANGES** |
| Alchemical fidelity | **SOUND WITH CHANGES** |
| **Overall recommendation to the Product Owner** | **ACCEPT WITH CHANGES** |

No Blocker was found. Four findings are Major and must change before adoption; the rest are Minor or Observations.

**What holds.** Every number in the proposal reproduces. I extracted the seven Appendix C scripts, verified their SHA-256 values, reran the v1 baseline, the v2 measurement, the goldens and the sensitivity analysis from a clone of `main` under closed rails, and matched the population, the per-pair v1 results, the two-run and AB↔BA hash (`9ec56f04…cb53`), the §4.4 lines, every table in §5 and §6, and Appendix D to the digit. The formula is integer-only, has one declared evaluation order, is symmetric by construction and fails closed as specified. Every doctrinal quotation exists at its stated page or segment and its words are in the source (a few are spliced or truncated, §3.4); the Type derivation is correct doctrine, and the any-route motor→Throat reading is the Complete Guide's own (printed p. 232: a Root power source bridged through Spleen and G "would immediately turn this Projector into a Manifestor"). No admitted source states a Type-pair rule, as the proposal says. The design can be built as pure Engine Core computation with catalogs injected, and the cache invalidation it relies on is real.

**What must change before adoption (Major).**

1. **Table 7a makes Type a per-person level, not a pair compatibility, and the effect is undisclosed** (R-01). Pairs containing a Manifestor reach Glow in `harmony`, the one band Reader v1 shows, 2.7% of the time against 9.1% overall; setting the single `manifestor`/`harmony` offset to 0 doubles that to 5.8%. Table 7a's rows sum to +500 per mille for Generators and −750 for Reflectors, so Generators are favoured in total by about nine points over Projectors and Manifestors. Doctrine describes auras; it does not say a Type's relationships score lower. The Product Owner asked for compatibility *between* aura types, which Table 7b gives and Table 7a does not.
2. **Reflector pairs cannot reach Glow in `balance` or `consistency` (0.0%) and almost never in `alignment` (0.9%), and average 45 points less in total; only `balance` is disclosed** (R-02). This comes from the center mechanics, not from the Type tables, and needs a Product Owner decision as a product effect on a 1.2% population.
3. **Two of the six pair-interaction rules rest on passages that do not support them, and no rejected alternative is presented** (R-05). Complete Guide p. 235's "natural relationship between the two" describes a Projector's not-self wish to be a Generator, not a Projector–Generator alignment; Generators' Course segment 15's "Manifestor propaganda" is cultural conditioning of Manifesting Generators, not a Generator–Manifestor pairing. The brief's route 2 requires the alternatives rejected; §2.4 and §3.7 give none, the "six stated principles" §2.4 promises do not appear in §3.7, and one basis clause is word for word a remark from the non-admitted blog the proposal says it does not rely on. Each misread citation alone is a Minor matter (at most 1.5 points; the tables are labelled inference); together with the missing alternatives the Q-3b record does not meet the brief's route 2, and re-examining the rows is the Q-3b decision itself.
4. **The search of the admitted collection behind "no admitted source states a rule" is undocumented and incomplete** (R-18). The claim is literally true, but the Rave Psychologist Reference Guide (A4; its Reference Index entry lists the Type domain, though the Index's Type routing row does not name it) carries the four aura keynotes and pairwise statements (Projectors and Generators "designed to influence each other"; Projectors "glance off" Manifestors and Reflectors; "A bond exists between Ms and Rs"), and Rave Cosmology VIII (A3) speaks of the Projector–Generator connection. None is recorded, a non-admitted blog's pair remarks are, and the register's conflicts line wrongly calls "resistant" a non-admitted word. The inference route was taken before the admitted collection was exhausted.

**What should change (Minor).** Double counting is never addressed although the brief's D-2 and the HDE Math Spec §7.3 invariant require it; an electromagnetic channel is scored in the channel component and again in the center component as the `mutual` outcome it creates, but my measurement shows the two components correlate weakly (0.02 to 0.44) and the center component carries information of its own, so what is missing is the justification, not a restructuring (R-07). The frozen band lines have their recalibration mechanism and a qualitative trigger disclosed in §10.1, but no Fermentation hook: no named observation, tolerance, minimum real population or PF09 row, and the brief's D-5 measurable targets are reported as values rather than set as pass/fail criteria; the lines should be labelled as calibrated on the synthetic reference population (R-08). Two deliverables are materially incomplete and must be completed in the Change before the Doc Delta and the implementation plan are drafted, which the Change Flow can do without re-deciding the design: the §7 canon delta list omits the v1 invariants v2 breaks (PF01 §5.2.4 "No default map assigns one Channel to both signals of the same category", §5.2.7's one-through-six channels per Balance signal and the `0..200` wire domain, §5.2.8's fixed invariants, §5.2.2's cache key, PF12 §2.9's `signal_scale`, loader rules and fixed-invariant list, PF04's band evidence entries) and the documents beyond the brief's six that pin v1 identities (PF05, PF14, PF19, PF07); applied as written, without the PF12 §2.9 loader-rule changes it omits, it would leave canon self-contradictory and still requiring the loader to reject the adopted configuration (R-03). The §8 impact inventory names one of fifteen surface groups fully and six partly, omitting two modules that fail at import on a per-category thresholds file, the loader's literal closure checks, the internal API contract change on `hdctl showcompat` and `POST /api/compat/v1`, the schema files, the consumer bundles, the evidence generators and most of the pinned tests, so the cost is understated (R-04). The open PF09 rows whose targets v2 changes (HDE-DIST008 Partial, HDE-CONJ010 Partial, a new Separation task in the shape of HDE-SEPA005) are not accounted for (R-06). The result schema is called "same shape" although the signal domain widens, and the v2 values of the fixed configuration fields are not given (R-19); the release cut says nothing about which evidence is regenerated and which captures stay frozen (R-20); three v2 rules have no governed home, and the `motor_throat` key would fail the proposal's own loader rule (R-21). The scripts do not run as published (hard-coded `REPO` path, undocumented layout, working-directory dependence, two missing calibration targets, unpublished statistics code) (R-10). The "5 of 5 vendor charts match" claim silently omits a sixth fixture that would not match, and no fixture tests the any-route rule (R-11). The required statement that viewer preferences and presets stay outside intrinsic scores is missing (R-22); the sensitivity analysis moves knobs in groups rather than each weight (R-23); and three single-home collisions are left open (derived Type beside the vendor `type`; the any-route predicate beside the governed direct set; §6.3 center tagging beside the new four-outcome contract), with the score-distribution utility (Candidate CRD item 13) not named as a dependency (R-09). The doctrinal example given for one-sided completion is, by the proposal's own rule, a mutual completion (R-15). The Reflector basis is mis-sourced (a wrong heading, a sleep-state sentence labelled source doctrine, "mirrors" without an admitted citation), and the record does not say that the admitted primary works give no mechanical Reflector definition, so the §3.4 Reflector branch rests on A5 corroboration (R-24). Two Type-derivation rules and the four-motor set are labelled source doctrine though they are derivation rules inferred from it (the Guide's text layer never names Manifesting Generators; the Root's motor status is stated only in A4 and A5), and I-6's rejected alternative is unrecorded (R-25).

**Decisions.** §8 of this review gives the effect on each of the proposal's Q-1 to Q-8 and adds four decisions the proposal does not list: whether Type may enter as a per-person level at all (Q-9); whether a pair with no connecting channel may score above 0 from Type alone (Q-10); whether the score-distribution utility is a dependency of the change (Q-11); and which PF09 rows the adoption re-targets (Q-12).

## 2. What was reviewed, and by whom

| Item | Value |
| :- | :- |
| Artifact | `docs/ephemeral/HDE-M10V2-mechanics-proposal-v1.0.md` |
| Commit | `0bf99656` on `main` (`0bf996565dc630d6cf356ab67e3cbbc39df30330`), an ancestor of the current head `84d6d1ca` |
| SHA-256 | `dc064a2780042a98ebefa2b3dc3f326a8674c4185ac950881b5845503a3f3c2a`, confirmed at `0bf99656`, at `84d6d1ca` and in the working tree before any other step |
| Reviewer session | `session_01Q789u1t8bov1DNsykHZ6vY` |
| Independence | the proposal's author (`01Q789tzD1cBKzL7p4Cec46s`) and the brief's author (`01Q789tyhUaytmY7x273kwes`) were not contacted; no transcript of either was read; the review prompt's §8 points were tested only after the findings below were formed |
| Method | own reading of the proposal (all sections and Appendices A–D), the brief, the two evidence records, the canon sections and Human Design references the prompt names; own reruns and re-measurements (§7); then eight independent read-only checkers in this session, each re-reading one dimension against the primary sources (Complete Guide citations, specialist citations, Appendix A against PF08, the aura-pairing gap, feasibility, canon deltas, brief compliance, alchemical fidelity). Their 48 merged points were ranked by severity; the twelve highest were each re-verified adversarially by a further checker against the primary sources, and a critic read the whole set. The first attempt at the merge, verification and critique stages failed on the account's usage limit and was resumed about two hours later with the sweep results reused unchanged. Every checker-derived point used in §6 I confirmed myself against the primary source before accepting it; where a verifier's severity differed from mine I re-checked the evidence and changed four ratings down (R-03, R-04, R-07, R-08) and two up (R-24, R-25) |
| Writes | this one file, through one pull request to `amthorn78/glow-hdengine-v2`; nothing else |

Section map: §3 correctness (review prompt §5.1), §4 engineering feasibility and scope (§5.2), §5 alchemical fidelity (§5.3), §6 findings table, §7 re-measurements with scripts and seeds, §8 effect on each Product Owner decision, §9 the points raised before the review (§8 of the prompt), §10 limits, nonclaims and canon relied on.

## 3. Correctness

### 3.1 Reproduction of the measurements

**What I did.** Extracted the seven Appendix C scripts and the two harness scripts the proposal depends on (`hdchart.py`, `distribution.py`, Appendices A and C of the score-range record) by taking the first fenced block after each heading, then hashed each file (contents plus one trailing newline). Laid them out as the scripts expect (`gen_people.py` and `v1_perpair.py` beside `harness/` and `out/`; `hdmech.py`, `m10v2.py`, `measure.py`, `sensitivity.py`, `goldens.py` in a sibling directory), changed exactly one line (`REPO` in `hdmech.py`, to my clone), and ran the chain from the clone root under closed rails with `PYTHONHASHSEED=0`. Commands, layout and the one-line patch are in §7.

**Hashes.** All seven Appendix C scripts and both harness scripts hash to the values the proposal and the score-range record state:

| Script | Stated SHA-256 (prefix) | Verified |
| :- | :- | :- |
| `gen_people.py` | `488dafea` | yes |
| `v1_perpair.py` | `6df1e78f` | yes |
| `hdmech.py` | `d5165bba` | yes (before the `REPO` patch; after it `ac5998bb…`) |
| `m10v2.py` | `507c6e67` | yes |
| `measure.py` | `5663dede` | yes |
| `sensitivity.py` | `6c5f0e0b` | yes |
| `goldens.py` | `8f318697` | yes |
| `hdchart.py` (record Appendix A) | `5969513b` | yes |
| `distribution.py` (record Appendix C) | `ee544853` | yes |

**Outputs.** `people.json` (`bb7e336d…`), `v1_perpair.json` (`eba6413e…`) and `v2_sensitivity.json` (`ce648a85…`) are byte-identical to the Appendix D digests: the population, its 20,000 pairs, every v1 per-pair result and all 18 sensitivity rows are the same bytes. `v1_distribution.json` and `v2_measure.json` differ in bytes only because each embeds a timing field (`pair_seconds`, `seconds`); every number in them matches. `v2_goldens.json` is identical in content to Appendix D.4 after sorting the `components` lists; its bytes vary with Python's hash seed because `hdmech.definition_components` iterates a `set` of center names (seed 0 gives `45ab9e98…`, seeds 1 and 2 give `07f6c437…`, the author's run gave `2bd75e39…`). The numbers never vary.

**Numbers confirmed.** Every figure I checked in §1, §2.3, §3.7, §4.3, §4.4, §5 and §6 of the proposal reproduces exactly:

| Claim (proposal locator) | Reproduced value |
| :- | :- |
| v1 baseline (§5): Cool 78.5 / Open 21.0 / Warm 0.4 / Glow 0.0; all-Cool pairs 19.3% | `distribution.py`: 0.785 / 0.21 / 0.004 / 0.0; 0.193 |
| v1 per-category means, p50/p90/p99, zero shares (§5.2 v1 columns) | all ten rows identical, including `balance` zero 41.8% |
| v2 two-run and AB↔BA identity hash (§1, §5.6) | `9ec56f0425e03eff6154501362921f6c89bb2cbe3501b503cc1d5516f699cb53`, `abba_identical: true` |
| v2 per-category mean, p10/p50/p90/p99, min/max, zero, distinct values (§5.2) | all ten rows identical (means 41.0, 41.9, 43.2, 45.0, 40.5, 49.9, 38.9, 40.1, 48.4, 57.4; distinct 66, 71, 67, 67, 66, 80, 69, 67, 77, 78) |
| component means `C` 303–529, `Z` 485–801, `T` 435–716 and zero shares (§5.2) | identical |
| per-category lines for target A (§4.4) and realised mixes | identical for all ten categories |
| overall v2 mix (§1) Cool 29.8 / Open 34.9 / Warm 25.3 / Glow 10.0 | 29.77 / 34.91 / 25.35 / 9.97 |
| Reader v2 distinct bands 0.1 / 7.4 / 48.2 / 44.3; any Glow 55.9%; Warm-or-Glow results 35.3% (§4.4, §5.4) | identical |
| alternative mixes B and C, lines and Reader figures (§4.4) | identical |
| alternative mixes D and E (§4.4) | identical, but only after adding the two targets to `measure.py`, which as published computes A, B and C only (see R-10) |
| global lines 37/49/61 and the divergent per-category mixes (§4.3: balance Glow 41.9%, Cool 7.7%; consistency Glow 18.5%; harmony Glow 1.2%; comfort Glow 1.1%; expansion Cool 44.5%) | identical |
| v2 under v1's absolute lines (§5.3) | all ten rows identical |
| Spearman v1 vs v2 0.82–0.91, `balance` 0.10 (§1) | 0.818–0.906; `balance` 0.097 |
| tie probability 2.3%–2.9% (§5.5) | 2.34%–2.91% |
| most common ten-band profiles 2%–2.4%; v1's five profiles 88% (§5.4) | 1.9%–2.4%; 87.7% |
| mean inter-category correlation v1 0.150, v2 0.153 (§5.5) | v1 0.150, v2 0.153 (my own code; `measure.py` does not compute it) |
| variance explained by `T` 0.4%–7.6%, `C` 40%–82%, `Z` 9%–31% (§3.7) | `T` 0.4–7.6, `C` 39.7–82.4, `Z` 9.1–31.0 (my own code; not produced by Appendix C) |
| Type shares 38.7 / 33.0 / 19.8 / 7.3 / 1.2, Solar Plexus 51.0%, 214 Type changes under direct-only (§2.3) | identical (187 Manifesting Generator→Generator, 27 Manifestor→Projector) |
| sensitivity table (§5.7), all nine knobs both directions | identical to `v2_sensitivity.json` |
| goldens: P1 and P2 scores and bands, G001, G002, G003 (split and one-sided), G004, G008 (§6) | identical, both orders |

AB↔BA and two-run identity therefore hold as stated. I also confirmed the proposal's description of P1 (11 channels: 6 electromagnetic, 4 dominance, 1 compromise; `ego` and `spleen` mutual, `sacral` shared, `head` open, five one-sided; motor→Throat mutual) from the golden vector.

**Verdict on the measurements.** Confirmed. Nothing in §1, §4.4, §5 or §6 is misstated. Three statistics the proposal states are not produced by the published scripts (inter-category correlation, variance shares, and the D and E target rows); I reproduced them with my own code (§7).

### 3.2 Formula integrity

| Check | Result | Evidence |
| :- | :- | :- |
| Integer-only arithmetic | Holds | `m10v2.py` uses only `int` operations; `rhu(n, d) = (2n + d) // (2d)`; no `float` anywhere in the scoring path (`m10v2.py` lines 26–28, 97–178) |
| `rhu` definition is `ROUND_HALF_UP` for `N ≥ 0`, `D > 0` | Holds | `floor((2N + D)/(2D)) = floor(N/D + 1/2)`; every numerator in the formula is a non-negative integer sum |
| Saturation values | Holds | one full channel 500, two 667, three 750, five 833 (`rhu(1000·S, S+K)` with `K = 10000`), as §3.5 states; G002 signals 667–833 confirm |
| One complete evaluation order | Holds | §3.3 steps 1–10; `score_pair` follows them in that order |
| Every value populated | Holds, one gap | all weights, profiles, offsets and lines are integers in the text; Table 7b lists offsets only for the categories a rule affects, and the prototype reads the others as `0` (`offsets.get(cat, 0)`, `m10v2.py` line 148). The catalog schema must list all ten categories per rule, or state that an absent category is `0`, otherwise this is a hidden default under HDE Math Spec §7.3 (R-13) |
| No hidden default elsewhere | Holds in the design; a placeholder in the prototype | profiles, center map, blend and lines are all explicit; `band_of` falls through to `Glow` only after the fourth maximum `100`, which every score ≤ 100 reaches. The prototype's `CONFIG` carries v1's `[24, 49, 74, 100]` as placeholder bands; `measure.py` fits the lines, and `goldens.py` and `sensitivity.py` replace the placeholder with the fitted lines, so no published number uses it |
| Fail-closed closure | Stated, not exercised | §3.1 states complete-or-fail-closed; the prototype is analysis code and does no validation, which is acceptable for a proposal |
| `A` symmetric, `I` predicates symmetric | Holds | `T_k = 500 + A_k[class_lo] + A_k[class_hi] + Σ I_k`; every predicate in `pair_predicates` is a set test |
| One clamp | Two clamps, one inactive | the score clamp (§3.3 step 8) and a clamp on `T` to `0..1000` (§3.7). With the published tables `T` reaches exactly 0 and exactly 1000 only in `drive` (two Reflectors, two Manifestors), so the `T` clamp never acts; §3.8's "one defensive clamp" is still inexact (R-13) |
| Rounding stages declared | Holds | four `ROUND_HALF_UP` stages: signal, channel component, center component, score; §3.8 names them |
| Equal masks | Holds | every channel `companionship` or `none`, every center `shared` or `open`, `gives_lo = gives_hi = 0`, equal Types (G008 confirms; same scores as G001) |
| `W = 0` and `F = 0` | Holds | both Balance signals return 0; G001 confirms |
| Pair of Reflectors | Holds | all centers open, all signals 0, scores are the Type floor only: 8, 2, 8, 7, 8, 2, 5, 6, 0, 11 (G001) |
| M10-G001 to G008 adaptations | Hold | every adapted expectation in §6 reproduces, including the per-category boundary matrix (G006) |
| Config identity | Inconsistent | §3.1 names `m10-relevance-centers-type-v2.0.0`; `m10v2.py` line 67 names `m10-relevance-centers-type-v2.0.0-candidate` (R-10) |

One consequence of the Type floor deserves the Product Owner's attention: a pair with no connecting channel and no composite definition at all (G001) scores 0 under v1 and 0 to 11 under v2, from the Type component alone. PF08 ("How you connect and where you connect determines the nature of the relationship") offers nothing for a pair that does not connect, so these points are a pure Type prior. This is a product choice, lawful under the brief, but §6 presents it as a mechanical expectation without saying so (R-12).

### 3.3 Type derivation

**Rule against doctrine.** The §3.4 rule (no definition → Reflector; Sacral defined → Generator, with a motor reaching the Throat → Manifesting Generator; otherwise Manifestor if a motor reaches the Throat, else Projector) is the standard Type mechanics. The Complete Guide states the Sacral split directly ("The moment you see an undefined Sacral Center right away you know that you're dealing with either a Manifestor or Projector or a Reflector", printed p. 229, verified); Winn's A5 table gives all five rows (segments 58–59, verified) and is used only to corroborate. The Reflector branch, though, has no mechanical definition in the admitted primary works: the Complete Guide's text layer names Reflectors on pp. 103, 122, 187 and 229 and never says they define nothing, and in the collection "no centers defined" occurs only in Winn (A5). The rule is right; the record should say that it rests on A5 corroboration and should state the gap (R-24).

**Any-route predicate.** The brief author asked whether any-route is the correct doctrine, since a direct-only rule would change 10.7% of Types. The Complete Guide passage the proposal cites (printed p. 232, verified in the PDF text layer) describes a split-definition Projector with 31/7 (Throat–G) and 54/32 (Root–Spleen) whose Root "is a power source that would immediately turn this Projector into a Manifestor" if "the bridge … a gate or a channel" joined the two areas; "all you need is one gate, the 57". Gate 57 completes 10-57 (G–Spleen), so the route Ra describes is Root → Spleen → G → Throat, three channels long, with no direct motor–Throat channel. The doctrine therefore supports **any connected definition route**, and a direct-only rule would contradict the central authority. The Generators' Course corroborates: it calls 20-34 "the only True Manifesting Generator" and adds "There are other variations" (segments 76–77, verified), so indirect routes are still Manifesting Generators. The governed Direct Motor→Throat set in HDE Math Spec §5.4.2.1 was never a Type rule; it serves "denominator logic" and "MUST NOT include two-hop routes" for that purpose. **Confirmed: any-route is correct, and Q-7's recommendation stands.** The Guide states the mechanism through one worked example rather than as a general rule, and the general statement is Winn's (A5), so I-5's label should read inference from source doctrine, corroborated by A5 (R-25). Keeping the direct set beside the new predicate is a single-home question (§5.4).

**Manifesting Generator as a Generator aura class.** The Generators' Course states "there are only four kinds of beings … There are two kinds of Generators. But Generators are Generators are Generators" (segment 15, verified), and the Complete Guide describes one Generator aura for "the two-thirds of humanity" (p. 230, verified). Pairing Manifesting Generators as Generators follows from those two statements (four kinds of beings; the two-thirds who share the enveloping aura include the one third who are Manifesting Generators), but it is an inference: the Complete Guide's text layer never names Manifesting Generators, no admitted work states their aura, and the nearest support, Holistic Analysis seg. 199 ("The aura is the Type"), is uncited. Deriving and reporting them separately costs nothing. **Confirmed as a sound inference; the label "source doctrine" and Q-3c's "with one aura" overstate it (R-25).**

**The "5 of 5 vendor charts match" claim.** I ran `hdmech.derive_type` on the gate lists of every chart in the repository that carries a Type:

| Chart | Vendor Type | Derived | Match | Notes |
| :- | :- | :- | :- | :- |
| `fixtures/hdapi/normalized/…012414Z` | Projector | Projector | yes | centers 2/2, one component (single) |
| `fixtures/hdapi/normalized/…015039Z` | Projector | Projector | yes | centers 6/6, two components (split) |
| `fixtures/hdapi/normalized/…015542Z` | Manifestor | Manifestor | yes | centers 6/6, three components (triple split); route is the direct 35-36 |
| `fixtures/charts/alice.json` | Manifesting Generator | Manifesting Generator | yes | hand-made fixture; its five listed centers do not follow from its six gates (derived three); route is the direct 20-34 |
| `tests/fixtures/bodygraph/source_invariance/vendor_chart_result.v1.json` | Manifesting Generator | Manifesting Generator | yes | hand-made fixture; listed centers inconsistent with gates; route is the direct 20-34 |
| `fixtures/charts/bob.json` | Projector | Manifesting Generator | **no** | hand-made fixture in the same directory as `alice.json`; its gates form 04-63, 09-52 and 12-22 while its own `channelsShort` lists only 4-63, so the fixture is internally inconsistent and not a valid test; **omitted from the proposal's count without disclosure** |
| `.audit_src/artifacts/live_vendor/20250929T022319Z_response.json` | Projector | Projector | yes | a real vendor response the proposal did not check; centers 4/4, split |
| `audit/qa/hde-epic037/checks/po-007/stdout.json` | Generator | Generator | yes | a resolved vendor chart the proposal did not check; centers 2/2 |

So the claim is true for the five charts named, two further vendor-backed charts also match, and one hand-made fixture that would not match was left out silently. More important for Q-7: **not one of these charts has an indirect motor→Throat route** (every Manifestor or Manifesting Generator above reaches the Throat through 20-34 or 35-36), so the fixtures cannot distinguish any-route from direct-only. The proposal says so in §10.1 ("No fixture exercises an indirect motor→Throat route"); the any-route choice rests on doctrine and population shares, not on this validation. The vendor Types of P1, P2, SYN-A and SYN-B are indeed absent from the OPS01 evidence (no `type` field in any of its 38 files), as §10.1 states. (R-11.)

### 3.4 Doctrine citations

**What I did.** Verified every row of the Appendix B register at its stated locator: the PF08 rows by exact-phrase search in `PF08-Reference-Human Design System.md`; the Complete Guide rows in a `pdftotext -layout` text layer of the admitted PDF, using the printed page numbers in the page footers (PDF page = printed page + 12, confirmed on pages 100, 101, 103, 106, 108, 122, 229–232 and 235); the specialist rows at their `## Source segment N` markers; and the nine center keynotes and all 36 channel keynotes of Appendix A against PF08 "The Centers" and "Channels", the two centers of each channel against `catalog/channels_v1.json`, and the "signals fed" column against `catalog/magic10_mechanics_v1.json`. Independent checkers in this session re-read every row.

**Result.** Every quoted passage exists at its stated page or segment, and the quoted words are present in the source; the exceptions are matters of form, listed in the table below (two splices in reverse source order, one dropped word, two truncated keynotes, one resolved uncertainty marker, two imprecise headings). Appendix A is exact on all 36 rows: channel identities, centers, keynotes and signal maps. Seven of the nine center keynotes are exact and two are truncated without an ellipsis. The claim-status labels follow the Reference Index tiers correctly: A2 and A3 as source doctrine, A5 only as corroboration, and every S-row names the D-row it corroborates; no rule rests on A5 alone.

Where the register needs correction is in *use*, not location:

| Row | Issue | Severity |
| :- | :- | :- |
| D-08 (PF08, "Most important for Johannes, together he has an emotional base. Together they connect and define the Heart to the Solar Plexus center") as the example of `one_sided` completion | The quoted words are exact, but the example is misclassified. In PF08 Johannes carries gate 40 (Personality Venus, line 584) and his Solar Plexus has no gate opened (line 925); Renate's single definition is Throat–Heart, 21-45 (line 1346), and she "open[s] the gate of Grace 22 … connecting to Johannes' 12th gate" (line 1356), with gate 37 likewise hers. The channels of Community (37-40) and Openness (12-22) are therefore electromagnetic, and the Solar Plexus is defined only together, which is the proposal's `mutual` outcome (§3.5); the one center Renate's definition conditions one-sidedly in that composite is the Heart. Running the proposal's own `center_outcomes` on the two gate sets gives `solar_plexus: mutual`, `ego: one_sided`. The `one_sided` concept is still grounded, by D-02 (a partner who "connects his Solar Plexus Center") and D-03 (a defined Spleen meeting an unconnected one) | Minor (R-15) |
| D-09 (PF08 center keynotes) | two of the nine are truncated inside quotation marks without an ellipsis: Head "Inspiration, initiation [and undergoing]", Throat "Action, metamorphosis [and unfolding]"; the other seven are exact | Observation (R-13) |
| D-14 (p. 235, "a natural relationship between the two") | In context Ra is describing what the open-Sacral child's not-self wants to *be*: "all this child wants to do is be a Manifestor; not a Generator. Most Projectors would rather be a Generator; it's a natural relationship between the two. Not in this case…". It is the Projector's affinity for Generator energy (the conditioning p. 104 calls unhealthy), not a statement about two people in relationship, and it carries no positive valence. Using it as the basis for `generator_projector` `alignment` +100 (Table 7b) and as a consistency check on the outside blog (O-02) is not supported | Minor (R-05) |
| D-25 (Generators' Course seg. 15, "most deeply conditioned by Manifestor propaganda") as basis for `generator_manifestor` | The passage is about Manifesting Generators' not-self being seduced by the culture's "manifesting propaganda" and pretending to be Manifestors. It says nothing about a Generator with a Manifestor | Minor (R-05) |
| D-17 (p. 105, "The Root Center is a pressure center like the Head Center") inside the "motors and the Throat" bullet | The Complete Guide never calls the Root a motor; its text layer has no four-motor list. The Root's motor status rests on p. 232 ("a power source that would immediately turn this Projector into a Manifestor"), which is functional support, and on A5 (Winn) and A4 (HD-CIRCUIT-01 "the four motors") for the word. The §2.2 bullet's "All source doctrine" is therefore slightly overstated for the Root; the derivation itself is standard and unaffected | Observation (R-13) |
| D-15 ("two-thirds of humanity are Generators") used at §2.3 to check the synthetic 71.7% | the source says "somewhere around two-thirds"; the proposal drops the hedge | Observation |
| S-01 (Winn's Type table) cited as corroboration for the any-route rule (I-5) | the table is silent on direct versus indirect routes. The passage in the same book that does corroborate any-route is segment 51 ("one is direct, the Channel 34-20, and the other meanders through the chart connecting the Channel 3-60 … 28-38 … 48-16"), which the proposal does not cite | Observation (R-13) |
| S-03 and the register's closing line "Conflicts: none found between admitted sources on the claims used" | Winn (chapter 9, segment 94) calls Manifestor auras "intense penetrating auras", where the Complete Guide (p. 230) and Table 7a reserve "penetrating" for Projectors. A vocabulary disagreement between an A5 source and the central authority is exactly what Index §10 asks to keep visible | Observation (R-13) |
| D-07 (PF08 Johannes/Renate) | the source carries an editorial uncertainty marker, "mental activity without \[clarity/relevance — unclear\]"; the proposal renders it "mental activity without \[relevance\]". The square brackets signal an editorial reading, but the "unclear" marker is dropped, which Index §10 ("Do not resolve disagreements silently") and PF08's own derivative-defect warnings counsel against. The mechanics the proposal takes from the passage (two hanging gates completing a channel together) do not depend on the word | Observation (R-13) |
| D-18, D-19, D-20 (pp. 106, 108, 102) | quotation form: D-18 and D-19 are spliced in reverse source order under an ellipsis (p. 106 reads "It's the thing that makes us feel good. It's the Spleen that gives us a sense of security in this life"; p. 108 reads "The Spleen is not a motor. The Ajna is not a motor. The Solar Plexus is a motor"); D-20 drops a repeated word ("This deep, deep desperateness to try to prove yourself"). Meaning unaffected; Index §10 asks for quotation from the verified location | Observation (R-13) |
| D-22 (p. 122, "deeply, deeply, deeply open") | the source sentence is "Amongst waking raves 1.4% are Reflectors. Among sleeping raves 35% are Reflectors; deeply, deeply, deeply open. We are incredibly vulnerable when we sleep." The openness is predicated of the sleeping state; using it as the Type's descriptor is a stretch, and the register's heading ("The Sleep State is Our Deepest Conditioning Process") stands on p. 116, not p. 122. The 1.4% figure is correct. The Complete Guide never gives a mechanical Reflector definition ("no centers defined" is A5 only, Winn), which the §3.4 rule nevertheless states correctly as standard mechanics | Minor (R-24) |
| D-13, D-23 locators | D-13 names the heading of p. 231 for sentences on p. 232 (same chart example; page correct); D-23's range pp. 113–114 omits p. 115, which carries the interpenetration statement, and no rule cites D-23 | Observation |
| Table 7a `reflector` basis "mirrors" | no admitted citation; "mirror" for Reflectors appears in the collection only in Winn (A5, uncited) and in the non-admitted blog the proposal says it does not rely on | Minor (R-24) |
| §2.4 "six stated principles (§3.7)" | §3.7 states no principles (its only six-item list is the six pair rules, with one-phrase bases) and gives no derivation of the offset sizes (±50 to ±250); the brief's route 2 asks that each inference step be tied to doctrine and the resulting rule stated | Major (R-05) |
| I-6 ("Manifesting Generator shares the Generator aura class") labelled source doctrine | the Generators' Course sentence is about Strategy ("their Strategy is the same"), and p. 230 is silent on Manifesting Generators; the nearest admitted support is Holistic Analysis Fundamentals, "The aura is the Type. The aura is representing the mechanics of the Type" (segment 199, uncited). Winn (A5) draws a relational distinction the merge erases: Manifestors do well "with someone who is also self-possessed and independent, namely other Manifestors or Manifesting Generators" (segment 104). The merge is the right call for the reasons given in §3.3; the label should read inference from doctrine, and Q-3c should drop "with one aura" | Minor (R-25) |
| Unrecorded admitted material on Type relations | Winn (A5) has several statements on how Types relate in relationship (Generator–Projector; Generators "reliant on relationships with others"; Manifestors with Manifestors or Manifesting Generators, segment 104; Reflectors in "a stable relationship with a Generator"), and the Generators' Course (A3) has "when Manifestors ruled, it was so easy to have Generators as slaves … 'Be like me'" (segment 7) and "a Projector isn't even useful until a Generator wakes up. Because only then can they have a legitimate relationship" (segment 38). None states a rule, so the gap claim stands; but the register records pair remarks from a non-admitted blog while omitting these admitted ones | Major (R-18) |
| HD-SELF-01 | the brief's D-3 routes Type through HD-TYPE-01 and HD-SELF-01; the proposal neither cites HD-SELF-01 nor lists it as read and not used | Observation (R-13) |

**Is §2.6 complete?** The brief asked for every outside-source and inferred rule to be listed together. §2.6 lists eleven rules. Two labels deserve a second look:

* **I-5** ("Type is derived with any connected definition route") and **I-6** ("Manifesting Generator shares the Generator aura class") are labelled *source doctrine*. The underlying facts are doctrine (p. 232; Generators' Course seg. 15), but the rules as stated are Glow's derivation rules built from that doctrine, and the Reference Index §9 records that Type depth "is not exhaustive". For I-5 the Guide gives the mechanism through one worked example and no general rule (the general statement is Winn's, A5); for I-6 the Guide's text layer never names Manifesting Generators, no admitted work states their aura, the nearest support (Holistic Analysis seg. 199, "The aura is the Type") is uncited, and no rejected alternative is recorded, while Q-7 records one for I-5. Both should be labelled analyst inference from source doctrine, corroborated by A5; as labelled they would enter the Math Spec as doctrine (Minor, R-25).
* Three product choices appear in §2 and §3 but not in §2.6: the four-motor set `MOTORS` (doctrine for three centers and functional for the Root, as above), the choice of reference population and seed (part of I-11 by implication), and the Type floor of a no-connection pair (a consequence of I-7/I-9, see §3.2). None is presented as doctrine, so the list is honest; the motor set belongs in it, since the Root's motor status is stated only in A4 and A5 (Minor, R-25); the rest is slight incompleteness (Observation, R-13; the floor is R-12).

### 3.5 The aura-pairing gap

**My own search.** I searched every Markdown work in `docs/hd_refs/` (20 companions; the Index's count of 29 includes archived and excluded works) and the Complete Guide text layer for: any Type name within one sentence of another Type name and a relationship word (relationship, partner, couple, marriage, lover, attract, compatib-, together, connection); "aura" near relationship words; "composite", "connection chart", "relationship chart", "partnership"; and the aura descriptors (enveloping, penetrating, repelling, sampling). The word "compatib-" occurs in no admitted work (only in the Reference Index itself). PF08 contains no occurrence of Projector, Manifestor or Reflector. The Complete Guide's clearest two-Type passage is p. 104 (the Projector in the Generator's aura), which is about conditioning and health, not about pairing; p. 235 is about the Projector's not-self wish (above). The Generators' Course, Holistic Analysis Fundamentals, Design Resonance Mapping and Winn describe each Type's aura and, in Winn, how a practitioner should work with each Type. An independent checker ran a broader sweep (seven search angles, including the abbreviations "Ps", "Gs", "Ms", "Rs" the Rave Psychology material uses), and I verified every hit it reported in the sources. **Confirmed: no admitted source states a Type-pair rule, matrix, valence or score.** The Reference Index already records the gap (§9: "Relationship/composite teaching is partial … do not establish a general compatibility score"), and Design Resonance Mapping (HD-SYN-02) is correctly excluded as "establishes no app compatibility score".

**What the admitted collection does contain, and the proposal does not record.** Two admitted works carry qualitative Type-pair teaching that bears directly on Table 7b, and neither appears anywhere in the proposal:

| Source (tier, index routing) | Passage | Bears on |
| :- | :- | :- |
| HD-RP-05, Rave Psychologist Reference Guide for Practitioners (A4; its register entry lists M03 Type among its domains and "Coverage: … Type … Affinity priority charts", though the Index §4 M03 routing row itself names only the Complete Guide, HD-TYPE-01 and HD-SELF-01, so only a search of the collection, which the proposal's universal negative presupposes, would have surfaced it) | aura keynotes for all four Types: "Aura: Open & Enveloping" (Generator, line 443), "Aura: Focused & Probing" (Projector, 523), "Aura: Closed & Repelling" (Manifestor, 605), "Aura: Resistant & Sampling" (Reflector, 663); "Interaction with others is determined by aura" (431); Projectors: "Only designed to really probe the open aura of Generators. Ps and Gs, 90% of the world, are designed to influence each other, are most deeply penetrated and conditioned by each other" (558–562); "Is a need for a formality (respect) in the way Gs and Ps deal with each other" (566); "Can't penetrate well into Reflectors and Manifestors; there is a tendency to glance off them rather than have real lasting impact. With Ms, tend to backup and never come forward again" (570–573); Manifestors: "Ms are conditioned by other beings, but it does not have a great deal of power" (626); Reflectors: "They can always skim along on the edges of the social communion rooted in the Generator and the Projector" (676–677), "A bond exists between Ms and Rs in their connection to and operation in the program" (688) | `generator_projector` (supported, as mutual conditioning with a need for formality); `projector_manifestor` (supported in sign: glance off, back up); the absent `manifestor_reflector` rule ("a bond exists"); the Reflector basis ("resistant" is an admitted keynote, which the register's conflicts line denies) |
| HD-COS-01, Rave Cosmology VIII (A3; "RETAIN — context only"; the Index warns "Not a default chart-reading or compatibility manual") | "the Projector-Generator connection, how profound that's intended to be" (lines 6746–6747); "think about types relative to their auras … the generator, we're dealing with this enveloping aura" (7881 ff.); "I'm a manifestor with a repelling aura. Projectors are only good one at a time. It's a focused aura … reflectors are just gliding by" (7966–7970); "the relationship between the projector and the generator is one that can be so profound" (7972–7975); "Projectors are the most important people to understand generators, because they can actually make things possible for the generator" (8507–8510) | `generator_projector` (context-only support for a positive sign) |

Neither states a rule, matrix, valence table or score, so the proposal's gap sentence is literally true. But the brief's method is "Human Design doctrine comes only from the admitted reference collection … then the admitted specialist teaching the index routes to each domain", and route 2 (inference) is open only "when the admitted collection does not provide". The proposal records no search of the collection (its §10.1 bounds only the outside search; §10.3 lists five works read and two not used), goes to outside pages and inference, and then records pair remarks from a non-admitted blog while the admitted A4 booklet's pair statements, which say similar things with a tier the Index admits for corroboration, go unrecorded. Its conflicts line is also wrong on one point: "where O-02 adds 'resistant' (Reflector) … v2 relies only on the admitted words" — "Resistant & Sampling" is the admitted HD-RP-05 keynote. A Product Owner deciding Q-3a and Q-3b from §2.4 alone would believe the collection is silent on Type pairs, when it is silent only on a *rule*. **This is a Major finding (R-18)**: before Tables 7a and 7b are adopted, the admitted material must be put in the register (A4 as corroboration, A3 context-only with the Index's caveat), each Table 7b row re-tied to it or labelled as having no admitted support, and the gap statement restated precisely.

**The outside-source record (Appendix B, O-01 to O-03).** I did not fetch the three URLs (the review runs offline), so I assess the record as a record. It meets the brief's route-1 discipline: it names each page, its date and access date, states that the Jovian Archive product page publishes no passage and that the blog cannot be verified as Ra's text, and relies on neither for any rule. Recording what the blog says "for the reviewer" is harmless provided it is never promoted to a basis; the one place it is used, as a consistency check for Tables 7a/7b (O-02 "consistent with"), leans on the D-14 reading corrected above and should go. One Table 7b basis clause, "Manifestor initiates, Generator responds", is word for word the O-03 remark, and four of the six pair rules have a counterpart in the recorded blog remarks; the proposal says the blog was "consistent with, but not the basis of" the inferences, and nothing in the record shows the order of work, so the revision should state it and tie each row to admitted doctrine step by step, as the brief's route 2 requires (R-05).

**The acquisition recommendation (Q-3b).** Ra Uru Hu's *Type Sexual Signatures* (Jovian Archive, Ibiza 2008) is, by the proposal's record, a primary Ra lecture on Type in relationship, which is exactly the kind of source the Reference Index §9 asks for ("Obtain dedicated direct partnership/composite source before claiming such coverage") and §10 permits adding (identify work, author, publisher, edition, completeness; propose a role). The proposal names the work, author, publisher and year but not the edition or format it would acquire, nor the role it proposes for it; the Index's intake rule wants those, and the content is unseen (the basis is one product-page sentence). Two further points for the intake record: the work's declared subject sits against the brief's "no … sexual … claims" boundary, so its proposed role must be doctrine on Type in relationship and nothing more; and the admitted HD-RP-05 Type pages cite their own source lecture (RPY1S2L5, Rave Psychology Year 1 Semester 2 Lecture 5, lines 509, 587, 641), a more targeted candidate the proposal did not surface. **Recommendation sound; intake record incomplete** (Observation, R-13). If acquired, Tables 7a/7b should be re-derived from it before the pair rules are treated as more than placeholders, which is a Product Owner sequencing decision (Q-3b).

### 3.6 Inference quality: Tables 7a and 7b

The brief's route 2 requires each inferred rule to be tied to cited doctrine, presented as Glow product synthesis, with the rejected alternatives given. I read each row against the passages it cites, which I verified in the sources (§3.4).

**Table 7a (per-class offsets).**

| Class | What the cited doctrine says | What the row does | Does the row follow? |
| :- | :- | :- | :- |
| generator | enveloping, open aura that "brings everything inward" (p. 230); "a prime motor … doesn't give up" (Generators' Course seg. 1); responds, does not initiate | `consistency` +200, `drive` +150, `harmony`/`heat`/`comfort`/`balance` +50, `expansion` −50 | `consistency` and `drive` follow from the sustained motor. The +50s on `harmony`, `heat`, `comfort` and `balance` rest on "takes everything in", which describes conditioning, not relational warmth. `expansion` −50 ("responds rather than initiates") is a weak link; Ra's Generator course is about response, not about resistance to growth. Row sum +500: the only class with a net positive level |
| projector | focused, penetrating aura; recognizes and guides (p. 230; Holistic seg. 28); non-energy, dependent (p. 229) | `communication` +200, `alignment` +150, `heat` −150, `consistency` −150, `drive` −200 | the signs follow the descriptors. But the three negatives read the Projector's own lack of a motor as a *pair* deficit, while p. 104 says the Projector in a Generator's aura has that energy amplified; rule `generator_with_nonsacral` adds back +100 on `heat` only |
| manifestor | closed aura, "pushing off quality", "a barrier" (p. 230); a motor to the Throat; initiates | `harmony` −200, `comfort` −200, `communication` −150, `balance` −100, `drive` +250, `expansion` +200, `heat` +150, `creativity` +100 | the signs follow the descriptors, with the largest negatives on the two categories closest to approachability. Doctrine says Manifestors are hard to approach; it does not say their relationships have less harmony once formed. The row drives the Reader v1 effect in §4.10 |
| reflector | sampling aura, deeply open (p. 122; Holistic seg. 117); no fixed definition | `drive` −250, `heat` −200, `consistency` −200, `expansion` −100, `balance` +100 | the negatives restate the absence of a motor, which the center component already reads directly from the gate set: a Reflector pair has no `shared` center and no bilateral completion. The row therefore counts the same fact twice (R-07, §4.6). `balance` +100 ("mirrors") is inference without a passage |

**Table 7b (pair interactions).**

| Rule | Cited basis | Assessment |
| :- | :- | :- |
| `same_class` `alignment` +50 | "like auras meet alike" | no passage cited; pure inference |
| `generator_with_nonsacral` `heat` +100, `comfort` −50 | p. 104: the Projector in the Generator's aura takes in and amplifies the Sacral energy and "does not know when enough is enough" | **follows**, and it is the one rule whose cited passage is actually about two Types in each other's aura; the comfort penalty catches the unhealthy side Ra describes |
| `generator_manifestor` `harmony` −50, `drive` +50 | Generators' Course seg. 15: Manifesting Generators are "the most deeply conditioned by Manifestor propaganda" | **misapplied.** The passage (verified) is about Manifesting Generators being seduced by the culture's "manifesting propaganda" and pretending to be Manifestors; it says nothing about a Generator and a Manifestor in relationship; the row's second clause, "Manifestor initiates, Generator responds", is word for word the O-03 blog remark recorded as not relied on |
| `generator_projector` `alignment` +100, `communication` +50 | p. 235: "Most Projectors would rather be a Generator; it's a natural relationship between the two" | **overread.** In context (verified) Ra is describing the open-Sacral child's not-self wish: "all this child wants to do is be a Manifestor; not a Generator. Most Projectors would rather be a Generator; it's a natural relationship between the two. Not in this case…". The "relationship" is the Projector's affinity for Generator energy, the same conditioning p. 104 calls unhealthy, not an alignment between the two people. The Winn A5 remark that an empowered Projector "moves the Generator energy into action" (seg. 56) points the same way as the rule but is not cited and could not carry it alone. The passage would, if anything, support `generator_with_nonsacral` (heat, comfort) rather than alignment, which PF01 §5.2.3 defines as coherence of direction, principles and values, or communication, the capacity to formulate and exchange; the row's gloss ("the Projector recognizes, the Generator supplies energy") comes from pp. 104, 229 and 230, not from p. 235 |
| `projector_manifestor` `harmony` −50, `alignment` −50 | "focused aura meets a closed, repelling one" | inference from the two descriptors; no passage about the pair |
| `reflector_present` `balance` +50 | "the sampling aura reflects the other" | inference; no passage |

**Signs and sizes.** The magnitudes are small by design (each 100 per mille is 1.5 points; `A` and `I` together explain 0.4% to 7.6% of score variance) and the sensitivity table shows them to be the least influential knobs. The *signs* are where the doctrine is thin: of the six pair rules, one follows its passage, two cite passages that do not say what the rule needs, and three cite no passage. Of the four class rows, the motor-related cells follow doctrine and the approachability cells (Manifestor `harmony`/`comfort`, Generator `harmony`/`comfort`) extend aura descriptors into relationship categories by analogy.

**Alternatives the proposal did not present** (the brief asks for "the alternatives you rejected"; §2.4 and §3.7 give none):

1. **Pair rules only.** Keep Table 7b, drop Table 7a. Aura compatibility is pairwise; a per-person level is not compatibility.
2. **Zero-sum rows.** Keep Table 7a but constrain each class row to sum to 0 across the ten categories, so Type redistributes a pair's profile without raising or lowering its total. This removes the Generator +500 / Reflector −750 bias while keeping "Generators carry consistency and drive".
3. **Offsets only where doctrine speaks.** Keep the motor-derived cells (`consistency`, `drive`, `heat`) and the one pair rule with a passage (`generator_with_nonsacral`); drop the approachability cells and the unsupported pair rules until *Type Sexual Signatures* or another primary source is admitted.
4. **No Type component** (blend 60/40 or 70/30). Center completion already carries the mechanical content of Type (defined Sacral, motor to Throat, openness); the aura descriptors would wait for a source.

**What the admitted collection would have given the tables.** The A4 Rave Psychologist booklet (§3.5) supports, at corroboration tier, the sign of `generator_projector` (Projectors and Generators "designed to influence each other, are most deeply penetrated and conditioned by each other", with "a need for a formality (respect)"), the sign of `projector_manifestor` ("Can't penetrate well into Reflectors and Manifestors … With Ms, tend to backup and never come forward again"), and a rule the proposal lacks, `manifestor_reflector` ("A bond exists between Ms and Rs"); it also gives all four aura keynotes in one place, including "Resistant & Sampling" for the Reflector. Had the tables been built from this material, labelled as corroborated inference, the register would be stronger and two of the misapplied bases would be unnecessary (R-18).

**Verdict.** The inferences are honestly labelled, bounded and measured, which is what the brief required. Two of the six pair rules rest on passages that do not support them, Table 7a is a per-person prior rather than a pair compatibility, and no alternative was presented. SOUND WITH CHANGES: fix the two citations or drop the rules, present the alternatives, and let the Product Owner choose between a pairwise-only Table 7b and the full tables with their §4.10 effects disclosed. (R-01, R-02, R-05.)

### 3.7 Statistical validity

**Circularity.** The per-category lines are the integer scores whose cumulative shares are closest to 30%, 65% and 90% on the same 20,000 pairs they are measured on, so the 30/35/25/10 headline mix holds by construction (realised shares deviate by up to about one point only because integer scores tie). The same is true of the per-category mix table in §4.4 and of the overall mix in §1. These numbers describe the calibration, not a result. What is informative:

* everything measured before the lines are chosen: the score distributions (§5.2), zeros and ties (§5.5), the Spearman agreement with v1, inter-category correlation, component means and variance shares;
* everything that depends on the joint distribution across categories, which the per-category marginal calibration does not fix: the Reader v2 distinct-band distribution (§5.4), the share of pairs with any Glow, the ten-band profiles, and the per-Type effects in §4.10 below;
* per-pair results: the live pairs P1 and P2 and the goldens;
* out-of-sample populations (next paragraph) and, once available, live pairs.

**Out of sample.** I generated seven further populations with the proposal's own chart generator (`hdchart.py`, mean node), 2,000 people and 20,000 distinct random pairs each, and applied the frozen §4.4 lines:

| Population (seed, births) | Cool / Open / Warm / Glow | Pairs with any Glow | Type shares G / MG / P / M / R |
| :- | :- | -: | :- |
| reference: 20261101, 1950–2005 | 29.8 / 34.9 / 25.3 / 10.0 | 55.9% | 38.7 / 33.0 / 19.8 / 7.3 / 1.2 |
| 20261102, 1950–2005 | 30.1 / 34.7 / 25.2 / 10.1 | 56.2% | 36.8 / 33.8 / 20.1 / 8.4 / 0.9 |
| 7, 1950–2005 | 30.3 / 34.3 / 25.2 / 10.2 | 56.7% | 35.8 / 35.2 / 20.1 / 7.5 / 1.4 |
| 20261101, 1985–2005 | 30.7 / 34.7 / 24.9 / 9.7 | 55.0% | 36.3 / 31.8 / 22.9 / 7.8 / 1.1 |
| 20261101, 1995–2004 | 30.5 / 34.8 / 25.3 / 9.4 | 52.3% | 38.5 / 38.1 / 15.9 / 7.0 / 0.5 |
| 20261101, 1950–1970 | 32.3 / 34.6 / 23.5 / 9.6 | 53.9% | 39.8 / 28.1 / 24.0 / 7.1 / 1.1 |
| 20261101, 1970–1990 | 29.9 / 34.2 / 25.6 / 10.2 | 57.2% | 40.3 / 35.9 / 16.2 / 6.7 / 0.9 |
| 20261101, 2000–2008 | 31.7 / 34.6 / 24.5 / 9.2 | 52.6% | 31.4 / 31.6 / 23.6 / 12.7 / 0.8 |

The frozen lines hold to within about 2.5 points of target on every synthetic population, including birth windows of nine and twenty years, while the Type mix moves considerably with the era (Manifestors 6.7% to 12.7%, Projectors 15.9% to 24.0%). This confirms the brief author's point 5 and extends it. It says nothing about a real user pool, whose births, places and pairing are not random; that remains the recalibration case the proposal names.

**How much of "no zero scores" is constant offset?** The brief author suggested the Type component's 500 baseline at 15% weight adds about 7.5 points to every score. Measured on the reference population the Type component adds 6.5 to 10.7 points per category on average (mean `T` 435 to 716 per mille × 0.015), more than 7.5 in most categories because the population is Generator-heavy and Generators carry positive offsets. But the Type constant is **not** what removes the zeros. With the Type weight set to 0 (blend 60/25/0), zero scores would be 0.01% to 0.59% of pairs per category (`communication` highest), against v1's 2.5% to 8.0% and 41.8% for `balance`; those residual zeros are exactly the pairs whose channel component and center component are both 0. The center component removes the zeros: it is non-zero whenever any center is defined in the composite, which is nearly always. Under relative bands a constant offset is immaterial anyway, because the lines absorb it; what matters is the differential part of `T`, measured below. Removing the Type signal entirely (all offsets 0) under the frozen lines moves the overall mix to Cool 32.9 / Open 36.0 / Warm 23.8 / Glow 7.3, so the Type tables add about 2.7 points of Glow share overall, almost all to pairs of Generators.

**What Glow means now.** Under the recommended lines Glow is, by construction, the top decile of each category's scores. If the ten categories were independent, 1 − 0.9^10 = 65% of pairs would show at least one Glow; the observed 55.9% reflects the positive inter-category correlation (mean 0.153, §5.5, reproduced). Across a pair's ten categories: 44.1% of pairs show no Glow, 29.2% exactly one, 15.3% two and 11.3% three or more; the most a pair shows is seven. For a given person, on average 56% of their partners show at least one Glow (10th percentile of people 37%, 90th percentile 74%). For the one band Reader v1 shows, `harmony`, Glow appears for 9.1% of pairs, and for the "#1 category" band at the top of a Glow Story card it appears for about 10% of pairs whatever the category. So Glow keeps a clear meaning per category (one pair in ten) and loses its meaning as a pair-level rarity ("a Glow somewhere" is the majority outcome). Mix D (Glow 5%) gives one pair in three any Glow. This is a product decision inside Q-5, not a defect, but the proposal's §1 line "Pairs with any Glow: 3 of 20,000 → 55.9%" should be read with that distinction in mind (R-14).

## 4. Engineering feasibility and scope

### 4.1 Implementation impact: is §8 complete?

**Code areas.** §8 names the right modules (`composite.py`, `signals.py`, `calculators.py`, `core.py`, `registry_loader.py`, `compute.py`, schemas, goldens, the 2.16 owner tests) and the right catalogs. What it does not name are the specific v1 commitments those modules enforce, each of which the v2 design breaks and each of which an implementer would have to find:

| Surface | v1 commitment in code | What v2 needs | Named in §8? |
| :- | :- | :- | :- |
| `engine/magic10/signals.py` `_signal_q` | `1 <= len(channels) <= 6` per signal; operations limited to the three v1 names; `0 <= q <= 200` | two Balance signals over 36 channels; three new operations; per-mille `0..1000` | no |
| `engine/magic10/signals.py` `_compute_signals` | "overlapping category signals" is a hard error when the two signals of one category share a channel; `index < 18` ordinary, 18–19 Balance by position | both Balance signals read all 36 channels, so they overlap completely | no |
| `engine/config/registry_loader.py` | `sum(len(signal['channels'])) != 90` fails; `config_id != 'm10-channel-state-v1.0.0'` fails (line 1191); `ADMITTED_RELEASE_ROSTER` of exactly 45 members; `ADMITTED_RELEASE_VERSION = "1.3.0"`, `ADMITTED_RELEASE_BUILT_AT_UTC` | 150 channel rows (78 ordinary + 72 Balance); new `config_id`; roster grows by at least three members (centers catalog, Type-pairing catalog, v2 config and schema) | "two new catalogs, roster, admitted release constants": partly |
| `engine/core/core.py` `_validate_bundle` | literal `magic10_mechanics_config.v1`, `magic10_result.v1`, `signal_scale == 2`, `response_scale == 10000`, exact `rounding` strings, exact mechanics field set, sources roster `{caps, categories, channels, thresholds}` | v2 schema id, result schema, a per-mille signal scale, new fields (`saturation_k_bp`, `blend`, `center_profiles`, `center_map`, `sources.centers`, `sources.type_pairing`) | "bundle validation for the new catalogs and schema v2": partly |
| `engine/core/core.py` `_validate_result` | `0 <= q <= 200`; bands recomputed from 24/49/74 | per-mille signals; per-category lines | band rule yes; signal domain no |
| `engine/magic10/calculators.py` | band from 24/49/74; two-input weighted mean | three-component reduction; per-category lines | yes |
| `engine/magic10/thresholds.py` | reads `math/thresholds.json` `edges` as one flat list **at import time** (`tuple(int(edge) for edge in _DATA["edges"])`); `engine/compat/thresholds.py` then requires exactly four edges or raises at import | per-category object; with the file in v2 shape both modules fail at import, before any request is served | no (neither file is named) |
| `engine/compat/compute.py` | `band_for`/`_band_for_score`; `COMPAT_RESULT_SCHEMA = "magic10_compat_result.v1"` and its schema file; `PURE_RESULT_SCHEMA`; `_pure_result_matches` re-checks `q` in `0..200` and the 24/49/74 bands on any cache hit | `magic10_compat_result.v2`, new result schema identity in the pair preimage, widened `q` | "result schema v2 identity": partly; the compat result schema is not named in §7's PF12 list either |
| internal compat surfaces: `hdctl showcompat` stdout and `POST /api/compat/v1` (`engine/cli/main.py`, `engine/http/compat_handler.py`) | emit one canonical `magic10_compat_result.v1` document, which PF05 pins (lines 671, 677) | `magic10_compat_result.v2`; an internal API contract change | no |
| `schemas/` | `magic10_mechanics_v1.schema.json` (`additionalProperties: false`, `signals` `maxItems 6`, operation constants, `signal_scale` const 2, exactly four `sources`), `magic10_result_v1.schema.json` and `magic10_compat_result_v1.schema.json` (`q` maximum 200) | v2 versions of all three, plus schemas for the two new catalogs and a schema for the per-category thresholds file, which has none today | §7 names the shapes; §8 names "schemas" only |
| consumer bundles and artifacts: `docs/schemas/config_bundle_{be,fe}.json`, `tools/config/artifacts.py` (`band_edges.json`, `band_edges.v1`), `engine/config/bundles.py` (a governed consumer contract, PF12 §8.15 Required-Now) | flat `edges` list | per-category object | no |
| `engine/sampler/core.py` (dev sampler) | derives one band from a single aggregate `compat_score` through `band_for` | per-category lines give no mapping for an aggregate score; the sampler's band needs a rule or must be dropped | no |
| `engine/config/registry_loader.py` line 1204; `tools/evidence/run_canonical_json_gate.py` line 416 | the loader pins `math/thresholds.json` `edges == [24, 49, 74, 100]`; the evidence gate checks every category band against the global `band_for` | per-category lines fail both as written; with `core.py`, `calculators.py`, the two `compute.py` helpers, `magic10/thresholds.py` and the sampler, the band mapping has at least six code homes to collapse into one | no |
| `tests/fixtures/magic10/v1/goldens.json`, `tests/m10/*`, the five 2.16 owner tests and others | v1 goldens; at least nine test files pin v1 literals by my narrow search (`magic10_result.v1`, the `config_id`, `24, 49, 74`); three of the five owner tests are among them (`test_engine_core_abba.py` and `test_evaluate_pair_eligibility.py` pin `magic10_result.v1`; `test_engine_core_determinism.py` validates against `schemas/magic10_result_v1.schema.json`; the eligibility test also pins the `magic10:v1:` cache prefix, the `config_id` and `G008_PAIR_KEY`, which depends on it), while the other two check structure only and change with their fixtures; independent checkers counted 22 to 34 of the 220 test files with broader pattern sets | v2 goldens (§6) and re-pinned expectations | goldens yes; the breadth no |
| `tools/evidence/generate_determinism_gate_proofs.py`, `tools/evidence/run_sanity_pipeline.py`, `scripts/cut_release_manifest.py` | the gate proofs under `audit/gates/parity/…` are generated from `fixtures/charts/alice.json` and `bob.json`, embed the release identity and bands, and are drift-checked (`--check` raises `DRIFT`) by the sanity pipeline | regeneration of current evidence, while PF04 §4.1.6 forbids regenerating historical captures "merely because the manifest or release ID changes" | no (R-20) |

None of this makes v2 infeasible; all of it is ordinary Conjunction work. But of the fifteen surface groups above, §8 names one fully and six partly (counting its generic mentions of schemas, goldens and release constants as coverage) and omits eight; it omits an import-time failure, omits the internal API contract change on the two compat surfaces, and understates the test and evidence work; the cost is materially understated (R-04). The invariant changes are the ones that matter for canon (§4.8).

**Governed homes.** Three v2 rules have no stated governed home and would otherwise live as code constants, against HDE Math Spec §7.3 (closed identities, no hidden defaults): the Type-to-aura-class mapping and the set of class names; the predicate names and semantics of the `I` rules (`same_class`, `generator_with_nonsacral`, …); and the `motor_throat` key in the center map, which is not a center, so the proposal's own proposed loader rule "every center in the map exists" would reject the `heat` and `drive` rows unless the rule names `motor_throat` as the one permitted non-center key (R-21).

**Catalogs and schemas.** Correct as far as listed: centers catalog, Type-pairing catalog, mechanics configuration v2, thresholds shape; gates, channels, `magic10.json`, `magic10_caps.json`, narratives unchanged. Missing: the compat result schema v2 and the Reader schemas' *evidence* (goldens regenerated) even though the public shapes do not change.

**Admission constants.** `ADMITTED_RELEASE_ROSTER` (45 members, import-time invariant), `ADMITTED_RELEASE_VERSION` and `ADMITTED_RELEASE_BUILT_AT_UTC` all change; §8 says "grows" and "new `release_id`", which is right in substance.

**Release cut, cache, performance, Reader shapes.**

* Release cut: one release carrying all members, v2 replacing v1; correct under HDE Math Spec §5.4.1 and PF12 §2.9.
* Stale cache: confirmed for the seam. `engine/compat/compute.py` builds the pair preimage from `schema`, `members`, `config_id`, `release_id` and `result_schema`, and `_cached_pure_result` requires all four identities to match, so every v1 entry misses and is recomputed. No migration is needed. Two caveats §8 should carry: no production caller passes an intrinsic cache today (`engine/http/compat_handler.py`, `adapter/http_reader.py`, `engine/cli/main.py` all call `evaluate_pair` without one), so the statement is correct but moot; and `_pure_result_matches` would reject every v2 result until its `0..200` and 24/49/74 checks are rewritten. PF01 §5.2.2's cache key `magic10:v1:<pair_key>` and preimage `result_schema` value also change, and §7 does not list §5.2.2.
* Performance: the new per-pair work is two union-find passes over nine centers and 36 channels (per member and for the union), nine center outcomes, a Type lookup, and ten three-term blends; the prototype scores 20,000 pairs in 4.6 s in pure Python, about 0.2 ms per pair. An independent checker's benchmark on the same population (one machine, the first 2,000 pairs; order of magnitude only) puts v1's `compute_core` at about 1.4 ms per pair, of which about 1.1 ms is the per-call `_validate_bundle` re-digest of the catalogs and about 0.25 ms the kernel; the v2 mathematics adds roughly 25 to 120 µs. Negligible against the Reader path; the one implementation note is that per-call bundle validation grows with the added catalogs and should bind a validated projection to the frozen bundle rather than re-digest on every call.
* Reader shapes: unchanged, confirmed against PF01 §2.5 and PF04 §12.1 `GATE:CORE-READER`; the v2 schema files need no change, only new goldens.

### 4.2 Pure Engine Core

The formula is a pure function of two masks and the governed catalogs. Every input it reads is already a normalized input to `compute_core` or would be added as one (centers catalog, Type-pairing catalog, v2 configuration, thresholds): no file, environment, clock or network access at compute time, no mutable state. The Type derivation and center outcomes are pure graph computations over `catalog/channels_v1.json`, which the bundle already carries; the connected-components step is deterministic given any fixed center order (the prototype's output *bytes* vary with Python's hash seed only in the order of its diagnostic `components` listing, never in a score; a production implementation would iterate a tuple). Fail-closed validation of the new inputs (every center in the map exists; weights 1..3; profiles have four outcome keys with `open = 0`; blend sums to 100; `K > 0`; `A` has four classes by ten categories; every `I` rule names a known predicate and known categories) belongs in the loader, outside the core, as PF02 §2.1 requires. **Feasible as pure Engine Core, with catalogs injected (HDE Math Spec §7.2 item 7, §7.3). Confirmed.**

### 4.3 Open PF09 work

| Row | State | What v2 does to it | Proposal |
| :- | :- | :- | :- |
| PF09.6 Task HDE-DIST008 "Full-domain Magic10 verification and current release binding" | Partial. HDE-DIST008.1 lists v1-specific proofs: `magic10_result.v1`, `magic10_compat_result.v1`, "Both Balance operations under symmetric, one-sided, empty, and mixed ownership", "All twenty signals at zero, maximum, midpoint, and half-up boundaries", "all ten category reducers at every band edge", `tests/fixtures/magic10/v1/goldens.json`; .2 cuts the manifest at `--version 1.1.0` with `M10-CANON-001.adopted_at_utc`; .3 attests that candidate | Its target changes: the signal domain, the Balance operations, the reducer and the band edges are all different under v2, and the manifest version and adoption timestamp are v1's. Left as written, the row would verify a formula the release no longer runs | not mentioned |
| PF09.4 Task HDE-CONJ010 "Full Magic10 deterministic scoring integration" | Partial; .1, .2, .5 Not done; .3, .4, .6 Partial. Subtask texts describe the five-state kernel (unchanged by v2), "Twenty governed signal producers" (operations change), "Ten-category Magic10 calculation" (reduction changes), Engine Core integration, goldens and parity | v2 re-opens the content of .2, .3, .4 and .6 | not mentioned |
| PF09.3 Task HDE-SEPA005 "Production Magic10 mechanics configuration contract" | Done, bound to HDE-EPIC040 | v2 needs the same five subtasks (catalog, schema and default configuration, fail-closed loader, configuration identity, tests) again for the v2 contract; by PF09's collision-free-owner rule that is a new task, not a reopening | not mentioned |

Two more rows bear on the change. PF09.7 Subtask HDE-COAG003.6 "Magic10 active-config cutover guard" is Not done and is the row Q-6's cutover posture would land on. HDE-DIST008.1 requires proof of "Absence of UID hashing and Type-only fallback" (line 1845) and HDE-CONJ010.5 requires "Remove UID-hash and Type-only scoring authority" (line 2158): v2's bounded Type component is not that retired fallback (Type is derived from the gate set and never scores alone), but the proposal should say so in one sentence so the Distillation proof family can be re-targeted without ambiguity. PF12's "PF09 and PF30 work accountability" rule (line 145 ff.) requires implementation work to resolve to exactly one PF09 task or PF30 CRD, which is why the placement matters.

The brief did not ask for PF09 placement, so this is a gap against Glow's method rather than against the brief (§5.5). It should be in the adoption record or the Change specification (R-06).

### 4.4 Gates and tests

* **HDE Build Notes 2.16 R-1** names the five owner tests that are `GATE:CORE-DET` evidence under closed rails. All five exercise `compute_core`, `evaluate_pair` or `hdctl showcompat` and would run against v2 unchanged in intent; their fixtures and any pinned expectations change. On my scratch clone at `0bf99656` under closed rails, the five files together with `tests/m10` give 184 passed and 3 skipped (the open-rails cases), which is the v1 baseline a v2 change must re-earn. §8 names them.
* **Goldens.** §6 supplies the v2 expectations for P1, P2, SYN-A with SYN-B and the adapted G001–G008, all reproduced here; G006 becomes ten per-category boundary matrices, which HDE Math Spec §9.1 and PF04 §4.1.5 `BAND_EDGE_GOLDENS_OK` must be rewritten to accept (the proposal says so).
* **Live compat test (2.15 R-1).** The deployed check scores SYN-A and SYN-B; §6 gives the expected v2 bands (4 Open, 4 Warm, 2 Glow). The 2.15 pass predicates are shape, parity and identity, which v2 satisfies; a v2 QA plan should add the band expectations as findings, as 2.15 already does for deployed-versus-CLI differences.
* **The score-distribution utility (Candidate CRD item 13).** The Product Owner directed on 2026-11-01 that the mass scoring test be built as a command-line utility that runs "any time there is a change to math spec or configuration". v2 is exactly such a change, the proposal's `measure.py` is a prototype of the utility, the §4.2 recalibration rule has nothing to run without it, and the only measurement of "the product works" after release is the one it produces. The proposal does not mention it. **It should be a named dependency of the v2 change, built before or with it, and the frozen lines should be cut by it, not by an ephemeral script** (R-09, Q-11).

### 4.5 Reproducibility

Someone other than the author can reproduce every number, and I did. They cannot do it "as published": they must (1) replace the `REPO` path in `hdmech.py` (after which the file no longer hashes to the stated value); (2) infer the directory layout from the scripts' relative paths; (3) run the engine scripts from the clone root, or the narrative-pack loader fails; (4) add the D and E targets to `measure.py` to obtain two rows of the §4.4 table; and (5) write their own code for the variance shares (§3.7) and inter-category correlation (§5.5). The `config_id` in the prototype ends in `-candidate` where §3.1 does not, and the goldens file's bytes depend on the hash seed. None of this is a correctness problem; all of it belongs in the Appendix C preamble (R-10).

### 4.6 Brief compliance

Checked row by row against brief §5 (D-1 to D-7), §7 (deliverables 1 to 10), §12 (Q-1 to Q-6) and §6 (constraints), by me and again by an independent checker. The rows that need comment are below; every row not listed is met with a locator in the proposal.

| Requirement | Result | Evidence |
| :- | :- | :- |
| D-1: the three readings resolved, with a recommendation; a typical pair's relevant connections can reach every band; a missing connection does not push every score down | Met | §4 Q-1; saturation removes the division by unformed channels; every category reaches Glow for 9–11% of pairs |
| D-2: which centers the pair defines together; which are completions; motor-to-throat completion; weights with reasons; which categories; **avoid double counting, state exactly how the two contributions combine** | **Partial** | the first five are in §3.5–§3.6. The combination is stated (blend 60/25/15), but the word "double counting" does not occur in the proposal and no argument is given that channel states, center outcomes and Type are three deliberate readings of the same gate sets rather than one contribution counted thrice. The overlap is real: a motor–Throat definition feeds the `motor_throat` center feature (`heat` weight 1, `drive` weight 2) and the Type component (Manifestor `drive` +250); a Reflector's absence of definition feeds the center component (no `shared`, no bilateral completion) and Table 7a (`drive` −250, `heat` −200). HDE Math Spec §7.3 and §8.3 name "No double counting" as a promotion invariant. Measured on the reference population (§7), `C` and `Z` correlate at 0.02–0.33 in nine categories and 0.44 in `balance`, the covariance share of score variance is at most 17% outside `balance` (31% there), and `Z` changes 20–39% of bands, so the overlap is modest and the missing piece is the statement, not a restructuring (R-07) |
| D-3: Type derived from the gate set; derivation checked against vendor `type` for the test people; MG decision; symmetric matrix with doctrine per cell; limits stated; routed through the Complete Guide then HD-TYPE-01 and HD-SELF-01; gap stated then route | Met, two notes | the vendor Types of "the test people" (P1, P2, SYN-A, SYN-B) are not in the repository, so the check was done on fixtures instead, disclosed in §10.1 (R-11); HD-SELF-01 is neither cited nor listed as not used (R-13) |
| D-4: absolute or relative; global or per-category; target mix measured on v2; reference population named; recalibration rule | Met | §4 |
| D-5: *propose measurable targets* (share of pairs with three or more distinct bands; no category stuck); Reader v2 shape unchanged | **Partial** | the measures are reported (§5.4: 92.5% of pairs with three or more bands; least-used band 9.1%) and the shape is unchanged (§8), but no target threshold is proposed; "target" is used only for the band-mix shares, so the §4.2 recalibration case has no pass or fail criterion (R-08) |
| D-6: zeros and ties before and after | Met | §5.5 |
| Deliverable 5: sensitivity, "the effect of moving each weight by ±20%" | **Partial** | §5.7 moves knobs in groups (one center weight per category; all `A` offsets together; all `I` offsets together; profile responses together), not each weight (R-23) |
| Deliverable 1: before-and-after table of the brief §4.3 measures | Met, one row short | eight of the nine §4.3 rows; "Channels a pair forms, of 36" is omitted (an input property the formula does not change) (R-13) |
| Brief §6 constraint "one monotone band mapping (§5.3)"; HDE Math Spec §7.2/§8.2 item 6 (decision on interaction with presets and viewer preferences) | **Partial** | the mapping becomes ten per-category monotone mappings, which §4 argues for but §3.8 does not reconcile with the constraint's wording or with the canon passages that say "single"/"global" (R-03); the preset and viewer-preference decision is nowhere stated and is met only implicitly by §3.8 (R-22) |
| D-7: unchanged list, or a Product Owner decision with impact | Met | none of the seven items is changed; the two new decisions Q-7 and Q-8 are presented as decisions |
| Deliverables 1–10 | Met, one gap | all ten present. Deliverable 2 asks that inferred rules be listed together "so the reviewer can check them": §2.6 does this but labels two derivation rules as source doctrine (§3.4) |
| Brief §2.4 route 2: "give the alternatives you rejected" | **Not met** | §2.4 and §3.7 present no alternative to Tables 7a and 7b (R-05) |
| Q-1 to Q-6 answered with recommendations | Met | §9 |

### 4.7 Canon constraints (brief §6)

| Constraint | Result | Evidence |
| :- | :- | :- |
| Inputs closed; each new input a governed release input with new `config_id` and release (§5.2.1, §5.4.1, §5.4.4) | Met | §3.1, §7, §8 |
| AB↔BA identity; identity never enters; two-run identity; integer only; `ROUND_HALF_UP` at declared stages; clamp; one monotone band mapping (§5.2.6, §5.3) | Met | §3.2, §3.3, §3.8; reproduced (§3.1). The band mapping stays one monotone mapping per category; ten of them in place of one is the Q-5 decision |
| Promotion prerequisites §7.2/§8.2 items 1–8 | Met in substance | 1 (Product Owner approval) is the decision this review informs; 2 (complete feature-to-category model, each output once) §3.5–§3.7; 3 (paths and schemas) §7 names what PF12 must own; 4 (populated values) yes; 5 (one evaluation order) §3.3; 6 (viewer preferences outside intrinsic scores) yes, nothing from the viewer enters; 7 (pure Engine Core) §4.2; 8 (PF12 treatment) §7 |
| Invariants §7.3/§8.3: closed identities; no hidden defaults; no double counting; atomic completeness | Met, two notes | hidden default: Table 7b's absent categories (R-13); no double counting: not argued (R-07) |
| Public covenants and privacy (§2.1, §2.5, §5.5) | Met | no public change; no numerics |
| Eligibility unchanged (§4.1) | Met | §7: "any Type combination remains eligible; Type now enters scoring, not eligibility" |
| Out of scope: no relationship verdicts; no medical/psychological/sexual/safety/destiny claims; no viewer-preference weighting in intrinsic scores; no runtime A/B; no caller weights | Met, one question | the nonclaims hold and no caller input exists. The per-Type level effects of Table 7a are not a relationship verdict but are a systematic statement about a Type (§4.10); the Product Owner should decide whether that is inside the boundary (R-01) |
| HDE Governance §12.1 `GATE:CORE-MATCH`: closed sets, inclusive maxima, determinism, no public numerics | Met | inclusive maxima per category remain inclusive maxima; §7 adds "per category" |

### 4.8 Canon delta list (§7)

**Existence.** Every section the proposal cites exists in the current canon files, including the indented PF01 headings (§5.2.2 line 599, §5.2.7 line 786, §5.2.8 line 798), PF04 §4.1.5 (line 1346) and §12.1 (line 4142), PF12 §2.1/§2.6/§2.9/§2.10, PF02 §2.1, PF17 §2.3, PF29 §5.1/§6.4/§7, and the PF10 addenda 2.15 and 2.16. Three characterizations are off. The PF29 sampler example `compat_score 50, band Open` is at line 310 inside §5.2 "CLI dev sampler" (heading at line 305), not §5.1, and it is already wrong under v1's own lines (50 is Warm; its neighbour `compat_score 75, band Warm` is Glow), so it is not a v2-caused delta but a pre-existing defect that v2's per-category lines would additionally require to name a category (R-16). The §7 entry for PF01 §6.3 offers to "promote" the Speculative center-tagging contract (dominant / compromise / neutral per center) to the four-outcome contract; the two are different concepts, so only the "retire in favour of it" alternative is accurate (R-13). The PF10 entry proposes to "supersede" `M10-CANON-001`'s aura-diagnostic exclusion, but that record is not in the current PF10 base version and the current-version rule forbids carrying forward superseded content; the entry should be a fresh adoption addendum (R-13). Two pre-existing canon defects will complicate the Doc-Delta: PF01 carries two sections numbered §5.2.8 (lines 798 and 818), which the proposal cites without disambiguation, and PF01 §2.5's "V2" means Reader v2, which will sit beside Magic10 v2, `m10-…-v2.0.0` and `magic10_result.v2` (R-17).

**Missing changes.** The delta list is organised by section and is good on the sections it names. It omits the normative statements v2 falsifies:

| Canon text v2 breaks | Where | In §7? |
| :- | :- | :- |
| "No default map assigns one Channel to both signals of the same category" | PF01 §5.2.4 (line 675) | no; both Balance signals read all 36 channels |
| "Require each Balance signal to use its exact named operation and one through six unique canonical Channels"; "Require every signal wire value to be an integer in `0..200`" | PF01 §5.2.7 (lines 790, 793) | no |
| "`0..200` signal domain … are fixed v1 invariants, not tuning knobs"; the two Balance operations as named; Balance Channel membership "one through six" | PF01 §5.2.8 knob table and invariants (lines 809, 812) | §5.2.8 is listed for "v2 knob table and what counts as structural", without naming these |
| `signal_scale: 2`, `rounding.signal: round_half_up_to_half_score_unit`; "ordinary and Balance signal Channel lists each contain one through six unique valid rows"; "no Channel appears twice … in both signals of one category"; "signal and category outputs remain within `0..200` and `0..100`"; the fixed-invariant list | PF12 §2.9 (lines 1369–1378, 1412–1433) | §2.9 is listed for new fields and new closure rules; the existing rules that must change are not named |
| "Band thresholds (inclusive maxima): `tests/compat/bands_thresholds/*`" | PF04 §12.2 evidence link (that path does not exist in the repository today, a pre-existing drift) | no |
| `magic10_compat_result.v1` identity and schema | PF12 §2.9 "Governed result schemas"; `engine/compat/compute.py` | §7 says "compat result schema v2" under PF12 §2.9: partly |
| `magic10:v1:<pair_key>` cache key and preimage `result_schema = magic10_result.v1` | PF01 §5.2.2 (lines 599–633) | no; §3.3 step 10 changes both |
| "The inspected canonical manifest records release version `1.3.0` with 45 members" and the other 45-member statements | PF01 §5.4.3 (line 982); PF12 §2.10 (line 1467), §6 (lines 1868, 1904, 1969–1970) | no |
| `hdctl showcompat` stdout and `POST /api/compat/v1` emit one canonical `magic10_compat_result.v1` document | PF05 §4.1.3/§5.5 (lines 671, 677 and the HTTP route) | no; PF05 is outside the brief's six documents |
| `magic10_result.v1` and `magic10_compat_result.v1` as the result identities; "global edges (for example, 24, 49, 74, 100)"; "Internal compat threshold code MUST derive `THRESHOLDS_V1` from `engine.magic10.thresholds.THRESHOLD_EDGES`"; the `band_edges_binding.log` record of the resolved `THRESHOLDS_V1` | PF14 (lines 1856, 1903–1905, 1913, 1915, 1940; line 1883, which assigns the mechanics gate to HDE-DIST008.1, is generic and survives) | no; PF14 is outside the brief's six documents |
| band-edge proofs `audit/gates/bands/edges.snapshot.json`, `edges.diff.json` "(boundaries at 24/49/74/100)"; "`BAND_EDGE_GOLDENS_OK` — Goldens at 24/49/74/100 pass"; "inclusive maxima thresholds" checklist and `ci/jobs/band_thresholds_inclusive.yml`; the §9.2 rule that a change to "band maxima … or any manifest bytes that would yield a new `release_id`" requires a Doc-Delta opened before the change | PF04 Appendix D (lines 4726–4727; the paths do not exist in the repository), §2.0 token roster (line 605), Appendix B.6 (lines 4487–4495), §9.2 (line 2546) | no; §4.2's recalibration rule cites PF01 §5.2.8 and §5.3.5 but not PF04 §9.2 |
| "Magic-10 v1 promoted release inputs" roster; "Magic-10 v1 current-attestation predicate"; "Magic-10 v1 authoritative-config boundary" (authoritative path `catalog/magic10_mechanics_v1.json`, goldens `tests/fixtures/magic10/v1/goldens.json`, eight cases); the `config.band_edges` artifact (`band_edges.v1`, flat edges) | PF12 §5.1 (line 1888), §6.2.1 (line 2053), §8.14.1 (line 4943), §8.14.2 (line 4982) | no; the §7 PF12 entry says only "Manifest membership for all new members; new `release_id`" |
| "Magic-10 pure Engine Core flow: BodyGraph Gates → Channel states → signal wire values → category scores → bands"; the threshold shim `engine.compat.thresholds.THRESHOLDS_V1` derives from `engine.magic10.thresholds.THRESHOLD_EDGES` | PF02 §2.2 (line 408), §3.1 (line 755); PF14 §7.3 (line 1915) | no; the §7 PF02 entry also leaves open whether the two new catalogs ride inside `mechanics_bundle` (keeping the four-argument `compute_core` contract) or change the entrypoint |
| "Preset-specific maxima or an alternative band profile require separately authorized Future-Promotion and must not be inferred from legacy configuration or examples" | PF01 §5.3, the paragraph after the band list | §5.3 is listed; this sentence must be rewritten so that ten per-category maxima are the single §5.3 mapping and not a preset or alternative profile |
| "consistent with the single mapping" (§5.3.5); "handoff to the single band mapping in §5.3" (§7.2 item 5, §8.2 item 5); "Do not duplicate or reorder band mapping" (§7.3); "this section does not define a second mapping or threshold table" (§8.4) | PF01 lines 869, 1775, 1788, 1825, 1847 | no; the brief's §6 constraint "one monotone band mapping (§5.3)" is likewise not reconciled in §3.8 or §4 with the move to ten mappings |
| the dev sampler derives one band from a single aggregate `compat_score` (`engine/sampler/core.py` imports `band_for`; PF29 §5.2 example) | `engine/sampler/core.py`; PF29 §5.2 | no; under per-category lines there is no mapping for an aggregate score, so the proposal must either define one or state that no aggregate band exists |
| "Required canonical target: `catalog/magic10_mechanics_v1.json`"; `CONFIG_MAGIC10_OK` (band edges "match the Engine's band definitions"; `config.band_edges` artifact) | PF07 (line 1253); PF19 §9.2.3 (line 3499 ff.) | no; both are outside the brief's six documents. PF07's path changes; PF19's token wording is generic and may survive, but its `band_edges` artifact reference follows the §8.14.2 shape change |

The §7 list also says "retain the 18 ordinary maps" and "the Balance maps become all 36 channels" as if the second were a map change like any other; under PF01 §5.2.8 changing Balance membership is a "structural mechanics revision" requiring a Doc Delta naming every changed signal row and its rationale, and under PF12 §2.9 the new membership violates two loader rules until those rules are rewritten. Applied as written, without the §2.9 loader-rule changes it omits, §7 would leave canon contradicting itself and still requiring the loader to reject the adopted configuration. **This is the delta-list defect that must be fixed before the canon change is drafted** (R-03). The PF05 and PF14 omissions originate in the brief, whose §7 item 7 named six documents; they are still needed changes, and the review notes them as such rather than as a failure against the brief.

**Two more statements in §3 and §7 need tightening.** First, the result schema v2 is described as "same shape as v1" (§3.3 step 10, §7), but the signal domain widens from `0..200` to `0..1000`, which the result and compat-result schemas pin as `q` maximum 200; and the v2 configuration's fixed fields (`signal_scale`, `response_scale`, `rounding.signal`, `rounding.category`), which PF12 §2.9 and `core.py` pin to v1 values, are given no v2 values (R-19). Second, the §8 release-cut bullet says nothing about evidence: the determinism-gate proofs and band-edge artifacts embed the release identity and bands and are drift-checked, while PF04 §4.1.6 forbids regenerating historical captures merely because the release identity changes; the adoption record or the Change must say which current evidence is regenerated and which captures stay frozen (R-20).

### 4.9 Overreach

* **New decisions Q-7 and Q-8** go beyond the brief's six, and both are necessary consequences of D-2 and D-3; presenting them as decisions is correct.
* **`balance` redefinition** (Q-8) changes the operations and membership of two governed signals and the meaning of a public band. It is inside D-1/D-2's remit (the brief itself observed `balance` "runs lower than the rest") and is flagged for decision. Correct.
* **PF01 §6.3 "promote or retire"** and §6.4 are inside the canon delta list's remit; the choice is left to the Product Owner. Correct.
* **Acquiring a source** is a recommendation under Q-3b, which the brief invited. Correct.
* **Naming a `config_id`** (`m10-relevance-centers-type-v2.0.0`) is a proposal, and §10.2 says it creates none. Correct.
* **The Type floor for no-connection pairs** (G001 scores up to 11) is a product consequence the brief did not ask for and the proposal does not call out as a choice (R-12).
* **Language.** I found no relationship verdict and no quality claim in the normative text; §2.2 ("v2 treats completion as salient, not as a verdict") and §10.2 are careful. Two phrases read as evaluative and should be neutralised: "Type never drowns out the chart-specific mechanics" (§3.7) is a measured statement and fine; "a natural relationship between the two" (Table 7b) imports a valence the source does not carry (§3.4).

**Scope verdict: SOUND WITH CHANGES.** The proposal does what the brief asked, within canon, and names its additions as decisions. It omits two things the brief required (double counting; rejected alternatives), labels two derivation rules as doctrine, and leaves the delta list incomplete on the invariants it breaks.

### 4.10 Product effects of Type

**What I did.** On the reference population, with the §4.4 lines, I grouped the 20,000 pairs by the aura classes present and by each person's derived Type, and reran the formula twice more: once with the Manifestor `harmony` offset set to 0, and once with every `A` and `I` offset set to 0 (no Type signal; `T = 500` for all), to separate what the Type tables do from what the center and channel mechanics do by themselves.

**Measured, reference population, frozen lines:**

| Pairs containing a… | n | Mean of the ten scores | `harmony` Cool / Open / Warm / Glow | Any Glow |
| :- | -: | -: | :- | -: |
| Generator (incl. Manifesting Generator) | 18,404 | 448.8 | 28.4 / 36.5 / 25.9 / **9.2** | 56.0% |
| Projector | 7,116 | 440.0 | 29.2 / 35.4 / 25.1 / **10.3** | 55.1% |
| Manifestor | 2,809 | 440.8 | 38.6 / 40.6 / 18.1 / **2.7** | 56.3% |
| Reflector | 452 | **402.0** | 31.9 / 28.5 / 24.8 / 14.8 | 56.2% |
| all pairs | 20,000 | 446.3 | 28.9 / 36.4 / 25.6 / 9.1 | 55.9% |

Per person, averaging each person's totals over their partners: Generators 451.7, Manifesting Generators 447.8, Manifestors 440.4, Projectors 437.9, Reflectors 401.9. The brief author's figures (Manifestor `harmony` Glow 2.6% against 9.3% and 10.5%; Reflector totals 402 against 446) are confirmed to within rounding.

Per category, the Glow rate for pairs containing a Manifestor is 2.7% (`harmony`), 1.9% (`consistency`), 3.6% (`comfort`), 3.7% (`alignment`) and 4.7% (`communication`), against 18.0% (`drive`), 19.7% (`heat`) and 23.4% (`expansion`). Pairs containing a Reflector never reach Glow in `balance` or `consistency` (0.0%) and almost never in `alignment` (0.9%), while reaching it in 25.7% of `communication` results.

**Where the effects come from.**

| Effect | Source | Evidence |
| :- | :- | :- |
| Manifestor `harmony` Glow 2.7% instead of about 6% | Table 7a, `manifestor` `harmony` −200 | setting that one offset to 0 gives 5.8%; removing all Type offsets also gives 5.8%; other classes then sit at 6.8%–7.7% |
| Generators ahead of Projectors and Manifestors by about 9 points in total | Table 7a row sums: generator +500, projector −50, manifestor −50, reflector −750 per mille | with no Type signal the three classes are within 3.5 points of each other (436.1, 432.6, 435.9) |
| Reflector pairs about 45 points lower in total, 0% Glow in `balance` and `consistency` | the mechanics, not the tables: a Reflector defines nothing, so no center can be `shared` (the top of the `foundation` profile), bilateral completion is 0 (`gives_lo = 0`), and the pair forms fewer channels (7.6 against about 10) | with no Type signal Reflector pairs still average 406.4 against 436; `balance` and `consistency` Glow stay at 0.0% |
| Type tables redistribute Glow by category and class | Table 7a | with no Type signal, Generator pairs' Glow rate falls in `consistency` (10.7% → 2.7%) and `drive` (9.5% → 3.9%); Manifestor pairs' falls in `heat` (19.7% → 10.2%) and `drive` (18.0% → 3.8%) and rises in `harmony`, `comfort` and `communication` |

**Assessment.**

1. **Doctrine.** The admitted sources describe each Type's aura (closed and pushing-off; enveloping; focused and penetrating; sampling) and the Generator's sustained motor. They do not say that a Manifestor's relationships carry less harmony or comfort, that a Generator's carry more consistency and drive, or that any Type is lower across the board. Table 7a turns aura descriptors into per-person level shifts of up to ±3.75 points per category and a systematic total advantage for Generators. The sign of each cell is arguable from the descriptor; the claim that the descriptor should move a *relationship* score at all is Glow's inference, and the proposal labels it so (I-7). The Product Owner asked for "compatibility between aura types", which is a pairwise notion; Table 7b is pairwise, Table 7a is not.
2. **Disclosure.** The proposal discloses the Reflector `balance` effect (§10.1, "mean 36 against 58") and nothing else: not the Manifestor `harmony` deficit in the one band Reader v1 shows, not the Generator advantage in total, not the Reflector zeros in `consistency` and `alignment`. A Product Owner deciding Q-3b and Q-4 from §9 alone would not know that Table 7a makes Reader v1 show Glow to Manifestor pairs about one third as often as to others.
3. **The "no relationship verdicts" boundary.** No score is a verdict on a relationship, and the proposal's nonclaims (§10.2) hold. But a per-Type level shift is a verdict on a *person*: every pair a Manifestor is in loses three `harmony` points before any chart mechanics are read. HDE Math Spec §5.2 says the formula "does not assert … relationship quality"; a systematic per-Type effect on the public band is close enough to that line that it needs a deliberate Product Owner decision, and a statement in canon of what is intended.
4. **The mechanics effect on Reflectors** is a faithful consequence of the design the brief asked for (center completion, bilateral completion). It should be stated for all three affected categories, and the Product Owner should decide whether a 1.2% population with structurally unreachable Glow in three categories is acceptable or whether the `foundation` profile should give Reflector pairs some other reading (for example, treating `one_sided` completion of an open center as the top of the profile when one member is a Reflector).

**Which decision it bears on.** Q-3b (adopt Tables 7a and 7b), Q-4 (how much Type may move a score) and a decision the proposal does not list: whether Type may enter as a per-person level (Table 7a) at all, or only as pair interaction (Table 7b). Options for the Product Owner: (a) adopt as proposed, with the effects above disclosed in the adoption record; (b) keep Table 7b, drop Table 7a or constrain each class's row to sum to 0 so no Type is favoured in total; (c) drop the Type component and let center completion carry the aura doctrine. I recommend (b): it keeps what the Product Owner asked for, pairwise aura compatibility, removes the undisclosed per-Type bias, and costs at most 15 points of swing that the sensitivity table already shows to be the least influential knobs (`A` and `I` offsets ±20% move 0.4 and 0.04 points on average). (R-01, R-02.)

## 5. Alchemical fidelity

Each criterion is scored against the canon passage applied. Canon read: `PF21-Reference-7 Phases of Alchemical Engineering.md` in full; `PF13- Reference-Glow-Development-Philosophy v1.md` §B, §C, §D, §I; `PF-Reference-Glow Story.md`; PF09.3 Task HDE-SEPA005, PF09.4 Task HDE-CONJ010, PF09.6 Task HDE-DIST008.

### 5.1 Phase placement and mode discipline

**The phase.** PF21 Separation is "Filter, sort, and choose … Evaluate prototypes; choose the primary architecture … Define clear system boundaries and interfaces … Decide which future directions are deliberately not pursued this cycle." That is this proposal: it evaluates a prototype on the harness, chooses between absolute and relative lines, global and per-category lines, direct and any-route derivation, Manifesting Generator as its own class or as a Generator, and defers planetary placement. In PF13 §D terms it is the **Design** phase, whose exit signal is "Named contract, version/evolution note, minimal data to observe, and stated failure mode". The brief's §9 sequence (brief → proposal → independent review → adoption → Change) places adoption before any Conjunction work, which is right.

**Does it stay in the phase?** Yes on implementation: nothing is edited, the prototype is analysis code, and §8 is an impact list, not a build. The design outputs the brief asked for (goldens, canon deltas, impact) are Design-phase deliverables, not Conjunction.

**Is freezing band lines from a synthetic population Coagulation before Fermentation?** PF21 Coagulation is "solidify into a durable product … stability over rapid change"; Fermentation is when "the product meets real users … Be willing to adjust positioning or roadmap based on what actually works, not what was planned." The lines are governed bytes frozen into a release before any user has met v2, derived from births drawn uniformly over 1950–2005 and random pairings. Two facts keep this from being a mode mix: every release must carry *some* thresholds (v1's 24/49/74 were frozen with no user data at all), and §4.2 names the reference population, calls the lines a product choice (I-11) and routes any recalibration to "a Product Owner decision taken as a release, never a runtime adjustment", which is a later Distillation step reached through Fermentation. What is missing is the Fermentation hook itself: the proposal does not say what real-user observation would trigger recalibration (for example, the realised band mix over stored people, which is what the Candidate CRD item 13 utility would measure), nor what "the product works" looks like once v2 is live. §10.1 discloses the synthetic calibration and a qualitative trigger ("a real user pool will fall differently … that is the recalibration case of §4.2"), so nothing is concealed; but the lines are not labelled provisional, and the observation that would test them is unnamed.

**Score: SOUND WITH CHANGES.** State in §4.2 that mix A is calibrated on the synthetic reference population and provisional until tested in Fermentation; give the recalibration rule its observation, numeric tolerance, minimum population and observer; and tie it to the score-distribution utility (R-08). An independent checker reached the same placement (Separation mode, PF13 Design phase) and the same gap and rated it Major because the brief's D-4 asked how the lines would be revisited; a second checker, re-reading the brief, showed that D-4 asked only to "say how the lines would be revisited, which would mean a new release", which §4.2 answers, that §4.2 names the Product Owner as the decision owner, and that §10.1 discloses the synthetic calibration. I verified each of those passages and rate the finding Minor: what is missing is additive acceptance content (observation, tolerance, minimum population, the D-5 targets as criteria, a provisional label) that the Change's Specification can carry without re-deciding Q-5, and real users do not yet exist, so the observation is a deferred row in any case.

### 5.2 Ψ / Λ / Σ coherence

| Layer | Moved by the proposal | Left inconsistent |
| :- | :- | :- |
| Ψ vision (Glow Story) | bands become "the user-visible signal" in fact as well as name: all four bands and all 360 narrative rows become reachable; scores rank with far fewer ties; the "#1 category" band at the top of a card is Glow for about one pair in ten whatever the category | Reader v1 shows `harmony` only, while the Glow Story puts the viewer's #1-category band at the top of the card: a pre-existing vision/body divergence the proposal leaves unmentioned, and the place where §4.10's Manifestor effect lands unsurfaced. "Glow somewhere" becomes the majority outcome (55.9% of pairs); the Glow Story does not say which meaning of Glow is intended, and the proposal does not ask |
| Λ model (HDE Math Spec, Governance, Schemas) | §7 names the sections that change in PF01 §5.2–§5.4, §6.3, §6.4, §9; PF04 §4.1.5 and §12.1; PF12 §2.1, §2.6, §2.9, §2.10 | §7 omits the invariants v2 breaks: PF01 §5.2.4 "No default map assigns one Channel to both signals of the same category", §5.2.7 "one through six unique canonical Channels" per Balance signal and the `0..200` signal wire domain, §5.2.8 and PF12 §2.9's "fixed v1 invariants" (`0..200` signal domain, two Balance operations as named), PF12 §2.9 `signal_scale: 2` and the loader rules that enforce them, PF04 §12.2's band evidence entry. Applied as written, §7 would leave the model saying one thing and the loader enforcing another (§4.8) |
| Σ body (catalogs, code) | §8 names the code areas and catalogs | §8 omits the hard-coded checks the code carries (§4.1) and the PF09 rows whose targets change (§4.3). The band mapping alone has at least six code homes (`core.py`, `calculators.py`, two helpers in `compute.py`, `magic10/thresholds.py`, the loader's pinned edges, the sampler, the evidence gate); §8 names two, and a per-category mapping would leave the others contradicting the model unless every home changes or they collapse to one |

The HDE Users Guide sampler example the proposal flags (`compat_score 50, band Open`, with `compat_score 75, band Warm` beside it) is in §5.2, not §5.1, and both rows already contradict v1's own lines (50 is Warm, 75 is Glow), so the example needs refreshing regardless of v2 (R-16).

**Score: SOUND WITH CHANGES.** The three layers move in the same direction; the model and body lists are incomplete (R-03, R-04, R-06).

### 5.3 PF13 four elements and definition of done (§C, §I)

| Element | PF13 asks for | What the proposal gives | Score |
| :- | :- | :- | :- |
| FIRE | "Outcome (one sentence): After this change, X is true" and "the smallest observable that proves X" | §1 gives a paragraph of outcomes and a before/after table with measurable targets (no zero scores, 66–80 distinct values, 92.5% of pairs with three or more bands, Warm and Glow templates reached 35.3%). No single sentence, and no observable to read *after release* on real pairs. "The product works" (the Product Owner's words in the brief) is not operationalised | PARTIAL |
| WATER | "No second surface": one formula, one active configuration, public contracts unchanged | one formula; v2 replaces v1 in the adopting release (Q-6); Reader v1 and v2 shapes unchanged (§8); no numerics exposed. One new duplication inside the engine: a derived Type beside the stored vendor `type` (see 5.4) | PARTIAL |
| AIR | "Contract name … version forward … programmatic configuration … rollback is one move" | `config_id` v2.0.0, `magic10_result.v2`, thresholds as a per-category object, centers and Type-pairing catalogs, all governed and versioned; rollback is the complete prior release (PF12 §2.9). Canon forbids running old and new side by side, so coexistence is by release, not by flag, which is the governed posture | SOUND (one inconsistency: the prototype's `-candidate` suffix on the `config_id`) |
| EARTH | "fails closed … the future reader can follow the why … what did we learn" | complete-or-fail-closed stated (§3.1); the why is legible (§1 diagnosis of v1, §2 grounding, §2.6 list of non-doctrine rules, §10 limits); learning captured (why v1 piled up below 25). Two things a future reader would want and will not find: the alternatives rejected for Tables 7a/7b (brief §2.4 route 2) and a statement on double counting (brief D-2) | PARTIAL |

**Definition of done (§I).** FIRE: a skeptical reader would state the same outcome after seeing the result (the harness numbers), so the change matches its claim. WATER: no second public surface. AIR: boundaries named and versioned, additive and reversible. EARTH: safe failure stated; learning captured; the two gaps above.

**Score: SOUND WITH CHANGES.** Add the one-sentence outcome and the post-release success signal (R-08), the alternatives (R-05) and the double-counting statement (R-07).

### 5.4 PF13 tenets (§B)

**Single home per concept.**

| Concept | Homes after v2 | Assessment |
| :- | :- | :- |
| A person's Type | the vendor's stored `type` field (BodyGraph projection), the legacy Type/Strategy module `engine/compat/ts_v0.py` that still reads it (imported by two `hdctl` scripts, a test and an evidence tool; its removal is HDE-CONJ010.5, Not done), and the engine's derived Type (not public, not stored) | three homes that can disagree with no reconciliation surface. The proposal validates agreement on five fixtures and says the vendor field "is not consumed"; it does not say what implementation QA does when they differ for a stored person, nor whether a disagreement should fail closed, be logged, or be ignored. PF13: "if a fact appears in two places, one of them is wrong" |
| Motor to Throat | the governed Direct Motor→Throat set (HDE Math Spec §5.4.2.1, `engine/constants.py`, the `direct_mt` channel flags in `registry_loader.py`, the §6.4 direct-MT flag; "MUST NOT include two-hop routes") and the new any-route predicate | two definitions of one phrase with different semantics. §7 keeps both ("the direct set remains governed; v2's predicate … is stated as such"). Nothing consumes the direct set today ("artifact closure remains an implementation gap") and nothing would after v2, so the clean move is to make the any-route predicate the single home and retire the direct set as a governed scoring input, or name its consumer |
| Center definition in a pair | PF01 §6.3 center tagging `[Speculative]` (dominant / compromise / neutral) and the new four-outcome contract | the proposal names the collision and offers "promote … or retire in favour of it"; the two are different concepts (center-level dominance against definition-based completion), so only "retire" fits, and the decision should be made in the adoption record, not left open |
| Band lines | one home, `math/thresholds.json` | sound |

**Phase discipline and verification before scale.** PF13 §B.6: "Is there a concrete verify step and success signal before release?" The proposal routes verification to the HDE Build Notes 2.15 live compat test, with expected v2 bands for SYN-A and SYN-B (§8), and to the 2.16 owner tests. Those prove determinism, parity and the live path; they do not measure whether the band distribution on real pairs is what the product intends, which is the question v2 exists to answer. The only instrument for that is the Candidate CRD item 13 utility, which does not exist yet and which the proposal does not name. So there is a verify step for correctness and none for the product outcome.

**Score: SOUND WITH CHANGES** (R-08, R-09).

### 5.5 Fit with the phase-named build checklists

| v2 work | Checklist home | Current row and state | Proposal places it there? |
| :- | :- | :- | :- |
| v2 mechanics configuration contract, centers catalog, Type-pairing catalog, schema v2, fail-closed loader, configuration identity | PF09.3 Separation, the shape of Task HDE-SEPA005 "Production Magic10 mechanics configuration contract" | HDE-SEPA005 is Done for v1 and bound to HDE-EPIC040; v2 needs its own Separation task (PF09's collision-free-owner rule) | No. §8 lists code areas only |
| three new signal operations, center outcomes, Type derivation, three-component reduction, Engine Core integration | PF09.4 Conjunction, Task HDE-CONJ010 "Full Magic10 deterministic scoring integration" | Partial; .1, .2, .5 Not done; .3, .4, .6 Partial; its subtask texts describe v1's twenty signals and ten reducers | No |
| full-domain v2 verification, goldens, manifest cut, release attestation | PF09.6 Distillation, Task HDE-DIST008 "Full-domain Magic10 verification and current release binding" | Partial; written around v1 (`magic10_result.v1`, `tests/fixtures/magic10/v1/goldens.json`, `--version 1.1.0`, `M10-CANON-001.adopted_at_utc`) | No |

The proposal's impact list is organised by file, which is how a developer reads it; Glow's checklists are organised by phase, which is how the Product Owner tracks it. Adopting v2 without re-homing these rows would leave HDE-DIST008 verifying a formula the release no longer runs. The brief did not ask for this mapping, so its absence is a gap against Glow's method rather than against the brief.

**Score: SOUND WITH CHANGES** (R-06).

### 5.6 Alchemical verdict

**SOUND WITH CHANGES.** The proposal is in the right phase and stays there; it moves vision, model and body in one direction; its contracts are named and versioned and its failure posture is closed. What it lacks is the Fermentation hook (what real-user observation tests the frozen lines and triggers recalibration), the single-home decisions for Type and for Motor→Throat, the alternatives it rejected, and the placement of its work in the phase-named checklists.

## 6. Findings

Severity scale: **Blocker** (adoption would be wrong or unsafe), **Major** (must change before adoption), **Minor** (should change), **Observation** (worth recording). "PO decision" names the proposal §9 decision the finding bears on, or the new decision proposed in §8 of this review.

| ID | Dimension | Severity | Finding | Evidence | Recommended fix | PO decision |
| :- | :- | :- | :- | :- | :- | :- |
| R-01 | correctness, scope | **Major** | Table 7a is a per-person Type level, not a pair compatibility, and produces undisclosed systematic effects: Manifestor pairs reach Glow in `harmony` (the Reader v1 band) 2.7% of the time against 9.1% overall; row sums are generator +500, projector −50, manifestor −50, reflector −750 per mille, so Generators lead Projectors and Manifestors by about nine total points | §4.10; `manifestor`/`harmony` offset set to 0 gives 5.8%; no Type signal gives 5.8%; totals 448.8 / 440.0 / 440.8 against 436.1 / 432.6 / 435.9 with no Type signal; proposal §9 and §10.1 do not mention it | Decide Q-9: keep Table 7b only, or constrain Table 7a rows to sum to 0; whichever is kept, state the measured per-Type band effects in the adoption record | Q-3b, Q-4, **Q-9** |
| R-02 | correctness, scope | **Major** | Pairs containing a Reflector cannot reach Glow in `balance` or `consistency` (0.0%) and almost never in `alignment` (0.9%), and average 402 against 446 in total; the proposal discloses `balance` only. The cause is the center mechanics (no `shared` center, no bilateral completion, fewer channels), not the Type tables | §4.10; the effect persists with no Type signal (406.4; `balance` and `consistency` Glow 0.0%) | Disclose all three categories in §10.1 and the adoption record; decide whether a 1.2% population with structurally unreachable Glow in three categories is acceptable, or give the `foundation` profile a reading for one-sided completion of a Reflector's open centers | Q-8, **Q-9** |
| R-05 | correctness | **Major** | Two of the six Table 7b rules cite passages that do not support them. `generator_projector` (alignment +100, communication +50) rests on Complete Guide p. 235, which describes a Projector's not-self wish to be a Generator and would, if anything, support `generator_with_nonsacral` (heat, comfort) rather than alignment ("coherence of direction … principles, values", PF01 §5.2.3) or communication ("capacity to formulate … exchange"); the row's gloss ("the Projector recognizes, the Generator supplies energy") draws on pp. 104, 229 and 230, not on p. 235, and the O-02 note inherits the reading. `generator_manifestor` rests on Generators' Course seg. 15, which describes cultural conditioning of Manifesting Generators and says "Manifesting Generators", not "Generators". Three rules cite no passage (`projector_manifestor` is traceable to the p. 230 aura descriptors quoted in §2.4; `same_class` and `reflector_present` to nothing); §2.4 promises "six stated principles (§3.7)" but §3.7 states no principles (its only six-item list is the six pair rules, whose one-phrase bases generate neither Table 7a's forty offsets nor the ±50 to ±250 scale); one basis clause, "Manifestor initiates, Generator responds", is word for word the O-03 blog remark the proposal says it does not rely on, four of the six rules have a counterpart in the recorded blog remarks, and the order of work is not stated; and no rejected alternative is presented although brief §2.4 route 2 requires it ("Tie every step of the inference to cited admitted doctrine … give the alternatives you rejected"). Each misread citation alone would be Minor (at most 1.5 and 0.75 points; the tables are labelled inference); the Major rating is for the Q-3b record as a whole, which asks the Product Owner to adopt a row set whose cited doctrine does not carry the content attributed to it and whose alternatives are unrecorded, and re-examining rows is the Q-3b decision itself, not a Change Flow fix | §3.4, §3.6 | Re-ground or drop the two rules (restate what p. 235 says; correct "Generators" to "Manifesting Generators" in the Table 7b basis and tighten the §2.4 label, which quotes the Manifesting Generator sentence under a "Generators" heading); label the passage-less rules as inference without doctrine; state the principles §2.4 promises or change the sentence; present the alternatives (pairwise-only, zero-sum rows, doctrine-only cells, no Type component, Manifesting Generator as its own class) | Q-3b |
| R-18 | correctness, scope | **Major** | The admitted-collection search behind the gap claim is undocumented and incomplete. HD-RP-05 (A4; its Index entry lists the Type domain, though the Index's M03 routing row does not name it) carries the four aura keynotes and pairwise interaction statements (Projectors and Generators "designed to influence each other … most deeply penetrated and conditioned by each other"; Projectors "glance off" Manifestors and Reflectors; "A bond exists between Ms and Rs"), and HD-COS-01 (A3, context-only) speaks of the Projector–Generator connection; none is recorded, while a non-admitted blog's pair remarks are; and the relational passages of two works the proposal does cite are themselves uncited (Winn seg. 104, Manifestors do well with "other Manifestors or Manifesting Generators", which runs against `generator_manifestor` −50 as applied to Manifesting Generators and is an unrecorded rejected alternative under Q-3c; Generators' Course segs. 7 and 38). The conflicts line wrongly says "resistant" is not an admitted word. The strict claim (no admitted *rule*) stands | §3.5 with line numbers | Record the admitted material in Appendix B at its tier; re-tie each Table 7b row to it or label it unsupported; restate the gap as "no rule, matrix, valence or score"; correct the conflicts line; document the collection search (works, terms) | Q-3a, Q-3b |
| R-03 | feasibility, scope | Minor | The §7 canon delta list omits the normative statements v2 falsifies: PF01 §5.2.4 "No default map assigns one Channel to both signals of the same category"; §5.2.7 one-through-six channels per Balance signal and the `0..200` wire domain; §5.2.8 fixed v1 invariants and the Balance-membership knob; §5.2.2's `magic10:v1:` cache key and preimage `result_schema`; §5.4.3's 45-member statement; PF12 §2.9 `signal_scale`, `rounding.signal`, the one-through-six and no-overlap loader rules, the `0..200` output rule and the fixed-invariant list, and its 45-member statements; PF04 §2.0 token semantics, §9.2's Doc-Delta trigger for band-maxima changes, §12.2 and Appendices B.6 and D band evidence entries (naming paths that do not exist); PF12 §5.1 release-inputs roster, §6.2.1 attestation predicate, §8.14.1 authoritative-config boundary and §8.14.2 `band_edges` artifact; PF02 §2.2 flow description and §3.1 threshold shim; PF01 §5.3's "preset-specific maxima … must not be inferred" sentence and the "single mapping" statements in §5.3.5, §7.2/§8.2 item 5, §7.3 and §8.4 (the brief's own constraint "one monotone band mapping (§5.3)" is not reconciled with ten mappings). Outside the brief's six documents but still needed: PF05's `magic10_compat_result.v1` and `q` in `0..200` on `hdctl showcompat` stdout and `POST /api/compat/v1`, PF14's result identities and `THRESHOLDS_V1` derivation rule, and PF07's canonical target path (PF19's `CONFIG_MAGIC10_OK` wording is generic and may survive unchanged; it should be checked). Both v2 Balance signals read all 36 channels and signals become per-mille | §4.8 with line numbers; `engine/magic10/signals.py` enforces the 1..6 bound and the "overlapping category signals" error today | Add the omitted sections and statements to §7 as explicit changes (a "rules relaxed and their replacements" table), name the Balance change as a §5.2.8 structural mechanics revision with its Doc Delta, state that per-category maxima are the single §5.3 mapping and not a preset, cite PF04 §9.2 in the recalibration rule, and add a "beyond the brief's list" paragraph for PF05, PF14, PF19 and PF07. Completing the list is Change Flow work that does not re-decide the design, but it must precede the Doc Delta | Q-8 |
| R-04 | feasibility | Minor | §8's impact inventory is materially incomplete and understates the cost: of the fifteen surface groups in §4.1 it names one fully and six partly (counting its generic mentions of schemas, goldens and release constants as coverage) and omits eight. Omitted: `engine/magic10/thresholds.py` and `engine/compat/thresholds.py`, which read the flat edge list at import and would fail at import on a per-category thresholds file; the admission loader's literal closure checks (90 channel rows, `config_id`, 1..6 membership, no category overlap, `signal_scale`, result schema, and `edges == [24, 49, 74, 100]` at line 1204); `_pure_result_matches` and the hard-coded `_band_for_score` in `compute.py`; the evidence gate `tools/evidence/run_canonical_json_gate.py`, which checks every category band against the global `band_for` (the band mapping has at least six code homes today and §8 names two); the internal compat result identity on the two internal surfaces (`hdctl showcompat` stdout, `POST /api/compat/v1`); the three result and configuration schema files and a schema for the per-category thresholds; the consumer bundle schemas and `band_edges` artifact (a governed consumer contract under PF12 §8.15); the dev sampler's single-score band (`engine/sampler/core.py`), which has no mapping under per-category lines; the determinism-gate proof generator and sanity pipeline; and the breadth of pinned tests (at least nine files by my narrow search, three of the five 2.16 owner tests among them; 22 to 34 of the 220 test files by independent checkers' broader pattern sets) | §4.1 | Rewrite §8 as an enumerated surface inventory grouped by import-time and loader literals, kernel modules, compat and CLI/HTTP result identity, consumer bundles and evidence generators, tests and fixtures, and release-cut constants; or state plainly that §8 is indicative and that the Change's implementation plan will enumerate. Fixable in the Change without re-deciding the design, but the Product Owner should read the cost as understated | Q-6 |
| R-06 | scope, alchemical | Minor | Open PF09 work is not accounted for: HDE-DIST008 (Partial) is written around v1 (`magic10_result.v1`, v1 goldens, Balance operations, band edges, manifest `1.1.0`); HDE-CONJ010 (Partial; .1, .2, .5 Not done) describes v1's signal producers and reducer; HDE-SEPA005 (Done) is the shape of the v2 configuration contract that needs a new task; HDE-COAG003.6 "Magic10 active-config cutover guard" (Not done) is where Q-6 lands. HDE-DIST008.1 and HDE-CONJ010.5 require the absence of a "Type-only fallback", and the proposal should state that its bounded Type component is not that | §4.3, §5.5 | The adoption addendum or the Change specification names the rows v2 re-targets and the new Separation task, and states in one sentence that the Type component is derived from the gate set and never scores alone | **Q-12** |
| R-07 | scope, correctness | Minor | Brief D-2 ("avoid double counting; state exactly how the two contributions combine") and the HDE Math Spec §7.3/§8.3 invariant "no double counting … derivation provenance cannot create an independent contribution" are not addressed in words anywhere in the proposal. The overlap is structural: an electromagnetic channel is scored once in `C` through its signal response (7500 basis points) and again in `Z` as the `mutual` center outcome it alone creates (10000 basis points); a motor–Throat definition feeds the `motor_throat` center feature and the Type component; a Reflector's absence of definition feeds the center component and Table 7a. Measured on the reference population the overlap is modest: `C` and `Z` correlate at 0.02 to 0.33 in nine categories and 0.44 in `balance`; the covariance share of score variance is −6% to 17% outside `balance` (31% there); `Z` changes 20% to 39% of bands and the score ranks differently without it (Spearman 0.855 to 0.967); the two Balance signals are negatively correlated (−0.20), so they are not redundant. The gap is therefore a missing justification, not a design defect | §4.6; the words "double", "twice" and "overlap" do not occur in the proposal; measurements in §7 | Add an explicit double-counting statement to §3.6/§3.8: `C` scores channel relevance and `Z` where the connection lands, with the measured `C`–`Z` correlation and `Z`'s information beyond `C` per category, and a sentence on why two readings of the same channels in `balance` (owner mass against mutual share) are not one contribution counted twice | Q-1, Q-4 |
| R-08 | alchemical, scope | Minor | The frozen per-category lines have their recalibration *mechanism* (§4.2: new thresholds bytes, new release, a Product Owner decision) and a qualitative trigger disclosed in §10.1 ("a real user pool will fall differently … that is the recalibration case of §4.2"), but no Fermentation hook: no named observation (which measure, from which surface, recorded where), no tolerance against the target mix, no minimum real population before an observation counts, no one named to perform it, and no PF09 Fermentation row; the lines are not labelled provisional. Brief D-5 asked for *proposed measurable targets*; the proposal reports the measured values (92.5% of pairs with three or more bands; least-used band 9.1%) and the qualitative criterion "all four bands are a meaningful share of every category" (§4.4), but sets no value that would count as pass or fail on a real population. There is also no PF13 FIRE outcome sentence or success signal | §5.1, §5.3; proposal §4.2, §4.4, §5.4, §10.1 | Extend §4.2 into a complete recalibration rule: the observation (realised per-category band mix and distinct bands per pair over the stored real population, from the admin numeric result via the score-distribution utility), a tolerance against the target, a minimum population, who observes, and a deferred PF09.5 row; set the D-5 targets as acceptance criteria; label the v2.0 lines "calibrated on the synthetic reference population"; add the one-sentence outcome. Additive content the Change's Specification can carry without re-deciding Q-5 | Q-5, **Q-11** |
| R-09 | alchemical, feasibility | Minor | Single-home collisions left open. Type would have three homes: the stored vendor `type` in the BodyGraph projection, the legacy Type/Strategy module `engine/compat/ts_v0.py` that still reads it (imported by `scripts/hdctl.clean.py`, `scripts/hdctl.backup.py`, a test and an evidence tool; its removal is HDE-CONJ010.5, Not done), and the new derived Type in Engine Core, with no rule for when derived and stored disagree. Motor→Throat would have two definitions: the governed direct set (§5.4.2.1 "MUST NOT include two-hop routes", `engine/constants.py`, the `direct_mt` channel flags in `registry_loader.py`, the §6.4 direct-MT flag) with no consumer after v2, beside the any-route predicate. §6.3 center tagging beside the four-outcome contract is left "promote or retire". The score-distribution utility, the only instrument for the product outcome, is not named as a dependency | §5.4, §4.4 | Decide each in the adoption record and recommend one disposition rather than coexistence: the derived Type is the single scoring home and the stored `type` is non-scoring vendor metadata, with implementation QA comparing them and a stated failure mode on divergence; retire the direct set as a governed scoring input or name its consumer; retire §6.3 in favour of the four-outcome contract with its actor indication re-homed to the `one_sided` owner; name item 13 as a dependency | Q-7, **Q-11** |
| R-10 | feasibility | Minor | The scripts do not run as published: `hdmech.py` hard-codes the author's scratch `REPO`; the directory layout is undocumented; engine runs need the clone root as working directory (narrative-pack loader); `measure.py` lacks the D and E targets of §4.4; the §3.7 variance shares and §5.5 inter-category correlation come from unpublished code; the prototype's `config_id` ends in `-candidate` (and so does Appendix D's); the prototype keeps the v1 operation names (`weighted_state_sum_v1`, `twice_min_owner_mass_v1`, `companionship_em_mass_v1`) with v2 semantics where §3.5 and §7 name `saturating_state_sum_v2`, `bilateral_owner_mass_v2`, `mutual_state_share_v2`; `v2_goldens.json` bytes vary with the hash seed | §3.1, §4.5, §7 | Parameterise `REPO`, document the layout and the working directory, add the two targets and the statistics code to Appendix C, align the `config_id` and operation names, iterate centers in a fixed order | none |
| R-11 | correctness | Minor | The Type-derivation validation set is small and selectively reported: five fixtures match (the two vendor-shaped ones are synthetic and carry centers fields inconsistent with their own gates: `alice.json` lists Ajna and Solar Plexus beside the G, Sacral and Throat its gates define, and the source-invariance fixture lists only Ajna and Solar Plexus while its gates 10, 20 and 34 define G, Sacral and Throat, so for them only the Type comparison is meaningful), `fixtures/charts/bob.json` (a hand-made fixture whose gates contradict its own channel list) would not and is omitted without disclosure, two further vendor-backed charts in audit artifacts match and were not checked, and no chart exercises an indirect motor→Throat route, so the set cannot test the any-route rule | §3.3 | State the full set and the exclusion reason; add the two audit charts; for Q-7 rely on doctrine and shares, and add an indirect-route check to implementation QA against SYN-A, SYN-B and production rows | Q-7 |
| R-15 | correctness | Minor | The doctrinal example given for `one_sided` completion (PF08, Johannes and Renate's emotional base through 37-40) is, by the proposal's own §3.5 rule, a `mutual` completion: Johannes carries gate 40 (Personality Venus) and Renate gate 37, so the channel is electromagnetic and the Solar Plexus is defined only together; the only center Renate conditions one-sidedly there is the Heart (21-45). The quoted words are accurate; the concept remains grounded in D-02 and D-03 | §3.4; PF08 lines 584, 1346, 1352–1356 | Re-ground `one_sided` on D-02 ("a female … who connects his Solar Plexus Center") and D-03 (a defined Spleen meeting an unconnected one); use Johannes and Renate as the `mutual` example | none |
| R-19 | feasibility, scope | Minor | The result schema v2 is called "same shape as v1" (§3.3 step 10, §7) although the signal domain widens from `0..200` to `0..1000`, which `magic10_result_v1.schema.json` and `magic10_compat_result_v1.schema.json` pin as `q` maximum 200; and the v2 configuration gives no values for the fixed fields `signal_scale`, `response_scale`, `rounding.signal` and `rounding.category`, which PF12 §2.9 and `core.py` pin to v1 values. `math/thresholds.json` changes shape in place at the same path although it carries `"version": "1"`, with no version step named. HDE Math Spec §7.2 items 4–5 require every value stated; PF13 §C AIR asks for a versioned seam rather than a rewrite of a live contract | §4.8; `schemas/`; `engine/core/core.py` `_validate_bundle`; `math/thresholds.json` | State that the result and compat-result v2 schemas widen `q` to `0..1000`, that the compat-result change is an internal API contract change, give the v2 values (or replacements) for the four fixed fields, and bump the thresholds artifact's `version` (or move it to a new path) | Q-6 |
| R-20 | feasibility | Minor | §8's release-cut bullet omits evidence: the determinism-gate proofs (`audit/gates/parity/…`, generated from `fixtures/charts/alice.json` and `bob.json`) and the band-edge artifacts embed the release identity and bands and are drift-checked by the sanity pipeline, while PF04 §4.1.6 forbids regenerating historical captures "merely because the manifest or release ID changes" | §4.1; `tools/evidence/generate_determinism_gate_proofs.py` lines 30–87; PF04 lines 1352–1360 | Add to §8 a "current evidence to regenerate" list and a "historical captures to leave frozen" list, with the decision owner named | Q-6 |
| R-21 | feasibility | Minor | Three v2 rules have no stated governed home: the Type-to-aura-class mapping and class names; the `I`-rule predicate names and semantics; and the `motor_throat` key in the center map, which is not a center, so the proposal's own proposed loader rule "every center in the map exists" would reject the `heat` and `drive` rows. Per-category lines also need a loader rule that every category has a four-value set ending in 100 | §4.1; proposal lines 200, 207, 420; `m10v2.py` lines 36–47, 85–94 | Put the class list and predicate names as closed enums in the Type-pairing catalog schema, have the loader reject unknown names, name `motor_throat` as the one permitted non-center key, and add the per-category line rule | Q-8 |
| R-22 | scope | Minor | HDE Math Spec §7.2/§8.2 item 6 requires "a decision on how presets interact with intrinsic scores and viewer preferences", and brief §6 requires viewer preferences kept outside intrinsic scores; the proposal never states it (the words "viewer", "preset" and "caller" do not occur in §1–§10), meeting it only implicitly through §3.8's "nothing but the two masks and the governed catalogs is read" | §4.7 | Add one sentence to §3.8 and to the §7 PF01 §5.2.5/§5.2.6 entry: viewer preferences, presets and caller weights remain sampler and ranker inputs and never enter `C`, `Z`, `T`, scores or bands | Q-6 |
| R-23 | scope | Minor | Brief §7 deliverable 5 asks for "the effect of moving each weight by ±20%"; §5.7 moves knobs in groups (each category's largest center weight only; all Table 7a offsets together; all Table 7b offsets together; the three non-zero center responses together; the four non-zero signal responses together), so individual weights were not tested | §4.6; proposal §5.7 | Add a per-weight table, or justify the grouping and list the individual weights not tested | Q-4 |
| R-24 | correctness | Minor | The Reflector basis is mis-sourced and the collection's gap on the Reflector definition is unrecorded. Register row D-22 gives the heading "The Sleep State is Our Deepest Conditioning Process" (printed p. 116) for a passage that stands on p. 122 under "The Program is at Work in the Sleep State", and labels "deeply, deeply, deeply open" source doctrine although the sentence is predicated of sleeping raves in the Dream Rave discussion ("Among sleeping raves 35% are Reflectors; deeply, deeply, deeply open. We are incredibly vulnerable when we sleep"); reading it as a statement about the waking Type is inference. Table 7a's "mirrors" has no admitted citation: the Complete Guide text layer has no Reflector "mirror" statement, and the only sources in the collection that say it are Winn's A5 chapters (*Understanding Your Clients* seg. 120: "karmic mirrors", "function like mirrors"), uncited, and the non-admitted blog recorded as not relied on. The Complete Guide's text layer names Reflectors on pp. 103, 122, 187 and 229 only and never defines the Type mechanically; in the admitted collection "no centers defined" occurs only in Winn (A5), which §2.4 cites as corroboration. So the §3.4 branch `defined is empty → Reflector`, correct as standard mechanics, rests in this collection on A5 corroboration and an A2 quote read out of context, and neither §2.4, §2.6 nor §10.1 records that the admitted primary works give no mechanical Reflector definition, which brief §2.4 requires to be stated before a route is taken | §3.3, §3.4 | Correct the D-22 heading and relabel its claim status; cite p. 122 for the 1.4% only; add an S-row for Winn seg. 120 or drop "mirrors"; record under §2.4 that the admitted A2 and A3 works give no mechanical Reflector definition and that the rule rests on A5 corroboration, or locate an admitted A3 passage that states it | Q-3b |
| R-25 | correctness | Minor | Three §2 rules carry a stronger claim status than the collection supports, and would enter the Math Spec as doctrine with it. I-5 (any connected route from a motor to the Throat) is labelled source doctrine, but the Complete Guide states the mechanism through one worked example (p. 232: a Root power source bridged by gate 57 "would immediately turn this Projector into a Manifestor") and nowhere as a general rule; the general statement is Winn's (A5). I-6 (Manifesting Generator shares the Generator aura class) is labelled source doctrine, but the Generators' Course sentence concerns Strategy, the Complete Guide's text layer never names Manifesting Generators, and no admitted work states their aura; the nearest support, Holistic Analysis seg. 199 ("The aura is the Type … a Generator, so … an open and enveloping aura"), is uncited, no rejected alternative is recorded for I-6 (Q-7 records one for I-5), and Q-3c puts "with one aura" outside the quotation. The four-motor set is introduced under "(All source doctrine.)" and `hdmech.py` comments "doctrine: four motors", but the Root's motor status is stated only in A4 (HD-CIRCUIT-01) and A5 (Winn), and §2.6 has no row for the set. §2.6 also says its statuses come from Index §10 but drops "provisional teaching" and adds two labels | §3.3, §3.4 | Relabel I-5 and I-6 "analyst inference from source doctrine, corroborated by A5"; add a MOTORS row with the Root's status; record I-6's rejected alternative (Manifesting Generator as a fifth class) and the A5 counter-indication (Winn seg. 104); cite Holistic Analysis seg. 199 and HD-CROSS-01's direct-channel statement; reword Q-3c; state the vocabulary departure from Index §10 | Q-3c, Q-7 |
| R-12 | scope | Observation | A pair with no connecting channel and no composite definition scores 0 to 11 from the Type component alone (G001), where v1 scored 0; this is a product choice presented as a mechanical expectation | §3.2 | State it as a choice and let the Product Owner decide | **Q-10** |
| R-13 | correctness | Observation | Citation form and label issues, none affecting a number: D-18/D-19 spliced in reverse source order; D-20 drops a repeated word; D-13 names the previous page's heading; D-23 omits p. 115 and is cited by no rule; D-07 resolves PF08's "[clarity/relevance — unclear]" to "[relevance]"; D-09 truncates two center keynotes without ellipsis; S-01 cited for route though silent on it (Winn seg. 51 is the passage); "Conflicts: none found" omits Winn's "penetrating" for Manifestors; HD-SELF-01 not recorded; "one defensive clamp" (there are two, one inactive); Table 7b's absent categories default to 0; the "two-thirds" hedge dropped; the acquisition record lacks edition and proposed role; the §7 PF01 §6.3 entry calls the four-outcome contract a "promotion" of a different concept (only "retire" fits) and offers two options without the recommendation the brief requires; the §7 PF10 entry would "supersede" a record that is not in the current base version; §5.2.8 is cited without saying which of PF01's two §5.2.8 sections is meant; the §7 PF17 and PF10 entries do not record that `balance`'s construct changes from owner-mass equilibrium to bilateral completion while its 36 narrative templates stay (they fit both readings); the §1 table omits one of the brief's §4.3 measures ("Channels a pair forms, of 36", unchanged by the formula); the proposal's claim-status vocabulary (adds "outside source" and "product choice", drops "provisional teaching") is not mapped to the Index §10 statuses; Q-3c says the derived Type "is validated and reported" but no result or admin schema in the proposal carries it (only the analysis prototype emits it); Appendix C's `m10v2.py` is a complete reference implementation inside an ephemeral record, which PF13 §F warns can become a de facto normative source, so the adoption addendum should say the PF01 Doc Delta is the formula's home; several PF08 locators in Appendix B are sub-headings added by the Markdown transcription rather than headings of the original text, and D-04/D-05's named heading "Transfer to the Body Graph" stands hundreds of lines from the quoted passages (the opening words Appendix B gives make every quote findable regardless); Appendix A's 07-31 row drops the source's quotation marks around "good" and "bad" | §3.2, §3.4, §3.5, §4.8 | Correct in a v1.1 of the proposal | none |
| R-14 | scope | Observation | Under mix A, a Glow somewhere is the majority outcome (55.9% of pairs; 11.3% show three or more); Glow keeps its meaning per category (one pair in ten) and loses it as a pair-level rarity. Mix D gives one pair in three. The proposal does not state which meaning is intended | §3.7 | Say so under Q-5 | Q-5 |
| R-16 | scope | Observation | The HDE Users Guide sampler example the proposal flags is in §5.2 (line 310), not §5.1, and both of its rows (`compat_score 50, band Open`; `compat_score 75, band Warm`) are already wrong under v1's own lines (50 is Warm, 75 is Glow); it is a pre-existing defect, not a v2-caused delta, and per-category lines would additionally require it to name a category | §4.8 | Correct the citation and the characterization in the PF29 delta | none |
| R-17 | feasibility | Observation | Pre-existing canon drift the v2 Doc-Delta will meet: PF04 §12.2 cites `tests/compat/bands_thresholds/*` and Appendix D cites `audit/gates/bands/edges.snapshot.json`, neither of which exists in the repository; PF01 carries two sections numbered §5.2.8 (lines 798 and 818); PF01 §2.5's "V2" means Reader v2 and will sit beside Magic10 v2; PF09.6 HDE-DIST008.2 pins `--version 1.1.0` while the current cut is `1.3.0` | §4.8 | Name the real band-golden evidence in the PF04 delta; have the adopting Doc-Delta renumber the second §5.2.8, qualify "Reader v2" in PF01 §2.5 and refresh DIST008.2's version text | none |

## 7. Independent re-measurements: how to rerun them

Everything below ran in a scratch directory outside both repositories, under `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0`, with Python 3.13.18, PyEphem 4.2.1 and the repository's `requirements.txt` installed in a virtual environment, and a clone of `main` checked out at `0bf99656`.

### 7.1 Layout, extraction and the one-line patch

```text
run/
  gen_people.py        Appendix C.1 (SHA-256 488dafea…)
  v1_perpair.py        Appendix C.2 (6df1e78f…)
  harness/
    hdchart.py         score-range record Appendix A (5969513b…)
    distribution.py    score-range record Appendix C (ee544853…)
  out/                 outputs
  v2/
    hdmech.py          Appendix C.3 (d5165bba…), REPO patched (see below), then ac5998bb…
    m10v2.py           Appendix C.4 (507c6e67…)
    measure.py         Appendix C.5 (5663dede…)
    sensitivity.py     Appendix C.6 (6c5f0e0b…)
    goldens.py         Appendix C.7 (8f318697…)
    review_stats.py    this review's script (§7.3)
```

Extraction: for each heading of the form ``### C.n `name.py` (SHA-256 `…`)`` take the first fenced block after it and write it with one trailing newline; the digests then match. The only edit was line 9 of `hdmech.py`:

```diff
-REPO = pathlib.Path("/tmp/claude-0/-home-user/5d854c62-60a7-548f-87fb-0d88643ee7eb/scratchpad/hde/repo")
+REPO = pathlib.Path("<absolute path of the clone of main at 0bf99656>")
```

### 7.2 Commands, in order, from the clone root

The working directory must be the clone root: `engine/narratives/loader.py` resolves `catalog/narratives` relative to the current directory and otherwise raises `no narrative pack files found`, which the proposal does not say.

```bash
cd <clone>
python run/gen_people.py                                   # 1.7 s; people.json sha256 bb7e336d… (matches Appendix D)
python run/v1_perpair.py <clone>                           # 64 s; v1_perpair.json sha256 eba6413e… (matches Appendix D)
python run/harness/distribution.py <clone> run/out/v1_distribution.json 2000 20000 cache   # 65 s; reproduces the record
python run/v2/measure.py                                   # 20 s; two_run_sha256 9ec56f04…cb53, abba_identical true
python run/v2/goldens.py                                   # 1 s
python run/v2/sensitivity.py                               # 104 s
python run/v2/review_stats.py                              # 72 s; writes run/out/review_stats.json
```

To reproduce the §4.4 rows D and E, which `measure.py` does not compute, add `"D_30_40_25_5": (30, 40, 25, 5)` and `"E_35_35_22_8": (35, 35, 22, 8)` to its `targets` dictionary, or run:

```python
from measure import calibrate, mix, reader_stats, masks, pairs, ORDER
import m10v2 as v2
res = [v2.score_pair(masks[a], masks[b], v2.CONFIG) for a, b in pairs]
by = {k: [r["scores"][k] for r in res] for k in ORDER}
for t in ((30, 40, 25, 5), (35, 35, 22, 8)):
    lines = calibrate(by, [x / 100 for x in t]); print(lines, reader_stats(res, lines))
```

### 7.3 `review_stats.py` (SHA-256 of the file as run: `92fcf96a9c35ec91ee7ea0343d057bcd2c64c9837640d190a96270680ee184f3`)

The script hard-codes the §4.4 lines from the proposal's table rather than reading the author's `v2_measure.json`, so the band figures it reports are independent of that file. Seeds and eras for the out-of-sample populations are in the `D` section of the script; charts come from `hdchart.gates_utc` with the mean node, as in the proposal.

```python
"""Independent re-measurement for the Magic10 v2 review (reviewer's own script).

Frozen lines are the proposal's published §4.4 table (typed in here), not the author's JSON.
Parts: A reference-population mix and reader stats; B Type fairness; C constant-offset decomposition;
D out-of-sample populations (seeds, eras); E Glow meaning; F v1 comparison if v1_perpair.json exists.
"""
from __future__ import annotations
import collections, copy, datetime as dt, json, pathlib, random, statistics, sys, uuid
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE.parent / "harness"))
import hdmech as m, m10v2 as v2
from hdchart import gates_utc
OUT = HERE.parent / "out"; ORDER = v2.ORDER; BANDS = ("Cool", "Open", "Warm", "Glow")
LINES_44 = {  # proposal §4.4, inclusive maxima
 "harmony": [35, 45, 54, 100], "heat": [36, 46, 56, 100], "communication": [36, 48, 58, 100],
 "alignment": [39, 49, 58, 100], "comfort": [34, 45, 53, 100], "consistency": [44, 55, 65, 100],
 "expansion": [32, 43, 53, 100], "creativity": [34, 44, 54, 100], "drive": [42, 54, 63, 100], "balance": [52, 63, 71, 100]}
cfg = copy.deepcopy(v2.CONFIG); cfg["bands"] = LINES_44
report = {}

def mix(scores, maxima):
    n = len(scores); c = collections.Counter(v2.band_of(s, maxima) for s in scores)
    return {b: round(100 * c[b] / n, 1) for b in BANDS}

def score_all(masks, pairs, cfg):
    return [v2.score_pair(masks[a], masks[b], cfg) for a, b in pairs]

def reader_stats(res, lines):
    distinct = collections.Counter(); any_glow = 0; wg = 0; nglow = collections.Counter()
    for r in res:
        bands = [v2.band_of(r["scores"][k], lines[k]) for k in ORDER]
        distinct[len(set(bands))] += 1; g = bands.count("Glow"); any_glow += g > 0; nglow[g] += 1
        wg += sum(b in ("Warm", "Glow") for b in bands)
    n = len(res)
    return {"distinct_pct": {k: round(100 * distinct[k] / n, 1) for k in sorted(distinct)},
            "pairs_any_glow_pct": round(100 * any_glow / n, 1), "warm_or_glow_results_pct": round(100 * wg / (10 * n), 1),
            "glow_count_per_pair_pct": {k: round(100 * nglow[k] / n, 1) for k in sorted(nglow)}}

def overall_mix(res, lines):
    c = collections.Counter(v2.band_of(r["scores"][k], lines[k]) for r in res for k in ORDER); n = 10 * len(res)
    return {b: round(100 * c[b] / n, 2) for b in BANDS}

def tie_rate(v):
    n = len(v); c = collections.Counter(v); return sum(x * x for x in c.values()) / (n * n)

# ---------- A. reference population ----------
P = json.loads((OUT / "people.json").read_text()); masks = [m.mask_of(p["gates"]) for p in P["people"]]; pairs = P["pairs"]
res = score_all(masks, pairs, cfg)
by = {k: [r["scores"][k] for r in res] for k in ORDER}
A = {"overall_mix": overall_mix(res, LINES_44), "per_category_mix": {k: mix(by[k], LINES_44[k]) for k in ORDER},
     "reader": reader_stats(res, LINES_44),
     "per_category": {k: {"mean": round(statistics.mean(by[k]), 1), "min": min(by[k]), "max": max(by[k]), "zero_pct": round(100 * by[k].count(0) / len(by[k]), 2),
                          "distinct": len(set(by[k])), "tie_pct": round(100 * tie_rate(by[k]), 2)} for k in ORDER}}
types = [m.derive_type(mk) for mk in masks]
A["type_shares_pct"] = {t: round(100 * c / len(types), 1) for t, c in collections.Counter(types).items()}
A["solar_plexus_defined_pct"] = round(100 * sum("solar_plexus" in m.defined_centers(mk) for mk in masks) / len(masks), 1)
# direct-only alternative
def direct_mt(mask):
    return any(cid in m.complete_channels(mask) for cid in ("12-22", "20-34", "21-45", "35-36"))
def derive_direct(mask):
    d = m.defined_centers(mask)
    if not d: return "Reflector"
    mt = direct_mt(mask)
    return ("Manifesting Generator" if mt else "Generator") if "sacral" in d else ("Manifestor" if mt else "Projector")
changes = collections.Counter((t, derive_direct(mk)) for t, mk in zip(types, masks) if t != derive_direct(mk))
A["direct_only_type_changes"] = {f"{a}->{b}": c for (a, b), c in changes.items()}; A["direct_only_changed_total"] = sum(changes.values())
report["A_reference"] = A
print("A overall mix", A["overall_mix"]); print("A reader", A["reader"]); print("A types", A["type_shares_pct"], "SP", A["solar_plexus_defined_pct"]); print("A direct-only changes", A["direct_only_type_changes"], A["direct_only_changed_total"])

# ---------- B. Type fairness ----------
cls = [m.aura_class(t) for t in types]
B = {"by_pair_class": {}, "by_person_type": {}, "harmony_glow_by_presence": {}, "glow_any_by_presence": {}}
pairs_with = collections.defaultdict(list)
for i, (a, b) in enumerate(pairs):
    for c in {cls[a], cls[b]}: pairs_with[c].append(i)
    pairs_with["pair:" + "+".join(sorted((cls[a], cls[b])))].append(i)
for key, idx in sorted(pairs_with.items()):
    sub = [res[i] for i in idx]
    totals = [sum(r["scores"][k] for k in ORDER) for r in sub]
    row = {"n_pairs": len(sub), "mean_total": round(statistics.mean(totals), 1),
           "harmony_glow_pct": round(100 * sum(v2.band_of(r["scores"]["harmony"], LINES_44["harmony"]) == "Glow" for r in sub) / len(sub), 1),
           "any_glow_pct": round(100 * sum(any(v2.band_of(r["scores"][k], LINES_44[k]) == "Glow" for k in ORDER) for r in sub) / len(sub), 1),
           "glow_pct_by_cat": {k: round(100 * sum(v2.band_of(r["scores"][k], LINES_44[k]) == "Glow" for r in sub) / len(sub), 1) for k in ORDER},
           "mean_by_cat": {k: round(statistics.mean(r["scores"][k] for r in sub), 1) for k in ORDER}}
    (B["by_pair_class"] if key.startswith("pair:") else B["by_person_type"])[key] = row
alltot = [sum(r["scores"][k] for k in ORDER) for r in res]
B["overall"] = {"mean_total": round(statistics.mean(alltot), 1), "harmony_glow_pct": round(100 * sum(v2.band_of(r["scores"]["harmony"], LINES_44["harmony"]) == "Glow" for r in res) / len(res), 1)}
# person-level: mean total over each person's partners, averaged by Type
per_person = collections.defaultdict(list)
for (a, b), r in zip(pairs, res):
    t = sum(r["scores"][k] for k in ORDER); per_person[a].append(t); per_person[b].append(t)
pt = collections.defaultdict(list)
for i, lst in per_person.items(): pt[types[i]].append(statistics.mean(lst))
B["person_mean_total_by_type"] = {t: {"n_people": len(v), "mean": round(statistics.mean(v), 1), "min": round(min(v), 1), "max": round(max(v), 1)} for t, v in pt.items()}
# T-table column sums per class (per mille) = systematic Type level
B["A_table_row_sums_per_mille"] = {c: sum(cfg["type_a"][c].values()) for c in cfg["type_a"]}
report["B_type_fairness"] = B
print("B overall", B["overall"]); print("B by presence:", {k: (v["n_pairs"], v["mean_total"], v["harmony_glow_pct"], v["any_glow_pct"]) for k, v in B["by_person_type"].items()})
print("B person-level mean total by type", B["person_mean_total_by_type"]); print("B A-row sums", B["A_table_row_sums_per_mille"])

# ---------- C. constant offsets ----------
C = {}
# component means
C["component_means_per_mille"] = {k: {c: round(statistics.mean(r[c][k] for r in res)) for c in ("C", "Z", "T")} for k in ORDER}
C["mean_points_from_T"] = {k: round(0.015 * statistics.mean(r["T"][k] for r in res), 2) for k in ORDER}
C["mean_points_from_Z"] = {k: round(0.025 * statistics.mean(r["Z"][k] for r in res), 2) for k in ORDER}
C["mean_points_from_C"] = {k: round(0.060 * statistics.mean(r["C"][k] for r in res), 2) for k in ORDER}
# variance share of each component (as in proposal): var(0.015 T)/var(score) etc.
def var(v): mu = statistics.mean(v); return sum((x - mu) ** 2 for x in v) / len(v)
C["variance_share_pct"] = {}
for k in ORDER:
    s = by[k]; vs = var(s)
    C["variance_share_pct"][k] = {c: round(100 * var([f * r[c][k] for r in res]) / vs, 1) for c, f in (("C", 0.06), ("Z", 0.025), ("T", 0.015))}
# zeros with T removed (blend 60/25/0 renormalised? no: keep weights, T:=0) and with T fixed at 500 (no Type signal)
def rescored(mod):
    c2 = copy.deepcopy(cfg); mod(c2); return score_all(masks, pairs, c2)
def zero_T(c2): c2["blend"] = {"channel": 60, "center": 25, "type": 0}
def flat_T(c2):
    for cl in c2["type_a"]: c2["type_a"][cl] = {k: 0 for k in ORDER}
    c2["type_i"] = []
rT0 = rescored(zero_T); rTflat = rescored(flat_T)
C["zero_pct_if_T_weight_0"] = {k: round(100 * sum(r["scores"][k] == 0 for r in rT0) / len(rT0), 2) for k in ORDER}
C["zero_pct_if_T_flat_500"] = {k: round(100 * sum(r["scores"][k] == 0 for r in rTflat) / len(rTflat), 2) for k in ORDER}
C["min_if_T_weight_0"] = {k: min(r["scores"][k] for r in rT0) for k in ORDER}
C["pairs_with_C_and_Z_both_zero_pct"] = {k: round(100 * sum(r["C"][k] == 0 and r["Z"][k] == 0 for r in res) / len(res), 2) for k in ORDER}
# mix under frozen lines if T flat (shows how much T moves bands)
C["mix_if_T_flat_500"] = overall_mix(rTflat, LINES_44)
C["spearman_T_flat_vs_base_min"] = None
report["C_constants"] = C
print("C comp means", C["component_means_per_mille"]); print("C points from T", C["mean_points_from_T"]); print("C var share", C["variance_share_pct"])
print("C zero% if T weight 0", C["zero_pct_if_T_weight_0"]); print("C zero% if T flat", C["zero_pct_if_T_flat_500"]); print("C C&Z both zero", C["pairs_with_C_and_Z_both_zero_pct"]); print("C mix if T flat", C["mix_if_T_flat_500"])

# ---------- D. out of sample ----------
def population(seed, start, end, n_people=2000, n_pairs=20000):
    rng = random.Random(seed); s = dt.datetime(*start); span = (dt.datetime(*end) - s).total_seconds()
    ppl = [gates_utc(s + dt.timedelta(seconds=rng.random() * span), true_node=False) for _ in range(n_people)]
    prs, seen = [], set()
    while len(prs) < n_pairs:
        a, b = rng.sample(range(n_people), 2); key = (min(a, b), max(a, b))
        if key not in seen: seen.add(key); prs.append([a, b])
    return [m.mask_of(g) for g in ppl], prs
D = {}
for name, seed, start, end in [("seed20261102_1950-2005", 20261102, (1950, 1, 1), (2006, 1, 1)), ("seed7_1950-2005", 7, (1950, 1, 1), (2006, 1, 1)),
                               ("seed20261101_1985-2005", 20261101, (1985, 1, 1), (2006, 1, 1)), ("seed20261101_1995-2004", 20261101, (1995, 1, 1), (2005, 1, 1)),
                               ("seed20261101_1950-1970", 20261101, (1950, 1, 1), (1971, 1, 1)), ("seed20261101_1970-1990", 20261101, (1970, 1, 1), (1991, 1, 1)),
                               ("seed20261101_2000-2008", 20261101, (2000, 1, 1), (2009, 1, 1))]:
    mk, pr = population(seed, start, end); rr = score_all(mk, pr, cfg)
    tt = collections.Counter(m.derive_type(x) for x in mk)
    D[name] = {"overall_mix": overall_mix(rr, LINES_44), "per_category_glow_pct": {k: mix([r["scores"][k] for r in rr], LINES_44[k])["Glow"] for k in ORDER},
               "per_category_cool_pct": {k: mix([r["scores"][k] for r in rr], LINES_44[k])["Cool"] for k in ORDER},
               "reader": reader_stats(rr, LINES_44), "type_shares_pct": {t: round(100 * c / len(mk), 1) for t, c in tt.items()},
               "mean_total": round(statistics.mean(sum(r["scores"][k] for k in ORDER) for r in rr), 1)}
    print("D", name, D[name]["overall_mix"], "anyGlow", D[name]["reader"]["pairs_any_glow_pct"], "types", D[name]["type_shares_pct"])
report["D_out_of_sample"] = D

# ---------- E. Glow meaning ----------
E = {"glow_results_pct_overall": report["A_reference"]["overall_mix"]["Glow"], "pairs_any_glow_pct": A["reader"]["pairs_any_glow_pct"],
     "glow_count_per_pair_pct": A["reader"]["glow_count_per_pair_pct"]}
# per person: share of partners with any Glow, and with Glow in harmony
pp_any = collections.defaultdict(list); pp_h = collections.defaultdict(list)
for (a, b), r in zip(pairs, res):
    g = any(v2.band_of(r["scores"][k], LINES_44[k]) == "Glow" for k in ORDER); h = v2.band_of(r["scores"]["harmony"], LINES_44["harmony"]) == "Glow"
    for i in (a, b): pp_any[i].append(g); pp_h[i].append(h)
sh = [statistics.mean(v) for v in pp_any.values()]
E["per_person_share_of_partners_with_any_glow"] = {"mean": round(100 * statistics.mean(sh), 1), "p10": round(100 * sorted(sh)[len(sh) // 10], 1), "p90": round(100 * sorted(sh)[9 * len(sh) // 10], 1)}
E["pairs_with_3plus_glow_pct"] = round(sum(v for k, v in A["reader"]["glow_count_per_pair_pct"].items() if k >= 3), 1)
# top-two-band (Warm or Glow) share per pair
report["E_glow_meaning"] = E
print("E", E)

# ---------- F. v1 comparison ----------
v1p = OUT / "v1_perpair.json"
if v1p.exists():
    V1 = json.loads(v1p.read_text()); assert V1["order"] == ORDER
    v1by = {k: [r["scores"][i] for r in V1["results"]] for i, k in enumerate(ORDER)}
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
    F = {"spearman_v1_v2": {k: spearman(v1by[k], by[k]) for k in ORDER},
         "v1_mix": overall_mix([{"scores": {k: r["scores"][i] for i, k in enumerate(ORDER)}} for r in V1["results"]], {k: [24, 49, 74, 100] for k in ORDER}),
         "v1_zero_pct": {k: round(100 * v1by[k].count(0) / len(v1by[k]), 2) for k in ORDER}}
    report["F_v1"] = F; print("F", F)
else:
    print("F: v1_perpair.json not present yet")
(OUT / "review_stats.json").write_text(json.dumps(report, indent=1))
print("written", OUT / "review_stats.json")
```

### 7.4 Decomposition of the per-Type effects

Run from the `v2/` directory after `measure.py`:

```python
import copy, json, collections, statistics, hdmech as m, m10v2 as v2
P = json.load(open("../out/people.json")); masks = [m.mask_of(p["gates"]) for p in P["people"]]; pairs = P["pairs"]
L = json.load(open("../out/v2_measure.json"))["calibration"]["A_30_35_25_10"]["per_category_lines"]
cls = [m.aura_class(m.derive_type(mk)) for mk in masks]
def run(cfg): return [v2.score_pair(masks[a], masks[b], cfg) for a, b in pairs]
def harmony_glow_by_presence(res):
    out = {}
    for c in ("generator", "projector", "manifestor", "reflector"):
        idx = [i for i, (a, b) in enumerate(pairs) if c in (cls[a], cls[b])]
        out[c] = round(100 * sum(v2.band_of(res[i]["scores"]["harmony"], L["harmony"]) == "Glow" for i in idx) / len(idx), 1)
    return out
base = copy.deepcopy(v2.CONFIG); base["bands"] = L
print("base", harmony_glow_by_presence(run(base)))              # generator 9.2, projector 10.3, manifestor 2.7, reflector 14.8
c1 = copy.deepcopy(base); c1["type_a"]["manifestor"]["harmony"] = 0
print("manifestor harmony offset 0", harmony_glow_by_presence(run(c1)))   # manifestor 5.8
c2 = copy.deepcopy(base)
for k in c2["type_a"]: c2["type_a"][k] = {x: 0 for x in v2.ORDER}
c2["type_i"] = []
print("no Type signal", harmony_glow_by_presence(run(c2)))      # 6.8, 7.7, 5.8, 13.9
```

### 7.5 Type derivation on every repository chart with a Type

```python
import json, hdmech as m
cases = {  # path: (type getter, gates getter)
  "fixtures/hdapi/normalized/bodygraph_20250927T012414Z_normalized.json": lambda d: (d["type"], d["mechanics"]["gates"]),
  "fixtures/hdapi/normalized/bodygraph_20250927T015039Z_normalized.json": lambda d: (d["type"], d["mechanics"]["gates"]),
  "fixtures/hdapi/normalized/bodygraph_20250927T015542Z_normalized.json": lambda d: (d["type"], d["mechanics"]["gates"]),
  "fixtures/charts/alice.json": lambda d: (d["bodygraph"]["type"], d["bodygraph"]["gates"]),
  "fixtures/charts/bob.json": lambda d: (d["bodygraph"]["type"], d["bodygraph"]["gates"]),
  "tests/fixtures/bodygraph/source_invariance/vendor_chart_result.v1.json": lambda d: (d["payload"]["type"], d["payload"]["gates"]),
  ".audit_src/artifacts/live_vendor/20250929T022319Z_response.json": lambda d: (d["type"], d["gates"]),
  "audit/qa/hde-epic037/checks/po-007/stdout.json": lambda d: (d["resolved"]["bodygraph"]["type"], d["resolved"]["bodygraph"]["gates"]),
}
for path, g in cases.items():
    vendor, gates = g(json.load(open(f"{m.REPO}/{path}")))
    mk = m.mask_of(int(x) for x in gates)
    print(path.split("/")[-1], vendor, m.derive_type(mk), "direct" if any(c in m.complete_channels(mk) for c in ("12-22", "20-34", "21-45", "35-36")) else "no direct route")
```

Result: seven match, `bob.json` does not (its gate list forms 04-63, 09-52 and 12-22 while the fixture lists only 4-63), and every Manifestor or Manifesting Generator reaches the Throat through a direct channel, so no chart tests the any-route rule.

### 7.6 Channel–center overlap (for R-07)

Run from the `v2/` directory after `measure.py`:

```python
import json, statistics, hdmech as m, m10v2 as v2
P = json.load(open("../out/people.json")); masks = [m.mask_of(p["gates"]) for p in P["people"]]; pairs = P["pairs"]
L = json.load(open("../out/v2_measure.json"))["calibration"]["A_30_35_25_10"]["per_category_lines"]
res = [v2.score_pair(masks[a], masks[b], v2.CONFIG) for a, b in pairs]
def pearson(x, y):
    mx, my = statistics.mean(x), statistics.mean(y)
    return sum((a - mx) * (b - my) for a, b in zip(x, y)) / (sum((a - mx) ** 2 for a in x) * sum((b - my) ** 2 for b in y)) ** 0.5
def var(v): mu = statistics.mean(v); return sum((x - mu) ** 2 for x in v) / len(v)
def cov(x, y): mx, my = statistics.mean(x), statistics.mean(y); return sum((a - mx) * (b - my) for a, b in zip(x, y)) / len(x)
def ranks(v):
    o = sorted(range(len(v)), key=lambda i: v[i]); r = [0.0] * len(v); i = 0
    while i < len(v):
        j = i
        while j + 1 < len(v) and v[o[j + 1]] == v[o[i]]: j += 1
        for k in range(i, j + 1): r[o[k]] = (i + j) / 2 + 1
        i = j + 1
    return r
for k in v2.ORDER:
    C = [r["C"][k] for r in res]; Z = [r["Z"][k] for r in res]; T = [r["T"][k] for r in res]; S = [r["scores"][k] for r in res]
    covshare = 2 * cov([0.06 * c for c in C], [0.025 * z for z in Z]) / var(S) * 100
    noZ = [v2.rhu(60 * c + 15 * t, 750) for c, t in zip(C, T)]                      # score without Z, renormalised
    zbar = round(statistics.mean(Z)); S2 = [min(100, max(0, v2.rhu(60 * c + 25 * zbar + 15 * t, 1000))) for c, t in zip(C, T)]
    bands_changed = sum(v2.band_of(a, L[k]) != v2.band_of(b, L[k]) for a, b in zip(S, S2)) / len(S) * 100
    print(k, round(pearson(C, Z), 2), round(covshare, 1), round(pearson(ranks(S), ranks(noZ)), 3), round(bands_changed, 1))
eq = [r["signals"]["equilibrium_score"] for r in res]; cw = [r["signals"]["counterweight_ratio"] for r in res]
print("r(equilibrium_score, counterweight_ratio)", round(pearson(eq, cw), 3))
```

Result (category, `r(C, Z)`, covariance share of score variance in %, Spearman of the score against the score without `Z`, bands changed by `Z` in %): harmony 0.02 / 1.3 / 0.874 / 35.5; heat 0.01 / 0.7 / 0.934 / 26.2; communication 0.26 / 17.2 / 0.905 / 32.1; alignment 0.11 / 8.1 / 0.923 / 27.9; comfort 0.04 / 2.9 / 0.888 / 35.8; consistency 0.33 / 14.9 / 0.967 / 19.8; expansion −0.07 / −6.4 / 0.879 / 36.9; creativity −0.07 / −6.2 / 0.865 / 36.3; drive 0.18 / 10.9 / 0.923 / 27.5; balance 0.44 / 30.6 / 0.855 / 38.9. The two Balance signals correlate at −0.197. An independent checker obtained the same values.

### 7.7 Output digests from this rerun

| File | SHA-256 | Against Appendix D |
| :- | :- | :- |
| `people.json` | `bb7e336d2a3efe9b596f98d9df8467b97a0ef79b75c970842c72445fd24d4b19` | identical |
| `v1_perpair.json` | `eba6413e74a58eff120a14ea9df6ce3feffba879a3cddb5fb85799bcb9e67b32` | identical |
| `v1_distribution.json` | `e6b64820b8a647671e353499838def6e3dcc6d61bc1d4830b21e7576359280b7` | differs only in `chart_seconds`/`pair_seconds` |
| `v2_measure.json` | `c63dd9b922c9222fe94926481b4f0604a89ab8e6e49fe693b3c614a3602688ac` | differs only in `seconds` |
| `v2_goldens.json` | `45ab9e98465b63f2fea0070dbb3849808c146f265cb613eebd95b21acf5ca08a` (seed 0); `07f6c437…` (seeds 1, 2) | same content; bytes depend on `PYTHONHASHSEED` through `set` iteration in `hdmech.definition_components` |
| `v2_sensitivity.json` | `ce648a855d8a6e71995760f746df2548e2eff82b498c182f7d9c6b4fda1f73cb` | identical |

## 8. Effect on each Product Owner decision (proposal §9)

| Q | Proposal's recommendation | Review | Effect |
| :- | :- | :- | :- |
| Q-1 Meaning of "relevant placement" | (a) quality over coverage and (b) center relevance together; defer (c) planetary | Sound. Saturating accumulation removes the dilution the brief described; the center component carries "where you connect" from PF08 doctrine; planetary placement is correctly costed as a data change | **Adopt as recommended** |
| Q-2 Planetary activations as input | not in v2.0 | Sound and complete (vendor adapter, stored schema, re-acquisition of every stored person). The raw vendor fixtures confirm that `activations` exist in the vendor payload and are dropped by the adapter | **Adopt as recommended** |
| Q-3a Do admitted references support a Type pairing model and the composite rules? | composite rules yes; Type derivation and each Type's aura yes; a Type pairing rule no | Confirmed in the strict sense by my own search (§3.5): no admitted source states a rule, matrix, valence or score. But the collection is not silent: the A4 Rave Psychologist booklet carries pairwise aura statements and the A3 Rave Cosmology course speaks of the Projector–Generator connection, and the proposal records neither (R-18) | **Confirmed as "no rule"; the answer should add what the collection does say** |
| Q-3b Which route, adopt the rules, acquire a source? | route 2 inference; adopt Tables 7a and 7b bounded to 15 points; acquire *Type Sexual Signatures* | The route is permitted only once the admitted collection is exhausted, and it was not (R-18). Two of six pair rules cite passages that do not support them and no alternative is recorded (R-05); the Reflector branch's record is mis-sourced, with the primary-source gap unrecorded (R-24); Table 7a is a per-person level, not pair compatibility, and produces the undisclosed effects in §4.10 (R-01). Acquisition is the right call, with the Index §10 intake fields filled | **Do not adopt Tables 7a and 7b as they stand.** Decide among: (a) adopt after the register is completed from the admitted material and the two misapplied rows are re-grounded, with §4.10 disclosed; (b) Table 7b only, re-grounded, or Table 7a constrained to zero-sum rows; (c) no Type component until a primary source is admitted. I recommend (b). Acquire the source either way |
| Q-3c Is Manifesting Generator its own Type? | derive and report it; pair it as a Generator | A sound inference from doctrine (Generators' Course seg. 15; Complete Guide p. 230), not a stated doctrine: no admitted work names the Manifesting Generator aura. Label it so, drop "with one aura" and record the rejected alternative and Winn's counter-indication (R-25) | **Adopt as recommended**, with the label corrected |
| Q-4 How much may Type move a score? | 15 points at most; 0.4%–7.6% of variance; keep 60/25/15 | The bound and the variance figures are confirmed. The bound does not prevent systematic per-Type effects on the public band (Manifestor `harmony` Glow 2.7% against 9.1%), because a small constant shift applied to every pair a person is in moves that person's band shares materially | **Adopt the bound; decide the per-Type question explicitly** (see Q-3b). If Table 7a stays, the adoption record should state the measured per-Type band effects |
| Q-5 Bands | relative, per-category, target 30/35/25/10 (A); D if Glow should be rarer; reference population as §4.2; recalibration only by release | Relative and per-category are well argued and the global alternative is shown to fail (§4.3 reproduced). The lines hold on seven further synthetic populations (§3.7). Two things to add: the Fermentation hook (what real-user observation triggers recalibration) and a statement of what Glow means at the pair level (55.9% of pairs show at least one) | **Adopt relative and per-category.** Choose A or D knowing that under A a Glow somewhere is the majority outcome and under D one pair in three. Add the recalibration observation and tolerance and bind them to the score-distribution utility (item 13) |
| Q-6 Cutover | v2 replaces v1; one active configuration; rollback is the prior release | Matches HDE Math Spec §5.4.1 and PF12 §2.9 rollback coupling | **Confirm** |
| Q-7 (new) Motor→Throat route | any connected definition; keep the §5.4.2.1 direct set as a governed subset | Any-route is the doctrine (Complete Guide p. 232, three-channel bridge; Generators' Course "other variations"; Winn seg. 51). Keeping two definitions of the phrase is a single-home problem | **Adopt any-route.** Decide the direct set's future in the same adoption record: reduce it to evidence or retire it |
| Q-8 (new) `balance` redefinition | both Balance signals over all 36 channels; bilateral completion as center component; name and position stay | The redefinition is what rescues `balance` (v1 zero 41.8% → 0%, Spearman with v1 0.10). It also breaks three stated v1 invariants (no channel in both signals of one category; one through six channels per Balance signal; the Balance maps as named) that §7 does not list, and it makes `balance` and `consistency` Glow unreachable for pairs containing a Reflector | **Adopt the redefinition** with the invariant changes named in the Doc Delta (R-03) and the Reflector effect disclosed (R-02) |

**Decisions the proposal does not list and the Product Owner should take:**

| New | Decision | Why |
| :- | :- | :- |
| Q-9 | Whether Type may enter as a per-person level (Table 7a) at all, or only as pair interaction (Table 7b) | the Product Owner asked for compatibility between aura types, which is pairwise; Table 7a produces the systematic per-Type effects in §4.10 |
| Q-10 | Whether a pair with no connecting channel may score above 0 from Type alone (the G001 floor, up to 11 points) | v1 scored such a pair 0; PF08 locates the relationship in the connection |
| Q-11 | Whether the score-distribution command-line utility (Candidate CRD item 13) is a dependency of the v2 change, sequenced before the v2 release cut as its own CRD or as the first work unit of the v2 Epic, and built on `evaluate_pair` so it creates no second scoring surface | it is the only instrument that measures the outcome v2 exists to produce; the §4.4 lines should be cut by it rather than by an ephemeral script, and the recalibration rule in §4.2 has nothing to run without it |
| Q-12 | Which PF09 rows the adoption re-targets (HDE-DIST008, HDE-CONJ010; a new Separation task in the shape of HDE-SEPA005) | adopting v2 changes the target of a Partial Distillation task written around v1 |

## 9. Points raised before this review

The review prompt §8 records eight points the brief's author raised after reading the proposal. I formed the findings above first, then tested each point.

| # | Point | Result | Evidence |
| :- | :- | :- | :- |
| 1 | `hdmech.py` hard-codes `REPO` to the author's scratch path, so the scripts do not run elsewhere as published | **Confirmed, and understated.** Besides `REPO` (line 9, `/tmp/claude-0/-home-user/5d854c62-…/scratchpad/hde/repo`), the scripts assume an undocumented directory layout, the engine runs need the clone root as working directory (the narrative-pack loader resolves `catalog/narratives` relative to the CWD and raises `no narrative pack files found` otherwise), `measure.py` cannot produce the §4.4 rows D and E, and the §3.7/§5.5 variance shares and inter-category correlation come from unpublished code. The hash-verified `hdmech.py` cannot run unedited; after the one-line edit it hashes to `ac5998bb…`. Every number nevertheless reproduced (§3.1) | §3.1, §4.5, §7 |
| 2 | The 30/35/25/10 mix holds by construction; only per-pair, out-of-sample and live results are informative | **Confirmed**, with one refinement: the Reader v2 distinct-band distribution and the per-Type effects depend on the joint distribution across categories, which per-category marginal calibration does not fix, so they are informative too | §3.7 |
| 3 | The Type component's 500 baseline at 15% weight adds about 7.5 points to every score; some of "no zero scores" may be constant rather than relational | **Partly confirmed.** The Type component adds 6.5 to 10.7 points per category on average (more than 7.5, because the population is Generator-heavy). But removing it leaves zero scores at only 0.01% to 0.59% of pairs; the center component, not the Type constant, removes v1's zeros. The constant is absorbed by relative lines; its differential part is the issue in §4.10 | §3.7 |
| 4 | Pairs containing a Manifestor reach Glow on `harmony` 2.6% of the time against 9.3% (Generators) and 10.5% (Projectors); Reflector person-pairs average 402 against 446; `harmony` is the band Reader v1 shows | **Confirmed** (2.7% / 9.2% / 10.3%; 402.0 against 446.3) and extended: the Manifestor effect comes from Table 7a's `harmony` −200 (5.8% without it); the Reflector effect comes from the center mechanics and extends to 0% Glow in `balance` and `consistency`; Generators are favoured in total by Table 7a's row sum | §4.10 |
| 5 | The frozen lines held on younger populations: 1985–2005 gave 30.3 / 34.6 / 25.2 / 9.9 and 1995–2004 gave 30.6 / 34.5 / 25.2 / 9.7 | **Confirmed** on my own generations (30.7 / 34.7 / 24.9 / 9.7 and 30.5 / 34.8 / 25.3 / 9.4; the small differences are different pair draws) and on five further seeds and eras, the widest deviation being Cool 32.3% for births 1950–1970 | §3.7 |
| 6 | The rerun reproduced the reference mix (29.8 / 34.9 / 25.4 / 10.0; the proposal states Warm 25.3) and the distinct-band distribution (0.1 / 7.4 / 48.2 / 44.3) | **Confirmed.** Warm is 25.35% exactly; 25.3 and 25.4 are the two roundings of the same number | §3.1 |
| 7 | HDE-DIST008 (Partial) is a v1-specific verification task whose target v2 changes; the proposal's §7 and §8 do not mention it | **Confirmed.** `HDE-DIST008` and its subtasks name `magic10_result.v1`, `tests/fixtures/magic10/v1/goldens.json`, "Both Balance operations", "All twenty signals at … half-up boundaries", "every band edge" and a manifest cut at `--version 1.1.0`; none of §7, §8 or §10.3 names PF09.3, PF09.4 or PF09.6. `HDE-CONJ010` (Partial; subtasks .1, .2, .5 Not done) and `HDE-SEPA005` (Done) are likewise unmentioned | §4.3 |
| 8 | HDE Math Spec §5.2.7 and HDE Governance §4.1.5, both cited by the proposal, exist | **Confirmed.** `PF01-Canon-HDE-Math-Spec-v1.3.8.md` line 786 (`### **5.2.7 Validation and failure behavior**`, an indented heading) and line 599 (`5.2.2`); `PF04-Canon-HDE-Governance-v2.8.8.md` line 1346 (`### **4.1.5 Bands — inclusive-high thresholds (by preset)**`) | §4.8 |

## 10. Limits, nonclaims, canon relied on

### 10.1 Limits

* **Independence.** I did not contact the proposal's author or the brief's author and read no transcript of either session. Both repositories were read on `main`; the review prompt (`#825`) and the proposal (`#824`) were the only session-specific inputs.
* **Reproduction scope.** Every published number was reproduced from the hash-verified scripts in a scratch clone of `main` at `0bf99656` (catalogs, math and engine identical to `e2b7427f`, the head the proposal read). My own measurements use the proposal's chart generator, so they share its validation basis (60 of 60 against four live people, mean node) and its limits; they are synthetic populations, not users.
* **Doctrine.** Every citation was verified in the admitted collection: the Complete Guide through a `pdftotext -layout` text layer with printed page numbers read from the footers, which is a faithful text source but not the illustrated page; no quotation checked depends on a diagram. I consulted no outside source and fetched no URL; the three outside pages in Appendix B were assessed as a record, not re-fetched.
* **Code.** I read the engine modules, loader, schemas and tests the proposal names and the ones its changes touch. On the scratch clone I ran only the five HDE Build Notes 2.16 owner tests and `tests/m10` (184 passed, 3 skipped) to fix the v1 baseline; I did not run the full suite, implement any part of v2 or build anything. Feasibility judgments are from reading, not from an implementation attempt.
* **Agents.** Eight independent read-only checkers re-verified citations, the doctrine gap, feasibility, canon deltas, brief compliance and alchemical fidelity. Their 48 merged points were ranked by severity; the twelve highest were each re-verified adversarially by a further checker against the primary sources and a critic read the whole set; the remaining 36, Minor or Observation in the checkers' own rating, had no second checker beyond my own check. The first attempt at the merge, verification and critique stages failed on the account's usage limit and was resumed about two hours later; the eight sweep results were reused unchanged. Every finding in §6 is one I confirmed myself against the primary source; the checkers' role was to find what I had missed, not to decide.
* **No live or vendor data.** The vendor Types of P1, P2, SYN-A and SYN-B are not in the repository, so the Type derivation is validated on eight repository charts only, none with an indirect motor→Throat route.

### 10.2 Nonclaims

This review:

* approves nothing; it gives verdicts and recommendations, and the Product Owner decides;
* changes no canon, code, catalog, test, schema, data or Notion page; it is one file under `docs/ephemeral/`, through one pull request;
* creates no change, CRD candidate, release, `config_id` or PF09 movement;
* makes no QA verdict, acceptance, Ops result or closure claim;
* makes no claim about relationship quality or outcomes and no medical, psychological, sexual, safety or destiny claim; where it reports per-Type effects it describes what the formula does to scores, not what Types are.

### 10.3 Canon relied on

Read on `main` at `84d6d1c` (`amthorn78/glow-hdengine-v2`; `docs/pfcanon/` unchanged since `0bf99656`) and `edaa34c` (`amthorn78/glow-docs`).

* **HDE Math Spec v1.3.8 (PF01):** §2.5; §4.1; §5.2 in full, including the indented §5.2.2 and §5.2.7; §5.3 in full; §5.4.1 to §5.4.4 and §5.4.2.1; §6.1; §6.3; §6.4; §6.7; §7.1 to §7.5; §8.1 to §8.4; §9.1, §9.2, §9.5, §9.6.
* **HDE Governance v2.8.8 (PF04):** §4.1.5, §4.1.6; §12.1 (`GATE:CORE-MATCH`, `GATE:CORE-DET`); §12.2 band entry.
* **HDE Schemas & Artifacts v2.9.7 (PF12):** §2.1, §2.6, §2.9 in full, §2.10 heading.
* **HDE Architecture v2.4.7 (PF02):** §2.1 components and the Engine Core four-argument boundary.
* **HDE Narratives Guide v1.5.4 (PF17):** §2.3 candidate registry.
* **HDE Users Guide v1.0.3 (PF29):** §5.1 (sampler example), §6.4, §7 headings.
* **HDE Build Notes v14.0.5 (PF10):** current-version rule; addenda 2.15 (R-1 to R-4) and 2.16 (R-1 to R-3).
* **HDE Build Checklists:** PF09.3 Task HDE-SEPA005 (Done) and its subtasks by heading; PF09.4 Task HDE-CONJ010 (Partial) and subtasks .1 to .6 by status; PF09.6 Task HDE-DIST008 (Partial) and subtasks .1 to .3.
* **7 Phases of Alchemical Engineering (PF21):** in full.
* **Glow Development Philosophy (PF13):** §B, §C, §D, §I.
* **Glow Story:** in full.
* **PF08 Human Design System:** "The Centers"; "Channels"; "The Rave Charts" (Composite Rave passage; Johannes analysis; "RAVE — Channel and Definition Analysis Graph"; "Composite with Renate", "Emotional Channels Opened"); whole-text search for Type words.
* **Records:** `docs/ephemeral/HDE-M10V2-mechanics-proposal-v1.0.md` (under review); `docs/ephemeral/HDE-M10V2-hd-math-specialist-design-brief-v1.0.md`; `docs/ephemeral/HDE-M10V2-mechanics-proposal-review-prompt-v1.0.md`; `docs/ephemeral/HDE-EPIC041-POSTCLOSE-compat-score-range-v1.0.md`; `docs/ephemeral/HDE-EPIC041-POSTCLOSE-OPS01-ops-execution-result-v1.0.md` and `audit/ops/hde-epic041/postclose-ops01/` (38 files, searched for `type`); the Notion page "Candidate CRD Items List" (item 13), read only.
* **Code and catalogs (read only):** `engine/core/core.py`; `engine/magic10/composite.py`, `signals.py`, `calculators.py`, `thresholds.py`; `engine/compat/compute.py`; `engine/config/registry_loader.py`; `engine/narratives/loader.py`; `catalog/magic10_mechanics_v1.json`, `magic10_caps.json`, `magic10.json`, `channels_v1.json`; `math/thresholds.json`; `fixtures/hdapi/`, `fixtures/charts/`, `tests/fixtures/bodygraph/source_invariance/`; `.audit_src/artifacts/live_vendor/20250929T022319Z_response.json`; `audit/qa/hde-epic037/checks/po-007/stdout.json`.
* **Human Design references (`glow-docs/docs/hd_refs/`):** Human Design Reference Index v1.2.0 (§1, §3, §4, §5 entries HD-FND-01, HD-TYPE-01, HD-SYN-01, HD-SYN-02, HD-RP-05, HD-COS-01, HD-SECONDARY-01, HD-SECONDARY-02; §9; §10); *The Complete Guide to the Human Design System* (PDF text layer, printed pp. 100–114, 122, 229–235 read in full; whole text searched); Generators' Course segments 1, 7, 15, 16, 38, 76, 77 (segment 51 of Winn and segments 77–78 of the course via a checker); Holistic Analysis Fundamentals segments 28, 117, 199; Rave Psychologist Reference Guide for Practitioners lines 428–690 (the Type and aura keynote pages); Rave Cosmology VIII lines 6744–6748, 7879–7883, 7964–7976, 8505–8511; Winn, *Understanding Your Clients* segments 48, 55, 56, 58, 59, 94, 104; Winn, *Understanding the Centers* segment 64; every Markdown work searched for Type-pair statements.
* **Mathematics:** none beyond the proposal's own; the hyperbolic saturation and quantile-calibration references in Appendix B (M-01, M-02) are standard and were not re-fetched.
