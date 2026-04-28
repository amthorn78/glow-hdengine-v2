Remediation Implementation Guide HDE-EPIC030

Version: r2 

Executive Summary

* po-006 is blocked because the behavior gate failed: `FAIL_BEHAVIOR`, `exit_code=1`, `pytest_rc=1`, `grep_rc=0`, with the numeric-free marker present.  
* The primary failure signature is a direct compatibility compute/test contract break: `compat_public()` was called without five required invocation arguments, while ordering still requires `person_uid`.  
* The deeper proof defect is that the current po-006 plan/evidence posture does not honor the pre-App/no-user reality: a real live compatibility behavior test must call the vendor because person data is not currently stored in JSON or database.  
* Affected surfaces are `engine/compat/compute.py`, `engine/compat/ordering.py`, direct compatibility tests, the public Reader/public-output proof boundary, the internal/admin compat route, and the po-006 QA plan block.  
* Remediation execution is PR \+ OPS only: PR work repairs or bounds the no-user compatibility seam, and OPS work by the PO discovers and, if unblocked, executes the controlled vendor-backed no-user smoke. QA plan correction and documentation drainage remain PO-owned preconditins or follow-ups outside the executable remediation task plan.  
* Discovery is required before change work: the exact vendor-backed no-user command is not proven, current po-006 evidence appears out of sync with current test source, and Thoth must approve the no-user public/birth-facing contract direction.  
* This guide does not authorize a QA rerun, Live QA closure, PF-canon redline task, PR review, or closure decision.

Canon Frame (What “Correct” Means)

* Public user-facing compatibility output must remain bands-only and numeric-free. Internal/admin compat JSON may include scores and keys only while remaining bounded to internal/admin surfaces. PF04 — HDE-Governance, §2.0.11 Catalog hygiene (where applicable); PF02 — HDE Architecture, §3.1 Compat v1 \[Implemented\]; PF02 — HDE Architecture, §3.2 Reader v1 \[Required-Now\].  
* In the current pre-App/no-user environment, live compatibility behavior proof must not depend on app user IDs or DB-backed user BodyGraphs. Live behavior proof must use vendor-backed birth/no-user inputs when behavior, not only local serializer/math, is being tested. PF19 — Glow QA Guide, §3.3 Environment constraints — pre-App, no-user QA mode.  
* PO Live QA vendor behavior is vendor-first; identity, determinism, and static/internal checks are preconditions or QA/infra work, not substitutes for vendor behavior proof. PF19 — Glow QA Guide, §3.5.6 PO Live QA sessions (vendor-first rails).  
* Any public or birth-facing compatibility path used for po-006 must not require the caller to supply `person_uid`. If strict compute remains internal, a sanctioned adapter boundary must supply deterministic internal metadata without making UID an external public input.  
* Direct compute tests, public Reader output, and internal/admin compat output must remain separate proof classes. The remediation must not “pass” po-006 by relabeling an internal/admin numeric payload as public output.  
* Vendor-backed OPS work must use explicit open rails only for the controlled vendor step, must capture presence-only secret posture, and must not persist secret values. PF04 — HDE-Governance, §3.4 Open rails (controlled); PF04 — HDE-Governance, §3.3 Secrets & env validation.  
* Governed evidence must remain under governed roots with coherent index/mirror/path-proof posture when promoted as governed evidence. PF12 — HDE Schemas & Artifacts, §8.3 Machine Evidence Index — JSONL mirror (records-only).  
* QA plan and remediation artifacts must not invent executable loci or rely on non-PF attachments for downstream execution. PF27 — Canon Plan Templates, §Purpose & scope \[Required−Now\].

Plan Alignment Snapshot

* The approved QA plan, as provided, is audit-style and identifies repo facts, ambiguity, and mismatch; it is not sufficient as an executable corrected po-006 QA plan block.  
* The po-006 expectation under review is to prove public user-facing compatibility output remains band-only and numeric-free.  
* The observed po-006 path used direct compatibility tests plus a grep for `public_reader_bands_only_numeric_free: True`.  
* The approved implementation plan defines HDE-EPIC030 as PR-only implementation work and explicitly leaves close-pack and close-stage QA outputs outside the implementation plan.  
* Overall alignment status: Conflicting, with an embedded ambiguity.  
* Conflict: the PO’s required real-test posture says vendor must be called in the current no-user environment, while the po-006 proof path under review is repo-local and can pass the numeric-free grep without proving live vendor-backed no-user behavior.  
* Ambiguity: the phrase “public user-facing compatibility output” is being tested through direct `compat_public` compute tests, while repo facts distinguish the public Reader output path from the internal/admin compat compute path.  
* Clarification needed: define whether po-006 is a public Reader numeric-free proof, a no-user public/birth-facing compatibility adapter proof, or a direct internal compute proof.  
* Resolution locations: QAP-01 resolves the QA proof split; DOC-01 records the no-user vendor proof posture; PR-01 resolves current repo boundary/source-skew facts; PR-02 implements the approved no-user boundary; OPS-01 and OPS-02 resolve and exercise the real vendor-backed command posture.

Observed Evidence Snapshot

The failure signature is self-contained: po-006 recorded `FAIL_BEHAVIOR`, `exit_code=1`, `pytest_rc=1`, `grep_rc=0`, and `public_reader_bands_only_numeric_free: True` was present. The exact pytest failure is `TypeError: compat_public() missing 5 required positional arguments: 'viewer_top', 'viewer_weights', 'engine_tag', 'release_id', and 'invocation_tag'`. The failing test named in evidence is `tests/compat/test_compat_public_lf_bom.py::test_public_bytes_lf_and_no_bom`.

The current compute signature reported by the codex audit is `compat_public(a, b, viewer_top, viewer_weights, engine_tag, release_id, invocation_tag)`. The UID ordering path is `engine/compat/ordering.py`, where `_uid` reads `person_uid`, raises `ValueError("invalid or missing person_uid")` when absent or invalid, and `normalize_pair(a, b)` calls `_uid` for both inputs.

The public Reader output path is reported as `engine/runtime/public.py`, `presenter/reader_v1/emitter.py`, `engine/presenter/emitter.py`, and `adapter/http_reader.py`. The internal/admin compat HTTP path is reported as `engine/http/compat_handler.py` mounted at `/api/compat/v1`, calling `compat_public(...)` and returning a compat payload including scores and keys. The endpoint catalog reportedly marks `/api/compat/v1` as `internal_admin`.

The operational discovery notes report Python 3.13.5, pytest 8.4.2, grep at `/usr/bin/grep`, a parsable po-006 primary header, and captured open rails: `SAFE_MODE=0`, `ALLOW_NETWORK=1`, `APP_ENV=dev`, `LC_ALL=C`, `LANG=C`, `TZ=UTC`. They also report that Step-0A discovery artifacts for po-015 were absent.

The current PO note states that a real test requires calling the vendor because there is not yet a way to store the person data in JSON or database. That statement is consistent with PF19’s pre-App/no-user QA posture and must be treated as an active remediation driver.

