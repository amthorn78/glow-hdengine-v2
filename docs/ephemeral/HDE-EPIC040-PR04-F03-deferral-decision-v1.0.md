# HDE-EPIC040-PR04-F03 — Production Reader route gap: Product Owner deferral decision v1.0

```yaml
artifact_type: PRODUCT_OWNER_DEFERRAL_DECISION
DECISION_ID: HDE-EPIC040-PR04-F03-DEFERRAL
version: v1.0
state: DECIDED
repository_path: docs/ephemeral/HDE-EPIC040-PR04-F03-deferral-decision-v1.0.md
change_class: EPIC
change_id: HDE-EPIC040
work_unit_id: HDE-EPIC040-PR04
finding_ref: HDE-EPIC040-PR04-F03
finding_title: The production Reader is not served at the PF05 Required-Now route POST /api/reader
raised_by: Codex code review on head 7fe363069bcd9471fe7146dadcfc9b3cced85817 (P1, adapter/http_reader.py:577)
verified_by: dedicated PR04 PR-development session, PR-35 phase, by execution against the Procfile entry point
decision: DEFER — PR04 merges as implemented; the gap is an accepted, owned deviation
decided_by: Nathan / Product Owner, 2026-09-22
return_point: PR07 (already owns the adjacent endpoint-catalog gap O-03)
rescope_raised: NO — no RESCOPE_REQUEST was issued; PR_RETURN_PHASE remains PR-35
```

## 1. Decision

The Product Owner decided to **defer**. HDE-EPIC040-PR04 merges as implemented; the production Reader continues to be served at `POST /reader`. The divergence from PF05's Required-Now `POST /api/reader?v=1` is recorded here as an accepted deviation with a named owner and return point (PR07), not as a rescope. No corrective push was made for this finding and no approved scope changed.

This record exists so no later work unit has to rediscover the finding, and so the disproven premise in plan v1.2 does not silently propagate.

## 2. The finding, as verified

Measured on the deployed entry point `adapter.factory:create_app()` (`Procfile`: `gunicorn 'adapter.factory:create_app()'`) under closed rails `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev`:

| Request | Result |
| --- | --- |
| `POST /reader?v=1` | 503 — reaches the production handler (expected F01 non-admitted posture) |
| `POST /api/reader?v=1` | **404 — no such route** |
| `GET /reader?v=1` | 400 — reaches the dev fixture handler |

`app.url_map` contains exactly `/reader` (GET, POST) and `/dev/reader/conjunction`. `adapter/http_reader.py:963` binds `bp = get_reader_bp()`; `adapter/factory.py` registers it with `url_prefix=""` and `adapter/wsgi.py` with no prefix. Neither file is touched by this PR.

## 3. What PF05 says

`docs/pfcanon/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.2.md`, SHA-256 `a12574965dc98c96c53822c4151db38bad48c91a00e3851e973e6a7ffa33d11e`:

- §"CLI commands" (line 107), **Required-Now**: "`POST /api/reader?v=1` is the adopted production application route. … The existing file-path GET Reader remains development-only and non-authoritative."
- §5.1.0 "Production POST request and resolution (normative)" (line 2065): "`POST /api/reader?v=1` accepts one JSON object with exactly `a_id` and `b_id`."
- §5.6 Endpoint Catalog route table (line 2481): `| /api/reader | POST | production application Reader v1 … |`, listed separately from `| /reader | GET, HEAD | internal dev-harness … |`.
- §"Route and gate (must)" (line 2357): the `/api/reader` alias holds "**when** the Reader blueprint is mounted under an `/api` prefix in a runtime configuration" — a mount this runtime does not configure.
- §"Route and gate (must)" (line 2353): `GET /reader` is the canonical Reader route for the v1 dev/proof surface — correct as implemented.

## 4. Consequences accepted by this decision

1. The PF05 Required-Now production route `POST /api/reader?v=1` is not reachable; a client calling it receives 404.
2. The production Reader handler is served unprefixed, so ingress policy scoped to `/api` does not cover it. This is the security-relevant half of the finding and is accepted knowingly, under the standing posture that no release is admitted yet (F01) and every production path currently ends `RELEASE_NOT_ADMITTED`.
3. Plan v1.2's justification (item 5, risk R-18, observation O-11) — that the two spellings "name the same existing declared route in this application" — remains in the approved plan text but is factually wrong. Recorded as O-13 for correction.

## 5. Why PR04 did not cause it, and why no in-scope fix existed

`@bp.post("/reader")` already existed at the approved base `3b8084d0` as a 405 `method_not_allowed` stub. The route-declaration set is identical between base and head — same fifteen declarations, same paths and methods, line numbers shifted only. What PR04 changed is that this path now serves the real production handler, converting a dormant mount discrepancy into a live one.

| Candidate fix | Why it exceeded this work unit |
| --- | --- |
| Add a second `@bp.post("/api/reader")` decorator | Plan v1.2 states "PR04 adds no route"; PF05's mechanism is a mount-prefix alias, not a duplicate declaration; it would need a `docs/ENDPOINTS_CATALOG.json` row governed by PR07 (O-03) |
| Mount the blueprint under `/api` | Moves `GET /reader` — the PF05 canonical dev/proof surface — plus `/internal/version`, `/ops/*` and `/dev/*`; breaks the A7 transport proofs, the endpoint catalog and the determinism/parity families |

## 6. What PR07 inherits

| Item | Detail |
| --- | --- |
| Serve the production Reader at `/api/reader` | By the mechanism PR07 / the IA selects, consistent with PF05 §5.6 and the alias posture |
| `docs/ENDPOINTS_CATALOG.json` | Already owed a `POST` success row (O-03); a production `/api/reader` row would join it |
| Ingress scope | Confirm the production route falls inside `/api`-scoped policy once moved |
| Plan note correction | Supersede plan v1.2 item 5 / R-18 / O-11 (O-13) |

## 7. Status of this finding on the PR

Codex thread `#discussion_r4073702876` carries the verification and this disposition. The finding is real, dispositioned and owned; it is not fixed in PR04 by Product Owner decision. Nothing in the PR was reverted, and the rest of the PR-35 work is unaffected and verified on the current head.
