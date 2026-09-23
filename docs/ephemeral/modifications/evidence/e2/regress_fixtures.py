"""§8b.10 fixture-document regressions R-FX-1 and R-FX-2, run through the edited runner with a mutated
scenarios file under TMPDIR. Pass = exactly the stated failing cases.
usage: PYTHONDONTWRITEBYTECODE=1 python3 regress_fixtures.py <edited-skills-root>"""
import json, os, subprocess, sys
from pathlib import Path
sys.dont_write_bytecode = True
K = Path(sys.argv[1]); TMP = Path("/tmp/claude-0/e2/tmp")
FVD = K / "flowmaster-validate"
S = FVD / "fixtures/gcfpe-20260914.1-091426.1/scenarios.json"
ENV = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1", "TMPDIR": str(TMP)}
base = S.read_text(encoding="utf-8")


def run_with(mut):
    d = json.loads(base); mut(d)
    p = TMP / "scen_regress.json"; p.write_text(json.dumps(d), encoding="utf-8")
    r = subprocess.run([sys.executable, str(FVD / "scripts/run_gcfpe_20260914_fixtures.py"), str(K / "change-flow"),
                        "--contract", str(K / "change-flow/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json"),
                        "--fixture", str(p)], capture_output=True, text=True, env=ENV)
    out = json.loads(r.stdout); p.unlink()
    failing = sorted(c["name"] for c in out["cases"] if not c["passed"])
    doc = [c.get("errors") for c in out["cases"] if c["name"] == "section-13-fixture-document"]
    return failing, doc


def v(d, name):
    row = next(r for r in d["scenarios"] if r["id"] == "REPLAN-NEG-01")
    return next(x for x in row["variants"] if x["name"] == name)


clean, cdoc = run_with(lambda d: None)
print("clean failing:", clean, cdoc)
# The --fixture path is not the pinned file, so the profile's fixture hash case may differ; subtract clean.
res = []
f1, d1 = run_with(lambda d: v(d, "reject-routed-to-pr30").__setitem__("expected_rule", "PR40_REJECT_REPLAN_PROCEED"))
e1 = sorted(set(f1) - set(clean))
ok1 = e1 == ["REPLAN-NEG-01::reject-routed-to-pr30::single-defect", "section-13-fixture-document"] and any("FIXTURE_REPLAN_VARIANT_RULES" in (x or []) for x in d1)
print(("OK   " if ok1 else "BAD  ") + "R-FX-1", e1, d1)
f2, d2 = run_with(lambda d: v(d, "reject-routed-to-pr30")["input"].__setitem__("second_proceed_same_plan", True))
e2 = sorted(set(f2) - set(clean))
ok2 = e2 == ["REPLAN-NEG-01::reject-routed-to-pr30::single-defect"]
print(("OK   " if ok2 else "BAD  ") + "R-FX-2", e2)
print(f"FIXTURE_REGRESSIONS {ok1 + ok2} of 2 exact")