| Expectation | Source | Status | Embedded evidence excerpt | Why it matters | Execution handling |
| :---- | :---- | ----: | :---- | :---- | :---- |
| po-006 must prove public user-facing compatibility output remains band-only and numeric-free. | the escalation report and the approved QA plan | Supported | “Public user-facing compatibility output must remain band-only and free of numeric compatibility details.” | Establishes the target of the failed proof. | QA\_PLAN\_UPDATE |
| po-006 PASS requires pytest success, not only grep success. | the escalation report | Supported | “pytest exit code is 0” and observed `pytest_rc=1`. | The numeric-free grep can pass while the step still fails. | PR |
| Numeric-free marker is present. | the escalation report and operational discovery notes | Supported | `grep_rc=0`; `public_reader_bands_only_numeric_free: True`. | Confirms the failure is not simply a grep-marker absence. | None |
| Direct `compat_public` requires seven arguments. | the codex audit | Supported | `compat_public(a, b, viewer_top, viewer_weights, engine_tag, release_id, invocation_tag)`. | Explains the TypeError and current compute contract. | PR |
| Direct compat ordering requires `person_uid`. | the escalation report and codex audit | Supported | `_uid` reads `person_uid`; `normalize_pair` calls `_uid` for both inputs. | This conflicts with the no-user/birth-input expectation unless bounded internally. | PR |
| Real live behavior test requires vendor in current no-user posture. | current PO note and PF19 | Supported | “real test” requires “call the vendor” because person data is not stored in JSON or database. | This is the operational proof posture that was repeatedly missed. | QA\_PLAN\_UPDATE |
| Exact vendor-backed no-user command is known. | operational discovery notes | Missing | Help/command discovery did not prove an exact no-user vendor command. | Cannot run vendor behavior proof safely without exact command and secret-safe posture. | OPS |
| po-006 setup used closed rails. | escalation report and operational discovery notes | Unclear | Plan setup says closed rails; observed header captured `SAFE_MODE=0`, `ALLOW_NETWORK=1`. | Rails mismatch weakens proof interpretation and must be corrected in plan wording. | QA\_PLAN\_UPDATE |
| Step-0A discovery exists for baseline context. | operational discovery notes | Missing | `audit/qa/hde-epic030/checks/po-015/discovery.json exists: false`; `primary.log exists: false`. | The failed proof lacks required baseline context. | QA\_PLAN\_UPDATE |
| Public Reader path and internal/admin compat path are distinct. | the codex audit | Supported | Reader emits bands-only envelope; `/api/compat/v1` is internal/admin and emits scores/keys. | Prevents the fix from collapsing proof classes. | PR |
| Current failure artifact matches current checked-in test source. | the codex audit | Unclear | Logged failure shows `mod.compat_public(ca, cb)` while current test reportedly passes full args and injects `person_uid`. | Determines whether code change, test change, QA rerun, or stale evidence handling is needed. | PR |
| The approved implementation plan includes OPS/vendor proof. | the approved implementation plan | Missing | It says implementation is PR-only and no OPS tasks are required. | This is acceptable for implementation scope but insufficient for the real-test proof now being remediated. | OPS |
| The repeated vendor/no-user requirement is documented in a current, execution-facing place. | current PO note and provided inputs | Unclear | The PO states it has been repeatedly documented and disregarded; the current po-006 path still did not call vendor. | A DOC\_UPDATE is needed to prevent recurrence and make the correction visible. | DOC\_UPDATE |

Root Cause Analysis (RCA)

What went wrong:

po-006 tried to use a repo-local direct compatibility test lane as proof for a public user-facing numeric-free compatibility condition. That lane failed on current internal compute contract shape and UID-coupled ordering. The numeric-free grep marker passed, but it did not prove the required behavior. Separately, the plan did not encode the PO’s operational truth: in the current pre-App/no-user environment, a real compatibility behavior test must call the vendor because there is no stored person data in JSON or DB.

How it manifested:

* po-006 recorded `FAIL_BEHAVIOR`.  
* `pytest_rc=1`, `grep_rc=0`, `exit_code=1`.  
* The exact failure was the missing-arguments `compat_public()` TypeError.  
* UID coupling remains observable in `normalize_pair`.  
* Open rails were captured in the failed run even though the planned local proof posture expected closed rails.  
* The current test source may no longer match the recorded failing artifact.

Documentation ignored:

* The current PO note states that real testing requires a vendor call because no person data is stored in JSON or database.  
* PF19 states that in the current pre-App/no-user environment, live compat behavior tests must use vendor-backed birth/no-user inputs and must not rely on DB/app user IDs.  
* Evidence basis: the failed po-006 run did not establish a vendor-backed no-user behavior proof.

Documentation incorrect:

* The po-006 proof path treats direct `compat_public` testing as if it were sufficient for public user-facing output, while repo facts distinguish the public Reader output path from internal/admin compat compute.  
* Evidence basis: the codex audit reports Reader path and internal/admin compat path as separate, with `/api/compat/v1` classified as internal/admin.

Documentation missing:

* The exact vendor-backed no-user command is not embedded.  
* The exact acceptance split among public Reader numeric-free proof, internal/admin compat compute proof, and vendor-backed no-user behavior proof is not encoded.  
* Step-0A baseline discovery is absent.  
* Evidence basis: operational discovery found missing Step-0A artifacts and did not prove exact vendor command context.

Implementation mismatch:

* `compat_public` requires invocation metadata.  
* `normalize_pair` requires UID-backed ordering.  
* The public/birth-facing no-user contract is not clearly implemented or bounded at a sanctioned adapter boundary.  
* Evidence basis: failure trace and repo-surface audit.

Runtime/ops mismatch:

* The failed reproduction ran with `SAFE_MODE=0` and `ALLOW_NETWORK=1`, but that did not resolve the failure and was not the local closed-rails posture expected for the repo-local part of the proof.  
* The vendor-backed real-test lane was not executed because its exact command and operational prerequisites were not proven.  
* Evidence basis: operational discovery and current PO note.

Evidence/proof mismatch:

* The numeric-free grep passed while pytest failed.  
* Current source may differ from the logged failing test line, so the evidence family may be stale or source-skewed.  
* The failure was classified as behavior, not tooling, because pytest and grep ran and the failure was a contract break.  
* Evidence basis: escalation report and codex audit.

Planning ambiguity:

* The guide must choose whether public/birth-facing no-user compatibility is direct compute, a no-user adapter around strict compute, or a public Reader-only proof.  
* Evidence basis: the escalation report lists competing remediation directions, and the codex audit reports the public/admin boundary split.

QA plan defect:

* The current po-006 proof posture is incomplete for the PO’s real-test requirement.  
* It lacks an executable vendor-backed no-user step, exact rails posture split, exact command discovery posture, and clear failure classifications for missing vendor command or credentials.  
* Evidence basis: current PO note, PF19, and operational discovery.

