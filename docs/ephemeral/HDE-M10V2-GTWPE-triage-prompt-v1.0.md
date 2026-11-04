---
artifact_type: SESSION_PROMPT
artifact_id: HDE-M10V2-GTWPE-TRIAGE-PROMPT
artifact_version: "1.0"
subject: GTWPE triage entry for draining the Magic10 v2 adoption into permanent canon
requested_by: Nathan / Product Owner, 2026-11-02 ("You can create a prompt that will go into the GTWPE flow for triage. it only needs the files you specified. The caveats and classifiers should be in source files, not prompt context")
author: Isis, Lead Developer (https://claude.ai/code/session_01Q789tyhUaytmY7x273kwes)
precondition: the next PF10 base version, containing the Magic10 v2 adoption addendum (docs/ephemeral/HDE-M10V2-PF10-adoption-addendum-draft-v1.0.md), is published on main (SUP-1 to SUP-4 are already on main: #824, #831, #832, #823)
created_at: 2026-11-02T13:45:00Z
---

**Model and reasoning setting**

**TypeSafe v8.2: Opus 5.5 at extra high.** Effort score 2.78 (confidence 0.37).

- **Rung probabilities:** low 0.00, medium 0.08, high 0.41, extra high 0.32, max 0.02, ultracode 0.17.
- **Model probabilities:** Fable 5.1 0.01, Opus 5.5 0.60, Sonnet 5.5 0.29, Haiku 5.5 0.10 (confidence 0.47).
- **Twenty-four cells,** computed from the two answers:

  | Model | low | medium | high | extra high | max | ultracode |
  | :- | -: | -: | -: | -: | -: | -: |
  | Fable 5.1 | 0.000 | 0.001 | 0.004 | 0.003 | 0.000 | 0.002 |
  | Opus 5.5 | 0.000 | 0.048 | 0.246 | 0.192 | 0.012 | 0.102 |
  | Sonnet 5.5 | 0.000 | 0.023 | 0.119 | 0.093 | 0.006 | 0.049 |
  | Haiku 5.5 | 0.000 | 0.008 | 0.041 | 0.032 | 0.002 | 0.017 |

- **Flags:** boundary between extra high and high.
- **Sent:** 2026-11-02T13:37:50Z.

Nathan picks the cell.

# Prompt (paste everything below the rule)

---

Run GTWPE-FLOW-10 100926.1, Triage and Hand Off Technical Writing, with TW-TRIAGE-10 100926.1, in repository `amthorn78/glow-hdengine-v2` at the current `origin/main`.

Source set:

- **SRC-1.** The latest PF10 base version under `docs/pfcanon/`, read whole.
- **SUP-1.** `docs/ephemeral/HDE-M10V2-mechanics-proposal-v1.0.md`
- **SUP-2.** `docs/ephemeral/HDE-M10V2-mechanics-proposal-review-v1.0.md`
- **SUP-3.** `docs/ephemeral/HDE-M10V2-open-questions-resolution-and-drain-targets-v1.0.md`
- **SUP-4.** `docs/ephemeral/HDE-M10V2-hd-math-specialist-design-brief-v1.0.md`

Target set: the current versions under `docs/pfcanon/` of:

- PF01 HDE Math Spec
- PF12 HDE Schemas and Artifacts
- PF04 HDE Governance
- PF14 HDE Mechanics Guide
- PF05 HDE CLI API Vendor Ref
- PF02 HDE Architecture
- PF07 Glow Infrastructure
- PF29 HDE Users Guide
- PF19 Glow QA Guide
- PF09.3 Separation
- PF09.4 Conjunction
- PF09.5 Fermentation
- PF09.6 Distillation
- PF09.7 Coagulation
