#!/usr/bin/env python3
"""PLAN successor dry run (D26-A step 1) for MODIFICATION-20261010-gcfpe-candidate-skill-analysis.

Re-runnable evidence, not a gate implementation. Read-only against the repository and the installed
skills: it copies the installed skills it needs into SCRATCH, runs every gate of the dated plan's
normal path that can run without repaired bytes, and prints one JSON receipt on stdout. It writes
only under SCRATCH. Native Notion page checks are separate (plan-successor-native-checks.json).

Usage, from the repository root:

    PYTHONDONTWRITEBYTECODE=1 python3 \
      docs/ephemeral/modifications/evidence/20261010-gcfpe-candidate-skill-analysis/plan-successor-dry-run.py \
      <installed-skills-root> <scratch-dir> > <receipts.json>

<installed-skills-root> is the synced skill bucket (one directory per skill). It is never written.
"""
from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path

MOD = "MODIFICATION-20261010-gcfpe-candidate-skill-analysis"
RECORD = f"docs/ephemeral/modifications/{MOD}.md"
FREEZE = "docs/prompt_ecosystem_management/freeze.py"
REGISTRY = "docs/prompt_ecosystem_management/project-prompt-contract-registry.md"
SELECTED_PARTS = "docs/graph/parts"
CANDIDATE_PARTS = ("docs/ephemeral/modifications/evidence/20261009-gcfpe-latest-alpha-analysis/"
                   "execute/candidate-graph-parts")
TEMPLATE = "docs/graph/contract-template/gcfpe-20260914.1-091426.1-direct-handoff-contract-4.0.6.json"
CONTRACT = "references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json"
DECISIONS = "docs/prompt_ecosystem_management/gcfpe.decision-record.md"

# Expected per-skill freeze output (freeze.py), and the repository record that binds it.
EXPECTED = {
    "change-flow": ("22 9a551af36e042e56a48045297ac316b4102a4eb21f31622853c8be700e223f47",
                    "source-identities.md (supplied archive); closeout-residuals execute/installed_freeze.txt"),
    "flowmaster-validate": ("31 90c15e985a0c4b78d24298fe8187e8a50576689ddfc509d09fa11187ab97fcc2",
                            "source-identities.md (supplied archive); tw1 packages-tw1.json by skill_tree_digest"),
    "glow-hde-pr-development": ("4 265f9170d8459fc477287c320f0bbdd8eaaf0e6ba1dd4ee513275a76a22f8f7a",
                                "source-identities.md (supplied archive); closeout-residuals installed_freeze.txt"),
    "flowmaster-primary": ("2 2d41da26a39de98af02ad65e0f2818732fc0930e87223cb90ef75a2dc9e977e6",
                           "source-identities.md (supplied archive)"),
    "typesafe-scoring": ("3 088c77f36ae96bcb9a1bcbdd9b1b8ee58272175094b0f3208b5337a3ce4881f5",
                         "source-identities.md (supplied archive)"),
    "glow-graph-contract": ("9 e241bb9a67c4470895fc666a25d0f97d8df7e8e2df06539de5deaf12bc46467c",
                            "closeout-residuals installed_freeze.txt; cr1 SKILL_FIT_CONFIRMED x2"),
    "session-relay-flowmaster": ("5 c8a5b22432a44f57fb12bc508169f85aa3d0ca3298b793590c364eb9a2afc8e4",
                                 "closeout-residuals installed_freeze.txt; cr1 SKILL_FIT_CONFIRMED x2"),
    "amthor-workspace-governance-audit": ("15 c214e8741e9c54d395cfbd1379cbc7947e6c07beee5bd03aca433dc5dda937ab",
                                          "closeout-residuals installed_freeze.txt; cr1 SKILL_FIT_CONFIRMED x2"),
    "tw-flowmaster": ("2 0581205ba29f195ce784ff585ca9019de5644750c9e357b06e377e91827a722c",
                      "gtwpe-tw-model-advice packages-tw1.json; tw1 SKILL_FIT_CONFIRMED x2"),
    "session-branch-flowmaster": ("2 17b5800b35d352216eb6ea7708fa4058400f66dd7d908debbea16fa9154b3008",
                                  "NO repository verdict; accepted only by flowmaster-validate 3.3.2 suite pins"),
    "skill-creator": ("18 e4fee9c98c4f3941916fd9005ea9e8bec6bc1adc1aae85380f0150febbdf6ebe",
                      "governed packaging mechanism (skill-packaging-and-delivery.md); no verdict expected"),
}
# Supplied, analysed, but not installed identically in this environment: recorded, never substituted.
SUPPLIED_NOT_INSTALLED = {
    "glow-merged-change-attribution-lock": "11 ee253cfaf844a5ce28da3646e469d3a926167ecb3898e5dc205b0365dc946a8e",
    "flowmaster-propagate": "3 6297d67ad34ae0b33c1a31c29d32eef4db6156537c7b101469d499309e326ddf",
}
TW1_FV_TREE_DIGEST = "284b3ac150bedb51054aa9b3d0ce7ddfc1679d29dfb4178ded6095022d1fd733"


