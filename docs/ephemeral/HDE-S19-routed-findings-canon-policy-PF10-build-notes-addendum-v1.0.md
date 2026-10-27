---
artifact_type: PF10_BUILD_NOTES_ADDENDUM
addendum_id: HDE-S19-ROUTED-FINDINGS-CANON-POLICY-ADR-1
proposed_pf10_number: "2.1 (PF10 v13.8.9 on main carries no addenda: \"No current addenda\"; allocation and publication are the Product Owner's)"
authority: Nathan / Product Owner's request of 2026-10-27 to Isis, "ADR decision request from the Product Owner ... Decide D-1 to D-5 ... and draft your decision as one HDE Build Notes addendum record under docs/ephemeral/". The decisions are Isis's drafted ADR decisions; they take effect when the Product Owner publishes this addendum (HDE Governance §9.7.3; HDE Build Notes "Precedence, versioning, and scope" item 1). No approval prompt produced this addendum, and none is claimed
decision_brief: docs/ephemeral/HDE-S19-routed-findings-canon-policy-ADR-brief-v1.0.md (Master Scrum; on main via #765, adbacfa2; SHA-256 f7bd3052a65a311f65d1151b6c9c1bf4611ad185948f149cdb1b7dd5abe93b27)
source_record: docs/ephemeral/HDE-CRD-0002-S19-code-security-review-v1.0.md §4 "Confirmed, routed", §8 and §9 (reviewed head 1e97ba9b)
producing_session: Isis (Isis-54), Lead Developer, https://claude.ai/code/session_01ToyGWTKT1QqGQNNB2BDWJS
repository_head_read: origin/main adbacfa2 (#765). Outside docs/ephemeral/ and docs/pfcanon/, nothing has changed since 0adce9d9, so every cited code line is as the review and the brief found it
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.8.9.md, in full (10,569 bytes; "No current addenda")
capture_time_utc: 2026-10-27T02:30:00Z
page_ready_text: the H2 section below, from its heading to the end of this file. The "Canon relied on" block above the H2 is record-only and is not page text
incorporated_into: not yet
---

**Canon relied on** (read on `main` at `adbacfa2`; each section read in full):

* PF04-Canon-HDE-Governance v2.8.8: §2.0.6 (`EVIDENCE_PATHS_VALIDATED_OK`, repository-relative paths); §2.0.10 (`LOGS_KEYS_ONLY_OK`; `ENV_RAILS_POLICY_OK` and dev/admin gating); §3.1 "SAFE rails default ON" ("Public traffic (Reader/Aux)", "Admin ops windows (vendor override)", "Governance stance"); §4.1.4 "Rails posture — closed refusal; open conformance", including "Dev/admin APP\_ENV gating (dev/test/local only)"; §4.1.8 "Sanity pipeline & evidence skeleton (EPIC018+)", "Sanity log artifact"; §6.3.2 "Diagnostics and failure handling"; §7.1 to §7.1.5 "Keys-only logging"; §8.3 to §8.3.5 "Admin surfaces authentication & authorization"; §9.7.3.
* PF05-Canon-HDE-CLI-API-Vendor-Ref v2.5.4: §5.5 "Compat v1 (dev-only) route & parity harness"; §7.1.10 "Endpoint policy (explicit version-gated dual lineage)"; §7.1.11 "SAFE rails and production vendor override", including its implementation-state limits, and §7.1.11a to §7.1.11f; §7.2.0 "Contract and implementation posture".
* PF06-Canon-Change-Process-Guide v2.5.5: §0.1A (lanes; the agent-authored HDE Build Notes addendum form); §1.0.5 "Canon changes".
* PF07-Canon-Glow-Infrastructure v2.3.4: §2.2 "Environment facts" (shared database; Staging/QA in GitHub Codespaces; loopback client access); §2.4 "Env Deployment Inventory" (Production `APP_ENV=prod`, `SAFE_MODE=0`, `ALLOW_NETWORK=1`, `HD_API_BASE_URL` ending `/v2`; Development and QA `APP_ENV=dev`, `HD_API_BASE_URL` ending `/v2`).
* PF09.7-Canon-HDE-Build-Checklist-Coagulation v1.1.9: HDE-COAG006.5.
* PF10-HDE-Build-Notes v13.8.9, in full.
* PF12-Canon-HDE-Schemas-and-Artifacts v2.9.7: §1.2, "Canonical JSON gate artifacts (primary family plus legacy coexistence)"; §6.2.1 "External release attestation"; the Evidence Catalog entry "Canonical JSON and topology".
* PF14-Canon-HDE-Mechanics-Guide v3.5.9: §1.1 "Capabilities the repo must provide", the HDAPI v2 request-shaping and response-mapping mechanics; §27.3 "External release attestation"; §27.5 "Sanity pipeline (release & provenance)".
* PF27-Canon-Plan-Templates v2.0.6: "`bg:resolve --source vendor` route-policy posture".
* PF29-Canon-HDE-Users-Guide v1.0.3: §11.3 "Non-v2 legacy fallback"; §13.3 "Production/open-rails vendor BodyGraph acquisition"; §16 "Known limitations and nonclaims", including its troubleshooting rows.
* PF30.1-Canon-HDE-CRD-Records v0.9.2: the HDE-CRD-0002 record, "Deferred or residual work".
* In-flight and source: the decision brief and the S19 review named above; `AGENTS.md` ("EPIC036 docs posture", "Showcompat Live QA posture"); the precedent form of `docs/ephemeral/HDE-CRD-0002-PF10-build-notes-addendum-aq1-adr-v1.0.md`.
* Code read on `main` at `adbacfa2`: `engine/bodygraph/vendor_client.py` lines 102 to 153; `engine/bodygraph/resolver.py` lines 704, 915 to 1021, 1083; `engine/cli/main.py` lines 748 and 799; `engine/http/compat_handler.py` lines 108 to 173; `adapter/env_guard.py` lines 31 to 51; `adapter/http_reader.py` lines 901 to 907; `tools/evidence/run_canonical_json_gate.py` lines 1195 to 1205; `tools/evidence/run_sanity_pipeline.py` lines 328 to 347; `tools/evidence/build_release_attestation.py` lines 178 to 191, 603 to 617, 904 to 912; `tools/evidence/generate_v2_mapped_cache_evidence.py` lines 267 and 275; the tests named under D-2 and D-3; `.github/workflows/ci.yml` lines 51 and 322 to 324; `audit/gates/json_gate/canonical/json_gate_check_log.ndjson`.

## 2.1 Canon policy for the S19 routed security findings: production vendor gate scope, vendor route selection, compat route gating, evidence-tool output roots and gate-row content

Timestamp: 102726 02:30 (UTC). Details: Records the architecture decisions on five canon policy questions that HDE-CRD-0002's code security review left open when it routed findings S19-R01, S19-R02, S19-R03, S19-R05 and S19-R07 to the Product Owner. Each finding is rated Low. Each one needed a canon decision before an implementing change could fix it, because a fix would set policy that canon does not state or that canon states in conflict. Origin: the S19 review record (`docs/ephemeral/HDE-CRD-0002-S19-code-security-review-v1.0.md` §4, reviewed head `1e97ba9b`); the decision brief `docs/ephemeral/HDE-S19-routed-findings-canon-policy-ADR-brief-v1.0.md`; and the Product Owner's request of 2026-10-27 that Isis decide the brief's D-1 to D-5. Evidence: the canon and code readings named in the record's "Canon relied on" block, on `main` at `adbacfa2`.

### Decision and approval status

* **Decisions.** D-1 to D-5 are decided below. Isis drafted them as the ADR decisions for these findings. They are architecture decisions under Change Process Guide §1.0.5, and the Product Owner owns them (HDE Governance §9.7.3). Each takes effect as canon when this addendum is published. It then governs over the conflicting permanent text it names until that text is drained.
* **Chosen options.**

  | Decision | Finding | Choice | Option in the brief |
  | :- | :- | :- | :- |
  | D-1 | S19-R01 | The production vendor override gate applies to `hdctl showcompat --source vendor` and to conjunction vendor acquisition | A |
  | D-2 | S19-R02 | HDE CLI/API/Vendor Ref §7.1.10 governs: a base that does not end in exactly `v1` or `v2` fails closed, and the configured-base boundary is enforced | A |
  | D-3 | S19-R03 | `POST /api/compat/v1` is a dev/admin surface under HDE Governance §4.1.4; no credential is required while it stays one | A, with a rule that a credential is needed before any wider exposure |
  | D-4 | S19-R05 | The attestation builder claims an existing empty output root exclusively, writes only through paths it created, and deletes only what it created. `--log-path` is bounded | B, made exclusive |
  | D-5 | S19-R07 | Governed gate check rows carry closed issue tokens and repository-relative paths only, never exception text or absolute paths | A |

* **Independence.** Each decision stands alone. Each finding's fix belongs to the implementing change for Candidate CRD Items List item 9. These decisions are that change's ADR prerequisite, not the change itself.

### D-1 — The production vendor override covers showcompat and conjunction acquisition (S19-R01)

**Decision.**

* The production vendor override of HDE CLI/API/Vendor Ref §7.1.11 applies to every CLI path that acquires a chart from the vendor:
  * `hdctl bg:resolve --source vendor`;
  * `hdctl showcompat --source vendor`;
  * `hdctl showcompat --conjunction` whenever the invocation selects vendor acquisition for either party. Today that is any source other than `db` or `auto` (`engine/cli/main.py` line 799).
* Each of these paths applies, unchanged, the §7.1.11b classification, the §7.1.11c matrix and the §7.1.11e initiator rule.
* **The flag** `--allow-prod-vendor <AUTHORIZATION_REF>` is accepted by the three paths above and by no other command. Its syntax, single occurrence and value rules are unchanged (§7.1.11a).
* **Order.** The §7.1.11d order applies to each path. Its step 2 reads, for each command: "the invocation selects vendor acquisition". Supplying the flag to an invocation that selects no vendor acquisition is a CLI usage error, exit `64`. That covers `--source db`, `--source auto`, and conjunction with `db` or `auto`.
* **Scope of one authorization.**
  * One valid flag authorizes the bounded vendor acquisitions of one invocation: at most one acquisition per party, two for a pair.
  * It authorizes nothing §7.1.11d excludes: no write, no public Reader or Aux vendor traffic, no opening of a closed rail.
* **Audit.**
  * Each production-like invocation of these paths that reaches override evaluation writes one §7.1.11f event before any I/O.
  * The `command` field is exactly one of `bg:resolve`, `showcompat` or `showcompat:conjunction`. Every other field and exclusion is unchanged.
* **Error carrier.**
  * Policy refusals on `showcompat` use that command's existing canonical typed error carrier, with the same stable codes (`PROVIDER_PROD_OVERRIDE_REQUIRED`, `PROVIDER_PROD_OVERRIDE_INVALID`, `PROVIDER_AUDIT_UNAVAILABLE`, `PROVIDER_CONFIG_INVALID`) and exit `1`.
  * Every refusal has outbound-attempt count `0`.

**Basis.**

* HDE Governance §3.1 lets Ops run vendor calls in production and drives the vendor override by CLI flags. §7.1.11 then built that override for `bg:resolve` only.
* A gate that covers one of three paths to the same vendor, credentials and production shell does not gate production vendor access: any operator can reach the vendor through `showcompat`.
* Extending the delivered S14 machinery (classification, matrix, order, carrier, audit) keeps the existing capability. Pre-Glow Live QA uses `showcompat --source vendor` (`AGENTS.md`, "Showcompat Live QA posture"). The extension makes production runs authorized and audited.
* Option B would remove that capability in production. Option C would leave the §7.1.11 gate bypassable.

**Canon superseded or added to.**

* HDE CLI/API/Vendor Ref §7.1.11a: "accepted only by `hdctl bg:resolve --source vendor`" is superseded by the three-path scope above.
* HDE CLI/API/Vendor Ref §7.1.11d step 2: superseded as stated above.
* HDE CLI/API/Vendor Ref §7.1.11e: added to, with the `showcompat` carrier rule.
* HDE CLI/API/Vendor Ref §7.1.11f: the `command` rule "exactly `bg:resolve`" is superseded by the three values above.
* HDE CLI/API/Vendor Ref §7.1.11, implementation state: the limit "The gate covers only the command §7.1.11a names …" becomes a gap against this decision, not a decided limit.
* HDE Governance §3.1 is unchanged; this decision applies it.

**Drainage targets.**

* HDE CLI/API/Vendor Ref §7.1.11, §7.1.11a, §7.1.11d, §7.1.11e and §7.1.11f.
* HDE Users Guide §13.3, and §16 with its troubleshooting row for the three `PROVIDER_PROD_OVERRIDE_*` and `PROVIDER_AUDIT_UNAVAILABLE` codes.
* `AGENTS.md` "Showcompat Live QA posture": a production-like Live QA run needs the flag. This is a Product Owner-instructed edit.

**Consequences for tests, governed evidence and frozen captures.**

* New owner tests prove the §7.1.11c matrix, the order, the audit event and zero outbound attempts on refusal, for `showcompat --source vendor` and for vendor-selecting conjunction.
* Existing showcompat tests that run under closed rails are unaffected, because the rails refuse first (§7.1.11d step 3).
* Open-rails showcompat tests with an absent or unrecognized environment now refuse with `PROVIDER_CONFIG_INVALID`. CI sets `APP_ENV=dev` (`.github/workflows/ci.yml` line 51).
* No governed evidence family changes. Frozen `artifacts/cli/showcompat/` captures are closed-rails history and stay as recorded.

**Left undecided.** None in this decision.

### D-2 — Vendor route selection fails closed outside a terminal `v1` or `v2` (S19-R02)

**Decision.**

* **What governs.** HDE CLI/API/Vendor Ref §7.1.10 governs route selection and the configured-base boundary, for every resolver-selected vendor acquisition:
  * `bg:resolve --source vendor`;
  * compat chart acquisition by `showcompat` and conjunction, which uses the same classifier (`engine/bodygraph/resolver.py` line 704).
* **Selection.**
  * A terminal, case-sensitive `v2` segment selects `charts`. A terminal, case-sensitive `v1` segment selects `bodygraphs`.
  * Every other base fails with `PROVIDER_ROUTE_UNSUPPORTED` before credential projection or any external I/O. That includes an unversioned base, any other version, a nonterminal or case-variant marker, and multiple markers.
* **The base.** It must be absolute HTTPS, with a host and no userinfo, query or fragment, and end in exactly `v1` or `v2` (§7.1.10, "Configured-base boundary").
* **The `v1` path** is retained legacy selection, not fallback. Its retirement still needs the separately versioned decision §7.1.10 requires.
* **No fallback.** No non-v2 base reaches `bodygraphs` by fallback.
* **The two canon rules fit together as follows.**
  * §7.1.10's classification is the single permitted reading of a version from the configured base. It is one exact comparison of the validated terminal segment against the two allow-listed values, made once, before any route is built.
  * The selected route's resource, payload family and credential projection then come from that route's contract metadata, as HDE Mechanics Guide §1.1 requires.
  * HDE Mechanics Guide §1.1's prohibitions continue to govern everything else. Nothing may:
    * hardcode `/v1` or `/v2` as route-construction constants;
    * append or normalize a version;
    * select auth by path prefix;
    * key any other runtime behavior on a version string.
* **Classification label.** The emitted classification label `explicit_legacy_fallback`, for a terminal `v1` base, is kept unchanged as an existing wire value in governed evidence. It names the retained `v1` legacy selection and makes no fallback claim.

**Basis.**

* HDE Mechanics Guide §1.1 preserves v1 behavior "until the owning architecture and byte-contract homes decide whether v1 remains a fallback or is retired". It states only that non-v2 bases "MAY" keep the fallback.
* HDE CLI/API/Vendor Ref, the byte-contract home, has decided in §7.1.10. Its §7.2.0 already records "broad non-v2 legacy selection" as "a material gap against this contract".
* The current classifier reads any path segment, case-folded (`engine/bodygraph/vendor_client.py` lines 102 to 109). So:
  * a mistyped or unversioned base projects `HD_API_KEY` as `HD-Api-Key` to a legacy route;
  * a malformed base can carry the Bearer credential to an unintended URL.
* Every recorded environment configures a base ending in `/v2` (Glow Infrastructure §2.4: Production, Development and QA). Failing closed changes no recorded deployment.
* Option B would withdraw a fail-closed rule for no recorded need. Option C would close the base-boundary risk and leave the canon conflict open.

**Canon superseded or added to.**

* HDE Mechanics Guide §1.1: "Non-v2 configured bases MAY preserve explicit legacy BodyGraph fallback …" is superseded. A terminal `v1` base keeps the legacy route-family posture described there, with `HD-Api-Key` auth, governed geokey handling and no v2 BodyGraph-detail claim. No other non-v2 base selects a route.
* HDE Mechanics Guide §1.1, "infer runtime behavior from vendor API version path strings": added to, with the single permitted classification above.
* HDE Users Guide §11.3, §13.3 ("With a non-v2 configured base, explicit legacy fallback may proceed …") and §16 ("For non-v2 configured bases, explicit legacy BodyGraph fallback is preserved"): superseded. The legacy route is reached only with a terminal `v1` base.
* HDE CLI/API/Vendor Ref §7.1.10: added to. Its scope covers compat chart acquisition as well as `bg:resolve`.
* Plan Templates "`bg:resolve --source vendor` route-policy posture": its category "explicit legacy fallback" reads as the terminal-`v1` legacy selection.

**Drainage targets.**

* HDE Mechanics Guide §1.1.
* HDE Users Guide §11.3, §13.3 and §16.
* HDE CLI/API/Vendor Ref §7.1.10 (scope sentence) and §7.2.0 (the gap, once the implementing change delivers).
* Plan Templates "`bg:resolve --source vendor` route-policy posture".
* `AGENTS.md`, "EPIC036 docs posture" and the EPIC038 posture lines that say non-v2 bases keep the fallback. This is a Product Owner-instructed edit.

**Consequences for tests, governed evidence and frozen captures.**

* The cost is smaller than the brief records. Each pin the brief and the S19 review cite for the fallback uses a terminal `v1` base, so each still holds under this decision:
  * `tests/bodygraph/test_bg_resolve_route_policy.py` line 86 classifies `https://vendor.test/v1`;
  * `tests/bodygraph/test_bg_resolve_v2_mapped_cache.py` line 237 resolves with `https://vendor.test/v1`;
  * the governed EPIC038 predicate `explicit_legacy_fallback` (`tools/evidence/generate_v2_mapped_cache_evidence.py` line 275) is computed from a run with `https://fixture.invalid/v1` (line 267).

  Their names and descriptions say "fallback" and are corrected by their owners in the implementing change. The governed evidence bytes need no regeneration for this decision.
* `tests/bodygraph/test_hde_epic038_mapped_cache_smoke.py` line 118 tests the smoke tool's own preflight, which refuses every non-v2 base. It is unaffected.
* The implementing change adds owner tests, with zero I/O, for each refused shape:
  * unversioned, `v3`, nonterminal, case-variant and multiple-marker bases;
  * bases carrying userinfo, query or fragment;
  * a non-HTTPS base.
* Two low-level request-builder tests use the unversioned base `https://vendor.test` (`tests/bodygraph/test_vendor_client.py` lines 548 and 569). They change only if the implementing change validates the boundary inside the low-level builder as well. This decision requires the boundary before any resolver-selected route is built.
* Frozen EPIC036 and EPIC037 captures stay as history. They record the earlier posture at capture time and are not rewritten.

**Left undecided.**

* Retirement of the `v1` legacy route stays a separate, versioned decision (§7.1.10).

### D-3 — `POST /api/compat/v1` is a dev/admin surface (S19-R03)

**Decision.**

* **Classification.** The compat namespace, `/api/compat/v1` and its descendants, is a dev/admin-only surface under HDE Governance §4.1.4. HDE CLI/API/Vendor Ref §5.5 already calls the route "dev only", "development-only" and "internal admin".
* **Gate order.** On every method, before any compat computation, database read or vendor call:
  1. **Production-like posture**, as §5.5 resolves it, keeps its current response. That posture is `prod`, `production` or `live`, read from trimmed, case-folded nonempty `APP_ENV`, otherwise `ENGINE_ENV`. The response is `404`, `error_v1` with `code=ERR_NOT_FOUND`, and `Cache-Control: no-store`; `HEAD` carries no body.
  2. **Any other request** is served only when `APP_ENV` is exactly `dev`, `test` or `local`, with no trimming, no case-folding and no default.
     * A missing, empty or other value refuses with the writer-style refusal the dev/admin HTTP surfaces use: `ERR_WRITER_FORBIDDEN`, status `403`, `Cache-Control: no-store`, no `ETag`, and no body on `HEAD`.
     * `ENGINE_ENV` never admits the surface.
  3. The existing method, probe and `POST` rules of §5.5 apply.
* **Authentication.**
  * No credential is required while the surface is admitted only under `APP_ENV` exactly `dev`, `test` or `local`. This matches every other dev/admin surface under §4.1.4.
  * §5.5's "authenticated" and "internal authentication" are withdrawn: no mechanism exists in canon or code.
* **Wider exposure.** Before the compat route is served in any other environment, a later decision must:
  * require the HDE Governance §8.3.2 admin credential, or an equivalent credential pinned in HDE CLI/API/Vendor Ref;
  * add the §8.3.4 logging rules.
* **Residual risk, accepted and recorded.**
  * A dev, test or local process connected to the shared production database serves stored-user compat results to whoever reaches its port. The Staging/QA HD Engine is a GitHub Codespace on that database (Glow Infrastructure §2.2), with `APP_ENV=dev` (§2.4).
  * That exposure is controlled by where the process listens, the documented loopback access of Glow Infrastructure §2.2, not by this route. It is the same posture as every other dev/admin surface.

**Basis.**

* HDE Governance controls authority and permissions (Change Process Guide §0.1A). Its §4.1.4 rule is explicit:
  * dev/admin surfaces "MUST" allow exactly `dev`, `test` and `local`;
  * they "MUST NOT assume a default".
* The current guard refuses only production-like values (`engine/http/compat_handler.py` line 112). `adapter/env_guard.py::_compute_env_mode` returns `dev` when both variables are unset, and passes `staging` and unknown values through (lines 31 to 51). So the route serves unauthenticated results in exactly the cases §4.1.4 forbids.
* Gating closes that with a rule canon already states and a gate the code already has (`adapter/http_reader.py` lines 901 to 907).
* A credential for a dev-only route (options B and C) adds secret, transport and rotation machinery that removes no exposure once the gate holds. HDE-COAG006.5 scopes that machinery to admin bundles, and this decision does not widen that subtask.

**Canon superseded or added to.**

* HDE CLI/API/Vendor Ref §5.5, "Validation and environment gating": added to, with the dev/admin gate as step 2.
* HDE CLI/API/Vendor Ref §5.5, "Success body (dev/internal; authenticated)", and "Parity (clarified)" ("authenticated `POST /api/compat/v1`"): "authenticated" is superseded.
* HDE Governance §4.1.4: added to, naming the compat namespace as a dev/admin surface.
* HDE Governance §8.3 is unchanged. Its admin-bundle scope stays as written.

**Drainage targets.**

* HDE CLI/API/Vendor Ref §5.5.
* HDE Governance §4.1.4.
* HDE Users Guide §16: the "POST /api/compat/v1 is not production-public" line and the troubleshooting row "HTTP 404 from POST /api/compat/v1 in prod" gain the non-production refusal.

**Consequences for tests, governed evidence and frozen captures.**

* The existing production-hiding tests (`tests/http/test_compat_endpoint_contract.py` lines 224 to 261) keep their assertions.
* New owner tests prove the `403` refusal, with zero compat work, for each of these: an unset or empty `APP_ENV`, `staging`, `stage`, an unknown value, case and whitespace variants, and `ENGINE_ENV=dev` with `APP_ENV` unset.
* Compat tests that rely on an unset `APP_ENV` meaning `dev` set `APP_ENV` explicitly. CI already runs with `APP_ENV=dev` (`.github/workflows/ci.yml` line 51).
* The governed compat-route proof bytes of §5.5 (`artifacts/compat/AB.json`, `BA.json`, `identity_hash.txt`) are produced under a dev posture and need no change.

**Left undecided.** None in this decision.

### D-4 — Evidence tools own their output: exclusive claim, no symlink writes, scoped cleanup (S19-R05)

**Decision for the release attestation builder** (`tools/evidence/build_release_attestation.py`):

* **Documented interface unchanged.** The documented invocation `--output <external-empty-directory>` is unchanged. An absent output root is created by the builder. An existing, empty, non-symlinked directory outside the source repository is accepted.
* **Exclusive claim.**
  * Before any other write, the builder claims the output root exclusively for the run, by an atomic create that fails if another run holds the root.
  * A root it cannot claim refuses with a typed failure code before any write.
  * The claim adds no member to a successful bundle beyond the `hde.release_attestation.v1` contract.
* **No writes through symlinks.**
  * Every write below the output root goes to a path this run created.
  * A pre-existing or substituted symlink anywhere below the root is refused, not followed.
* **Scoped cleanup.**
  * On failure, the builder removes only files and directories this run created, then writes its failure receipt.
  * It never removes a path it did not create.
* **Unchanged.** HDE Schemas & Artifacts §6.2.1 and HDE Mechanics Guide §27.3 still govern everything else: their refusals, the isolated build, the byte-stable checkout and the contracts.

**Decision for the sanity pipeline** (`tools/evidence/run_sanity_pipeline.py --log-path`):

* **Inside the repository,** the only accepted target is the canonical log `audit/gates/sanity_pipeline/sanity_pipeline.log`.
* **Outside the repository,** a target is accepted only when it meets all of these:
  * it is not a symlink, and no component of its path is a symlink;
  * its parent directory exists;
  * it names a regular file or no existing file.
* **Refusals.** A refused target fails with a typed, numeric-free error before any step runs or any byte is written.

**Basis.**

* Canon accepts an existing empty destination. Changing the documented command line (option A) would change every caller and runbook. The flaw the review proved is not the empty directory: it is non-exclusive use, symlink following and cleanup of files another run made.
* The exclusive claim removes the concurrency hole that plain option B leaves, without changing the interface.
* For `--log-path`, canon is silent. Bounding the target to the canonical log, or to a non-symlinked external file, keeps CI's `$RUNNER_TEMP` use. It removes the path by which an operator's argument could overwrite a governed file (line 347 resolves symlinks).

**Canon superseded or added to.**

* HDE Schemas & Artifacts §6.2.1 and HDE Mechanics Guide §27.3: added to, with the exclusive-claim, no-symlink-write and scoped-cleanup rules. The refusal list stands.
* HDE Governance §4.1.8 "Sanity log artifact", and HDE Mechanics Guide §27.5: added to, with the `--log-path` bound.

**Drainage targets.**

* HDE Schemas & Artifacts §6.2.1.
* HDE Mechanics Guide §27.3 and §27.5.
* HDE Governance §4.1.8.

**Consequences for tests, governed evidence and frozen captures.**

* New owner tests cover:
  * a concurrent second run refused before writing;
  * a symlink planted below the root refused;
  * a failing run leaving another run's files intact;
  * `--log-path` refusing a symlink, a symlinked parent and a non-canonical path inside the repository.
* The builder's success and failure contracts and the canonical sanity log bytes do not change. CI's invocation (`.github/workflows/ci.yml` lines 322 to 324) is unchanged.

**Left undecided.** The mechanism of the exclusive claim, within the rules above, belongs to the implementing change.

### D-5 — Governed gate check rows carry closed tokens and repository-relative paths only (S19-R07)

**Decision.**

* **Scope.** A governed gate check row is a governed log under HDE Governance §2.0.10 (`LOGS_KEYS_ONLY_OK`) and §7.1. That covers each row of `audit/gates/json_gate/canonical/json_gate_check_log.ndjson` and `json_gate_compare_log.ndjson`, and of any other PF12-governed gate family.
* **Issue entries.**
  * Each issue entry is a closed token.
  * An exception contributes its type name at most, as `validation_error:<ExceptionType>`.
  * No row carries exception message text, library message text or a stack trace.
* **Paths.** Every path a row records is repository-relative (HDE Governance §2.0.6). No row carries an absolute or machine-local path.
* **Diagnostics.** Detail for diagnosing a failing run goes to the tool's stderr, which is not governed evidence.

**Basis.**

* HDE Governance already states the principle:
  * operational logs are keys-only, with "No free text" and errors as typed tuples that "never echo vendor or body text" (§7.1, §7.1.2, §7.1.4);
  * governed logs are keys-only (§2.0.10);
  * physical paths are repository-relative (§2.0.6).
* Exception text and absolute paths make rows machine-dependent and non-deterministic, which a governed gate's rows must not be.
* Option B keeps library text, which varies by version.

**Canon superseded or added to.**

* HDE Governance §2.0.10 `LOGS_KEYS_ONLY_OK`: added to, naming governed gate check rows as governed logs.
* HDE Schemas & Artifacts §1.2, "Canonical JSON gate artifacts": added to, with the row-content rule.
* HDE Governance §6.3.2 is unchanged; its database scope stands.

**Drainage targets.**

* HDE Governance §2.0.10.
* HDE Schemas & Artifacts §1.2 "Canonical JSON gate artifacts", and the Evidence Catalog entry "Canonical JSON and topology".

**Consequences for tests, governed evidence and frozen captures.**

* The committed `json_gate_check_log.ndjson` and `json_gate_compare_log.ndjson` carry no `validation_error` or `json_error` entry today: on `main` at `adbacfa2`, all 31 rows of each have `"issues":[]`. So publishing this rule changes no current governed bytes.
* `tools/evidence/run_canonical_json_gate.py` line 1205, and its `json_error:<msg>` entry at line 1197, change in the implementing change. An owner test proves a failing target yields only the closed token.
* Frozen gate captures stay as recorded.

**Left undecided.** None in this decision.

### Scope, exclusions and nonclaims

* **Not decided here.**
  * S19-R04 (owner tools acting on any invocation) and S19-R06 (a frozen-family generator's relative script path). The brief does not request them; their owners are named in S19 review §4.
  * X-01 to X-04, which raise no policy question (S19 review §8).
  * Candidate CRD Items List item 10.
* **Establishes no:**
  * code, test, tool, workflow, schema, configuration or governed-evidence change;
  * CRD identity, Specification or implementation authority for item 9;
  * QA verdict, acceptance, PF09 or PF30 movement, board change, deployment or closure.
* **No other document is written.** No PF canon document and no repository document is edited, and no ADR file is written under `docs/adr/`. The decisions stand as canon from publication and as drainage targets until drained.
* **Current facts.** The facts above were read on `main` at `adbacfa2`. A later change to the cited code or canon makes the matching consequence a fresh question; it does not change the decision.

### Dependencies and unresolved obligations

* **Item 9.** The implementing change is Candidate CRD Items List item 9 (state Open, review status New). This addendum is its approved-ADR prerequisite under Change Process Guide §1.0.5, once published. Item 9's review, CRD identity and Specification remain the Product Owner's.
* **Drainage.** The drainage targets above are unperformed. The permanent-canon edits under each decision are canon drainage. The `AGENTS.md` lines under D-1 and D-2 need the Product Owner's explicit instruction.
* **Brief correction.** The brief records that D-2 option A replaces two route-policy tests and the `explicit_legacy_fallback` predicate. On `main` all three use a terminal `v1` base and hold under D-2; only their naming changes.

### Evidence

* Decision brief: `docs/ephemeral/HDE-S19-routed-findings-canon-policy-ADR-brief-v1.0.md`, [amthorn78/glow-hdengine-v2\#765](https://github.com/amthorn78/glow-hdengine-v2/pull/765), merged as `adbacfa2`.
* Source review: `docs/ephemeral/HDE-CRD-0002-S19-code-security-review-v1.0.md` §4, §8 and §9, reviewed head `1e97ba9b`.
* Repository: `main` at `adbacfa2`. The files and lines are cited under each decision.
* Prior record of item 9: HDE CRD Records, the HDE-CRD-0002 record, "Deferred or residual work" ("no disposition yet").