Documentation drift:

* The repeated vendor/no-user requirement has not remained visible enough in the execution-facing plan layer to prevent recurrence.  
* Evidence basis: the PO note and the fact that the failed proof path still did not call vendor.

Remediation Work Plan

Non-executable PO-owned posture, outside this executable remediation task plan:

* QA plan wording correction for po-006 may proceed as a PO-owned prerequisite or follow-up. It is not a remediation work item in this Plan, and this Plan does not assign a QA\_PLAN\_UPDATE task.  
* The no-user/vendor documentation posture may be recorded as a PO-owned doc-delta candidate or later drainage item. It is not a remediation work item in this Plan, and this Plan does not assign a DOC\_UPDATE task.  
* Documentation drainage does not substitute for PR or OPS remediation and is not an execution deliverable, acceptance condition, QA PASS claim, or closure condition.  
* The executable remediation task plan below contains only PR and OPS work items.

### 6.1 Work Item Overview

| Work Item ID | Work item name | Work item type | Work item intent | Owner/role | Depends on | Cross-lane dependency | Outputs |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| OPS-01 | Discover exact vendor-backed no-user command and safe execution context | OPS | DISCOVERY | PO; Facilitator: IA | ADR-002 | None | `audit/ops/hde-epic030/ops-01/discovery_summary.md` and supporting captures |
| PR-01 | Read-only repo boundary and source-skew discovery | PR | DISCOVERY | Implementation Owner / Codex | ADR-001 | None | Codex read-only report; no repo artifact required |
| PR-02 | Remediate no-user compatibility boundary and po-006 proof tests | PR | CHANGE | Implementation Owner / Codex | PR-01, ADR-001 | Inputs needed from Work Item OPS-01 during implementation | Minimal repo diff; exact changed files determined by PR-01 discovery |
| OPS-02 | Execute controlled vendor-backed no-user implementation smoke when PF07 target facts are proven | OPS | CHANGE | PO; Facilitator: IA | OPS-01, PR-02, ADR-002 | Inputs needed from Work Item PR-02 during implementation | `audit/ops/hde-epic030/ops-02/result_summary.md` and supporting captures |

### 6.2 Work Item Details

Work Item ID: OPS-01

Work item name: Discover exact vendor-backed no-user command and safe execution context

Work item type (PR / OPS): OPS

Work item intent (DISCOVERY or CHANGE): DISCOVERY

Owner/role: PO

Facilitator: IA

Implementation agent:

OPS: PO manual

Target system/service:

* HD Engine CLI command surface in a PO-controlled repository workspace or QA console.  
* No live vendor call is authorized in this work item unless ADR-002 explicitly authorizes a discovery smoke and the exact no-secret command is proven first.  
* The discovery target is CLI/help/env posture only: `hdctl`, `hdctl --help`, `hdctl showcompat --help`, and presence-only environment posture.

Working directory assumptions:

* Repository root containing the HD Engine CLI.  
* The PO runs commands from the repository root unless the repository’s CLI invocation requires an already-proven alternate working directory.  
* No command may rely on an unproven path, host, port, URL, or service binding.

Preconditions:

* ADR-002 is approved before any live vendor call.  
* Do not print, store, or echo secret values.  
* Do not run a live vendor command in OPS-01 unless the command is proven and ADR-002 explicitly allows the discovery step to include a smoke call.

Inputs:

* Repo workspace with the HD Engine CLI available or discoverable.  
* PO-held environment secret posture, presence-only.  
* No secret values.

Canon constraints:

* PF07 — Glow Infrastructure, §2.4 Env Deployment Inventory Required−NowRequired-NowRequired−Now  
* PF07 — Glow Infrastructure, §4.1 HD Engine  
* PF07 — Glow Infrastructure, §8 Config keys & references (names \+ current values)  
* PF19 — Glow QA Guide, §3.3 Environment constraints — pre-App, no-user QA mode  
* PF19 — Glow QA Guide, §3.5.6 PO Live QA sessions (vendor-first rails)  
* PF04 — HDE-Governance, §3.3 Secrets & env validation \[Required-Now\]  
* PF04 — HDE-Governance, §3.4 Open rails (controlled) \[Required-Now\]

Observed Evidence / Findings (non-PF):

* A real behavior test requires the vendor because there is no stored person data in JSON or database.  
* Operational discovery found Python, pytest, and grep available.  
* Operational discovery found Step-0A po-015 discovery artifacts absent.  
* The failed po-006 run captured open rails but failed on contract shape.  
* The exact no-user vendor-backed command was not proven in the reviewed inputs.

Rollback intent:

* No external state change is intended.  
* If discovery captures are wrong, contaminated, or secret-bearing, discard or supersede the affected `audit/ops/hde-epic030/ops-01/` artifacts and rerun OPS-01 from a clean capture posture.  
* Do not attempt to roll back code, repo state, vendor state, or runtime state in OPS-01 because this work item is discovery-only.

Secret-handling posture:

* Capture only key names and presence booleans.  
* Never print or persist secret values.  
* Never inline secret values into `vendor_command_candidate.txt`.  
* Treat `HD_API_KEY`, `GEO_API_KEY`, and any other credential-like value as presence-only.  
* If any output contains a secret value, mark OPS-01 `FAIL_TOOLING`, quarantine the artifact path in `discovery_summary.md`, and do not use it as evidence.

Actions:

* Create `audit/ops/hde-epic030/ops-01/`.  
* Write every command actually run to `audit/ops/hde-epic030/ops-01/commands.txt`.  
* Capture tool preflight:  
  * `python --version > audit/ops/hde-epic030/ops-01/python_version.txt 2> audit/ops/hde-epic030/ops-01/python_version.stderr`  
  * `python -m pytest --version > audit/ops/hde-epic030/ops-01/pytest_version.txt 2> audit/ops/hde-epic030/ops-01/pytest_version.stderr`  
  * `command -v grep > audit/ops/hde-epic030/ops-01/grep_path.txt 2> audit/ops/hde-epic030/ops-01/grep_path.stderr`  
* Capture CLI availability and help without executing behavior:  
  * `command -v hdctl > audit/ops/hde-epic030/ops-01/hdctl_path.txt 2> audit/ops/hde-epic030/ops-01/hdctl_path.stderr`  
  * `hdctl --help > audit/ops/hde-epic030/ops-01/hdctl_help.txt 2> audit/ops/hde-epic030/ops-01/hdctl_help.stderr`  
  * `hdctl showcompat --help > audit/ops/hde-epic030/ops-01/showcompat_help.txt 2> audit/ops/hde-epic030/ops-01/showcompat_help.stderr`  
* Capture secret and rails presence only with a small Python script that writes `audit/ops/hde-epic030/ops-01/env_presence.json`. The script must include only key names and booleans for:  
  * `SAFE_MODE`  
  * `ALLOW_NETWORK`  
  * `APP_ENV`  
  * `LC_ALL`  
  * `LANG`  
  * `TZ`  
  * `HDE_BASE_URL`  
  * `HDAPI_BASE_URL`  
  * `HD_API_KEY`  
  * `GEO_API_KEY`  
