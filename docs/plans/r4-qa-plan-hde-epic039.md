# HDE-EPIC039 Live QA Plan

## 1) Live QA Plan

### Front matter

Epic ID: HDE-EPIC039
Plan type: Live QA Plan / Runbook
Prompt family: AUTHORING
Execution venue: GitHub Codespaces (preferred) | Other: Not selected
Approval sentinel: final line of this document

Venue-specific claim: NOT CLAIMED

Why venue can affect the result: NOT APPLICABLE

Required venue evidence: NOT APPLICABLE

Effect of missing venue evidence: NOT APPLICABLE

The execution-venue field is descriptive and records the preferred operator surface. Venue is not an acceptance axis for these closed-rails, repository-local checks.

Target environment: staging/QA — GitHub Codespaces repository workspace
Plan revision: r4
Date (UTC): 2026-08-22
Operators (names-only): Product Owner

PF07 infrastructure posture: PF07-derived.

| Infrastructure fact used by this plan | Exact PF07 fact and locator                                                                                                                         | Plan use                                                     |
| ------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| GitHub Codespaces QA console          | PF07 — Glow Infrastructure, §2.6 identifies GitHub Codespaces for `amthorn78/glow-hdengine-v2` as the QA console and artifact sink, not production. | Preferred execution venue and target QA workspace            |
| Repository identity                   | PF07 — Glow Infrastructure, §5.1 identifies `amthorn78/glow-hdengine-v2` and its governed `audit/` layout.                                          | Repository checkout prerequisite and source-routing identity |
| Stable epic QA root                   | PF07 — Glow Infrastructure, §§2.8 and 5.1 establish `audit/qa/<epic-id>/...` as the canonical governed QA-root pattern.                             | Concrete root `audit/qa/hde-epic039/`                        |

PF07-gap facts: none for this runbook. No executable step requires a provider project, deployed service, base URL, port, database instance or schema, secret, or service-start command. The determinism pins and closed-rails variables below are QA controls, not additional infrastructure claims.

“Applicable, active, non-superseded PF10 addenda supersede conflicting PF-Canon only for the exact scope they address; otherwise follow PF-Canon. A formally approved bounded Product Owner rescope may supersede conflicting PF-Canon only for the exact decision it adjudicates.”

When a formally approved bounded Product Owner rescope applies, identify the exact approved decision, any transferred later-PR work, the preserved boundaries, the preserved nonclaims, and the PF drain candidates.

#### Canon set (explicit; stable references only)

* PF10 — HDE Build Notes:

  * Addendum 2.5 — Require budget-efficient CI remediation in HDE-EPIC039
  * Addendum 2.6 — HDE-EPIC039 PR-01 Lineage
  * Addendum 2.7 — HDE-EPIC039 PR-02 Lineage and Review-Process Correction
  * Addendum 2.8 — Require Automated CI Budget Control and Supersede Manual Push Circuit Breakers
  * Addendum 2.9 — HDE-EPIC039 PR-03 Lineage
  * Addendum 2.10 — HDE-EPIC039 PR-04 Automated CI Remediation and HDE-EPIC038 Closeout-Layer Removal
  * Addendum 2.11 — HDE-EPIC039 PR-05 Authorized Scope Expansions and Proof-Boundary Decisions
  * Addendum 2.12 — HDE-EPIC039 PR-05 Generic Feedback-Free Closeout Lifecycle
  * Addendum 2.14 — HDE-EPIC039 D3 PF09 Row-Closure Authorization
  * Addendum 2.16 — HDE-EPIC039 Post-Implementation Audit Analysis and Required Evidence-Canon Drainage

* PF04 — HDE Governance — token registry and acceptance invariants; this runbook makes no acceptance-token claim.

* PF07 — Glow Infrastructure, §§2.6, 2.8, and 5.1 — GitHub Codespaces QA-console posture, repository identity, and governed epic QA-root pattern.


* PF06 — Epic Process Guide, §0.4.1 — Discovery and QA RCA / Doc Delta execution deliverables.

* PF09.1 — HDE Build Checklist — Calcination:

  * HDE-CALC002.2 — Canonical JSON rules
  * HDE-CALC002.3 — Arrays-as-sets semantics
  * HDE-CALC003.10 — Indexing & parity CI gates
  * HDE-CALC003.11 — Evidence index touch discipline
  * HDE-CALC003.13 — Canonical pytest invocation for QA & CI
  * HDE-CALC003.14 — QA harness discipline (tooling vs behavior, commands, emptiness)
  * HDE-CALC003.15 — Acceptance map & QA harness viability check
  * HDE-CALC003.21 — HDE-EPIC038 closeout subsystem removal and CI-cost cleanup
  * HDE-CALC003.22 — Feedback-free closeout lifecycle reachability

* PF12 — HDE Schemas and Artifacts, §§4.1, 4.2, 6.2.2, and 8.3 — structured-data, evidence-integrity, and feedback-free-candidate obligations carried into the proof steps below.

* PF19 — Glow QA Guide, §§2.2.5 and 3.4.10 — causal tooling classification and semantic normalization.

* PF27 — Canon Plan Templates, Live QA Plan — structure, evidence, headers, Step-0B, closeout, and review guardrails.

PF20 is not used as a requirements source.

### Scope statement

This plan evaluates:

* D0 — dependency readiness, protected Doc Delta capture, discovery, and QA evidence bootstrap.
* D1 — deterministic structured-data representation, declared set semantics, and corpus invariants.
* D2 — coherent evidence publication, integrity, parity, provenance, and duplicated Doc Delta agreement.
* D3 — causal QA classification, semantic declaration propagation, and current-versus-historical identity.
* D4 — change-aware CI behavior and continuing retirement of obsolete epic-specific automation.
* D5 — feedback-free closeout derivation, coherent candidate publication, and reusable-capability-only scope.

This plan explicitly excludes:

* Live vendor, network, production, deployed-service, database, public Reader, and external API behavior.
* Creation or validation of a real HDE-EPIC039 closeout candidate.
* Deployment, release, migration, OPS, implementation remediation, PR activity, or repository administration.
* Product Owner acceptance, epic closure, board movement, PF09 status editing, or permanent-canon drainage.
* New acceptance tokens, acceptance maps, token-evidence matrices, routes, environment variables, or public contracts.

#### PF10 overrides / conflicts (if any)

* PF10 §2.14 supersedes PF10 §2.9 only where §2.9 withheld closure support for HDE-CALC003.13, HDE-CALC003.14, and HDE-CALC003.15. It does not claim Live QA PASS or epic closure.
* PF10 §2.16 establishes no new implementation, remediation, OPS, or PF09 task. PF14 publication ownership and PF04 Machine Mirror self-reference wording remain later, Product Owner-owned canon-drain candidates.
* PF10 §§2.11–2.12 establish a reusable closeout capability but expressly do not establish a real HDE-EPIC039 candidate.
* The Product Owner’s bounded authoring instruction for this plan makes PF23 consultation conditional on an unresolved Repo-locus question. Direct Repo validation resolved every required locus, so PF23 was not consulted and creates no check, token, or deliverable.

### Open-Rails Live QA Requirement for production-affecting epics

Classification: this runbook tests repository-local deterministic data, evidence, QA-harness, CI-definition, and reusable closeout behavior under closed rails. It makes no production-affecting or externally observed claim.

Open-rails Live QA is omitted.

Authorization: the Product Owner’s bounded task explicitly limits this plan to the reusable capability actually delivered and prohibits live external calls during plan preparation. The runbook preserves that boundary during execution.

Production claim not made: no deployed behavior, external integration, vendor response, secret binding, public Reader behavior, production CLI/API behavior, or real closeout candidate is proved.

Later open-rails requirement: not required for this repository-local QA scope. Any future production use or real candidate validation requires its own approved plan and target-specific rails posture.

### PF23 anchors

PF23 was not consulted because direct Repo validation and the completed path-proof discovery record left no unresolved ownership, existence, component, or terminology question. This is a bounded source-routing decision for this authoring event only.

No PF23 acceptance token, evidence output, update, or operator action is created.

### Environment and rails posture

#### Determinism pins (canonical pins only)

Every command below carries:

* LC_ALL=C
* LANG=C
* TZ=UTC

No additional determinism pin is introduced.

#### Rails posture (explicit)

Default rails for every check:

* SAFE_MODE=1
* ALLOW_NETWORK=0
* APP_ENV=test

Rails changes by check: none.

No command may contact an external service or require a credential. If a selected test unexpectedly requires open rails, a vendor target, or a secret, classify the affected check as TOOLING_BLOCKED and stop. Do not change the rails in flight.


#### No VCS mutation or preplanned-commit gate (hard)

This runbook contains no checkout, branch creation, commit, merge, rebase, pull, push, tag, PR, reset, clean, stash, or other state-changing VCS action.

The QA-created helper may execute only these read-only source-provenance queries:

* `git rev-parse --show-toplevel`
* `git rev-parse HEAD`
* `git symbolic-ref --short -q HEAD`
* `git status --short --untracked-files=all`
* `git remote get-url origin`

Step-0B must capture their actual results in `audit/qa/hde-epic039/00_meta/discovery.json` and bind the same query sequence into the Step-0B primary log. The governed record must include the actual HEAD, branch or `DETACHED`, working-tree status, normalized repository route, approved runner entrypoint, plan revision, venue preference, and venue-specific-claim posture.

Equality to a preplanned commit is not required and does not control readiness, routing, PASS, or FAIL. Working-tree status is descriptive and non-gating. A failure of the required read-only queries or inability to establish the current repository identity is `TOOLING_BLOCKED`, not `FAIL_BEHAVIOR`.

Required current code posture means:

* the repository route resolves to `amthorn78/glow-hdengine-v2`;
* the reported repository root is the root used by the harness;
* the current QA manifest-entry validator and close-pack HEAD/tree readers are importable through their Repo-confirmed interfaces;
* Step-0B validates those interfaces before PASS; and
* every later check preflights its exact current selector and entrypoint before behavior execution.

These validations prove that the required current code surfaces are available. They do not make the captured commit identity an acceptance predicate.

### PO inputs needed

Required external inputs: none.

Required execution prerequisites:

* PF07-derived repository checkout: an accessible checkout of `amthorn78/glow-hdengine-v2` under PF07 §§2.6 and 5.1.
* PF07-derived QA console: a shell opened at that repository root in GitHub Codespaces under PF07 §2.6.
* Product Owner authorization to execute this approved runbook.
* Python available as `python`.
* Git available for the five read-only source-provenance queries above.

No secrets, URLs, ports, credentials, auth headers, user identities, or live targets are required.

