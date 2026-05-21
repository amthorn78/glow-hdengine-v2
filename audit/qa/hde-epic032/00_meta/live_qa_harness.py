#!/usr/bin/env python3
import datetime
import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from datetime import timezone

EPIC = "hde-epic032"
ROOT = Path("audit/qa/hde-epic032")
META = ROOT / "00_meta"
CHECKS_ROOT = ROOT / "checks"
MANIFEST = ROOT / "qa_step_logs_manifest.json"
MANIFEST_PROOF = ROOT / "qa_step_logs_manifest.json.path_proof.txt"
DOC_DELTA_DRAFT = Path("audit/docdeltas/hde-epic032_doc_deltas.md")
DOC_DELTA_CAPTURE = META / "doc_deltas.md"

PF_REFS = [
	"PF10 - HDE-Build Notes",
	"PF19 - Glow QA Guide",
	"PF27 - Canon Plan Templates",
]

ENV_KEYS = ["SAFE_MODE", "ALLOW_NETWORK", "APP_ENV", "LC_ALL", "LANG", "TZ"]

PATHS = {
	"router_key_table": "audit/gates/narratives/keys_10x4.table.json",
	"registry_diff": "audit/gates/narratives/registry.diff.json",
	"pack_identity": "audit/gates/narratives/pack_identity.txt",
	"router_parity_abba": "artifacts/narratives/router/parity_abba.log",
	"router_cli_http_parity": "artifacts/narratives/router/cli_http_parity.log",
	"db_provider_parity": "artifacts/db_bridge/provider_parity.proof.json",
	"db_adapter_selection": "artifacts/db_bridge/adapter_selection.snapshot.json",
	"env_nondev_failure": "artifacts/runtime/env_connectivity.nondev_failure.json",
	"env_connectivity": "artifacts/runtime/env_connectivity.snapshot.json",
	"ops_provider_closure": "audit/ops/hde-epic032/db-provider-parity/provider_parity_closure_decision.json",
	"ops_provider_closure_proof": "audit/ops/hde-epic032/db-provider-parity/provider_parity_closure_decision.json.path_proof.txt",
	"human_index": "docs/evidence/INDEX.json",
	"human_index_hash": "docs/evidence/INDEX.sha256",
	"machine_mirror": "artifacts/evidence_index.jsonl",
	"machine_mirror_hash": "artifacts/evidence_index.jsonl.sha256",
	"endpoint_catalog": "docs/ENDPOINTS_CATALOG.json",
	"http_reader": "adapter/http_reader.py",
	"cli_main": "engine/cli/main.py",
	"registry_generator": "tools/evidence/generate_narrative_registry_diff.py",
	"db_generator": "tools/evidence/generate_db_bridge_parity.py",
	"index_updater": "tools/evidence/update_evidence_index.py",
	"path_validator": "tools/evidence/validate_evidence_paths.py",
	"lf_checker": "tools/evidence/check_lf_endings.py",
	"mirror_schema": "ci/checks/check_mirror_schema.sh",
	"index_hash": "ci/checks/check_evidence_index_hash.sh",
	"test_router": "tests/unit/test_narratives_router.py",
	"test_db_adapter": "tests/db/test_adapter_selection.py",
	"test_db_nondev": "tests/evidence/test_generate_db_bridge_parity_nondev.py",
	"test_cli_aux": "tests/cli/test_aux_preview.py",
	"test_transport_aux": "tests/transport/test_aux_narrative.py",
	"pyproject": "pyproject.toml",
	"readme": "README.md",
	"changelog": "CHANGELOG.md",
	"agents": "AGENTS.md",
	"docs_index": "docs/INDEX.md",
	"narrative_manifest": "catalog/narratives/manifest.json",
}

