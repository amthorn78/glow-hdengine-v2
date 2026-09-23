"""E2: run the §2 live suites, historical layer and other-package validators on one skills tree.

usage: run_suites.py <skills-root> <graph-json-for-candidate-root> <out-dir>
Writes <out-dir>/<n>.out (stdout+stderr+exit) per command and prints each command's top-level flag.
Runs with PYTHONDONTWRITEBYTECODE=1 and TMPDIR inside /tmp/claude-0/e2/tmp.
"""
import hashlib, json, os, shutil, subprocess, sys
from pathlib import Path

sys.dont_write_bytecode = True
copy, graph, out = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
REPO = Path("/home/user/glow-hdengine-v2")
TMP = Path("/tmp/claude-0/e2/tmp")
out.mkdir(parents=True, exist_ok=True)
root = out / "candidate-root"
(root / "graph").mkdir(parents=True, exist_ok=True)
shutil.copyfile(graph, root / "graph" / "GCFPE-20260914.1-Candidate-Graph-Contract.json")
fv, cf = copy / "flowmaster-validate" / "scripts", copy / "change-flow"
contract = cf / "references" / "gcfpe-20260914.1-091426.1-direct-handoff-contract.json"
env = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1", "TMPDIR": str(TMP)}
py = sys.executable
AM = copy / "amthor-workspace-governance-audit" / "scripts"
CMDS = [
    ("live", "fm-default", [py, fv / "validate_flowmaster.py", "--skills-root", copy], None),
    ("live", "fm-candidate", [py, fv / "validate_flowmaster.py", "--skills-root", copy, "--strict-warnings",
                               "--gcfpe-contract", contract, "--gcfpe-candidate-root", root], None),
    ("live", "gcfpe-20260914", [py, fv / "validate_gcfpe_20260914.py", cf, "--contract", contract], None),
    ("live", "gcfpe-20260914-fixtures", [py, fv / "run_gcfpe_20260914_fixtures.py", cf, "--contract", contract], None),
    ("live", "gcfpe-current", [py, fv / "validate_gcfpe_current.py", cf], None),
    ("live", "gcfpe-current-fixtures", [py, fv / "run_gcfpe_current_fixtures.py", cf], None),
    ("live", "change-flow-fixtures", [py, fv / "run_change_flow_fixtures.py"], None),
    ("live", "cf-validator", [py, cf / "scripts" / "validate_gcfpe_20260914.py"], None),
    ("live", "pr-dev", [py, copy / "glow-hde-pr-development" / "scripts" / "validate_glow_hde_pr_development.py"], None),
    ("live", "relay-self-test", [py, copy / "session-relay-flowmaster" / "scripts" / "validate_relay_manifest.py", "--self-test"], None),
    ("live", "amthor-fixtures", [py, "run_fixture_suite.py"], AM),
    ("live", "amthor-registry", [py, "validate_project_prompt_registry.py",
                                  REPO / "docs/prompt_ecosystem_management/project-prompt-contract-registry.md"], AM),
    ("hist", "strength-middleware", [py, fv / "validate_strength_middleware.py", cf], None),
    ("hist", "epic-alpha", [py, fv / "validate_epic_alpha.py", cf], None),
    ("hist", "epic-reengineering", [py, fv / "validate_epic_reengineering.py", "--change-flow", cf], None),
    ("hist", "strength-middleware-fixtures", [py, fv / "run_strength_middleware_fixtures.py", cf], None),
    ("hist", "epic-alpha-fixtures", [py, fv / "run_epic_alpha_fixtures.py", cf], None),
    ("hist", "integrated-readiness", [py, fv / "validate_integrated_readiness.py"], None),
    ("hist", "pre-guide-correction", [py, fv / "validate_pre_guide_correction.py"], None),
    ("hist", "final-scan", [py, fv / "validate_final_scan.py"], None),
    ("hist", "alpha-feedback", [py, fv / "validate_alpha_feedback.py"], None),
    ("hist", "integrated-readiness-fixtures", [py, fv / "run_integrated_readiness_fixtures.py"], None),
    ("hist", "final-scan-fixtures", [py, fv / "run_final_scan_fixtures.py"], None),
    ("hist", "alpha-feedback-fixtures", [py, fv / "run_alpha_feedback_fixtures.py"], None),
]


def flag(name, rc, text):
    try:
        data = json.loads(text)
    except Exception:
        data = None
    if isinstance(data, dict):
        keys = {}
        for k in ("verdict", "suite_ok", "self_identity", "status", "ok", "fixture_suite_ok", "valid", "passed", "failed",
                  "case_count", "total", "passed_expectations", "finding_counts"):
            if k in data:
                v = data[k]
                keys[k] = len(v) if isinstance(v, list) and k != "problems" else v
        if "cases" in data and isinstance(data["cases"], list):
            keys["cases"] = len(data["cases"])
            keys["failed_cases"] = sum(1 for c in data["cases"] if isinstance(c, dict) and not c.get("passed", True))
        if "errors" in data:
            keys["errors"] = data["errors"] if len(json.dumps(data["errors"])) < 400 else f"{len(data['errors'])} errors"
        if "problems" in data:
            keys["problems"] = data["problems"]
        return keys
    tail = text.strip().splitlines()[-3:] if text.strip() else []
    return {"text_tail": tail}


results = []
for layer, name, cmd, cwd in CMDS:
    r = subprocess.run([str(c) for c in cmd], capture_output=True, text=True, env=env, cwd=str(cwd) if cwd else None)
    body = r.stdout + ("\n--stderr--\n" + r.stderr if r.stderr else "")
    (out / f"{name}.out").write_text(body + f"\n--exit {r.returncode}--\n", encoding="utf-8")
    info = {"layer": layer, "name": name, "exit": r.returncode,
            "stdout_sha256": hashlib.sha256(r.stdout.encode()).hexdigest(), "stdout_bytes": len(r.stdout.encode()),
            "stdout_sha256_rootless": hashlib.sha256(r.stdout.replace(str(copy), "<copy>").encode()).hexdigest(),
            "flag": flag(name, r.returncode, r.stdout if r.stdout.strip() else r.stderr)}
    results.append(info)
    print(json.dumps(info, ensure_ascii=False))
(out / "summary.json").write_text(json.dumps(results, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
