Epic ID: HDE-EPIC036
Plan type: Live QA Plan / Runbook
Execution venue: Codespaces
Target environment: dev, plus one bounded PO-approved live-target configuration check in PO-010
Plan revision: r1
Date (UTC): 2026-07-02
Operators (names-only): PO, Kronos

#### Canon precedence statement

“PF10 supersedes all other PF docs where it speaks; otherwise follow PF-Canon.”

#### Canon set

Canon set:

* PF10 — HDE-Build Notes; relevant addenda: PR-01 HDE-EPIC036, PR-02 HDE-EPIC036, Implementation Retrospective HDE-EPIC036
* PF19 — Glow QA Guide
* PF27 — Canon Plan Templates
* PF05 — HDE CLI/API Vendor Reference
* PF02 — HDE Architecture
* PF23 — Reality Audits

### Scope statement

This plan evaluates the following in-scope surfaces / checks:

* Step-0B — Doc Delta Capture
* PO-001 — configured-v2 bg:resolve refusal before accidental legacy-style vendor request
* PO-002 — unsupported configured-v2 policy vs explicit legacy fallback distinction
* PO-003 — simple v2 chart success does not prove complete BodyGraph detail
* PO-004 — no claim that v2 chart data feeds BodyGraph/person/cache/compatibility flows
* PO-005 — explicit legacy fallback preserved only for non-v2 configured bases
* PO-006 — secret-safe behavior and no uncontrolled raw vendor payload persistence
* PO-007 — separation of implementation evidence, operational observation, QA evidence, status movement, and closeout
* PO-008 — coherent route-policy, BodyGraph-detail sufficiency, runtime nonclaim, and policy-binding proof set
* PO-009 — no public product behavior, new public transport behavior, app-side vendor ownership, full vendor runtime conformance, raw payload persistence, or AI scope claims
* PO-010 — bounded live production-like route-policy proof, using PO-approved live v2 base configuration and no secret capture
* PO-011 — bounded live proof demonstrates route-policy behavior without overclaiming broader runtime compatibility
* PO-012 — future work must not use this epic’s evidence to claim full BodyGraph-detail compatibility without later internal coverage proof
* qa-13-governed-evidence-gates — governed repo evidence, tests, indexes, mirrors, hashes, path proofs, canonical JSON, and LF gates
* qa-14-close-out-deliverables — PF27 closeout execution deliverables

This plan explicitly excludes:

* OPS execution
* live vendor observation that sends a BodyGraph request
* PF09 status movement
* HDE-FERM008 parent Done
* epic closeout
* PO closeout
* branch, commit, PR, merge, or release workflow
* PF document edits
* public Reader changes
* new public routes, flags, payloads, transport, or HTTP homes
* app-side HumanDesignAPI credential ownership
* raw request, raw response, raw vendor payload, or secret persistence
* AI scope
* full HumanDesignAPI v2 runtime conformance

#### PF10 overrides / conflicts

PF10 records that HDE-EPIC036 affects CLI behavior and vendor ingestion / vendor route-policy behavior, so this plan includes a bounded open-rails live QA step. The selected live step proves configured-v2 route-policy refusal using a PO-approved live base value while avoiding live vendor request construction and avoiding full runtime-conformance claims.

### Open-Rails Live QA Requirement for production-affecting epics

This plan includes one bounded open-rails live QA step:

* Check ID: po-010
* Production-relevant behavior proved: `bg:resolve --source vendor` configured-v2 route-policy refusal before accidental legacy BodyGraph request construction
* Live target: PO-approved HumanDesignAPI v2 base URL, supplied only inside PO-010 Variable Import as `HD_API_BASE_URL`
* Rails posture: `SAFE_MODE=0`, `ALLOW_NETWORK=1`, `APP_ENV=dev`, with no secret values captured
* Secret-safety posture: no `HD_API_KEY`, `GEO_API_KEY`, or vendor response payload is required or logged for the proof; the expected behavior is refusal before request construction
* Evidence to capture: `audit/qa/hde-epic036/checks/po-010/live_route_policy.log`, sibling path proof, and `primary.log`
* What the live step proves: the operator-facing CLI route-policy behavior refuses configured-v2 BodyGraph resolution as `PROVIDER_ROUTE_UNSUPPORTED` / `unsupported_runtime_nonclaim`
* What the live step does not prove: full vendor runtime conformance, BodyGraph-detail compatibility, charts/simple compatibility, public Reader behavior, OPS completion, PF09 status movement, or epic closeout

### PF23 anchors

PF23 was treated as planning-time repo-reality context only. PF23 is not a deliverable, not a required check, not an acceptance token, not an execution artifact, and not an operator command source.

### Environment and rails posture

#### Determinism pins

When producing governed bytes, use:

* `LC_ALL=C`
* `LANG=C`
* `TZ=UTC`

#### Default rails posture

Default rails for this runbook:

* `SAFE_MODE=1`
* `ALLOW_NETWORK=0`
* `APP_ENV=dev`

Rails changes by check:

* `po-010` → `SAFE_MODE=0`, `ALLOW_NETWORK=1`, `APP_ENV=dev` → required for bounded live production-like route-policy proof → produces `live_route_policy.log`, path proof, and primary log
* all other checks → closed rails: `SAFE_MODE=1`, `ALLOW_NETWORK=0`, `APP_ENV=dev`

### Stable QA root

Use the stable canonical epic QA root:

`audit/qa/hde-epic036/`

Use check-centric paths under:

`audit/qa/hde-epic036/checks/<check-id>/`

Do not use `EVIDENCE_ROOT`.
Do not use per-run root selection.
Do not use run-id directories.

### Evidence posture

Every check produces one primary step log:

`audit/qa/hde-epic036/checks/<check-id>/primary.log`

Every primary step log must have a sibling path proof:

`audit/qa/hde-epic036/checks/<check-id>/primary.log.path_proof.txt`

Step logs must use schema label:

`pf27.step_log_header.v1`

Each primary log header must include:

* `schema_version`
* `timestamp_utc`
* `check_id`
* `check_name`
* `status`
* `fail_status`
* `command`
* `command_provenance`
* `exit_code`
* `evidence_artifacts`
* `captured_env`
* `pf_refs`
* `intended_tokens`
* `claimed_tokens`

The Step-0B QA helper created by this plan emits that header contract consistently for every check.

### Runbook Check Matrix

| Order | Check ID                      | Step name                   | Rails              | Main proof target                                              | Primary deliverable                                                     | Intended tokens                                                                                                                                                                          |
| ----: | ----------------------------- | --------------------------- | ------------------ | -------------------------------------------------------------- | ----------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|     0 | step-0b-doc-delta-capture     | Step-0B — Doc Delta Capture | closed             | doc-delta surfaces and QA helper                               | `audit/qa/hde-epic036/checks/step-0b-doc-delta-capture/primary.log`     | `DOC_DELTA_PRESENT_OK`                                                                                                                                                                   |
|     1 | po-001                        | PO-001                      | closed             | configured-v2 refusal before accidental legacy request         | `audit/qa/hde-epic036/checks/po-001/primary.log`                        | `NO_EXTERNAL_IO_ON_REFUSAL_OK`                                                                                                                                                           |
|     2 | po-002                        | PO-002                      | closed             | unsupported v2 vs explicit legacy fallback distinction         | `audit/qa/hde-epic036/checks/po-002/primary.log`                        | `ENV_RAILS_POLICY_OK`                                                                                                                                                                    |
|     3 | po-003                        | PO-003                      | closed             | simple v2 chart success does not prove BodyGraph detail        | `audit/qa/hde-epic036/checks/po-003/primary.log`                        | none                                                                                                                                                                                     |
|     4 | po-004                        | PO-004                      | closed             | no v2 chart data compatibility overclaim                       | `audit/qa/hde-epic036/checks/po-004/primary.log`                        | none                                                                                                                                                                                     |
|     5 | po-005                        | PO-005                      | closed             | explicit legacy fallback only for non-v2 base                  | `audit/qa/hde-epic036/checks/po-005/primary.log`                        | none                                                                                                                                                                                     |
|     6 | po-006                        | PO-006                      | closed             | secret-safe and no raw payload persistence                     | `audit/qa/hde-epic036/checks/po-006/primary.log`                        | none                                                                                                                                                                                     |
|     7 | po-007                        | PO-007                      | closed             | evidence/status/closeout separation                            | `audit/qa/hde-epic036/checks/po-007/primary.log`                        | none                                                                                                                                                                                     |
|     8 | po-008                        | PO-008                      | closed             | coherent evidence-loop proof set                               | `audit/qa/hde-epic036/checks/po-008/primary.log`                        | none                                                                                                                                                                                     |
|     9 | po-009                        | PO-009                      | closed             | public/product/runtime/AI nonclaims                            | `audit/qa/hde-epic036/checks/po-009/primary.log`                        | none                                                                                                                                                                                     |
|    10 | po-010                        | PO-010                      | bounded open rails | live production-like route-policy refusal proof                | `audit/qa/hde-epic036/checks/po-010/primary.log`                        | `NO_EXTERNAL_IO_ON_REFUSAL_OK`, `ENV_RAILS_POLICY_OK`                                                                                                                                    |
|    11 | po-011                        | PO-011                      | closed             | live proof does not overclaim compatibility                    | `audit/qa/hde-epic036/checks/po-011/primary.log`                        | none                                                                                                                                                                                     |
|    12 | po-012                        | PO-012                      | closed             | future work compatibility boundary                             | `audit/qa/hde-epic036/checks/po-012/primary.log`                        | none                                                                                                                                                                                     |
|    13 | qa-13-governed-evidence-gates | Governed evidence gates     | closed             | tests, evidence paths, index, mirror, hash, LF, canonical JSON | `audit/qa/hde-epic036/checks/qa-13-governed-evidence-gates/primary.log` | `TESTS_PASS_OK`, `EVIDENCE_INDEX_UPDATED_OK`, `MACHINE_MIRROR_UPDATED_OK`, `EVIDENCE_INDEX_HASH_OK`, `EVIDENCE_PATHS_VALIDATED_OK`, `EVIDENCE_PATH_PROOFS_OK`, `JSON_CANONICAL_CHECK_OK` |
|    14 | qa-14-close-out-deliverables  | Close-out deliverables      | closed             | manifest, discovery artifact, QA RCA / Doc Delta summary       | `audit/qa/hde-epic036/checks/qa-14-close-out-deliverables/primary.log`  | none                                                                                                                                                                                     |

### Dependency readiness standard

For every executable step:

Required dependencies:

* Python 3
* repo root with `engine/`, `tools/`, `tests/`, `artifacts/`, `docs/`, and `audit/` available
* Step-0B QA helper after Step-0B runs
* pytest only for `qa-13-governed-evidence-gates`
* bash only for `qa-13-governed-evidence-gates`
* PO-approved `HD_API_BASE_URL` only for `po-010`

Preflight check:

* Python: `python --version`
* pytest: handled by `qa-13-governed-evidence-gates` helper import check
* bash: handled by shell-script execution in `qa-13-governed-evidence-gates`
* PO-approved live base: checked inside `po-010`

If missing, activation/install action:

* Do not install packages inside this runbook.
* Do not mutate the repo to resolve missing dependencies.
* If the environment is missing a required tool, classify the affected step as `TOOLING_BLOCKED`.
* PO must provide an environment where the repo’s existing dependency set is available.

If still unavailable:

* Record `TOOLING_BLOCKED` in that check’s primary log.
* Do not classify missing tools as `FAIL_BEHAVIOR`.

### Common execution rule

Run Step-0B first.
Then run PO-001 through PO-012 in order.
Then run `qa-13-governed-evidence-gates`.
Then run `qa-14-close-out-deliverables`.

