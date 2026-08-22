from __future__ import annotations

from contextlib import contextmanager
import hashlib
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

BOOTSTRAP_ROOT = Path(__file__).resolve().parents[4]
if str(BOOTSTRAP_ROOT) not in sys.path:
    sys.path.insert(0, str(BOOTSTRAP_ROOT))

from tools.evidence.update_evidence_index import _refresh_path_proof
from tools.qa import generate_epic_close_pack as close_pack
from tools.qa.generate_epic_close_pack import (
    REGULAR_GIT_MODES,
    _GitObjectStore,
    _establish_git_context,
    _git_blob_payload,
    _head,
    _load_model,
    _tree_entries,
)
from tools.qa.qa_harness import (
    CheckResult,
    HarnessConfig,
    Status,
    record_check,
    run_pytest_check,
    verify_manifest_entry,
)

EPIC = "HDE-EPIC039"
EXPECTED_REPOSITORY = "amthorn78/glow-hdengine-v2"
CFG = HarnessConfig(EPIC)
ROOT = CFG.repo_root
QA = CFG.qa_root
SCRIPT = "audit/qa/hde-epic039/00_meta/qa_runner.py"
SOURCE_COMMANDS = (
    ("git", "rev-parse", "--show-toplevel"),
    ("git", "rev-parse", "HEAD"),
    ("git", "symbolic-ref", "--short", "-q", "HEAD"),
    ("git", "status", "--short", "--untracked-files=all"),
    ("git", "remote", "get-url", "origin"),
)
ENV = {
    "LC_ALL": "C",
    "LANG": "C",
    "TZ": "UTC",
    "SAFE_MODE": "1",
    "ALLOW_NETWORK": "0",
    "APP_ENV": "test",
}
REFS = (
    "PF09.1-Canon-HDE-Build-Checklist-Calcination",
    "PF12-Canon-HDE-Schemas-and-Artifacts",
    "PF19-Canon-Glow-QA-Guide",
    "PF27-Canon-Plan-Templates",
)
NAMES = {
    "step-0b-doc-delta-capture": "Step-0B Doc Delta Capture",
    "po-001": "Deterministic governed structured-data outputs",
    "po-002": "Declared unordered-collection semantics",
    "po-003": "Governed Human Design corpus invariants",
    "po-004": "Coherent evidence publication",
    "po-005": "Human and machine evidence agreement",
    "po-006": "Causal QA outcome classification",
    "po-007": "Semantic declaration propagation",
    "po-008": "Current and historical evidence identity",
    "po-009": "Change-aware exact-candidate automation",
    "po-010": "Retired automation remains inactive",
    "po-011": "Feedback-free closeout derivation",
    "po-012": "Manifest-committed candidate publication",
    "po-013": "Reusable capability scope boundary",
}
ORDER = tuple(NAMES)
EXTRA_IDS = {"po-004", "po-005"}
MOON_LOOP_REVISION = "moon-loop-2-extended"
MOON_LOOP_AUTHORITY = "Product Owner direct instruction on 2026-08-22"
MOON_LOOP_AUTHORIZATION = "We aren't doing that. I need you to fix the script as a moon loop revision, and mention the planning defect in your report so it can fix future process"
EXTENDED_MOON_LOOP_AUTHORIZATION = "do an extended moon loop if needed"
ORIGINAL_HELPER_SHA256 = "7cc185a4b31f56232a69743f2c7203088628b951e704abb93a9f643a8541849e"
PLANNING_DEFECT = (
    "The approved r4 plan validated the embedded runner only by payload SHA-256 and "
    "compile() syntax; it did not smoke-test the exact direct-path command it required for "
    "execution. The pinned runner therefore lacked repository-root import bootstrapping. "
    "The same plan prohibited the requirements-dev.txt synchronization mandated before pytest "
    "by AGENTS.md, so its subsequent pytest version checks did not satisfy the required "
    "install-then-readiness sequence. It also assumed the close-pack Git reader could consume "
    "Codespaces-added, quoted hash-bearing branch metadata even though that reader rejects "
    "such non-core Git-config values. It also treated pytest and jsonschema as the complete "
    "dependency boundary even though the selected canonical-gate test imports Flask from "
    "requirements.txt, which requirements-dev.txt does not include. Finally, the approved "
    "PO-003 selector retained a legacy pre-directional-corpus key assertion and lacked the "
    "temporary-pack isolation already used by sibling narrative tests, allowing repo-root "
    "cache residue. These were QA planning, test-maintenance, and execution-surface defects, "
    "not product-runtime regressions."
)
FUTURE_PROCESS_CORRECTION = (
    "Before approval, execute the exact generated helper command in the named venue, "
    "reconcile plan dependency policy with repository instructions, and validate every "
    "venue-created Git configuration form consumed by repository-native readers; synchronize "
    "both runtime and development requirements and smoke-collect the complete approved selector "
    "import closure before publishing the first governed QA receipt; reconcile selected test "
    "expectations with current governed key grammars and require temporary-path isolation for "
    "tests that mount content-addressed runtime data; validate ephemeral venue metadata for "
    "stability within each proof operation rather than treating it as event-wide source identity."
)
_CODESPACES_METADATA_KEY = "github-pr-owner-number"
_CODESPACES_METADATA_VALUE_RE = re.compile(
    r'amthorn78#glow-hdengine-v2#[0-9]+'
)


