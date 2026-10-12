#!/usr/bin/env python3
"""Proof for flowmaster-validate 3.4.1 and freeze.py (Nathan's decision 2, 2026-10-12; D28).

Two copies of the WHOLE installed skills directory, with the new package in both: in one every
skill's name line is quoted (`name: "<skill>"`, as Save skill writes it), in the other every one
is plain. Every gate and the freeze.py comparison runs on both and must give the same result, and
every GCFPE gate must pass. Two control copies carry the installed 3.4.0 instead, to show the setup
detects the defect. Then the standing tests are shown to fire. Prints a JSON receipt: flags,
counts, digests and error codes only (paths are written as <root>).

Usage: fv341_proof.py <installed-skills-dir> <extracted-package-dir> <scratch-dir> [--roots-only]
  With --roots-only, only the two new roots are built and gated (used on the installed tree after
  Nathan installs: pass the install itself as <installed-skills-dir> and its own
  flowmaster-validate as <extracted-package-dir>).
"""
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

REPO = Path("/home/user/glow-hdengine-v2")
E = REPO / "docs/ephemeral/modifications/evidence/20261011-gcfpe-mb008-to-promotion"
FREEZE = REPO / "docs/prompt_ecosystem_management/freeze.py"
ENV = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1"}
PLAIN_RE = re.compile(rb"(?m)\A(---\r?\n(?:(?!---).*\r?\n)*?)name:([ \t]*)([a-z0-9-]+)([ \t]*\r?)$")
QUOTED_RE = re.compile(rb"(?m)\A(---\r?\n(?:(?!---).*\r?\n)*?)name:([ \t]*)([\"'])([a-z0-9-]+)\3([ \t]*\r?)$")
# The suite's own six skills (EXPECTED in validate_flowmaster.py). Run untargeted, the suite also checks every other
# marked specialization in the root; the installed human-design-reading-flowmaster (another project) fails its
# 1.0.1 contract markers with or without this change, so the GCFPE gate is the suite targeted at these six, on the
# whole root. The untargeted run is recorded too, and must differ from the targeted one only by that skill.
SUITE_TARGETS = ["flowmaster-primary", "tw-flowmaster", "change-flow", "session-branch-flowmaster", "session-relay-flowmaster", "flowmaster-validate"]
TARGET_ARGS = [a for name in SUITE_TARGETS for a in ("--target", name)]
REVIEWED = {  # the packet's tree digests (execute/x10-packages.json), and the 3.4.1 build
    "change-flow": "25 c9b0927f327c31328c4b64a0408a946619c985a492702a70a2cd88e216cf22c2",
    "glow-hde-pr-development": "4 f0880ceb6c5d8104a79fb37260ce2cdd90cac110878eaabc2a12106f8b6bbaf0",
    "glow-graph-contract": "9 d00c8d1705e3aa181b22c151f103edc9a0f9eccdcfe593fd3a92b90cb0fec6b9",
    "session-relay-flowmaster": "5 33d8b9be98288b1ba698a403964409fb65f5cc53d81cbd94a348ff5b3ce4b52c",
    "amthor-workspace-governance-audit": "15 f0f00820a1df24d20974dd3ad1a58bc4cb8d358d6e7b9a77ccd9ec26329e45f8",
    "glow-merged-change-attribution-lock": "10 c518ccb0076b042859de4d2e136ef682bb127b6524133d2a575d433490eaf48f",
    "flowmaster-validate": "37 45c7d5d743fbcdf2100fa74ba6b2ff06609c0f056b7cfdee93a5fd74750f716d",
}


def run(args, cwd=None, timeout=600):
    r = subprocess.run([str(a) for a in args], cwd=cwd, capture_output=True, text=True, env=ENV, timeout=timeout)
    return r.returncode, r.stdout, r.stderr


def js(text):
    try:
        return json.loads(text)
    except ValueError:
        return {}