CHECK_NAMES = {
	"step-0a-discovery": "Step-0A Discovery posture and Live QA harness setup",
	"step-0b-doc-delta": "Step-0B Doc Delta Capture",
	"po-001": "PO-001",
	"po-002": "PO-002",
	"po-003": "PO-003",
	"po-004": "PO-004",
	"po-005": "PO-005",
	"po-006": "PO-006",
	"po-007": "PO-007",
	"po-008": "PO-008",
	"po-009": "PO-009",
	"po-010": "PO-010",
	"po-011": "PO-011",
	"po-012": "PO-012",
	"po-013": "PO-013",
	"po-014": "PO-014",
	"po-015": "PO-015",
	"po-016": "PO-016",
	"po-017": "PO-017",
	"po-018": "PO-018",
	"po-019": "PO-019",
	"po-020": "PO-020",
	"po-021": "PO-021",
	"po-022": "PO-022",
	"po-023": "PO-023",
	"po-024": "PO-024",
}


def utc_now():
	return datetime.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"


def mtime_utc(p):
	value = datetime.datetime.fromtimestamp(p.stat().st_mtime, tz=timezone.utc).replace(microsecond=0)
	return value.strftime("%Y-%m-%dT%H:%M:%SZ")


def env(name, default=""):
	value = os.environ.get(name)
	return value if value is not None else default


def path(key):
	return Path(PATHS[key])


def exists(key):
	return path(key).exists()


def text(key):
	p = path(key)
	return p.read_text(encoding="utf-8", errors="replace") if p.exists() else ""


def sha256_file(p):
	h = hashlib.sha256()
	with p.open("rb") as handle:
		for chunk in iter(lambda: handle.read(65536), b""):
			h.update(chunk)
	return h.hexdigest()


def write_path_proof(artifact_path, produced_at=None):
	artifact_path = Path(artifact_path)
	produced_at = produced_at or utc_now()
	proof_path = Path(str(artifact_path) + ".path_proof.txt")
	proof_path.parent.mkdir(parents=True, exist_ok=True)
	body = (
		f"path: {artifact_path}\n"
		f"sha256: {sha256_file(artifact_path)}\n"
		f"size_bytes: {artifact_path.stat().st_size}\n"
		f"mtime_utc: {mtime_utc(artifact_path)}\n"
		f"produced_at_utc: {produced_at}\n"
	)
	proof_path.write_text(body, encoding="utf-8")
	return proof_path


def canonical_json_bytes(value):
	return (json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n").encode("utf-8")


def run_cmd(cmd):
	try:
		proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, env=os.environ.copy())
		return {"cmd": cmd, "returncode": proc.returncode, "stdout": proc.stdout, "stderr": proc.stderr}
	except Exception as exc:
		return {"cmd": cmd, "returncode": 127, "stdout": "", "stderr": f"{type(exc).__name__}: {exc}"}


def check_pytest_available():
	return run_cmd([sys.executable, "-c", "import pytest; print('pytest import PASS')"])


def missing(keys):
	return [PATHS[k] for k in keys if not exists(k)]


def has_all_strings(blob, values):
	return all(v in blob for v in values)


def status_from(blockers, tooling_failures, behavior_failures):
	if blockers:
		return "TOOLING_BLOCKED"
	if tooling_failures:
		return "FAIL_TOOLING"
	if behavior_failures:
		return "FAIL_BEHAVIOR"
	return "PASS"


def result_base(check_id):
	return {
		"schema": f"hde_epic032.{check_id.replace('-', '_')}.v1",
		"check_id": check_id,
		"checked_at_utc": utc_now(),
		"rails": {k: env(k) for k in ENV_KEYS},
	}


def evaluate_step0a():
	ROOT.mkdir(parents=True, exist_ok=True)
	META.mkdir(parents=True, exist_ok=True)
	CHECKS_ROOT.mkdir(parents=True, exist_ok=True)
	repo_paths = {k: {"path": v, "exists": Path(v).exists()} for k, v in PATHS.items()}
	r = result_base("step-0a-discovery")
	r.update(
		{
			"epic_qa_root": str(ROOT),
			"meta_root": str(META),
			"checks_root": str(CHECKS_ROOT),
			"qa_root_created": ROOT.exists(),
			"repo_locus_discovery": repo_paths,
			"status": "PASS",
		}
	)
	return r


