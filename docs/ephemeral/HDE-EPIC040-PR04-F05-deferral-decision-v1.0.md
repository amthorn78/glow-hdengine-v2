# HDE-EPIC040-PR04-F05 — Reader response vs published schema: Product Owner deferral decision v1.0

```yaml
artifact_type: PRODUCT_OWNER_DEFERRAL_DECISION
DECISION_ID: HDE-EPIC040-PR04-F05-DEFERRAL
version: v1.0
state: DECIDED
repository_path: docs/ephemeral/HDE-EPIC040-PR04-F05-deferral-decision-v1.0.md
change_class: EPIC
change_id: HDE-EPIC040
work_unit_id: HDE-EPIC040-PR04
finding_ref: HDE-EPIC040-PR04-F05
finding_title: The production Reader response fails schemas/reader.v1.schema.json
raised_by: Codex code review on head aa5c3ccf33df367dbaadec490e12de99bb89fd95 (P2, adapter/http_reader.py:602)
verified_by: dedicated PR04 PR-development session, PR-35 phase, by execution plus jsonschema validation
decision: DEFER — PR04 merges as implemented; the mismatch is an accepted, owned deviation
decided_by: Nathan / Product Owner, 2026-09-22 (option 3 — fix F06, defer F05)
return_point: PR07
rescope_raised: NO — no RESCOPE_REQUEST was issued; PR_RETURN_PHASE remains PR-35
```

## 1. Decision

The Product Owner chose option 3: fix the stored-row Gate error contract (F06) in PR04, and **defer this one**. The production Reader keeps emitting the admitted magic10 category identities, and `schemas/reader.v1.schema.json` plus `goldens/reader/v1/*` keep the legacy identities. The divergence is recorded here as an accepted deviation with a named owner, not a rescope. No corrective push was made for this finding.

## 2. The finding, as verified

Executed against the production `POST /reader` route under closed rails, with the synthetic complete release injected so the route returns a success body:

```
POST /reader?v=1  ->  200
categories emitted:   ['harmony']
jsonschema validate:  FAIL — 'harmony' is not one of
                      ['open_leader', 'warm_leader', 'cool_leader', 'glow_leader']
```

The dev `GET /reader` surface emits the same `harmony` identity. `goldens/reader/v1/g03_open_leader.json` still carries `open_leader`.

## 3. Why it is this PR's doing

`adapter/http_reader.py` at the approved base `3b8084d0` contained **zero** occurrences of `harmony`: the identity is not hardcoded, it comes from the admitted mechanics order. PR04 switched the Reader onto the PR03 magic10 core, whose authority is `engine.categories.registry.FROZEN_MAGIC10_ORDER` (plan correction P-10), and that changed the emitted category identities away from the legacy `*_leader` set of the retired scorer.

Plan v1.2 §7 lists `schemas/reader.v1.schema.json` and `goldens/reader/v1/*` as unchanged by PR04, so they were left describing the retired scorer's identities. The result is a public Reader success body that does not validate against the repository's own published Reader schema.

## 4. Consequence accepted by this decision

A schema-validating client or SDK rejects a successful production Reader response. This is accepted knowingly under the current posture, in which no release is admitted and every production path ends `RELEASE_NOT_ADMITTED`, so no client is served today.

## 5. Why no in-scope fix was attempted

Correcting it means changing `schemas/reader.v1.schema.json` — the published public Reader contract — together with the `goldens/reader/v1/*` fixtures that pin it. Plan v1.2 §7 explicitly holds both unchanged, and a published-schema change is a public-contract decision rather than an implementation detail. The alternative, reverting the Reader to the legacy identities, would contradict P-10 and the admitted mechanics authority.

## 6. What PR07 inherits

| Item | Detail |
| --- | --- |
| `schemas/reader.v1.schema.json` | Admit the magic10 category identities, or otherwise reconcile the published contract with the admitted mechanics order |
| `goldens/reader/v1/*` | Regenerate the pinned fixtures alongside the schema, through their owner |
| Any published SDK or client contract | Confirm consumers move with the identity set |
| Relationship to F03 | F03 (production route path) is also deferred to PR07; both concern the same production Reader surface and should be settled together |

## 7. Status of this finding on the PR

Codex thread `#discussion_r4074095779` carries the verification and this disposition. The finding is real, dispositioned and owned; it is not fixed in PR04 by Product Owner decision. Nothing in the PR was reverted, and the rest of the PR-35 work is unaffected and verified on the current head.
