## 2.24) HDE-EPIC030 OPS-02 completion contract - birth-only vendor-backed no-user smoke

Timestamp: 042926 17:28

### Why

OPS-02 was previously blocked by a planning failure: the task instruction treated required execution facts as still unknown even though the remediation path must provide a complete operator-ready contract for the controlled vendor-backed no-user smoke.

The core product concern is that compatibility must be able to work from birth data only in the current pre-App/no-user posture. A caller-facing or OPS-facing compatibility proof is not sufficient if it requires a fictitious app user_id, a DB-backed user record, or caller-provided person_uid.

This addendum supplies the missing live-truth contract for OPS-02 so the PO can complete the controlled smoke without guessing command shape, target posture, no-user semantics, evidence outputs, or classification rules.

This addendum supersedes any earlier HDE-EPIC030 OPS-02 guidance that treats the following as unresolved when the current OPS evidence has them:

- exact no-user vendor command shape
- birth-only input posture
- PR-02 birth-only no-user implementation proof
- controlled CLI-target execution posture
- OPS-02 evidence-output contract

This addendum does not execute OPS-02. It does not claim QA PASS, Live QA completion, PF09 status change, epic closure, or public contract change.

### Decision / rule / clarification

#### OPS-02 no-user meaning

For HDE-EPIC030 OPS-02, "no-user" means the external command and caller-facing proof use birth data only.

Allowed caller or command inputs for the controlled OPS-02 vendor smoke:

- --source vendor
- --birthdate-a
- --birthtime-a
- --location-a
- --birthdate-b
- --birthtime-b
- --location-b

Forbidden caller or command inputs for the controlled OPS-02 vendor smoke:

- --user-a
- --user-b
- --a-user
- --b-user
- app user IDs
- user_id
- person_uid
- DB-backed user BodyGraphs as caller input
- --source db
- any inline secret value

The command may create or consume deterministic internal metadata inside the resolver boundary if the implementation does so, but the PO-run command must not require the caller to supply any user identity.

#### Exact command template

The OPS-02 command template is:

hdctl showcompat --source vendor --birthdate-a "<YYYY-MM-DD>" --birthtime-a "<HH:MM>" --location-a "<LOCATION_A>" --birthdate-b "<YYYY-MM-DD>" --birthtime-b "<HH:MM>" --location-b "<LOCATION_B>"

Before execution, OPS-02 must replace every placeholder in that template using the birth data recorded in:

audit/ops/hde-epic030/ops-02/sample_birth_inputs.json

OPS-02 must not invent substitute birth values while sample_birth_inputs.json exists.

The executable command copied into:

audit/ops/hde-epic030/ops-02/vendor_command.txt

must contain no unresolved placeholder tokens before it is run.

#### OPS-02 target fact posture

For this specific OPS-02 controlled smoke, the target is the HD Engine CLI running in the PO-controlled execution context, using the vendor source through HDAPI.

The required target facts are:

- command target: hdctl showcompat
- data source: --source vendor
- execution context: PO-controlled terminal with hdctl available
- vendor binding: HDAPI_BASE_URL
- vendor credential presence: HD_API_KEY
- geocoding credential presence, if required by the command path: GEO_API_KEY
- deterministic capture pins: LC_ALL=C, LANG=C, TZ=UTC
- open rails for the vendor step only: SAFE_MODE=0, ALLOW_NETWORK=1
- application environment for this controlled smoke: APP_ENV=dev

HDE_BASE_URL is not required for this exact CLI vendor smoke unless the command is changed to call an HD Engine HTTP service. A missing HDE_BASE_URL is therefore not a blocker for the command above.

If a future OPS-02 attempt changes the target from CLI vendor execution to an HD Engine HTTP service call, that change requires a new PF07-backed target fact set before execution.

#### PR-02 prerequisite now satisfied at implementation-proof level

PR-02 remediation corrected the local implementation proof shape.

The accepted PR-02 remediation proof is:

test_no_user_boundary_accepts_birth_only_input_without_person_uid_or_user_id_and_is_ab_ba_stable

That proof establishes the local boundary from pure birth caller inputs:

- birthdate
- birthtime
- location

and explicitly excludes caller-provided:

- person_uid
- user_id