### CHECK step-0b-doc-delta-capture: Step-0B — Doc Delta Capture

Goal:

Create the stable doc-delta surfaces and the QA helper used by later checks. Record known planning caveats before the PO executes proof checks.

Required dependencies:

* Python 3
* write access to `audit/qa/hde-epic036/`
* write access to `audit/docdeltas/`

Preflight check:

* `python --version`

If missing, activation/install action:

* Do not install Python inside this runbook.
* Mark the step `TOOLING_BLOCKED`.

If still unavailable:

* Stop this step and do not run later checks.

Preconditions:

* Execute from repo root.
* Do not run OPS commands.
* Do not call live external services in Step-0B.

Setup:

* None beyond repo-root execution.

Numbered PO actions:

1. Paste Command 1 to create the QA helper.
2. Paste Command 2 to execute Step-0B.
3. Open `audit/qa/hde-epic036/checks/step-0b-doc-delta-capture/primary.log`.
4. Confirm the header has `check_id` set to `step-0b-doc-delta-capture`.
5. Confirm `status` is `PASS`.
6. Confirm the doc-delta surfaces and helper are listed in `evidence_artifacts`.
7. Confirm `audit/qa/hde-epic036/checks/step-0b-doc-delta-capture/primary.log.path_proof.txt` exists.

Command 1:
mkdir -p audit/qa/hde-epic036/00_meta audit/qa/hde-epic036/checks audit/docdeltas && cat > audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py <<'PY'
from **future** import annotations
import datetime
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any

EPIC_ID = "HDE-EPIC036"
QA_ROOT = Path("audit/qa/hde-epic036")
CHECKS_ROOT = QA_ROOT / "checks"
META_ROOT = QA_ROOT / "00_meta"
DOCDELTA_DRAFT = Path("audit/docdeltas/hde-epic036_doc_deltas.md")
DOCDELTA_CAPTURE = META_ROOT / "doc_deltas.md"

class ToolingBlocked(Exception): pass
class FailBehavior(Exception): pass
class FailTooling(Exception): pass

def utc_now() -> str:
return datetime.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"

def sha256(path: Path) -> str:
h = hashlib.sha256()
with path.open("rb") as f:
for chunk in iter(lambda: f.read(8192), b""):
h.update(chunk)
return h.hexdigest()

def write_path_proof(path: Path) -> Path:
if not path.exists():
raise ToolingBlocked(f"MISSING_PATH_FOR_PROOF:{path}")
proof = Path(str(path) + ".path_proof.txt")
stat = path.stat()
proof.write_text(
"\n".join([
f"path: {path}",
f"size_bytes: {stat.st_size}",
f"sha256: {sha256(path)}",
f"mtime_utc: {datetime.datetime.utcfromtimestamp(stat.st_mtime).replace(microsecond=0).isoformat()}Z",
f"produced_at_utc: {utc_now()}",
"",
]),
encoding="utf-8",
)
return proof

def read_text(path: str | Path) -> str:
p = Path(path)
if not p.exists():
raise ToolingBlocked(f"MISSING_FILE:{p}")
return p.read_text(encoding="utf-8")

def load_json(path: str | Path) -> dict[str, Any]:
return json.loads(read_text(path))

def require_file(path: str | Path, body: list[str]) -> None:
p = Path(path)
if not p.exists():
raise ToolingBlocked(f"MISSING_FILE:{p}")
body.append(f"FILE_OK {p} sha256={sha256(p)}")

def require_contains(path: str | Path, needle: str, body: list[str]) -> None:
text = read_text(path)
if needle not in text:
raise FailBehavior(f"MISSING_TEXT:{path}:{needle}")
body.append(f"TEXT_OK {path} :: {needle}")

def require_absent(path: str | Path, needle: str, body: list[str]) -> None:
text = read_text(path)
if needle in text:
raise FailBehavior(f"FORBIDDEN_TEXT:{path}:{needle}")
body.append(f"ABSENT_OK {path} :: {needle}")

def require_json_value(path: str | Path, dotted_key: str, expected: Any, body: list[str]) -> None:
payload: Any = load_json(path)
for key in dotted_key.split("."):
if not isinstance(payload, dict) or key not in payload:
raise FailBehavior(f"MISSING_JSON_KEY:{path}:{dotted_key}")
payload = payload[key]
if payload != expected:
raise FailBehavior(f"JSON_VALUE_MISMATCH:{path}:{dotted_key}:{payload!r}!={expected!r}")
body.append(f"JSON_OK {path} :: {dotted_key}={expected!r}")

def require_json_list_contains(path: str | Path, dotted_key: str, expected: Any, body: list[str]) -> None:
payload: Any = load_json(path)
for key in dotted_key.split("."):
if not isinstance(payload, dict) or key not in payload:
raise FailBehavior(f"MISSING_JSON_KEY:{path}:{dotted_key}")
payload = payload[key]
if not isinstance(payload, list) or expected not in payload:
raise FailBehavior(f"JSON_LIST_MISSING:{path}:{dotted_key}:{expected!r}")
body.append(f"JSON_LIST_OK {path} :: {dotted_key} contains {expected!r}")

def require_token(path: str | Path, token: str, body: list[str]) -> None:
text = read_text(path)
if token not in text:
raise FailBehavior(f"MISSING_TOKEN:{path}:{token}")
body.append(f"TOKEN_OK {path} :: {token}")

def canonical_json_file(path: str | Path, body: list[str]) -> None:
p = Path(path)
raw = p.read_bytes()
if not raw.endswith(b"\n") or raw.endswith(b"\n\n") or raw.startswith(b"\xef\xbb\xbf"):
raise FailBehavior(f"JSON_CANONICAL_BYTES_FAIL:{p}")
payload = json.loads(raw.decode("utf-8"))
expected = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8") + b"\n"
if raw != expected:
raise FailBehavior(f"JSON_CANONICAL_SORT_FAIL:{p}")
body.append(f"JSON_CANONICAL_OK {p}")

def run_cmd(cmd: list[str], body: list[str], tooling: bool = False, env: dict[str, str] | None = None, expected_exit: int = 0) -> tuple[int, str]:
body.append("COMMAND " + " ".join(cmd))
try:
cp = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, check=False, env=env)
except FileNotFoundError as exc:
raise ToolingBlocked(f"COMMAND_MISSING:{cmd[0]}") from exc
if cp.stdout:
body.append(cp.stdout.strip())
body.append(f"EXIT_CODE {cp.returncode}")
if cp.returncode != expected_exit:
if tooling:
raise FailTooling(f"COMMAND_FAILED:{' '.join(cmd)}:{cp.returncode}!={expected_exit}")
raise FailBehavior(f"COMMAND_FAILED:{' '.join(cmd)}:{cp.returncode}!={expected_exit}")
return cp.returncode, cp.stdout or ""

