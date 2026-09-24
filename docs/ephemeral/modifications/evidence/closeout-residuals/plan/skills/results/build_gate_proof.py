"""Build EV/skills/results/gate_proof_x.json from the round-5 proof run: up to 400 lines of each step's output (the first and last 200; X4.2 and X7.4 post were cut) and each set's rows."""
import json
S = "/tmp/claude-0/-home-user-glow-hdengine-v2/398e36e8-b34a-56a2-83e3-75550250e4f5/scratchpad/plan/r5/proof"
EVR = "/home/user/glow-hdengine-v2/docs/ephemeral/modifications/evidence/closeout-residuals/plan/skills/results"
steps = json.load(open(S + "/proof_x.json"))
def clean(s):
    return s.replace(S + "/scratch", "$SCRATCH").replace(S + "/repo", "$REPO")
for x in steps:
    x["output"] = [clean(l) for l in x["output"]]
sets = {}
for name in ("pre", "pkg", "post"):
    g = json.load(open(S + f"/scratch/gate/gate_{name}.json"))
    root = [r for r in g["rows"] if r["name"] == "freeze.skills_root"]
    sets[name] = {"exit": 0 if g["ok"] else 1, "rows_total": g["rows_total"], "rows_ok": g["rows_ok"],
                  "rows_not_ok": g["rows_not_ok"], "not_run": g["not_run"], "row_names": [r["name"] for r in g["rows"]],
                  "skills_root_measured": (root[0]["observed"] if root else None)}
x43 = [x for x in steps if x["step"] == "X4.3"]
expected_exit = {("X4.1", "diff"): 1}
bad = [x["cmd"][:80] for x in steps if x["exit"] != (1 if x["step"] == "X4.1" and x["cmd"].startswith("diff ") else 0)]
out = {"what": "the committed manifest's execute commands, run literally in spec §9 order on a fresh copy of the repository (scratch), 2026-09-24, after repair round 5 (the guarded rm forms, P-92; X4.3's digest comparison by diff)",
       "order": "X0.3(b), X1.1, X1.2, X1.3 pre, X2.1 (texts X2.2), X3.1 registry.diff, X3.2 execute.2, X3.3 execute.3, X3.4 (texts X3.5), X4.1 execute.4, X4.2 pkg, X4.3 execute.4b (package, extract, compare), X7.4 post with $PKG standing in for the installed root",
       "all_exit_as_expected": not bad, "unexpected_exits": bad,
       "note": "X4.1's plain diff of the 4.1.0 and 4.1.1 contracts exits 1 by design (two changed lines, manifest execute.4 expected). The whole skills root is measured and compared within each run (P-79). Each step keeps up to 400 lines of its output (the first and last 200); two steps, X4.2 and X7.4 post, were cut (1007 and 818 lines); paths are shown as $SCRATCH and $REPO",
       "x43": {"skill_is_valid_count": sum(l.count("Skill is valid!") for x in x43 for l in x["output"]),
               "freeze_compare_diff_exit": [x["exit"] for x in x43 if "expected_after_patch.txt" in x["cmd"]],
               "archives": [l.split()[0] + " " + l.split("/")[-1] for x in x43 if x["cmd"].startswith("sha256sum") for l in x["output"]]},
       "sets": sets, "steps": steps}
json.dump(out, open(EVR + "/gate_proof_x.json", "w"), indent=1, ensure_ascii=False)
open(EVR + "/gate_proof_x.json", "a").write("\n")
print(out["all_exit_as_expected"], out["unexpected_exits"], out["x43"]["skill_is_valid_count"], out["x43"]["freeze_compare_diff_exit"], {k: (v["rows_ok"], v["rows_total"], v["skills_root_measured"]) for k, v in sets.items()})
