---
artifact_type: PR_WORK_UNIT_INSTRUCTION
artifact_id: HDE-CRD-0002-WU-PR-04-PR-INSTRUCTION
artifact_version: "1.0"
artifact_state: INSTRUCTION_READY
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-04
work_unit_title: "Provider gate and Aux preview (PR; Fermentation; S08, S14)"
AUTHORING_CONTEXT: APPROVED_BASE_WITH_OVERLAYS
immutable_approved_base: Specification v1.1 (approved) → Implementation Plan v1.1 + IA-30 review v1.1 (approved)
applicable_pf10_overlays: PF10 addendum 2.3 (reviewer chain without the Codex security review); addendum 2.6 ("Affected surfaces", Dependencies and Downstream work, for this unit: refresh against the 22-path label roster; updater-consumer, label-timing and stale-label rules; the step-3b order and restart point); addendum 2.7 AD-5 ("New base" for this unit, the order and restart rules) and "Affected surfaces / Downstream" ("WU-PR-04 and WU-PR-05 refresh from the new release_id"). Addendum 2.5 carries LR-O1 to LR-O3, which 2.6 applies to the 22-path roster. Addenda 2.2 and 2.4 have no item for this unit (§15). Addendum 2.1 governs §19 only
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
SPECIFICATION_REF: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (v1.1, SPECIFICATION_APPROVED, "ASK OK."; blob c4802a5a7fa3)
IMPLEMENTATION_PLAN_REF: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (v1.1; blob abffa2ccbd44; approved by PLAN_REVIEW_REF)
PLAN_REVIEW_REF: docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (v1.1, IA-30 INITIAL_APPROVE; blob 0cc0276524b2)
IMPLEMENTATION_AUDIT_REF: docs/ephemeral/HDE-CRD-0002-implementation-audit-v1.0.md (v1.0, AUDIT_COMPLETE; blob b39ac9f276db) — lineage; §5 re-measures its S08 and S14 facts at the current baseline
predecessor_unit_acceptance: WU-PR-01 docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-work-unit-lineage-review-v2.0.md (ACCEPT; PF10 addendum 2.4); WU-PR-02 docs/ephemeral/HDE-CRD-0002-WU-PR-02-pr-work-unit-lineage-review-v2.0.md (ACCEPT; PF10 addendum 2.5); WU-PR-03 docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-work-unit-lineage-review-v1.0.md (ACCEPT across #643 and #646; blob 7c9a00bd0de2; landed on main at 39afdc6, #648)
structure_precedent: docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-instruction-v1.0.md (blob 74e8f158b48d)
refresh_record_read: docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-implementation-result-v2.0.md (blob 5d8a84c7ab00; §8, the converged refresh that set the current release_id) and its PR-35 successor docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-implementation-result-v2.1.md (blob ebc70d08ff98)
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.8.md (v13.5.8; blob 3c13456a576c; 103,474 bytes; sha256 94573d06200935fdd29c71b04bafd2035c69b9d0537d1e4f69d9e7f02fe27eb6). Read for this unit: addenda 2.6 and 2.7 in full; 2.3 in full; 2.5 "Retained decisions and requirements" and "Epic, task, and status effects"; 2.1, 2.2 and 2.4 for applicability (rules, binding requirements and downstream items). The document was read in full earlier in this IA lineage (WU-PR-03 lineage review)
pf10_addendum_paths: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.8.md §2.3, §2.5, §2.6, §2.7; §2.1 for §19
pf10_addendum_created: none (PR-10 is not a qualifying approval prompt)
issuer: the continuing whole-change Implementation Agent (IA) for HDE-CRD-0002, session https://claude.ai/code/session_01CCKsYD2yX5WgU3biWKb59j
prompt: PR-10 — Create PR Work-Unit Instructions — 100926.1 (https://app.notion.com/p/3f44590a05eb815d97d5f3930c7d3e8a; page state as of 2026-10-12T02:29:33.739Z; read in full in this invocation)
prompt_release: GCFPE-20261009.1 / 100926.1
created_at: 2026-10-18T09:58:27Z
repository_baseline: origin/main 39afdc663034a5432f28924b8c308d32614f3c34 (#648, the WU-PR-03 lineage review); docs/pfcanon/ last changed at 79eac95; every repository fact in §5 measured there
receiver: dedicated HDE-CRD-0002 WU-PR-04 PR engineering session (session_disposition INITIAL_DEDICATED_ASSIGNMENT; role_session_ref NOT_YET_ASSIGNED, assigned by Nathan / Product Owner at launch)
next_prompt: PR-20 — Create Detailed PR Implementation Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb819fbea5dcd966a750ba)
canon_conflict_register: CR-1 to CR-8 carried, all decided; no new entry (§16)
---

# HDE-CRD-0002 WU-PR-04 — PR Work-Unit Instruction v1.0

## 1. Result and authority boundary

**INSTRUCTION_READY.** This is the one complete, self-contained PR instruction for work unit WU-PR-04 of HDE-CRD-0002. The whole-change IA issues it from the approved Implementation Plan v1.1. A dedicated PR-20 session can plan the unit from this instruction and the linked current repository and canon, without reconstructing upstream intent (§17).

It does not:
- author the detailed per-file plan (PR-20's output);
- authorize implementation, a commit, a pull request, a merge, Ops, QA, acceptance or closure. Only Nathan / Product Owner's `PR Implementation Proceed` (PR-30) for the exact PR-20 plan authorizes implementation, and only Nathan merges;
- authorize any live use of `--allow-prod-vendor`. The flag is implemented and tested here with no live vendor call; its first live use belongs to the QA Plan under the override-initiator constraint;
- change canon or create a PF10 addendum.

## 2. Identity and lineage

| Item | Identity |
| :- | :- |
| Change | CRD HDE-CRD-0002 |
| Work unit | WU-PR-04 (Plan v1.1 §7 heading "WU-PR-04 — Provider gate and Aux preview (PR; Fermentation)") |
| Requirements | S08, S14; engineering choice EC-7; interfaces IF-1, IF-2; the same-version manifest refresh and convergence its member changes force |
| Approved base | Specification v1.1 → Plan v1.1 + review v1.1 (refs above). Review v1.1 carries review v1.0's note N4 ("override actor principal and sink key") to this unit's PR-20 plan |
| Overlays | PF10 addenda 2.3, 2.6 and 2.7 AD-5 as named in the header |
| Upstream units | WU-PR-01, WU-PR-02 and WU-PR-03, all accepted |
| Phase | Fermentation |
| Live QA class (Specification table; Plan §6) | S08: functional-feature; S14: functional-feature, with the mandatory live vendor call |

## 3. Unit selection and dependency state

- **Plan approval.** Isis approved exactly Plan v1.1 (review v1.1, INITIAL_APPROVE).
- **Unit type.** PR unit.
- **Dependency state: ready.**
  - Plan v1.1 §7: "Fourth; after WU-PR-01 and WU-PR-03."
  - WU-PR-01 is accepted (addendum 2.4). It registered `tests/bodygraph/test_resolver_vendor.py` in a lane.
  - WU-PR-03 is accepted (lineage review v1.0, on `main` at `39afdc6`). It set the refresh base this unit starts from (§5.9).
  - WU-PR-02 is accepted (addendum 2.5); its label model governs the refresh.
  - AQ-1 gates only WU-PR-07's merge. No QA Guide, QA Plan or Ops receipt is a prerequisite.
- **Order.** WU-PR-01 → WU-PR-02 → WU-PR-03 → **WU-PR-04** → WU-PR-05 → WU-PR-06 → WU-PR-07 → WU-PR-08 → WU-DOC-01 → WU-OPS-01 (Plan §7).
- **Downstream dependents** (contracts in §8):
  - WU-PR-05 takes this unit's refreshed `release_id` as its refresh base, reviews the override code under S19, and receives the observations in §15.
  - WU-PR-06 reads the classifier registrations this unit adds.
  - WU-PR-08 cuts `1.4.0` after this unit.
  - WU-DOC-01 owns the README, AGENTS and canon-adjacent documentation this unit leaves stale.
  - The QA Plan designs the Live QA vendor call on this unit's override contract.

## 4. Required behavior

**Acceptance intents**, verbatim from the approved Specification (Requirements table):

| ID | Requirement | Acceptance intent |
| :- | :- | :- |
| S08 | Apply `aux-preview --band` when the band comes from the pair file | "The band flag takes effect for pair-file input" |
| S14 | Implement the production vendor override as CLI/API/Vendor Ref §7.1.11a to §7.1.11f state it | "`--allow-prod-vendor` behaves as §7.1.11 specifies, including environment classification, rails, evaluation order, error carrier, authorized initiator and audit; closed rails still refuse first, and public Reader or Aux traffic never reaches the vendor" |

**Specification constraints that bind this unit**, verbatim:
- **Vendor override.** "S14 keeps generic SAFE rails first: the override never opens a closed rail and never lets public Reader or Aux traffic call the vendor (CLI/API/Vendor Ref §7.1.11)."
- **Override initiator.** "Any live invocation of `--allow-prod-vendor`, in QA or elsewhere, is initiated only by an authenticated human Product Owner or a human operations executor the Product Owner explicitly delegates in the referenced approved work item; an AI agent, CI job, application request or unauthenticated shell cannot self-authorize (CLI/API/Vendor Ref §7.1.11e)."
- **Live QA.** "Live QA steps are bounded, Product Owner-authorized, synthetic-data-only, secret-safe and subject to request limits and stop checks …"
- **Release members.** The observed loci of S08 and S14 (`engine/cli/main.py`: `aux-preview --band`, the `bg:resolve` parser; and `engine/bodygraph/resolver.py`) are release members.
- **Exclusions bullet 5.** "As implementation work: no deployment, no production configuration change, and no live vendor call made by an implementation work unit."

**Interfaces**, verbatim from Plan v1.1 §5:
- **IF-1.** "`hdctl bg:resolve --source vendor --allow-prod-vendor <AUTHORIZATION_REF>` — One value-bearing flag, accepted only with `--source vendor`; value `^[A-Za-z0-9][A-Za-z0-9._:/-]{0,127}$`; empty, malformed, duplicated or inapplicable use is a CLI usage error (exit 64). Environment: `APP_ENV` canonical, `ENGINE_ENV` alias when `APP_ENV` blank; production-like `{prod, production, live}`, non-production `{dev, test, local, stage, staging}`; conflict or unknown → `PROVIDER_CONFIG_INVALID` before I/O. Matrix and evaluation order exactly as HDE-CLI-API-Vendor-Ref §7.1.11c–d; policy refusals `status="error"` envelope with one typed code, exit 1, `outbound_attempted: false`."
- **IF-2.** "Append-only, locally durable JSONL, one event per invocation reaching override evaluation, fields exactly `schema_version`, `event` (`vendor_prod_override`), `occurred_at`, `correlation_id`, `actor_principal`, `authorization_ref`, `command` (`bg:resolve`), `source` (`vendor`), `environment`, `safe_mode_open`, `network_open`, `route_family`, `resource_path`, `outcome` (`refused`/`allowed`/`failed`/`completed`), `error_code`, `outbound_attempted`; no subject, URL, header, token or raw provider data; CR/LF-sanitized; sink path from one operator environment key (name fixed at PR-20; Glow Infrastructure doc-delta candidate) with a default under the operator's state directory; persistence failure → `PROVIDER_AUDIT_UNAVAILABLE`."

**Engineering choice**, verbatim from Audit §7.1 as carried by the Plan:
- **EC-7 (S14):** "Audit sink: one local append-only JSONL file; path from one new operator environment key with a default under the operator's state directory; actor principal from the OS user of the executing shell; absence of either refuses with `PROVIDER_AUDIT_UNAVAILABLE`."

### 4.1 Canon §7.1.11, clause by clause (HDE-CLI-API-Vendor-Ref §7.1.11, read in full)

| Canon clause | What it requires of this unit | Where it lands |
| :- | :- | :- |
| §7.1.11 preamble, "Closed SAFE or network rails refuse before every vendor decision and perform no credential loading, DNS, socket, or HTTP activity" | rails stay step 3, unchanged | ID-1, ID-7 |
| §7.1.11 preamble, "never opens either generic rail and never permits public Reader or Aux traffic to call the vendor" | no rail opened; no HTTP surface gains a vendor path | ID-1; §5.3 |
| §7.1.11a, one value-bearing flag, `bg:resolve --source vendor` only; no short spelling, alias, negated form, environment-variable form or default | parser and pre-scan | ID-1 |
| §7.1.11a, the pattern, 1–128 ASCII characters; empty, control character, whitespace, outside the allow-list, missing value, duplicate all invalid; "must never contain a token or secret" | step-1 validation | ID-1 |
| §7.1.11b, the six normalization and selection bullets; "Never treat an unknown label as non-production"; "The flag never changes environment classification" | step 4 | ID-2 |
| §7.1.11c, the eight-row matrix; "The production flag substitutes for neither value" | step 5 | ID-4; §10 M-1 to M-8 |
| §7.1.11d, the seven-step order "before client construction, secret loading, DNS, sockets, or HTTP" | CLI steps 1–2, resolver steps 3–7 | ID-1 |
| §7.1.11d, "only one bounded admin vendor HTTP opportunity"; not "public Reader/Aux vendor traffic, production `--upsert`, any production database write, bypass of `PROVIDER_WRITE_UNSUPPORTED`, a route or version, credentials, expanded retries, or a no-network dry run"; "A production dry run that contacts the vendor still requires the flag" | read-only override; retries unchanged; dry run gated | ID-3 |
| §7.1.11e, usage carrier exit 64; policy refusals in the `status="error"` resolver envelope, "one stable typed code and a non-sensitive message", exit 1; "Every refusal has outbound-attempt count `0`" | carriers | ID-1, ID-7 |
| §7.1.11e, authorized initiator; "Actor identity comes from the authenticated execution environment or control plane, never a free-form `--operator` value. If a stable authenticated actor identity is unavailable, refuse the operation." The reference "is not authentication" | actor resolution | ID-5 |
| §7.1.11f, one append-only, locally durable, keys-only event before I/O for "every production-like invocation that reaches semantic override evaluation"; syntax failures stay with the process/control-plane audit | event scope | ID-4 |
| §7.1.11f, the 15-row field table (16 keys: one row names `route_family` and `resource_path`) | record shape | ID-4, ID-6 |
| §7.1.11f, the exclusions list; CR/LF and delimiter sanitization; "The flag value, actor, and policy state never appear in an exception string or raw diagnostic outside the governed audit record" | redaction | ID-6, ID-7 |
| §7.1.11f, "Failure to persist the pre-I/O event is `PROVIDER_AUDIT_UNAVAILABLE` and blocks the call. A post-I/O completion event may update the same correlation record or append a second state event" | persistence and the state event | ID-4 |
| §7.1.11 "Required-Now implementation gap (DD-04; held)" paragraph | stale after this unit lands; doc-delta candidate, not edited | §15 |

Supporting canon, read: HDE Governance §3.1 "SAFE rails default ON", sections "Public traffic (Reader/Aux)" ("Prod public surfaces … must serve requests **without** vendor HTTP"), "Admin ops windows (vendor override)" ("Vendor override is driven by CLI flags"; when enabled, the bounded-retry, typed-429, Retry-After and no-payload-logging tokens apply) and "Governance stance" (`BG_VENDOR_CALLS_DISABLED_IN_PROD_OK` scopes to public traffic). HDE-CLI-API-Vendor-Ref §4.6 ("`auto` — DB-only; vendor fallback is prohibited"; "`bg:resolve --source=vendor --upsert` **must not** be used in prod"). HDE Mechanics Guide §17.10.3 "BodyGraph resolver & vendor ingest (prod QA)" ("Under rails CLOSED, any bg:resolve --source=vendor invocation MUST return a typed refusal and MUST NOT perform outbound HTTP"; `--upsert` not in production) and §22 "SAFE Rails and Provider Gate" ("Refuse outbound/vendor work unless explicitly enabled"; "Logging. Keys-only; no payloads, header values, or secrets").

### 4.2 Binding IA decisions (canon-conforming readings; HDE Governance §9.1.2)

**ID-1. Gate placement, order and scope.**
- **Scope.** The gate applies to `hdctl bg:resolve --source vendor`, through `resolve_bodygraph(source="vendor")` → `_resolve_vendor`. It is not placed in `_resolve_vendor_v2_chart` or `_acquire_dry_run`. Those functions are shared with `hdctl showcompat --source vendor` and the dev conjunction routes (§5.3), which §7.1.11a does not cover. Their behavior and bytes are unchanged (OBS-W4-1, §15).
- **CLI, steps 1–2** (`engine/cli/main.py`):
  - a pre-scan of `argv` counts every occurrence of the option, in both the `--allow-prod-vendor VALUE` and `--allow-prod-vendor=VALUE` spellings, because argparse keeps the last value silently. Two or more occurrences are a usage error;
  - the value must match §7.1.11a's pattern; a missing or empty value is a usage error;
  - the option with `--source db`, `--source auto` or no `--source` (the default is `auto`) is a usage error;
  - each usage error: exit 64, stdout empty, one short stderr line or synopsis that may name the option and never echoes the value. argparse's own "invalid value: 'X'" message echoes it, so it must not be used for this option.
- **Existing CLI checks stay.** `MISSING_VENDOR_INPUT` (exit 64) for an incomplete birth tuple keeps its place before the resolver. PR-20 fixes and records the order among the step-1/2 usage errors and `MISSING_VENDOR_INPUT`. All of them come before step 3.
- **Resolver, steps 3–7** (`engine/bodygraph/resolver.py`), in this order:
  1. step 3: the existing SAFE and network refusals, bytes unchanged;
  2. step 4: environment classification (ID-2);
  3. step 5: the matrix (ID-4);
  4. step 6: actor resolution and the durable pre-I/O event (ID-4, ID-5, ID-6);
  5. step 7: the existing gates in their current order (route policy and base-URL classification, input resolution, identity, the write-intent and write guards, client construction and fetch), plus ID-3's production write refusal.
- **Library interface.** The resolver receives the reference through one explicit keyword argument whose default means "absent". PR-20 names it. A library caller passing a reference that fails §7.1.11a's pattern is refused with zero I/O. PR-20 names the code and tests it.
- **Proof of order.** No client construction, credential read, DNS, socket or HTTP happens before step 7 on any path.

**ID-2. Environment classification (step 4).**
- **The rule.** Implement §7.1.11b exactly in one function: trim ASCII whitespace and lowercase; blank or all-whitespace counts as absent; nonblank `APP_ENV` and `ENGINE_ENV` must be equal or the result is `PROVIDER_CONFIG_INVALID`; use `APP_ENV`, else `ENGINE_ENV`; absent or outside both allow-lists → `PROVIDER_CONFIG_INVALID` before I/O.
- **Where the values come from.** Classify from the same merged view the vendor configuration uses (`_vendor_config_env`: process environment overlaid by the caller's mapping). For the CLI that is the process environment.
- **No downgrade.** A production-like `APP_ENV` or `ENGINE_ENV` in the process environment is never downgraded to non-production by a caller-supplied mapping. This mirrors the existing v2 write guard, which already reads both views (resolver lines 246–248). PR-20 states the exact rule, including conflicting values across the two views, and tests it.
- **Effect on non-production.** This step applies to every open-rails `--source vendor` invocation. An unset or unknown environment now refuses where it proceeded before. PR-20 inventories the tests and tools that rely on the process `APP_ENV=dev` of the closed-rails profile (§5.7, §5.8).
- **Unchanged.** The v2 write guard's own reading stays unchanged as an additional check. The `ENGINE_ENV` alias applies to this gate only (§7.1.11b).

**ID-3. In a production-like environment the override permits a vendor read only.**
- **The rule.** When step 4 classifies the environment as production-like, every write path refuses `PROVIDER_WRITE_UNSUPPORTED` before database construction and before vendor I/O. `PROVIDER_WRITE_UNSUPPORTED` is the existing typed code for production-like persistence refusal (HDE-CLI-API-Vendor-Ref §4.6).
- **The v2 mapped-cache path.** The existing guard (resolver lines 236–252) stays and also refuses whenever step 4 classified the environment as production-like.
- **The legacy v1 ingest path.** `ingest_vendor_bodygraph` with `dry_run=False` writes database rows and has no production guard today (§5.4). It gains this refusal in the resolver before the call.
- **Why.** §7.1.11d says the flag does not authorize "production `--upsert`, any production database write, bypass of `PROVIDER_WRITE_UNSUPPORTED`". Without this rule, a valid flag on a legacy base without `--dry-run` would write in production.
- **Unchanged.** A production dry run that contacts the vendor still needs the flag (step 5). Non-production write behavior is unchanged. Retry and timeout pins are unchanged.

**ID-4. Matrix, event scope and outcomes (steps 5–7).**
- **(a) Code precedence follows the matrix row.**
  - Production-like with the flag absent → `PROVIDER_PROD_OVERRIDE_REQUIRED`, even when its event cannot be persisted. Row 3 has no audit condition; row 5 applies only to a valid flag.
  - Production-like with a valid flag, but actor or sink unavailable → `PROVIDER_AUDIT_UNAVAILABLE`.
  - Recognized non-production with the flag present → `PROVIDER_PROD_OVERRIDE_INVALID`.
  - Recognized non-production with the flag absent → current behavior.
- **(b) Which invocations write an application event.** Only production-like invocations that reach step 5. None for:
  - step-1/2 usage errors (§7.1.11f second sentence);
  - closed rails;
  - step-4 `PROVIDER_CONFIG_INVALID`;
  - non-production invocations, including `PROVIDER_PROD_OVERRIDE_INVALID`. The `environment` field is "normalized production alias".
- **(c) Flag absent.** The event is written when actor and sink are available, with:
  - `authorization_ref` null, `outcome` `refused`, `error_code` `PROVIDER_PROD_OVERRIDE_REQUIRED`;
  - `outbound_attempted` false, route fields null.

  If either is unavailable, no event is written and the result is still row 3's.
- **(d) Valid flag.** The pre-I/O event has:
  - `outcome` `allowed`, `error_code` null;
  - `route_family` and `resource_path` null (route classification is step 7);
  - `outbound_attempted` false.

  It is durable (append, flush, `fsync`) before step 7 starts. A failure is `PROVIDER_AUDIT_UNAVAILABLE`, and the call stops.
- **(e) State event after step 7.** After step 7 ends, one state event is appended with the same `correlation_id`:
  - `refused`: a step-7 refusal before I/O; its code; `outbound_attempted` false;
  - `completed`: success; `outbound_attempted` true;
  - `failed`: a vendor error after an attempt; its code; `outbound_attempted` true.

  Route fields carry the allow-listed labels route classification produced. Failure to append this event does not change the command's result and prints nothing. Basis: IF-2 lists the `failed` and `completed` outcomes, which only this event uses; §7.1.11f permits appending "a second state event".
- **(f) The word "invalid" in §7.1.11f's list** ("absent, invalid, refused, or allowed") has no separately reachable case: a syntactically invalid value stops at step 1 with no application event, as §7.1.11f's second sentence and the matrix's usage-error row require.

**ID-5. Actor principal (§7.1.11e; EC-7; N4).**
- **Source.** The actor comes from the process's own credentials: the effective user ID, resolved to an account name through the system user database.
- **Never from** `USER`, `LOGNAME`, `LNAME`, `USERNAME` or any other caller-settable environment value, from a CLI option, or from the reference.
- **Unavailable.** If the lookup fails, the actor is unavailable and ID-4 applies. PR-20 decides and records whether a numeric UID without an account name counts as a stable identity.
- **Not decided here.** Whether the Live QA venue yields a stable authenticated human principal is a QA Plan question (Plan R-3; review v1.0 N4), not this unit's.
- **Sanitized.** The principal is sanitized like every other field (ID-6).

**ID-6. Audit record and sink (IF-2; EC-7).**
- **New module.** `engine/bodygraph/vendor_audit.py`, imported by the resolver as `vendor_client.py` is. It is not a release member (§5.9).
- **Sink path.**
  - It comes from one new operator environment key, whose name PR-20 fixes and records. Existing HD Engine keys in Glow Infrastructure §8.1 use the `HDE_` prefix; that is an observation, not a binding rule.
  - The default is under the operator's state directory; PR-20 fixes the rule (for example `$XDG_STATE_HOME`, else `~/.local/state`, plus a sub-path).
  - The resolved path is absolute and never inside the repository checkout.
- **Writing.**
  - One canonical JSON object per line: UTF-8, sorted keys, compact, one LF.
  - Opened for append; created owner-only.
  - Each event is flushed and `fsync`ed before the next step.
  - Creating a missing parent directory, and the refusal when that fails, are PR-20's to fix and test.
- **Fields.** Exactly the 16 keys IF-2 lists, which are the rows of §7.1.11f's 15-row table (one row names both `route_family` and `resource_path`).
  - `schema_version`: a constant in the module that PR-20 names. No new file under `schemas/`; if canon is found to require one, that is a finding (§14).
  - `occurred_at`: UTC, from an injectable clock. Canon names a "governed clock boundary" that neither canon nor the repository defines (OBS-W4-4).
  - `correlation_id`: generated by the runtime through an injectable generator, never from input.
- **Excluded content.** Nothing from §7.1.11f's exclusion list: `--user`, birth fields, location, coordinates, bodies, the configured URL, header values, keys, database identifiers, raw provider messages. Every string field is sanitized against CR, LF, other control characters and delimiter injection.
- **Tests.** Every test, and every tool run by this unit, uses a temporary sink. The repository gains no sink file.

**ID-7. Output bytes and redaction.**
- **Unchanged envelopes.** The stdout envelopes of every existing path stay byte-identical: closed-rails refusals, step-7 refusals and success envelopes, in production and non-production alike. A frozen EPIC037 capture embeds the closed-rails `PROVIDER_REFUSED` envelope byte for byte (§5.8).
- **New refusals** (steps 4–6, `PROVIDER_CONFIG_INVALID`, `PROVIDER_PROD_OVERRIDE_REQUIRED`, `PROVIDER_PROD_OVERRIDE_INVALID`, `PROVIDER_AUDIT_UNAVAILABLE`) use the existing envelope shape (`status`, `error` with `code` and a fixed non-sensitive `message`, `resolver`), exit 1. They carry `outbound_attempted: false` at one place PR-20 fixes and records (IF-1).
- **Never emitted.** The reference, actor, correlation ID, sink path, timestamp and override state never appear on stdout or stderr, in an exception message or in a log.
- **Determinism.** Stdout keeps two-run identity (HDE-CLI-API-Vendor-Ref §3.3 "Determinism pins").
- **Emitter.** `bg_resolve` keeps emitting only through `emitter.emit_public`, which the CLI emitter-symbol proof records.

**ID-8. Existing tests and evidence tools that assert a later guard.**
- **The rule.** Each production-like scenario that today asserts a later guard keeps asserting that guard, by supplying a valid reference, a test actor and a temporary sink. No expected code is weakened and no assertion is removed.
- **Known cases at the baseline** (§5.7, §5.8):
  - `tests/bodygraph/test_bg_resolve_v2_mapped_cache.py`: `test_production_like_refuses_before_vendor_and_db` (three parameters) and `test_process_production_environment_cannot_be_overridden_for_database_write`;
  - `tools/evidence/generate_v2_mapped_cache_evidence.py`, its `production` scenario.
- **Why the generator matters.** Its predicate `production_like_refused` requires `PROVIDER_WRITE_UNSUPPORTED`. Without this rule it would become false at step 5, and two things would fail:
  - the sanity pipeline's `validate_current_mapped_cache`;
  - the release attestation's `mapped_cache` closure step.
- **Generator bound.** Only the scenario's invocation changes. `PREDICATE_KEYS` and every output byte stay unchanged; `--check` exits 0. The classifier gains its `_EVIDENCE_GENERATOR_TEST_OWNERS` entry (ID-10), because a change to it otherwise fails classification with `CI_EVIDENCE_OWNER_TEST_MISSING`.
- **Test-environment setup.** A test whose open-rails environment relies on an ambient `APP_ENV` may set it explicitly; only the environment setup changes.
- **Anything else.** Any other affected test or tool found by PR-20's prototype sweep is listed in the plan under this same rule. An output change in any governed or frozen family is a finding (§14).

**ID-9. Aux preview band (S08).**
- With `--pair-file`, an explicit `--band` (argparse choices `AUX_BANDS`) replaces only the band read from the file.
- Unchanged:
  - category selection and the `MISSING_COMPAT_CATEGORY` and `INVALID_COMPAT_INPUT` refusals (the category must still resolve in the file);
  - perspective;
  - the file's `release_id`;
  - stdout emission (`--show-narrative`) and the `--admin-out` sidecar.
- Without `--band`, the file's band is used, as today.
- The non-pair-file path is unchanged.
- A band that selects a governed suppressed key emits zero bytes, as any suppressed key does (HDE-CLI-API-Vendor-Ref §3.1.1 `aux_suppressed_empty`).

**ID-10. Classifier registration (Plan deliverable; §5.10).**
- **What changes.** `ci/checks/classify_ci_changes.py` changes by the smallest registration that classifies:
  - `engine/bodygraph/vendor_audit.py` with a real owner test (`_PRODUCT_TEST_OWNER_PATHS`); today it is refused with `CI_PRODUCT_OWNER_TEST_MISSING`;
  - `tools/evidence/generate_v2_mapped_cache_evidence.py` with its existing owner test `tests/evidence/test_v2_mapped_cache_evidence.py` (`_EVIDENCE_GENERATOR_TEST_OWNERS`); today it is refused with `CI_EVIDENCE_OWNER_TEST_MISSING`.
- **New test modules** must satisfy the WU-PR-01 coverage guard (`test_every_tracked_test_module_is_reached_by_a_lane_or_full_validation_target`) through that registration, with no `ci.yml` change.
- **Pins.** Every registry pin in `tests/evidence/test_rails_ci_workflow_integration.py` stays true. A pin the registration requires is added there.
- **Lanes.** The classifier is a full-validation path, so this unit's pull request runs all seven lanes.

## 5. Current repository and reference baseline (measured at `39afdc6`)

The Audit's S08 and S14 facts were measured at `982071b`. They still hold at `39afdc6`, with these corrections and additions:
- line numbers moved;
- §5.3 to §5.5 and §5.8 are new findings;
- `tests/bodygraph/test_resolver_vendor.py` is in a lane (WU-PR-01).

### 5.1 CLI (`engine/cli/main.py`, member)

- **`aux-preview` parser** (lines 125–136): `--category`, `--band` (choices `AUX_BANDS`), `--perspective` (choices), `--pair-file`, `--show-narrative`, `--admin-out`.
- **`bg:resolve` parser** (lines 137–163): `--user` (required), `--source {auto,db,vendor}` (default `auto`), `--upsert`, `--dry-run`, `--birthdate`, `--birthtime`, `--location`; `allow_abbrev=False`. No `--allow-prod-vendor` exists anywhere outside `docs/`.
- **`_resolver_env()`** (lines 186–187) passes `SAFE_MODE`, `ALLOW_NETWORK`, `APP_ENV`, `HD_API_BASE_URL`, `HDAPI_BASE_URL`. It does not pass `ENGINE_ENV`; the merged vendor view reads it from the process.
- **`bg_resolve`** (lines 210–228): `MISSING_VENDOR_INPUT` (exit 64) for an incomplete vendor birth tuple, then `resolve_bodygraph(...)`. It writes the result envelope to stdout through `emitter.emit_public` and returns its `exit_code`.
- **`cli()`** (lines 231–268):
  - argparse `SystemExit` → 64;
  - `CliError` → its code on stderr, its exit code;
  - `VendorError` and `CompatBoundaryError` → token on stderr, exit 1.

### 5.2 Resolver vendor path (`engine/bodygraph/resolver.py`, member)

- **`resolve_bodygraph`** (lines 59–109): `auto` and `db` are the no-I/O stub; `vendor` → `_resolve_vendor`.
- **`_resolve_vendor`** (lines 112–221), in order:
  1. `PROVIDER_REFUSED` (SAFE);
  2. `PROVIDER_NETWORK_BLOCKED`;
  3. `_vendor_config_env` and `_classify_env_route_policy` (`PROVIDER_CONFIG_INVALID` for conflicting base URLs, `PROVIDER_CONFIG_MISSING`);
  4. inputs and identity;
  5. then either the v2 path (`recommended_v2_chart`) or `ingest_vendor_bodygraph` (legacy).
- **Refusals.** Each returns `{"status":"error","error":{...},"resolver":{...}}`, exit 1, through `_vendor_error` (lines 442–448) or inline (rails).
- **No environment classification exists on this path.** The only `APP_ENV`/`ENGINE_ENV` reading is inside `_resolve_vendor_v2_chart` (lines 246–248). It applies only to the non-dry-run write path, using `or` semantics over the requested view and the process view.
- **`classify_bg_resolve_route_policy`** (`engine/bodygraph/vendor_client.py` lines 124–151) treats every non-`v2` base as legacy (OBS-W4-3).

### 5.3 Shared acquisition paths outside the gate

- **showcompat.** `hdctl showcompat --source vendor` (lines 685–693, and conjunction mode at line 737) calls `resolve_compat_chart(..., source_policy="vendor", env=_resolver_env())`. That reaches `_acquire_dry_run` (resolver lines 632–748), which calls `_resolve_vendor_v2_chart` directly, or `ingest_vendor_bodygraph(dry_run=True)`, under open rails, with no override.
- **Dev conjunction routes.** `/dev/sampler/conjunction`, `/dev/reader/conjunction` and `/dev/writer/conjunction` (`adapter/http_reader.py` lines 1056–1078) reach the same path through `conjunction_public_resolved` (default `source_policy="vendor"`). They call `_dev_admin_gate()` (`dev`/`test`/`local`) before acquisition, so they refuse under `APP_ENV=prod`.
- **No public route reaches the vendor.** Every other HTTP call site passes `source_policy="local"` (`adapter/http_reader.py` lines 528–529 and 637–638; `engine/http/compat_handler.py` lines 105 and 164–165). The Aux route does not call the resolver.

### 5.4 Write paths

- **v2.** `_resolve_vendor_v2_chart`:
  - non-dry-run without `--upsert` → `PROVIDER_WRITE_UNSUPPORTED`;
  - non-dry-run with a production-like requested or process environment → `PROVIDER_WRITE_UNSUPPORTED`;
  - both before `DBAccess` and the client.
- **Legacy.** `ingest_vendor_bodygraph` (`engine/bodygraph/ingest.py` line 131):
  - with `dry_run=False` it constructs `DBAccess` and persists rows (line 207), with no environment check;
  - with `dry_run=True` it appends a success line (including `user_id`) to its success log (pre-existing; not this unit's subject).

### 5.5 Typed codes

- **Defined locally.** Provider codes are string literals passed to `VendorError` (`vendor_client.py` lines 213–226). No token map, schema or release member registers them (`git grep` over `errors/`, `schemas/`, `adapter/schemas/`, `engine/compat/error_tokens.py`, `catalog/`: no hit).
- **New codes.** `PROVIDER_PROD_OVERRIDE_REQUIRED`, `PROVIDER_PROD_OVERRIDE_INVALID` and `PROVIDER_AUDIT_UNAVAILABLE` exist nowhere outside `docs/`. `PROVIDER_CONFIG_INVALID` and `PROVIDER_WRITE_UNSUPPORTED` exist.

### 5.6 Aux preview (S08)

- **Pair-file mode.** `_resolve_from_pair_file` (lines 538–559) takes the band from the pair file's category row (line 554) and never reads `args.band`. `--category` and `--perspective` are honored.
- **Other mode.** Without `--pair-file`, `--category`, `--band` and `--perspective` are all required (`MISSING_AUX_INPUT`, line 565).
- **Emission.** Stdout emission happens only with `--show-narrative` or without a pair file (line 581).

### 5.7 Tests that pin current behavior

- **`tests/cli/test_bg_resolve.py`** (6 tests):
  - the closed-rails vendor refusal (envelope on stdout, `PROVIDER_REFUSED`, nonzero exit);
  - an open-rails legacy write with `APP_ENV=dev` and a fake ingest (`rows_written` 1);
  - `APP_ENV` deleted only on the `db` source.
- **`tests/cli/test_aux_preview.py`** (2 tests): both use the non-pair-file path.
- **`tests/bodygraph/test_resolver_vendor.py`** (4 tests).
- **`tests/bodygraph/test_bg_resolve_v2_mapped_cache.py`** (13 test functions):
  - its `env()` helper sets `APP_ENV=test`;
  - the two production-like tests named in ID-8 assert `PROVIDER_WRITE_UNSUPPORTED` with no vendor or DB construction.
- **`tests/bodygraph/test_bg_resolve_route_policy.py`** (12 tests): several open-rails mappings carry no `APP_ENV` and rely on the process value. `tests/conftest.py` sets none.
- **Other usage-error and showcompat tests.** `tests/cli/test_cli_usage_and_errors.py` and `tests/cli/test_showcompat_sources.py` exercise `bg:resolve` and showcompat vendor usage errors.

### 5.8 Evidence tools and frozen captures on this path

| Tool | Scenario | Effect of S14 without ID-8 | Consumers |
| :- | :- | :- | :- |
| `tools/evidence/generate_v2_mapped_cache_evidence.py` | `production`: `APP_ENV=production`, open rails, v2 base, `upsert=True`, `dry_run=False`; predicate `production_like_refused` requires `PROVIDER_WRITE_UNSUPPORTED` | predicate false (step 5 refuses first) | `run_sanity_pipeline.py` `validate_current_mapped_cache`; `regenerate_identity_closure.py` step `mapped_cache` (write and `--check`); `tests/evidence/test_v2_mapped_cache_evidence.py`; `tests/evidence/test_sanity_pipeline.py` |
| `tools/evidence/generate_hde_epic037_bg_resolve.py` | open-rails v2 dry run whose mapping has no `APP_ENV` (process `APP_ENV=dev` under the closed-rails profile); closed-rails refusal embedded byte for byte in `artifacts/vendor/hdapi_v2/hde_epic037_bg_resolve_closed_rails_no_io.json` | none if ID-2 and ID-7 hold | `--check` (no CI test found) |
| `tools/evidence/generate_bodygraph_policy_proofs.py` | closed rails only | none | sanity pipeline stage `--check`; closure step `bodygraph_policy` |
| `artifacts/cli/guards/emitter_symbol_proof.txt` | records `bg:resolve:bg_resolve:emitter.emit_public` | none if ID-7 holds | `tests/cli/test_serializer_guards.py` |

`artifacts/architecture/architecture_snapshot.keys_only.json` lists `engine/bodygraph/resolver.py`'s import symbols. `tests/evidence/test_architecture_snapshot.py` checks the current analysis in memory, and `engine/` paths classify `allowed`, so a new import does not fail it.

### 5.9 Release identity and the refresh

- **Manifest.** `catalog/manifest.json`: version `1.3.0`, `built_at_utc 2026-08-24T18:04:49Z`, 45 members, `release_id d84d99e1f2ffd1f97157097302e6480a4abfc04ae70c3b54dfd9283d8eae68c7` (sha256 of the file at `39afdc6`, equal to WU-PR-03 result v2.0 §8 and addendum 2.7 AD-5's "New base").
- **Members this unit changes:** `engine/cli/main.py` (S08, S14) and `engine/bodygraph/resolver.py` (S14).
- **Non-members:** `engine/bodygraph/vendor_client.py`, `engine/bodygraph/ingest.py`, the new `engine/bodygraph/vendor_audit.py`, `tools/**`, `ci/**`, `tests/**`, `docs/**`. Admission's roster is fixed at 45.
- **Required refresh.** A same-version cut at `1.3.0` / `2026-08-24T18:04:49Z` through the cutter, then convergence in the order WU-PR-03 result v2.0 §8 executed: Plan v1.1 §10 with step 3b after admission. Restart a member change at step 2 and an evidence-primary change at step 3b (addenda 2.6 RP-2 and 2.7 AD-5). Steps 3b to 10 must be byte-stable on a second pass.
- **Labels** (WU-PR-02 lineage review v1.0 §7; addenda 2.5 and 2.6):
  - **LR-O3 (a).** The updater refuses `CURRENT_RELEASE_LABEL_MANIFEST_INVALID` between the member edits and the cut. Do not run it there.
  - **LR-O3 (b).** Roster captures take the new label at the first updater run after their owner regenerates them.
  - **LR-O3 (c).** A roster capture left byte-stable keeps its earlier label. That is a finding to the IA, never a roster edit; the roster holds 22 paths and the engine-core purity report stays unlabelled.
  - **LR-O1.** The label is not proof that an owner ran.
- **Expected changed set.** Modelled on WU-PR-03's 61 paths: the manifest, `FROZEN_OPEN_ABBA_SHA256`, the release-binding primaries and their path proofs, Index and Mirror. The catalog family is rewritten byte-identically unless the catalog validator changes, and this unit does not change it.
- **Stale-binding sweep.** At step 11 it searches for `d84d99e1` and the superseded open-rails digest `06611525…` outside `docs/`, `.audit_src/`, `handoff/`, `manifest_pre.sha256` and `manifest_post.sha256`.

### 5.10 CI classification at the baseline

`ci/checks/classify_ci_changes.py` (`_lanes_for_path`, `changed_test_targets`, `classify_paths`), run at `39afdc6`:

| Path | Lanes | Owner targets |
| :- | :- | :- |
| `engine/cli/main.py` | compat, product, release | `tests/cli/test_cli_file_inputs.py`, `tests/cli/test_showcompat_sources.py`, `tests/qa/test_cli_admin_dumps.py`, `tests/qa/test_cli_admin_parity.py` |
| `engine/bodygraph/resolver.py` | product, release | `tests/bodygraph/test_bg_resolve_route_policy.py`, `test_bg_resolve_v2_mapped_cache.py`, `test_resolve_compat_chart.py`, `test_resolver_vendor.py`, `tests/cli/test_bg_resolve.py` |
| `engine/bodygraph/vendor_audit.py` (new) | product, release | **refused: `CI_PRODUCT_OWNER_TEST_MISSING`** |
| `tools/evidence/generate_v2_mapped_cache_evidence.py` | evidence, release | **refused: `CI_EVIDENCE_OWNER_TEST_MISSING`** |
| `tests/cli/test_aux_preview.py` | compat, product, release | itself and `tests/evidence/test_http_reader_ci_ownership.py` |
| `tests/bodygraph/test_resolver_vendor.py` | product, rails, release | itself |
| `catalog/manifest.json` | release | — |
| `docs/CLI_commands.md` | none | — |

`tests/evidence/test_hdapi_v2_contract_inventory.py` needs `ruby` on `PATH` (addendum 2.2). It is present on the hosted runner; its version is unprinted (O-6).

## 6. Bounded files and components

Plan v1.1 §7 WU-PR-04 "Deliverables" approves each locus, except those marked ID-8, which this instruction binds.

| Path | Bound |
| :- | :- |
| `engine/cli/main.py` (member) | S14 / IF-1 / ID-1: the option, its pre-scan, validation, applicability and usage carrier; passing the reference to the resolver. S08 / ID-9: the band override in `_resolve_from_pair_file`. Nothing else |
| `engine/bodygraph/resolver.py` (member) | S14 / ID-1 to ID-4, ID-7: steps 4–6 in `_resolve_vendor`, the keyword argument, the state event after step 7, and ID-3's production write refusal. `_acquire_dry_run`'s behavior and every existing envelope byte unchanged |
| `engine/bodygraph/vendor_audit.py` (new) | IF-2 / ID-4 to ID-6: record, sink, actor, clock and correlation seams |
| `tests/cli/test_bg_resolve.py`; `tests/cli/test_aux_preview.py`; `tests/bodygraph/test_resolver_vendor.py`; `tests/bodygraph/test_vendor_prod_override.py` (new) | the matrix, order, usage, audit and band tests (§10) |
| `tests/bodygraph/test_bg_resolve_v2_mapped_cache.py`; `tools/evidence/generate_v2_mapped_cache_evidence.py` | ID-8 only |
| `ci/checks/classify_ci_changes.py`; `tests/evidence/test_rails_ci_workflow_integration.py` | ID-10 only |
| `docs/CLI_commands.md` | the `bg:resolve` synopsis with the option, a sentence on the production gate and audit sink key, and the `aux-preview` band sentence (Plan "flag and band wording") |
| `catalog/manifest.json` | the refresh at `1.3.0` / `2026-08-24T18:04:49Z`, by the cutter only |
| Every evidence family the refresh regenerates, by its owner, and the Index/Mirror by the updater | as the convergence requires (§5.9) |
| `docs/ephemeral/` PR result records | evidence obligations (§10) |

Any other file the work needs is a finding: route it under §14 before changing it. In particular:
- these are expected to stay unchanged: `engine/bodygraph/vendor_client.py`, `engine/bodygraph/ingest.py`, `engine/compat/**`, `adapter/**`, `engine/http/**`, `engine/narratives/**`, `engine/config/registry_loader.py`, `tools/evidence/update_evidence_index.py`, `tools/evidence/generate_hde_epic037_bg_resolve.py`, `.github/workflows/ci.yml`;
- every frozen family stays byte-unchanged, including `artifacts/vendor/**`, `artifacts/cli/**`, `artifacts/architecture/**` and `audit/ops/**`.

## 7. Exclusions

- **Surfaces.** No change to `hdctl showcompat`, the conjunction paths or any HTTP route. No vendor path is added to Reader, Aux or any HTTP surface. No public contract, payload, flag or transport change (Specification Exclusions; Plan §4 invariant 1).
- **Existing behavior.** No change to existing stdout or stderr bytes, retry or timeout pins, route selection, credential handling, or non-production write behavior.
- **Release.** No version bump and no admission-constant change (WU-PR-08 owns `1.4.0`).
- **Canon.** No canon edit and no PF10 addendum. No new `schemas/` file. No new evidence family or acceptance token.
- **Live and production.** No live vendor, production or database call; closed rails throughout, except monkeypatched open-rails unit tests with fake clients. No real credentials. No production configuration change. No audit sink file in the repository.
- **Documents.** No `AGENTS.md`, `README.md`, `CHANGELOG.md` or `.env.example` edit (WU-DOC-01 and WU-PR-08).
- **Tests.** No skipped, disabled, `xfail`-marked or quarantined test.
- **Observations.** OBS-W4-1 to OBS-W4-4 (§15) are recorded, not fixed.

## 8. Interface contracts with other units

| Contract | Consumer | Content |
| :- | :- | :- |
| F-1 Release base | WU-PR-05, WU-PR-08 | This unit's refreshed `release_id` and converged evidence are the next refresh's base. The result record names it |
| F-2 Override contract | QA Plan (Live QA vendor call), WU-DOC-01 | The exact command form; the sink key name and default; the actor rule; the event shapes and outcomes (ID-4); the refusal codes and where `outbound_attempted` sits. The live call needs an authenticated human initiator and an available sink, which the QA Plan verifies before the call (R-3) |
| F-3 Classifier registrations | WU-PR-06 | The ID-10 registrations are part of the classifier's rules |
| F-4 Production write refusal | WU-PR-05 (S19), QA | ID-3 holds on both write paths. It is a behavior of this unit, not a QA step |
| F-5 Observations for S19 | WU-PR-05 | OBS-W4-1 and OBS-W4-3 are named inputs of the S19 review (§15) |

## 9. Disposition rules PR-20 must apply and record

1. **ID decisions.** Apply ID-1 to ID-10 as written. Record each of PR-20's own choices with its reason:
   - the usage-error text;
   - the keyword name;
   - the codes for a malformed library reference;
   - the view-merging rule (ID-2);
   - the UID-only actor case;
   - the parent-directory rule;
   - the key name and default path;
   - the schema-version constant;
   - the `outbound_attempted` placement.
2. **Order tables.** Write the seven-step table and the eight-row matrix table with, for each cell, the expected code, exit status, stdout and stderr shape, event (none, `refused`, `allowed`, then the state event), and the proof of zero outbound attempts.
3. **Prototype sweep.** Prototype in a throwaway copy, run the full `tests/` sweep and the evidence tools of §5.8, and list every affected test or tool under ID-8.
4. **Refresh.** Follow §5.9 exactly. Record every step, both passes' results, the byte-stability digest and the stale-binding sweep.
5. **Stale documents.** Name each document or canon passage this unit makes stale but may not change, with its owner (§15).
6. **Route-policy statement** (Plan Templates "`bg:resolve --source vendor` route-policy posture"). The plan states that the route policy is unchanged: v2 chart-backed for configured `v2` bases, explicit legacy fallback otherwise. It claims no complete BodyGraph-resolution conformance beyond the existing evidence.

## 10. Acceptance, tests and evidence

**Plan v1.1 §7 WU-PR-04 acceptance, verbatim**, with the binding readings in brackets:
1. "Table-driven tests cover the eight matrix rows and the seven evaluation steps with a monkeypatched vendor client proving no client construction, DNS, socket or HTTP on any refusal; `outbound_attempted` false and exit 1 for policy refusals, exit 64 for usage errors; `ENGINE_ENV` alias and conflict; a vendor `--dry-run` in a production-like environment without the flag refuses `PROVIDER_PROD_OVERRIDE_REQUIRED`." [The guards make construction of `HdApiClient`, `DBAccess` and `urllib` requests, `socket.getaddrinfo` and `socket.socket` fail the test. Usage errors include duplicate (both spellings), empty, missing value, each class of invalid character, 129 characters, and the option with `db`, `auto` and the default source. The allowed rows assert exactly one fake fetch.]
2. "The audit record has exactly the IF-2 fields, is CR/LF-sanitized, contains no subject or secret data, and an unwritable sink yields `PROVIDER_AUDIT_UNAVAILABLE` before I/O." [Also: actor unavailable → `PROVIDER_AUDIT_UNAVAILABLE`; the ID-4 (c) event; the state events of ID-4 (e); a search of every captured stdout, stderr and sink line for the reference, the birth inputs, the base URL and the key values.]
3. "Closed rails refuse first in every case; no Reader or Aux route gains a vendor path." [Every matrix row also runs under each closed rail with the existing bytes. The call sites of §5.3 are unchanged, and ID-3 holds on both write paths.]
4. "`aux-preview --pair-file … --band <band>` emits the flagged band; without the flag, the file's band." [Plus the ID-9 unchanged refusals, and `--admin-out` naming the flagged band's key.]
5. "Admission and convergence as WU-PR-03 (7); all lanes green." [That is: admission at the PR head reports `1.3.0`, 45 members and the refreshed `release_id`; steps 3b to 10 byte-stable on a second pass; `release_id_recompute.py --check-manifest-only` exits 0; all seven lanes green because of ID-10.]

**Evidence obligations**, verbatim from the Plan: "PR result record; no live call; no audit sink in the repository." The record also names:
- each check actually run, with counts;
- the refreshed `release_id` and every regenerated family;
- the matrix and order tables with results;
- the sink key name and default rule;
- the actor rule;
- the ID-8 list;
- the classifier keys (ID-10);
- the stale-document list (§9.5);
- the nonclaims (§12).

**Validation PR-20 plans** (minimum):
- all seven lanes;
- the full `tests/` sweep in a detached worktree with `ruby`, `bash` and `curl` on `PATH`, which covers every updater consumer (the refresh rewrites the Index and Mirror; LR-O2);
- `generate_v2_mapped_cache_evidence.py --check`, `generate_hde_epic037_bg_resolve.py --check` and `generate_bodygraph_policy_proofs.py --check` under the closed-rails profile;
- the sanity pipeline ending `summary:PASS`;
- `ci/checks/check_cli_help.sh`;
- `tests/cli/test_serializer_guards.py`;
- the convergence checks of Plan v1.1 §10 steps 4–10;
- the attestation build and verify into an external empty directory with `--require-clean`;
- negative controls, at least:
  - removing step 5 makes a matrix test fail;
  - skipping the event write makes an audit test fail;
  - removing ID-3's legacy refusal makes its test fail.

Each run that can write tracked files runs in a detached worktree and ends with `git diff --exit-code` and an empty untracked status.

| Requirement | Acceptance item | Proof | Stage |
| :- | :- | :- | :- |
| S14 flag, order, matrix, carrier | (1) | `tests/bodygraph/test_vendor_prod_override.py` tables M-1 to M-8 and O-1 to O-7; CLI usage tests | PR-30; CI |
| S14 initiator and audit | (2) | actor and sink tests; redaction search | PR-30; CI |
| S14 rails first, no public path, read-only | (3) | closed-rail rows; §5.3 call sites unchanged; ID-3 tests | PR-30; CI |
| S14 live behavior | — | the Live QA vendor call (QA Plan) | QA, not this unit |
| S08 | (4) | pair-file tests with and without `--band` | PR-30; CI |
| Refresh | (5) | admission; second-pass stability; recompute; seven lanes; attestation | PR-30; PR-35 (CI) |

## 11. Migration and security constraints

- **Migration:** none (no data or schema change).
- **Rollback:** Nathan's revert of the squash commit, followed by a same-version manifest refresh, because this unit changes members (Plan §7 common paragraph).
- **Security:**
  - The gate only narrows: no rail opens, no write path opens (ID-3), and no surface gains vendor access.
  - The reference is not authentication and grants nothing by itself.
  - The actor is never caller-asserted.
  - The audit record is keys-only, owner-readable and outside the repository.
  - Nothing in stdout, stderr, exceptions or logs carries the reference, actor, sink path or any secret (ID-7).
  - Tests and records hold no secret, token or key value.

## 12. Engineering, review, CI and merge obligations

- **PR-20** (dedicated PR session):
  - reads this instruction and its lineage, the §5 and §6 repository files, and canon on `main`;
  - writes one complete `PR_IMPLEMENTATION_PLAN` under `docs/ephemeral/`: the design per §4.2 and §9, the requirement-to-change/test map, ordered steps including the refresh, risks and recovery;
  - returns `AWAITING_PO_PROCEED` only for a complete plan within this scope.
- **PR-30** (after Nathan's Proceed for that exact plan):
  - recovers existing work first;
  - implements only the authorized scope;
  - converges the evidence by owners only;
  - tests locally under §10;
  - commits coherently;
  - publishes `PR_CANDIDATE_PUBLISHED`;
  - hands off to PR-35 in its own session.
- **PR-35** (its own dedicated session):
  - retrieves and resolves the Codex code review findings (PF10 addendum 2.3: the Codex security review is not part of the chain);
  - retests, and pushes coherent corrections. Any member change re-runs the refresh from step 2; an evidence-primary change from step 3b;
  - verifies current-head CI (all seven lanes, `CI_APPLICABILITY_AND_EXACT_HEAD_OK`) and mergeability;
  - returns `MERGE_PENDING` without merging.
- **PR description:** the `.github/pull_request_template.md` headings with the `AGENTS.md` content rules.
- **Merge:** Nathan merges manually. No agent merges, enables auto-merge, enqueues or schedules a merge.
- **PR-40:** after the merge is observed or asserted, this IA reviews the landed lineage and, on ACCEPT, issues WU-PR-05's instruction.
- **Attributable lineage:** the PR result records, the PR reference and the squash commit.
- **Nonclaims** every record keeps:
  - the flag was not exercised live;
  - no QA verdict, acceptance, Ops, deployment, PF09 movement or closure;
  - no conformance claim beyond §7.1.11's implementation;
  - the DD-04 canon paragraph is not edited.

## 13. Recovery

- **Interruption:** resume in the same dedicated phase session from its last saved artifact. Inspect existing worktrees, branches, PRs and `docs/ephemeral/` before creating anything.
- **A failed or interrupted refresh** restarts:
  - at step 2 for a member change;
  - at step 3b for an evidence-primary change.
- **An ordinary defect in this instruction** returns to this IA through PR-10. A corrected instruction is a new version, never an edit of v1.0.
- **Abort** is only Nathan's manual PR-50 instruction.

## 14. Rescope behavior

- **Material** means a change to an approved acceptance intent; a protected architecture, security, data-model or external-contract boundary; several units' scope; an accepted dependency; or budget, schedule or risk needing Product Owner direction.
- **Before Proceed:** the PR-20 author owns any rescope proposal (RS-10 optional support; RS-30 for revisions), and this IA reviews it through RS-20. The decision returns to the PR-20 planning context.
- **After Proceed:** PR-30 or PR-35 records `PR_RETURN_PHASE`.
- **Specification issue:** `SPECIFICATION_CHANGE_REQUIRED` returns to Nathan.
- **Expected triggers:**
  - a change needed outside §6, in particular to `vendor_client.py`, `ingest.py`, `adapter/**`, the updater, `ci.yml` or a frozen family;
  - a governed output that cannot stay byte-identical under ID-8;
  - a need to gate showcompat or conjunction acquisition;
  - a canon requirement for a registered audit schema;
  - a frozen-family `--check` failure after the refresh;
  - a reading of ID-1 to ID-9 that PR-20 believes conflicts with canon.

## 15. Unresolved items, carried observations and owners

| Item | Owner | State |
| :- | :- | :- |
| The PR-20 choices listed in §9.1 | PR-20 session | In the plan |
| N4 (actor principal and sink key; review v1.0, carried by review v1.1) | PR-20 (mechanism, ID-5, ID-6); QA Plan (the venue's principal and sink, R-3) | Carried |
| LR-O1, LR-O3 (labels; updater timing) | this unit applies them (§5.9) | Applied here |
| LR-O2 (run every updater consumer on an updater change) | IA | Not triggered: the updater does not change. Its consumers still run, because the refresh rewrites the Index and Mirror |
| OBS-17: intermittent hosted failure of `tests/qa/test_generate_epic_close_pack.py` | QA tool and test owner, through the IA; Product Owner to route | All seven lanes run here (ID-10). A qa-lane failure of that test is recorded as OBS-17, never "fixed" here |
| O-6: hosted `ruby` version unprinted | IA | PR-35 records it if the job log shows it |
| **OBS-W4-1** (new). `hdctl showcompat --source vendor`, including conjunction mode, reaches vendor HTTP under open rails through `_acquire_dry_run` with no production override or audit (§5.3). PF07 §2.4 records production rails open, and HDE Governance "Governance stance" assumes admin-guarded CLI vendor calls in production. §7.1.11a scopes the flag to `bg:resolve`, so S14 does not cover it, and this unit must not change it. HDE Mechanics Guide §22 describes conjunction acquisition as going through the resolver (`resolve_db_user_id` and `resolve_bodygraph`); the repository's acquisition seam bypasses `resolve_bodygraph`. Whether production showcompat or conjunction acquisition must meet the §7.1.11 gate, which those commands cannot pass, is not decided by canon | WU-PR-05 (S19 reads it; its code came from HDE-EPIC040 PR04); Product Owner (PF05 owner) for any canon or scope decision | Recorded |
| **OBS-W4-2** (new). HDE-CLI-API-Vendor-Ref §4.6 and §3.4 put typed failures on stderr only, while `bg:resolve` writes its error envelope to stdout. PF05 §1 and the §4.7 matrix already record this ("failure streams diverge"). §7.1.11e names "the canonical `status="error"` resolver envelope" for override refusals, and this unit follows it without changing streams | Product Owner (PF05) | Pre-existing; recorded |
| **OBS-W4-3** (new). `classify_bg_resolve_route_policy` maps every non-`v2` base, including unversioned or nonterminal ones, to the legacy route. §7.1.10 requires `PROVIDER_ROUTE_UNSUPPORTED` for those. Step 7 keeps current behavior here | WU-PR-05 (S19 input); Product Owner | Pre-existing; recorded |
| **OBS-W4-4** (new). §7.1.11f's "governed clock boundary" is defined nowhere in canon or the repository. ID-6 uses an injectable UTC clock | Product Owner (doc-delta candidate) | Recorded |
| AD-4's four gaps, OBS-P3-3, OBS-P3-14, OBS-P3-17, LR3-O2's wording | WU-PR-05 instruction | Not this unit |
| LR3-O1 (PF10 rendering of 2.7), LR3-O4 (README `release_id`), LR3-O5 | Product Owner; WU-DOC-01; IA | Not this unit |
| AQ-1 | Product Owner | WU-PR-07 only |
| Doc-delta candidates (not edited here) | Product Owner (canon); WU-DOC-01 (repository docs) | Recorded |

The doc-delta candidates are:
- HDE-CLI-API-Vendor-Ref §7.1.11 "Required-Now implementation gap (DD-04; held)" paragraph (stale once this unit lands);
- HDE Users Guide §16 `--allow-prod-vendor` bullet ("absent from the inspected active CLI parser");
- Glow Infrastructure §8 config keys (the new sink key);
- OBS-W4-4's clock term;
- `README.md` and `AGENTS.md` mentions (WU-DOC-01).

The historical records `audit/docdeltas/hde-epic040_doc_deltas.md` DD-04 and HDE Phased Epics' DD-04 row stay as they are.

## 16. Canon-conflict register

`CANON_CONFLICT_REGISTER` is carried unchanged:

| ID | Status | Decision owner | Record |
| :- | :- | :- | :- |
| CR-1, CR-2, CR-3 (CANON_RECONCILIATION) | APPROVED_AS_CHANGED | Thoth | Specification v1.1 lineage |
| CR-4 | APPROVED | Product Owner | `docs/ephemeral/HDE-CRD-0002-WU-PR-01-po-disposition-cr-4-cr-5-v1.0.md` §2 |
| CR-5 | APPROVED_AS_CHANGED | Product Owner | same record §3 |
| CR-6 | APPROVED, alternative (a) | this IA through RS-20 | rescope review v1.0 §12; addendum 2.6 |
| CR-7, CR-8 | APPROVED, alternative (a) each | Product Owner direction of 2026-10-14 | decision record §6; addendum 2.7 |

No new conflict:
- ID-1 to ID-9 apply HDE-CLI-API-Vendor-Ref §7.1.11 as written, within the Plan's IF-1, IF-2 and EC-7.
- ID-4 (a) and (f) read §7.1.11c and §7.1.11f together; the matrix and the step order settle each case.
- ID-3 applies §7.1.11d's "does not authorize … any production database write" with the existing typed code.
- OBS-W4-1 to OBS-W4-3 are pre-existing gaps between canon and the repository, or between two canon passages, outside S08 and S14's acceptance intents. They are recorded for their owners and not resolved here.

Coverage read for this unit:
- HDE-CLI-API-Vendor-Ref §7.1 (§7.1.1 to §7.1.11f, all read in full), §3.1.1 carrier table, §3.3 "Usage & typed errors", §3.4, §4.5, §4.6, §4.7, and the §1 status lines for `aux-preview` and `bg:resolve`;
- HDE Governance §3.1 (all four parts) and §11.1.1's `bg:resolve` route-policy and mapped-cache paragraphs;
- HDE Mechanics Guide §17.10.2, §17.10.3 and §22 in full;
- Glow Infrastructure §2.4, §2.6, §2.7 and §8.1;
- Plan Templates `bg:resolve` posture bullets;
- a whole-canon search for `allow-prod-vendor`, `PROVIDER_PROD_OVERRIDE`, `PROVIDER_AUDIT_UNAVAILABLE` and `vendor_prod_override`. Hits: HDE-CLI-API-Vendor-Ref §7.1.11, HDE Users Guide §16, HDE Phased Epics DD-04, and two unrelated "live" passages in the Separation checklist and the QA Guide.

## 17. Semantic readiness comparison

| Source clause | Intended meaning | Instruction meaning | Unit | Acceptance | Evidence stage |
| :- | :- | :- | :- | :- | :- |
| S14 "behaves as §7.1.11 specifies" | the canon contract, complete | §4.1 clause map; ID-1 to ID-7 | WU-PR-04 | (1)–(3) | PR-30; CI |
| S14 "closed rails still refuse first" | rails before every vendor decision | step 3 unchanged and first; closed-rail rows | WU-PR-04 | (3) | PR-30; CI |
| S14 "public Reader or Aux traffic never reaches the vendor" | no public vendor path | §5.3 measured; call sites unchanged | WU-PR-04 | (3) | PR-30; CI; Live QA |
| S14 "authorized initiator" | human, authenticated, not self-asserted | ID-5; the live initiator is QA's | WU-PR-04 / QA | (2) / Live QA | PR-30; QA |
| §7.1.11d "does not authorize … any production database write" | read-only override | ID-3 on both write paths | WU-PR-04 | (3) | PR-30; CI |
| IF-2 fields and outcomes | one keys-only record, durable before I/O | ID-4, ID-6 | WU-PR-04 | (2) | PR-30; CI |
| EC-7 "default under the operator's state directory" | an operator-local sink, never the repository | ID-6; key name fixed by PR-20 | WU-PR-04 | (2) | PR-30 |
| S08 "takes effect for pair-file input" | the flag overrides the file's band | ID-9 | WU-PR-04 | (4) | PR-30; CI |
| Plan "same-version manifest refresh and convergence" | admission and evidence current after member changes | §5.9 order with step 3b, rules LR-O1 and LR-O3 | WU-PR-04 | (5) | PR-30; PR-35 |
| Addenda 2.6 and 2.7 downstream items | 22-path roster; refresh from `d84d99e1…` | §5.9 | WU-PR-04 | (5) | PR-30 |

Checks against the full PR-20 contract:
- Its sole substantive input is `PR_INSTRUCTION_ID`.
- This instruction carries everything PR-20 needs:
  - the Specification, Audit, Plan and review lineage;
  - the PF10 path and overlays;
  - the baseline, loci, exclusions, interfaces and dependencies;
  - acceptance, evidence, migration and security;
  - recovery, rescope, merge ownership and the return owner.
- Numeric domains: the reference length is 1–128 characters with no zero or sentinel meaning; absent is a separate state (ID-1). Booleans: `safe_mode_open`, `network_open` and `outbound_attempted` are booleans, never counts.
- No decisive comparison fails. The facts in §5 were measured at `39afdc6` by this IA, not carried unverified. The §5.8 consequence for the mapped-cache generator follows from the canon order and the generator's own predicate; PR-20's prototype confirms it.

## 18. Return owner and next step

- **Next:** PR-20 — Create Detailed PR Implementation Plan — 100926.1, in a new dedicated top-level WU-PR-04 PR engineering session that Nathan creates. It returns `AWAITING_PO_PROCEED`.
- **Return to the IA:**
  - PR-40 lineage review after Nathan's merge;
  - rescope review through RS-20;
  - same-owner correction of this instruction through PR-10.

## 19. TypeSafe reading for the receiving session (PR-20, WU-PR-04)

Action sent (v8.2): "Write, in a new dedicated session, the first detailed PR implementation plan for one work unit of an approved change, from a ready instruction that lists the files and fixes ten design decisions: a production vendor-override flag on one CLI command with an eight-row environment matrix, a seven-step pre-I/O evaluation order, an append-only local audit record with actor and sink resolution in one new module, a production write refusal and a band-flag fix, across two release members, about eight test files, one evidence generator and a CI classifier registration, plus a same-version release re-cut with a fixed twelve-step governed-evidence convergence. Planning only, with a prototype in a throwaway copy and no live provider call; a Product Owner Proceed, implementation, code review and lineage review follow."

- **TypeSafe v8.2: Opus 5.5 at extra high.** Effort score 2.50 (confidence 0.65); rung probabilities low 0.00, medium 0.01, high 0.53, extra high 0.40, max 0.06, ultracode 0.00. Model probabilities Fable 5.1 0.12, Opus 5.5 0.65, Sonnet 5.5 0.22, Haiku 5.5 0.01 (confidence 0.53). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.001, Fable 5.1 at high 0.064, Fable 5.1 at extra high 0.048, Fable 5.1 at max 0.007, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.000, Opus 5.5 at medium 0.007, Opus 5.5 at high 0.345, Opus 5.5 at extra high 0.260, Opus 5.5 at max 0.039, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.000, Sonnet 5.5 at medium 0.002, Sonnet 5.5 at high 0.117, Sonnet 5.5 at extra high 0.088, Sonnet 5.5 at max 0.013, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.005, Haiku 5.5 at extra high 0.004, Haiku 5.5 at max 0.001, Haiku 5.5 at ultracode 0.000. Flags: boundary between extra high and high. Sent 2026-10-18T09:52:39Z. Nathan picks the cell.
- **Detail:** v8.2 sent 2026-10-18T09:52:39Z; HTTP 200 in 0.67 s; 5498 input and 71 output tokens; jev-1.13.0. Rung by rule: extra high (nearest to the score, halves up); model by rule: Opus 5.5 (the most probable of the four options, a tie going to the higher-priced model). Flags: boundary between extra high and high.
- **Which request.** The installed TypeSafe scoring skill now carries request v8.2 (`request-v8.2.json`, sha256 `62486fcc…22ec`) and `score_v8.py`, and states that v8.2 passed its pre-registered gates on 2026-10-18. Earlier records in this lineage used v6. On `main` at `39afdc6`, `docs/ephemeral/typesafe-ladder/four-model-20261016/` holds the v8 pre-registration (#647); no v8.2 acceptance record is there yet. That is recorded as fact, not as a gate.
- **Notion row:** not written, as PR-10 directs. **Nathan's pick for PR-20:** not stated. **For this PR-10 session:** not stated (its v6 reading is in WU-PR-03 lineage review v1.0 §11).

**Surface advice:** run PR-20 as a new top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, with Notion read access for the prompt.
- **Environment.**
  - The prototype, the sweep and the refresh rehearsal need Python 3.12 with CI's install (package-index access for `pip install`).
  - They also need `ruby` on `PATH` for the contract-inventory test (present at `/usr/local/bin/ruby` in the cloud container used for this instruction), plus `bash` and `curl`.
  - Run under closed rails with the vendor, database and GitHub keys unset; the container sets several of them.
- **Run times observed in this lineage.** A full `tests/` sweep takes about 20–25 minutes, the evidence lane about 13, and an attestation build about 3.
- **Access.** No live vendor, production or database access is needed. The open-rails tests use fake clients and temporary sinks.
- **Order.** This instruction's pull request should be merged first.

## 20. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / WU-PR-04 / PR-10 / instruction 1 |
| change / specification | CRD HDE-CRD-0002 / `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` v1.1 |
| work unit | WU-PR-04 (S08, S14) |
| release | GCFPE-20261009.1 / 100926.1 |
| prompt | PR-10 — Create PR Work-Unit Instructions — 100926.1, https://app.notion.com/p/3f44590a05eb815d97d5f3930c7d3e8a (page state as of 2026-10-12T02:29:33.739Z) |
| role/stage | continuing whole-change IA / PR-10 |
| capture time | 2026-10-18T09:58:27Z |
| execution identity | https://claude.ai/code/session_01CCKsYD2yX5WgU3biWKb59j |
| inherited usage | WU-PR-03 lineage review v1.0 §12 (PR-40) and the earlier uses it names |
| repository persistence | recorded here only (installed writer `docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent on `main`; pending, non-gating) |

## Canon relied on

Read on `main` at `39afdc6`. `docs/pfcanon/` was last changed at `79eac95`.

| Topic | Sources and sections |
| :- | :- |
| Instruction authority, content and readiness | PR-10 — Create PR Work-Unit Instructions — 100926.1 (read in full); HDE Governance (`docs/pfcanon/PF04-Canon-HDE-Governance-v2.8.7.md`) §9.1.1 (PR Instructions are the IA's; Proceed per detailed PR plan; PR merges remain Product Owner actions) and §9.1.2 (canon precedence over in-flight documents; ID-1 to ID-9 rest on it) |
| Overlays and carried items | PF10-HDE-Build-Notes v13.5.8 (`docs/pfcanon/PF10-HDE-Build-Notes-v13.5.8.md`): addendum 2.3 (Rules 1–5; the reviewer chain); 2.5 ("Retained decisions and requirements": LR-O1 to LR-O3, OBS-17, O-6); 2.6 ("Approved delta (RP-3)", "RP-2" (step 3b and its restart point), "Affected surfaces", Dependencies and Downstream work); 2.7 (AD-5 "Order" and "New base"; "Affected surfaces", Downstream; "Unresolved obligations and owners"); 2.1 (§19); 2.2 and 2.4 read for applicability, with no item for this unit |
| S14 | HDE-CLI-API-Vendor-Ref (`docs/pfcanon/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.3.md`): §7.1.11 preamble and §7.1.11a to §7.1.11f, each bullet and table row (mapped in §4.1); §7.1.1 to §7.1.10 (rails, refusal semantics, environment variables, route policy; OBS-W4-3); §3.1.1 carrier table; §3.3 "Usage & typed errors → stderr" and "Determinism pins"; §3.4 exit codes; §4.6 (sources, `auto` DB-only, `--upsert` not in prod; OBS-W4-2); §4.7; the §1 status lines. HDE Governance §3.1 "Public traffic (Reader/Aux)", "Admin ops windows (vendor override)", "Governance stance"; §2.0.10 "Prod posture"; §11.1.1 `bg:resolve` route-policy and mapped-cache paragraphs. HDE Mechanics Guide (`docs/pfcanon/PF14-Canon-HDE-Mechanics-Guide-v3.5.8.md`) §17.10.3 "BodyGraph resolver & vendor ingest (prod QA)" and §22 "SAFE Rails and Provider Gate" (defaults, keys-only logging, and the conjunction acquisition rules that OBS-W4-1 cites). Glow Infrastructure (`docs/pfcanon/PF07-Canon-Glow-Infrastructure-v2.3.3.md`) §2.4 "Production — Railway", §2.6, §2.7 "Any-shell terminal access", §8 policy and §8.1 key names |
| S08 | HDE-CLI-API-Vendor-Ref §4.5 (admin preview from `--pair-file`); §3.1.1 `aux_narrative_text` and `aux_suppressed_empty`; HDE Mechanics Guide §17.10.2 "Aux narratives (prod QA)" |
| Plans and route-policy statements | Plan Templates (`docs/pfcanon/PF27-Canon-Plan-Templates-v2.0.5.md`) "`bg:resolve --source vendor` route-policy posture", "`bg:resolve` nonclaim language", "Route-family proof requirement" (§9.6) |
| Release refresh | Implementation Plan v1.1 §10; Audit §5.1 and §7.3; WU-PR-03 result v2.0 §8; `AGENTS.md` "Release identity" and "HDE-EPIC040 admission addition"; WU-PR-02 lineage review v1.0 §7 (LR-O1 to LR-O3) |
| In-flight documents | Specification v1.1 rows S08 and S14, constraints "Release members", "Vendor override", "Override initiator", "Live QA", Exclusions; Plan v1.1 §3, §4, §5 (IF-1, IF-2), §6, §7 (common paragraph; WU-PR-04 block), §9 item 3, §10, §11 (R-2, R-3, R-8), §12, §13, §14; review v1.0 N4 and review v1.1 §4; Audit §6 S08 and S14, §7.1 (EC-7), §7.2 (DD-C1), §7.3, §7.5, §7.6; WU-PR-03 instruction v1.0 (structure) and lineage review v1.0 §7–§9 |
| Operative documentation | `AGENTS.md` (canon-first rule; closed rails and redaction; sole Index/Mirror writer; no hand edits; pytest readiness; PR descriptions; EPIC037 and EPIC038 validation entrypoints for the §5.8 tools) |