def run(argv: list[str], cwd: str | None = None, env: dict | None = None) -> dict:
    p = subprocess.run(argv, cwd=cwd, env=env, capture_output=True, text=True)
    return {"argv": argv, "cwd": cwd or ".", "exit_code": p.returncode, "stdout": p.stdout, "stderr": p.stderr}


def freeze(path: Path, env: dict) -> str:
    return run([sys.executable, FREEZE, str(path)], env=env)["stdout"].strip()


def main() -> int:
    installed, scratch = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve()
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TMPDIR=str(scratch / "tmp"))
    for d in ("skills-root", "build", "tmp", "pkg"):
        (scratch / d).mkdir(parents=True, exist_ok=True)
    sr = scratch / "skills-root"
    out: dict = {"record_type": "PLAN_SUCCESSOR_DRY_RUN", "modification": MOD,
                 "date_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                 "repository_head": run(["git", "rev-parse", "HEAD"])["stdout"].strip(),
                 "origin_main": run(["git", "rev-parse", "origin/main"])["stdout"].strip(), "gates": {}}
    g = out["gates"]

    # G1 identities: installed bytes, scratch copy fidelity, and the record that binds each.
    ident = []
    for name, (expected, binding) in EXPECTED.items():
        src = installed / name
        row = {"skill": name, "expected": expected, "binding": binding}
        if not src.is_dir():
            row.update(installed=None, matches_expected=False)
        else:
            shutil.rmtree(sr / name, ignore_errors=True)
            shutil.copytree(src, sr / name, symlinks=True)
            row["installed"] = freeze(src, env)
            row["scratch_copy"] = freeze(sr / name, env)
            row["matches_expected"] = row["installed"] == expected
            row["copy_faithful"] = row["scratch_copy"] == row["installed"]
        ident.append(row)
    for name, supplied in SUPPLIED_NOT_INSTALLED.items():
        src = installed / name
        ident.append({"skill": name, "supplied_analysed": supplied,
                      "installed": freeze(src, env) if src.is_dir() else None,
                      "note": "not a repair target; never substituted for the supplied archive"})
    sys.path.insert(0, str(sr / "flowmaster-validate" / "scripts"))
    import validate_gcfpe_20260914 as fv  # noqa: E402  (the shipped tw1 recipe)
    tw1 = fv.skill_tree_digest(sr / "flowmaster-validate")
    g["G1_identities"] = {"rows": ident, "flowmaster_validate_tw1_recipe": tw1,
                          "flowmaster_validate_matches_tw1": tw1 == TW1_FV_TREE_DIGEST,
                          "ok": all(r.get("matches_expected", True) and r.get("copy_faithful", True)
                                    for r in ident if "expected" in r) and tw1 == TW1_FV_TREE_DIGEST}

    gc = sr / "glow-graph-contract" / "scripts"
    # G2/G3 shipped graph build, selected and candidate parts. Output stays in SCRATCH.
    for key, parts, md in (("G2_build_selected", SELECTED_PARTS, "selected-graph.md"),
                           ("G3_build_candidate", CANDIDATE_PARTS, "candidate-graph.md")):
        r = run([sys.executable, str(gc / "graph_parts.py"), "build", parts, str(scratch / "build" / md)], env=env)
        r["ok"] = r["exit_code"] == 0 and "validation PASS" in r["stdout"]
        g[key] = r
    # G4/G5 shipped registry derivation (never writes the registry).
    for key, parts in (("G4_registry_vs_selected", SELECTED_PARTS), ("G5_registry_vs_candidate", CANDIDATE_PARTS)):
        r = run([sys.executable, str(gc / "registry_deriver.py"), str(sr / "amthor-workspace-governance-audit"),
                 REGISTRY, parts, "--derive"], env=env)
        r["parsed"] = json.loads(r["stdout"]) if r["stdout"].strip().startswith("{") else None
        g[key] = r
    g["G4_registry_vs_selected"]["ok"] = (g["G4_registry_vs_selected"]["exit_code"] == 0
                                         and g["G4_registry_vs_selected"]["parsed"]["drift"] == [])
    g["G5_registry_vs_candidate"]["interpretation"] = (
        "Observed drift is the candidate's own routing change, derivable by the shipped deriver; "
        "not a selected-registry defect.")

    # G6 the bundled direct-handoff contract regenerates from the SELECTED build, byte-equal.
    r = run([sys.executable, str(gc / "contract_recipe.py"), str(scratch / "build" / "selected-graph.md"), TEMPLATE,
             str(sr / "flowmaster-validate" / "references" / "glow-hde-canonical-change-flow-r1-20260923.json"),
             DECISIONS, str(scratch / "build" / "contract-regen.json"),
             "--contract-revision", "4.1.1", "--primary-skill-revision", "1.3.1",
             "--check", str(sr / "change-flow" / CONTRACT), str(sr / "flowmaster-validate" / CONTRACT)], env=env)
    r["ok"] = r["exit_code"] == 0 and r["stdout"].count("EQUAL ") == 2
    g["G6_contract_regenerates_from_selected"] = r

    # G7 full Flowmaster suite, strict, with the installed companions.
    r = run([sys.executable, str(sr / "flowmaster-validate" / "scripts" / "validate_flowmaster.py"),
             "--skills-root", str(sr), "--strict-warnings"], env=env)
    rep = json.loads(r["stdout"]) if r["stdout"].strip().startswith("{") else {}
    g["G7_flowmaster_suite"] = {"argv": r["argv"], "exit_code": r["exit_code"],
                                "fields": {k: rep.get(k) for k in ("verdict", "suite_ok", "validator_revision",
                                           "primary_revision", "self_identity", "missing_expected_skills",
                                           "finding_counts", "warnings")},
                                "fixture_suite_ok": (rep.get("fixtures") or {}).get("fixture_suite_ok"),
                                "ok": r["exit_code"] == 0 and rep.get("suite_ok") is True}
    # G8 baseline package validators (selected-release profile; zero bodies is no body pass).
    g["G8a_change_flow"] = run([sys.executable, str(sr / "change-flow" / "scripts" / "validate_gcfpe_20260914.py")], env=env)
    g["G8b_pr_development"] = run([sys.executable, str(sr / "glow-hde-pr-development" / "scripts" /
                                   "validate_glow_hde_pr_development.py")], env=env)
    for key in ("G8a_change_flow", "G8b_pr_development"):
        g[key]["ok"] = g[key]["exit_code"] == 0 and g[key]["stdout"].startswith("PASS")
    r = run([sys.executable, str(sr / "flowmaster-validate" / "scripts" / "validate_gcfpe_20260914.py"),
             str(sr / "change-flow"), "--contract", str(sr / "change-flow" / CONTRACT)], env=env)
    rep = json.loads(r["stdout"]) if r["stdout"].strip().startswith("{") else {}
    g["G8c_fv_gcfpe_profile"] = {"argv": r["argv"], "exit_code": r["exit_code"],
                                 "fields": {k: rep.get(k) for k in ("ok", "profile", "prompt_body_count",
                                            "prompt_body_checks_not_evaluated", "frozen_graph_sha256",
                                            "contract_sha256", "errors")},
                                 "ok": r["exit_code"] == 0 and rep.get("ok") is True,
                                 "note": "selected-release profile; zero prompt bodies is not a body-level pass"}

    # SUBSTITUTE, informational only: the same two gates with the INSTALLED attribution lock as sibling.
    # It advertises the analysed revision (1.2.0) with different bytes, so it is not the analysed source
    # and its result counts for nothing. Recorded so the dependency is visible, never as a pass.
    sub = scratch / "skills-root-installed-attribution"
    shutil.rmtree(sub, ignore_errors=True)
    shutil.copytree(sr, sub, symlinks=True)
    shutil.copytree(installed / "glow-merged-change-attribution-lock", sub / "glow-merged-change-attribution-lock",
                    symlinks=True)
    r = run([sys.executable, str(sub / "flowmaster-validate" / "scripts" / "validate_flowmaster.py"),
             "--skills-root", str(sub), "--strict-warnings"], env=env)
    rep = json.loads(r["stdout"]) if r["stdout"].strip().startswith("{") else {}
    r2 = run([sys.executable, str(sub / "flowmaster-validate" / "scripts" / "validate_gcfpe_20260914.py"),
              str(sub / "change-flow"), "--contract", str(sub / "change-flow" / CONTRACT)], env=env)
    rep2 = json.loads(r2["stdout"]) if r2["stdout"].strip().startswith("{") else {}
    g["X_substitute_installed_attribution_sibling"] = {
        "informational_only": True,
        "attribution_sibling_freeze": freeze(sub / "glow-merged-change-attribution-lock", env),
        "analysed_attribution_freeze": SUPPLIED_NOT_INSTALLED["glow-merged-change-attribution-lock"],
        "suite": {"exit_code": r["exit_code"], "verdict": rep.get("verdict"), "suite_ok": rep.get("suite_ok"),
                  "finding_counts": rep.get("finding_counts")},
        "fv_gcfpe_profile": {"exit_code": r2["exit_code"], "ok": rep2.get("ok"), "errors": rep2.get("errors")}}

    # G9 governed packaging route (skill-creator), on an UNCHANGED package: proves the mechanism
    # round-trips bytes; it certifies nothing about repaired bytes.
    pkg = scratch / "pkg"
    shutil.rmtree(pkg, ignore_errors=True)
    (pkg / "work").mkdir(parents=True)
    (pkg / "out").mkdir()
    shutil.copytree(sr / "glow-hde-pr-development", pkg / "work" / "glow-hde-pr-development")
    qv = run([sys.executable, "-m", "scripts.quick_validate", str(pkg / "work" / "glow-hde-pr-development")],
             cwd=str(sr / "skill-creator"), env=env)
    pk = run([sys.executable, "-m", "scripts.package_skill", str(pkg / "work" / "glow-hde-pr-development"),
              str(pkg / "out")], cwd=str(sr / "skill-creator"), env=env)
    archive = pkg / "out" / "glow-hde-pr-development.skill"
    g9 = {"quick_validate_exit": qv["exit_code"], "package_exit": pk["exit_code"], "archive_exists": archive.is_file()}
    if archive.is_file():
        z = zipfile.ZipFile(archive)
        names = z.namelist()
        g9["entries"] = len(names)
        g9["traversal"] = [n for n in names if n.startswith("/") or ".." in n.split("/")]
        g9["roots"] = sorted({n.split("/")[0] for n in names})
        z.extractall(pkg / "extract")
        g9["archive_bytes"] = archive.stat().st_size
        g9["archive_sha256"] = hashlib.sha256(archive.read_bytes()).hexdigest()
        g9["extracted_freeze"] = freeze(pkg / "extract" / "glow-hde-pr-development", env)
        g9["gate_from_extracted_exit"] = run([sys.executable, str(pkg / "extract" / "glow-hde-pr-development" /
                                              "scripts" / "validate_glow_hde_pr_development.py")], env=env)["exit_code"]
    g9["ok"] = (g9.get("extracted_freeze") == EXPECTED["glow-hde-pr-development"][0] and qv["exit_code"] == 0
                and pk["exit_code"] == 0 and g9.get("traversal") == [] and g9.get("gate_from_extracted_exit") == 0)
    g["G9_packaging_route_unchanged_package"] = g9

    # G10/G11 record and whitespace checks.
    r = run([sys.executable, "docs/prompt_ecosystem_management/modification_validate.py", RECORD], env=env)
    r["ok"] = r["exit_code"] == 0
    g["G10_record_validates"] = r
    r = run(["git", "diff", "--check"])
    r["ok"] = r["exit_code"] == 0
    g["G11_git_diff_check"] = r

    # DR-1 facts: the two contract fields the dated plan would change are graph-derived.
    regen = (gc / "regenerate_contract.py").read_text(encoding="utf-8").splitlines()
    fvsrc = (sr / "flowmaster-validate" / "scripts" / "validate_gcfpe_20260914.py").read_text(encoding="utf-8").splitlines()
    sel_g = json.loads(Path(SELECTED_PARTS, "global.json").read_text(encoding="utf-8"))
    cand_g = json.loads(Path(CANDIDATE_PARTS, "global.json").read_text(encoding="utf-8"))
    bundled = json.loads((sr / "change-flow" / CONTRACT).read_text(encoding="utf-8"))

    def role(parts: str) -> str:
        d = json.loads(Path(parts, "prompts", "QA-100.json").read_text(encoding="utf-8"))
        return (d.get("node") or d).get("receiving_role")

    g["DR1_facts"] = {
        "regenerator_lines": [f"{i}: {l.strip()}" for i, l in enumerate(regen, 1)
                              if "producer_allocates_pf10_number" in l or '"receiving_role": "receiving_role"' in l],
        "validator_lines": [f"{i}: {l.strip()}" for i, l in enumerate(fvsrc, 1)
                            if "producer_allocates_pf10_number" in l or "GRAPH_PF10_CONTRACT_MISMATCH" in l],
        "producer_allocates_pf10_number": {
            "selected_parts": sel_g["pf10_addendum_contract"]["producer_allocates_pf10_number"],
            "candidate_parts": cand_g["pf10_addendum_contract"]["producer_allocates_pf10_number"],
            "bundled_contract": bundled["pf10_addendum_contract"]["producer_allocates_pf10_number"]},
        "QA-100_receiving_role": {"selected_parts": role(SELECTED_PARTS), "candidate_parts": role(CANDIDATE_PARTS),
                                  "bundled_contract": bundled["member_registry"]["QA-100"]["receiving_role"]},
    }
    out["all_normal_path_gates_ok"] = all(v.get("ok", True) for k, v in g.items() if k.startswith("G")
                                          and isinstance(v, dict) and "ok" in v)
    json.dump(out, sys.stdout, indent=1, sort_keys=True, ensure_ascii=False)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
