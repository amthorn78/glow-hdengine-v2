## 1\) Live QA Plan

### Front matter

Epic ID: HDE-EPIC038 Plan type: Live QA Plan / Runbook Execution venue: Codespaces Target environment: dev; one separately authorized, bounded canonical-vendor check Plan revision: r7 Date (UTC): 2026-07-26 Operators (names-only): PO

#### Canon precedence statement (required)

> “PF10 supersedes all other PF docs where it speaks; otherwise follow PF-Canon.”

#### Canon set (explicit; stable references only)

* PF10 — HDE Build Notes  
  * Addendum 2.1 — PR-01 HDE-EPIC038  
  * Addendum 2.2 — PR-02 HDE-EPIC038  
  * Addendum 2.3 — PR-03 HDE-EPIC038  
  * Addendum 2.4 — PR-04 HDE-EPIC038 — Approved Rescope and Canon Decisions  
  * Addendum 2.5 — PR-04 HDE-EPIC038  
  * Addendum 2.6 — OPS-01 HDE-EPIC038  
  * Addendum 2.7 — PR-05 HDE-EPIC038  
  * Addendum 2.8 — OPS-02 HDE-EPIC038  
  * Addendum 2.9 — PR-06 Post-Merge Remediation and OPS-01R HDE-EPIC038 — Approved Rescope and ADR-CANON-004  
  * Addendum 2.10 — PR-06 Remediation PR-A HDE-EPIC038  
  * Addendum 2.11 — PO-Delegated OPS Execution Authority — PO Authorization Controls Executor Identity  
  * Addendum 2.12 — pg-bridge and DB\_BRIDGE\_URL Deprecation and Retirement \- Direct PostgreSQL Is the Sole Active HDE Database Transport  
  * Addendum 2.13 — HDE-EPIC038 Post-PR359 Remediation — ADR-CANON-006 Direct-Only Selection Evidence and Historical Bridge Quarantine  
  * Addendum 2.14 — HDE-EPIC038 Post-PR359 Remediation — ADR-CANON-007 Authorization-Bound OPS-03 Direct Read-Only Posture Packet  
  * Addendum 2.15 — HDE-EPIC038 Post-PR359 Remediation — ADR-CANON-008 Direct-Only PF09.6 Completion Semantics and PR-06R Ownership  
  * Addendum 2.16 — HDE-EPIC038 PR-06R-A Merge — Scalable Manifest-Derived Release Identity, External Attestation, and Portable Evidence Semantics  
  * Addendum 2.17 — PR-06 Remediation HDE-EPIC038 PR-06R-A  
  * Addendum 2.18 — PR-06 Remediation \- OPS-03 HDE-EPIC038  
  * Addendum 2.19 — PR-06 Remediation \- HDE-EPIC038 OPS-03 — Authorized Reader-Role Provisioning, Direct Read-Only Capture, and Evidence-Admission Boundary  
  * Addendum 2.20 — PR-06 Remediation PR-06R-B HDE-EPIC038  
  * Addendum 2.21 — PR-06 Remediation State  
  * Addendum 2.22 — Implementation Retrospective HDE-EPIC038  
  * Addendum 2.23 — Post Implementation Audit Triage HDE-EPIC038  
  * Addendum 2.24 — Syntax-Origin Defects Remain Non-Blocking Regardless of Literal Execution Effect  
  * Addendum 2.25 — Recognize Epic Remediation Plans Pending Template Drainage  
  * Addendum 2.26 — HDE-EPIC038 Epic Remediation PR-01 — PF09.6 HDE-DIST007 Canonical Adapter Factory Route-Mount Parity  
  * Addendum 2.27 — HDE-EPIC038 HDE-DIST007 Post-Merge Bounded Rescope and CI Completion Authority  
  * Addendum 2.28 — Epic Remedial PR-01 HDE-EPIC038  
* PF04 — HDE Governance, §2.0 Acceptance Tokens (single-home roster); §9.7 Token fidelity & plan approval rails; §9.8 QA plans — step-level Deliverables (no screen-only acceptance)  
* PF06 — Epic Process Guide, §0.4.1  
* PF09.6 — HDE Build Checklist Distillation, §Subtask HDE-DIST001.4 — DB posture & runtime checks (harness for HDE-FERM004); §Subtask HDE-DIST001.5 — BodyGraph mechanics gates; §Subtask HDE-DIST001.6 — One-button evidence harness & release sanity pipeline; §Subtask HDE-DIST001.9 — DB–bridge parity & env connectivity; §Subtask HDE-DIST001.10 — Architecture snapshot (keys-only) evidence; §Subtask HDE-DIST001.11 — v2 mapped-cache persistence hardening; §Subtask HDE-DIST005.1 — Canonical encodings & environment pins; §Subtask HDE-DIST005.2 — Global Index & Mirror discipline  
* PF12 — HDE Schemas and Artifacts, §0.2; §6.2; §8.6; §Path-proof transcript schema (governed artifacts)  
* PF19 — Glow QA Guide, §3.1; §4.4.3 Per-epic QA step logs manifest (qa\_step\_logs\_manifest.json); §4.4.5 Step log header (required fields; token semantics are claims-safe); §12.2  
* PF27 — Canon Plan Templates, §Canon set (explicit; stable references only); §CHECK \<check\_id\>: \<check\_name\>  
* PF29 — HDE Users Guide, §3; §4.1; §7.2; §13.2; used only for the documented local launcher and compatibility-surface posture

### Scope statement

This runbook independently exercises all twenty-three required proof obligations in order. It separates Live QA from implementation records, repository presence, operational captures, deployment, migration, PF09 movement, acceptance, and epic closure.

Except for the explicitly authorized bounded check `qa-08-po-008`, execution remains local, deterministic, closed-rails, and non-operational. The runbook does not start services, rerun OPS, invoke database provisioning, deploy, migrate, or remediate source code.

The PO-approved in-place safety correction for `qa-08-po-008` is the sole source-remediation exception: it is required before the authorized call and is limited to closing producer authorization, target, rails, input, request-bound, retained-shape, and check-mode bypasses identified during execution. All future outputs begin as `NOT RUN`. A pre-existing artifact never establishes current-run PASS.

#### PF10 overrides / conflicts (if any)

* Direct database access is the only active transport. Retained bridge-era material is historical integrity evidence, not a fallback or current provider.  
* `catalog/manifest.json` is the sole tracked release-identity input. External attestation is produced outside the source checkout.  
* The integrated chain has nineteen ordered stages, stops at the first required failure, reruns no OPS, and does not repair an inconsistent evidence graph.  
* `tools/evidence/update_evidence_index.py` is the canonical companion-artifact authority. `--check` detects drift; omitting `--check` writes.  
* Addenda 2.26 through 2.28 record the HDE-DIST007 mapping and the completed selected-factory route-mount and hosted-CI remediation. The production and documented startup factory now mounts the existing compatibility blueprint; Live QA remains unexecuted and separate from implementation, repository, CI, release, PF09, acceptance, and closeout claims.  
* Implementation and release evidence do not establish QA PASS, token satisfaction, deployment, migration, PF09 movement, acceptance, or closeout.

### Open-Rails Live QA Requirement for production-affecting epics

* PO execution override (2026-07-27): the supplied fixed-HEAD precondition is a planning defect and is waived. QA execution records the runtime source identity for provenance, but no QA readiness, behavioral, routing, or finalization judgment depends on equality to a preplanned commit hash; future plan generation must not reintroduce a fixed-HEAD QA gate.
* PO-approved producer correction (2026-07-27): live generation is permitted only for the exact sole canonical v2 target, a fresh event-bound PO receipt, caller-supplied open rails and canonical pins, built-in synthetic defaults, and at most two attempts. It does not self-open rails or pass the authorization receipt into the vendor client. Read-only `--live --check` remains credential-free and network-free. The sole-owner companion derives the live entry’s `produced_at_utc` from the validated current artifact instead of a historical constant. These corrections are required to prevent the same bypass and false-provenance posture from reaching production.
Check `qa-08-po-008` is the required bounded open-rails step.

* Behavior proved: two same-run vendor acquisitions using synthetic inputs, followed by AB/BA canonical Reader emission and independent validation.  
* Target: the exact canonical HumanDesignAPI v2 base `https://api.humandesignapi.nl/v2`; the vendor provides no separately marked staging, sandbox, development, or nonproduction base.
* Rails: `SAFE_MODE=0`, `ALLOW_NETWORK=1`, `APP_ENV=dev`, `LC_ALL=C`, `LANG=C`, `TZ=UTC`. `APP_ENV=dev` constrains the local application invocation; it does not classify the external canonical vendor target as development or nonproduction.
* Bound: no more than two requests; one attempt per request; bounded timeouts; no uncontrolled retry.  
* Authorization: fresh, one-time PO authorization and a unique event receipt are mandatory. Only the receipt hash is retained. A checked-in historical note, proof, or receipt hash confers no current authority.
* Secret safety: only presence is checked. No key, base URL, personal input, request body, response body, or raw vendor payload may enter the step log.  
* Evidence: `audit/qa/hde-epic038/checks/qa-08-po-008/primary.log` and, only after a successful current run, `audit/gates/determinism/open_rails_vendor_abba.json`.  
* It proves: the bounded current interaction, two-request limit, same-input reuse, canonical AB/BA equality, repeatability, and safe retained shape.  
* It does not prove: broad vendor-version conformance, application production behavior, recurring authorization, acceptance-token satisfaction, deployment, or closeout.
* If fresh authorization, required secret presence, or exact canonical-target classification is absent, record `TOOLING_BLOCKED`; do not make a call.

### PF23 anchors

PF23 was consulted for names-only planning context concerning the application factories, compatibility route mounting, and indexed evidence topology. Live repository validation controls current-state conflicts. PF23 supplies no executable check, deliverable, evidence requirement, token claim, blocker, or current-repository proof in this plan.

### Environment and rails posture

#### Determinism pins (canonical pins only)

Default execution pins:

* `LC_ALL=C`  
* `LANG=C`  
* `TZ=UTC`

#### Rails posture (explicit)

Default rails:

* `SAFE_MODE=1`  
* `ALLOW_NETWORK=0`  
* `APP_ENV=dev`

Only `qa-08-po-008` may temporarily use open rails. The logging wrapper applies rails to the child command without altering later checks.

The operator working checkout's branch and cleanliness are informational and are not general Live QA PASS/FAIL predicates. For `qa-21-po-021`, current `HEAD` supplies the exact source commit; the check creates a separate checkout at that commit, proves the isolated checkout clean before the builder runs, and then relies on the builder and verifier to enforce their own exact-source and cleanliness contracts.

No service process is started by this runbook.

#### Dependency profiles

Profile A — Python QA:

* Required dependencies: Python 3.10 or newer, pytest, Flask, jsonschema, psycopg, and the importable repository package.  
* Preflight check, Command A1: `command -v python >/dev/null 2>&1 && python -c 'import sys, pytest, flask, jsonschema, psycopg, engine; raise SystemExit(0 if sys.version_info >= (3, 10) else 1)'`  
* If missing, activation/install action, Command A2: `bash .devcontainer/scripts/post-create.sh`  
* If still unavailable: no alternative installation command is proven; record the affected check as `TOOLING_BLOCKED`.

Profile B — Python QA plus shell validators:

* Required dependencies: Profile A, bash, cat, mkdir, rm, head, sha256sum, awk, cut, tail, od, grep, and tr.  
* Preflight check, Command B1: `command -v bash >/dev/null 2>&1 && command -v cat >/dev/null 2>&1 && command -v mkdir >/dev/null 2>&1 && command -v rm >/dev/null 2>&1 && command -v head >/dev/null 2>&1 && command -v sha256sum >/dev/null 2>&1 && command -v awk >/dev/null 2>&1 && command -v cut >/dev/null 2>&1 && command -v tail >/dev/null 2>&1 && command -v od >/dev/null 2>&1 && command -v grep >/dev/null 2>&1 && command -v tr >/dev/null 2>&1 && command -v python >/dev/null 2>&1 && python -c 'import sys, pytest, flask, jsonschema, psycopg, engine; raise SystemExit(0 if sys.version_info >= (3, 10) else 1)'`  
* If missing, activation/install action, Command B2: `bash .devcontainer/scripts/post-create.sh`  
* If a system utility remains unavailable: none proven; record `TOOLING_BLOCKED`.

Profile C — external release attestation:

* Required dependencies: Python 3.10 or newer, git, setuptools 68 or newer, wheel, and an absent external output target.  
* Preflight check, Command C1: `command -v git >/dev/null 2>&1 && command -v python >/dev/null 2>&1 && python -c 'import importlib.metadata, sys, setuptools, wheel; setuptools_major=int(importlib.metadata.version("setuptools").split(".", 1)[0]); raise SystemExit(0 if sys.version_info >= (3, 10) and setuptools_major >= 68 else 1)' && test ! -e /tmp/hde-epic038-release-attestation`  
* If Python/project dependencies are missing, activation action, Command C2: `bash .devcontainer/scripts/post-create.sh`  
* If builder packages remain missing, install action, Command C3: `python -m pip install 'setuptools>=68' wheel`  
* If git is missing or the external target already exists: no safe automatic action is proven; record `TOOLING_BLOCKED`.

Profile D — bounded live vendor check:

* Required dependencies: Profile A, fresh one-time PO authorization, a unique unprinted `QA08_PO_EVENT_RECEIPT`, `HD_API_KEY`, `GEO_API_KEY`, and `HD_API_BASE_URL` identifying the exact canonical HumanDesignAPI v2 base; the deprecated temporary compatibility alias `HDAPI_BASE_URL` is permitted only when `HD_API_BASE_URL` is absent.
* PO endpoint-availability decision (2026-07-27): HumanDesignAPI provides no separately marked staging, sandbox, development, or nonproduction base. The exact canonical base is eligible only for this two-request producer after a fresh one-time PO authorization event; neither configuration presence nor a prior artifact confers recurring authority.
* Value-safe preflight, Command D1: `SAFE_MODE=0 ALLOW_NETWORK=1 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC python tools/evidence/generate_open_rails_abba_proof.py --live-readiness-check`
* If packages are missing, activation action: Command A2.  
* If authorization, secrets, or exact canonical-target classification are absent: none may be installed or inferred; record `TOOLING_BLOCKED`.

### PO inputs needed

* Executing PO identity, names-only.  
* Fresh one-time authorization for `qa-08-po-008`.  
* A unique one-event `QA08_PO_EVENT_RECEIPT`, generated without printing and cleared with the confirmation immediately after invocation; only its SHA-256 digest may be retained.
* Required open-rails secret names provisioned in the Codespace; values must never be copied into commands or logs.  
* The public canonical vendor base is required; no live database credential, OPS authorization, or reusable login is requested.
* Missing optional synthetic input variables are acceptable; the repository producer uses fabricated synthetic defaults.  
* If a required input is missing, block only the affected check.

### Evidence posture and directory structure

#### Epic QA root normalization (required)

Canonical root:

`audit/qa/hde-epic038/`

The root is `QA-created`; it was absent at plan-validation time. Step 0 creates it.

No per-run root, timestamp directory, mutable root selector, or alternate acceptance root is permitted.

#### Recommended canonical layout (default for new plans)

* Meta: `audit/qa/hde-epic038/00_meta/`  
* Check evidence: `audit/qa/hde-epic038/checks/<check-id>/`  
* Required check log: `audit/qa/hde-epic038/checks/<check-id>/primary.log`  
* Manifest: `audit/qa/hde-epic038/qa_step_logs_manifest.json`  
* Manifest proof: `audit/qa/hde-epic038/qa_step_logs_manifest.json.path_proof.txt`  
* QA RCA and Doc Delta summary: `audit/qa/hde-epic038/00_meta/qa_rca_doc_delta_summary.md`

All check logs are current-state evidence. A rerun replaces the stable check log rather than creating a new directory.

All checks are tokenless:

* `intended_tokens`: `[]`  
* `claimed_tokens`: `[]`

#### Step-log header schema expectations (minimum; required)

Each `primary.log` begins with one JSON line using schema `pf27.step_log_header.v1`. Required status values are `PASS`, `FAIL_BEHAVIOR`, `FAIL_TOOLING`, `TOOLING_BLOCKED`, `SKIPPED`, or `WARN`.

For PASS:

* `exit_code` must be `0`.  
* `evidence_artifacts` must include that check’s `primary.log`.  
* Every additional required artifact must exist.  
* PASS cannot rely only on path presence.

For non-PASS:

* `fail_status` equals `status`.  
* `claimed_tokens` remains `[]`.

Exit `125` means a declared prerequisite or required input is unavailable and maps to `TOOLING_BLOCKED`. Exit `126` or `127` means the command could not execute and maps to `FAIL_TOOLING`. For every other nonzero behavior result, declare `QA_NONZERO_CAUSE` as exactly `FAIL_BEHAVIOR` or `FAIL_TOOLING` before invoking `qa_run`. The wrapper records both that classification and the caller-supplied predicate; the predicate is not used as an automatic verdict. If `QA_NONZERO_CAUSE` is absent or invalid when such a result occurs, the wrapper records the invalid classification and fails closed as `FAIL_TOOLING` with exit code `74`.

