---
artifact_type: PF10_BUILD_NOTES_ADDENDUM
addendum_id: HDE-EPIC040-PR06-F01
decision_id: HDE-EPIC040-PR06-F01-RESCOPE-REVIEW v1.0 (APPROVE)
immutable_base: HDE-EPIC040-IMPLEMENTATION-PLAN v2.1 (SHA-256 10732f9338b209e3ce19e81936119e47c9551ea912298a27c731c9e60e2a61be) + HDE-EPIC040-PR06-PR-INSTRUCTION v1.0
pf10_number: not allocated (Product Owner publication)
capture_time_utc: 2026-09-25T13:45:47Z
---

# HDE-EPIC040-PR06-F01 — Frozen-capture identity source for the canonical JSON gate

**Decision.** The whole-change IA approved this bounded implementation rescope on 2026-09-25, by Product Owner direction, as alternative A. The decision record is `docs/ephemeral/HDE-EPIC040-PR06-F01-rescope-review-v1.0.md`.

**Base.** Plan v2.1 §6.6 and PR06 instruction v1.0 §§4–6. Neither is rewritten.

**Delta.** HDE-EPIC040-PR06's loci are extended by exactly two items:
- `tools/evidence/run_canonical_json_gate.py`;
- that file's existing test home.

`_CAPTURE_IDENTITY_META` is derived from the frozen captures' own recorded capture-time identity, read only after each capture's frozen digest is verified. It is no longer read from `artifacts/identity/service_identity.json`, which the isolated attestation closure regenerates to the current release.

**Effects.** Once the complete release is admitted, the closure can run and the attestation can pass. `service_identity.json` and the identity family stay certified against the current release by their own owners.

**Exclusions.** This addendum changes none of the following:
- the success schema `hde.release_attestation.v1` or its wire value `PR06R_B_FINAL_PASS`;
- the frozen captures, their generators or their digests;
- the identity family or the closure;
- the 26 gate targets or the six set rules;
- any Index/Mirror row except by a legitimate owner run.

It does not re-identify the captures. That is alternative B, a Product Owner capture-contract decision, and remains available to PR07 or the Product Owner.

**Binding conditions.** See review §4:
- the identity source must be digest-verified;
- capture identities must agree with each other;
- the existing checks are not weakened;
- tests prove the pass case and every refusal case;
- the attestation must describe its contents honestly.

**Conflicts.** None. `CANON_CONFLICT_REGISTER` entries C040-01 to C040-06 are unchanged.

**Unresolved.** PF10 numbering and publication are for Nathan.

**Return phase.** PR-20 in the dedicated PR06 session. There is no open PR, and RS-40 does not apply.

**Normalized approved-delta digest:** not computed. No governed normalization procedure exists, and none is invented here.
