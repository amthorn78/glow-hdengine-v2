# PF10 — HDE-EPIC038 addendum draft (paste-ready; non-canonical)

## Status and authority

This document is a standalone PF10 addendum draft for human PF-Canon-owner review. It does not amend the active PF10 lettered set and has no PF10 authority until it is separately published through the canonical PF change process.

Proposed target: PF10 — HDE Build Notes, active v12.5 lettered set.

Proposed number: Addendum 2.33. The publisher must confirm the next available addendum number at publication time.

The active PF10 files under `docs/pfcanon/` are intentionally unchanged by this draft.

## Proposed Addendum Index entry

2.33) `ci/checks/check_mirror_schema.sh` Is a Python Entry Point with a Legacy Stable Path

## Proposed Addendum

## 2.33) `ci/checks/check_mirror_schema.sh` Is a Python Entry Point with a Legacy Stable Path

Timestamp: 072926 05:47 UTC

Details: Clarifies the interpreter, repository locus, fixed-input behavior, failure classification, retained-path decision, and future migration boundary for the Machine Mirror schema gate.

### 1. Scope

This addendum applies only to the executable repository entrypoint:

`ci/checks/check_mirror_schema.sh`

It governs how plans, CI jobs, QA harnesses, operator instructions, and automated agents identify and invoke that entrypoint. It does not change the Machine Mirror schema, validator behavior, evidence ownership, token semantics, or acceptance posture.

### 2. Current repository fact and history

The current file is Python source. It begins with:

`#!/usr/bin/env python3`

It is tracked as executable and its body is implemented in Python.

The path originated in commit `7b9ce11ca5fb14405fa0a18473ea982705726cbf` as a Bash wrapper that changed to the repository root and executed an embedded Python program. Commit `3040b95d066c088b6cf7f80a0d4ff0aeda94a316` replaced that wrapper with direct Python while retaining the existing path and executable mode.

The historical commits do not state why the `.sh` suffix was retained. Compatibility must therefore not be presented as a proven historical motive. Preserving the established path is, however, the current compatibility decision because CI, sanity orchestration, QA harnesses, tests, documentation, and retained evidence refer to that exact entrypoint.

The `.sh` suffix is legacy path identity. It does not declare the current interpreter.

### 3. Supported invocation contract

The gate must be invoked from the repository root using one of these forms:

Preferred explicit-Python form:

`python ci/checks/check_mirror_schema.sh`

The `python` command must resolve to the supported Python 3 interpreter for the active repository environment.

Supported direct-execution form when Git executable mode and shebang handling are guaranteed:

`ci/checks/check_mirror_schema.sh`

A Python harness should use its active interpreter explicitly, equivalent to:

`[sys.executable, "ci/checks/check_mirror_schema.sh"]`

The following forms are invalid:

`bash ci/checks/check_mirror_schema.sh`

`sh ci/checks/check_mirror_schema.sh`

Forcing the file through a shell causes Python statements to be parsed as shell commands. Typical output includes `import: command not found` followed by a shell syntax error. In an environment containing an unrelated executable named `import`, the invalid invocation may also attempt to run that unrelated command before parsing stops.

### 4. Repository locus and fixed input

The current implementation uses fixed repository-relative paths and must be run from the repository root. Running it from another working directory can produce `MISSING:artifacts/evidence_index.jsonl` even when the tracked mirror exists.

The validator always reads the repository Machine Mirror at:

`artifacts/evidence_index.jsonl`

The current implementation does not parse command-line arguments and does not support caller-selected mirror paths.

Some retained examples append `artifacts/evidence_index.jsonl` to the command. The current program ignores that operand. Such examples must not be interpreted as proof of custom-path support. New plans, operator instructions, and harnesses should omit the unused operand.

### 5. Failure classification and correction

Shell-parser output from `bash ci/checks/check_mirror_schema.sh` or `sh ci/checks/check_mirror_schema.sh` is an invocation or tooling defect, not a Machine Mirror schema finding.

A missing-mirror result obtained outside the repository root is likewise a locus defect until the same supported command is evaluated from the repository root.

