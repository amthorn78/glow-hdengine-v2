# HDE-EPIC039 QA RCA and Doc Delta Summary

## Live QA findings and RCA

No new product-behavior delta was found. A QA planning/execution-surface defect was found and remediated under the authorized Moon Loop revision.

The existing proof-bearing doc-delta pair was preserved; Live QA did not overwrite either surface.

## Moon Loop revision and planning defect

- Authority: Product Owner direct instruction on 2026-08-22.
- Authorization (verbatim): “We aren't doing that. I need you to fix the script as a moon loop revision, and mention the planning defect in your report so it can fix future process”.
- Extended authorization (verbatim): “do an extended moon loop if needed”.
- Revision: moon-loop-2-extended.
- Initial attempt: the exact r4 direct-path command failed before helper main() with `ModuleNotFoundError: No module named 'tools'`; no governed receipt was created.
- Operator-observed first `po-001` attempt: pytest collection failed before any product assertion with `ModuleNotFoundError: No module named 'flask'`, exposing the omitted runtime-requirements readiness check; the Moon Loop replaced that current-state receipt after correcting readiness, so the prior receipt is not independently retained.
- Operator-observed first `po-003` attempt: 116 assertions passed and one legacy composer assertion expected `harmony.cool.shared...` while the current governed grammar, catalog, router, and sibling tests require `nar.harmony.cool.shared...`; the test also mounted an untracked repo-root cache because it lacked temporary-path isolation. The Moon Loop replaced that current-state receipt, so the prior receipt is not independently retained.
- First all-PASS finalizer attempt: every check receipt was PASS, but the Moon Loop finalizer incorrectly treated mutable Codespaces branch metadata as event-wide identity and returned NOT READY. The correction preserves strict within-operation config stability while allowing venue metadata to change between operations.
- Extended corrective scope: repository-root import bootstrap; an in-memory waiver for only exact Codespaces `branch.main.github-pr-owner-number` metadata; complete runtime/development readiness; and test-only correction of the stale composer key expectation plus temporary-pack isolation.
- Source protection: no product runtime source, governed source, `.git/config`, selector path, rails variable, or evidence path was changed. The only tracked Moon Loop change was the selected narrative-composer test.
- Dependency-network note: pip package-index access occurred during runtime and development synchronization before QA behavior checks; this setup I/O is not product or Live QA evidence.
- Planning defect: The approved r4 plan validated the embedded runner only by payload SHA-256 and compile() syntax; it did not smoke-test the exact direct-path command it required for execution. The pinned runner therefore lacked repository-root import bootstrapping. The same plan prohibited the requirements-dev.txt synchronization mandated before pytest by AGENTS.md, so its subsequent pytest version checks did not satisfy the required install-then-readiness sequence. It also assumed the close-pack Git reader could consume Codespaces-added, quoted hash-bearing branch metadata even though that reader rejects such non-core Git-config values. It also treated pytest and jsonschema as the complete dependency boundary even though the selected canonical-gate test imports Flask from requirements.txt, which requirements-dev.txt does not include. Finally, the approved PO-003 selector retained a legacy pre-directional-corpus key assertion and lacked the temporary-pack isolation already used by sibling narrative tests, allowing repo-root cache residue. These were QA planning, test-maintenance, and execution-surface defects, not product-runtime regressions.
- Future process correction: Before approval, execute the exact generated helper command in the named venue, reconcile plan dependency policy with repository instructions, and validate every venue-created Git configuration form consumed by repository-native readers; synchronize both runtime and development requirements and smoke-collect the complete approved selector import closure before publishing the first governed QA receipt; reconcile selected test expectations with current governed key grammars and require temporary-path isolation for tests that mount content-addressed runtime data; validate ephemeral venue metadata for stability within each proof operation rather than treating it as event-wide source identity.
- Original helper SHA-256: `7cc185a4b31f56232a69743f2c7203088628b951e704abb93a9f643a8541849e`.
- Revised helper SHA-256: `fbd5bbd15683ae9634174a425c65efff838186d9c81440450ad70c6f72a16522`.
- Corrected selected-test SHA-256: `8378089bc5cfefce1b9d0239f429cce7a2660dea6e09ebf7e6060315c70d9a67` (`tests/unit/test_narratives_composer.py`).

## PF-Canon doc-delta intents