* From CLI help and PF19 posture, determine whether a concrete no-user vendor-backed `showcompat` command can be written without guessing:  
  * It must use birth/no-user inputs.  
  * It must use an explicit vendor source.  
  * It must not use `--user-a`, `--user-b`, `--source=db`, app user IDs, or `person_uid`.  
  * It must not inline secret values.  
* Write the proposed command to `audit/ops/hde-epic030/ops-01/vendor_command_candidate.txt` only if exact flags and input shape are proven.  
* If exact flags or input shape are not proven, write exactly: `UNRESOLVED — exact vendor-backed no-user command not proven from CLI help and available canon`.  
* Write `audit/ops/hde-epic030/ops-01/discovery_summary.md` with:  
  * whether `hdctl` exists,  
  * whether `showcompat --help` exists,  
  * whether a concrete no-user vendor command was proven,  
  * whether required secret names are present, presence-only,  
  * whether the live vendor smoke remains blocked pending ADR-002 or command proof,  
  * whether no `person_uid` is required in the proposed command,  
  * whether any secret-bearing artifact was detected and quarantined.  
* Generate checksums:  
  * `find audit/ops/hde-epic030/ops-01 -type f ! -name files_sha256.txt -print | sort | xargs sha256sum > audit/ops/hde-epic030/ops-01/files_sha256.txt`

Expected output or success criteria:

* `discovery_summary.md` states either that a concrete no-user vendor command is proven or that command discovery is unresolved.  
* `vendor_command_candidate.txt` contains either a concrete no-secret command or the exact unresolved statement.  
* `env_presence.json` contains presence booleans only.  
* No live vendor call is performed unless ADR-002 explicitly permits it and the summary records that permission.

Failure handling:

* Missing `hdctl` or missing `showcompat --help` is `TOOLING_BLOCKED`.  
* Missing exact no-user vendor flags is `TOOLING_BLOCKED`.  
* Secret value capture is `FAIL_TOOLING`.  
* Any attempted live call without ADR-002 approval and exact command proof is `FAIL_TOOLING`.

Codex Prompt:

None — forbidden for OPS work items.

Outputs:

* `audit/ops/hde-epic030/ops-01/commands.txt`  
* `audit/ops/hde-epic030/ops-01/python_version.txt`  
* `audit/ops/hde-epic030/ops-01/python_version.stderr`  
* `audit/ops/hde-epic030/ops-01/pytest_version.txt`  
* `audit/ops/hde-epic030/ops-01/pytest_version.stderr`  
* `audit/ops/hde-epic030/ops-01/grep_path.txt`  
* `audit/ops/hde-epic030/ops-01/grep_path.stderr`  
* `audit/ops/hde-epic030/ops-01/hdctl_path.txt`  
* `audit/ops/hde-epic030/ops-01/hdctl_path.stderr`  
* `audit/ops/hde-epic030/ops-01/hdctl_help.txt`  
* `audit/ops/hde-epic030/ops-01/hdctl_help.stderr`  
* `audit/ops/hde-epic030/ops-01/showcompat_help.txt`  
* `audit/ops/hde-epic030/ops-01/showcompat_help.stderr`  
* `audit/ops/hde-epic030/ops-01/env_presence.json`  
* `audit/ops/hde-epic030/ops-01/vendor_command_candidate.txt`  
* `audit/ops/hde-epic030/ops-01/discovery_summary.md`  
* `audit/ops/hde-epic030/ops-01/files_sha256.txt`

Verification:

* `discovery_summary.md` exists and states whether a concrete no-user vendor command is proven.  
* `env_presence.json` contains presence booleans only and no secret values.  
* `vendor_command_candidate.txt` either contains a concrete no-secret command or the exact unresolved statement.  
* No live vendor call is run in OPS-01 unless explicitly authorized by ADR-002 and recorded as such.  
* `files_sha256.txt` exists and covers OPS-01 captured files.

In-flight determinations:

* Caveat: If `hdctl showcompat --help` is unavailable or lacks enough information to derive a no-user vendor command, vendor behavior proof remains TOOLING\_BLOCKED.  
* Owner: PO  
* Evidence trigger: `showcompat_help.stderr`, `vendor_command_candidate.txt`, and `discovery_summary.md`.  
* Safe default: do not run a vendor call.  
* Risk if unresolved: remediation may repair repo-local tests while still failing the PO’s real-test requirement.

ADR linkage:

ADR-002

Work Item ID: PR-01

Work item name: Read-only repo boundary and source-skew discovery

Work item type (PR / OPS): PR

Work item intent (DISCOVERY or CHANGE): DISCOVERY

Owner/role: Implementation Owner / Codex

Implementation agent:

PR: Codex PR

Preconditions:

* ADR-001 is approved or explicitly pending with discovery allowed.  
* Read-only only: no file edits, no tests, no vendor calls.

Inputs:

* Self-contained observed evidence in this Plan.  
* Repo checkout.

Canon constraints:

* PF02 — HDE Architecture, §3.1 Compat v1 \[Implemented\]  
* PF02 — HDE Architecture, §3.2 Reader v1 \[Required-Now\]  
* PF14 — HDE Mechanics Guide, §7.2 Compatibility Engine (pair) — contract  
* PF14 — HDE Mechanics Guide, §9.3 Compat (pair; internal/admin) \[Implemented (dev/admin)\]  
* PF19 — Glow QA Guide, §3.3 Environment constraints — pre-App, no-user QA mode

Observed Evidence / Findings (non-PF):

* po-006 failed with `FAIL_BEHAVIOR`, `exit_code=1`, `pytest_rc=1`, `grep_rc=0`.  
* `public_reader_bands_only_numeric_free: True` was present.  
* The TypeError was missing five required `compat_public` args.  
* UID ordering requires `person_uid`.  
* Current test source may differ from the failing artifact: logged failure shows a two-argument call while current source reportedly calls full args and injects `person_uid`.  
* Public Reader output path is separate from internal/admin compat compute path.

Actions:

* Perform read-only repo inspection only.  
* Confirm the current `compat_public` signature and first-order calls.  
* Confirm whether `normalize_pair` still requires `person_uid`.  
* Confirm all current direct callers of `compat_public`.  
* Confirm whether any existing public/birth-facing adapter provides a no-user compatibility path.  
* Confirm whether current `tests/compat/test_compat_public_lf_bom.py` and `tests/compat/test_compat_public_ab_ba_identity.py` prove no-user behavior or only inject `person_uid`.  
* Confirm public Reader vs internal/admin compat boundary.  
* Confirm endpoint catalog classification of `/api/compat/v1`.  
* Confirm source/evidence skew for po-006 by comparing logged traceback line shape to current test file content.

Codex Prompt:

You are Codex performing read-only discovery for HDE-EPIC030 po-006 remediation. Do not edit files. Do not run tests. Do not perform operational discovery. Do not call the vendor.

Observed Evidence / Findings:

* po-006 failed with status `FAIL_BEHAVIOR`.  
* Observed rc values: `exit_code=1`, `pytest_rc=1`, `grep_rc=0`.  
* Numeric-free marker was present: `public_reader_bands_only_numeric_free: True`.  
* Failure excerpt: `compat_public() missing 5 required positional arguments: 'viewer_top', 'viewer_weights', 'engine_tag', 'release_id', and 'invocation_tag'`.  
* Reported UID gate: `engine/compat/ordering.py` reads `person_uid` and raises `ValueError("invalid or missing person_uid")`; `normalize_pair` calls `_uid` for both inputs.  
* Reported current compute signature: `compat_public(a, b, viewer_top, viewer_weights, engine_tag, release_id, invocation_tag)`.  
* Reported public Reader path: `adapter/http_reader.py`, `engine/runtime/public.py`, `presenter/reader_v1/emitter.py`, and `engine/presenter/emitter.py`.  
* Reported internal/admin compat path: `engine/http/compat_handler.py` and `engine/compat/compute.py`; `/api/compat/v1` is reportedly classified as `internal_admin`.  
* Current source may be out of sync with the failed artifact: logged failure shows a two-argument `compat_public(ca, cb)` call, while current test source reportedly passes full args and injects `person_uid`.  
* User requirement: compatibility execution from chart/birth/vendor-derived payloads must not require the public caller to provide `person_uid`.

Read-only tasks:

1. Inspect `engine/compat/compute.py` and list the exact `compat_public` signature and direct first-order calls.  
2. Inspect `engine/compat/ordering.py` and determine whether `person_uid` is required for pair normalization.  
3. Search for all direct `compat_public(` callers and classify them as CLI, HTTP/internal/admin, test, public Reader, or other.  
4. Inspect `tests/compat/test_compat_public_lf_bom.py` and `tests/compat/test_compat_public_ab_ba_identity.py` and determine whether they prove no-user behavior or rely on injected `person_uid`.  
5. Inspect `adapter/http_reader.py`, `engine/runtime/public.py`, `presenter/reader_v1/emitter.py`, `engine/presenter/emitter.py`, and `engine/http/compat_handler.py` to map public Reader vs internal/admin compat boundary.  
6. Inspect `docs/ENDPOINTS_CATALOG.json` to confirm `/api/compat/v1` classification and whether it is public or internal/admin.  
7. Inspect po-006 evidence files under `audit/qa/hde-epic030/checks/po-006/` if present to compare logged traceback against current source line maps.  
8. Identify minimal safe change loci for a no-user public/birth-facing compatibility boundary.  
9. Identify risks to avoid, especially fixture-only `person_uid` injection, public numeric output, public route creation, new flags, or collapsing internal/admin compat into public Reader proof.

Return a report with exactly these sections:  
 A. Current source facts  
 B. Evidence/source skew check  
 C. Public Reader vs internal/admin compat boundary  
 D. No-user compatibility gap  
 E. Minimal safe change loci  
 F. Risks to avoid  
 G. Targeted tests/checks recommended after change

Constraints:

* Read-only repo inspection only.  
* No edits.  
* No tests.  
* No vendor calls.  
* No operational discovery.  
* No PF canon edits.  
* No new routes or flags.  
* Do not recommend fixture-only `person_uid` injection as the no-user fix.

Outputs:

Unknown — PR DISCOVERY is read-only and produces a Codex report in the agent response; no repository artifact is created by this work item.

Verification:

* Codex report includes current source facts for compute signature, UID ordering, public Reader path, internal/admin compat path, endpoint classification, and current test behavior.  
* Report identifies whether the failing evidence is stale relative to current source.  
* Report identifies minimal change loci for PR-02.  
* Report does not recommend OPS work, QA reruns, PF edits, or vendor calls.

In-flight determinations:

* Caveat: If PR-01 proves direct `compat_public` is internal-only, PR-02 must implement or enforce a no-user public/birth-facing adapter boundary rather than making internal compute itself the public proof.  
* Owner: Implementation Owner  
* Evidence trigger: PR-01 report sections C, D, and E.  
* Safe default: preserve internal/admin numeric compat boundaries and do not widen public output.  
* Risk if unresolved: PR-02 may fix a stale test artifact while leaving the real no-user boundary broken.

ADR linkage:

ADR-001

Work Item ID: PR-02

Work item name: Remediate no-user compatibility boundary and po-006 proof tests

Work item type (PR / OPS): PR

Work item intent (DISCOVERY or CHANGE): CHANGE

Owner/role: Implementation Owner / Codex

Implementation agent:

PR: Codex PR

Preconditions:

* PR-01 read-only discovery is complete.  
* ADR-001 is approved.  
* Do not run vendor calls.  
* Do not perform OPS tasks.  
* Do not edit PF canon.

Inputs:

* PR-01 read-only report.  
* Self-contained observed evidence in this Plan.  
* Optional OPS-01 discovery summary, if available, for awareness of vendor command posture only.

Inputs needed from Work Item OPS-01 during implementation:

* Optional awareness only: `audit/ops/hde-epic030/ops-01/discovery_summary.md`, if available.  
* Optional awareness only: `audit/ops/hde-epic030/ops-01/vendor_command_candidate.txt`, if available.  
* Otherwise: None.

Inputs needed from Work Item PR-01 during implementation:

* PR-01 Codex read-only report sections A through G.

Canon constraints:

* PF02 — HDE Architecture, §3.1 Compat v1 \[Implemented\]  
* PF02 — HDE Architecture, §3.2 Reader v1 \[Required-Now\]  
* PF14 — HDE Mechanics Guide, §7.2 Compatibility Engine (pair) — contract  
* PF14 — HDE Mechanics Guide, §9.3 Compat (pair; internal/admin) \[Implemented (dev/admin)\]  
* PF19 — Glow QA Guide, §3.3 Environment constraints — pre-App, no-user QA mode  
* PF12 — HDE Schemas & Artifacts, §8.3 Machine Evidence Index — JSONL mirror (records-only), if governed evidence artifacts change

Observed Evidence / Findings (non-PF):

* po-006 failed because direct compatibility compute/test invocation lacked required args.  
* UID ordering currently requires `person_uid`.  
* The numeric-free marker was present, so the failure was not only public numeric leakage.  
* Public Reader output and internal/admin compat compute are distinct surfaces.  
* Current evidence may be stale relative to current tests.  
* The user requirement is that compatibility should not require a UID to run.

Actions:

* Reuse existing repo surfaces and keep the diff minimal.  
* Use PR-01 discovery to choose the smallest implementation path under ADR-001:  
  * direct no-user compatibility compute path, or  
  * strict internal compute retained behind a sanctioned no-user public/birth-facing adapter boundary.  