PR-02 also preserves:

- /api/compat/v1 as internal/admin
- public Reader bands-only and numeric-free posture
- no vendor command run by Codex
- OPS-02 as PO-only vendor validation

OPS-02 must therefore validate the vendor-backed runtime path, not re-litigate the PR-02 local proof.

#### OPS-01 command-proof posture now usable for OPS-02

Current OPS-01 discovery evidence records a concrete command candidate rather than an unresolved command posture.

OPS-01 command proof is usable for OPS-02 only if the current file:

audit/ops/hde-epic030/ops-01/vendor_command_candidate.txt

contains the concrete command template above or the same command with concrete birth values substituted.

If that file contains the unresolved sentinel, OPS-02 must stop as TOOLING_BLOCKED.

If current OPS evidence conflicts with earlier PF10 text that said OPS-01 command proof was unresolved, the later current evidence posture plus this addendum governs for OPS-02.

#### Required OPS-02 preflight matrix

OPS-02 may run only when all rows below are satisfied.

- Exact command exists: audit/ops/hde-epic030/ops-02/vendor_command.txt contains an executable hdctl showcompat --source vendor command with birth-only flags. If unresolved or placeholder-bearing: TOOLING_BLOCKED.
- Birth-only input exists: audit/ops/hde-epic030/ops-02/sample_birth_inputs.json contains birth values for A and B. If absent or incomplete: TOOLING_BLOCKED.
- No user identity in command: vendor_command.txt contains no --user-a, --user-b, --a-user, --b-user, user_id, or person_uid. If present: FAIL_TOOLING before execution.
- No inline secrets: vendor_command.txt contains no secret values. If present: FAIL_TOOLING before execution.
- Vendor source explicit: command contains --source vendor. If absent: TOOLING_BLOCKED.
- Open rails are explicit for vendor step only: execution wrapper sets SAFE_MODE=0 and ALLOW_NETWORK=1 for the command run. If absent: TOOLING_BLOCKED.
- Determinism pins present: execution wrapper sets LC_ALL=C, LANG=C, TZ=UTC. If absent: TOOLING_BLOCKED.
- Required vendor env presence captured: redacted_env_presence.json records booleans for HDAPI_BASE_URL, HD_API_KEY, and GEO_API_KEY as applicable. If required keys are false or uncaptured: TOOLING_BLOCKED.
- Secret posture safe: env capture is presence-only booleans and no secret values appear in stdout, stderr, command, summaries, or JSON. If secret values are persisted: FAIL_TOOLING and quarantine affected artifact.
- PR-02 proof exists: PF10 Addendum 2.23 records the birth-only no-user boundary proof and no Codex vendor run. If absent or contradicted by current PR evidence: TOOLING_BLOCKED.
- PO proceed authorization recorded: request_summary.txt records PO authorization to run the controlled vendor smoke. If absent: TOOLING_BLOCKED.

#### Required OPS-02 execution wrapper

Use this wrapper only after every preflight row above is satisfied:

set +e; SAFE_MODE=0 ALLOW_NETWORK=1 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC sh -lc "$(cat audit/ops/hde-epic030/ops-02/vendor_command.txt)" > audit/ops/hde-epic030/ops-02/stdout.json 2> audit/ops/hde-epic030/ops-02/stderr.log; printf "%s\n" "$?" > audit/ops/hde-epic030/ops-02/exit_code.txt

Rules:

- Do not edit the command after a failed run to force a PASS.
- Do not retry with different flags, URLs, hostnames, ports, credentials, or birth data unless the change is PF07-backed or PF10-backed and recorded in result_summary.md.
- Do not run this command through Codex or any automated agent.
- Do not persist secret values.
- Do not treat an exit-zero run as QA PASS or epic closure.

#### Required OPS-02 evidence outputs

OPS-02 completion requires these files under:

audit/ops/hde-epic030/ops-02/

Required files:

- vendor_command.txt
- sample_birth_inputs.json
- redacted_env_presence.json
- request_summary.txt
- stdout.json
- stderr.log
- exit_code.txt
- result_summary.md
- pfcanon_ops02_completion_matrix.md
- files_sha256.txt

Required content:

