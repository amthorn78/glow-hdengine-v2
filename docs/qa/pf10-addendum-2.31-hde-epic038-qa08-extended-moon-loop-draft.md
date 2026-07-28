# Draft PF10 Addendum Candidate — Non-Canonical

Publication note: This candidate was prepared at the Product Owner's direction. Repository review resolves the intended canonical publication target as `docs/pfcanon/PF10-HDE-Build-Notes-v12.4.8b.md`, after Addendum 2.30, with the index entry below. No canonical insertion was performed because the request was to draft the addendum, not publish it. Until publication occurs, this file creates no canon authority; remove this wrapper when inserting the addendum canonically.

Proposed Addendum Index entry: `2.31) HDE-EPIC038 qa-08-po-008 — PO-Approved Extended Moon Loop Remediation and CI Completion Authority`

---

## 2.31) HDE-EPIC038 qa-08-po-008 — PO-Approved Extended Moon Loop Remediation and CI Completion Authority

Timestamp: 072826 00:35
Details: This addendum records the Product Owner-approved extended remediation that was required to execute and close `qa-08-po-008` safely, preserve its one-time live-vendor authority boundary, correct the causal-chain and evidence-provenance defects exposed by the step, route the corrections through reviewable PR posture and merge, and continue through a second PR until hosted CI was clean. It also establishes the narrowly governed term **PO-approved Extended Moon Loop remediation** for cases in which live QA exposes functional drift or causal uncertainty that cannot be resolved inside the ordinary QA-root-only Moon Loop.

### **Decision summary**

The Product Owner makes the following decisions:

1. A QA run must not depend on equality to a preplanned Git commit. Source identity is execution provenance, not a readiness, behavior, routing, or PASS predicate. The fixed-HEAD condition supplied for `qa-08-po-008` was a planning defect and was overridden. QA must still capture actual execution-source identity, validate the required current code posture, and preserve routing provenance. This rule prohibits equality to a stale preplanned HEAD as a QA validity predicate; it does not waive clean-source checks, authorization-bound source identity, routed-artifact provenance, OPS source binding, or exact-source release-attestation verification.
2. When the approved proof objective remains stable but live execution reveals planning defects, functional drift, safety defects, evidence-generator defects, governed-companion defects, or downstream CI defects, repeatedly revising and reissuing the plan is not mandatory. The defects may be corrected in place through a PO-approved Extended Moon Loop remediation.
3. An Extended Moon Loop may cross code, tests, plan/bootstrap instructions, governed generators, canonical companion refreshes, PR routing, and hosted CI when each change is causally necessary to establish the original approved proof and required CI-clean integrated repository state.
4. Extended Moon Loop authority is not ordinary Moon Loop authority. Product code, repo tests, repo generators, and governed artifacts outside the QA root remain remediation work and retain their normal PR, OPS, QA plan update, or documentation update routing requirements.
5. Uncertainty is resolved through inspection, the smallest causally complete correction, regression proof, canonical regeneration, routing, and final validation. Uncertainty permits read-only investigation only; a write requires an evidenced causal defect and authority covering the affected surface. Uncertainty does not authorize speculative refactoring, feature expansion, or unrelated cleanup.
6. `qa-08-po-008` received one fresh authorization for one live generation event, bounded to two vendor requests. That authority expired immediately after the event. Neither this addendum, the retained proof, a receipt, configuration presence, a merge, nor successful CI authorizes another call.
7. The Product Owner confirmed for this execution event that the only available vendor API base/environment target was the canonical live v2 base `https://api.humandesignapi.nl/v2`, and stated that no separately marked staging, sandbox, test, mock, development, or nonproduction base was available or expected. This is an event-grounded PO decision, not a general vendor-endpoint inventory or future-availability claim. The base must not be described as nonproduction. `APP_ENV=dev` constrained only the local application invocation.
8. The source correction was required before the call because the inspected producer could otherwise self-open rails, accept authority or client-injection bypasses, accept personal input overrides, retain false historical provenance, or permit a wider target posture. The PO approved correcting those defects in the active QA execution rather than allowing the unsafe posture to survive toward production.
9. The narrow QA behavioral PASS, PR routing, merge state, and hosted-CI completion are separate facts. `qa-08-po-008` finalized PASS before hosted CI ran. PR #371 was not CI-clean. A CI-clean integrated repository state was established only by PR #372 and the successful post-merge `main` workflow.
10. The instruction to continue until CI was clean was a completion condition for the identified causal chain. It did not widen product scope, renew live-call authority, or authorize unrelated changes.
11. No public or application-runtime implementation under `engine/**` or `adapter/**` changed. Functional source changes were confined to the live evidence producer and canonical evidence-index owner; the remaining changes were regression tests, runbook correction, QA evidence, and canonically generated companions.

### 2. Terminology and ordinary Moon Loop boundary

#### Functional drift

For this addendum, **functional drift** is a material difference between the approved proof objective and the behavior of the integrated plan, bootstrap, implementation, evidence generator, governed companion graph, or CI pipeline encountered during execution.

This event also exposed planning, tooling, evidence, conditionality, provenance, isolation, and CI defects. Each defect retains its own governing classification. The Extended Moon Loop label does not alter `FAIL_BEHAVIOR`, `FAIL_TOOLING`, `TOOLING_BLOCKED`, planning-defect, evidence-defect, or CI-failure meaning.