def scrub(value, root: Path):
    return json.loads(json.dumps(value).replace(str(root), "<root>"))


def set_form(root: Path, form: str) -> int:
    changed = 0
    for skill_md in sorted(root.glob("*/SKILL.md")):
        data = skill_md.read_bytes()
        if form == "quoted":
            new = PLAIN_RE.sub(rb'\1name:\2"\3"\4', data, count=1)
        else:
            new = QUOTED_RE.sub(rb"\1name:\2\4\5", data, count=1)
        if new != data:
            skill_md.write_bytes(new)
            changed += 1
    return changed


def make_root(installed: Path, package: Path, dest: Path, form: str) -> dict:
    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(installed, dest, ignore=shutil.ignore_patterns("__pycache__"))
    shutil.rmtree(dest / "flowmaster-validate")
    shutil.copytree(package, dest / "flowmaster-validate", ignore=shutil.ignore_patterns("__pycache__"))
    changed = set_form(dest, form)
    lines = {}
    for skill_md in sorted(dest.glob("*/SKILL.md")):
        m = re.search(rb"(?m)^name:.*$", skill_md.read_bytes())
        lines[skill_md.parent.name] = "quoted" if m and b'"' in m.group(0) or (m and b"'" in m.group(0)) else "plain"
    return {"skills": len(lines), "lines_rewritten": changed, "forms": sorted(set(lines.values()))}


def freeze(path: Path, script: Path = FREEZE) -> str:
    c, o, e = run([sys.executable, script, path])
    return o.strip() if c == 0 else f"EXIT {c}: {e.strip()[:200]}"


def suite_summary(c, o, e, root):
    d = js(o)
    cov = d.get("change_contract_coverage", {})
    cur = cov.get("gcfpe_current_direct_handoff", {})
    fx = cov.get("gcfpe_current_fixtures", {})
    return scrub({
        "exit": c, "verdict": d.get("verdict"), "suite_ok": d.get("suite_ok"), "fatal_error": js(e).get("fatal_error"),
        "finding_counts": d.get("finding_counts"), "self_identity": d.get("self_identity"),
        "name_line_forms": d.get("name_line_forms"),
        "skills": {n: s.get("status") for n, s in d.get("skills", {}).items()},
        "rows_exact": cov.get("rows_exact"), "interfaces_closed": cov.get("interfaces_closed"),
        "current_overlay": {k: cur.get(k) for k in ("ok", "errors", "profile", "target_release", "contract_status")},
        "current_fixtures": {k: fx.get(k) for k in ("fixture_suite_ok", "section_13_fixture_count", "section_13_passed", "case_count")},
        "change_flow_fixtures": {k: (d.get("fixtures") or {}).get(k) for k in ("total", "passed_expectations", "fixture_suite_ok")},
        "findings": sorted({f.get("rule_id", "") + ":" + f.get("severity", "") for f in d.get("findings", [])}),
    }, root)


