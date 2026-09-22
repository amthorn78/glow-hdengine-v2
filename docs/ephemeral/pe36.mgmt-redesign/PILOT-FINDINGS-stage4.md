---
artifact_type: GCFPE_MGMT_REDESIGN_PILOT_FINDINGS
artifact_version: "1.0"
created_date: 2026-09-22
session: PE36
stage: 4 — pilot
vehicle: MODIFICATION-20260922-af005-workspace-currency-hardening
status: ANALYZE_RUN_AWAITING_PRODUCT_OWNER_RULING
scope: findings about the process, not about AF-005
---

# Stage 4 pilot — findings from running `ANALYZE` for real

`AF-005` was run through `MODE = ANALYZE` as the stage 4 pilot, on the Product Owner's
instruction that this is a test and no prompt is promoted. The Modification is
`docs/ephemeral/modifications/MODIFICATION-20260922-af005-workspace-currency-hardening.md`,
at `status: ANALYZED`, `readiness: NEEDS_RULING`.

**Five findings, two of them serious and both fixed.** Three are gaps in the stage 1 tooling, one
is the pilot working exactly as intended, and one is the Product Owner catching the design with
the authority inverted.

---

## P1 — The scope-freeze guard was opt-in and silently inert. **FIXED**

**Severity: the highest of the four.** Scope freeze is the rule that bounds the review loops — it
is the answer to twenty review rounds on one PR. Its guard did nothing unless someone remembered
to set a field.

`modification_validate.py` read `item_count_at_approval` and compared it to the item count *only
when the field was present*. A Modification that never set it could grow items freely after
approval and still pass every check. Demonstrated, not reasoned about: a fixture at
`status: EXECUTING` with an item openly labelled "smuggled in after approval" **passed**.

This is `PAIR-001` — the invariant is violated and every check passes, because the instrument that
tests it cannot run.

**Fixed in the same pass.** The field is now required once status reaches `PLANNING` or later, and
a fourteenth injected regression asserts it. The selftest is 14/14.

**The lesson generalises past this script.** A guard with an optional precondition is not a guard;
it is a guard-shaped thing that fires when the author was already being careful. Every future
check in this design should be read with the question *what happens if the field is simply absent?*

## P2 — `closure.py` covers prompts only, so the tier model has no answer for skills

`glow-workspace-currency` is a skill. `closure.py` reads `docs/graph/parts/prompts/*.json`, and no
skill has a graph part — confirmed by listing the directory. Upstream, downstream and state-sharers
are therefore **undefined** for a skill-targeted Modification, not empty.

That propagates into §3.4. Tier 0 is defined as *"the rebuilt graph part is byte-identical."* A
skill has no graph part, so the test cannot return true and **Tier 0 is unreachable rather than
satisfied.** The pilot assigned Tier 1 by conservative default and recorded why.

Not fixed, because the right fix is a design decision rather than a code change. Three options, in
rough order of appeal:

1. **Say plainly that skills are always Tier 1 or 2, and that Tier 0 is a prompt-only concept.**
   Cheapest, honest, and matches the fact that any skill byte change voids its §10 verdict anyway.
2. Define a skill equivalent of the interface contract — description unchanged plus body sections
   unchanged — and let that unlock a Tier 0.
3. Extend the graph to model skills. Large, and `D16` already rejected adding skill machinery
   without a consumer.

**Recommendation: (1).** A skill change always costs a package, a review and an install, so there
is no cheap tier to unlock. Pretending otherwise would be the shortcut that eventually bites.

## P3 — `coupling` is degenerate for a single-item Modification

With one item, `ATOMIC` and `INDEPENDENT` behave identically. The pilot set `ATOMIC` and said so.

Harmless, and not worth a rule. Recorded so a future session does not spend time deciding it.

## P4 — `ANALYZE` refused the change, and that is the pilot succeeding

The Modification came back `NEEDS_RULING` with one open question, because `AF-005`'s own deferral
condition says *"apply it in the next change that touches `glow-workspace-currency` for some other
reason"* — and no such change exists. Running it standalone spends exactly the review round the
deferral was created to avoid.

`ANALYZE` also surfaced that the classification is ambiguous between **Class B** and **Class E**,
and `ecosystem-change-management.md` §2 says of Class E: **"Do not do it."** The §10 reviewer had
already found the gap is closed elsewhere in the same skill, which is a weak consumer by
construction — `NORM-001`.

**The process caught a change that arguably should not be made, before anyone planned it.** That is
worth more as a pilot result than a clean run through all three modes would have been. The old
process had no step at which that question got asked.

It also produced the number the deferral was reasoning about intuitively: **five round trips for
one sentence.**

## P5 — `readiness` read as a refusal, and there was no override. **FIXED**

Raised by the Product Owner on seeing the pilot's result: *"I need to be able to override of
course, I don't want to be told I have to wait if I need the modification."*

Correct, and the design had the authority backwards in two ways.

**The name.** `BLOCKED_ON_YOU` reads as *the system is refusing you*. It never blocked anything
mechanically — `readiness` was only ever vocabulary-checked — but the token, the document and this
session's own reporting all made it sound like a gate. Renamed **`NEEDS_RULING`**, which says what
it is: a conclusion, not a refusal. It also removes a near-collision with the triage disposition
`NEEDS_YOU`, which is a different, item-level thing.

**The missing mechanism.** Some gates genuinely do fail closed — scope freeze most of all, and P1
had just made it mandatory. There was no way for the Product Owner to say *do it anyway*, so the
only routes were to argue with the validator or bypass it. Both are worse than a recorded waiver.

An `override` block now waives a policy gate and records that the waiver was deliberate:

```yaml
override:
  by: Nathan
  overrides: [scope_freeze]
  reason: "needed now"
```

Accepted for `scope_freeze`, `readiness`, `modification_class`, `gate_tier` and `deferral`.
Rejected when unattributed, unreasoned, or when it claims to waive a **well-formedness** check —
an override waives policy, but it cannot make a malformed record well-formed, because a missing
section is the document failing to say what happened and waiving that only makes the record lie.

Three injected regressions assert those rejections. The selftest is 17/17.

**The principle, now written into the template and the plan:** every gate in this design exists to
stop a **session** proceeding on its own judgement. None exists to stop Nathan. A process that
tells the Product Owner to wait for his own change has the authority inverted, and this one did.

---

## What the pilot has not yet tested

`PLAN` and `EXECUTE` have not run. That is correct rather than incomplete — the design requires
Product Owner approval between modes, and self-approving would have tested nothing. The gates held.

**Interaction cost prediction is uncalibrated.** This is the first Modification; predicted is 5 and
actual is empty. One data point will not calibrate anything, and three or four will begin to.

## Recommended next step

**Run the pilot to `PLAN` and stop there.** It exercises both approval gates and the planning
discipline, produces a plan whose cost is visible and whose steps are mechanical, and **spends no
review round** — the plan then sits until other work touches the skill, which is exactly what
`AF-005` asked for.

That tests two of three modes, respects the deferral, and leaves a ready-to-execute plan attached
to the deferred item. `EXECUTE` gets tested by the first real change that has a reason to ship.