Functional drift may exist even when an isolated behavior appears correct. Examples include a proof producer that silently opens its own rails, a conditional artifact treated as globally mandatory, a current artifact indexed with a historical timestamp, an isolated release build that rewrites retained evidence outside its permitted graph, or a hosted gate evaluating stale canonical evidence.

#### Causal uncertainty

**Causal uncertainty** is uncertainty that cannot be resolved reliably at plan-review time and becomes observable only while executing the approved proof or its required integration gates. It includes uncertainty about:

* whether a planned command is executable in the actual repository;
* whether a safety predicate is enforced at every call boundary;
* whether a governed artifact remains conditional outside its generating event;
* whether canonical companion ownership reaches a fixed point;
* whether isolated release validation preserves retained provenance; and
* whether the final routed source passes the hosted gates required for CI-clean completion.

#### PO-approved Extended Moon Loop remediation

A **PO-approved Extended Moon Loop remediation** is an event-bound, repository-anchored, routed continuation of one identified QA or hosted-CI failure, blocker, or evidenced safety defect after the ordinary Moon Loop boundary has been exceeded.

“Extended” describes the causal and delivery lineage: the work may span multiple focused commits, PR or merge cycles, hosted-CI reruns, and mechanically necessary canonical companion refreshes. It does not enlarge the approved proof target, runtime or product scope, rails posture, secret posture, evidence identity, acceptance posture, or nonclaims. It does not relabel source or non-QA-root remediation as ordinary Moon Loop correction.

The ordinary Moon Loop defined by the Glow QA Guide, §3.4.8, “Rails posture for manual Live QA,” and the Canon Epic Process Guide, §1.1.11, “Plan review rules (content-first; blockers vs caveats),” remains controlling for ordinary minimal QA-root-only correction. A published version of this addendum would define a separate Extended Moon Loop process, but would not relabel routed work as ordinary Moon Loop correction. For each event, fresh PO approval must be recorded before the corresponding action. Only the stop-and-issue-another-plan requirement is displaced after that approval; routing, evidence ownership, safety, and final-proof requirements remain in force.

### 3. Extended Moon Loop operating rules

#### 3.1 Invocation

An Extended Moon Loop exists only after fresh, explicit Product Owner direction. The direction must identify or make unambiguous:

* the epic and QA check or hosted-CI run;
* the repository or routed-source anchor;
* the triggering failure, blocker, or safety discovery;
* the unchanged proof objective and PASS or FAIL meaning;
* the allowed causal scope;
* the rails, network, credential, and data-safety posture;
* whether code change, PR publication, merge, and CI completion are authorized;
* the completion gate; and
* any one-time authority that must expire separately.

Each action class must be expressly authorized before use; an omitted action class is unauthorized. Approval of investigation or one action class does not imply code-write, external-call, publication, merge, OPS, deployment, or rerun authority.

Required authorization must be recorded before the corresponding write, external call, publication, or merge action. Later HDE Build Notes or evidence binding records that authority; it cannot create authority retroactively. A new remediation plan is not required when the original proof identity is stable and the above facts are clear.

#### 3.2 Causal-closure rule

The loop may correct each separately evidenced root cause encountered in the required proof and CI-completion chain, plus the minimum regression tests and canonical companion refreshes needed to prevent recurrence.

A newly exposed defect remains inside the same Extended Moon Loop only when all of the following are true:

1. It is produced by, blocks, or invalidates the original correction or a required downstream gate.
2. Its relationship to the original proof chain is recorded.
3. Correcting it does not change the proof objective, acceptance surface, public contract, endpoint family, evidence family, or epic scope.
4. The correction is routed according to the kind of file or system changed.

An independent or opportunistic defect requires a separate PO disposition.

#### 3.3 No forced-replanning rule

When causal closure remains satisfied within a freshly authorized Extended Moon Loop event, the operator continues that remediation lineage instead of restarting discovery or issuing serial plan revisions. The execution record must absorb the new facts, decisions, receipts, and validation results.

Replanning is required only when the desired proof, product behavior, acceptance criteria, public boundary, endpoint family, evidence family, or substantive epic scope changes.

Continuation authority is never inferred from the `qa-08-po-008` record. A future event requires fresh explicit PO direction before its first write or external action. A new path, system, proof goal, public behavior, evidence family, or independent root cause requires fresh PO disposition.

#### 3.4 Routing and evidence

Code, repo tests, evidence generators, and governed artifacts outside the QA root remain routed remediation. They must be carried by the applicable PR, OPS, QA plan update, or documentation update posture before they can support the affected QA step's final PASS.

The record must preserve:

* the original failed, blocked, or pre-routing receipt;
* each material root-cause finding;
* the exact changed paths or reviewable diff;
* canonical generator commands for governed outputs;
* local regression results;
* PR, routing, and merge receipts;
* intermediate hosted-CI failures;
* the final accepted QA receipt; and
* the final clean hosted-CI source and run when CI cleanliness is a completion condition.

Governed artifacts remain canonical-tool-only. Primary artifacts, checksums, path proofs, Human Index rows, Machine Mirror rows, and self-records must be refreshed as one coherent family when applicable.

For this event, `qa-08-po-008` PASS came only from its approved post-route finalization predicates. PR #372 established a CI-clean integrated repository state; it did not create another QA PASS or retroactively alter the earlier receipt.

#### 3.5 Authority limits