def gates(root: Path, scratch: Path) -> dict:
    fv, cf = root / "flowmaster-validate", root / "change-flow"
    cc = cf / "references/gcfpe-20261009.1-100926.1-direct-handoff-contract.json"
    g = {}
    g["suite_untargeted"] = suite_summary(*run([sys.executable, "scripts/validate_flowmaster.py", "--skills-root", root], cwd=fv), root)
    g["suite"] = suite_summary(*run([sys.executable, "scripts/validate_flowmaster.py", "--skills-root", root, *TARGET_ARGS], cwd=fv), root)
    croot = scratch / f"croot-{root.name}"
    (croot / "graph").mkdir(parents=True, exist_ok=True)
    shutil.copyfile(cf / "references/gcfpe-20261009.1-100926.1-candidate-graph-contract.json", croot / "graph/GCFPE-20261009.1-Candidate-Graph-Contract.json")
    c, o, e = run([sys.executable, "scripts/validate_flowmaster.py", "--skills-root", root, *TARGET_ARGS, "--gcfpe-contract", cc, "--gcfpe-candidate-root", croot], cwd=fv)
    d = js(o); cov = d.get("change_contract_coverage", {})
    g["suite_explicit_100926"] = scrub({"exit": c, "verdict": d.get("verdict"), "candidate_ok": cov.get("gcfpe_20260914_candidate", {}).get("ok"),
        "candidate_errors": cov.get("gcfpe_20260914_candidate", {}).get("errors"),
        "candidate_fixtures_ok": cov.get("gcfpe_20260914_candidate_fixtures", {}).get("fixture_suite_ok")}, root)
    c, o, e = run([sys.executable, "scripts/validate_gcfpe_20261009.py", cf, "--contract", cc], cwd=fv); d = js(o)
    g["profile_100926"] = scrub({"exit": c, "ok": d.get("ok"), "errors": d.get("errors"), "profile": d.get("profile"),
        "not_evaluated": d.get("prompt_body_checks_not_evaluated")}, root)
    c, o, e = run([sys.executable, "scripts/run_gcfpe_20261009_fixtures.py", cf, "--contract", cc], cwd=fv); d = js(o)
    g["fixtures_100926"] = {"exit": c, "fixture_suite_ok": d.get("fixture_suite_ok"), "fixtures": d.get("section_13_fixture_count"),
        "passed": d.get("section_13_passed"), "variants": d.get("section_13_variant_count"), "cases": d.get("case_count")}
    c, o, e = run([sys.executable, "scripts/run_gcfpe_current_fixtures.py", cf], cwd=fv); d = js(o)
    g["fixtures_current"] = {"exit": c, "fixture_suite_ok": d.get("fixture_suite_ok"), "cases": d.get("case_count")}
    c, o, e = run([sys.executable, "scripts/run_change_flow_fixtures.py"], cwd=fv); d = js(o)
    g["change_flow_fixtures"] = {"exit": c, "total": d.get("total"), "passed": d.get("passed_expectations"), "ok": d.get("fixture_suite_ok")}
    hist = {}
    for name, args in (("run_alpha_feedback_fixtures", []), ("run_final_scan_fixtures", []), ("run_integrated_readiness_fixtures", []),
                       ("run_epic_alpha_fixtures", []), ("run_strength_middleware_fixtures", [])):
        c, o, e = run([sys.executable, f"scripts/{name}.py", *args], cwd=fv); d = js(o)
        hist[name] = {"exit": c, "fixture_suite_ok": d.get("fixture_suite_ok"), "total": d.get("total", d.get("cases"))}
    g["historical_runners"] = hist
    for label, script in (("change_flow_validate_100926", "validate_gcfpe_20261009.py"), ("change_flow_validate_091426_history", "validate_gcfpe_20260914.py")):
        c, o, e = run([sys.executable, f"scripts/{script}"], cwd=cf)
        g[label] = scrub({"exit": c, "line": ((o + e).strip().splitlines() or [""])[-1][:300]}, root)
    c, o, e = run([sys.executable, "scripts/validate_glow_hde_pr_development.py"], cwd=root / "glow-hde-pr-development")
    g["pr_development_validator"] = {"exit": c, "line": ((o + e).strip().splitlines() or [""])[-1][:200]}
    c, o, e = run([sys.executable, "scripts/run_fixture_suite.py"], cwd=root / "amthor-workspace-governance-audit")
    g["audit_fixture_suite"] = {"exit": c, "line": ((o + e).strip().splitlines() or [""])[-1][:200]}
    c, o, e = run([sys.executable, "scripts/validate_relay_manifest.py", "--self-test"], cwd=root / "session-relay-flowmaster")
    g["relay_self_test"] = {"exit": c, "status": js(o).get("status")}
    att = {}
    for name in ("run_fixture_tests", "run_artifact_adversarial_tests", "run_collector_adversarial_tests"):
        c, o, e = run([sys.executable, f"scripts/{name}.py"], cwd=root / "glow-merged-change-attribution-lock")
        d = js(o)
        att[name] = {"exit": c, **{k: d.get(k) for k in ("ok", "status", "passed", "failed", "total") if k in d}}
    g["attribution_lock_tests"] = att
    gc = root / "glow-graph-contract/scripts"
    oracle = fv / "references/glow-hde-canonical-change-flow-r1-20260923.json"
    template = REPO / "docs/graph/contract-template/gcfpe-20260914.1-091426.1-direct-handoff-contract-4.0.6.json"
    decisions = REPO / "docs/prompt_ecosystem_management/gcfpe.decision-record.md"
    builds = {}
    for label, parts in (("main", REPO / "docs/graph/parts"), ("candidate", E / "execute/candidate-graph-parts"), ("production", E / "execute/production-graph-parts")):
        md = scratch / f"graph-{root.name}-{label}.md"
        c, o, e = run([sys.executable, gc / "graph_parts.py", "build", parts, md])
        builds[label] = {"exit": c, "line": ((o + e).replace(str(scratch), "<scratch>").replace(root.name, "<root>").strip().splitlines() or [""])[-1][:200]}
    g["graph_builds"] = builds
    c, o, e = run([sys.executable, gc / "contract_recipe.py", scratch / f"graph-{root.name}-main.md", template, oracle, decisions, scratch / f"regen-{root.name}-shipped.json",
                   "--contract-revision", "4.1.1", "--primary-skill-revision", "1.3.1", "--check",
                   cf / "references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json", fv / "references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json"])
    g["regenerator_shipped_091426"] = {"exit": c, "equal_lines": o.count("EQUAL    ")}
    for n in ("candidate", "production"):
        out = scratch / f"regen-{root.name}-{n}.json"
        c, o, e = run([sys.executable, gc / "contract_recipe.py", scratch / f"graph-{root.name}-{n}.md", template, oracle, decisions, out,
                       "--contract-revision", "4.2.0", "--primary-skill-revision", "1.4.0", "--release-values", E / "execute/contracts/release-values-100926.1.filled.json"])
        g[f"regenerator_{n}_100926"] = {"exit": c, "equal_to_x7": out.is_file() and out.read_bytes() == (E / f"execute/contracts/gcfpe-20261009.1-100926.1-{n}-contract.json").read_bytes()}
    c, o, e = run([sys.executable, gc / "registry_deriver.py", root / "amthor-workspace-governance-audit", REPO / "docs/prompt_ecosystem_management/project-prompt-contract-registry.md", REPO / "docs/graph/parts"])
    g["registry_deriver_main"] = {"exit": c, "line": ((o + e).strip().splitlines() or [""])[-1][:200]}
    c, o, e = run([sys.executable, gc / "registry_deriver.py", root / "amthor-workspace-governance-audit", E / "execute/candidate-registry.md", E / "execute/candidate-graph-parts"])
    g["registry_deriver_candidate"] = {"exit": c, "line": ((o + e).strip().splitlines() or [""])[-1][:200]}
    g["freeze"] = {p.name: freeze(p) for p in sorted(root.iterdir()) if p.is_dir()}
    return g


