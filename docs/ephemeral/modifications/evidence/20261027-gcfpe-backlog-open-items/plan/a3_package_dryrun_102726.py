#!/usr/bin/env python3
"""A3's PLAN dry run of the four packages (MODIFICATION-20261027-gcfpe-backlog-open-items, PART-24; W7 Q6 in PLAN form).

  a3_package_dryrun_102726.py <installed-skills-root> <scratch> --a2 <A2 scratch dir> --map <stand-in map> [--receipt R]

<installed-skills-root> is read only (copied into <scratch>). Every build and run happens in <scratch>. Gates, each
reported by its own top-level flag (never inferred):

  G1 redlines        make_package_redlines_102726.py --check and --selftest; package_apply.py on scratch copies: every
                     op LANDED, a second application refused; the R-P1 conditional set lands once on top, a second
                     application refused, and it is refused on an unredlined base (it requires SR-W7-CF-04)
  G2 build           package_build_102726.py build on the stand-in inputs; --check byte-identical; --selftest
  G3 suite           validate_flowmaster.py --skills-root over all installed skills with the four built packages;
                     findings split into this change's and those the unchanged installed suite already reports. C-21:
                     ok when findings_from_this_change is empty and the findings on the unchanged and the built suite
                     alike are exactly the three named human-design-reading-flowmaster FMV-SKILL-STRUCTURE-001 ones
  G4 release         flowmaster-validate validate_gcfpe_20261027.py, run_gcfpe_20261027_fixtures.py; change-flow
                     validate_gcfpe_20261027.py; glow-hde-pr-development's validator; skill-creator quick_validate x4
  G5 contracts       contract_recipe.py --check on both bundled 102726.1 copies (Q5) and both bundled 100926.1 copies with
                     the patched regenerator (Q1)
  G6 injections      each new check fires on an injected regression: FMV-ORACLE-019 (A3-C2), FMV-ORACLE-020 (A3-C3),
                     OPTIONAL_REFERENCES (A3-C1), the new runner cases, the two change-flow fixture scenarios

Expected-pending vs real: values that only EXECUTE knows (the real successor ids and URLs, the real PLAN file, every
digest that depends on them) are stand-ins here; a check that fails only because of a stand-in is EXPECTED_PENDING.
Anything else is REAL. Writes only <scratch> and, with --receipt, that file. Run with PYTHONDONTWRITEBYTECODE=1.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
REPO = HERE.parents[5]
PACKAGES = ("change-flow", "flowmaster-validate", "glow-hde-pr-development", "glow-graph-contract")
ENV = {"PYTHONDONTWRITEBYTECODE": "1", "PATH": os.environ.get("PATH", "/usr/bin:/bin")}
CL05_PARENT = "3db4590a05eb81d59059eb6b95ed5fcf"  # W5 expected_parent_id (the HDE Change Flow hub; C-9)
# C-21: the three findings the unchanged installed suite already reports (pre-existing, outside every part)
PREEXISTING_C21 = {
    ("FMV-SKILL-STRUCTURE-001", "human-design-reading-flowmaster",
     "missing specialization contract: HUMAN_DESIGN_READING_SPECIALIZATION_REVISION: 1.0.1"),
    ("FMV-SKILL-STRUCTURE-001", "human-design-reading-flowmaster",
     "missing specialization contract: AUTHOR_SKILL_TARGET_SURFACE_UNAVAILABLE"),
    ("FMV-SKILL-STRUCTURE-001", "human-design-reading-flowmaster", "missing specialization contract: Original-session QA"),
}


def run(cmd, cwd=None, stdin=None) -> tuple[int, str, str]:
    p = subprocess.run([str(c) for c in cmd], cwd=cwd, capture_output=True, text=True, env=ENV, input=stdin)
    return p.returncode, p.stdout, p.stderr


def js(text: str):
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return None


def freeze(path: Path) -> str:
    rc, out, _ = run([sys.executable, REPO / "docs/prompt_ecosystem_management/freeze.py", path])
    return out.strip().splitlines()[-1] if rc == 0 and out.strip() else f"FREEZE_FAILED:{rc}"


def suite_findings(root: Path) -> tuple[int, dict | None]:
    rc, out, _ = run([sys.executable, "scripts/validate_flowmaster.py", "--skills-root", root], cwd=root / "flowmaster-validate")
    return rc, js(out)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("installed"); ap.add_argument("scratch")
    ap.add_argument("--a2", required=True); ap.add_argument("--map", required=True)
    ap.add_argument("--receipt")
    a = ap.parse_args()
    SK, W, A2 = Path(a.installed), Path(a.scratch).resolve(), Path(a.a2)
    if "/skills/synced/" in str(W):
        raise SystemExit("refusing to write under the synced install directory")
    W.mkdir(parents=True, exist_ok=True)
    rec: dict = {"record_type": "A3_PLAN_PACKAGE_RECEIPT", "modification": "MODIFICATION-20261027-gcfpe-backlog-open-items",
                 "worker": "A3", "date": "2026-10-27", "stand_in_used": True,
                 "stand_ins": ["successor map: " + str(Path(a.map).name) + " (each SUCCESSOR page id = its 100926.1 page id; "
                               "CL-05 = candidate 4054590a05eb8155b301e2cb6dec31d5)",
                               "PLAN file: A2's 116-byte scratch stand-in for PLAN-20261027.md",
                               "production contract and graph: A2's stand-in-map builds (their digests move in EXECUTE)"]}
    inst = W / "installed"
    if inst.exists():
        shutil.rmtree(inst)
    inst.mkdir()
    for d in sorted(SK.iterdir()):
        if d.is_dir():
            shutil.copytree(d, inst / d.name, ignore=shutil.ignore_patterns("__pycache__"))
    rec["base_digests"] = {k: freeze(inst / k) for k in PACKAGES}
    # ---------------------------------------------------------------------------------------------- G1
    g1: dict = {}
    rc, out, _ = run([sys.executable, HERE / "make_package_redlines_102726.py", "--check"])
    g1["redlines_file_reproduced"] = rc == 0 and (js(out) or {}).get("equal") is True
    rc, out, _ = run([sys.executable, HERE / "make_package_redlines_102726.py", "--selftest"])
    st = js(out) or {}
    g1["merge_selftest_ok"] = st.get("selftest_ok") is True
    g1["merge_selftest_rows"] = st.get("rows")
    ap_dir = W / "apply"
    if ap_dir.exists():
        shutil.rmtree(ap_dir)
    ap_dir.mkdir()
    for k in PACKAGES:
        shutil.copytree(inst / k, ap_dir / k)
    rc1, out1, _ = run([sys.executable, HERE / "package_apply.py", ap_dir])
    rc2, out2, _ = run([sys.executable, HERE / "package_apply.py", ap_dir])
    rc3, out3, _ = run([sys.executable, HERE / "package_apply.py", ap_dir, "--check"])
    r1, r2, r3 = js(out1) or {}, js(out2) or {}, js(out3) or {}
    doc = json.loads((HERE / "package-redlines.json").read_text(encoding="utf-8"))
    final_counts_ok = all((ap_dir / o["skill"] / o["file"]).read_text(encoding="utf-8").count(o["new"]) >= o["count"]
                          for o in doc["ops"])
    g1.update({"ops": len(doc["ops"]), "op_counts": doc["op_counts"],
               "first_apply_ok": rc1 == 0 and r1.get("written") is True and all(r["state"] == "UNTOUCHED" for r in r1.get("rows", [])),
               "second_apply_refused": rc2 != 0 and r2.get("written") is False,
               "every_op_landed": rc3 == 0 and all(r["state"] == "LANDED" for r in r3.get("rows", [])),
               "every_new_text_present_at_end": final_counts_ok,
               "regenerator_sha256": hashlib.sha256((ap_dir / "glow-graph-contract/scripts/regenerate_contract.py").read_bytes()).hexdigest()})
    rp = W / "rp1"
    if rp.exists():
        shutil.rmtree(rp)
    (rp / "tool").mkdir(parents=True)
    shutil.copytree(ap_dir, rp / "tree")
    shutil.copyfile(HERE / "package_apply.py", rp / "tool/package_apply.py")
    cond = next(s for s in doc["conditional_sets"] if s["set"] == "R-P1")
    (rp / "tool/package-redlines.json").write_text(json.dumps({"ops": cond["ops"]}), encoding="utf-8")
    c1 = run([sys.executable, rp / "tool/package_apply.py", rp / "tree"])
    c2 = run([sys.executable, rp / "tool/package_apply.py", rp / "tree"])
    (rp / "base").mkdir()
    for k in ("change-flow", "flowmaster-validate"):
        shutil.copytree(inst / k, rp / "base" / k)
    c3 = run([sys.executable, rp / "tool/package_apply.py", rp / "base"])
    g1["r_p1_default_excluded"] = not any(o["id"].startswith("RP1-") for o in doc["ops"])
    g1["r_p1_lands_once"] = c1[0] == 0 and c2[0] != 0
    g1["r_p1_refused_on_unredlined_base"] = c3[0] != 0 and (js(c3[1]) or {}).get("written") is False
    g1["ok"] = all(g1[k] for k in ("redlines_file_reproduced", "merge_selftest_ok", "first_apply_ok", "second_apply_refused",
                                   "every_op_landed", "every_new_text_present_at_end", "r_p1_default_excluded",
                                   "r_p1_lands_once", "r_p1_refused_on_unredlined_base"))
    rec["G1_redlines"] = g1
    # ---------------------------------------------------------------------------------------------- G2
    inputs = ["--production-contract", A2 / "contracts/gcfpe-20261027.1-102726.1-production-contract.json",
              "--production-graph-md", A2 / "production-102726.1.md", "--r1-dir", A2 / "r1",
              "--plan", A2 / "PLAN-20261027.standin.md", "--map", a.map, "--stand-in-ok"]
    build = W / "build"
    if build.exists():
        shutil.rmtree(build)
    env_tmp = {**ENV, "TMPDIR": str(W)}
    p = subprocess.run([sys.executable, HERE / "package_build_102726.py", "build", inst, build, *map(str, inputs)],
                       capture_output=True, text=True, env=env_tmp, cwd=W)
    b = js(p.stdout) or {}
    g2 = {"build_exit": p.returncode, "build_error": p.stderr.strip()[-400:] or None,
          "stand_in_used": b.get("stand_in_used"), "conditional_sets_applied": b.get("conditional_sets_applied"),
          "steps": [r for r in b.get("report", []) if "step" in r],
          "substitutions": sum(1 for r in b.get("report", []) if "substitution" in r)}
    p = subprocess.run([sys.executable, HERE / "package_build_102726.py", "check", inst, build, *map(str, inputs)],
                       capture_output=True, text=True, env=env_tmp, cwd=W)
    g2["check_byte_identical"] = p.returncode == 0 and (js(p.stdout) or {}).get("equal") is True
    p = subprocess.run([sys.executable, HERE / "package_build_102726.py", "selftest", inst, W, *map(str, inputs)],
                       capture_output=True, text=True, env=env_tmp, cwd=W)
    s = js(p.stdout) or {}
    g2["selftest_ok"] = p.returncode == 0 and s.get("selftest_ok") is True
    g2["selftest_rows"] = s.get("rows")
    g2["built_digests"] = {k: freeze(build / k) for k in PACKAGES}
    g2["ok"] = g2["build_exit"] == 0 and g2["check_byte_identical"] and g2["selftest_ok"]
    rec["G2_build"] = g2
    # ---------------------------------------------------------------------------------------------- G3
    base_suite, suite = W / "base-suite", W / "suite"
    for d in (base_suite, suite):
        if d.exists():
            shutil.rmtree(d)
        shutil.copytree(inst, d)
    for k in PACKAGES:
        shutil.rmtree(suite / k)
        shutil.copytree(build / k, suite / k)
    rcb, base_rep = suite_findings(base_suite)
    rcs, rep = suite_findings(suite)
    key = lambda f: (f["rule_id"], f["subject"].replace(str(base_suite), "<root>").replace(str(suite), "<root>"), f["evidence"])
    base_keys = {key(f) for f in (base_rep or {}).get("findings", [])}
    pre = [f for f in (rep or {}).get("findings", []) if key(f) in base_keys]
    new = [f for f in (rep or {}).get("findings", []) if key(f) not in base_keys]
    rec["G3_suite"] = {
        "baseline_installed_suite": {"exit": rcb, "suite_ok": (base_rep or {}).get("suite_ok"), "verdict": (base_rep or {}).get("verdict"),
                                     "findings": [{"rule_id": f["rule_id"], "skill": Path(f["subject"]).parent.name, "evidence": f["evidence"]}
                                                  for f in (base_rep or {}).get("findings", [])]},
        "built_suite": {"exit": rcs, "suite_ok": (rep or {}).get("suite_ok"), "verdict": (rep or {}).get("verdict"),
                        "self_identity": (rep or {}).get("self_identity"), "validator_revision": (rep or {}).get("validator_revision"),
                        "oracle_profile": (rep or {}).get("oracle_profile"),
                        "r1_coverage": {k: (rep or {}).get("change_contract_coverage", {}).get(k) for k in ("declared_rows", "expected_rows", "core_rows")},
                        "change_flow_fixtures_ok": ((rep or {}).get("fixtures") or {}).get("fixture_suite_ok"),
                        "change_flow_fixture_expectations": [((rep or {}).get("fixtures") or {}).get("passed_expectations"),
                                                             ((rep or {}).get("fixtures") or {}).get("failed_expectations")]},
        "findings_preexisting_in_installed_suite": len(pre),
        "findings_from_this_change": [{"rule_id": f["rule_id"], "evidence": f["evidence"][:300]} for f in new],
        "ok_except_preexisting": rep is not None and not new and (rep.get("suite_ok") is True or bool(pre)),
    }
    # C-21: the suite gate passes when findings_from_this_change is empty and the only findings, on the unchanged and
    # the built suite alike, are the three named pre-existing human-design-reading-flowmaster findings
    named = lambda r: sorted((f["rule_id"], Path(f["subject"]).parent.name, f["evidence"]) for f in (r or {}).get("findings", []))
    g3 = rec["G3_suite"]
    g3["c21_preexisting_named"] = [list(x) for x in sorted(PREEXISTING_C21)]
    g3["c21_unchanged_suite_findings_are_the_named_three"] = rep is not None and named(base_rep) == sorted(PREEXISTING_C21)
    g3["c21_built_suite_findings_are_the_named_three"] = rep is not None and named(rep) == sorted(PREEXISTING_C21)
    g3["suite_ok_flag"] = (rep or {}).get("suite_ok") is True
    g3["ok"] = (rep is not None and not new and g3["c21_unchanged_suite_findings_are_the_named_three"]
                and g3["c21_built_suite_findings_are_the_named_three"])
    g3["invariants_not_claimed"] = ("PAIR-001 (C-21): the invariants FMV-SKILL-STRUCTURE-001 covers for "
                                    "human-design-reading-flowmaster are not claimed")
    # ---------------------------------------------------------------------------------------------- G4
    cf, fv, pr = suite / "change-flow", suite / "flowmaster-validate", suite / "glow-hde-pr-development"
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
                                             "failed": [c["name"] for c in f.get("cases", []) if not c.get("passed")],
                                             "new_cases": sorted(c["name"] for c in f.get("cases", []) if c.get("name", "").startswith(
                                                 ("reject-qa-pass-straight", "reject-cl05", "reject-do-not-close", "reject-close-set",
                                                  "reject-doc20", "reject-member-version", "reject-kept-member", "reject-55",
                                                  "reject-merge-pending", "reject-old-r1", "reject-20260923", "reject-binding",
                                                  "accept-binding")))}
    rc, out, err = run([sys.executable, "scripts/validate_gcfpe_20261027.py"], cwd=cf)
    real = "staged_parent_id" in err
    g4["cf_validate_gcfpe_20261027"] = {"exit": rc, "pass_line": out.strip().startswith("PASS"),
                                         "error_tail": (err.strip().splitlines() or [""])[-1][:200],
                                         "classification": "REAL: the 102726.1 contract carries no member_registry.CL-05.staged_parent_id (A2's contract build)" if real else None}
    diag = W / "diag-cf"
    if diag.exists():
        shutil.rmtree(diag)
    shutil.copytree(cf, diag / "change-flow")
    dp = diag / "change-flow/references/gcfpe-20261027.1-102726.1-direct-handoff-contract.json"
    c = json.loads(dp.read_text(encoding="utf-8"))
    c["member_registry"]["CL-05"]["staged_parent_id"] = CL05_PARENT
    c["notion_page_manifest"]["CL-05"]["parent_id"] = CL05_PARENT
    dp.write_text(json.dumps(c, indent=2, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")
    rc, out, _ = run([sys.executable, "scripts/validate_gcfpe_20261027.py"], cwd=diag / "change-flow")
    g4["cf_validate_gcfpe_20261027_diagnostic_with_cl05_parent"] = {
        "note": "diagnostic only, not a gate: the same run on a scratch contract copy with only CL-05's two parent fields added",
        "exit": rc, "pass_line": out.strip().startswith("PASS")}
    rc, out, _ = run([sys.executable, "scripts/validate_glow_hde_pr_development.py"], cwd=pr)
    g4["glow_hde_pr_development_validator"] = {"exit": rc, "pass_line": out.strip().startswith("PASS")}
    qv = {}
    for k in PACKAGES:
        rc, out, _ = run([sys.executable, "-m", "scripts.quick_validate", build / k], cwd=suite / "skill-creator")
        qv[k] = {"exit": rc, "valid": "Skill is valid" in out}
    g4["skill_creator_quick_validate"] = qv
    g4["ok"] = (g4["fv_validate_gcfpe_20261027"]["ok"] is True and g4["fv_run_gcfpe_20261027_fixtures"]["fixture_suite_ok"] is True
                and g4["cf_validate_gcfpe_20261027"]["exit"] == 0 and g4["glow_hde_pr_development_validator"]["exit"] == 0
                and all(v["valid"] for v in qv.values()))
    rec["G4_release_validators"] = g4
    # ---------------------------------------------------------------------------------------------- G5
    T = REPO / "docs/graph/contract-template/gcfpe-20260914.1-091426.1-direct-handoff-contract-4.0.6.json"
    DR = REPO / "docs/prompt_ecosystem_management/gcfpe.decision-record.md"
    recipe = build / "glow-graph-contract/scripts/contract_recipe.py"
    g5 = {}
    for name, md, oracle, rev, prv, rv, rel in (
        ("Q5_102726_1", A2 / "production-102726.1.md", "glow-hde-canonical-change-flow-r1-20261027.json", "4.3.0", "1.5.0",
         A2 / "contracts/release-values-102726.1.filled.json", "gcfpe-20261027.1-102726.1-direct-handoff-contract.json"),
        ("Q1_100926_1", A2 / "graph-100926.1.md", "glow-hde-canonical-change-flow-r1-20260923.json", "4.2.0", "1.4.0",
         REPO / "docs/ephemeral/modifications/evidence/20261011-gcfpe-mb008-to-promotion/execute/contracts/release-values-100926.1.filled.json",
         "gcfpe-20261009.1-100926.1-direct-handoff-contract.json")):
        rc, out, _ = run([sys.executable, recipe, md, T, build / "flowmaster-validate/references" / oracle, DR, W / f"recipe-{name}.json",
                          "--contract-revision", rev, "--primary-skill-revision", prv, "--release-values", rv,
                          "--check", build / "change-flow/references" / rel, build / "flowmaster-validate/references" / rel], cwd=W)
        g5[name] = {"exit": rc, "equal_lines": out.count("EQUAL "), "different_lines": out.count("DIFFERENT")}
    g5["ok"] = all(v["exit"] == 0 and v["equal_lines"] == 2 for v in g5.values())
    rec["G5_contracts"] = g5
    # ---------------------------------------------------------------------------------------------- G6
    g6 = {}
    inj = W / "inject"

    def suite_copy(tag: str) -> Path:
        d = inj / tag
        if d.exists():
            shutil.rmtree(d)
        shutil.copytree(suite, d)
        return d

    def oracle_edit(tag: str, mutate) -> list:
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
    # the runner's new cases fail when the contract already carries the defect (each case also needs a clean contract)
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
    # ---------------------------------------------------------------------------------------------- summary
    rec["real_errors"] = ([x["rule_id"] + ": " + x["evidence"] for x in rec["G3_suite"]["findings_from_this_change"]]
                          + ([g4["cf_validate_gcfpe_20261027"]["classification"]] if g4["cf_validate_gcfpe_20261027"]["classification"] else [])
                          + ([] if g4["fv_validate_gcfpe_20261027"]["ok"] else ["fv validate_gcfpe_20261027: " + json.dumps(g4["fv_validate_gcfpe_20261027"]["errors"])])
                          + ([] if not g4["fv_run_gcfpe_20261027_fixtures"]["failed"] else ["runner: " + ", ".join(g4["fv_run_gcfpe_20261027_fixtures"]["failed"])]))
    rec["preexisting_outside_this_change"] = rec["G3_suite"]["baseline_installed_suite"]["findings"]
    rec["expected_pending"] = [
        "every digest that depends on the successor map's URLs or the real PLAN file (bundled contract and graph, profile, "
        "fixtures, validators, SKILL_TREE_SHA256, the four package digests): re-measured in EXECUTE",
        "body-level checks (prompt_body_checks_not_evaluated ALL_BODY_LEVEL_CHECKS; QA-closure body cases need QA-120, "
        "CL-E-10 and CL-C-10 bodies): A5 and x12 in EXECUTE",
    ]
    if a.receipt:
        Path(a.receipt).write_text(json.dumps(rec, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({k: (v.get("ok") if isinstance(v, dict) and "ok" in v else None) for k, v in rec.items() if k.startswith("G")}
                     | {"G3_ok_except_preexisting": rec["G3_suite"]["ok_except_preexisting"], "real_errors": rec["real_errors"]}, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
