#!/usr/bin/env python3
"""X13 (Q6, the four packages) for EXECUTE of MODIFICATION-20261027-gcfpe-backlog-open-items.

    x13_packages_102726.py <installed-skills-root> <work> --x10 <build-root> --x11 <dir> --x12 <dir> [--receipt R]

PLAN X13 on the real inputs, in the gate order of plan/a3_package_dryrun_102726.py (A3's PLAN form of Q6), with what
EXECUTE adds: the real PLAN-20261027.md, the real successor map, R-P1 (Nathan opted in: "with R-P1 and R-P2"),
packaging and extraction, the two skills-root copies of D28 (every name line quoted in one, plain in the other) and
freeze.py on every skill.

  inputs  <work>/a2: X12's production contract and filled release values, X11's production graph, X12's 100926.1
          graph build, and the R1 files from build_r1_successor_20261027.py --out-dir (identical to X10's Q2 output)
  G1      make_package_redlines_102726.py --check and --selftest; package_apply.py: every op LANDED once, a second
          application refused; the R-P1 set lands once on top, a second refused, refused on an unredlined base
  G2      execute/package_build_102726.py (a byte-identical copy of plan/package_build_102726.py, as its docstring
          says EXECUTE makes) build with --with-conditional R-P1; check byte-identical; selftest
  PKG     skill-creator quick_validate and package_skill for each package; each archive extracted; the extracted tree's
          freeze digest equals the built tree's
  ROOTS   two copies of the installed skills root with the four extracted packages: every skill's name line quoted in
          one, plain in the other. In each: G3 the suite (validate_flowmaster.py --skills-root; C-21: no finding from
          this change, and the unchanged and built suites carry exactly the three named pre-existing findings), G4 the
          release validators, G5 contract_recipe.py --check on both bundled 102726.1 copies (Q5) and both bundled
          100926.1 copies (Q1), and freeze.py on every skill. The two roots must give identical results and digests.
  G6      on the plain root, each new check fires on its injected regression

Writes only under <work> and, with --receipt, that file; the installed tree is only read. Prints a JSON summary.
Run with PYTHONDONTWRITEBYTECODE=1.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
PLAN = HERE.parent / "plan"
REPO = HERE.parents[5]
MAP = HERE / "successor-pages-102726.1.json"
PLAN_FILE = HERE.parent / "PLAN-20261027.md"
PACKAGES = ("change-flow", "flowmaster-validate", "glow-hde-pr-development", "glow-graph-contract")
ENV = {"PYTHONDONTWRITEBYTECODE": "1", "PATH": os.environ.get("PATH", "/usr/bin:/bin")}
PREEXISTING_C21 = {
    ("FMV-SKILL-STRUCTURE-001", "human-design-reading-flowmaster",
     "missing specialization contract: HUMAN_DESIGN_READING_SPECIALIZATION_REVISION: 1.0.1"),
    ("FMV-SKILL-STRUCTURE-001", "human-design-reading-flowmaster",
     "missing specialization contract: AUTHOR_SKILL_TARGET_SURFACE_UNAVAILABLE"),
    ("FMV-SKILL-STRUCTURE-001", "human-design-reading-flowmaster", "missing specialization contract: Original-session QA"),
}
PLAIN_RE = re.compile(rb"(?m)\A(---\r?\n(?:(?!---).*\r?\n)*?)name:([ \t]*)([a-z0-9-]+)([ \t]*\r?)$")
QUOTED_RE = re.compile(rb"(?m)\A(---\r?\n(?:(?!---).*\r?\n)*?)name:([ \t]*)([\"'])([a-z0-9-]+)\3([ \t]*\r?)$")


def run(cmd, cwd=None, extra=None):
    p = subprocess.run([str(c) for c in cmd], cwd=cwd, capture_output=True, text=True, env={**ENV, **(extra or {})})
    return p.returncode, p.stdout, p.stderr


def js(text):
    try:
        return json.loads(text)
    except (json.JSONDecodeError, TypeError):
        return None


def freeze(path: Path) -> str:
    rc, out, _ = run([sys.executable, REPO / "docs/prompt_ecosystem_management/freeze.py", path])
    return out.strip().splitlines()[-1] if rc == 0 and out.strip() else f"FREEZE_FAILED:{rc}"


def suite_findings(root: Path):
    rc, out, _ = run([sys.executable, "scripts/validate_flowmaster.py", "--skills-root", root], cwd=root / "flowmaster-validate")
    return rc, js(out)


def copytree(src: Path, dst: Path):
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst, ignore=shutil.ignore_patterns("__pycache__"))


def set_name_lines(root: Path, form: str) -> dict:
    """D28: every skill's SKILL.md name line in one form (quoted as Save skill writes it, or plain)."""
    changed = 0
    for sk in sorted(root.iterdir()):
        f = sk / "SKILL.md"
        if not f.is_file():
            continue
        data = f.read_bytes()
        new = PLAIN_RE.sub(rb'\1name:\2"\3"\4', data, count=1) if form == "quoted" else QUOTED_RE.sub(rb"\1name:\2\4\5", data, count=1)
        if new != data:
            f.write_bytes(new)
            changed += 1
    forms = {}
    for sk in sorted(root.iterdir()):
        f = sk / "SKILL.md"
        if f.is_file():
            m = re.search(rb"(?m)^name:.*$", f.read_bytes())
            forms[sk.name] = "quoted" if m and (b'"' in m.group(0) or b"'" in m.group(0)) else "plain"
    return {"changed": changed, "all_in_form": all(v == form for v in forms.values()), "skills": len(forms)}