def gcfpe_pass(g: dict) -> dict:
    checks = {
        "suite": g["suite"]["verdict"] == "FLOWMASTER_SUITE_PASS" and g["suite"]["self_identity"] == "OK" and (g["suite"]["name_line_forms"] or {}).get("ok") is True,
        "suite_explicit_100926": g["suite_explicit_100926"]["verdict"] == "FLOWMASTER_SUITE_PASS",
        "suite_untargeted_fails_only_on_other_project": {n for n, s in g["suite_untargeted"]["skills"].items() if s != "PASS"} <= {"human-design-reading-flowmaster"}
            and g["suite_untargeted"]["findings"] == ["FMV-SKILL-STRUCTURE-001:ERROR"] and (g["suite_untargeted"]["name_line_forms"] or {}).get("ok") is True,
        "profile_100926": g["profile_100926"]["ok"] is True,
        "fixtures_100926": g["fixtures_100926"]["fixture_suite_ok"] is True,
        "fixtures_current": g["fixtures_current"]["fixture_suite_ok"] is True,
        "change_flow_fixtures": g["change_flow_fixtures"]["ok"] is True,
        "change_flow_validate_100926": g["change_flow_validate_100926"]["exit"] == 0,
        "pr_development_validator": g["pr_development_validator"]["exit"] == 0,
        "audit_fixture_suite": g["audit_fixture_suite"]["exit"] == 0,
        "relay_self_test": g["relay_self_test"]["status"] == "PASS",
        "attribution_lock_tests": all(v["exit"] == 0 for v in g["attribution_lock_tests"].values()),
        "graph_builds": all(v["exit"] == 0 for v in g["graph_builds"].values()),
        "regenerator_shipped_091426": g["regenerator_shipped_091426"]["equal_lines"] == 2,
        "regenerator_candidate_100926": g["regenerator_candidate_100926"]["equal_to_x7"],
        "regenerator_production_100926": g["regenerator_production_100926"]["equal_to_x7"],
        "registry_deriver_main": g["registry_deriver_main"]["exit"] == 0,
        "registry_deriver_candidate": g["registry_deriver_candidate"]["exit"] == 0,
        "freeze_reviewed": all(g["freeze"].get(k) == v for k, v in REVIEWED.items()),
    }
    return {"ok": all(checks.values()), "checks": checks}