def evaluate_step0b():
	DOC_DELTA_DRAFT.parent.mkdir(parents=True, exist_ok=True)
	META.mkdir(parents=True, exist_ok=True)
	body = "\n".join(
		[
			"# HDE-EPIC032 Doc Deltas",
			"",
			"## BLOCKERS",
			"",
			"No deltas recorded before Live QA execution.",
			"",
			"## CAVEATS",
			"",
			"No deltas recorded before Live QA execution.",
			"",
		]
	)
	DOC_DELTA_DRAFT.write_text(body, encoding="utf-8")
	DOC_DELTA_CAPTURE.write_text(body, encoding="utf-8")
	r = result_base("step-0b-doc-delta")
	r.update(
		{
			"draft_path": str(DOC_DELTA_DRAFT),
			"capture_path": str(DOC_DELTA_CAPTURE),
			"draft_exists": DOC_DELTA_DRAFT.exists(),
			"capture_exists": DOC_DELTA_CAPTURE.exists(),
			"blockers_heading_present": "## BLOCKERS" in body,
			"caveats_heading_present": "## CAVEATS" in body,
		}
	)
	r["status"] = (
		"PASS"
		if r["draft_exists"] and r["capture_exists"] and r["blockers_heading_present"] and r["caveats_heading_present"]
		else "FAIL_TOOLING"
	)
	return r


def evaluate_po001():
	req = ["endpoint_catalog", "http_reader", "ops_provider_closure", "db_provider_parity"]
	blockers = missing(req)
	endpoint = text("endpoint_catalog")
	ops = text("ops_provider_closure")
	provider = text("db_provider_parity")
	behavior = []
	if not has_all_strings(endpoint, ["/reader", "/dev/reader/conjunction"]):
		behavior.append("endpoint_catalog_missing_reader_or_dev_reader_surface")
	if re.search(r'"qa_pass_claimed"\s*:\s*true', ops):
		behavior.append("ops_evidence_overclaims_qa_pass")
	if any(
		label in provider and re.search(rf'{label}.*"type"\s*:\s*"token"', provider)
		for label in ["DB_PROVIDER_PARITY_OK", "DB_BRIDGE_CAPS_OK", "DB_BRIDGE_FALLBACK_OK"]
	):
		behavior.append("db_proof_label_claimed_as_token")
	r = result_base("po-001")
	r.update(
		{
			"required_missing": blockers,
			"reader_surface_seen": "/reader" in endpoint,
			"dev_reader_surface_seen": "/dev/reader/conjunction" in endpoint,
			"db_proof_labels_checked": True,
			"behavior_failures": behavior,
		}
	)
	r["status"] = status_from(blockers, [], behavior)
	return r


def evaluate_po002():
	req = ["test_router", "router_key_table", "router_parity_abba"]
	blockers = missing(req)
	pytest_check = check_pytest_available()
	tooling = []
	command = None
	if pytest_check["returncode"] != 0:
		blockers.append("pytest import unavailable")
	else:
		command = run_cmd([sys.executable, "-m", "pytest", "-q", PATHS["test_router"]])
		if command["returncode"] != 0:
			tooling.append("router pytest nonzero")
	r = result_base("po-002")
	r.update(
		{
			"pytest_preflight": pytest_check,
			"pytest": command,
			"required_missing": blockers,
			"router_key_table_exists": exists("router_key_table"),
			"router_parity_abba_exists": exists("router_parity_abba"),
		}
	)
	r["status"] = status_from(blockers, tooling, [])
	return r


def evaluate_po003():
	req = ["router_key_table", "router_cli_http_parity", "endpoint_catalog", "http_reader"]
	blockers = missing(req)
	endpoint = text("endpoint_catalog")
	reader = text("http_reader")
	key_table = text("router_key_table")
	behavior = []
	if "/reader" not in endpoint:
		behavior.append("reader_route_not_visible")
	if "APP_ENV" not in reader:
		behavior.append("app_env_gate_not_visible")
	if "prose" in key_table.lower():
		behavior.append("router_key_table_contains_prose_marker")
	r = result_base("po-003")
	r.update(
		{
			"required_missing": blockers,
			"reader_route_visible": "/reader" in endpoint,
			"app_env_gate_visible": "APP_ENV" in reader,
			"keys_only_marker": "prose" not in key_table.lower(),
			"behavior_failures": behavior,
		}
	)
	r["status"] = status_from(blockers, [], behavior)
	return r