Before a Profile C invocation that may require activation, declare `QA_PROFILE_C_ACTION` as exactly `C2`, `C3`, or `NONE`, and declare `QA_PROFILE_C_FOLLOWUP` as exactly `C3` or `NONE`. Both default to `NONE`. Invalid values execute no activation and leave readiness fail-closed. The wrapper records the declared choices and logs only activation and preflight commands that actually execute.

Run the following bootstrap definitions once in the same terminal before Step 0\. If the terminal is replaced, rerun both definitions before continuing.

Bootstrap Command 1 — canonical header writer:

```
write_pf27_header() {
python - << 'PY'
import datetime
import json
import os

def env(name: str, default: str = "") -> str:
    value = os.environ.get(name)
    return value if value is not None else default

def env_json(name: str, default):
    raw = os.environ.get(name)
    if raw is None or raw == "":
        return default
    return json.loads(raw)

schema_version = "pf27.step_log_header.v1"
timestamp_utc = datetime.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"

status = env("PASS_FAIL")
fail_status = "" if status == "PASS" else status
exit_code_raw = env("EXIT_CODE", "")
exit_code = int(exit_code_raw) if exit_code_raw != "" else None
if status == "PASS" and exit_code != 0:
    raise SystemExit("PASS requires EXIT_CODE=0")
commands = env_json("COMMANDS_JSON", [])
if isinstance(commands, str):
    commands = [commands]
command = "; ".join(commands) if commands else "N/A"

header = {
    "schema_version": schema_version,
    "timestamp_utc": timestamp_utc,
    "check_id": env("CHECK_ID"),
    "check_name": env("CHECK_NAME"),
    "status": status,
    "fail_status": fail_status,
    "command": command,
    "command_provenance": env("COMMAND_PROVENANCE", "Explicitly created"),
    "exit_code": exit_code,
    "evidence_artifacts": env_json("ARTIFACTS_JSON", []),
    "captured_env": {
        "SAFE_MODE": env("SAFE_MODE"),
        "ALLOW_NETWORK": env("ALLOW_NETWORK"),
        "APP_ENV": env("APP_ENV"),
        "LC_ALL": env("LC_ALL"),
        "LANG": env("LANG"),
        "TZ": env("TZ"),
    },
    "pf_refs": env_json("PF_REFS_JSON", []),
    "intended_tokens": env_json("INTENDED_TOKENS_JSON", []),
    "claimed_tokens": env_json("CLAIMED_TOKENS_JSON", []),
}

print(json.dumps(header, ensure_ascii=False))
PY
}
```

Bootstrap Command 2 — QA-created stable-log wrapper:

```
qa_run() {
  if [ "$#" -ne 9 ]; then
    printf '%s\n' "qa_run requires 9 arguments"
    return 64
  fi

  qa_id="$1"
  qa_name="$2"
  qa_safe="$3"
  qa_network="$4"
  qa_app="$5"
  qa_declared_failure="$6"
  qa_refs="$7"
  qa_extra="$8"
  qa_command="$9"
  qa_log="audit/qa/hde-epic038/checks/${qa_id}/primary.log"
  qa_body="${qa_log}.body.tmp"
  qa_header="${qa_log}.header.tmp"
  qa_exact_command="SAFE_MODE=${qa_safe} ALLOW_NETWORK=${qa_network} APP_ENV=${qa_app} LC_ALL=C LANG=C TZ=UTC ${qa_command}"
  qa_activation_record=""
  qa_secondary_command=""
  qa_c_action="${QA_PROFILE_C_ACTION:-NONE}"
  qa_c_followup="${QA_PROFILE_C_FOLLOWUP:-NONE}"
  qa_cause="${QA_NONZERO_CAUSE:-}"

  case "$qa_id" in
    qa-00-step-0-discovery|qa-03-po-003|qa-19-po-019|qa-20-po-020)
      qa_profile="B"
      ;;
    qa-08-po-008)
      qa_profile="D"
      ;;
    qa-21-po-021)
      qa_profile="C"
      ;;
    *)
      qa_profile="A"
      ;;
  esac

  case "$qa_profile" in
    A)
      qa_profile_command="command -v python >/dev/null 2>&1 && python -c 'import sys, pytest, flask, jsonschema, psycopg, engine; raise SystemExit(0 if sys.version_info >= (3, 10) else 1)'"
      qa_activation_command="bash .devcontainer/scripts/post-create.sh"
      ;;
    B)
      qa_profile_command="command -v bash >/dev/null 2>&1 && command -v cat >/dev/null 2>&1 && command -v mkdir >/dev/null 2>&1 && command -v rm >/dev/null 2>&1 && command -v head >/dev/null 2>&1 && command -v sha256sum >/dev/null 2>&1 && command -v awk >/dev/null 2>&1 && command -v cut >/dev/null 2>&1 && command -v tail >/dev/null 2>&1 && command -v od >/dev/null 2>&1 && command -v grep >/dev/null 2>&1 && command -v tr >/dev/null 2>&1 && command -v python >/dev/null 2>&1 && python -c 'import sys, pytest, flask, jsonschema, psycopg, engine; raise SystemExit(0 if sys.version_info >= (3, 10) else 1)'"
      qa_activation_command="bash .devcontainer/scripts/post-create.sh"
      ;;
    C)
qa_profile_command="command -v git >/dev/null 2>&1 && command -v python >/dev/null 2>&1 && python -c 'import importlib.metadata, sys, setuptools, wheel; setuptools_major=int(importlib.metadata.version(\"setuptools\").split(\".\", 1)[0]); raise SystemExit(0 if sys.version_info >= (3, 10) and setuptools_major >= 68 else 1)' && test ! -e /tmp/hde-epic038-release-attestation"
      qa_activation_command=""
      ;;
    D)
      qa_profile_command="command -v python >/dev/null 2>&1 && python -c 'import sys, pytest, flask, jsonschema, psycopg, engine; raise SystemExit(0 if sys.version_info >= (3, 10) else 1)'"
      qa_activation_command="bash .devcontainer/scripts/post-create.sh"
      qa_secondary_command="python tools/evidence/generate_open_rails_abba_proof.py --live-readiness-check"
      ;;
  esac
  if [ "$qa_profile" = "D" ]; then
    case "${qa_safe}:${qa_network}" in
      0:1) ;;
      1:0) qa_secondary_command="" ;;
      *) qa_secondary_command="printf '%s\\n' 'INVALID_PROFILE_D_RAILS'; exit 1" ;;
    esac
  fi

  case "$qa_id" in
    qa-00-step-0-discovery)
      qa_path_command='test "$(basename "$(git rev-parse --show-toplevel)")" = "glow-hdengine-v2"'
      ;;
    qa-01-po-001)
      qa_path_command='test -f tests/evidence/test_hde_epic038_release_sanity.py'
      ;;
    qa-02-po-002)
      qa_path_command='test -f scripts/release_id_recompute.py && test -f tests/runtime/test_identity.py && test -f tests/cli/test_showcompat_parity_and_identity.py && test -f tests/transport/test_internal_version_contract.py'
      ;;
    qa-03-po-003)
      qa_path_command='test -f ci/checks/check_env_pins.sh && test -f tools/evidence/generate_env_matrix_snapshot.py && test -f artifacts/runtime/env_matrix.snapshot.json'
      ;;
    qa-04-po-004)
      qa_path_command='test -f tools/evidence/run_canonical_json_gate.py && test -f tools/evidence/generate_open_rails_abba_proof.py && test -f tests/cli/test_cli_canonical_bytes.py && test -f tests/cli/test_showcompat_parity_and_identity.py'
      ;;
    qa-05-po-005)
      qa_path_command='test -f tools/evidence/generate_a7_transport_proofs.py && test -f tests/http/test_reader_a7_transport.py && test -f tests/http/test_endpoint_catalog.py && test -f docs/ENDPOINTS_CATALOG.json'
      ;;
    qa-06-po-006)
      qa_path_command='test -f Procfile && test -f scripts/start_web.sh && test -f adapter/factory.py && test -f adapter/http_reader.py && test -f adapter/wsgi.py && test -f engine/http/compat_handler.py && test -f tests/http/test_compat_endpoint_contract.py && test -f tests/adapter/test_compat_http_dev.py && test -f tests/adapter/test_compat_http_parity.py'
      ;;
    qa-07-po-007)
      qa_path_command='test -f ci/checks/run_rails_job_definitions.py && test -f ci/jobs/rails_closed_refusal.yml && test -f ci/jobs/rails_open_conformance.yml && test -f ci/jobs/logs_keys_only_redaction.yml'
      ;;
    qa-08-po-008)
      qa_path_command='test -f tools/evidence/generate_open_rails_abba_proof.py && test -f tools/evidence/update_evidence_index.py'
      ;;
    qa-09-po-009)
      qa_path_command='test -f tests/bodygraph/test_projection.py && test -f tools/evidence/generate_bodygraph_policy_proofs.py'
      ;;
    qa-10-po-010)
      qa_path_command='test -f tests/bodygraph/test_vendor_client.py && test -f tests/bodygraph/test_resolver_vendor.py && test -f tests/bodygraph/test_ingest.py && test -f tools/evidence/generate_rails_gate_evidence.py'
      ;;
    qa-11-po-011)
      qa_path_command='test -f tests/evidence/test_architecture_snapshot.py && test -f tests/http/test_endpoint_catalog.py && test -f artifacts/architecture/architecture_snapshot.keys_only.json && test -f docs/ENDPOINTS_CATALOG.json'
      ;;
    qa-12-po-012)
      qa_path_command='test -f ci/checks/check_direct_db_contract.py && test -f tests/db/test_direct_db_pr06r.py && test -f tests/unit/test_check_direct_db_contract.py'
      ;;
    qa-13-po-013)
      qa_path_command='test -f tests/evidence/test_hde_epic038_release_sanity.py && test -d audit/ops/hde-epic038/ops-01'
      ;;
    qa-14-po-014)
      qa_path_command='test -f engine/db/ddl_identity_projection.py && test -f tests/db/test_ddl_identity_projection.py'
      ;;
    qa-15-po-015)
      qa_path_command='test -f tests/ops/test_hde_epic038_ops03.py && test -d audit/ops/hde-epic038/ops-03'
      ;;
    qa-16-po-016)
      qa_path_command='test -f tools/evidence/generate_v2_mapped_cache_evidence.py && test -f tests/bodygraph/test_bg_resolve_v2_mapped_cache.py && test -f tests/bodygraph/test_hde_epic038_mapped_cache_smoke.py'
      ;;
    qa-17-po-017)
      qa_path_command='test -f tests/bodygraph/test_v2_mapped_cache.py && test -f tests/bodygraph/test_bg_resolve_v2_mapped_cache.py'
      ;;
    qa-18-po-018)
      qa_path_command='test -f tools/evidence/update_evidence_index.py && test -f tests/evidence/test_hde_epic038_release_sanity.py'
      ;;
    qa-19-po-019)
      qa_path_command='test -f tools/evidence/update_evidence_index.py && test -f tools/evidence/validate_evidence_paths.py && test -f ci/checks/check_mirror_schema.sh && test -f ci/checks/check_evidence_index_hash.sh && test -f ci/checks/check_final_lf.sh && test -f tools/evidence/orientation_demo.py && test -f artifacts/evidence_index.jsonl.sha256'
      ;;
    qa-20-po-020)
      qa_path_command='test -f tools/evidence/run_sanity_pipeline.py && test -f tests/evidence/test_hde_epic038_release_sanity.py'
      ;;
    qa-21-po-021)
      qa_path_command='test -f catalog/manifest.json && test -f scripts/release_id_recompute.py && test -f tools/evidence/build_release_attestation.py'
      ;;
    qa-22-po-022)
      qa_path_command='test -f tests/evidence/test_hde_epic038_release_sanity.py && test -f tests/ops/test_hde_epic038_ops03.py && test -d audit/ops/hde-epic038/ops-02 && test -d audit/ops/hde-epic038/ops-03'
      ;;
    qa-23-po-023)
      qa_path_command='test -f tools/evidence/generate_rails_gate_evidence.py && test -f tests/bodygraph/test_vendor_client.py && test -f tests/bodygraph/test_resolver_vendor.py && test -f tests/evidence/test_release_attestation.py && test -f tests/ops/test_hde_epic038_ops03.py'
      ;;
  esac

  mkdir -p "audit/qa/hde-epic038/checks/${qa_id}"
  : >"$qa_body"

  printf '%s\n' "[dependency preflight: initial] ${qa_profile_command}" >>"$qa_body"
  set +e
  SAFE_MODE="$qa_safe" ALLOW_NETWORK="$qa_network" APP_ENV="$qa_app" LC_ALL=C LANG=C TZ=UTC bash -c "$qa_profile_command" >>"$qa_body" 2>&1
  qa_profile_initial_rc=$?
  set -e
  printf '%s\n' "DEPENDENCY_INITIAL_EXIT_CODE=${qa_profile_initial_rc}" >>"$qa_body"
  qa_profile_final_rc="$qa_profile_initial_rc"

  if [ "$qa_profile_initial_rc" -ne 0 ]; then
    if [ "$qa_profile" = "C" ]; then
      printf '%s\n' "PROFILE_C_ACTION=${qa_c_action}" >>"$qa_body"
      case "$qa_c_action" in
        C2)
          qa_activation_record="bash .devcontainer/scripts/post-create.sh"
          printf '%s\n' "[activation action] ${qa_activation_record}" >>"$qa_body"
          set +e
          bash .devcontainer/scripts/post-create.sh >>"$qa_body" 2>&1
          qa_activation_rc=$?
          set -e
          printf '%s\n' "ACTIVATION_EXIT_CODE=${qa_activation_rc}" >>"$qa_body"
          ;;
        C3)
          qa_activation_record="python -m pip install 'setuptools>=68' wheel"
          printf '%s\n' "[activation action] ${qa_activation_record}" >>"$qa_body"
          set +e
          python -m pip install 'setuptools>=68' wheel >>"$qa_body" 2>&1
          qa_activation_rc=$?
          set -e
          printf '%s\n' "ACTIVATION_EXIT_CODE=${qa_activation_rc}" >>"$qa_body"
          ;;
        NONE)
          printf '%s\n' "[activation action] NONE" >>"$qa_body"
          ;;
        *)
          printf '%s\n' "[activation action] INVALID_SELECTION" >>"$qa_body"
          ;;
      esac
    else
      qa_activation_record="$qa_activation_command"
      printf '%s\n' "[activation action] ${qa_activation_record}" >>"$qa_body"
      set +e
      bash -c "$qa_activation_command" >>"$qa_body" 2>&1
      qa_activation_rc=$?
      set -e
      printf '%s\n' "ACTIVATION_EXIT_CODE=${qa_activation_rc}" >>"$qa_body"
    fi

    printf '%s\n' "[dependency preflight: final] ${qa_profile_command}" >>"$qa_body"
    set +e
    SAFE_MODE="$qa_safe" ALLOW_NETWORK="$qa_network" APP_ENV="$qa_app" LC_ALL=C LANG=C TZ=UTC bash -c "$qa_profile_command" >>"$qa_body" 2>&1
    qa_profile_final_rc=$?
    set -e

    if [ "$qa_profile" = "C" ] && [ "$qa_profile_final_rc" -ne 0 ] && [ "$qa_c_action" = "C2" ]; then
      printf '%s\n' "PROFILE_C_FOLLOWUP=${qa_c_followup}" >>"$qa_body"
      case "$qa_c_followup" in
        C3)
          qa_activation_record="${qa_activation_record}; python -m pip install 'setuptools>=68' wheel"
          printf '%s\n' "[activation action] python -m pip install 'setuptools>=68' wheel" >>"$qa_body"
          set +e
          python -m pip install 'setuptools>=68' wheel >>"$qa_body" 2>&1
          qa_activation_rc=$?
          set -e
          printf '%s\n' "ACTIVATION_EXIT_CODE=${qa_activation_rc}" >>"$qa_body"
          printf '%s\n' "[dependency preflight: final] ${qa_profile_command}" >>"$qa_body"
          set +e
          SAFE_MODE="$qa_safe" ALLOW_NETWORK="$qa_network" APP_ENV="$qa_app" LC_ALL=C LANG=C TZ=UTC bash -c "$qa_profile_command" >>"$qa_body" 2>&1
          qa_profile_final_rc=$?
          set -e
          ;;
        NONE)
          printf '%s\n' "[activation follow-up] NONE" >>"$qa_body"
          ;;
        *)
          printf '%s\n' "[activation follow-up] INVALID_SELECTION" >>"$qa_body"
          ;;
      esac
    fi
  else
    printf '%s\n' "[activation action] NONE" >>"$qa_body"
    printf '%s\n' "[dependency preflight: final] ${qa_profile_command}" >>"$qa_body"
  fi

  printf '%s\n' "DEPENDENCY_FINAL_EXIT_CODE=${qa_profile_final_rc}" >>"$qa_body"

  qa_dependency_rc="$qa_profile_final_rc"
  if [ "$qa_profile_final_rc" -eq 0 ] && [ -n "$qa_secondary_command" ]; then
    printf '%s\n' "[dependency preflight: value-safe] ${qa_secondary_command}" >>"$qa_body"
    set +e
    SAFE_MODE="$qa_safe" ALLOW_NETWORK="$qa_network" APP_ENV="$qa_app" LC_ALL=C LANG=C TZ=UTC bash -c "$qa_secondary_command" >>"$qa_body" 2>&1
    qa_secondary_rc=$?
    set -e
    printf '%s\n' "DEPENDENCY_VALUE_SAFE_EXIT_CODE=${qa_secondary_rc}" >>"$qa_body"
    qa_dependency_rc="$qa_secondary_rc"
  fi

  printf '%s\n' "[path preflight] ${qa_path_command}" >>"$qa_body"
  set +e
  SAFE_MODE="$qa_safe" ALLOW_NETWORK="$qa_network" APP_ENV="$qa_app" LC_ALL=C LANG=C TZ=UTC bash -c "$qa_path_command" >>"$qa_body" 2>&1
  qa_path_rc=$?
  set -e
  printf '%s\n' "PATH_PREFLIGHT_EXIT_CODE=${qa_path_rc}" >>"$qa_body"

  if [ "$qa_dependency_rc" -ne 0 ] || [ "$qa_path_rc" -ne 0 ]; then
    qa_status="TOOLING_BLOCKED"
    qa_rc=125
    printf '%s\n' "FINAL_READINESS=NOT_READY" >>"$qa_body"
  else
    printf '%s\n' "FINAL_READINESS=READY" >>"$qa_body"
    printf '%s\n' "[behavior command] ${qa_exact_command}" >>"$qa_body"
    set +e
    SAFE_MODE="$qa_safe" ALLOW_NETWORK="$qa_network" APP_ENV="$qa_app" LC_ALL=C LANG=C TZ=UTC bash -c "$qa_command" >>"$qa_body" 2>&1
    qa_rc=$?
    set -e
    printf '%s\n' "BEHAVIOR_EXIT_CODE=${qa_rc}" >>"$qa_body"

    if [ "$qa_rc" -eq 0 ]; then
      qa_status="PASS"
    elif [ "$qa_rc" -eq 125 ]; then
      qa_status="TOOLING_BLOCKED"
    elif [ "$qa_rc" -eq 126 ] || [ "$qa_rc" -eq 127 ]; then
      qa_status="FAIL_TOOLING"
    else
      printf '%s\n' "DECLARED_NONZERO_PREDICATE=${qa_declared_failure}" >>"$qa_body"
      printf '%s\n' "NONZERO_CAUSE_CLASSIFICATION=${qa_cause}" >>"$qa_body"
      case "$qa_cause" in
        FAIL_BEHAVIOR)
          qa_status="FAIL_BEHAVIOR"
          ;;
        FAIL_TOOLING)
          qa_status="FAIL_TOOLING"
          ;;
        *)
          qa_status="FAIL_TOOLING"
          qa_rc=74
          printf '%s\n' "NONZERO_CAUSE_CLASSIFICATION_INVALID" >>"$qa_body"
          ;;
      esac
    fi
  fi

  qa_effective_extra="$qa_extra"
  if [ "$qa_status" = "PASS" ]; then
    set +e
    python -c 'import json, pathlib, sys; missing=[p for p in json.loads(sys.argv[1]) if not pathlib.Path(p).is_file()]; print("MISSING_REQUIRED_ARTIFACTS="+",".join(missing)) if missing else None; raise SystemExit(1 if missing else 0)' "$qa_effective_extra" >>"$qa_body" 2>&1
    qa_artifact_rc=$?
    set -e
    if [ "$qa_artifact_rc" -ne 0 ]; then
      qa_status="FAIL_TOOLING"
      qa_rc=74
      qa_effective_extra='[]'
    fi
  else
    qa_effective_extra='[]'
  fi

  export CHECK_ID="$qa_id"
  export CHECK_NAME="$qa_name"
  export PASS_FAIL="$qa_status"
  export EXIT_CODE="$qa_rc"
  export COMMANDS_JSON="$(python -c 'import json,sys; profile,profile_command,initial_rc,activation,action,followup,secondary,final_rc,path_command,dependency_rc,path_rc,behavior=sys.argv[1:]; commands=[profile_command]; activation_commands=activation.split("; ") if activation else []; initial_failed=int(initial_rc)!=0; commands.extend(([activation_commands[0]] if profile=="C" and action in {"C2","C3"} and activation_commands else ([activation] if profile!="C" and activation else [])) if initial_failed else []); commands.extend([profile_command] if initial_failed else []); commands.extend([activation_commands[1],profile_command] if initial_failed and profile=="C" and action=="C2" and followup=="C3" and len(activation_commands)>1 else []); commands.extend([secondary] if int(final_rc)==0 and secondary else []); commands.append(path_command); commands.extend([behavior] if int(dependency_rc)==0 and int(path_rc)==0 else []); print(json.dumps(commands,separators=(",",":")))' "$qa_profile" "$qa_profile_command" "$qa_profile_initial_rc" "$qa_activation_record" "$qa_c_action" "$qa_c_followup" "$qa_secondary_command" "$qa_profile_final_rc" "$qa_path_command" "$qa_dependency_rc" "$qa_path_rc" "$qa_exact_command")"
  export ARTIFACTS_JSON="$(python -c 'import json,sys; extra=json.loads(sys.argv[1]); print(json.dumps([sys.argv[2],*extra], separators=(",",":")))' "$qa_effective_extra" "$qa_log")"
  export PF_REFS_JSON="$qa_refs"
  export COMMAND_PROVENANCE="Copy/paste from plan"
  export INTENDED_TOKENS_JSON='[]'
  export CLAIMED_TOKENS_JSON='[]'
  export SAFE_MODE="$qa_safe"
  export ALLOW_NETWORK="$qa_network"
  export APP_ENV="$qa_app"
  export LC_ALL="C"
  export LANG="C"
  export TZ="UTC"
  write_pf27_header >"$qa_header"
  {
    cat "$qa_header"
    printf '\n'
    cat "$qa_body"
  } >"$qa_log"
  rm -f "$qa_header" "$qa_body"
  printf '%s %s\n' "$qa_status" "$qa_log"
  return 0
}
```