An Extended Moon Loop does not by itself authorize:

* another vendor, database, deployment, migration, service-start, or OPS action;
* a new endpoint or a wider target allowlist;
* a new feature, route, public contract, payload field, acceptance criterion, token, or evidence family;
* a raw request, response, personal input, credential, or vendor payload capture;
* a PF09 status change, board movement, deployment claim, acceptance claim, or epic closeout;
* bypassing PR routing, canonical evidence owners, review, or hosted CI; or
* recurring authority derived from a previous one-time approval.

#### 3.6 Completion and expiry

The loop completes only when:

1. the original approved proof satisfies its final predicates;
2. every required routed correction is present in the validation workspace;
3. canonical evidence companions are coherent;
4. the named local regression gates pass;
5. the final hosted CI passes on the routed or merged source when CI is in the completion condition; and
6. the record preserves the full receipt lineage without converting earlier failures into PASS.

Extended authority expires at completion. One-time live, OPS, merge, or deployment authorities expire according to their own narrower terms and are never extended implicitly.

### 4. Event trigger and PO authority for qa-08-po-008

The approved step intended to prove one bounded, same-input, independently checked live vendor acquisition event. Execution exposed planning and producer defects before the call, a companion-provenance defect during the required post-generation refresh, and integration defects when hosted CI ran.

Pre-call planning and producer defects were:

* the Variable Import block required equality to a historical HEAD;
* bootstrap content contained nested-quote corruption and duplicated path-command fragments;
* the readiness predicate required a nonproduction marker that the sole canonical vendor API base/environment target cannot possess;
* the plan failed to distinguish local `APP_ENV=dev` from external target classification;
* final closed-rails artifact validation was coupled to live target and credential readiness;
* the producer accepted a reusable confirmation string without an event-bound receipt;
* the producer could construct its client with internally forced open rails;
* injected client paths could bypass the intended readiness boundary;
* optional environment variables could replace built-in synthetic inputs;
* live-proof provenance used a historical constant rather than the current event time; and
* check-mode environment handling did not mechanically demonstrate that target, credentials, confirmation, and receipt were absent.

During the required post-generation companion refresh, the canonical index owner was found to assign the live row the same historical timestamp rather than deriving current provenance from the validated artifact. The later hosted-CI integration defects are recorded separately in Section 8.

The Product Owner then:

1. waived the fixed-HEAD equality gate and directed that all QA runs be HEAD-independent;
2. directed that bootstrap defects be fixed in place instead of starting another revision cycle;
3. confirmed for this event that the exact canonical live v2 base was the only available vendor API base/environment target and that no separately marked alternative was available or expected;
4. freshly authorized one live event with no more than two requests;
5. approved correcting any producer defect discovered in this path so the unsafe posture could not reach production;
6. directed continuation through routing and merge; and
7. after hosted failures appeared, directed that the CI failures be corrected without stopping until CI was clean.

These directions constitute the event-specific Extended Moon Loop authority. They did not authorize a second live generation event.

### 5. Repository, proof, routing, and CI map

| Item | Receipt or identity | Meaning |
| --- | --- | --- |
| Initial inspected source | `376914bf765a9c0c1900a74f9214f5e346f790c1` | Provenance anchor only; not an execution gate |
| Approved step | `qa-08-po-008` / `PO-008` | Original proof objective and verdict taxonomy remained unchanged |
| Live proof generation time | `2026-07-27T23:38:09Z` | Actual event time retained in the governed proof |
| Governed proof | `audit/gates/determinism/open_rails_vendor_abba.json` | Two-request, same-input, canonical AB/BA proof |
| Governed proof SHA-256 | `24068e135d24dcb7cc88c4431dfae62dbac236b708545307cba7b9e11278138b` | Current proof-byte binding |
| Pre-routing receipt | `commit:5f57b049b605105cccb9c7fa4cec99a67c308846` | Later durable receipt preserving the authorized generation and intentional routing-pending `TOOLING_BLOCKED` record; not asserted as the live-call HEAD |
| Routing receipt used by finalization | `PR#371@30e93dfa2d9bd24779e35a6433a034fc996b6ae4` | Current proof and companion refresh were in PO-approved PR posture |
| Final PR #371 head / final-log commit | `544e680a06eadee6214bbd8e7c5ffcc18fd87798` | Preserved post-route closed-rails finalization |
| PR #371 merge | `870e0db41f78a7ab49a87dc56bcefd1859d53c06` | Merged qa-08 remediation; not CI-clean |
| Final QA log | `audit/qa/hde-epic038/checks/qa-08-po-008/primary.log` | `PASS`, exit `0`, closed rails, routing proof separate from behavior proof |
| Final QA log SHA-256 | `a951cf95094797a05415bf4b46c2031e53774b390ee300227e40870437f3f856` | Final log-byte binding |
| PR #372 correction commits | `d754e6f587c3f72b8c338adaba24925eaa40d9a4`; `86a260af3bf7e6ebcb58eeabf1b1b89e21d17764` | Closed-rails CI integration and canonical fixed-point correction |
| PR #372 merge and final clean-CI integrated source | `b08d9dc47f31baa79101a323795237fde4e25b53` | CI-clean integrated repository state |
| Final `main` CI | GitHub Actions run `30317268158` | All seven jobs passed |