- vendor_command.txt must contain the exact executable command used.
- sample_birth_inputs.json must contain the birth values substituted into the command.
- redacted_env_presence.json must contain key names and booleans only.
- request_summary.txt must state:
  - explicit vendor source was used
  - no person_uid was supplied
  - no user_id or app user ID was supplied
  - birth-only input shape was used
  - PO proceed authorization was present
- stdout.json must contain the command stdout, if any.
- stderr.log must contain the command stderr, if any.
- exit_code.txt must contain only the command exit code and trailing LF.
- result_summary.md must classify the outcome as exactly one of:
  - PASS
  - FAIL_BEHAVIOR
  - FAIL_TOOLING
  - TOOLING_BLOCKED
- pfcanon_ops02_completion_matrix.md must map each OPS-02 prerequisite to its PF canon or PF10 basis and evidence status.
- files_sha256.txt must include hashes for all OPS-02 evidence files except itself.

#### OPS-02 outcome classification

Use these classifications exactly.

PASS

Use PASS only when all of the following are true:

- all preflight rows pass
- the exact command runs
- exit_code.txt records 0
- the command uses --source vendor
- the command uses birth-only flags
- no app user ID, user_id, or caller-provided person_uid is supplied
- no secret values are persisted
- stdout.json is non-empty and parseable as JSON, unless the command's documented success output differs
- result_summary.md states this is implementation-validation evidence only, not QA PASS, Live QA completion, PF09 status change, or epic closure

FAIL_BEHAVIOR

Use FAIL_BEHAVIOR only when all prerequisites are proven, the command runs, no tooling or secret failure occurs, and the observed runtime behavior shows that vendor-backed compatibility cannot be computed from the birth-only no-user command.

Examples:

- command requires user_id
- command requires caller-provided person_uid
- command cannot resolve BodyGraphs from birth-only vendor input even though vendor env and credentials are present
- command output contradicts the expected no-user vendor behavior

FAIL_TOOLING

Use FAIL_TOOLING when OPS-02 execution or evidence is contaminated or invalid as a tool run.

Examples:

- command contains inline secret values
- stdout, stderr, command files, summaries, JSON, checksum ledgers, or logs persist secret values
- command was changed by guesswork after failure
- command uses a user identity input
- evidence files are missing after an attempted run
- env capture stores secret values instead of booleans

Any secret-bearing artifact must be quarantined, named in result_summary.md, and excluded from proof.

TOOLING_BLOCKED

Use TOOLING_BLOCKED when OPS-02 cannot safely run.

Examples:

- vendor_command.txt is unresolved
- vendor_command.txt still contains placeholders
- sample_birth_inputs.json is missing or incomplete
- required vendor env presence is false or uncaptured
- hdctl is unavailable
- PO proceed authorization is absent
- PR-02 accepted birth-only proof is unavailable or contradicted
- the target is changed to an HTTP service call without PF07-backed target facts

### PF09 impact and status posture

Affected PF09 task:

HDE-DISS005

Affected PF09 subtask:

HDE-DISS005.2

OPS-02 by itself does not authorize an immediate PF09 status change.

A successful OPS-02 run may support the following statement:

Supportable from repo evidence: HDE-DISS005.2 has vendor-backed birth-only no-user implementation-validation evidence, pending final QA interpretation and any later PF09.2 drain.

If OPS-02 is TOOLING_BLOCKED, FAIL_TOOLING, or FAIL_BEHAVIOR, no PF09 status change is supportable.

### Non-claims

This addendum does not claim:

- QA PASS
- Live QA completion
- final po-006 acceptance
- public Reader change
- new public compat route
- new CLI flag
- PF09 status change
- epic closure
- PF-canon drain completion

### Drain targets

Primary drain target:

the HDE-EPIC030 po-006 OPS-02 task block and any remediation runbook derived from it

Secondary drain targets, only if PO determines the guidance must persist after HDE-EPIC030:

- Glow QA Guide pre-App/no-user compatibility QA posture
- HDE CLI-API-Vendor-Ref hdctl showcompat --source vendor birth-argument posture
- Glow Infrastructure CLI-target versus HTTP-target distinction for vendor smoke tasks
- HDE Build Checklist Dissolution HDE-DISS005.2 notes
- HDE Mechanics Guide no-user compatibility boundary notes