def require_pytest(body: list[str]) -> None:
cp = subprocess.run([sys.executable, "-c", "import pytest"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, check=False)
if cp.returncode != 0:
raise ToolingBlocked("PYTEST_IMPORT_MISSING")
body.append("PYTEST_IMPORT_OK")

def check_step0b(body: list[str]) -> tuple[list[str], list[str], list[str]]:
META_ROOT.mkdir(parents=True, exist_ok=True)
DOCDELTA_DRAFT.parent.mkdir(parents=True, exist_ok=True)
text = "\n".join([
"# HDE-EPIC036 Live QA Doc Delta Capture",
"",
"BLOCKERS:",
"- None at planning time.",
"",
"CAVEATS:",
"- Existing audit reported no repo-resident HDE-EPIC036 OPS-01 evidence root.",
"- Bounded live production-like route-policy proof is required by this plan and is executed as PO-010 under the QA root.",
"- PO-010 uses a PO-approved live v2 base value and expects configured-v2 refusal before legacy BodyGraph request construction.",
"- This plan does not claim OPS completion, PF09 status movement, HDE-FERM008 parent Done, epic closeout, public Reader change, new HTTP home, AI scope, raw payload persistence, or full HumanDesignAPI v2 runtime conformance.",
"",
])
DOCDELTA_DRAFT.write_text(text, encoding="utf-8")
DOCDELTA_CAPTURE.write_text(text, encoding="utf-8")
draft_proof = write_path_proof(DOCDELTA_DRAFT)
capture_proof = write_path_proof(DOCDELTA_CAPTURE)
helper = Path("audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py")
helper_proof = write_path_proof(helper)
body.append(f"DOC_DELTA_DRAFT={DOCDELTA_DRAFT}")
body.append(f"DOC_DELTA_CAPTURE={DOCDELTA_CAPTURE}")
body.append(f"QA_HELPER={helper}")
return [str(DOCDELTA_DRAFT), str(draft_proof), str(DOCDELTA_CAPTURE), str(capture_proof), str(helper), str(helper_proof)], ["DOC_DELTA_PRESENT_OK"], ["DOC_DELTA_PRESENT_OK"]

def check_po001(body: list[str]) -> tuple[list[str], list[str], list[str]]:
route = "artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json"
shape = "artifacts/vendor/hdapi_v2/bg_resolve_request_shape.snapshot.json"
test = "tests/bodygraph/test_bg_resolve_route_policy.py"
for p in [route, shape, test]:
require_file(p, body)
require_json_value(route, "epic_id", EPIC_ID, body)
require_json_value(route, "configured_v2_policy.classification", "unsupported_runtime_nonclaim", body)
require_json_value(route, "configured_v2_policy.supported", False, body)
require_json_value(route, "configured_v2_policy.error_code", "PROVIDER_ROUTE_UNSUPPORTED", body)
require_json_value(shape, "configured_v2_bg_resolve_request_shape", "NO_BODYGRAPHS_REQUEST_BUILT_UNSUPPORTED_RUNTIME_NONCLAIM", body)
require_contains(test, "assert calls == []", body)
return [route, shape, test], ["NO_EXTERNAL_IO_ON_REFUSAL_OK"], ["NO_EXTERNAL_IO_ON_REFUSAL_OK"]

def check_po002(body: list[str]) -> tuple[list[str], list[str], list[str]]:
route = "artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json"
decision = "audit/qa/hde-epic036/route_policy_decision.log"
for p in [route, decision]:
require_file(p, body)
require_json_value(route, "selected_posture", "unsupported_runtime_nonclaim", body)
require_json_value(route, "supported_postures.unsupported_runtime_nonclaim", "SELECTED_FOR_CONFIGURED_V2_BASE", body)
require_json_value(route, "supported_postures.explicit_legacy_fallback", "PRESERVED_ONLY_FOR_NON_V2_CONFIGURED_BASE", body)
require_json_value(route, "legacy_fallback_policy.classification", "explicit_legacy_fallback", body)
require_contains(decision, "explicit_legacy_fallback=PRESERVED_ONLY_FOR_NON_V2_CONFIGURED_BASE", body)
return [route, decision], ["ENV_RAILS_POLICY_OK"], ["ENV_RAILS_POLICY_OK"]

def check_po003(body: list[str]) -> tuple[list[str], list[str], list[str]]:
bodygraph = "artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json"
route = "artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json"
response = "artifacts/vendor/hdapi_v2/response_mapping.snapshot.json"
for p in [bodygraph, route, response]:
require_file(p, body)
require_json_value(bodygraph, "bodygraph_detail_sufficiency", "UNSUPPORTED_RUNTIME_NONCLAIM", body)
require_json_value(route, "route_family_identity.v2_chart_candidate.bodygraph_detail_sufficiency", "NOT_CLAIMED", body)
require_contains(response, "ChartSimpleResult", body)
require_contains(bodygraph, "NO_COMPLETE_V2_CHARTRESULT_OR_CHARTSIMPLERESULT_TO_BODYGRAPH_PERSON_CACHE_ADAPTER_FOUND_IN_INSPECTED_LOCI", body)
return [bodygraph, route, response], [], []

def check_po004(body: list[str]) -> tuple[list[str], list[str], list[str]]:
bodygraph = "artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json"
response = "artifacts/vendor/hdapi_v2/response_mapping.snapshot.json"
for p in [bodygraph, response]:
require_file(p, body)
require_json_value(bodygraph, "v2_chart_data_feeds_existing_bodygraph_cache_person_compat_flows", False, body)
require_json_value(bodygraph, "adapter_sufficiency", "NO_COMPLETE_V2_CHARTRESULT_OR_CHARTSIMPLERESULT_TO_BODYGRAPH_PERSON_CACHE_ADAPTER_FOUND_IN_INSPECTED_LOCI", body)
require_json_value(response, "normalized_data_path_proof_claim", "NONE", body)
require_json_value(response, "schema_gap_status", "GAP_RECORDED", body)
return [bodygraph, response], [], []

def check_po005(body: list[str]) -> tuple[list[str], list[str], list[str]]:
route = "artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json"
test = "tests/bodygraph/test_bg_resolve_route_policy.py"
for p in [route, test]:
require_file(p, body)
require_json_value(route, "legacy_fallback_policy.classification", "explicit_legacy_fallback", body)
require_json_value(route, "legacy_fallback_policy.supported", True, body)
require_json_value(route, "legacy_fallback_policy.configured_base_version", "v1", body)
require_json_value(route, "configured_v2_policy.supported", False, body)
require_contains(test, "test_explicit_legacy_fallback_remains_available_for_non_v2_configured_base", body)
return [route, test], [], []

def check_po006(body: list[str]) -> tuple[list[str], list[str], list[str]]:
nonclaims = "artifacts/vendor/hdapi_v2/bg_resolve_runtime_nonclaims.json"
shape = "artifacts/vendor/hdapi_v2/bg_resolve_request_shape.snapshot.json"
for p in [nonclaims, shape]:
require_file(p, body)
for key in ["raw_payload_persistence", "raw_request_body_persisted", "raw_response_body_persisted", "app_side_humandesignapi_credential_ownership"]:
require_json_value(nonclaims, f"no_claims.{key}", "NONE", body)
require_json_value(shape, "raw_request_body_persisted", False, body)
require_json_value(shape, "raw_response_body_persisted", False, body)
require_json_value(shape, "raw_vendor_payload_persisted", False, body)
return [nonclaims, shape], [], []

def check_po007(body: list[str]) -> tuple[list[str], list[str], list[str]]:
acceptance = "docs/acceptance_map_epic036.json"
binding = "artifacts/vendor/hdapi_v2/bg_resolve_policy_binding.snapshot.json"
decision = "audit/qa/hde-epic036/route_policy_decision.log"
for p in [acceptance, binding, decision]:
require_file(p, body)
for nonclaim in ["QA PASS", "OPS completion", "PF09 status movement", "HDE-FERM008 parent Done", "epic closeout"]:
require_json_list_contains(acceptance, "nonclaims", nonclaim, body)
require_json_value(binding, "policy_binding.ops_01_requirement", "OPS-01 not required by PR-01; route-policy classification proved closed-rails from repo evidence.", body)
require_contains(decision, "OPS-01 not required by PR-01; route-policy classification proved closed-rails from repo evidence.", body)
return [acceptance, binding, decision], [], []

def check_po008(body: list[str]) -> tuple[list[str], list[str], list[str]]:
paths = [
"artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json",
"artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json",
"artifacts/vendor/hdapi_v2/bg_resolve_runtime_nonclaims.json",
"artifacts/vendor/hdapi_v2/bg_resolve_request_shape.snapshot.json",
"artifacts/vendor/hdapi_v2/bg_resolve_policy_binding.snapshot.json",
"audit/qa/hde-epic036/route_policy_decision.log",
]
for p in paths:
require_file(p, body)
require_file(p + ".path_proof.txt", body)
require_json_value(paths[4], "policy_binding.selected_classification", "unsupported_runtime_nonclaim", body)
require_json_value(paths[4], "policy_binding.hde_ferm008_6_completion_role", "Complete in this epic for route-policy classification only", body)
return paths + [p + ".path_proof.txt" for p in paths], [], []

def check_po009(body: list[str]) -> tuple[list[str], list[str], list[str]]:
nonclaims = "artifacts/vendor/hdapi_v2/bg_resolve_runtime_nonclaims.json"
acceptance = "docs/acceptance_map_epic036.json"
decision = "audit/qa/hde-epic036/route_policy_decision.log"
for p in [nonclaims, acceptance, decision]:
require_file(p, body)
for key in ["public_reader_change", "public_route", "public_flag", "public_payload_change", "new_http_home", "app_side_humandesignapi_credential_ownership", "full_hdapi_v2_runtime_conformance", "raw_payload_persistence", "ai_scope"]:
require_json_value(nonclaims, f"no_claims.{key}", "NONE", body)
for needle in ["no_public_reader_change=true", "no_public_route=true", "no_ai_scope=true", "no_full_hdapi_v2_runtime_conformance=true"]:
require_contains(decision, needle, body)
return [nonclaims, acceptance, decision], [], []

def check_po010(body: list[str]) -> tuple[list[str], list[str], list[str]]:
helper_artifacts: list[str] = []
base = os.environ.get("HD_API_BASE_URL", "").strip()
if not base:
raise ToolingBlocked("PO_APPROVED_HD_API_BASE_URL_REQUIRED")
if "/v2" not in base.rstrip("/").lower().split("?")[0]:
raise ToolingBlocked("HD_API_BASE_URL_MUST_BE_PO_APPROVED_V2_BASE")
live_log = CHECKS_ROOT / "po-010" / "live_route_policy.log"
cmd = [
sys.executable, "-m", "engine.cli", "bg:resolve",
"--user", "hde-epic036-live-route-policy",
"--source", "vendor",
"--dry-run",
"--birthdate", "1990-01-01",
"--birthtime", "12:00",
"--location", "Amsterdam, NL",
]
env = os.environ.copy()
env.update({"SAFE_MODE": "0", "ALLOW_NETWORK": "1", "APP_ENV": "dev", "LC_ALL": "C", "LANG": "C", "TZ": "UTC", "HD_API_BASE_URL": base})
rc, out = run_cmd(cmd, body, env=env, expected_exit=1)
safe_out = "\n".join(line for line in out.splitlines() if "api" not in line.lower() or "PROVIDER_ROUTE_UNSUPPORTED" in line or "unsupported_runtime_nonclaim" in line)
live_log.write_text(
"\n".join([
"HDE-EPIC036 bounded live production-like route-policy proof",
"SAFE_MODE=0",
"ALLOW_NETWORK=1",
"APP_ENV=dev",
"HD_API_BASE_URL=PO_APPROVED_V2_BASE_REDACTED",
"expected_cli_exit_code=1",
f"observed_cli_exit_code={rc}",
safe_out,
"",
]),
encoding="utf-8",
)
proof = write_path_proof(live_log)
text = live_log.read_text(encoding="utf-8")
if "PROVIDER_ROUTE_UNSUPPORTED" not in text or "unsupported_runtime_nonclaim" not in text:
raise FailBehavior("LIVE_ROUTE_POLICY_PROOF_MISSING_EXPECTED_REFUSAL")
if "BODYGRAPH_DETAIL_COMPATIBLE" in text or "full runtime conformance" in text:
raise FailBehavior("LIVE_ROUTE_POLICY_OVERCLAIM")
helper_artifacts.extend([str(live_log), str(proof)])
return helper_artifacts, ["NO_EXTERNAL_IO_ON_REFUSAL_OK", "ENV_RAILS_POLICY_OK"], ["NO_EXTERNAL_IO_ON_REFUSAL_OK", "ENV_RAILS_POLICY_OK"]

def check_po011(body: list[str]) -> tuple[list[str], list[str], list[str]]:
live_log = CHECKS_ROOT / "po-010" / "live_route_policy.log"
live_proof = Path(str(live_log) + ".path_proof.txt")
nonclaims = "artifacts/vendor/hdapi_v2/bg_resolve_runtime_nonclaims.json"
bodygraph = "artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json"
for p in [live_log, live_proof, nonclaims, bodygraph]:
require_file(p, body)
require_contains(live_log, "PROVIDER_ROUTE_UNSUPPORTED", body)
require_contains(live_log, "unsupported_runtime_nonclaim", body)
require_json_value(nonclaims, "chart_simple_success_bodygraph_detail_claim", "NONE", body)
require_json_value(nonclaims, "no_compatibility_by_inference", True, body)
require_json_value(bodygraph, "bodygraph_detail_sufficiency", "UNSUPPORTED_RUNTIME_NONCLAIM", body)
return [str(live_log), str(live_proof), nonclaims, bodygraph], [], []

def check_po012(body: list[str]) -> tuple[list[str], list[str], list[str]]:
acceptance = "docs/acceptance_map_epic036.json"
bodygraph = "artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json"
nonclaims = "artifacts/vendor/hdapi_v2/bg_resolve_runtime_nonclaims.json"
for p in [acceptance, bodygraph, nonclaims]:
require_file(p, body)
require_json_value(acceptance, "v2_chart_data_feeds_existing_bodygraph_cache_person_compat_flows", False, body)
require_json_value(acceptance, "bodygraph_detail_sufficiency", "UNSUPPORTED_RUNTIME_NONCLAIM", body)
require_json_value(bodygraph, "v2_chart_data_feeds_existing_bodygraph_cache_person_compat_flows", False, body)
require_json_value(nonclaims, "chart_simple_success_bodygraph_detail_claim", "NONE", body)
return [acceptance, bodygraph, nonclaims], [], []

def check_qa13(body: list[str]) -> tuple[list[str], list[str], list[str]]:
require_pytest(body)
artifacts = [
"tests/bodygraph/test_bg_resolve_route_policy.py",
"tests/bodygraph/test_resolver_vendor.py",
"tests/cli/test_bg_resolve.py",
"tests/evidence/test_hde_epic036_pr02_evidence_loop.py",
"tools/evidence/generate_hde_epic036_bg_resolve_route_policy.py",
"tools/evidence/validate_evidence_paths.py",
"tools/evidence/check_lf_endings.py",
"tools/evidence/update_evidence_index.py",
"ci/checks/check_mirror_schema.sh",
"ci/checks/check_evidence_index_hash.sh",
"ci/checks/check_final_lf.sh",
"docs/evidence/INDEX.json",
"docs/evidence/INDEX.sha256",
"artifacts/evidence_index.jsonl",
"artifacts/evidence_index.jsonl.sha256",
"docs/acceptance_map_epic036.json",
"artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json",
"artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json",
"artifacts/vendor/hdapi_v2/bg_resolve_runtime_nonclaims.json",
"artifacts/vendor/hdapi_v2/bg_resolve_request_shape.snapshot.json",
"artifacts/vendor/hdapi_v2/bg_resolve_policy_binding.snapshot.json",
]
for p in artifacts:
require_file(p, body)
for p in [
"docs/acceptance_map_epic036.json",
"artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json",
"artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json",
"artifacts/vendor/hdapi_v2/bg_resolve_runtime_nonclaims.json",
"artifacts/vendor/hdapi_v2/bg_resolve_request_shape.snapshot.json",
"artifacts/vendor/hdapi_v2/bg_resolve_policy_binding.snapshot.json",
]:
canonical_json_file(p, body)
run_cmd([sys.executable, "-m", "pytest", "tests/bodygraph/test_bg_resolve_route_policy.py", "tests/bodygraph/test_resolver_vendor.py", "tests/cli/test_bg_resolve.py", "tests/evidence/test_hde_epic036_pr02_evidence_loop.py"], body)
run_cmd([sys.executable, "tools/evidence/generate_hde_epic036_bg_resolve_route_policy.py", "--check"], body)
run_cmd([sys.executable, "tools/evidence/validate_evidence_paths.py"], body)
run_cmd([sys.executable, "tools/evidence/check_lf_endings.py"], body)
run_cmd([sys.executable, "tools/evidence/update_evidence_index.py", "--check"], body)
run_cmd(["bash", "ci/checks/check_mirror_schema.sh"], body)
run_cmd(["bash", "ci/checks/check_evidence_index_hash.sh"], body)
run_cmd(["bash", "ci/checks/check_final_lf.sh"], body)
tokens = ["TESTS_PASS_OK", "EVIDENCE_INDEX_UPDATED_OK", "MACHINE_MIRROR_UPDATED_OK", "EVIDENCE_INDEX_HASH_OK", "EVIDENCE_PATHS_VALIDATED_OK", "EVIDENCE_PATH_PROOFS_OK", "JSON_CANONICAL_CHECK_OK"]
for token in tokens:
require_token("docs/acceptance_map_epic036.json", token, body)
return artifacts, tokens, tokens

def check_closeout(body: list[str]) -> tuple[list[str], list[str], list[str]]:
expected = ["step-0b-doc-delta-capture"] + [f"po-{i:03d}" for i in range(1, 13)] + ["qa-13-governed-evidence-gates"]
entries = []
for check_id in expected:
log = CHECKS_ROOT / check_id / "primary.log"
proof = Path(str(log) + ".path_proof.txt")
if not log.exists():
raise ToolingBlocked(f"NOT_RUN:{check_id}:{log}")
if not proof.exists():
raise ToolingBlocked(f"MISSING_PATH_PROOF:{check_id}:{proof}")
header = json.loads(log.read_text(encoding="utf-8").splitlines()[0])
entries.append({"check_id": check_id, "status": header.get("status"), "log_path": str(log), "path_proof_path": str(proof)})
manifest = QA_ROOT / "qa_step_logs_manifest.json"
manifest.write_text(json.dumps({"schema_version": "pf27.qa_step_logs_manifest.v1", "epic_id": EPIC_ID, "entries": entries}, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n", encoding="utf-8")
manifest_proof = write_path_proof(manifest)
discovery = META_ROOT / "discovery_artifact.md"
discovery.write_text(
"\n".join([
"# HDE-EPIC036 Discovery Artifact",
"",
"Repo loci were grounded by PF10, QA audit, and live repo validation before this plan was drafted.",
"The QA run validates existing governed artifacts and creates check-scoped QA logs under audit/qa/hde-epic036/checks/.",
"PO-010 creates bounded live production-like route-policy evidence under the QA root using a PO-approved live v2 base value.",
"No OPS completion, PF09 status movement, HDE-FERM008 parent Done, epic closeout, public Reader change, new HTTP home, AI scope, raw payload persistence, or full HumanDesignAPI v2 runtime conformance is claimed.",
"",
]),
encoding="utf-8",
)
discovery_proof = write_path_proof(discovery)
rca = META_ROOT / "qa_rca_doc_delta_summary.md"
rca.write_text(
"\n".join([
"# HDE-EPIC036 QA RCA and Doc Delta Summary",
"",
"Coverage vs plan:",
"- Step-0B, PO-001 through PO-012, and qa-13 are represented by check-scoped primary logs and sibling path proofs under audit/qa/hde-epic036/checks/.",
"- qa-14-close-out-deliverables created this closeout assembly evidence.",
"",
"Doc deltas:",
"- Existing HDE-EPIC036 doc-delta surfaces remain audit/docdeltas/hde-epic036_doc_deltas.md and audit/qa/hde-epic036/00_meta/doc_deltas.md.",
"",
"Readiness posture:",
"- This artifact supports QA closeout review only. It does not perform PO closeout, board update, PF edit, merge, PF09 status movement, OPS completion, full runtime conformance, public expansion, raw payload persistence, or AI scope.",
"",
]),
encoding="utf-8",
)
rca_proof = write_path_proof(rca)
return [str(manifest), str(manifest_proof), str(discovery), str(discovery_proof), str(rca), str(rca_proof)], [], []

CHECKS = {
"step-0b-doc-delta-capture": ("Step-0B - Doc Delta Capture", check_step0b),
"po-001": ("PO-001", check_po001),
"po-002": ("PO-002", check_po002),
"po-003": ("PO-003", check_po003),
"po-004": ("PO-004", check_po004),
"po-005": ("PO-005", check_po005),
"po-006": ("PO-006", check_po006),
"po-007": ("PO-007", check_po007),
"po-008": ("PO-008", check_po008),
"po-009": ("PO-009", check_po009),
"po-010": ("PO-010", check_po010),
"po-011": ("PO-011", check_po011),
"po-012": ("PO-012", check_po012),
"qa-13-governed-evidence-gates": ("Governed evidence gates", check_qa13),
"qa-14-close-out-deliverables": ("Close-out deliverables", check_closeout),
}

def run(check_id: str) -> int:
if check_id not in CHECKS:
print(f"UNKNOWN_CHECK:{check_id}", file=sys.stderr)
return 99
check_name, fn = CHECKS[check_id]
check_root = CHECKS_ROOT / check_id
check_root.mkdir(parents=True, exist_ok=True)
primary = check_root / "primary.log"
proof = Path(str(primary) + ".path_proof.txt")
command = f"python audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py {check_id}"
body = [f"check_id={check_id}", f"check_name={check_name}", f"command={command}", "pins=LC_ALL=C LANG=C TZ=UTC"]
status = "PASS"
exit_code = 0
artifacts: list[str] = []
intended: list[str] = []
claimed: list[str] = []
try:
artifacts, intended, claimed = fn(body)
except ToolingBlocked as exc:
status = "TOOLING_BLOCKED"; exit_code = 99; claimed = []; body.append(f"TOOLING_BLOCKED:{exc}")
except FailTooling as exc:
status = "FAIL_TOOLING"; exit_code = 2; claimed = []; body.append(f"FAIL_TOOLING:{exc}")
except FailBehavior as exc:
status = "FAIL_BEHAVIOR"; exit_code = 1; claimed = []; body.append(f"FAIL_BEHAVIOR:{exc}")
except Exception as exc:
status = "FAIL_TOOLING"; exit_code = 2; claimed = []; body.append(f"FAIL_TOOLING:{type(exc).**name**}:{exc}")
if status != "PASS":
claimed = []
captured_env = {
"SAFE_MODE": os.environ.get("SAFE_MODE", ""),
"ALLOW_NETWORK": os.environ.get("ALLOW_NETWORK", ""),
"APP_ENV": os.environ.get("APP_ENV", ""),
"LC_ALL": os.environ.get("LC_ALL", ""),
"LANG": os.environ.get("LANG", ""),
"TZ": os.environ.get("TZ", ""),
}
if check_id == "po-010":
captured_env.update({
"SAFE_MODE": "0",
"ALLOW_NETWORK": "1",
"APP_ENV": "dev",
"HD_API_BASE_URL": "PO_APPROVED_V2_BASE_REDACTED" if os.environ.get("HD_API_BASE_URL") else "",
})
evidence = [str(primary), str(proof)] + artifacts
header = {
"schema_version": "pf27.step_log_header.v1",
"timestamp_utc": utc_now(),
"check_id": check_id,
"check_name": check_name,
"status": status,
"fail_status": "" if status == "PASS" else status,
"command": command,
"command_provenance": "Copy/paste from plan via QA-created helper",
"exit_code": exit_code,
"evidence_artifacts": evidence,
"captured_env": captured_env,
"pf_refs": ["PF10 — HDE-Build Notes", "PF19 — Glow QA Guide", "PF27 — Canon Plan Templates", "PF05 — HDE CLI/API Vendor Reference", "PF02 — HDE Architecture"],
"intended_tokens": intended,
"claimed_tokens": claimed,
}
primary.write_text(json.dumps(header, ensure_ascii=False) + "\n" + "\n".join(body) + "\n", encoding="utf-8")
write_path_proof(primary)
print(f"{check_id} status={status} exit_code={exit_code} primary={primary}")
return exit_code

if **name** == "**main**":
if len(sys.argv) != 2:
print("usage: hde036_live_qa_harness.py <check_id>", file=sys.stderr)
raise SystemExit(99)
raise SystemExit(run(sys.argv[1]))
PY

Command 2:
SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC python audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py step-0b-doc-delta-capture

What to look for:

* `step-0b-doc-delta-capture status=PASS exit_code=0`
* `audit/docdeltas/hde-epic036_doc_deltas.md`
* `audit/qa/hde-epic036/00_meta/doc_deltas.md`
* `audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py`
* sibling path proofs for the primary log and doc-delta surfaces

Required deliverables:

* `audit/qa/hde-epic036/checks/step-0b-doc-delta-capture/primary.log`
* `audit/qa/hde-epic036/checks/step-0b-doc-delta-capture/primary.log.path_proof.txt`
* `audit/docdeltas/hde-epic036_doc_deltas.md`
* `audit/docdeltas/hde-epic036_doc_deltas.md.path_proof.txt`
* `audit/qa/hde-epic036/00_meta/doc_deltas.md`
* `audit/qa/hde-epic036/00_meta/doc_deltas.md.path_proof.txt`
* `audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py`
* `audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py.path_proof.txt`

PASS criteria tied to deliverables:

* PASS if both doc-delta surfaces exist and are path-proven.
* PASS if the QA helper exists under `audit/qa/hde-epic036/00_meta/`.
* PASS if the primary log has the PF27 header and sibling path proof.
* PASS may claim `DOC_DELTA_PRESENT_OK`.

FAIL criteria tied to deliverables:

* `TOOLING_BLOCKED` if Python or write access to `audit/` is unavailable.
* `FAIL_TOOLING` if doc-delta surfaces, helper, primary log, or path proofs cannot be written.
* `FAIL_BEHAVIOR` if Step-0B claims OPS completion, PF09 status movement, HDE-FERM008 parent Done, epic closeout, public Reader change, new HTTP home, AI scope, raw payload persistence, or full runtime conformance.

Blocked posture:

* If Step-0B is not PASS, do not run later checks until the PO resolves the missing helper or evidence-root access.

### CHECK po-001: PO-001

Goal:

Verify that the vendor-backed BodyGraph resolution workflow refuses unsupported configured v2 BodyGraph runtime behavior before making an accidental legacy-style vendor request.

Required dependencies:

* Python 3
* Step-0B QA helper
* Existing repo artifacts:

  * `artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json`
  * `artifacts/vendor/hdapi_v2/bg_resolve_request_shape.snapshot.json`
  * `tests/bodygraph/test_bg_resolve_route_policy.py`

Preflight check:

* Confirm Step-0B completed.
* The helper checks required files at runtime.

If missing, activation/install action:

* Do not install dependencies.
* Mark this check `TOOLING_BLOCKED`.

If still unavailable:

* Keep `TOOLING_BLOCKED` and do not invent replacement evidence.

Preconditions:

* Run from repo root.
* Closed rails only.

Numbered PO actions:

1. Paste the command.
2. Open `audit/qa/hde-epic036/checks/po-001/primary.log`.
3. Confirm `status=PASS`.
4. Confirm the log records `unsupported_runtime_nonclaim`, `PROVIDER_ROUTE_UNSUPPORTED`, no BodyGraph request built, and `assert calls == []`.
5. Confirm the sibling path proof exists.

Command 1:
SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC python audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py po-001

What to look for:

* `JSON_OK ... configured_v2_policy.classification='unsupported_runtime_nonclaim'`
* `JSON_OK ... configured_v2_policy.supported=False`
* `JSON_OK ... configured_v2_policy.error_code='PROVIDER_ROUTE_UNSUPPORTED'`
* `JSON_OK ... configured_v2_bg_resolve_request_shape='NO_BODYGRAPHS_REQUEST_BUILT_UNSUPPORTED_RUNTIME_NONCLAIM'`
* `TEXT_OK tests/bodygraph/test_bg_resolve_route_policy.py :: assert calls == []`

Required deliverables:

* `audit/qa/hde-epic036/checks/po-001/primary.log`
* `audit/qa/hde-epic036/checks/po-001/primary.log.path_proof.txt`
* `artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json`
* `artifacts/vendor/hdapi_v2/bg_resolve_request_shape.snapshot.json`
* `tests/bodygraph/test_bg_resolve_route_policy.py`

PASS criteria tied to deliverables:

* PASS if configured-v2 route-policy refusal is recorded before BodyGraph request construction.
* PASS if no accidental legacy-style vendor request is built.
* PASS if the primary log and sibling path proof exist.
* PASS may claim `NO_EXTERNAL_IO_ON_REFUSAL_OK`.

FAIL criteria tied to deliverables:

* `FAIL_BEHAVIOR` if configured-v2 policy is not `unsupported_runtime_nonclaim`.
* `FAIL_BEHAVIOR` if a configured-v2 `bodygraphs` request shape is built.
* `FAIL_BEHAVIOR` if no-external-I/O evidence is missing.
* `TOOLING_BLOCKED` if required artifacts or helper are missing.
* `FAIL_TOOLING` if the primary log or path proof cannot be written.

Blocked posture:

* If required artifacts are missing, keep the step `TOOLING_BLOCKED`; do not substitute OPS or prior-epic evidence.

### CHECK po-002: PO-002

Goal:

Verify that the selected vendor-path policy clearly distinguishes unsupported configured v2 behavior from explicit legacy fallback behavior.

Required dependencies:

* Python 3
* Step-0B QA helper
* Existing repo artifacts:

  * `artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json`
  * `audit/qa/hde-epic036/route_policy_decision.log`

Preflight check:

* Confirm Step-0B completed.
* The helper checks required files at runtime.

If missing, activation/install action:

* Do not install dependencies.
* Mark this check `TOOLING_BLOCKED`.

If still unavailable:

* Keep `TOOLING_BLOCKED`.

Preconditions:

* Run from repo root.
* Closed rails only.

Numbered PO actions:

1. Paste the command.
2. Open `audit/qa/hde-epic036/checks/po-002/primary.log`.
3. Confirm unsupported configured-v2 policy and explicit legacy fallback are both present and distinct.
4. Confirm the sibling path proof exists.

Command 1:
SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC python audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py po-002

What to look for:

* `JSON_OK ... selected_posture='unsupported_runtime_nonclaim'`
* `JSON_OK ... supported_postures.unsupported_runtime_nonclaim='SELECTED_FOR_CONFIGURED_V2_BASE'`
* `JSON_OK ... supported_postures.explicit_legacy_fallback='PRESERVED_ONLY_FOR_NON_V2_CONFIGURED_BASE'`
* `JSON_OK ... legacy_fallback_policy.classification='explicit_legacy_fallback'`

Required deliverables:

* `audit/qa/hde-epic036/checks/po-002/primary.log`
* `audit/qa/hde-epic036/checks/po-002/primary.log.path_proof.txt`
* `artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json`
* `audit/qa/hde-epic036/route_policy_decision.log`

PASS criteria tied to deliverables:

* PASS if unsupported configured-v2 behavior and explicit legacy fallback are both recorded and distinct.
* PASS if configured-v2 does not inherit the legacy fallback posture.
* PASS may claim `ENV_RAILS_POLICY_OK`.

FAIL criteria tied to deliverables:

* `FAIL_BEHAVIOR` if configured-v2 and non-v2 fallback classifications are collapsed.
* `FAIL_BEHAVIOR` if explicit legacy fallback is treated as supported for configured-v2.
* `TOOLING_BLOCKED` if required artifacts or helper are missing.
* `FAIL_TOOLING` if the primary log or path proof cannot be written.

Blocked posture:

* If route-policy evidence is missing, do not infer policy from code comments; keep `TOOLING_BLOCKED`.

### CHECK po-003: PO-003

Goal:

Verify that simple v2 chart success is not treated as proof that complete BodyGraph detail can be resolved.

Required dependencies:

* Python 3
* Step-0B QA helper
* Existing repo artifacts:

  * `artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json`
  * `artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json`
  * `artifacts/vendor/hdapi_v2/response_mapping.snapshot.json`

Preflight check:

* Confirm Step-0B completed.
* The helper checks required files at runtime.

If missing, activation/install action:

* Do not install dependencies.
* Mark this check `TOOLING_BLOCKED`.

If still unavailable:

* Keep `TOOLING_BLOCKED`.

Preconditions:

* Run from repo root.
* Closed rails only.

Numbered PO actions:

1. Paste the command.
2. Open `audit/qa/hde-epic036/checks/po-003/primary.log`.
3. Confirm BodyGraph-detail sufficiency remains `UNSUPPORTED_RUNTIME_NONCLAIM`.
4. Confirm v2 chart candidate sufficiency remains `NOT_CLAIMED`.
5. Confirm the sibling path proof exists.

Command 1:
SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC python audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py po-003

What to look for:

* `JSON_OK ... bodygraph_detail_sufficiency='UNSUPPORTED_RUNTIME_NONCLAIM'`
* `JSON_OK ... route_family_identity.v2_chart_candidate.bodygraph_detail_sufficiency='NOT_CLAIMED'`
* `TEXT_OK ... ChartSimpleResult`
* `TEXT_OK ... NO_COMPLETE_V2_CHARTRESULT_OR_CHARTSIMPLERESULT_TO_BODYGRAPH_PERSON_CACHE_ADAPTER_FOUND_IN_INSPECTED_LOCI`

Required deliverables:

* `audit/qa/hde-epic036/checks/po-003/primary.log`
* `audit/qa/hde-epic036/checks/po-003/primary.log.path_proof.txt`
* `artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json`
* `artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json`
* `artifacts/vendor/hdapi_v2/response_mapping.snapshot.json`

PASS criteria tied to deliverables:

* PASS if simple v2 chart success is not treated as full BodyGraph-detail proof.
* PASS if BodyGraph-detail sufficiency remains unsupported runtime nonclaim.
* PASS if the primary log and sibling path proof exist.

FAIL criteria tied to deliverables:

* `FAIL_BEHAVIOR` if simple chart success is treated as complete BodyGraph-detail resolution.
* `FAIL_BEHAVIOR` if adapter/schema gap evidence is absent.
* `TOOLING_BLOCKED` if required artifacts or helper are missing.
* `FAIL_TOOLING` if the primary log or path proof cannot be written.

Blocked posture:

* If response mapping or BodyGraph-detail proof is missing, do not use route names as proof; keep `TOOLING_BLOCKED`.

### CHECK po-004: PO-004

Goal:

Verify that the current implementation does not claim v2 chart data feeds existing BodyGraph, person, cache, or compatibility behavior.

Required dependencies:

* Python 3
* Step-0B QA helper
* Existing repo artifacts:

  * `artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json`
  * `artifacts/vendor/hdapi_v2/response_mapping.snapshot.json`

Preflight check:

* Confirm Step-0B completed.
* The helper checks required files at runtime.

If missing, activation/install action:

* Do not install dependencies.
* Mark this check `TOOLING_BLOCKED`.

If still unavailable:

* Keep `TOOLING_BLOCKED`.

Preconditions:

* Run from repo root.
* Closed rails only.

Numbered PO actions:

1. Paste the command.
2. Open `audit/qa/hde-epic036/checks/po-004/primary.log`.
3. Confirm compatibility flow flag is false.
4. Confirm normalized data path proof remains `NONE`.
5. Confirm schema gap remains `GAP_RECORDED`.
6. Confirm the sibling path proof exists.

Command 1:
SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC python audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py po-004

What to look for:

* `JSON_OK ... v2_chart_data_feeds_existing_bodygraph_cache_person_compat_flows=False`
* `JSON_OK ... adapter_sufficiency='NO_COMPLETE_V2_CHARTRESULT_OR_CHARTSIMPLERESULT_TO_BODYGRAPH_PERSON_CACHE_ADAPTER_FOUND_IN_INSPECTED_LOCI'`
* `JSON_OK ... normalized_data_path_proof_claim='NONE'`
* `JSON_OK ... schema_gap_status='GAP_RECORDED'`

Required deliverables:

* `audit/qa/hde-epic036/checks/po-004/primary.log`
* `audit/qa/hde-epic036/checks/po-004/primary.log.path_proof.txt`
* `artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json`
* `artifacts/vendor/hdapi_v2/response_mapping.snapshot.json`

PASS criteria tied to deliverables:

* PASS if no compatibility feed claim is present.
* PASS if normalized data path proof remains absent.
* PASS if schema gap remains recorded.

FAIL criteria tied to deliverables:

* `FAIL_BEHAVIOR` if the evidence claims v2 chart data feeds existing BodyGraph/person/cache/compatibility flows.
* `FAIL_BEHAVIOR` if normalized data path proof is claimed without a later adapter proof.
* `TOOLING_BLOCKED` if required artifacts or helper are missing.
* `FAIL_TOOLING` if the primary log or path proof cannot be written.

Blocked posture:

* If required artifacts are missing, keep `TOOLING_BLOCKED`.

### CHECK po-005: PO-005

Goal:

Verify that legacy fallback is preserved only as an explicit and intentional compatibility posture, not as accidental version-mismatched behavior.

Required dependencies:

* Python 3
* Step-0B QA helper
* Existing repo artifacts:

  * `artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json`
  * `tests/bodygraph/test_bg_resolve_route_policy.py`

Preflight check:

* Confirm Step-0B completed.
* The helper checks required files at runtime.

If missing, activation/install action:

* Do not install dependencies.
* Mark this check `TOOLING_BLOCKED`.

If still unavailable:

* Keep `TOOLING_BLOCKED`.

Preconditions:

* Run from repo root.
* Closed rails only.

Numbered PO actions:

1. Paste the command.
2. Open `audit/qa/hde-epic036/checks/po-005/primary.log`.
3. Confirm explicit legacy fallback is supported only for non-v2 configured base.
4. Confirm configured-v2 is unsupported.
5. Confirm the sibling path proof exists.

Command 1:
SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC python audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py po-005

What to look for:

* `JSON_OK ... legacy_fallback_policy.classification='explicit_legacy_fallback'`
* `JSON_OK ... legacy_fallback_policy.supported=True`
* `JSON_OK ... legacy_fallback_policy.configured_base_version='v1'`
* `JSON_OK ... configured_v2_policy.supported=False`
* `TEXT_OK ... test_explicit_legacy_fallback_remains_available_for_non_v2_configured_base`

Required deliverables:

* `audit/qa/hde-epic036/checks/po-005/primary.log`
* `audit/qa/hde-epic036/checks/po-005/primary.log.path_proof.txt`
* `artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json`
* `tests/bodygraph/test_bg_resolve_route_policy.py`

PASS criteria tied to deliverables:

* PASS if legacy fallback is explicit and limited to non-v2 configured base.
* PASS if configured-v2 behavior remains unsupported runtime nonclaim.

FAIL criteria tied to deliverables:

* `FAIL_BEHAVIOR` if legacy fallback is treated as accidental or version-mismatched behavior.
* `FAIL_BEHAVIOR` if configured-v2 is allowed to use legacy BodyGraph fallback.
* `TOOLING_BLOCKED` if required artifacts or helper are missing.
* `FAIL_TOOLING` if the primary log or path proof cannot be written.

Blocked posture:

* If route-policy evidence is missing, keep `TOOLING_BLOCKED`.

### CHECK po-006: PO-006

Goal:

Verify that the vendor-backed workflow preserves secret-safe behavior and avoids uncontrolled raw vendor payload recording.

Required dependencies:

* Python 3
* Step-0B QA helper
* Existing repo artifacts:

  * `artifacts/vendor/hdapi_v2/bg_resolve_runtime_nonclaims.json`
  * `artifacts/vendor/hdapi_v2/bg_resolve_request_shape.snapshot.json`

Preflight check:

* Confirm Step-0B completed.
* The helper checks required files at runtime.

If missing, activation/install action:

* Do not install dependencies.
* Mark this check `TOOLING_BLOCKED`.

If still unavailable:

* Keep `TOOLING_BLOCKED`.

Preconditions:

* Run from repo root.
* Closed rails only.

Numbered PO actions:

1. Paste the command.
2. Open `audit/qa/hde-epic036/checks/po-006/primary.log`.
3. Confirm no raw request, response, or vendor payload persistence.
4. Confirm app-side credential ownership remains a nonclaim.
5. Confirm the sibling path proof exists.

Command 1:
SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC python audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py po-006

What to look for:

* `JSON_OK ... no_claims.raw_payload_persistence='NONE'`
* `JSON_OK ... no_claims.raw_request_body_persisted='NONE'`
* `JSON_OK ... no_claims.raw_response_body_persisted='NONE'`
* `JSON_OK ... raw_vendor_payload_persisted=False`

Required deliverables:

* `audit/qa/hde-epic036/checks/po-006/primary.log`
* `audit/qa/hde-epic036/checks/po-006/primary.log.path_proof.txt`
* `artifacts/vendor/hdapi_v2/bg_resolve_runtime_nonclaims.json`
* `artifacts/vendor/hdapi_v2/bg_resolve_request_shape.snapshot.json`

PASS criteria tied to deliverables:

* PASS if secret-safe posture is preserved.
* PASS if no raw request body, response body, raw vendor payload, or app-side credential ownership claim is present.

FAIL criteria tied to deliverables:

* `FAIL_BEHAVIOR` if raw request, response, vendor payload, or secret-bearing material is persisted.
* `FAIL_BEHAVIOR` if app-side vendor credential ownership is claimed.
* `TOOLING_BLOCKED` if required artifacts or helper are missing.
* `FAIL_TOOLING` if the primary log or path proof cannot be written.

Blocked posture:

* If required nonclaim evidence is missing, keep `TOOLING_BLOCKED`.

### CHECK po-007: PO-007

Goal:

Verify that route-policy evidence preserves the distinction between implementation proof, operational observation, QA evidence, status movement, and closeout.

Required dependencies:

* Python 3
* Step-0B QA helper
* Existing repo artifacts:

  * `docs/acceptance_map_epic036.json`
  * `artifacts/vendor/hdapi_v2/bg_resolve_policy_binding.snapshot.json`
  * `audit/qa/hde-epic036/route_policy_decision.log`

Preflight check:

* Confirm Step-0B completed.
* The helper checks required files at runtime.

If missing, activation/install action:

* Do not install dependencies.
* Mark this check `TOOLING_BLOCKED`.

If still unavailable:

* Keep `TOOLING_BLOCKED`.

Preconditions:

* Run from repo root.
* Closed rails only.

Numbered PO actions:

1. Paste the command.
2. Open `audit/qa/hde-epic036/checks/po-007/primary.log`.
3. Confirm nonclaims for QA PASS, OPS completion, PF09 status movement, HDE-FERM008 parent Done, and epic closeout.
4. Confirm OPS-01 is not required by PR-01 and was not claimed as executed.
5. Confirm the sibling path proof exists.

Command 1:
SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC python audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py po-007

What to look for:

* `JSON_LIST_OK ... nonclaims contains 'QA PASS'`
* `JSON_LIST_OK ... nonclaims contains 'OPS completion'`
* `JSON_LIST_OK ... nonclaims contains 'PF09 status movement'`
* `JSON_LIST_OK ... nonclaims contains 'HDE-FERM008 parent Done'`
* `JSON_LIST_OK ... nonclaims contains 'epic closeout'`
* `TEXT_OK ... OPS-01 not required by PR-01`

Required deliverables:

* `audit/qa/hde-epic036/checks/po-007/primary.log`
* `audit/qa/hde-epic036/checks/po-007/primary.log.path_proof.txt`
* `docs/acceptance_map_epic036.json`
* `artifacts/vendor/hdapi_v2/bg_resolve_policy_binding.snapshot.json`
* `audit/qa/hde-epic036/route_policy_decision.log`

PASS criteria tied to deliverables:

* PASS if implementation evidence, operational observation, QA evidence, status movement, and closeout remain distinct.
* PASS if no QA PASS, OPS completion, PF09 status movement, HDE-FERM008 parent Done, or epic closeout is claimed by implementation evidence.

FAIL criteria tied to deliverables:

* `FAIL_BEHAVIOR` if evidence categories are collapsed.
* `FAIL_BEHAVIOR` if PF09 status movement, HDE-FERM008 parent Done, epic closeout, OPS completion, or QA PASS is claimed.
* `TOOLING_BLOCKED` if required artifacts or helper are missing.
* `FAIL_TOOLING` if the primary log or path proof cannot be written.

Blocked posture:

* If acceptance-map or policy-binding evidence is missing, keep `TOOLING_BLOCKED`.

### CHECK po-008: PO-008

Goal:

Verify that the route-policy decision, BodyGraph-detail sufficiency posture, runtime nonclaims, request-shape posture, and policy binding form one coherent governed proof set.

Required dependencies:

* Python 3
* Step-0B QA helper
* Existing repo artifacts and sibling path proofs:

  * `artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json`
  * `artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json`
  * `artifacts/vendor/hdapi_v2/bg_resolve_runtime_nonclaims.json`
  * `artifacts/vendor/hdapi_v2/bg_resolve_request_shape.snapshot.json`
  * `artifacts/vendor/hdapi_v2/bg_resolve_policy_binding.snapshot.json`
  * `audit/qa/hde-epic036/route_policy_decision.log`

Preflight check:

* Confirm Step-0B completed.
* The helper checks required files and sibling path proofs at runtime.

If missing, activation/install action:

* Do not install dependencies.
* Mark this check `TOOLING_BLOCKED`.

If still unavailable:

* Keep `TOOLING_BLOCKED`.

Preconditions:

* Run from repo root.
* Closed rails only.

Numbered PO actions:

1. Paste the command.
2. Open `audit/qa/hde-epic036/checks/po-008/primary.log`.
3. Confirm all five `bg_resolve_*` artifacts and route-policy decision log are present.
4. Confirm sibling path proofs are present.
5. Confirm selected classification is `unsupported_runtime_nonclaim`.
6. Confirm HDE-FERM008.6 completion role is route-policy classification only.
7. Confirm the sibling path proof exists.

Command 1:
SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC python audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py po-008

What to look for:

* `FILE_OK` for every required artifact and `.path_proof.txt`
* `JSON_OK ... policy_binding.selected_classification='unsupported_runtime_nonclaim'`
* `JSON_OK ... policy_binding.hde_ferm008_6_completion_role='Complete in this epic for route-policy classification only'`

Required deliverables:

* `audit/qa/hde-epic036/checks/po-008/primary.log`
* `audit/qa/hde-epic036/checks/po-008/primary.log.path_proof.txt`
* `artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json`
* `artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json.path_proof.txt`
* `artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json`
* `artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json.path_proof.txt`
* `artifacts/vendor/hdapi_v2/bg_resolve_runtime_nonclaims.json`
* `artifacts/vendor/hdapi_v2/bg_resolve_runtime_nonclaims.json.path_proof.txt`
* `artifacts/vendor/hdapi_v2/bg_resolve_request_shape.snapshot.json`
* `artifacts/vendor/hdapi_v2/bg_resolve_request_shape.snapshot.json.path_proof.txt`
* `artifacts/vendor/hdapi_v2/bg_resolve_policy_binding.snapshot.json`
* `artifacts/vendor/hdapi_v2/bg_resolve_policy_binding.snapshot.json.path_proof.txt`
* `audit/qa/hde-epic036/route_policy_decision.log`
* `audit/qa/hde-epic036/route_policy_decision.log.path_proof.txt`

PASS criteria tied to deliverables:

* PASS if route-policy decision, BodyGraph-detail sufficiency posture, runtime nonclaims, request shape, and policy binding all exist as one coherent proof set.
* PASS if each required proof artifact has a sibling path proof.
* PASS if HDE-FERM008.6 role is route-policy classification only.

FAIL criteria tied to deliverables:

* `FAIL_BEHAVIOR` if proof artifacts contradict each other.
* `FAIL_BEHAVIOR` if HDE-FERM008.6 is overclaimed beyond route-policy classification.
* `TOOLING_BLOCKED` if required artifacts, path proofs, or helper are missing.
* `FAIL_TOOLING` if the primary log or path proof cannot be written.

Blocked posture:

* If any required artifact or sibling path proof is missing, keep `TOOLING_BLOCKED`.

### CHECK po-009: PO-009

Goal:

Verify that the implementation does not claim public product behavior, new public transport behavior, app-side vendor ownership, full vendor runtime conformance, raw payload persistence, or AI scope.

Required dependencies:

* Python 3
* Step-0B QA helper
* Existing repo artifacts:

  * `artifacts/vendor/hdapi_v2/bg_resolve_runtime_nonclaims.json`
  * `docs/acceptance_map_epic036.json`
  * `audit/qa/hde-epic036/route_policy_decision.log`

Preflight check:

* Confirm Step-0B completed.
* The helper checks required files at runtime.

If missing, activation/install action:

* Do not install dependencies.
* Mark this check `TOOLING_BLOCKED`.

If still unavailable:

* Keep `TOOLING_BLOCKED`.

Preconditions:

* Run from repo root.
* Closed rails only.

Numbered PO actions:

1. Paste the command.
2. Open `audit/qa/hde-epic036/checks/po-009/primary.log`.
3. Confirm nonclaims for public Reader, public route, public flag, public payload change, new HTTP home, app-side credential ownership, full runtime conformance, raw payload persistence, and AI scope.
4. Confirm the sibling path proof exists.

Command 1:
SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC python audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py po-009

What to look for:

* `JSON_OK ... no_claims.public_reader_change='NONE'`
* `JSON_OK ... no_claims.public_route='NONE'`
* `JSON_OK ... no_claims.new_http_home='NONE'`
* `JSON_OK ... no_claims.full_hdapi_v2_runtime_conformance='NONE'`
* `JSON_OK ... no_claims.ai_scope='NONE'`
* `TEXT_OK ... no_full_hdapi_v2_runtime_conformance=true`

Required deliverables:

* `audit/qa/hde-epic036/checks/po-009/primary.log`
* `audit/qa/hde-epic036/checks/po-009/primary.log.path_proof.txt`
* `artifacts/vendor/hdapi_v2/bg_resolve_runtime_nonclaims.json`
* `docs/acceptance_map_epic036.json`
* `audit/qa/hde-epic036/route_policy_decision.log`

PASS criteria tied to deliverables:

* PASS if forbidden public/product/runtime/raw-payload/AI claims remain absent.
* PASS if the boundaries are recorded as nonclaims.

FAIL criteria tied to deliverables:

* `FAIL_BEHAVIOR` if public Reader, public route, public flag, public payload, new HTTP home, app-side credential ownership, raw payload persistence, AI scope, or full runtime conformance is claimed.
* `TOOLING_BLOCKED` if required artifacts or helper are missing.
* `FAIL_TOOLING` if the primary log or path proof cannot be written.

Blocked posture:

* If nonclaim evidence is missing, keep `TOOLING_BLOCKED`.

### CHECK po-010: PO-010

Goal:

Produce one bounded live production-like QA proof for this epic unless a controlling exemption is supplied. This plan uses a PO-approved live v2 base value and expects route-policy refusal before legacy BodyGraph request construction.

Required dependencies:

* Python 3
* Step-0B QA helper
* importable repo CLI package
* PO-approved live v2 base URL assigned to `HD_API_BASE_URL`
* no vendor secret value required for the expected proof

Preflight check:

* Confirm Step-0B completed.
* Confirm the PO-approved target is a v2 base.
* Confirm no raw secret value is entered into the log.

If missing, activation/install action:

* Do not install dependencies.
* If `HD_API_BASE_URL` is not supplied, mark `TOOLING_BLOCKED`.
* If the repo CLI is not importable, mark `TOOLING_BLOCKED`.

If still unavailable:

* Keep `TOOLING_BLOCKED`.

Preconditions:

* PO must authorize the bounded live-target configuration check.
* PO must supply the v2 base value only in Variable Import.
* Do not supply `HD_API_KEY` or `GEO_API_KEY` for this check.
* Do not run OPS.
* Do not persist raw vendor payloads.
* Expected CLI exit code inside the proof is `1`; the helper check passes only if the observed failure is `PROVIDER_ROUTE_UNSUPPORTED` / `unsupported_runtime_nonclaim`.

Setup:

A) Variable Import

Command 1:
export HD_API_BASE_URL="PO_SET_APPROVED_LIVE_V2_BASE_URL"

Numbered PO actions:

1. Replace the value in Variable Import with the PO-approved live v2 base URL.
2. Paste the Variable Import command.
3. Paste the PO-010 command.
4. Open `audit/qa/hde-epic036/checks/po-010/live_route_policy.log`.
5. Confirm it records `SAFE_MODE=0`, `ALLOW_NETWORK=1`, and `HD_API_BASE_URL=PO_APPROVED_V2_BASE_REDACTED`.
6. Confirm it records `PROVIDER_ROUTE_UNSUPPORTED`.
7. Confirm it records `unsupported_runtime_nonclaim`.
8. Open `audit/qa/hde-epic036/checks/po-010/primary.log`.
9. Confirm `status=PASS`.
10. Confirm the sibling path proofs exist.

Command 2:
SAFE_MODE=0 ALLOW_NETWORK=1 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC HD_API_BASE_URL="${HD_API_BASE_URL}" python audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py po-010

What to look for:

* `po-010 status=PASS exit_code=0`
* `audit/qa/hde-epic036/checks/po-010/live_route_policy.log`
* `PROVIDER_ROUTE_UNSUPPORTED`
* `unsupported_runtime_nonclaim`
* `HD_API_BASE_URL=PO_APPROVED_V2_BASE_REDACTED`
* no secret value
* no raw request or response payload
* sibling path proof for `live_route_policy.log`
* sibling path proof for `primary.log`

Required deliverables:

* `audit/qa/hde-epic036/checks/po-010/primary.log`
* `audit/qa/hde-epic036/checks/po-010/primary.log.path_proof.txt`
* `audit/qa/hde-epic036/checks/po-010/live_route_policy.log`
* `audit/qa/hde-epic036/checks/po-010/live_route_policy.log.path_proof.txt`

PASS criteria tied to deliverables:

* PASS if the bounded live-target configuration check records `PROVIDER_ROUTE_UNSUPPORTED`.
* PASS if the bounded live-target configuration check records `unsupported_runtime_nonclaim`.
* PASS if the proof shows the PO-approved v2 base was redacted in evidence.
* PASS if no raw vendor payload, secret value, full runtime conformance, BodyGraph-detail compatibility, OPS completion, PF09 movement, HDE-FERM008 parent Done, or closeout is claimed.
* PASS may claim `NO_EXTERNAL_IO_ON_REFUSAL_OK` and `ENV_RAILS_POLICY_OK`.

FAIL criteria tied to deliverables:

* `TOOLING_BLOCKED` if PO-approved `HD_API_BASE_URL` is missing.
* `TOOLING_BLOCKED` if the repo CLI is unavailable.
* `FAIL_BEHAVIOR` if the live-target route-policy result does not record `PROVIDER_ROUTE_UNSUPPORTED`.
* `FAIL_BEHAVIOR` if the live-target route-policy result does not record `unsupported_runtime_nonclaim`.
* `FAIL_BEHAVIOR` if the step logs a raw secret value, raw vendor payload, or full runtime-conformance claim.
* `FAIL_TOOLING` if the primary log, live proof log, or path proofs cannot be written.

Blocked posture:

* If the PO-approved v2 base is unavailable, classify the step as `TOOLING_BLOCKED`.
* Do not substitute HDE-EPIC035 OPS evidence for this step.
* Do not invent a controlling exemption.

### CHECK po-011: PO-011

Goal:

Verify that the bounded live production-like proof demonstrates the relevant route-policy behavior without overclaiming broader runtime compatibility.

Required dependencies:

* Python 3
* Step-0B QA helper
* Successful or at least interpretable PO-010 live proof log
* Existing repo artifacts:

  * `artifacts/vendor/hdapi_v2/bg_resolve_runtime_nonclaims.json`
  * `artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json`

Preflight check:

* Confirm PO-010 ran and produced `audit/qa/hde-epic036/checks/po-010/live_route_policy.log`.
* The helper checks required files at runtime.

If missing, activation/install action:

* Do not install dependencies.
* Mark this check `TOOLING_BLOCKED`.

If still unavailable:

* Keep `TOOLING_BLOCKED`.

Preconditions:

* Run after PO-010.
* Closed rails for this interpretive check.

Numbered PO actions:

1. Paste the command.
2. Open `audit/qa/hde-epic036/checks/po-011/primary.log`.
3. Confirm the PO-010 live proof log is present and path-proven.
4. Confirm it contains `PROVIDER_ROUTE_UNSUPPORTED`.
5. Confirm it contains `unsupported_runtime_nonclaim`.
6. Confirm runtime nonclaims and BodyGraph-detail sufficiency remain bounded.
7. Confirm the sibling path proof exists.

Command 1:
SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC python audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py po-011

What to look for:

* `FILE_OK audit/qa/hde-epic036/checks/po-010/live_route_policy.log`
* `TEXT_OK ... PROVIDER_ROUTE_UNSUPPORTED`
* `TEXT_OK ... unsupported_runtime_nonclaim`
* `JSON_OK ... chart_simple_success_bodygraph_detail_claim='NONE'`
* `JSON_OK ... no_compatibility_by_inference=True`
* `JSON_OK ... bodygraph_detail_sufficiency='UNSUPPORTED_RUNTIME_NONCLAIM'`

Required deliverables:

* `audit/qa/hde-epic036/checks/po-011/primary.log`
* `audit/qa/hde-epic036/checks/po-011/primary.log.path_proof.txt`
* `audit/qa/hde-epic036/checks/po-010/live_route_policy.log`
* `audit/qa/hde-epic036/checks/po-010/live_route_policy.log.path_proof.txt`
* `artifacts/vendor/hdapi_v2/bg_resolve_runtime_nonclaims.json`
* `artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json`

PASS criteria tied to deliverables:

* PASS if PO-010 live proof exists and records route-policy refusal.
* PASS if the live proof does not claim broader runtime compatibility.
* PASS if runtime nonclaims and BodyGraph-detail insufficiency remain recorded.

FAIL criteria tied to deliverables:

* `TOOLING_BLOCKED` if PO-010 live proof is missing.
* `FAIL_BEHAVIOR` if PO-010 overclaims full runtime compatibility.
* `FAIL_BEHAVIOR` if BodyGraph-detail sufficiency is claimed without later proof.
* `FAIL_TOOLING` if the primary log or path proof cannot be written.

Blocked posture:

* If PO-010 is absent or blocked, keep PO-011 `TOOLING_BLOCKED`.

### CHECK po-012: PO-012

Goal:

Verify that future work does not use this epic’s evidence to claim full BodyGraph-detail compatibility unless a later proof establishes required internal data coverage.

Required dependencies:

* Python 3
* Step-0B QA helper
* Existing repo artifacts:

  * `docs/acceptance_map_epic036.json`
  * `artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json`
  * `artifacts/vendor/hdapi_v2/bg_resolve_runtime_nonclaims.json`

Preflight check:

* Confirm Step-0B completed.
* The helper checks required files at runtime.

If missing, activation/install action:

* Do not install dependencies.
* Mark this check `TOOLING_BLOCKED`.

If still unavailable:

* Keep `TOOLING_BLOCKED`.

Preconditions:

* Run from repo root.
* Closed rails only.

Numbered PO actions:

1. Paste the command.
2. Open `audit/qa/hde-epic036/checks/po-012/primary.log`.
3. Confirm acceptance map records `v2_chart_data_feeds_existing_bodygraph_cache_person_compat_flows=false`.
4. Confirm BodyGraph-detail sufficiency remains `UNSUPPORTED_RUNTIME_NONCLAIM`.
5. Confirm chart simple success BodyGraph detail claim remains `NONE`.
6. Confirm the sibling path proof exists.

Command 1:
SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC python audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py po-012

What to look for:

* `JSON_OK docs/acceptance_map_epic036.json :: v2_chart_data_feeds_existing_bodygraph_cache_person_compat_flows=False`
* `JSON_OK docs/acceptance_map_epic036.json :: bodygraph_detail_sufficiency='UNSUPPORTED_RUNTIME_NONCLAIM'`
* `JSON_OK ... chart_simple_success_bodygraph_detail_claim='NONE'`

Required deliverables:

* `audit/qa/hde-epic036/checks/po-012/primary.log`
* `audit/qa/hde-epic036/checks/po-012/primary.log.path_proof.txt`
* `docs/acceptance_map_epic036.json`
* `artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json`
* `artifacts/vendor/hdapi_v2/bg_resolve_runtime_nonclaims.json`

PASS criteria tied to deliverables:

* PASS if future compatibility remains blocked on later internal data coverage proof.
* PASS if this epic’s evidence does not claim full BodyGraph-detail compatibility.
* PASS if the primary log and sibling path proof exist.

FAIL criteria tied to deliverables:

* `FAIL_BEHAVIOR` if future compatibility is claimed without a later proof.
* `FAIL_BEHAVIOR` if this epic’s evidence is used to claim full BodyGraph-detail compatibility.
* `TOOLING_BLOCKED` if required artifacts or helper are missing.
* `FAIL_TOOLING` if the primary log or path proof cannot be written.

Blocked posture:

* If required future-proof boundary artifacts are missing, keep `TOOLING_BLOCKED`.

### CHECK qa-13-governed-evidence-gates: Governed evidence gates

Goal:

Verify targeted tests, generated evidence check mode, evidence paths, canonical JSON posture, Evidence Index, Machine Mirror, hash sentinels, mirror schema, and LF gates for HDE-EPIC036.

Required dependencies:

* Python 3
* pytest
* bash
* Step-0B QA helper
* Existing repo scripts:

  * `tools/evidence/generate_hde_epic036_bg_resolve_route_policy.py`
  * `tools/evidence/validate_evidence_paths.py`
  * `tools/evidence/check_lf_endings.py`
  * `tools/evidence/update_evidence_index.py`
  * `ci/checks/check_mirror_schema.sh`
  * `ci/checks/check_evidence_index_hash.sh`
  * `ci/checks/check_final_lf.sh`

Preflight check:

* Helper imports pytest before running tests.
* Helper checks required scripts and files before running commands.

If missing, activation/install action:

* Do not install pytest or other dependencies inside this runbook.
* Mark this check `TOOLING_BLOCKED`.

If still unavailable:

* Keep `TOOLING_BLOCKED`.

Preconditions:

* Run after PO-001 through PO-012.
* Closed rails only.
* Do not regenerate artifacts; the generator is invoked only with `--check`.

Numbered PO actions:

1. Paste the command.
2. Open `audit/qa/hde-epic036/checks/qa-13-governed-evidence-gates/primary.log`.
3. Confirm pytest import succeeded.
4. Confirm targeted pytest command exited 0.
5. Confirm generator check exited 0.
6. Confirm evidence path validation exited 0.
7. Confirm LF check exited 0.
8. Confirm evidence index check exited 0.
9. Confirm mirror schema, evidence hash, and final-LF scripts exited 0.
10. Confirm canonical JSON checks passed for the acceptance map and `bg_resolve_*` JSON artifacts.
11. Confirm intended and claimed tokens match the approved token set for this gate.
12. Confirm the sibling path proof exists.

Command 1:
SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC python audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py qa-13-governed-evidence-gates

What to look for:

* `PYTEST_IMPORT_OK`
* `COMMAND ... pytest ...`
* `EXIT_CODE 0` after pytest
* `COMMAND ... generate_hde_epic036_bg_resolve_route_policy.py --check`
* `EXIT_CODE 0`
* `COMMAND ... validate_evidence_paths.py`
* `EXIT_CODE 0`
* `COMMAND ... check_lf_endings.py`
* `EXIT_CODE 0`
* `COMMAND ... update_evidence_index.py --check`
* `EXIT_CODE 0`
* `COMMAND bash ci/checks/check_mirror_schema.sh`
* `EXIT_CODE 0`
* `COMMAND bash ci/checks/check_evidence_index_hash.sh`
* `EXIT_CODE 0`
* `COMMAND bash ci/checks/check_final_lf.sh`
* `EXIT_CODE 0`
* `JSON_CANONICAL_OK`
* token checks for `TESTS_PASS_OK`, `EVIDENCE_INDEX_UPDATED_OK`, `MACHINE_MIRROR_UPDATED_OK`, `EVIDENCE_INDEX_HASH_OK`, `EVIDENCE_PATHS_VALIDATED_OK`, `EVIDENCE_PATH_PROOFS_OK`, and `JSON_CANONICAL_CHECK_OK`

Required deliverables:

* `audit/qa/hde-epic036/checks/qa-13-governed-evidence-gates/primary.log`
* `audit/qa/hde-epic036/checks/qa-13-governed-evidence-gates/primary.log.path_proof.txt`
* `tests/bodygraph/test_bg_resolve_route_policy.py`
* `tests/bodygraph/test_resolver_vendor.py`
* `tests/cli/test_bg_resolve.py`
* `tests/evidence/test_hde_epic036_pr02_evidence_loop.py`
* `tools/evidence/generate_hde_epic036_bg_resolve_route_policy.py`
* `tools/evidence/validate_evidence_paths.py`
* `tools/evidence/check_lf_endings.py`
* `tools/evidence/update_evidence_index.py`
* `ci/checks/check_mirror_schema.sh`
* `ci/checks/check_evidence_index_hash.sh`
* `ci/checks/check_final_lf.sh`
* `docs/evidence/INDEX.json`
* `docs/evidence/INDEX.sha256`
* `artifacts/evidence_index.jsonl`
* `artifacts/evidence_index.jsonl.sha256`
* `docs/acceptance_map_epic036.json`
* `artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json`
* `artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json`
* `artifacts/vendor/hdapi_v2/bg_resolve_runtime_nonclaims.json`
* `artifacts/vendor/hdapi_v2/bg_resolve_request_shape.snapshot.json`
* `artifacts/vendor/hdapi_v2/bg_resolve_policy_binding.snapshot.json`

PASS criteria tied to deliverables:

* PASS if targeted tests exit 0.
* PASS if route-policy generator check mode exits 0.
* PASS if evidence path validation exits 0.
* PASS if LF checks exit 0.
* PASS if Evidence Index check exits 0.
* PASS if mirror schema, hash sentinel, and final-LF checks exit 0.
* PASS if canonical JSON checks pass for HDE-EPIC036 acceptance map and `bg_resolve_*` artifacts.
* PASS may claim `TESTS_PASS_OK`, `EVIDENCE_INDEX_UPDATED_OK`, `MACHINE_MIRROR_UPDATED_OK`, `EVIDENCE_INDEX_HASH_OK`, `EVIDENCE_PATHS_VALIDATED_OK`, `EVIDENCE_PATH_PROOFS_OK`, and `JSON_CANONICAL_CHECK_OK`.

FAIL criteria tied to deliverables:

* `TOOLING_BLOCKED` if Python, pytest, bash, required tests, required scripts, or required evidence files are missing.
* `FAIL_TOOLING` if a command cannot execute due to tool/invocation failure.
* `FAIL_BEHAVIOR` if a targeted test or governed evidence check executes and reports mismatch.
* `FAIL_BEHAVIOR` if approved tokens are missing from the acceptance map.
* `FAIL_TOOLING` if primary log or path proof cannot be written.

Blocked posture:

* If pytest or a required script is unavailable, keep `TOOLING_BLOCKED`.
* Do not install missing dependencies inside this runbook.

### CHECK qa-14-close-out-deliverables: Close-out deliverables

Goal:

Produce the PF27-required closeout execution deliverables: QA step-log manifest, discovery artifact, and QA RCA / Doc Delta summary. This check does not perform PO closeout and does not claim epic closure.

Required dependencies:

* Python 3
* Step-0B QA helper
* Existing prior check primary logs and sibling path proofs for:

  * `step-0b-doc-delta-capture`
  * `po-001`
  * `po-002`
  * `po-003`
  * `po-004`
  * `po-005`
  * `po-006`
  * `po-007`
  * `po-008`
  * `po-009`
  * `po-010`
  * `po-011`
  * `po-012`
  * `qa-13-governed-evidence-gates`

Preflight check:

* Helper checks every prior primary log and sibling path proof.

If missing, activation/install action:

* Do not reconstruct missing evidence.
* Mark this check `TOOLING_BLOCKED`.

If still unavailable:

* Keep `TOOLING_BLOCKED`.

Preconditions:

* Run after Step-0B, PO-001 through PO-012, and `qa-13-governed-evidence-gates`.
* Closed rails only.
* This check writes only closeout QA artifacts under `audit/qa/hde-epic036/`.

Numbered PO actions:

1. Paste the command.
2. Open `audit/qa/hde-epic036/checks/qa-14-close-out-deliverables/primary.log`.
3. Confirm status is PASS.
4. Open `audit/qa/hde-epic036/qa_step_logs_manifest.json`.
5. Confirm each expected check is listed with `check_id`, `status`, `log_path`, and `path_proof_path`.
6. Open `audit/qa/hde-epic036/00_meta/discovery_artifact.md`.
7. Open `audit/qa/hde-epic036/00_meta/qa_rca_doc_delta_summary.md`.
8. Confirm no PO closeout, board update, PF edit, merge, PF09 status movement, OPS completion, full runtime conformance, public expansion, raw payload persistence, or AI scope is claimed.
9. Confirm sibling path proofs exist for all closeout deliverables.

Command 1:
SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC python audit/qa/hde-epic036/00_meta/hde036_live_qa_harness.py qa-14-close-out-deliverables

What to look for:

* `audit/qa/hde-epic036/qa_step_logs_manifest.json`
* `audit/qa/hde-epic036/qa_step_logs_manifest.json.path_proof.txt`
* `audit/qa/hde-epic036/00_meta/discovery_artifact.md`
* `audit/qa/hde-epic036/00_meta/discovery_artifact.md.path_proof.txt`
* `audit/qa/hde-epic036/00_meta/qa_rca_doc_delta_summary.md`
* `audit/qa/hde-epic036/00_meta/qa_rca_doc_delta_summary.md.path_proof.txt`
* `audit/qa/hde-epic036/checks/qa-14-close-out-deliverables/primary.log`
* `audit/qa/hde-epic036/checks/qa-14-close-out-deliverables/primary.log.path_proof.txt`

Required deliverables:

* `audit/qa/hde-epic036/checks/qa-14-close-out-deliverables/primary.log`
* `audit/qa/hde-epic036/checks/qa-14-close-out-deliverables/primary.log.path_proof.txt`
* `audit/qa/hde-epic036/qa_step_logs_manifest.json`
* `audit/qa/hde-epic036/qa_step_logs_manifest.json.path_proof.txt`
* `audit/qa/hde-epic036/00_meta/discovery_artifact.md`
* `audit/qa/hde-epic036/00_meta/discovery_artifact.md.path_proof.txt`
* `audit/qa/hde-epic036/00_meta/qa_rca_doc_delta_summary.md`
* `audit/qa/hde-epic036/00_meta/qa_rca_doc_delta_summary.md.path_proof.txt`

PASS criteria tied to deliverables:

* PASS if the QA step-log manifest exists and lists every expected check with status, log_path, and path_proof_path.
* PASS if the manifest path proof exists and matches the manifest path.
* PASS if the discovery artifact exists.
* PASS if the QA RCA / Doc Delta summary exists and includes coverage vs plan accounting.
* PASS if the qa-14 primary log has the PF27 header and sibling path proof.
* PASS does not claim PO closeout.

FAIL criteria tied to deliverables:

* `TOOLING_BLOCKED` if one or more expected prior check primary logs or sibling path proofs is missing.
* `FAIL_TOOLING` if a primary log exists but has an unreadable header.
* `FAIL_TOOLING` if closeout deliverables cannot be written.
* `FAIL_BEHAVIOR` if closeout deliverables claim PO closeout, runtime vendor conformance, public Reader expansion, new HTTP home, AI scope, PF edits, product implementation, OPS completion, HDE-FERM008 parent Done, PF09 status movement, or epic closeout.

Blocked posture:

* If any expected prior check primary log or path proof is missing, keep `TOOLING_BLOCKED`.
* Do not invent or reconstruct missing prior evidence.

### Moon Loop posture

Moon Loop is not the default path.

Allowed Moon Loop scope:

* QA-created evidence-harness defects
* header repair
* path-proof repair
* doc-delta capture repair
* manifest assembly repair
* QA evidence assembly defects under `audit/qa/hde-epic036/`

Not allowed under Moon Loop:

* product code changes
* repo tests changes
* evidence generator changes
* governed artifact changes outside the QA root
* public contracts
* PF documents
* acceptance tokens
* OPS execution
* implementation subsystem changes

If a non-QA-root change is needed, classify it as outside this Live QA run and stop the affected check.

### Final check before PO submission

Before submitting the QA evidence bundle, confirm:

* every check has `primary.log`
* every `primary.log` has `primary.log.path_proof.txt`
* `audit/qa/hde-epic036/qa_step_logs_manifest.json` exists
* `audit/qa/hde-epic036/qa_step_logs_manifest.json.path_proof.txt` exists
* `audit/qa/hde-epic036/00_meta/discovery_artifact.md` exists
* `audit/qa/hde-epic036/00_meta/discovery_artifact.md.path_proof.txt` exists
* `audit/qa/hde-epic036/00_meta/qa_rca_doc_delta_summary.md` exists
* `audit/qa/hde-epic036/00_meta/qa_rca_doc_delta_summary.md.path_proof.txt` exists
* `po-010` live proof log exists and contains no secret value
* no primary log claims PF09 status movement, HDE-FERM008 parent Done, OPS completion, epic closeout, public expansion, raw payload persistence, AI scope, or full runtime conformance

ASK OK?
