# HDE-EPIC035 OPS-01 Result Summary

Result classification: `vendor_error_class_observed`

OPS-01 evidence produced: yes, as a bounded open-rails HD Engine CLI BodyGraph vendor/geocode dry-run observation.

Final app result: `vendor_error_class`

Executed command: `SAFE_MODE=0 ALLOW_NETWORK=1 LC_ALL=C LANG=C TZ=UTC hdctl bg:resolve --user qa-user --source vendor --birthdate 1990-01-01 --birthtime 12:00 --location "Paris, FR" --dry-run`.

Observed safe result: the command exited `1` and emitted JSON with `status=error`, `error.code=PROVIDER_NOT_FOUND`, and `details.status=404`. The keys-only retry log recorded `route=vendor.hdapi.post:/bodygraphs`, `rails_state=open_exception`, `outcome=failure`, `error_class=4xx`, `error_code=PROVIDER_NOT_FOUND`, and `status=404`.

No-version rerun: overriding `HD_API_BASE_URL` to `https://api.humandesignapi.nl` shaped the request to path suffix `/bodygraphs` with `HD-Api-Key` and `HD-Geocode-Key` present in-memory and `Authorization` absent. The rerun also exited `1` with `status=error`, `error.code=PROVIDER_NOT_FOUND`, and `details.status=404`.

Diagnosis: configured-base/resource mismatch for the current runnable target remains the likely cause, now narrowed further. The `hdctl bg:resolve` path uses the legacy BodyGraph resource `bodygraphs`; local request-shaping code appends version-neutral resources directly to `HD_API_BASE_URL`. The original configured v2 base shaped `/v2/bodygraphs` and failed with 404. The no-version override shaped `/bodygraphs` and also failed with 404. This points away from missing auth/geokey config and toward the legacy BodyGraph route requiring its legacy versioned base, likely `/v1/bodygraphs`, while v2 bases/routes belong to chart-family calls rather than `bg:resolve`.

Geokey behavior supportable from redacted evidence: partially bounded only. `GEO_API_KEY`, `HD_API_KEY`, and `HD_API_BASE_URL` were present in the operator shell as redacted presence-only values, and the command used a geocode-required legacy BodyGraph path. Retained logs did not expose redacted request header shape, so this record does not prove `HD-Geocode-Key: <redacted>` by header observation.

PR-03 binding posture: PR-03 may bind this OPS output as retained evidence of an open-rails HD Engine BodyGraph vendor error class if desired. It should not bind this as conclusive v2 chart auth/geokey header-shape proof or v2 ChartResult / ChartSimpleResult normalization proof.

Required deliverables: D1 through D7 were created under `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/`.

Nonclaims:

- no QA PASS
- no PF09 status movement
- no epic closeout
- no full HumanDesignAPI v2 runtime conformance
- no public Reader change
- no new public route
- no app-side vendor credential ownership
- no raw payload persistence
- no AI scope
