#!/usr/bin/env python3
"""PLAN successor 2 dry run (D26-A step 1) for MODIFICATION-20261010-gcfpe-candidate-skill-analysis.

The narrowed scope Nathan chose in DN-1 (Option 1): the eight candidate native pages and the candidate
execution-copy graph and registry. Re-runnable evidence, not a gate implementation. Read-only against the
repository, the installed skills and Notion: it copies the two graph/registry skills into SCRATCH, rehearses
every planned edit in memory and on scratch copies, and prints one JSON receipt on stdout. Nothing in the
receipt is prompt-body text (D22); page bodies are read only as transient reads by body_check.py.

Usage, from the repository root, with the newest fetch of each page in this session's harness records:

    PYTHONDONTWRITEBYTECODE=1 python3 \\
      docs/ephemeral/modifications/evidence/20261010-gcfpe-candidate-skill-analysis/plan-successor-2/dry_run.py \\
      <installed-skills-root> <scratch-dir> [<since-minutes>] > <receipt.json>
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

MOD = "MODIFICATION-20261010-gcfpe-candidate-skill-analysis"
HERE = Path(__file__).resolve().parent
FREEZE = "docs/prompt_ecosystem_management/freeze.py"
REGISTRY = "docs/prompt_ecosystem_management/project-prompt-contract-registry.md"
SELECTED_PARTS = "docs/graph/parts"
BASE_PARTS = "docs/ephemeral/modifications/evidence/20261009-gcfpe-latest-alpha-analysis/execute/candidate-graph-parts"
EXPECTED = {  # freeze.py output, bound in PLAN-SUCCESSOR-1-20261011.md §2
    "glow-graph-contract": "9 e241bb9a67c4470895fc666a25d0f97d8df7e8e2df06539de5deaf12bc46467c",
    "amthor-workspace-governance-audit": "15 c214e8741e9c54d395cfbd1379cbc7947e6c07beee5bd03aca433dc5dda937ab",
}
# PR-40's derivation as successor 1 observed it on the unrepaired candidate (G5); the repair must not move it.
PR40_DERIVED = {"required_interfaces": ["DOC-10", "DOC-20", "OPS-10", "PR-10", "PR-20", "QA-10", "RS-10"],
                "consumers": ["DOC-10", "DOC-20", "OPS-10", "PR-10", "PR-20", "QA-10", "RS-10"],
                "states": ["ACCEPT", "PENDING", "REJECT"]}


def run(argv, env, cwd=None) -> dict:
    p = subprocess.run([str(a) for a in argv], cwd=cwd, env=env, capture_output=True, text=True)
    return {"argv": [str(a) for a in argv], "exit_code": p.returncode, "stdout": p.stdout, "stderr": p.stderr}


def as_json(r: dict):
    try:
        return json.loads(r["stdout"])
    except ValueError:
        return None


def main() -> int:
    installed, scratch = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve()
    since = sys.argv[3] if len(sys.argv) > 3 else "120"
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TMPDIR=str(scratch / "tmp"))
    for d in ("skills-root", "tmp", "graph"):
        (scratch / d).mkdir(parents=True, exist_ok=True)
    sr = scratch / "skills-root"
    out = {"record_type": "PLAN_SUCCESSOR_2_DRY_RUN", "modification": MOD,
           "date_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
           "repository_head": run(["git", "rev-parse", "HEAD"], env)["stdout"].strip(),
           "origin_main": run(["git", "rev-parse", "origin/main"], env)["stdout"].strip(), "gates": {}}
    g = out["gates"]

    # N0 identities of the two skills whose shipped scripts the graph/registry steps run.
    rows = []
    for name, expected in EXPECTED.items():
        shutil.rmtree(sr / name, ignore_errors=True)
        shutil.copytree(installed / name, sr / name, symlinks=True)
        got = run([sys.executable, FREEZE, installed / name], env)["stdout"].strip()
        copy = run([sys.executable, FREEZE, sr / name], env)["stdout"].strip()
        rows.append({"skill": name, "expected": expected, "installed": got, "scratch_copy": copy,
                     "ok": got == expected == copy})
    g["N0_identities"] = {"rows": rows, "ok": all(r["ok"] for r in rows)}
    gc = sr / "glow-graph-contract" / "scripts"

    # N1-N3 native pages: guard self-test, in-memory rehearsal of all 22 operations, registry-form guards.
    body = [sys.executable, HERE / "body_check.py"]
    r = run(body + ["selftest"], env)
    rep = as_json(r) or {}
    g["N1_body_guard_selftest"] = {"exit_code": r["exit_code"], "guards": rep.get("guards"),
                                   "fixture_rows": len(rep.get("fixture_rows", [])),
                                   "span_resolver": rep.get("span_resolver"), "ok": rep.get("ok") is True}
    r = run(body + ["plan", "--no-ops", "--since-minutes", since], env)
    rep = as_json(r) or {}
    pages = []
    for p in rep.get("pages", []):
        if "error" in p:
            pages.append(p)
            continue
        pages.append({"prompt": p["prompt"], "fetch_captured": p["fetch_captured"], "as_of": p["as_of"],
                      "revision_matches_plan": p["revision_matches_plan"],
                      "ops": len(p["ops"]), "ops_applied": sum(o["applied"] for o in p["ops"]),
                      "batch_safe": p["batch_safe"],
                      "guards": len(p["guards_before"]),
                      "guards_failing_before": sorted(k for k, v in p["guards_before"].items() if not v["pass"]),
                      "guards_failing_after": sorted(k for k, v in p["guards_after"].items() if not v["pass"]),
                      "all_landed_after": all(v == "LANDED" for v in p["landed_state_after"].values()),
                      "ok": p["ok"]})
    g["N2_native_rehearsal"] = {"exit_code": r["exit_code"], "pages": pages,
                                "ops_total": sum(p.get("ops", 0) for p in pages), "ok": rep.get("ok") is True}
    r = run(body + ["registry", "--audit-root", sr / "amthor-workspace-governance-audit", "--since-minutes", since],
            env)
    rep = as_json(r) or {}
    g["N3_registry_form_guards"] = {
        "exit_code": r["exit_code"], "engine": rep.get("engine"),
        "fixtures": len(rep.get("fixtures", [])), "fixtures_agree": sum(f["agrees"] for f in rep.get("fixtures", [])),
        "page_guard_rows": len(rep.get("pages", [])),
        "page_guard_rows_agree": sum(p.get("agrees", False) for p in rep.get("pages", [])),
        "ok": rep.get("ok") is True}

    # N4-N5 graph: self-test with injected regressions, then the planned sequence on a scratch copy.
    graph = [sys.executable, HERE / "graph_repair.py"]
    r = run(graph + ["selftest", BASE_PARTS, scratch / "graph" / "selftest", gc / "graph_parts.py"], env)
    rep = as_json(r) or {}
    g["N4_graph_repair_selftest"] = {"exit_code": r["exit_code"], "rows": rep.get("rows"),
                                     "ok": rep.get("ok") is True}
    parts = scratch / "graph" / "parts"
    shutil.rmtree(parts, ignore_errors=True)
    shutil.copytree(BASE_PARTS, parts)
    steps = {}
    steps["apply"] = as_json(run(graph + ["apply", parts], env))
    steps["apply_again"] = as_json(run(graph + ["apply", parts], env))
    steps["reindex"] = run([sys.executable, gc / "graph_parts.py", "reindex", parts], env)
    steps["reindex_again"] = run([sys.executable, gc / "graph_parts.py", "reindex", parts], env)
    steps["build_base"] = run([sys.executable, gc / "graph_parts.py", "build", BASE_PARTS,
                               scratch / "graph" / "base-graph.md"], env)
    steps["build_repaired"] = run([sys.executable, gc / "graph_parts.py", "build", parts,
                                   scratch / "graph" / "repaired-graph.md"], env)
    steps["check"] = as_json(run(graph + ["check", parts, BASE_PARTS], env))
    steps["built"] = as_json(run(graph + ["built", scratch / "graph" / "repaired-graph.md",
                                          scratch / "graph" / "base-graph.md"], env))
    rewritten = [l.strip() for l in steps["reindex"]["stdout"].splitlines()[1:]]
    g["N5_graph_repair_dry_run"] = {
        "apply": steps["apply"], "apply_again_noop": (steps["apply_again"] or {}).get("already_applied") is True,
        "reindex_stdout_first_line": steps["reindex"]["stdout"].splitlines()[0] if steps["reindex"]["stdout"] else "",
        "reindex_files_rewritten": len(rewritten),
        "reindex_again_stdout": steps["reindex_again"]["stdout"].strip(),
        "build_base_stdout": steps["build_base"]["stdout"].strip().splitlines(),
        "build_repaired_stdout": steps["build_repaired"]["stdout"].strip().splitlines(),
        "check": steps["check"], "built": steps["built"],
        "ok": ((steps["apply"] or {}).get("changed") is not None and len(steps["apply"]["changed"]) == 7
               and (steps["apply_again"] or {}).get("already_applied") is True
               and steps["reindex"]["exit_code"] == 0
               and "0 file(s) rewritten" in steps["reindex_again"]["stdout"]
               and steps["build_base"]["exit_code"] == 0 and "validation PASS" in steps["build_base"]["stdout"]
               and steps["build_repaired"]["exit_code"] == 0
               and "validation PASS" in steps["build_repaired"]["stdout"]
               and (steps["check"] or {}).get("ok") is True and (steps["built"] or {}).get("ok") is True)}

    # N6 shipped registry derivation on the repaired copy (never writes the registry).
    r = run([sys.executable, gc / "registry_deriver.py", sr / "amthor-workspace-governance-audit", REGISTRY,
             parts, "--derive"], env)
    rep = as_json(r) or {}
    derived = rep.get("derived") or {}
    base_rs20 = json.loads(Path(BASE_PARTS, "prompts", "RS-20.json").read_text(encoding="utf-8"))
    base_ifaces = sorted({e["to"] for e in base_rs20["edges"] if e.get("to_kind") == "prompt" and e["to"] != "RS-20"})
    g["N6_registry_derivation"] = {
        "exit_code": r["exit_code"], "rows": rep.get("rows"), "parts": rep.get("parts"), "drift": rep.get("drift"),
        "derived": derived, "rs20_interfaces_before_repair": base_ifaces,
        "ok": (r["exit_code"] == 1 and rep.get("drift") == ["PR-40", "RS-20"]
               and derived.get("PR-40") == PR40_DERIVED
               and derived.get("RS-20", {}).get("required_interfaces") == sorted(base_ifaces + ["PR-20"])
               and derived.get("RS-20", {}).get("consumers") == sorted(base_ifaces + ["PR-20"]))}

    # N7 surfaces the plan must not touch; N8 record and whitespace checks.
    untouched = {
        "selected_parts_and_registry_vs_origin_main": run(
            ["git", "diff", "--quiet", "origin/main", "--", SELECTED_PARTS, REGISTRY], env)["exit_code"] == 0,
        "pfcanon_vs_origin_main": run(["git", "diff", "--quiet", "origin/main", "--", "docs/pfcanon"],
                                      env)["exit_code"] == 0,
        "base_candidate_parts_vs_head": run(["git", "diff", "--quiet", "HEAD", "--", BASE_PARTS], env)["exit_code"] == 0,
    }
    g["N7_untouched_surfaces"] = {**untouched, "ok": all(untouched.values())}
    r = run([sys.executable, "docs/prompt_ecosystem_management/modification_validate.py",
             "docs/ephemeral/modifications/"], env)
    g["N8a_records_validate"] = {"exit_code": r["exit_code"], "stdout_tail": r["stdout"].strip().splitlines()[-3:],
                                 "ok": r["exit_code"] == 0}
    r = run(["git", "diff", "--check"], env)
    g["N8b_git_diff_check"] = {"exit_code": r["exit_code"], "ok": r["exit_code"] == 0}

    out["ok"] = all(v.get("ok") for v in g.values())
    out["d22"] = ("page bodies read only as transient reads of this session's harness records by body_check.py; "
                  "no body text in this receipt")
    print(json.dumps(out, indent=1, ensure_ascii=False))
    return 0 if out["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