If the repository root, Python, or the read-only Git queries are unavailable, stop before Step-0B and classify execution as TOOLING_BLOCKED. No installation, checkout, pull, reset, or alternate-repository action is authorized by this runbook.

### Evidence posture and directory structure

#### Epic QA root normalization (required)

Stable epic QA root:

`audit/qa/hde-epic039/`

Infrastructure classification: PF07-derived. PF07 §§2.8 and 5.1 establish `audit/qa/<epic-id>/...` as the governed QA-root pattern; this plan substitutes the concrete lowercase epic ID.

The root is Repo-confirmed at the reviewed baseline. Its existing proof-bearing Doc Delta record must be preserved.

#### Check-centric, single-root evidence posture (normative)

Each executed check writes one canonical primary log and one required sibling receipt proof under its concrete check directory. Every primary log must list its receipt proof in `evidence_artifacts`, and the proof must validate the log’s current path, SHA-256, and size before the receipt can contribute trusted PASS.

The shared current-state manifest is:

`audit/qa/hde-epic039/qa_step_logs_manifest.json`

Its required sibling proof is:

`audit/qa/hde-epic039/qa_step_logs_manifest.json.path_proof.txt`

No run ID, per-run directory, “latest” selector, or alternate evidence root is permitted.

#### Required layout and initial artifact posture

| Artifact                                                                        | Locus class             | State before execution               |
| ------------------------------------------------------------------------------- | ----------------------- | ------------------------------------ |
| `audit/docdeltas/hde-epic039_doc_deltas.md`                                     | Repo-confirmed existing | PRESENT                              |
| `audit/docdeltas/hde-epic039_doc_deltas.md.path_proof.txt`                      | Repo-confirmed existing | PRESENT                              |
| `audit/qa/hde-epic039/00_meta/doc_deltas.md`                                    | Repo-confirmed existing | PRESENT                              |
| `audit/qa/hde-epic039/00_meta/doc_deltas.md.path_proof.txt`                     | Repo-confirmed existing | PRESENT                              |
| `audit/qa/hde-epic039/00_meta/qa_runner.py`                                     | QA-created              | NOT RUN                              |
| `audit/qa/hde-epic039/00_meta/discovery.json`                                   | QA-created              | NOT RUN                              |
| Fourteen concrete `primary.log` paths listed in the Check Blocks                | QA-created              | NOT RUN                              |
| Fourteen concrete `primary.log.path_proof.txt` paths listed in the Check Blocks | QA-created              | NOT RUN                              |
| `audit/qa/hde-epic039/qa_step_logs_manifest.json`                               | QA-created              | NOT RUN                              |
| `audit/qa/hde-epic039/qa_step_logs_manifest.json.path_proof.txt`                | QA-created              | DEFERRED until closeout finalization |
| `audit/qa/hde-epic039/00_meta/qa_rca_doc_delta_summary.md`                      | QA-created              | DEFERRED until closeout finalization |
| `audit/qa/hde-epic039/00_meta/qa_rca_doc_delta_summary.md.path_proof.txt`       | QA-created              | DEFERRED until closeout finalization |

#### Step-log header schema expectations (required; v2)

New primary logs use `pf27.step_log_header.v2`.

The status is exactly one of `PASS`, `FAIL_BEHAVIOR`, `FAIL_TOOLING`, `TOOLING_BLOCKED`, or `PARKED`. `WARN` is an annotation or log-body severity, not a terminal outcome. A native runner's skipped result does not map blindly to a governed outcome: authorized pre-execution non-performance is `PARKED`; an unavailable mandatory prerequisite is `TOOLING_BLOCKED`. `NOT RUN` and `DEFERRED` remain artifact-inventory states under the QA planning QoS contract, not step-log statuses.

Exact status predicates:

* `PASS`: all mandatory prerequisites are established; the intended command or approved proof action reaches its decisive point; every in-scope predicate passes; required evidence is present and trustworthy; the check's `primary.log` is in `evidence_artifacts`; status-specific schema validation passes; `exit_code` is `0`; and any token claims are explicit and governance-valid. A tokenless check may pass with both token arrays empty.
* `FAIL_BEHAVIOR`: prerequisites and QA tooling are trustworthy, behavior is exercised, and observed product, runtime, or domain behavior violates an explicit in-scope predicate. Do not use it for missing tools, credentials, open-rails authorization, malformed evidence, or an invalid harness.
* `FAIL_TOOLING`: the QA mechanism, validator, harness, evidence writer, or proof pipeline is present and attempted but malfunctions, violates its contract, or produces untrustworthy evidence. The product or domain predicate remains unproven unless an independent trustworthy proof establishes it.
* `TOOLING_BLOCKED`: a required check cannot reach the behavior-decisive point because a prerequisite, dependency, approved target, authorization, credential presence, required entrypoint, required environment fact, or safe execution rail is unavailable or unresolved. No product-behavior verdict is permitted.
* `PARKED`: the check is intentionally not attempted under an explicit scope exclusion, supersession, or authorized deferral recorded before the outcome is known. Record the reason, authority or controlling source, affected acceptance claim, and reactivation condition. `PARKED` is not PASS and cannot satisfy a token or required Human Design predicate.

Causal precedence:

1. `PARKED` is available only for a pre-existing authorized non-execution decision; attempted execution cannot be hidden by parking.
2. Invalid or untrustworthy attempted tooling or evidence selects `FAIL_TOOLING`.
3. Otherwise, a missing mandatory prerequisite that prevents behavior-decisive execution selects `TOOLING_BLOCKED`.
4. Otherwise, trustworthy execution that proves the behavior predicate false selects `FAIL_BEHAVIOR`.
5. `PASS` is available only after every mandatory predicate is affirmatively satisfied.

Required v2 keys:

| Key                  | Contract                                                           |
| -------------------- | ------------------------------------------------------------------ |
| `schema_version`     | Exact value `pf27.step_log_header.v2`.                             |
| `timestamp_utc`      | Actual finalization time in RFC 3339 UTC form ending in `Z`.       |
| `check_id`           | Non-empty stable ID matching this plan.                            |
| `check_name`         | Non-empty name matching this plan.                                 |
| `status`             | One exact value from the five-status set.                          |
| `status_reason`      | Empty only for `PASS`; causal explanation otherwise.               |
| `command`            | Exact executed command sequence; empty only if nothing ran.        |
| `command_provenance` | Truthful command source.                                           |
| `exit_code`          | Actual integer when a command ran; `PASS` requires `0`.            |
| `evidence_artifacts` | Includes the check’s own `primary.log` and relied-on artifacts.    |
| `captured_env`       | Actual secret-safe values for the canon-defined environment names. |
| `pf_refs`            | Exact in-document PF titles only.                                  |
| `intended_tokens`    | Explicit array; empty for this plan.                               |
| `claimed_tokens`     | Explicit array; empty for this plan.                               |

Header serialization is UTF-8 compact JSON with lexicographically sorted object keys, no BOM, and exactly one terminating LF.

### Mandatory Step-0 artifacts

> `Step-0A` is reserved for identifier compatibility. PF27 does not currently define a reusable Step-0A contract. Existing artifact-specific or historical Step-0A records do not create that contract. Plans must not invent Step-0A obligations. Any future reusable Step-0A definition requires an explicit PF27 revision and migration decision.

#### Step-0B — Doc Delta Capture (mechanical; runbook self-honesty)

Step-0B verifies and preserves the existing proof-bearing Doc Delta pair. It must not replace either file with a blank or “no deltas” scaffold.

Moon Loop authorization: not authorized by this runbook.

Dependency readiness receives one closed-rails preflight attempt. This runbook authorizes no package installation, dependency activation, network resolution, or dependency-remediation rerun.

If Python, pytest, jsonschema, Git, a required Repo entrypoint, or another mandatory dependency is unavailable, record `TOOLING_BLOCKED`, stop the QA ladder, and run closeout finalization. Do not install, fetch, substitute, or retry within this runbook.

Any helper defect, product/test change, evidence-generator change, governed-artifact change outside this QA root, behavior failure, or dependency remediation requires a separately approved plan change or implementation route.

#### Step-0C — Prod handshake (identity-only) when target is prod-like

Not applicable. The target is a closed-rails development workspace, and no production-like target is used.

### Runbook Check Matrix