def now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def moon_loop_record():
    corrected_test = ROOT / "tests/unit/test_narratives_composer.py"
    return {
        "authority": MOON_LOOP_AUTHORITY,
        "authorization_verbatim": MOON_LOOP_AUTHORIZATION,
        "extended_authorization_verbatim": EXTENDED_MOON_LOOP_AUTHORIZATION,
        "dependency_action": "python -m pip install -r requirements.txt; python -m pip install -r requirements-dev.txt; python -m pytest --version",
        "dependency_setup_network_observed": True,
        "dependency_setup_network_note": "pip package-index access occurred during runtime and development synchronization before QA behavior checks",
        "future_process_correction": FUTURE_PROCESS_CORRECTION,
        "initial_attempt": {
            "command": "python -B audit/qa/hde-epic039/00_meta/qa_runner.py step-0b-doc-delta-capture",
            "governed_receipt_created": False,
            "observed_failure": "ModuleNotFoundError: No module named 'tools' before helper main()",
            "plan_status_mapping": "TOOLING_BLOCKED",
        },
        "po001_collection_attempt": {
            "governed_receipt_created": True,
            "historical_record_kind": "operator-observed; replaced current-state receipt is not independently retained",
            "observed_failure": "ModuleNotFoundError: No module named 'flask' during pytest collection",
            "plan_status_mapping": "FAIL_TOOLING",
            "product_assertion_reached": False,
        },
        "po003_behavior_attempt": {
            "governed_receipt_created": True,
            "historical_record_kind": "operator-observed; replaced current-state receipt is not independently retained",
            "observed_failure": "legacy harmony.cool.shared prefix expectation contradicted current nar.harmony.cool.shared key grammar",
            "plan_status_mapping": "FAIL_BEHAVIOR",
            "product_runtime_regression_found": False,
            "test_only_corrections": [
                "tests/unit/test_narratives_composer.py namespaced key expectation",
                "tests/unit/test_narratives_composer.py temporary-pack isolation fixture",
            ],
        },
        "initial_ready_finalizer_attempt": {
            "all_check_receipts_passed": True,
            "observed_result": "NOT READY",
            "reason": "Moon Loop finalizer incorrectly compared ephemeral Codespaces Git-config bytes across the full QA event",
            "correction": "retain per-operation byte/fingerprint stability checks and validate only the recorded config digest shape at finalization",
        },
        "original_helper_sha256": ORIGINAL_HELPER_SHA256,
        "planning_defect": PLANNING_DEFECT,
        "revision": MOON_LOOP_REVISION,
        "revised_helper_sha256": sha(ROOT / SCRIPT),
        "scope": "QA-created runner plus the selected stale narrative-composer test only; approved selector paths, rails variables, evidence paths, product runtime sources, governed sources, and Git config remain unchanged",
        "tracked_test_correction": {
            "path": corrected_test.relative_to(ROOT).as_posix(),
            "sha256": sha(corrected_test),
            "changes": [
                "require current nar.harmony.cool.shared key namespace",
                "mount the narrative pack only under pytest tmp_path",
            ],
        },
    }


def _codespaces_config_payload(payload):
    try:
        text = payload.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise RuntimeError("Codespaces Git config is not UTF-8") from exc
    section = ""
    subsection = None
    removed = 0
    retained = []
    for raw_line in text.splitlines(keepends=True):
        stripped = raw_line.strip()
        if stripped.startswith("["):
            match = re.fullmatch(
                r'\[([A-Za-z0-9.-]+)(?:\s+"([^"\\]*)")?\]', stripped
            )
            if match is None:
                section, subsection = "", None
            else:
                section, subsection = match.group(1).casefold(), match.group(2)
        if section == "branch" and subsection == "main":
            metadata = re.fullmatch(
                r'github-pr-owner-number\s*=\s*"([^"\\]*)"',
                stripped,
                flags=re.IGNORECASE,
            )
            if metadata is not None:
                if _CODESPACES_METADATA_VALUE_RE.fullmatch(metadata.group(1)) is None:
                    raise RuntimeError("Codespaces Git metadata route is outside the Moon Loop waiver")
                removed += 1
                continue
            if stripped.casefold().startswith(_CODESPACES_METADATA_KEY):
                raise RuntimeError("Codespaces Git metadata syntax is outside the Moon Loop waiver")
        retained.append(raw_line)
    if removed == 0:
        raise RuntimeError("expected Codespaces Git metadata is absent")
    return "".join(retained).encode("utf-8"), removed


@contextmanager
def codespaces_git_config_compat(context):
    config_path = context.common_dir / "config"
    original_reader = close_pack._stable_absolute_read
    payload, metadata = original_reader(config_path, max_bytes=16 * 1024 * 1024)
    original_fingerprint = close_pack._fingerprint(metadata)
    original_sha256 = hashlib.sha256(payload).hexdigest()
    sanitized, removed = _codespaces_config_payload(payload)

    def compatible_reader(path, *, max_bytes=None):
        current_payload, current_metadata = original_reader(path, max_bytes=max_bytes)
        if Path(path) != config_path:
            return current_payload, current_metadata
        if (
            current_payload != payload
            or close_pack._fingerprint(current_metadata) != original_fingerprint
        ):
            raise RuntimeError("Git config changed during Moon Loop compatibility read")
        return sanitized, current_metadata

    close_pack._stable_absolute_read = compatible_reader
    try:
        yield {
            "applied": True,
            "config_sha256": original_sha256,
            "source_config_modified": False,
            "waived_key": "branch.main." + _CODESPACES_METADATA_KEY,
            "waived_line_count": removed,
        }
    finally:
        close_pack._stable_absolute_read = original_reader
        final_payload, final_metadata = original_reader(
            config_path, max_bytes=16 * 1024 * 1024
        )
        if (
            final_payload != payload
            or close_pack._fingerprint(final_metadata) != original_fingerprint
        ):
            raise RuntimeError("Git config changed during Moon Loop compatibility scope")


