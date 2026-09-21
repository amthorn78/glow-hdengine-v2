---
artifact_type: PROMPT_ECOSYSTEM_EVIDENCE_NOTE
artifact_version: "1.0"
created_date: 2026-09-21
author: PE35
release: GCFPE-20260914.1 / 091426.1 / 55
subject: D5 is closed, and what the old fixture name concealed — measured, not read
---

# D5 closed, and the coverage it concealed

Written because the record did not say D5 had landed, and a session reading that record concluded it
was still open. That conclusion cost a cycle. This note closes it with evidence.

## D5 is closed — round 21, one line

Round 20's `D5` deferred a correction to the fixture `reject-source-missing-crd-branch` "into the
same change as D4". Round 21 carried `D4` (`SF10-07`) and **also carried D5**, but round 21's report
does not mention it, so the record left D5 looking open.

It landed as a rename, at `docs/ephemeral/gcfpe.round21/sf10-07.patch:205-206`:

```
-            ("reject-source-missing-crd-branch", "QA-120", "`CL-C-10 — ", "`CL-Z-99 — ", "QA_PASS_BODY_CLASS_MAP"),
+            ("reject-source-retargeted-crd-destination", "QA-120", "`CL-C-10 — ", "`CL-Z-99 — ", "QA_PASS_BODY_CLASS_MAP"),
```

The renamed fixture is present in the installed tree at
`flowmaster-validate/scripts/run_gcfpe_20260914_fixtures.py:608`, unchanged in behaviour.

**Why the record misled.** Searching the installed tree for `reject-source-missing-crd-branch`
returns nothing, which is equally consistent with "corrected by rename", "deleted", and "silently
dropped". A grep proves the absence of a *string*, never the absence of a *thing*. The rename is
only findable by reading the patch that performed it.

## What the old name claimed, and what the fixture does

| | |
|---|---|
| name claimed | a CRD branch is **missing** from QA-120's PASS class map |
| mutation actually performs | the CRD branch is **retargeted** — `` `CL-C-10 — `` becomes `` `CL-Z-99 — `` |

Both raise `QA_PASS_BODY_CLASS_MAP`, so the test always fired and always guarded something real. The
defect was purely the label: it advertised coverage of an absent branch that no fixture exercises.
Concealed coverage is worse than visible absence, because it stops anyone from looking.

## The concealed case is guarded — proven by execution, not by reading the code

Reading `validate_qa_closure_bodies` suggests `len(rows) != 2` would catch an absent branch. Reading
is not evidence, so it was measured: on a throwaway copy of the corpus, QA-120's entire `CRD` row was
removed from the class map and the end-to-end validator was run against the installed tree.

```
errors: ['PROMPT_HANDOFF_RECEIVER:QA-120:CL-C-10', 'QA_PASS_BODY_CLASS_MAP']
```

**Two independent checks catch it**, not one — the class-map arity check and the handoff-receiver
binding check. So the finding is precise:

- **Not** a missing guard. Absence of a class-map branch is enforced, twice.
- **Is** an untested path. No fixture exercises absence, so nothing would notice if either guard
  later regressed.

That is a real but minor gap, now visible instead of concealed. It is **not repaired here**: adding
a fixture changes packaged skill bytes, which voids the hash-scoped `SKILL_FIT_CONFIRMED` and costs a
fresh §10 round. It belongs in the next change that moves those bytes, batched with `F1`
(`validator_revision` → 3.2.9), exactly as `D5` itself was batched with `D4`.

## The economics, which is the durable lesson

A one-line naming fix changes packaged bytes, and packaged bytes are hash-scoped, so a typo in a test
name carries the same review price as a substantive repair. `SFR-01` wanted D5 before installation
and was right on the merits; `D5` declined anyway and batched it, buying one §10 round instead of
three. `F1` and this fixture gap now sit in the same queue for the same reason.