Bootstrap verification, Command 3: `type write_pf27_header >/dev/null 2>&1 && type qa_run >/dev/null 2>&1`

Expected result: exit code `0`.

### Mandatory Step-0 artifacts

#### CHECK qa-00-step-0-discovery: Step-0 Discovery

Goal: Create the stable QA root, mechanically capture the current production-factory route posture, and create the required Doc Delta pair without overwriting proof-bearing content.

Rails: closed. Required dependencies: Profile B. Preflight check: Command B1. If missing, activation/install action: Command B2. If still unavailable: stop; Step 0 is `TOOLING_BLOCKED` and no later check may run. Preconditions: repository root basename must be `glow-hdengine-v2`. Tokens: `[]` intended; `[]` claimed.

PO actions:

1. Define Bootstrap Commands 1 and 2\.  
2. Run Bootstrap verification, Command 3\.  
3. Define the mechanically generated Step-0 command.  
4. Execute Step-0 Command 3 through `qa_run`; the wrapper captures Command B1, any Command B2 activation, repeated Command B1, and Command 1 before behavior evaluation.  
5. If the wrapper records `FINAL_READINESS=NOT_READY`, stop; Step 0 is `TOOLING_BLOCKED` and no later check may run.  
6. Verify the header and Doc Delta pair.

Command 1: `test "$(basename "$(git rev-parse --show-toplevel)")" = "glow-hdengine-v2"`

Command 2 — define the Step-0 command:

```
qa_step0_command=$(cat <<'STEP0SH'
python - <<'STEP0PY'
import json
from pathlib import Path
from adapter.factory import create_app

required = {
    ("/reader", "GET"),
    ("/internal/version", "GET"),
    ("/api/compat/v1", "POST"),
}
actual = {
    (rule.rule, method)
    for rule in create_app().url_map.iter_rules()
    for method in rule.methods
}
missing = sorted(required - actual)

paths = [
    Path("audit/docdeltas/hde-epic038_doc_deltas.md"),
    Path("audit/qa/hde-epic038/00_meta/doc_deltas.md"),
]
existing = [path.read_bytes() if path.exists() else b"" for path in paths]
if existing[0].strip() and existing[1].strip() and existing[0] != existing[1]:
    raise SystemExit("DOC_DELTA_DIVERGENCE")

retained = existing[0] if existing[0].strip() else existing[1]
if retained.strip():
    data = retained
    delta_posture = "preserved_existing"
else:
    lines = [
        "# HDE-EPIC038 QA Doc Deltas",
        "",
        "## BLOCKERS",
    ]
    if ("/api/compat/v1", "POST") in missing:
        lines.append(
            "- DOC-BLOCKER-001: The production and documented startup factory omits the existing internal compatibility blueprint mounted by adjacent factories. This does not authorize a new or public surface."
        )
    else:
        lines.append("- None identified by Step-0 route discovery.")
    lines.extend(
        [
            "",
            "## CAVEATS",
            "- DOC-CAVEAT-001: Implementation, repository, release, and operational evidence do not independently establish Live QA acceptance or epic closeout.",
        ]
    )
    data = ("\n".join(lines) + "\n").encode("utf-8")
    delta_posture = "created"

for path in paths:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and path.read_bytes().strip() and path.read_bytes() != data:
        raise SystemExit("DOC_DELTA_OVERWRITE_REFUSED")
    path.write_bytes(data)

if paths[0].read_bytes() != paths[1].read_bytes():
    raise SystemExit("DOC_DELTA_PAIR_MISMATCH")

print(
    json.dumps(
        {
            "epic_id": "HDE-EPIC038",
            "qa_root": "audit/qa/hde-epic038/",
            "repository": "glow-hdengine-v2",
            "production_factory_required_routes": sorted(required),
            "production_factory_missing_routes": missing,
            "doc_delta_posture": delta_posture,
            "future_check_artifacts": "NOT RUN",
        },
        sort_keys=True,
    )
)
STEP0PY
STEP0SH
)
```

Command 3: `qa_run qa-00-step-0-discovery "Step-0 Discovery" 1 0 dev TOOLING_BLOCKED '["HDE Build Notes","Canon Plan Templates","HDE User Guide"]' '["audit/docdeltas/hde-epic038_doc_deltas.md","audit/qa/hde-epic038/00_meta/doc_deltas.md"]' "$qa_step0_command"`

Command 4: `head -n 1 audit/qa/hde-epic038/checks/qa-00-step-0-discovery/primary.log`

Command 5: `python -c 'from pathlib import Path; a=Path("audit/docdeltas/hde-epic038_doc_deltas.md").read_bytes(); b=Path("audit/qa/hde-epic038/00_meta/doc_deltas.md").read_bytes(); raise SystemExit(0 if a and a==b else 1)'`

What to look for:

* Command 3 reports `PASS`.  
* The discovery body reports the exact production-factory missing-route set.  
* The two Doc Delta files are nonempty and byte-identical.  
* Existing proof-bearing Doc Delta content is preserved.

Required deliverables:

* `audit/qa/hde-epic038/checks/qa-00-step-0-discovery/primary.log` — QA-created discovery artifact.  
* `audit/docdeltas/hde-epic038_doc_deltas.md` — PF27-governed staging surface.  
* `audit/qa/hde-epic038/00_meta/doc_deltas.md` — QA-created authoritative epic surface.

PASS: all three files exist, the header is valid with exit code `0`, the Doc Delta pair is byte-identical, and the discovery body contains the mechanically observed route posture. FAIL\_BEHAVIOR: route divergence is not a Step-0 failure; it is recorded for `qa-06-po-006`. FAIL\_TOOLING: discovery execution or evidence capture fails after dependencies passed. TOOLING\_BLOCKED: required dependencies, repository root, or safe Doc Delta preservation cannot be established. Initial state: `NOT RUN`.

#### Step-0B — Doc Delta Capture (mechanical; runbook self-honesty)

Step 0 above creates or preserves the required two-surface pair. It never replaces proof-bearing content with an empty scaffold. Current-run route discovery creates stable blocker ID `DOC-BLOCKER-001` only when it reports `POST /api/compat/v1` absent from the production-selected factory; otherwise Step 0 records no route blocker.

No implementation Moon Loop is authorized. A command, path, or dependency defect requires a plan change; a behavior defect requires an implementation change.

#### Step-0C — Prod handshake (identity-only) when target is prod-like

Not applicable. This plan targets Codespaces dev behavior and makes no Codespaces-to-production handshake claim.

### Runbook Check Matrix

| Check ID | Goal | Rails | Required evidence | Initial state |
| :---- | :---- | :---- | :---- | :---- |
| qa-00-step-0-discovery | Discovery and Doc Delta capture | Closed | `primary.log` plus Doc Delta pair | NOT RUN |
| qa-01-po-001 | Independent QA/closure boundaries | Closed | `primary.log` | NOT RUN |
| qa-02-po-002 | Single immutable identity | Closed | `primary.log` | NOT RUN |
| qa-03-po-003 | Deterministic, presence-only environment | Closed | `primary.log` | NOT RUN |
| qa-04-po-004 | Canonical cross-surface output | Closed | `primary.log` | NOT RUN |
| qa-05-po-005 | Public success transport contract | Closed | `primary.log` | NOT RUN |
| qa-06-po-006 | Production/local entrypoint surface set | Closed | `primary.log` | NOT RUN |
| qa-07-po-007 | Default refusal and bounded simulation | Closed with fixture-open subprocess | `primary.log` | NOT RUN |
| qa-08-po-008 | Bounded live-vendor proof | Open, conditional | `primary.log`; conditional governed proof | NOT RUN |
| qa-09-po-009 | Source-neutral BodyGraph projection | Closed | `primary.log` | NOT RUN |
| qa-10-po-010 | Effect isolation and vendor policy | Closed | `primary.log` | NOT RUN |
| qa-11-po-011 | Current architecture classification | Closed | `primary.log` | NOT RUN |
| qa-12-po-012 | Direct-only database transport | Closed | `primary.log` | NOT RUN |
| qa-13-po-013 | Historical alternate-transport integrity | Closed | `primary.log` | NOT RUN |
| qa-14-po-014 | Strict shared DDL identity projection | Closed | `primary.log` | NOT RUN |
| qa-15-po-015 | Retained operational DB controls | Closed; no OPS | `primary.log` | NOT RUN |
| qa-16-po-016 | Authorized mapped-persistence boundaries | Closed, hermetic | `primary.log` | NOT RUN |
| qa-17-po-017 | Mapped-persistence identity and idempotence | Closed, hermetic | `primary.log` | NOT RUN |
| qa-18-po-018 | Canonical evidence ownership | Closed | `primary.log` | NOT RUN |
| qa-19-po-019 | Evidence mirror and topology coherence | Closed | `primary.log` | NOT RUN |
| qa-20-po-020 | Nineteen-stage integrated chain | Closed | `primary.log`; integrated validation log | NOT RUN |
| qa-21-po-021 | Release identity and external attestation | Closed | `primary.log`; transient external workspace | NOT RUN |
| qa-22-po-022 | Immutable admitted operational captures | Closed; no OPS | `primary.log` | NOT RUN |
| qa-23-po-023 | Secret and raw-payload exclusion | Closed | `primary.log` | NOT RUN |

### Check Blocks

Run checks in matrix order. Invoke each supplied `qa_run` command directly. For every check, the wrapper captures the named dependency-profile preflight, any permitted activation action, the final dependency result, the check’s path preflight, and `FINAL_READINESS=READY` or `FINAL_READINESS=NOT_READY` before behavior evaluation. A not-ready result is recorded as `TOOLING_BLOCKED`, and the behavior command does not execute.

#### CHECK qa-01-po-001: PO-001

Goal: Live QA must independently establish each affected functional truth without treating implementation records, operational activity, repository presence, or release validation as acceptance, checklist movement, deployment, migration, or epic closure.

Rails: closed. Required dependencies: Profile A. Preflight check: Command A1 and the path preflight below. Path preflight: `test -f tests/evidence/test_hde_epic038_release_sanity.py` If missing, activation/install action: Command A2 for packages; none proven for a missing repository locus. If still unavailable: use the `TOOLING_BLOCKED` command. Preconditions: Step 0 completed; no OPS command is executed. PF anchors: HDE Build Notes; Canon Plan Templates. Tokens: `[]` intended; `[]` claimed.

PO actions:

1. Run the behavior command through `qa_run`; let the wrapper capture dependency readiness, any permitted activation, and the path preflight before behavior evaluation.  
2. Run the behavior command.  
3. Read the JSON header and test output.  
4. Keep QA, OPS, release, acceptance, PF09, and closeout conclusions separate.

TOOLING\_BLOCKED command: `qa_run qa-01-po-001 PO-001 1 0 dev TOOLING_BLOCKED '["HDE Build Notes","Canon Plan Templates"]' '[]' "printf '%s\n' 'DEPENDENCIES_OR_REPO_LOCUS_UNAVAILABLE'; exit 125"`