* Do not satisfy no-user behavior by adding fixture-only `person_uid` values in tests.  
* Do not introduce public numeric output.  
* Do not create a new public route.  
* Do not add a new flag.  
* Do not collapse internal/admin compat JSON into public Reader output.  
* Ensure the public/birth-facing path used for po-006 can run from chart/birth/vendor-derived payloads without caller-provided `person_uid`.  
* Preserve AB↔BA identity and two-run identity.  
* Update tests so po-006 proof tests fail if the public/birth-facing path requires `person_uid`.  
* If governed evidence artifacts are changed or generated, refresh Human Index, Machine Mirror, hash sentinel, and sibling path proofs through canonical tooling.

Codex Prompt:

You are Codex implementing HDE-EPIC030 po-006 remediation after read-only discovery.

Observed Evidence / Findings:

* po-006 failed with status `FAIL_BEHAVIOR`.  
* Observed rc values: `exit_code=1`, `pytest_rc=1`, `grep_rc=0`.  
* Numeric-free marker was present: `public_reader_bands_only_numeric_free: True`.  
* Failure excerpt: `compat_public() missing 5 required positional arguments: 'viewer_top', 'viewer_weights', 'engine_tag', 'release_id', and 'invocation_tag'`.  
* UID gate evidence: pair ordering currently requires `person_uid`; missing or invalid `person_uid` raises `ValueError("invalid or missing person_uid")`.  
* Public Reader output and internal/admin compat compute are separate proof classes.  
* User requirement: compatibility execution from chart/birth/vendor-derived payloads must not require the public caller to provide `person_uid`.  
* Current pre-App/no-user reality: live behavior proof uses vendor-backed birth/no-user inputs; do not rely on app user IDs or DB-backed BodyGraphs as public behavior proof.  
* Current source may not match the failed artifact, so verify before editing.

Goal:  
 Implement the smallest repo change that makes the po-006 no-user public/birth-facing compatibility boundary coherent while preserving public numeric-free output and internal/admin compat boundaries.

Discovery-first requirements:

1. Reconfirm the current `compat_public` signature and all direct callers.  
2. Reconfirm whether `compat_public` is internal compute or a public/birth-facing API.  
3. Reconfirm UID ordering behavior in `engine/compat/ordering.py`.  
4. Reconfirm public Reader path vs internal/admin compat path.  
5. Reconfirm current behavior of `tests/compat/test_compat_public_lf_bom.py` and `tests/compat/test_compat_public_ab_ba_identity.py`.  
6. Choose the smallest implementation path consistent with this rule: the public/birth-facing compatibility path used for po-006 must not require caller-provided `person_uid`.

Implementation requirements:

* Reuse existing modules and adapters first.  
* Keep the diff minimal.  
* Preserve AB↔BA identity and two-run identity.  
* Preserve canonical JSON and LF/BOM posture.  
* Preserve public Reader bands-only numeric-free output.  
* Preserve internal/admin-only status for numeric compat payloads.  
* Do not add a public route.  
* Do not add a public flag.  
* Do not edit PF canon.  
* Do not run vendor calls.  
* Do not do OPS work.  
* Do not solve the issue with fixture-only `person_uid` injection.

Likely loci to inspect before editing:

* `engine/compat/compute.py`  
* `engine/compat/ordering.py`  
* `engine/http/compat_handler.py`  
* `adapter/http_reader.py`  
* `engine/runtime/public.py`  
* `presenter/reader_v1/emitter.py`  
* `engine/presenter/emitter.py`  
* `tests/compat/test_compat_public_lf_bom.py`  
* `tests/compat/test_compat_public_ab_ba_identity.py`  
* any additional caller/test loci discovered by searching for `compat_public(` and `person_uid`

Minimum targeted tests/checks after change:

* `python -m pytest -q tests/compat/test_compat_public_lf_bom.py tests/compat/test_compat_public_ab_ba_identity.py`  
* Add or run adjacent targeted tests discovered by source inspection when they cover the changed no-user boundary.  
* If governed evidence artifacts change, run the existing canonical evidence refresh flow and check mode.  
* Do not run Live QA.  
* Do not call the vendor.  
* Do not generate close-pack artifacts.

Evidence outputs to produce:

* Exact changed files are determined by PR-01 and the minimal PR-02 diff.  
* If governed evidence changes, refresh:  
  * `docs/evidence/INDEX.json`  
  * `docs/evidence/INDEX.sha256`  
  * `artifacts/evidence_index.jsonl`  
  * `artifacts/evidence_index.jsonl.sha256`  
  * affected sibling `.path_proof.txt` files

Return a report with:

1. Files changed.  
2. Contract decision implemented.  
3. How no-user public/birth-facing behavior is proven without `person_uid`.  
4. How AB↔BA identity is preserved.  
5. How public numeric-free posture is preserved.  
6. Commands run and results.  
7. Remaining OPS-only vendor validation needed.

Outputs:

* Exact changed files: Unknown — determined by PR-01 and the minimal PR-02 diff.  
* Candidate loci if change is needed:  
  * `engine/compat/compute.py`  
  * `engine/compat/ordering.py`  
  * `engine/http/compat_handler.py`  
  * `adapter/http_reader.py`  
  * `engine/runtime/public.py`  
  * `tests/compat/test_compat_public_lf_bom.py`  
  * `tests/compat/test_compat_public_ab_ba_identity.py`  
* If governed evidence changes:  
  * `docs/evidence/INDEX.json`  
  * `docs/evidence/INDEX.sha256`  
  * `artifacts/evidence_index.jsonl`  
  * `artifacts/evidence_index.jsonl.sha256`  
  * affected sibling `.path_proof.txt` files

Verification:

* Targeted compatibility pytest command exits `0`.  
* The missing-arguments `compat_public()` TypeError is absent.  
* The public/birth-facing no-user test path does not require caller-provided `person_uid`.  
* Public numeric-free posture remains intact.  
* Internal/admin numeric compat output remains bounded to internal/admin surfaces.  
* Any changed governed evidence is coherent through Human Index, Machine Mirror, hash sentinel, and path proofs.  
* PR-02 report names any remaining OPS-only vendor validation.

In-flight determinations:

* Caveat: If PR-01 proves current po-006 evidence is stale but current tests already pass, PR-02 must still address whether tests prove no-user behavior rather than only full-arg plus `person_uid` compatibility.  
* Owner: Implementation Owner  
* Evidence trigger: PR-01 source-skew check and PR-02 targeted tests.  
* Safe default: preserve internal/admin numeric compat boundaries and do not widen public output.  
* Risk if unresolved: the repo may appear green while the PO’s real no-user/vendor requirement remains unproven.

ADR linkage:

ADR-001

Work Item ID: OPS-02

Work item name: Execute controlled vendor-backed no-user implementation smoke when PF07 target facts are proven

Work item type (PR / OPS): OPS

Work item intent (DISCOVERY or CHANGE): CHANGE

Owner/role: PO