def differences(a: dict, b: dict, prefix="") -> list[str]:
    out = []
    for k in sorted(set(a) | set(b)):
        x, y = a.get(k), b.get(k)
        if isinstance(x, dict) and isinstance(y, dict):
            out += differences(x, y, f"{prefix}{k}.")
        elif x != y:
            out.append(f"{prefix}{k}")
    return out


def mutate(package: Path, scratch: Path, plain_root: Path) -> dict:
    """The standing tests must fire when the equivalence is removed, on an all-plain root."""
    cases = {}
    edits = {
        "flowmaster_NAME_RE_one_form": ("scripts/validate_flowmaster.py", 'NAME_RE = re.compile(r"(?m)^name:\\s*([\\"\']?)([a-z0-9-]+)\\1\\s*$")', 'NAME_RE = re.compile(r"(?m)^name:\\s*()([a-z0-9-]+)\\s*$")'),
        "current_find_skill_one_form": ("scripts/validate_gcfpe_current.py", "        if names_skill(text, name):\n", '        if re.search(rf"(?m)^name:\\s*{re.escape(name)}\\s*$", text):\n'),
        "digest_without_canonical": ("scripts/validate_gcfpe_20260914.py", "        return canonical_skill_md(SELF_IDENTITY_RE.sub(b\"\", data))\n", "        return SELF_IDENTITY_RE.sub(b\"\", data)\n"),
        "canonical_removed_1009": ("scripts/validate_gcfpe_20261009.py", "    return SKILL_NAME_QUOTED_RE.sub(rb\"\\1\\3\\4\", data[:end], count=1) + data[end:]\n", "    return data\n"),
    }
    for label, (rel, old, new) in edits.items():
        root = scratch / f"mut-{label}"
        if root.exists():
            shutil.rmtree(root)
        shutil.copytree(plain_root, root, ignore=shutil.ignore_patterns("__pycache__"))
        path = root / "flowmaster-validate" / rel
        text = path.read_text(encoding="utf-8")
        found = text.count(old)
        path.write_text(text.replace(old, new), encoding="utf-8")
        c, o, e = run([sys.executable, "scripts/validate_flowmaster.py", "--skills-root", root, *TARGET_ARGS], cwd=root / "flowmaster-validate")
        d = js(o)
        nf = d.get("name_line_forms") or {}
        cases[label] = {"edit_found": found, "suite_exit": c, "verdict": d.get("verdict"), "name_line_forms_ok": nf.get("ok"),
                        "fired": c != 0 and nf.get("ok") is False, "error_kinds": sorted({x.split(":")[0] + ":" + x.split(":")[1] for x in nf.get("errors", [])})}
        shutil.rmtree(root)
    text = FREEZE.read_text(encoding="utf-8")
    broken = scratch / "freeze_broken.py"
    old = "    return SKILL_NAME_QUOTED_RE.sub(rb\"\\1\\3\\4\", data[:end], count=1) + data[end:]\n"
    broken.write_text(text.replace(old, "    return data\n"), encoding="utf-8")
    c, o, e = run([sys.executable, broken, plain_root / "change-flow"])
    cases["freeze_canonical_removed"] = {"edit_found": text.count(old), "exit": c, "printed_digest": bool(o.strip()), "fired": c == 2 and not o.strip(), "stderr": e.strip()[:200]}
    return cases