def evaluate_po004():
	req = ["test_router", "router_parity_abba"]
	blockers = missing(req)
	pytest_check = check_pytest_available()
	tooling = []
	command = None
	if pytest_check["returncode"] != 0:
		blockers.append("pytest import unavailable")
	else:
		command = run_cmd([sys.executable, "-m", "pytest", "-q", PATHS["test_router"]])
		if command["returncode"] != 0:
			tooling.append("identity pytest nonzero")
	parity = text("router_parity_abba")
	behavior = []
	if not re.search(r"PASS|pass|abba|AB", parity):
		behavior.append("parity_abba_log_lacks_identity_pass_marker")
	r = result_base("po-004")
	r.update(
		{
			"pytest_preflight": pytest_check,
			"pytest": command,
			"required_missing": blockers,
			"parity_log_has_identity_marker": not behavior,
			"behavior_failures": behavior,
		}
	)
	r["status"] = status_from(blockers, tooling, behavior)
	return r


def evaluate_po005():
	req = ["registry_generator", "registry_diff", "pack_identity", "narrative_manifest"]
	blockers = missing(req)
	command = run_cmd([sys.executable, PATHS["registry_generator"], "--check"]) if not blockers else None
	tooling = []
	if command and command["returncode"] != 0:
		tooling.append("registry generator check nonzero")
	reg = text("registry_diff")
	pack = text("pack_identity")
	behavior = []
	if "HDE-EPIC032" not in reg:
		behavior.append("registry_diff_missing_epic_id")
	if "pack" not in pack.lower() and "sha" not in pack.lower():
		behavior.append("pack_identity_lacks_pack_or_sha_marker")
	r = result_base("po-005")
	r.update(
		{
			"generator_check": command,
			"required_missing": blockers,
			"registry_diff_contains_epic": "HDE-EPIC032" in reg,
			"pack_identity_marker_present": not behavior,
			"behavior_failures": behavior,
		}
	)
	r["status"] = status_from(blockers, tooling, behavior)
	return r


def evaluate_po006():
	req = ["human_index", "machine_mirror", "router_key_table"]
	blockers = missing(req)
	index = text("human_index") + "\n" + text("machine_mirror")
	behavior = []
	if "NARR_REGISTRY_CLOSURE_OK" in index and "keys_10x4" in index:
		behavior.append("possible_router_key_table_registry_token_overclaim")
	r = result_base("po-006")
	r.update(
		{
			"required_missing": blockers,
			"unsupported_registry_token_claim_seen": bool(behavior),
			"behavior_failures": behavior,
		}
	)
	r["status"] = status_from(blockers, [], behavior)
	return r


def evaluate_po007():
	req = ["registry_diff", "pack_identity", "human_index", "machine_mirror"]
	blockers = missing(req)
	draft_exists = DOC_DELTA_DRAFT.exists() or Path(PATHS["readme"]).exists()
	behavior = []
	reg = text("registry_diff")
	if "HDE-FERM003.2" not in reg and "HDE-EPIC032" not in reg:
		behavior.append("registry_diff_not_bound_to_epic_or_row")
	r = result_base("po-007")
	r.update(
		{
			"required_missing": blockers,
			"doc_delta_surface_available": draft_exists,
			"registry_diff_bound": not behavior,
			"behavior_failures": behavior,
		}
	)
	r["status"] = status_from(blockers, [], behavior)
	return r


def evaluate_po008():
	req = ["db_generator", "db_provider_parity", "db_adapter_selection", "ops_provider_closure"]
	blockers = missing(req)
	command = run_cmd([sys.executable, PATHS["db_generator"], "--check"]) if not blockers else None
	tooling = []
	if command and command["returncode"] != 0:
		tooling.append("db bridge parity check nonzero")
	provider = text("db_provider_parity")
	ops = text("ops_provider_closure")
	behavior = []
	if "DB_PROVIDER_PARITY_OK" not in provider:
		behavior.append("provider_parity_label_not_visible")
	if "provider_parity_closure_status" not in ops:
		behavior.append("ops_closure_status_not_visible")
	r = result_base("po-008")
	r.update(
		{
			"generator_check": command,
			"required_missing": blockers,
			"provider_parity_label_visible": "DB_PROVIDER_PARITY_OK" in provider,
			"ops_closure_status_visible": "provider_parity_closure_status" in ops,
			"behavior_failures": behavior,
		}
	)
	r["status"] = status_from(blockers, tooling, behavior)
	return r