def self_cmd(check_id, args=()):
    return (sys.executable, "-B", SCRIPT, check_id, *args)


def env_issue():
    bad = {
        key: {"expected": value, "actual": os.environ.get(key)}
        for key, value in ENV.items()
        if os.environ.get(key) != value
    }
    return "" if not bad else "required environment mismatch: " + json.dumps(bad, sort_keys=True)


def _origin_slug(url):
    match = re.search(r"github\.com(?::|/)([^/\s:]+)/([^/\s]+?)(?:\.git)?/?$", url)
    return f"{match.group(1)}/{match.group(2)}" if match else "UNKNOWN"


def source_snapshot():
    completed = []
    for command in SOURCE_COMMANDS:
        result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, check=False)
        completed.append(result)
    root_result, head_result, branch_result, status_result, origin_result = completed
    if any(result.returncode for result in (root_result, head_result, status_result, origin_result)):
        raise RuntimeError("required read-only source-provenance query failed")
    if branch_result.returncode not in {0, 1}:
        raise RuntimeError("branch-or-detached query failed")
    context = _establish_git_context(ROOT)
    with codespaces_git_config_compat(context) as config_compat:
        store = _GitObjectStore(context)
        parsed_head = _head(context, store)
        tree = _tree_entries(context, store)
    head = head_result.stdout.strip()
    head_ref = branch_result.stdout.strip() if branch_result.returncode == 0 else "DETACHED"
    repository = _origin_slug(origin_result.stdout.strip())
    reported_root = Path(root_result.stdout.strip()).resolve()
    interfaces = {
        "manifest_entry_validator": callable(verify_manifest_entry),
        "close_pack_head_reader": callable(_head),
        "close_pack_tree_reader": callable(_tree_entries),
    }
    posture_ok = (
        repository == EXPECTED_REPOSITORY
        and reported_root == ROOT.resolve()
        and ROOT.name == "glow-hdengine-v2"
        and parsed_head == head
        and all(interfaces.values())
        and bool(tree)
    )
    snapshot = {
        "actual_head": head,
        "head_ref_or_detached": head_ref,
        "repository": repository,
        "repository_root_basename": ROOT.name,
        "source_identity_is_pass_gate": False,
        "preplanned_commit_equality_required": False,
        "required_current_code_posture_valid": posture_ok,
        "required_interfaces": interfaces,
        "tracked_tree_entry_count": len(tree),
        "working_tree_status_non_gating": status_result.stdout.splitlines(),
        "source_provenance_commands": [list(command) for command in SOURCE_COMMANDS],
        "routing_provenance": {
            "approved_entrypoint": SCRIPT,
            "moon_loop_authority": MOON_LOOP_AUTHORITY,
            "plan_revision": "r4 + " + MOON_LOOP_REVISION,
            "repository_route": repository,
            "venue_preference": "GitHub Codespaces",
            "venue_specific_claim": "NOT CLAIMED",
        },
        "codespaces_git_config_compat": config_compat,
    }
    return snapshot, context, store, tree


def proof_ok(path):
    proof = Path(str(path) + ".path_proof.txt")
    if not path.is_file() or not proof.is_file():
        return False, "artifact or sibling proof missing"
    fields = {}
    try:
        for line in proof.read_text(encoding="utf-8").splitlines():
            if ": " in line:
                key, value = line.split(": ", 1)
                fields[key] = value
    except (OSError, UnicodeError):
        return False, "proof unreadable"
    relative = path.relative_to(ROOT).as_posix()
    if fields.get("path") != relative:
        return False, "proof path mismatch"
    if fields.get("sha256") != sha(path):
        return False, "proof sha256 mismatch"
    if fields.get("size_bytes") != str(path.stat().st_size):
        return False, "proof size mismatch"
    return True, ""


def receipt_paths(check_id):
    log = QA / "checks" / check_id / "primary.log"
    return log, Path(str(log) + ".path_proof.txt")


def receipt_ok(log, check_id):
    expected_log, proof = receipt_paths(check_id)
    if log.resolve() != expected_log.resolve():
        return False, "primary-log path mismatch"
    ok, detail = proof_ok(log)
    if not ok:
        return False, detail
    try:
        header_line = log.read_text(encoding="utf-8").splitlines()[0]
        header = json.loads(header_line)
    except (OSError, UnicodeError, IndexError, json.JSONDecodeError):
        return False, "primary-log header unreadable or malformed"
    proof_relative = proof.relative_to(ROOT).as_posix()
    if proof_relative not in header.get("evidence_artifacts", []):
        return False, "primary-log header does not bind sibling receipt proof"
    return True, ""


def _record_and_validate(result, additional_files=()):
    log, manifest = record_check(CFG, result, additional_files=additional_files)
    _refresh_path_proof(log, default_produced_at=now(), check=False)
    ok, detail = receipt_ok(log, result.check_id)
    if not ok:
        raise RuntimeError(detail)
    verify_manifest_entry(CFG, result.check_id)
    return log, manifest