| check_id                    | check name                        | D-goal | rails  | commands                          | expected result                                                                                                                                | primary evidence                                                    | additional deliverables                               | tokens | PF anchors                    |
| --------------------------- | --------------------------------- | ------ | ------ | --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- | ----------------------------------------------------- | ------ | ----------------------------- |
| `step-0b-doc-delta-capture` | Doc Delta and discovery bootstrap | D0     | closed | Exact commands in its Check Block | PASS only after dependency readiness, pair identity, proofs, source provenance, routing provenance, and required current code posture validate | `audit/qa/hde-epic039/checks/step-0b-doc-delta-capture/primary.log` | Discovery artifact; primary-log proof; manifest entry | `[]`   | PF27; PF10 §§2.7, 2.9         |
| `po-001`                    | Deterministic structured outputs  | D1     | closed | Command 1 in its Check Block      | PASS only if all selected deterministic and fail-closed tests pass                                                                             | `audit/qa/hde-epic039/checks/po-001/primary.log`                    | Primary-log proof; manifest entry                     | `[]`   | PF10 §2.6; PF12 §4.1          |
| `po-002`                    | Declared set semantics            | D1     | closed | Command 1 in its Check Block      | PASS only if the complete arrays-as-sets suite passes                                                                                          | `audit/qa/hde-epic039/checks/po-002/primary.log`                    | Primary-log proof; manifest entry                     | `[]`   | PF10 §2.6; PF12 §4.2          |
| `po-003`                    | Corpus invariants                 | D1     | closed | Command 1 in its Check Block      | PASS only if all selected full-file topology, calculation, scoring, classification, narrative, suppression, and public-output suites pass      | `audit/qa/hde-epic039/checks/po-003/primary.log`                    | Primary-log proof; manifest entry                     | `[]`   | PF10 §2.6                     |
| `po-004`                    | Coherent evidence publication     | D2     | closed | Command 1 in its Check Block      | PASS only if transaction tests and current updater check pass                                                                                  | `audit/qa/hde-epic039/checks/po-004/primary.log`                    | Primary-log proof; manifest entry                     | `[]`   | PF10 §2.7; PF12 §8.3          |
| `po-005`                    | Evidence parity and integrity     | D2     | closed | Command 1 in its Check Block      | PASS only if current parity, proof, chronology, and self-record tests pass                                                                     | `audit/qa/hde-epic039/checks/po-005/primary.log`                    | Primary-log proof; manifest entry                     | `[]`   | PF10 §§2.7, 2.16; PF12 §8.3   |
| `po-006`                    | Causal QA status handling         | D3     | closed | Command 1 in its Check Block      | PASS only if causal classification and fail-closed input tests pass                                                                            | `audit/qa/hde-epic039/checks/po-006/primary.log`                    | Primary-log proof; manifest entry                     | `[]`   | PF10 §§2.9, 2.14; PF19 §2.2.5 |
| `po-007`                    | Semantic declaration propagation  | D3     | closed | Command 1 in its Check Block      | PASS only if semantic forms and selector normalization reach the intended runtime                                                              | `audit/qa/hde-epic039/checks/po-007/primary.log`                    | Primary-log proof; manifest entry                     | `[]`   | PF10 §2.14; PF19 §3.4.10      |
| `po-008`                    | Current and historical identity   | D3     | closed | Command 1 in its Check Block      | PASS only if current-state checks fail closed while historical records remain historical                                                       | `audit/qa/hde-epic039/checks/po-008/primary.log`                    | Primary-log proof; manifest entry                     | `[]`   | PF10 §2.9                     |
| `po-009`                    | Change-aware exact-candidate CI   | D4     | closed | Command 1 in its Check Block      | PASS only if selection, deduplication, ownership, and exact-candidate tests pass                                                               | `audit/qa/hde-epic039/checks/po-009/primary.log`                    | Primary-log proof; manifest entry                     | `[]`   | PF10 §§2.5, 2.8, 2.10         |
| `po-010`                    | Retired automation inactivity     | D4     | closed | Command 1 in its Check Block      | PASS only if selected safeguards pass and the bounded operative-locus scan is clean                                                            | `audit/qa/hde-epic039/checks/po-010/primary.log`                    | Primary-log proof; manifest entry                     | `[]`   | PF10 §2.10                    |
| `po-011`                    | Feedback-free derivation          | D5     | closed | Command 1 in its Check Block      | PASS only if causal-input, non-feedback, nonwriting, and closed-rails tests pass                                                               | `audit/qa/hde-epic039/checks/po-011/primary.log`                    | Primary-log proof; manifest entry                     | `[]`   | PF10 §§2.11–2.12; PF12 §6.2.2 |
| `po-012`                    | Coherent candidate publication    | D5     | closed | Command 1 in its Check Block      | PASS only if publication-point, mixed-state, interruption, recovery, and source-protection tests pass                                          | `audit/qa/hde-epic039/checks/po-012/primary.log`                    | Primary-log proof; manifest entry                     | `[]`   | PF10 §§2.11–2.12              |
| `po-013`                    | Reusable-capability-only boundary | D5     | closed | Command 1 in its Check Block      | PASS only if generic capability tests pass and no real candidate state is found                                                                | `audit/qa/hde-epic039/checks/po-013/primary.log`                    | Primary-log proof; manifest entry                     | `[]`   | PF10 §§2.12, 2.16             |

Every row has one corresponding Check Block below.

#### Token coverage and evidence binding (required)

Every check is a tokenless evidence check:

* `intended_tokens`: `[]`
* `claimed_tokens`: `[]`

No current HDE-EPIC039 acceptance map, token-evidence matrix, or registered epic-token roster is relied upon. No token is inferred from a passing test or log.

These checks are required because each proves a named, guide-defined behavior or evidence obligation. They are not “for good measure.”

Functional proof is supplied by executable loader, generator, publisher, harness, workflow-classifier, and closeout-lifecycle tests. Static scans are used only for the explicit negative-state portions of `po-010` and `po-013`.

### Check Blocks

#### Embedded harness checks (pattern; use when no standalone script exists)

`tools/qa/qa_harness.py` is the Repo-confirmed v2 evidence writer and current-state manifest publisher used by the QA-created wrapper.

`audit/qa/hde-epic039/00_meta/qa_runner.py` is QA-created. It is limited to:

* invoking the exact selected existing pytest nodes;
* running the existing evidence updater in `--check` mode for `po-004` and `po-005`;
* executing the five approved read-only Git queries and capturing actual execution-source identity, current-code-posture validation, and routing provenance;
* performing the bounded negative-state probe for `po-010`;
* enumerating every regular file in the current tracked HEAD tree through the close-pack generator’s current Git-object readers and using the generator’s current model loader to identify every accepted HDE-EPIC039 candidate source for `po-013`;
* treating inability to enumerate or validate the complete candidate-source domain as `FAIL_TOOLING`;
* writing PF27 v2 primary logs and the flat current-state manifest through the existing harness;
* calling `verify_manifest_entry` after each published check and again for every planned check during finalization;
* refusing to classify an entry as COVERED or include it in READY when referenced evidence is missing, malformed, untrusted, non-PASS, or identity-mismatched;
* creating discovery and closeout artifacts under the stable epic QA root; and
* generating required sibling path proofs through the existing updater-owned proof writer.

REPO VALIDATION NOTE: `tools/qa/step_log_header.py` exists but does not implement the required v2 contract and is not executable authority for this plan. It must not be used. The current v2-capable locus is `tools/qa/qa_harness.py`.

#### Canon check clarifications (routed)



* Check ID: `po-003`
* Applicability: required because this check protects Human Design corpus, calculation, scoring, classification, narrative, and public-meaning invariants.
* Complete required coverage: 64 Gates, 36 Channels, distinct endpoints, center projections, the ten-item special subset, 360 direction-native narratives with 120 per perspective, both governed suppressions, and no change to calculations, scoring, classifications, or public meaning.
* Repo-confirmed full-file proof suite: `tests/evidence/test_canonical_json_gate_check_outputs.py`, `tests/unit/test_narratives_loader.py`, `tests/core/test_engine_core_determinism.py`, `tests/core/test_engine_core_abba.py`, `tests/m10/test_thresholds_rounding.py`, `tests/m10/test_m10_symmetry_identity.py`, `tests/em/test_goldens_public_shape_and_identity.py`, `tests/reader_v1/test_goldens.py`, and `tests/unit/test_narratives_composer.py`.
* Coverage determination: the selected full-file suites jointly exercise the required topology, special-subset, calculation, scoring, classification, narrative-roster, perspective-count, suppression, composition, and public-output identity predicates; no bounded example node is represented as complete PO-003 proof.
* Mechanical decision: PASS requires exit `0` from the exact full-file selector set plus a trusted current primary log, matching sibling receipt proof, and agreeing manifest entry.
* Execution posture: `po-003` executes the exact full-file selector set and may contribute PASS; after trusted PASS, the PO proceeds to `po-004`.
* Owning source and locator: PF10 — HDE Build Notes, §2.6.
* Required local evidence: `audit/qa/hde-epic039/checks/po-003/primary.log` and `audit/qa/hde-epic039/checks/po-003/primary.log.path_proof.txt`.
* Failure-class consequence: an unavailable required selector, dependency, or entrypoint is `TOOLING_BLOCKED`; collection, import, helper, receipt-proof, or evidence-publication failure is `FAIL_TOOLING`; a trustworthy assertion contradiction is `FAIL_BEHAVIOR`.
* Nonclaims: no public Reader traffic, new calculation, scoring change, acceptance token, PF09 edit, or epic closure.


#### CHECK step-0b-doc-delta-capture: Doc Delta Capture and discovery bootstrap

Surface / D-goal mapping: D0 — dependencies, protected Doc Delta pair, execution-source provenance, current-code-posture validation, discovery, helper validation, primary log, and manifest bootstrap
Rails: SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=test
Pins: LC_ALL=C LANG=C TZ=UTC
PF anchors: PF27 — Canon Plan Templates; PF10 — HDE Build Notes, §§2.7 and 2.9

Goal / intent: establish a trustworthy closed-rails execution environment, create the bounded QA-only runner, capture actual execution-source and routing provenance without a preplanned-commit gate, validate required current interfaces and the existing proof-bearing Doc Delta pair without overwriting it, and mechanically create the discovery artifact, Step-0B primary log, and first manifest entry.

Required dependencies: Python standard library; Git for the five approved read-only queries; `requirements-dev.txt`; `tools/qa/qa_harness.py`; `tools/qa/generate_epic_close_pack.py`; `tools/evidence/update_evidence_index.py`; pytest; jsonschema.

Preflight check: Command 1 proves Python availability. Command 3 proves the QA-created helper’s exact SHA-256 and syntax. Command 4 performs dependency readiness, read-only source capture, current-interface validation, Doc Delta validation, discovery creation, and evidence publication.

If missing, activation/install action: None proven; stop this step.

If still unavailable: TOOLING_BLOCKED; stop the QA ladder and run the closeout finalization command. Do not install, activate, fetch, or retry dependencies.

Preconditions:

* Run from the PF07-derived repository root for `amthorn78/glow-hdengine-v2`.
* Do not edit either existing Doc Delta file or proof companion.
* Do not perform a checkout, pull, reset, clean, stash, commit, push, or other state-changing VCS action.
* If `audit/qa/hde-epic039/00_meta/qa_runner.py` already exists with different bytes, stop. Do not overwrite it.

Setup and PO actions:

1. Run Command 1.
2. Run Command 2 exactly once. It creates the QA-only helper only if absent and refuses differing existing bytes.
3. Run Command 3.
4. Run Command 4.
5. Inspect the emitted JSON, discovery artifact, and primary log before continuing.

Command 1: LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=test python --version

Expected result: Python prints its version and exits `0`. Otherwise stop before file creation.

Command 2: LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=test python -B -c 'import base64,gzip,hashlib,pathlib; data=gzip.decompress(base64.b64decode("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")); expected="7cc185a4b31f56232a69743f2c7203088628b951e704abb93a9f643a8541849e"; (hashlib.sha256(data).hexdigest()==expected) or (_ for _ in ()).throw(SystemExit("STOP_HELPER_PAYLOAD_HASH")); p=pathlib.Path("audit/qa/hde-epic039/00_meta/qa_runner.py"); old=p.read_bytes() if p.exists() else None; (old is None or old==data) or (_ for _ in ()).throw(SystemExit("STOP_EXISTING_HELPER_DIFF")); p.parent.mkdir(parents=True,exist_ok=True); p.write_bytes(data) if old is None else None; print(p)'

Expected result: the command prints `audit/qa/hde-epic039/00_meta/qa_runner.py` and exits `0`. `STOP_HELPER_PAYLOAD_HASH` or `STOP_EXISTING_HELPER_DIFF` is TOOLING_BLOCKED.

Command 3: LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=test python -B -c 'import hashlib,pathlib; p=pathlib.Path("audit/qa/hde-epic039/00_meta/qa_runner.py"); data=p.read_bytes(); expected="7cc185a4b31f56232a69743f2c7203088628b951e704abb93a9f643a8541849e"; (hashlib.sha256(data).hexdigest()==expected) or (_ for _ in ()).throw(SystemExit("STOP_HELPER_HASH_MISMATCH")); compile(data,p.as_posix(),"exec"); print(expected)'

