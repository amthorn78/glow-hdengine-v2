#!/usr/bin/env python3
"""X8 gates on the built packages; prints a JSON receipt of flags, counts and digests only."""
import json, os, shutil, subprocess, sys
from pathlib import Path
REPO = Path("/home/user/glow-hdengine-v2")
E = REPO / "docs/ephemeral/modifications/evidence/20261011-gcfpe-mb008-to-promotion"
S = Path(sys.argv[1])          # x8 scratch dir with base/, out/, graph/
I = Path(sys.argv[2])          # installed skills root (read only, copied)
ENV = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1"}
PK = ["change-flow", "flowmaster-validate", "glow-hde-pr-development", "glow-graph-contract", "session-relay-flowmaster", "amthor-workspace-governance-audit"]
SUITE13 = ["amthor-workspace-governance-audit", "change-flow", "flowmaster-primary", "flowmaster-validate", "glow-graph-contract", "glow-hde-pr-development", "glow-merged-change-attribution-lock", "glow-po-reporting", "session-branch-flowmaster", "session-relay-flowmaster", "skill-creator", "tw-flowmaster", "typesafe-scoring"]
def run(args, cwd=None):
    r = subprocess.run([str(a) for a in args], cwd=cwd, capture_output=True, text=True, env=ENV)
    return r.returncode, r.stdout, r.stderr
def js(out):
    try: return json.loads(out)
    except ValueError: return {"_unparsed": out[-300:]}
out, base = S / "out", S / "base"
contract = E / "execute/contracts/gcfpe-20261009.1-100926.1-production-contract.json"
g = {}
c, o, _ = run([sys.executable, E / "plan/package_apply.py", out, "--check"]); d = js(o)
g["redlines_check"] = {"exit": c, "ok": d.get("ok"), "landed": sum(r["state"] == "LANDED" for r in d.get("rows", [])), "ops": len(d.get("rows", [])),
    "not_landed": sorted(r["id"] for r in d.get("rows", []) if r["state"] != "LANDED")}
# X10 repair: DR-REV and DR-REV-FX (execute/d24-repair-redlines.json) supersede AU-REV and AU-REV-FX's value 1.14.0 with 1.14.1
_audit = out / "amthor-workspace-governance-audit"
g["redlines_check"]["superseded_by_d24_repair"] = (g["redlines_check"]["not_landed"] == ["AU-REV", "AU-REV-FX"]
    and "WORKSPACE_GOVERNANCE_AUDITOR_REVISION:** 1.14.1" in (_audit / "SKILL.md").read_text(encoding="utf-8")
    and "WORKSPACE_GOVERNANCE_AUDITOR_REVISION:** 1.14.1" in (_audit / "scripts/run_fixture_suite.py").read_text(encoding="utf-8"))
c, o, _ = run([sys.executable, E / "execute/package_build.py", base, out, "--contract", contract, "--graph", S / "graph/production-graph.json", "--plan", E / "PLAN-20261011.md", "--check"]); d = js(o)
g["package_build_check"] = {"exit": c, "equal": d.get("equal"), "files": d.get("files")}
suite = S / "suite"
if suite.exists(): shutil.rmtree(suite)
suite.mkdir()
for k in SUITE13:
    shutil.copytree(out / k if k in PK else I / k, suite / k, ignore=shutil.ignore_patterns("__pycache__"))
fv, cf = suite / "flowmaster-validate", suite / "change-flow"
c, o, _ = run([sys.executable, "scripts/validate_flowmaster.py", "--skills-root", suite], cwd=fv); d = js(o)
cov = d.get("change_contract_coverage", {}); cur = cov.get("gcfpe_current_direct_handoff", {}); fx = cov.get("gcfpe_current_fixtures", {})
g["flowmaster_suite"] = {"exit": c, "verdict": d.get("verdict"), "suite_ok": d.get("suite_ok"), "finding_counts": d.get("finding_counts"), "self_identity": d.get("self_identity"),
    "skills": {n: s.get("status") for n, s in d.get("skills", {}).items()}, "rows_exact": cov.get("rows_exact"), "interfaces_closed": cov.get("interfaces_closed"),
    "current_overlay": {k: cur.get(k) for k in ("ok", "profile", "target_release", "contract_status", "frozen_graph_edge_count")},
    "current_fixtures": {k: fx.get(k) for k in ("fixture_suite_ok", "section_13_fixture_count", "section_13_passed", "section_13_variant_count", "section_13_variants_passed", "case_count")},
    "dependency_cases": sum(1 for x in fx.get("cases", []) if x.get("name", "").startswith("dependency-") and x.get("passed")),
    "change_flow_fixtures": {k: (d.get("fixtures") or {}).get(k) for k in ("total", "positive_count", "negative_count", "passed_expectations", "fixture_suite_ok")}}