def main() -> int:
    installed, package, scratch = (Path(a).resolve() for a in sys.argv[1:4])
    roots_only = "--roots-only" in sys.argv[4:]
    scratch.mkdir(parents=True, exist_ok=True)
    # The recipe before D28, from `main` at 3473b34, for the control's raw digests only.
    (scratch / "freeze_raw.py").write_text(subprocess.run(["git", "-C", str(REPO), "show", "3473b34:docs/prompt_ecosystem_management/freeze.py"],
                                                          capture_output=True, text=True, check=True).stdout, encoding="utf-8")
    receipt = {"record_type": "MB008_FV341_PROOF", "freeze_selftest": run([sys.executable, FREEZE, "--selftest"])[1].strip(),
               "package_freeze": freeze(package), "roots": {}, "gates": {}}
    for form in ("quoted", "plain"):
        receipt["roots"][form] = make_root(installed, package, scratch / f"new-{form}", form)
        receipt["gates"][form] = gates(scratch / f"new-{form}", scratch)
    q, p = receipt["gates"]["quoted"], receipt["gates"]["plain"]
    receipt["quoted_vs_plain_differences"] = differences(q, p)
    receipt["gcfpe_pass"] = {"quoted": gcfpe_pass(q), "plain": gcfpe_pass(p)}
    if not roots_only:
        control = {}
        old = installed / "flowmaster-validate"
        for form in ("quoted", "plain"):
            root = scratch / f"old-{form}"
            make_root(installed, old, root, form)
            c, o, e = run([sys.executable, "scripts/validate_flowmaster.py", "--skills-root", root, *TARGET_ARGS], cwd=root / "flowmaster-validate")
            s = suite_summary(c, o, e, root)
            cf = root / "change-flow"
            c2, o2, _ = run([sys.executable, "scripts/validate_gcfpe_20261009.py", cf, "--contract", cf / "references/gcfpe-20261009.1-100926.1-direct-handoff-contract.json"], cwd=root / "flowmaster-validate")
            control[form] = {"installed_revision": "3.4.0", "suite": {k: s[k] for k in ("exit", "verdict", "fatal_error", "self_identity")},
                             "profile_100926": scrub({"exit": c2, "ok": js(o2).get("ok"), "errors": js(o2).get("errors")}, root),
                             "freeze_raw_recipe": {k: freeze(root / k, scratch / "freeze_raw.py") for k in ("flowmaster-validate", "change-flow")}}
            shutil.rmtree(root)
        receipt["control_3_4_0"] = control
        receipt["mutations"] = mutate(package, scratch, scratch / "new-plain")
    receipt["ok"] = (not receipt["quoted_vs_plain_differences"] and receipt["gcfpe_pass"]["quoted"]["ok"] and receipt["gcfpe_pass"]["plain"]["ok"]
                     and (roots_only or all(m["fired"] for m in receipt["mutations"].values())))
    print(json.dumps(receipt, indent=1, sort_keys=True))
    return 0 if receipt["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