Expected result: prints the expected SHA-256 and exits `0`.

Command 4: LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=test python -B audit/qa/hde-epic039/00_meta/qa_runner.py step-0b-doc-delta-capture

Expected result: exits `0` and prints JSON with `status` equal to `PASS`. A dependency, Git-query, repository-identity, or required-interface failure remains TOOLING_BLOCKED; no install or retry is authorized.

What to look for:

* The Doc Delta pair is byte-identical.
* Both existing path proofs match current path, SHA-256, and size.
* `discovery.json` uses `hde_epic039.qa_discovery.v2` and reports the exact six environment values.
* `execution_source` records actual HEAD, branch or detached state, working-tree status, normalized repository identity, source-provenance commands, required-interface availability, current-code-posture validity, and routing provenance.
* `source_identity_is_pass_gate` and `preplanned_commit_equality_required` are both `false`.
* The primary log begins with a v2 header and binds the read-only source-provenance command sequence.
* Both token arrays are empty.
* Neither existing Doc Delta file was modified.

Required deliverables:

* `audit/qa/hde-epic039/00_meta/qa_runner.py`
* `audit/qa/hde-epic039/00_meta/discovery.json`

* `audit/qa/hde-epic039/checks/step-0b-doc-delta-capture/primary.log`
* `audit/qa/hde-epic039/checks/step-0b-doc-delta-capture/primary.log.path_proof.txt`
* `audit/qa/hde-epic039/qa_step_logs_manifest.json`

PASS criteria:

* All pre-existing loci and dependencies are available without installation.
* Helper hash and syntax validate.
* Actual execution-source identity and routing provenance are captured.
* Required current repository identity and helper interfaces validate.
* No equality to a preplanned commit is required.
* Doc Delta pair and proofs validate.
* Discovery and primary log are non-empty.
* The primary log lists its sibling receipt proof in `evidence_artifacts`, and that proof matches the current log path, SHA-256, and size.
* `verify_manifest_entry` validates the Step-0B manifest entry, referenced log, v2 identity, self-binding, check identity, and status agreement.

FAIL_BEHAVIOR criteria:

* Trustworthy evaluation proves the two Doc Delta bodies differ.

FAIL_TOOLING criteria:

* A path proof is malformed, stale, or mismatched, or the evidence writer or validator malfunctions.

TOOLING_BLOCKED criteria:

* Python, Git, pytest, jsonschema, a required existing locus, required rails, source-provenance capture, current repository identity, required current interface, or the approved helper is unavailable.

Blocked posture: stop the ladder. Do not install dependencies or create substitute paths, interfaces, or helpers.

Tokens:

* `intended_tokens`: `[]`
* `claimed_tokens`: `[]`

#### CHECK po-001: PO-001 —

Surface / D-goal mapping: D1 — deterministic generation and exact 26-target inventory
Rails: SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=test
Pins: LC_ALL=C LANG=C TZ=UTC
PF anchors: PF10 — HDE Build Notes, §2.6; PF12 — HDE Schemas and Artifacts, §4.1

Goal / intent: prove that the current 26-target structured-data inventory is exact and deterministically executable, while incomplete, substituted, erased, or empty target contracts fail closed.

Required dependencies: Step-0B PASS; Python; pytest; jsonschema; `tools/qa/qa_harness.py`; the Repo-confirmed selectors in Command 1.

Preflight check: the helper verifies every selector path and runs `python -m pytest --version` before behavior evaluation.

If missing, activation/install action: None proven; stop this step.

If still unavailable: TOOLING_BLOCKED; stop this step.

Preconditions: Step-0B is PASS. No product or governed source file has been edited during QA.

Setup: none.

PO actions:

1. Run Command 1.
2. Confirm the emitted JSON status.
3. Inspect the primary log and manifest entry.
4. Stop the ladder on any non-PASS result.

Command 1: LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=test python -B audit/qa/hde-epic039/00_meta/qa_runner.py po-001 tests/evidence/test_canonical_json_gate_check_outputs.py::test_d1_inventory_is_complete_unique_sorted_and_bound tests/evidence/test_canonical_json_gate_check_outputs.py::test_all_26_current_target_bindings_execute tests/evidence/test_canonical_json_gate_check_outputs.py::test_incomplete_target_inventory_fails_closed tests/evidence/test_canonical_json_gate_check_outputs.py::test_same_cardinality_target_substitution_fails_closed tests/evidence/test_canonical_json_gate_check_outputs.py::test_same_path_binding_erasure_and_set_rule_substitution_fail_closed tests/evidence/test_canonical_json_gate_check_outputs.py::test_generated_target_contracts_reject_empty_objects -q

What to look for: selected tests are collected, all pass, and no unexpected-target or malformed-contract condition is accepted.

Required deliverables:


* `audit/qa/hde-epic039/checks/po-001/primary.log`
* `audit/qa/hde-epic039/checks/po-001/primary.log.path_proof.txt`
* Updated `audit/qa/hde-epic039/qa_step_logs_manifest.json`
* Manifest proof remains DEFERRED until closeout finalization.

PASS criteria: Command 1 exits `0`; every selected test passes; the v2 primary log and matching `PASS` manifest entry exist; the log lists its sibling receipt proof, and the proof matches the current log path, SHA-256, and size.

FAIL_BEHAVIOR criteria: trustworthy assertions contradict inventory completeness, deterministic binding, or fail-closed rejection.

FAIL_TOOLING criteria: collection, import, harness, evidence-writer, or selector execution malfunctions.

TOOLING_BLOCKED criteria: prerequisite, selector, Python module, or runnable pytest entrypoint is unavailable.

Blocked posture: preserve the log, stop, and run closeout finalization.

Tokens: `intended_tokens: []`; `claimed_tokens: []`.

#### CHECK po-002: PO-002 —

Surface / D-goal mapping: D1 — six declared unordered-collection rules and ordered-list preservation
Rails: SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=test
Pins: LC_ALL=C LANG=C TZ=UTC
PF anchors: PF10 — HDE Build Notes, §2.6; PF12 — HDE Schemas and Artifacts, §4.2

Goal / intent: prove that only the six declared collections receive set normalization, identical members collapse deterministically, conflicts fail, and ordered collections retain order.

Required dependencies: Step-0B PASS; Python; pytest; `tools/qa/qa_harness.py`; `tests/compare/test_arrays_as_sets.py`.

Preflight check: selector existence and `python -m pytest --version` are checked inside the helper.

If missing, activation/install action: None proven; stop this step.

If still unavailable: TOOLING_BLOCKED; stop this step.

Preconditions: Step-0B PASS.

Setup: none.

PO actions:

1. Run Command 1.
2. Confirm `status: PASS`.
3. Inspect the primary log for the complete file-level suite result.

Command 1: LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=test python -B audit/qa/hde-epic039/00_meta/qa_runner.py po-002 tests/compare/test_arrays_as_sets.py -q

What to look for: deterministic report behavior, canonical ASCII ordering, conflict rejection, and no normalization of ordered collections.

Required deliverables:


* `audit/qa/hde-epic039/checks/po-002/primary.log`
* `audit/qa/hde-epic039/checks/po-002/primary.log.path_proof.txt`
* Updated manifest entry for `po-002`
* Manifest proof DEFERRED until closeout.

PASS criteria: complete selected suite passes with exit `0`; log and manifest identities agree; the log lists its sibling receipt proof, and the proof matches the current log path, SHA-256, and size.

FAIL_BEHAVIOR criteria: trustworthy assertions show undeclared normalization, unstable order, accepted conflicts, or altered ordered semantics.

FAIL_TOOLING criteria: collection, import, harness, or evidence publication fails.

TOOLING_BLOCKED criteria: required dependency or entrypoint is unavailable.

Blocked posture: preserve evidence and stop.

Tokens: `intended_tokens: []`; `claimed_tokens: []`.




#### CHECK po-003: PO-003 —

Surface / D-goal mapping: D1 — Human Design topology, calculations, scoring, classifications, narratives, suppressions, and public meaning
Rails: SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=test
Pins: LC_ALL=C LANG=C TZ=UTC
PF anchors: PF10 — HDE Build Notes, §2.6

Goal / intent: execute the source-grounded full-file predicate set that mechanically decides whether the governed Human Design corpus preserves all required PO-003 invariants without calculation, scoring, classification, narrative, suppression, or public-meaning drift.

Required dependencies: Step-0B PASS; Python; pytest; `tools/qa/qa_harness.py`; `tools/evidence/update_evidence_index.py`; `tests/evidence/test_canonical_json_gate_check_outputs.py`; `tests/unit/test_narratives_loader.py`; `tests/core/test_engine_core_determinism.py`; `tests/core/test_engine_core_abba.py`; `tests/m10/test_thresholds_rounding.py`; `tests/m10/test_m10_symmetry_identity.py`; `tests/em/test_goldens_public_shape_and_identity.py`; `tests/reader_v1/test_goldens.py`; and `tests/unit/test_narratives_composer.py`.

Preflight check: the helper verifies the required rails, every selector path, and pytest readiness before invoking the exact full-file selector set. It then publishes and validates the primary log, sibling receipt proof, and manifest entry.

If missing, activation/install action: None proven; stop this step.

If still unavailable: TOOLING_BLOCKED.

Preconditions: Step-0B PASS; no product, test, generator, or governed-artifact edit has been made during QA.

Setup: none.

PO actions:

1. Run Command 1 exactly as written.
2. Confirm the emitted JSON reports `status` as `PASS` and `primary_log_proof_valid` as `true`.
3. Inspect the primary log, sibling receipt proof, and manifest entry; confirm they identify the exact full-file selector set and agree on check ID, status, path, SHA-256, and size.
4. Continue to `po-004` only after trusted PASS. On any non-PASS result, preserve the evidence, stop the ladder, and run closeout finalization.

Command 1: LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=test python -B audit/qa/hde-epic039/00_meta/qa_runner.py po-003 tests/evidence/test_canonical_json_gate_check_outputs.py tests/unit/test_narratives_loader.py tests/core/test_engine_core_determinism.py tests/core/test_engine_core_abba.py tests/m10/test_thresholds_rounding.py tests/m10/test_m10_symmetry_identity.py tests/em/test_goldens_public_shape_and_identity.py tests/reader_v1/test_goldens.py tests/unit/test_narratives_composer.py -q

Expected result: exits `0` and prints JSON with `status` equal to `PASS` and `primary_log_proof_valid` equal to `true` after every selected full-file suite collects and passes.

What to look for:

* The canonical structured-data suite passes its exact Gate, Channel, endpoint, center-projection, special-subset, generated-output, and identity predicates.
* The narrative loader and composer suites pass the 360-row roster, 120-per-perspective distribution, source identity, routing, both governed suppressions, fallback, and composition predicates.
* The core and Magic10 suites pass deterministic calculation, AB/BA, threshold, rounding, band-classification, symmetry, and identity predicates.
* The Extended Mechanics and Reader golden suites pass public-output shape, content, schema, AB/BA identity, and hash predicates.
* The primary log records the exact child command and lists its sibling receipt proof in `evidence_artifacts`.
* The sibling proof matches the current log path, SHA-256, and size, and the manifest entry agrees with the receipt.

Required deliverables:

* `audit/qa/hde-epic039/checks/po-003/primary.log`
* `audit/qa/hde-epic039/checks/po-003/primary.log.path_proof.txt`
* Updated manifest entry for `po-003`
* Manifest proof DEFERRED until closeout.

PASS criteria: every selected full-file suite collects and passes with pytest exit `0`; the result is `PASS`; the trusted receipt demonstrates the required 64 Gates, 36 Channels, distinct endpoints, correct center projections, complete ten-item special subset, 360 direction-native narratives with 120 per perspective, both governed suppressions, and unchanged calculations, scoring, classifications, and public meaning; log, sibling proof, and manifest identities agree.

FAIL_BEHAVIOR criteria: a trustworthy collected assertion contradicts any required topology, special-subset, calculation, scoring, classification, narrative-roster, perspective-count, suppression, composition, public-output, or identity predicate.

FAIL_TOOLING criteria: collection, import, helper, header writing, receipt-proof writing, manifest publication, or validation fails before a trustworthy behavioral conclusion.

TOOLING_BLOCKED criteria: Python, pytest, the helper entrypoint, an exact required selector, or another mandatory prerequisite is unavailable before behavior-decisive execution.

Blocked posture: preserve the non-PASS receipt and proof, stop the ladder, and run closeout finalization. Do not install dependencies, substitute or trim selectors, or treat later checks as executed.

Tokens: `intended_tokens: []`; `claimed_tokens: []`.

#### CHECK po-004: PO-004 —

Surface / D-goal mapping: D2 — single-authority coherent evidence publication
Rails: SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=test
Pins: LC_ALL=C LANG=C TZ=UTC
PF anchors: PF10 — HDE Build Notes, §2.7; PF12 — HDE Schemas and Artifacts, §8.3

Goal / intent: exercise staged publication, rollback, coherent final validation, and updater ownership, then run the existing updater’s nonwriting current-state check.

Required dependencies: Step-0B PASS; Python; pytest; `tools/evidence/update_evidence_index.py`; selected transaction tests.

Preflight check: selector and pytest readiness are checked before tests; the helper invokes the updater only as `python -B tools/evidence/update_evidence_index.py --check`.

If missing, activation/install action: None proven; stop this step.

If still unavailable: TOOLING_BLOCKED.

Preconditions: Step-0B PASS; no manual evidence edits.

Setup: none.

PO actions:

1. Run Command 1.
2. Confirm both pytest and `EXTRA_COMMAND` exit codes are `0`.
3. Inspect the primary log and manifest entry.

Command 1: LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=test python -B audit/qa/hde-epic039/00_meta/qa_runner.py po-004 tests/evidence/test_machine_mirror_self_proof.py::test_staged_publication_add_replace_remove_is_transactional tests/evidence/test_machine_mirror_self_proof.py::test_staged_publication_rolls_back_every_preimage tests/evidence/test_machine_mirror_self_proof.py::test_sanity_rebind_publishes_coherent_model tests/evidence/test_machine_mirror_self_proof.py::test_sanity_rebind_rolls_back_partial_publication tests/evidence/test_evidence_skeleton.py::test_index_canonical_and_hash_matches tests/evidence/test_rails_ci_workflow_integration.py::test_feature_producers_do_not_reference_path_proof_writer -q

What to look for: transactional tests pass; rollback tests pass; the updater `--check` reports no stale publication state.

Required deliverables:


* `audit/qa/hde-epic039/checks/po-004/primary.log`
* `audit/qa/hde-epic039/checks/po-004/primary.log.path_proof.txt`
* Updated manifest entry for `po-004`
* No non-QA-root file is written by the updater check.

PASS criteria: all selected tests and updater check exit `0`; primary log records both command families; the log lists its sibling receipt proof, and the proof matches the current log path, SHA-256, and size.

FAIL_BEHAVIOR criteria: trustworthy tests or updater check expose incoherent, stale, non-convergent, multi-authority, or non-rollback behavior.

FAIL_TOOLING criteria: updater or test mechanism malfunctions or produces untrustworthy evidence.

TOOLING_BLOCKED criteria: updater, tests, interpreter, or dependency is unavailable.

Blocked posture: stop. Do not run updater write mode.

Tokens: `intended_tokens: []`; `claimed_tokens: []`.

#### CHECK po-005: PO-005 —

Surface / D-goal mapping: D2 — Human Index, Machine Mirror, proofs, checksums, chronology, and Doc Delta agreement
Rails: SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=test
Pins: LC_ALL=C LANG=C TZ=UTC
PF anchors: PF10 — HDE Build Notes, §§2.7 and 2.16; PF12 — HDE Schemas and Artifacts, §8.3

Goal / intent: prove current human/machine parity, self-record semantics, complete size and hash bindings, proof companions, chronology handling, and Doc Delta integrity.

Required dependencies: Step-0B PASS; Python; pytest; current Human Index, Machine Mirror, path proofs, checksums, updater, and selected tests.

Preflight check: helper validates selectors and pytest readiness; it then invokes the updater in `--check` mode.

If missing, activation/install action: None proven; stop this step.

If still unavailable: TOOLING_BLOCKED.

Preconditions: Step-0B PASS.

Setup: none.

PO actions:

1. Run Command 1.
2. Confirm all tests and the updater check pass.
3. Inspect the primary log for parity, self-proof, chronology, and current-index results.

Command 1: LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=test python -B audit/qa/hde-epic039/00_meta/qa_runner.py po-005 tests/evidence/test_evidence_skeleton.py::test_index_canonical_and_hash_matches tests/evidence/test_evidence_skeleton.py::test_mirror_schema_and_parity tests/evidence/test_evidence_skeleton.py::test_index_entries_have_mirrors_and_path_proofs tests/evidence/test_evidence_skeleton.py::test_epic039_doc_delta_byte_changes_refresh_chronology tests/evidence/test_machine_mirror_self_proof.py::test_machine_mirror_self_proof_matches_canonical_digest tests/qa/test_qa_harness_followup.py::test_machine_mirror_self_record_uses_body_and_full_file_hashes tests/qa/test_qa_harness_followup.py::test_machine_mirror_self_record_rejects_incoherent_hash_or_size -q

What to look for: complete parity, current hashes and sizes, coherent self-record, valid proof companions, and non-backdated chronology behavior.

Required deliverables:


* `audit/qa/hde-epic039/checks/po-005/primary.log`
* `audit/qa/hde-epic039/checks/po-005/primary.log.path_proof.txt`
* Updated manifest entry for `po-005`
* Manifest proof DEFERRED until closeout.

PASS criteria: selected tests and current updater check all exit `0`; the log lists its sibling receipt proof, and the proof matches the current log path, SHA-256, and size.

FAIL_BEHAVIOR criteria: trustworthy evaluation finds parity, self-reference, hash, size, companion, chronology, or duplicated-content contradiction.

FAIL_TOOLING criteria: evidence checker, parser, updater, harness, or writer malfunctions.

TOOLING_BLOCKED criteria: any required evidence surface or dependency is unavailable.

Blocked posture: stop; do not refresh evidence during this QA step.

Tokens: `intended_tokens: []`; `claimed_tokens: []`.

#### CHECK po-006: PO-006 —

Surface / D-goal mapping: D3 — causal current-state QA classification
Rails: SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=test
Pins: LC_ALL=C LANG=C TZ=UTC
PF anchors: PF10 — HDE Build Notes, §§2.9 and 2.14; PF19 — Glow QA Guide, §2.2.5

Goal / intent: prove that unavailable prerequisites, evaluation failures, and behavior contradictions receive distinct outcomes and that absent, malformed, empty, or unevaluated conditions cannot become PASS.

Required dependencies: Step-0B PASS; Python; pytest; existing generic QA harness and selected harness tests.

Preflight check: selector existence and pytest readiness are captured by the helper.

If missing, activation/install action: None proven; stop this step.

If still unavailable: TOOLING_BLOCKED.

Preconditions: Step-0B PASS.

Setup: none.

PO actions:

1. Run Command 1.
2. Confirm all causal-classification tests pass.
3. Inspect the log for exact command and empty token arrays.

Command 1: LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=test python -B audit/qa/hde-epic039/00_meta/qa_runner.py po-006 tests/qa/test_generic_qa_harness.py::test_exact_status_set_and_causal_rollup tests/qa/test_generic_qa_harness.py::test_same_interpreter_and_classification tests/qa/test_generic_qa_harness.py::test_pytest_no_collection_is_tooling_blocked tests/qa/test_generic_qa_harness.py::test_missing_and_malformed_inputs_are_structured tests/qa/test_generic_qa_harness.py::test_writer_failure_is_fail_tooling tests/qa/test_generic_qa_harness.py::test_pytest_returncode_classification_is_causal tests/qa/test_generic_qa_harness.py::test_missing_sibling_path_proof_is_tooling_blocked tests/qa/test_generic_qa_harness.py::test_evidence_graph_failure_classification_is_causal -q

What to look for: five-status closure, causal precedence, same-interpreter execution, no-tests blocking, malformed-input rejection, and writer failure as tooling.

Required deliverables:


* `audit/qa/hde-epic039/checks/po-006/primary.log`
* `audit/qa/hde-epic039/checks/po-006/primary.log.path_proof.txt`
* Updated manifest entry for `po-006`

PASS criteria: every selected causal predicate passes with exit `0`; the log lists its sibling receipt proof, and the proof matches the current log path, SHA-256, and size.

FAIL_BEHAVIOR criteria: trustworthy tests show an invalid PASS or incorrect behavior classification.

FAIL_TOOLING criteria: the harness, writer, collection, or classification mechanism itself fails.

TOOLING_BLOCKED criteria: the test runner or mandatory inputs cannot reach the decisive point.

Blocked posture: stop; do not relabel tooling absence as behavior failure.

Tokens: `intended_tokens: []`; `claimed_tokens: []`.

#### CHECK po-007: PO-007 —

Surface / D-goal mapping: D3 — semantic declaration forms and runtime propagation
Rails: SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=test
Pins: LC_ALL=C LANG=C TZ=UTC
PF anchors: PF10 — HDE Build Notes, §2.14; PF19 — Glow QA Guide, §3.4.10