Facilitator: IA

Implementation agent:

OPS: PO manual

Target system/service:

* PF07-backed execution target for the PR-02-remediated HD Engine runtime.  
* Current blocker: the exact PF07 target fact set is not proven in this Plan.  
* Missing PF07 fact set:  
  * target environment name for the vendor-backed smoke,  
  * service/base URL or CLI execution context for the remediated HD Engine runtime,  
  * deployment, branch, or build binding that proves PR-02 is available on the target,  
  * authorized open-rails vendor credential source, presence-only,  
  * required target-specific environment bindings for the no-user vendor command.  
* Until those PF07 facts are supplied, OPS-02 is `TOOLING_BLOCKED` and must not execute a vendor smoke.

Working directory assumptions:

* Repository root or PF07-backed CLI execution context, only after PF07 target facts are supplied.  
* If PF07 does not prove the working directory or execution context, write the blocked summary and stop.

Preconditions:

* ADR-002 is approved.  
* OPS-01 produced a concrete no-secret vendor command or explicitly recorded it as unresolved.  
* PR-02 report confirms the repo-local remediation and targeted tests.  
* PF07-backed target facts listed above are proven before any vendor smoke runs.  
* This is implementation validation only, not a QA rerun and not a closure decision.

Inputs:

* `audit/ops/hde-epic030/ops-01/vendor_command_candidate.txt`  
* `audit/ops/hde-epic030/ops-01/discovery_summary.md`  
* PR-02 report confirming targeted tests passed.  
* PF07-backed target fact set for the remediated runtime.  
* PO-held secret values, presence-only.

Inputs needed from Work Item PR-02 during implementation:

* PR-02 report confirming targeted tests passed.  
* PR-02 report naming any runtime command or no-user compatibility surface to exercise.  
* If PR-02 reports no executable runtime surface, classify OPS-02 as TOOLING\_BLOCKED rather than inventing one.

Canon constraints:

* PF07 — Glow Infrastructure, §0 Front Matter  
* PF19 — Glow QA Guide, §3.3 Environment constraints — pre-App, no-user QA mode  
* PF19 — Glow QA Guide, §3.5.6 PO Live QA sessions (vendor-first rails)  
* PF04 — HDE-Governance, §3.4 Open rails (controlled) \[Required-Now\]  
* PF04 — HDE-Governance, §3.3 Secrets & env validation \[Required-Now\]  
* PF12 — HDE Schemas & Artifacts, §8.3 Machine Evidence Index — JSONL mirror (records-only), if later promoted as governed evidence

Observed Evidence / Findings (non-PF):

* The PO states real compatibility behavior testing requires the vendor because no person data is stored in JSON or database.  
* The failed po-006 path did not establish vendor-backed no-user behavior.  
* The failed open-rails reproduction still failed locally because of compute/test contract shape.  
* OPS-02 is needed after PR remediation to prove the implementation can run in the current real no-user posture.  
* The Plan does not currently prove the PF07 target facts needed to bind PR-02 availability to a runtime target.

Rollback intent:

* No persistent vendor, DB, or app-user state change is intended.  
* If the command runs and fails, do not retry by changing flags, inputs, hostnames, ports, URLs, or credentials unless those changes are PF07-backed and recorded in `result_summary.md`.  
* If the smoke produces contaminated or secret-bearing output, mark `FAIL_TOOLING`, quarantine the affected artifact path in `result_summary.md`, and do not use the artifact as evidence.  
* If the smoke cannot run because PF07 target facts are missing, record `TOOLING_BLOCKED` and stop without touching external state.

Secret-handling posture:

* Use secret values only as runtime environment values supplied by the PO.  
* Do not write secret values to command files, logs, summaries, stderr, stdout, JSON, checksums, or environment snapshots.  
* `redacted_env_presence.json` must contain only key names and presence booleans.  
* Any command string containing a secret value is invalid and must not be executed.

Actions:

* Create `audit/ops/hde-epic030/ops-02/`.  
* Copy the command candidate:  
  * `cp audit/ops/hde-epic030/ops-01/vendor_command_candidate.txt audit/ops/hde-epic030/ops-02/vendor_command.txt`  
* If `vendor_command.txt` contains `UNRESOLVED`, write `TOOLING_BLOCKED — exact vendor-backed no-user command unresolved` to `audit/ops/hde-epic030/ops-02/result_summary.md` and do not run a vendor call.  
* If the PF07 target fact set is missing, write `TOOLING_BLOCKED — PF07 target facts missing: target environment name; service/base URL or CLI execution context; PR-02 deployment or build binding; authorized open-rails vendor credential source; target-specific environment bindings` to `audit/ops/hde-epic030/ops-02/result_summary.md` and do not run a vendor call.  
* If `vendor_command.txt` contains inline secret values, write `FAIL_TOOLING — command contains secret value inline` to `audit/ops/hde-epic030/ops-02/result_summary.md` and do not run a vendor call.  
* Set rails for the vendor smoke only after command and PF07 target facts are proven:  
  * `SAFE_MODE=0`  
  * `ALLOW_NETWORK=1`  
  * `APP_ENV=dev`  
  * `LC_ALL=C`  
  * `LANG=C`  
  * `TZ=UTC`  
* Run the exact command in `vendor_command.txt` only after confirming it is no-secret, no-user, and PF07-target-bound:  
  * `set +e; SAFE_MODE=0 ALLOW_NETWORK=1 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC sh -lc "$(cat audit/ops/hde-epic030/ops-02/vendor_command.txt)" > audit/ops/hde-epic030/ops-02/stdout.json 2> audit/ops/hde-epic030/ops-02/stderr.log; printf "%s\n" "$?" > audit/ops/hde-epic030/ops-02/exit_code.txt`  
* Capture redacted environment presence to `audit/ops/hde-epic030/ops-02/redacted_env_presence.json`.  
* Write `audit/ops/hde-epic030/ops-02/request_summary.txt` stating:  
  * command source was OPS-01,  
  * no `person_uid` was present in command inputs,  
  * no app user IDs were used,  
  * vendor source was explicit,  
  * PF07 target facts used, names-only,  
  * secrets were not stored.  
* If `stdout.json` exists, generate:  
  * `sha256sum audit/ops/hde-epic030/ops-02/stdout.json > audit/ops/hde-epic030/ops-02/stdout.json.sha256`  
* Write `audit/ops/hde-epic030/ops-02/result_summary.md` with:  
  * status: PASS, FAIL\_BEHAVIOR, FAIL\_TOOLING, or TOOLING\_BLOCKED,  
  * exit code if command ran,  
  * whether no-user inputs were used,  
  * whether vendor source was explicit,  
  * whether PF07 target facts were proven,  
  * whether output was produced,  
  * whether secrets were avoided,  
  * statement that this is not a QA rerun or closure verdict.  
* Generate:  
  * `find audit/ops/hde-epic030/ops-02 -type f ! -name files_sha256.txt -print | sort | xargs sha256sum > audit/ops/hde-epic030/ops-02/files_sha256.txt`

