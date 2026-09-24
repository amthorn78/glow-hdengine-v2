"""PLAN test of the committed fill_brief.py across its eight variants (repair round 8, P-112 (f)). Each case copies the
scratch fixture (a git repository holding EX/packages.json with the seven expected freeze lines), adds the briefs,
verdict files and run.json the case names, runs fill_brief.py and prints the outcome only (no brief text).

  brief_cases_r8.py <scratchpad> <repository root>
"""
import json, shutil, subprocess, sys
from pathlib import Path
S = Path(sys.argv[1]); REPO = Path(sys.argv[2])
FIX = S / "plan/r8/brief"
D = "docs/ephemeral/modifications/evidence/closeout-residuals"
FB = REPO / D / "plan/skills/fill_brief.py"
DRAFT = REPO / D / "plan/skills/REVIEWER-PROMPT-cr.draft.md"
EXP = REPO / D / "plan/skills/expected_after_patch.txt"
PRIOR = FIX / "prior.md"
CONF = "Verdict: SKILL_FIT_CONFIRMED\n"
REJ = "Verdict: SKILL_REPAIR_REQUIRED\n"
QUOTE = "One verdict, using exactly this vocabulary: SKILL_FIT_CONFIRMED or SKILL_REPAIR_REQUIRED.\n\nVerdict: SKILL_FIT_CONFIRMED\n"

def case(name, briefs=(), verdicts=(), run=None, prior=False):
    w = S / "plan/r8/briefcases" / name
    if w.exists():
        shutil.rmtree(w)
    shutil.copytree(FIX, w, ignore=shutil.ignore_patterns("attempt-1"))
    base = w / D
    for p in base.glob("attempt-*"):
        shutil.rmtree(p)
    for p in base.glob("REVIEWER-PROMPT-cr*.md"):
        p.unlink()
    shutil.copy(FB, base / "plan/skills/fill_brief.py")
    shutil.copy(DRAFT, base / "plan/skills/REVIEWER-PROMPT-cr.draft.md")
    shutil.copy(EXP, base / "plan/skills/expected_after_patch.txt")
    for b in briefs:
        (base / b).parent.mkdir(parents=True, exist_ok=True)
        (base / b).write_text("brief\n", encoding="utf-8")
    for v, t in verdicts:
        (base / v).write_text(t, encoding="utf-8")
    (base / "execute/run.json").write_text(json.dumps(run or {}) + "\n", encoding="utf-8")
    subprocess.run(["git", "add", "-A"], cwd=w, capture_output=True)
    subprocess.run(["git", "-c", "user.email=t@t", "-c", "user.name=t", "commit", "-qm", "case"], cwd=w, capture_output=True)
    cmd = [sys.executable, f"{D}/plan/skills/fill_brief.py", f"{D}/execute/packages.json"]
    if prior:
        cmd += ["--prior-file", str(PRIOR)]
    r = subprocess.run(cmd, cwd=w, capture_output=True, text=True, env={"PYTHONDONTWRITEBYTECODE": "1", "PATH": "/usr/bin:/bin"})
    out = r.stdout
    res = {"exit": r.returncode}
    if r.returncode:
        res["refused"] = json.loads(r.stderr.strip().splitlines()[-1])["refused"]
    else:
        import re
        res["round"] = re.search(r"# Reviewer prompt, round (cr\d+)", out).group(1)
        res["tokens_left"] = "{{" in out
        res["prior_text"] = "PLAN-CHANGE prior text" in out
        res["recut_text"] = "not delivered" in out
        res["first_text"] = "NONE, first review." in out
    shutil.rmtree(w)
    return res

v1 = [("SECTION-10-REVIEW-cr1-SFR-CR1-1.md", CONF), ("SECTION-10-REVIEW-cr1-SFR-CR1-2.md", CONF)]
rows = {
 "first": case("first"),
 "recut": case("recut", ["REVIEWER-PROMPT-cr1.md"], v1),
 "recut_after_rejection": case("rej", ["REVIEWER-PROMPT-cr1.md"], [v1[0], ("SECTION-10-REVIEW-cr1-SFR-CR1-2.md", REJ)]),
 "recut_after_a_confirmed_record_quoting_both_words": case("quote", ["REVIEWER-PROMPT-cr1.md"], [v1[0], ("SECTION-10-REVIEW-cr1-SFR-CR1-2.md", QUOTE)]),
 "recut_after_delivery": case("deliv", ["REVIEWER-PROMPT-cr1.md"], v1, {"delivered_cr1": "2026-09-24T00:00:00Z"}),
 "plan_change_without_prior_file": case("pcno", ["attempt-1/REVIEWER-PROMPT-cr1.md"]),
 "plan_change_with_prior_file": case("pcyes", ["attempt-1/REVIEWER-PROMPT-cr1.md"], prior=True),
 "after_x71_plan_change_top_level_brief_delivered": case("x71", ["REVIEWER-PROMPT-cr1.md"], v1, {"delivered_cr1": "2026-09-24T00:00:00Z"}, prior=True),
}
want = {
 "first": lambda r: r["exit"] == 0 and r["round"] == "cr1" and r["first_text"] and not r["tokens_left"],
 "recut": lambda r: r["exit"] == 0 and r["round"] == "cr2" and r["recut_text"] and not r["prior_text"] and not r["tokens_left"],
 "recut_after_rejection": lambda r: r.get("refused") == "REPAIR_VERDICT_PENDING",
 "recut_after_a_confirmed_record_quoting_both_words": lambda r: r.get("refused") == "REPAIR_VERDICT_PENDING",
 "recut_after_delivery": lambda r: r.get("refused") == "PRIOR_ROUND_DELIVERED",
 "plan_change_without_prior_file": lambda r: r.get("refused") == "PLAN_CHANGE_ROUND_NEEDS_PRIOR_FILE",
 "plan_change_with_prior_file": lambda r: r["exit"] == 0 and r["round"] == "cr2" and r["prior_text"] and not r["recut_text"],
 "after_x71_plan_change_top_level_brief_delivered": lambda r: r["exit"] == 0 and r["round"] == "cr2" and r["prior_text"] and not r["recut_text"],
}
for k, r in rows.items():
    r["ok"] = bool(want[k](r))
print(json.dumps({"all_ok": all(r["ok"] for r in rows.values()), "cases": rows}, indent=1))