For this PASS, “post-route” meant present in the PO-approved PR posture at `PR#371@30e93dfa2d9bd24779e35a6433a034fc996b6ae4`; it did not mean formal GitHub review approval, merge, or hosted-CI completion.

PR references:

* PR #371: `https://github.com/amthorn78/glow-hdengine-v2/pull/371`
* PR #372: `https://github.com/amthorn78/glow-hdengine-v2/pull/372`
* Final `main` workflow: `https://github.com/amthorn78/glow-hdengine-v2/actions/runs/30317268158`

### 6. PR #371 — live-proof authority, safety, provenance, and finalization

PR #371 contained three focused commits:

1. `5f57b049b605105cccb9c7fa4cec99a67c308846` — live-proof authority rails;
2. `30e93dfa2d9bd24779e35a6433a034fc996b6ae4` — proof provenance and canonical companions; and
3. `544e680a06eadee6214bbd8e7c5ffcc18fd87798` — post-route QA finalization.

#### 6.1 Approved plan and bootstrap correction

Path: `docs/qa/r7-qa-plan-hde-epic038.md`

Changes:

* converted fixed HEAD from a hard gate to captured provenance;
* recorded the PO override and the rule that future QA generation must not reintroduce fixed-HEAD execution gating;
* fixed Profile C nested quoting;
* repaired corrupted `qa-06-po-006` and `qa-07-po-007` path-preflight commands;
* moved Profile D readiness into the producer's value-safe readiness command;
* permitted only the valid Profile D rail tuples `0:1` for generation and `1:0` for closed validation;
* replaced the impossible marker-based endpoint rule with exact canonical vendor API base/environment-target classification;
* recorded the PO's event-specific statement that no separately marked nonproduction base was available or expected;
* separated local `APP_ENV=dev` from external target classification;
* added a unique, unprinted `QA08_PO_EVENT_RECEIPT`;
* required immediate clearing of the confirmation and event receipt after generation;
* removed live readiness from closed finalization;
* explicitly unset keys, endpoint variables, authorization confirmation, and event receipt before independent check and finalization; and
* recorded the source-correction exception and its production-safety reason.

Why required:

The original bootstrap could not be executed reliably, its target predicate rejected the only available vendor API base/environment target identified by the PO, and its fixed-source gate would turn normal routed change into false invalidation. More importantly, closed artifact checks should not require live credentials or retain ambient authority. These were planning and execution defects, not failures of the intended AB/BA behavior.

#### 6.2 Live-proof producer correction

Path: `tools/evidence/generate_open_rails_abba_proof.py`

Changes:

* exact-target allowlisting for the sole canonical v2 base;
* canonical-variable precedence with compatibility alias allowed only when the canonical variable is absent;
* fail-closed rejection when canonical and alias posture is ambiguous;
* value-safe `--live-readiness-check`;
* mandatory caller-supplied `SAFE_MODE=0`, `ALLOW_NETWORK=1`, `APP_ENV=dev`, `LC_ALL=C`, `LANG=C`, and `TZ=UTC`;
* mandatory fresh confirmation, both credential presences, unique event receipt, and absence of all optional personal-input variables before client creation;
* an event-receipt format, digest-only retention, existing-artifact reuse check, and explicit reuse refusal;
* exact authority scope `one_generation_two_requests_no_recurring_authority`;
* target identity retained as an identifier and SHA-256 rather than a raw URL in the proof;
* a minimal allowlisted client environment instead of merging ambient environment values and internally forcing rails open;
* readiness enforcement before the default or injected client path can be used;
* built-in fabricated synthetic inputs as the only accepted live inputs;
* no more than two total requests, one attempt per request, and bounded connect, read, and total timeouts;
* actual UTC generation time instead of the historical `2026-07-14T00:00:00Z` constant;
* explicit retained truth that the vendor API base/environment target is canonical live and is not proven nonproduction;
* exact route-policy, target, secret-presence, synthetic-input, receipt, timestamp, authority, and top-level proof-shape validation;
* recursive forbidden-key and forbidden-string validation for raw payload, personal input, credential, authorization, and URL residue;
* pass-only artifact writes;
* credential-free, endpoint-free, authority-free, network-free `--live --check`; and
* no check-mode vendor re-execution.

Why required:

The earlier producer could satisfy open rails by overwriting the caller's environment at client construction. That design weakened the closed-default guarantee and could allow a future production path to perform network I/O despite incorrect caller posture. The producer also lacked an event-bound authority primitive, allowed personal-input substitution, exposed an injected-client bypass boundary, and attached historical provenance to a current claim. A one-time live proof is trustworthy only when the producer itself refuses every wider posture before network-client creation.

#### 6.3 Producer regression tests

Path: `tests/evidence/test_open_rails_abba_proof.py`

Coverage added or strengthened:

* exact-target readiness success;
* refusal for each missing or widened rail, pin, authorization, receipt, credential, or synthetic-input condition;
* canonical and alias precedence;
* event-receipt reuse refusal;
* refusal before proof construction or client creation;
* closed-rails refusal before client creation;
* injected-client-path safety;
* exact two-request and one-attempt behavior;
* distinct input and normalized-payload binding;
* same-input AB/BA reuse and two-run equality;
* check-mode no-I/O;
* failed, inconclusive, noncanonical, or Unicode-escaped artifact refusal;
* independently derived AB/BA identity;
* no-overwrite behavior for a nonpassing proof; and
* closed-schema and recursive safety drift rejection.

