---
artifact_type: RESCOPE_REVIEW
artifact_id: HDE-EPIC040-PR06-F01-RESCOPE-REVIEW
artifact_version: "1.0"
artifact_state: COMPLETE
decision: APPROVE
change_class: EPIC
change_id: HDE-EPIC040
work_unit_id: HDE-EPIC040-PR06
finding_ref: HDE-EPIC040-PR06-F01
authoring_context: APPROVED_BASE_WITH_OVERLAYS
decided_by: retained whole-change HDE-EPIC040 Implementation Architect, by Product Owner direction
capture_time_utc: 2026-09-25T13:45:47Z
return_to: dedicated PR06 PR-development session (PR-20), the finding's author
---

# HDE-EPIC040-PR06-F01 — Rescope Review v1.0

## 1. Decision and authority

**decision: APPROVE — alternative A, bounded implementation rescope, with the conditions in §4.**

**Authority.** On 2026-09-25, Nathan / Product Owner directed: "The rescoping analysis is yours. It must go back to the PR session that authored it, whether approved or denied." Under that direction the retained whole-change IA owns this analysis and decision. No separate RS-10 proposal session was created.

The finding's own record is the proposal of record: PR06 plan v1.0 §14.1, `docs/ephemeral/HDE-EPIC040-PR06-pr-implementation-plan-v1.0.md`, SHA-256 `583de879f619ccdb5f32e20d5447b69c1509f447d6fb4227dcb963caaaf2e7b7`.

The decision goes back to the session that authored the finding: the dedicated PR06 PR-20 session. The finding arose at pre-Proceed planning, so there is no open PR, no `PR_RETURN_PHASE`, and RS-40 does not apply.

**Bases, unchanged:**
- Specification v1.1
- Audit v2.0
- Plan v2.1 (`10732f93…`)
- Plan Review v2.1
- PR06 instruction v1.0 (`20517abc…`)

**PF10 read:** `docs/pfcanon/PF10-HDE-Build-Notes-v13.3.1.md`, SHA-256 `66305b8f…9c14`. The addenda that bear on this finding are §§2.12, 2.15 and 2.20.

## 2. Boundary — verified

- **Where the gate reads its identity.** `tools/evidence/run_canonical_json_gate.py:70–72` builds `_CAPTURE_IDENTITY_META` from `artifacts/identity/service_identity.json`. At `:365` it raises `runtime_identity_source_mismatch` unless the frozen captures carry exactly that identity. Verified by reading.
- **What the captures carry.** They record their capture-time identity; for example, `artifacts/cli/showcompat/args.json["identity"]["meta"]` has `release_id` `12523fec11d4f0ff375bbc7e0d88352a6f3beb07f3a74cecfae901307bbb6e5c`. They are digest-frozen, and their generators refuse to write (PR04 O-09, O-20, O-21). Verified by reading.
- **What breaks.** PR06 must cut the complete manifest, which moves `release_id`. Inside the isolated closure, the identity family's owners regenerate `service_identity.json` to the current release, as PF12 §6.2.1 and `AGENTS.md` require. The gate then fails, and so does the attestation. The PR06 session reproduced this twice (plan §§3.3 and 10.6). I did not re-run the closure; I verified the code path that produces the failure.
- **Classification.** This is a **bounded implementation rescope**, not in-scope repair. The fix changes which source a governed gate certifies against, and that source is outside instruction §6's loci. That is the gate-semantics line PF10 §2.15 draws.
  - It is **not material** in the PR-10 sense. It changes no Epic outcome, acceptance criterion, product contract or other unit's scope. It restores the gate's own stated intent: governed captures keep their capture-time identity.
  - It is **not** a Specification change and **not** a defect in PR01–PR05.

## 3. Alternatives

| Alt. | Disposition |
| --- | --- |
| **A.** Derive `_CAPTURE_IDENTITY_META` from the frozen captures' own recorded identity instead of `service_identity.json` | **Approved.** One file plus its test. No capture, identity family, closure, builder, schema or wire-value change |
| B. Regenerate the five captures from the admitted release | Not chosen. It re-identifies governed captures and needs a Product Owner capture-contract decision (instruction §9). It stays available for PR07/PO later; this approval does not foreclose it |
| C. Stop regenerating the identity family in the closure | Rejected. It contradicts PF12 §6.2.1 and `AGENTS.md` |

## 4. Conditions (binding on PR-30/PR-35)

1. **Loci extension.** Exactly `tools/evidence/run_canonical_json_gate.py` and its existing test home (for example `tests/evidence/test_canonical_json_gate_check_outputs.py`). Nothing else is added by this approval.
2. **The source must itself be frozen-verified.** Read the capture-time identity only *after* the capture's frozen digest has been verified against the gate's `_FROZEN_GENERATED_SHA256`. Never read it from any file the closure or an owner regenerates.
3. **No weakening of the check.**
   - Every frozen capture that carries identity must agree on that identity; any disagreement refuses.
   - The existing byte, digest and canonical-form checks are unchanged.
   - The 26-target roster and the six set rules are untouched.
4. **Current identity is still certified elsewhere.** `service_identity.json` and the identity family continue to be checked against the current release by their own owners. This change only stops the frozen-capture check from reading a mutable source.
5. **Tests must prove:**
   - the check passes when the closure regenerates `service_identity.json` to a new `release_id`;
   - it refuses a tampered capture identity;
   - it refuses disagreeing capture identities;
   - it refuses an unverified digest.
6. **No other changes.** No change to `hde.release_attestation.v1`, `PR06R_B_FINAL_PASS`, frozen captures, generators or Index rows beyond what the owner run legitimately regenerates. Nothing is hand-edited.
7. **Honest attestation content.** The external attestation carries current identity evidence alongside frozen historical captures with their existing nonclaims. It makes no claim that the captures were produced by the current release.

## 5. Effects

- **Requirements.** `K040-REQ-012` and `AC040-08` become achievable through the end of the interval. Nothing else changes.
- **Other units.**
  - PR07 still owns F03, F05 and F07. PR07 and the PO may later choose alternative B to re-identify the captures.
  - OPS01's final attestation depends on this fix landing.
- **No effect on:** Ops, deployment or QA.
- **PR06 plan completeness.** The rest of PR06 plan v1.0 (§§5–13) stands as complete planning work.

## 6. PF10 overlay

Exactly one addendum is produced: `docs/ephemeral/HDE-EPIC040-PR06-F01-PF10-build-notes-addendum-v1.0.md`. Publishing and numbering it in PF10 is Nathan's action; this review does not edit PF10.

## 7. Return

This decision returns to the dedicated PR06 PR-development session, at PR-20. That session issues PR06 plan v1.1 as a complete successor that incorporates §4, in state `AWAITING_PO_PROCEED` for Nathan's PR-30 Proceed.

No Proceed is requested here. Nothing is implemented, nothing is merged, and PR-50 is not invoked.

## 8. Register and provenance

- **`CANON_CONFLICT_REGISTER`:** C040-01 through C040-06 are carried unchanged. No entry is opened or decided.
- **Provenance:** `GCFPE-USE-HDE-EPIC040-RS-20-20260925-PR06-F01-01`.
  - Role: whole-change IA, deciding by PO direction under RS-20 semantics (091426.1).
  - Captured: 2026-09-25T13:45:47Z.
  - Repository persistence: `PENDING / NON_GATING`.

ASK OK.