Goal / intent: verify that semantically valid declaration and selector forms reach intended collection/runtime behavior and that presentation form alone is not treated as a substantive contradiction.

Required dependencies: Step-0B PASS; Python; pytest; existing QA harness tests.

Preflight check: helper validates selectors and pytest readiness.

If missing, activation/install action: None proven; stop this step.

If still unavailable: TOOLING_BLOCKED.

Preconditions: Step-0B PASS.

Setup: none.

PO actions:

1. Run Command 1.
2. Confirm semantic and normalized selector tests pass.
3. Treat any rendering-only difference as non-gating unless an independent semantic contradiction remains.

Command 1: LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=test python -B audit/qa/hde-epic039/00_meta/qa_runner.py po-007 tests/qa/test_generic_qa_harness.py::test_pf04_declaration_forms_ignore_explanatory_prose tests/qa/test_generic_qa_harness.py::test_viability_normalizes_and_compares_acceptance_posture tests/qa/test_generic_qa_harness.py::test_pytest_preflight_skips_admitted_option_values tests/qa/test_qa_harness_followup.py::test_collection_normalization_preserves_selector_options tests/qa/test_qa_harness_followup.py::test_pytest_locator_options_are_preserved_during_collection tests/qa/test_qa_harness_followup.py::test_exact_node_locator_with_quiet_flag_uses_one_quiet_collection_command -q

What to look for: declarations are interpreted semantically, selector options remain intact, and exact nodes are collected once.

Required deliverables:


* `audit/qa/hde-epic039/checks/po-007/primary.log`
* `audit/qa/hde-epic039/checks/po-007/primary.log.path_proof.txt`
* Updated manifest entry for `po-007`

PASS criteria: all selected semantic propagation tests pass with exit `0`; the log lists its sibling receipt proof, and the proof matches the current log path, SHA-256, and size.

FAIL_BEHAVIOR criteria: trustworthy execution proves a semantically valid declaration does not reach its intended behavior.

FAIL_TOOLING criteria: normalization, collection, harness, or evidence mechanism fails independently of product behavior.

TOOLING_BLOCKED criteria: required entrypoint or dependency is unavailable.

Blocked posture: stop; do not create a syntax-only remediation proposal.

Tokens: `intended_tokens: []`; `claimed_tokens: []`.

#### CHECK po-008: PO-008 —

Surface / D-goal mapping: D3 — current governed references and historical identity separation
Rails: SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=test
Pins: LC_ALL=C LANG=C TZ=UTC
PF anchors: PF10 — HDE Build Notes, §2.9

Goal / intent: verify that current conclusions bind to current bytes and stable identities while historical rows, manifests, and evidence remain historical and are not promoted into current proof.

Required dependencies: Step-0B PASS; Python; pytest; existing current-state and historical-transition tests.

Preflight check: helper validates all selectors and pytest readiness.

If missing, activation/install action: None proven; stop this step.

If still unavailable: TOOLING_BLOCKED.

Preconditions: Step-0B PASS.

Setup: none.

PO actions:

1. Run Command 1.
2. Confirm stale and late-changing current evidence fails closed.
3. Confirm historical identities remain recognized without becoming current proof.

Command 1: LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=test python -B audit/qa/hde-epic039/00_meta/qa_runner.py po-008 tests/qa/test_qa_harness_followup.py::test_normal_governance_binding_rejects_stale_artifact_bytes tests/qa/test_qa_harness_followup.py::test_governance_validator_rechecks_artifact_bytes_within_evaluation tests/qa/test_qa_harness_followup.py::test_governance_validator_final_stability_check_rejects_late_change tests/qa/test_qa_harness_followup.py::test_governance_graph_allows_minimal_historical_human_rows tests/qa/test_qa_harness_followup.py::test_epic027_flat_v1_transition_retains_all_historical_identities tests/qa/test_qa_harness_followup.py::test_epic021_runs_envelope_is_recognized_without_import tests/evidence/test_canonical_json_gate_check_outputs.py::test_frozen_audit_reader_pair_rejects_coherent_rewrite -q

What to look for: current bytes are rechecked, late drift is rejected, historical identities survive, and frozen evidence cannot be rewritten coherently.

Required deliverables:


* `audit/qa/hde-epic039/checks/po-008/primary.log`
* `audit/qa/hde-epic039/checks/po-008/primary.log.path_proof.txt`
* Updated manifest entry for `po-008`

PASS criteria: every selected current/historical boundary test passes; the log lists its sibling receipt proof, and the proof matches the current log path, SHA-256, and size.

FAIL_BEHAVIOR criteria: current proof accepts stale or changing bytes, or historical evidence is treated as mutable current proof.

FAIL_TOOLING criteria: graph evaluator, transition parser, harness, collection, or evidence writer fails.

TOOLING_BLOCKED criteria: required historical/current surface or dependency is unavailable.

Blocked posture: stop; do not rewrite historical evidence.

Tokens: `intended_tokens: []`; `claimed_tokens: []`.

#### CHECK po-009: PO-009 —

Surface / D-goal mapping: D4 — relevant-change selection, cancellation posture, deduplication, ownership, and exact candidate
Rails: SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=test
Pins: LC_ALL=C LANG=C TZ=UTC
PF anchors: PF10 — HDE Build Notes, §§2.5, 2.8, and 2.10

Goal / intent: prove that continuing automation is change-aware, conservative for ambiguity, nonduplicative, ownership-complete, and exact-candidate-bound.

Required dependencies: Step-0B PASS; Python; pytest; `.github/workflows/ci.yml`; CI classifier and selected workflow integration tests.

Preflight check: helper validates selectors and pytest readiness. Tests inspect workflow definitions without starting hosted CI.

If missing, activation/install action: None proven; stop this step.

If still unavailable: TOOLING_BLOCKED.

Preconditions: Step-0B PASS.

Setup: none.

PO actions:

1. Run Command 1.
2. Confirm topology, scenario, ownership, deduplication, exact-reference, and secret-free job-definition tests pass.
3. Do not trigger a hosted workflow.

Command 1: LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=test python -B audit/qa/hde-epic039/00_meta/qa_runner.py po-009 tests/evidence/test_rails_ci_workflow_integration.py::test_workflow_has_one_truthful_exact_head_summary_topology tests/evidence/test_rails_ci_workflow_integration.py::test_change_classifier_selects_expected_execution_scenarios tests/evidence/test_rails_ci_workflow_integration.py::test_qa_tool_owner_policy_is_exhaustive_and_deduplicated tests/evidence/test_rails_ci_workflow_integration.py::test_full_validation_roster_is_exhaustive_nonoverlapping_and_owned tests/evidence/test_rails_ci_workflow_integration.py::test_change_classifier_executes_against_exact_git_refs tests/evidence/test_rails_ci_workflow_integration.py::test_pull_request_classification_uses_merge_base_not_base_tip tests/evidence/test_rails_ci_workflow_integration.py::test_every_active_workflow_command_input_has_an_applicable_lane tests/evidence/test_rails_ci_workflow_integration.py::test_job_definitions_are_reusable_secret_free_and_live_forbidden -q

What to look for: one truthful final topology, relevant lane selection, exhaustive ownership, no duplicate full validation, conservative coverage, and exact candidate reference.

Required deliverables:


* `audit/qa/hde-epic039/checks/po-009/primary.log`
* `audit/qa/hde-epic039/checks/po-009/primary.log.path_proof.txt`
* Updated manifest entry for `po-009`

PASS criteria: all selected CI-definition behavior tests pass with exit `0`; the log lists its sibling receipt proof, and the proof matches the current log path, SHA-256, and size.

FAIL_BEHAVIOR criteria: trustworthy tests expose omitted risk, duplicate or irrelevant full evaluation, ambiguous permissive routing, or wrong-candidate conclusion.

FAIL_TOOLING criteria: workflow parser, classifier harness, collection, or evidence writer fails.

TOOLING_BLOCKED criteria: workflow, classifier, tests, or dependency is unavailable.

Blocked posture: stop; do not alter workflows or repository settings.

Tokens: `intended_tokens: []`; `claimed_tokens: []`.

#### CHECK po-010: PO-010 —

Surface / D-goal mapping: D4 — retired epic-specific automation absence and preservation of history and generic safeguards
Rails: SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=test
Pins: LC_ALL=C LANG=C TZ=UTC
PF anchors: PF10 — HDE Build Notes, §2.10

Goal / intent: verify that five retired HDE-EPIC038 automation loci and their operative references remain absent while historical records, the generic QA harness, CI workflow, and generic closeout tool remain available.

Required dependencies: Step-0B PASS; Python; pytest; current operative directories; selected safeguard tests.

Preflight check: helper validates selectors and pytest readiness before performing its bounded operative-locus scan.

If missing, activation/install action: None proven; stop this step.

If still unavailable: TOOLING_BLOCKED.

Preconditions: Step-0B PASS.

Setup: none.

PO actions:

1. Run Command 1.
2. Confirm selected safeguard tests pass.
3. Inspect the `PROBE` record for empty retired-path and operative-text hit lists.
4. Confirm preserved generic/historical loci are not reported missing.

Command 1: LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=test python -B audit/qa/hde-epic039/00_meta/qa_runner.py po-010 tests/evidence/test_rails_ci_workflow_integration.py::test_manual_closeout_validation_is_isolated_read_only_and_exact_head tests/evidence/test_rails_ci_workflow_integration.py::test_job_definitions_are_reusable_secret_free_and_live_forbidden tests/qa/test_qa_tool_ownership.py::test_qa_tool_registry_matches_candidate_sources tests/qa/test_qa_tool_ownership.py::test_step_log_header_is_canonical_and_tmp_scoped -q

What to look for:

* No retired path is present.
* No retired filename appears in `tools`, `tests`, `ci`, `.github`, or `engine`.
* `audit/qa/hde-epic038`, `tools/qa/qa_harness.py`, `.github/workflows/ci.yml`, and `tools/qa/generate_epic_close_pack.py` remain present.

Required deliverables:


* `audit/qa/hde-epic039/checks/po-010/primary.log`
* `audit/qa/hde-epic039/checks/po-010/primary.log.path_proof.txt`
* Updated manifest entry for `po-010`
* The negative scan report embedded in the primary log

PASS criteria: selected tests pass; retired-path and operative-hit arrays are empty; required preserved loci exist; the log lists its sibling receipt proof, and the proof matches the current log path, SHA-256, and size.

FAIL_BEHAVIOR criteria: a retired path or operative reference is found after trustworthy scanning.

FAIL_TOOLING criteria: test, scan, harness, or evidence mechanism malfunctions.

TOOLING_BLOCKED criteria: a required generic safeguard or historical locus cannot be inspected.

