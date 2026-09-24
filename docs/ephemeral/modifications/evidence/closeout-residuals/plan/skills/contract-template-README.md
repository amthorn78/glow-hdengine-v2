# Direct-handoff contract template

`gcfpe-20260914.1-091426.1-direct-handoff-contract-4.0.6.json` is the 091426.1 direct-handoff contract as
installed before the `D23` E2 regeneration: `contract_revision` 4.0.6, 606 657 bytes, sha256
`2b78f877e7a31efb2da8488d7f129794e60bcbdbf9f43e9851a319f83f06b53b`. It holds no prompt bodies.

It is the template that `glow-graph-contract`'s `scripts/contract_recipe.py` regenerates the contract from,
together with a build of `docs/graph/parts`, the successor R1 oracle bundled in `flowmaster-validate`, and
`docs/prompt_ecosystem_management/gcfpe.decision-record.md`. With `--contract-revision 4.1.0
--primary-skill-revision 1.3.0` the recipe reproduces the contract shipped until 2026-09-23 (`6902924a…`,
613 326 B) byte for byte. `MODIFICATION-20260923-closeout-residuals` PART-01 regenerates it with 4.1.1 and
1.3.1.

Moved here from `docs/ephemeral/modifications/evidence/pre-e2-contract/` (kept there in commit `245b21b`)
by `MODIFICATION-20260923-closeout-residuals` ITEM-13: every regeneration reads it, so it is maintained
source, not evidence. Do not edit it; it is an input, and its digest is stated above.