Why required:

The new restrictions are production safety properties, not one-off runbook conventions. Regression tests had to prove refusal occurs before any client can be created and that later changes cannot silently restore self-open rails, reusable authority, personal input, check-mode I/O, or self-attested proof fields.

#### 6.4 Current-event provenance and canonical index ownership

Path: `tools/evidence/update_evidence_index.py`

PR #371 changes:

* removed the historical fixed `produced_at_utc` for the live row;
* loaded the timestamp from the present, validated, passing live proof;
* rejected malformed timestamps, wrong artifact kind, nonpassing posture, or acceptance-token overclaim;
* made an ordinary non-isolated refresh rewrite an unchanged-hash path proof when its explicit produced timestamp is wrong; and
* updated the live row note to state event-bound exact-target posture and no recurring authority.

Why required:

A current live interaction indexed with a historical timestamp is false provenance. Hash equality alone cannot justify retaining an explicitly incorrect production time. The sole index owner had to derive the time from the validated artifact and correct stale companion provenance.

#### 6.5 Updater and path-proof regression tests

Paths:

* `tests/ops/test_evidence_index.py`
* `tests/evidence/test_evidence_skeleton.py`

PR #371 coverage:

* current live-row timestamp is derived from the artifact;
* malformed timestamp and nonpassing live posture fail closed; and
* explicit produced-time correction rewrites an unchanged-hash proof in an ordinary source-tree refresh.

Why required:

These tests bind the producer's current event time to the Human Index and Machine Mirror and prevent a future fallback to the historical constant or hash-only stale provenance.

#### 6.6 Governed proof and companion refresh

Primary proof:

* `audit/gates/determinism/open_rails_vendor_abba.json`
* `audit/gates/determinism/open_rails_vendor_abba.json.path_proof.txt`

Human Index family:

* `docs/evidence/INDEX.json`
* `docs/evidence/INDEX.json.path_proof.txt`
* `docs/evidence/INDEX.sha256`
* `docs/evidence/INDEX.sha256.path_proof.txt`

Machine Mirror family:

* `artifacts/evidence_index.jsonl`
* `artifacts/evidence_index.jsonl.path_proof.txt`
* `artifacts/evidence_index.jsonl.sha256`
* `artifacts/evidence_index.jsonl.sha256.path_proof.txt`

Changes:

* replaced the historical live capture with the freshly authorized current proof;
* bound the actual generation time, proof hash, size, target identifier/hash, authority scope, and event-receipt digest;
* recorded the sole-endpoint rationale without claiming nonproduction classification;
* refreshed Human Index and Machine Mirror rows through the canonical updater;
* refreshed hash sentinels, path proofs, and mirror self-record coherence.

Why required:

The approved step required a current artifact and sole-owner companion refresh before finalization. Manual edits were prohibited. The current event could not support PASS while the ledgers retained historical time or stale proof bytes.

#### 6.7 Final QA record

Path: `audit/qa/hde-epic038/checks/qa-08-po-008/primary.log`

The final log records:

* `PASS`;
* behavior exit code `0`;
* `SAFE_MODE=1` and `ALLOW_NETWORK=0`;
* non-`NONE` routing and pre-routing receipts;
* current proof check `result=pass`, `status=OK`, and `top_level_pass=true`;
* updater `--check` under closed rails; and
* routing proof separately from `BEHAVIOR_PROOF=CLOSED_RAILS_CURRENT_ARTIFACT_AND_COMPANION_VALIDATION`.

The target, credentials, confirmation, and event receipt were unset for finalization. The log contains no credential or endpoint values, authorization-header values, personal-input values, request or response bodies, or raw vendor payload.

### 7. qa-08 execution chronology and PASS basis

1. Before the call, the PO overrode fixed-HEAD equality, identified the exact canonical live v2 base as the sole available vendor API base/environment target for the event, freshly authorized one event, and approved the in-place safety correction.
2. At `2026-07-27T23:38:09Z`, the producer attempted and completed exactly two vendor requests using fabricated synthetic defaults, with one attempt per request and no retry.
3. The proof recorded distinct input fingerprints, distinct normalized-payload SHA-256 bindings, same-input reuse, canonical JSON, one final LF, AB/BA byte identity, two-run AB and BA identity, no-raw-payload and no-secret-value predicates, and `acceptance_token_satisfied=false`.
4. The proof truthfully recorded `non_production_environment.proven=false` because no separately marked nonproduction base was available for the canonical live target.
5. Independent validation ran under closed rails after target, credential, confirmation, and event-receipt variables were removed.
6. The generation record intentionally remained `TOOLING_BLOCKED`, exit `125`, with `ROUTING_STATUS=PR_PENDING`. Successful generation awaiting routing was not mislabeled PASS.
7. Commit `5f57b049b605105cccb9c7fa4cec99a67c308846` preserved the pre-routing receipt.
8. The canonical companion refresh was recorded in `30e93dfa2d9bd24779e35a6433a034fc996b6ae4` and routed through PR #371.
9. Post-route finalization—meaning present in the PO-approved PR posture, not merged or CI-clean—ran exactly once under closed rails, checked the current proof and companion graph, and recorded PASS at `2026-07-27T23:51:41Z`.
10. Commit `544e680a06eadee6214bbd8e7c5ffcc18fd87798` preserved that final record.