Expected output or success criteria:

* If PF07 target facts are missing, `result_summary.md` records `TOOLING_BLOCKED` and no vendor call runs.  
* If command proof is missing, `result_summary.md` records `TOOLING_BLOCKED` and no vendor call runs.  
* If command and PF07 target facts are proven and the command runs, `exit_code.txt`, `request_summary.txt`, and `result_summary.md` state the observed outcome without claiming QA PASS or closure.  
* No secret values are persisted.

Failure handling:

* Missing vendor credentials, missing exact command, or missing PF07 target facts is `TOOLING_BLOCKED`.  
* Inline secrets or secret-bearing output is `FAIL_TOOLING`.  
* Runtime output contradicting expected no-user vendor behavior after command and PF07 target facts are proven is `FAIL_BEHAVIOR`.  
* Do not modify the command or target by guesswork to force a PASS.

Codex Prompt:

None — forbidden for OPS work items.

Outputs:

* `audit/ops/hde-epic030/ops-02/vendor_command.txt`  
* `audit/ops/hde-epic030/ops-02/stdout.json`  
* `audit/ops/hde-epic030/ops-02/stderr.log`  
* `audit/ops/hde-epic030/ops-02/exit_code.txt`  
* `audit/ops/hde-epic030/ops-02/redacted_env_presence.json`  
* `audit/ops/hde-epic030/ops-02/request_summary.txt`  
* `audit/ops/hde-epic030/ops-02/stdout.json.sha256`  
* `audit/ops/hde-epic030/ops-02/result_summary.md`  
* `audit/ops/hde-epic030/ops-02/files_sha256.txt`

Verification:

* `result_summary.md` exists and reports PASS, FAIL\_BEHAVIOR, FAIL\_TOOLING, or TOOLING\_BLOCKED.  
* `result_summary.md` states whether PF07 target facts were proven.  
* `exit_code.txt` exists if the command ran.  
* `request_summary.txt` states no `person_uid`, no app user ID, and explicit vendor source.  
* `redacted_env_presence.json` contains no secret values.  
* If the smoke ran, `stdout.json` is non-empty and hash-captured.  
* The work item does not claim QA PASS, Live QA completion, or epic closure.

In-flight determinations:

* Caveat: Missing vendor credentials, exact command, or PF07 target facts should be TOOLING\_BLOCKED, not FAIL\_BEHAVIOR.  
* Owner: PO  
* Evidence trigger: `vendor_command.txt`, `redacted_env_presence.json`, `request_summary.txt`, `exit_code.txt`, and `result_summary.md`.  
* Safe default: do not run a vendor call until exact command and PF07 target facts are proven.  
* Risk if unresolved: local repo tests may pass without proving the actual current no-user/vendor behavior required by the PO.

ADR linkage:

ADR-002

PF Docs Consulted

PF10 — HDE-Build Notes

PF02 — HDE Architecture

PF04 — HDE-Governance

PF07 — Glow Infrastructure

PF12 — HDE Schemas & Artifacts

PF14 — HDE Mechanics Guide

PF19 — Glow QA Guide

PF23 — Reality Audits

PF27 — Canon Plan Templates

ADRs Requiring Thoth Approval

ADR ID: ADR-001

Title: po-006 no-user compatibility proof authority and boundary

Type:

QA PLAN AUTHORITY DECISION

Status:

PROPOSED (pending Thoth approval)

Context:

po-006 failed with `FAIL_BEHAVIOR`, `pytest_rc=1`, and a missing-arguments `compat_public()` TypeError while the numeric-free marker was present. Repo facts distinguish public Reader output from internal/admin compat compute. Ordering remains UID-coupled. The PO requires real no-user behavior testing through vendor because person data is not stored in JSON or database.

Decision:

Approve a corrected po-006 authority model: public numeric-free output proof, internal/admin compat compute proof, and vendor-backed no-user behavior proof are separate proof classes. The public/birth-facing compatibility path must not require caller-provided `person_uid`. Strict compute may remain internal only if a sanctioned no-user adapter boundary supplies deterministic internal metadata before compute.

Consequences:

* PR-01 can inspect the repo boundary without changing files.  
* PR-02 can implement the minimal approved boundary.  
* Fixture-only `person_uid` injection is not sufficient remediation.  
* PO-owned QA plan correction may proceed as a non-execution precondition or follow-up outside this remediation task plan.  
* PO-owned documentation drainage may be recorded later as a non-blocking doc-delta candidate outside this remediation task plan.  
* This ADR does not create a new public route, new public flag, new acceptance token, QA PASS, or closure decision.

Implementation notes:

* Work Item IDs that depend on it: PR-01, PR-02.  
* Evidence confirming adoption: PR-01 boundary report, PR-02 targeted test report, and absence of caller-provided `person_uid` from the public/birth-facing no-user proof.  
* This ADR changes QA plan posture and implementation-boundary selection. It does not change final PASS criteria except to require the real no-user/vendor proof class to be explicit.  
* This ADR does not make QA plan edits, PF10 addenda, documentation drainage, or PF-canon edits executable remediation work.

ADR ID: ADR-002

Title: Controlled vendor-backed no-user smoke for po-006 remediation

Type:

OPS POSTURE DECISION

Status:

PROPOSED (pending Thoth approval)

Context:

The PO states that real behavior testing requires calling the vendor because person data is not stored in JSON or database. PF19 supports vendor-backed no-user behavior proof in the pre-App environment. The failed po-006 run did not prove vendor-backed no-user behavior, and the exact command is currently unproven.

Decision:

Approve a controlled PO manual vendor-backed no-user smoke after command discovery and PR remediation. The smoke must use explicit open rails only for the vendor step, use no app user IDs or `person_uid`, store no secret values, and classify missing command or credentials as TOOLING\_BLOCKED or FAIL\_TOOLING rather than behavior failure.

Consequences:

* OPS-01 can discover exact command and secret presence posture.  
* OPS-02 can execute the controlled smoke only if exact command and safe posture are proven.  
* If exact command or credentials remain unavailable, the guide records TOOLING\_BLOCKED rather than fabricating a behavior verdict.  
* The smoke is implementation validation only; it is not a QA rerun, Live QA plan, closure decision, or substitute for po-006 final QA.

Implementation notes:

* Work Item IDs that depend on it: OPS-01, OPS-02.  
* Evidence confirming adoption: `audit/ops/hde-epic030/ops-01/vendor_command_candidate.txt`, `audit/ops/hde-epic030/ops-01/discovery_summary.md`, `audit/ops/hde-epic030/ops-02/request_summary.txt`, `audit/ops/hde-epic030/ops-02/exit_code.txt`, and `audit/ops/hde-epic030/ops-02/result_summary.md`.  
* This ADR changes sequencing and OPS posture. It does not authorize public-surface widening, PF edits, acceptance-token creation, or closure claims.

ASK OK?  
