# PF29-Canon-HDE-Users-Guide v1.0.3 — redlines — gtwpe-20261101-pf10-v14-0-5 (T-08)

## Identity

| Field | Value |
| :---- | :---- |
| Run identity | `gtwpe-20261101-pf10-v14-0-5/T-08/drain-r1` |
| Producing prompt | TW-DRAIN-10 — Prepare PF Document Redlines — 100926.1 (Notion page `3f44590a05eb8172a314fe6b958bb9ff`) |
| Preparer | The Claude Code document session Nathan started for T-08, https://claude.ai/code/session_01Q789u3KLSaV6qHFgm3m8t4 |
| Preparation date | 2026-11-02 |
| Preparation outcome | `READY` |
| Target document | PF29-Canon-HDE-Users-Guide (in-document title), v1.0.3 |
| Target file | `docs/pfcanon/PF29-Canon-HDE-Users-Guide-v1.0.3.md` on `main`, read at `e2b7427ff418ca8f08f05587c4a541308a76da56`; byte-identical at `84d6d1cad95c67788336d174dc4b8922d9bb0cb2` |
| Target bytes | git blob `6730222d2f352221ddbe140a08c260380bbf5abc`; SHA-256 `2ef3b8a7bfabbc768bf0ae1799d29449fe3ecdc37b509a03dd7292f09f0c8301`; 76,613 bytes; 1,079 lines, LF-terminated |
| Source | `docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md` (PF10-HDE-Build-Notes v14.0.5), git blob `9df074d90b59fe783c32f7cb3db25872d5dfe9d2`, SHA-256 `cea605d0475889bd9120a51947e23176ce7d2308eb5ab4503b040fd68ddf669d` |
| Selected source units | Addendum 2.1: D-1 (lines 225–276), D-2 (lines 277–344), D-3 (lines 345–396); context lines 205–224 and 491–516 |
| Ledger | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/LEDGER.md` at `142feb35144d8795f927e0c78b665ace52279064`; task T-08; rows C-01, C-02, C-03; supporting C-06 |
| Repository snapshot inspected for availability | `e2b7427ff418ca8f08f05587c4a541308a76da56` (code under `engine/` and `adapter/` is byte-identical at `84d6d1cad95c67788336d174dc4b8922d9bb0cb2`) |
| Proof log | `PF29-Canon-HDE-Users-Guide-v1.0.3.redlines.gtwpe-20261101-pf10-v14-0-5.proof-log.md`, beside this file |

## Document-control inputs for TW-APPLY-10

The baseline header (§0.1 "Header") uses these fields, in this order: Title `PF29-Canon-HDE-Users-Guide`; Version `v1.0.3`; Status `Canon`; Effective date `2026-10-26` (ISO `YYYY-MM-DD`); Last Update Gate `BN 13.8.8; HDE-CRD-0002-specification-v1.1-approved.md`; Invocation tag `INV-f2ac55d77ce9aacc`. The version scheme is `vMAJOR.MINOR.PATCH`.

Sources that justify this update, in source order: PF10-HDE-Build-Notes v14.0.5, file `PF10-HDE-Build-Notes-v14.0.5.md`. No redline below touches §0.1; the header is left to TW-APPLY-10's metadata plan. PF29 v1.0.3 has no change log, revision history or Doc-Delta section, so no history-entry redline is prepared.

## Payload convention

Every operation is `REPLACE`, with expected block occurrence 1 in the unchanged original. The OLD and NEW literals are the complete bytes between the opening fence line and the line feed that precedes the closing fence; that final line feed is not part of the literal. The fence is four backticks, and no payload line begins with a backtick fence. Labels, line numbers and notes outside the fences are not part of any literal. Each OLD block begins at a line start and ends at the end of a line, before that line's terminating line feed. Line numbers locate the original block for review only; the literal governs.

## Redlines

### RL-01

* Source items: C-01, C-02, C-03 (provenance of the new availability qualifiers)
* Change type: CONSISTENCY
* Operation: `REPLACE`
* Target document: PF29-Canon-HDE-Users-Guide
* Section path: "# **1\. Feature availability map**" > "## **1.1 Implemented local and QA surfaces**"
* Original location: §1.1, line 81 of the original
* Expected occurrence: 1 (whole original)
* Rationale: Records the repository snapshot inspected for the new current-gap statements, as PF29 §0.2 requires.

OLD:

````text
Availability below is based on bounded read-only inspection of repository snapshot `e7265a090ad0cc8de5f36de2f19481216aa3d073`, except for the statements updated for delivered HDE-CRD-0002 behavior, which were inspected at repository snapshot `0838ba08254eaefc888019df49a06aa2ae99cc6c`: the retired-route production posture in this section, the start-helper bind in §4.1, the Reader environment gate in §6.1, Aux preview band selection in §10.1, the `bg:resolve --source vendor` environment classification and production override in §11.2, §13.3, §15 Recipe F, §16, §17 and §18, and the unknown-path, CLI help and dev-route gate limits in §16. Commands are examples to run from the repository root with their stated prerequisites; no recipe was executed for this revision.
````

NEW:

````text
Availability below is based on bounded read-only inspection of repository snapshot `e7265a090ad0cc8de5f36de2f19481216aa3d073`, except for the statements updated for delivered HDE-CRD-0002 behavior, which were inspected at repository snapshot `0838ba08254eaefc888019df49a06aa2ae99cc6c`: the retired-route production posture in this section, the start-helper bind in §4.1, the Reader environment gate in §6.1, Aux preview band selection in §10.1, the `bg:resolve --source vendor` environment classification and production override in §11.2, §13.3, §15 Recipe F, §16, §17 and §18, and the unknown-path, CLI help and dev-route gate limits in §16. The statements that record current gaps against decided canon for the production vendor override scope, vendor route selection and compat route gating, in the `hdctl bg:resolve` row of this section, §11.3, §13.3, §16 and §17, were inspected at repository snapshot `e2b7427ff418ca8f08f05587c4a541308a76da56`. Commands are examples to run from the repository root with their stated prerequisites; no recipe was executed for this revision.
````

### RL-02

* Source items: C-02 (2.1 D-2, PF10 lines 277–344)
* Change type: CONSISTENCY
* Operation: `REPLACE`
* Target document: PF29-Canon-HDE-Users-Guide
* Section path: "# **1\. Feature availability map**" > "## **1.1 Implemented local and QA surfaces**"
* Original location: §1.1, line 92 of the original
* Expected occurrence: 1 (whole original)
* Rationale: The bg:resolve row restates the non-v2 fallback that D-2 supersedes; it now states the terminal-v1 route and the gap.

OLD:

````text
| hdctl bg:resolve | \[Implemented\] | Resolve BodyGraph control-flow envelope and vendor route-policy classification. Configured-v2 dry-run uses the version-neutral charts resource path and deterministic v2 ChartResult adapter mapping. Configured-v2 non-dry-run mapped-cache persistence is implemented only with explicit \--upsert, open rails, non-production-like requested and process environments, and an available sanctioned direct PostgreSQL target; failed gates refuse before the vendor request. Non-v2 configured bases preserve explicit legacy BodyGraph fallback |
````

NEW:

````text
| hdctl bg:resolve | \[Implemented\] | Resolve BodyGraph control-flow envelope and vendor route-policy classification. Configured-v2 dry-run uses the version-neutral charts resource path and deterministic v2 ChartResult adapter mapping. Configured-v2 non-dry-run mapped-cache persistence is implemented only with explicit \--upsert, open rails, non-production-like requested and process environments, and an available sanctioned direct PostgreSQL target; failed gates refuse before the vendor request. A configured base whose final path segment is exactly `v1` selects the retained legacy BodyGraph route; checked-in code still sends every other non-v2 base to that route, which canon refuses \[Current gap\] (§11.3). |
````

### RL-03

* Source items: C-02 (2.1 D-2, PF10 lines 281–298, 312–314)
* Change type: CANON_UPDATE
* Operation: `REPLACE`
* Target document: PF29-Canon-HDE-Users-Guide
* Section path: "# **11\. BodyGraph resolve and vendor ingest workflow**" > "## **11.3 Non-v2 legacy fallback \[Implemented\] \[Operator-authorized only\]**"
* Original location: §11.3, lines 712–714 of the original
* Expected occurrence: 1 (whole original)
* Rationale: D-2 supersedes §11.3: the legacy route is reached only with a terminal v1 base; checked-in code does not yet fail closed.

OLD:

````text
When the configured base is non-v2, explicit legacy BodyGraph fallback is preserved. Treat this as legacy fallback only, not v2 runtime conformance.

For non-v2 legacy fallback, persistent success must be determined by fields emitted in the JSON payload, including rows\_written, db\_rows\_after, db\_emitted\_sha256, and parity\_match where present. Do not claim rows were written by assumption.
````

NEW:

````text
Canon reaches the legacy BodyGraph route only with a configured base whose final path segment is exactly `v1`. That route is retained legacy selection, not fallback, and not v2 runtime conformance; the emitted classification label `explicit_legacy_fallback` is its existing wire value and makes no fallback claim. Every other non-v2 base, including an unversioned base, another version, a nonterminal or case-variant marker, and multiple markers, must fail with `PROVIDER_ROUTE_UNSUPPORTED` before credential projection or any external I/O. The same rule covers `bg:resolve --source vendor` and the compat chart acquisition of `showcompat --source vendor` and vendor-selecting conjunction. PF05-Canon-HDE-CLI-API-Vendor-Ref owns route selection and the configured-base boundary.

\[Current gap\] The checked-in route classifier does not yet fail closed. It reads a `v2` or `v1` marker from any path segment, case-insensitively, so a nonterminal or case-variant `v2` marker still selects the charts route, and every base without a `v2` marker, including an unversioned base, reaches the legacy BodyGraph route. No checked-in runtime code under `engine/` or `adapter/` emits `PROVIDER_ROUTE_UNSUPPORTED`. Configure a base whose final path segment is exactly `v2`, or exactly `v1` for legacy work, and do not rely on any other base shape.

For the legacy route, persistent success must be determined by fields emitted in the JSON payload, including rows\_written, db\_rows\_after, db\_emitted\_sha256, and parity\_match where present. Do not claim rows were written by assumption.
````

### RL-04

* Source items: C-02 (2.1 D-2, PF10 line 314)
* Change type: CANON_UPDATE
* Operation: `REPLACE`
* Target document: PF29-Canon-HDE-Users-Guide
* Section path: "# **13\. Production posture**" > "## **13.3 Production/open-rails vendor BodyGraph acquisition \[Operator-authorized only\]**"
* Original location: §13.3, line 838 of the original
* Expected occurrence: 1 (whole original)
* Rationale: D-2 supersedes the §13.3 sentence "With a non-v2 configured base, explicit legacy fallback may proceed".

OLD:

````text
This section summarizes production and production-like posture. Configured-v2 bg:resolve \--source vendor \--dry-run may use the version-neutral charts route and deterministic v2 ChartResult adapter under authorized open rails. With a non-v2 configured base, explicit legacy fallback may proceed under its normal rails, configuration, and emitted-payload success rules.
````

NEW:

````text
This section summarizes production and production-like posture. Configured-v2 bg:resolve \--source vendor \--dry-run may use the version-neutral charts route and deterministic v2 ChartResult adapter under authorized open rails. With a configured base whose final path segment is exactly `v1`, the retained legacy BodyGraph route may proceed under its normal rails, configuration, and emitted-payload success rules. Canon refuses every other non-v2 base, which the checked-in classifier does not yet do \[Current gap\] (§11.3).
````

### RL-05

* Source items: C-01 (2.1 D-1, PF10 lines 229–244, 265); C-02 (2.1 D-2, PF10 line 314)
* Change type: CANON_UPDATE
* Operation: `REPLACE`
* Target document: PF29-Canon-HDE-Users-Guide
* Section path: "# **13\. Production posture**" > "## **13.3 Production/open-rails vendor BodyGraph acquisition \[Operator-authorized only\]**"
* Original location: §13.3, line 848 of the original
* Expected occurrence: 1 (whole original)
* Rationale: D-1 extends the production override to showcompat and vendor-selecting conjunction (not yet delivered); the §13.3 fallback sentence follows D-2.

OLD:

````text
Persistent success for any supported non-v2 legacy fallback must be determined by emitted JSON fields, not by assumption.
````

NEW:

````text
Canon applies the same production override, with the same environment classification, initiator rule and pre-I/O audit event, to `hdctl showcompat --source vendor` and to `hdctl showcompat --conjunction` whenever the invocation selects vendor acquisition for either party, which in the checked-in CLI is any conjunction source other than `db` or `auto`. An unset or unrecognized environment then refuses with `PROVIDER_CONFIG_INVALID`. One flag authorizes at most one vendor acquisition per party, two for a pair, and no write, public Reader or Aux vendor traffic, or opening of a closed rail. Refusals use the showcompat typed error carrier with the same stable codes and exit 1, and make no outbound attempt. Supplying the flag to an invocation that selects no vendor acquisition, including `--source db`, `--source auto` and conjunction with either, is a usage error with exit 64. PF05-Canon-HDE-CLI-API-Vendor-Ref owns these rules.

\[Current gap\] The checked-in CLI accepts `--allow-prod-vendor` only on `bg:resolve` and refuses it on every `showcompat` invocation as a usage error with exit 64. Showcompat and conjunction vendor acquisition do not classify the environment, apply the override or write an audit event before the vendor request. Until that gate is delivered, no canon-conforming production-like showcompat or conjunction vendor run is available.

Persistent success on the legacy route must be determined by emitted JSON fields, not by assumption.
````

### RL-06

* Source items: C-03 (2.1 D-3, PF10 lines 349–364, 386)
* Change type: CANON_UPDATE
* Operation: `REPLACE`
* Target document: PF29-Canon-HDE-Users-Guide
* Section path: "# **16\. Known limitations and nonclaims**"
* Original location: §16, line 963 of the original
* Expected occurrence: 1 (whole original)
* Rationale: D-3 makes the §16 "POST /api/compat/v1 is not production-public" line gain the non-production refusal; the checked-in guard does not yet return it.
* Note: the OLD and NEW literals each end with two space characters, as the original line does.

OLD:

````text
* POST /api/compat/v1 is not production-public. Current code returns 404 when APP\_ENV resolves to prod, production, or live, or when APP\_ENV is empty and ENGINE\_ENV resolves to one of those values.  
````

NEW:

````text
* POST /api/compat/v1 is not production-public. Current code returns 404 when APP\_ENV resolves to prod, production, or live, or when APP\_ENV is empty and ENGINE\_ENV resolves to one of those values. Canon classifies the compat namespace, `/api/compat/v1` and its descendants, as a dev/admin-only surface: outside production-like posture it is served only when APP\_ENV is exactly `dev`, `test` or `local`, with no trimming or case-folding, and any other value, including an unset or empty APP\_ENV, refuses with `ERR_WRITER_FORBIDDEN` (403) before any compat work; ENGINE\_ENV never admits it. \[Current gap\] The checked-in guard refuses only production-like posture and treats unset APP\_ENV and ENGINE\_ENV as dev, so it still serves the route when APP\_ENV is unset or empty and ENGINE\_ENV is not production-like, when APP\_ENV is a case or whitespace variant of `dev`, `test` or `local`, and when it is `staging` or another unrecognized value. Run local HTTP compat with APP\_ENV=dev, as the §4.1 harness does. No credential is required while the surface stays dev/admin-only; serving it in any other environment needs a later decision, which PF04-Canon-HDE-Governance and PF05-Canon-HDE-CLI-API-Vendor-Ref own.  
````

### RL-07

* Source items: C-02 (2.1 D-2, PF10 line 314)
* Change type: CANON_UPDATE
* Operation: `REPLACE`
* Target document: PF29-Canon-HDE-Users-Guide
* Section path: "# **16\. Known limitations and nonclaims**"
* Original location: §16, line 969 of the original
* Expected occurrence: 1 (whole original)
* Rationale: D-2 supersedes the §16 sentence "For non-v2 configured bases, explicit legacy BodyGraph fallback is preserved".
* Note: the OLD and NEW literals each end with two space characters, as the original line does.

OLD:

````text
* Current configured-v2 bg:resolve \--source vendor \--dry-run may use the version-neutral charts route and deterministic v2 ChartResult adapter. For non-v2 configured bases, explicit legacy BodyGraph fallback is preserved.  
````

NEW:

````text
* Current configured-v2 bg:resolve \--source vendor \--dry-run may use the version-neutral charts route and deterministic v2 ChartResult adapter. A configured base whose final path segment is exactly `v1` selects the retained legacy BodyGraph route, which is legacy selection, not fallback. Canon gives no other non-v2 base a route; the checked-in classifier still sends one to the legacy route \[Current gap\] (§11.3).  
````

### RL-08

* Source items: C-01 (2.1 D-1, PF10 lines 229–237, 265)
* Change type: CANON_UPDATE
* Operation: `REPLACE`
* Target document: PF29-Canon-HDE-Users-Guide
* Section path: "# **16\. Known limitations and nonclaims**"
* Original location: §16, line 985 of the original
* Expected occurrence: 1 (whole original)
* Rationale: D-1 drains into the §16 production-override limit, with the current gap.

OLD:

````text
* `--allow-prod-vendor <AUTHORIZATION_REF>` is implemented, for `hdctl bg:resolve --source vendor` only. A production-like environment requires it for any vendor access and a recognized non-production environment refuses it; only an authenticated human initiator supplies it. It permits one bounded vendor read and authorizes no `--upsert`, production write, public Reader or Aux vendor traffic, or opening of a closed rail (§11.2, §13.3). PF05-Canon-HDE-CLI-API-Vendor-Ref owns the flag, environment classification, evaluation order and audit contract. The checked-in implementation does not prove a live or deployed override run.
````

NEW:

````text
* `--allow-prod-vendor <AUTHORIZATION_REF>` is implemented, for `hdctl bg:resolve --source vendor` only. A production-like environment requires it for any vendor access and a recognized non-production environment refuses it; only an authenticated human initiator supplies it. It permits one bounded vendor read and authorizes no `--upsert`, production write, public Reader or Aux vendor traffic, or opening of a closed rail (§11.2, §13.3). Canon extends the same override to `hdctl showcompat --source vendor` and to vendor-selecting `hdctl showcompat --conjunction`, with at most one vendor acquisition per party; the checked-in CLI refuses the flag on `showcompat` as a usage error, and its vendor acquisition applies no override \[Current gap\] (§13.3). PF05-Canon-HDE-CLI-API-Vendor-Ref owns the flag, environment classification, evaluation order and audit contract. The checked-in implementation does not prove a live or deployed override run.
````

### RL-09

* Source items: C-03 (2.1 D-3, PF10 lines 351–354, 386)
* Change type: CANON_UPDATE
* Operation: `REPLACE`
* Target document: PF29-Canon-HDE-Users-Guide
* Section path: "# **17\. Troubleshooting**"
* Original location: §17, line 998 of the original
* Expected occurrence: 1 (whole original)
* Rationale: D-3 makes the troubleshooting row "HTTP 404 from POST /api/compat/v1 in prod" gain the non-production refusal.

OLD:

````text
| HTTP 404 from POST /api/compat/v1 in prod | Expected current production block. | Use dev/QA HTTP compat locally or an internal CLI/server-side production workflow. |
````

NEW:

````text
| HTTP 404 from POST /api/compat/v1 in prod | Expected current production block. Canon also refuses the route outside production with `ERR_WRITER_FORBIDDEN` (403) unless APP\_ENV is exactly `dev`, `test` or `local`; the checked-in guard does not yet return that refusal \[Current gap\] (§16). | Use dev/QA HTTP compat locally with APP\_ENV=dev, or an internal CLI/server-side production workflow. |
````

### RL-10

* Source items: C-01 (2.1 D-1, PF10 lines 242–244, 265)
* Change type: CANON_UPDATE
* Operation: `REPLACE`
* Target document: PF29-Canon-HDE-Users-Guide
* Section path: "# **17\. Troubleshooting**"
* Original location: §17, line 1006 of the original
* Expected occurrence: 1 (whole original)
* Rationale: D-1 drains into the troubleshooting row for PROVIDER_PROD_OVERRIDE_REQUIRED, PROVIDER_PROD_OVERRIDE_INVALID and PROVIDER_AUDIT_UNAVAILABLE, with the current gap.

OLD:

````text
| PROVIDER\_PROD\_OVERRIDE\_REQUIRED, PROVIDER\_PROD\_OVERRIDE\_INVALID, or PROVIDER\_AUDIT\_UNAVAILABLE | bg:resolve \--source vendor ran in a production-like environment without \--allow-prod-vendor, supplied the flag in a recognized non-production environment, or could not resolve the authenticated actor or write the pre-I/O audit event. | Do not change the environment value to avoid the refusal. Only an authenticated human initiator supplies the flag (§13.3); for non-production work, use §11.2 without it. |
````

NEW:

````text
| PROVIDER\_PROD\_OVERRIDE\_REQUIRED, PROVIDER\_PROD\_OVERRIDE\_INVALID, or PROVIDER\_AUDIT\_UNAVAILABLE | bg:resolve \--source vendor ran in a production-like environment without \--allow-prod-vendor, supplied the flag in a recognized non-production environment, or could not resolve the authenticated actor or write the pre-I/O audit event. Canon gives `showcompat --source vendor` and vendor-selecting conjunction the same refusals, on the showcompat error carrier with exit 1; the checked-in `showcompat` does not yet emit them and refuses the flag as a usage error with exit 64 \[Current gap\] (§13.3). | Do not change the environment value to avoid the refusal. Only an authenticated human initiator supplies the flag (§13.3); for non-production work, use §11.2 without it. No canon-conforming production-like showcompat or conjunction vendor run is available until that gate is delivered (§13.3). |
````

END OF REDLINES