The step's approved PASS criteria were satisfied because current authorization was recorded by generation, the producer and independent check succeeded, the pre-routing receipt was preserved, the routed current artifact and companion receipt were present, both final closed-rails checks exited `0`, and routing proof remained distinct from behavioral proof.

### 8. Hosted-CI failure after PR #371

The qa-08 behavioral PASS did not establish hosted-CI cleanliness.

PR #371's push workflow `30315572042` completed red at `2026-07-27T23:55:37Z`, and its pull-request workflow `30315574425` completed red at `2026-07-27T23:56:13Z`. PR #371 then merged at `2026-07-27T23:57:15Z`, after both PR-head workflows were already red. The first post-merge `main` workflow `30315806448` failed through `2026-07-28T00:00:14Z`. The failed jobs were `test` and `sanity-pipeline`, and three causal integration defects were established:

1. **Stale architecture snapshot.** The producer's static architecture row had changed to include `datetime` and a `requests` external-I/O symbol, but the canonical architecture snapshot and its companions had not been regenerated.
2. **Conditional artifact made mandatory.** The new live-row loader raised a missing-artifact failure in temporary test roots that correctly lacked the one-time conditional live proof.
3. **Isolated retained-proof rewrite.** Explicit produced-time equality caused isolated release-attestation builds to rewrite unchanged retained path proofs outside the isolated generated-evidence graph.

PR #371 was merged as `870e0db41f78a7ab49a87dc56bcefd1859d53c06` despite those failures. This addendum classifies that sequence as a merge-sequencing defect. A future CI-clean completion claim must keep behavioral PASS, routing, merge, and hosted-CI state as separately evidenced predicates.

### 9. PR #372 — CI integration closure

PR #372's validation made no vendor call, required no vendor credential, and ran under closed rails.

PR #372 did not regenerate or alter the governed live proof, rerun `qa-08-po-008` finalization, renew either receipt, or make a second live call. It repaired only the surrounding closed-rails integration defects.

#### 9.1 Conditional live-artifact semantics

Path: `tools/evidence/update_evidence_index.py`

Change:

* when the conditional live proof is absent, omit its index row;
* when the proof is present, continue validating timestamp, kind, PASS posture, and non-token posture and fail closed if malformed.

Why required:

The live artifact exists only after a separately authorized event. A temporary test root that correctly omits the artifact must not acquire a dangling row or fail merely because no live event occurred. Conditional absence is valid; malformed presence is not.

Regression:

* `tests/ops/test_evidence_index.py` now proves omission when the conditional artifact is absent.

#### 9.2 Isolated retained-provenance semantics

Path: `tools/evidence/update_evidence_index.py`

Change:

* ordinary source-tree refresh still corrects an explicit produced-time mismatch;
* isolated release builds preserve unchanged retained path-proof bytes and capture-time provenance.

Why required:

The first correction was valid for current source-tree companion repair but too broad for isolated attestation. Isolated builds must not retimestamp unchanged retained evidence or write outside their declared generated graph.

Regression:

* `tests/evidence/test_evidence_skeleton.py` now proves an isolated build preserves unchanged retained proof bytes.

#### 9.3 Architecture snapshot and canonical fixed point

Paths:

* `artifacts/architecture/architecture_snapshot.keys_only.json`
* `artifacts/architecture/architecture_snapshot.keys_only.json.path_proof.txt`
* `artifacts/evidence_index.jsonl`
* `artifacts/evidence_index.jsonl.path_proof.txt`
* `artifacts/evidence_index.jsonl.sha256`
* `artifacts/evidence_index.jsonl.sha256.path_proof.txt`

Changes:

* regenerated the architecture snapshot through its canonical owner so the producer row reflected the current imports and static external-I/O classification;
* refreshed the snapshot path proof;
* refreshed the Machine Mirror architecture row, self-record, hash, and path proofs; and
* completed the canonical fixed point in `86a260af3bf7e6ebcb58eeabf1b1b89e21d17764`.

Why required:

Hosted architecture and evidence-coherence gates compare current analyzed source to current canonical bytes. A source change without its owned snapshot is incomplete, even when the changed code is correct. The mirror's self-reference requires a final fixed-point refresh after dependent bytes change.

### 10. Validation and final hosted-CI completion

The PR #372 remediation record reports these local checks:

* focused updater regressions: 8 passed;
* faithful local evidence shard: 1,097 passed in 188.50 seconds; and
* external clean-source release-attestation build and exact verification: passed.

Hosted workflows established:

* canonical JSON, evidence-index, mirror, hash, path, LF, release-identity, test, and sanity stages passed;
* PR #372 push workflow `30317077189`: all seven jobs passed;
* PR #372 pull-request workflow `30317079532`: all seven jobs passed;
* PR #372 merge: `b08d9dc47f31baa79101a323795237fde4e25b53`; and
* post-merge `main` workflow `30317268158`: all seven jobs passed, including the exact evidence/OPS shard with 1,097 passed in 137.80 seconds.

The final clean-CI integrated source is therefore `b08d9dc47f31baa79101a323795237fde4e25b53`, not the earlier qa-08 PASS commit or PR #371 merge. Clean CI does not retroactively alter, broaden, or create a second instance of the `2026-07-27T23:51:41Z` qa-08 PASS.

### 11. Complete net changed-path inventory

The combined base-to-final range changed 19 paths, with 671 insertions and 131 deletions:

