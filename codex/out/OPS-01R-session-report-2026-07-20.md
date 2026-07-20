# OPS-01R Session Execution Report

Date: 2026-07-20 UTC  
Scope: HDE-EPIC038 / Distillation Pass 3 / OPS-01R  
Classification: temporary, non-governed operator report  
PF09 items: `HDE-DIST001`, `HDE-DIST001.4`, `HDE-DIST001.9`

## Executive summary

OPS-01R did not produce a v5 candidate and did not establish direct/bridge parity.

The governed production discovery stopped because its target-identity contract required both `DATABASE_URL` and `DB_BRIDGE_URL` to be injected by the Railway production service. The Product Owner subsequently clarified that production intentionally has `DATABASE_URL` and intentionally does not have `DB_BRIDGE_URL`. PF07's production inventory is consistent with that clarification.

A separate, explicitly non-governed parity diagnostic was then run in GitHub Codespaces, where both settings are present. Both the direct database and bridge paths completed their transports and the code reached the final posture/parity comparison. That comparison raised `OPS01R_LIVE_PARITY_MISMATCH`. The runner combines many predicates behind that one error and preserves no predicate-level failure record, so the session cannot determine which database posture value or direct/bridge comparison failed without performing additional live reads.

No database write, schema change, deployment change, tracked-file write, raw secret persistence, raw BodyGraph persistence, QA claim, PF09 status movement, or epic closeout occurred.

## Result

| Item | Result |
|---|---|
| Detached-source preflight | PASS |
| Railway project/environment/service discovery | Target found |
| Railway endpoint-presence gate | FAIL: production intentionally lacks `DB_BRIDGE_URL` |
| Codespaces direct connectivity | Reached observation/comparison phase |
| Codespaces bridge connectivity | Reached observation/comparison phase |
| Codespaces posture/parity predicate | FAIL: `OPS01R_LIVE_PARITY_MISMATCH` |
| Governed live authorization | Not created |
| Live-authority marker | Not created |
| Temporary v5 candidate | Not created |
| QA execution or claim | None |
| PF09 status movement | None; affected items remain `Partial` |
| Repository writes from the parity attempt | None |

## Source and environment identity

- Repository: `amthorn78/glow-hdengine-v2`
- Original PR-A source identified during validation: `ffe67e3d2c2831cb42c12dc583340ddde77d0980`
- Railway integration correction: `cd4a696121e0e66749dcc18b5654ada667066ff5`
- Discovery diagnostic correction and final preflight source: `b3cf346cc6e84147056f0e4e739b8b2d6917db4f`
- Current worktree: `main` at `b3cf346cc6e84147056f0e4e739b8b2d6917db4f`, clean, one commit ahead of `origin/main`
- Final governed staging run ID: `e0b12b4ee37a44a7b798f7cd6c8abccc`
- Final detached source root: `/tmp/hde-epic038-ops01r/e0b12b4ee37a44a7b798f7cd6c8abccc/source`
- Preflight identity: `095b9ab9b2072f4d406048476c900e31c22335a73204686ab219f733130d9de8`
- Source manifest identity: `f6ac3744b5c99ff85c41bd4a79727513593e4d045165866346dacb5739927234`
- Final approved discovery contract self-hash: `27713f571360645b240bb1df940b9e0d769c79e7a4f8bdc443e0a2aded97f8da`
- Railway CLI version bound by the authorization: `5.26.2`
- Required rails: `LC_ALL=C`, `LANG=C`, `TZ=UTC`, `SAFE_MODE=1`, `ALLOW_NETWORK=0`, `ALLOW_DB_WRITE=0`, `APP_ENV=dev`

The original OPS description named immutable PR-A commit `ffe67e3d...`, but the final preflight and discovery authorization used corrective commit `b3cf346c...`. The resulting work therefore cannot honestly be described as a recapture from the original immutable PR-A bytes without relying on the later PF10 authorization/update.

## What was done

1. PF07 and PF29 were inspected for target and environment facts. PF07 supplied project `ample-illumination`, environment `production`, service `glow-hdengine-v2`, database `ample-illumination/production/postgres`, schema `hde`, and the documented bridge endpoint. PF29 did not define Railway database/bridge injection; its relevant configuration guidance is vendor-focused.
2. The repository runner, validator, and DDL identity projector were inspected. The runner exposes preflight, target probe, discovery, live launch, and live child modes. The validator validates supplied contracts and captures but does not construct operator authorizations.
3. Corrective repository commits were used to address Railway CLI integration and improve bounded discovery diagnostics.
4. A clean detached source tree was materialized under the final staging root. Preflight passed and verified the detached state, component identities, source manifest, exact Python `-I -B` posture, and temporary-only write set.
5. The Product Owner approved the final discovery authorization bytes and self-hash `27713f...`.
6. The six read-only Railway discovery subprocesses were dispatched. Project, environment, and service identity resolved, and the target probe returned presence-only endpoint information. Contract derivation rejected the probe with `OPS01R_DISCOVERY_TARGET_AMBIGUOUS:target_identity_probe:endpoint_presence` because both endpoints were not present on the Railway service.
7. The Product Owner clarified that production is direct-only: `DATABASE_URL` is set and `DB_BRIDGE_URL` is intentionally unset. No secret value was requested or captured.
8. The Codespaces shell was checked by variable name only and confirmed both `DATABASE_URL` and `DB_BRIDGE_URL` were present.
9. An isolated local invocation first stopped during module setup because the import harness had not registered the dynamically loaded module. It performed no provider or database operation.
10. A second isolated invocation stopped before provider construction because `/usr/local/bin/python` did not contain `psycopg`. This exposed a preflight readiness gap: the exact preflight interpreter could pass without proving the live runtime dependency was importable.
11. The repository virtual-environment interpreter was verified to contain `psycopg 3.2.13`.
12. The bounded live observation routine was invoked locally under the required rails using the Codespaces endpoints. Its SQL guard permitted only `SELECT` and `SHOW`. Direct and bridge operations returned far enough to reach the final combined comparison, which failed with `OPS01R_LIVE_PARITY_MISMATCH`.
13. Repository status and temporary outputs were checked after the diagnostic. No tracked or untracked repository file was created by it. Its temporary candidate directory remained empty.