croot = S / "croot"; (croot / "graph").mkdir(parents=True, exist_ok=True)
shutil.copyfile(cf / "references/gcfpe-20261009.1-100926.1-candidate-graph-contract.json", croot / "graph/GCFPE-20261009.1-Candidate-Graph-Contract.json")
cc = cf / "references/gcfpe-20261009.1-100926.1-direct-handoff-contract.json"
c, o, _ = run([sys.executable, "scripts/validate_flowmaster.py", "--skills-root", suite, "--gcfpe-contract", cc, "--gcfpe-candidate-root", croot], cwd=fv); d = js(o)
cov = d.get("change_contract_coverage", {})
g["flowmaster_suite_explicit_100926"] = {"exit": c, "verdict": d.get("verdict"), "candidate_ok": cov.get("gcfpe_20260914_candidate", {}).get("ok"), "candidate_profile": cov.get("gcfpe_20260914_candidate", {}).get("profile"), "candidate_fixtures_ok": cov.get("gcfpe_20260914_candidate_fixtures", {}).get("fixture_suite_ok")}
c, o, _ = run([sys.executable, "scripts/validate_gcfpe_20261009.py", cf, "--contract", cc], cwd=fv); d = js(o)
g["profile_100926_direct"] = {"exit": c, "ok": d.get("ok"), "errors": d.get("errors"), "profile": d.get("profile")}
c, o, _ = run([sys.executable, "scripts/run_gcfpe_20261009_fixtures.py", cf, "--contract", cc], cwd=fv); d = js(o)
g["fixtures_100926_direct"] = {"exit": c, "fixture_suite_ok": d.get("fixture_suite_ok"), "fixtures": d.get("section_13_fixture_count"), "passed": d.get("section_13_passed"), "variants": d.get("section_13_variant_count"), "cases": d.get("case_count")}
c, o, _ = run([sys.executable, "scripts/run_change_flow_fixtures.py"], cwd=fv); d = js(o)
g["change_flow_fixtures"] = {"exit": c, "total": d.get("total"), "passed": d.get("passed_expectations"), "ok": d.get("fixture_suite_ok")}
c, o, e = run([sys.executable, "scripts/validate_gcfpe_20261009.py"], cwd=cf); g["change_flow_validate_100926"] = {"exit": c, "line": (o + e).strip().splitlines()[-1]}
c, o, e = run([sys.executable, "scripts/validate_gcfpe_20260914.py"], cwd=cf); g["change_flow_validate_091426_history"] = {"exit": c, "line": (o + e).strip().splitlines()[-1], "expected": "fails by design on the new revision (PLAN §6)"}
c, o, e = run([sys.executable, "scripts/validate_glow_hde_pr_development.py"], cwd=suite / "glow-hde-pr-development"); g["pr_development_validator"] = {"exit": c, "line": (o + e).strip().splitlines()[-1]}
c, o, e = run([sys.executable, "scripts/run_fixture_suite.py"], cwd=suite / "amthor-workspace-governance-audit"); g["audit_fixture_suite"] = {"exit": c, "line": (o + e).strip().splitlines()[-1]}
c, o, e = run([sys.executable, "scripts/validate_relay_manifest.py", "--self-test"], cwd=suite / "session-relay-flowmaster"); g["relay_self_test"] = {"exit": c, "status": js(o).get("status")}
R = out / "glow-graph-contract/scripts/contract_recipe.py"; T = REPO / "docs/graph/contract-template/gcfpe-20260914.1-091426.1-direct-handoff-contract-4.0.6.json"
OR = out / "flowmaster-validate/references/glow-hde-canonical-change-flow-r1-20260923.json"; D = REPO / "docs/prompt_ecosystem_management/gcfpe.decision-record.md"
c, o, _ = run([sys.executable, R, S.parent / "x7/selected.md", T, OR, D, S / "regen-shipped.json", "--contract-revision", "4.1.1", "--primary-skill-revision", "1.3.1", "--check",
               base / "change-flow/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json", base / "flowmaster-validate/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json"])
g["regenerator_shipped_091426"] = {"exit": c, "equal_lines": o.count("EQUAL    ")}
for n in ("candidate", "production"):
    c, o, _ = run([sys.executable, R, S / f"graph/{n}.md", T, OR, D, S / f"regen-{n}.json", "--contract-revision", "4.2.0", "--primary-skill-revision", "1.4.0", "--release-values", E / "execute/contracts/release-values-100926.1.filled.json"])
    g[f"regenerator_{n}_100926"] = {"exit": c, "equal_to_x7": (S / f"regen-{n}.json").read_bytes() == (E / f"execute/contracts/gcfpe-20261009.1-100926.1-{n}-contract.json").read_bytes()}
def freeze(p): return run([sys.executable, REPO / "docs/prompt_ecosystem_management/freeze.py", p])[1].strip().splitlines()[-1]
g["digests"] = {k: {"base": freeze(base / k), "built": freeze(out / k)} for k in PK}
g["pycache_in_out"] = sum(1 for _ in out.rglob("__pycache__"))
ok = ((g["redlines_check"]["landed"] == 46 or (g["redlines_check"]["landed"] == 44 and g["redlines_check"]["superseded_by_d24_repair"])) and g["package_build_check"]["equal"] and g["flowmaster_suite"]["verdict"] == "FLOWMASTER_SUITE_PASS"
      and g["flowmaster_suite_explicit_100926"]["verdict"] == "FLOWMASTER_SUITE_PASS" and g["profile_100926_direct"]["ok"] and g["fixtures_100926_direct"]["fixture_suite_ok"]
      and g["change_flow_fixtures"]["ok"] and g["change_flow_validate_100926"]["exit"] == 0 and g["pr_development_validator"]["exit"] == 0
      and g["audit_fixture_suite"]["exit"] == 0 and g["relay_self_test"]["status"] == "PASS" and g["regenerator_shipped_091426"]["equal_lines"] == 2
      and all(g[f"regenerator_{n}_100926"]["equal_to_x7"] for n in ("candidate", "production")) and g["pycache_in_out"] == 0)
print(json.dumps({"record_type": "MB008_X8_GATES", "ok": ok, "gates": g}, indent=1))
