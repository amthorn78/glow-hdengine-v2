#!/usr/bin/env python3
"""PLAN proof of nam002_live.py's command line (P-63) on the synthetic child list; no Notion call, no prompt body.

Runs the four EXECUTE runs (committed-registry stand-in = registry.new.md; control = reg-old.md, from
`git show HEAD:docs/prompt_ecosystem_management/project-prompt-contract-registry.md`, sha256 8b4e46ed...) with three audit
roots (the byte-identical wga_scripts copy, the installed audit, the r1 final audit copy), plus the unusable-input cases.
Each exit code is the script's own return code (subprocess.run, no pipe). Writes cli_matrix.json next to this file.
"""
import glob, hashlib, json, os, subprocess, sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
REG = os.path.dirname(HERE)
SCR = os.path.dirname(os.path.dirname(REG))
N = os.path.join(REG, "nam002_live.py")
NEW = os.path.join(REG, "registry.new.md")
OLD = os.path.join(HERE, "reg-old.md")
CL = os.path.join(HERE, "childlist.synthetic.json")
ESC_HUB, CF_HUB = "3db4590a05eb81cd938de84cfffead9c", "3db4590a05eb81d59059eb6b95ed5fcf"
ROOTS = {"wga_scripts copy (default)": None,
         "installed": sorted(glob.glob("/root/.claude/skills/synced/*/amthor-workspace-governance-audit"))[0],
         "r1 final": os.path.join(SCR, "r1/skills/final/amthor-workspace-governance-audit")}
RUNS = [("1 committed (new)", NEW, []), ("2 inject parent ESC-10", NEW, ["--inject", f"ESC-10={CF_HUB}"]),
        ("3 inject title Escalation hub", NEW, ["--inject-title", f"{ESC_HUB}=Escalation"]), ("4 control (old)", OLD, [])]
EXPECT = {"1 committed (new)": 0, "2 inject parent ESC-10": 0, "3 inject title Escalation hub": 0, "4 control (old)": 1}
env = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1"}


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def call(args):
    r = subprocess.run([sys.executable, N] + args, capture_output=True, text=True, env=env)
    try:
        out = json.loads(r.stdout)
    except Exception:  # noqa: BLE001
        out = None
    return r.returncode, out, r.stderr.strip()[-200:]


res = {"inputs": {"nam002_live.py": sha(N), "registry.new.md": sha(NEW), "reg-old.md": sha(OLD),
                  "childlist.synthetic.json": sha(CL)}, "runs": {}, "unusable_input": {}}
ok = res["inputs"]["reg-old.md"] == "8b4e46ed2dc24442e3dadc416dfe4c810a048788bf03c799808927a54c2677d4"
for rname, root in ROOTS.items():
    for name, reg, extra in RUNS:
        args = [reg, CL] + (["--audit-root", root] if root else []) + extra
        code, out, err = call(args)
        s = out["summary"] if out else {}
        res["runs"][f"{rname} | {name}"] = {
            "exit": code, "expectation_met": out.get("expectation_met") if out else None,
            "NAM-002": s.get("NAM-002"), "NAM-002_rows": s.get("NAM-002_rows") if s.get("NAM-002") == 1 else None,
            "lane_parent_findings": s.get("lane_parent_findings"), "title_findings": s.get("title_findings"),
            "title_hubs": s.get("title_hubs"), "title_references": s.get("title_references"),
            "unplaced_rows": s.get("unplaced_rows"), "other_errors": s.get("other_errors"), "stderr": err}
        ok &= code == EXPECT[name]
bad = os.path.join(HERE, "childlist.notitle.tmp.json")
d = json.load(open(CL, encoding="utf-8"))
del d["hubs"][0]["title"]
json.dump(d, open(bad, "w", encoding="utf-8"))
for name, args in (("inject-title on a non-hub id", [NEW, CL, "--inject-title", "0123456789abcdef0123456789abcdef=X"]),
                   ("inject-title equal to the fetched title", [NEW, CL, "--inject-title", f"{ESC_HUB}=Escalation — GCFPE-20260914.1 — 091426.1"]),
                   ("--inject with --inject-title", [NEW, CL, "--inject", f"ESC-10={CF_HUB}", "--inject-title", f"{ESC_HUB}=Escalation"]),
                   ("a hub without its title", [NEW, bad]),
                   ("missing child-list file", [NEW, os.path.join(HERE, "missing.json")])):
    code, out, err = call(args)
    res["unusable_input"][name] = {"exit": code, "error": (out or {}).get("error") or err}
    ok &= code == 2
os.remove(bad)
res["ALL_OK"] = bool(ok)
json.dump(res, open(os.path.join(HERE, "cli_matrix.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print(json.dumps({k: (v["exit"], v["NAM-002"], v["lane_parent_findings"], v["title_findings"],
                      (v["title_references"] or {}).get("mismatched")) for k, v in res["runs"].items()}, indent=1, ensure_ascii=False))
print(json.dumps({k: v["exit"] for k, v in res["unusable_input"].items()}, ensure_ascii=False), "ALL_OK", res["ALL_OK"])
sys.exit(0 if ok else 1)