def evaluate_po009():
	req = ["ops_provider_closure", "ops_provider_closure_proof"]
	blockers = missing(req)
	ops = text("ops_provider_closure")
	behavior = []
	if re.search(r'"qa_pass_claimed"\s*:\s*true', ops):
		behavior.append("ops_evidence_claims_qa_pass")
	if "provider_parity_closure_status" not in ops:
		behavior.append("provider_parity_closure_status_missing")
	r = result_base("po-009")
	r.update(
		{
			"required_missing": blockers,
			"ops_status_visible": "provider_parity_closure_status" in ops,
			"ops_qa_pass_not_claimed": not behavior,
			"behavior_failures": behavior,
		}
	)
	r["status"] = status_from(blockers, [], behavior)
	return r


def evaluate_po010():
	req = ["db_provider_parity", "db_adapter_selection", "ops_provider_closure"]
	blockers = missing(req)
	provider = text("db_provider_parity")
	adapter = text("db_adapter_selection")
	ops = text("ops_provider_closure")
	behavior = []
	if "DB_PROVIDER_PARITY_OK" not in provider:
		behavior.append("provider_parity_proof_missing")
	if "selection_order" not in provider + adapter:
		behavior.append("selection_order_missing")
	if "drain" in ops.lower() and "claimed" in ops.lower() and "false" not in ops.lower():
		behavior.append("possible_checklist_drainage_overclaim")
	r = result_base("po-010")
	r.update(
		{
			"required_missing": blockers,
			"combined_provider_and_adapter_evidence_seen": not behavior,
			"behavior_failures": behavior,
		}
	)
	r["status"] = status_from(blockers, [], behavior)
	return r


def evaluate_po011():
	req = ["test_db_adapter", "test_db_nondev", "env_nondev_failure"]
	blockers = missing(req)
	pytest_check = check_pytest_available()
	tooling = []
	command = None
	if pytest_check["returncode"] != 0:
		blockers.append("pytest import unavailable")
	else:
		command = run_cmd([sys.executable, "-m", "pytest", "-q", PATHS["test_db_adapter"], PATHS["test_db_nondev"]])
		if command["returncode"] != 0:
			tooling.append("db typed failure pytest nonzero")
	nondev = text("env_nondev_failure")
	behavior = []
	for marker in ["numeric_free", "missing_bridge_url", "BridgeUnavailable"]:
		if marker not in nondev:
			behavior.append(f"nondev_failure_missing_{marker}")
	r = result_base("po-011")
	r.update(
		{
			"pytest_preflight": pytest_check,
			"pytest": command,
			"required_missing": blockers,
			"numeric_free_seen": "numeric_free" in nondev,
			"missing_bridge_url_seen": "missing_bridge_url" in nondev,
			"behavior_failures": behavior,
		}
	)
	r["status"] = status_from(blockers, tooling, behavior)
	return r


def evaluate_po012():
	req = ["env_nondev_failure", "db_adapter_selection", "test_db_adapter"]
	blockers = missing(req)
	nondev = text("env_nondev_failure")
	behavior = []
	if "no_proactive_probes" not in nondev:
		behavior.append("no_proactive_probes_missing")
	if "adapter_path_only" not in nondev:
		behavior.append("adapter_path_only_missing")
	if "missing_bridge_url" not in nondev:
		behavior.append("typed_failure_missing")
	r = result_base("po-012")
	r.update(
		{
			"required_missing": blockers,
			"no_proactive_probes_seen": "no_proactive_probes" in nondev,
			"typed_failure_seen": "missing_bridge_url" in nondev,
			"behavior_failures": behavior,
		}
	)
	r["status"] = status_from(blockers, [], behavior)
	return r


def evaluate_po013():
	req = ["human_index", "human_index_hash", "machine_mirror", "machine_mirror_hash", "index_updater", "path_validator"]
	blockers = missing(req)
	commands = []
	tooling = []
	if not blockers:
		for cmd in ([sys.executable, PATHS["index_updater"], "--check"], [sys.executable, PATHS["path_validator"]]):
			res = run_cmd(cmd)
			commands.append(res)
			if res["returncode"] != 0:
				tooling.append("evidence coherence command nonzero")
	r = result_base("po-013")
	r.update(
		{
			"commands": commands,
			"required_missing": blockers,
			"human_index_present": exists("human_index"),
			"machine_mirror_present": exists("machine_mirror"),
		}
	)
	r["status"] = status_from(blockers, tooling, [])
	return r