## Findings

### Confirmed

- The Railway project, environment, and service identity are discoverable without reading secret values.
- Production's lack of `DB_BRIDGE_URL` is intentional, not a missing credential or production defect.
- The Codespaces context has both endpoint settings by presence.
- The Codespaces direct and bridge paths were sufficiently reachable for all observation functions to return and for the final comparison block to execute.
- At least one strict expected-posture predicate or direct/bridge comparison did not match.
- No governed candidate or useful failure artifact was created.
- Secret and raw BodyGraph persistence controls held.
- The repository remained unchanged by the discovery and parity executions.

### Not determined

The runner's single failure code does not distinguish among these conditions:

- direct grants differed from the hard-coded grant roster;
- bridge grants differed from the hard-coded grant roster;
- default privileges differed from `[(none)]`;
- direct search path differed from `hde, public`;
- direct and bridge search paths differed;
- `SELECT 1` differed or failed parity;
- the bounded DDL identity projections differed;
- the selected BodyGraph user ID differed;
- the direct and bridge canonical BodyGraph rows differed;
- the expected partition roster differed;
- the expected read-only boundary-view posture differed.

Because these predicates are evaluated in one compound condition and no redacted predicate matrix is written on failure, the exact cause cannot be reconstructed from this attempt.

## Process assessment

The process was effective at enforcing negative guarantees: no tracked writes, no database writes, no raw credential capture, exact component hashes, detached-source checks, bounded subprocesses, and explicit one-attempt authority.

It was not effective at producing actionable operational information. The main defects are:

1. **The target model contradicts production reality.** Discovery requires both endpoint variables to originate from the Railway service even though production intentionally uses only the direct database setting.
2. **Discovery and execution contexts are inseparably coupled.** The Railway target-probe command prefix becomes the live-launch prefix. The contract cannot represent production identity discovery followed by parity execution in Codespaces.
3. **Endpoint provenance is hard-coded incorrectly for a split-context run.** Both endpoints are labeled `railway_service`; there is no valid representation for a Codespaces-provided bridge endpoint.
4. **Preflight does not prove live dependency readiness.** `/usr/local/bin/python` passed preflight but could not import the required `psycopg` package.
5. **Failure diagnostics are too coarse.** Eleven or more distinct posture/parity predicates collapse into `OPS01R_LIVE_PARITY_MISMATCH`.
6. **The one-attempt rule and failure-output design conflict.** One attempt is consumed, but a predicate failure produces no safe predicate-level record. The rule prevents a diagnostic retry while the implementation withholds the data needed to avoid one.
7. **The evidence contract is internally awkward.** The operation requires a useful audit result while forbidding tracked evidence integration, and the runner does not retain a complete temporary failure report.
8. **Authorization effort is disproportionate to useful output.** Multiple byte-exact approvals were required for read-only discovery, yet the successful safety checks did not help locate the actual database mismatch.
9. **Source identity drift complicates the claim.** The process began as a recapture from `ffe67e3d...` but ultimately preflighted and discovered with `b3cf346c...` after operational corrections.

Overall assessment: **safe but low-utility and non-diagnostic**. It should not be repeated unchanged.

## Recommended corrections before another launch

- Represent identity discovery and parity execution as separate, independently named contexts.
- Allow endpoint provenance to state `railway_service`, `codespaces_secret`, or another approved presence-only source accurately.
- Add a preflight import check for every live dependency using the exact live interpreter.
- Replace the compound parity condition with a redacted predicate matrix containing one status per check.
- Persist a canonical temporary failure summary whenever live execution begins, without secrets or raw user payloads.
- Make the failure summary sufficient to diagnose a one-attempt failure; otherwise define a separate diagnostic authority that does not claim candidate production.
- Reconcile the temporary-write boundary with the required audit-report destination before execution.
- Bind the authorized source commit explicitly after operational fixes and stop describing it as the original immutable PR-A source when the bytes differ.

## Final disposition

- OPS-01R status: **NO CANDIDATE / NOT VALIDATED**
- Direct/bridge parity claim: **NOT ESTABLISHED**
- Connectivity conclusion: **both Codespaces paths reached the comparison phase**
- Actionable mismatch identity: **not retained by the runner**
- QA status: **not run and not claimed**
- PF09 status: **no movement; `HDE-DIST001.4` and `HDE-DIST001.9` remain `Partial`**
- Recommended next action: **repair the procedure and failure capture before authorizing another live read attempt**

## Authority references

- PF07 — *PF07-Canon-Glow-Infrastructure*, §§2.2, 2.4, 2.6, 3.1
- PF09.6 — *PF09.6-Canon-HDE-Build-Checklist-Distillation*, §Task `HDE-DIST001`, §Subtasks `HDE-DIST001.4` and `HDE-DIST001.9`
- PF29 — *PF29-Canon-HDE-Users-Guide*, §§12.1, 13, 17
- PF10 — *HDE-Build Notes*, applicable OPS-01R authorization/update language

This report is a temporary operator narrative. It is not governed evidence, was not produced by an Evidence Index or close-pack generator, and must not be used as a QA PASS or PF09 status-change artifact.