An operator or harness may normalize either defect by rerunning the supported invocation from the correct locus. Only the supported invocation's exit status and validator output may be used to claim the Mirror-schema gate PASS or FAIL.

Plans and evidence must preserve the actual command transcript. They must not rewrite a shell-parser failure as validator behavior.

### 6. Compatibility and retained-path decision

Retaining `ci/checks/check_mirror_schema.sh` is accepted. Under a supported invocation, the legacy suffix is not a runtime defect and does not impair current hosted CI.

Retaining the path preserves a broadly referenced gate identity and avoids an incidental rename across active CI, orchestration, QA, documentation, and governance bindings.

The known costs are:

* The suffix can mislead an operator into forcing the file through Bash or `sh`.
* Editors, linters, and path-based automation may initially classify the source as shell code.
* Inconsistent documentation can create false gate failures and unnecessary remediation records.
* Contributors may spend time diagnosing interpreter errors that do not concern the Machine Mirror.

These costs require clear invocation documentation. They do not, by themselves, require an immediate rename.

### 7. Future migration boundary

Any future migration to a `.py` path must be an intentional compatibility change. It must:

1. Introduce and validate the new Python entrypoint.
2. Inventory and update active CI jobs, sanity orchestration, QA harnesses, tests, operator documentation, and current canon references.
3. Preserve historical evidence and historical command transcripts without rewriting them.
4. Preserve both currently supported call shapes during the transition: direct execution and explicit Python execution of the legacy path.
5. Re-run the closed-rails Mirror, Evidence Index, path, hash, and final-LF validation gates required by the owning workflow.
6. Define an explicit deprecation and removal point for the legacy path.

A Bash compatibility wrapper at the legacy path is not transparent while any active caller uses:

`python ci/checks/check_mirror_schema.sh`

Python would attempt to parse that Bash wrapper. Therefore the legacy file must remain Python-compatible until all explicit-Python callers have been drained or another compatibility mechanism preserves their behavior.

No incidental cleanup, suffix-only rename, or partial caller migration is authorized by this addendum.

### 8. Nonclaims

This addendum does not:

* publish or amend active PF10 by itself;
* rename `ci/checks/check_mirror_schema.sh`;
* add a wrapper or change executable mode;
* change the validator, its fixed input, or its exit semantics;
* change the Machine Mirror schema, role rules, field rules, ordering rules, self-record rules, or path-proof rules;
* refresh or modify governed evidence, the Human Evidence Index, the Machine Mirror, hashes, path proofs, manifests, acceptance maps, or close reports;
* establish QA PASS, acceptance-token satisfaction, PF09 movement, deployment readiness, epic completion, or formal closeout; or
* authorize the rewriting of historical artifacts merely to normalize old command spelling.

### 9. Source basis

This addendum is grounded in:

* the current executable `ci/checks/check_mirror_schema.sh`;
* its introduction in commit `7b9ce11ca5fb14405fa0a18473ea982705726cbf`;
* its conversion from a Bash wrapper to direct Python in commit `3040b95d066c088b6cf7f80a0d4ff0aeda94a316`;
* the current direct-execution call sites in `.github/workflows/ci.yml`;
* the current direct-execution call in `tools/evidence/run_sanity_pipeline.py`;
* HDE Governance, the `CI_CHECK_MIRROR_SCHEMA_OK` entry;
* HDE CLI/API Vendor Reference, “Mirror schema check invocation (operator note)”; and
* Glow QA Guide, “Invocation rule (normative; operator-facing).”

### 10. Drain targets

If adopted, this clarification should be kept in PF10 until the stable-path, repository-locus, fixed-input, invalid-shell-invocation, and migration rules are fully represented in their permanent owning homes.

Permanent-canon and repository-documentation review targets:

* HDE Governance, the `CI_CHECK_MIRROR_SCHEMA_OK` entry;
* HDE CLI/API Vendor Reference, “Mirror schema check invocation (operator note)”;
* Glow QA Guide, “Invocation rule (normative; operator-facing)”; and
* the repository Evidence Index operator documentation.