Behavior command: `qa_run qa-01-po-001 PO-001 1 0 dev FAIL_BEHAVIOR '["HDE Build Notes","Canon Plan Templates"]' '[]' "python -m pytest -q tests/evidence/test_hde_epic038_release_sanity.py::test_pre_ops_pipeline_consumes_prebuilt_artifacts_without_repairing_them tests/evidence/test_hde_epic038_release_sanity.py::test_current_release_validators_do_not_rewrite_frozen_captures tests/evidence/test_hde_epic038_release_sanity.py::test_tracked_ops03_fixture_is_validated_without_execution"`

Evidence command: `head -n 1 audit/qa/hde-epic038/checks/qa-01-po-001/primary.log`

What to look for: three passing tests; no OPS execution; no frozen-capture rewrite; no evidence repair or closure inference. Required deliverable: `audit/qa/hde-epic038/checks/qa-01-po-001/primary.log` — QA-created. PASS: header status PASS, exit code `0`, and all three functional separation checks pass. FAIL\_BEHAVIOR: a separation, no-rerun, or no-rewrite assertion fails. FAIL\_TOOLING: pytest or capture machinery fails without reaching assertions. TOOLING\_BLOCKED: dependencies or the test locus remain unavailable. Initial state: `NOT RUN`.

#### CHECK qa-02-po-002: PO-002

Goal: One immutable and validated service identity must remain consistent across public, internal, command-line, runtime, release, and evidence consumers without a second production authority or request-time fallback.

Rails: closed. Required dependencies: Profile A. Preflight check: Command A1. Path preflight: `test -f scripts/release_id_recompute.py && test -f tests/runtime/test_identity.py && test -f tests/cli/test_showcompat_parity_and_identity.py && test -f tests/transport/test_internal_version_contract.py` If missing, activation/install action: Command A2 for packages; none for missing loci. If still unavailable: use the blocker command. PF anchors: HDE Build Notes; Canon Plan Templates. Tokens: `[]`; `[]`.

TOOLING\_BLOCKED command: `qa_run qa-02-po-002 PO-002 1 0 dev TOOLING_BLOCKED '["HDE Build Notes","Canon Plan Templates"]' '[]' "printf '%s\n' 'IDENTITY_DEPENDENCY_UNAVAILABLE'; exit 125"`

Behavior command: `qa_run qa-02-po-002 PO-002 1 0 dev FAIL_BEHAVIOR '["HDE Build Notes","Canon Plan Templates"]' '[]' "python scripts/release_id_recompute.py --check-manifest-only && python -m pytest -q tests/runtime/test_identity.py tests/cli/test_showcompat_parity_and_identity.py tests/transport/test_internal_version_contract.py"`

Evidence command: `head -n 1 audit/qa/hde-epic038/checks/qa-02-po-002/primary.log`

What to look for: canonical manifest validation; runtime, CLI, public, and internal identity agreement; no environment or evidence fallback. Required deliverable: `audit/qa/hde-epic038/checks/qa-02-po-002/primary.log`. PASS: both command stages exit `0` and identity tests establish one authority. FAIL\_BEHAVIOR: identity differs, manifest bytes are noncanonical, or a fallback authority is observed. FAIL\_TOOLING: the runner fails before contract evaluation. TOOLING\_BLOCKED: readiness remains unavailable. Initial state: `NOT RUN`.

#### CHECK qa-03-po-003: PO-003

Goal: Environment posture must remain deterministic, versioned, presence-only, locale-and-time pinned, and incapable of revealing configuration values.

Rails: closed. Required dependencies: Profile B. Preflight check: Command B1. Path preflight: `test -f ci/checks/check_env_pins.sh && test -f tools/evidence/generate_env_matrix_snapshot.py && test -f artifacts/runtime/env_matrix.snapshot.json` If missing, activation/install action: Command B2 for packages; none for missing loci or system utilities. If still unavailable: use the blocker command. PF anchors: HDE Build Notes; Canon Plan Templates. Tokens: `[]`; `[]`.

TOOLING\_BLOCKED command: `qa_run qa-03-po-003 PO-003 1 0 dev TOOLING_BLOCKED '["HDE Build Notes","Canon Plan Templates"]' '[]' "printf '%s\n' 'ENVIRONMENT_CHECK_DEPENDENCY_UNAVAILABLE'; exit 125"`

Behavior command: `qa_run qa-03-po-003 PO-003 1 0 dev FAIL_BEHAVIOR '["HDE Build Notes","Canon Plan Templates"]' '[]' "bash ci/checks/check_env_pins.sh && python tools/evidence/generate_env_matrix_snapshot.py --check"`

Evidence command: `head -n 1 audit/qa/hde-epic038/checks/qa-03-po-003/primary.log`

What to look for: `[env-pins] OK`, versioned snapshot agreement, presence labels only, and no configuration value output. Required deliverable: `audit/qa/hde-epic038/checks/qa-03-po-003/primary.log`. PASS: both checks exit `0`; pins are C/C/UTC and rails 1/0; output contains no secret values. FAIL\_BEHAVIOR: pin, schema, presence-only, or value-safety contract fails. FAIL\_TOOLING: shell or snapshot checker fails mechanically. TOOLING\_BLOCKED: dependencies remain missing. Initial state: `NOT RUN`.

#### CHECK qa-04-po-004: PO-004

Goal: Governed output must remain canonically equivalent across public and command-line interfaces, reversed input order, independent repeated evaluation, source recomputation, and canonical re-emission.

SOURCE EXCERPT (verbatim): An older repository-host result conflicts with the historical success statement, so current proof must stand independently of that history.

Rails: closed; fixture-backed open-rails proof performs zero vendor calls. Required dependencies: Profile A. Preflight check: Command A1. Path preflight: `test -f tools/evidence/run_canonical_json_gate.py && test -f tools/evidence/generate_open_rails_abba_proof.py && test -f tests/cli/test_cli_canonical_bytes.py && test -f tests/cli/test_showcompat_parity_and_identity.py` If missing, activation/install action: Command A2. If still unavailable: use the blocker command. PF anchors: HDE Build Notes; Canon Plan Templates. Tokens: `[]`; `[]`.

TOOLING\_BLOCKED command: `qa_run qa-04-po-004 PO-004 1 0 dev TOOLING_BLOCKED '["HDE Build Notes","Canon Plan Templates"]' '[]' "printf '%s\n' 'CANONICAL_OUTPUT_DEPENDENCY_UNAVAILABLE'; exit 125"`

Behavior command: `qa_run qa-04-po-004 PO-004 1 0 dev FAIL_BEHAVIOR '["HDE Build Notes","Canon Plan Templates"]' '[]' "python tools/evidence/run_canonical_json_gate.py --check-only && python tools/evidence/generate_open_rails_abba_proof.py --check-current && python -m pytest -q tests/cli/test_cli_canonical_bytes.py tests/cli/test_showcompat_parity_and_identity.py"`

Evidence command: `head -n 1 audit/qa/hde-epic038/checks/qa-04-po-004/primary.log`

What to look for: canonical JSON PASS, fixture AB/BA and repeated-run equality, zero vendor calls, CLI/public parity. Required deliverable: `audit/qa/hde-epic038/checks/qa-04-po-004/primary.log`. PASS: every check exits `0` and current proof independently establishes the required equivalences. FAIL\_BEHAVIOR: any byte, ordering, repeat, recomputation, or re-emission predicate diverges. FAIL\_TOOLING: a checker cannot execute after preflight. TOOLING\_BLOCKED: a required locus remains unavailable. Initial state: `NOT RUN`.

#### CHECK qa-05-po-005: PO-005

Goal: The uniquely designated public success surface must preserve governed successful-read, metadata-only, unchanged-resource, error, caching, entity-metadata, length, and equivalent-encoding behavior while internal and operational surfaces remain outside that proof class.

Rails: closed. Required dependencies: Profile A. Preflight check: Command A1. Path preflight: `test -f tools/evidence/generate_a7_transport_proofs.py && test -f tests/http/test_reader_a7_transport.py && test -f tests/http/test_endpoint_catalog.py && test -f docs/ENDPOINTS_CATALOG.json` If missing, activation/install action: Command A2. If still unavailable: use the blocker command. PF anchors: HDE Build Notes; Canon Plan Templates. Tokens: `[]`; `[]`.

TOOLING\_BLOCKED command: `qa_run qa-05-po-005 PO-005 1 0 dev TOOLING_BLOCKED '["HDE Build Notes","Canon Plan Templates"]' '[]' "printf '%s\n' 'TRANSPORT_PROOF_DEPENDENCY_UNAVAILABLE'; exit 125"`

Behavior command: `qa_run qa-05-po-005 PO-005 1 0 dev FAIL_BEHAVIOR '["HDE Build Notes","Canon Plan Templates"]' '[]' "python tools/evidence/generate_a7_transport_proofs.py --check && python -m pytest -q tests/http/test_reader_a7_transport.py tests/http/test_endpoint_catalog.py"`

Evidence command: `head -n 1 audit/qa/hde-epic038/checks/qa-05-po-005/primary.log`

What to look for: unique `GET /reader` designation; GET, HEAD, 304, error, cache, ETag, length, identity/gzip/brotli equivalence. Required deliverable: `audit/qa/hde-epic038/checks/qa-05-po-005/primary.log`. PASS: generator check and HTTP/catalog tests pass. FAIL\_BEHAVIOR: any transport predicate or success-surface classification fails. FAIL\_TOOLING: the generator or tests fail mechanically. TOOLING\_BLOCKED: dependencies or loci remain unavailable. Initial state: `NOT RUN`.

#### **CHECK qa-06-po-006: PO-006**

Goal: The canonical production and documented local application entry point must expose every existing public and internal surface assigned to that deployment role while preserving their distinct proof meanings.

SOURCE EXCERPT (verbatim): All implementation and remediation requirements are satisfied in the current repository state.

REPO VALIDATION NOTE: `Procfile` and `scripts/start_web.sh` select `adapter.factory:create_app()`. Current `adapter/factory.py` registers both the primary blueprint and the existing `compat_blueprint`. The compatibility prefix remains `/api/compat/v1` and is an internal surface, not a new public contract.

Rails: closed. Required dependencies: Profile A. Preflight check: Command A1. Path preflight: `test -f Procfile && test -f scripts/start_web.sh && test -f adapter/factory.py && test -f adapter/http_reader.py && test -f adapter/wsgi.py && test -f engine/http/compat_handler.py && test -f tests/http/test_compat_endpoint_contract.py && test -f tests/adapter/test_compat_http_dev.py && test -f tests/adapter/test_compat_http_parity.py` If missing, activation/install action: Command A2 for packages; none for missing loci. If still unavailable: use the blocker command. PF anchors: HDE Build Notes; Canon Plan Templates; HDE User Guide. Tokens: `[]`; `[]`.

TOOLING\_BLOCKED command: `qa_run qa-06-po-006 PO-006 1 0 dev TOOLING_BLOCKED '["HDE Build Notes","Canon Plan Templates","HDE User Guide"]' '[]' "printf '%s\n' 'ENTRYPOINT_PROOF_DEPENDENCY_UNAVAILABLE'; exit 125"`

Behavior command: `qa_run qa-06-po-006 PO-006 1 0 dev FAIL_BEHAVIOR '["HDE Build Notes","Canon Plan Templates","HDE User Guide"]' '[]' "python -c 'from adapter.factory import create_app; required={(\"/reader\",\"GET\"),(\"/internal/version\",\"GET\"),(\"/api/compat/v1\",\"POST\")}; actual={(r.rule,m) for r in create_app().url_map.iter_rules() for m in r.methods}; missing=sorted(required-actual); print({\"missing\":missing}); raise SystemExit(1 if missing else 0)' && python -m pytest -q tests/http/test_compat_endpoint_contract.py tests/adapter/test_compat_http_dev.py tests/adapter/test_compat_http_parity.py"`

Evidence command: `head -n 1 audit/qa/hde-epic038/checks/qa-06-po-006/primary.log`

What to look for: an empty `missing` array and a passing complete compatibility suite covering endpoint-contract, development, and parity behavior. Required deliverable: `audit/qa/hde-epic038/checks/qa-06-po-006/primary.log`. PASS: the production-selected factory contains all three assigned surfaces and all three compatibility test files pass, establishing the accepted namespace, environment, method, subpath, error-contract, development, and parity behavior. FAIL\_BEHAVIOR: the route assertion reports a missing assigned surface or any endpoint-contract, development, or parity assertion fails. FAIL\_TOOLING: safe route introspection or test execution cannot proceed after preflight. TOOLING\_BLOCKED: dependencies or loci are unavailable. A missing assigned route observed during the future QA run is `FAIL_BEHAVIOR`; no missing route is presumed before execution. Initial state: `NOT RUN`.

#### CHECK qa-07-po-007: PO-007

Goal: The default safety posture must refuse external access before outbound activity, while permitted non-live validation remains deterministic, bounded, simulated, value-safe, and limited to eligible transient retries.

Rails: closed parent; the governed fixture jobs may set their pinned rails internally but forbid live calls. Required dependencies: Profile A. Preflight check: Command A1. Path preflight: `test -f ci/checks/run_rails_job_definitions.py && test -f ci/jobs/rails_closed_refusal.yml && test -f ci/jobs/rails_open_conformance.yml && test -f ci/jobs/logs_keys_only_redaction.yml` If missing, activation/install action: Command A2. If still unavailable: use the blocker command. PF anchors: HDE Build Notes; Canon Plan Templates. Tokens: `[]`; `[]`.

TOOLING\_BLOCKED command: `qa_run qa-07-po-007 PO-007 1 0 dev TOOLING_BLOCKED '["HDE Build Notes","Canon Plan Templates"]' '[]' "printf '%s\n' 'RAILS_VALIDATOR_DEPENDENCY_UNAVAILABLE'; exit 125"`

Behavior command: `qa_run qa-07-po-007 PO-007 1 0 dev FAIL_BEHAVIOR '["HDE Build Notes","Canon Plan Templates"]' '[]' "python ci/checks/run_rails_job_definitions.py ci/jobs/rails_closed_refusal.yml ci/jobs/rails_open_conformance.yml ci/jobs/logs_keys_only_redaction.yml"`

Evidence command: `head -n 1 audit/qa/hde-epic038/checks/qa-07-po-007/primary.log`

What to look for: refusal before I/O, mocked bounded retry, deterministic fixtures, keys-only redaction, and zero live-vendor calls. Required deliverable: `audit/qa/hde-epic038/checks/qa-07-po-007/primary.log`. PASS: all three required governed job definitions execute successfully without a live call. FAIL\_BEHAVIOR: refusal ordering, retry bounds, required identity coverage, or value-safety assertions fail. FAIL\_TOOLING: the job runner fails mechanically. TOOLING\_BLOCKED: dependencies remain unavailable. Initial state: `NOT RUN`.

#### **CHECK qa-08-po-008: PO-008**

Goal: Any live-vendor proof claim must remain expressly authorized, narrowly bounded, same-input, independently validated, raw-payload-free, non-credential-bearing, and incapable of conferring recurring authority.

SOURCE EXCERPT (verbatim): The historical proof did not independently establish its nonproduction environment and cannot establish broad vendor-version conformance.

PO EXECUTION NOTE (2026-07-27): The PO confirmed that the exact canonical HumanDesignAPI v2 base is the only available vendor endpoint and that no separately marked staging, sandbox, development, or nonproduction endpoint exists or is expected. The PO freshly authorized this one bounded two-request generation event; this decision does not confer recurring authority. The PO also approved the narrow in-place producer/bootstrap correction recorded above and overrode the supplied fixed-HEAD precondition as a planning defect.

Rails: open only for the authorized generation invocation; the independent generation check and post-route finalization run under closed rails. Required dependencies: Profile D. Generation preflight uses Command A1 and Command D1 plus explicit human confirmation of fresh authorization. Closed finalization uses Command A1 and the path preflight but skips D1, requires no endpoint or credentials, and cannot execute vendor I/O. Path preflight: `test -f tools/evidence/generate_open_rails_abba_proof.py && test -f tools/evidence/update_evidence_index.py` If missing, activation/install action: Command A2 for packages; none for authorization, secrets, exact target classification, routing provenance, or missing loci. If still unavailable: record `TOOLING_BLOCKED`; make no call. PF anchors: HDE Build Notes; Canon Plan Templates. Tokens: `[]`; `[]`.

PO actions:

1. Obtain fresh one-time PO authorization.  
2. Declare `QA08_AUTHORIZATION_CONFIRMATION=CONFIRMED` and generate a unique unprinted `QA08_PO_EVENT_RECEIPT` only for the current authorization event.
3. Declare `QA_NONZERO_CAUSE` as `FAIL_BEHAVIOR` or `FAIL_TOOLING` for any other nonzero result.  
4. Leave `QA08_ROUTING_RECEIPT` and `QA08_PRE_ROUTING_RECEIPT` unset during generation.  
5. Run the generation command once; `qa_run` captures Command A1, any permitted Command A2 activation, Command D1, the path preflight, authorization provenance, and the actual generation command.  
6. Do not provide personal input variables; use the built-in synthetic defaults. Do not retry a failed live command in the same authorization event.  
7. Clear `QA08_AUTHORIZATION_CONFIRMATION` and `QA08_PO_EVENT_RECEIPT` immediately after the generation invocation so neither can confer recurring authority.
8. When the producer and independent closed-rails artifact check succeed, generation records `TOOLING_BLOCKED` with routing pending. Capture a durable pre-routing receipt for that generation record before routing.  
9. Route the current generated artifact and its required sole-owner companion refresh through the approved PR posture. No QA process remains open during that transition.  
10. After the routed refresh is present in the execution workspace, declare `QA08_ROUTING_RECEIPT` as the approved non-`NONE` PR routing receipt and declare `QA08_PRE_ROUTING_RECEIPT` as the preserved non-`NONE` generation receipt.  
11. Run the finalization command once. It validates the routed current artifact and companion graph under closed rails without regenerating either.  
12. Clear `QA08_ROUTING_RECEIPT` and `QA08_PRE_ROUTING_RECEIPT` immediately after finalization.  
13. Inspect the final current-run log, the governed proof, the separately labeled routing proof, the preserved pre-routing receipt, and the separately labeled behavioral proof.

TOOLING\_BLOCKED command: `qa_run qa-08-po-008 PO-008 1 0 dev TOOLING_BLOCKED '["HDE Build Notes","Canon Plan Templates"]' '[]' "printf '%s\n' 'FRESH_AUTHORIZATION_OR_OPEN_RAILS_READINESS_UNAVAILABLE'; exit 125"`

Generation command: `qa_run qa-08-po-008 PO-008 0 1 dev FAIL_BEHAVIOR '["HDE Build Notes","Canon Plan Templates"]' '[]' "qa_authorization_confirmation=\"\${QA08_AUTHORIZATION_CONFIRMATION:-}\"; qa_po_event_receipt=\"\${QA08_PO_EVENT_RECEIPT:-}\"; if [ \"\$qa_authorization_confirmation\" != 'CONFIRMED' ] || [ -z \"\$qa_po_event_receipt\" ]; then printf '%s\n' 'FRESH_AUTHORIZATION_UNAVAILABLE'; exit 125; fi; printf '%s\n' 'HEAD_PIN_OVERRIDE=QA_HEAD_INDEPENDENT' 'FRESH_PO_AUTHORIZATION_CONFIRMED_BY_EXECUTING_PO' 'GENERATION_PHASE=AUTHORIZED_LIVE_PRODUCER'; python tools/evidence/generate_open_rails_abba_proof.py --live || exit \$?; env -u HD_API_KEY -u GEO_API_KEY -u HD_API_BASE_URL -u HDAPI_BASE_URL -u QA08_AUTHORIZATION_CONFIRMATION -u QA08_PO_EVENT_RECEIPT SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC python tools/evidence/generate_open_rails_abba_proof.py --live --check || exit \$?; printf '%s\n' 'BEHAVIOR_PROOF=LIVE_PRODUCER_AND_INDEPENDENT_CHECK' 'ROUTING_STATUS=PR_PENDING'; exit 125"`

Finalization command: `qa_run qa-08-po-008 PO-008 1 0 dev FAIL_BEHAVIOR '["HDE Build Notes","Canon Plan Templates"]' '["audit/gates/determinism/open_rails_vendor_abba.json"]' "qa_routing_receipt=\"\${QA08_ROUTING_RECEIPT:-}\"; qa_pre_routing_receipt=\"\${QA08_PRE_ROUTING_RECEIPT:-}\"; if [ -z \"\$qa_routing_receipt\" ] || [ \"\$qa_routing_receipt\" = 'NONE' ] || [ -z \"\$qa_pre_routing_receipt\" ] || [ \"\$qa_pre_routing_receipt\" = 'NONE' ]; then printf '%s\n' 'ROUTED_CURRENT_ARTIFACT_PROVENANCE_UNAVAILABLE'; exit 125; fi; printf '%s\n' 'ROUTING_TYPE=PR' \"ROUTING_PROOF=\$qa_routing_receipt\" \"PRE_ROUTING_RECEIPT=\$qa_pre_routing_receipt\"; env -u HD_API_KEY -u GEO_API_KEY -u HD_API_BASE_URL -u HDAPI_BASE_URL -u QA08_AUTHORIZATION_CONFIRMATION -u QA08_PO_EVENT_RECEIPT python tools/evidence/generate_open_rails_abba_proof.py --live --check || exit \$?; env -u HD_API_KEY -u GEO_API_KEY -u HD_API_BASE_URL -u HDAPI_BASE_URL -u QA08_AUTHORIZATION_CONFIRMATION -u QA08_PO_EVENT_RECEIPT python tools/evidence/update_evidence_index.py --check || exit \$?; printf '%s\n' 'BEHAVIOR_PROOF=CLOSED_RAILS_CURRENT_ARTIFACT_AND_COMPANION_VALIDATION'"`

Evidence command: `head -n 1 audit/qa/hde-epic038/checks/qa-08-po-008/primary.log`

What to look for during generation: two requests attempted and completed, bounded attempts, same normalized inputs, AB/BA equality, repeated equality, canonical single-LF output, redacted target, no raw payload or secret value, and `ROUTING_STATUS=PR_PENDING`. What to look for during finalization: closed rails, non-`NONE` routing and pre-routing receipts, successful current-artifact validation, and successful sole-owner companion check. Conditional deliverable: `audit/gates/determinism/open_rails_vendor_abba.json` is required only after the authorized producer succeeds. Required deliverable: `audit/qa/hde-epic038/checks/qa-08-po-008/primary.log`.

PASS is available only from post-route finalization: current authorization was recorded by generation, the producer and independent check succeeded, the pre-routing generation receipt is preserved, the routed current artifact and companion-refresh receipt is recorded, both closed-rails finalization checks exit `0`, and routing proof remains distinct from behavioral proof.

FAIL\_BEHAVIOR: an authorized interaction or post-route validation occurs but a bound, safety, canonicalization, same-input, artifact, or companion predicate fails. FAIL\_TOOLING: execution machinery fails after readiness passed and before a behavioral conclusion can be trusted. TOOLING\_BLOCKED: authorization, exact canonical-target classification, secrets, packages, loci, pre-routing receipt, routed refresh, or routing receipt is unavailable; successful generation awaiting routing remains `TOOLING_BLOCKED`. Initial state: `NOT RUN`.

#### CHECK qa-09-po-009: PO-009

Goal: Distinct supported source representations must converge through one pure source-neutral BodyGraph projection and one canonical output authority, producing equivalent output while rejecting meaningful divergence.

Rails: closed. Required dependencies: Profile A. Preflight check: Command A1. Path preflight: `test -f tests/bodygraph/test_projection.py && test -f tools/evidence/generate_bodygraph_policy_proofs.py` If missing, activation/install action: Command A2. If still unavailable: use the blocker command. PF anchors: HDE Build Notes; Canon Plan Templates. Tokens: `[]`; `[]`.

TOOLING\_BLOCKED command: `qa_run qa-09-po-009 PO-009 1 0 dev TOOLING_BLOCKED '["HDE Build Notes","Canon Plan Templates"]' '[]' "printf '%s\n' 'BODYGRAPH_PROJECTION_DEPENDENCY_UNAVAILABLE'; exit 125"`

Behavior command: `qa_run qa-09-po-009 PO-009 1 0 dev FAIL_BEHAVIOR '["HDE Build Notes","Canon Plan Templates"]' '[]' "python -m pytest -q tests/bodygraph/test_projection.py && python tools/evidence/generate_bodygraph_policy_proofs.py --check"`

Evidence command: `head -n 1 audit/qa/hde-epic038/checks/qa-09-po-009/primary.log`

What to look for: pure projection, DB/vendor fixture convergence, repeated stability, and negative-control divergence rejection. Required deliverable: `audit/qa/hde-epic038/checks/qa-09-po-009/primary.log`. PASS: tests and check-only proof validation pass. FAIL\_BEHAVIOR: projection neutrality, equivalence, or rejection behavior fails. FAIL\_TOOLING: runner mechanics fail. TOOLING\_BLOCKED: dependency or locus missing. Initial state: `NOT RUN`.

#### CHECK qa-10-po-010: PO-010

Goal: Deterministic BodyGraph computation must remain isolated from database and vendor effects, with all effectful vendor behavior governed by refusal, refresh, retry, rate, failure-protection, observability, and safe-logging policy.

Rails: closed. Required dependencies: Profile A. Preflight check: Command A1. Path preflight: `test -f tests/bodygraph/test_vendor_client.py && test -f tests/bodygraph/test_resolver_vendor.py && test -f tests/bodygraph/test_ingest.py && test -f tools/evidence/generate_rails_gate_evidence.py` If missing, activation/install action: Command A2. If still unavailable: use the blocker command. PF anchors: HDE Build Notes; Canon Plan Templates. Tokens: `[]`; `[]`.

TOOLING\_BLOCKED command: `qa_run qa-10-po-010 PO-010 1 0 dev TOOLING_BLOCKED '["HDE Build Notes","Canon Plan Templates"]' '[]' "printf '%s\n' 'EFFECT_ISOLATION_DEPENDENCY_UNAVAILABLE'; exit 125"`

Behavior command: `qa_run qa-10-po-010 PO-010 1 0 dev FAIL_BEHAVIOR '["HDE Build Notes","Canon Plan Templates"]' '[]' "python -m pytest -q tests/bodygraph/test_vendor_client.py tests/bodygraph/test_resolver_vendor.py tests/bodygraph/test_ingest.py && python tools/evidence/generate_rails_gate_evidence.py --check"`

Evidence command: `head -n 1 audit/qa/hde-epic038/checks/qa-10-po-010/primary.log`

What to look for: deterministic core isolation, refusal, bounded retry/rate behavior, failure protection, and keys-only logging. Required deliverable: `audit/qa/hde-epic038/checks/qa-10-po-010/primary.log`. PASS: all tests and rails evidence checks pass. FAIL\_BEHAVIOR: any effect boundary or policy predicate fails. FAIL\_TOOLING: runner or checker mechanics fail. TOOLING\_BLOCKED: dependency or locus missing. Initial state: `NOT RUN`.

#### **CHECK qa-11-po-011: PO-011**

Goal: Architecture proof must reflect the actual current public, internal, database, vendor, and compatibility surfaces using a closed classification vocabulary that reveals no sensitive values and rejects unknown or forbidden conditions.

Rails: closed. Required dependencies: Profile A. Preflight check: Command A1. Path preflight: `test -f tests/evidence/test_architecture_snapshot.py && test -f tests/evidence/test_hdapi_v2_contract_inventory.py && test -f tests/http/test_endpoint_catalog.py && test -f artifacts/architecture/architecture_snapshot.keys_only.json && test -f docs/ENDPOINTS_CATALOG.json` If missing, activation/install action: Command A2. If still unavailable: use the blocker command. PF anchors: HDE Build Notes; Canon Plan Templates. Tokens: `[]`; `[]`.

TOOLING\_BLOCKED command: `qa_run qa-11-po-011 PO-011 1 0 dev TOOLING_BLOCKED '["HDE Build Notes","Canon Plan Templates"]' '[]' "printf '%s\n' 'ARCHITECTURE_PROOF_DEPENDENCY_UNAVAILABLE'; exit 125"`

Behavior command: `qa_run qa-11-po-011 PO-011 1 0 dev FAIL_BEHAVIOR '["HDE Build Notes","Canon Plan Templates"]' '[]' "python -m pytest -q tests/evidence/test_architecture_snapshot.py tests/evidence/test_hdapi_v2_contract_inventory.py tests/http/test_endpoint_catalog.py"`

Evidence command: `head -n 1 audit/qa/hde-epic038/checks/qa-11-po-011/primary.log`

What to look for: current surface inventory, closed allowed/forbidden/out-of-scope/unknown vocabulary, no sensitive values, and exact HDAPI non-public-boundary behavior: `/api/compat/v1` and its descendants are non-public while `/api/compat/v10` remains unmatched. Required deliverable: `audit/qa/hde-epic038/checks/qa-11-po-011/primary.log`. PASS: all three test files pass without unknown or unsafe classifications, and the exact compatibility-namespace inclusion and overmatch-exclusion predicates pass. FAIL\_BEHAVIOR: surface inventory, classification, value-safety, compatibility-namespace, descendant, or overmatch-exclusion assertions fail. FAIL\_TOOLING: tests cannot execute after preflight. TOOLING\_BLOCKED: dependency or locus unavailable. Initial state: `NOT RUN`.

#### CHECK qa-12-po-012: PO-012

Goal: Direct database access must remain the sole active transport, with retired settings refused before value access or activity and with missing, unavailable, or unauthorized access failing closed without fallback, alternate providers, retries, or inferred endpoints.

Rails: closed. Required dependencies: Profile A. Preflight check: Command A1. Path preflight: `test -f ci/checks/check_direct_db_contract.py && test -f tests/db/test_direct_db_pr06r.py && test -f tests/unit/test_check_direct_db_contract.py` If missing, activation/install action: Command A2. If still unavailable: use the blocker command. PF anchors: HDE Build Notes; Canon Plan Templates. Tokens: `[]`; `[]`.

TOOLING\_BLOCKED command: `qa_run qa-12-po-012 PO-012 1 0 dev TOOLING_BLOCKED '["HDE Build Notes","Canon Plan Templates"]' '[]' "printf '%s\n' 'DIRECT_DB_CHECK_DEPENDENCY_UNAVAILABLE'; exit 125"`

Behavior command: `qa_run qa-12-po-012 PO-012 1 0 dev FAIL_BEHAVIOR '["HDE Build Notes","Canon Plan Templates"]' '[]' "python ci/checks/check_direct_db_contract.py && python -m pytest -q tests/db/test_direct_db_pr06r.py tests/unit/test_check_direct_db_contract.py"`

Evidence command: `head -n 1 audit/qa/hde-epic038/checks/qa-12-po-012/primary.log`

What to look for: `DIRECT_DB_CONTRACT_OK`, Psycopg-only selection, retired-key refusal before value read or I/O, zero alternate attempts, and fail-closed behavior. Required deliverable: `audit/qa/hde-epic038/checks/qa-12-po-012/primary.log`. PASS: checker and tests exit `0`. FAIL\_BEHAVIOR: alternate selection, late refusal, fallback, retry, or endpoint inference occurs. FAIL\_TOOLING: checker/test mechanics fail. TOOLING\_BLOCKED: dependency or locus unavailable. Initial state: `NOT RUN`.

#### CHECK qa-13-po-013: PO-013

Goal: Retained alternate-transport material must remain immutable and explicitly historical, with separate identity, meaning, ownership, and release predicates that cannot establish current availability, fallback, parity, or readiness.

Rails: closed; retained commands are never executed. Required dependencies: Profile A. Preflight check: Command A1. Path preflight: `test -f tests/evidence/test_hde_epic038_release_sanity.py && test -d audit/ops/hde-epic038/ops-01` If missing, activation/install action: Command A2 for packages; none for missing retained evidence. If still unavailable: use the blocker command. PF anchors: HDE Build Notes; Canon Plan Templates. Tokens: `[]`; `[]`.

TOOLING\_BLOCKED command: `qa_run qa-13-po-013 PO-013 1 0 dev TOOLING_BLOCKED '["HDE Build Notes","Canon Plan Templates"]' '[]' "printf '%s\n' 'HISTORICAL_PACKET_OR_VALIDATOR_UNAVAILABLE'; exit 125"`

Behavior command: `qa_run qa-13-po-013 PO-013 1 0 dev FAIL_BEHAVIOR '["HDE Build Notes","Canon Plan Templates"]' '[]' "python -m pytest -q tests/evidence/test_hde_epic038_release_sanity.py::test_historical_bridge_evidence_validates_frozen_packet_without_execution tests/evidence/test_hde_epic038_release_sanity.py::test_historical_integrity_does_not_rederive_bridge_success tests/evidence/test_hde_epic038_release_sanity.py::test_historical_packet_keeps_required_nonclaims"`

Evidence command: `head -n 1 audit/qa/hde-epic038/checks/qa-13-po-013/primary.log`

What to look for: immutable checksums/path proofs, no historical command execution, and required nonclaims. Required deliverable: `audit/qa/hde-epic038/checks/qa-13-po-013/primary.log`. PASS: all three targeted tests pass. FAIL\_BEHAVIOR: historical bytes, bindings, inventory, or nonclaims fail. FAIL\_TOOLING: validator mechanics fail. TOOLING\_BLOCKED: required retained evidence or tests are unavailable. Initial state: `NOT RUN`.

#### CHECK qa-14-po-014: PO-014

Goal: Any retained database-structure comparison claim must prove only equality of the strict shared identity projection, reject malformed or conflicting observations, and never imply complete semantic equivalence.