def publish(result, additional_files=(), extra_payload=None):
    log, proof = receipt_paths(result.check_id)
    manifest = QA / "qa_step_logs_manifest.json"
    proof_valid = False
    proof_detail = ""
    try:
        log, manifest = _record_and_validate(result, additional_files)
        proof_valid = True
    except Exception as exc:
        proof_detail = "primary-log receipt-proof publication or validation failed: " + type(exc).__name__
        if result.status is not Status.FAIL_TOOLING:
            result = base_result(
                result.check_id,
                Status.FAIL_TOOLING,
                proof_detail,
                result.command,
                result.output,
                result.evidence_artifacts,
            )
            try:
                log, manifest = _record_and_validate(result, additional_files)
                proof_valid = True
            except Exception as retry_exc:
                proof_detail += "; FAIL_TOOLING receipt publication failed: " + type(retry_exc).__name__
    payload = {
        "check_id": result.check_id,
        "status": result.status.value,
        "primary_log": log.relative_to(ROOT).as_posix(),
        "primary_log_proof": proof.relative_to(ROOT).as_posix(),
        "primary_log_proof_valid": proof_valid,
        "primary_log_proof_detail": proof_detail,
        "manifest": manifest.relative_to(ROOT).as_posix(),
    }
    if extra_payload:
        payload.update(extra_payload)
    print(
        json.dumps(payload, sort_keys=True)
    )
    return 0 if result.status is Status.PASS and proof_valid else 1


def base_result(check_id, status, reason, command, output, artifacts=()):
    _, proof = receipt_paths(check_id)
    proof_relative = proof.relative_to(ROOT).as_posix()
    bound_artifacts = tuple(dict.fromkeys((*artifacts, proof_relative)))
    return CheckResult(
        check_id=check_id,
        status=status,
        status_reason=reason,
        check_name=NAMES[check_id],
        command=command,
        command_provenance=(
            "QA-created helper invocation plus exact child argv from the approved Live QA Plan "
            "and the Product Owner-authorized " + MOON_LOOP_REVISION + " runner correction"
        ),
        exit_code=0 if status is Status.PASS else 1,
        output=output,
        evidence_artifacts=bound_artifacts,
        intended_tokens=(),
        pf_refs=REFS,
    )


def step0b():
    check_id = "step-0b-doc-delta-capture"
    runtime_install = (
        sys.executable,
        "-m",
        "pip",
        "install",
        "-r",
        "requirements.txt",
    )
    runtime_installed = subprocess.run(
        runtime_install, cwd=ROOT, capture_output=True, text=True, check=False
    )
    install = (
        sys.executable,
        "-m",
        "pip",
        "install",
        "-r",
        "requirements-dev.txt",
    )
    installed = subprocess.run(
        install, cwd=ROOT, capture_output=True, text=True, check=False
    )
    ready = (
        sys.executable,
        "-m",
        "pytest",
        "--version",
    )
    completed = subprocess.run(ready, cwd=ROOT, capture_output=True, text=True, check=False)
    schema_ready = (
        sys.executable,
        "-B",
        "-c",
        'import jsonschema; print("jsonschema import OK")',
    )
    schema_completed = subprocess.run(
        schema_ready, cwd=ROOT, capture_output=True, text=True, check=False
    )
    runtime_ready = (
        sys.executable,
        "-B",
        "-c",
        'import flask,gunicorn,psycopg; print("runtime requirements import OK")',
    )
    runtime_completed = subprocess.run(
        runtime_ready, cwd=ROOT, capture_output=True, text=True, check=False
    )
    required = tuple(
        ROOT / value
        for value in (
            "requirements-dev.txt",
            "requirements.txt",
            "tools/qa/qa_harness.py",
            "tools/qa/generate_epic_close_pack.py",
            "tools/evidence/update_evidence_index.py",
            SCRIPT,
            "audit/docdeltas/hde-epic039_doc_deltas.md",
            "audit/docdeltas/hde-epic039_doc_deltas.md.path_proof.txt",
            "audit/qa/hde-epic039/00_meta/doc_deltas.md",
            "audit/qa/hde-epic039/00_meta/doc_deltas.md.path_proof.txt",
        )
    )
    missing = [path.relative_to(ROOT).as_posix() for path in required if not path.is_file()]
    canonical = ROOT / "audit/docdeltas/hde-epic039_doc_deltas.md"
    qa_copy = ROOT / "audit/qa/hde-epic039/00_meta/doc_deltas.md"
    status = Status.PASS
    reason = ""
    provenance = {}
    try:
        provenance, _, _, _ = source_snapshot()
    except Exception as exc:
        status, reason = Status.TOOLING_BLOCKED, "execution-source provenance unavailable: " + type(exc).__name__
    if env_issue():
        status, reason = Status.TOOLING_BLOCKED, env_issue()
    elif runtime_installed.returncode:
        status, reason = Status.TOOLING_BLOCKED, "requirements dependency synchronization failed"
    elif installed.returncode:
        status, reason = Status.TOOLING_BLOCKED, "requirements-dev dependency synchronization failed"
    elif completed.returncode:
        status, reason = Status.TOOLING_BLOCKED, "pytest dependency readiness failed"
    elif schema_completed.returncode:
        status, reason = Status.TOOLING_BLOCKED, "jsonschema dependency readiness failed"
    elif runtime_completed.returncode:
        status, reason = Status.TOOLING_BLOCKED, "runtime dependency readiness failed"
    elif missing:
        status, reason = Status.TOOLING_BLOCKED, "required pre-existing locus missing: " + missing[0]
    elif not provenance.get("required_current_code_posture_valid", False):
        status, reason = Status.TOOLING_BLOCKED, "required current repository code posture could not be validated"
    else:
        for path in (canonical, qa_copy):
            ok, detail = proof_ok(path)
            if not ok:
                status, reason = Status.FAIL_TOOLING, path.relative_to(ROOT).as_posix() + ": " + detail
                break
        if status is Status.PASS and canonical.read_bytes() != qa_copy.read_bytes():
            status, reason = Status.FAIL_BEHAVIOR, "doc-delta pair is not byte-identical"
    same = bool(
        canonical.is_file()
        and qa_copy.is_file()
        and canonical.read_bytes() == qa_copy.read_bytes()
    )
    discovery = {
        "schema_version": "hde_epic039.qa_discovery.v2",
        "epic_id": EPIC,
        "captured_at_utc": now(),
        "environment": {key: os.environ.get(key) for key in ENV},
        "runtime_dependency_sync_command": list(runtime_install),
        "runtime_dependency_sync_exit_code": runtime_installed.returncode,
        "dependency_sync_command": list(install),
        "dependency_sync_exit_code": installed.returncode,
        "dependency_readiness_exit_code": completed.returncode,
        "dependency_readiness_output": (completed.stdout + completed.stderr).strip(),
        "jsonschema_readiness_command": list(schema_ready),
        "jsonschema_readiness_exit_code": schema_completed.returncode,
        "jsonschema_readiness_output": (schema_completed.stdout + schema_completed.stderr).strip(),
        "runtime_readiness_command": list(runtime_ready),
        "runtime_readiness_exit_code": runtime_completed.returncode,
        "runtime_readiness_output": (runtime_completed.stdout + runtime_completed.stderr).strip(),
        "doc_delta_pair_byte_identical": same,
        "execution_source": provenance,
        "moon_loop_revision": moon_loop_record(),
        "required_loci": {
            path.relative_to(ROOT).as_posix(): (
                {"sha256": sha(path), "size_bytes": path.stat().st_size}
                if path.is_file()
                else {"status": "MISSING"}
            )
            for path in required
        },
        "status": status.value,
        "status_reason": reason,
        "venue_specific_claim": "NOT CLAIMED",
    }
    text = json.dumps(discovery, sort_keys=True, separators=(",", ":")) + "\n"
    discovery_path = QA / "00_meta/discovery.json"
    artifacts = (
        discovery_path.relative_to(ROOT).as_posix(),
        canonical.relative_to(ROOT).as_posix(),
        Path(str(canonical) + ".path_proof.txt").relative_to(ROOT).as_posix(),
        qa_copy.relative_to(ROOT).as_posix(),
        Path(str(qa_copy) + ".path_proof.txt").relative_to(ROOT).as_posix(),
    )
    result = base_result(
        check_id,
        status,
        reason,
        (
            self_cmd(check_id),
            runtime_install,
            install,
            ready,
            schema_ready,
            runtime_ready,
            *SOURCE_COMMANDS,
        ),
        text,
        artifacts,
    )
    return publish(
        result,
        additional_files=((discovery_path, text),),
        extra_payload={"discovery": discovery_path.relative_to(ROOT).as_posix()},
    )