def evaluate_po014():
	req = ["human_index", "machine_mirror", "mirror_schema", "path_validator", "machine_mirror_hash"]
	blockers = missing(req)
	commands = []
	tooling = []
	if not blockers:
		for cmd in ([sys.executable, PATHS["mirror_schema"]], [sys.executable, PATHS["path_validator"]]):
			res = run_cmd(cmd)
			commands.append(res)
			if res["returncode"] != 0:
				tooling.append("mirror alignment command nonzero")
	r = result_base("po-014")
	r.update(
		{
			"commands": commands,
			"required_missing": blockers,
			"human_machine_loci_present": exists("human_index") and exists("machine_mirror"),
		}
	)
	r["status"] = status_from(blockers, tooling, [])
	return r


def evaluate_po015():
	req = ["registry_generator", "db_generator", "index_updater", "path_validator", "index_hash", "mirror_schema", "lf_checker"]
	blockers = missing(req)
	commands = []
	tooling = []
	if not blockers:
		for cmd in (
			[sys.executable, PATHS["registry_generator"], "--check"],
			[sys.executable, PATHS["db_generator"], "--check"],
			[sys.executable, PATHS["index_updater"], "--check"],
			[sys.executable, PATHS["path_validator"]],
			["bash", PATHS["index_hash"]],
			[sys.executable, PATHS["mirror_schema"]],
			[sys.executable, PATHS["lf_checker"]],
		):
			res = run_cmd(cmd)
			commands.append(res)
			if res["returncode"] != 0:
				tooling.append("fail_closed_or_coherence_command_nonzero")
	r = result_base("po-015")
	r.update(
		{
			"commands": commands,
			"required_missing": blockers,
			"all_commands_green": bool(commands) and all(c["returncode"] == 0 for c in commands),
		}
	)
	r["status"] = status_from(blockers, tooling, [])
	return r


def evaluate_po016():
	req = ["db_provider_parity", "human_index", "machine_mirror"]
	blockers = missing(req)
	blob = text("db_provider_parity") + "\n" + text("human_index") + "\n" + text("machine_mirror")
	behavior = []
	for label in ["DB_PROVIDER_PARITY_OK", "DB_BRIDGE_CAPS_OK", "DB_BRIDGE_FALLBACK_OK"]:
		if label in blob and re.search(rf'{label}.*"type"\s*:\s*"token"', blob):
			behavior.append(f"{label}_claimed_as_token")
	r = result_base("po-016")
	r.update(
		{
			"required_missing": blockers,
			"db_labels_token_overclaim_detected": bool(behavior),
			"behavior_failures": behavior,
		}
	)
	r["status"] = status_from(blockers, [], behavior)
	return r


def evaluate_po017():
	req = ["db_provider_parity"]
	blockers = missing(req)
	blob = text("db_provider_parity")
	behavior = []
	if "DEV_DB_BRIDGE_FALLBACK_OK" in blob and "dev" not in blob.lower():
		behavior.append("dev_bridge_fallback_token_scope_unclear")
	for label in ["DB_BRIDGE_FALLBACK_OK", "DB_PROVIDER_PARITY_OK", "DB_BRIDGE_CAPS_OK"]:
		if label in blob and re.search(rf'{label}.*"type"\s*:\s*"token"', blob):
			behavior.append(f"{label}_scope_broadened_to_token")
	r = result_base("po-017")
	r.update(
		{
			"required_missing": blockers,
			"fallback_scope_checked": True,
			"behavior_failures": behavior,
		}
	)
	r["status"] = status_from(blockers, [], behavior)
	return r


