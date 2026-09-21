---
artifact_type: PROMPT_ECOSYSTEM_EVIDENCE_NOTE
artifact_version: "1.0"
created_date: 2026-09-21
author: PE35
release: GCFPE-20260914.1 / 091426.1 / 55
subject: The §5 optional-input line cannot be closed by any instrument that exists, and two earlier claims about it were wrong
---

# The optional-input item, measured

The plan's §5 line reads:

> *Verify that each optional input has an exact predicate and does not silently become mandatory.*

It was the last open plan item that is not a gate. **It cannot be ticked, and the reason is not that
the work is outstanding — it is that nothing in the ecosystem records which inputs are optional.**

## Measured: input optionality is classified nowhere

| surface | `REQUIRED` | `OPTIONAL` | `CONDITIONAL` |
|---|---|---|---|
| `project-prompt-contract-registry.md` | 0 | **0** | **0** |
| the candidate contract | — | **0** | 56, but every one is a `route_kind` — `CONDITIONAL_RECOVERY`, `CONDITIONAL_CONTINUATION` — describing **route branches, not inputs** |
| `gcfpe.batch-1.contract-ledger.md` | 2 | **0** | **0** |
| `gcfpe.batch-2.contract-ledger.md` | 1 | **0** | **0** |
| `gcfpe.consolidated-pass.repair-report.md` | 0 | **0** | **0** |

The registry's `inputs:` are flat token lists. The contract's `member_registry` carries no input
classification at all. **Optionality exists only as prose inside the prompt bodies.**

## Two of PE35's own claims were wrong

**1. "One pass over the 37 registry rows closes it."** Written into the plan reconciliation earlier
today. False — the registry holds no optionality data, so no pass over it can establish the
property.

**2. "Batches 1 and 2 verified it per prompt for their 18."** Also false. Their contract ledgers
carry `REQUIRED` twice and once respectively, and `OPTIONAL` and `CONDITIONAL` **zero times**. The
per-prompt reviews did not record an optionality classification either.

So the line has never been satisfied for **any** of the 55, not for 37 of them. The reconciliation
asserted partial coverage that the record does not support. Both statements were made confidently
and neither was checked — the same failure as *"the package is SMALLER than the tree it replaces."*

## The mechanical proxy is already struck

The obvious corpus-free substitute — *is every declared input produced by something?* — was built and
discarded during the consolidated pass: an artifact-equality closure test failed on **109 of 114
pairs**, because consumers declare references such as `SPECIFICATION_ID` where producers declare
artifacts such as `CRD_SPECIFICATION`. Under **`D11`**, a check that fails on nearly every member of
a set indicts the check, not the set. It is not available as evidence and must not be revived as a
proxy here.

## What the line was actually protecting against, and whether that is covered

The concrete harm is stated elsewhere in the plan, at §12:

> *Ordinary PR work does not require QA Guide or QA Plan artifacts; specifically relevant later QA
> evidence is conditional only.*

That instance **is** evidenced, mechanically and without any body: `PR-20`'s registry row declares
exactly one input, `PR_INSTRUCTION_ID`, and that row is validated against the live page. The
specific defect the §5 line guards against is caught. Its **general** form is unfalsifiable as the
ecosystem currently records itself.

## Disposition

**The box stays unticked, permanently, with this note as its reason.** Closing it would require
adding an input-classification field to all 55 registry rows, which means reading all 55 bodies —
a corpus read the Prompt Corpus Storage and Fidelity Policy forbids in bulk, to establish a
property no consumer currently reads.

**Recommended:** record the line as *not satisfiable by any existing instrument*, note that its one
concrete instance is separately evidenced, and let post-release change management add optionality
classification if a consumer for it ever appears. Spending a corpus read on an unread field, at the
end of a repair, inverts the policy's own test: *before proposing any check, ask what it would catch
that matters.*

## The durable lesson

**An unfalsifiable acceptance criterion is a defect in the plan, not a task in the backlog.** This
line survived twenty-seven rounds because it reads like work. It is not work; it is a question the
ecosystem has no way to answer about itself, and the honest disposition is to say so rather than to
keep it open or to tick it on adjacent evidence.
