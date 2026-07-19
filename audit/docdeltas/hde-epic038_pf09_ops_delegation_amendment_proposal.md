# HDE-EPIC038 PF09.6 Ops Delegation Amendment Proposal

## Status and authority

This document is a non-canonical amendment proposal for human PF-Canon-owner review. It does not amend PF09.6, authorize an OPS execution, revise an implementation plan, move PF09 status, establish QA PASS, satisfy an acceptance token, or authorize edits to `docs/pfcanon/**` by an automated agent.

Proposed canon target: PF09.6 — PF09.6-Canon-HDE-Build-Checklist-Distillation, §Ops tasks (PO-only execution; evidence required).

Motivating bounded case: HDE-EPIC038 OPS-01R, affecting `HDE-DIST001.4` and `HDE-DIST001.9`, where the checked-in procedure is read-only, fail-closed, one-attempt, secret-safe, exact-source-bound, and independently validated, but the current actor rule prohibits an automated agent from invoking it even under explicit PO direction.

## Proposed section title

Replace:

`Ops tasks (PO-only execution; evidence required)`

With:

`Ops tasks (PO-accountable execution; bounded read-only delegation; evidence required)`

## Proposed replacement wording

An Ops task is work requiring privileged access or observation outside the repository, including service configuration, secrets or environment-variable handling, deploy/runtime settings, infrastructure-console actions, and privileged database operations.

The PO remains accountable for every Ops task. An Ops task MUST be executed by the PO as human operator unless all requirements for bounded read-only automated delegation below are satisfied. Automated execution MUST identify itself as automated and MUST NOT claim to be, impersonate, or substitute identity for the human PO.

The PO MAY delegate execution of a bounded read-only Ops task to an automated agent only when all of the following are true:

* The PO gives explicit, task-specific delegation in the active execution context and identifies the epic or task, repository, immutable source revision, provider, project, case-sensitive environment, service, and intended evidence boundary.
* The applicable PF-Canon, approved decision record, or checked-in governed procedure defines the exact runner and independent validator, permitted subprocess families, rails, call or attempt budget, write set, stop conditions, secret-handling rules, and evidence disposition. The agent MUST NOT invent a missing privileged command, target, mutation, retry, or authority.
* The operation is observational and read-only. `ALLOW_DB_WRITE=0` is mandatory for database access. SQL writes, DDL, grants, migrations, role or schema changes, deployment, restart, relink, selection change, provider-variable mutation, secret mutation, and external-state mutation are forbidden.
* The delegated procedure is fail-closed before its privileged boundary. Every required local preflight, immutable-source check, executable identity, canonical authorization, independent validation, and target-identity check MUST pass before the applicable subprocess or provider call.
* Secrets remain presence-only. The agent MUST NOT print, persist, summarize, transmit, or return credential values, endpoint-bearing secrets, raw private payloads, or authentication material. Evidence remains redacted, hashed, or presence-only as required by the owning contract.
* Any one-attempt or bounded-call authority remains exact. Marker creation, subprocess start, or indeterminate launch consumes authority when the owning contract says it does. Automated delegation creates no retry, recovery launch, fallback, or authority expansion.
* Where the owning procedure requires the PO to approve final canonical bytes and hashes, the human PO MUST approve those actual bytes and hashes after construction. General delegation does not approve unknown future authorization identities.
* The automated agent may write only paths explicitly allowed by the owning procedure. It may not integrate temporary evidence into tracked governed paths unless a separate implementation or integration authority explicitly permits that work and the canonical artifact owners produce all governed companions.
* Completion produces the required secret-free repository evidence under the canonical lowercase Ops evidence root. A temporary candidate is not Ops completion when a later governed integration step owns the retained artifact.

Automated execution remains prohibited when any of the following applies:

* the task changes external state, including production data, schema, roles, grants, variables, service selection, deployment, restart, relink, or infrastructure configuration;
* raw secret values or uncontrolled private payloads must be retrieved, viewed, copied, or persisted;
* the target, command, source revision, environment, write set, evidence destination, attempt budget, or stop condition is missing or ambiguous;
* execution is interactive, unbounded, retry-capable, destructive, or lacks an independent fail-closed validator where one is required;
* PF-Canon or a more specific governing contract explicitly retains human-only execution for the task.

For every Ops task:

* Success criteria and evidence to capture MUST be specified before execution.
* Completion MUST produce a repo-stored evidence artifact under a lowercase audit path such as `audit/ops/<epic-id>/`. If captured during QA execution, it MUST still be stored under the Ops evidence root and referenced from QA artifacts as dependency evidence, not as QA evidence.
* Ops tasks are not QA tasks. Ops evidence is not a substitute for QA evidence.
* Evidence MUST be secret-free. Sensitive settings and values MUST be presence-only, redacted, or hashed while still proving the intended state.
* Delegated execution does not itself establish QA PASS, acceptance-token satisfaction, PF09 status movement, deployment readiness, epic completion, or closeout.

## Intended HDE-EPIC038 effect if adopted

For OPS-01R only, this amendment would make an automated agent eligible to invoke the exact immutable PR-A runner and independent validator under the approved HDE-EPIC038 `RSC-004` contract, provided the PO separately approves the actual final discovery-authorization bytes/hash and later the actual final live-authorization bytes/hash.

It would not relax any HDE-EPIC038 constraint: exact commit `ffe67e3d2c2831cb42c12dc583340ddde77d0980`; exact `-I -B` Python execution; empty case-folded `PYTHON*` child environment; Railway target `ample-illumination` / `production` / `glow-hdengine-v2`; `SAFE_MODE=1`; `ALLOW_NETWORK=0`; `ALLOW_DB_WRITE=0`; `APP_ENV=dev`; one live launch; no retry; no DB, Railway, vendor, or bridge mutation; no raw secret or payload persistence; temporary candidate only; and no PR-C, QA, PF09 movement, PF-Canon edit, board work, or closeout.

This proposal would not make a general-purpose automated production-operations lane. Mutating operations and tasks without an exact fail-closed governed procedure would remain human-only.

## Current blockers before adoption

1. PF09.6 — PF09.6-Canon-HDE-Build-Checklist-Distillation, §Ops tasks currently defines an Ops task as work that cannot be executed by automated agents and states that automated agents MUST NOT attempt it, claim completion, or simulate external state changes.
2. Repository `AGENTS.md` makes PF-Canon the source of truth and says PF-Canon wins on divergence. A PO instruction in chat supplies authority but does not alter the canonical actor restriction.
3. Repository `AGENTS.md` makes `docs/pfcanon/**` read-only for Codex/dev agents. Therefore an automated agent cannot adopt this amendment directly or edit PF09.6 to remove its own restriction.
4. HDE-EPIC038 `RSC-004` requires separate approval of the actual final discovery-authorization bytes/hash after preflight and the actual final live-authorization bytes/hash after validated discovery. Those run-specific identities do not exist before their prescribed construction gates and cannot be approved by a blanket statement in advance.
5. Calling an automated agent a “human agent” does not satisfy the current rule because the rule classifies the actor by whether it is automated, not by delegation or agency-law terminology.
6. This proposal has no authority until a human PF-Canon owner adopts equivalent wording into PF09.6 through the canonical PF change process and resolves any required PF10 or repository-rule alignment.

## Human adoption decision requested

The PF-Canon owner is asked to accept, reject, or revise the proposed bounded read-only delegation exception. Adoption should preserve PO accountability and exact per-run approvals while distinguishing validated, non-mutating observation from human-only external-state mutation.
