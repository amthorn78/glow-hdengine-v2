#!/usr/bin/env python3
"""X11 (Q3 and Q4, the graphs) for EXECUTE of MODIFICATION-20261027-gcfpe-backlog-open-items.

    x11_graphs_102726.py <build-root> <out>

The plan's commands, on the real successor map (PLAN X11; the dry run's N4): docs/graph/parts copied to
<out>/candidate-parts; graph_assemble_102726.py apply (plan/graph-edits.json, plan/members-100926.1.tsv); the
installed graph_parts.py reindex; check against docs/graph/parts; build <out>/candidate-102726.1.md; routes;
flip to <out>/production-parts; check --flipped; build <out>/production-102726.1.md; routes; selftest. <build-root>
is X10's copy of the installed skills (its graph_parts.py is the installed one, unpatched). Prints a JSON receipt
(tokens, flags and counts only); writes only under <out>. Run with PYTHONDONTWRITEBYTECODE=1.
"""
from __future__ import annotations

import importlib.util
import json
import shutil
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
PLAN = HERE.parent / "plan"
MAP = HERE / "successor-pages-102726.1.json"


def main() -> int:
    build, out = Path(sys.argv[1]), Path(sys.argv[2])
    spec = importlib.util.spec_from_file_location("dr", PLAN / "dry_run_102726.py")
    dr = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(dr)
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)
    ga, ggc, tmp = PLAN / "graph_assemble_102726.py", build / "glow-graph-contract/scripts/graph_parts.py", {"TMPDIR": str(out)}
    cand, prod = out / "candidate-parts", out / "production-parts"
    shutil.copytree(dr.REPO / "docs/graph/parts", cand)
    c_ap, ap = dr.jrun([dr.PY, ga, "apply", cand, MAP, "--graph-edits", PLAN / "graph-edits.json",
                        "--members-tsv", PLAN / "members-100926.1.tsv"])
    c_ri, _, e_ri = dr.run([dr.PY, ggc, "reindex", cand], env_extra=tmp)
    c_ck, ck = dr.jrun([dr.PY, ga, "check", cand, dr.REPO / "docs/graph/parts", MAP])
    c_b1, o1, _ = dr.run([dr.PY, ggc, "build", cand, out / "candidate-102726.1.md"], env_extra=tmp)
    c_r1, rt1 = dr.jrun([dr.PY, ga, "routes", out / "candidate-102726.1.md"])
    c_fl, fl = dr.jrun([dr.PY, ga, "flip", cand, prod])
    c_ck2, ck2 = dr.jrun([dr.PY, ga, "check", prod, dr.REPO / "docs/graph/parts", MAP, "--flipped"])
    c_b2, o2, _ = dr.run([dr.PY, ggc, "build", prod, out / "production-102726.1.md"], env_extra=tmp)
    c_r2, rt2 = dr.jrun([dr.PY, ga, "routes", out / "production-102726.1.md"])
    c_st, stg = dr.jrun([dr.PY, ga, "selftest", dr.REPO / "docs/graph/parts", MAP, out / "graph-selftest", ggc])
    t1, t2 = dr.build_token(o1), dr.build_token(o2)
    rec = {"apply": {"exit": c_ap, **{k: v for k, v in ap.items() if k in ("apply_ok", "sole_added_node", "counts",
                                                                            "edges_added", "edges_removed", "stand_in_used")}},
           "reindex_exit": c_ri, "check_candidate": {"exit": c_ck, **{k: v for k, v in ck.items() if k != "mode"}},
           "candidate_token": t1, "routes_candidate": {"exit": c_r1, **{k: v for k, v in rt1.items() if k != "mode"}},
           "flip": {"exit": c_fl, **{k: v for k, v in fl.items() if k != "mode"}},
           "check_production": {"exit": c_ck2, **{k: v for k, v in ck2.items() if k != "mode"}},
           "production_token": t2, "routes_production": {"exit": c_r2, **{k: v for k, v in rt2.items() if k != "mode"}},
           "selftest": {"exit": c_st, **{k: v for k, v in stg.items() if k != "mode"}}}
    want = (56, 240, 56)
    rec["ok"] = (all(x == 0 for x in (c_ap, c_ri, c_ck, c_b1, c_r1, c_fl, c_ck2, c_b2, c_r2, c_st))
                 and ap.get("apply_ok") is True and ck.get("check_ok") is True and ck2.get("check_ok") is True
                 and rt1.get("routes_ok") is True and rt2.get("routes_ok") is True and stg.get("selftest_ok") is True
                 and t1["validation_pass"] and t2["validation_pass"]
                 and (t1["nodes"], t1["edges"], t1["state_routes"]) == want == (t2["nodes"], t2["edges"], t2["state_routes"]))
    print(json.dumps(rec, indent=1, ensure_ascii=False))
    return 0 if rec["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