def probe10():
    retired = (
        "tools/evidence/generate_hde_epic038_closeout.py",
        "tools/evidence/check_hde_epic038_qa_current_state.py",
        "tests/evidence/test_hde_epic038_closeout.py",
        "tests/evidence/test_hde_epic038_qa_current_state.py",
        "tests/evidence/test_hde_epic038_release_sanity.py",
    )
    present = [value for value in retired if (ROOT / value).exists()]
    tokens = tuple(Path(value).name.encode() for value in retired)
    hits = []
    for root_name in ("tools", "tests", "ci", ".github", "engine"):
        for path in (ROOT / root_name).rglob("*"):
            if not path.is_file() or path.is_symlink():
                continue
            try:
                data = path.read_bytes()
            except OSError:
                continue
            if any(token in data for token in tokens):
                hits.append(path.relative_to(ROOT).as_posix())
    generic = (
        "tools/qa/qa_harness.py",
        ".github/workflows/ci.yml",
        "tools/qa/generate_epic_close_pack.py",
        "audit/qa/hde-epic038",
    )
    missing = [value for value in generic if not (ROOT / value).exists()]
    output = json.dumps(
        {
            "retired_paths_present": present,
            "operative_text_hits": sorted(hits),
            "missing_preserved_or_generic_loci": missing,
        },
        sort_keys=True,
    )
    if present or hits:
        return Status.FAIL_BEHAVIOR, "retired epic-specific automation remains active in operative loci", output
    if missing:
        return Status.TOOLING_BLOCKED, "historical or generic safeguard locus unavailable", output
    return Status.PASS, "", output


def _strict_json(payload):
    def pairs(items):
        result = {}
        for key, value in items:
            if key in result:
                raise ValueError("duplicate key")
            result[key] = value
        return result

    return json.loads(payload.decode("utf-8"), object_pairs_hook=pairs)