| Path | Change class | Purpose |
| --- | --- | --- |
| `tools/evidence/generate_open_rails_abba_proof.py` | Code | Live authority, rails, target, input, request, timestamp, safety, and check-mode enforcement |
| `tools/evidence/update_evidence_index.py` | Code | Current provenance, conditional artifact semantics, ordinary versus isolated proof preservation |
| `tests/evidence/test_open_rails_abba_proof.py` | Tests | Producer safety and proof-validation regressions |
| `tests/evidence/test_evidence_skeleton.py` | Tests | Explicit provenance correction and isolated preservation regressions |
| `tests/ops/test_evidence_index.py` | Tests | Current live-row provenance, malformed-present refusal, conditional-absence behavior |
| `docs/qa/r7-qa-plan-hde-epic038.md` | QA plan/runbook | HEAD-independent execution, bootstrap repair, sole-endpoint truth, event authority, closed finalization |
| `audit/qa/hde-epic038/checks/qa-08-po-008/primary.log` | QA evidence | Final closed-rails PASS receipt |
| `audit/gates/determinism/open_rails_vendor_abba.json` | Governed proof | Current bounded live AB/BA event |
| `audit/gates/determinism/open_rails_vendor_abba.json.path_proof.txt` | Governed companion | Current proof hash, size, and provenance |
| `docs/evidence/INDEX.json` | Governed Human Index | Current live-proof row |
| `docs/evidence/INDEX.json.path_proof.txt` | Governed companion | Human Index byte binding |
| `docs/evidence/INDEX.sha256` | Governed sentinel | Human Index hash |
| `docs/evidence/INDEX.sha256.path_proof.txt` | Governed companion | Sentinel byte binding |
| `artifacts/evidence_index.jsonl` | Governed Machine Mirror | Current proof and architecture rows plus mirror self-record |
| `artifacts/evidence_index.jsonl.path_proof.txt` | Governed companion | Machine Mirror byte binding |
| `artifacts/evidence_index.jsonl.sha256` | Governed sentinel | Machine Mirror hash |
| `artifacts/evidence_index.jsonl.sha256.path_proof.txt` | Governed companion | Mirror sentinel byte binding |
| `artifacts/architecture/architecture_snapshot.keys_only.json` | Governed architecture evidence | Current producer static analysis |
| `artifacts/architecture/architecture_snapshot.keys_only.json.path_proof.txt` | Governed companion | Architecture snapshot byte binding |

### 12. Root-cause assessment

The event did not have one isolated cause. It exposed a coupled proof-chain problem:

1. **Planning rigidity:** fixed-source equality and syntax-corrupted bootstrap content confused provenance with execution validity.
2. **Environment-model drift:** a local `APP_ENV` value and URL-substring markers were treated as proxies for the nature of an external vendor API base/environment target.
3. **Authority-model drift:** a reusable confirmation string was treated as sufficient one-time authority.
4. **Rail-enforcement drift:** the producer could internally open rails rather than require them from the caller.
5. **Input-boundary drift:** personal-input environment variables and injected clients weakened the synthetic, same-input proof boundary.
6. **Provenance drift:** a current proof and index row could retain an historical timestamp.
7. **Conditionality drift:** a one-event artifact became mandatory in temporary test roots that correctly omitted it.
8. **Isolation drift:** a correct ordinary provenance repair changed retained bytes during isolated release construction.
9. **Evidence-graph drift:** source changed without the corresponding architecture snapshot and final mirror fixed point.
10. **Merge-sequencing drift:** PR #371 was merged while required hosted checks were red, even though behavioral PASS, merge state, and CI state remained separately recorded.

Repeated replanning would have documented successive partial understandings without proving the integrated correction. The PO-approved Extended Moon Loop was necessary because each downstream gate revealed the next causal defect, while the original qa-08 proof objective and nonclaims remained unchanged.

### 13. Prevention requirements

Future live-proof and QA work must apply the following:

1. Never make QA execution contingent on a preplanned commit hash.
2. Validate bootstrap functions and path commands in the actual execution shell before relying on them.
3. Model vendor API base/environment-target authority by exact contract and explicit PO decision, not by substring heuristics.
4. Never infer that `APP_ENV=dev` makes an external target nonproduction.
5. Require network rails from the caller; a producer must not self-open them.
6. Bind one-time authority to an event-specific, unprinted receipt and refuse reuse before client creation.
7. Do not pass authorization receipts or unrelated ambient variables into vendor clients.
8. Refuse personal-input overrides when the approved proof requires built-in synthetic inputs.
9. Keep live check mode independent, read-only, credential-free, and network-free.
10. Derive current-event provenance from a validated current artifact.
11. Preserve conditional artifact semantics in clean and isolated roots.
12. Distinguish ordinary source-tree provenance repair from immutable isolated-build behavior.
13. Regenerate every canonically owned source-analysis and evidence companion affected by code change.
14. Treat canonical mirror self-reference as a fixed-point operation.
15. Keep QA behavioral PASS, routing, merge, and hosted-CI completion separate in evidence and claims.
16. Do not merge a remediation as clean when required hosted checks are red; if an exceptional merge occurs, record it and continue causal closure until the final merged source is green.

### 14. Nonclaims

This addendum and the recorded work do not establish:

