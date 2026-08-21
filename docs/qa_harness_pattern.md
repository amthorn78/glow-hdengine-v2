# QA harness pattern (non-canonical summary)

This is a repository-facing summary of the current generic harness in `tools/qa/qa_harness.py`. It does not itself create QA results, Live QA, acceptance, or closeout.

## Stable identity

Create `HarnessConfig("HDE-EPIC<NNN>")` with the stable epic identity and optional lowercase `step_names`. The harness derives `audit/qa/hde-epic<NNN>/`, `docs/acceptance_map_epic<NNN>.json`, the token matrix, and the viability ledger from that identity. Each `check_id` must be a lowercase ASCII-safe path segment.

Run IDs are not current-state correctness identity. Older run-ID-era wrappers and captures remain historical; new generic-harness work binds results to the stable epic and check IDs.

## Governed statuses

The status set is exactly:

- `PASS` — the exact executed command or approved proof action succeeded and the required current-state validation completed.
- `FAIL_BEHAVIOR` — an available evaluation completed and contradicted the required behavior.
- `FAIL_TOOLING` — the evaluation mechanism, parsing, collection, or evidence writer malfunctioned.
- `TOOLING_BLOCKED` — a required prerequisite, input, script, test, or selector is unavailable, empty, missing, or cannot be evaluated.
- `PARKED` — the check is explicitly parked rather than evaluated as successful.

Absent, empty, placeholder, stale, or unevaluated inputs never become `PASS`. A harness result is not a Live QA result unless separately authorized Live QA was actually performed.

## Pytest and viability mechanics

`run_pytest_check` uses the same interpreter for readiness and execution through `sys.executable -m pytest`. Reference viability resolves exact repository paths and test selectors, rejects placeholders and unsupported shell composition, performs same-interpreter collection, verifies current input stability, and fails closed when acceptance-map and token-matrix coverage or status disagree.

A viability `PASS` requires an exact command or approved proof action. Publication and manifest verification occur only after evaluation; writer failure is `FAIL_TOOLING`, and close-pack consumers must refuse any non-`PASS` or stale/mismatched viability ledger.

## Current client pattern

`tools/qa/epic021_qa.py` is a current client of the generic harness. An epic wrapper supplies stable configuration and check definitions; it must not reintroduce run-ID correctness, collapse causal status classes, synthesize a phantom PASS, or treat repository evidence as proof that Live QA ran.
