---
artifact_type: DECISION_SUPPORT_RECORD
artifact_id: HDE-M10V2-OPEN-QUESTIONS-RESOLUTION
artifact_version: "1.0"
subject: Engineering resolution of every open question on the Magic10 v2 mechanics proposal (Q-1 to Q-12 and the review's open dispositions), and the drain target summary for the adopted change
requested_by: Nathan / Product Owner, 2026-11-02 ("I would like you to resolve any open questions based on engineering fidelity, and then I want a drain target summary so I know which PF documents need to be drained to")
author: Isis, Lead Developer (https://claude.ai/code/session_01Q789tyhUaytmY7x273kwes)
decision_owner: Product Owner
inputs:
  proposal: docs/ephemeral/HDE-M10V2-mechanics-proposal-v1.0.md (main, SHA-256 dc064a2780042a98ebefa2b3dc3f326a8674c4185ac950881b5845503a3f3c2a)
  review: docs/ephemeral/HDE-M10V2-mechanics-proposal-review-v1.0.md (amthorn78/glow-hdengine-v2#831, branch claude/peaceful-dijkstra-jo6r3z, commit d69a977c, SHA-256 579c52b39cba6d95de2764cf3b96b89fdb24e1cdf1b7e794a0e14fb17b0fc425)
  brief: docs/ephemeral/HDE-M10V2-hd-math-specialist-design-brief-v1.0.md
  candidate_item: Candidate CRD Items List (Notion), item 13
repository_head_read: origin/main 99f00c5c (after #829 published the GTWPE v14.0.5 canon set)
created_at: 2026-11-02T12:32:00Z
---

# Magic10 v2: open questions resolved, and drain targets

## 1. Result

All twelve open questions are resolved below, along with the four review dispositions that are not numbered questions (§3). Two resolutions change the formula:

- **Q-9:** Type enters only pairwise.
- **Q-10:** Type alone never produces a score.

So the proposal needs a v1.1 from the HD Math Specialist, re-measured, before adoption (§4). Two items stay with the Product Owner under canon: the classification in Q-11, and acquiring the Q-3b source.

The adopted change drains into **nine permanent canon documents** and **five PF09 build checklists**, and its source is one HDE Build Notes adoption addendum (§5).

**Resolution rule.** I resolved each question on engineering fidelity. Concretely, the formula must meet four tests:

- it measures the pair and nothing else;
- every rule has one governed home;
- every number is reproducible by a governed tool;
- canon stays internally consistent.

Where a question is about Human Design doctrine rather than engineering, I set the engineering rule and leave the doctrinal content to the Specialist.

| Q | Question | Resolution | Engineering basis |
| :- | :- | :- | :- |
| Q-9 | May Type enter as a per-person level (Table 7a)? | **No.** Drop Table 7a: every per-class offset is 0. Type enters only through pair rules (Table 7b) | A pair score must not contain a term that applies to every pair a person is in. Table 7a is that term, and it produces the review's per-Type effects (R-01). Zero-sum rows would not fix this; see §2 |
| Q-10 | May a pair with no connection score above 0 from Type alone? | **No.** If `C_k = 0` and `Z_k = 0`, then `score_k = 0` | Open canon forbids Type-only scoring (HDE Build Checklist Conjunction, HDE-CONJ010.5; Distillation, HDE-DIST008.1). v1 scores such a pair 0, as M10-G001 records |
| Q-3b | Which route, and adopt Tables 7a and 7b? | **The review's option (b).** Keep Table 7b's structure. The Specialist re-grounds its rows from the admitted collection. Acquire *Type Sexual Signatures* | No unsupported constant may enter the formula: a cell with no cited admitted passage is 0. The admitted collection was not exhausted (R-18) |
| Q-3a | Does the admitted collection support a pairing model? | **"No rule, matrix, valence or score"**, plus a record of what the collection does say | The review confirmed this (R-18) |
| Q-3c | Is Manifesting Generator its own Type? | **Derive it; pair it as a Generator.** Label this an inference | R-25 |
| Q-1 | Meaning of "relevant placement" | **Adopt** (a) quality over coverage and (b) center relevance. Add the double-counting statement (R-07) | The review measured that the channel and center components carry separate information |
| Q-2 | Planetary activations as input | **Not in v2.0** | It is a data change: the adapter, the stored schema, and re-acquiring every stored person |
| Q-4 | How much may Type move a score? | **15 points at most**, a hard ceiling. Report the realized per-Type band effects after the v1.1 re-measure | Q-9 removes the systematic part. With Table 7a gone, the realized swing is smaller than the ceiling |
| Q-5 | Bands | **Relative and per-category, target mix A (30/35/25/10)**, recut after v1.1. Add the recalibration observation of §2 | A carries more information per result than D (1.883 against 1.766 bits) and shows all four bands to more pairs (44.3% against 27.3%). Moving to D later changes only the thresholds bytes |
| Q-6 | Cutover | **Confirm.** v2 replaces v1 in one release; there is one active configuration; rollback is the whole prior release. Add the schema, fixed-field and evidence conditions of §3 | HDE Math Spec §5.4.1; HDE Schemas & Artifacts §2.9 |
| Q-7 | Motor→Throat route | **Any connected route.** Retire the direct four-channel set as a governed input | The set has no scoring consumer today (verified, §2). Keeping it would give one phrase two definitions |
| Q-8 | `balance` redefinition | **Adopt.** Name the v1 invariants it breaks in the Doc Delta. Disclose the Reflector effect in all three categories. Add no Type-specific branch | A Reflector branch would bring back the per-person term that Q-9 removes |
| Q-11 | Is the score-distribution utility a dependency? | **Yes.** No v2 band line ships unless the governed utility cuts it. I recommend its own CRD, landed before the v2 release cut | The lines and the recalibration rule need a governed, repeatable instrument. The proposal's scripts do not run as published (R-10) |
| Q-12 | Which PF09 rows change? | **Five rows**, listed in §5.2 | PF09 rows are verified in the current checklists |

## 2. Resolutions in detail

### Q-9: Type enters only pairwise

**Why Table 7a fails.** The Type component is `T_k = 500 + A_k[class_lo] + A_k[class_hi] + Σ I_k`. The `A` terms are separable: each depends on one person only. So a Manifestor's `harmony −200` applies to every pair that Manifestor is in, whoever the partner is. That is a level for the person, not compatibility between two auras. The review measured the result: pairs containing a Manifestor reach Glow in `harmony` 2.7% of the time, against 9.1% overall (R-01).

**Why zero-sum rows would not fix it.** Zero-sum rows remove the total effect but keep each category's per-person effect. Only `A ≡ 0` removes the separable term.

**What Table 7b-only still does.** Table 7b rules depend on both classes, so they are pair interactions. A class's average effect then depends on who its partners are. That is a legitimate consequence of pairing, and the v1.1 re-measure reports it.

### Q-10: Type never scores alone

The step-8 score rule becomes:

```text
score_k = 0                                                   if C_k = 0 and Z_k = 0
score_k = min(100, max(0, rhu(60·C_k + 25·Z_k + 15·T_k, 1000)))  otherwise
```

- **Effect on M10-G001** (two Reflectors, no channel): every category scores 0, as in v1.
- **Determinism, AB↔BA symmetry and monotonicity** are unaffected.
- **The 7.5-point baseline** the 500 midpoint gives every connected pair is absorbed by relative lines.

### Q-3b: the engineering rule for Table 7b

The Specialist's v1.1 redoes Table 7b under three rules:

1. **Every non-zero cell cites an admitted passage at its tier.** This includes the A4 Rave Psychologist pairwise statements the review found (R-18), and the corrected readings of Complete Guide p. 235 and Generators' Course seg. 15 (R-05).
2. **A rule with no admitted support is 0**, not "inference without doctrine".
3. **The rejected alternatives are recorded.** These are pairwise-only, no Type component, and Manifesting Generator as a fifth class.

When *Type Sexual Signatures* is admitted, the rows are re-derived in a later release. Acquiring it is the Product Owner's action.

### Q-5: target A and the recalibration observation

**Why A.** Each category result carries up to 2 bits. Mix A carries 1.883 bits, D carries 1.766, and A shows all four bands to 44.3% of pairs against 27.3%. Reader v2 exists to differentiate (D-5), so A serves it better. The lines are governed bytes, so moving to D later is a thresholds-only release with no code change.

**Default recalibration observation.** The Specification may tighten these values; these are the engineering defaults.

| Element | Default |
| :- | :- |
| Measure | Realized band mix per category, and distinct bands per pair |
| Instrument | The score-distribution utility (Q-11), over the stored real population, reporting aggregates only |
| Minimum population | 400 stored real people before an observation counts. At 400, the 95% sampling margin on any band share is at most ±4.9 points |
| Tolerance | A band share in any category more than 5 points from the target (30/35/25/10) is a recalibration case |
| Response | A Product Owner decision taken as a release (HDE Math Spec §5.3.5), never a runtime adjustment |
| Home | A deferred HDE Build Checklist Fermentation row (§5.2) |

**Label.** The v2.0 lines are labelled "calibrated on the synthetic reference population".

### Q-7: the direct motor→Throat set has no consumer

Verified on `main` `99f00c5c`:

- `DIRECT_MOTOR_THROAT` in `engine/constants.py` is read only by `tests/mech/test_constants.py`.
- The `direct_mt` flags on four channel rows in `engine/config/registry_loader.py` are read by no code.

Retiring the set means:

- **Canon:** HDE Math Spec §5.4.2.1 and the §6.4 direct-MT flag are retired, and the freeze-pack entry in §5.4.1 is removed at the v2 cut.
- **Code:** removing the constant and the flags is dead-code cleanup inside the Change.

### Q-8: the Reflector effect is disclosed, not special-cased

**The effect.** Pairs containing a Reflector cannot reach Glow in `balance` or `consistency`, and almost never in `alignment` (R-02). These constructs are defined over definition: `foundation` scores shared definition, and `bilateral_completion` scores mutual giving. A Reflector has no definition, so the result follows from the definition of the constructs.

**Why no special case.** Special-casing Reflectors would add a Type-conditioned branch to center mechanics, the per-person term Q-9 removes.

**Disclosure.** The adoption addendum and HDE Math Spec §5.2 state the effect in all three categories. The review measured the population at 1.2%.

### Q-11: the utility comes first

**The dependency.** The governed utility cuts the v2 lines and guards them afterwards. The proposal's ephemeral scripts do not.

**Why its own CRD.** It runs on every math or configuration change, including v1 today. Its acceptance should not depend on v2's.

**Classification.** Whether it is a CRD or the first work unit of the v2 change is the Product Owner's call (Change Process Guide). Item 13's routing decision says the same.

**Engineering resolutions of item 13's five drafting decisions:**

| # | Decision | Resolution | Reason |
| :- | :- | :- | :- |
| 1 | Form | A standalone tool under `tools/`, not an `hdctl` subcommand | No HDE CLI/API/Vendor Ref change; never a public surface |
| 2 | Chart source | A frozen, vendor-validated synthetic chart corpus committed as a fixture | CI needs no ephemeris; results cannot drift with an ephemeris library version |
| 3 | Math Spec trigger | The classifier selects it for configuration and code paths. The Specification and QA stages of every Math Spec change attach its report | CI exempts `docs/pfcanon/` from its lanes |
| 4 | Gate or report | **Gate on the reference corpus:** the realized per-category mix must equal the frozen expected values exactly. **Report on real populations,** against the §2 Q-5 tolerance | The corpus result is deterministic, so any unintended distribution change fails loudly |
| 5 | Population | The corpus and its seed are a governed input with a pinned hash | Required for decision 4 |

**Additional requirement.** The utility needs a second mode that reads stored real people through the governed database path and emits aggregates only. The Q-5 observation needs it.

**Built on the real path.** It scores through `evaluate_pair` with the admitted bundle (`bundle_provider`), so it creates no second scoring surface.

### Q-12: see §5.2

## 3. Review dispositions that are not numbered questions

| Item | Resolution | Basis |
| :- | :- | :- |
| R-09: three homes for Type | **The derived Type is the only scoring home.** The stored vendor `type` is non-scoring vendor metadata. Engine Core never reads it, so a divergence has no runtime effect. Implementation QA compares derived and vendor Type on every vendor-backed chart: SYN-A, SYN-B, stored production rows, and the two audit charts. Any mismatch is a QA FAIL to investigate before acceptance | `engine/compat/ts_v0.py` is outside the scoring path. Only `scripts/hdctl.clean.py`, `scripts/hdctl.backup.py`, `tests/cli/test_showcompat_sources.py` and `tools/evidence/generate_hde_epic037_v2_to_compat.py` import it (verified). Its removal stays HDE-CONJ010.5 |
| R-09: §6.3 center tagging | **Retire** it in favour of the four-outcome center contract. The owner of a `one_sided` outcome carries its actor indication | The four outcomes are a different concept. Of the two options, only "retire" fits (R-13) |
| R-19 / Q-6: fixed fields and versions | `signal_scale` 2 → 10, since signals become per-mille `0..1000`. `response_scale` stays 10000. `rounding.signal` becomes ROUND_HALF_UP to integer per-mille. A new `rounding.component` uses the same rule for `C` and `Z`. `rounding.category` stays `round_half_up_once`. `math/thresholds.json` stays at its path with `"version": "2"` and a per-category object, plus a new schema. The result and compat-result schemas become v2, widening `q` to `0..1000`. The compat-result change is an internal API contract change for `hdctl showcompat` stdout and `POST /api/compat/v1`. The rounding token names are proposals for the Doc Delta | v1 values verified in `catalog/magic10_mechanics_v1.json`. Both v1 result schemas pin `q` maximum 200 (verified). Keeping the path avoids a dead roster member; rollback restores the prior bytes with the prior release |
| R-04 / R-19: import-time and loader literals | The Change's implementation plan enumerates every literal. At minimum: `engine/magic10/thresholds.py` reads `edges` at import, and `engine/config/registry_loader.py` line 1204 requires `edges == [24, 49, 74, 100]` (both verified) | Each fails closed on a per-category thresholds file |
| R-21: map keys and enums | The center-map key set is a closed enum: the nine center IDs plus `motor_throat`, the one permitted non-center key. Aura classes and pair-rule predicate names are closed enums in the Type-pairing catalog schema, and the loader rejects unknown names. Each category's lines are four ascending values ending in 100 | Without this, the proposal's own loader rule rejects its `heat` and `drive` rows |
| R-20: evidence at the cut | **Regenerated:** the release-sanity stage 04 determinism outputs, the band-edge artifacts and the goldens. They are current evidence, and the stage 04 outputs are GATE:CORE-DET closed-rails evidence under the decided HDE Build Notes addendum 2.1. **Frozen:** historical captures, which are not regenerated merely because the release changes (HDE Governance §4.1.6) | The two lists go in the Change's Specification |
| R-22: viewer preferences | Viewer preferences, presets and caller weights stay as sampler and ranker inputs. They never enter `C`, `Z`, `T`, scores or bands | HDE Math Spec §7.2 item 6 |

The review's other Minor findings and Observations are corrections for v1.1 and need no decision: R-03, R-06, R-10, R-11, R-13 to R-17, R-23, R-24 and R-25.

## 4. Order of work

1. **Proposal v1.1 (HD Math Specialist).** Inputs are this record and review #831. It covers:
   - dropping Table 7a and adding the Q-10 rule;
   - re-grounding Table 7b under the §2 rule;
   - re-measuring per-Type effects;
   - recutting lines at target A and regenerating the goldens;
   - per-weight sensitivity (R-23);
   - the double-counting statement (R-07);
   - portable scripts (R-10);
   - the review's corrections.
2. **Score-distribution utility (item 13)**, as classified under Q-11, landed before the v2 release cut.
3. **Adoption.** The Product Owner's decision, recorded as an HDE Build Notes addendum. It takes the next number in the PF10 base version current at that time. Its "Required canon drainage" names §5 below.
4. **The v2 change** (Epic or CRD, as classified). Its Specification carries the Doc Delta, and its PF09 maintenance carries §5.2.

## 5. Drain target summary

Section numbers are in the canon published on `main` at `99f00c5c`. Each row was found by searching that document for the v1 identities v2 changes, such as `magic10_result.v1`, `24/49/74`, `0..200` and `signal_scale`.

### 5.1 Permanent canon (Doc Delta of the v2 change)

| Document | Sections | What drains |
| :- | :- | :- |
| **HDE Math Spec** (owner of the formula) | §0.2; §1; §2.5; §3.1; §4.1; §5.2.1 to §5.2.9; a new §5.2.x; §5.3 to §5.3.6; §5.4.1 to §5.4.4 and §5.4.2.1; §6.3; §6.4; §7.2, §7.3, §8.2, §8.4; §9.1; §9.5 | See the breakdown below this table |
| **HDE Schemas & Artifacts** | §0.4; §0.5 (MAGIC10-HOME); §2.1; §2.6; §2.9; §5.1; §5.3; §6.2.1; §8.6.3.3; §8.6.3.9; §8.14.1; §8.14.2; §8.15 | See the breakdown below this table |
| **HDE Governance** | §2.0.7; §2.0.11; §2.0.15; §4.1.5; §4.1.10; §5.1; §9.2; §12.1; §12.2; Appendix B.6; Appendix D.10 | See the breakdown below this table |
| **HDE Mechanics Guide** | §0.3; §3.7.3; §6.7; §7.2; §7.3; §9.2; §37.10 | v2 result identities; the per-category band-edges artifact; the `THRESHOLDS_V1` derivation becomes per-category; the Engine Core module and test list; inclusive-high band edges per category. §9.2 names `ts_v0`, and gains the rule that the derived Type is the only scoring home (§3) |
| **HDE CLI/API/Vendor Ref** | §4.1.3; §4.1.6; §5.1.1; §5.1.7; §5.5 | `magic10_compat_result.v2` and `q` in `0..1000` on `hdctl showcompat` stdout and `POST /api/compat/v1`, an internal API contract change; the new `config_id`; the 45-member roster statement in §5.1.7 |
| **HDE Architecture** | §2.2; §3.1 | The flow line gains centers and derived Type, and states that the stored `type` is not consumed; the compat threshold shim becomes per-category |
| **Glow Infrastructure** | §8.2.1 | The required canonical target `catalog/magic10_mechanics_v1.json` becomes the v2 configuration path |
| **HDE Users Guide** | §5.2; §7 workflows; §7.6; §8.1 and §8.2; §16 | See the breakdown below this table |
| **Glow QA Guide** | §9.2.4 | `CONFIG_MAGIC10_OK`: "band edges are sorted, span the clamp range" becomes per category. Wording only |

**HDE Math Spec** drains:

- **Formula:**
  - v2 operations; Balance over all 36 channels;
  - the three-component reduction with the Q-10 gate;
  - Type derivation, aura classes, center outcomes, any-route motor→Throat;
  - Table 7b only, under the 15-point ceiling.
- **Bands:**
  - per-category inclusive maxima as the single §5.3 mapping;
  - the recalibration rule;
  - the "single mapping" and "preset maxima" sentences reconciled.
- **Configuration and identity:**
  - the new `config_id`, `magic10_result.v2` and the `magic10:v2:` cache key;
  - the new manifest member count.
- **Invariants v2 breaks** (R-03):
  - no channel in both signals of one category;
  - one through six channels per Balance signal;
  - the `0..200` domain.
- **Retired:** §5.4.2.1 and the §6.4 flag (Q-7), and §6.3 (R-09).
- **Disclosures:** the Reflector effect (Q-8) and the viewer-preferences sentence (R-22).
- **Goldens:** M10-G001 to G008 replaced.
- **Housekeeping:**
  - renumber the duplicate §5.2.8;
  - qualify "V2" in §2.5;
  - eligibility in §4.1 is unchanged, and Type now enters scoring only.

**HDE Schemas & Artifacts** drains:

- **Doc-Delta triggers and the MAGIC10-HOME decision.**
- **New catalogs:** the centers catalog and the Type-pairing catalog, with paths and schemas.
- **Bands:** per-category bands and the thresholds v2 schema.
- **The v2 configuration** (§2.9):
  - `magic10_mechanics_config.v2` and its fixed fields (§3);
  - loader rules relaxed and added (R-03, R-21);
  - result and compat-result schemas v2.
- **Release:**
  - manifest roster and member count;
  - attestation predicate;
  - evidence entries.
- **Configuration artifacts:** the authoritative-configuration boundary, `config.band_edges`, and consumer bundles.

**HDE Governance** drains:

- **Manifest and catalog:** freeze-pack and catalog-hygiene entries for the new members.
- **Bands:**
  - `BAND_EDGE_GOLDENS_OK` and §4.1.5's 24/49/74 become ten per-category sets;
  - typed bundles' band edges.
- **Release identity.**
- **Doc Delta:** the trigger for band-maxima changes.
- **GATE:CORE-MATCH:**
  - "inclusive maxima, per category";
  - its evidence entries corrected to real paths (R-17: `tests/compat/bands_thresholds/*` and `audit/gates/bands/edges.snapshot.json` do not exist).
- **GATE:CORE-DET** is unchanged.

**HDE Users Guide** drains:

- **The sampler example**, already wrong under v1 (R-16); it must also name a category.
- **Examples and counts:**
  - compat workflow examples;
  - the roster count;
  - `pair.compat.proof.json` thresholds.
- **Known limitations:** `magic10_compat_result.v1` becomes v2.

### 5.2 HDE Build Checklists (PF09 maintenance by the v2 change)

| Checklist | Row | Change |
| :- | :- | :- |
| HDE Build Checklist — Separation | **New task** in the shape of HDE-SEPA005 | The v2 mechanics configuration contract: catalogs, schema, fail-closed loader, identity. HDE-SEPA005 stays Done as v1 history |
| HDE Build Checklist — Conjunction | HDE-CONJ010 (Partial); .1 and .2 | .1 and .2 describe v1's kernel and signal producers, and are re-targeted to v2 |
| HDE Build Checklist — Conjunction | HDE-CONJ010.5 | Unchanged scope (`ts_v0` removal, no Type-only authority). It gains one sentence: the v2 Type component is derived from the gate set and never scores alone (Q-10) |
| HDE Build Checklist — Distillation | HDE-DIST008 (Partial); .1 to .3 | Re-targeted from `magic10_result.v1`, the v1 goldens, Balance operations, band edges and the manifest version text to v2. The stale `--version 1.1.0` text is refreshed (R-17) |
| HDE Build Checklist — Coagulation | HDE-COAG003.6 (Not done) | The active-config cutover guard becomes the v1→v2 cutover |
| HDE Build Checklist — Fermentation | **New deferred row** | The recalibration observation of §2 Q-5 |

### 5.3 Checked, no drain

| Document | Why not |
| :- | :- |
| HDE Narratives Guide | Keys `(category, band, perspective, slot)` and the 360-row registry are unchanged. `balance`'s 36 templates fit the new construct (R-13). One optional sentence may record the construct change |
| HDE Copy Tonality Guide | `balance` reads "give and receive feel even", which fits bilateral completion |
| Plan Templates | The all-ten-categories proof rule is unchanged |
| HD Engine Epics Map | Only if the change is classified as an Epic: a new entry is added. The closed v1 entry stays |
| Change Process Guide; Glow Development Philosophy; Human Design System; The Rave I Ching; 7 Phases of Alchemical Engineering | No Magic10 mechanics content |

### 5.4 Historical, not rewritten

HDE Build Checklist — Calcination, HDE Build Checklist — Dissolution, HDE Phased Epics, Reality Audits, HDE State of the Repository and HDE CRD Records name v1 identities as history. The Change Process Guide keeps historical records in their original identities, so none of them drains.

## 6. Limits, nonclaims, sources

- **Limits.**
  - I verified the engineering facts cited as "verified".
  - The per-Type, per-category and Reflector figures are the review's measurements (#831), which I did not rerun.
  - The §2 Q-5 defaults treat people as independent units, which is conservative for pairs drawn from them.
  - Table 7b's v1.1 effects are unmeasured until the Specialist re-measures.
- **Nonclaims.** This record changes no canon, code, catalog, test, schema, data or Notion page. It adopts nothing: adoption is the Product Owner's, through an HDE Build Notes addendum. It makes no QA, Ops or acceptance claim.
- **Repository sources** (on `main` at `99f00c5c`):
  - **Canon:** `PF01-Canon-HDE-Math-Spec-v1.3.8.md`, `PF02-Canon-HDE-Architecture-v2.4.8.md`, `PF04-Canon-HDE-Governance-v2.8.12.md`, `PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.5.md`, `PF07-Canon-Glow-Infrastructure-v2.3.5.md`, `PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.8.md`, `PF14-Canon-HDE-Mechanics-Guide-v3.5.10.md`, `PF19-Canon-Glow-QA-Guide-v3.0.8.md` and `PF29-Canon-HDE-Users-Guide-v1.0.4.md`.
  - **Build checklists:** `PF09.3-…-v1.1.9.md`, `PF09.4-…-v1.3.3.md`, `PF09.5-…-v1.6.3.md`, `PF09.6-…-v1.1.10.md` and `PF09.7-…-v1.1.10.md`.
  - **Other documents:** `PF15 HDE Copy Tonality Guide v1.2.0.md`, `PF16-Canon-HD Engine Epics Map v2.3.8.md`, `PF17-Canon-HDE-Narratives-Guide-v1.5.4.md` and `PF27-Canon-Plan-Templates-v2.0.7.md`.
  - **Code and schemas:** `engine/constants.py`, `engine/config/registry_loader.py`, `engine/magic10/thresholds.py`, `math/thresholds.json`, `catalog/magic10_mechanics_v1.json` and `schemas/magic10_result_v1.schema.json`, `schemas/magic10_compat_result_v1.schema.json`.
- **Notion:** Candidate CRD Items List, item 13 (read only).