def evaluate_po018():
	req = ["router_key_table", "registry_diff", "db_provider_parity", "ops_provider_closure"]
	blockers = missing(req)
	behavior = []
	ops = text("ops_provider_closure")
	if "drain" in ops.lower() and re.search(r'"pf09.*claimed"\s*:\s*true', ops.lower()):
		behavior.append("pf09_drainage_claimed")
	r = result_base("po-018")
	r.update(
		{
			"required_missing": blockers,
			"active_evidence_families_present": len(blockers) == 0,
			"pf09_drainage_not_claimed": not behavior,
			"behavior_failures": behavior,
		}
	)
	r["status"] = status_from(blockers, [], behavior)
	return r


def evaluate_po019():
	req = ["readme", "changelog", "docs_index"]
	blockers = missing(req)
	blob = text("readme") + "\n" + text("changelog") + "\n" + text("docs_index")
	behavior = []
	if "HDE-EPIC032" not in blob:
		behavior.append("epic032_repo_docs_marker_missing")
	r = result_base("po-019")
	r.update(
		{
			"required_missing": blockers,
			"reused_foundation_checked_from_repo_docs": "HDE-EPIC032" in blob,
			"behavior_failures": behavior,
		}
	)
	r["status"] = status_from(blockers, [], behavior)
	return r


def evaluate_po020():
	req = ["ops_provider_closure"]
	blockers = missing(req)
	ops = text("ops_provider_closure")
	behavior = []
	for marker in ["qa_pass_claimed", "epic_closure", "checklist"]:
		if marker in ops and re.search(rf'"{marker}"\s*:\s*true', ops):
			behavior.append(f"truth_class_overclaim_{marker}")
	r = result_base("po-020")
	r.update(
		{
			"required_missing": blockers,
			"truth_classes_remain_separate": not behavior,
			"behavior_failures": behavior,
		}
	)
	r["status"] = status_from(blockers, [], behavior)
	return r


def evaluate_po021():
	req = ["ops_provider_closure", "db_provider_parity"]
	blockers = missing(req)
	blob = text("ops_provider_closure") + "\n" + text("db_provider_parity")
	behavior = []
	if re.search(r"vendor.version.*conformance.*true", blob.lower()):
		behavior.append("vendor_version_runtime_conformance_claimed")
	r = result_base("po-021")
	r.update(
		{
			"required_missing": blockers,
			"vendor_version_runtime_conformance_claimed": bool(behavior),
			"behavior_failures": behavior,
		}
	)
	r["status"] = status_from(blockers, [], behavior)
	return r


def evaluate_po022():
	req = ["ops_provider_closure", "db_provider_parity"]
	blockers = missing(req)
	blob = text("ops_provider_closure") + "\n" + text("db_provider_parity")
	behavior = []
	if re.search(r"live.*provider.*pass", blob.lower()) and "unavailable" not in blob.lower() and "false" not in blob.lower():
		behavior.append("live_provider_behavior_claimed")
	r = result_base("po-022")
	r.update(
		{
			"required_missing": blockers,
			"live_provider_behavior_claimed": bool(behavior),
			"behavior_failures": behavior,
		}
	)
	r["status"] = status_from(blockers, [], behavior)
	return r


def evaluate_po023():
	req = ["endpoint_catalog", "http_reader"]
	blockers = missing(req)
	endpoint = text("endpoint_catalog")
	reader = text("http_reader")
	behavior = []
	if "/api/reader-proof/v1" in endpoint + reader:
		behavior.append("invented_reader_proof_route_seen")
	if "/reader" not in endpoint:
		behavior.append("reader_route_missing_from_catalog")
	r = result_base("po-023")
	r.update(
		{
			"required_missing": blockers,
			"reader_route_visible": "/reader" in endpoint,
			"invented_reader_proof_route_absent": "/api/reader-proof/v1" not in endpoint + reader,
			"behavior_failures": behavior,
		}
	)
	r["status"] = status_from(blockers, [], behavior)
	return r


def evaluate_po024():
	r = result_base("po-024")
	r.update(
		{
			"live_qa_planning_or_execution_performed_implementation": False,
			"live_qa_planning_or_execution_performed_pf_edit": False,
			"live_qa_planning_or_execution_performed_closeout_action": False,
			"live_qa_role": "prove_current_results_only",
			"status": "PASS",
		}
	)
	return r


