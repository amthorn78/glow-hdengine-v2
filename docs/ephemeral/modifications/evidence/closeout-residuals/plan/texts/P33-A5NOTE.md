## Correction, 2026-09-23 — C8 and §2 overstated the comment rule

Recorded by `MODIFICATION-20260923-closeout-residuals` (ITEM-15). The brief above is left as written
(`AUTH-001`). SFR-A5-1 N1 and SFR-A5-2 F3 are one finding in two halves: a code half, which ITEM-15
repairs in `flowmaster-validate`, and a claim half, which this note corrects. Both round-a5 verdicts
were `SKILL_FIT_CONFIRMED`, and neither depends on the statements corrected here.

- **C8 was too broad** (the claim half of N1). It says that adding "any HTML comment other than a
  whole-line FLOWMASTER marker" fails the suites. The round-a4 rule (R1) looked only for `<!--`,
  `-->` and `--!>`. A bogus comment (`<!x …>`), a processing instruction (`<?…?>`) and a CDATA
  section (`<![CDATA[`), which an HTML parser also turns into comment nodes, passed every gate
  (SFR-A5-1 probes D1, D2 and D4; SFR-A5-2 probe Q2). C8 held for `<!--`-delimited comments only.
  SFR-A5-2 read C8 as holding as worded; this note takes N1's reading.
- **§2's known limits were incomplete** (the claim half of F3, and N1's limit entry). They did not
  list text hidden in a rendered file by markup other than a comment: an unclosed `<script>` or
  `<style>`, a `<template>` element, a `<div hidden>` element, or a `[//]: #` reference line. Each
  passed every gate (SFR-A5-1 probes D3, D5, D7 and D8; SFR-A5-2 probes Q1, Q2b and Q4).

**What ITEM-15 changes.** `flowmaster-validate` 3.3.1 replaces R1's token test with
`DISPATCH_HIDING_RE`. After the six whole-line section markers are removed, it rejects any `<!` or
`<?` in a carrying file (every comment, bogus comment, declaration, CDATA section and processing
instruction), any `--!>`, any opening `<script`, `<style`, `<template` or `<textarea` tag, and any
`[label]: #` reference line. The markers it admits are exactly `FLOWMASTER_CORE_`,
`FLOWMASTER_SPECIALIZATION_` and `FLOWMASTER_PROHIBITIONS_`, each with `BEGIN` or `END` (SFR-A5-2
F2), and a bare `-->` arrow is no longer rejected (SFR-A5-1 N4, SFR-A5-2 F4). From 3.3.1, C8's
comment clause holds for every construct that opens with `<!` or `<?`.

**The limit that remains.** `<div hidden>`, `<details>` and other type-6 HTML blocks are not matched
by `DISPATCH_HIDING_RE`, and neither is any other element that hides text through an attribute such
as `hidden`. They hide text only in some renderers, and they share their HTML block type with
ordinary markup. The whole passage moved intact into such an element stays a known limit, as §2
lists for `<details>`. A model reads the raw file, and the pinned passage is counted on the raw
file, so the risk is to a human reading the rendered file.
