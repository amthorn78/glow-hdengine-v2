---
artifact_type: RESCOPE_REVIEW
artifact_id: HDE-EPIC040-PR06b-RESCOPE-DECISION
artifact_version: "1.0"
artifact_state: COMPLETE
decision: APPROVE
change_class: EPIC
change_id: HDE-EPIC040
finding_ref: HDE-EPIC040-PR06a CR-02 / C040-08
authoring_context: APPROVED_BASE_WITH_OVERLAYS
decided_by: retained whole-change HDE-EPIC040 Implementation Architect, by Product Owner direction ("Decide on this", 2026-09-26)
capture_time_utc: 2026-09-26T12:28:59Z
---

# HDE-EPIC040-PR06b — Rescope Decision v1.0 (C040-08)

## 1. Decision

**decision: APPROVE alternative A.** The Reader v1 schema's error branch will admit the error envelope the route actually emits. This is delivered by a new bounded code unit, **HDE-EPIC040-PR06b**, whose overlay is `docs/ephemeral/HDE-EPIC040-PR06b-PF10-build-notes-addendum-v1.0.md`.

**Authority.** On 2026-09-26, Nathan / Product Owner directed: "Decide on this". This follows the route PR06a used (PF10 §2.23). The bases are unchanged: Specification v1.1, Audit v2.0, Plan v2.1 and Plan Review v2.1.

## 2. Defect — verified

- Every Reader v1 error response carries `"schema":"v1"`. For example, `POST /api/reader?v=1` with body `{}` returns 422 `{"code":"ERR_READER_INVALID_INPUT","error":"invalid Reader request","ok":false,"schema":"v1"}`. I reproduced this at `d79cfc1`.
- The v1 error branch (`additionalProperties: false`; keys `ok`, `code`, `error`, `retry_after_ms`) rejects that response. Any client that validates v1 errors against the published schema therefore rejects real errors. Success responses are not affected.
- The Reader v2 schema already has the correct shape: the key `schema`, plus an error branch built from the governed token/message pairs of `ERROR_TOKEN_MAP`.
- The canon conflict: PF05 §5.2 requires the envelope that carries `schema`, while PF01 §2.3 and PF04 §8.1.2 forbid it.

## 3. Alternatives

| Alt. | Disposition |
| --- | --- |
| **A.** Admit `schema` (const `"v1"`) and the governed error codes in the v1 error branch, matching the v2 error branch | **Approved.** The published schema then matches the bytes clients receive. It is a small change. Its cost is a release re-cut, because the schema is a release member |
| B. Retire v1 and refuse `v=1` | Rejected. It reverses PF10 §2.23 and PF04 OI-001, changes PF05's production route, and breaks the Reader↔CLI parity family. That is a cross-canon public-contract change |
| C. Leave it as recorded | Rejected. It keeps a known, client-visible contract defect in the release that OPS01 attests |

## 4. Classification and placement

- **Classification.** This is a bounded implementation rescope that changes a governed public schema. It is **not material** at Epic level: it changes no Epic outcome, no Magic-10 behaviour and no route. It corrects the v1 schema so that it describes existing bytes. Reader v1's *response* bytes do not change.
- **Why a new unit.** It cannot go into PR06a, which is merged, or into PR07, which is documentation-only. It must land **before OPS01**, because it changes the `release_id` that OPS01 verifies.
- **New order:** `PR01 → … → PR06 → PR06a → PR06b → PR07 → OPS01`. PR07 documents the v1 schema as PR06b delivers it.

## 5. Register

- **C040-08** is decided **A**. PR06b makes the repository schema conform to PF05 §5.2.
- Updating PF01 §2.3 and PF04 §8.1.2 so that they admit `schema` in the Reader v1 error envelope belongs to their governed maintainers. That drainage is pending and non-gating for PR06b, as it was for C040-07.
- C040-01 through C040-07 are unchanged.

## 6. Return

The next stage is PR-10 for HDE-EPIC040-PR06b in this whole-change IA session, then PR-20 in a dedicated PR06b session. No Proceed is requested here. Nothing is implemented or merged, and PR-50 is not invoked. PF10 numbering and publication of the overlay are Nathan's actions.

## 7. Provenance

`GCFPE-USE-HDE-EPIC040-RS-20-20260926-PR06b-01`. The role is the whole-change IA, deciding by PO direction under RS-20 semantics (091426.1). Repository persistence is `PENDING / NON_GATING`.
