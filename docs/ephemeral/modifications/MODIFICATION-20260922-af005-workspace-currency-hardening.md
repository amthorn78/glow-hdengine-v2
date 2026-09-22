---
artifact_type: GCFPE_MODIFICATION_RECORD
modification_id: MODIFICATION-20260922-af005-workspace-currency-hardening
status: ANALYZED
coupling: ATOMIC
targets: [skill, notion_control]
gate_tier: 1
closure:
  upstream: []
  downstream: []
  state_sharers: []
  note: "NOT COMPUTED — closure.py covers prompts only; this targets a skill, which has no graph part. See finding A3."
readiness: NEEDS_RULING
modification_class: B
modification_class_note: "B or E is genuinely ambiguous, and E means do not do it. See finding A1 — this is the open ruling."
interaction_cost_predicted: 5
interaction_cost_actual:
item_count_at_approval:
items:
  - id: ITEM-01
    statement: "Add one trailing clause to glow-workspace-currency so the executing-by-default rule meets its counterweight in the same breath."
    disposition: ""
request: "Pilot the Modification format end to end on AF-005, the one-clause hardening of glow-workspace-currency deferred 2026-09-22. Testing only; no prompt promotion."
requested_by: Nathan
analyze_approved_by: ""
analyze_approved_date: ""
plan_approved_by: ""
plan_approved_date: ""
supersedes: ""
spawned_from: ""
---

# MODIFICATION-20260922-af005-workspace-currency-hardening

Close `AF-005` — the asymmetric safe default in `glow-workspace-currency` — by adding one trailing
clause, so a session that treats itself as executing also learns that a Notion surface already
naming its item is a destination rule.

**This is the stage 4 pilot.** It is a test of the process. Its findings about the process itself
are recorded separately in `../pe36.mgmt-redesign/PILOT-FINDINGS-stage4.md`.

## §A — Analysis

### The change

One sentence in a body section of `glow-workspace-currency`. The clause is already settled and
recorded verbatim on the Alpha Feedback page, so no wording needs deriving:

```plain text
…and if the Consult step found a Notion surface that already names your item, that surface is a
destination rule and the record belongs there too.
```

It attaches to `A session that cannot tell which kind it is treats itself as executing.` in the
"Where it lands" block. **Not the description**, so the trigger surface does not move.

### Closure and gate tier

**The closure could not be computed, and that is a finding rather than an omission.**
`glow-workspace-currency` is a skill. `closure.py` reads `docs/graph/parts/prompts/*.json`, and
there is no part for any skill — confirmed by listing the directory. So upstream, downstream and
state-sharers are all undefined here, not empty.

**Tier 1 by the conservative rule, not by measurement.** §3.4 defines Tier 0 as "the rebuilt graph
part is byte-identical." A skill has no graph part, so that test cannot return true, and Tier 0 is
unreachable rather than satisfied. The §3.4 caveat also applies directly: this changes what the
skill *instructs*, which is closer to what a prompt *produces* than to how it *routes*.

The practical blast radius is nonetheless real and worth stating plainly: this skill's description
is in context for **every** session in the workspace, and its body loads whenever it fires. The
clause lands in the body, not the description — so the trigger surface is untouched, which is the
one thing `AF-003` says to protect.

### Targets and what they cost

| target | why | what it costs |
|---|---|---|
| **skill** | `glow-workspace-currency` body section | package → **independent §10 review** → Nathan installs → post-install digest comparison |
| **notion_control** | `AF-005` on the Alpha Feedback page must close when this lands | an established destination rule already covers it; the page's own rule is that items are recorded there when the Product Owner defers them |

Baseline digest of the installed skill, measured now: `3 5f2b4ae0d43f0609ae3c3b88409a2578791b008cf6908bd6516181688e06dd93`.

**Coupling is `ATOMIC` but the field is degenerate here** — there is one item, so both values behave
identically. Recorded as a pilot finding, not as a problem with this change.

### Scope, and how it was measured

Broad match, not enumeration. The sentence being amended appears **once** in the installed skill;
grep for `cannot tell which kind` returns exactly one hit in `SKILL.md` and none in either
reference file. No other surface in the workspace restates that default — checked across
`docs/prompt_ecosystem_management/` and the other 24 installed skills.

So scope is one file, one sentence. That part is settled.

### Contradictions and risks

**A1 — `AF-005`'s own deferral condition says not to do this standalone. This is the open ruling.**

The Alpha Feedback entry defers it **with a trigger rather than a date**: *"apply it in the next
change that touches `glow-workspace-currency` for some other reason."* No such change exists. So
running it alone spends precisely the review round the deferral was created to avoid, and the
entry says so in terms: *"the edit is one sentence; the process around it is the whole cost, which
is why it should ride with other work."*

Compounding it, the classification is genuinely ambiguous:

- **Class B, rule application** — carrying a settled reviewer recommendation into the artifact.
- **Class E, normalisation** — `ecosystem-change-management.md` §2 says of Class E: **"Do not do
  it."** And `NORM-001` says *"establish the consumer before proposing the repair."* The §10
  reviewer found the gap is **already closed** elsewhere in the same skill, through the unchanged
  Consult step. A hardening whose gap is already closed has a weak consumer by construction.

The consumer is not zero — it is a reader who meets the default without meeting its counterweight,
across a section boundary. But it is weak, and Class E exists to stop exactly this kind of work.

**This is a policy question with no evidence-determined answer, so it is the Product Owner's.**

**A2 — the pilot's purpose and the change's purpose are not the same thing.** Nathan's instruction
was *"we are only testing."* If the answer to A1 is "do not ship it," the Modification still
succeeds as a pilot: it will have proved that `ANALYZE` catches a change that should not be made,
which is more valuable than proving it can plan one that should.

**A3 — `closure.py` does not cover skills.** Recorded in the pilot findings; it is a gap in the
stage 1 tooling, not in this change.

### Open questions for the Product Owner

**Q1.** `AF-005` defers itself until other work touches this skill, and the change may be Class E,
which the taxonomy forbids. Do you want it applied anyway as a pilot vehicle, or should the pilot
stop here with `ANALYZE` having correctly refused it?

There is a third option worth naming: **run the pilot to `PLAN` and stop there.** That exercises
both approval gates and the planning discipline, produces a complete plan whose cost is visible,
and spends no review round — the plan simply sits until other work touches the skill, which is
exactly what `AF-005` asked for.

### Readiness and interaction cost

    open rulings                     1   (Q1)
    approvals, fixed                 2   (ANALYZE, PLAN)
    independent §10 review cycles    1   (one skill package)
    install events                   1
    merge events                     1   (the repository record)
    ----------------------------------------
    interaction_cost_predicted       5   with Q1 answered; 6 counting the ruling itself

**Readiness: `NEEDS_RULING`** — one open question, and it is not evidence-resolvable.

**This does not block you.** `readiness` is advisory: it reports what `ANALYZE` concluded and has
no power to refuse. If you want this shipped now, say so and it ships — an `override` block
records that the deferral was waived deliberately, and nothing here argues with you.

Splitting saves nothing; there is one item. **What would save the whole cost is waiting**, which is
what `AF-005` already decided. Five round trips for one sentence is the arithmetic that entry was
making, now stated as a number rather than an intuition.

**Prediction confidence: low, and this is the first one.** There is no calibration data yet. §E
records actual against predicted, and that comparison is the only thing that will make later
predictions worth anything.
