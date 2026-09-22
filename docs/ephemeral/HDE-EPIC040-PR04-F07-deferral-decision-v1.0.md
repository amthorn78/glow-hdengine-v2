# HDE-EPIC040-PR04-F07 — Dev conjunction evidence capture unrunnable: Product Owner deferral decision v1.0

```yaml
artifact_type: PRODUCT_OWNER_DEFERRAL_DECISION
DECISION_ID: HDE-EPIC040-PR04-F07-DEFERRAL
version: v1.0
state: DECIDED
repository_path: docs/ephemeral/HDE-EPIC040-PR04-F07-deferral-decision-v1.0.md
change_class: EPIC
change_id: HDE-EPIC040
work_unit_id: HDE-EPIC040-PR04
finding_ref: HDE-EPIC040-PR04-F07
finding_title: The dev conjunction writer evidence capture can no longer run, so tests/evidence/test_dev_conjunction_identity.py fails
raised_by: base-vs-head sweep of the uncovered test set (this session), and independently by Codex code review on head 6f5aeed68a60551013f23ba49fa7909225d90cc3 (P2, adapter/http_reader.py:820)
verified_by: dedicated PR04 PR-development session, PR-35 phase, by execution against the dev writer route under its own open-dev rails
decision: DEFER — PR04 merges as implemented; the two failing tests are an accepted, owned deviation
decided_by: Nathan / Product Owner, 2026-09-22 ("defer F07 to PR07")
return_point: PR07
rescope_raised: NO — no RESCOPE_REQUEST was issued; PR_RETURN_PHASE remains PR-35
```

## 1. Decision

The Product Owner chose to **defer**. PR04 keeps the dev conjunction route as implemented — no fabricated local person store, no `dev_compat_identity()` stamp, real release admission — and
`tools/evidence/generate_conjunction_writer_evidence.py` together with its two owning tests remains unrunnable until a release is admitted. This is recorded as an accepted deviation with a named
owner, not a rescope. No corrective push was made for this finding.

## 2. The finding, as verified

`tests/evidence/test_dev_conjunction_identity.py` fails on two of its three tests:

- `test_dev_conjunction_identity_evidence_is_current_and_nonwriting`
- `test_check_mode_neutralizes_database_url_and_preserves_artifacts`

Both fail inside the generator's `_capture_outputs()`, which refuses unless the writer, the two-run writer and the reader all return 200. Measured directly under the tests' own open-dev rails
(`SAFE_MODE=0 ALLOW_NETWORK=1 APP_ENV=dev`), `GET /dev/writer/conjunction`:

| configuration | status | code |
| --- | --- | --- |
| as implemented (`local_lookup=None`) | 503 | `ERR_WRITER_RAILS_CLOSED` / `PROVIDER_CONFIG_MISSING`, `missing: ["HD_API_KEY"]` |
| + deterministic mapped-row seam | 503 | `ERR_M10_MANIFEST_MISMATCH` |
| + synthetic complete release injected | **200** | — |

The three rows are the whole finding. Row one is the vendor dependency Codex identified. Row two shows a resolver seam removes that dependency but does not make the capture runnable, because the
route then goes through real release admission and refuses under the F01 posture. Row three shows a 200 is reachable only with an admitted release.

## 3. Why it is this PR's doing

At the approved base the route sidestepped admission entirely: `git show 3b8084d0:adapter/http_reader.py` carries `compat_identity = dev_compat_identity()` at line 675, alongside a local person
store fabricated under open rails. This PR removed both — correctly, since a dev route stamping a dev identity is an admission bypass on a surface that reaches the compat core. The evidence
generator was built on that bypass and is collateral.

The sweep recorded in the result record §8.8 found these two among four regressions in the 132 test files that no CI lane and no changed-test target covers. The other two were fixed in `1e02823`.
Codex independently raised this one.

## 4. Consequence accepted by this decision

1. `tools/evidence/generate_conjunction_writer_evidence.py` cannot produce or re-check its capture. The frozen `artifacts/writer/conjunction_write_readback.log` and
   `artifacts/writer/conjunction_writer_summary.json` remain capture-time records that no current run can reproduce or refute.
2. Two tests fail at the candidate head. They are invisible to CI — the file is in neither a lane nor the changed-test targets — so CI is green with a known-failing test in the tree. This is stated
   plainly rather than relied on: the failure is real, it is simply not gating.

Both are accepted under the current posture, where no release is admitted and every gate ends `RELEASE_NOT_ADMITTED`.

## 5. Why no in-scope fix was attempted

The seam in row two of the table above **was implemented and then reverted**: a dev-only `current_app.config["DEV_CONJUNCTION_LOCAL_LOOKUP"]`, absent by default so the route still fabricates
nothing, with the generator supplying deterministic mapped rows for its own two identities. It was reverted because it does not make the tests pass, and because registering the changed generator
with the CI classifier would have promoted the failing test into the changed-test targets — turning an invisible failure into a red lane with no fix available.

Reaching row three inside PR04 would mean fabricating an admitted release inside a governed evidence generator. That is an admission bypass, which this work unit's constraints forbid, and it would
re-introduce in the generator exactly what the PR removed from the route.

There is also a contract question that is not this phase's to settle. The test asserts

```python
assert summary["checks"]["writer_dev_identity"] is True
assert dev_compat_identity() == {"engine_tag": "dev", "release_id": "dev", "invocation_tag": "INV-DEV"}
```

— the dev identity stamp the PR removed. So "make the capture valid again" requires deciding what identity the dev conjunction route should carry now, which is a contract decision of the same kind
as F03 and F05.

## 6. What PR07 inherits

1. Decide the dev conjunction route's identity now that it no longer stamps a dev one, and update the generator's assertions to match.
2. Land the resolver seam (or an equivalent) so the capture does not depend on live vendor credentials. The reverted shape is described in §5 and in the reply on the Codex thread.
3. Register the generator with `_EVIDENCE_GENERATOR_TEST_OWNERS` in `ci/checks/classify_ci_changes.py` so `tests/evidence/test_dev_conjunction_identity.py` becomes a changed-test target and this
   class of failure stops being invisible.
4. Regenerate the frozen writer artifacts through their owner once a release is admitted.

Gated on **PR06** for admission: until the roster is admitted, item 4 cannot run and items 1–3 cannot be proven by execution.

Settle alongside **F03** (O-14) and **F05** (O-15) — all three are deferred findings on surfaces this PR moved onto the admitted magic10 core.

## 7. Status of this finding on the PR

The Codex thread at `adapter/http_reader.py:820` (comment 4075000425) is left **open**, with the measurements above and the reverted seam recorded on it. Observation **O-19** in
`docs/ephemeral/HDE-EPIC040-PR04-pr-implementation-result-v1.0.md` §10 carries it; the sweep that found it is §8.8.
