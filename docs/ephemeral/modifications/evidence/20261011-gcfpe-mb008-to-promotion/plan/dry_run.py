#!/usr/bin/env python3
"""PLAN dry run (D26-A step 1) for MODIFICATION-20261011-gcfpe-mb008-to-promotion.

Re-runnable evidence, not a gate implementation. Read-only against the repository, the installed skills and
Notion: it copies the installed skills and the parent's candidate graph parts into SCRATCH, rehearses every planned
change there and in memory, and prints one JSON receipt on stdout. Nothing in the receipt is prompt-body text
(D22); page bodies are read only as transient reads of this session's own fetch records, by body_check.py.

Usage, from the repository root, after fetching all 55 pages listed in edits.json in this session:

    PYTHONDONTWRITEBYTECODE=1 CLAUDE_CODE_SESSION_ID=<session> python3 \\
      docs/ephemeral/modifications/evidence/20261011-gcfpe-mb008-to-promotion/plan/dry_run.py \\
      <installed-skills-root> <scratch-dir> <fetched-after> > <receipt.json>

<fetched-after> is an ISO UTC time taken just before those fetches. The MGMT-10 successor page does not exist
until EXECUTE, so the dry run uses the testing page's URL as a stand-in, and the PLAN document's digest is
stood in by edits.json's; both are named in the receipt.
"""
from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[5]
SESSION = os.environ.get("CLAUDE_CODE_SESSION_ID", "")
SKILLS = ["change-flow", "flowmaster-validate", "glow-hde-pr-development", "glow-graph-contract",
          "session-relay-flowmaster", "amthor-workspace-governance-audit", "glow-merged-change-attribution-lock",
          "flowmaster-primary", "tw-flowmaster", "session-branch-flowmaster", "skill-creator", "typesafe-scoring",
          "glow-po-reporting"]
EXPECTED = {  # freeze.py output, source-identities.md
    "change-flow": "22 9a551af36e042e56a48045297ac316b4102a4eb21f31622853c8be700e223f47",
    "flowmaster-validate": "31 90c15e985a0c4b78d24298fe8187e8a50576689ddfc509d09fa11187ab97fcc2",
    "glow-hde-pr-development": "4 265f9170d8459fc477287c320f0bbdd8eaaf0e6ba1dd4ee513275a76a22f8f7a",
    "glow-graph-contract": "9 e241bb9a67c4470895fc666a25d0f97d8df7e8e2df06539de5deaf12bc46467c",
    "session-relay-flowmaster": "5 c8a5b22432a44f57fb12bc508169f85aa3d0ca3298b793590c364eb9a2afc8e4",
    "amthor-workspace-governance-audit": "15 c214e8741e9c54d395cfbd1379cbc7947e6c07beee5bd03aca433dc5dda937ab",
    "glow-merged-change-attribution-lock": "10 c518ccb0076b042859de4d2e136ef682bb127b6524133d2a575d433490eaf48f",
}
PARENT_PARTS = REPO / "docs/ephemeral/modifications/evidence/20261010-gcfpe-candidate-skill-analysis/execute/candidate-graph-parts"
TEMPLATE = REPO / "docs/graph/contract-template/gcfpe-20260914.1-091426.1-direct-handoff-contract-4.0.6.json"
DECISIONS = REPO / "docs/prompt_ecosystem_management/gcfpe.decision-record.md"
STAND_IN_URL = "https://app.notion.com/p/3e34590a05eb811b93d2da9b4ef8106d?pvs=204"
R1 = "references/glow-hde-canonical-change-flow-r1-20260923.json"


def run(args, cwd=None, inp=None):
    env = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1"}
    r = subprocess.run([str(a) for a in args], cwd=cwd, input=inp, capture_output=True, text=True, env=env)
    return r.returncode, r.stdout, r.stderr


def jrun(args, cwd=None, inp=None):
    code, out, err = run(args, cwd, inp)
    try:
        return code, json.loads(out)
    except ValueError:
        return code, {"_unparsed": (out + err)[-600:]}