* that the canonical HumanDesignAPI vendor API base/environment target is nonproduction;
* recurring vendor-call authority or any renewal of the completed event's authority;
* broad HumanDesignAPI v2 or vendor-version conformance;
* absence of transient processing by the vendor;
* production application behavior or production deployment;
* a public Reader, route, payload, or transport change;
* a service start, migration, database write, deployment, or OPS completion;
* acceptance-token satisfaction;
* any PF09 status movement; the proof merely retains an existing `Partial` mapping and does not move PF09 status;
* whole-plan PASS;
* any retroactive alteration or broadening of the time, scope, or meaning of the `2026-07-27T23:51:41Z` qa-08 PASS from later clean CI;
* another live interaction or authority renewal from PR #372 or any CI run;
* epic acceptance or closeout; or
* permanent-canon drainage merely because this candidate exists.

### 15. Supersession and drain targets

If published, this addendum establishes the reusable Extended Moon Loop process definition, but it creates no standing authority to take action. It supersedes only the requirement to stop and issue a separate remediation plan after a fresh, pre-action PO approval has expressly authorized an Extended Moon Loop event. It does not supersede the ordinary Moon Loop classification boundary, the distinction between QA-root correction and routed remediation, or evidence ownership, safety, secret handling, PASS criteria, and nonclaim rules. In the absence of fresh event-specific approval, the ordinary Moon Loop stop rule remains controlling.

No other epic, QA check, agent, or later run may rely on the `qa-08-po-008` approval as authority to edit source during Live QA, make a live call, publish or merge a PR, or continue remediation. Every later use requires fresh explicit authority recorded before the corresponding write, external call, publication, or merge.

HDE Build Notes, Addenda 2.24, 2.25, 2.26, 2.27, 2.28, 2.29, and 2.30 remain applicable to their distinct syntax, remediation-plan, implementation-remediation, bounded-rescope, review, QA, and scope-model topics.

If published into the active HDE-EPIC038 HDE Build Notes sequence, this addendum would be the higher-numbered same-topic authority only for the Extended Moon Loop process definition and the bounded `qa-08-po-008` / PR #371 / PR #372 execution, remediation, routing, and CI-cleanup history described here. As a candidate outside the active set, it is not current authority.

Proposed permanent-canon drain targets:

* Glow QA Guide, §3.4.8, “Rails posture for manual Live QA” — add the Extended Moon Loop class, invocation conditions, causal-closure rule, receipt lineage, and completion/expiry model.
* Canon Epic Process Guide, §1.1.11, “Plan review rules (content-first; blockers vs caveats)” — distinguish ordinary QA-root Moon Loop from PO-approved routed Extended Moon Loop remediation.
* Canon Epic Process Guide, §3.5.5, “Remediation PR pattern (separate from Live QA)” — permit one recorded causal lineage to span follow-up PR and CI cycles without requiring repeated remediation-plan issuance when scope and proof identity remain stable.
* Canon Plan Templates — prohibit fixed-HEAD QA gates, require source identity as provenance only, and provide an Extended Moon Loop decision-record field.

### 16. Source basis

This addendum is grounded in:

* HDE Build Notes, Addendum 2.3, “PR-03 HDE-EPIC038” — bounded live proof, same-input, independent validation, raw-payload prohibition, and non-recurring authority;
* HDE Build Notes, Addendum 2.15, “HDE-EPIC038 Post-PR359 Remediation — ADR-CANON-008 Direct-Only PF09.6 Completion Semantics and PR-06R Ownership” — canonical evidence-index ownership and finalization order;
* HDE Build Notes, Addendum 2.24, “Syntax-Origin Defects Remain Non-Blocking Regardless of Literal Execution Effect” — execution-time syntax normalization boundaries;
* HDE Build Notes, Addendum 2.25, “Recognize Epic Remediation Plans Pending Template Drainage” — remediation recognition and nonclaims;
* HDE Build Notes, Addendum 2.26, “HDE-EPIC038 Epic Remediation PR-01 — PF09.6 HDE-DIST007 Canonical Adapter Factory Route-Mount Parity” — implementation-remediation posture;
* HDE Build Notes, Addendum 2.27, “HDE-EPIC038 HDE-DIST007 Post-Merge Bounded Rescope and CI Completion Authority” — bounded rescope and CI completion authority;
* HDE Build Notes, Addendum 2.28, “Epic Remedial PR-01 HDE-EPIC038” — completed-remediation review structure;
* HDE Build Notes, Addendum 2.29, “QA Pass 1 HDE-EPIC038” — QA deviation accounting and preserved receipts;
* HDE Build Notes, Addendum 2.30, “PF10 Scope Model: Independently Scoped Addenda and Lettered Multi-Document Version Sets” — addendum-level scope and supersession;
* Glow QA Guide, §3.4.8, “Rails posture for manual Live QA” — ordinary Live QA Moon Loop and non-QA-root routing boundary;
* Canon Epic Process Guide, §1.1.11, “Plan review rules (content-first; blockers vs caveats),” and §3.5.5, “Remediation PR pattern (separate from Live QA)” — ordinary Moon Loop and routed-remediation boundaries;
* the approved HDE-EPIC038 Live QA Plan and its PO-approved in-place execution correction;
* the governed proof and `qa-08-po-008` primary log;
* PR #371 and PR #372 commit, routing, merge, and hosted-CI records; and
* the successful final `main` workflow on `b08d9dc47f31baa79101a323795237fde4e25b53`.
