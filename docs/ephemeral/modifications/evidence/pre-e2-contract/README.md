# Pre-E2 direct-handoff contract, kept as the regenerator's input

`gcfpe-20260914.1-091426.1-direct-handoff-contract-4.0.6.json` is the 091426.1 direct-handoff
contract as installed before the `D23` E2 regeneration: `contract_revision` 4.0.6, 606 657 bytes,
sha256 `2b78f877e7a31efb2da8488d7f129794e60bcbdbf9f43e9851a319f83f06b53b`. It holds no prompt bodies.

`evidence/repair-a4/contract_recipe.py` regenerates the shipped contract (`6902924a…`, 613 326 B)
byte for byte from this file, and from no other. Until 2026-09-23 the file existed only in session
scratch copies. It is kept here so that the regeneration can be reproduced from the repository
(`MODIFICATION-20260923-closeout-residuals`, ITEM-13). Verified in the ANALYZE verification run:
`contract_recipe.py` with this template produced the shipped contract byte-identical.