def strip_paths(obj, roots):
    s = json.dumps(obj, sort_keys=True, ensure_ascii=False)
    for r in roots:
        s = s.replace(str(r), "<root>")
    return json.loads(s)


def root_gates(root: Path, base: Path, build: Path, a2: Path, work: Path) -> dict:
    """G3, G4, G5 and freeze on one skills root (the built packages extracted in), against its unchanged twin `base`."""
    g: dict = {}
    rcb, base_rep = suite_findings(base)
    rcs, rep = suite_findings(root)
    key = lambda f: (f["rule_id"], Path(f["subject"]).parent.name, f["evidence"])
    base_keys = {key(f) for f in (base_rep or {}).get("findings", [])}
    new = [f for f in (rep or {}).get("findings", []) if key(f) not in base_keys]
    named = lambda r: sorted(key(f) for f in (r or {}).get("findings", []))
    g["G3_suite"] = {
        "baseline_exit": rcb, "built_exit": rcs, "built_verdict": (rep or {}).get("verdict"),
        "validator_revision": (rep or {}).get("validator_revision"), "oracle_profile": (rep or {}).get("oracle_profile"),
        "r1_coverage": {k: (rep or {}).get("change_contract_coverage", {}).get(k) for k in ("declared_rows", "expected_rows", "core_rows")},
        "change_flow_fixtures_ok": ((rep or {}).get("fixtures") or {}).get("fixture_suite_ok"),
        "findings_from_this_change": [{"rule_id": f["rule_id"], "evidence": f["evidence"][:300]} for f in new],
        "c21_unchanged_suite_findings_are_the_named_three": named(base_rep) == sorted(PREEXISTING_C21),
        "c21_built_suite_findings_are_the_named_three": named(rep) == sorted(PREEXISTING_C21)}
    g["G3_suite"]["ok"] = (rep is not None and not new and g["G3_suite"]["c21_unchanged_suite_findings_are_the_named_three"]
                           and g["G3_suite"]["c21_built_suite_findings_are_the_named_three"])
    cf, fv, pr = root / "change-flow", root / "flowmaster-validate", root / "glow-hde-pr-development"
    cpath = cf / "references/gcfpe-20261027.1-102726.1-direct-handoff-contract.json"
    g4: dict = {}
    rc, out, _ = run([sys.executable, "scripts/validate_gcfpe_20261027.py", cf, "--contract", cpath], cwd=fv)
    v = js(out) or {}
    g4["fv_validate_gcfpe_20261027"] = {"exit": rc, "ok": v.get("ok"), "errors": v.get("errors"),
                                         "frozen_graph_node_count": v.get("frozen_graph_node_count"),
                                         "frozen_graph_edge_count": v.get("frozen_graph_edge_count"),
                                         "prompt_body_checks_not_evaluated": v.get("prompt_body_checks_not_evaluated")}
    rc, out, _ = run([sys.executable, "scripts/run_gcfpe_20261027_fixtures.py", cf, "--contract", cpath], cwd=fv)
    f = js(out) or {}
    g4["fv_run_gcfpe_20261027_fixtures"] = {"exit": rc, "fixture_suite_ok": f.get("fixture_suite_ok"), "case_count": f.get("case_count"),
                                             "section_13": [f.get("section_13_passed"), f.get("section_13_fixture_count")],
                                             "failed": [c["name"] for c in f.get("cases", []) if not c.get("passed")]}
    rc, out, err = run([sys.executable, "scripts/validate_gcfpe_20261027.py"], cwd=cf)
    g4["cf_validate_gcfpe_20261027"] = {"exit": rc, "pass_line": out.strip().startswith("PASS"),
                                         "error_tail": (err.strip().splitlines() or [""])[-1][:200]}
    rc, out, _ = run([sys.executable, "scripts/validate_glow_hde_pr_development.py"], cwd=pr)
    g4["glow_hde_pr_development_validator"] = {"exit": rc, "pass_line": out.strip().startswith("PASS")}
    qv = {}
    for k in PACKAGES:
        rc, out, _ = run([sys.executable, "-m", "scripts.quick_validate", root / k], cwd=root / "skill-creator")
        qv[k] = {"exit": rc, "valid": "Skill is valid" in out}
    g4["skill_creator_quick_validate"] = qv
    g4["ok"] = (g4["fv_validate_gcfpe_20261027"]["ok"] is True and g4["fv_run_gcfpe_20261027_fixtures"]["fixture_suite_ok"] is True
                and g4["cf_validate_gcfpe_20261027"]["exit"] == 0 and g4["cf_validate_gcfpe_20261027"]["pass_line"]
                and g4["glow_hde_pr_development_validator"]["exit"] == 0 and all(x["valid"] for x in qv.values()))
    g["G4_release_validators"] = g4
    T = REPO / "docs/graph/contract-template/gcfpe-20260914.1-091426.1-direct-handoff-contract-4.0.6.json"
    DR = REPO / "docs/prompt_ecosystem_management/gcfpe.decision-record.md"
    recipe = root / "glow-graph-contract/scripts/contract_recipe.py"
    g5 = {}
    for name, md, oracle, rev, prv, rv, rel in (
        ("Q5_102726_1", a2 / "production-102726.1.md", "glow-hde-canonical-change-flow-r1-20261027.json", "4.3.0", "1.5.0",
         a2 / "contracts/release-values-102726.1.filled.json", "gcfpe-20261027.1-102726.1-direct-handoff-contract.json"),
        ("Q1_100926_1", a2 / "graph-100926.1.md", "glow-hde-canonical-change-flow-r1-20260923.json", "4.2.0", "1.4.0",
         REPO / "docs/ephemeral/modifications/evidence/20261011-gcfpe-mb008-to-promotion/execute/contracts/release-values-100926.1.filled.json",
         "gcfpe-20261009.1-100926.1-direct-handoff-contract.json")):
        out_json = work / f"recipe-{root.name}-{name}.json"
        rc, out, _ = run([sys.executable, recipe, md, T, root / "flowmaster-validate/references" / oracle, DR, out_json,
                          "--contract-revision", rev, "--primary-skill-revision", prv, "--release-values", rv,
                          "--check", root / "change-flow/references" / rel, root / "flowmaster-validate/references" / rel],
                         cwd=REPO, extra={"TMPDIR": str(work)})
        g5[name] = {"exit": rc, "equal_lines": out.count("EQUAL "), "different_lines": out.count("DIFFERENT"),
                    "sha256": hashlib.sha256(out_json.read_bytes()).hexdigest() if out_json.exists() else None}
    g5["ok"] = all(x["exit"] == 0 and x["equal_lines"] == 2 for x in g5.values())
    g["G5_contracts"] = g5
    g["freeze"] = {p.name: freeze(p) for p in sorted(root.iterdir()) if p.is_dir()}
    g["ok"] = g["G3_suite"]["ok"] and g4["ok"] and g5["ok"]
    return g


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("installed"); ap.add_argument("work")
    ap.add_argument("--x10", required=True); ap.add_argument("--x11", required=True); ap.add_argument("--x12", required=True)
    ap.add_argument("--receipt")
    a = ap.parse_args()
    SK, W = Path(a.installed), Path(a.work).resolve()
    if "/skills/synced/" in str(W):
        raise SystemExit("refusing to write under the synced install directory")
    if W.exists():
        shutil.rmtree(W)
    W.mkdir(parents=True)
    rec: dict = {"record_type": "X13_PACKAGE_RECEIPT", "modification": "MODIFICATION-20261027-gcfpe-backlog-open-items",
                 "stand_in_used": False, "with_conditional": ["R-P1"]}
    inst = W / "installed"
    inst.mkdir()
    for d in sorted(SK.iterdir()):
        if d.is_dir():
            shutil.copytree(d, inst / d.name, ignore=shutil.ignore_patterns("__pycache__"))
    rec["base_digests"] = {k: freeze(inst / k) for k in PACKAGES}
    # ---------------------------------------------------------------------------------------------- inputs
    a2 = W / "a2"
    (a2 / "contracts").mkdir(parents=True)
    x12c = Path(a.x12) / "contracts"
    shutil.copyfile(x12c / "gcfpe-20261027.1-102726.1-production-contract.json", a2 / "contracts/gcfpe-20261027.1-102726.1-production-contract.json")
    shutil.copyfile(HERE / "contracts/release-values-102726.1.filled.json", a2 / "contracts/release-values-102726.1.filled.json")
    shutil.copyfile(Path(a.x11) / "production-102726.1.md", a2 / "production-102726.1.md")
    shutil.copyfile(x12c / "graph-100926.1.md", a2 / "graph-100926.1.md")
    (a2 / "r1").mkdir()
    rc, out, err = run([sys.executable, HERE.parent / "build_r1_successor_20261027.py", inst, REPO, "--out-dir", a2 / "r1",
                        "--expect-decision-record", REPO / "docs/prompt_ecosystem_management/gcfpe.decision-record.md"])
    r1 = js(out) or {}
    x10 = Path(a.x10)
    same_as_q2 = all((a2 / "r1" / f"{kind}-{p.name}").read_bytes() == p.read_bytes() for kind, p in (   # --out-dir prefixes the kind
        ("matrix", x10 / "flowmaster-validate/references/r1-successor-source-20261027.md"),
        ("oracle", x10 / "flowmaster-validate/references/glow-hde-canonical-change-flow-r1-20261027.json"),
        ("map", x10 / "change-flow/references/glow-hde-canonical-change-flow-r1-runtime-map-20261027.json")))
    rec["inputs"] = {"r1_out_dir_exit": rc, "r1_decision_record_match": r1.get("decision_record_match"),
                     "r1_files_equal_x10_q2": same_as_q2,
                     "production_contract_sha256": hashlib.sha256((a2 / "contracts/gcfpe-20261027.1-102726.1-production-contract.json").read_bytes()).hexdigest(),
                     "production_graph_sha256": hashlib.sha256((a2 / "production-102726.1.md").read_bytes()).hexdigest(),
                     "plan_sha256": hashlib.sha256(PLAN_FILE.read_bytes()).hexdigest()}
    # ---------------------------------------------------------------------------------------------- G1
    g1: dict = {}
    rc, out, _ = run([sys.executable, PLAN / "make_package_redlines_102726.py", "--check"])
    g1["redlines_file_reproduced"] = rc == 0 and (js(out) or {}).get("equal") is True
    rc, out, _ = run([sys.executable, PLAN / "make_package_redlines_102726.py", "--selftest"])
    g1["merge_selftest_ok"] = (js(out) or {}).get("selftest_ok") is True
    ap_dir = W / "apply"
    ap_dir.mkdir()
    for k in PACKAGES:
        shutil.copytree(inst / k, ap_dir / k)
    rc1, out1, _ = run([sys.executable, PLAN / "package_apply.py", ap_dir])
    rc2, out2, _ = run([sys.executable, PLAN / "package_apply.py", ap_dir])
    rc3, out3, _ = run([sys.executable, PLAN / "package_apply.py", ap_dir, "--check"])
    r1j, r2j, r3j = js(out1) or {}, js(out2) or {}, js(out3) or {}
    doc = json.loads((PLAN / "package-redlines.json").read_text(encoding="utf-8"))
    g1.update({"ops": len(doc["ops"]),
               "first_apply_ok": rc1 == 0 and r1j.get("written") is True and all(r["state"] == "UNTOUCHED" for r in r1j.get("rows", [])),
               "second_apply_refused": rc2 != 0 and r2j.get("written") is False,
               "every_op_landed": rc3 == 0 and all(r["state"] == "LANDED" for r in r3j.get("rows", []))})
    rp = W / "rp1"
    (rp / "tool").mkdir(parents=True)
    shutil.copytree(ap_dir, rp / "tree")
    shutil.copyfile(PLAN / "package_apply.py", rp / "tool/package_apply.py")
    cond = next(s for s in doc["conditional_sets"] if s["set"] == "R-P1")
    (rp / "tool/package-redlines.json").write_text(json.dumps({"ops": cond["ops"]}), encoding="utf-8")
    c1 = run([sys.executable, rp / "tool/package_apply.py", rp / "tree"])
    c2 = run([sys.executable, rp / "tool/package_apply.py", rp / "tree"])
    (rp / "base").mkdir()
    for k in ("change-flow", "flowmaster-validate"):
        shutil.copytree(inst / k, rp / "base" / k)
    c3 = run([sys.executable, rp / "tool/package_apply.py", rp / "base"])
    g1["r_p1_ops"] = len(cond["ops"])
    g1["r_p1_lands_once"] = c1[0] == 0 and c2[0] != 0
    g1["r_p1_refused_on_unredlined_base"] = c3[0] != 0 and (js(c3[1]) or {}).get("written") is False
    g1["ok"] = all(g1[k] for k in ("redlines_file_reproduced", "merge_selftest_ok", "first_apply_ok", "second_apply_refused",
                                   "every_op_landed", "r_p1_lands_once", "r_p1_refused_on_unredlined_base"))
    rec["G1_redlines"] = g1
    # ---------------------------------------------------------------------------------------------- G2
    pb = HERE / "package_build_102726.py"
    src = PLAN / "package_build_102726.py"
    if not pb.exists():
        shutil.copyfile(src, pb)
    inputs = ["--production-contract", a2 / "contracts/gcfpe-20261027.1-102726.1-production-contract.json",
              "--production-graph-md", a2 / "production-102726.1.md", "--r1-dir", a2 / "r1",
              "--plan", PLAN_FILE, "--map", MAP, "--with-conditional", "R-P1"]
    build = W / "build"
    env_tmp = {"TMPDIR": str(W)}
    rc, out, err = run([sys.executable, pb, "build", inst, build, *inputs], cwd=W, extra=env_tmp)
    b = js(out) or {}
    g2 = {"package_build_copy_byte_identical_to_plan": pb.read_bytes() == src.read_bytes(),
          "build_exit": rc, "build_error": err.strip()[-400:] or None, "stand_in_used": b.get("stand_in_used"),
          "conditional_sets_applied": b.get("conditional_sets_applied"),
          "substitutions": sum(1 for r in b.get("report", []) if "substitution" in r)}
    rc, out, _ = run([sys.executable, pb, "check", inst, build, *inputs], cwd=W, extra=env_tmp)
    g2["check_byte_identical"] = rc == 0 and (js(out) or {}).get("equal") is True
    rc, out, _ = run([sys.executable, pb, "selftest", inst, W / "pb-selftest", *inputs], cwd=W, extra=env_tmp)
    s = js(out) or {}
    g2["selftest_ok"] = rc == 0 and s.get("selftest_ok") is True
    g2["selftest_false"] = [k for k, v in (s.get("rows") or {}).items() if v is False]
    # One self-test case needs a stand-in map by construction: it drops --stand-in-ok and expects the build to stop,
    # which only a stand-in map can make it do. X4b recorded it so; it passed on the stand-in map in A3's PLAN receipt.
    a3 = json.loads((PLAN / "receipts-A3/A3-packages-102726.1.json").read_text(encoding="utf-8"))["G2_build"]
    stand_in_only = {"stops_on_stand_in_map_without_flag"}
    g2["selftest_not_applicable_real_map"] = {
        k: "NOT_APPLICABLE_REAL_MAP (true on the stand-in map, plan/receipts-A3/A3-packages-102726.1.json)"
        for k in g2["selftest_false"] if k in stand_in_only and (a3.get("selftest_rows") or {}).get(k) is True}
    g2["selftest_ok_on_real_map"] = (g2["selftest_ok"] or (set(g2["selftest_false"]) == set(g2["selftest_not_applicable_real_map"])
                                                          and bool(g2["selftest_false"])))
    g2["built_digests"] = {k: freeze(build / k) for k in PACKAGES}
    g2["ok"] = (g2["package_build_copy_byte_identical_to_plan"] and g2["build_exit"] == 0 and g2["check_byte_identical"]
                and g2["selftest_ok_on_real_map"] and g2["stand_in_used"] is False)
    rec["G2_build"] = g2
    if not g2["ok"]:
        rec["ok"] = False
        if a.receipt:
            Path(a.receipt).write_text(json.dumps(strip_paths(rec, [W]), indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        print(json.dumps(strip_paths(rec, [W]), indent=1, ensure_ascii=False))
        return 1
    # ---------------------------------------------------------------------------------------------- PKG
    dist, ext = W / "dist", W / "extracted"
    dist.mkdir(); ext.mkdir()
    pkg = {}
    for k in PACKAGES:
        rq, oq, _ = run([sys.executable, "-m", "scripts.quick_validate", build / k], cwd=inst / "skill-creator")
        rp_, op_, ep_ = run([sys.executable, "-m", "scripts.package_skill", build / k, dist], cwd=inst / "skill-creator")
        arc = dist / f"{k}.skill"
        row = {"quick_validate_valid": "Skill is valid" in oq, "package_exit": rp_, "archive": arc.name if arc.exists() else None}
        if arc.exists():
            row["skill_sha256"] = hashlib.sha256(arc.read_bytes()).hexdigest()
            row["skill_bytes"] = arc.stat().st_size
            with zipfile.ZipFile(arc) as z:
                z.extractall(ext)
            row["extracted_freeze"] = freeze(ext / k)
            row["built_freeze"] = g2["built_digests"][k]
            row["extracted_equals_built"] = row["extracted_freeze"] == row["built_freeze"]
        pkg[k] = row
    rec["packages"] = pkg
    rec["packages_ok"] = all(r.get("quick_validate_valid") and r.get("package_exit") == 0 and r.get("extracted_equals_built") for r in pkg.values())
    # ---------------------------------------------------------------------------------------------- ROOTS (D28)
    roots = {}
    for form in ("quoted", "plain"):
        base, root = W / f"base-{form}", W / f"root-{form}"
        copytree(inst, base)
        copytree(inst, root)
        for k in PACKAGES:
            shutil.rmtree(root / k)
            shutil.copytree(ext / k, root / k)
        nb, nr = set_name_lines(base, form), set_name_lines(root, form)
        g = root_gates(root, base, build, a2, W)
        g["name_lines"] = {"base": nb, "root": nr}
        roots[form] = g
    q, p = strip_paths(roots["quoted"], [W / "root-quoted", W / "base-quoted"]), strip_paths(roots["plain"], [W / "root-plain", W / "base-plain"])
    for x in (q, p):
        x.pop("name_lines", None)
    rec["roots"] = {f: {k: v for k, v in g.items()} for f, g in roots.items()}
    rec["quoted_vs_plain"] = {"gates_identical": {k: q[k] == p[k] for k in q if k != "freeze"},
                              "freeze_identical": q["freeze"] == p["freeze"],
                              "freeze_differences": sorted(k for k in q["freeze"] if q["freeze"][k] != p["freeze"].get(k))}
    rec["roots_ok"] = (roots["quoted"]["ok"] and roots["plain"]["ok"] and all(rec["quoted_vs_plain"]["gates_identical"].values())
                       and rec["quoted_vs_plain"]["freeze_identical"])
    # ---------------------------------------------------------------------------------------------- G6
    suite = W / "root-plain"
    inj = W / "inject"
    g6 = {}

    def suite_copy(tag):
        d = inj / tag
        copytree(suite, d)
        return d

    def oracle_edit(tag, mutate):
        d = suite_copy(tag)
        op = d / "flowmaster-validate/references/glow-hde-canonical-change-flow-r1-20261027.json"
        o = json.loads(op.read_text(encoding="utf-8"))
        mutate(o)
        op.write_text(json.dumps(o, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        _, r = suite_findings(d)
        shutil.rmtree(d)
        return [(f["rule_id"], f["evidence"]) for f in (r or {}).get("findings", [])]

    def move_close_row(o):
        rows = o["runtime_rows"]
        i = next(k for k, r in enumerate(rows) if r["id"] == "GCF-24.CLOSE")
        row = rows.pop(i)
        j = next(k for k, r in enumerate(rows) if r["id"] == "GCF-25")
        rows.insert(j + 1, row)
    f = oracle_edit("c2", move_close_row)
    g6["A3_C2_added_row_out_of_place_fires_FMV_ORACLE_019"] = any(r == "FMV-ORACLE-019" and "added successor row" in e for r, e in f)

    def bad_token(o):
        o["required_global_tokens"] = [t.replace("47/47", "46/46") for t in o["required_global_tokens"]]
    f = oracle_edit("c3", bad_token)
    g6["A3_C3_coverage_token_fires_FMV_ORACLE_020"] = any(r == "FMV-ORACLE-020" and "required_global_tokens" in e for r, e in f)
    d = suite_copy("c1")
    sp = d / "change-flow/SKILL.md"
    sp.write_text(sp.read_text(encoding="utf-8").replace(
        "references/gcfpe-20261027.1-102726.1-direct-handoff-contract.json)", "references/gcfpe-20261009.1-100926.1-direct-handoff-contract.json)", 1), encoding="utf-8")
    _, r = suite_findings(d)
    shutil.rmtree(d)
    g6["A3_C1_link_to_superseded_contract_fires"] = any("unapproved reference-file dependency" in x["evidence"] for x in (r or {}).get("findings", []))
    d = suite_copy("fx")
    fx = d / "flowmaster-validate/fixtures/change-flow/scenarios.json"
    fx.write_text(fx.read_text(encoding="utf-8").replace('"id": "negative_qa_report_skips_close_stage",\n      "expected_pass": false,',
                                                         '"id": "negative_qa_report_skips_close_stage",\n      "expected_pass": true,', 1), encoding="utf-8")
    _, r = suite_findings(d)
    shutil.rmtree(d)
    g6["change_flow_close_stage_negative_is_a_real_failure"] = ((r or {}).get("fixtures") or {}).get("fixture_suite_ok") is False
    d = suite_copy("runner")
    cp = d / "change-flow/references/gcfpe-20261027.1-102726.1-direct-handoff-contract.json"
    c = json.loads(cp.read_text(encoding="utf-8"))
    c["artifact_availability_contract"]["stage_categories"]["CL-05"] = "POST_CLOSURE"
    cp.write_text(json.dumps(c, indent=2, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")
    rc, out, _ = run([sys.executable, "scripts/run_gcfpe_20261027_fixtures.py", d / "change-flow", "--contract", cp], cwd=d / "flowmaster-validate")
    fr = js(out) or {}
    failed = {x["name"] for x in fr.get("cases", []) if not x.get("passed")}
    shutil.rmtree(d)
    g6["runner_case_fails_on_defective_base"] = rc != 0 and "reject-close-set-as-post-closure" in failed
    g6["ok"] = all(v for v in g6.values())
    rec["G6_injections"] = g6
    shutil.rmtree(inj, ignore_errors=True)
    rec["ok"] = (g1["ok"] and g2["ok"] and rec["packages_ok"] and rec["roots_ok"] and g6["ok"]
                 and rec["inputs"]["r1_files_equal_x10_q2"] and rec["inputs"]["r1_decision_record_match"] is True)
    out_rec = strip_paths(rec, [W])
    if a.receipt:
        Path(a.receipt).write_text(json.dumps(out_rec, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    summary = {k: (v.get("ok") if isinstance(v, dict) and "ok" in v else v) for k, v in out_rec.items()
               if k in ("G1_redlines", "G2_build", "packages_ok", "roots_ok", "G6_injections", "ok")}
    print(json.dumps(summary, indent=1))
    return 0 if rec["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