def freeze(path: Path) -> str:
    return run([sys.executable, REPO / "docs/prompt_ecosystem_management/freeze.py", path])[1].strip().splitlines()[-1]


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def graph_json(md: Path) -> str:
    lines = md.read_text(encoding="utf-8").split("\n")
    s = next(i for i, l in enumerate(lines) if l == "```json")
    e = max(i for i, l in enumerate(lines) if l == "```")
    return "\n".join(lines[s + 1:e]) + "\n"


def main() -> int:
    installed, scratch, fetched_after = Path(sys.argv[1]), Path(sys.argv[2]), sys.argv[3]
    if scratch.exists():
        shutil.rmtree(scratch)
    base, work, graph = scratch / "base", scratch / "work", scratch / "graph"
    for d in (base, work, graph):
        d.mkdir(parents=True)
    gates, ok = {}, True

    # N0: identities of the installed skills and of their scratch copies
    rows = []
    for k in SKILLS:
        shutil.copytree(installed / k, base / k, ignore=shutil.ignore_patterns("__pycache__"))
        shutil.copytree(base / k, work / k)
        if k in EXPECTED:
            row = {"skill": k, "expected": EXPECTED[k], "installed": freeze(installed / k), "copy": freeze(base / k)}
            row["ok"] = row["expected"] == row["installed"] == row["copy"]
            rows.append(row)
    gates["N0_identities"] = {"rows": rows, "ok": all(r["ok"] for r in rows)}

    # N1-N3: body operations, guards and registry form on this session's fresh reads
    bc = HERE / "body_check.py"
    c1, st = jrun([sys.executable, bc, "selftest"])
    gates["N1_body_guard_selftest"] = {"exit_code": c1, "guards": st.get("guards"),
                                       "fixture_rows": len(st.get("fixture_rows", [])),
                                       "span_resolver": st.get("span_resolver"), "ok": c1 == 0 and st.get("ok")}
    c2, pl = jrun([sys.executable, bc, "plan", "--no-ops", "--since-minutes", "900", "--fetched-after", fetched_after])
    pages = pl.get("pages", [])
    gates["N2_body_rehearsal"] = {
        "exit_code": c2, "pages": len(pages),
        "ops": sum(len(p.get("ops", [])) for p in pages),
        "ops_applied": sum(sum(o["applied"] for o in p.get("ops", [])) for p in pages),
        "revisions_match_pins": sum(bool(p.get("revision_matches_plan")) for p in pages),
        "batch_safe": sum(bool(p.get("batch_safe")) for p in pages),
        "guard_rows_after": sum(len(p.get("guards_after", {})) for p in pages),
        "guard_rows_passing_after": sum(sum(v["pass"] for v in p.get("guards_after", {}).values()) for p in pages),
        "guard_rows_passing_before": sum(sum(v["pass"] for v in p.get("guards_before", {}).values()) for p in pages),
        "check_would_pass": sum(bool(p.get("check_would_pass")) for p in pages),
        "failing_pages": [p.get("prompt") for p in pages if not p.get("ok")], "ok": c2 == 0 and pl.get("ok")}
    c3, rg = jrun([sys.executable, bc, "registry", "--audit-root", base / "amthor-workspace-governance-audit",
                   "--since-minutes", "900", "--fetched-after", fetched_after])
    gates["N3_registry_form"] = {"exit_code": c3, "fixtures": len(rg.get("fixtures", [])),
                                 "fixtures_agree": sum(f["agrees"] for f in rg.get("fixtures", [])),
                                 "page_rows": len(rg.get("pages", [])),
                                 "page_rows_agree": sum(bool(p.get("agrees")) for p in rg.get("pages", [])),
                                 "ok": c3 == 0 and rg.get("ok")}

    # N4: graph assembly (MGMT-10 successor part, measured proofs, lifecycle flip) and builds
    ga, gp = HERE / "graph_assemble.py", base / "glow-graph-contract/scripts/graph_parts.py"
    c4, sto, _ = run([sys.executable, ga, "selftest", PARENT_PARTS, graph, gp])
    selft = json.loads(sto.strip().splitlines()[-1])
    cand, prod = graph / "parts-cand", graph / "parts-prod"
    shutil.copytree(PARENT_PARTS, cand)
    run([sys.executable, ga, "apply", cand, STAND_IN_URL])
    run([sys.executable, gp, "reindex", cand])
    chk_c = json.loads(run([sys.executable, ga, "check", cand, PARENT_PARTS])[1])
    run([sys.executable, ga, "flip", cand, prod])
    chk_p = json.loads(run([sys.executable, ga, "check", prod, PARENT_PARTS, "--flipped"])[1])
    tokens = {}
    for name, parts in (("parent", PARENT_PARTS), ("candidate", cand), ("production", prod)):
        code, out, err = run([sys.executable, gp, "build", parts, graph / f"{name}.md"])
        gj = graph_json(graph / f"{name}.md") if code == 0 else ""
        tokens[name] = {"exit_code": code, "edges": json.loads(gj)["edges"].__len__() if gj else None,
                        "bytes": len(gj.encode()) if gj else None,
                        "sha256": hashlib.sha256(gj.encode()).hexdigest() if gj else None,
                        "validation_pass": "validation PASS" in out}
    gates["N4_graph"] = {"selftest": selft, "check_candidate": chk_c, "check_production": chk_p, "builds": tokens,
                         "mgmt10_url": "STAND-IN: the testing page; EXECUTE uses the duplicated successor's URL",
                         "ok": c4 == 0 and chk_c["ok"] and chk_p["ok"] and all(t["validation_pass"] for t in tokens.values())
                         and tokens["parent"]["sha256"] == "ff296b1e740a77ee207c1223cc9bdff1f56c6c167bd4714a41ae92ef8708f18b"}

    # N5: regenerator with the glow-graph-contract patch: the shipped contract still regenerates; 100926.1 contracts
    # the patch was written from base/<skill> to work/<skill>, so two leading components are stripped
    code, out, err = run(["patch", "-p2", "--batch", "-d", work / "glow-graph-contract", "-i",
                          HERE / "patches/glow-graph-contract-mb008.patch"])
    recipe = work / "glow-graph-contract/scripts/contract_recipe.py"
    shipped = []
    for k in ("change-flow", "flowmaster-validate"):
        shipped.append(base / k / "references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json")
    selected_md = graph / "selected.md"
    run([sys.executable, gp, "build", REPO / "docs/graph/parts", selected_md])
    ce, eq_out, _ = run([sys.executable, recipe, selected_md, TEMPLATE, base / "flowmaster-validate" / R1, DECISIONS,
                         graph / "shipped-check.json", "--contract-revision", "4.1.1", "--primary-skill-revision", "1.3.1",
                         "--check", *shipped])
    rv = json.loads((HERE / "release-values-100926.1.json").read_text(encoding="utf-8"))
    stand = (HERE / "edits.json")
    filled = json.dumps(rv).replace('"@PLAN_SHA256"', f'"{sha(stand)}"').replace('"@PLAN_BYTES"', str(stand.stat().st_size))
    (graph / "release-values.json").write_text(filled, encoding="utf-8")
    cu, _, _ = run([sys.executable, recipe, graph / "candidate.md", TEMPLATE, base / "flowmaster-validate" / R1, DECISIONS,
                    graph / "x.json", "--contract-revision", "4.2.0", "--primary-skill-revision", "1.4.0",
                    "--release-values", HERE / "release-values-100926.1.json"])
    contracts = {}
    for name in ("candidate", "production"):
        c, o, e = run([sys.executable, recipe, graph / f"{name}.md", TEMPLATE, base / "flowmaster-validate" / R1, DECISIONS,
                       graph / f"{name}-contract.json", "--contract-revision", "4.2.0", "--primary-skill-revision", "1.4.0",
                       "--release-values", graph / "release-values.json"])
        p = graph / f"{name}-contract.json"
        contracts[name] = {"exit_code": c, "bytes": p.stat().st_size if p.exists() else None,
                           "sha256": sha(p) if p.exists() else None}
    gates["N5_regenerator"] = {"patch_applied": code == 0, "shipped_091426_contract_regenerates_equal":
                               ce == 0 and eq_out.count("EQUAL    ") == 2, "unfilled_marker_refused": cu != 0,
                               "contracts_100926": contracts, "plan_digest": "STAND-IN: edits.json",
                               "ok": code == 0 and ce == 0 and cu != 0 and all(v["exit_code"] == 0 for v in contracts.values())}

    # N6: the 100926.1 profile derived from the 091426.1 validator, run on the production contract
    fv, cf = work / "flowmaster-validate", work / "change-flow"
    gj = graph_json(graph / "production.md")
    for k in (fv, cf):
        (k / "references/gcfpe-20261009.1-100926.1-candidate-graph-contract.json").write_text(gj, encoding="utf-8")
        shutil.copyfile(graph / "production-contract.json", k / "references/gcfpe-20261009.1-100926.1-direct-handoff-contract.json")
    fxd = fv / "fixtures/gcfpe-20261009.1-100926.1"
    fxd.mkdir(parents=True)
    fx = json.loads((fv / "fixtures/gcfpe-20260914.1-091426.1/scenarios.json").read_text(encoding="utf-8"))
    fx.update(suite_id="GCFPE-20261009.1-100926.1-SECTION-13", release="GCFPE-20261009.1", prompt_version="100926.1")
    (fxd / "scenarios.json").write_text(json.dumps(fx, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    prof = json.loads((fv / "references/gcfpe-20260914.1-091426.1-validation-profile.json").read_text(encoding="utf-8"))
    cpath = fv / "references/gcfpe-20261009.1-100926.1-direct-handoff-contract.json"
    gpath = fv / "references/gcfpe-20261009.1-100926.1-candidate-graph-contract.json"
    prof.update(profile_id="GCFPE-20261009.1-100926.1-VALIDATION", prompt_version="100926.1",
                target_release="GCFPE-20261009.1", selected_member_count_during_staging=55,
                selected_prompt_version_during_staging="091426.1", selected_release_during_staging="GCFPE-20260914.1",
                validator_revision="3.4.0",
                installed_skill_revisions={"change-flow": "3.4.0", "glow-hde-pr-development": "1.4.0"})
    prof["candidate_contract"].update(bundled_relative_path="references/gcfpe-20261009.1-100926.1-direct-handoff-contract.json",
                                      relative_to_change_flow="references/gcfpe-20261009.1-100926.1-direct-handoff-contract.json",
                                      byte_count=cpath.stat().st_size, sha256=sha(cpath))
    g = json.loads(gj)
    prof["frozen_graph"].update(bundled_relative_path="references/gcfpe-20261009.1-100926.1-candidate-graph-contract.json",
                                relative_to_candidate_root="graph/GCFPE-20261009.1-Candidate-Graph-Contract.json",
                                byte_count=gpath.stat().st_size, sha256=sha(gpath), edge_count=len(g["edges"]),
                                node_count=len(g["nodes"]))
    prof["fixtures"].update(relative_path="fixtures/gcfpe-20261009.1-100926.1/scenarios.json", sha256=sha(fxd / "scenarios.json"))
    (fv / "references/gcfpe-20261009.1-100926.1-validation-profile.json").write_text(
        json.dumps(prof, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    cm, mk = jrun([sys.executable, HERE / "make_profile_20261009.py", fv / "scripts/validate_gcfpe_20260914.py",
                   fv / "scripts/validate_gcfpe_20261009.py", "--contract", cpath, "--graph", gpath,
                   "--fixtures", fxd / "scenarios.json", "--plan", stand])
    cp, prof_run = jrun([sys.executable, "scripts/validate_gcfpe_20261009.py", cf, "--contract",
                         cf / "references/gcfpe-20261009.1-100926.1-direct-handoff-contract.json"], cwd=fv)
    pending = {"CHANGE_FLOW_CONTRACT:CHANGE_FLOW_SPECIALIZATION_REVISION: 3.4.0"}
    errs = prof_run.get("errors", [])
    unexpected = [e for e in errs if e not in pending and not e.startswith("SKILL_SELF_IDENTITY:")]
    gates["N6_profile_100926"] = {
        "substitutions": sum(1 for r in mk.get("report", []) if "substitution" in r),
        "errors": errs, "unexpected_errors": unexpected,
        "pending_by_design": "change-flow's revision moves to 3.4.0 with its redlines in EXECUTE's package build; "
                             "SKILL_TREE_SHA256 is recomputed as the package build's last step",
        "ok": cm == 0 and not unexpected}

    # N7: the profile's body checks on the 54 candidate member bodies, unedited and with the edits applied in memory
    sys.path.insert(0, str(HERE))
    sys.dont_write_bytecode = True
    import body_check as B  # noqa: E402
    root = os.path.expanduser("~/.claude/projects")
    rows = {}
    for mode in ("before", "after"):
        bodies = {}
        for prompt, meta in B.EDITS["pages"].items():
            if prompt == "PE":
                continue
            got = B.latest_fetch(meta["page_id"], root, SESSION, 900, fetched_after)
            text = got[2] if got else ""
            if mode == "after":
                text, _ = B.apply_all(text, [o for o in B.EDITS["ops"] if o["prompt"] == prompt])
            bodies[prompt] = text
        cb, res = jrun([sys.executable, "scripts/validate_gcfpe_20261009.py", cf, "--contract",
                        cf / "references/gcfpe-20261009.1-100926.1-direct-handoff-contract.json", "--bodies-stdin"],
                       cwd=fv, inp=json.dumps(bodies))
        body_errs = sorted({e.split(":")[0] for e in res.get("errors", []) if e.startswith("PROMPT")})
        rows[mode] = {"bodies_validated": len(res.get("prompt_bodies_validated", [])),
                      "not_evaluated": res.get("prompt_body_checks_not_evaluated"),
                      "body_error_classes": body_errs,
                      "body_errors": sum(1 for e in res.get("errors", []) if e.startswith("PROMPT"))}
    gates["N7_bodies_through_profile"] = {**rows, "ok": rows["after"]["bodies_validated"] == 54
                                          and rows["after"]["body_errors"] == 0 and rows["before"]["body_errors"] > 0}

    # N8: package text redlines on the scratch copies; the governance audit's own fixture suite afterwards
    ap = HERE / "package_apply.py"
    c8a, a1 = jrun([sys.executable, ap, work])
    c8b, a2 = jrun([sys.executable, ap, work, "--check"])
    c8c, _ = jrun([sys.executable, ap, work])
    c8d, out8, err8 = run([sys.executable, "scripts/run_fixture_suite.py"], cwd=work / "amthor-workspace-governance-audit")
    gates["N8_package_redlines"] = {"ops": len(a1.get("rows", [])), "applied": c8a == 0,
                                    "landed": sum(r["state"] == "LANDED" for r in a2.get("rows", [])),
                                    "second_apply_refused": c8c != 0,
                                    "audit_fixture_suite_ok": c8d == 0 and "OK" in (out8 + err8).splitlines()[-1],
                                    "ok": c8a == 0 and c8c != 0 and c8d == 0}

    ok = all(v["ok"] for v in gates.values())
    print(json.dumps({"record_type": "MB008_PLAN_DRY_RUN", "modification": "MODIFICATION-20261011-gcfpe-mb008-to-promotion",
                      "date_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                      "repository_head": run(["git", "-C", REPO, "rev-parse", "HEAD"])[1].strip(),
                      "fetched_after": fetched_after, "gates": gates, "ok": ok,
                      "d22": "transient reads of this session's harness records; no body text in this receipt"},
                     indent=1, ensure_ascii=False))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