Rails: closed. Required dependencies: Profile A. Preflight check: Command A1. Path preflight: `test -f engine/db/ddl_identity_projection.py && test -f tests/db/test_ddl_identity_projection.py` If missing, activation/install action: Command A2 for packages; none for missing loci. If still unavailable: use the blocker command. PF anchors: HDE Build Notes; Canon Plan Templates. Tokens: `[]`; `[]`.

TOOLING\_BLOCKED command: `qa_run qa-14-po-014 PO-014 1 0 dev TOOLING_BLOCKED '["HDE Build Notes","Canon Plan Templates"]' '[]' "printf '%s\n' 'DDL_PROJECTION_TEST_UNAVAILABLE'; exit 125"`

Behavior command: `qa_run qa-14-po-014 PO-014 1 0 dev FAIL_BEHAVIOR '["HDE Build Notes","Canon Plan Templates"]' '[]' "python -m pytest -q tests/db/test_ddl_identity_projection.py"`

Evidence command: `head -n 1 audit/qa/hde-epic038/checks/qa-14-po-014/primary.log`

What to look for: comparison limited to object kind/name and column name/type; rejection of malformed, duplicate, invalid, or conflicting observations; no claim about defaults, constraints, nullability, or view semantics. Required deliverable: `audit/qa/hde-epic038/checks/qa-14-po-014/primary.log`. PASS: the strict projection suite passes and the log makes no full-equivalence claim. FAIL\_BEHAVIOR: malformed/conflicting input passes or comparison scope expands. FAIL\_TOOLING: tests cannot execute. TOOLING\_BLOCKED: dependency or locus unavailable. Initial state: `NOT RUN`.

#### CHECK qa-15-po-015: PO-015

Goal: Current operational database access must remain authorization-bound, direct-only, read-only, least-privileged, exact-source-bound, secret-safe, free of uncontrolled retries or alternate providers, and incapable of leaving reusable login access.

Rails: closed; validates retained evidence and hermetic tests only. No database or OPS call. Required dependencies: Profile A. Preflight check: Command A1. Path preflight: `test -f tests/ops/test_hde_epic038_ops03.py && test -d audit/ops/hde-epic038/ops-03` If missing, activation/install action: Command A2 for packages; none for missing packet evidence. If still unavailable: use the blocker command. PF anchors: HDE Build Notes; Canon Plan Templates. Tokens: `[]`; `[]`.

TOOLING\_BLOCKED command: `qa_run qa-15-po-015 PO-015 1 0 dev TOOLING_BLOCKED '["HDE Build Notes","Canon Plan Templates"]' '[]' "printf '%s\n' 'OPS03_VALIDATION_DEPENDENCY_UNAVAILABLE'; exit 125"`

Behavior command: `qa_run qa-15-po-015 PO-015 1 0 dev FAIL_BEHAVIOR '["HDE Build Notes","Canon Plan Templates"]' '[]' "python -m pytest -q tests/ops/test_hde_epic038_ops03.py"`

Evidence command: `head -n 1 audit/qa/hde-epic038/checks/qa-15-po-015/primary.log`

What to look for: authorization binding, direct/read-only role controls, source identity, bounded behavior, secret rejection, and nonreusable authorization. Required nonclaim: the retained capture does not prove the complete external privilege graph, exact provisioning, complete legacy-role provenance, current infrastructure inventory, or current absence of reusable external access. Required deliverable: `audit/qa/hde-epic038/checks/qa-15-po-015/primary.log`. PASS: retained packet and control semantics pass without an OPS rerun, while the required nonclaims remain visible. FAIL\_BEHAVIOR: authorization, role, source, secret, retry, provider, or reuse controls fail. FAIL\_TOOLING: test mechanics fail. TOOLING\_BLOCKED: retained packet or validation locus unavailable. Initial state: `NOT RUN`.

#### CHECK qa-16-po-016: PO-016

Goal: Controlled mapped persistence must require explicit bounded nonproduction authorization, refuse production-like use before external activity, store only validated source-neutral mapped data, and exclude raw vendor, request, response, personal, and credential content.

Rails: closed, hermetic; no live upsert. Required dependencies: Profile A. Preflight check: Command A1. Path preflight: `test -f tools/evidence/generate_v2_mapped_cache_evidence.py && test -f tests/bodygraph/test_bg_resolve_v2_mapped_cache.py && test -f tests/bodygraph/test_hde_epic038_mapped_cache_smoke.py` If missing, activation/install action: Command A2. If still unavailable: use the blocker command. PF anchors: HDE Build Notes; Canon Plan Templates. Tokens: `[]`; `[]`.

TOOLING\_BLOCKED command: `qa_run qa-16-po-016 PO-016 1 0 dev TOOLING_BLOCKED '["HDE Build Notes","Canon Plan Templates"]' '[]' "printf '%s\n' 'MAPPED_PERSISTENCE_BOUNDARY_TEST_UNAVAILABLE'; exit 125"`

Behavior command: `qa_run qa-16-po-016 PO-016 1 0 dev FAIL_BEHAVIOR '["HDE Build Notes","Canon Plan Templates"]' '[]' "python tools/evidence/generate_v2_mapped_cache_evidence.py --check && python -m pytest -q tests/bodygraph/test_bg_resolve_v2_mapped_cache.py tests/bodygraph/test_hde_epic038_mapped_cache_smoke.py"`

Evidence command: `head -n 1 audit/qa/hde-epic038/checks/qa-16-po-016/primary.log`

What to look for: explicit upsert/nonproduction gates, refusal before I/O, source-neutral projection, and secret/raw-content exclusion. Required deliverable: `audit/qa/hde-epic038/checks/qa-16-po-016/primary.log`. PASS: evidence check and boundary tests pass. FAIL\_BEHAVIOR: authorization/refusal, projection, or content-safety behavior fails. FAIL\_TOOLING: checker/test mechanics fail. TOOLING\_BLOCKED: dependencies or loci unavailable. Initial state: `NOT RUN`.

#### CHECK qa-17-po-017: PO-017

Goal: Controlled mapped persistence must preserve normalized single-record identity, canonical write/read-back equivalence, repeat-operation idempotence, explicit legacy behavior, and closed or dry-run operation without creating another persistence or public-transport authority.

Rails: closed, hermetic. Required dependencies: Profile A. Preflight check: Command A1. Path preflight: `test -f tests/bodygraph/test_v2_mapped_cache.py && test -f tests/bodygraph/test_bg_resolve_v2_mapped_cache.py` If missing, activation/install action: Command A2. If still unavailable: use the blocker command. PF anchors: HDE Build Notes; Canon Plan Templates. Tokens: `[]`; `[]`.

TOOLING\_BLOCKED command: `qa_run qa-17-po-017 PO-017 1 0 dev TOOLING_BLOCKED '["HDE Build Notes","Canon Plan Templates"]' '[]' "printf '%s\n' 'MAPPED_CACHE_IDENTITY_TEST_UNAVAILABLE'; exit 125"`

Behavior command: `qa_run qa-17-po-017 PO-017 1 0 dev FAIL_BEHAVIOR '["HDE Build Notes","Canon Plan Templates"]' '[]' "python -m pytest -q tests/bodygraph/test_v2_mapped_cache.py tests/bodygraph/test_bg_resolve_v2_mapped_cache.py"`

Evidence command: `head -n 1 audit/qa/hde-epic038/checks/qa-17-po-017/primary.log`

What to look for: normalized identity, one stored row, canonical read-back, second-write idempotence, explicit legacy behavior, and no second authority. Required deliverable: `audit/qa/hde-epic038/checks/qa-17-po-017/primary.log`. PASS: both suites pass. FAIL\_BEHAVIOR: identity, read-back, idempotence, dry-run, legacy, or authority boundaries fail. FAIL\_TOOLING: tests cannot execute. TOOLING\_BLOCKED: dependency or locus unavailable. Initial state: `NOT RUN`.

#### CHECK qa-18-po-018: PO-018

Goal: Feature producers must own only their primary proof outputs, while one canonical evidence authority must update governed companions atomically after primaries are final and validation must detect rather than repair drift.

Rails: closed. Required dependencies: Profile A. Preflight check: Command A1. Path preflight: `test -f tools/evidence/update_evidence_index.py && test -f tests/evidence/test_hde_epic038_release_sanity.py` If missing, activation/install action: Command A2. If still unavailable: use the blocker command. PF anchors: HDE Build Notes; Canon Plan Templates. Tokens: `[]`; `[]`.

TOOLING\_BLOCKED command: `qa_run qa-18-po-018 PO-018 1 0 dev TOOLING_BLOCKED '["HDE Build Notes","Canon Plan Templates"]' '[]' "printf '%s\n' 'EVIDENCE_OWNERSHIP_CHECK_UNAVAILABLE'; exit 125"`

Behavior command: `qa_run qa-18-po-018 PO-018 1 0 dev FAIL_BEHAVIOR '["HDE Build Notes","Canon Plan Templates"]' '[]' "python tools/evidence/update_evidence_index.py --check && python -m pytest -q tests/evidence/test_hde_epic038_release_sanity.py::test_pipeline_checks_prebuilt_evidence_without_post_seal_writes tests/evidence/test_hde_epic038_release_sanity.py::test_stale_evidence_graph_fails_final_pipeline_without_repair"`

Evidence command: `head -n 1 audit/qa/hde-epic038/checks/qa-18-po-018/primary.log`

What to look for: canonical owner in check mode, stale-graph rejection, no producer companion writes, and no repair. Required deliverable: `audit/qa/hde-epic038/checks/qa-18-po-018/primary.log`. PASS: updater check and targeted tests pass. FAIL\_BEHAVIOR: ownership, atomicity, drift detection, or no-repair predicates fail. FAIL\_TOOLING: validator mechanics fail. TOOLING\_BLOCKED: dependencies or loci unavailable. Initial state: `NOT RUN`.

#### CHECK qa-19-po-019: PO-019

Goal: Human-facing and machine-readable evidence records must remain mutually complete, identically bound, coherent in hashes and topology, free of duplicate, orphaned, stale, fabricated, or misclassified entries, and portable across checkouts.

Rails: closed. Required dependencies: Profile B. Preflight check: Command B1. Path preflight: `test -f tools/evidence/update_evidence_index.py && test -f tools/evidence/validate_evidence_paths.py && test -f ci/checks/check_mirror_schema.sh && test -f ci/checks/check_evidence_index_hash.sh && test -f ci/checks/check_final_lf.sh && test -f tools/evidence/orientation_demo.py && test -f artifacts/evidence_index.jsonl.sha256` If missing, activation/install action: Command B2 for packages; none for missing loci or system utilities. If still unavailable: use the blocker command. PF anchors: HDE Build Notes; Canon Plan Templates. Tokens: `[]`; `[]`.

TOOLING\_BLOCKED command: `qa_run qa-19-po-019 PO-019 1 0 dev TOOLING_BLOCKED '["HDE Build Notes","Canon Plan Templates"]' '[]' "printf '%s\n' 'EVIDENCE_TOPOLOGY_VALIDATOR_UNAVAILABLE'; exit 125"`

Behavior command: `qa_run qa-19-po-019 PO-019 1 0 dev FAIL_BEHAVIOR '["HDE Build Notes","Canon Plan Templates"]' '[]' "python tools/evidence/update_evidence_index.py --check && python tools/evidence/validate_evidence_paths.py && python ci/checks/check_mirror_schema.sh && bash ci/checks/check_evidence_index_hash.sh && python tools/evidence/orientation_demo.py --check && bash ci/checks/check_final_lf.sh"`

Evidence command: `head -n 1 audit/qa/hde-epic038/checks/qa-19-po-019/primary.log`

What to look for: current human/machine agreement, path resolution, schema/hash integrity, orientation coherence, and final-LF validity. Required deliverable: `audit/qa/hde-epic038/checks/qa-19-po-019/primary.log`. PASS: all six validators exit `0`. FAIL\_BEHAVIOR: duplicate, orphan, stale, fabricated, misclassified, hash, topology, path, or portability predicates fail. FAIL\_TOOLING: a validator cannot execute. TOOLING\_BLOCKED: dependency or locus unavailable. Initial state: `NOT RUN`.

#### CHECK qa-20-po-020: PO-020

Goal: The complete integrated validation chain must cover every mandated proof domain in its canonical order, omit none, stop at the first required failure, perform no live or operational rerun, repair no source state, and leave no partial generated state.

Rails: closed. Required dependencies: Profile B. Preflight check: Command B1. Path preflight: `test -f tools/evidence/run_sanity_pipeline.py && test -f tests/evidence/test_hde_epic038_release_sanity.py` If missing, activation/install action: Command B2. If still unavailable: use the blocker command. Setup: the custom QA log parent is created by `qa_run`; do not use the runner’s default log location. PF anchors: HDE Build Notes; Canon Plan Templates. Tokens: `[]`; `[]`.

TOOLING\_BLOCKED command: `qa_run qa-20-po-020 PO-020 1 0 dev TOOLING_BLOCKED '["HDE Build Notes","Canon Plan Templates"]' '[]' "printf '%s\n' 'INTEGRATED_PIPELINE_DEPENDENCY_UNAVAILABLE'; exit 125"`

Behavior command: `qa_run qa-20-po-020 PO-020 1 0 dev FAIL_BEHAVIOR '["HDE Build Notes","Canon Plan Templates"]' '["audit/qa/hde-epic038/checks/qa-20-po-020/integrated-validation.log"]' "python tools/evidence/run_sanity_pipeline.py --log-path audit/qa/hde-epic038/checks/qa-20-po-020/integrated-validation.log && python -m pytest -q tests/evidence/test_hde_epic038_release_sanity.py"`

Evidence command: `head -n 1 audit/qa/hde-epic038/checks/qa-20-po-020/primary.log`

Integrated-log command: `tail -n 5 audit/qa/hde-epic038/checks/qa-20-po-020/integrated-validation.log`

What to look for: exact nineteen-stage order, `first_failed_stage:NONE`, `summary:PASS`, no live or OPS execution, no repair, and no partial PASS state. Required deliverables:

* `audit/qa/hde-epic038/checks/qa-20-po-020/primary.log`  
* `audit/qa/hde-epic038/checks/qa-20-po-020/integrated-validation.log`

Both are QA-created.

PASS: the pipeline and full release-sanity suite exit `0`; both logs exist; exact stage and no-repair predicates pass. FAIL\_BEHAVIOR: a required stage fails, order changes, a domain is omitted, later execution continues after failure, OPS/live activity occurs, repair occurs, or partial state is accepted. FAIL\_TOOLING: the pipeline cannot execute or its required log cannot be captured. TOOLING\_BLOCKED: dependency or locus unavailable. Initial state: `NOT RUN`.

#### **CHECK qa-21-po-021: PO-021**

Goal: Runtime release identity must derive exclusively and deterministically from one canonical tracked release descriptor, while exact-source attestation remains external, repeatable, clean-source-bound, package-realistic, closed-environment, acyclic, non-mutating, and free of unsafe retained data.

Rails: closed. Required dependencies: Profile C. Preflight check: Command C1. Path preflight: `test -f catalog/manifest.json && test -f scripts/release_id_recompute.py && test -f tools/evidence/build_release_attestation.py` If missing, activation/install action: Commands C2 and C3 only as applicable. If git is missing, the external target exists, or a locus is missing: no automatic action proven; use the blocker command. PF anchors: HDE Build Notes; Canon Plan Templates. Tokens: `[]`; `[]`.

The `/tmp/hde-epic038-release-attestation` directory is the canon-governed external attestation workspace, not the QA evidence root. It must be absent before the check begins and remains outside both the operator working checkout and the isolated source checkout. The step's governed QA evidence remains `audit/qa/hde-epic038/checks/qa-21-po-021/primary.log`.

The behavior command captures the operator checkout's current `HEAD`, creates a runtime-derived temporary local clone, detaches that clone at the captured commit, verifies that the operator `HEAD` did not change during setup, and requires the isolated checkout's `HEAD` to equal the captured commit. It then requires `git status --porcelain=v1 --untracked-files=all` to return no output before invoking the manifest check or builder.

The isolated checkout is not the QA logging workspace. `qa_run` creates and writes `primary.log` only in the operator checkout. The behavior command's source-identity receipt, clean-source preflight, resolved manifest/build/verify command records, command outputs, and clean-source postcheck therefore flow directly into `primary.log` without creating QA files in the isolated checkout.

PO actions:

1. Ensure Command C1 is ready and `/tmp/hde-epic038-release-attestation` is absent.  
2. Define Command 1 in the same terminal that contains `qa_run`.  
3. Run Command 2 once. Do not invoke the manifest checker, builder, or verifier separately.  
4. Preserve `/tmp/hde-epic038-release-attestation` for inspection after the command. Command 1 removes only its runtime-derived temporary source clone.  
5. Inspect the recorded source commit, `CLEAN_SOURCE_PREFLIGHT=PASS`, `CLEAN_SOURCE_PREBUILDER=PASS`, the three resolved command records, builder and verifier output, and `CLEAN_SOURCE_POSTCHECK=PASS` in `primary.log`.