EVALUATORS = {
	"step-0a-discovery": evaluate_step0a,
	"step-0b-doc-delta": evaluate_step0b,
	"po-001": evaluate_po001,
	"po-002": evaluate_po002,
	"po-003": evaluate_po003,
	"po-004": evaluate_po004,
	"po-005": evaluate_po005,
	"po-006": evaluate_po006,
	"po-007": evaluate_po007,
	"po-008": evaluate_po008,
	"po-009": evaluate_po009,
	"po-010": evaluate_po010,
	"po-011": evaluate_po011,
	"po-012": evaluate_po012,
	"po-013": evaluate_po013,
	"po-014": evaluate_po014,
	"po-015": evaluate_po015,
	"po-016": evaluate_po016,
	"po-017": evaluate_po017,
	"po-018": evaluate_po018,
	"po-019": evaluate_po019,
	"po-020": evaluate_po020,
	"po-021": evaluate_po021,
	"po-022": evaluate_po022,
	"po-023": evaluate_po023,
	"po-024": evaluate_po024,
}


def write_manifest(check_id, status, primary_log, primary_proof):
	ROOT.mkdir(parents=True, exist_ok=True)
	existing = []
	if MANIFEST.exists():
		try:
			loaded = json.loads(MANIFEST.read_text(encoding="utf-8"))
			if isinstance(loaded, list):
				existing = [row for row in loaded if row.get("check_id") != check_id]
		except Exception:
			existing = []
	entry = {
		"check_id": check_id,
		"log_path": str(primary_log),
		"log_path_proof": str(primary_proof),
		"status": status,
		"updated_at_utc": utc_now(),
	}
	existing.append(entry)
	existing.sort(key=lambda row: row.get("check_id", ""))
	MANIFEST.write_bytes(canonical_json_bytes(existing))
	write_path_proof(MANIFEST)


def write_primary(check_id, result, command):
	check_dir = CHECKS_ROOT / check_id
	check_dir.mkdir(parents=True, exist_ok=True)
	primary = check_dir / "primary.log"
	primary_proof = Path(str(primary) + ".path_proof.txt")
	result_path = check_dir / "result.json"
	result_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
	status = result.get("status", "FAIL_TOOLING")
	exit_code = 0 if status == "PASS" else 2 if status == "TOOLING_BLOCKED" else 1
	header = {
		"schema_version": "pf27.step_log_header.v1",
		"timestamp_utc": utc_now(),
		"check_id": check_id,
		"check_name": CHECK_NAMES.get(check_id, check_id),
		"status": status,
		"fail_status": "" if status == "PASS" else status,
		"command": command,
		"command_provenance": "Copy/paste from plan",
		"exit_code": exit_code,
		"evidence_artifacts": [str(primary), str(primary_proof), str(result_path)],
		"captured_env": {k: env(k) for k in ENV_KEYS},
		"pf_refs": PF_REFS,
		"intended_tokens": [],
		"claimed_tokens": [],
	}
	body = json.dumps(result, indent=2, sort_keys=True)
	primary.write_text(json.dumps(header, ensure_ascii=False, sort_keys=True) + "\n" + body + "\n", encoding="utf-8")
	primary_proof = write_path_proof(primary)
	write_manifest(check_id, status, primary, primary_proof)
	return exit_code


def main():
	if len(sys.argv) != 2 or sys.argv[1] not in EVALUATORS:
		print("usage: live_qa_harness.py CHECK_ID", file=sys.stderr)
		print("known: " + ", ".join(sorted(EVALUATORS)), file=sys.stderr)
		return 2
	check_id = sys.argv[1]
	for k, v in {
		"SAFE_MODE": "1",
		"ALLOW_NETWORK": "0",
		"APP_ENV": "dev",
		"LC_ALL": "C",
		"LANG": "C",
		"TZ": "UTC",
	}.items():
		os.environ.setdefault(k, v)
	ROOT.mkdir(parents=True, exist_ok=True)
	META.mkdir(parents=True, exist_ok=True)
	CHECKS_ROOT.mkdir(parents=True, exist_ok=True)
	command = f"python audit/qa/hde-epic032/00_meta/live_qa_harness.py {check_id}"
	result = EVALUATORS[check_id]()
	return write_primary(check_id, result, command)


if __name__ == "__main__":
	raise SystemExit(main())