Blocked posture: stop; do not delete or restore files during QA.

Tokens: `intended_tokens: []`; `claimed_tokens: []`.

#### CHECK po-011: PO-011 —

Surface / D-goal mapping: D5 — deterministic feedback-free candidate derivation
Rails: SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=test
Pins: LC_ALL=C LANG=C TZ=UTC
PF anchors: PF10 — HDE Build Notes, §§2.11 and 2.12; PF12 — HDE Schemas and Artifacts, §6.2.2

Goal / intent: prove through temporary-repository tests that candidate bytes derive only from reviewed tracked inputs, exclude hosted or feedback dependencies, require closed rails, and remain nonwriting in check mode.

Required dependencies: Step-0B PASS; Python; pytest; `tools/qa/generate_epic_close_pack.py`; its schema and selected tests.

Preflight check: helper validates every exact node and pytest readiness.

If missing, activation/install action: None proven; stop this step.

If still unavailable: TOOLING_BLOCKED.

Preconditions: Step-0B PASS. Do not provide a real candidate source.

Setup: none.

PO actions:

1. Run Command 1.
2. Confirm all lifecycle tests pass.
3. Verify no real HDE-EPIC039 output is created by this step.

Command 1: LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=test python -B audit/qa/hde-epic039/00_meta/qa_runner.py po-011 tests/qa/test_generate_epic_close_pack.py::test_schema_rejects_feedback_dependencies_in_every_causal_role tests/qa/test_generate_epic_close_pack.py::test_actual_head_cannot_enter_through_nonclaims tests/qa/test_generate_epic_close_pack.py::test_unsafe_schema_reference_is_rejected_without_network_or_outputs tests/qa/test_generate_epic_close_pack.py::test_tracked_causal_payloads_are_opaque_byte_inputs tests/qa/test_generate_epic_close_pack.py::test_complete_candidate_lifecycle_is_committable_exact_and_idempotent tests/qa/test_generate_epic_close_pack.py::test_check_mode_is_nonwriting_for_bytes_mode_and_metadata tests/qa/test_generate_epic_close_pack.py::test_source_commit_hash_and_feedback_dependencies_do_not_enter_outputs tests/qa/test_generate_epic_close_pack.py::test_modes_use_no_git_subprocess tests/qa/test_generate_epic_close_pack.py::test_closed_rails_are_required_without_becoming_candidate_bytes -q

What to look for: feedback dependencies are rejected, causal inputs are fixed, check mode is nonwriting, closed rails are enforced, and lifecycle output is deterministic in temporary repositories.

Required deliverables:


* `audit/qa/hde-epic039/checks/po-011/primary.log`
* `audit/qa/hde-epic039/checks/po-011/primary.log.path_proof.txt`
* Updated manifest entry for `po-011`

PASS criteria: all selected derivation and boundary tests pass with exit `0`; the log lists its sibling receipt proof, and the proof matches the current log path, SHA-256, and size.

FAIL_BEHAVIOR criteria: trustworthy tests show hosted feedback, external attestation, later source state, noncausal metadata, or mutation entering candidate derivation.

FAIL_TOOLING criteria: schema, temporary-repository harness, collection, or evidence writer fails.

TOOLING_BLOCKED criteria: closeout tool, schema, tests, or dependency is unavailable.

Blocked posture: stop; do not invoke the closeout tool against a real source.

Tokens: `intended_tokens: []`; `claimed_tokens: []`.

#### CHECK po-012: PO-012 —

Surface / D-goal mapping: D5 — manifest-committed pair, stable observation, interruption rejection, rollback, and deterministic recovery
Rails: SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=test
Pins: LC_ALL=C LANG=C TZ=UTC
PF anchors: PF10 — HDE Build Notes, §§2.11 and 2.12

Goal / intent: prove that mutually dependent candidate outputs become valid only at the manifest publication point, mixed or changing states fail, interrupted work recovers safely, and reviewed source state remains protected.

Required dependencies: Step-0B PASS; Python; pytest; generic closeout tool and selected publication tests.

Preflight check: helper validates exact selectors and pytest readiness.

If missing, activation/install action: None proven; stop this step.

If still unavailable: TOOLING_BLOCKED.

Preconditions: Step-0B PASS. Tests operate in isolated temporary repositories.

Setup: none.

PO actions:

1. Run Command 1.
2. Confirm all publication, reader, interruption, recovery, rollback, source-protection, and atime-exception tests pass.
3. Inspect the primary log.

Command 1: LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=test python -B audit/qa/hde-epic039/00_meta/qa_runner.py po-012 tests/qa/test_generate_epic_close_pack.py::test_publication_uses_report_first_manifest_commit_point_order tests/qa/test_generate_epic_close_pack.py::test_readers_at_every_publication_boundary_accept_only_complete_generations tests/qa/test_generate_epic_close_pack.py::test_process_termination_is_fail_closed_and_fresh_write_recovers tests/qa/test_generate_epic_close_pack.py::test_process_termination_during_recovery_cleanup_is_safely_recoverable tests/qa/test_generate_epic_close_pack.py::test_manifest_reader_rejects_new_report_with_old_manifest tests/qa/test_generate_epic_close_pack.py::test_manifest_mutation_between_reads_is_rejected tests/qa/test_generate_epic_close_pack.py::test_publication_failure_restores_previous_pair_and_leaves_no_temp_residue tests/qa/test_generate_epic_close_pack.py::test_write_rechecks_worktree_after_final_pair_read tests/qa/test_generate_epic_close_pack.py::test_check_allows_only_relatime_symlink_atime_update -q

What to look for: report-first/manifest-last commitment, complete-generation reads, rejection of mixed or changing bytes, safe recovery, restored prior pair, no residue, protected source state, and only the bounded relatime symlink-atime exception.

Required deliverables:


* `audit/qa/hde-epic039/checks/po-012/primary.log`
* `audit/qa/hde-epic039/checks/po-012/primary.log.path_proof.txt`
* Updated manifest entry for `po-012`

PASS criteria: every selected coherent-publication predicate passes with exit `0`; the log lists its sibling receipt proof, and the proof matches the current log path, SHA-256, and size.

FAIL_BEHAVIOR criteria: trustworthy tests admit mixed, stale, changing, interrupted, unrecoverable, or source-mutating states.

FAIL_TOOLING criteria: temporary-repository harness, publication test mechanism, collection, or evidence writer fails.

TOOLING_BLOCKED criteria: required tool, test, or dependency is unavailable.

Blocked posture: stop; do not publish a real candidate.

Tokens: `intended_tokens: []`; `claimed_tokens: []`.


#### CHECK po-013: PO-013 —

Surface / D-goal mapping: D5 — reusable capability without real-candidate or closure presumption
Rails: SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=test
Pins: LC_ALL=C LANG=C TZ=UTC
PF anchors: PF10 — HDE Build Notes, §§2.12 and 2.16

Goal / intent: prove the reusable closeout capability’s schema, CLI boundary, nonwriting check behavior, and non-Git-subprocess posture while mechanically confirming across the complete current generator-accepted source domain that this run has no real HDE-EPIC039 candidate source or output pair.

Required dependencies: Step-0B PASS; Python; pytest; `tools/qa/generate_epic_close_pack.py`; its current tracked-HEAD tree and model-loading interfaces; schema; manual validation workflow; and selected tests.

Preflight check: the helper validates selectors and pytest readiness before enumerating every regular tracked current-HEAD file and applying the generator’s current model loader to every HDE-EPIC039 candidate marker.

If missing, activation/install action: None proven; stop this step.

If still unavailable: TOOLING_BLOCKED.

Preconditions: Step-0B PASS.

Setup: none.

REPO VALIDATION NOTE: `tools/qa/generate_epic_close_pack.py`, `schemas/epic_close_candidate_source.v1.json`, `.github/workflows/epic-closeout-validation.yml`, and `tests/qa/test_generate_epic_close_pack.py` are current reusable loci. The generator’s source interface accepts a tracked repository-relative candidate source, so the probe covers all regular files in the current tracked HEAD tree rather than only JSON under `audit/`. `audit/EPIC-039_close_report.md` and `audit/EPIC-039_MANIFEST.json` are governed future output loci and are not current inputs to this plan.

PO actions:

1. Run Command 1.
2. Confirm selected generic capability tests pass.
3. Inspect the `PROBE` record.
4. Confirm the complete candidate-source domain was enumerated.
5. Confirm no generator-accepted HDE-EPIC039 source or real output is reported.
6. Treat a source-domain scan failure as FAIL_TOOLING and any detected accepted source or output as TOOLING_BLOCKED scope drift.

Command 1: LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=test python -B audit/qa/hde-epic039/00_meta/qa_runner.py po-013 tests/qa/test_generate_epic_close_pack.py::test_schema_is_closed_and_admits_truthful_dependency_nonclaims tests/qa/test_generate_epic_close_pack.py::test_cli_accepts_exactly_one_source_and_one_mode tests/qa/test_generate_epic_close_pack.py::test_check_mode_is_nonwriting_for_bytes_mode_and_metadata tests/qa/test_generate_epic_close_pack.py::test_modes_use_no_git_subprocess -q

What to look for:

* Generic capability tests pass.
* `candidate_source_domain` states that all regular files in the current tracked HEAD tree accepted by the generator’s repository-relative source interface were covered.
* `tracked_regular_files_examined` is a positive integer.
* `candidate_source_domain_error` is absent.
* `missing_reusable_capability_loci` is empty.
* `real_candidate_outputs_present` is empty.
* `real_candidate_sources_present` is empty.
* Marker-shaped files rejected by the current generator may appear only in `candidate_marker_sources_rejected_by_generator`; they do not count as accepted sources.

Required deliverables:


* `audit/qa/hde-epic039/checks/po-013/primary.log`
* `audit/qa/hde-epic039/checks/po-013/primary.log.path_proof.txt`
* Updated manifest entry for `po-013`
* Complete source-domain and output-state probe embedded in the primary log

PASS criteria: generic tests pass, reusable loci exist, the complete current tracked-HEAD source domain is enumerated through the generator’s current source-validation behavior, and no generator-accepted HDE-EPIC039 source or real output is found; the log lists its sibling receipt proof, and the proof matches the current log path, SHA-256, and size.

FAIL_BEHAVIOR criteria: trustworthy generic capability tests contradict the reusable tool’s schema, CLI, or nonwriting behavior.

FAIL_TOOLING criteria: test execution, tracked-HEAD enumeration, Git-object reading, source parsing, generator validation, probe, harness, or evidence publication malfunctions or leaves the accepted-source domain incomplete.

TOOLING_BLOCKED criteria: reusable loci are unavailable or a generator-accepted HDE-EPIC039 source or real output is detected, making this reusable-capability-only plan stale.