TOOLING\_BLOCKED command: `qa_run qa-21-po-021 PO-021 1 0 dev TOOLING_BLOCKED '["HDE Build Notes","Canon Plan Templates"]' '[]' "printf '%s\n' 'ATTESTATION_PREFLIGHT_UNAVAILABLE'; exit 125"`

Command 1 — define the isolated exact-source behavior:

```
qa21_command=$(cat <<'QA21SH'
qa_source_root="$(git rev-parse --show-toplevel)" || exit 126
qa_source_commit="$(git -C "$qa_source_root" rev-parse --verify 'HEAD^{commit}')" || exit 126
qa_isolation_root="$(python -c 'import tempfile; print(tempfile.mkdtemp(prefix="hde-epic038-clean-source-", dir="/tmp"))')" || exit 126
qa_clean_source="$qa_isolation_root/source"
qa_attestation_output="/tmp/hde-epic038-release-attestation"

qa_cleanup() {
  python - "$qa_isolation_root" <<'QA21CLEANPY'
import pathlib
import shutil
import sys

path = pathlib.Path(sys.argv[1]).resolve()
temp_root = pathlib.Path("/tmp").resolve()
if path.parent != temp_root or not path.name.startswith(
    "hde-epic038-clean-source-"
):
    raise SystemExit("CLEAN_SOURCE_CLEANUP_REFUSED")
shutil.rmtree(path)
QA21CLEANPY
}
trap qa_cleanup EXIT

if [ -e "$qa_attestation_output" ]; then
  printf '%s\n' 'ATTESTATION_OUTPUT_NOT_ABSENT'
  exit 125
fi

git clone --quiet --no-local --no-checkout "$qa_source_root" "$qa_clean_source" || exit 126
git -C "$qa_clean_source" checkout --quiet --detach "$qa_source_commit" || exit 126

qa_source_commit_after="$(git -C "$qa_source_root" rev-parse --verify 'HEAD^{commit}')" || exit 126
qa_isolated_commit="$(git -C "$qa_clean_source" rev-parse --verify 'HEAD^{commit}')" || exit 126
if [ "$qa_source_commit_after" != "$qa_source_commit" ] || [ "$qa_isolated_commit" != "$qa_source_commit" ]; then
  printf '%s\n' 'EXACT_SOURCE_BINDING=FAIL'
  exit 126
fi

qa_clean_status="$(git -C "$qa_clean_source" status --porcelain=v1 --untracked-files=all)" || exit 126
if [ -n "$qa_clean_status" ]; then
  printf '%s\n' 'CLEAN_SOURCE_PREFLIGHT=FAIL'
  exit 126
fi

printf '%s\n' \
  "ATTESTATION_SOURCE_COMMIT=$qa_source_commit" \
  "ATTESTATION_CLEAN_SOURCE=$qa_clean_source" \
  'CLEAN_SOURCE_PREFLIGHT=PASS' \
  "MANIFEST_CHECK_COMMAND=(cd $qa_clean_source && PYTHONDONTWRITEBYTECODE=1 python scripts/release_id_recompute.py --check-manifest-only)" \
  "ATTESTATION_BUILD_COMMAND=(cd $qa_clean_source && PYTHONDONTWRITEBYTECODE=1 python tools/evidence/build_release_attestation.py --output $qa_attestation_output --require-clean)" \
  "ATTESTATION_VERIFY_COMMAND=(cd $qa_clean_source && PYTHONDONTWRITEBYTECODE=1 python tools/evidence/build_release_attestation.py --verify $qa_attestation_output --require-clean)"

(
  cd "$qa_clean_source" || exit 126
  PYTHONDONTWRITEBYTECODE=1 python scripts/release_id_recompute.py --check-manifest-only || exit $?
  qa_prebuilder_status="$(git status --porcelain=v1 --untracked-files=all)" || exit 126
  if [ -n "$qa_prebuilder_status" ]; then
    printf '%s\n' 'CLEAN_SOURCE_PREBUILDER=FAIL'
    exit 1
  fi
  printf '%s\n' 'CLEAN_SOURCE_PREBUILDER=PASS'
  PYTHONDONTWRITEBYTECODE=1 python tools/evidence/build_release_attestation.py --output "$qa_attestation_output" --require-clean || exit $?
  PYTHONDONTWRITEBYTECODE=1 python tools/evidence/build_release_attestation.py --verify "$qa_attestation_output" --require-clean || exit $?
)
qa21_rc=$?
if [ "$qa21_rc" -ne 0 ]; then
  exit "$qa21_rc"
fi

qa_post_status="$(git -C "$qa_clean_source" status --porcelain=v1 --untracked-files=all)" || exit 126
if [ -n "$qa_post_status" ]; then
  printf '%s\n' 'CLEAN_SOURCE_POSTCHECK=FAIL'
  exit 1
fi
printf '%s\n' 'CLEAN_SOURCE_POSTCHECK=PASS'

trap - EXIT
qa_cleanup || exit 126
QA21SH
)
```

Command 2 — behavior command: `qa_run qa-21-po-021 PO-021 1 0 dev FAIL_BEHAVIOR '["HDE Build Notes","Canon Plan Templates"]' '[]' "$qa21_command"`

Evidence command: `head -n 1 audit/qa/hde-epic038/checks/qa-21-po-021/primary.log`

What to look for: the captured operator `HEAD`; the isolated checkout bound to that exact commit; `CLEAN_SOURCE_PREFLIGHT=PASS` before the manifest checker; `CLEAN_SOURCE_PREBUILDER=PASS` immediately before builder invocation; the resolved manifest, build, and verify commands plus their actual output in `primary.log`; canonical manifest identity; external initially absent output; packaged entrypoint; closed rails; verification PASS; `CLEAN_SOURCE_POSTCHECK=PASS`; temporary-source cleanup; and no unsafe retained values. Required deliverable: `audit/qa/hde-epic038/checks/qa-21-po-021/primary.log`. Transient output: `/tmp/hde-epic038-release-attestation`; inspect only through the verified command result. PASS: exact-commit binding, both pre-build cleanliness checks, identity check, build, verification, post-build cleanliness, and temporary-source cleanup all succeed. FAIL\_BEHAVIOR: after valid isolated-source setup, manifest, attestation, source, identity, packaging, cycle, mutation, or value-safety behavior fails. FAIL\_TOOLING: exact-source construction, builder execution, clean-source mechanics, package setup, logging, or cleanup fails. TOOLING\_BLOCKED: Profile C readiness, a required locus, or the absent external destination cannot be established. Initial state: `NOT RUN`.

#### CHECK qa-22-po-022: PO-022

Goal: Accepted operational captures must remain byte-stable, source-bound, and separately admitted without rerunning privileged activity or rewriting what the operator observed.

REPO VALIDATION NOTE: Governed packet roots `audit/ops/hde-epic038/ops-01`, `ops-02`, and `ops-03` have checksum/path-proof families. The separate `audit/ops/hde-epic038/ops-03-operator-record/` root lacks a proven sibling path-proof family and must not be treated as equivalent to the admitted packet.

Rails: closed; no OPS commands. Required dependencies: Profile A. Preflight check: Command A1. Path preflight: `test -f tests/evidence/test_hde_epic038_release_sanity.py && test -f tests/ops/test_hde_epic038_ops03.py && test -d audit/ops/hde-epic038/ops-02 && test -d audit/ops/hde-epic038/ops-03` If missing, activation/install action: Command A2 for packages; none for missing packet evidence. If still unavailable: use the blocker command. PF anchors: HDE Build Notes; Canon Plan Templates. Tokens: `[]`; `[]`.

TOOLING\_BLOCKED command: `qa_run qa-22-po-022 PO-022 1 0 dev TOOLING_BLOCKED '["HDE Build Notes","Canon Plan Templates"]' '[]' "printf '%s\n' 'OPERATIONAL_CAPTURE_VALIDATOR_UNAVAILABLE'; exit 125"`

Behavior command: `qa_run qa-22-po-022 PO-022 1 0 dev FAIL_BEHAVIOR '["HDE Build Notes","Canon Plan Templates"]' '[]' "python -m pytest -q tests/evidence/test_hde_epic038_release_sanity.py::test_ops02_is_validated_without_executing_commands tests/evidence/test_hde_epic038_release_sanity.py::test_tracked_ops03_fixture_is_validated_without_execution tests/ops/test_hde_epic038_ops03.py::test_final_commit_rejects_post_validator_candidate_mutation tests/ops/test_hde_epic038_ops03.py::test_successful_authorization_cannot_be_reused tests/ops/test_hde_epic038_ops03.py::test_validator_binds_exact_mode_argv"`

Evidence command: `head -n 1 audit/qa/hde-epic038/checks/qa-22-po-022/primary.log`

What to look for: retained-packet validation without command execution, source/mode binding, mutation rejection, and nonreusable authorization. Required deliverable: `audit/qa/hde-epic038/checks/qa-22-po-022/primary.log`. PASS: all five targeted tests pass and no operational command runs. FAIL\_BEHAVIOR: bytes, source binding, admission separation, mutation rejection, or authorization reuse controls fail. FAIL\_TOOLING: validator mechanics fail. TOOLING\_BLOCKED: packet or test locus unavailable. Initial state: `NOT RUN`.

#### CHECK qa-23-po-023: PO-023

Goal: No proof surface, diagnostic output, operational record, architecture observation, failure record, or release attestation may retain secrets, personal inputs, raw vendor payloads, endpoint values, or credential material.

Rails: closed. Required dependencies: Profile A. Preflight check: Command A1. Path preflight: `test -f tools/evidence/generate_rails_gate_evidence.py && test -f tests/bodygraph/test_vendor_client.py && test -f tests/bodygraph/test_resolver_vendor.py && test -f tests/evidence/test_release_attestation.py && test -f tests/ops/test_hde_epic038_ops03.py` If missing, activation/install action: Command A2. If still unavailable: use the blocker command. PF anchors: HDE Build Notes; Canon Plan Templates. Tokens: `[]`; `[]`.

TOOLING\_BLOCKED command: `qa_run qa-23-po-023 PO-023 1 0 dev TOOLING_BLOCKED '["HDE Build Notes","Canon Plan Templates"]' '[]' "printf '%s\n' 'REDACTION_VALIDATION_DEPENDENCY_UNAVAILABLE'; exit 125"`

Behavior command: `qa_run qa-23-po-023 PO-023 1 0 dev FAIL_BEHAVIOR '["HDE Build Notes","Canon Plan Templates"]' '[]' "python tools/evidence/generate_rails_gate_evidence.py --check && python -m pytest -q tests/bodygraph/test_vendor_client.py tests/bodygraph/test_resolver_vendor.py tests/evidence/test_release_attestation.py tests/ops/test_hde_epic038_ops03.py -k 'redact or secret or raw_payload'"`

Evidence command: `head -n 1 audit/qa/hde-epic038/checks/qa-23-po-023/primary.log`

What to look for: `RAILS_GATE_EVIDENCE_OK` and passing secret, redaction, raw-payload, attestation, and operational-record safety tests. Required deliverable: `audit/qa/hde-epic038/checks/qa-23-po-023/primary.log`. PASS: checker and selected safety tests exit `0`, and the primary log itself contains no prohibited value. FAIL\_BEHAVIOR: any prohibited value or raw-content class is retained or emitted. FAIL\_TOOLING: checker/test mechanics fail. TOOLING\_BLOCKED: dependency or locus unavailable. Initial state: `NOT RUN`.

### Close-out deliverables

Required closeout paths:

* Discovery artifact: `audit/qa/hde-epic038/checks/qa-00-step-0-discovery/primary.log`  
* Step manifest: `audit/qa/hde-epic038/qa_step_logs_manifest.json`  
* Manifest path proof: `audit/qa/hde-epic038/qa_step_logs_manifest.json.path_proof.txt`  
* QA RCA and Doc Delta summary: `audit/qa/hde-epic038/00_meta/qa_rca_doc_delta_summary.md`  
* Authoritative Doc Delta record: `audit/qa/hde-epic038/00_meta/doc_deltas.md`

Run Profile B preflight before closeout. After all planned checks have either executed or received an explicit `TOOLING_BLOCKED` log, use these separate noninteractive phases:

1. Declare `QA_CLOSEOUT_PRE_ROUTING_RECEIPT` as the initial blocked or failed routing receipt, or literal `NONE` when no such receipt exists. Leave `QA_CLOSEOUT_ROUTING_RECEIPT` unset or set it to `NONE`.  
2. Define Closeout Command 1, then run Closeout Command 2\. Generation creates and validates the current manifest and path proof, writes the routing-blocked summary, records the actual generation command and pre-routing receipt, and exits `125` because approved routing and companion refresh remain pending. The generation process then ends.  
3. Route the current generated manifest and required companion refresh through the approved PR posture. No terminal process remains open during that transition.  
4. After the approved routed refresh is present in the execution workspace, declare `QA_CLOSEOUT_ROUTING_RECEIPT` as the approved non-`NONE` PR routing receipt and redeclare the same `QA_CLOSEOUT_PRE_ROUTING_RECEIPT`.  
5. Define Closeout Command 1 again if the terminal was replaced, then run Closeout Command 3\. Finalization reopens and validates the current manifest, path proof, generation summary, step logs, Doc Delta pair, canonical evidence updater/source, Human Evidence Index, and Machine Mirror before performing canonical lookup.  
6. Run Closeout Commands 4 and 5 only after finalization. Missing routing provenance or generated inputs records `TOOLING_BLOCKED`; malformed generated state or mechanical validation failure records `FAIL_TOOLING`.

Closeout Command 1 — define the phase runner:

```
qa_closeout() {
  if [ "$#" -ne 1 ]; then
    printf '%s\n' "qa_closeout requires one phase argument"
    return 64
  fi

  QA_CLOSEOUT_PHASE="$1" python - <<'CLOSEPY'
import datetime
import hashlib
import json
import os
import subprocess
from pathlib import Path

phase = (os.environ.get("QA_CLOSEOUT_PHASE") or "").strip()
pre_routing_receipt = (
    os.environ.get("QA_CLOSEOUT_PRE_ROUTING_RECEIPT") or ""
).strip()
routing_receipt = (
    os.environ.get("QA_CLOSEOUT_ROUTING_RECEIPT") or ""
).strip()

if phase not in {"generation", "finalize"}:
    raise SystemExit("INVALID_CLOSEOUT_PHASE")
if not pre_routing_receipt:
    print("PRE_ROUTING_RECEIPT_UNDECLARED")
    raise SystemExit(125)
if phase == "generation" and routing_receipt not in {"", "NONE"}:
    print("GENERATION_REQUIRES_NO_ROUTING_RECEIPT")
    raise SystemExit(125)

root = Path("audit/qa/hde-epic038")
manifest_path = root / "qa_step_logs_manifest.json"
proof_path = root / "qa_step_logs_manifest.json.path_proof.txt"
summary_path = root / "00_meta" / "qa_rca_doc_delta_summary.md"
staging_delta = Path("audit/docdeltas/hde-epic038_doc_deltas.md")
authoritative_delta = root / "00_meta" / "doc_deltas.md"

check_ids = [
    "qa-00-step-0-discovery",
    "qa-01-po-001",
    "qa-02-po-002",
    "qa-03-po-003",
    "qa-04-po-004",
    "qa-05-po-005",
    "qa-06-po-006",
    "qa-07-po-007",
    "qa-08-po-008",
    "qa-09-po-009",
    "qa-10-po-010",
    "qa-11-po-011",
    "qa-12-po-012",
    "qa-13-po-013",
    "qa-14-po-014",
    "qa-15-po-015",
    "qa-16-po-016",
    "qa-17-po-017",
    "qa-18-po-018",
    "qa-19-po-019",
    "qa-20-po-020",
    "qa-21-po-021",
    "qa-22-po-022",
    "qa-23-po-023",
]

allowed_statuses = {
    "PASS",
    "FAIL_BEHAVIOR",
    "FAIL_TOOLING",
    "TOOLING_BLOCKED",
    "SKIPPED",
    "WARN",
}

manifest = {}
coverage = []
for check_id in check_ids:
    log = root / "checks" / check_id / "primary.log"
    if not log.exists():
        coverage.append((check_id, "NOT RUN", None))
        continue

    raw = log.read_bytes()
    try:
        header = json.loads(raw.splitlines()[0])
    except Exception as exc:
        raise SystemExit(f"INVALID_STEP_LOG_HEADER:{check_id}:{exc}")

    if header.get("check_id") != check_id:
        raise SystemExit(f"CHECK_ID_MISMATCH:{check_id}")

    status = header.get("status")
    if status not in allowed_statuses:
        raise SystemExit(f"INVALID_STEP_STATUS:{check_id}")

    rel = log.relative_to(root).as_posix()
    manifest[check_id] = {
        "check_id": check_id,
        "status": status,
        "log_path": rel,
        "sha256": hashlib.sha256(raw).hexdigest(),
        "size_bytes": len(raw),
    }
    coverage.append((check_id, status, rel))

manifest_bytes = (
    json.dumps(manifest, sort_keys=True, separators=(",", ":")) + "\n"
).encode("utf-8")


def write_summary(
    lookup_status,
    lookup_detail,
    recorded_routing_receipt,
    finalization_ran,
):
    all_pass = (
        len(coverage) == len(check_ids)
        and all(status == "PASS" for _, status, _ in coverage)
        and lookup_status == "PASS"
    )
    findings = [
        f"{check_id}: {status}"
        for check_id, status, _ in coverage
        if status != "PASS"
    ]
    if lookup_status != "PASS":
        findings.append(f"qa_step_logs_manifest lookup: {lookup_status}")

    lines = [
        "# HDE-EPIC038 QA RCA and Doc Delta Summary",
        "",
        "## Live QA findings",
    ]
    if findings:
        lines.extend(f"- {finding}" for finding in findings)
    else:
        lines.append("- no new deltas found")

    lines.extend(
        [
            "",
            "## PF-Canon mapping",
            "- Runtime, database, evidence, release, and operational findings: HDE Build Notes.",
            "- QA evidence and closeout posture: Canon Plan Templates.",
            "- Local launcher and compatibility usage terminology: HDE User Guide.",
            "",
            "## Coverage versus QA Plan",
            "| Check ID | Coverage status | Evidence |",
            "|---|---|---|",
        ]
    )
    for check_id, status, rel in coverage:
        evidence = rel if rel is not None else "Unknown"
        lines.append(f"| {check_id} | {status} | {evidence} |")

    blocked = [
        (check_id, status, rel)
        for check_id, status, rel in coverage
        if status
        in {
            "TOOLING_BLOCKED",
            "FAIL_TOOLING",
            "NOT RUN",
            "SKIPPED",
        }
    ]
    lines.extend(["", "## Blocked, unexecuted, or deferred work"])
    if not blocked:
        lines.append("- None.")
    else:
        for check_id, status, rel in blocked:
            lines.append(
                f"- {check_id}: precondition or execution readiness was unmet; status {status}; evidence {rel or 'Unknown'}; closeout impact: required coverage incomplete; required follow-up: plan change."
            )

    behavior_failures = [
        (check_id, rel)
        for check_id, status, rel in coverage
        if status == "FAIL_BEHAVIOR"
    ]
    for check_id, rel in behavior_failures:
        lines.append(
            f"- {check_id}: behavior failure remains unresolved; evidence {rel}; closeout impact: acceptance blocked; required follow-up: implementation change."
        )

    lines.extend(
        [
            "",
            "## Closeout phase commands",
            "- Generation command: qa_closeout generation.",
            (
                "- Finalization command: qa_closeout finalize."
                if finalization_ran
                else "- Finalization command: NOT RUN."
            ),
            "",
            "## Manifest lookup and routing proof",
            f"- Lookup status: {lookup_status}.",
            f"- Lookup detail: {lookup_detail}.",
            "- Required routing type: PR.",
            f"- Routing receipt: {recorded_routing_receipt}.",
            f"- Pre-routing blocked or failed receipt: {pre_routing_receipt}.",
            "- Routing and lookup proof do not replace any check’s behavioral proof.",
            "",
            "## Token posture",
            "- Every planned check is tokenless. Intended and claimed token arrays are empty.",
            "- Missing required evidence is Unknown and is not inferred from repository, release, or operational records.",
            "",
            "## Moon Loop",
            "- No implementation Moon Loop is authorized or claimed by this runbook.",
            "",
            "## Completion states",
            (
                "- Repo-supported completion: READY FOR CLOSEOUT REVIEW."
                if all_pass
                else "- Repo-supported completion: NOT READY."
            ),
            "- Canon-drain completion: NOT CLAIMED.",
            "- Formal close-pack completion: NOT CLAIMED.",
            "",
            "## Documentation drainage",
            "- Undrained documentation deltas remain follow-up work. Documentation drainage is not an independent step verdict or closeout blocker when all required QA evidence is complete and trusted.",
            "",
            "## Readiness recommendation",
            (
                "- Proceed to closeout review using the governed evidence pointers above."
                if all_pass
                else "- Do not claim QA closeout; resolve or formally disposition every non-PASS and NOT RUN item."
            ),
        ]
    )

    summary_path.parent.mkdir(parents=True, exist_ok=True)
    summary_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return all_pass


if not staging_delta.exists() or not authoritative_delta.exists():
    raise SystemExit("DOC_DELTA_PAIR_MISSING")
if staging_delta.read_bytes() != authoritative_delta.read_bytes():
    raise SystemExit("DOC_DELTA_PAIR_MISMATCH")

if phase == "generation":
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_bytes(manifest_bytes)

    produced_at_utc = (
        datetime.datetime.now(datetime.timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z")
    )
    mtime_utc = (
        datetime.datetime.fromtimestamp(
            manifest_path.stat().st_mtime,
            datetime.timezone.utc,
        )
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z")
    )
    proof_lines = [
        f"path: {manifest_path.as_posix()}",
        f"sha256: {hashlib.sha256(manifest_bytes).hexdigest()}",
        f"size_bytes: {len(manifest_bytes)}",
        f"mtime_utc: {mtime_utc}",
        f"produced_at_utc: {produced_at_utc}",
    ]
    proof_path.write_text(
        "\n".join(proof_lines) + "\n",
        encoding="utf-8",
    )

    lookup_status = "TOOLING_BLOCKED"
    lookup_detail = "approved PR routing and required companion refresh pending"
    write_summary(
        lookup_status,
        lookup_detail,
        "NONE",
        False,
    )
    print(
        json.dumps(
            {
                "phase": phase,
                "manifest": manifest_path.as_posix(),
                "manifest_path_proof": proof_path.as_posix(),
                "summary": summary_path.as_posix(),
                "manifest_lookup_status": lookup_status,
                "manifest_lookup_detail": lookup_detail,
                "routing_type": "PR",
                "routing_receipt": "NONE",
                "pre_routing_receipt": pre_routing_receipt,
            },
            sort_keys=True,
        )
    )
    raise SystemExit(125)

missing_generated_inputs = [
    path.as_posix()
    for path in (manifest_path, proof_path, summary_path)
    if not path.is_file()
]
generated_validation_error = ""

if not missing_generated_inputs:
    try:
        current_manifest = json.loads(
            manifest_path.read_text(encoding="utf-8")
        )
        if current_manifest != manifest:
            raise ValueError("MANIFEST_DOES_NOT_MATCH_CURRENT_STEP_LOGS")

        proof_lines = proof_path.read_text(
            encoding="utf-8"
        ).splitlines()
        if len(proof_lines) != 5 or any(
            ": " not in line for line in proof_lines
        ):
            raise ValueError("INVALID_PATH_PROOF_SHAPE")

        proof_keys = [
            line.split(": ", 1)[0] for line in proof_lines
        ]
        if proof_keys != [
            "path",
            "sha256",
            "size_bytes",
            "mtime_utc",
            "produced_at_utc",
        ]:
            raise ValueError("INVALID_PATH_PROOF_KEYS")

        proof = dict(
            line.split(": ", 1) for line in proof_lines
        )
        if proof["path"] != manifest_path.as_posix():
            raise ValueError("PATH_PROOF_PATH_MISMATCH")
        if proof["sha256"] != hashlib.sha256(
            manifest_path.read_bytes()
        ).hexdigest():
            raise ValueError("PATH_PROOF_HASH_MISMATCH")
        if proof["size_bytes"] != str(
            len(manifest_path.read_bytes())
        ):
            raise ValueError("PATH_PROOF_SIZE_MISMATCH")

        for key in ("mtime_utc", "produced_at_utc"):
            value = proof[key]
            if not value.endswith("Z"):
                raise ValueError(f"PATH_PROOF_TIMESTAMP:{key}")
            parsed = datetime.datetime.fromisoformat(
                value.replace("Z", "+00:00")
            )
            if parsed.tzinfo is None:
                raise ValueError(f"PATH_PROOF_TIMEZONE:{key}")

        generation_summary = summary_path.read_text(
            encoding="utf-8"
        )
        required_generation_lines = {
            "- Generation command: qa_closeout generation.",
            "- Finalization command: NOT RUN.",
            "- Routing receipt: NONE.",
            f"- Pre-routing blocked or failed receipt: {pre_routing_receipt}.",
        }
        if not required_generation_lines.issubset(
            set(generation_summary.splitlines())
        ):
            raise ValueError(
                "GENERATION_PHASE_PROVENANCE_MISMATCH"
            )
    except (
        OSError,
        UnicodeError,
        ValueError,
        TypeError,
        json.JSONDecodeError,
    ) as exc:
        generated_validation_error = (
            f"{exc.__class__.__name__}:{exc}"
        )

lookup_paths = {
    "canonical evidence updater/source": Path(
        "tools/evidence/update_evidence_index.py"
    ),
    "Human Evidence Index": Path("docs/evidence/INDEX.json"),
    "Machine Mirror": Path("artifacts/evidence_index.jsonl"),
}
missing_lookup_inputs = [
    label
    for label, path in lookup_paths.items()
    if not path.is_file()
]
lookup_hits = {}
updater_rc = None
updater_error = ""

if not routing_receipt or routing_receipt == "NONE":
    lookup_status = "TOOLING_BLOCKED"
    lookup_detail = "approved PR routing receipt unavailable; lookup not run"
elif missing_generated_inputs:
    lookup_status = "TOOLING_BLOCKED"
    lookup_detail = (
        "missing generated closeout input: "
        + ", ".join(missing_generated_inputs)
    )
elif generated_validation_error:
    lookup_status = "FAIL_TOOLING"
    lookup_detail = (
        "generated closeout validation failed mechanically: "
        + generated_validation_error
    )
elif missing_lookup_inputs:
    lookup_status = "TOOLING_BLOCKED"
    lookup_detail = (
        "missing lookup input: " + ", ".join(missing_lookup_inputs)
    )
else:
    manifest_lookup = manifest_path.as_posix()
    try:
        for label, path in lookup_paths.items():
            lookup_hits[label] = (
                manifest_lookup
                in path.read_text(encoding="utf-8")
            )
        updater_result = subprocess.run(
            [
                "python",
                "tools/evidence/update_evidence_index.py",
                "--check",
            ],
            capture_output=True,
            text=True,
            check=False,
        )
        updater_rc = updater_result.returncode
    except (OSError, UnicodeError) as exc:
        updater_error = exc.__class__.__name__

    if updater_error:
        lookup_status = "FAIL_TOOLING"
        lookup_detail = (
            "canonical lookup validator failed mechanically: "
            + updater_error
        )
    elif updater_rc in {126, 127}:
        lookup_status = "FAIL_TOOLING"
        lookup_detail = (
            f"canonical lookup validator exit: {updater_rc}"
        )
    elif updater_rc != 0:
        lookup_status = "FAIL_TOOLING"
        lookup_detail = (
            f"canonical lookup validator exit: {updater_rc}"
        )
    elif not all(lookup_hits.values()):
        lookup_status = "TOOLING_BLOCKED"
        lookup_detail = (
            "required routed canonical lookup unavailable: "
            f"{json.dumps(lookup_hits, sort_keys=True)}"
        )
    else:
        lookup_status = "PASS"
        lookup_detail = (
            f"updater_exit={updater_rc}; "
            f"lookup_hits={json.dumps(lookup_hits, sort_keys=True)}"
        )

all_pass = write_summary(
    lookup_status,
    lookup_detail,
    routing_receipt or "NONE",
    True,
)
print(
    json.dumps(
        {
            "phase": phase,
            "manifest": manifest_path.as_posix(),
            "manifest_path_proof": proof_path.as_posix(),
            "summary": summary_path.as_posix(),
            "all_pass": all_pass,
            "manifest_lookup_status": lookup_status,
            "manifest_lookup_detail": lookup_detail,
            "routing_type": "PR",
            "routing_receipt": routing_receipt or "NONE",
            "pre_routing_receipt": pre_routing_receipt,
        },
        sort_keys=True,
    )
)

if lookup_status == "TOOLING_BLOCKED":
    raise SystemExit(125)
if lookup_status == "FAIL_TOOLING":
    raise SystemExit(126)
raise SystemExit(0 if all_pass else 1)
CLOSEPY
}
```

Closeout Command 2 — generation phase: `qa_closeout generation`

Closeout Command 3 — post-route finalization phase: `qa_closeout finalize`

Closeout Command 4: `python -c 'import datetime,hashlib,json; from pathlib import Path; root=Path("audit/qa/hde-epic038"); m=root/"qa_step_logs_manifest.json"; manifest=json.loads(m.read_text(encoding="utf-8")); proof_lines=(root/"qa_step_logs_manifest.json.path_proof.txt").read_text(encoding="utf-8").splitlines(); keys=[line.split(": ",1)[0] for line in proof_lines]; proof=dict(line.split(": ",1) for line in proof_lines); entries_ok=isinstance(manifest,dict) and all(isinstance(entry,dict) and {"check_id","status","log_path"} <= entry.keys() and entry["check_id"]==check_id and not Path(entry["log_path"]).is_absolute() and bool(Path(entry["log_path"]).parts) and Path(entry["log_path"]).parts[0]=="checks" and (root/entry["log_path"]).is_file() and json.loads((root/entry["log_path"]).read_bytes().splitlines()[0]).get("status")==entry["status"] for check_id,entry in manifest.items()); timestamps_ok=all(proof[key].endswith("Z") and datetime.datetime.fromisoformat(proof[key].replace("Z","+00:00")).tzinfo is not None for key in ("mtime_utc","produced_at_utc")); ok=entries_ok and keys==["path","sha256","size_bytes","mtime_utc","produced_at_utc"] and proof["path"]==m.as_posix() and proof["sha256"]==hashlib.sha256(m.read_bytes()).hexdigest() and proof["size_bytes"]==str(len(m.read_bytes())) and timestamps_ok; raise SystemExit(0 if ok else 1)'`

Closeout Command 5: `test -s audit/qa/hde-epic038/00_meta/qa_rca_doc_delta_summary.md`

Closeout PASS criteria:

* Manifest is a JSON object keyed uniquely by `check_id` and contains every executed check, including every `TOOLING_BLOCKED` check.  
* Each manifest entry has a key-matching `check_id`, a status matching its step-log header, and a log path relative to the epic QA root.  
* Manifest proof is line-oriented and contains `path`, `sha256`, `size_bytes`, `mtime_utc`, and `produced_at_utc` exactly once.  
* After the approved PR route has refreshed the current generated manifest and required companions, post-generation lookup proves the current manifest is discoverable in the canonical evidence updater/source, Human Evidence Index, and Machine Mirror.  
* The approved PR routing receipt is recorded before closeout PASS, any pre-routing blocked or failed receipt is preserved, and routing proof remains distinct from behavioral proof.  
* Missing or mechanically unavailable lookup proof remains `TOOLING_BLOCKED` or `FAIL_TOOLING` according to cause.  
* Coverage lists every planned check in order.  
* Missing logs are `NOT RUN`, with evidence `Unknown`.  
* Behavior and tooling failures remain distinct.  
* Readiness, canon drainage, and formal close-pack completion remain separate.

#### What “QA RCA & Doc Delta summary” means (explicit; non-drifting)

The summary is an execution deliverable, not a debugging diary. It must:

* State actual Live QA findings or `no new deltas found`.  
* Map substantive findings to PF titles.  
* Account for every check in plan order.  
* Point covered checks to stable step evidence.  
* Mark absent evidence `Unknown`.  
* Preserve explicit `TOOLING_BLOCKED`, `FAIL_TOOLING`, `FAIL_BEHAVIOR`, and `NOT RUN` postures.  
* Require a plan change for execution defects and an implementation change for behavior defects.  
* Make no token claim without governed evidence.  
* Keep repository-supported completion, canon drainage, and formal close-pack completion separate.  
* Treat documentation drainage as follow-up rather than an independent QA blocker.

## Review guardrails

* Execute only after Step 0 passes.  
* Do not start a service, deploy, migrate, provision infrastructure, or run OPS.  
* Do not execute commands recorded inside retained operational packets.  
* Do not run mapped-cache live upsert commands.  
* Do not run the evidence updater without `--check` except immediately after the successful authorized live primary in `qa-08-po-008`, under the approved PR route, after recording its routing receipt and preserving any pre-routing blocked or failed receipt separately from behavioral proof.  
* Do not use the integrated pipeline’s default log path; use the QA-created path in `qa-20-po-020`.  
* Do not expose secret values, endpoint values, personal inputs, or raw vendor payloads.  
* Do not infer acceptance from file presence, historical PASS, implementation records, release evidence, or operational captures.  
* Do not convert the compatibility surface into a new public route.  
* Do not classify missing dependencies as `FAIL_BEHAVIOR`.  
* If future QA observes a missing assigned route in the production-selected factory, classify that observation as `FAIL_BEHAVIOR`, not tooling or an unresolved audit gap.  
* Do not substitute alternate commands, paths, tests, helpers, environment keys, or installation instructions.  
* If a validated repository locus has moved or disappeared, record `TOOLING_BLOCKED` and require a plan change.  
* All future artifacts remain `NOT RUN` until their owning action executes.  
* A non-PASS check claims no tokens.  
* Do not claim QA closeout unless every required check is PASS and every required closeout artifact validates.

ASK OK?  