def probe13():
    generic = (
        "tools/qa/generate_epic_close_pack.py",
        "schemas/epic_close_candidate_source.v1.json",
        ".github/workflows/epic-closeout-validation.yml",
        "tests/qa/test_generate_epic_close_pack.py",
    )
    missing = [value for value in generic if not (ROOT / value).is_file()]
    outputs = ("audit/EPIC-039_close_report.md", "audit/EPIC-039_MANIFEST.json")
    present = [value for value in outputs if (ROOT / value).exists()]
    accepted_sources = []
    marker_sources = []
    rejected_markers = {}
    scanned = 0
    domain = "all regular files in the current tracked HEAD tree accepted by the generator's repository-relative source interface"
    config_compat = {}
    try:
        context = _establish_git_context(ROOT)
        with codespaces_git_config_compat(context) as config_compat:
            store = _GitObjectStore(context)
            head = _head(context, store)
            tree = _tree_entries(context, store)
            for relative, entry in sorted(tree.items()):
                if entry.mode not in REGULAR_GIT_MODES:
                    continue
                scanned += 1
                payload = _git_blob_payload(context, entry.object_id, store)
                try:
                    value = _strict_json(payload)
                except (UnicodeError, json.JSONDecodeError, ValueError):
                    continue
                if not (
                    isinstance(value, dict)
                    and value.get("epic_id") == EPIC
                    and value.get("schema_version") == "epic_close_candidate_source.v1"
                ):
                    continue
                marker_sources.append(relative)
                try:
                    _load_model(ROOT, context, head, relative)
                except Exception as exc:
                    rejected_markers[relative] = type(exc).__name__
                else:
                    accepted_sources.append(relative)
    except Exception as exc:
        output = json.dumps(
            {
                "candidate_source_domain": domain,
                "candidate_source_domain_error": type(exc).__name__,
                "codespaces_git_config_compat": config_compat,
                "missing_reusable_capability_loci": missing,
                "real_candidate_outputs_present": present,
                "real_candidate_sources_present": [],
            },
            sort_keys=True,
        )
        return Status.FAIL_TOOLING, "complete candidate-source-domain scan failed", output
    output = json.dumps(
        {
            "candidate_source_domain": domain,
            "codespaces_git_config_compat": config_compat,
            "tracked_regular_files_examined": scanned,
            "candidate_marker_sources_present": marker_sources,
            "candidate_marker_sources_rejected_by_generator": rejected_markers,
            "missing_reusable_capability_loci": missing,
            "real_candidate_outputs_present": present,
            "real_candidate_sources_present": accepted_sources,
        },
        sort_keys=True,
    )
    if missing:
        return Status.TOOLING_BLOCKED, "reusable closeout capability locus unavailable", output
    if present or accepted_sources:
        return Status.TOOLING_BLOCKED, "real HDE-EPIC039 candidate state exists; reusable-capability-only scope requires a fresh plan decision", output
    return Status.PASS, "", output


def run(check_id, args):
    if check_id not in NAMES or check_id == "step-0b-doc-delta-capture":
        print("UNKNOWN_OR_EMPTY_CHECK:" + check_id, file=sys.stderr)
        return 2
    if not args:
        print("UNKNOWN_OR_EMPTY_CHECK:" + check_id, file=sys.stderr)
        return 2
    outer = self_cmd(check_id, args)
    if env_issue():
        return publish(base_result(check_id, Status.TOOLING_BLOCKED, env_issue(), (outer,), ""))
    raw = run_pytest_check(CFG, check_id, args, check_name=NAMES[check_id], intended_tokens=())
    children = raw.command if raw.command and isinstance(raw.command[0], tuple) else ((raw.command,) if raw.command else ())
    output = raw.output.rstrip("\n")
    status = raw.status
    reason = raw.status_reason
    if status is Status.PASS and check_id in EXTRA_IDS:
        command = (sys.executable, "-B", "tools/evidence/update_evidence_index.py", "--check")
        completed = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, check=False)
        children = (*children, command)
        detail = completed.stdout + completed.stderr
        output += "\nEXTRA_COMMAND " + json.dumps(list(command), separators=(",", ":"))
        output += "\nEXTRA_EXIT_CODE " + str(completed.returncode)
        if detail:
            output += "\n" + detail.rstrip("\n")
        if completed.returncode:
            if any(value in detail for value in ("ModuleNotFoundError", "ImportError", "Traceback")):
                status, reason = Status.FAIL_TOOLING, "evidence check mechanism failed"
            else:
                status, reason = Status.FAIL_BEHAVIOR, "current evidence publication check contradicted the required state"
    if status is Status.PASS and check_id in {"po-010", "po-013"}:
        status, reason, probe_output = probe10() if check_id == "po-010" else probe13()
        output += "\nPROBE " + probe_output
    result = base_result(check_id, status, reason, (outer, *children), output)
    return publish(result)


def _load_manifest_strict(path):
    if not path.is_file():
        return {}, "manifest missing"
    try:
        value = _strict_json(path.read_bytes())
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as exc:
        return {}, "manifest unreadable or malformed: " + type(exc).__name__
    if not isinstance(value, dict):
        return {}, "manifest is not a flat object"
    return value, ""