Blocked posture: stop and require a fresh bounded plan decision. Do not validate, overwrite, delete, or publish the candidate.

Tokens: `intended_tokens: []`; `claimed_tokens: []`.


### Close-out deliverables

Run closeout finalization after:

* all fourteen checks are PASS; or
* the first unresolved non-PASS result, leaving later artifacts NOT RUN.

Required dependencies: Python; the validated QA-created runner; `tools/qa/qa_harness.py`; its current `verify_manifest_entry` interface; and the `tools/evidence/update_evidence_index.py` receipt-proof writer used by the pinned helper.

Preflight check: Step-0B Command 3 must still pass. The finalizer must strictly parse the flat manifest, call `verify_manifest_entry` separately for every planned check that has an entry, and validate that each referenced primary log binds a sibling proof whose path, SHA-256, and size match the current log.

If missing, activation/install action: None proven; stop finalization.

If still unavailable: FAIL_TOOLING; required closeout deliverables are incomplete and the recommendation is `NOT READY`.

PO actions:

1. Run the finalization command.
2. Inspect its JSON result.
3. Verify the summary, summary proof, manifest, and manifest proof.
4. Verify every executed check’s concrete `primary.log.path_proof.txt` deliverable listed below.
5. Confirm every COVERED row has a step-scoped primary-log pointer that passed `verify_manifest_entry` and receipt-proof validation.
6. A nonzero finalization exit means the recommendation is `NOT READY`; do not force PASS.

Command 1: LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=test python -B audit/qa/hde-epic039/00_meta/qa_runner.py finalize

Expected result when every check is PASS and trusted under an approved revision that permits every check to PASS: exits `0`, reports `READY FOR PRODUCT OWNER QA CLOSEOUT REVIEW`, reports both proof-valid fields as `true`, and contains no untrusted, blocked, not-run, non-PASS, extra, identity-mismatched, or receipt-proof-invalid entry.

Expected result for this revision: after `po-003` records a trusted `PASS`, `po-004` through `po-013` remain reachable in plan order; when all fourteen checks are trusted `PASS`, the finalizer exits `0` and reports `READY FOR PRODUCT OWNER QA CLOSEOUT REVIEW`; otherwise it reports `NOT READY` and exits nonzero.

Expected result after any other incomplete, malformed, untrusted, non-PASS, identity-mismatched, or receipt-proof-invalid ladder: creates the summary and available proofs where possible, reports `NOT READY`, and exits nonzero.

Required closeout deliverables:

* Discovery artifact: `audit/qa/hde-epic039/00_meta/discovery.json`
* QA RCA & Doc Delta summary: `audit/qa/hde-epic039/00_meta/qa_rca_doc_delta_summary.md`
* Summary proof: `audit/qa/hde-epic039/00_meta/qa_rca_doc_delta_summary.md.path_proof.txt`
* Step-log manifest: `audit/qa/hde-epic039/qa_step_logs_manifest.json`
* Manifest proof: `audit/qa/hde-epic039/qa_step_logs_manifest.json.path_proof.txt`
* Per-check primary-log receipt proofs:

  * `audit/qa/hde-epic039/checks/step-0b-doc-delta-capture/primary.log.path_proof.txt`
  * `audit/qa/hde-epic039/checks/po-001/primary.log.path_proof.txt`
  * `audit/qa/hde-epic039/checks/po-002/primary.log.path_proof.txt`
  * `audit/qa/hde-epic039/checks/po-003/primary.log.path_proof.txt`
  * `audit/qa/hde-epic039/checks/po-004/primary.log.path_proof.txt`
  * `audit/qa/hde-epic039/checks/po-005/primary.log.path_proof.txt`
  * `audit/qa/hde-epic039/checks/po-006/primary.log.path_proof.txt`
  * `audit/qa/hde-epic039/checks/po-007/primary.log.path_proof.txt`
  * `audit/qa/hde-epic039/checks/po-008/primary.log.path_proof.txt`
  * `audit/qa/hde-epic039/checks/po-009/primary.log.path_proof.txt`
  * `audit/qa/hde-epic039/checks/po-010/primary.log.path_proof.txt`
  * `audit/qa/hde-epic039/checks/po-011/primary.log.path_proof.txt`
  * `audit/qa/hde-epic039/checks/po-012/primary.log.path_proof.txt`
  * `audit/qa/hde-epic039/checks/po-013/primary.log.path_proof.txt`
* Preserved Doc Delta pair:

  * `audit/docdeltas/hde-epic039_doc_deltas.md`
  * `audit/qa/hde-epic039/00_meta/doc_deltas.md`

#### What “QA RCA & Doc Delta summary” means (explicit; non-drifting)

The generated summary must:

* state either the new Live QA findings or “No new Live QA deltas found”;
* preserve the existing proof-bearing Doc Delta pair;
* map later doc-drain intent to PF14, PF04, and PF09.1 by title;
* list every check in plan order;
* classify every check as COVERED, BLOCKED/UNEXECUTABLE, or NOT RUN;
* provide a step-scoped primary-log pointer for every COVERED check;

* classify a check as COVERED only after `verify_manifest_entry` validates its referenced log, v2 header, self-binding, check identity, log path, and status agreement, and after the log’s bound sibling receipt proof matches the current log path, SHA-256, and size;
* record that no dependency installation or Moon Loop was authorized or executed;
* enumerate remaining open or deferred work;
* keep undrained documentation work nonblocking when QA evidence is otherwise complete;
* keep repo-supported completion, canon-drain completion, and formal close-pack completion separate;
* make no acceptance, deployment, PF09-edit, close-pack, or epic-closure claim.

PASS criteria for closeout finalization:

* The manifest contains exactly the fourteen planned check IDs.
* Every planned entry is `PASS` under an approved plan revision that authorizes every check to PASS.
* `verify_manifest_entry` succeeds separately for every planned check.
* Every referenced primary log exists, has a valid v2 header and self-binding, matches the planned check identity and log path, agrees with the manifest status, lists its sibling receipt proof, and has a receipt proof matching its current path, SHA-256, and size.
* Summary and manifest sibling proofs match current bytes and sizes.
* The recommendation is `READY FOR PRODUCT OWNER QA CLOSEOUT REVIEW`.

FAIL criteria:

* A trustworthy non-PASS `po-003` entry stops the ladder, leaves later unexecuted checks NOT RUN, and makes the recommendation `NOT READY`.
* A missing planned entry remains NOT RUN and makes the recommendation `NOT READY`.
* An extra entry makes the recommendation `NOT READY`.
* A malformed manifest, failed `verify_manifest_entry`, missing or invalid primary-log receipt proof, or receipt-proof binding mismatch is untrusted evidence, classifies the affected check as BLOCKED/UNEXECUTABLE, and makes the recommendation `NOT READY`.
* A non-PASS or identity-mismatched entry makes the recommendation `NOT READY`.
* Missing or invalid summary or manifest proofs are FAIL_TOOLING.
* Future steps that never executed remain NOT RUN and are not mislabeled as missing executed evidence.

### Review guardrails

#### Hard blockers for plan approval/execution

Stop execution when any of the following occurs:

* A command would require an unlisted path, selector, route, helper, environment variable, secret, or target.
* The QA-created helper differs from the pinned SHA-256.
* Required rails or determinism pins cannot be established.
* Step-0B is not PASS.

* A required dependency is unavailable under the approved closed rails; classify the affected step as TOOLING_BLOCKED without installation or retry.
* A primary log or manifest entry cannot be written through the current harness.
* A real HDE-EPIC039 candidate is detected.
* A check produces unresolved FAIL_BEHAVIOR, FAIL_TOOLING, or TOOLING_BLOCKED.
* A required closeout artifact or proof remains untrusted.
* Continuing would require product, test, generator, governed-artifact, workflow, PF, OPS, deployment, or external-service changes.

Do not invent alternatives. Preserve the governed state and run closeout finalization.

#### PF09 phased-routing boundary

| Plan activity                                     | PF09 disposition                                                                               |
| ------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `po-001` and `po-003`                             | Evidence for existing HDE-CALC002.2 scope; no status edit                                      |
| `po-002`                                          | Evidence for existing HDE-CALC002.3 scope; no status edit                                      |
| `po-004` and `po-005`                             | Evidence for existing HDE-CALC003.10 and HDE-CALC003.11 scope; no status edit                  |
| `po-006`, `po-007`, and `po-008`                  | Evidence for existing HDE-CALC003.13, HDE-CALC003.14, and HDE-CALC003.15 scope; no status edit |
| `po-009` and `po-010`                             | Evidence for existing HDE-CALC003.21 scope; no status edit                                     |
| `po-011`, `po-012`, and `po-013`                  | Evidence for existing HDE-CALC003.22 scope; no status edit                                     |
| QA runner, logs, manifest, discovery, and summary | QA execution/evidence assembly only; no new PF09 task                                          |
| PF14, PF04, and PF09.1 follow-up                  | Documentation/status drainage only; Product Owner-owned                                        |

This runbook does not create free-floating implementation, QA, or OPS backlog.

#### Review-record identifier boundary

This runbook creates no review-record identifier and assigns no finding counter. Any later review IDs belong to the reviewing artifact and must not be retrofitted into these check identities.

#### QA planning QoS guardrails - templates, deferred steps, and prompt-family separation

##### Template semantics: future-step artifacts

* PRESENT means the artifact exists and is referenced.
* MISSING means its producing step executed but the required artifact is absent or unproven.
* NOT RUN / DEFERRED means the producing step has not executed and no artifact is expected yet.

No future primary log, manifest proof, summary, or summary proof is treated as present before its producing action runs.

##### Prompt-family separation: AUTHORING vs REVIEW modes for QA prompts

This document is AUTHORING output. It is the executable runbook, not an approval review or QA result.

A later REVIEW prompt must review this runbook or its evidence without silently authoring replacement commands, except where a separately authorized remediation route permits reuse of approved commands.

##### QoS stop-rule: iteration churn escalation

On the first controlling structural, helper, evidence, dependency, or execution failure, stop. Do not install dependencies, retry through an unapproved recovery, or continue patching this runbook in-session. Route corrective work to systems RCA and the appropriate plan, implementation, or documentation owner.

##### Redline bundle construction discipline (required for editorial redline sets)

Not applicable. This runbook creates no editorial redline bundle.

##### Review stability and no-moving-target discipline (required for diff-first approval loops)

Approval binds to this revision’s check IDs, proof targets, rails, concrete paths, command families, evidence identities, tokenless posture, and nonclaims.

After approval, do not change selectors, helper bytes, paths, rails, status predicates, or deliverables during execution. A substantive change requires a new plan revision and approval.

ASK OK?