- PF14 - HDE Mechanics Guide: later PO-owned drainage for orientation and evidence-index publication ownership identified by current PF10.
- PF04 - HDE Governance: later PO-owned drainage for Machine Mirror self-reference semantics identified by current PF10.
- PF09.1 - HDE Build Checklist - Calcination: status drainage remains a separate Product Owner closeout action; this QA run makes no PF09 status change.
- Documentation drainage is not a blocker for step verdicts or this recommendation when required QA evidence is complete and trustworthy.

## Deferrals and nonclaims

- No open-rails product, vendor, deployment, production, public Reader, database, or service behavior was exercised. Moon Loop dependency setup performed the package-index activity recorded above.
- No real HDE-EPIC039 closeout candidate, operational validation, acceptance, closure, deployment, or checklist status change is claimed.
- Acceptance tokens were neither intended nor claimed.
- Codespaces venue is NOT CLAIMED as a proof axis.

## Coverage vs QA Plan

| check_id | check name | coverage status | execution status | evidence |
| --- | --- | --- | --- | --- |
| step-0b-doc-delta-capture | Step-0B Doc Delta Capture | COVERED | PASS | audit/qa/hde-epic039/checks/step-0b-doc-delta-capture/primary.log |
| po-001 | Deterministic governed structured-data outputs | COVERED | PASS | audit/qa/hde-epic039/checks/po-001/primary.log |
| po-002 | Declared unordered-collection semantics | COVERED | PASS | audit/qa/hde-epic039/checks/po-002/primary.log |
| po-003 | Governed Human Design corpus invariants | COVERED | PASS | audit/qa/hde-epic039/checks/po-003/primary.log |
| po-004 | Coherent evidence publication | COVERED | PASS | audit/qa/hde-epic039/checks/po-004/primary.log |
| po-005 | Human and machine evidence agreement | COVERED | PASS | audit/qa/hde-epic039/checks/po-005/primary.log |
| po-006 | Causal QA outcome classification | COVERED | PASS | audit/qa/hde-epic039/checks/po-006/primary.log |
| po-007 | Semantic declaration propagation | COVERED | PASS | audit/qa/hde-epic039/checks/po-007/primary.log |
| po-008 | Current and historical evidence identity | COVERED | PASS | audit/qa/hde-epic039/checks/po-008/primary.log |
| po-009 | Change-aware exact-candidate automation | COVERED | PASS | audit/qa/hde-epic039/checks/po-009/primary.log |
| po-010 | Retired automation remains inactive | COVERED | PASS | audit/qa/hde-epic039/checks/po-010/primary.log |
| po-011 | Feedback-free closeout derivation | COVERED | PASS | audit/qa/hde-epic039/checks/po-011/primary.log |
| po-012 | Manifest-committed candidate publication | COVERED | PASS | audit/qa/hde-epic039/checks/po-012/primary.log |
| po-013 | Reusable capability scope boundary | COVERED | PASS | audit/qa/hde-epic039/checks/po-013/primary.log |

## Dependency and Moon Loop posture

Product Owner-authorized Moon Loop work was recorded. Runtime synchronization was `python -m pip install -r requirements.txt` (exit 0), development synchronization was `python -m pip install -r requirements-dev.txt` (exit 0), pytest readiness was `python -m pytest --version` (exit 0), the jsonschema probe exited 0, and the runtime-import probe exited 0.

## Open issues and deferred work

No unresolved QA-ladder behavior issue. The planning-process correction above remains follow-up work and is not a product-behavior blocker.

Undrained documentation deltas remain PO-owned follow-up and are not converted into QA blockers.

## Completion-state separation

- Repo-supported completion: SUPPORTED BY THIS QA EVENT STREAM
- Canon-drain completion: NOT CLAIMED
- Formal close-pack completion: NOT CLAIMED

## Readiness / closeout recommendation

READY FOR PRODUCT OWNER QA CLOSEOUT REVIEW

Evidence pointers: audit/qa/hde-epic039/qa_step_logs_manifest.json; audit/qa/hde-epic039/qa_step_logs_manifest.json.path_proof.txt; audit/qa/hde-epic039/00_meta/discovery.json; audit/docdeltas/hde-epic039_doc_deltas.md; audit/qa/hde-epic039/00_meta/doc_deltas.md.