def finalize():
    manifest_path = QA / "qa_step_logs_manifest.json"
    discovery_path = QA / "00_meta/discovery.json"
    summary_path = QA / "00_meta/qa_rca_doc_delta_summary.md"
    manifest, manifest_error = _load_manifest_strict(manifest_path)
    discovery, discovery_error = _load_manifest_strict(discovery_path)
    if discovery_error:
        discovery_error = discovery_error.replace("manifest", "discovery")
    rows = []
    blockers = []
    behavior_failures = []
    expected_moon_loop = moon_loop_record()
    if discovery_error:
        blockers.append("Moon Loop discovery: " + discovery_error)
    else:
        discovery_checks = {
            "schema/epic identity": (
                discovery.get("schema_version") == "hde_epic039.qa_discovery.v2"
                and discovery.get("epic_id") == EPIC
            ),
            "Step-0B status": discovery.get("status") == "PASS",
            "protected Doc Delta pair": discovery.get("doc_delta_pair_byte_identical") is True,
            "closed-rails environment": discovery.get("environment") == ENV,
            "dependency synchronization": discovery.get("dependency_sync_exit_code") == 0,
            "runtime dependency synchronization": discovery.get("runtime_dependency_sync_exit_code") == 0,
            "pytest readiness": discovery.get("dependency_readiness_exit_code") == 0,
            "jsonschema readiness": discovery.get("jsonschema_readiness_exit_code") == 0,
            "runtime dependency readiness": discovery.get("runtime_readiness_exit_code") == 0,
            "Moon Loop identity": discovery.get("moon_loop_revision") == expected_moon_loop,
            "current helper hash": (
                discovery.get("required_loci", {})
                .get(SCRIPT, {})
                .get("sha256")
                == expected_moon_loop["revised_helper_sha256"]
            ),
            "current code posture": (
                discovery.get("execution_source", {})
                .get("required_current_code_posture_valid")
                is True
            ),
            "Codespaces config compatibility": (
                discovery.get("execution_source", {})
                .get("codespaces_git_config_compat", {})
                .get("applied")
                is True
                and discovery.get("execution_source", {})
                .get("codespaces_git_config_compat", {})
                .get("source_config_modified")
                is False
                and discovery.get("execution_source", {})
                .get("codespaces_git_config_compat", {})
                .get("waived_line_count", 0)
                > 0
                and re.fullmatch(
                    r"[0-9a-f]{64}",
                    discovery.get("execution_source", {})
                    .get("codespaces_git_config_compat", {})
                    .get("config_sha256", ""),
                )
                is not None
            ),
        }
        blockers.extend(
            "Moon Loop discovery mismatch: " + name
            for name, valid in discovery_checks.items()
            if not valid
        )
    for check_id in ORDER:
        raw_entry = manifest.get(check_id)
        if manifest_error:
            status = "UNTRUSTED"
            evidence = "UNTRUSTED"
            coverage = "BLOCKED/UNEXECUTABLE"
            blockers.append(check_id + ": " + manifest_error)
        elif raw_entry is None:
            status = "NOT RUN"
            evidence = "NOT RUN"
            coverage = "NOT RUN"
            blockers.append(check_id + ": NOT RUN")
        else:
            try:
                entry = verify_manifest_entry(CFG, check_id)
            except Exception as exc:
                status = "UNTRUSTED"
                evidence = "UNTRUSTED"
                coverage = "BLOCKED/UNEXECUTABLE"
                blockers.append(check_id + ": manifest-entry validation failed: " + type(exc).__name__)
            else:
                status = entry["status"]
                evidence = entry["log_path"]
                receipt_valid, receipt_detail = receipt_ok(ROOT / evidence, check_id)
                if not receipt_valid:
                    status = "UNTRUSTED"
                    evidence = "UNTRUSTED"
                    coverage = "BLOCKED/UNEXECUTABLE"
                    blockers.append(check_id + ": primary-log receipt-proof validation failed: " + receipt_detail)
                else:
                    coverage = "COVERED" if status == "PASS" else "BLOCKED/UNEXECUTABLE"
                    if status == "FAIL_BEHAVIOR":
                        behavior_failures.append(check_id)
                    if status != "PASS":
                        blockers.append(check_id + ": " + status)
        rows.append("| " + check_id + " | " + NAMES[check_id] + " | " + coverage + " | " + status + " | " + evidence + " |")
    extras = sorted(set(manifest) - set(ORDER))
    blockers.extend("unplanned manifest entry: " + value for value in extras)
    complete = (
        not blockers
        and not manifest_error
        and not discovery_error
        and set(manifest) == set(ORDER)
    )
    recommendation = "READY FOR PRODUCT OWNER QA CLOSEOUT REVIEW" if complete else "NOT READY"
    if behavior_failures:
        behavior_finding = "Live QA found a product-behavior contradiction; see: " + ", ".join(behavior_failures) + "."
    elif complete:
        behavior_finding = "No new product-behavior delta was found."
    else:
        behavior_finding = "No product-behavior conclusion is claimed for checks that were not behavior-decisive or not run."
    planning_finding = " A QA planning/execution-surface defect was found and remediated under the authorized Moon Loop revision."
    findings = behavior_finding + planning_finding
    if not complete:
        findings += " Unresolved execution states: " + "; ".join(blockers)
    text = "\n".join(
        (
            "# HDE-EPIC039 QA RCA and Doc Delta Summary",
            "",
            "## Live QA findings and RCA",
            "",
            findings,
            "",
            "The existing proof-bearing doc-delta pair was preserved; Live QA did not overwrite either surface.",
            "",
            "## Moon Loop revision and planning defect",
            "",
            "- Authority: " + MOON_LOOP_AUTHORITY + ".",
            "- Authorization (verbatim): “" + MOON_LOOP_AUTHORIZATION + "”.",
            "- Extended authorization (verbatim): “" + EXTENDED_MOON_LOOP_AUTHORIZATION + "”.",
            "- Revision: " + MOON_LOOP_REVISION + ".",
            "- Initial attempt: the exact r4 direct-path command failed before helper main() with `ModuleNotFoundError: No module named 'tools'`; no governed receipt was created.",
            "- Operator-observed first `po-001` attempt: pytest collection failed before any product assertion with `ModuleNotFoundError: No module named 'flask'`, exposing the omitted runtime-requirements readiness check; the Moon Loop replaced that current-state receipt after correcting readiness, so the prior receipt is not independently retained.",
            "- Operator-observed first `po-003` attempt: 116 assertions passed and one legacy composer assertion expected `harmony.cool.shared...` while the current governed grammar, catalog, router, and sibling tests require `nar.harmony.cool.shared...`; the test also mounted an untracked repo-root cache because it lacked temporary-path isolation. The Moon Loop replaced that current-state receipt, so the prior receipt is not independently retained.",
            "- First all-PASS finalizer attempt: every check receipt was PASS, but the Moon Loop finalizer incorrectly treated mutable Codespaces branch metadata as event-wide identity and returned NOT READY. The correction preserves strict within-operation config stability while allowing venue metadata to change between operations.",
            "- Extended corrective scope: repository-root import bootstrap; an in-memory waiver for only exact Codespaces `branch.main.github-pr-owner-number` metadata; complete runtime/development readiness; and test-only correction of the stale composer key expectation plus temporary-pack isolation.",
            "- Source protection: no product runtime source, governed source, `.git/config`, selector path, rails variable, or evidence path was changed. The only tracked Moon Loop change was the selected narrative-composer test.",
            "- Dependency-network note: pip package-index access occurred during runtime and development synchronization before QA behavior checks; this setup I/O is not product or Live QA evidence.",
            "- Planning defect: " + PLANNING_DEFECT,
            "- Future process correction: " + FUTURE_PROCESS_CORRECTION,
            "- Original helper SHA-256: `" + ORIGINAL_HELPER_SHA256 + "`.",
            "- Revised helper SHA-256: `" + sha(ROOT / SCRIPT) + "`.",
            "- Corrected selected-test SHA-256: `" + expected_moon_loop["tracked_test_correction"]["sha256"] + "` (`tests/unit/test_narratives_composer.py`).",
            "",
            "## PF-Canon doc-delta intents",
            "",
            "- PF14 - HDE Mechanics Guide: later PO-owned drainage for orientation and evidence-index publication ownership identified by current PF10.",
            "- PF04 - HDE Governance: later PO-owned drainage for Machine Mirror self-reference semantics identified by current PF10.",
            "- PF09.1 - HDE Build Checklist - Calcination: status drainage remains a separate Product Owner closeout action; this QA run makes no PF09 status change.",
            "- Documentation drainage is not a blocker for step verdicts or this recommendation when required QA evidence is complete and trustworthy.",
            "",
            "## Deferrals and nonclaims",
            "",
            "- No open-rails product, vendor, deployment, production, public Reader, database, or service behavior was exercised. Moon Loop dependency setup performed the package-index activity recorded above.",
            "- No real HDE-EPIC039 closeout candidate, operational validation, acceptance, closure, deployment, or checklist status change is claimed.",
            "- Acceptance tokens were neither intended nor claimed.",
            "- Codespaces venue is NOT CLAIMED as a proof axis.",
            "",
            "## Coverage vs QA Plan",
            "",
            "| check_id | check name | coverage status | execution status | evidence |",
            "| --- | --- | --- | --- | --- |",
            *rows,
            "",
            "## Dependency and Moon Loop posture",
            "",
            "Product Owner-authorized Moon Loop work was recorded. Runtime synchronization was `python -m pip install -r requirements.txt` (exit " + str(discovery.get("runtime_dependency_sync_exit_code", "UNAVAILABLE")) + "), development synchronization was `python -m pip install -r requirements-dev.txt` (exit " + str(discovery.get("dependency_sync_exit_code", "UNAVAILABLE")) + "), pytest readiness was `python -m pytest --version` (exit " + str(discovery.get("dependency_readiness_exit_code", "UNAVAILABLE")) + "), the jsonschema probe exited " + str(discovery.get("jsonschema_readiness_exit_code", "UNAVAILABLE")) + ", and the runtime-import probe exited " + str(discovery.get("runtime_readiness_exit_code", "UNAVAILABLE")) + ".",
            "",
            "## Open issues and deferred work",
            "",
            "No unresolved QA-ladder behavior issue. The planning-process correction above remains follow-up work and is not a product-behavior blocker." if complete else "Resolve every BLOCKED/UNEXECUTABLE or NOT RUN row before closeout; retain the planning-process correction above as a separate follow-up.",
            "",
            "Undrained documentation deltas remain PO-owned follow-up and are not converted into QA blockers.",
            "",
            "## Completion-state separation",
            "",
            "- Repo-supported completion: " + ("SUPPORTED BY THIS QA EVENT STREAM" if complete else "NOT SUPPORTED"),
            "- Canon-drain completion: NOT CLAIMED",
            "- Formal close-pack completion: NOT CLAIMED",
            "",
            "## Readiness / closeout recommendation",
            "",
            recommendation,
            "",
            "Evidence pointers: audit/qa/hde-epic039/qa_step_logs_manifest.json; audit/qa/hde-epic039/qa_step_logs_manifest.json.path_proof.txt; audit/qa/hde-epic039/00_meta/discovery.json; audit/docdeltas/hde-epic039_doc_deltas.md; audit/qa/hde-epic039/00_meta/doc_deltas.md.",
            "",
        )
    )
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    summary_path.write_text(text, encoding="utf-8", newline="\n")
    stamp = now()
    _refresh_path_proof(summary_path, default_produced_at=stamp, check=False)
    if manifest_path.is_file():
        _refresh_path_proof(manifest_path, default_produced_at=stamp, check=False)
    summary_ok, summary_detail = proof_ok(summary_path)
    manifest_ok, manifest_detail = proof_ok(manifest_path)
    print(
        json.dumps(
            {
                "recommendation": recommendation,
                "summary": summary_path.relative_to(ROOT).as_posix(),
                "summary_proof_valid": summary_ok,
                "manifest_proof_valid": manifest_ok,
                "summary_proof_detail": summary_detail,
                "manifest_proof_detail": manifest_detail,
            },
            sort_keys=True,
        )
    )
    return 0 if complete and summary_ok and manifest_ok else 1


def main():
    if len(sys.argv) < 2:
        print("USAGE: qa_runner.py <check-id|finalize>", file=sys.stderr)
        return 2
    check_id = sys.argv[1]
    if check_id == "finalize":
        if len(sys.argv) != 2:
            print("FINALIZE_ARGUMENTS_NOT_ALLOWED", file=sys.stderr)
            return 2
        return finalize()
    tail = tuple(sys.argv[2:])
    if check_id == "step-0b-doc-delta-capture":
        if tail:
            print("STEP0B_ARGUMENTS_NOT_ALLOWED", file=sys.stderr)
            return 2
        return step0b()
    return run(check_id, tail)


if __name__ == "__main__":
    raise SystemExit(main())
